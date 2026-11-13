#!/usr/bin/env python3
"""Finite-mesh T134 trace audit plus exact-rational curved-P3 geometry certificates."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
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
from models.morandotti_exact_geometry import certify_p3_cell_geometry
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


def certify_curved_p3_geometry(mesh):
    """Certify every local cubic geometry map with exact rational arithmetic."""
    from fractions import Fraction
    import hashlib
    import math
    import basix

    tdim = mesh.topology.dim
    nc = mesh.topology.index_map(tdim).size_local
    cmap = mesh.geometry.cmaps[0]
    lagrange_variant = int(cmap.variant)
    if cmap.degree != 3 or cmap.dim != 10:
        raise RuntimeError(
            "exact geometry certificate requires a nodal equispaced triangular P3 "
            f"coordinate element; got degree={cmap.degree}, dim={cmap.dim}, "
            f"lagrange_variant={lagrange_variant}"
        )
    expected_variant = int(basix.LagrangeVariant.equispaced)
    if int(cmap.variant) != expected_variant:
        raise RuntimeError(
            "exact P3 reconstruction requires the equispaced Lagrange coordinate variant; "
            f"got variant={int(cmap.variant)}, expected={expected_variant}"
        )
    coordinate_element = basix.create_element(
        basix.ElementFamily.P, basix.CellType.triangle, 3,
        basix.LagrangeVariant.equispaced,
    )
    if not coordinate_element.interpolation_is_identity:
        raise RuntimeError("Basix equispaced P3 coordinate element is not nodal")
    points = np.asarray(coordinate_element.points, dtype=np.float64)
    geometry_dofmap = np.asarray(mesh.geometry.dofmaps[0], dtype=np.int32)
    if geometry_dofmap.shape != (nc, 10):
        raise RuntimeError(
            f"expected 10 geometry dofs per owned triangle, got {geometry_dofmap.shape}"
        )

    def as_fraction(pair):
        return Fraction(int(pair[0]), int(pair[1]))

    def outward_upper(value):
        return math.nextafter(float(value), math.inf)

    def outward_lower(value):
        return math.nextafter(float(value), -math.inf)

    extrema = {
        "M1": None, "M2": None, "M_minus1": None,
        "j0": None, "j1": None,
    }
    certificate_digest = hashlib.sha256()
    coordinate_digest = hashlib.sha256()
    failed_cells = []
    cell_certificates = []
    max_depth = 0
    max_nodes = 0

    for cell in range(nc):
        dofs = geometry_dofmap[cell]
        coordinates = mesh.geometry.x[dofs, :2]
        cert = certify_p3_cell_geometry(coordinates, points)
        coordinate_digest.update(cert["coordinate_sha256"].encode("ascii"))
        certificate_digest.update(str(cell).encode("ascii"))
        certificate_digest.update(b":")
        if not cert["positive"]:
            failed_cells.append({
                "cell": int(cell),
                "failure": cert["failure"],
                "subdivision_depth_max": cert["subdivision_depth_max"],
            })
            certificate_digest.update(b"FAIL:")
            certificate_digest.update(cert["coordinate_sha256"].encode("ascii"))
            cell_certificates.append({
                "cell": int(cell),
                "positive": False,
                "failure": cert["failure"],
                "coordinate_sha256": cert["coordinate_sha256"],
                "subdivision_depth_max": int(cert["subdivision_depth_max"]),
                "subdivision_nodes": int(cert["subdivision_nodes"]),
            })
            continue

        values = {
            "M1": as_fraction(cert["M1_upper_scaled_exact"]),
            "M2": as_fraction(cert["M2_upper_scaled_exact"]),
            "M_minus1": as_fraction(cert["M_minus1_upper_scaled_exact"]),
            "j0": (
                as_fraction(cert["determinant_lower_scaled_exact"])
                / (2 * as_fraction(cert["M1_upper_scaled_exact"]) ** 2)
            ),
            "j1": as_fraction(cert["determinant_upper_scaled_exact"]),
        }
        for name, value in values.items():
            if extrema[name] is None:
                extrema[name] = value
            elif name == "j0":
                extrema[name] = min(extrema[name], value)
            else:
                extrema[name] = max(extrema[name], value)
        max_depth = max(max_depth, int(cert["subdivision_depth_max"]))
        max_nodes = max(max_nodes, int(cert["subdivision_nodes"]))
        certificate_digest.update(
            repr(tuple((name, values[name].numerator, values[name].denominator)
                       for name in sorted(values))).encode("ascii")
        )
        certificate_digest.update(cert["coordinate_sha256"].encode("ascii"))
        cell_certificates.append({
            "cell": int(cell),
            "positive": True,
            "coordinate_sha256": cert["coordinate_sha256"],
            "determinant_lower_scaled_exact": cert["determinant_lower_scaled_exact"],
            "determinant_upper_scaled_exact": cert["determinant_upper_scaled_exact"],
            "M1_upper_scaled_exact": cert["M1_upper_scaled_exact"],
            "M2_upper_scaled_exact": cert["M2_upper_scaled_exact"],
            "M_minus1_upper_scaled_exact": cert["M_minus1_upper_scaled_exact"],
            "j0_lower_scaled_exact": [values["j0"].numerator, values["j0"].denominator],
            "j1_upper_scaled_exact": [values["j1"].numerator, values["j1"].denominator],
            "subdivision_depth_max": int(cert["subdivision_depth_max"]),
            "subdivision_nodes": int(cert["subdivision_nodes"]),
        })

    certified = not failed_cells and nc > 0
    return {
        "method": (
            "exact dyadic-rational P3 nodal reconstruction; exact polynomial "
            "differentiation/determinant; exact triangular Bernstein coefficients "
            "and rational four-way subdivision"
        ),
        "arithmetic": "Python fractions.Fraction; no floating-point polynomial reconstruction",
        "input_coordinates": "stored IEEE-754 binary64 geometry coordinates interpreted as exact dyadic rationals",
        "coordinate_element": {
            "degree": int(cmap.degree),
            "dimension": int(cmap.dim),
            "lagrange_variant": lagrange_variant,
            "interpolation_is_identity": bool(coordinate_element.interpolation_is_identity),
            "reference_nodes": int(points.shape[0]),
            "node_set": "equispaced triangular P3 lattice, checked against interpolation points to 1e-12 before exact rational reconstruction",
        },
        "cells": int(nc),
        "all_cell_jacobians_certified_positive": bool(certified),
        "failed_cell_count": len(failed_cells),
        "failed_cells": failed_cells[:20],
        "global_M1_upper_bound": outward_upper(extrema["M1"]) if certified else None,
        "global_M2_upper_bound": outward_upper(extrema["M2"]) if certified else None,
        "global_M_minus1_upper_bound": outward_upper(extrema["M_minus1"]) if certified else None,
        "global_j0_lower_bound": outward_lower(extrema["j0"]) if certified else None,
        "global_j1_upper_bound": outward_upper(extrema["j1"]) if certified else None,
        "global_M1_upper_bound_exact": (
            [extrema["M1"].numerator, extrema["M1"].denominator] if certified else None
        ),
        "global_M2_upper_bound_exact": (
            [extrema["M2"].numerator, extrema["M2"].denominator] if certified else None
        ),
        "global_M_minus1_upper_bound_exact": (
            [extrema["M_minus1"].numerator, extrema["M_minus1"].denominator] if certified else None
        ),
        "global_j0_lower_bound_exact": (
            [extrema["j0"].numerator, extrema["j0"].denominator] if certified else None
        ),
        "global_j1_upper_bound_exact": (
            [extrema["j1"].numerator, extrema["j1"].denominator] if certified else None
        ),
        "maximum_subdivision_depth": max_depth,
        "maximum_subdivision_nodes_per_cell": max_nodes,
        "coordinate_data_sha256": coordinate_digest.hexdigest(),
        "cell_certificate_sha256": certificate_digest.hexdigest(),
        "cell_certificates": cell_certificates,
        "formal_exact_rational_certificate": bool(certified),
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
    parser.add_argument("--certificate-out", default="artifacts/morandotti_trace_constant/cell-certificates.jsonl.gz")
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
    certificate_path = Path(args.certificate_out)
    certificate_path.parent.mkdir(parents=True, exist_ok=True)
    with certificate_path.open("wb") as certificate_file:
        with gzip.GzipFile(filename="", mode="wb", fileobj=certificate_file, mtime=0) as compressed:
            certificate_stream = io.TextIOWrapper(compressed, encoding="utf-8")
            for distance in args.distances:
                centers = ((-0.5 * distance, 0.0), (0.5 * distance, 0.0))
                for h in args.mesh_sizes:
                    for seed in args.seeds:
                        mesh, _ = make_mesh(1.0, 0.12, centers, h, MPI.COMM_WORLD, random_seed=seed)
                        result = trace_constant_for_mesh(mesh)
                        cell_records = result["geometry_certificate"].pop("cell_certificates")
                        for cell_record in cell_records:
                            record = {
                                "distance": float(distance),
                                "h_target": float(h),
                                "mesh_seed": int(seed),
                                **cell_record,
                            }
                            certificate_stream.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
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
            certificate_stream.flush()
            certificate_stream.detach()
    certificate_hash = hashlib.sha256()
    with certificate_path.open("rb") as certificate_file:
        for chunk in iter(lambda: certificate_file.read(1024 * 1024), b""):
            certificate_hash.update(chunk)

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
        "cell_certificate_archive": {
            "path": str(certificate_path),
            "format": "gzip-compressed JSON Lines; one exact-rational record per local cell and generated mesh",
            "sha256": certificate_hash.hexdigest(),
            "records": sum(r["geometry_certificate"]["cells"] for r in runs),
            "fields": ["distance", "h_target", "mesh_seed", "cell", "positive", "coordinate_sha256", "determinant_lower_scaled_exact", "determinant_upper_scaled_exact", "M1_upper_scaled_exact", "M2_upper_scaled_exact", "M_minus1_upper_scaled_exact", "j0_lower_scaled_exact", "j1_upper_scaled_exact", "subdivision_depth_max", "subdivision_nodes"],
        },
        "limitations": [
            "a finite set of generalized eigenvalues does not prove sup_h C_tr,h is bounded",
            "exact geometry certificates cover every cell in each generated mesh, but the finite seed/resolution sweep does not certify every possible mesh generated by the parameterized family",
            "the geometry certificate proves positive Jacobians and scaled derivative/inverse-Jacobian bounds for the represented cell maps; it does not by itself prove a mesh-uniform trace-constant bound",
            "the estimate uses the generated two-core P3 mesh family and the T134 facet weights; it is not a universal P3 constant",
            "quadrature stability is assessed from the last two estimates (degrees 32 and 40); instability is reported rather than aborting the sweep",
            "even a stable finite quadrature sequence is numerical evidence, not an exact integration certificate",
            "the exact-rational geometry certificate treats each stored binary64 geometry coordinate as its exact dyadic value; it certifies the represented polynomial map, not uncertainty in the upstream CAD/Gmsh construction",
        ],
    }
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
