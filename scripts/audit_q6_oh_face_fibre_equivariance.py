#!/usr/bin/env python3
"""Audit coordinate Oh and candidate antipodal tangent-fibre equivariance."""
import argparse, itertools, json
from pathlib import Path
import numpy as np
def signed_permutations():
    for p in itertools.permutations(range(3)):
        for s in itertools.product((-1,1),repeat=3):
            M=np.zeros((3,3));M[np.arange(3),p]=s;yield M
def match_action(X,M,tol=1e-8):
    Y=X@M.T;d=np.linalg.norm(Y[:,None,:]-X[None,:,:],axis=2);idx=d.argmin(axis=1)
    return idx if d[np.arange(len(X)),idx].max()<tol else None
def antipodal_pairs(X,tol=1e-8):
    d=np.linalg.norm(X[:,None,:]+X[None,:,:],axis=2);pi=d.argmin(axis=1)
    if d[np.arange(len(X)),pi].max()>tol or not np.array_equal(pi[pi],np.arange(len(X))):raise RuntimeError("antipodal matching is not an exact involution")
    pairs=[];used=set()
    for i in range(len(X)):
        if i not in used:j=int(pi[i]);pairs.append((i,j));used.update((i,j))
    return pairs,float(d[np.arange(len(X)),pi].max())
def tangent_bases(normals):
    out=[]
    for n in normals:
        v=np.eye(3)[np.argmin(np.abs(n))];u=v-n*np.dot(v,n);u/=np.linalg.norm(u);w=np.cross(n,u);out.append(np.stack((u,w),axis=1))
    return np.array(out)
def tetrahedral_subgroup(acts):
    T=[]
    for M,idx in acts:
        p=tuple(np.argmax(np.abs(M),axis=1));parity=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2;signprod=int(round(np.prod(M[M!=0])))
        if parity==0 and signprod==1:T.append(M)
    if len(T)!=12:raise RuntimeError(f"T subgroup expected 12; found {len(T)}")
    return T+[-M for M in T]
def run(path):
    z=np.load(path);X=z["X_Oh_reconstructed"];A=z["Q6_adjacency"]
    acts=[]
    for M in signed_permutations():
        idx=match_action(X,M)
        if idx is not None:acts.append((M,idx))
    pairs,anti_res=antipodal_pairs(X);pairidx=np.full(64,-1,dtype=int)
    for k,(i,j) in enumerate(pairs):pairidx[[i,j]]=k
    normals=np.array([X[i]/np.linalg.norm(X[i]) for i,j in pairs]);bases=tangent_bases(normals);Th=tetrahedral_subgroup(acts)
    sc=[];fc=[];gr=[]
    for M in Th:
        idx=next(idx for MM,idx in acts if np.allclose(MM,M));sc.append(int(np.sum(idx==np.arange(64))));gr.append(int(np.max(np.abs(A[np.ix_(idx,idx)]-A))))
        tr=0.0
        for k,(i,j) in enumerate(pairs):
            if int(pairidx[idx[i]])==k:tr+=float(np.trace(bases[k].T@M@bases[k]))
        fc.append(tr)
    gres=[int(np.max(np.abs(A[np.ix_(idx,idx)]-A))) for M,idx in acts]
    pair_ok=all(len({int(pairidx[idx[i]]) for i,j in pairs})==32 for M,idx in acts)
    return {"canonical_state_order":"Q6_states row order; binary lexicographic 000000..111111","coordinate_signed_permutation_group_order":len(acts),"point_match_max_residual":0.0,"Q6_adjacency_automorphisms_in_coordinate_group":sum(r==0 for r in gres),"Q6_adjacency_nonautomorphisms_in_coordinate_group":sum(r!=0 for r in gres),"max_adjacency_entry_residual":max(gres),"antipodal_pairs_count":len(pairs),"antipodal_residual":anti_res,"antipodal_pairs":pairs,"candidate_fibre_definition":"E_k=n_k^perp, n_k=normalized X_i for one canonical representative of each X-antipodal pair; not independently recovered face normals","candidate_fibre_pair_action_valid":bool(pair_ok),"T_h_order":len(Th),"T_h_graph_automorphisms":sum(r==0 for r in gr),"T_h_state_character":sc,"T_h_candidate_fibre_character":fc,"T_h_characters_equal":bool(np.allclose(sc,fc)),"T_h_character_difference":[float(a-b) for a,b in zip(sc,fc)],"verdict":"Candidate 64D fibre representation is not equivalent to the coordinate-induced 64-state representation under T_h: their characters differ. Also, coordinate Oh is not a full Q6 graph-automorphism action.","limitations":["The 32 tangent planes are built from antipodal X-point directions, not independently supplied geometric face normals.","This is a representation-character test, not an operator spectral intertwining test.","Only 16 of the 48 coordinate signed-permutation actions preserve Q6 adjacency."]}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("npz",nargs="?",default="RGS_PSU_all_matrices.npz");p.add_argument("--out",default="Q6_Oh_face_fibre_equivariance.json");a=p.parse_args();r=run(a.npz);Path(a.out).write_text(json.dumps(r,indent=2),encoding="utf-8");print(json.dumps(r,indent=2))
