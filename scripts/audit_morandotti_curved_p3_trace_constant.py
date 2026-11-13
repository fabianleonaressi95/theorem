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
    return {
        "cells": int(nc),
        "free_dofs_after_zero_value_boundary_conditions": free_dofs,
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



def _aic_bic(y, fitted, k):
    """Gaussian least-squares AIC/BIC; small-sample AICc is reported too."""
    n = len(y)
    rss = max(float(np.sum((y - fitted) ** 2)), 1e-300)
    aic = n * np.log(rss / n) + 2 * k
    bic = n * np.log(rss / n) + k * np.log(n)
    aicc = aic + (2 * k * (k + 1) / (n - k - 1)) if n > k + 1 else float("inf")
    return {"AIC": float(aic), "AICc": float(aicc), "BIC": float(bic), "RSS": rss, "n": n, "k": k}


def statistical_model_audit(runs, distances, mesh_sizes, bootstrap_replicates=2000):
    """Exploratory scaling-model comparison and seed-stratified bootstrap.

    Models are fitted to all seed-level C_tr,h observations at each distance:
    constant; power law a*h^p; and asymptotic C_inf+a*h^p. The bootstrap
    resamples independent mesh seeds within each h level, not FEM DOFs.
    """
    from scipy.optimize import curve_fit
    rng = np.random.default_rng(20261113)
    output = {}
    for distance in distances:
        rows = [r for r in runs if r["distance"] == float(distance)]
        h = np.asarray([r["h_target"] for r in rows], dtype=float)
        y = np.asarray([r["quadrature_estimates"][-1]["C_tr_h"] for r in rows], dtype=float)
        def constant(x, c): return np.full_like(x, c, dtype=float)
        def power(x, a, p): return a * np.power(x, p)
        def asymptotic(x, c, a, p): return c + a * np.power(x, p)
        candidates = {}
        for name, fn, p0, bounds in (
            ("constant", constant, [float(np.mean(y))], (-np.inf, np.inf)),
            ("power_law", power, [float(np.mean(y)), 0.5], ([0.0, -4.0], [np.inf, 4.0])),
            ("finite_limit_power_law", asymptotic, [max(0.0, float(np.min(y))*0.8), 1.0, 0.5],
             ([-np.inf, -np.inf, -4.0], [np.inf, np.inf, 4.0])),
        ):
            try:
                params, _ = curve_fit(fn, h, y, p0=p0, bounds=bounds, maxfev=50000)
                fitted = fn(h, *params)
                score = _aic_bic(y, fitted, len(params))
                candidates[name] = {"parameters": [float(v) for v in params], **score}
            except Exception as exc:
                candidates[name] = {"fit_error": str(exc)}
        valid = {k:v for k,v in candidates.items() if "AICc" in v}
        if valid:
            best = min(valid, key=lambda k: valid[k]["AICc"])
            min_aicc = valid[best]["AICc"]
            for item in valid.values():
                item["delta_AICc"] = float(item["AICc"] - min_aicc)
        else:
            best = None

        # Resample the seed realizations independently within each mesh level.
        by_h = []
        for level in mesh_sizes:
            vals = np.asarray([r["quadrature_estimates"][-1]["C_tr_h"]
                               for r in rows if r["h_target"] == float(level)], dtype=float)
            if vals.size < 2:
                raise RuntimeError("Monte Carlo bootstrap requires at least two seeds at every mesh size")
            by_h.append(vals)
        limits = []
        for _ in range(int(bootstrap_replicates)):
            hb, yb = [], []
            for level, vals in zip(mesh_sizes, by_h):
                draw = rng.choice(vals, size=vals.size, replace=True)
                hb.extend([float(level)] * draw.size)
                yb.extend(draw.tolist())
            try:
                pars, _ = curve_fit(asymptotic, np.asarray(hb), np.asarray(yb),
                                    p0=[max(0.0, min(yb)*0.8), 1.0, 0.5],
                                    bounds=([-np.inf, -np.inf, -4.0], [np.inf, np.inf, 4.0]),
                                    maxfev=10000)
                if np.isfinite(pars[0]): limits.append(float(pars[0]))
            except Exception:
                pass
        output[f"d{float(distance):.4f}"] = {
            "observations": int(y.size),
            "mesh_levels": [float(v) for v in mesh_sizes],
            "models": candidates,
            "preferred_model_by_AICc": best,
            "bootstrap": {
                "method": "seed-stratified nonparametric bootstrap; resample seed-level C_tr,h values independently within each h",
                "requested_replicates": int(bootstrap_replicates),
                "successful_fits": len(limits),
                "C_infinity_percentile_95_interval": ([float(v) for v in np.quantile(limits, [0.025, 0.975])]
                                                       if limits else None),
                "C_infinity_median": float(np.median(limits)) if limits else None,
                "warning": "Exploratory uncertainty conditional on the sampled mesh generator and only the supplied seeds; not a mesh-uniform bound or proof."
            }
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
