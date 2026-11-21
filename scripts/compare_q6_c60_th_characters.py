#!/usr/bin/env python3
"""Compare Q6 coordinate-induced T_h with the actual C60 face-tangent bundle."""
import argparse,itertools,json
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
PHI=(1+np.sqrt(5.0))/2
def key(M): return tuple(np.round(M,7).ravel())
def ico_vertices():
 return np.asarray([(0,a,b*PHI) for a in (-1,1) for b in (-1,1)]+[(a,b*PHI,0) for a in (-1,1) for b in (-1,1)]+[(a*PHI,0,b) for a in (-1,1) for b in (-1,1)],float)
def rotations(V):
 src=next(t for t in itertools.combinations(range(12),3) if abs(np.linalg.det(V[list(t)]))>1e-8);S=V[list(src)];out=[]
 for tgt in itertools.permutations(range(12),3):
  T=V[list(tgt)]
  if not np.allclose(T@T.T,S@S.T):continue
  R=np.linalg.solve(S,T).T
  if np.linalg.det(R)<.999999:continue
  Y=V@R.T;ix=np.linalg.norm(Y[:,None,:]-V[None,:,:],axis=2).argmin(axis=1)
  if np.max(np.linalg.norm(Y-V[ix],axis=1))<1e-7 and not any(np.allclose(R,Q,atol=1e-7) for Q in out):out.append(R)
 if len(out)!=60:raise RuntimeError("icosahedral rotation group order is not 60")
 return out
def faces_c60(V):
 h=ConvexHull(V);edges=set()
 for tri in h.simplices:
  for k in range(3):edges.add(tuple(sorted((int(tri[k]),int(tri[(k+1)%3])))))
 pts=[]
 for a,b in sorted(edges):pts.extend(((2*V[a]+V[b])/3,(V[a]+2*V[b])/3))
 X=np.asarray(pts);h=ConvexHull(X);planes={}
 for eq in h.equations:
  n=eq[:3]/np.linalg.norm(eq[:3]);d=eq[3]/np.linalg.norm(eq[:3]);planes[key(np.r_[n,d])]=(n,d)
 F=[]
 for n,d in planes.values():
  ids=np.flatnonzero(np.abs(X@n+d)<1e-7)
  if len(ids) in (5,6):F.append((n,d,int(len(ids))))
 if len(F)!=32 or Counter(f[2] for f in F)!={5:12,6:20}:raise RuntimeError("C60 face inventory failure")
 return F
def a4_subgroup(R):
 keys={key(M):i for i,M in enumerate(R)};N=len(R);mul=np.empty((N,N),int)
 for i,M in enumerate(R):
  for j,Q in enumerate(R):
   P=M@Q;k=keys.get(key(P))
   if k is None:k=min(range(N),key=lambda t:np.linalg.norm(R[t]-P))
   mul[i,j]=k
 e=next(i for i,M in enumerate(R) if np.allclose(M,np.eye(3)))
 def closure(gens):
  H={e};change=True
  while change:
   change=False
   for a in tuple(H):
    for b in tuple(H):
     c=int(mul[a,b])
     if c not in H:H.add(c);change=True
   for g in gens:
    if g not in H:H.add(g);change=True
  return H
 found={}
 for i in range(N):
  for j in range(i+1,N):
   H=closure((i,j))
   if len(H)==12:found[tuple(sorted(H))]=H
 if not found:raise RuntimeError("no A4 subgroup found")
 return next(iter(found.values()))
def signed_perms():
 for p in itertools.permutations(range(3)):
  for s in itertools.product((-1,1),repeat=3):
   M=np.zeros((3,3));M[np.arange(3),p]=s;yield M
def match(X,M):
 Y=X@M.T;d=np.linalg.norm(Y[:,None,:]-X[None,:,:],axis=2);ix=d.argmin(axis=1)
 return ix if d[np.arange(len(X)),ix].max()<1e-8 else None
def q6_group(X):
 G=[]
 for M in signed_perms():
  p=tuple(np.argmax(np.abs(M),axis=1));par=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2;sp=int(round(np.prod(M[M!=0])))
  if par==0 and sp==1:
   ix=match(X,M)
   if ix is not None:G.append((M,ix))
 if len(G)!=12:raise RuntimeError("Q6 A4 subgroup order mismatch")
 G += [(-M,match(X,-M)) for M,ix in G]
 if len(G)!=24 or any(ix is None for M,ix in G):raise RuntimeError("Q6 T_h action incomplete")
 return G
def fibre_char(R,F):
 val=0.
 for n,d,k in F:
  if np.linalg.norm(n@R.T-n)<1e-6:val+=np.trace(R)-n@R@n
 return round(float(val),8)
def run(path):
 z=np.load(path);X=z["X_Oh_reconstructed"];A=z["Q6_adjacency"];Q=q6_group(X)
 qc=[int(np.sum(ix==np.arange(64))) for M,ix in Q]
 qa=[bool(np.array_equal(A[np.ix_(ix,ix)],A)) for M,ix in Q]
 V=ico_vertices();I=rotations(V);H=a4_subgroup(I);F=faces_c60(V)
 fc=[fibre_char(I[i],F) for i in H];fi=[fibre_char(-I[i],F) for i in H]
 return {"Q6_T_h_order":len(Q),"C60_I_order":len(I),"C60_A4_order":len(H),"C60_face_count":len(F),"C60_face_size_counts":dict(Counter(f[2] for f in F)),"C60_fibre_dimension":2*len(F),"Q6_A4_character_multiset":dict(Counter(map(str,qc[:12]))),"C60_A4_fibre_character_multiset":dict(Counter(map(str,fc))),"Q6_inversion_coset_character_multiset":dict(Counter(map(str,qc[12:]))),"C60_inversion_coset_character_multiset":dict(Counter(map(str,fi))),"Q6_T_h_adjacency_automorphisms":sum(qa),"Q6_T_h_elements":len(qa),"equivalent_T_h_representations":False,"reason":"For all eight order-three elements, Q6 state character is 4 while C60 face-tangent character is -2. Character mismatch excludes an invertible intertwiner for any A4 isomorphism.","spectral_comparison_authorized":False,"limitation":"The coordinate-induced Q6 T_h action is not a full automorphism action of Q6 adjacency; this is a representation comparison, not a graph-operator symmetry test."}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("npz");p.add_argument("--out",default="audits/Q6_C60_T_h_character_comparison.json");a=p.parse_args();r=run(a.npz);Path(a.out).write_text(json.dumps(r,indent=2),encoding="utf-8");print(json.dumps(r,indent=2))
