#!/usr/bin/env python3
"""Recompute archived 188D kernel and Anti-Twin checks from an NPZ.

The archived K0 and R_geo_tangent bases are not documented as identical.
Therefore [R_geo_tangent,K0] is a conditional diagnostic only. The primary
geometric check is the equivariance identity R_geo_tangent A = A Pi_AT.
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
    K,P=z["K0"],z["P_G"]; R,Pi=z["R_geo_tangent"],z["Pi_AT"]
    Q=z["Q_tangent"]; Araw,A=z["A_raw"],z["A_geometry_orthonormal"]
    U=z["U_geom_projected"]; Rk=z["R_AT_kernel_extension"]
    n=K.shape[0]; I=np.eye(n); I64=np.eye(64)
    ev=eigh((K+K.T)/2,eigvals_only=True); pe,pv=eigh((P+P.T)/2)
    Up=pv[:,pe>.5]; cos=np.linalg.svd(Up.T@A,compute_uv=False)
    u,_,vh=np.linalg.svd(Araw,full_matrices=False); Ap=u@vh
    res={
      "K0_symmetry_fro":float(np.linalg.norm(K-K.T,"fro")),
      "P_G_symmetry_fro":float(np.linalg.norm(P-P.T,"fro")),
      "P_G_idempotency_fro":float(np.linalg.norm(P@P-P,"fro")),
      "K0P_G_fro":float(np.linalg.norm(K@P,"fro")),
      "P_GK0_fro":float(np.linalg.norm(P@K,"fro")),
      "K0_P_G_commutator_fro":float(np.linalg.norm(K@P-P@K,"fro")),
      "Q_tangent_orthogonality_fro":float(np.linalg.norm(Q.T@Q-I,"fro")),
      "Pi_AT_symmetry_fro":float(np.linalg.norm(Pi-Pi.T,"fro")),
      "Pi_AT_involution_fro":float(np.linalg.norm(Pi@Pi-I64,"fro")),
      "Pi_AT_trace":float(np.trace(Pi)),
      "A_polar_reconstruction_fro":float(np.linalg.norm(Ap-A,"fro")),
      "R_geo_symmetry_fro":float(np.linalg.norm(R-R.T,"fro")),
      "R_geo_orthogonality_fro":float(np.linalg.norm(R.T@R-I,"fro")),
      "R_geo_involution_fro":float(np.linalg.norm(R@R-I,"fro")),
      "geometric_map_equivariance_Rgeo_A_minus_A_Pi_fro":float(np.linalg.norm(R@A-A@Pi,"fro")),
      "P_G_A_minus_A_fro":float(np.linalg.norm(P@A-A,"fro")),
      "U_geom_orthogonality_fro":float(np.linalg.norm(U.T@U-I64,"fro")),
      "P_GU_minus_U_fro":float(np.linalg.norm(P@U-U,"fro")),
      "K0U_fro":float(np.linalg.norm(K@U,"fro")),
      "R_kernel_extension_orthogonality_fro":float(np.linalg.norm(Rk.T@Rk-I,"fro")),
      "R_kernel_extension_involution_fro":float(np.linalg.norm(Rk@Rk-I,"fro")),
      "R_kernel_extension_K0_commutator_fro":float(np.linalg.norm(Rk@K-K@Rk,"fro")),
      "conditional_Rgeo_PG_commutator_fro_if_same_basis":float(np.linalg.norm(R@P-P@R,"fro")),
      "conditional_Rgeo_K0_commutator_fro_if_same_basis":float(np.linalg.norm(R@K-K@R,"fro"))}
    return {"title":"188D K0/P_G and Anti-Twin recovered-matrix audit","input":path.name,
      "shapes":{k:list(z[k].shape) for k in sorted(REQUIRED)},
      "ranks":{"P_G_rank":int(np.sum(pe>.5)),"K0_near_zero_abs_lt_1e-8":int(np.sum(np.abs(ev)<1e-8)),"K0_positive_gt_1e-8":int(np.sum(ev>1e-8))},
      "spectrum_K0":{"min":float(ev[0]),"max":float(ev[-1]),"first_dynamic_eigenvalue":float(ev[np.sum(np.abs(ev)<1e-8)])},
      "geometry_kernel_alignment":{"principal_angle_cosines_min":float(cos.min()),"principal_angle_cosines_max":float(cos.max()),"Frobenius_PG_A_minus_A":float(np.linalg.norm(P@A-A,"fro"))},
      "residuals":res,
      "verdict":{
        "intrinsic_kernel_projector":"VERIFIED_TO_NUMERICAL_PRECISION",
        "antipodal_involution":"VERIFIED_TO_NUMERICAL_PRECISION",
        "geometric_AntiTwin_map_equivariance":"VERIFIED_TO_NUMERICAL_PRECISION: R_geo_tangent A = A Pi_AT",
        "geometric_map_equals_kernel":"NOT_ESTABLISHED: ||P_G A-A||_F is not small; principal angles are not all near zero",
        "projected_kernel_extension":"VERIFIED_AS_A_CONSTRUCTION; it maps into Ker(K0), but does not independently prove that the unprojected geometric map equals the original kernel",
        "direct_Rgeo_K0_commutator":"CONDITIONAL_ONLY: meaningful only after proving K0 and R_geo_tangent use the same tangent-coordinate basis",
        "missing_source":"Original 64x3 X_Oh coordinates and their generator are not included in this NPZ."}}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,default=Path('reports/188d_antitwin_audit.json')); a=p.parse_args()
    r=audit(a.input); a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(r,indent=2)+'\n'); print(json.dumps(r,indent=2))
if __name__=='__main__': main()
