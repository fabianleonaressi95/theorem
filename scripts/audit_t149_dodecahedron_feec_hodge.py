#!/usr/bin/env python3
"""T149: supergolden and regular-control Whitney--FEEC Hodge audit."""
from __future__ import annotations
from itertools import combinations, permutations
from pathlib import Path
import json
import numpy as np
from scipy.spatial import ConvexHull
from scipy.linalg import eigvalsh

PSI_SG=1.465571231876768
PHI=(1+np.sqrt(5.0))/2
CODES=np.asarray((3,5,58,60,9,17,46,54,33,6,57,30),dtype=int)
TOL=2e-9

def build_case(t, supergolden):
    x=np.asarray([(0.,a,b*t) for a in (-1.,1.) for b in (-1.,1.)]+[(a,b*t,0.) for a in (-1.,1.) for b in (-1.,1.)]+[(a*t,0.,b) for a in (-1.,1.) for b in (-1.,1.)])
    hull=ConvexHull(x); eq={tuple(sorted(map(int,s))):e for s,e in zip(hull.simplices,hull.equations)}
    faces=sorted(eq); y0=np.asarray([eq[f][:3]/(-eq[f][3]) for f in faces])
    av=[]
    for p in x:
        hits=np.flatnonzero(np.linalg.norm(x+p,axis=1)<1e-8)
        assert len(hits)==1; av.append(int(hits[0]))
    av=np.asarray(av); fi={f:i for i,f in enumerate(faces)}
    af=np.asarray([fi[tuple(sorted(av[list(f)]))] for f in faces])
    dedges=[(i,j) for i,j in combinations(range(20),2) if len(set(faces[i])&set(faces[j]))==2]
    cycles=[]
    for v in range(12):
        inc=[i for i,f in enumerate(faces) if v in f]
        adj={i:[j for j in inc if j!=i and len(set(faces[i])&set(faces[j]))==2] for i in inc}
        assert len(inc)==5 and all(len(adj[i])==2 for i in inc)
        start=min(inc); cyc=[start]; prev=None; cur=start; nxt=min(adj[cur])
        while nxt!=start:
            cyc.append(nxt); prev,cur=cur,nxt; nxt=next(q for q in adj[cur] if q!=prev)
        cycles.append(cyc)
    scale=1.
    if not supergolden:
        raw=np.linalg.norm(y0[dedges[0][0]]-y0[dedges[0][1]])
        scale=2*np.sin(np.pi/5)/raw
    y=scale*y0; V=np.vstack([y,np.asarray([y[c].mean(axis=0) for c in cycles])])
    tris=[]
    for f,cyc in enumerate(cycles):
        c=20+f
        for k in range(5):
            tri=(c,cyc[k],cyc[(k+1)%5]); p=V[list(tri)]
            if np.dot(np.cross(p[1]-p[0],p[2]-p[0]),p.mean(axis=0))<0: tri=(c,cyc[(k+1)%5],cyc[k])
            tris.append(tri)
    eset=set()
    for tri in tris: eset.update(tuple(sorted(e)) for e in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])))
    edges=sorted(eset); ei={e:i for i,e in enumerate(edges)}
    n0,n1,n2=len(V),len(edges),len(tris)
    D0=np.zeros((n1,n0)); D1=np.zeros((n2,n1)); M0=np.zeros((n0,n0)); M1=np.zeros((n1,n1)); M2=np.zeros((n2,n2))
    areas=[]; frame=[]; qpts=np.asarray([[2/3,1/6,1/6],[1/6,2/3,1/6],[1/6,1/6,2/3]])
    for cyc in cycles:
        pts=y[cyc]; c=pts.mean(axis=0); n=c/np.linalg.norm(c); e1=pts[0]-c; e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
        xy=np.asarray([[np.dot(p-c,e1),np.dot(p-c,e2)] for p in pts]); ang=np.arctan2(xy[:,1],xy[:,0])
        da=(np.diff(np.r_[ang,ang[0]])+np.pi)%(2*np.pi)-np.pi
        frame.append([np.ptp(np.linalg.norm(xy,axis=1)),np.ptp(np.linalg.norm(pts-np.roll(pts,-1,axis=0),axis=1)),np.max(np.abs(np.abs(da)-2*np.pi/5))])
    for ti,tri in enumerate(tris):
        p=V[list(tri)]; E=np.column_stack([p[1]-p[0],p[2]-p[0]]); Gi=np.linalg.inv(E.T@E)
        g1=E@Gi[:,0]; g2=E@Gi[:,1]; grad=np.asarray([-g1-g2,g1,g2])
        A=np.sqrt(np.linalg.det(E.T@E))/2; areas.append(A)
        M0[np.ix_(tri,tri)]+=A/12*(np.ones((3,3))+np.eye(3))
        pairs=((0,1),(1,2),(2,0)); ids=[]; signs=[]
        for a,b in pairs:
            key=tuple(sorted((tri[a],tri[b]))); k=ei[key]; sg=1 if (tri[a],tri[b])==key else -1
            ids.append(k); signs.append(sg); D0[k,key[0]]=-1; D0[k,key[1]]=1; D1[ti,k]+=sg
        w=np.asarray([[lam[a]*grad[b]-lam[b]*grad[a] for a,b in pairs] for lam in qpts])
        loc=np.einsum('qia,qja->ij',w,w)*A/3
        for a in range(3):
            for b in range(3): M1[ids[a],ids[b]]+=signs[a]*signs[b]*loc[a,b]
        # Normalized Whitney 2-form has integral 1, hence squared L2 norm 1/A.
        M2[ti,ti]=1/A
    anti0=np.asarray([af[i] for i in range(20)]+[20+av[v] for v in range(12)])
    S0=np.zeros((n0,n0))
    for i,j in enumerate(anti0): S0[j,i]=1
    S1=np.zeros((n1,n1))
    for i,(a,b) in enumerate(edges):
        aa,bb=anti0[a],anti0[b]; key=tuple(sorted((aa,bb)))
        S1[ei[key],i]=1 if (aa,bb)==key else -1
    ti={frozenset(tri):i for i,tri in enumerate(tris)}; S2=np.zeros((n2,n2))
    for i,tri in enumerate(tris):
        mapped=[anti0[v] for v in tri]; j=ti[frozenset(mapped)]; target=tris[j]
        perm=[target.index(v) for v in mapped]; inv=sum(perm[a]>perm[b] for a in range(3) for b in range(a+1,3))
        S2[j,i]=(-1)**inv
    K0=D0.T@M1@D0
    K1=M1@D0@np.linalg.solve(M0,D0.T@M1)+D1.T@M2@D1
    L2=D1@np.linalg.solve(M1,D1.T@M2)
    spec={"0":eigvalsh(K0,M0).tolist(),"1":eigvalsh(K1,M1).tolist(),"2":np.sort(np.real_if_close(np.linalg.eigvals(L2)).real).tolist()}
    parity={}
    for d,(S,M,K) in enumerate(((S0,M0,K0),(S1,M1,K1),(S2,M2,M2@L2))):
        vals,U=np.linalg.eigh(S); parity[str(d)]={}
        for sign in (-1,1):
            Q=U[:,np.abs(vals-sign)<1e-7]; parity[str(d)][str(sign)]=eigvalsh(Q.T@K@Q,Q.T@M@Q).tolist()
    Kvv=K0[:20,:20]; Kvc=K0[:20,20:]; Kcc=K0[20:,20:]
    H=np.vstack([np.eye(20),-np.linalg.solve(Kcc,Kvc.T)])
    schur=eigvalsh(H.T@K0@H,H.T@M0@H)
    out={"parameter":float(t),"label":"supergolden" if supergolden else "regular_control","scale":float(scale),
      "counts":[n0,n1,n2],"euler_characteristic":int(n0-n1+n2),
      "incidence_ranks":[int(np.linalg.matrix_rank(D0)),int(np.linalg.matrix_rank(D1))],
      "incidence_residuals":[float(np.linalg.norm(D1@D0)),float(np.linalg.norm(D0@S0-S1@D0)),float(np.linalg.norm(D1@S1-S2@D1))],
      "antipodal_mass_residuals":[float(np.linalg.norm(S0.T@M0@S0-M0)),float(np.linalg.norm(S1.T@M1@S1-M1)),float(np.linalg.norm(S2.T@M2@S2-M2))],
      "antipodal_involution_residuals":[float(np.linalg.norm(S@S-np.eye(len(S)))) for S in (S0,S1,S2)],
      "frame_residuals":np.max(frame,axis=0).tolist(),"mean_triangle_area":float(np.mean(areas)),"mean_pentagon_area":float(5*np.mean(areas)),
      "mass_eigenvalue_bounds":[np.linalg.eigvalsh(M)[[0,-1]].tolist() for M in (M0,M1,M2)],
      "spectra":spec,"parity_spectra":parity,"schur_spectrum":schur.tolist(),
      "schur_mass":"H^T M0 H; H=[I;-Kcc^{-1}Kcv]"}
    if supergolden:
        B=np.zeros((20,64))
        for i,f in enumerate(faces):
            for v in f: B[i,CODES[v]]+=1/3
        L6=np.zeros((64,64))
        for s in range(64):
            for bit in range(6): L6[s,s]+=1; L6[s,s^(1<<bit)]-=1
        qe=[]; qi={}
        for s in range(64):
            for bit in range(6):
                z=s^(1<<bit)
                if s<z: qi[(s,z)]=len(qe); qe.append((s,z))
        C1=np.zeros((192,30)); D=np.zeros((20,30))
        for k,(i,j) in enumerate(dedges):
            D[i,k]=-1; D[j,k]=1
            a=next(iter(set(faces[i])-set(faces[j]))); b=next(iter(set(faces[j])-set(faces[i])))
            src,dst=CODES[a],CODES[b]; bits=[q for q in range(6) if ((src^dst)>>q)&1]
            for order in permutations(bits):
                cur=src
                for bit in order:
                    nxt=cur^(1<<bit); key=tuple(sorted((cur,nxt)))
                    C1[qi[key],k]+=1/(3*math_factorial(len(bits)))*(1 if cur<nxt else -1); cur=nxt
        Lpull=B@L6@B.T; Lchain=D@C1.T@C1@D.T
        C=np.asarray([np.ones(8)/np.sqrt(8),np.asarray([7,1,-3,-5,-5,-3,1,7])/np.sqrt(168),np.asarray([1,-1,-1,1,-1,1,1,-1])/np.sqrt(8)])
        Es=np.zeros((9,3)); Es[0,0]=1; Es[1,1]=Es[3,1]=1/np.sqrt(2); Es[2,2]=Es[6,2]=1/np.sqrt(2)
        KK=np.kron(C,C); F=np.zeros((3,64))
        for code in range(64):
            lo,hi=code&7,(code>>3)&7; F[:,code]=Es.T@KK[:,lo*8+hi]
        Phi=F@B.T; Lam=np.diag([0.,4.,6.])
        out["q6_comparison"]={"barycentre_map_rank":int(np.linalg.matrix_rank(B)),
          "pull_spectrum":np.linalg.eigvalsh(Lpull).tolist(),"chain_spectrum":np.linalg.eigvalsh(Lchain).tolist(),
          "pull_intertwiner_residual":float(np.linalg.norm(Lam@Phi-Phi@Lpull)),
          "chain_intertwiner_residual":float(np.linalg.norm(Lam@Phi-Phi@Lchain)),
          "original_q6_sector_residual":float(np.linalg.norm(F@L6-Lam@F))}
    return out

def math_factorial(n):
    return 1 if n<2 else n*math_factorial(n-1)

def build_report():
    return {"supergolden":build_case(PSI_SG,True),"regular_control":build_case(PHI,False)}

def main():
    report=build_report()
    for c in report.values():
        assert c["counts"]==[32,90,60] and c["euler_characteristic"]==2
        assert c["incidence_ranks"]==[31,59]
        assert max(c["incidence_residuals"])<TOL
        assert max(c["antipodal_mass_residuals"])<TOL
        assert max(c["antipodal_involution_residuals"])<TOL
        assert min(v[0] for v in c["mass_eigenvalue_bounds"])>0
    q=report["supergolden"]["q6_comparison"]
    assert q["original_q6_sector_residual"]<TOL
    assert q["pull_intertwiner_residual"]>1e-2 and q["chain_intertwiner_residual"]>1e-2
    path=Path("results/json/t149_supergolden_dodecahedron_feec_hodge.json")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
