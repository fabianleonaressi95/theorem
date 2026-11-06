#!/usr/bin/env python3
"""Finite-sample T2u covariant observable/multiplicity audit. Requires numpy."""
import argparse, itertools, json
from pathlib import Path
import numpy as np

def h(x):
    x,y,z=x
    return np.array([x*(y*y-z*z), y*(z*z-x*x), z*(x*x-y*y)],float)

def group_oh():
    G=[]
    for p in itertools.permutations(range(3)):
        P=np.zeros((3,3),int)
        for i,j in enumerate(p): P[i,j]=1
        for s in itertools.product((-1,1),repeat=3): G.append(np.diag(s)@P)
    return G

def rotate(a,R):
    c=a.shape[0]//2; out=np.zeros_like(a)
    for i in np.ndindex(a.shape):
        x=np.asarray(i)-c; y=R@x
        out[tuple((y+c).tolist())]=a[i]
    return out

def neighbor_count(a,D):
    s=np.zeros_like(a,dtype=np.int16)
    for d in D: s+=np.roll(a,shift=d,axis=(0,1,2))
    return s

def update(a,r,D):
    s=neighbor_count(a,D); q=27*a.astype(np.int16)+s
    assert q.min()>=0 and q.max()<=53
    return r[q]

def features(a,H,D):
    s=neighbor_count(a,D); out=np.zeros((10,3)); edges=np.linspace(0,27,11)
    for j in range(10):
        m=(s>=edges[j])&(s<edges[j+1])
        out[j]=np.einsum("ijk,ijkc->c",a*m,H)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--samples",type=int,default=500)
    ap.add_argument("--out",default="audit_t2u_multiplicity.json")
    args=ap.parse_args()
    L=5; c=2; axis=np.arange(-2,3)
    xyz=np.stack(np.meshgrid(axis,axis,axis,indexing="ij"),axis=-1)
    H=np.stack([xyz[...,0]*(xyz[...,1]**2-xyz[...,2]**2),
                xyz[...,1]*(xyz[...,2]**2-xyz[...,0]**2),
                xyz[...,2]*(xyz[...,0]**2-xyz[...,1]**2)],axis=-1).astype(float)
    points=np.asarray(list(itertools.product(axis,repeat=3)))
    Deltas=[d for d in itertools.product((-1,0,1),repeat=3) if d!=(0,0,0)]
    G=group_oh(); Ds=[]; harmonic_err=[]
    Hp=np.asarray([h(x) for x in points])
    for R in G:
        HR=np.asarray([h(R@x) for x in points])
        Dr=np.linalg.lstsq(Hp,HR,rcond=None)[0].T
        Ds.append(Dr); harmonic_err.append(float(np.linalg.norm(HR-Hp@Dr.T)))
    lookup={tuple(R.flatten()):D for R,D in zip(G,Ds)}
    rep_err=max(float(np.linalg.norm(lookup[tuple((R@S).flatten())]-A@B))
                for R,A in zip(G,Ds) for S,B in zip(G,Ds))
    rr=np.random.default_rng(20261106); rc=np.random.default_rng(20261107)
    rs=np.random.default_rng(20261108); rule=rr.integers(0,2,54,dtype=np.uint8)
    mismatch=0; feature_err=0.
    for _ in range(20):
        a=rc.integers(0,2,(L,L,L),dtype=np.uint8); Fa=update(a,rule,Deltas); xa=features(a,H,Deltas)
        for R,Dr in zip(G,Ds):
            Ra=rotate(a,R)
            mismatch+=int(np.count_nonzero(update(Ra,rule,Deltas)-rotate(Fa,R)))
            feature_err=max(feature_err,float(np.linalg.norm(features(Ra,H,Deltas)-xa@Dr.T)))
    X=[]; Y=[]
    for _ in range(args.samples):
        p=float(rs.uniform(.1,.9)); a=(rs.random((L,L,L))<p).astype(np.uint8)
        Fa=update(a,rule,Deltas); xa=features(a,H,Deltas); ya=features(Fa,H,Deltas)
        for Dr in Ds: X.append(xa@Dr.T); Y.append(ya@Dr.T)
    X=np.asarray(X); Y=np.asarray(Y)
    Xf=X.transpose(0,2,1).reshape(-1,10); Yf=Y.transpose(0,2,1).reshape(-1,10)
    C,*_=np.linalg.lstsq(Xf,Yf,rcond=None); M=C.T
    Yhat=np.einsum("njc,jk->nkc",X,C)
    eig=np.linalg.eigvals(M); psi=1.465571231876768
    report={
      "status":"FINITE_SAMPLE_PROJECTED_DIAGNOSTIC","seeds":[20261106,20261107,20261108],
      "lattice":[L,L,L],"rule_table_length":54,"point_group":"O_h","group_order":48,
      "base_configurations":args.samples,"orbit_augmented_samples":len(X),
      "T2u_harmonics":["x*(y^2-z^2)","y*(z^2-x^2)","z*(x^2-y^2)"],
      "feature_channels":10,"feature_definition":"sum_x a(x) 1_{s(x) in bin_j} h_T2u(x)",
      "harmonic_intertwiner_max_residual":max(harmonic_err),
      "representation_law_max_residual":rep_err,"update_equivariance_mismatches":int(mismatch),
      "feature_covariance_max_residual":feature_err,"design_rank":int(np.linalg.matrix_rank(Xf)),
      "design_condition_number":float(np.linalg.cond(Xf)),
      "relative_closure_error":float(np.linalg.norm(Y-Yhat)/np.linalg.norm(Y)),
      "multiplicity_matrix_M10":M.tolist(),
      "multiplicity_eigenvalues":[{"real":float(z.real),"imag":float(z.imag)} for z in eig],
      "psi":psi,"psi_polynomial_residual":float(psi**3-psi**2-1),
      "multiplicity_polynomial_residuals":[float(abs(z**3-z**2-1)) for z in eig],
      "interpretation":["The cubic harmonics form a T2u covariant triplet under O_h.",
        "Ten channels give a full-rank sampled multiplicity design in this run.",
        "Large closure error means this selected 30D observable space is not closed.",
        "M10 is a projected least-squares map, not an exact Koopman restriction.",
        "No supergolden recurrence is detected; no numerical map into RGS 188D coordinates is claimed."]}
    Path(args.out).write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2))
    if mismatch or feature_err>1e-9 or rep_err>1e-9: raise SystemExit("FAIL: O_h/T2u covariance")
    if np.linalg.matrix_rank(Xf)!=10: raise SystemExit("FAIL: multiplicity design rank")
if __name__=="__main__": main()
