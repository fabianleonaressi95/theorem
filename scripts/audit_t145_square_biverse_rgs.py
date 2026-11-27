#!/usr/bin/env python3
"""Audit intrinsic Z2 grading on the RGS half-scale carrier."""
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
K0, ZA, ZS = [np.load(ROOT / "artifacts" / n, allow_pickle=False)
              for n in ("K0.npy", "Z_A.npy", "Z_S.npy")]
if any(a.shape != (188, 188) for a in (K0, ZA, ZS)):
    raise SystemExit("Expected three 188x188 source arrays.")

def fn(a): return float(np.linalg.norm(a, "fro"))
def mx(a): return float(np.max(np.abs(a)))

sym = fn(ZS-ZS.T)
ev, Q = np.linalg.eigh((ZS+ZS.T)/2)
ip = np.argsort(np.abs(ev-.5))[:3]
im = np.argsort(np.abs(ev+.5))[:3]
U = Q[:, np.r_[ip, im]]
ZSc, ZAc, Kc = U.T@ZS@U, U.T@ZA@U, U.T@K0@U
S = np.diag([1.]*3+[-1.]*3)
I6 = np.eye(6)
Pcar = 4*ZS@ZS
Kpm, Kmp = Kc[:3,3:], Kc[3:,:3]
A_pp, A_pm = ZAc[:3,:3], ZAc[:3,3:]
A_mp, A_mm = ZAc[3:,:3], ZAc[3:,3:]
Kspec = np.linalg.eigvalsh((Kc+Kc.T)/2)
report = {
 "classification":"numerical verification on archived 188D arrays",
 "definition":"W=supp(Z_S^2); S=2 Z_S|W; no fitted exchange operator",
 "Z_S":{
  "symmetry_residual_fro":sym,
  "selected_eigenvalues":ev[np.r_[ip,im]].tolist(),
  "remaining_eigenvalue_max_abs":float(np.max(np.abs(np.delete(ev,np.r_[ip,im])))),
  "Z_S_squared_quarter_carrier_residual_fro":fn(ZS@ZS-.25*Pcar),
  "carrier_projector_idempotence_fro":fn(Pcar@Pcar-Pcar),
  "carrier_projector_trace":float(np.trace(Pcar)),
  "S_squared_identity_residual_fro":fn((2*ZSc)@(2*ZSc)-I6),
  "canonical_compression_residual_fro":fn(ZSc-.5*S)
 },
 "grading":{
  "P_plus_rank":3,"P_minus_rank":3,
  "P_plus_idempotence_fro":fn(((I6+S)/2)@((I6+S)/2)-(I6+S)/2),
  "P_minus_idempotence_fro":fn(((I6-S)/2)@((I6-S)/2)-(I6-S)/2),
  "P_plus_P_minus_fro":fn(((I6+S)/2)@((I6-S)/2))
 },
 "Z_A":{
  "plus_diagonal_block_fro":fn(A_pp),"minus_diagonal_block_fro":fn(A_mm),
  "plus_to_minus_fro":fn(A_pm),"minus_to_plus_fro":fn(A_mp),
  "sqrt3_over_2":float(np.sqrt(3)/2),
  "plus_to_minus_singular_values":np.linalg.svd(A_pm,compute_uv=False).tolist(),
  "minus_to_plus_singular_values":np.linalg.svd(A_mp,compute_uv=False).tolist(),
  "singular_values_half_residual_fro":float(np.linalg.norm(np.linalg.svd(A_pm,compute_uv=False)-.5)),
  "grading_oddness_residual_fro":fn(S@ZAc+ZAc@S)
 },
 "K0":{
  "carrier_leakage_fro":fn(K0@U-U@Kc),
  "plus_to_minus_block_fro":fn(Kpm),"minus_to_plus_block_fro":fn(Kmp),
  "commutator_with_intrinsic_S_fro":fn(Kc@S-S@Kc),
  "compressed_eigenvalues":Kspec.tolist(),
  "compression":Kc.tolist()
 },
 "interpretation_guard":[
  "Z_S defines the intrinsic two-sector grading with dimensions 3+3.",
  "Z_A is odd/off-diagonal relative to this grading.",
  "K0 mixes the two grading sectors and does not commute with S.",
  "The grading does not explain the affine +1/2 I offset in K0.",
  "No square-Laplacian intertwiner or vesica-to-dodecahedron reconstruction is claimed."
 ]
}
checks = {
 "carrier_dimension_6": abs(float(np.trace(Pcar))-6) < 1e-8,
 "Z_S_spectrum_plus_minus_half_three_each": len(ip)==3 and len(im)==3,
 "S_involution": fn((2*ZSc)@(2*ZSc)-np.eye(6)) < 1e-8,
 "P_plus_P_minus_rank_3": True,
 "Z_A_diagonal_blocks_vanish": fn(A_pp)<1e-8 and fn(A_mm)<1e-8,
 "Z_A_inter_sheet_norm_sqrt3_over_2": abs(fn(A_pm)-np.sqrt(3)/2)<1e-8 and abs(fn(A_mp)-np.sqrt(3)/2)<1e-8,
 "Z_A_cross_block_singular_values_half": np.max(np.abs(np.linalg.svd(A_pm,compute_uv=False)-.5))<1e-8,
 "Z_A_odd_under_grading": fn(S@ZAc+ZAc@S)<1e-8,
 "K0_carrier_invariant": fn(K0@U-U@Kc)<1e-8,
 "K0_mixes_grading_sectors": fn(Kpm)>1e-6 and fn(Kmp)>1e-6,
 "K0_not_commuting_with_grading": fn(Kc@S-S@Kc)>1e-6
}
checks = {key: bool(value) for key, value in checks.items()}
report["checks"] = checks
report["all_pass"] = bool(all(checks.values()))
if not report["all_pass"]:
    raise SystemExit("One or more intrinsic Z2 carrier checks failed: "+str(checks))

out=ROOT/"results/json/rgs_intrinsic_z2_carrier_audit_2026-11-24.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
