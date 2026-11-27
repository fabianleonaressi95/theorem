#!/usr/bin/env python3
"""C60 Stone-Wales 90-degree graph switch, chain map and geometry audit."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from collections import defaultdict
import networkx as nx
import numpy as np
from audit_c60_mmff94s_relaxed_coulomb import c60_ideal, mmff_relax

def graph_from_bonds(n,bonds):
    g=nx.Graph(); g.add_nodes_from(range(n)); g.add_edges_from(bonds); return g

def oriented_faces(g):
    planar,emb=nx.check_planarity(g)
    if not planar: raise ValueError("non-planar graph")
    marked=set(); faces=[]
    for u in sorted(g):
        for v in sorted(g[u]):
            if (u,v) not in marked:
                f=emb.traverse_face(u,v,mark_half_edges=marked)
                k=f.index(min(f)); faces.append(tuple(f[k:]+f[:k]))
    return sorted(faces,key=lambda f:(len(f),f))

def incidence(faces):
    d=defaultdict(list)
    for i,f in enumerate(faces):
        for u,v in zip(f,f[1:]+f[:1]): d[tuple(sorted((u,v)))].append(i)
    if any(len(x)!=2 for x in d.values()): raise ValueError("edge-face incidence != 2")
    return d

def topology(g,faces):
    z=[len(f) for f in faces]
    return {"V":g.number_of_nodes(),"E":g.number_of_edges(),"F":len(faces),
      "pentagons":z.count(5),"hexagons":z.count(6),
      "other_face_sizes":sorted(q for q in z if q not in (5,6)),
      "degrees":sorted(dict(g.degree()).values()),
      "euler":g.number_of_nodes()-g.number_of_edges()+len(faces)}

def enumerate_switches(g,faces):
    # The SW_5|6 operation is a single diagonal flip in the triangulated
    # fullerene dual. Dual vertices are direct-graph faces; dual triangles
    # are direct-graph carbon atoms.
    ef=incidence(faces)
    dual=nx.Graph(); dual.add_nodes_from(range(len(faces)))
    for fs in ef.values(): dual.add_edge(*fs)
    if any(len(f)!=3 for f in oriented_faces(dual)):
        raise ValueError("fullerene dual is not a triangulation")
    atom_tri={}
    for v in g:
        incident=tuple(sorted(i for i,f in enumerate(faces) if v in f))
        if len(incident)!=3: raise ValueError("direct vertex not trivalent")
        atom_tri[incident]=v
    found={}
    for h1,h2 in sorted(dual.edges()):
        if dual.degree[h1]!=6 or dual.degree[h2]!=6: continue
        opposite=sorted(set(dual[h1]) & set(dual[h2]))
        if len(opposite)!=2: continue
        p1,p2=opposite
        if dual.degree[p1]!=5 or dual.degree[p2]!=5: continue
        if dual.has_edge(p1,p2): continue
        b=atom_tri.get(tuple(sorted((h1,h2,p1))))
        c=atom_tri.get(tuple(sorted((h1,h2,p2))))
        if b is None or c is None: continue
        d2=dual.copy(); d2.remove_edge(h1,h2); d2.add_edge(p1,p2)
        try: tri_faces=oriented_faces(d2)
        except ValueError: continue
        if len(tri_faces)!=60 or any(len(t)!=3 for t in tri_faces): continue
        tri_to_atom={}
        new1=tuple(sorted((p1,p2,h1))); new2=tuple(sorted((p1,p2,h2)))
        for tri in tri_faces:
            key=tuple(sorted(tri))
            if key in atom_tri: tri_to_atom[key]=atom_tri[key]
            elif key==new1: tri_to_atom[key]=b
            elif key==new2: tri_to_atom[key]=c
        if len(tri_to_atom)!=60 or len(set(tri_to_atom.values()))!=60: continue
        edge_tri=defaultdict(list)
        for tri in tri_faces:
            key=tuple(sorted(tri))
            for u,v in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
                edge_tri[tuple(sorted((u,v)))].append(key)
        h=nx.Graph(); h.add_nodes_from(range(60))
        valid=True
        for ts in edge_tri.values():
            if len(ts)!=2: valid=False; break
            h.add_edge(tri_to_atom[ts[0]],tri_to_atom[ts[1]])
        if not valid: continue
        try: hf=oriented_faces(h)
        except ValueError: continue
        t=topology(h,hf)
        if (t["V"],t["E"],t["F"],t["pentagons"],t["hexagons"],t["other_face_sizes"],t["euler"]) != (60,90,32,12,20,[],2): continue
        removed=sorted(set(tuple(sorted(e)) for e in g.edges())-set(tuple(sorted(e)) for e in h.edges()))
        added=sorted(set(tuple(sorted(e)) for e in h.edges())-set(tuple(sorted(e)) for e in g.edges()))
        if len(removed)!=2 or len(added)!=2: continue
        key=tuple(sorted(h.edges()))
        found.setdefault(key,{"dual_edge":[h1,h2],"opposite_pentagon_faces":[p1,p2],
          "rotated_carbon_vertices":[b,c],"removed_edges":[list(e) for e in removed],
          "added_edges":[list(e) for e in added],"graph":h,"faces":hf})
    return [found[k] for k in sorted(found)]

def boundary(g,faces):
    edges=sorted(tuple(sorted(e)) for e in g.edges()); ix={e:i for i,e in enumerate(edges)}
    b1=np.zeros((g.number_of_nodes(),len(edges)),dtype=np.int64)
    for j,(u,v) in enumerate(edges): b1[u,j]=-1; b1[v,j]=1
    b2=np.zeros((len(edges),len(faces)),dtype=np.int64)
    for j,f in enumerate(faces):
        for u,v in zip(f,f[1:]+f[:1]): b2[ix[tuple(sorted((u,v)))],j]+=1 if u<v else -1
    if np.any(b1@b2): raise ValueError("boundary squared nonzero")
    return edges,b1,b2

def make_chain_map(g,fg,h,fh):
    oe,ob1,ob2=boundary(g,fg); ne,nb1,nb2=boundary(h,fh); ni={e:i for i,e in enumerate(ne)}
    s1=np.zeros((len(ne),len(oe)),dtype=np.int64)
    for j,(u,v) in enumerate(oe):
        path=[u,v] if h.has_edge(u,v) else nx.shortest_path(h,u,v)
        for a,b in zip(path,path[1:]): s1[ni[tuple(sorted((a,b)))],j]+=1 if a<b else -1
    if not np.array_equal(nb1@s1,ob1): raise ValueError("B1' S1 != B1")
    target=s1@ob2; s2=np.zeros((len(fh),len(fg)),dtype=np.int64)
    for j in range(len(fg)):
        x=np.linalg.lstsq(nb2.astype(float),target[:,j].astype(float),rcond=None)[0]
        x=np.rint(x-x[0]).astype(np.int64)
        if not np.array_equal(nb2@x,target[:,j]): raise ValueError("no integral 2-chain filling for face "+str(j))
        s2[:,j]=x
    if not np.array_equal(nb2@s2,s1@ob2): raise ValueError("B2' S2 != S1 B2")
    return {"B1S1_equals_B1":True,"B2S2_equals_S1B2":True,
      "S1_shape":list(s1.shape),"S2_shape":list(s2.shape),
      "S1_rank":int(np.linalg.matrix_rank(s1)),"S2_rank":int(np.linalg.matrix_rank(s2)),
      "S1":s1.tolist(),"S2":s2.tolist()}

def cov(x,ids=None):
    y=np.asarray(x,float).copy()
    if ids is not None: y=y[sorted(ids)]
    y-=y.mean(axis=0); q=y.T@y/len(y); ev=np.linalg.eigvalsh(q)
    return {"matrix":q.tolist(),"eigenvalues":ev.tolist(),
      "anisotropy":float((ev[-1]-ev[0])/(ev[-1]+ev[0]))}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--out-dir",default="c60_stone_wales_audit")
    p.add_argument("--relax",action="store_true"); p.add_argument("--max-iterations",type=int,default=10000)
    a=p.parse_args(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    xyz,bonds=c60_ideal(); g=graph_from_bonds(len(xyz),bonds); fg=oriented_faces(g); t0=topology(g,fg)
    if (t0["V"],t0["E"],t0["F"],t0["pentagons"],t0["hexagons"],t0["euler"])!=(60,90,32,12,20,2) or set(t0["degrees"])!={3}:
        raise RuntimeError("initial C60 topology failed: "+str(t0))
    cs=enumerate_switches(g,fg)
    if not cs: raise RuntimeError("no admissible planar SW_5|6 dual-edge-flip switch found")
    c=cs[0]; h,fh=c["graph"],c["faces"]; t1=topology(h,fh)
    chain=make_chain_map(g,fg,h,fh)
    report={"status":"computed_graph_audit","operation":"dual edge flip / equivalent direct-graph 2-switch; Stone-Wales dual diagonal flip; direct graph changes by a degree-preserving 2-switch",
      "distinct_admissible_postgraphs":len(cs),"selected_switch":{k:v for k,v in c.items() if k not in ("graph","faces")},
      "before":t0,"after":t1,"chain_map":{k:v for k,v in chain.items() if k not in ("S1","S2")},
      "limitations":["Topological switch, not an atomistic transition-state trajectory.",
       "Chain-map path and filling choices are not unique and do not establish an embedding isotopy.",
       "Nuclear-coordinate covariance is not electron-density covariance.",
       "MMFF94s is empirical molecular mechanics, not DFT or experiment.","No Kathara/Q6 map is constructed."]}
    if a.relax:
        x0,m0=mmff_relax(xyz,bonds,a.max_iterations)
        x1,m1=mmff_relax(xyz,sorted(h.edges()),a.max_iterations)
        patch=set()
    report={
      "status":"computed_graph_audit",
      "operation":"Stone-Wales dual diagonal flip; direct graph changes by a degree-preserving 2-switch",
      "distinct_admissible_postgraphs":len(cs),
      "selected_switch":{k:v for k,v in c.items() if k not in ("graph","faces")},
      "before":t0,"after":t1,
      "chain_map":{k:v for k,v in chain.items() if k not in ("S1","S2")},
      "limitations":[
        "Topological switch, not an atomistic transition-state trajectory.",
        "Chain-map path and filling choices are not unique and do not establish an embedding isotopy.",
        "Nuclear-coordinate covariance is not electron-density covariance.",
        "MMFF94s is empirical molecular mechanics, not DFT or experiment.",
        "No Kathara/Q6 map is constructed."
      ]
    }
    if a.relax:
        x0,m0=mmff_relax(xyz,bonds,a.max_iterations)
        x1,m1=mmff_relax(xyz,sorted(h.edges()),a.max_iterations)
        patch=set(c["rotated_carbon_vertices"])
        for e in c["removed_edges"]+c["added_edges"]: patch.update(e)
        for v in list(patch): patch.update(g[v]); patch.update(h[v])
        report["mmff94s"]={"before_model":m0,"after_model":m1,
          "nuclear_covariance_before":cov(x0),"nuclear_covariance_after":cov(x1),
          "patch_vertices":sorted(patch),"patch_covariance_before":cov(x0,patch),
          "patch_covariance_after":cov(x1,patch)}
    np.savez_compressed(out/"C60_Stone_Wales_graphs.npz",X_ideal=xyz,
      bonds_before=np.asarray(sorted(g.edges()),int),bonds_after=np.asarray(sorted(h.edges()),int))
    (out/"report.json").write_text(json.dumps(report,indent=2)+"\\n")
    (out/"report.md").write_text("# C60 Stone-Wales graph audit\\n\\n"+
      "Admissible distinct postgraphs: "+str(len(cs))+"\\n\\n"+
      "Before: "+str(t0)+"\\n\\nAfter: "+str(t1)+"\\n\\n"+
      "Both cellular chain-map identities verified exactly over integers.\\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
