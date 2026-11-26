#!/usr/bin/env python3
"""EG-01 diagnostic: regular square grid versus a one-edge bottleneck.
Requires numpy and scipy. The bottleneck violates the path-tube condition G5.
"""
import argparse, csv
from pathlib import Path
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

def run(n, bottleneck):
    edges=[]
    for i in range(n):
        for j in range(n):
            a=i*n+j
            if i+1<n and (not bottleneck or i!=n//2-1 or j==n//2):
                edges.append((a,(i+1)*n+j))
            if j+1<n: edges.append((a,a+1))
    rr=[]; cc=[]
    for a,b in edges: rr += [a,b]; cc += [b,a]
    A=sp.coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(n*n,n*n)).tocsr()
    L=sp.diags(np.asarray(A.sum(axis=1)).ravel())-A
    ev=np.sort(spla.eigsh(L,k=3,which="SM",return_eigenvectors=False,tol=1e-10))
    cut=sum(1 for a,b in edges if (a//n<n//2)!=(b//n<n//2))
    return dict(n=n,epsilon=1/n,vertices=n*n,edges=len(edges),
      graph_gap=float(ev[1]),scaled_gap=float(ev[1]*n*n),
      cut_edges=cut,step_energy=0.5*cut if not bottleneck else 0.5,
      path_tube_lower_bound=0.0 if not bottleneck else 0.25-1/n,
      family="single_bridge" if bottleneck else "regular_grid")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--sizes",nargs="+",type=int,default=[8,12,16,24,32,40])
    p.add_argument("--output",default="eg01_bottleneck_results.csv")
    a=p.parse_args()
    rows=[run(n,b) for n in a.sizes for b in (False,True)]
    with Path(a.output).open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    for r in rows:
        print("%-13s n=%2d scaled_gap=%.6g cut=%d E_step=%.4g tube_lb=%.4g" %
          (r["family"],r["n"],r["scaled_gap"],r["cut_edges"],r["step_energy"],r["path_tube_lower_bound"]))
    print("Wrote",a.output)
if __name__=="__main__": main()
