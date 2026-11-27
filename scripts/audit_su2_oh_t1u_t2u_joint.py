#!/usr/bin/env python3
"""Joint K0 spin-ladder / O_h T1u,T2u audit.

Requires an independently certified orthogonal basis map. Never fits that map
by minimizing commutators; refuses cross-basis claims without the certificate.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from itertools import permutations, product
import numpy as np


def signed_permutations():
    out=[]
    for perm in permutations(range(3)):
        P=np.zeros((3,3))
        for row,col in enumerate(perm): P[row,col]=1.0
        for signs in product((-1.0,1.0),repeat=3): out.append(P@np.diag(signs))
    return out


def t2g_character(R):
    return float(sum(R[i,i]*R[j,j]+R[i,j]*R[j,i]
                     for i,j in ((0,1),(1,2),(2,0))))


def tangent_action(X,Q,G,tol=1e-8):
    d=np.linalg.norm((X@G.T)[:,None,:]-X[None,:,:],axis=2)
    p=np.argmin(d,axis=1)
    if d[np.arange(len(X)),p].max()>tol or len(np.unique(p))!=len(X):
        raise ValueError("O_h element does not preserve the point cloud")
    D=np.zeros((3*len(X),3*len(X)))
    for source,target in enumerate(p):
        D[3*target:3*target+3,3*source:3*source+3]=G
    R=Q.T@D@Q
    err=np.linalg.norm(D@Q-Q@R)
    if err>1e-7: raise ValueError(f"tangent action residual {err:g}")
    return R


def cubic_projector(X,Q,label):
    terms=[]
    for G in signed_permutations():
        parity=int(round(np.linalg.det(G)))
        Rp=parity*G
        chi=np.trace(Rp) if label=="T1u" else t2g_character(Rp)
        terms.append((parity*chi,tangent_action(X,Q,G)))
    P=(3.0/48.0)*sum(c*R for c,R in terms)
    return 0.5*(P+P.T)


def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""): h.update(chunk)
    return h.hexdigest()


def rank(A,tol=1e-8): return int(np.linalg.matrix_rank(A,tol=tol))


def intersection_dim(A,B,tol=1e-7):
    s=np.linalg.svd(A.T@B,compute_uv=False)
    return int(np.sum(s>=1.0-tol)),s.tolist()


def four_blocks(P,B):
    Q=np.eye(P.shape[0])-P
    blocks={"GG":P@B@P,"Gperp":P@B@Q,"perpG":Q@B@P,"perpperp":Q@B@Q}
    return {k:{"rank":rank(v),"fro":float(np.linalg.norm(v,"fro")),
               "spectral":float(np.linalg.norm(v,2))} for k,v in blocks.items()}


def delta_profile(B,V):
    M=V.T@B@V
    profile={str(d):float(np.linalg.norm(np.diag(M,k=-d)))
             for d in range(-123,124)}
    total=float(np.linalg.norm(M,"fro"))
    outside=sum(v*v for k,v in profile.items() if abs(int(k))!=3)
    return {"fro":total,"delta_m_fro":profile,
            "fraction_norm_outside_abs_delta3":float(np.sqrt(outside)/total) if total else 0.0}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--npz",default="data/RGS_PSU_all_matrices.npz")
    ap.add_argument("--k0",default="artifacts/K0.npy"); ap.add_argument("--zs",default="artifacts/Z_S.npy")
    ap.add_argument("--za",default="artifacts/Z_A.npy"); ap.add_argument("--pg",default="artifacts/P_G.npy")
    ap.add_argument("--basis-map",required=True,
      help="188x188 orthogonal C: operator coordinates = C @ geometric coordinates")
    ap.add_argument("--out",default="audits/SU2_OH_DOUBLE_GROUP_T1U_T2U_NUMERICAL.json")
    a=ap.parse_args()
    cp=Path(a.basis_map)
    if not cp.exists(): raise SystemExit(f"Missing independent basis-map certificate: {cp}")
    C=np.load(cp)
    if C.shape!=(188,188): raise SystemExit("basis map must be 188x188")
    orth=float(np.linalg.norm(C.T@C-np.eye(188),"fro"))
    if orth>1e-8: raise SystemExit(f"basis map not orthogonal: {orth:g}")

    z=np.load(a.npz); X=np.asarray(z["X_Oh_reconstructed"],float)
    Q=np.asarray(z["Q_tangent"],float)
    K,ZS,ZA,PG=(np.load(a.k0),np.load(a.zs),np.load(a.za),np.load(a.pg))
    P1g=cubic_projector(X,Q,"T1u"); P2g=cubic_projector(X,Q,"T2u")
    P1=C@P1g@C.T; P2=C@P2g@C.T
    e1=float(np.linalg.norm(P1@P1-P1,"fro")); e2=float(np.linalg.norm(P2@P2-P2,"fro"))
    r1,r2=rank(P1),rank(P2)
    if (r1,r2)!=(39,30) or max(e1,e2)>1e-7:
        raise SystemExit(f"cubic projectors failed: ranks={(r1,r2)}, idempotence={(e1,e2)}")

    wg,vg=np.linalg.eigh(0.5*(PG+PG.T)); UG=vg[:,wg>0.5]
    Pperp=np.eye(188)-PG
    wp,vp=np.linalg.eigh(0.5*(Pperp+Pperp.T)); Uperp=vp[:,wp>0.5]
    inter={}
    for name,P in (("T1u",P1),("T2u",P2)):
        w,v=np.linalg.eigh(0.5*(P+P.T)); U=v[:,w>0.5]
        dg,sg=intersection_dim(U,UG); dp,sp=intersection_dim(U,Uperp)
        inter[name]={"kernel_intersection":dg,"complement_intersection":dp,
          "kernel_principal_cosines":sg,"complement_principal_cosines":sp,
          "commutator_P_PG_fro":float(np.linalg.norm(P@PG-PG@P,"fro"))}

    ev,V=np.linalg.eigh(0.5*(K+K.T)); ids=np.flatnonzero(ev>1e-8)
    ids=ids[np.argsort(ev[ids])]
    if len(ids)!=124: raise SystemExit(f"expected 124 positive modes, got {len(ids)}")
    V=V[:,ids]; expected=(np.arange(124)+5.0)/10.0
    specerr=float(np.max(np.abs(ev[ids]-expected)))
    if specerr>1e-7: raise SystemExit(f"K0 ladder mismatch: {specerr:g}")
    j=61.5; m=-j+np.arange(124); Jz=np.diag(m); Jp=np.zeros((124,124))
    for n in range(123): Jp[n+1,n]=np.sqrt((j-m[n])*(j+m[n]+1))
    Jm=Jp.T
    ladder={"spectrum_max_error":specerr,
      "Jz_Jplus_fro":float(np.linalg.norm(Jz@Jp-Jp@Jz-Jp)),
      "Jz_Jminus_fro":float(np.linalg.norm(Jz@Jm-Jm@Jz+Jm)),
      "Jplus_Jminus_fro":float(np.linalg.norm(Jp@Jm-Jm@Jp-2*Jz)),
      "casimir_fro":float(np.linalg.norm(0.25*(Jp+Jm)@(Jp+Jm)
       -0.25*(Jp-Jm)@(Jp-Jm)+Jz@Jz-j*(j+1)*np.eye(124),"fro"))}
    ops={"Z_S":ZS,"Z_A":ZA,"T_transport":np.asarray(z["T_transport"],float)}
    opreport={}
    for name,B in ops.items():
        opreport[name]={"kernel_complement_blocks":four_blocks(PG,B),
          "cubic_blocks":{"T1u_T1u":float(np.linalg.norm(P1@B@P1,"fro")),
          "T1u_T2u":float(np.linalg.norm(P1@B@P2,"fro")),
          "T2u_T1u":float(np.linalg.norm(P2@B@P1,"fro")),
          "T2u_T2u":float(np.linalg.norm(P2@B@P2,"fro"))}}
        if name in ("Z_S","Z_A"): opreport[name]["delta_m_profile"]=delta_profile(B,V)
    report={"classification":"numerical results conditional on certified common-basis map",
      "basis_map":{"path":str(cp),"sha256":sha256(cp),"orthogonality_fro":orth},
      "cubic_projectors":{"T1u_rank":r1,"T2u_rank":r2,"T1u_idempotence":e1,
       "T2u_idempotence":e2,"intersections":inter},
      "spin_61_2_ladder":ladder,"operators":opreport,
      "scope_note":"Ordinary O_h blocks and ladder are audited. Binary-octahedral double-group character multiplicities remain a separate follow-up; no spin-1 identification is inferred.",
      "input_sha256":{p:sha256(p) for p in (a.npz,a.k0,a.zs,a.za,a.pg)}}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__": main()
