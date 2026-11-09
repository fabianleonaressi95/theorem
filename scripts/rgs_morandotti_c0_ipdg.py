#!/usr/bin/env python3
"""Single-core P3 C0-IPDG reproduction driver for the Morandotti Airy cell problems.

Requires DOLFINx 0.11, Gmsh Python bindings and PETSc/MUMPS. The driver is
intentionally separate from the lightweight NumPy/SciPy CI workflow.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from mpi4py import MPI
from petsc4py import PETSc
import gmsh
import ufl
from dolfinx import fem
from dolfinx.fem.petsc import LinearProblem
from dolfinx.io import gmshio


def radial_coefficients(a: float, R: float, mode: int) -> np.ndarray:
    if mode == 0:
        def trace(r):
            return (np.array([1., np.log(r), r*r, r*r*np.log(r)]),
                    np.array([0., 1/r, 2*r, 2*r*np.log(r)+r]))
        rhs=np.array([1.,0.,0.,0.])
    else:
        def trace(r):
            return (np.array([r,1/r,r**3,r*np.log(r)]),
                    np.array([1.,-1/r**2,3*r*r,np.log(r)+1]))
        rhs=np.array([a,1.,0.,0.])
    fa,pa=trace(a); fR,pR=trace(R)
    return np.linalg.solve(np.vstack((fa,pa,fR,pR)),rhs)


def exact_cell_expression(x, a: float, R: float, mode: int):
    r=ufl.sqrt(x[0]**2+x[1]**2)
    c=radial_coefficients(a,R,0 if mode==0 else 1)
    if mode==0:
        return c[0]+c[1]*ufl.ln(r)+c[2]*r**2+c[3]*r**2*ufl.ln(r)
    radial=c[0]*r+c[1]/r+c[2]*r**3+c[3]*r*ufl.ln(r)
    return radial*x[0]/r if mode==1 else radial*x[1]/r


def make_annulus_mesh(R: float, a: float, h: float, comm):
    if comm.size != 1:
        raise RuntimeError("The initial reproduction gate is serial; MPI parallelism is not yet audited")
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
    gmsh.model.add("single_core_annulus")
    outer=gmsh.model.occ.addDisk(0,0,0,R,R)
    inner=gmsh.model.occ.addDisk(0,0,0,a,a)
    surfaces,_=gmsh.model.occ.cut([(2,outer)],[(2,inner)],removeObject=True,removeTool=True)
    gmsh.model.occ.synchronize()
    curves=gmsh.model.getBoundary(surfaces,combined=False,oriented=False)
    outer_curves=[]; inner_curves=[]
    for dim,tag in curves:
        if dim != 1: continue
        bb=gmsh.model.getBoundingBox(dim,tag)
        extent=max(abs(bb[0]),abs(bb[1]),abs(bb[3]),abs(bb[4]))
        (outer_curves if extent>(R+a)/2 else inner_curves).append(tag)
    if not outer_curves or not inner_curves:
        gmsh.finalize()
        raise RuntimeError("Could not classify outer and core circular boundaries")
    gmsh.model.addPhysicalGroup(2,[tag for _,tag in surfaces],10)
    gmsh.model.addPhysicalGroup(1,outer_curves,1)
    gmsh.model.addPhysicalGroup(1,inner_curves,2)
    gmsh.option.setNumber("Mesh.MeshSizeMin",h)
    gmsh.option.setNumber("Mesh.MeshSizeMax",h)
    gmsh.option.setNumber("Mesh.ElementOrder",3)
    gmsh.option.setNumber("Mesh.HighOrderOptimize",2)
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(3)
    data=gmshio.model_to_mesh(gmsh.model,comm,0,gdim=2)
    gmsh.finalize()
    return data.mesh,data.facet_tags


def assemble_scalar(expr, mesh):
    return mesh.comm.allreduce(fem.assemble_scalar(fem.form(expr)),op=MPI.SUM)


def solve_level(h: float, R: float=1.0, a: float=0.2, alpha: float=10.0):
    comm=MPI.COMM_WORLD
    mesh,facet_tags=make_annulus_mesh(R,a,h,comm)
    mesh.topology.create_connectivity(mesh.topology.dim-1,mesh.topology.dim)
    V=fem.functionspace(mesh,("Lagrange",3))
    n=ufl.FacetNormal(mesh); cell_h=ufl.CellDiameter(mesh)
    dx=ufl.Measure("dx",domain=mesh,metadata={"quadrature_degree":9})
    ds=ufl.Measure("ds",domain=mesh,subdomain_data=facet_tags,metadata={"quadrature_degree":9})
    dS=ufl.Measure("dS",domain=mesh,metadata={"quadrature_degree":9})
    u=ufl.TrialFunction(V); v=ufl.TestFunction(V)
    Hu=ufl.grad(ufl.grad(u)); Hv=ufl.grad(ufl.grad(v))
    Hun=ufl.dot(ufl.dot(Hu,n),n); Hvn=ufl.dot(ufl.dot(Hv,n),n)
    j_u=ufl.jump(ufl.grad(u),n); j_v=ufl.jump(ufl.grad(v),n)
    a_form=(ufl.inner(Hu,Hv)*dx
        -(j_u*ufl.avg(Hvn)+j_v*ufl.avg(Hun))*dS
        -(ufl.dot(ufl.grad(u),n)*Hvn+ufl.dot(ufl.grad(v),n)*Hun)*ds
        +(alpha/ufl.avg(cell_h))*j_u*j_v*dS
        +(alpha/cell_h)*ufl.dot(ufl.grad(u),n)*ufl.dot(ufl.grad(v),n)*ds)
    outer_facets=facet_tags.find(1); core_facets=facet_tags.find(2)
    outer_dofs=fem.locate_dofs_topological(V,1,outer_facets)
    core_dofs=fem.locate_dofs_topological(V,1,core_facets)
    x=ufl.SpatialCoordinate(mesh)
    results=[]; fields=[]
    for mode in range(3):
        if mode==0:
            gD=fem.Constant(mesh,PETSc.ScalarType(1.0))
            gN=ufl.as_ufl(0.0)
        elif mode==1:
            gD=fem.Function(V); gD.interpolate(lambda X:X[0])
            gN=n[0]
        else:
            gD=fem.Function(V); gD.interpolate(lambda X:X[1])
            gN=n[1]
        zero=fem.Constant(mesh,PETSc.ScalarType(0.0))
        bcs=[fem.dirichletbc(zero,outer_dofs,V),
             fem.dirichletbc(gD,core_dofs)]
        L=(-gN*Hvn+(alpha/cell_h)*gN*ufl.dot(ufl.grad(v),n))*ds(2)
        problem=LinearProblem(a_form,L,bcs=bcs,
            petsc_options={"ksp_type":"preonly","pc_type":"lu",
                           "pc_factor_mat_solver_type":"mumps"})
        uh=problem.solve(); fields.append(uh)
        exact=exact_cell_expression(x,a,R,mode)
        errH=assemble_scalar(ufl.inner(ufl.grad(ufl.grad(uh-exact)),
                                       ufl.grad(ufl.grad(uh-exact)))*dx,mesh)
        normH=assemble_scalar(ufl.inner(ufl.grad(ufl.grad(exact)),
                                        ufl.grad(ufl.grad(exact)))*dx,mesh)
        val_expr=1.0 if mode==0 else (x[0] if mode==1 else x[1])
        val_res=np.sqrt(max(assemble_scalar((uh-val_expr)**2*ds(2),mesh),0.0))
        normal_res=np.sqrt(max(assemble_scalar((ufl.dot(ufl.grad(uh),n)-gN)**2*ds(2),mesh),0.0))
        results.append({"mode":mode,"relative_H2_seminorm_error":float(np.sqrt(errH/max(normH,1e-300))),
                        "core_value_L2_residual":float(val_res),
                        "core_normal_derivative_L2_residual":float(normal_res),
                        "hessian_energy":float(assemble_scalar(0.5*ufl.inner(ufl.grad(ufl.grad(uh)),ufl.grad(ufl.grad(uh)))*dx,mesh))})
    MH=np.zeros((3,3)); ML=np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            MH[i,j]=assemble_scalar(ufl.inner(ufl.grad(ufl.grad(fields[i])),
                                                ufl.grad(ufl.grad(fields[j])))*dx,mesh)
            ML[i,j]=assemble_scalar(ufl.div(ufl.grad(fields[i]))*
                                     ufl.div(ufl.grad(fields[j]))*dx,mesh)
    rel=np.linalg.norm(MH-ML,"fro")/max(np.linalg.norm(MH,"fro"),1e-300)
    report={"h_target":h,"num_cells":int(mesh.topology.index_map(2).size_local),
        "num_vertices":int(mesh.topology.index_map(0).size_local),
        "polynomial_degree":3,"penalty_alpha":alpha,"cell_problems":results,
        "M_hessian":MH.tolist(),"M_laplacian":ML.tolist(),
        "relative_matrix_difference":float(rel),
        "symmetry_residual_hessian":float(np.linalg.norm(MH-MH.T)),
        "symmetry_residual_laplacian":float(np.linalg.norm(ML-ML.T)),
        "min_eigenvalue_hessian":float(np.linalg.eigvalsh(MH).min()),
        "min_eigenvalue_laplacian":float(np.linalg.eigvalsh(ML).min()),
        "condition_number_hessian":float(np.linalg.cond(MH)),
        "condition_number_laplacian":float(np.linalg.cond(ML))}
    return report


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",default="artifacts/morandotti_c0_ipdg/report.json")
    parser.add_argument("--mesh-sizes",nargs="+",type=float,default=[0.22,0.14,0.09])
    parser.add_argument("--alpha",type=float,default=10.0)
    args=parser.parse_args()
    reports=[solve_level(h,alpha=args.alpha) for h in args.mesh_sizes]
    payload={"title":"Single-core annulus P3 C0-IPDG cell-problem reproduction",
        "reference":"Cesana, Fabbrini, León Baldelli, Morandotti (2026), arXiv:2609.29614",
        "status":"executed DOLFINx P3 C0-IPDG; single circular core; serial MPI",
        "operator":"source-matched Hessian volume, symmetric interior/boundary consistency, alpha/h normal-gradient penalties",
        "mesh_sizes":args.mesh_sizes,"levels":reports}
    path=Path(args.out); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(payload,indent=2)+"\n")
    print(json.dumps(payload,indent=2))


if __name__=="__main__":
    main()
