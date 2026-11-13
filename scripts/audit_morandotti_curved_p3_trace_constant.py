#!/usr/bin/env python3
"""Direct finite-mesh T134 trace-constant audit on generated curved P3 meshes.

For each mesh this computes the largest generalized eigenvalue
  C_tr,h = sup_{v_h in V_h^0} H_{h,l}(v_h)^2 / D_h(v_h)^2
from the assembled physical-coordinate FEM matrices. It also records sampled
scaled geometry-Jacobian diagnostics. Finite samples do not prove a
mesh-uniform bound or all-points Jacobian positivity.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from mpi4py import MPI
from petsc4py import PETSc
import ufl
from dolfinx import fem
from dolfinx.fem.petsc import assemble_matrix
from scipy.sparse import csr_matrix

from models.morandotti_trace_constant import largest_generalized_eigenvalue
from scripts.rgs_morandotti_two_core_c0_ipdg import make_mesh


def _petsc_to_scipy(matrix, size):
    indptr, indices, data = matrix.getValuesCSR()
    return csr_matrix((data, indices, indptr), shape=(size, size))


def _assemble_pair(form_d, form_h, V, mesh, quadrature_degree):
    D = assemble_matrix(fem.form(form_d))
    H = assemble_matrix(fem.form(form_h))
    D.assemble()
    H.assemble()

    tdim = mesh.topology.dim
    mesh.topology.create_connectivity(tdim - 1, tdim)
    from dolfinx.mesh import exterior_facet_indices
    boundary_facets = exterior_facet_indices(mesh.topology)
    boundary_dofs = fem.locate_dofs_topological(V, tdim - 1, boundary_facets)

    # The elementwise Hessian seminorm has the entire continuous P1 space
    # in its kernel: every globally continuous piecewise-affine function has
    # D^2 v = 0 inside each cell. The facet Hessian form vanishes on the same
    # kernel. A generalized EVP on the full C0-P3 space therefore has a
    # singular denominator and an undefined 0/0 quotient on these modes.
    # Choose the canonical quotient representative with all vertex values
    # set to zero: subtracting the global P1 nodal interpolant gives exactly
    # one such representative in every equivalence class modulo C0-P1.
    # This removes only the common affine kernel; edge and cell P3 modes stay.
    mesh.topology.create_entities(0)
    # locate_dofs_topological needs the vertex-to-cell adjacency explicitly.
    mesh.topology.create_connectivity(0, tdim)
    vertex_count = mesh.topology.index_map(0).size_local
    vertices = np.arange(vertex_count, dtype=np.int32)
    vertex_dofs = fem.locate_dofs_topological(V, 0, vertices)

    n = V.dofmap.index_map.size_local
    constrained = np.union1d(boundary_dofs, vertex_dofs)
    free = np.setdiff1d(np.arange(n, dtype=np.int32), constrained)
    if free.size < 3:
        raise RuntimeError(
            "too few quotient P3 degrees of freedom after homogeneous boundary "
            f"and continuous-P1-kernel constraints: {free.size}"
        )
    Dsp = _petsc_to_scipy(D, n)[free][:, free]
    Hsp = _petsc_to_scipy(H, n)[free][:, free]
    D.destroy()
    H.destroy()
    value, spectral = largest_generalized_eigenvalue(
        Hsp, Dsp, return_diagnostics=True
    )
    return value, spectral, int(free.size)


def _bernstein_indices(degree):
    return [(degree-i-j, i, j)
            for i in range(degree+1) for j in range(degree+1-i)]


def _bernstein_matrix(degree):
    from math import factorial
    indices = _bernstein_indices(degree)
    points = np.asarray([(j/degree, k/degree) if degree else (0.0, 0.0)
                         for i, j, k in indices], dtype=float)
    matrix = np.empty((len(indices), len(indices)), dtype=float)
    for row, (x, y) in enumerate(points):
        lam = (1.0-x-y, x, y)
        for col, (a, b, d) in enumerate(indices):
            multinomial = factorial(degree) / (
                factorial(a)*factorial(b)*factorial(d))
            matrix[row, col] = multinomial * lam[0]**a * lam[1]**b * lam[2]**d
    return indices, points, matrix


def _bernstein_coefficients(samples, degree):
    indices, points, matrix = _bernstein_matrix(degree)
    values = np.asarray(samples)
    if values.shape[1] != len(points):
        raise ValueError("sample count does not match triangular Bernstein degree")
    coeff = np.linalg.solve(matrix, values.reshape(values.shape[0], values.shape[1], -1))
    return coeff.reshape((values.shape[0], len(indices)) + values.shape[2:])


def _evaluate_bernstein(coeff, degree, point):
    from math import factorial
    x, y = point
    lam = (1.0-x-y, x, y)
    value = np.zeros(coeff.shape[1:], dtype=float)
    for q, (a, b, d) in enumerate(_bernstein_indices(degree)):
        multinomial = factorial(degree) / (
            factorial(a)*factorial(b)*factorial(d))
        value += coeff[q] * multinomial * lam[0]**a * lam[1]**b * lam[2]**d
    return value


def _certify_positive_bernstein(coeff, degree, *, max_depth=8):
    """Subdivide a triangular Bernstein polynomial until every coefficient is positive.

    The guard accounts conservatively for floating-point interpolation/evaluation
    error. This is a guarded floating-point certificate, not interval arithmetic.
    """
    eps = np.finfo(float).eps
    scale = max(1.0, float(np.max(np.abs(coeff))))
    _, _, basis = _bernstein_matrix(degree)
    guard = 512.0 * eps * max(1.0, float(np.linalg.cond(basis))) * scale
    vertices = np.asarray([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    leaves = []

    def visit(local_coeff, tri, depth):
        lower = float(np.min(local_coeff))
        upper = float(np.max(local_coeff))
        if lower > guard:
            leaves.append((lower, upper, depth))
            return True
        if depth >= max_depth:
            return False
        v0, v1, v2 = tri
        m01, m12, m20 = 0.5*(v0+v1), 0.5*(v1+v2), 0.5*(v2+v0)
        children = (
            np.asarray([v0, m01, m20]),
            np.asarray([m01, v1, m12]),
            np.asarray([m20, m12, v2]),
            np.asarray([m01, m12, m20]),
        )
        indices, local_points, matrix = _bernstein_matrix(degree)
        for child in children:
            global_points = np.asarray([
                (1.0-p[0]-p[1])*child[0] + p[0]*child[1] + p[1]*child[2]
                for p in local_points
            ])
            samples = np.asarray([
                _evaluate_bernstein(coeff, degree, p) for p in global_points
            ])
            child_coeff = np.linalg.solve(matrix, samples)
            if not visit(child_coeff, child, depth+1):
                return False
        return True

    success = visit(np.asarray(coeff), vertices, 0)
    return {
        "positive_on_reference_triangle": bool(success),
        "certified_lower_bound": float(min(q[0] for q in leaves)) if success else None,
        "bernstein_upper_bound": float(max(q[1] for q in leaves)) if success else None,
        "subdivision_depth_max": int(max((q[2] for q in leaves), default=0)),
        "floating_point_guard": float(guard),
        "method": "triangular Bernstein coefficients with recursive four-way subdivision",
        "formal_interval_arithmetic": False,
    }


def certify_curved_p3_geometry(mesh):
    """Bound scaled map derivatives and certify det(J/h^2)>0 cellwise."""
    tdim = mesh.topology.dim
    nc = mesh.topology.index_map(tdim).size_local
    cells = np.arange(nc, dtype=np.int32)
    h = np.asarray(mesh.h(tdim, cells), dtype=float)
    if np.any(~np.isfinite(h)) or np.any(h <= 0.0):
        raise RuntimeError("invalid cell diameter in geometry certificate")

    # For a cubic triangular map, J is degree 2, det(J) degree at most 4,
    # and the second map derivative is degree 1.
    _, points2, _ = _bernstein_matrix(2)
    _, points4, _ = _bernstein_matrix(4)
    _, points1, _ = _bernstein_matrix(1)
    J_expr = fem.Expression(ufl.Jacobian(mesh), points2, comm=mesh.comm)
    H_expr = fem.Expression(ufl.grad(ufl.Jacobian(mesh)), points1, comm=mesh.comm)
    J2 = J_expr.eval(mesh, cells)
    H1 = H_expr.eval(mesh, cells)

    J_scaled = J2 / h[:, None, None, None]
    J_coeff = _bernstein_coefficients(J_scaled, 2)
    H_scaled = H1 / h[:, None, None, None, None]
    H_coeff = _bernstein_coefficients(H_scaled, 1)
    component_bounds_J = np.max(np.abs(J_coeff), axis=1)
    component_bounds_H = np.max(np.abs(H_coeff), axis=1)
    M1_cells = np.sqrt(np.sum(component_bounds_J**2, axis=(1, 2)))
    M2_cells = np.sqrt(np.sum(component_bounds_H**2, axis=(1, 2, 3)))

    J4_expr = fem.Expression(ufl.Jacobian(mesh), points4, comm=mesh.comm)
    J4 = J4_expr.eval(mesh, cells) / h[:, None, None, None]
    det_samples = np.linalg.det(J4)
    det_coeff = _bernstein_coefficients(det_samples, 4)

    rows = []
    for cell in range(nc):
        cert = _certify_positive_bernstein(det_coeff[cell], 4)
        j0 = cert["certified_lower_bound"]
        if j0 is not None:
            # For a 2x2 matrix, ||J^{-1}||_F = ||J||_F / |det J|.
            mminus1 = float(M1_cells[cell] / j0)
        else:
            mminus1 = None
        rows.append({
            "cell": int(cell),
            "determinant_certificate": cert,
            "M1_upper_bound": float(M1_cells[cell]),
            "M2_upper_bound": float(M2_cells[cell]),
            "M_minus1_upper_bound": mminus1,
        })
    certified = all(q["determinant_certificate"]["positive_on_reference_triangle"]
                    for q in rows)
    return {
        "method": "cubic-map polynomial bounds via triangular Bernstein convex-hull property",
        "cells": int(nc),
        "all_cell_jacobians_certified_positive": bool(certified),
        "global_M1_upper_bound": float(np.max(M1_cells)),
        "global_M2_upper_bound": float(np.max(M2_cells)),
        "global_M_minus1_upper_bound": (
            float(max(q["M_minus1_upper_bound"] for q in rows)) if certified else None
        ),
        "global_j0_lower_bound": (
            float(min(q["determinant_certificate"]["certified_lower_bound"]
                      for q in rows)) if certified else None
        ),
        "global_j1_upper_bound": (
            float(max(q["determinant_certificate"]["bernstein_upper_bound"]
                      for q in rows)) if certified else None
        ),
        "floating_point_not_interval_certification": True,
        "cell_certificates": rows,
    }


def trace_constant_for_mesh(mesh, quadrature_degrees=(24, 32, 40)):
    """Assemble T134's H and D quadratic forms and solve their generalized EVP."""
    mesh.topology.create_connectivity(mesh.topology.dim - 1, mesh.topology.dim)
    V = fem.functionspace(mesh, ("Lagrange", 3))
    hspace = fem.functionspace(mesh, ("DG", 0))
    cell_h = fem.Function(hspace)
    nc = mesh.topology.index_map(mesh.topology.dim).size_local
    cells = np.arange(nc, dtype=np.int32)
    cell_h.x.array[:] = mesh.h(mesh.topology.dim, cells)
    cell_h.x.scatter_forward()

    u = ufl.TrialFunction(V)
    v = ufl.TestFunction(V)
    Hu = ufl.grad(ufl.grad(u))
    Hv = ufl.grad(ufl.grad(v))
    n = ufl.FacetNormal(mesh)

    q_u_plus = ufl.dot(ufl.dot(Hu("+"), n("+")), n("+"))
    q_u_minus = ufl.dot(ufl.dot(Hu("-"), n("-")), n("-"))
    q_v_plus = ufl.dot(ufl.dot(Hv("+"), n("+")), n("+"))
    q_v_minus = ufl.dot(ufl.dot(Hv("-"), n("-")), n("-"))
    q_u_int = 0.5 * (q_u_plus + q_u_minus)
    q_v_int = 0.5 * (q_v_plus + q_v_minus)
    q_u_bnd = ufl.dot(ufl.dot(Hu, n), n)
    q_v_bnd = ufl.dot(ufl.dot(Hv, n), n)

    estimates = []
    free_dofs = None
    for degree in quadrature_degrees:
        dx = ufl.Measure("dx", domain=mesh, metadata={"quadrature_degree": int(degree)})
        dS = ufl.Measure("dS", domain=mesh, metadata={"quadrature_degree": int(degree)})
        ds = ufl.Measure("ds", domain=mesh, metadata={"quadrature_degree": int(degree)})
        D_form = ufl.inner(Hu, Hv) * dx
        H_form = (ufl.avg(cell_h) * q_u_int * q_v_int * dS
                  + cell_h * q_u_bnd * q_v_bnd * ds)
        value, spectral, count = _assemble_pair(D_form, H_form, V, mesh, int(degree))
        estimates.append({
            "quadrature_degree": int(degree),
            "C_tr_h": value,
            "spectral_diagnostics": spectral,
        })
        free_dofs = count

    # Sample the actual cubic geometry map on a triangular reference grid.
    from dolfinx import fem as _fem
    points = np.asarray([
        (i / 16.0, j / 16.0)
        for i in range(17) for j in range(17 - i)
    ], dtype=np.float64)
    jac_expr = _fem.Expression(ufl.Jacobian(mesh), points, comm=mesh.comm)
    local_cells = np.arange(nc, dtype=np.int32)
    jac = jac_expr.eval(mesh, local_cells)
    det_j = np.linalg.det(jac)
    singular = np.linalg.svd(jac, compute_uv=False)
    h_cells = mesh.h(mesh.topology.dim, local_cells)
    scaled_min = singular[..., -1] / h_cells[:, None]
    scaled_max = singular[..., 0] / h_cells[:, None]
    geometry = {
        "sampled_reference_points_per_cell": int(points.shape[0]),
        "sampling_subdivisions_per_reference_edge": 16,
        "minimum_sampled_det_J": float(np.min(det_j)),
        "minimum_sigma_min_over_cell_diameter": float(np.min(scaled_min)),
        "maximum_sigma_max_over_cell_diameter": float(np.max(scaled_max)),
        "maximum_sampled_map_condition_number": float(np.max(singular[..., 0] / singular[..., -1])),
        "all_sampled_determinants_positive": bool(np.all(det_j > 0.0)),
    }
    geometry_certificate = certify_curved_p3_geometry(mesh)
    if not geometry_certificate["all_cell_jacobians_certified_positive"]:
        raise RuntimeError(
            "Bernstein subdivision could not certify positive Jacobians on every cell"
        )

    return {
        "cells": int(nc),
        "free_dofs_after_zero_value_boundary_conditions": free_dofs,
        "geometry_certificate": geometry_certificate,
        "quadrature_estimates": estimates,
        "quadrature_relative_difference_last_two": float(
            abs(estimates[-1]["C_tr_h"] - estimates[-2]["C_tr_h"])
            / max(abs(estimates[-1]["C_tr_h"]), 1e-300)
        ),
        "quadrature_stable_last_two": bool(
            abs(estimates[-1]["C_tr_h"] - estimates[-2]["C_tr_h"])
            / max(abs(estimates[-1]["C_tr_h"]), 1e-300) <= 5e-3
        ),
        "geometry_map_diagnostics": geometry,
    }



def _information_criteria(y, fitted, mean_parameter_count):
    """Gaussian information criteria, counting the estimated residual variance."""
    n = len(y)
    rss = max(float(np.sum((y - fitted) ** 2)), 1e-300)
    k = int(mean_parameter_count) + 1  # include sigma^2 in the Gaussian likelihood
    base = n * np.log(rss / n)
    aic = base + 2 * k
    bic = base + k * np.log(n)
    hqic = base + 2 * k * np.log(np.log(n)) if n > 1 else float("inf")
    aicc = aic + (2 * k * (k + 1) / (n - k - 1)) if n > k + 1 else float("inf")
    return {
        "AIC": float(aic), "AICc": float(aicc), "BIC": float(bic),
        "HQIC": float(hqic), "RSS": rss, "n": n,
        "mean_parameters": int(mean_parameter_count),
        "variance_parameter_included": True, "k_total": k,
    }


def statistical_model_audit(runs, distances, mesh_sizes, bootstrap_replicates=2000):
    """Exploratory model comparison with seed-block resampling and validation.

    The same mesh seed is followed across all h-levels. Bootstrap and
    leave-one-seed-out validation therefore operate on whole seed blocks,
    preserving cross-resolution dependence induced by reusing seed labels.
    """
    from scipy.optimize import curve_fit
    rng = np.random.default_rng(20261113)
    output = {}
    model_specs = {
        "constant": (lambda x, c: np.full_like(x, c, dtype=float),
                     lambda y: [float(np.mean(y))], (-np.inf, np.inf)),
        "power_law": (lambda x, a, p: a * np.power(x, p),
                      lambda y: [max(float(np.mean(y)), 1e-8), 0.5],
                      ([0.0, -4.0], [np.inf, 4.0])),
        "finite_limit_power_law": (lambda x, c, a, p: c + a * np.power(x, p),
                      lambda y: [max(0.0, float(np.min(y))*0.8), 1.0, 0.5],
                      ([-np.inf, -np.inf, -4.0], [np.inf, np.inf, 4.0])),
    }

    def fit_model(name, x, y):
        fn, p0_fn, bounds = model_specs[name]
        pars, _ = curve_fit(fn, x, y, p0=p0_fn(y), bounds=bounds, maxfev=50000)
        return pars, fn(x, *pars), fn

    for distance in distances:
        rows = [r for r in runs if r["distance"] == float(distance)]
        seeds = sorted({int(r["mesh_seed"]) for r in rows})
        levels = [float(v) for v in mesh_sizes]
        # Rectangular seed x h matrix: reject missing or duplicated seed-level cells.
        matrix = np.empty((len(seeds), len(levels)), dtype=float)
        for i, seed in enumerate(seeds):
            for j, level in enumerate(levels):
                vals = [r["quadrature_estimates"][-1]["C_tr_h"] for r in rows
                        if int(r["mesh_seed"]) == seed and r["h_target"] == level]
                if len(vals) != 1:
                    raise RuntimeError(
                        f"expected one C_tr,h for distance={distance}, seed={seed}, h={level}; got {len(vals)}"
                    )
                matrix[i, j] = float(vals[0])
        h = np.tile(np.asarray(levels, dtype=float), len(seeds))
        y = matrix.reshape(-1)
        candidates = {}
        for name in model_specs:
            try:
                pars, fitted, _ = fit_model(name, h, y)
                candidates[name] = {
                    "parameters": [float(v) for v in pars],
                    **_information_criteria(y, fitted, len(pars)),
                }
            except Exception as exc:
                candidates[name] = {"fit_error": str(exc)}

        valid = {k: v for k, v in candidates.items() if "AICc" in v and np.isfinite(v["AICc"])}
        if valid:
            best = min(valid, key=lambda k: valid[k]["AICc"])
            min_aicc = valid[best]["AICc"]
            for item in valid.values():
                item["delta_AICc"] = float(item["AICc"] - min_aicc)
        else:
            best = None

        # Leave-one-independent-seed-out CV: all resolutions of a seed stay together.
        cv = {}
        for name in model_specs:
            errors = []
            fold_failures = []
            for held in range(len(seeds)):
                train_mask = np.repeat(np.arange(len(seeds)) != held, len(levels))
                test_mask = ~train_mask
                try:
                    pars, _, fn = fit_model(name, h[train_mask], y[train_mask])
                    prediction = fn(h[test_mask], *pars)
                    errors.extend((y[test_mask] - prediction).tolist())
                except Exception as exc:
                    fold_failures.append(f"seed={seeds[held]}: {exc}")
            cv[name] = {
                "method": "leave-one-mesh-seed-out cross-validation; complete seed block held out",
                "folds_requested": len(seeds),
                "folds_successful": len(seeds) - len(fold_failures),
                "PRESS": float(np.sum(np.square(errors))) if errors else None,
                "RMSE": float(np.sqrt(np.mean(np.square(errors)))) if errors else None,
                "fold_failures": fold_failures,
            }

        # Cluster jackknife for the asymptotic-limit parameter C_infinity.
        jackknife_values = []
        jackknife_failures = []
        for held in range(len(seeds)):
            keep = np.repeat(np.arange(len(seeds)) != held, len(levels))
            try:
                pars, _, _ = fit_model("finite_limit_power_law", h[keep], y[keep])
                jackknife_values.append(float(pars[0]))
            except Exception as exc:
                jackknife_failures.append(f"seed={seeds[held]}: {exc}")
        jackknife = {"method": "delete-one-seed-block jackknife on C_infinity",
                     "successful_fits": len(jackknife_values),
                     "failed_fits": jackknife_failures}
        if len(jackknife_values) == len(seeds) and len(seeds) >= 2:
            jk = np.asarray(jackknife_values)
            jk_mean = float(np.mean(jk))
            full_c = candidates.get("finite_limit_power_law", {}).get("parameters", [None])[0]
            jackknife.update({
                "leave_one_seed_out_C_infinity": jackknife_values,
                "jackknife_mean": jk_mean,
                "bias_corrected_C_infinity": float(len(seeds) * full_c - (len(seeds)-1) * jk_mean),
                "standard_error": float(np.sqrt((len(seeds)-1)/len(seeds) * np.sum((jk-jk_mean)**2))),
            })

        # Paired cluster bootstrap: resample seed trajectories, not each h independently.
        limits = []
        for _ in range(int(bootstrap_replicates)):
            selected = rng.integers(0, len(seeds), size=len(seeds))
            boot_matrix = matrix[selected, :]
            hb = np.tile(np.asarray(levels, dtype=float), len(seeds))
            yb = boot_matrix.reshape(-1)
            try:
                pars, _, _ = fit_model("finite_limit_power_law", hb, yb)
                if np.isfinite(pars[0]):
                    limits.append(float(pars[0]))
            except Exception:
                pass
        output[f"d{float(distance):.4f}"] = {
            "observations": int(y.size),
            "independent_seed_blocks": len(seeds),
            "mesh_levels": levels,
            "models": candidates,
            "preferred_model_by_AICc": best,
            "cross_validation": cv,
            "jackknife": jackknife,
            "bootstrap": {
                "method": "paired nonparametric cluster bootstrap; resample complete seed trajectories across all h-levels",
                "requested_replicates": int(bootstrap_replicates),
                "successful_fits": len(limits),
                "C_infinity_percentile_95_interval": (
                    [float(v) for v in np.quantile(limits, [0.025, 0.975])] if limits else None
                ),
                "C_infinity_median": float(np.median(limits)) if limits else None,
                "warning": "Exploratory uncertainty conditional on the mesh generator and supplied seed blocks; not a mesh-uniform bound or proof."
            },
            "interpretation_warning": (
                "AIC/AICc/BIC/HQIC are conditional Gaussian-likelihood criteria; "
                "CV and resampling have only three independent seed blocks in the configured run. "
                "These diagnostics do not establish a uniform trace inequality."
            ),
        }
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mesh-sizes", nargs="+", type=float, default=[0.08, 0.045])
    parser.add_argument("--distances", nargs="+", type=float, default=[0.48, 0.56])
    parser.add_argument("--seeds", nargs="+", type=int, default=[11, 29, 47])
    parser.add_argument("--bootstrap-replicates", type=int, default=2000)
    parser.add_argument("--out", default="artifacts/morandotti_trace_constant/report.json")
    args = parser.parse_args()

    if MPI.COMM_WORLD.size != 1:
        raise RuntimeError("trace-constant audit is serial; distributed assembly is not audited")
    if not args.mesh_sizes or any(not np.isfinite(h) or h <= 0 for h in args.mesh_sizes):
        raise ValueError("mesh sizes must be finite and positive")
    if not args.distances or any(not np.isfinite(d) or d <= 0.24 or d >= 1.76 for d in args.distances):
        raise ValueError("two-core distances must satisfy 0.24 < d < 1.76")
    if len(set(args.seeds)) != len(args.seeds) or len(args.seeds) < 2:
        raise ValueError("at least two distinct mesh seeds are required")

    runs = []
    for distance in args.distances:
        centers = ((-0.5 * distance, 0.0), (0.5 * distance, 0.0))
        for h in args.mesh_sizes:
            for seed in args.seeds:
                mesh, _ = make_mesh(1.0, 0.12, centers, h, MPI.COMM_WORLD, random_seed=seed)
                result = trace_constant_for_mesh(mesh)
                row = {
                    "distance": float(distance),
                    "h_target": float(h),
                    "mesh_seed": int(seed),
                    **result,
                    "alpha_10_margin": float(10.0 - 2.0 * result["quadrature_estimates"][-1]["C_tr_h"]),
                    "alpha_10_exceeds_twice_C_tr_h": bool(
                        10.0 > 2.0 * result["quadrature_estimates"][-1]["C_tr_h"]
                    ),
                    "alpha_40_margin": float(40.0 - 2.0 * result["quadrature_estimates"][-1]["C_tr_h"]),
                    "alpha_40_exceeds_twice_C_tr_h": bool(
                        40.0 > 2.0 * result["quadrature_estimates"][-1]["C_tr_h"]
                    ),
                }
                if not row["geometry_map_diagnostics"]["all_sampled_determinants_positive"]:
                    raise RuntimeError(f"non-positive sampled cubic Jacobian for {row}")
                runs.append(row)
                print(json.dumps(row), flush=True)

    grouped = {}
    for distance in args.distances:
        for h in args.mesh_sizes:
            samples = [r for r in runs if r["distance"] == float(distance) and r["h_target"] == float(h)]
            values = [r["quadrature_estimates"][-1]["C_tr_h"] for r in samples]
            grouped[f"d{distance:.4f}_h{h:.4f}"] = {
                "realizations": len(samples),
                "seeds": sorted(r["mesh_seed"] for r in samples),
                "C_tr_h_max_over_seeds": float(max(values)),
                "C_tr_h_mean_over_seeds": float(np.mean(values)),
                "C_tr_h_sample_std_over_seeds": float(np.std(values, ddof=1)),
                "alpha_10_exceeds_twice_max_C_tr_h": bool(10.0 > 2.0 * max(values)),
                "alpha_40_margin_over_max_C_tr_h": float(40.0 - 2.0 * max(values)),
                "alpha_40_exceeds_twice_max_C_tr_h": bool(40.0 > 2.0 * max(values)),
            }

    statistical = statistical_model_audit(runs, args.distances, args.mesh_sizes, args.bootstrap_replicates)

    payload = {
        "title": "Morandotti curved-P3 finite-mesh T134 trace-constant audit",
        "status": "finite-mesh generalized-eigenvalue estimates; not a mesh-uniform proof",
        "provisional_penalty_diagnostic": "alpha=40 clears twice the largest C_tr,h in this finite sweep if all cases pass; this is a numerical tuning margin, not a mesh-uniform coercivity certificate",
        "quadrature_acceptance_threshold": 5e-3,
        "generalized_eigenpair_checks": "equilibrated denominator smallest/largest algebraic eigenvalue estimates and their residuals certify numerical positive definiteness; generalized eigenpair Rayleigh agreement and relative residual are also recorded at each quadrature degree",
        "quadrature_stability_is_diagnostic_not_a_claim_of_exactness": True,
        "definition": "C_tr,h = sup_{v_h in V_h^0} H_{h,l}(v_h)^2 / D_h(v_h)^2",
        "boundary_space": "globally continuous mapped P3 functions with zero value trace on outer and both core boundaries",
        "quadratic_forms": {
            "D": "integral_Omega D^2u:D^2v",
            "H": "sum_interior avg(h_K) integral_F avg(n^T D^2u n) avg(n^T D^2v n) + sum_boundary h_K integral_F (n^T D^2u n)(n^T D^2v n)",
        },
        "quadrature_degrees": [24, 32, 40],
        "mesh_sizes": args.mesh_sizes,
        "distances": args.distances,
        "seeds": args.seeds,
        "group_summary": grouped,
        "statistical_model_audit": statistical,
        "runs": runs,
        "limitations": [
            "a finite set of generalized eigenvalues does not prove sup_h C_tr,h is bounded",
            "positive Jacobians are checked only at sampled reference points, not certified at every point",
            "uniform mapped-element derivative and inverse-Jacobian bounds remain an analytic obligation",
            "the estimate uses the generated two-core P3 mesh family and the T134 facet weights; it is not a universal P3 constant",
            "quadrature stability is assessed from the last two estimates (degrees 32 and 40); instability is reported rather than aborting the sweep",
            "even a stable finite quadrature sequence is numerical evidence, not an exact integration certificate",
        ],
    }
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
