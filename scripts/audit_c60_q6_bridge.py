#!/usr/bin/env python3
"""Exact rational homology audit for C60, the declared Kathara disk, and Q6.

Kathara and Q6 incidence conventions are transcribed from the canonical
implementations in fabianleonaressi95/rgs-qlg-quaternion-bridge at commit
99ea9b9e4cb42d683073e02b64e8d94b9f144968. This script independently rebuilds
their integer boundary matrices and computes ranks over Q.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from fractions import Fraction
import numpy as np
from audit_c60_stone_wales import c60_ideal, graph_from_bonds, oriented_faces, boundary

K_LINES = {
    1:(1,2,5,8,11,12), 2:(3,6,9), 3:(4,7,10),
    4:(1,3), 5:(2,3), 6:(1,4), 7:(2,4),
    8:(9,12), 9:(9,11), 10:(10,12), 11:(10,11),
    12:(8,9), 13:(8,10), 14:(5,6), 15:(5,7)
}
K_FACES = (
    (1,2,3), (1,4,2), (2,4,7,5), (2,5,6,3),
    (5,7,10,8), (5,8,9,6), (8,10,11), (8,11,9),
    (9,11,12), (10,12,11)
)


def exact_rank(matrix: np.ndarray) -> int:
    a = [[Fraction(int(x)) for x in row] for row in np.asarray(matrix).tolist()]
    if not a: return 0
    m,n=len(a),len(a[0]); rank=0
    for col in range(n):
        pivot=next((r for r in range(rank,m) if a[r][col] != 0),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        p=a[rank][col]; a[rank]=[x/p for x in a[rank]]
        for r in range(m):
            if r != rank and a[r][col] != 0:
                q=a[r][col]
                a[r]=[x-q*y for x,y in zip(a[r],a[rank])]
        rank += 1
        if rank == m: break
    return rank


def homology_report(n0,n1,n2,b1,b2):
    r1,r2=exact_rank(b1),exact_rank(b2)
    return {
        "cell_counts_C0_C1_C2":[n0,n1,n2],
        "boundary_shapes":{"B1":list(b1.shape),"B2":list(b2.shape)},
        "boundary_ranks_over_Q":{"rank_B1":r1,"rank_B2":r2},
        "betti_numbers":{"beta0":n0-r1,"beta1":n1-r1-r2,"beta2":n2-r2},
        "euler_characteristic":n0-n1+n2,
        "boundary_squared_zero":bool(np.all(b1@b2==0))
    }


def build_kathara():
    vertices=tuple(range(1,13))
    edges=tuple(sorted({tuple(sorted((u,v))) for path in K_LINES.values()
                        for u,v in zip(path,path[1:])}))
    edge_index={e:i for i,e in enumerate(edges)}
    b1=np.zeros((12,len(edges)),dtype=np.int64)
    for j,(u,v) in enumerate(edges): b1[u-1,j],b1[v-1,j]=-1,1
    b2=np.zeros((len(edges),len(K_FACES)),dtype=np.int64)
    for j,face in enumerate(K_FACES):
        for u,v in zip(face,face[1:]+face[:1]):
            e=tuple(sorted((u,v)))
            b2[edge_index[e],j]=1 if (u,v)==e else -1
    return vertices,edges,K_FACES,b1,b2


def build_q6():
    vertices=tuple(range(64))
    def mask(axis): return 1 << (5-axis)
    edges=tuple(sorted((v,v^mask(a)) for v in vertices for a in range(6)
                       if v < (v^mask(a))))
    edge_index={e:i for i,e in enumerate(edges)}
    b1=np.zeros((64,len(edges)),dtype=np.int64)
    for j,(u,v) in enumerate(edges): b1[u,j],b1[v,j]=-1,1
    faces=[]
    for a in range(6):
        for b in range(a+1,6):
            ma,mb=mask(a),mask(b)
            for v in vertices:
                if v&ma or v&mb: continue
                va,vab,vb=v^ma,(v^ma)^mb,v^mb
                faces.append((v,va,vab,vb))
    faces=tuple(faces)
    b2=np.zeros((len(edges),len(faces)),dtype=np.int64)
    for j,face in enumerate(faces):
        for u,v in zip(face,face[1:]+face[:1]):
            b2[edge_index[tuple(sorted((u,v)))],j]=1 if u<v else -1
    return vertices,edges,faces,b1,b2


def audit():
    xyz,bonds=c60_ideal()
    c60=graph_from_bonds(len(xyz),bonds)
    c60_faces=oriented_faces(c60)
    c60_edges,b1c,b2c=boundary(c60,c60_faces)
    kv,ke,kf,b1k,b2k=build_kathara()
    qv,qe,qf,b1q,b2q=build_q6()
    reports={
        "C60":homology_report(c60.number_of_nodes(),len(c60_edges),len(c60_faces),b1c,b2c),
        "Kathara":homology_report(len(kv),len(ke),len(kf),b1k,b2k),
        "Q6":homology_report(len(qv),len(qe),len(qf),b1q,b2q)
    }
    return {
        "status":"exact_rational_homology_three_complexes",
        "source_commit":"99ea9b9e4cb42d683073e02b64e8d94b9f144968",
        "complexes":reports,
        "q6_graph_cycle_rank":len(qe)-len(qv)+1,
        "homological_obstruction":(
            "H2(C60;Q)=Q but H2(Kathara;Q)=0. Every chain map C60 -> Kathara "
            "therefore induces the zero map on H2; every composite C60 -> "
            "Kathara -> Q6 kills the C60 fundamental class. A direct C60 -> "
            "Q6 map is not ruled out by this argument."
        ),
        "existing_kathara_q6_maps":{
            "Gate_C":"R2=0: valid integral chain map but collapses all 10 source faces.",
            "Gate_D":"Non-degenerate integral face lift; R2 has 10 columns and rank 10 mod 1,000,003; exact chain identities are checked in source implementation.",
            "canonicality":"The declared axis order is combinatorial, not RGS-metric canonical."
        },
        "c60_to_kathara_required_maps":{
            "P0_shape":[12,60],"P1_shape":[21,90],"P2_shape":[10,32],
            "identities":["B1_K P1 = P0 B1_C60","B2_K P2 = P1 B2_C60"],
            "status":"open; no canonical cell assignment or map constructed"
        },
        "sw_intertwiner_status":"open; requires an explicit action on the Kathara/Q6 side and a commuting square."
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",default="c60_q6_bridge_audit.json")
    args=parser.parse_args()
    result=audit()
    Path(args.out).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":
    main()
