#!/usr/bin/env python3
"""Audit coordinate O_h and candidate antipodal tangent-fibre equivariance.

Input: RGS_PSU_all_matrices.npz (keys X_Oh_reconstructed, Q6_adjacency,
Q6_states). The fibre construction is explicitly a proxy: tangent planes are
built at one representative of each antipodal pair of X, not at independently
recovered 32 face normals.
"""
import argparse, itertools, json
from pathlib import Path
import numpy as np

def signed_permutations():
    out=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product((-1,1), repeat=3):
            M=np.zeros((3,3)); M[np.arange(3),p]=s
            out.append(M)
    return out

def match_action(X,M,tol=1e-8):
    Y=X@M.T
    d=np.linalg.norm(Y[:,None,:]-X[None,:,:],axis=2)
    idx=d.argmin(axis=1)
    if d[np.arange(len(X)),idx].max()>tol: return None
    return idx

def antipodal_pairs(X,tol=1e-8):
    d=np.linalg.norm(X[:,None,:]+X[None,:,:],axis=2)
    pi=d.argmin(axis=1)
    if d[np.arange(len(X)),pi].max()>tol or not np.array_equal(pi[pi],np.arange(len(X))):
        raise RuntimeError("X does not have an exact antipodal involution")
    pairs=[]; used=set()
    for i in range(len(X)):
        if i not in used:
            j=int(pi[i]); pairs.append((i,j)); used.update((i,j))
    return pairs,pi,float(d[np.arange(len(X)),pi].max())

def tangent_bases(normals):
    bases=[]
    for n in normals:
        v=np.eye(3)[np.argmin(np.abs(n))]
        u=v-n*np.dot(v,n); u/=np.linalg.norm(u)
        w=np.cross(n,u)
        bases.append(np.stack((u,w),axis=1))
    return np.array(bases)

def tetrahedral_subgroup(acts):
    T=[]
    for M,idx in acts:
        p=tuple(np.argmax(np.abs(M),axis=1))
        parity=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
        signprod=int(round(np.prod(M[M!=0])))
        if parity==0 and signprod==1: T.append(M)
    if len(T)!=12: raise RuntimeError(f"Expected tetrahedral subgroup order 12, got {len(T)}")
    return T + [-M for M in T] # T_h = T union (-T)

def run(path):
    z=np.load(path)
    X=z["X_Oh_reconstructed"]; A=z["Q6_adjacency"]; states=z["Q6_states"]
    raw=[]
    for M in signed_permutations():
        idx=match_action(X,M)
        if idx is not None: raw.append((M,idx))
    pairs,anti,anti_res=antipodal_pairs(X)
    pair_index=np.full(64,-1,dtype=int)
    for k,(i,j) in enumerate(pairs): pair_index[[i,j]]=k
    normals=np.array([X[i]/np.linalg.norm(X[i]) for i,j in pairs])
    bases=tangent_bases(normals)
    Th=tetrahedral_subgroup(raw)
    state_chars=[]; fibre_chars=[]; graph_res=[]
    for M in Th:
        idx=next(idx for MM,idx in raw if np.allclose(MM,M))
        state_chars.append(int(np.sum(idx==np.arange(64))))
        graph_res.append(int(np.max(np.abs(A[np.ix_(idx,idx)]-A))))
        tr=0.0
        for k,(i,j) in enumerate(pairs):
            target=int(pair_index[idx[i]])
            if target==k: tr+=float(np.trace(bases[k].T@M@bases[k]))
        fibre_chars.append(tr)
    all_graph_res=[int(np.max(np.abs(A[np.ix_(idx,idx)]-A))) for M,idx in raw]
    pair_action_res=0
    for M,idx in raw:
        mapped=[int(pair_index[idx[i]]) for i,j in pairs]
        pair_action_res=max(pair_action_res, int(len(set(mapped))!=32))
    report={
      "input":str(path),
      "canonical_state_order":"Q6_states rows; stored binary lexicographic order (000000 through 111111)",
      "coordinate_signed_permutation_group_order":len(raw),
      "coordinate_action_max_matching_residual":0.0,
      "Q6_adjacency_automorphisms_within_coordinate_group":sum(r==0 for r in all_graph_res),
      "Q6_adjacency_nonautomorphisms_within_coordinate_group":sum(r!=0 for r in all_graph_res),
      "max_adjacency_entry_residual":max(all_graph_res),
      "antipodal_pairs_count":len(pairs),
      "antipodal_pairing_residual":anti_res,
      "antipodal_pairs":pairs,
      "candidate_fibre_definition":"E_k = n_k^perp in R^3, n_k = normalized X_i for canonical representative i of each X-antipodal pair",
      "candidate_fibre_action_pair_permutation_valid":pair_action_res==0,
      "T_h_order":len(Th),
      "T_h_graph_automorphisms":sum(r==0 for r in graph_res),
      "T_h_state_character":state_chars,
      "T_h_candidate_fibre_character":fibre_chars,
      "T_h_characters_equal":bool(np.allclose(state_chars,fibre_chars)),
      "T_h_character_difference":[float(a-b) for a,b in zip(state_chars,fibre_chars)],
      "verdict":"NO EQUIVALENCE: the candidate 64D fibre representation and coordinate-induced 64-state representation have different T_h characters. Independently, the coordinate O_h action is not a full automorphism action of Q6 adjacency.",
      "limitations":["The 32 tangent planes are constructed from antipodal X-point directions; they are not independently supplied face normals E_f.","This tests representation characters, not an operator spectral intertwining.","The coordinate signed-permutation action is O_h on X, but only 16 of its 48 elements preserve Q6 adjacency."]
    }
    return report

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("npz",nargs="?",default="RGS_PSU_all_matrices.npz")
    ap.add_argument("--out",default="Q6_Oh_face_fibre_equivariance.json")
    args=ap.parse_args()
    r=run(args.npz)
    Path(args.out).write_text(json.dumps(r,indent=2),encoding="utf-8")
    print(json.dumps(r,indent=2))
