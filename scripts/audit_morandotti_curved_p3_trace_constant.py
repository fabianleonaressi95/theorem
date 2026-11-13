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
    n = V.dofmap.index_map.size_local
    free = np.setdiff1d(np.arange(n, dtype=np.int32), boundary_dofs)
    if free.size < 3:
        raise RuntimeError(f"too few free P3 degrees of freedom after homogeneous boundary constraints: {free.size}")
    Dsp = _petsc_to_scipy(D, n)[free][:, free]
    Hsp = _petsc_to_scipy(H, n)[free][:, free]
    D.destroy()
    H.destroy()
    return largest_generalized_eigenvalue(Hsp, Dsp), int(free.size)


def trace_constant_for_mesh(mesh, quadrature_degrees=(12, 16)):
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
        value, count = _assemble_pair(D_form, H_form, V, mesh, int(degree))
        estimates.append({"quadrature_degree": int(degree), "C_tr_h": value})
        free_dofs = count

    # Sample the actual cubic geometry map on a triangular reference grid.
    from dolfinx import fem as _fem
    points = np.asarray([
        (i / 8.0, j / 8.0)
        for i in range(9) for j in range(9 - i)
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
        "quadrature_relative_difference": float(
            abs(estimates[-1]["C_tr_h"] - estimates[0]["C_tr_h"])
            / max(abs(estimates[-1]["C_tr_h"]), 1e-300)
        ),
        "geometry_map_diagnostics": geometry,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mesh-sizes", nargs="+", type=float, default=[0.08, 0.045])
    parser.add_argument("--distances", nargs="+", type=float, default=[0.48, 0.56])
    parser.add_argument("--seeds", nargs="+", type=int, default=[11, 29, 47])
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
                }
                if not row["geometry_map_diagnostics"]["all_sampled_determinants_positive"]:
                    raise RuntimeError(f"non-positive sampled cubic Jacobian for {row}")
                if row["quadrature_relative_difference"] > 5e-3:
                    raise RuntimeError(f"trace-constant estimate is not quadrature-stable: {row}")
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
            }

    payload = {
        "title": "Morandotti curved-P3 finite-mesh T134 trace-constant audit",
        "status": "finite-mesh generalized-eigenvalue estimates; not a mesh-uniform proof",
        "definition": "C_tr,h = sup_{v_h in V_h^0} H_{h,l}(v_h)^2 / D_h(v_h)^2",
        "boundary_space": "globally continuous mapped P3 functions with zero value trace on outer and both core boundaries",
        "quadratic_forms": {
            "D": "integral_Omega D^2u:D^2v",
            "H": "sum_interior avg(h_K) integral_F avg(n^T D^2u n) avg(n^T D^2v n) + sum_boundary h_K integral_F (n^T D^2u n)(n^T D^2v n)",
        },
        "quadrature_degrees": [12, 16],
        "mesh_sizes": args.mesh_sizes,
        "distances": args.distances,
        "seeds": args.seeds,
        "group_summary": grouped,
        "runs": runs,
        "limitations": [
            "a finite set of generalized eigenvalues does not prove sup_h C_tr,h is bounded",
            "positive Jacobians are checked only at sampled reference points, not certified at every point",
            "uniform mapped-element derivative and inverse-Jacobian bounds remain an analytic obligation",
            "the estimate uses the generated two-core P3 mesh family and the T134 facet weights; it is not a universal P3 constant",
            "quadrature stability is checked at degrees 12 and 16 but does not replace exact integration",
        ],
    }
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
