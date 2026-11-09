#!/usr/bin/env python3
"""Regenerate PRISM C64 □ C6 □ C6 □ C6 □ C5 incidence operators."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix

MODS=np.array([64,6,6,6,5],dtype=np.int64); D=5

def build():
    V=int(np.prod(MODS)); E=D*V; F2=10*V
    strides=np.array([np.prod(MODS[d+1:]) for d in range(D)],dtype=np.int64)
    verts=np.arange(V,dtype=np.int64)
    shifts=np.empty((D,V),dtype=np.int64)
    for d in range(D):
        s=strides[d]; m=MODS[d]; q=(verts//s)%m
        shifts[d]=verts+np.where(q<m-1,s,-(m-1)*s)
    src=np.tile(verts,D); dst=shifts.ravel(order='C')
    rows=np.empty(2*E,dtype=np.int32); cols=np.empty(2*E,dtype=np.int32); dat=np.empty(2*E,dtype=np.int8)
    rows[0::2]=src; rows[1::2]=dst; cols[0::2]=np.repeat(np.arange(E),1); cols[1::2]=np.repeat(np.arange(E),1)
    dat[0::2]=-1; dat[1::2]=1
    B1=coo_matrix((dat,(rows,cols)),shape=(V,E)).tocsr()
    rs=[]; cs=[]; ds=[]; fbase=0
    for i in range(D):
      for j in range(i+1,D):
        vi=shifts[i]; vj=shifts[j]
        ei_v=i*V+verts; ej_vi=j*V+vi; ei_vj=i*V+vj; ej_v=j*V+verts
        fs=np.arange(fbase,fbase+V,dtype=np.int64)
        rs.append(np.concatenate([ei_v,ej_vi,ei_vj,ej_v])); cs.append(np.tile(fs,4))
        ds.append(np.concatenate([np.ones(V,dtype=np.int8),np.ones(V,dtype=np.int8),-np.ones(V,dtype=np.int8),-np.ones(V,dtype=np.int8)]))
        fbase+=V
    B2=coo_matrix((np.concatenate(ds),(np.concatenate(rs),np.concatenate(cs))),shape=(E,F2)).tocsr()
    return B1,B2

def audit():
    B1,B2=build(); product=B1@B2
    V,E,F2=B1.shape[0],B1.shape[1],B2.shape[1]
    cells=[V,5*V,10*V,10*V,5*V,V]; betti=[1,5,10,10,5,1]
    eig=np.array([0.0])
    for n in MODS:
        one=np.array([2-2*np.cos(2*np.pi*k/n) for k in range(int(n))])
        eig=(eig[:,None]+one[None,:]).ravel()
    eig.sort(); gap=float(eig[np.flatnonzero(eig>1e-12)[0]])
    sha=hashlib.sha256()
    for M in (B1,B2):
        sha.update(M.indptr.tobytes()); sha.update(M.indices.tobytes()); sha.update(M.data.tobytes())
    return B1,B2,{"mods":MODS.tolist(),"vertices":V,"edges":E,"square_faces":F2,
      "B1_shape":list(B1.shape),"B1_nnz":int(B1.nnz),"B2_shape":list(B2.shape),"B2_nnz":int(B2.nnz),
      "B1B2_nnz":int(product.nnz),"B1B2_exact_zero":bool(product.nnz==0),"graph_cycle_rank":int(E-V+1),
      "cell_counts":cells,"betti_product_torus":betti,"euler_characteristic":int(sum((-1)**k*c for k,c in enumerate(cells))),
      "vertex_laplacian_gap":gap,"gap_multiplicity":int(np.sum(np.isclose(eig,gap,atol=1e-12))),
      "structural_sha256":sha.hexdigest(),
      "scope_note":"Betti numbers are standard product-torus values; this script does not compute all boundary ranks B_k for k=1,...,5."}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--json',type=Path,default=Path('reports/prism_69120_audit.json')); p.add_argument('--npz',type=Path,default=Path('data/prism_69120_incidence.npz')); p.add_argument('--no-save-incidence',action='store_true'); a=p.parse_args()
    B1,B2,r=audit(); a.json.parent.mkdir(parents=True,exist_ok=True); a.json.write_text(json.dumps(r,indent=2)+'\n')
    if not a.no_save_incidence:
        a.npz.parent.mkdir(parents=True,exist_ok=True)
        np.savez_compressed(a.npz,B1_indptr=B1.indptr,B1_indices=B1.indices,B1_data=B1.data,B2_indptr=B2.indptr,B2_indices=B2.indices,B2_data=B2.data)
    print(json.dumps(r,indent=2))
if __name__=='__main__': main()
