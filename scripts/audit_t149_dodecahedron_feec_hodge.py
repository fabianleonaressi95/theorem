#!/usr/bin/env python3
"""T149: regular dodecahedron vesica-pentagon Whitney/FEEC Hodge audit."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.linalg import eigvalsh

PHI=(1+np.sqrt(5.0))/2
Q6_CODES=np.asarray((3,5,58,60,9,17,46,54,33,6,57,30),dtype=int)
TOL=2e-9

def build():
    x=np.asarray([(0.,a,b*PHI) for a in (-1.,1.) for b in (-1.,1.)]+[(a,b*PHI,0.) for a in (-1.,1.) for b in (-1.,1.)]+[(a*PHI,0.,b) for a in (-1.,1.) for b in (-1.,1.)])
    hull=ConvexHull(x); eq={tuple(sorted(map(int,s))):e for s,e in zip(hull.simplices,hull.equations)}
    faces=sorted(eq); y=np.asarray([eq[f][:3]/(-eq[f][3]) for f in faces])
    dual_edges=[(i,j) for i,j in combinations(range(20),2) if len(set(faces[i])&set(faces[j]))==2]
    cycles=[]
    for v in range(12):
        inc=[i for i,f in enumerate(faces) if v in f]
        adj={i:[j for j in inc if j!=i and len(set(faces[i])&set(faces[j]))==2] for i in inc}
        assert len(inc)==5 and all(len(adj[i])==2 for i in inc)
        start=min(inc); cyc=[start]; prev=None; cur=start; nxt=min(adj[cur])
        while nxt!=start:
            cyc.append(nxt); prev,cur=cur,nxt; nxt=next(q for q in adj[cur] if q!=prev)
        assert len(cyc)==5; cycles.append(cyc)
    raw=np.linalg.norm(y[dual_edges[0][0]]-y[dual_edges[0][1]])
    scale=2*np.sin(np.pi/5)/raw; y*=scale
    vertices=np.vstack([y,np.asarray([y[c].mean(axis=0) for c in cycles])])
    triangles=[]
    for fi,cyc in enumerate(cycles):
        centre=20+fi
        for k in range(5):
            tri=(centre,cyc[k],cyc[(k+1)%5]); p=vertices[list(tri)]
            if np.dot(np.cross(p[1]-p[0],p[2]-p[0]),p.mean(axis=0))<0: tri=(centre,cyc[(k+1)%5],cyc[k])
            triangles.append(tri)
    eset=set()
    for tri in triangles:
        eset.update(tuple(sorted(e)) for e in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])))
    edges=sorted(eset); eidx={e:i for i,e in enumerate(edges)}
    n0,n1,n2=len(vertices),len(edges),len(triangles)
    D0=np.zeros((n1,n0)); D1=np.zeros((n2,n1)); M0=np.zeros((n0,n0)); M1=np.zeros((n1,n1)); M2=np.zeros((n2,n2))
    areas=[]; frame=[]
    for cyc in cycles:
        pts=y[cyc]; centre=pts.mean(axis=0); normal=centre/np.linalg.norm(centre)
        e1=pts[0]-centre; e1/=np.linalg.norm(e1); e2=np.cross(normal,e1)
        xy=np.asarray([[np.dot(p-centre,e1),np.dot(p-centre,e2)] for p in pts])
        ang=np.arctan2(xy[:,1],xy[:,0]); da=(np.diff(np.r_[ang,ang[0]])+np.pi)%(2*np.pi)-np.pi
        frame.append((np.ptp(np.linalg.norm(xy,axis=1)),np.ptp(np.linalg.norm(pts-np.roll(pts,-1,axis=0),axis=1)),np.max(np.abs(np.abs(da)-2*np.pi/5))))
    qpts=np.asarray([[2/3,1/6,1/6],[1/6,2/3,1/6],[1/6,1/6,2/3]])
    for ti,tri in enumerate(triangles):
        p=vertices[list(tri)]; E=np.column_stack([p[1]-p[0],p[2]-p[0]]); Gi=np.linalg.inv(E.T@E)
        g1=E@Gi[:,0]; g2=E@Gi[:,1]; grad=np.asarray([-g1-g2,g1,g2])
        area=np.sqrt(np.linalg.det(E.T@E))/2; areas.append(area)
        M0[np.ix_(tri,tri)]+=area/12*(np.ones((3,3))+np.eye(3))
        pairs=((0,1),(1,2),(2,0)); ids=[]; signs=[]
        for a,b in pairs:
            key=tuple(sorted((tri[a],tri[b]))); ei=eidx[key]; sg=1 if (tri[a],tri[b])==key else -1
            ids.append(ei); signs.append(sg); D0[ei,key[0]]=-1; D0[ei,key[1]]=1; D1[ti,ei]+=sg
        w=np.asarray([[lam[a]*grad[b]-lam[b]*grad[a] for a,b in pairs] for lam in qpts])
        loc=np.einsum('qia,qja->ij',w,w)*area/3
        for a in range(3):
            for b in range(3): M1[ids[a],ids[b]]+=signs[a]*signs[b]*loc[a,b]
        M2[ti,ti]=1/area
    K0=D0.T@M1@D0; lam0=eigvalsh(K0,M0)
    K1=M1@D0@np.linalg.solve(M0,D0.T@M1)+D1.T@M2@D1; lam1=eigvalsh(K1,M1)
    lam2=np.sort(np.real_if_close(np.linalg.eigvals(D1@np.linalg.solve(M1,D1.T@M2))).real)
    B=np.zeros((20,64))
    for i,f in enumerate(faces):
        for v in f: B[i,Q6_CODES[v]]+=1/3
    P=np.vstack([B,np.asarray([B[c].mean(axis=0) for c in cycles])])
    L6=np.zeros((64,64))
    for s in range(64):
        for bit in range(6): L6[s,s]+=1; L6[s,s^(1<<bit)]-=1
    C=np.asarray([np.ones(8)/np.sqrt(8),np.asarray([7,1,-3,-5,-5,-3,-1,7])/np.sqrt(168),np.asarray([1,-1,-1,1,-1,1,1,-1])/np.sqrt(8)])
    # Exact archived coisometry rows (the second row's signs are [7,1,-3,-5,-5,-3,1,7]).
    C[1]=np.asarray([7,1,-3,-5,-5,-3,1,7])/np.sqrt(168)
    Es=np.zeros((9,3)); Es[0,0]=1; Es[1,1]=Es[3,1]=1/np.sqrt(2); Es[2,2]=Es[6,2]=1/np.sqrt(2)
    KK=np.kron(C,C); F=np.zeros((3,64))
    for code in range(64):
        lo,hi=code&7,(code>>3)&7; F[:,code]=Es.T@KK[:,lo*8+hi]
    Phi=F@P.T; Lfe=np.linalg.solve(M0,K0); Lam=np.diag([0.,4.,6.])
    return {"vertices":n0,"edges":n1,"triangles":n2,"dodeca_edges":len(dual_edges),"pentagons":len(cycles),
      "scale":float(scale),"dodeca_edge_length":float(2*np.sin(np.pi/5)),
      "triangle_area":float(np.mean(areas)),"pentagon_area":float(5*np.mean(areas)),
      "frame_max_residuals":np.max(frame,axis=0).tolist(),"boundary_squared_residual":float(np.linalg.norm(D1@D0)),
      "rank_D0":int(np.linalg.matrix_rank(D0)),"rank_D1":int(np.linalg.matrix_rank(D1)),"euler_characteristic":int(n0-n1+n2),
      "M0_eigenvalue_bounds":np.linalg.eigvalsh(M0)[[0,-1]].tolist(),"M1_eigenvalue_bounds":np.linalg.eigvalsh(M1)[[0,-1]].tolist(),"M2_eigenvalue_bounds":np.linalg.eigvalsh(M2)[[0,-1]].tolist(),
      "lambda0":lam0.tolist(),"lambda1_first12":lam1[:12].tolist(),"lambda2_first12":lam2[:12].tolist(),
      "q6_map_rank":int(np.linalg.matrix_rank(P)),"q6_sector_intertwiner_residual":float(np.linalg.norm(Lam@Phi-Phi@Lfe)),
      "q6_original_intertwiner_residual":float(np.linalg.norm(F@L6-Lam@F)),"q6_pulled_energy_eigenvalues":np.linalg.eigvalsh(P@L6@P.T).tolist()}

def main():
    r=build()
    assert (r["vertices"],r["edges"],r["triangles"])==(32,90,60)
    assert r["euler_characteristic"]==2 and (r["rank_D0"],r["rank_D1"])==(31,59)
    assert r["boundary_squared_residual"]<TOL and max(r["frame_max_residuals"])<TOL
    assert min(r["M0_eigenvalue_bounds"]+r["M1_eigenvalue_bounds"]+r["M2_eigenvalue_bounds"])>0
    assert r["q6_map_rank"]==12 and r["q6_original_intertwiner_residual"]<TOL
    assert r["q6_sector_intertwiner_residual"]>1e-2
    out=Path("results/json/dodecahedron_feec_hodge_t149.json"); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(r,indent=2)+"\n"); print(json.dumps(r,indent=2))
if __name__=="__main__": main()
