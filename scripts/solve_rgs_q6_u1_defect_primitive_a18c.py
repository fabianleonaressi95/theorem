#!/usr/bin/env python3
"""Construct an integral primitive beta with d beta = m for A18 Q6 defects.

Requires numpy and scipy (scipy.optimize.milp / HiGHS). The domain is the
finite non-periodic cubical 6-cube; this is not a continuum monopole solver.
"""
import argparse, itertools, json
Requires numpy and scipy (scipy.optimize.milp / HiGHS).
"""
import argparse, json
from pathlib import Path
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix, hstack, csr_matrix

def reconstruct_charges(path):
    with np.load(path, allow_pickle=False) as z:
        X=np.asarray(z["X"],float); edges=np.asarray(z["edges"],int); R=np.asarray(z["R_SO3"],float)
    if X.shape!=(64,3) or edges.shape!=(192,3) or R.shape!=(192,3,3):
        raise ValueError("Unexpected archive shapes")
    n=X/np.linalg.norm(X,axis=1)[:,None]; links={}
    for q,(g,h,_) in enumerate(edges):
        g=int(g); h=int(h); links[g,h]=R[q]; links[h,g]=R[q].T
    E=[]
    for ng in n:
        ref=np.eye(3)[int(np.argmin(np.abs(ng)))]
        u=np.cross(ref,ng); u/=np.linalg.norm(u); v=np.cross(ng,u)
        E.append(np.column_stack((u,v,ng)))
    E=np.asarray(E); A={(g,h):(E[h].T@Rg@E[g])[:2,:2] for (g,h),Rg in links.items()}
    face={}
    for a in range(6):
        for b in range(a+1,6):
            for g in range(64):
                if (g>>a)&1 or (g>>b)&1: continue
                j=g^(1<<a); k=j^(1<<b); l=g^(1<<b)
                H=A[l,g]@A[k,l]@A[j,k]@A[g,j]
                face[g,a,b]=float(np.arctan2(H[1,0],H[0,0]))
    charge={}
    for a in range(6):
        for b in range(a+1,6):
            for c in range(b+1,6):
                for g in range(64):
                    if any((g>>q)&1 for q in (a,b,c)): continue
                    ga=g^(1<<a); gb=g^(1<<b); gc=g^(1<<c)
                    s=(face[ga,b,c]-face[g,b,c]-face[gb,a,c]
                       +face[g,a,c]+face[gc,a,b]-face[g,a,b])
                    m=int(round(s/(2*np.pi)))
                    if abs(s-2*np.pi*m)>1e-8: raise ArithmeticError("Non-quantized cube boundary")
                    charge[g,a,b,c]=m
    return charge

def solve(path):
    charge=reconstruct_charges(path)
    faces=[(g,a,b) for a in range(6) for b in range(a+1,6)
           for g in range(64) if not ((g>>a)&1 or (g>>b)&1)]
    cubes=[(g,a,b,c) for a in range(6) for b in range(a+1,6)
           for c in range(b+1,6) for g in range(64)
           if not any((g>>q)&1 for q in (a,b,c))]
    fi={f:i for i,f in enumerate(faces)}
    D=lil_matrix((160,240),dtype=np.int64)
    for i,(g,a,b,c) in enumerate(cubes):
        terms=[(g^(1<<a),b,c,1),(g,b,c,-1),(g^(1<<b),a,c,-1),
               (g,a,c,1),(g^(1<<c),a,b,1),(g,a,b,-1)]
        for fg,fa,fb,s in terms: D[i,fi[(fg,fa,fb)]]+=s
    D=csr_matrix(D); m=np.array([charge[c] for c in cubes],dtype=np.int64)
    # beta = p - n; minimize ||beta||_1 over integral p,n >= 0.
    A=hstack([D,-D],format="csr")
    opt=milp(c=np.ones(480),integrality=np.ones(480),
             bounds=Bounds(np.zeros(480),np.full(480,np.inf)),
             constraints=LinearConstraint(A,m,m),options={"time_limit":180})
    if not opt.success or opt.x is None: raise RuntimeError(f"Integer optimization failed: {opt.message}")
    beta=np.rint(opt.x[:240]).astype(np.int64)-np.rint(opt.x[240:]).astype(np.int64)
    residual=np.asarray(D@beta-m).reshape(-1)
    if np.any(residual): raise ArithmeticError("d beta != m")
    bnon=[{"base_vertex":int(g),"axes":[int(a),int(b)],"coefficient":int(beta[i])}
          for i,(g,a,b) in enumerate(faces) if beta[i]]
    from collections import Counter
    return {
      "classification":"EXPLICIT_INTEGER_COBBOUNDARY",
      "method":"L1-minimizing integer MILP (HiGHS) for d:C^2(I^6;Z)->C^3(I^6;Z)",
      "complex":{"type":"full_nonperiodic_6_cube","oriented_2_faces":240,"oriented_3_cells":160},
      "optimization":{"status":opt.message,"l1_norm":int(np.abs(beta).sum()),
                      "nonzero_coefficients":len(bnon),"optimality_certified_by_solver":True},
    return {"classification":"EXPLICIT_INTEGER_COBBOUNDARY",
      "method":"L1-minimizing integer MILP (HiGHS) for d:C^2(I^6;Z)->C^3(I^6;Z)",
      "complex":{"type":"full_nonperiodic_6_cube","oriented_2_faces":240,"oriented_3_cells":160},
      "optimization":{"status":opt.message,"l1_norm":int(np.abs(beta).sum()),
                      "nonzero_coefficients":len(bnon)},
      "verification":{"max_abs_d_beta_minus_m":int(np.max(np.abs(residual))),
                      "exact_all_160_equations":bool(np.all(residual==0)),
                      "charge_histogram":{str(k):int(v) for k,v in sorted(Counter(m.tolist()).items())},
                      "total_charge":int(m.sum())},
      "beta_nonzero_faces":bnon,
      "conventions":{"face_orientation":"positive (a,b): +a,+b,-a,-b",
                     "cube_coboundary":"Delta_a beta_bc - Delta_b beta_ac + Delta_c beta_ab"},
      "nonuniqueness":"Any integral closed 2-cochain may be added to beta without changing d beta. The L1 minimizer is one convention-dependent representative, not a canonical physical sheet.",
      "interpretation_limits":["Finite cubical cochain identity only.",
      "nonuniqueness":"Any integral closed 2-cochain may be added to beta without changing d beta.",
      "limits":["Finite cubical cochain identity only.",
        "No physical Dirac sheet, magnetic monopole, or continuum source is established.",
        "The non-periodic cube has boundary; do not infer periodic neutrality."]}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--npz",required=True,type=Path); p.add_argument("--out",required=True,type=Path)
    a=p.parse_args(); result=solve(a.npz)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"optimization":result["optimization"],"verification":result["verification"]},indent=2))
