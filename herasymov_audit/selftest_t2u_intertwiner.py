#!/usr/bin/env python3
"""Synthetic unit test for the Reynolds intertwiner solver (not RGS data)."""
import itertools
import numpy as np

def h(x):
    x,y,z=x
    return np.array([x*(y*y-z*z),y*(z*z-x*x),z*(x*x-y*y)],float)

def main():
    G=[]
    for p in itertools.permutations(range(3)):
        P=np.zeros((3,3),int)
        for i,j in enumerate(p):P[i,j]=1
        for s in itertools.product((-1,1),repeat=3):G.append(np.diag(s)@P)
    pts=np.asarray(list(itertools.product(range(-2,3),repeat=3)))
    H=np.asarray([h(x) for x in pts])
    D=[]
    for R in G:
        HR=np.asarray([h(R@x) for x in pts])
        D.append(np.linalg.lstsq(H,HR,rcond=None)[0].T)
    D=np.asarray(D); lookup={tuple(R.ravel()):i for i,R in enumerate(G)}
    mult=np.asarray([[lookup[tuple((R@S).ravel())] for S in G] for R in G])
    U=np.zeros((48,188,188))
    for i in range(48):
        U[i,:30,:30]=np.kron(np.eye(10),D[i])
        U[i,30:,30:]=np.eye(158)
    sigma=[np.kron(np.eye(10),d) for d in D]
    rng=np.random.default_rng(20261106); J0=rng.normal(size=(188,30))
    J=sum(U[g]@J0@sigma[g].T for g in range(48))/48
    repD=max(np.linalg.norm(D[mult[i,j]]-D[i]@D[j]) for i in range(48) for j in range(48))
    repU=max(np.linalg.norm(U[mult[i,j]]-U[i]@U[j]) for i in range(48) for j in range(48))
    intertw=max(np.linalg.norm(U[g]@J-J@sigma[g]) for g in range(48))
    rank=int(np.linalg.matrix_rank(J,tol=1e-10))
    result={"status":"SYNTHETIC_UNIT_TEST_ONLY","group_order":48,
      "target_dimension":188,"source_dimension":30,
      "representation_D_residual":float(repD),"representation_U_residual":float(repU),
      "intertwining_residual":float(intertw),"projected_intertwiner_rank":rank,
      "smallest_singular_value":float(np.linalg.svd(J,compute_uv=False)[-1]),
      "warning":"U was constructed synthetically as 10 copies of T2u plus 158 trivial dimensions. This validates the Reynolds implementation only; it is not a result about the archived RGS tangent representation."}
    import json; print(json.dumps(result,indent=2))
    assert repD<1e-10 and repU<1e-10 and intertw<1e-10 and rank==30
if __name__=="__main__": main()
