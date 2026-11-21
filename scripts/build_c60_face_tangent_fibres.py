#!/usr/bin/env python3
"""Construct the 32 actual faces of the truncated icosahedron (C60)."""
import json
from collections import Counter
from pathlib import Path
import argparse
import numpy as np
from scipy.spatial import ConvexHull
PHI=(1+np.sqrt(5.0))/2
def build():
    v=np.asarray([(0,a,b*PHI) for a in (-1,1) for b in (-1,1)]+[(a,b*PHI,0) for a in (-1,1) for b in (-1,1)]+[(a*PHI,0,b) for a in (-1,1) for b in (-1,1)],float)
    h=ConvexHull(v); edges=set()
    for tri in h.simplices:
        for i in range(3): edges.add(tuple(sorted((int(tri[i]),int(tri[(i+1)%3])))))
    if len(edges)!=30: raise AssertionError("base icosahedron must have 30 edges")
    pts=[]
    for a,b in sorted(edges): pts.extend(((2*v[a]+v[b])/3,(v[a]+2*v[b])/3))
    X=np.asarray(pts)
    if len(np.unique(np.round(X,12),axis=0))!=60: raise AssertionError("truncation must produce 60 distinct vertices")
    hull=ConvexHull(X); planes={}
    for eq in hull.equations:
        n=eq[:3]; d=eq[3]; q=np.linalg.norm(n); n=n/q; d=d/q
        key=tuple(np.round(np.r_[n,d],8)); planes[key]=(n,d)
    faces=[]
    for n,d in planes.values():
        ids=np.flatnonzero(np.abs(X@n+d)<1e-7)
        if len(ids) in (5,6): faces.append({"vertices":ids.astype(int).tolist(),"size":int(len(ids)),"normal":n.tolist(),"offset":float(d)})
    unique={tuple(f["vertices"]):f for f in faces}; faces=list(unique.values())
    sizes=Counter(f["size"] for f in faces)
    if len(faces)!=32 or sizes!={5:12,6:20}: raise AssertionError(f"expected 12 pentagons + 20 hexagons; got {len(faces)} / {dict(sizes)}")
    used=set(); pairs=[]; residual=0.
    for i,f in enumerate(faces):
        if i in used: continue
        n=np.asarray(f["normal"]); d=f["offset"]
        j=min((j for j in range(len(faces)) if j!=i),key=lambda j:np.linalg.norm(n+faces[j]["normal"])+abs(d+faces[j]["offset"]))
        r=float(np.linalg.norm(n+faces[j]["normal"])+abs(d+faces[j]["offset"]))
        if r>1e-6: raise AssertionError("opposite supporting face not found")
        residual=max(residual,r); used.update((i,j)); pairs.append([i,j])
    if len(pairs)!=16: raise AssertionError("expected 16 antipodal face pairs")
    return {"model":"truncated regular icosahedron (C60)","base_icosahedron_vertices":12,"base_icosahedron_edges":30,"truncated_vertices":len(X),"faces":len(faces),"face_size_counts":dict(sizes),"antipodal_face_pairs":pairs,"antipodal_pair_count":len(pairs),"max_antipodal_plane_residual":residual,"max_normal_unit_residual":float(max(abs(np.linalg.norm(f["normal"])-1) for f in faces)),"fibre_definition":"E_f = {v in R^3 : n_f dot v = 0}; dim(E_f)=2","total_fibre_dimension":2*len(faces),"face_records":faces,"scope":"Actual C60 face-fibre geometry only; no Q6 state action or intertwiner is asserted."}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--out",default="audits/C60_face_tangent_fibres.json");a=p.parse_args()
    r=build();Path(a.out).write_text(json.dumps(r,indent=2),encoding="utf-8")
    print(json.dumps({k:v for k,v in r.items() if k!="face_records"},indent=2))
