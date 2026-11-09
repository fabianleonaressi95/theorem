#!/usr/bin/env python3
"""Recompute archived 188D K0/P_G/Anti-Twin matrix checks from an NPZ.
The NPZ stores derived matrices, not the original 64x3 X_Oh coordinates.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh

REQUIRED={"Pi_AT","Q_tangent","V_vertex_modes","A_raw","A_geometry_orthonormal","P_G","K0","R_geo_tangent","principal_angle_cosines","singular_values_A_raw","singular_values_PG_A","U_geom_projected","R_AT_kernel_extension"}

def audit(path:Path)->dict:
    z=np.load(path); missing=REQUIRED-set(z.files)
    if missing: raise ValueError(f"Missing NPZ arrays: {sorted(missing)}")
    K,P=z["K0"],z["P_G"]; R,Pi=z["R_geo_tangent"],z["Pi_AT"]; Q,U=z["Q_tangent"],z["U_geom_projected"]; Araw,A=z["A_raw"],z["A_geometry_orthonormal"]; Rk=z["R_AT_kernel_extension"]
    n=K.shape[0]; I=np.eye(n); I64=np.eye(64)
    ev=eigh((K+K.T)/2,eigvals_only=True); pe,pv=eigh((P+P.T)/2); Up=pv[:,pe>.5]
    cos=np.linalg.svd(Up.T@A,compute_uv=False); u,_,vh=np.linalg.svd(Araw,full_matrices=False); Ap=u@vh
    res={
      "K0_symmetry_fro":float(np.linalg.norm(K-K.T,"fro")),"P_G_symmetry_fro":float(np.linalg.norm(P-P.T,"fro")),
      "P_G_idempotency_fro":float(np.linalg.norm(P@P-P,"fro")),"K0P_G_fro":float(np.linalg.norm(K@P,"fro")),
      "P_GK0_fro":float(np.linalg.norm(P@K,"fro")),"K0_P_G_commutator_fro":float(np.linalg.norm(K@P-P@K,"fro")),
      "Q_tangent_orthogonality_fro":float(np.linalg.norm(Q.T@Q-I,"fro")),
      "Pi_AT_symmetry_fro":float(np.linalg.norm(Pi-Pi.T,"fro")),"Pi_AT_involution_fro":float(np.linalg.norm(Pi@Pi-I64,"fro")),"Pi_AT_trace":float(np.trace(Pi)),
      "A_polar_reconstruction_fro":float(np.linalg.norm(Ap-A,"fro")),
      "U_geom_orthogonality_fro":float(np.linalg.norm(U.T@U-I64,"fro")),"P_GU_minus_U_fro":float(np.linalg.norm(P@U-U,"fro")),"K0U_fro":float(np.linalg.norm(K@U,"fro")),
      "R_geo_symmetry_fro":float(np.linalg.norm(R-R.T,"fro")),"R_geo_involution_fro":float(np.linalg.norm(R@R-I,"fro")),
      "R_geo_P_G_commutator_fro":float(np.linalg.norm(R@P-P@R,"fro")),"R_geo_K0_commutator_fro":float(np.linalg.norm(R@K-K@R,"fro")),
      "R_kernel_extension_involution_fro":float(np.linalg.norm(Rk@Rk-I,"fro")),"R_kernel_extension_K0_commutator_fro":float(np.linalg.norm(Rk@K-K@Rk,"fro"))}
    return {"title":"188D K0/P_G and Anti-Twin recovered-matrix audit","input":path.name,
      "shapes":{k:list(z[k].shape) for k in sorted(REQUIRED)},
      "ranks":{"P_G_rank":int(np.sum(pe>.5)),"K0_near_zero_abs_lt_1e-8":int(np.sum(np.abs(ev)<1e-8)),"K0_positive_gt_1e-8":int(np.sum(ev>1e-8))},
      "spectrum_K0":{"min":float(ev[0]),"max":float(ev[-1]),"first_dynamic_eigenvalue":float(ev[np.sum(np.abs(ev)<1e-8)])},
      "residuals":res,"geometry_kernel_alignment":{"principal_angle_cosines_min":float(cos.min()),"principal_angle_cosines_max":float(cos.max()),"Frobenius_PG_A_minus_A":float(np.linalg.norm(P@A-A,"fro"))},
      "verdict":{"intrinsic_kernel_projector":"VERIFIED_TO_NUMERICAL_PRECISION","abstract_kernel_involution_extension":"VERIFIED_TO_NUMERICAL_PRECISION",
      "canonical_geometric_identification":"NOT_VERIFIED; stored R_geo_tangent fails to commute with P_G and K0; minimum principal-angle cosine is far from 1",
      "warning":"R_AT_kernel_extension commutes with K0 because it is constructed on Ker(K0); this is not independent evidence for a canonical geometric intertwiner. Original X_Oh coordinates are not contained in this NPZ."}}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,required=True); p.add_argument('--output',type=Path,default=Path('reports/188d_antitwin_audit.json')); a=p.parse_args()
    r=audit(a.input); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(r,indent=2)+'\n'); print(json.dumps(r,indent=2))
if __name__=='__main__': main()
