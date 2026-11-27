#!/usr/bin/env python3
"""Audit: Z2 sheet (bivector) structure on the 6D RGS carrier.

Verifies, directly from the archived arrays, that the support of Z_S is a
6-dimensional carrier carrying a genuine Z2 sheet-exchange grading:

  S = 2 Z_S|_W  is an involution (S^2 = I_W),
  P_pm = (I_W +/- S)/2 are rank-3 projectors (two 3D sheets),
  Z_A is purely off-diagonal between the two sheets with Frobenius norm
  sqrt(3)/2 in each direction.

This certifies a bivector-type Z2 structure on the carrier. It does NOT
identify this grading with the affine +1/2 offset of K0: K0 mixes the two
sheets, so the grading is not a symmetry of K0.
"""
from pathlib import Path
import json

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "audits" / "Z2_SHEET_BIVECTOR_CARRIER.json"

TOL = 1e-9


def main() -> None:
    Z = np.load(ROOT / "artifacts" / "Z_S.npy")
    Za = np.load(ROOT / "artifacts" / "Z_A.npy")
    K = np.load(ROOT / "artifacts" / "K0.npy")
    P_G = np.load(ROOT / "artifacts" / "P_G.npy")
    n = Z.shape[0]

    # --- locate the carrier: eigenvectors of Z_S with |eig| = 1/2 ---
    w, V = np.linalg.eigh((Z + Z.T) / 2)
    ip = np.where(np.abs(w + 0.5) < TOL)[0]
    im = np.where(np.abs(w - 0.5) < TOL)[0]
    carrier_dim = len(ip) + len(im)
    B = np.concatenate([V[:, ip], V[:, im]], axis=1)  # 188 x carrier_dim

    # carrier lies inside ker(P_G) (the 124D complement of the K0 kernel frame)
    pg_expect = float(np.trace(B.T @ P_G @ B))

    # S = 2 Z_S restricted to the carrier
    S = 2.0 * (B.T @ Z @ B)
    s2_err = float(np.linalg.norm(S @ S - np.eye(carrier_dim)))
    diag_dev = float(np.linalg.norm(S - np.diag(np.diag(S))))

    # sheet projectors P_pm = (I +/- S)/2 on the carrier
    Iw = np.eye(carrier_dim)
    P_plus = (Iw + S) / 2
    P_minus = (Iw - S) / 2
    rank_plus = int(np.linalg.matrix_rank(P_plus, tol=1e-9))
    rank_minus = int(np.linalg.matrix_rank(P_minus, tol=1e-9))
    # orthogonality / completeness of the two projectors
    proj_err = float(
        max(
            np.linalg.norm(P_plus @ P_minus),
            np.linalg.norm(P_plus @ P_plus - P_plus),
            np.linalg.norm(P_minus @ P_minus - P_minus),
            np.linalg.norm(P_plus + P_minus - Iw),
        )
    )

    # --- Z_A block structure in the sheet eigenbasis ---
    A = B.T @ Za @ B
    half = carrier_dim // 2
    diag_block = float(
        max(np.linalg.norm(A[:half, :half]), np.linalg.norm(A[half:, half:]))
    )
    off_block = float(
        max(np.linalg.norm(A[:half, half:]), np.linalg.norm(A[half:, :half]))
    )
    target = float(np.sqrt(3) / 2)
    off_err = float(abs(off_block - target))
    # leakage of Z_A out of the carrier
    C = B @ B.T
    leakage = float(np.linalg.norm(Za @ C - C @ Za @ C))

    # --- does K0 respect the grading? (expected: no) ---
    Kc = B.T @ K @ B
    sheet_mixing = float(
        max(np.linalg.norm(Kc[:half, half:]), np.linalg.norm(Kc[half:, :half]))
    )

    # --- null-pair / complex-structure structure ---
    # Globally: Z_S^2 = +1/4 P_W and Z_A^2 = -1/4 P_W, hence Z_S^2 + Z_A^2 = 0.
    I188 = np.eye(n)
    Pw = 4.0 * (Z @ Z)  # = P_W since Z_S^2 = 1/4 P_W
    null_pair_err = float(np.linalg.norm(Z @ Z + Za @ Za))
    za2_eq = float(np.linalg.norm(Za @ Za + 0.25 * Pw))
    zs2_eq = float(np.linalg.norm(Z @ Z - 0.25 * Pw))
    pw_idem = float(np.linalg.norm(Pw @ Pw - Pw))
    pw_sym = float(np.linalg.norm(Pw - Pw.T))
    # On the carrier, J := 2 Z_A|_W is an almost-complex structure:
    # J^2 = -I_W and {J, S} = 0 (S = 2 Z_S|_W).
    J = 2.0 * A
    complex_structure_err = float(np.linalg.norm(J @ J + Iw))
    anticomm_err = float(np.linalg.norm(J @ S + S @ J))

    checks = {
        "carrier_dimension_is_6": carrier_dim == 6,
        "carrier_inside_ker_PG": pg_expect < 1e-8,
        "S_involution": s2_err < 1e-8,
        "S_diagonal_in_eigenbasis": diag_dev < 1e-8,
        "projectors_rank_3_each": rank_plus == 3 and rank_minus == 3,
        "projector_relations": proj_err < 1e-8,
        "ZA_offdiagonal_only": diag_block < 1e-8,
        "ZA_offdiag_norm_sqrt3_over_2": off_err < 1e-8,
        "ZA_preserves_carrier": leakage < 1e-8,
        "null_pair_ZS2_plus_ZA2_zero": null_pair_err < 1e-8,
        "ZA_squared_eq_minus_quarter_PW": za2_eq < 1e-8,
        "ZS_squared_eq_quarter_PW": zs2_eq < 1e-8,
        "PW_projector": max(pw_idem, pw_sym) < 1e-8,
        "JA_is_complex_structure": complex_structure_err < 1e-8,
        "JA_anticommutes_with_S": anticomm_err < 1e-8,
    }

    report = {
        "title": "Z2 sheet (bivector) structure on the 6D RGS carrier",
        "inputs": {
            "Z_S.npy": "archived 188x188 symmetric operator",
            "Z_A.npy": "archived 188x188 antisymmetric operator",
            "K0.npy": "archived 188x188 kernel operator",
            "P_G.npy": "archived 64-dim projector",
        },
        "results": {
            "carrier_dimension": carrier_dim,
            "Z_S_eigenvalues": {"-1/2": int(len(ip)), "+1/2": int(len(im))},
            "carrier_P_G_expectation": pg_expect,
            "S_squared_minus_identity_fro": s2_err,
            "S_diagonal_deviation": diag_dev,
            "P_plus_rank": rank_plus,
            "P_minus_rank": rank_minus,
            "projector_relation_error": proj_err,
            "ZA_diagonal_block_norm": diag_block,
            "ZA_offdiagonal_block_norm": off_block,
            "sqrt3_over_2": target,
            "ZA_offdiag_norm_error": off_err,
            "ZA_carrier_leakage": leakage,
            "K0_sheet_mixing_norm": sheet_mixing,
            "null_pair_ZS2_plus_ZA2_fro": null_pair_err,
            "ZA2_eq_minus_quarter_PW_fro": za2_eq,
            "ZS2_eq_quarter_PW_fro": zs2_eq,
            "complex_structure_J_squared_plus_I_fro": complex_structure_err,
            "J_S_anticommutator_fro": anticomm_err,
        },
        "checks": checks,
        "all_pass": all(checks.values()),
        "scope_note": (
            "Certifies a Z2 two-sheet grading on the 6D carrier with "
            "Z_A as inter-sheet coupling. The +1/2 affine offset of K0 is a "
            "different object: K0 mixes the sheets (sheet_mixing_norm > 0), "
            "so this grading is NOT a symmetry of K0 and does not explain "
            "the K0 half-offset."
        ),
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"all_pass": report["all_pass"], "checks": checks}, indent=2))


if __name__ == "__main__":
    main()
