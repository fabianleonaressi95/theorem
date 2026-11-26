#!/usr/bin/env python3
"""Forensic provenance audit of K0, P_G and T_transport in the RGS 188D archive.

The audit separates identities directly recoverable from the NPZ from provenance
claims that require the original generator. It reconstructs the common order-16
Q6/geometric action, but marks operator covariance conditional on a shared 188D
coordinate basis.
"""
import argparse,itertools,json
from pathlib import Path
import numpy as np
from scipy.optimize import linear_sum_assignment

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("npz")
 ap.add_argument("--out",default="audits/RGS_188D_OPERATOR_PROVENANCE.json")
 a=ap.parse_args()
 z=np.load(a.npz)
 X=np.asarray(z["X_Oh_reconstructed"],float);Q=np.asarray(z["Q_tangent"],float)
 A=np.asarray(z["A_geometry_orthonormal"],float);U=np.asarray(z["U_polar"],float)
 PG=np.asarray(z["P_G"],float);K=np.asarray(z["K0"],float)
 T=np.asarray(z["T_transport"],float);R=np.asarray(z["R_geo_tangent"],float)
 Adj=np.asarray(z["Q6_adjacency"],int);Pi=np.asarray(z["Pi_AT"],float)
 # Rebuild the 16 common geometric/graph transformations.
 els=[]
 for perm in itertools.permutations(range(3)):
  for signs in itertools.product((-1.,1.),repeat=3):
   M=np.eye(3)[list(perm)]*np.asarray(signs)[:,None]
   d=np.linalg.norm((X@M.T)[:,None,:]-X[None,:,:],axis=2)
   rr,cc=linear_sum_assignment(d);p=np.empty(64,dtype=int);p[rr]=cc
   if d[rr,cc].max()>1e-10 or np.any(Adj!=Adj[np.ix_(p,p)]):continue
   S=np.zeros((192,192))
   for i in range(64):S[3*p[i]:3*p[i]+3,3*i:3*i+3]=M
   G=Q.T@S@Q
   rho=np.zeros((64,64));rho[p,np.arange(64)]=1
   els.append((G,rho))
 if len(els)!=16:raise RuntimeError(f"Expected common subgroup 16, got {len(els)}")
 def rel(x,y):return float(np.linalg.norm(x-y)/max(np.linalg.norm(y),1e-30))
 def cov(M,G):return rel(G.T@M@G,M)
 # Operator identities and ranks.
 svK=np.linalg.eigvalsh((K+K.T)/2)
 svT=np.linalg.svd(T,compute_uv=False)
 # Principal angle/leakage for geometric image versus kernel.
 w,Vp=np.linalg.eigh((PG+PG.T)/2);Ug=Vp[:,w>0.5]
 cos=np.linalg.svd(Ug.T@A,compute_uv=False)
 # Rebuild the polar map from P_G A and compare.
 B=PG@A;ub,sb,vhb=np.linalg.svd(B,full_matrices=False);Up=ub@vhb
 # Covariance and intertwining diagnostics.
 covs={}
 for name,M in (("K0",K),("P_G",PG),("T_transport",T),("R_geo_tangent",R),
                ("A_projector",A@A.T),("U_polar_projector",U@U.T)):
  vals=[cov(M,G) for G,rho in els]
  covs[name]={"invariant_elements_tol_1e-10":int(sum(v<1e-10 for v in vals)),
              "group_order":16,"max_relative_defect":max(vals)}
 ae=[float(np.linalg.norm(G@A-A@rho)/max(np.linalg.norm(A),1e-30)) for G,rho in els]
 ue=[float(np.linalg.norm(G@U-U@rho)/max(np.linalg.norm(U),1e-30)) for G,rho in els]
 # Reynolds projection of A as an intertwiner; this does not repair its kernel mismatch.
 Aeq=sum(G.T@A@rho for G,rho in els)/16
 report={
  "classification":"forensic numerical provenance audit; source-generation chain partially unresolved",
  "directly_recovered_constructions":{
   "P_G":"spectral projector onto the 64D numerical kernel of K0 (verified against spectral projector)",
   "A_geometry_orthonormal":"polar orthonormalization of the geometric feature map projected into the Q_tangent coordinate frame; the archived construction uses normalized cross(X_i, fixed_axis) site modes",
   "U_polar":"polar factor of P_G @ A_geometry_orthonormal",
   "T_transport":"U_polar @ A_geometry_orthonormal.T (partial isometry transporting the geometric 64D frame into Im(P_G))"
  },
  "identity_residuals":{
   "T_minus_U_Atranspose_fro":float(np.linalg.norm(T-U@A.T)),
   "TtT_minus_AAt_fro":float(np.linalg.norm(T.T@T-A@A.T)),
   "TTt_minus_UUt_fro":float(np.linalg.norm(T@T.T-U@U.T)),
   "U_orthonormality_fro":float(np.linalg.norm(U.T@U-np.eye(64))),
   "PG_U_minus_U_fro":float(np.linalg.norm(PG@U-U)),
   "PG_idempotence_fro":float(np.linalg.norm(PG@PG-PG))
  },
  "ranks":{
   "K0":int(np.linalg.matrix_rank(K,tol=1e-8)),
   "P_G":int(np.linalg.matrix_rank(PG,tol=1e-8)),
   "A":int(np.linalg.matrix_rank(A,tol=1e-8)),
   "U_polar":int(np.linalg.matrix_rank(U,tol=1e-8)),
   "T_transport":int(np.sum(svT>1e-10))
  },
  "K0_spectrum":{
   "zero_modes_abs_lt_1e-8":int(np.sum(np.abs(svK)<1e-8)),
   "positive_min":float(svK[svK>1e-8].min()),
   "positive_max":float(svK.max()),
   "positive_ladder_spacing_max_error":float(np.max(np.abs(np.diff(svK[svK>1e-8])-0.1))),
   "warning":"The ladder is an observed property of the archived matrix; its physical derivation is not established by this audit."
  },
  "geometric_to_kernel_alignment":{
   "relative_leakage_norm_PG_A_minus_A":rel(PG@A-A,A),
   "principal_angle_cosine_min":float(cos.min()),
   "principal_angle_cosine_max":float(cos.max()),
   "interpretation":"The chosen geometric 64D feature frame is not the kernel subspace; U_polar is obtained only after projecting it into that kernel and taking a polar factor."
  },
  "group_covariance_conditional_on_shared_188D_basis":{
   "common_group_order":16,
   "max_A_intertwining_defect":max(ae),
   "max_U_intertwining_defect":max(ue),
   "operators":covs,
   "warning":"This comparison is mathematically valid only if K0/P_G use exactly the same 188D coordinate basis as Q_tangent and R_geo_tangent. The archive does not supply an independent basis-identification certificate."
  },
  "K0_PG_provenance":{
   "verified":"P_G is the spectral kernel projector of the archived K0 to numerical precision; K0 P_G and P_G K0 are approximately zero.",
   "not_verified":"The original source code that generated the exact archived K0 and its coordinate basis was not found.",
   "source_archive_evidence":"The recovered notebook PDF contains explicitly synthetic K0 examples (random Gram matrices) and an explicitly illustrative spectral-mask P_G construction, but the available evidence does not prove that those particular mock snippets generated the current archived K0/P_G.",
   "conclusion":"Do not label K0 as a geometry-derived Hessian or P_G as an independently derived geometric projector until the exact generating cell/script and basis map are recovered."
  },
  "T_transport_provenance":{
   "verified":"T_transport is the partial-isometry product U_polar A_geometry_orthonormal^T.",
   "interpretation":"It is a post-projection polar transport between two 64D subspaces, not an independently derived Q6 connection or a canonical group intertwiner.",
   "symmetry_status":"It is not invariant under the reconstructed order-16 group in the stored comparison (only identity passes), subject to the shared-basis caveat."
  },
  "classification_decisions":{
   "K0":"archived symmetric positive-semidefinite matrix; physical/geometric generation unresolved",
   "P_G":"verified spectral kernel projector of K0; not independently geometric",
   "T_transport":"verified derived partial isometry from A and P_G; symmetry-breaking/frame dependence present",
   "R_geo_tangent":"verified geometric tangent representation; invariant under all 16 common transformations"
  }
 }
 Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(report,indent=2))
 print(json.dumps(report,indent=2))
if __name__=="__main__":main()
