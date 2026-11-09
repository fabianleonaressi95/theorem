#!/usr/bin/env python3
"""P2 finite-element interpolation audit of the Airy cell-matrix identity.

This is a structured annular P2 patch test, not the published P3 C0-IPDG solver.
The exact continuum cell fields are interpolated on a triangular annulus mesh;
elementwise constant P2 Hessians are integrated to form both interaction matrices.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np


def _radial_coefficients(a: float, R: float, mode: int) -> np.ndarray:
    def traces(r):
        if mode == 0:
            return (np.array([1., np.log(r), r*r, r*r*np.log(r)]),
                    np.array([0., 1/r, 2*r, 2*r*np.log(r)+r]))
        return (np.array([r, 1/r, r**3, r*np.log(r)]),
                np.array([1., -1/r**2, 3*r*r, np.log(r)+1]))
    fa, pa = traces(a); fR, pR = traces(R)
    rhs = np.array([1., 0., 0., 0.]) if mode == 0 else np.array([a, 1., 0., 0.])
    return np.linalg.solve(np.vstack((fa, pa, fR, pR)), rhs)


def _field(xy: np.ndarray, mode: int, coeff: np.ndarray, angular: str) -> np.ndarray:
    x, y = xy[:, 0], xy[:, 1]
    r = np.hypot(x, y)
    if mode == 0:
        radial = coeff @ np.vstack((np.ones_like(r), np.log(r), r*r, r*r*np.log(r)))
        return radial
    radial = coeff @ np.vstack((r, 1/r, r**3, r*np.log(r)))
    angle = x/r if angular == "cos" else y/r
    return radial*angle


def audit_p2_annulus(a: float = 0.2, R: float = 1.0,
                     radial_cells: int = 8, angular_cells: int = 32) -> dict:
    if not (0 < a < R) or radial_cells < 2 or angular_cells < 8:
        raise ValueError("invalid annulus or mesh resolution")
    vertices=[]
    for ir in range(radial_cells+1):
        r=a+(R-a)*ir/radial_cells
        for j in range(angular_cells):
            th=2*np.pi*j/angular_cells
            vertices.append((r*np.cos(th), r*np.sin(th)))
    vertices=np.asarray(vertices)
    triangles=[]
    for ir in range(radial_cells):
        for j in range(angular_cells):
            p=ir*angular_cells+j; q=ir*angular_cells+(j+1)%angular_cells
            s=(ir+1)*angular_cells+j; t=(ir+1)*angular_cells+(j+1)%angular_cells
            triangles.extend(((p,s,t),(p,t,q)))
    edge_ids={}
    tri6=[]
    for tri in triangles:
        mids=[]
        for i,j in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
            key=tuple(sorted((i,j)))
            if key not in edge_ids: edge_ids[key]=len(vertices)+len(edge_ids)
            mids.append(edge_ids[key])
        tri6.append((*tri,*mids))
    edge_array=list(edge_ids)
    mids=np.asarray([(vertices[i]+vertices[j])*0.5 for i,j in edge_array])
    nodes=np.vstack((vertices,mids))
    coeffs=(_radial_coefficients(a,R,0),
            _radial_coefficients(a,R,1),
            _radial_coefficients(a,R,1))
    fields=(_field(nodes,0,coeffs[0],"cos"),
            _field(nodes,1,coeffs[1],"cos"),
            _field(nodes,1,coeffs[2],"sin"))
    # P2 polynomial basis [1,x,y,x^2,xy,y^2].
    H=np.zeros((3,3)); L=np.zeros((3,3))
    for ids in tri6:
        xy=nodes[list(ids)]
        x,y=xy[:,0],xy[:,1]
        V=np.column_stack((np.ones(6),x,y,x*x,x*y,y*y))
        area=0.5*abs((xy[1,0]-xy[0,0])*(xy[2,1]-xy[0,1])-
                     (xy[1,1]-xy[0,1])*(xy[2,0]-xy[0,0]))
        local=[]
        for f in fields:
            c=np.linalg.solve(V,f[list(ids)])
            local.append(np.array([[2*c[3],c[4]],[c[4],2*c[5]]]))
        for i in range(3):
            for j in range(3):
                H[i,j]+=area*float(np.sum(local[i]*local[j]))
                L[i,j]+=area*float(np.trace(local[i])*np.trace(local[j]))
    rel=float(np.linalg.norm(H-L,"fro")/max(np.linalg.norm(H,"fro"),1e-300))
    return {"inner_radius":a,"outer_radius":R,"radial_cells":radial_cells,
            "angular_cells":angular_cells,"vertices":int(len(vertices)),
            "triangles":int(len(triangles)),"p2_dofs":int(len(nodes)),
            "hessian_matrix":H.tolist(),"laplacian_matrix":L.tolist(),
            "relative_frobenius_difference":rel,
            "symmetry_residual_hessian":float(np.linalg.norm(H-H.T)),
            "symmetry_residual_laplacian":float(np.linalg.norm(L-L.T)),
            "min_eigenvalue_hessian":float(np.linalg.eigvalsh(H).min()),
            "min_eigenvalue_laplacian":float(np.linalg.eigvalsh(L).min())}


def run():
    levels=((4,16),(8,32),(16,64),(32,128))
    cases=[audit_p2_annulus(radial_cells=nr,angular_cells=nt) for nr,nt in levels]
    errors=[c["relative_frobenius_difference"] for c in cases]
    rates=[float(np.log(errors[i-1]/errors[i])/np.log(2))
           for i in range(1,len(errors))]
    return {"title":"P2 annular finite-element matrix identity audit",
            "status":"P2 interpolation patch test; not P3 C0-IPDG reproduction",
            "matrix_identity":"M_H[i,j]=integral D2(kappa_i):D2(kappa_j); M_L[i,j]=integral Delta(kappa_i)Delta(kappa_j)",
            "mesh":"structured triangular annulus; exact continuum cell fields sampled at P2 nodes",
            "relative_matrix_difference":errors,"observed_halving_rates":rates,
            "cases":cases}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",default=None)
    args=p.parse_args()
    result=run(); payload=json.dumps(result,indent=2)
    if args.out:
        path=Path(args.out); path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(payload+"\n")
    print(payload)


if __name__=="__main__":
    main()
