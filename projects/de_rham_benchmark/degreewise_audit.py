#!/usr/bin/env python3
"""Degree-wise Hodge energy audit in the actual diagonal M_k norms."""
import argparse, json
import numpy as np
import scipy.linalg as la
from ddr.mesh import CubicalMesh
from ddr.geometry import PullbackGeometry
from ddr.hodge import hodge_matrices, betti_numbers

def run(dim, N, nvec):
    mesh = CubicalMesh(N, dim)
    geo = PullbackGeometry(mesh, {"type":"identity"}, {"type":"identity"}, nq=4, nqf=3)
    H = hodge_matrices(mesh, geo.M)
    beta, ranks = betti_numbers(mesh)
    degrees = []
    for k in range(dim+1):
        M = np.asarray(geo.M[k], float)
        B = H["B"][k].toarray()
        w, V = la.eigh(B, np.diag(M), subset_by_index=(0, min(nvec-1, len(M)-1)))
        pairs = []
        for j, lam in enumerate(w):
            x = V[:,j]
            grad = curl = 0.0
            if k:
                t = mesh.dmat[k-1].T @ (M*x)
                grad = float(np.sum(t*t/geo.M[k-1]))
            if k < dim:
                dx = mesh.dmat[k] @ x
                curl = float(np.sum(geo.M[k+1]*np.asarray(dx).ravel()**2))
            total = grad+curl
            gf = grad/total if total else 0.0
            cf = curl/total if total else 0.0
            dist = None
            if k:
                A = mesh.dmat[k-1].toarray()
                sw = np.sqrt(M)
                Aw, xw = sw[:,None]*A, sw*x
                c, *_ = np.linalg.lstsq(Aw, xw, rcond=None)
                dist = float(np.linalg.norm(xw-Aw@c)/np.linalg.norm(xw))
            r = B@x-lam*M*x
            den = np.linalg.norm(B,2)*np.linalg.norm(x)+abs(lam)*np.linalg.norm(M*x)
            pairs.append({
                "lambda":float(lam),
                "grad_energy_fraction":gf,
                "curl_energy_fraction":cf,
                "normalized_co_closedness_defect":float(np.sqrt(max(gf,0))),
                "M_relative_distance_to_im_d":dist,
                "relative_generalized_residual":float(np.linalg.norm(r)/max(den,1e-300))
            })
        degrees.append({"k":k,"n":len(M),"eigenpairs":pairs})
    return {"dimension":dim,"N":N,"betti":beta,"incidence_ranks":ranks,
            "degrees":degrees,
            "note":"For k=dim, d_k=0: positive modes have grad fraction 1 and cannot be co-closed."}

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--dim",type=int,choices=(2,3),required=True)
    p.add_argument("--N",type=int,required=True)
    p.add_argument("--nvec",type=int,default=4)
    p.add_argument("--out",default="")
    a=p.parse_args()
    result=run(a.dim,a.N,a.nvec)
    out=json.dumps(result,indent=2)
    if a.out:
        with open(a.out,"w",encoding="utf-8") as f: f.write(out+"\n")
    print(out)
