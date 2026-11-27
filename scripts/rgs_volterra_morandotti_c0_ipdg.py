#!/usr/bin/env python3
"""Matched three-core P3 C0-IPDG benchmark: Volterra dipole versus edge defect.

Requires the same DOLFINx 0.11 / Gmsh / PETSc-MUMPS stack as the existing
Morandotti reproduction scripts. Both configurations use the *same* perforated
domain, all nine P3 cell fields, and the same interaction matrix at each
(separation, core radius, mesh size). Only Frank/Burgers data are changed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import gmsh
import numpy as np
from mpi4py import MPI
from petsc4py import PETSc
import ufl
from dolfinx import fem
from dolfinx.fem.petsc import LinearProblem
from dolfinx.io import gmsh as gmshio

from models.morandotti_cell_reconstruction import (
    build_defect_components,
    reconstruct_airy_potential,
    solve_interaction_system,
)
from models.volterra_morandotti_benchmark import volterra_three_core_data


def assemble(expr, mesh) -> float:
    return float(mesh.comm.allreduce(fem.assemble_scalar(fem.form(expr)), op=MPI.SUM))


def make_three_core_mesh(radius: float, core_radius: float,
                         centers: np.ndarray, h: float, comm):
    if comm.size != 1:
        raise RuntimeError("The initial three-core benchmark is serial; MPI is not yet audited")
    gmsh.initialize()
    try:
        gmsh.option.setNumber("General.Terminal", 0)
        gmsh.model.add("volterra_three_core")
        outer = gmsh.model.occ.addDisk(0.0, 0.0, 0.0, radius, radius)
        holes = [gmsh.model.occ.addDisk(float(x), float(y), 0.0,
                                        core_radius, core_radius)
                 for x, y in centers]
        surfaces, _ = gmsh.model.occ.cut(
            [(2, outer)], [(2, tag) for tag in holes],
            removeObject=True, removeTool=True)
        gmsh.model.occ.synchronize()
        curves = gmsh.model.getBoundary(surfaces, combined=False, oriented=False)
        outer_curves: list[int] = []
        core_curves: list[list[int]] = [[] for _ in range(len(centers))]
        for dim, tag in curves:
            if dim != 1:
                continue
            bb = gmsh.model.getBoundingBox(dim, tag)
            cx, cy = 0.5*(bb[0]+bb[3]), 0.5*(bb[1]+bb[4])
            extent = max(bb[3]-bb[0], bb[4]-bb[1])
            if extent > 0.5*radius:
                outer_curves.append(tag)
            else:
                index = int(np.argmin(np.linalg.norm(centers-[cx, cy], axis=1)))
                core_curves[index].append(tag)
        if not outer_curves or any(not group for group in core_curves):
            raise RuntimeError(
                f"Boundary classification failed: outer={outer_curves}, cores={core_curves}")
        surface_tags = [tag for dim, tag in surfaces if dim == 2]
        gmsh.model.addPhysicalGroup(2, surface_tags, 10)
        gmsh.model.addPhysicalGroup(1, outer_curves, 1)
        for k, group in enumerate(core_curves):
            gmsh.model.addPhysicalGroup(1, group, 2+k)
        gmsh.option.setNumber("Mesh.MeshSizeMin", h)
        gmsh.option.setNumber("Mesh.MeshSizeMax", h)
        gmsh.option.setNumber("Mesh.ElementOrder", 3)
        gmsh.option.setNumber("Mesh.HighOrderOptimize", 2)
        gmsh.model.mesh.generate(2)
        gmsh.model.mesh.setOrder(3)
        data = gmshio.model_to_mesh(gmsh.model, comm, 0, gdim=2)
        return data.mesh, data.facet_tags
    finally:
        gmsh.finalize()


def solve_cell_basis(mesh, facet_tags, alpha: float) -> tuple[list, np.ndarray, dict]:
    mesh.topology.create_connectivity(mesh.topology.dim-1, mesh.topology.dim)
    V = fem.functionspace(mesh, ("Lagrange", 3))
    normal = ufl.FacetNormal(mesh)
    hspace = fem.functionspace(mesh, ("DG", 0))
    cell_h = fem.Function(hspace)
    ncells = mesh.topology.index_map(mesh.topology.dim).size_local
    cells = np.arange(ncells, dtype=np.int32)
    cell_h.x.array[:] = mesh.h(mesh.topology.dim, cells)
    cell_h.x.scatter_forward()

    dx = ufl.Measure("dx", domain=mesh, metadata={"quadrature_degree": 9})
    ds = ufl.Measure("ds", domain=mesh, subdomain_data=facet_tags,
                     metadata={"quadrature_degree": 9})
    dS = ufl.Measure("dS", domain=mesh, metadata={"quadrature_degree": 9})
    u, v = ufl.TrialFunction(V), ufl.TestFunction(V)
    Hu, Hv = ufl.grad(ufl.grad(u)), ufl.grad(ufl.grad(v))
    Hun = ufl.dot(ufl.dot(Hu, normal), normal)
    Hvn = ufl.dot(ufl.dot(Hv, normal), normal)
    ju, jv = ufl.jump(ufl.grad(u), normal), ufl.jump(ufl.grad(v), normal)
    bilinear = (
        ufl.inner(Hu, Hv)*dx
        -(ju*ufl.avg(Hvn)+jv*ufl.avg(Hun))*dS
        -(ufl.dot(ufl.grad(u), normal)*Hvn
          + ufl.dot(ufl.grad(v), normal)*Hun)*ds
        +(alpha/ufl.avg(cell_h))*ju*jv*dS
        +(alpha/cell_h("+"))*ufl.dot(ufl.grad(u), normal)
          *ufl.dot(ufl.grad(v), normal)*ds
    )
    outer_dofs = fem.locate_dofs_topological(V, 1, facet_tags.find(1))
    core_dofs = [fem.locate_dofs_topological(V, 1, facet_tags.find(2+k))
                 for k in range(3)]
    all_core_dofs = np.unique(np.concatenate(core_dofs))
    dof_xy = V.tabulate_dof_coordinates()[:, :2]
    zero = fem.Constant(mesh, PETSc.ScalarType(0.0))
    fields = []
    boundary_residuals = []
    for core_index in range(3):
        for mode in range(3):
            boundary_data = fem.Function(V)
            boundary_data.x.array[:] = 0.0
            active = core_dofs[core_index]
            if mode == 0:
                boundary_data.x.array[active] = 1.0
                normal_data = ufl.as_ufl(0.0)
            elif mode == 1:
                boundary_data.x.array[active] = dof_xy[active, 0]
                normal_data = normal[0]
            else:
                boundary_data.x.array[active] = dof_xy[active, 1]
                normal_data = normal[1]
            boundary_data.x.scatter_forward()
            bcs = [fem.dirichletbc(zero, outer_dofs, V),
                   fem.dirichletbc(boundary_data, all_core_dofs)]
            active_tag = 2+core_index
            linear = (
                -normal_data*Hvn
                +(alpha/cell_h("+"))*normal_data
                  *ufl.dot(ufl.grad(v), normal)
            )*ds(active_tag) + zero*v*dx
            problem = LinearProblem(
                bilinear, linear, bcs=bcs,
                petsc_options_prefix=f"volterra_core_{core_index}_{mode}_",
                petsc_options={"ksp_type": "preonly", "pc_type": "lu",
                               "pc_factor_mat_solver_type": "mumps"})
            field = problem.solve()
            fields.append(field)
            x = ufl.SpatialCoordinate(mesh)
            value_target = (1.0 if mode == 0 else
                            (x[0] if mode == 1 else x[1]))
            for tag, name in [(1, "outer"), (2, "core_0"),
                              (3, "core_1"), (4, "core_2")]:
                target_value = value_target if tag == active_tag else 0.0
                target_normal = normal_data if tag == active_tag else 0.0
                value_error = np.sqrt(max(assemble(
                    (field-target_value)**2*ds(tag), mesh), 0.0))
                normal_error = np.sqrt(max(assemble(
                    (ufl.dot(ufl.grad(field), normal)-target_normal)**2*ds(tag), mesh), 0.0))
                boundary_residuals.append({
                    "active_core": core_index, "mode": mode, "boundary": name,
                    "value_l2": float(value_error),
                    "normal_derivative_l2": float(normal_error)})
    count = len(fields)
    interaction = np.zeros((count, count))
    hessian_matrix = np.zeros_like(interaction)
    hessians = [ufl.grad(ufl.grad(field)) for field in fields]
    for i in range(count):
        for j in range(count):
            interaction[i, j] = assemble(
                ufl.div(ufl.grad(fields[i]))*ufl.div(ufl.grad(fields[j]))*dx, mesh)
            hessian_matrix[i, j] = assemble(
                ufl.inner(hessians[i], hessians[j])*dx, mesh)
    matrix_symmetry = float(np.linalg.norm(interaction-interaction.T, "fro") /
                            max(np.linalg.norm(interaction, "fro"), 1e-300))
    eigenvalues = np.linalg.eigvalsh(0.5*(interaction+interaction.T))
    diagnostics = {
        "num_cells": int(ncells),
        "num_p3_dofs": int(V.dofmap.index_map.size_global*V.dofmap.index_map_bs),
        "interaction_symmetry_residual": matrix_symmetry,
        "interaction_min_eigenvalue": float(eigenvalues[0]),
        "interaction_condition_number": float(np.linalg.cond(interaction)),
        "hessian_laplacian_matrix_relative_difference": float(
            np.linalg.norm(hessian_matrix-interaction, "fro") /
            max(np.linalg.norm(hessian_matrix, "fro"), 1e-300)),
        "boundary_residuals": boundary_residuals,
    }
    return fields, interaction, diagnostics


def reconstruct_case(fields, interaction, data: dict, case: str,
                     young_modulus: float, poisson_ratio: float,
                     mesh, facet_tags) -> dict:
    if case == "dipole":
        frank, burgers = data["frank_dipole"], data["burgers_dipole"]
    elif case == "edge":
        frank, burgers = data["frank_edge"], data["burgers_edge"]
    else:
        raise ValueError(f"unknown case: {case}")
    centers = data["centers"]
    phi = build_defect_components(centers, frank, burgers)[2]
    coefficients = solve_interaction_system(interaction, phi)
    field_coefficients = np.stack([field.x.array.copy() for field in fields])
    potential = reconstruct_airy_potential(
        field_coefficients, coefficients, young_modulus, poisson_ratio)
    V = fields[0].function_space
    airy = fem.Function(V)
    airy.x.array[:] = potential
    airy.x.scatter_forward()

    H = ufl.grad(ufl.grad(airy))
    stress = ufl.as_matrix([[H[1, 1], -H[0, 1]],
                            [-H[1, 0], H[0, 0]]])
    E = float(young_modulus)
    nu = float(poisson_ratio)
    mu = E/(2.0*(1.0+nu))
    lam = E*nu/((1.0+nu)*(1.0-2.0*nu))
    trace = stress[0, 0]+stress[1, 1]
    eps = (stress-(lam/(2.0*(mu+lam)))*trace*ufl.Identity(2))/(2.0*mu)
    energy_density = 0.5*ufl.inner(stress, eps)
    dx = ufl.Measure("dx", domain=mesh, metadata={"quadrature_degree": 9})
    ds = ufl.Measure("ds", domain=mesh, subdomain_data=facet_tags,
                     metadata={"quadrature_degree": 9})
    normal = ufl.FacetNormal(mesh)
    traction = ufl.dot(stress, normal)
    stress_norm = np.sqrt(max(assemble(ufl.inner(stress, stress)*dx, mesh), 0.0))
    strain_norm = np.sqrt(max(assemble(ufl.inner(eps, eps)*dx, mesh), 0.0))
    energy = assemble(energy_density*dx, mesh)
    traction_norms = {
        name: float(np.sqrt(max(assemble(
            ufl.inner(traction, traction)*ds(tag), mesh), 0.0)))
        for tag, name in [(1, "outer"), (2, "core_upper"),
                          (3, "core_lower"), (4, "core_centre")]
    }
    return {
        "source_vector": phi.tolist(),
        "interaction_coefficients": coefficients.tolist(),
        "stress_l2": float(stress_norm),
        "strain_l2": float(strain_norm),
        "bulk_elastic_energy": float(energy),
        "traction_l2_by_boundary": traction_norms,
    }


def solve_level(separation: float, core_radius: float, mesh_size: float,
                alpha: float, radius: float, omega: float,
                young_modulus: float, poisson_ratio: float) -> dict:
    data = volterra_three_core_data(separation, core_radius, omega)
    mesh, facet_tags = make_three_core_mesh(
        radius, core_radius, data["centers"], mesh_size, MPI.COMM_WORLD)
    fields, interaction, matrix_diagnostics = solve_cell_basis(mesh, facet_tags, alpha)
    dipole = reconstruct_case(fields, interaction, data, "dipole",
                              young_modulus, poisson_ratio, mesh, facet_tags)
    edge = reconstruct_case(fields, interaction, data, "edge",
                            young_modulus, poisson_ratio, mesh, facet_tags)
    stress_difference = abs(dipole["stress_l2"]-edge["stress_l2"])
    # The norm of the field difference is assembled directly, not inferred
    # from the difference of norms.
    V = fields[0].function_space
    dipole_coeff = np.asarray(dipole["interaction_coefficients"])
    edge_coeff = np.asarray(edge["interaction_coefficients"])
    field_coefficients = np.stack([field.x.array.copy() for field in fields])
    from models.morandotti_cell_reconstruction import reconstruct_airy_potential
    v_d = fem.Function(V)
    v_e = fem.Function(V)
    v_d.x.array[:] = reconstruct_airy_potential(
        field_coefficients, dipole_coeff, young_modulus, poisson_ratio)
    v_e.x.array[:] = reconstruct_airy_potential(
        field_coefficients, edge_coeff, young_modulus, poisson_ratio)
    v_d.x.scatter_forward()
    v_e.x.scatter_forward()
    H_d, H_e = ufl.grad(ufl.grad(v_d)), ufl.grad(ufl.grad(v_e))
    sigma_d = ufl.as_matrix([[H_d[1, 1], -H_d[0, 1]],
                             [-H_d[1, 0], H_d[0, 0]]])
    sigma_e = ufl.as_matrix([[H_e[1, 1], -H_e[0, 1]],
                             [-H_e[1, 0], H_e[0, 0]]])
    E = float(young_modulus)
    nu = float(poisson_ratio)
    mu = E/(2.0*(1.0+nu))
    lam = E*nu/((1.0+nu)*(1.0-2.0*nu))
    def strain_from_stress(sigma):
        tr = sigma[0, 0]+sigma[1, 1]
        return (sigma-(lam/(2.0*(mu+lam)))*tr*ufl.Identity(2))/(2.0*mu)
    eps_d, eps_e = strain_from_stress(sigma_d), strain_from_stress(sigma_e)
    dx = ufl.Measure("dx", domain=mesh, metadata={"quadrature_degree": 9})
    stress_diff = np.sqrt(max(assemble(ufl.inner(sigma_d-sigma_e,
                                                  sigma_d-sigma_e)*dx, mesh), 0.0))
    strain_diff = np.sqrt(max(assemble(ufl.inner(eps_d-eps_e,
                                                  eps_d-eps_e)*dx, mesh), 0.0))
    energy_difference = abs(dipole["bulk_elastic_energy"]-
                            edge["bulk_elastic_energy"])
    return {
        "separation": separation, "core_radius": core_radius,
        "mesh_size_target": mesh_size,
        "mesh_to_core_ratio": float(mesh_size/core_radius),
        "frank_magnitude": omega,
        "burgers_vector_matched": data["burgers_vector"].tolist(),
        "global_moments_dipole": data["global_moments_dipole"].tolist(),
        "global_moments_edge": data["global_moments_edge"].tolist(),
        "global_moment_residual": float(np.linalg.norm(data["global_moment_residual"])),
        "local_source_vector_difference": float(
            np.linalg.norm(data["local_source_vector_difference"])),
        "matrix": matrix_diagnostics,
        "dipole": dipole,
        "edge": edge,
        "relative_stress_l2_difference": float(
            stress_diff/max(edge["stress_l2"], 1e-30)),
        "relative_strain_l2_difference": float(
            strain_diff/max(edge["strain_l2"], 1e-30)),
        "relative_bulk_energy_difference": float(
            energy_difference/max(abs(dipole["bulk_elastic_energy"]),
                                   abs(edge["bulk_elastic_energy"]), 1e-30)),
        "stress_norm_difference_only": float(stress_difference),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts/volterra_morandotti_c0_ipdg/report.json")
    parser.add_argument("--separations", nargs="+", type=float, default=[0.48])
    parser.add_argument("--core-radii", nargs="+", type=float, default=[0.06, 0.04, 0.03])
    parser.add_argument("--mesh-size-factors", nargs="+", type=float, default=[1.0, 0.75])
    parser.add_argument("--mesh-sizes", nargs="+", type=float, default=None,
                        help="optional absolute mesh sizes; overrides mesh-size-factors")
    parser.add_argument("--core-radius", type=float, default=None,
                        help="legacy single-radius option; overrides core-radii")
    parser.add_argument("--outer-radius", type=float, default=1.0)
    parser.add_argument("--frank-magnitude", type=float, default=0.01)
    parser.add_argument("--young-modulus", type=float, default=1.0)
    parser.add_argument("--poisson-ratio", type=float, default=0.0)
    parser.add_argument("--alpha", type=float, default=10.0)
    args = parser.parse_args()
    if not (-1.0 < args.poisson_ratio < 0.5):
        parser.error("poisson-ratio must lie in (-1, 1/2)")
    core_radii = [args.core_radius] if args.core_radius is not None else args.core_radii
    rows = []
    mesh_schedule = {}
    for separation in args.separations:
        for core_radius in core_radii:
            mesh_sizes = (args.mesh_sizes if args.mesh_sizes is not None else
                          [core_radius*factor for factor in args.mesh_size_factors])
            mesh_schedule[str(core_radius)] = [float(h) for h in mesh_sizes]
            for h in mesh_sizes:
                rows.append(solve_level(
                    separation, core_radius, h, args.alpha, args.outer_radius,
                    args.frank_magnitude, args.young_modulus, args.poisson_ratio))
    report = {
        "title": "Volterra dipole-to-edge: matched three-core P3 C0-IPDG benchmark",
        "status": "C0-IPDG computation; results must be taken from this run's artifact",
        "reference": "Cesana, Fabbrini, León Baldelli, Morandotti (2026), arXiv:2609.29614",
        "method": "three-core perforated disk; nine P3 C0-IPDG cell problems; shared interaction matrix for both defect configurations",
        "geometry": "outer disk with upper, lower and central circular cores; all three holes retained in both configurations",
        "constitutive_law": {
            "young_modulus": args.young_modulus,
            "poisson_ratio": args.poisson_ratio,
            "plane_strain": True,
        },
        "penalty_alpha": args.alpha,
        "core_radii": core_radii,
        "separations": args.separations,
        "mesh_schedule_by_core_radius": mesh_schedule,
        "mesh_size_factors": args.mesh_size_factors if args.mesh_sizes is None else None,
        "source_convention": {
            "dipole": "Frank +Omega at (0,+d/2), -Omega at (0,-d/2)",
            "edge": "Burgers b=(-Omega*d,0) at (0,0)",
            "moment_map": "Phi_i=(s_i, s_i*x_i+b_i,y, s_i*y_i-b_i,x)",
            "matching": "equal global Frank/Burgers first moments; local 3N source vectors remain distinct for d>0",
        },
        "energy_scope": "bulk elastic energy of reconstructed stress only; excludes singular-core renormalization and any additional core self-energy terms",
        "limitations": [
            "This is the bounded perforated-domain C0-IPDG benchmark, not a periodic Fourier solve on the same boundary-value problem.",
            "The same three-core geometry and interaction matrix are used for dipole and edge at each fixed (d,a,h); this isolates source-data effects within C0-IPDG.",
            "The Fourier periodic experiment remains a separate boundary-condition benchmark; direct cross-method error claims require a common domain and boundary formulation.",
            "No singular-core, Mosco, Gamma, or physical validation claim is made.",
        ],
        "results": rows,
    }
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({
        "rows": len(rows),
        "output": str(path),
        "maximum_global_moment_residual": max(r["global_moment_residual"] for r in rows),
        "maximum_relative_stress_difference": max(r["relative_stress_l2_difference"] for r in rows),
        "maximum_relative_energy_difference": max(r["relative_bulk_energy_difference"] for r in rows),
    }, indent=2))


if __name__ == "__main__":
    main()
