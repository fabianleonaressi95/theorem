#!/usr/bin/env python3
"""P1 displacement transfer on the exact perforated P3 C0-IPDG mesh.

The eigenstrain is stress-equivalent and reconstructed from the P3 Airy field.
This is a cross-discretization consistency test, NOT independent defect-source
validation. Mesh coordinates, geometry dofmap, and P3 dof coordinates are
checked against the saved P3 artifact before solving.
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
from dolfinx.fem.petsc import LinearProblem

from scripts.rgs_morandotti_two_core_c0_ipdg import make_mesh
from models.morandotti_cell_reconstruction import (
    build_defect_components, solve_interaction_system, reconstruct_airy_potential,
)


def compliance_tensor(stress, E, nu):
    """Plane-strain compliance; tensor shear component is epsilon_xy."""
    sxx, syy, sxy = stress[0, 0], stress[1, 1], stress[0, 1]
    fac = (1.0 + nu) / E
    exx = fac * ((1.0 - nu) * sxx - nu * syy)
    eyy = fac * ((1.0 - nu) * syy - nu * sxx)
    exy = fac * sxy
    return ufl.as_tensor([[exx, exy], [exy, eyy]])


def run(input_path: str, output_path: str, young_modulus=1.0, poisson_ratio=0.0):
    data = np.load(input_path)
    centers = np.asarray(data["centers"], dtype=float)
    h = float(np.asarray(data["mesh_target_h"]).reshape(-1)[0])
    if centers.shape != (2, 2):
        raise ValueError("the P1 transfer currently requires the archived two-core geometry")
    mesh, tags = make_mesh(1.0, 0.12, tuple(map(tuple, centers)), h, MPI.COMM_WORLD)

    # Refuse a nominally identical but actually different remesh.
    geometry = np.asarray(mesh.geometry.x)
    geometry_dofmap = np.asarray(mesh.geometry.dofmap)
    if geometry.shape != data["geometry_coordinates"].shape or not np.array_equal(geometry_dofmap, data["geometry_dofmap"]):
        raise RuntimeError("regenerated mesh geometry dofmap differs from the P3 artifact")
    if not np.allclose(geometry, data["geometry_coordinates"], rtol=0.0, atol=2e-13):
        raise RuntimeError("regenerated mesh coordinates differ from the P3 artifact")

    V3 = fem.functionspace(mesh, ("Lagrange", 3))
    dof_coordinates = V3.tabulate_dof_coordinates()
    if dof_coordinates.shape != data["dof_coordinates"].shape or not np.allclose(
        dof_coordinates, data["dof_coordinates"], rtol=0.0, atol=2e-13
    ):
        raise RuntimeError("P3 function-space dof coordinates do not match the saved artifact")

    # Reconstruct the same mixed Frank/Burgers Airy case used by the P3 driver.
    frank = np.array([0.2, 0.0])
    burgers = np.array([[0.0, 0.0], [0.03, -0.04]])
    phi_f, phi_b, phi = build_defect_components(centers, frank, burgers)
    M = np.asarray(data["M_laplacian"], dtype=float)
    coeff = solve_interaction_system(M, phi)
    airy_dofs = reconstruct_airy_potential(
        np.asarray(data["field_coefficients"]), coeff, young_modulus, poisson_ratio
    )
    airy = fem.Function(V3)
    airy.x.array[:] = airy_dofs
    airy.x.scatter_forward()

    H = ufl.grad(ufl.grad(airy))
    sigma_A = ufl.as_tensor([[H[1, 1], -H[0, 1]], [-H[1, 0], H[0, 0]]])
    eps_star = -compliance_tensor(sigma_A, young_modulus, poisson_ratio)

    # Plane-strain displacement elasticity on P1 triangles. The three point
    # constraints remove the two translations and one in-plane rotation.
    V = fem.functionspace(mesh, ("Lagrange", 1, (2,)))
    u, v = ufl.TrialFunction(V), ufl.TestFunction(V)
    I = ufl.Identity(2)
    mu = young_modulus / (2.0 * (1.0 + poisson_ratio))
    lam = young_modulus * poisson_ratio / ((1.0 + poisson_ratio) * (1.0 - 2.0 * poisson_ratio))
    eps_u = ufl.sym(ufl.grad(u))
    eps_v = ufl.sym(ufl.grad(v))
    C_eps_u = 2.0 * mu * eps_u + lam * ufl.tr(eps_u) * I
    C_eps_star = 2.0 * mu * eps_star + lam * ufl.tr(eps_star) * I
    dx = ufl.Measure("dx", domain=mesh, metadata={"quadrature_degree": 10})
    ds = ufl.Measure("ds", domain=mesh, subdomain_data=tags,
                     metadata={"quadrature_degree": 10})
    a_form = ufl.inner(C_eps_u, eps_v) * dx
    L_form = ufl.inner(C_eps_star, eps_v) * dx

    nvertices = mesh.topology.index_map(0).size_local
    vertex_xy = mesh.geometry.x[:nvertices, :2]
    if len(vertex_xy) < 2:
        raise RuntimeError("mesh has too few vertices for rigid-mode gauge")
    v0 = int(np.argmin(np.linalg.norm(vertex_xy - np.array([1.0, 0.0]), axis=1)))
    v1 = int(np.argmin(np.linalg.norm(vertex_xy - np.array([-1.0, 0.0]), axis=1)))
    if v0 == v1:
        raise RuntimeError("could not select two distinct gauge vertices")
    d0x = fem.locate_dofs_topological(V.sub(0), 0, np.array([v0], dtype=np.int32))
    d0y = fem.locate_dofs_topological(V.sub(1), 0, np.array([v0], dtype=np.int32))
    d1y = fem.locate_dofs_topological(V.sub(1), 0, np.array([v1], dtype=np.int32))
    zero = PETSc.ScalarType(0.0)
    bcs = [
        fem.dirichletbc(zero, d0x, V.sub(0)),
        fem.dirichletbc(zero, d0y, V.sub(1)),
        fem.dirichletbc(zero, d1y, V.sub(1)),
    ]
    problem = LinearProblem(
        a_form, L_form, bcs=bcs, petsc_options_prefix="airy_p1_transfer_",
        petsc_options={"ksp_type": "preonly", "pc_type": "lu",
                       "pc_factor_mat_solver_type": "mumps"},
    )
    uh = problem.solve()
    eps_h = ufl.sym(ufl.grad(uh))
    sigma_h = 2.0 * mu * (eps_h - eps_star) + lam * ufl.tr(eps_h - eps_star) * I
    diff = sigma_h - sigma_A

    def integral(expr):
        return float(mesh.comm.allreduce(fem.assemble_scalar(fem.form(expr)), op=MPI.SUM))

    stress_error = np.sqrt(max(integral(ufl.inner(diff, diff) * dx), 0.0))
    stress_reference = np.sqrt(max(integral(ufl.inner(sigma_A, sigma_A) * dx), 0.0))
    energy_A = 0.5 * integral(ufl.inner(sigma_A, compliance_tensor(sigma_A, young_modulus, poisson_ratio)) * dx)
    energy_P1 = 0.5 * integral(ufl.inner(sigma_h, compliance_tensor(sigma_h, young_modulus, poisson_ratio)) * dx)

    traction = ufl.dot(sigma_h, ufl.FacetNormal(mesh))
    airy_traction = ufl.dot(sigma_A, ufl.FacetNormal(mesh))
    traction_rows = {}
    for tag, name in ((1, "outer"), (2, "core_0"), (3, "core_1")):
        traction_rows[name] = {
            "p1_l2": float(np.sqrt(max(integral(ufl.inner(traction, traction) * ds(tag)), 0.0))),
            "airy_l2": float(np.sqrt(max(integral(ufl.inner(airy_traction, airy_traction) * ds(tag)), 0.0))),
        }

    # Broken cellwise incompatibility identity. This intentionally does not
    # include distributional inter-element jump terms of the C0 Airy field.
    nu = float(poisson_ratio)
    coef = (1.0 - nu**2) / float(young_modulus)
    inc_star = (eps_star[0, 0].dx(1).dx(1) + eps_star[1, 1].dx(0).dx(0)
                - 2.0 * eps_star[0, 1].dx(0).dx(1))
    lap = airy.dx(0).dx(0) + airy.dx(1).dx(1)
    biharm = lap.dx(0).dx(0) + lap.dx(1).dx(1)
    inc_expected = -coef * biharm
    inc_residual = np.sqrt(max(integral((inc_star - inc_expected)**2 * dx), 0.0))
    inc_scale = np.sqrt(max(integral(inc_expected**2 * dx), 0.0))

    result = {
        "status": "computed",
        "method": "P1 displacement on regenerated mesh with exact P3 geometry/dof-coordinate checks",
        "source_status": "stress-equivalent eigenstrain derived from the Airy stress; consistency test, not independent defect validation",
        "mesh": {"h_target": h, "cells": int(mesh.topology.index_map(mesh.topology.dim).size_global),
                 "geometry_dofmap_exact_match": True, "geometry_coordinates_max_abs_difference":
                 float(np.max(np.abs(geometry - data["geometry_coordinates"])))},
        "material": {"young_modulus": float(young_modulus), "poisson_ratio": nu, "plane": "strain"},
        "stress": {"airy_l2": float(stress_reference), "p1_minus_airy_l2": float(stress_error),
                   "relative_l2": float(stress_error / max(stress_reference, 1e-300))},
        "energy": {"airy_complementary": float(energy_A), "p1_complementary": float(energy_P1),
                   "relative_difference": float(abs(energy_P1-energy_A) / max(abs(energy_A), 1e-300))},
        "boundary_traction_l2": traction_rows,
        "broken_cellwise_incompatibility": {"residual_l2": float(inc_residual),
                                             "reference_l2": float(inc_scale),
                                             "relative_residual": float(inc_residual / max(inc_scale, 1e-300))},
        "limitations": [
            "P1 displacement only; Q1 quadrilateral comparison is not yet implemented",
            "the eigenstrain is manufactured from the Airy stress and is not an independent Frank/Burgers source",
            "broken cellwise incompatibility excludes distributional inter-element jump contributions",
            "one mesh level is a transfer check, not a convergence study",
            "the historical 18.52% discrepancy is not declared resolved by this run",
        ],
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(json.dumps(result, indent=2) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="P3 cell_fields_h*.npz artifact")
    parser.add_argument("--out", default="artifacts/morandotti_p1_transfer/report.json")
    parser.add_argument("--young-modulus", type=float, default=1.0)
    parser.add_argument("--poisson-ratio", type=float, default=0.0)
    args = parser.parse_args()
    result = run(args.input, args.out, args.young_modulus, args.poisson_ratio)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
