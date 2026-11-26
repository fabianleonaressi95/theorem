#!/usr/bin/env python3
"""Non-degenerate integral chain map from spherical Kathara completion to Q6.

The standard Kathara audit fills only ten bounded faces and is a disk. Here we
also attach the outer 8-gon of the declared planar rotation system, obtaining
a closed 2-sphere cellulation with 11 faces. This is an explicit completion,
not a silent change to the original ten-face convention.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from math import atan2
from collections import defaultdict
import numpy as np

COORDS = {
    1:(0,0),2:(0,1),3:(-2,2),4:(2,2),5:(0,3),6:(-2,4),
    7:(2,4),8:(0,5),9:(-2,6),10:(2,6),11:(0,7),12:(0,8)
}
LINES = {
    1:(1,2,5,8,11,12),2:(3,6,9),3:(4,7,10),
    4:(1,3),5:(2,3),6:(1,4),7:(2,4),8:(9,12),
    9:(9,11),10:(10,12),11:(10,11),12:(8,9),
    13:(8,10),14:(5,6),15:(5,7)
}
BOUNDED_FACES = {
    frozenset(f) for f in (
        (1,2,3),(1,4,2),(2,4,7,5),(2,5,6,3),(5,7,10,8),
        (5,8,9,6),(8,10,11),(8,11,9),(9,11,12),(10,12,11)
    )
}
AXIS_ORDER = (1,2,0,3,4,5)
AXIS_POSITION = {axis:i for i,axis in enumerate(AXIS_ORDER)}
PRIME = 1_000_003


def kathara_edges():
    return tuple(sorted({tuple(sorted((u,v))) for path in LINES.values()
                         for u,v in zip(path,path[1:])}))


def kathara_faces():
    edges=kathara_edges()
    adj=defaultdict(list)
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    for u in adj:
        x,y=COORDS[u]
        adj[u].sort(key=lambda v:atan2(COORDS[v][1]-y,COORDS[v][0]-x))
    seen=set(); faces=[]
    for u in sorted(adj):
        for v in adj[u]:
            if (u,v) in seen: continue
            face=[]; a,b=u,v
            while (a,b) not in seen:
                seen.add((a,b)); face.append(a)
                neighbours=adj[b]
                reverse=neighbours.index(a)
                c=neighbours[(reverse-1)%len(neighbours)]
                a,b=b,c
            faces.append(tuple(face))
    outer=max(faces,key=len)
    bounded={frozenset(f) for f in faces if f != outer}
    if bounded != BOUNDED_FACES:
        raise AssertionError("bounded Kathara face inventory changed")
    return edges,tuple(faces),outer


def q6_complex():
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
    faces=tuple(faces); face_index={f:i for i,f in enumerate(faces)}
    b2=np.zeros((len(edges),len(faces)),dtype=np.int64)
    for j,face in enumerate(faces):
        for u,v in zip(face,face[1:]+face[:1]):
            b2[edge_index[tuple(sorted((u,v)))],j]=1 if u<v else -1
    return vertices,edges,faces,edge_index,face_index,b1,b2


def rank_mod_prime(matrix, prime=PRIME):
    a=np.asarray(matrix,dtype=np.int64).copy()%prime
    rows,cols=a.shape; rank=0
    for col in range(cols):
        pivot=next((r for r in range(rank,rows) if a[r,col]),None)
        if pivot is None: continue
        a[[rank,pivot]]=a[[pivot,rank]]
        inv=pow(int(a[rank,col]),-1,prime)
        a[rank]=(a[rank]*inv)%prime
        for r in range(rows):
            if r!=rank and a[r,col]:
                a[r]=(a[r]-int(a[r,col])*a[rank])%prime
        rank+=1
        if rank==rows: break
    return rank


def axis_mask(axis):
    return 1 << (5-axis)


def path_axes(start,end):
    diff=start^end
    return [axis for axis in AXIS_ORDER if diff&axis_mask(axis)]


def add_path(chain,start,word,edge_index,sign=1):
    current=start
    for axis in word:
        nxt=current^axis_mask(axis)
        edge=(min(current,nxt),max(current,nxt))
        chain[edge_index[edge]] += sign if current<nxt else -sign
        current=nxt
    return current


def path_difference(start,a,b,edge_index,edge_count):
    out=np.zeros(edge_count,dtype=np.int64)
    add_path(out,start,[a,b],edge_index,+1)
    add_path(out,start,[b,a],edge_index,-1)
    return out


def fill_closed_word(start,word,target_edges,target_faces,edge_index,face_index):
    word=list(word)
    if add_path(np.zeros(len(target_edges),dtype=np.int64),start,word,edge_index)!=start:
        raise ValueError("mapped face boundary is not closed")
    coefficients=np.zeros(len(target_faces),dtype=np.int64)
    swaps=0
    while True:
        changed=False; current=start
        for pos in range(len(word)-1):
            a,b=word[pos],word[pos+1]
            if AXIS_POSITION[a] > AXIS_POSITION[b]:
                difference=path_difference(current,a,b,edge_index,len(target_edges))
                low,high=sorted((a,b))
                base=current & ~axis_mask(low) & ~axis_mask(high)
                square=(base,base^axis_mask(low),
                        base^axis_mask(low)^axis_mask(high),base^axis_mask(high))
                square_id=face_index[square]
                boundary=np.zeros(len(target_edges),dtype=np.int64)
                for u,v in zip(square,square[1:]+square[:1]):
                    boundary[edge_index[tuple(sorted((u,v)))]]=1 if u<v else -1
                nonzero=np.flatnonzero(boundary); pivot=int(nonzero[0])
                coefficient=int(difference[pivot]//boundary[pivot])
                if not np.array_equal(difference,coefficient*boundary):
                    raise AssertionError("axis swap is not an exact square boundary")
                coefficients[square_id]+=coefficient
                word[pos],word[pos+1]=b,a
                swaps+=1; changed=True; break
            current ^= axis_mask(a)
        if not changed: break
    if any(word.count(axis)%2 for axis in range(6)):
        raise AssertionError("closed cube word has odd axis parity")
    if any(word[2*k]!=word[2*k+1] for k in range(len(word)//2)):
        raise AssertionError("sorted closed word did not reduce to backtracks")
    return coefficients,swaps


def audit():
    k_edges,k_faces,outer=kathara_faces()
    edge_index_k={e:i for i,e in enumerate(k_edges)}
    b1k=np.zeros((12,len(k_edges)),dtype=np.int64)
    for j,(u,v) in enumerate(k_edges): b1k[u-1,j],b1k[v-1,j]=-1,1
    b2k=np.zeros((len(k_edges),len(k_faces)),dtype=np.int64)
    for j,face in enumerate(k_faces):
        for u,v in zip(face,face[1:]+face[:1]):
            e=tuple(sorted((u,v)))
            b2k[edge_index_k[e],j]=1 if (u,v)==e else -1
    if np.any(b1k@b2k): raise AssertionError("Kathara B1 B2 != 0")
    if np.any(b2k@np.ones(len(k_faces),dtype=np.int64)):
        raise AssertionError("oriented spherical face boundaries do not cancel")

    qv,qe,qf,qei,qfi,b1q,b2q=q6_complex()
    labels=tuple(({ -2:0,0:1,2:2}[COORDS[v][0]]<<4)+COORDS[v][1]
                 for v in range(1,13))
    if len(set(labels))!=12: raise AssertionError("Kathara vertex chart not injective")
    R0=np.zeros((len(qv),12),dtype=np.int64)
    for j,label in enumerate(labels): R0[label,j]=1
    R1=np.zeros((len(qe),len(k_edges)),dtype=np.int64)
    for j,(u,v) in enumerate(k_edges):
        start,end=labels[u-1],labels[v-1]
        add_path(R1[:,j],start,path_axes(start,end),qei)
    R2=np.zeros((len(qf),len(k_faces)),dtype=np.int64)
    fill_l1=[]
    for j,face in enumerate(k_faces):
        word=[]
        for u,v in zip(face,face[1:]+face[:1]):
            lo,hi=sorted((u,v))
            axes=path_axes(labels[lo-1],labels[hi-1])
            if (u,v)!=(lo,hi): axes=list(reversed(axes))
            word.extend(axes)
        fill,_=fill_closed_word(labels[face[0]-1],word,qe,qf,qei,qfi)
        R2[:,j]=fill
        if not np.array_equal(b2q@fill,R1@b2k[:,j]):
            raise AssertionError(f"face {j} filling identity failed")
        fill_l1.append(int(np.sum(np.abs(fill))))
    identity0=np.array_equal(b1q@R1,R0@b1k)
    identity1=np.array_equal(b2q@R2,R1@b2k)
    if not identity0 or not identity1: raise AssertionError("chain-map identities failed")

    fundamental_image=R2@np.ones(len(k_faces),dtype=np.int64)
    if not np.array_equal(b2q@fundamental_image,np.zeros(len(qe),dtype=np.int64)):
        raise AssertionError("image of spherical fundamental cycle is not a Q6 2-cycle")
    support=int(np.count_nonzero(fundamental_image))
    l1=int(np.sum(np.abs(fundamental_image)))
    if support==0 or l1==0: raise AssertionError("fundamental class image collapsed")
    rank=rank_mod_prime(R2)
    if rank!=len(k_faces): raise AssertionError("R2 does not have full column rank")

    return {
        "status":"exact_integral_chain_map_with_nonzero_H2_image",
        "source_completion":{
            "name":"Kathara spherical completion (ten bounded faces plus outer face)",
            "outer_face":list(outer),
            "cell_counts_C0_C1_C2":[12,len(k_edges),len(k_faces)],
            "euler_characteristic":12-len(k_edges)+len(k_faces),
            "oriented_face_boundaries_cancel":True,
            "original_ten_face_complex_is_disk":True
        },
        "target":{"name":"Q6 cubical 2-skeleton","cell_counts_C0_C1_C2":[64,192,240]},
        "vertex_labels":list(labels),
        "maps":{"R0_shape":list(R0.shape),"R1_shape":list(R1.shape),"R2_shape":list(R2.shape),
                "R2_rank_mod_prime":rank,"prime":PRIME},
        "chain_identities":{"B1Q6_R1_equals_R0_B1K":identity0,
                            "B2Q6_R2_equals_R1_B2K":identity1},
        "face_fill_l1":fill_l1,
        "fundamental_class":{
            "image_is_cycle":True,"nonzero":True,"support_faces":support,"l1_norm":l1,
            "interpretation":"Q6 has no 3-cells in this target complex, so a nonzero 2-cycle represents a nonzero H2 class."
        },
        "scope_limitations":[
            "This is a map from the spherical completion of Kathara, not from the original ten-bounded-face disk.",
            "The axis order (1,2,0,3,4,5) is a declared combinatorial convention, not RGS-metric canonical.",
            "No C60-to-Kathara map has yet been constructed.",
            "No Stone-Wales action/intertwiner on the target has yet been defined."
        ]
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",default="kathara_spherical_q6_lift.json")
    args=parser.parse_args()
    result=audit()
    Path(args.out).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":
    main()
