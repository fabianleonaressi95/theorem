#!/usr/bin/env python3
"""Two-core P3 C0-IPDG interaction-matrix audit.

DOLFINx 0.11 / Gmsh / PETSc-MUMPS. This is a controlled two-core extension
of the single-core cell benchmark: six cell fields, 6x6 interaction matrices.
It does not claim the paper's general arbitrary-N reconstruction.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
from mpi4py import MPI
from petsc4py import PETSc
import gmsh, ufl
from dolfinx import fem
from dolfinx.fem.petsc import LinearProblem
from dolfinx.io import gmsh as gmshio
from models.morandotti_cell_reconstruction import (
    build_defect_components, rotate_defect_vector_to_frame,
    defect_quadratic_decomposition, deformation_metric,
    solve_interaction_system, reconstruct_airy_potential,
    deform_two_core_coordinates, two_core_support_radius,
)


def make_mesh(R, a, centers, h, comm, random_seed=1):
    if comm.size != 1:
        raise RuntimeError("This first two-core audit is serial; MPI is not yet audited")
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
    gmsh.option.setNumber("Mesh.RandomSeed", int(random_seed))
    gmsh.model.add("two_core_annulus")
    outer = gmsh.model.occ.addDisk(0, 0, 0, R, R)
    holes = [gmsh.model.occ.addDisk(cx, cy, 0, a, a) for cx, cy in centers]
    surfaces, _ = gmsh.model.occ.cut([(2, outer)], [(2, q) for q in holes],
                                      removeObject=True, removeTool=True)
    gmsh.model.occ.synchronize()
    curves = gmsh.model.getBoundary(surfaces, combined=False, oriented=False)
    outer_curves, core_curves = [], [[] for _ in centers]
    for dim, tag in curves:
        if dim != 1:
            continue
        bb = gmsh.model.getBoundingBox(dim, tag)
        cx, cy = 0.5*(bb[0]+bb[3]), 0.5*(bb[1]+bb[4])
        extent = max(bb[3]-bb[0], bb[4]-bb[1])
        if extent > 0.5*R:
            outer_curves.append(tag)
        else:
            k = int(np.argmin([np.hypot(cx-x, cy-y) for x, y in centers]))
            core_curves[k].append(tag)
    if not outer_curves or any(not q for q in core_curves):
        gmsh.finalize()
        raise RuntimeError(f"Boundary classification failed: outer={outer_curves}, cores={core_curves}")
    gmsh.model.addPhysicalGroup(2, [tag for _, tag in surfaces], 10)
    gmsh.model.addPhysicalGroup(1, outer_curves, 1)
    for k, q in enumerate(core_curves):
        gmsh.model.addPhysicalGroup(1, q, 2+k)
    gmsh.option.setNumber("Mesh.MeshSizeMin", h)
    gmsh.option.setNumber("Mesh.MeshSizeMax", h)
    gmsh.option.setNumber("Mesh.ElementOrder", 3)
    gmsh.option.setNumber("Mesh.HighOrderOptimize", 2)
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(3)
    data = gmshio.model_to_mesh(gmsh.model, comm, 0, gdim=2)
    gmsh.finalize()
    return data.mesh, data.facet_tags


def assemble(expr, mesh):
    return mesh.comm.allreduce(fem.assemble_scalar(fem.form(expr)), op=MPI.SUM)


def solve_level(h, alpha=10.0, R=1.0, a=0.12, young_modulus=1.0, poisson_ratio=0.0,
                centers=((-0.28, 0.0), (0.28, 0.0)), orientation_angle_deg=0.0,
                rotate_defect_data=True, core_separation=None,
                args_artifact_path="cell_fields.npz", mesh_bundle=None,
                reference_geometry=None):
    comm = MPI.COMM_WORLD
    theta = np.deg2rad(float(orientation_angle_deg))
    rotation = np.array([[np.cos(theta), -np.sin(theta)],
                         [np.sin(theta),  np.cos(theta)]])
    reference_centers = np.asarray(centers, dtype=float)
    if core_separation is None:
        target_centers = reference_centers.copy()
    else:
        direction = (reference_centers[1]-reference_centers[0]) / np.linalg.norm(reference_centers[1]-reference_centers[0])
        midpoint = 0.5*(reference_centers[0]+reference_centers[1])
        target_centers = np.vstack((midpoint-0.5*float(core_separation)*direction,
                                    midpoint+0.5*float(core_separation)*direction))
    centers = tuple(tuple(q) for q in (target_centers @ rotation.T))
    axis = rotation @ np.array([1.0, 0.0])
    transverse_axis = rotation @ np.array([0.0, 1.0])
    # Generate the reference mesh once. Both orientation and distance studies
    # transform its coordinates in place and preserve the cell connectivity.
    if mesh_bundle is None:
        mesh, tags = make_mesh(R, a, tuple(tuple(q) for q in reference_centers), h, comm)
    else:
        mesh, tags = mesh_bundle
        if reference_geometry is None or reference_geometry.shape != mesh.geometry.x.shape:
            raise ValueError("a matching reference_geometry snapshot is required with mesh_bundle")
        mesh.geometry.x[:] = reference_geometry
    reference_separation = float(np.linalg.norm(reference_centers[1]-reference_centers[0]))
    effective_support_radius = two_core_support_radius(a, reference_separation, 0.50)
    jacobian_subdivisions = 12
    reference_points = np.asarray([
        (i / jacobian_subdivisions, j / jacobian_subdivisions)
        for i in range(jacobian_subdivisions + 1)
        for j in range(jacobian_subdivisions + 1 - i)
    ], dtype=np.float64)
    geometry_cells_local = np.arange(mesh.topology.index_map(mesh.topology.dim).size_local, dtype=np.int32)
    jacobian_expression = fem.Expression(ufl.Jacobian(mesh), reference_points, comm=comm)
    reference_jacobians = jacobian_expression.eval(mesh, geometry_cells_local)
    mesh.geometry.x[:, :2] = deform_two_core_coordinates(
        mesh.geometry.x[:, :2], reference_centers, target_centers, a, 0.50)
    if abs(orientation_angle_deg) > 1e-14:
        mesh.geometry.x[:, :2] = mesh.geometry.x[:, :2] @ rotation.T
    geometry_cells = np.asarray(mesh.geometry.dofmap)
    corner_xy = mesh.geometry.x[geometry_cells[:, :3], :2]
    signed_areas = 0.5*((corner_xy[:,1,0]-corner_xy[:,0,0])*(corner_xy[:,2,1]-corner_xy[:,0,1])
                        -(corner_xy[:,1,1]-corner_xy[:,0,1])*(corner_xy[:,2,0]-corner_xy[:,0,0]))
    min_signed_area = float(np.min(signed_areas))
    if not np.isfinite(min_signed_area) or min_signed_area <= 0.0:
        raise RuntimeError(f"Distance/orientation map inverted a corner triangle: min signed area={min_signed_area}")
    # Compare the current curved-element Jacobian with the paired reference
    # Jacobian at identical reference points. G=F^T F measures mesh-map stretch.
    current_jacobians = jacobian_expression.eval(mesh, geometry_cells_local)
    metric_data = deformation_metric(reference_jacobians, current_jacobians)
    sampled_jacobians = np.linalg.det(current_jacobians)
    min_sampled_jacobian = float(np.min(sampled_jacobians))
    metric_eigenvalues = metric_data["eigenvalues"]
    metric_anisotropy = metric_data["anisotropy"]
    metric_summary = {
        "definition": "F=J_current @ inv(J_reference); G=F.T @ F",
        "interpretation": "mesh-coordinate deformation metric; not a constitutive anisotropy or defect invariant",
        "sample_count": int(metric_anisotropy.size),
        "minimum_eigenvalue": float(np.min(metric_eigenvalues[..., 0])),
        "maximum_eigenvalue": float(np.max(metric_eigenvalues[..., 1])),
        "mean_anisotropy": float(np.mean(metric_anisotropy)),
        "p95_anisotropy": float(np.quantile(metric_anisotropy, 0.95)),
        "maximum_anisotropy": float(np.max(metric_anisotropy)),
    }
    if not np.isfinite(min_sampled_jacobian) or min_sampled_jacobian <= 0.0:
        raise RuntimeError(
            "Distance/orientation map has a non-positive sampled cubic-geometry Jacobian: "
            f"min det(J)={min_sampled_jacobian}"
        )
    mesh.topology.create_connectivity(mesh.topology.dim-1, mesh.topology.dim)
    V = fem.functionspace(mesh, ("Lagrange", 3))
    n = ufl.FacetNormal(mesh)
    hspace = fem.functionspace(mesh, ("DG", 0))
    cell_h = fem.Function(hspace)
    nc = mesh.topology.index_map(mesh.topology.dim).size_local
    cells = np.arange(nc, dtype=np.int32)
    cell_h.x.array[:] = mesh.h(mesh.topology.dim, cells)
    cell_h.x.scatter_forward()
    dx = ufl.Measure("dx", domain=mesh, metadata={"quadrature_degree": 9})
    ds = ufl.Measure("ds", domain=mesh, subdomain_data=tags,
                     metadata={"quadrature_degree": 9})
    dS = ufl.Measure("dS", domain=mesh, metadata={"quadrature_degree": 9})
    u, v = ufl.TrialFunction(V), ufl.TestFunction(V)
    Hu, Hv = ufl.grad(ufl.grad(u)), ufl.grad(ufl.grad(v))
    Hun, Hvn = ufl.dot(ufl.dot(Hu, n), n), ufl.dot(ufl.dot(Hv, n), n)
    ju, jv = ufl.jump(ufl.grad(u), n), ufl.jump(ufl.grad(v), n)
    A = (ufl.inner(Hu, Hv)*dx
         -(ju*ufl.avg(Hvn)+jv*ufl.avg(Hun))*dS
         -(ufl.dot(ufl.grad(u), n)*Hvn+ufl.dot(ufl.grad(v), n)*Hun)*ds
         +(alpha/ufl.avg(cell_h))*ju*jv*dS
         +(alpha/cell_h('+'))*ufl.dot(ufl.grad(u), n)*ufl.dot(ufl.grad(v), n)*ds)
    outer_dofs = fem.locate_dofs_topological(V, 1, tags.find(1))
    core_dofs_by_tag = [fem.locate_dofs_topological(V, 1, tags.find(2+k))
                        for k in range(len(centers))]
    all_core_dofs = np.unique(np.concatenate(core_dofs_by_tag))
    dof_xy = V.tabulate_dof_coordinates()[:, :2]
    zero = fem.Constant(mesh, PETSc.ScalarType(0.0))
    fields = []
    boundary_rows = []
    for core_idx, (cx, cy) in enumerate(centers):
        for mode in range(3):
            gd = fem.Function(V)
            gd.x.array[:] = 0.0
            dofs = core_dofs_by_tag[core_idx]
            if mode == 0:
                gd.x.array[dofs] = 1.0
                gn = ufl.as_ufl(0.0)
            elif mode == 1:
                gd.x.array[dofs] = dof_xy[dofs] @ axis
                gn = axis[0]*n[0] + axis[1]*n[1]
            else:
                gd.x.array[dofs] = dof_xy[dofs] @ transverse_axis
                gn = transverse_axis[0]*n[0] + transverse_axis[1]*n[1]
            gd.x.scatter_forward()
            bcs = [fem.dirichletbc(zero, outer_dofs, V),
                   fem.dirichletbc(gd, all_core_dofs)]
            tag = 2 + core_idx
            L = (-gn*Hvn + (alpha/cell_h('+'))*gn*ufl.dot(ufl.grad(v), n))*ds(tag) + zero*v*dx
            problem = LinearProblem(A, L, bcs=bcs,
                petsc_options_prefix=f"two_core_{core_idx}_{mode}_",
                petsc_options={"ksp_type":"preonly", "pc_type":"lu",
                               "pc_factor_mat_solver_type":"mumps"})
            uh = problem.solve()
            fields.append(uh)
            # Record value and normal-derivative residuals on every boundary
            # component, not only the active core. Inactive components carry
            # homogeneous data for this cell problem.
            xcoord = ufl.SpatialCoordinate(mesh)
            val_active = (1.0 if mode == 0 else
                (axis[0]*xcoord[0] + axis[1]*xcoord[1] if mode == 1 else
                 transverse_axis[0]*xcoord[0] + transverse_axis[1]*xcoord[1]))
            for boundary_tag, boundary_name in [(1, "outer"), (2, "core_0"), (3, "core_1")]:
                target_value = val_active if boundary_tag == tag else 0.0
                target_normal = gn if boundary_tag == tag else 0.0
                value_res = np.sqrt(max(assemble((uh-target_value)**2*ds(boundary_tag), mesh), 0.0))
                normal_res = np.sqrt(max(assemble((ufl.dot(ufl.grad(uh),n)-target_normal)**2*ds(boundary_tag), mesh), 0.0))
                boundary_rows.append({"active_core":core_idx,"mode":mode,
                    "boundary":boundary_name,"value_L2_residual":float(value_res),
                    "normal_derivative_L2_residual":float(normal_res)})
    m = len(fields)
    MH, ML, MB, MI = (np.zeros((m,m)) for _ in range(4))
    Hs = [ufl.grad(ufl.grad(q)) for q in fields]
    cof = [ufl.as_matrix([[H[1,1],-H[0,1]],[-H[1,0],H[0,0]]]) for H in Hs]
    for i in range(m):
        for j in range(m):
            MH[i,j] = assemble(ufl.inner(Hs[i],Hs[j])*dx, mesh)
            ML[i,j] = assemble(ufl.div(ufl.grad(fields[i]))*
                               ufl.div(ufl.grad(fields[j]))*dx, mesh)
            flux = ufl.dot(ufl.dot(cof[i],n),ufl.grad(fields[j]))
            MB[i,j] = assemble(flux*ds, mesh)
            fi = (ufl.dot(ufl.dot(cof[i]("+"),n("+")),ufl.grad(fields[j])("+"))
                  + ufl.dot(ufl.dot(cof[i]("-"),n("-")),ufl.grad(fields[j])("-")))
            MI[i,j] = assemble(fi*dS, mesh)
    MF = MB + MI
    rel = lambda X: float(np.linalg.norm(X-X.T, "fro")/max(np.linalg.norm(X,"fro"),1e-300))

    # Resolve the two-core interaction into the geometrically preferred
    # longitudinal/transverse frame. This quantifies anisotropy; it does not
    # by itself establish that anisotropy is the sole cause of any residual.
    frame = np.column_stack((axis, transverse_axis))
    matrix_anisotropy = {}
    for i in range(2):
        for j in range(2):
            block = ML[3*i+1:3*i+3, 3*j+1:3*j+3]
            local = frame.T @ block @ frame
            longitudinal, transverse = float(local[0, 0]), float(local[1, 1])
            denom = abs(longitudinal) + abs(transverse)
            matrix_anisotropy[f"core_{i}_to_core_{j}"] = {
                "longitudinal": longitudinal,
                "transverse": transverse,
                "signed_anisotropy": float((longitudinal-transverse)/denom) if denom else 0.0,
                "longitudinal_transverse_coupling": float(local[0, 1]),
                "transverse_longitudinal_coupling": float(local[1, 0]),
                "local_block": local.tolist(),
            }

    residual_anisotropy = {}
    residual_groups = {}
    for row in boundary_rows:
        if row["mode"] in (1, 2):
            key = (row["active_core"], row["boundary"])
            residual_groups.setdefault(key, {})[row["mode"]] = row["normal_derivative_L2_residual"]
    for (active_core, boundary_name), values in residual_groups.items():
        rx, ry = float(values.get(1, 0.0)), float(values.get(2, 0.0))
        denom = rx*rx + ry*ry
        residual_anisotropy[f"active_core_{active_core}_{boundary_name}"] = {
            "mode_longitudinal_normal_residual": rx,
            "mode_transverse_normal_residual": ry,
            "signed_directional_anisotropy": float((rx*rx-ry*ry)/denom) if denom else 0.0,
            "residual_ratio_longitudinal_over_transverse": float(rx/ry) if ry else None,
        }

    # The published finite-dimensional reconstruction uses the Laplacian
    # product matrix. Preserve the six actual FE coefficient vectors and the
    # mesh/dof metadata so a later run can reproduce the reconstructed field.
    field_coefficients = np.stack([q.x.array.copy() for q in fields])
    dof_coordinates = V.tabulate_dof_coordinates().copy()
    geometry_coordinates = mesh.geometry.x.copy()
    geometry_dofmap = np.asarray(mesh.geometry.dofmap).copy()
    cases = {
        "single_disclination_core_0": (np.array([0.2, 0.0]), np.zeros((2,2))),
        "single_edge_dislocation_core_1": (np.zeros(2), np.array([[0.0,0.0],[0.03,-0.04]])),
        "opposite_disclination_dipole": (np.array([0.2,-0.2]), np.zeros((2,2))),
        "mixed_disclination_dislocation": (np.array([0.2,0.0]), np.array([[0.0,0.0],[0.03,-0.04]])),
    }
    reconstruction = {}
    for name, (frank, burgers) in cases.items():
        # Rotate the Burgers vectors together with the two-core geometry.
        burgers_used = np.asarray(burgers) @ rotation.T if rotate_defect_data else np.asarray(burgers)
        phi_frank_global, phi_burgers_global, phi_global = build_defect_components(
            np.asarray(centers), frank, burgers_used)
        # Resolve the two source sectors independently in the FE translational frame.
        phi_frank = rotate_defect_vector_to_frame(phi_frank_global, rotation)
        phi_burgers = rotate_defect_vector_to_frame(phi_burgers_global, rotation)
        phi = phi_frank + phi_burgers
        source_quadratic = defect_quadratic_decomposition(ML, phi_frank, phi_burgers)
        coeff = solve_interaction_system(ML, phi)
        coeff_frank = solve_interaction_system(ML, phi_frank)
        coeff_burgers = solve_interaction_system(ML, phi_burgers)
        vh_dofs = reconstruct_airy_potential(field_coefficients, coeff, young_modulus, poisson_ratio)
        vh = fem.Function(V)
        vh.x.array[:] = vh_dofs
        vh.x.scatter_forward()
        Hv_case = ufl.grad(ufl.grad(vh))
        sigma_case = ufl.as_matrix([[Hv_case[1,1], -Hv_case[0,1]],
                                    [-Hv_case[1,0], Hv_case[0,0]]])
        vh_frank = fem.Function(V)
        vh_frank.x.array[:] = reconstruct_airy_potential(
            field_coefficients, coeff_frank, young_modulus, poisson_ratio)
        vh_frank.x.scatter_forward()
        vh_burgers = fem.Function(V)
        vh_burgers.x.array[:] = reconstruct_airy_potential(
            field_coefficients, coeff_burgers, young_modulus, poisson_ratio)
        vh_burgers.x.scatter_forward()
        Hf = ufl.grad(ufl.grad(vh_frank))
        Hb = ufl.grad(ufl.grad(vh_burgers))
        sigma_frank = ufl.as_matrix([[Hf[1,1], -Hf[0,1]], [-Hf[1,0], Hf[0,0]]])
        sigma_burgers = ufl.as_matrix([[Hb[1,1], -Hb[0,1]], [-Hb[1,0], Hb[0,0]]])

        def stress_second_moment(stress):
            return np.array([
                [assemble((stress[0,0]**2 + stress[1,0]**2)*dx, mesh),
                 assemble((stress[0,0]*stress[0,1] + stress[1,0]*stress[1,1])*dx, mesh)],
                [assemble((stress[0,0]*stress[0,1] + stress[1,0]*stress[1,1])*dx, mesh),
                 assemble((stress[0,1]**2 + stress[1,1]**2)*dx, mesh)]
            ], dtype=float)

        stress_moment_total = stress_second_moment(sigma_case)
        stress_moment_frank = stress_second_moment(sigma_frank)
        stress_moment_burgers = stress_second_moment(sigma_burgers)
        stress_moment_cross = stress_moment_total - stress_moment_frank - stress_moment_burgers

        def directional_stress_anisotropy(moment):
            local_moment = frame.T @ moment @ frame
            eigenvalues = np.linalg.eigvalsh(0.5*(local_moment + local_moment.T))
            value = float((eigenvalues[-1]-eigenvalues[0]) /
                          max(eigenvalues[-1]+eigenvalues[0], 1e-300))
            return local_moment, value

        stress_moment_local, stress_anisotropy = directional_stress_anisotropy(stress_moment_total)
        stress_moment_frank_local, stress_anisotropy_frank = directional_stress_anisotropy(stress_moment_frank)
        stress_moment_burgers_local, stress_anisotropy_burgers = directional_stress_anisotropy(stress_moment_burgers)
        stress_moment_cross_local = frame.T @ stress_moment_cross @ frame
        traction = ufl.dot(sigma_case, n)
        boundary_traction = {}
        for boundary_tag, boundary_name in [(1, "outer"), (2, "core_0"), (3, "core_1")]:
            boundary_traction[boundary_name] = float(np.sqrt(max(
                assemble(ufl.inner(traction, traction)*ds(boundary_tag), mesh), 0.0)))

        # Integrated force and moment on each core boundary. The normal is
        # UFL's outward normal of the material domain (therefore points into
        # each circular hole); this convention is stated in the report.
        xphys = ufl.SpatialCoordinate(mesh)
        core_resultants = {}
        for k, (cx, cy) in enumerate(centers):
            tag = 2 + k
            fx = assemble(traction[0]*ds(tag), mesh)
            fy = assemble(traction[1]*ds(tag), mesh)
            moment = assemble(((xphys[0]-cx)*traction[1]
                               -(xphys[1]-cy)*traction[0])*ds(tag), mesh)
            core_resultants[f"core_{k}"] = {
                "force_x_domain_normal": float(fx),
                "force_y_domain_normal": float(fy),
                "moment_z_domain_normal": float(moment),
                "force_norm": float(np.hypot(fx, fy)),
                "force_longitudinal": float(fx*axis[0] + fy*axis[1]),
                "force_transverse": float(-fx*axis[1] + fy*axis[0]),
                "force_directional_anisotropy": float(((fx*axis[0]+fy*axis[1])**2-(-fx*axis[1]+fy*axis[0])**2) /
                    max((fx*axis[0]+fy*axis[1])**2+(-fx*axis[1]+fy*axis[0])**2, 1e-300)),
            }

        # Decompose the interior-facet traction jump into Frank, Burgers,
        # and their signed cross contribution. With UFL's jump convention,
        # each term is a physical vector on the interior facet.
        jump_frank = ufl.jump(sigma_frank, n)
        jump_burgers = ufl.jump(sigma_burgers, n)
        jump_total = ufl.jump(sigma_case, n)
        def facet_vector_second_moment(vector):
            return np.array([
                [assemble(vector[0]*vector[0]*dS, mesh),
                 assemble(vector[0]*vector[1]*dS, mesh)],
                [assemble(vector[1]*vector[0]*dS, mesh),
                 assemble(vector[1]*vector[1]*dS, mesh)]
            ], dtype=float)

        jump_moment_total = facet_vector_second_moment(jump_total)
        jump_moment_frank = facet_vector_second_moment(jump_frank)
        jump_moment_burgers = facet_vector_second_moment(jump_burgers)
        jump_moment_cross = jump_moment_total - jump_moment_frank - jump_moment_burgers
        jump_frank_sq = float(assemble(ufl.inner(jump_frank, jump_frank)*dS, mesh))
        jump_burgers_sq = float(assemble(ufl.inner(jump_burgers, jump_burgers)*dS, mesh))
        jump_total_sq = float(assemble(ufl.inner(jump_total, jump_total)*dS, mesh))
        # Assemble the mixed term independently (rather than obtaining it
        # by subtraction), so the additivity residual is a genuine check.
        jump_cross_term = float(2.0 * assemble(
            ufl.inner(jump_frank, jump_burgers)*dS, mesh))
        jump_additivity_residual = float(
            jump_total_sq - jump_frank_sq - jump_burgers_sq - jump_cross_term)
        jump_moment_local = frame.T @ jump_moment_total @ frame
        jump_moment_cross_local = frame.T @ jump_moment_cross @ frame
        jump_eigenvalues = np.linalg.eigvalsh(0.5*(jump_moment_local + jump_moment_local.T))
        jump_directional_anisotropy = float(
            (jump_eigenvalues[-1]-jump_eigenvalues[0]) /
            max(jump_eigenvalues[-1]+jump_eigenvalues[0], 1e-300))
        interior_traction_jump = float(np.sqrt(max(jump_total_sq, 0.0)))
        interior_traction_jump_frank = float(np.sqrt(max(jump_frank_sq, 0.0)))
        interior_traction_jump_burgers = float(np.sqrt(max(jump_burgers_sq, 0.0)))
        reconstruction[name] = {
            "Phi": phi.tolist(), "Phi_global_xy": phi_global.tolist(),
            "Phi_frank_local": phi_frank.tolist(),
            "Phi_burgers_local": phi_burgers.tolist(),
            "source_quadratic_decomposition": source_quadratic,
            "stress_second_moment_total_xy": stress_moment_total.tolist(),
            "stress_second_moment_frank_xy": stress_moment_frank.tolist(),
            "stress_second_moment_burgers_xy": stress_moment_burgers.tolist(),
            "stress_second_moment_cross_xy": stress_moment_cross.tolist(),
            "stress_second_moment_total_local": stress_moment_local.tolist(),
            "stress_second_moment_frank_local": stress_moment_frank_local.tolist(),
            "stress_second_moment_burgers_local": stress_moment_burgers_local.tolist(),
            "stress_second_moment_cross_local": stress_moment_cross_local.tolist(),
            "stress_directional_anisotropy": stress_anisotropy,
            "stress_directional_anisotropy_frank": stress_anisotropy_frank,
            "stress_directional_anisotropy_burgers": stress_anisotropy_burgers,
            "coefficients": coeff.tolist(),
            "linear_system_residual": float(np.linalg.norm(ML @ coeff - phi)),
            "airy_dof_values": vh_dofs.tolist(),
            "boundary_traction_L2": boundary_traction,
            "core_traction_resultants": core_resultants,
            "traction_normal_convention": "outward normal of material domain; points into each core hole",
            "interior_facet_traction_jump_L2": interior_traction_jump,
            "interior_facet_traction_jump_frank_L2": interior_traction_jump_frank,
            "interior_facet_traction_jump_burgers_L2": interior_traction_jump_burgers,
            "interior_facet_traction_jump_squared_decomposition": {
                "frank_squared": jump_frank_sq,
                "burgers_squared": jump_burgers_sq,
                "mixed_cross_term": jump_cross_term,
                "total_squared": jump_total_sq,
                "additivity_residual": jump_additivity_residual,
            },
            "interior_facet_traction_jump_second_moment_total_xy": jump_moment_total.tolist(),
            "interior_facet_traction_jump_second_moment_frank_xy": jump_moment_frank.tolist(),
            "interior_facet_traction_jump_second_moment_burgers_xy": jump_moment_burgers.tolist(),
            "interior_facet_traction_jump_second_moment_cross_xy": jump_moment_cross.tolist(),
            "interior_facet_traction_jump_second_moment_total_local": jump_moment_local.tolist(),
            "interior_facet_traction_jump_second_moment_cross_local": jump_moment_cross_local.tolist(),
            "interior_facet_traction_jump_directional_anisotropy": jump_directional_anisotropy,
        }
    npz_path = Path(args_artifact_path)
    npz_path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(npz_path, field_coefficients=field_coefficients,
        dof_coordinates=dof_coordinates, geometry_coordinates=geometry_coordinates,
        geometry_dofmap=geometry_dofmap, M_laplacian=ML, M_hessian=MH,
        M_boundary_flux=MB, M_interior_facet_flux=MI,
        centers=np.asarray(centers), core_radius=np.asarray([a]),
        mesh_target_h=np.asarray([h]), cell_count=np.asarray([nc]))
    return {"h_target":h,"core_separation":float(np.linalg.norm(np.asarray(centers[1])-np.asarray(centers[0]))),
        "min_signed_corner_area":min_signed_area,
        "min_sampled_jacobian_determinant":min_sampled_jacobian,
        "jacobian_sampling_subdivisions":jacobian_subdivisions,
        "deformation_metric":metric_summary,
        "effective_support_radius":effective_support_radius,
        "orientation_angle_deg":float(orientation_angle_deg),
        "defect_data_co_rotated":bool(rotate_defect_data),
        "cells":int(nc),"dofs":int(V.dofmap.index_map.size_global),
        "cores":[{"center":list(c),"radius":a} for c in centers],
        "cell_fields":len(fields),"interaction_dimension":[m,m],
        "boundary_residuals":boundary_rows,"reconstruction_cases":reconstruction,
        "field_export":str(npz_path),
        "M_hessian":MH.tolist(),"M_laplacian":ML.tolist(),
        "M_boundary_flux":MB.tolist(),"M_interior_facet_flux":MI.tolist(),
        "boundary_identity_relative_residual":float(np.linalg.norm((ML-MH)-MF,"fro")/max(np.linalg.norm(MH,"fro"),1e-300)),
        "hessian_symmetry_relative":rel(MH),"laplacian_symmetry_relative":rel(ML),
        "total_flux_symmetry_relative":rel(MF),
        "min_eigenvalue_hessian":float(np.linalg.eigvalsh(MH).min()),
        "min_eigenvalue_laplacian":float(np.linalg.eigvalsh(ML).min()),
        "condition_hessian":float(np.linalg.cond(MH)),
        "condition_laplacian":float(np.linalg.cond(ML)),
        "anisotropy": {
            "definition": "longitudinal/transverse frame aligned with the center-to-center axis",
            "axis_unit_vector": axis.tolist(),
            "matrix_blocks": matrix_anisotropy,
            "normal_derivative_residuals": residual_anisotropy,
        }}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mesh-sizes",nargs="+",type=float,default=[0.24,0.16,0.11])
    p.add_argument("--alpha",type=float,default=10.0)
    p.add_argument("--young-modulus",type=float,default=1.0)
    p.add_argument("--poisson-ratio",type=float,default=0.0)
    p.add_argument("--orientation-angles-deg",nargs="+",type=float,default=[0.0,30.0,60.0])
    p.add_argument("--orientation-mesh-size",type=float,default=0.06)
    p.add_argument("--distance-values",nargs="+",type=float,default=[0.48,0.56,0.64,0.72])
    p.add_argument("--distance-mesh-size",type=float,default=0.06)
    p.add_argument("--out",default="artifacts/morandotti_two_core/report.json")
    a=p.parse_args()
    if (not np.isfinite(a.distance_mesh_size) or a.distance_mesh_size <= 0.0):
        raise ValueError("--distance-mesh-size must be finite and positive")
    if (not np.isfinite(a.distance_values).all()
            or any(d <= 2.0*0.12 or d >= 2.0*(1.0-0.12) for d in a.distance_values)):
        raise ValueError("distance values must be finite and satisfy 2a < d < 2(R-a), with R=1 and a=0.12")
    if any(b <= aa for aa, b in zip(a.distance_values, a.distance_values[1:])):
        raise ValueError("--distance-values must be strictly increasing and contain no duplicates")
    levels=[solve_level(h,alpha=a.alpha,young_modulus=a.young_modulus,poisson_ratio=a.poisson_ratio,args_artifact_path=str(Path(a.out).with_name(f"cell_fields_h{h:.4f}.npz"))) for h in a.mesh_sizes]
    def orientation_sweep(co_rotate_defects, label):
        sweep=[]
        for angle in a.orientation_angles_deg:
            if (abs(angle) < 1e-12 and abs(a.orientation_mesh_size-a.mesh_sizes[-1]) < 1e-12
                    and co_rotate_defects):
                sweep.append(levels[-1])
            else:
                sweep.append(solve_level(
                    a.orientation_mesh_size, alpha=a.alpha, young_modulus=a.young_modulus,
                    poisson_ratio=a.poisson_ratio, orientation_angle_deg=angle,
                    rotate_defect_data=co_rotate_defects,
                    args_artifact_path=str(Path(a.out).with_name(
                        f"orientation_{label}_{angle:g}_deg_fields.npz"))))
        base=sweep[0]
        comparisons=[]
        for level in sweep:
            base_matrix=np.asarray(base["M_laplacian"])
            matrix=np.asarray(level["M_laplacian"])
            matrix_rel=float(np.linalg.norm(matrix-base_matrix,"fro")/max(np.linalg.norm(base_matrix,"fro"),1e-300))
            base_res=base["anisotropy"]["normal_derivative_residuals"]
            cur_res=level["anisotropy"]["normal_derivative_residuals"]
            residual_rel={}
            for key,values in cur_res.items():
                ref=base_res[key]
                v=np.array([values["mode_longitudinal_normal_residual"],values["mode_transverse_normal_residual"]])
                v0=np.array([ref["mode_longitudinal_normal_residual"],ref["mode_transverse_normal_residual"]])
                residual_rel[key]=float(np.linalg.norm(v-v0)/max(np.linalg.norm(v0),1e-300))
            traction_covariance={}
            for case,case_data in level["reconstruction_cases"].items():
                traction_covariance[case]={}
                for core,force in case_data["core_traction_resultants"].items():
                    traction_covariance[case][core]={
                        "force_longitudinal":force["force_longitudinal"],
                        "force_transverse":force["force_transverse"],
                        "force_directional_anisotropy":force["force_directional_anisotropy"],
                    }
            comparisons.append({
                "angle_deg":level["orientation_angle_deg"],
                "local_interaction_matrix_relative_difference_from_first":matrix_rel,
                "directional_residual_relative_difference_by_boundary":residual_rel,
                "core_traction_components_by_case":traction_covariance,
            })
        return {"defect_orientation":label,"comparisons":comparisons}

    # Experiment A: rotate geometry and Burgers vectors together.
    # Experiment B: rotate geometry only; keep Burgers vectors fixed in lab axes.
    orientation_covariance=[
        orientation_sweep(True,"co_rotated"),
        orientation_sweep(False,"defects_fixed_in_lab_frame"),
    ]

    # Build one reference mesh and reuse that exact mesh object/connectivity.
    distance_reference_mesh_bundle = make_mesh(1.0, 0.12,
        ((-0.28, 0.0), (0.28, 0.0)), a.distance_mesh_size, MPI.COMM_WORLD)
    distance_reference_mesh = distance_reference_mesh_bundle[0]
    distance_reference_geometry = distance_reference_mesh.geometry.x.copy()
    distance_reference_separation = 0.56
    distance_effective_support_radius = two_core_support_radius(0.12,
        distance_reference_separation, 0.50)
    import hashlib
    distance_geometry_dofmap_sha256 = hashlib.sha256(
        np.asarray(distance_reference_mesh.geometry.dofmap).tobytes()).hexdigest()
    # Same mesh object, material, core radius and laboratory-fixed defect data.
    distance_sweep=[]
    for distance in a.distance_values:
        if distance <= 2.0*0.12:
            raise ValueError("every core separation must exceed twice the core radius")
        level=solve_level(a.distance_mesh_size, alpha=a.alpha,
            young_modulus=a.young_modulus, poisson_ratio=a.poisson_ratio,
            core_separation=distance,
            mesh_bundle=distance_reference_mesh_bundle,
            reference_geometry=distance_reference_geometry,
            args_artifact_path=str(Path(a.out).with_name(f"distance_{distance:g}_fields.npz")))
        M=np.asarray(level["M_laplacian"])
        cross=M[1:3,4:6]
        self_block=M[1:3,1:3]
        frame=np.column_stack((np.array([1.0,0.0]),np.array([0.0,1.0])))
        local=frame.T @ cross @ frame
        m_parallel,m_transverse=float(local[0,0]),float(local[1,1])
        denom=abs(m_parallel)+abs(m_transverse)
        anisotropy=float((m_parallel-m_transverse)/denom) if denom else 0.0
        distance_sweep.append({
            "core_separation":float(distance),"edge_gap":float(distance-2.0*0.12),
            "h_target":float(a.distance_mesh_size),"cells":level["cells"],"dofs":level["dofs"],
            "min_signed_corner_area":level["min_signed_corner_area"],
            "min_sampled_jacobian_determinant":level["min_sampled_jacobian_determinant"],
            "jacobian_sampling_subdivisions":level["jacobian_sampling_subdivisions"],
            "effective_support_radius":level["effective_support_radius"],
            "M_parallel_01":m_parallel,"M_transverse_01":m_transverse,
            "signed_anisotropy_A_d":anisotropy,
            "longitudinal_transverse_coupling_01":float(local[0,1]),
            "transverse_longitudinal_coupling_01":float(local[1,0]),
            "cross_block_frobenius":float(np.linalg.norm(cross,"fro")),
            "self_block_frobenius_core0":float(np.linalg.norm(self_block,"fro")),
            "normalized_coupling_C_d":float(np.linalg.norm(cross,"fro")/max(np.linalg.norm(self_block,"fro"),1e-300)),
            "ratio_M_parallel_over_transverse":float(m_parallel/m_transverse) if abs(m_transverse)>1e-14 else None,
            "core_traction_resultants_by_case":{
                name:case["core_traction_resultants"]
                for name,case in level["reconstruction_cases"].items()},
        })
    report={"title":"Two-core P3 C0-IPDG interaction matrix audit",
        "reference":"Cesana, Fabbrini, León Baldelli, Morandotti (2026), arXiv:2609.29614",
        "status":"two circular cores; six P3 cell fields; serial MPI; numerical audit with algebraic Airy reconstruction",
        "material":{"young_modulus":a.young_modulus,"poisson_ratio":a.poisson_ratio},
        "limitations":["only two equal circular cores in a fixed outer disk",
          "no analytic off-centre cell-field error available",
          "traction resultants are integrated diagnostics; equilibrium interpretation still requires convergence and boundary-condition validation",
          "circulation is not computed: the static Airy stress potential does not define a velocity field",
          "not the arbitrary-N production reconstruction",
          "no singular-core limit, dynamics or material calibration"],
        "convergence": [
          {
            "from_h": levels[i-1]["h_target"],
            "to_h": levels[i]["h_target"],
            "relative_M_laplacian_change": float(np.linalg.norm(np.asarray(levels[i]["M_laplacian"])-np.asarray(levels[i-1]["M_laplacian"]), "fro") / max(np.linalg.norm(np.asarray(levels[i]["M_laplacian"]), "fro"), 1e-300)),
            "relative_M_hessian_change": float(np.linalg.norm(np.asarray(levels[i]["M_hessian"])-np.asarray(levels[i-1]["M_hessian"]), "fro") / max(np.linalg.norm(np.asarray(levels[i]["M_hessian"]), "fro"), 1e-300)),
            "traction_jump_relative_change_by_case": {
              name: float(abs(levels[i]["reconstruction_cases"][name]["interior_facet_traction_jump_L2"]-levels[i-1]["reconstruction_cases"][name]["interior_facet_traction_jump_L2"]) / max(abs(levels[i]["reconstruction_cases"][name]["interior_facet_traction_jump_L2"]), 1e-300))
              for name in levels[i]["reconstruction_cases"]
            }
          } for i in range(1, len(levels))
        ],
        "levels":levels,
        "distance_sweep": {
            "protocol":"one reference mesh object and geometry-DOF map reused; reference coordinates restored before each compactly supported deformation; fixed core radius, material and source orientation",
            "reference_separation":distance_reference_separation,
            "maximum_support_radius":0.50,
            "effective_support_radius":distance_effective_support_radius,
            "reference_mesh_reused":True,
            "geometry_dofmap_sha256":distance_geometry_dofmap_sha256,
            "mesh_size":a.distance_mesh_size,"separations":a.distance_values,
            "definition_A_d":"(M_parallel_01-M_transverse_01)/(|M_parallel_01|+|M_transverse_01|)",
            "definition_C_d":"||M_01||_F/||M_00||_F",
            "results":distance_sweep,
            "limitations":["distance sweep is initially performed at one mesh size; the existing three-level benchmark is at the reference separation", "cubic-geometry Jacobian is sampled on a 12-subdivision barycentric lattice; positive samples are not a formal all-points positivity certificate", "fit candidate decay laws only after mesh-refinement and mapping-quality checks"]
        },
        "orientation_covariance": {
            "protocol":"two sweeps: co-rotate core centres and Burgers vectors; then rotate core centres only while holding Burgers vectors fixed in laboratory coordinates; resolve modes in the co-rotating frame",
            "mesh_size":a.orientation_mesh_size,
            "angles_deg":a.orientation_angles_deg,
            "comparisons":orientation_covariance,
            "interpretation":"same reference mesh connectivity is rotated in place, so covariance differences isolate numerical transformation/geometry effects rather than angle-dependent remeshing",
        }}
    path=Path(a.out); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
