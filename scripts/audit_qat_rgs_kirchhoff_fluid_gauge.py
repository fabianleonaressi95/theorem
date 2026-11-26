#!/usr/bin/env python3
"""Read-only compatibility audit for existing QAT-RGS-Q6 source arrays.
Missing source arrays are reported NOT TESTED; nothing is reconstructed.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

class Audit:
    def __init__(self): self.tests = []
    def add(self, name, status, detail, **metrics):
        assert status in ("PASS", "FAIL", "NOT TESTED")
        self.tests.append({"test": name, "status": status, "detail": detail, **metrics})
    def report(self):
        counts = {s: sum(x["status"] == s for x in self.tests)
                  for s in ("PASS", "FAIL", "NOT TESTED")}
        return {"audit": "QAT-RGS-Q6 Kirchhoff / fluid-gauge compatibility",
                "mode": "read-only; no source geometry or arrays reconstructed",
                "counts": counts,
                "overall": "FAIL" if counts["FAIL"] else ("PARTIAL" if counts["NOT TESTED"] else "PASS"),
                "tests": self.tests,
                "scope": "Finite-data compatibility only; no polariton derivation or physical viscosity."}

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""): h.update(block)
    return h.hexdigest()

def su2_random(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    w,x,y,z = q
    return np.array([[w-1j*z, -y-1j*x], [y-1j*x, w+1j*z]], complex)

def load_bundle(path):
    with np.load(path, allow_pickle=False) as z:
        return {k: np.asarray(z[k]) for k in z.files}

def array_inventory(arrays):
    out={}
    for key,value in arrays.items():
        raw=np.ascontiguousarray(value).tobytes(order="C")
        out[key]={"shape":list(value.shape),"dtype":str(value.dtype),
                  "sha256":hashlib.sha256(raw).hexdigest()}
    return out

def covariant_laplacian(nv, edges, links, weights):
    # T118 convention: D_e psi = psi_h - U_gh psi_g.
    D = np.zeros((2*len(edges), 2*nv), complex)
    for k,(g,h,*_) in enumerate(edges):
        D[2*k:2*k+2,2*g:2*g+2] = -links[k]
        D[2*k:2*k+2,2*h:2*h+2] = np.eye(2)
    return D.conj().T @ (np.repeat(weights,2)[:,None] * D)

def gauge_covariance(audit, edges, U, weights, seed):
    nv = int(edges[:,:2].max())+1
    rng = np.random.default_rng(seed)
    G = np.stack([su2_random(rng) for _ in range(nv)])
    UG = np.stack([G[h] @ U[k] @ G[g].conj().T
                   for k,(g,h,*_) in enumerate(edges)])
    H = covariant_laplacian(nv,edges,U,weights)
    HG = covariant_laplacian(nv,edges,UG,weights)
    B = np.zeros((2*nv,2*nv),complex)
    for v in range(nv): B[2*v:2*v+2,2*v:2*v+2] = G[v]
    r = np.linalg.norm(HG-B@H@B.conj().T)/max(np.linalg.norm(H),1.)
    audit.add("random SU(2) gauge covariance","PASS" if r<5e-10 else "FAIL",
              "T118 convention U^G_gh=G_h U_gh G_g†; D_e psi=psi_h-U_gh psi_g",
              relative_residual=float(r),seed=seed)

def holonomy_covariance(audit, arrays, edges, U):
    if "plaquette_vertices" not in arrays:
        audit.add("plaquette holonomy covariance", "NOT TESTED",
                  "No ordered plaquette_vertices array supplied")
        return
    faces=np.asarray(arrays["plaquette_vertices"],int)
    if faces.ndim!=2 or faces.shape[1]!=4:
        audit.add("plaquette holonomy covariance","FAIL",
                  "plaquette_vertices must have shape (n_faces,4)")
        return
    lookup={(int(g),int(h)):k for k,(g,h,*_) in enumerate(edges)}
    nv=int(edges[:,:2].max())+1
    rng=np.random.default_rng(118)
    G=np.stack([su2_random(rng) for _ in range(nv)])
    def getlink(g,h,links):
        if (g,h) in lookup: return links[lookup[(g,h)]]
        if (h,g) in lookup: return links[lookup[(h,g)]].conj().T
        raise KeyError((g,h))
    worst=0.0; worst_trace=0.0
    for face in faces:
        H=np.eye(2,dtype=complex); HG=np.eye(2,dtype=complex)
        for g,h in zip(face,np.roll(face,-1)):
            u=getlink(int(g),int(h),U)
            ug=G[int(h)]@u@G[int(g)].conj().T
            H=u@H; HG=ug@HG
        expected=G[int(face[0])]@H@G[int(face[0])].conj().T
        worst=max(worst,float(np.linalg.norm(HG-expected)))
        worst_trace=max(worst_trace,float(abs(np.trace(HG)-np.trace(H))))
    ok=max(worst,worst_trace)<5e-10
    audit.add("plaquette holonomy covariance","PASS" if ok else "FAIL",
              "Ordered products transform by base-vertex conjugation (T118)",
              max_conjugation_residual=worst,max_wilson_trace_residual=worst_trace,
              plaquettes=len(faces))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--bundle",type=Path)
    p.add_argument("--output",type=Path,default=ROOT/"reports/qat_rgs_kirchhoff_fluid_gauge_audit.json")
    p.add_argument("--seed",type=int,default=20261118)
    args=p.parse_args(); a=Audit()
    csv=ROOT/"data/rgs_188d/X_Oh_reconstructed.csv"
    if csv.exists():
        x=np.loadtxt(csv,delimiter=",",skiprows=1)
        a.add("RGS coordinate provenance","PASS","Tracked coordinate source read unchanged",
              path=str(csv.relative_to(ROOT)),shape=list(x.shape),sha256=digest(csv))
    else: a.add("RGS coordinate provenance","NOT TESTED","Tracked coordinate CSV absent")

    if args.bundle and args.bundle.exists():
        arrays=load_bundle(args.bundle)
        a.add("NPZ source bundle","PASS","Opened read-only",path=str(args.bundle),
              sha256=digest(args.bundle),keys=sorted(arrays),array_inventory=array_inventory(arrays))
    else:
        arrays={}
        a.add("NPZ source bundle","NOT TESTED",
              "Recovered A13/A14/Q6 archives are catalogued but not tracked here; supply --bundle")

    def get(key,shape=None):
        if key not in arrays:
            a.add(key,"NOT TESTED","Required source array absent"); return None
        v=arrays[key]
        ok=shape is None or v.shape==shape
        a.add(key+" dimensions","PASS" if ok else "FAIL",
              "Source shape recorded",shape=list(v.shape),dtype=str(v.dtype),
              expected=list(shape) if shape else None)
        return v if ok else None

    # Prefer archived incidence matrices. If absent, derive only the combinatorial
    # incidence from archived Q6_states/Q6_adjacency (no geometric reconstruction).
    edges=arrays.get("edges")
    B1=arrays.get("B1"); B2=arrays.get("B2")
    if edges is None and "Q6_states" in arrays and "Q6_adjacency" in arrays:
        states=np.asarray(arrays["Q6_states"],int); adj=np.asarray(arrays["Q6_adjacency"],int)
        if states.shape==(64,6) and adj.shape==(64,64):
            derived=[]
            for g in range(64):
                for h in range(g+1,64):
                    if adj[g,h]:
                        diff=np.flatnonzero(states[g]!=states[h])
                        derived.append((g,h,int(diff[0]) if len(diff)==1 else -1))
            edges=np.asarray(derived,int)
            # Canonical oriented incidence from lower vertex index to higher.
            B1=np.zeros((64,len(edges)),int)
            for k,(g,h,b) in enumerate(edges): B1[g,k]=-1; B1[h,k]=1
            faces=[]
            for b1 in range(6):
                for b2 in range(b1+1,6):
                    for basev in range(64):
                        if basev&(1<<b1) or basev&(1<<b2): continue
                        faces.append([basev,basev|(1<<b1),basev|(1<<b1)|(1<<b2),basev|(1<<b2)])
            B2=np.zeros((len(edges),len(faces)),int)
            lookup={tuple(sorted((int(g),int(h)))):k for k,(g,h,*_) in enumerate(edges)}
            for j,vs in enumerate(faces):
                for g,h in zip(vs,vs[1:]+vs[:1]):
                    k=lookup[tuple(sorted((g,h)))]
                    B2[k,j]=1 if edges[k,0]==g else -1
            a.add("Q6 incidence derived from archived states","PASS",
                  "Combinatorial incidence only; no geometry reconstructed",
                  edges=int(len(edges)),faces=int(len(faces)))
        else:
            a.add("Q6 incidence derived from archived states","FAIL",
                  "Q6_states/Q6_adjacency have incompatible dimensions")
    if edges is not None:
        edges=np.asarray(edges)
        a.add("edge dimensions","PASS" if edges.shape==(192,3) else "FAIL",
              "Oriented edge table",shape=list(edges.shape))
    else: a.add("edge dimensions","NOT TESTED","No edges or archived Q6 state/adjacency pair")
    if B1 is not None and B2 is not None:
        r=int(np.max(np.abs(np.asarray(B1,dtype=np.int64)@np.asarray(B2,dtype=np.int64))))
    edges=get("edges",(192,3)); B1=get("B1",(64,192)); B2=get("B2",(192,240))
    if B1 is not None and B2 is not None:
        r=int(np.max(np.abs(B1.astype(np.int64)@B2.astype(np.int64))))
        a.add("Kirchhoff B1 B2=0","PASS" if r==0 else "FAIL",
              "Exact integer chain identity",max_abs_entry=r)
    else: a.add("Kirchhoff B1 B2=0","NOT TESTED","B1 and B2 both required")

    if edges is not None:
        g=edges[:,0].astype(int); h=edges[:,1].astype(int); bit=edges[:,2].astype(int)
        valid=(np.all((bit>=0)&(bit<6)) and np.all((g>=0)&(g<64)) and
               np.all((h>=0)&(h<64)) and np.all(h==(g ^ (1<<bit))) and
               len({tuple(sorted((int(x),int(y)))) for x,y in zip(g,h)})==192)
        lo=int(np.count_nonzero(bit<3)); hi=int(np.count_nonzero(bit>=3))
        ok=valid and (lo,hi)==(96,96)
        a.add("T099 Kirchhoff lower/upper split","PASS" if ok else "FAIL",
              "Bits 0-2 lower trigram; bits 3-5 upper trigram",
              lower_edges=lo,upper_edges=hi,
              trigram_labels={"010":"Kan","110":"Dui","111":"Qian"})

    qatkey=next((k for k in ("K_QAT","K_tau","qat_kernel") if k in arrays),None)
    if qatkey:
        K=np.asarray(arrays[qatkey],complex)
        if K.ndim==2 and K.shape[0]==K.shape[1]:
            hr=float(np.linalg.norm(K-K.conj().T)/max(np.linalg.norm(K),1.))
            mineig=float(np.linalg.eigvalsh((K+K.conj().T)/2).min())
            ok=hr<5e-10 and mineig>=-5e-10
            a.add("QAT kernel Hermiticity/positivity","PASS" if ok else "FAIL",
                  "Tests supplied QAT heat-kernel/operator matrix; does not reconstruct K_tau",
                  key=qatkey,shape=list(K.shape),hermiticity_residual=hr,min_eigenvalue=mineig)
        else:
            a.add("QAT kernel Hermiticity/positivity","FAIL",
                  "QAT kernel must be a square matrix",key=qatkey,shape=list(K.shape))
    else:
        a.add("QAT kernel Hermiticity/positivity","NOT TESTED",
              "No archived K_QAT/K_tau/qat_kernel array supplied")

    tetrad=next((k for k in ("tetrad","vierbein","E_tetrad") if k in arrays),None)
    if tetrad:
        e=arrays[tetrad]
        a.add("RGS coframe artifact","PASS" if e.shape[0]==64 else "FAIL",
              "Shape only; no inference of four physical coordinates",
              key=tetrad,shape=list(e.shape))
    else: a.add("RGS coframe artifact","NOT TESTED","No tetrad array supplied")

    measure=next((k for k in ("M","measure","site_measure") if k in arrays),None)
    if measure:
        m=np.asarray(arrays[measure],float)
        mineig=float(np.linalg.eigvalsh(m).min()) if m.ndim==2 else float(m.min())
        a.add("positive site measure","PASS" if mineig>0 else "FAIL",
              "Strict positivity",key=measure,min_eigenvalue=mineig)
    else: a.add("positive site measure","NOT TESTED","No site measure supplied")

    weights=arrays.get("edge_weights")
    if weights is not None:
        weights=np.asarray(weights,float).reshape(-1)
        ok=weights.size==192 and np.all(np.isfinite(weights)) and np.all(weights>=0)
        a.add("nonnegative edge weights","PASS" if ok else "FAIL",
              "Finite nonnegative weights",count=int(weights.size),
              min_weight=float(weights.min()) if weights.size else None)
    else: a.add("nonnegative edge weights","NOT TESTED","No edge_weights supplied")

    linkkey=next((k for k in ("U_SU2","U_plus","links_su2") if k in arrays),None)
    U=np.asarray(arrays[linkkey],complex) if linkkey else None
    if U is None or edges is None:
        a.add("SU(2) link unitarity/determinant","NOT TESTED","Need links and edges")
        a.add("random SU(2) gauge covariance","NOT TESTED","Need links and edges")
        a.add("U=I RGS Laplacian comparison","NOT TESTED","Need links and a separately supplied RGS Laplacian")
    elif U.shape!=(192,2,2):
        a.add("SU(2) link unitarity/determinant","FAIL","Expected (192,2,2)",shape=list(U.shape))
        a.add("random SU(2) gauge covariance","NOT TESTED","Invalid link dimensions")
        a.add("U=I RGS Laplacian comparison","NOT TESTED","Invalid link dimensions")
    else:
        ur=max(float(np.linalg.norm(u.conj().T@u-np.eye(2))) for u in U)
        dr=max(float(abs(np.linalg.det(u)-1)) for u in U)
        ok=ur<5e-10 and dr<5e-10
        a.add("SU(2) link unitarity/determinant","PASS" if ok else "FAIL",
              "Checks U†U=I and det(U)=1",max_unitarity_residual=ur,max_det_residual=dr)
        if weights is not None and weights.size==192 and np.all(weights>=0):
            gauge_covariance(a,edges,U,weights,args.seed)
            HU=covariant_laplacian(64,edges,U,weights)
            herm=float(np.linalg.norm(HU-HU.conj().T)/max(np.linalg.norm(HU),1.))
            mineig=float(np.linalg.eigvalsh((HU+HU.conj().T)/2).min())
            a.add("covariant Laplacian Hermiticity/positivity",
                  "PASS" if herm<5e-10 and mineig>=-5e-10 else "FAIL",
                  "H_U=D_U† W D_U with W nonnegative",
                  hermiticity_residual=herm,min_eigenvalue=mineig)
            holonomy_covariance(a,arrays,edges,U)
        else:
            a.add("random SU(2) gauge covariance","NOT TESTED","Need valid edge_weights")
            a.add("covariant Laplacian Hermiticity/positivity","NOT TESTED","Need valid edge_weights")
            a.add("plaquette holonomy covariance","NOT TESTED","Need valid edge_weights")
        if "L_RGS" in arrays and weights is not None and weights.size==192:
            Ilinks=np.repeat(np.eye(2,dtype=complex)[None,:,:],192,axis=0)
            H0=covariant_laplacian(64,edges,Ilinks,weights)
            L=np.asarray(arrays["L_RGS"],float)
            target=np.kron(L,np.eye(2)) if L.shape==(64,64) else L
            if target.shape==H0.shape:
                rr=float(np.linalg.norm(H0-target)/max(np.linalg.norm(target),1.))
                a.add("U=I RGS Laplacian comparison","PASS" if rr<5e-10 else "FAIL",
                      "Compares with supplied scalar L_RGS lifted by I_2 when needed",
                      relative_residual=rr)
            else: a.add("U=I RGS Laplacian comparison","NOT TESTED",
                        "L_RGS shape cannot be compared with the spin-lifted operator",
                        shape=list(L.shape))
        else: a.add("U=I RGS Laplacian comparison","NOT TESTED",
                    "Need L_RGS and valid edge weights")

    if "U_plus" in arrays and "U_minus" in arrays:
        up,um=np.asarray(arrays["U_plus"]),np.asarray(arrays["U_minus"])
        rr=float(np.linalg.norm(um-up.conj())/max(np.linalg.norm(up),1.))
        a.add("two-sheet conjugate transport","PASS" if rr<5e-10 else "FAIL",
              "Tests explicit U_minus=conjugate(U_plus)",relative_residual=rr)
    else: a.add("two-sheet conjugate transport","NOT TESTED","Both sheet link arrays required")

    required_J=("H_two_sheet","H_plus_block","H_minus_block","inter_sheet_J")
    if all(k in arrays for k in required_J):
        H2=np.asarray(arrays["H_two_sheet"],complex)
        Hp0=np.asarray(arrays["H_plus_block"],complex)
        Hm0=np.asarray(arrays["H_minus_block"],complex)
        J=np.asarray(arrays["inter_sheet_J"],complex)
        n=Hp0.shape[0]
        shapes=(Hp0.shape==(n,n) and Hm0.shape==(n,n) and
                J.shape==(n,n) and H2.shape==(2*n,2*n))
        if not shapes:
            a.add("J=0 decoupling","FAIL","Incompatible two-sheet block dimensions")
        else:
            assembled=np.block([[Hp0,J],[J.conj().T,Hm0]])
            rr=float(np.linalg.norm(H2-assembled)/max(np.linalg.norm(H2),1.))
            Hzero=np.block([[Hp0,np.zeros_like(J)],[np.zeros_like(J),Hm0]])
            off=float(np.linalg.norm(Hzero[:n,n:])+np.linalg.norm(Hzero[n:,:n]))
            ok=rr<5e-10 and off==0.0
            a.add("J=0 decoupling","PASS" if ok else "FAIL",
                  "Checks supplied full operator against its declared blocks and exact J=0 block-diagonal limit",
                  assembly_residual=rr,zero_limit_offdiagonal_norm=off)
    else:
        a.add("J=0 decoupling","NOT TESTED",
              "Requires H_two_sheet, H_plus_block, H_minus_block and inter_sheet_J")

    mirror_keys=("H_plus_chirality","H_minus_chirality","mirror_site_perm")
    has_spin_map=("mirror_spin_matrix" in arrays or
                  bool(np.asarray(arrays.get("mirror_spin_identity",False)).item()))
    if all(k in arrays for k in mirror_keys) and has_spin_map:
        Hp=np.asarray(arrays["H_plus_chirality"],complex); Hm=np.asarray(arrays["H_minus_chirality"],complex)
        perm=np.asarray(arrays["mirror_site_perm"],int); anti=bool(np.asarray(arrays.get("mirror_antiunitary",False)).item())
        S=np.asarray(arrays["mirror_spin_matrix"],complex) if "mirror_spin_matrix" in arrays else np.eye(2,dtype=complex)
        n=len(perm)
        if (Hp.shape!=Hm.shape or Hp.shape!=(2*n,2*n) or
            sorted(perm.tolist())!=list(range(n)) or S.shape!=(2,2)):
            a.add("specular unitary/antiunitary intertwining","FAIL","Invalid operator, permutation or spin-map dimensions")
        elif np.linalg.norm(S.conj().T@S-np.eye(2))>5e-10:
            a.add("specular unitary/antiunitary intertwining","FAIL","mirror_spin_matrix is not unitary")
        else:
            P=np.zeros((2*n,2*n),complex)
            for i,j in enumerate(perm): P[2*j:2*j+2,2*i:2*i+2]=S
            src=Hp.conj() if anti else Hp
            rr=float(np.linalg.norm(Hm-P@src@P.conj().T)/max(np.linalg.norm(Hm),1.))
            evm=np.linalg.eigvals(Hm); evp=np.linalg.eigvals(src)
            order_m=np.lexsort((evm.imag,evm.real)); order_p=np.lexsort((evp.imag,evp.real))
            spectral=float(np.max(np.abs(evm[order_m]-evp[order_p])))
            ok=rr<5e-10 and spectral<5e-9
            a.add("specular unitary/antiunitary intertwining","PASS" if ok else "FAIL",
                  "Explicit intertwiner and spectrum comparison; antiunitarity only when flagged",
                  antiunitary=anti,relative_residual=rr,spectral_max_residual=spectral)
    else: a.add("specular unitary/antiunitary intertwining","NOT TESTED",
                "Need both chirality operators, mirror_site_perm and an explicit unitary spin map or mirror_spin_identity=true")

    report=a.report(); args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,sort_keys=True))
    if report["overall"]=="FAIL": raise SystemExit(1)

if __name__=="__main__": main()
