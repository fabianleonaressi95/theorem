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


def make_mesh(R, a, centers, h, comm):
    if comm.size != 1:
        raise RuntimeError("This first two-core audit is serial; MPI is not yet audited")
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
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


def solve_level(h, alpha=10.0, R=1.0, a=0.12,
                centers=((-0.28, 0.0), (0.28, 0.0))):
    comm = MPI.COMM_WORLD
    mesh, tags = make_mesh(R, a, centers, h, comm)
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
                gd.x.array[dofs] = dof_xy[dofs, 0]
                gn = n[0]
            else:
                gd.x.array[dofs] = dof_xy[dofs, 1]
                gn = n[1]
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
            val = 1.0 if mode == 0 else (ufl.SpatialCoordinate(mesh)[0] if mode == 1
                                         else ufl.SpatialCoordinate(mesh)[1])
            value_res = np.sqrt(max(assemble((uh-val)**2*ds(tag), mesh), 0.0))
            normal_target = gn
            normal_res = np.sqrt(max(assemble((ufl.dot(ufl.grad(uh),n)-normal_target)**2*ds(tag),mesh),0.0))
            boundary_rows.append({"core":core_idx,"mode":mode,
                                  "core_value_L2_residual":float(value_res),
                                  "active_core_normal_L2_residual":float(normal_res)})
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
    return {"h_target":h,"cells":int(nc),"dofs":int(V.dofmap.index_map.size_global),
        "cores":[{"center":list(c),"radius":a} for c in centers],
        "cell_fields":len(fields),"interaction_dimension":[m,m],
        "boundary_residuals":boundary_rows,
        "M_hessian":MH.tolist(),"M_laplacian":ML.tolist(),
        "M_boundary_flux":MB.tolist(),"M_interior_facet_flux":MI.tolist(),
        "boundary_identity_relative_residual":float(np.linalg.norm((ML-MH)-MF,"fro")/max(np.linalg.norm(MH,"fro"),1e-300)),
        "hessian_symmetry_relative":rel(MH),"laplacian_symmetry_relative":rel(ML),
        "total_flux_symmetry_relative":rel(MF),
        "min_eigenvalue_hessian":float(np.linalg.eigvalsh(MH).min()),
        "min_eigenvalue_laplacian":float(np.linalg.eigvalsh(ML).min()),
        "condition_hessian":float(np.linalg.cond(MH)),
        "condition_laplacian":float(np.linalg.cond(ML))}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mesh-sizes",nargs="+",type=float,default=[0.24,0.16,0.11])
    p.add_argument("--alpha",type=float,default=10.0)
    p.add_argument("--out",default="artifacts/morandotti_two_core/report.json")
    a=p.parse_args()
    levels=[solve_level(h,alpha=a.alpha) for h in a.mesh_sizes]
    report={"title":"Two-core P3 C0-IPDG interaction matrix audit",
        "reference":"Cesana, Fabbrini, León Baldelli, Morandotti (2026), arXiv:2609.29614",
        "status":"two circular cores; six P3 cell fields; serial MPI; numerical audit",
        "limitations":["only two equal circular cores in a fixed outer disk",
          "no analytic off-centre cell-field error available",
          "not the arbitrary-N production reconstruction",
          "no singular-core limit, dynamics or material calibration"],
        "levels":levels}
    path=Path(a.out); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
