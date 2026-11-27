#!/usr/bin/env python3
"""Compare the Z_S / Z_A half-sector with the lowest eigenspace of K0.

This is a diagnostic only: it does not assign a physical interpretation to 1/2.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sym(A):
    return 0.5 * (A + A.T)


def projector_from_columns(U):
    if U.size == 0:
        return np.zeros((U.shape[0], U.shape[0]))
    return U @ U.T


def support_projector_symmetric(A, threshold=1e-8):
    w, V = np.linalg.eigh(sym(A))
    keep = np.abs(w) > threshold
    U = V[:, keep]
    return projector_from_columns(U), {
        "rank": int(np.sum(keep)),
        "eigenvalues": w.tolist(),
    }


def support_projector_svd(A, threshold=1e-8):
    U, s, _ = np.linalg.svd(A, full_matrices=False)
    keep = s > threshold
    U = U[:, keep]
    return projector_from_columns(U), {
        "rank": int(np.sum(keep)),
        "singular_values": s.tolist(),
    }


def compare(P, Q):
    s = np.linalg.svd(P @ Q, compute_uv=False)
    return {
        "rank_P": int(round(np.trace(P))),
        "rank_Q": int(round(np.trace(Q))),
        "principal_cosines": s.tolist(),
        "intersection_dimension_tol_1e-7": int(np.sum(s > 1.0 - 1e-7)),
        "projector_distance_fro": float(np.linalg.norm(P - Q, "fro")),
        "commutator_fro": float(np.linalg.norm(P @ Q - Q @ P, "fro")),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k0", default="artifacts/K0.npy")
    ap.add_argument("--zs", default="artifacts/Z_S.npy")
    ap.add_argument("--za", default="artifacts/Z_A.npy")
    ap.add_argument("--out", default="audits/HALF_SECTOR_VS_K0_2026-11-24.json")
    ap.add_argument("--tol", type=float, default=1e-8)
    a = ap.parse_args()

    K = np.load(a.k0)
    ZS = np.load(a.zs)
    ZA = np.load(a.za)
    if K.shape != (188, 188) or ZS.shape != K.shape or ZA.shape != K.shape:
        raise SystemExit("Expected K0, Z_S and Z_A to be 188x188.")

    ew, EV = np.linalg.eigh(sym(K))
    pos = np.flatnonzero(ew > a.tol)
    pos = pos[np.argsort(ew[pos])]
    if len(pos) != 124:
        raise SystemExit(f"Expected 124 positive K0 modes, found {len(pos)}")
    lowest = EV[:, pos[0]]
    P_low = np.outer(lowest, lowest)

    # Z_S is expected to be symmetric and have eigenvalues +/-1/2, 0.
    P_zs, zs_support = support_projector_symmetric(ZS, a.tol)
    # For a general antisymmetric Z_A, use its left singular subspace.
    P_za, za_support = support_projector_svd(ZA, a.tol)
    wz, Vz = np.linalg.eigh(sym(ZS))
    Uz = Vz[:, np.abs(wz) > a.tol]
    Ua, sa, _ = np.linalg.svd(ZA, full_matrices=False)
    Ua = Ua[:, sa > a.tol]

    I = np.eye(K.shape[0])
    report = {
        "classification": "numerical diagnostic; no physical interpretation inferred",
        "inputs_sha256": {p: sha256(p) for p in (a.k0, a.zs, a.za)},
        "operator_checks": {
            "K0_symmetry_fro": float(np.linalg.norm(K - K.T, "fro")),
            "ZS_symmetry_fro": float(np.linalg.norm(ZS - ZS.T, "fro")),
            "ZA_antisymmetry_fro": float(np.linalg.norm(ZA + ZA.T, "fro")),
            "ZS_ZA_anticommutator_fro": float(np.linalg.norm(ZS @ ZA + ZA @ ZS, "fro")),
        },
        "K0_spectrum": {
            "positive_count": int(len(pos)),
            "lowest_positive": float(ew[pos[0]]),
            "second_positive": float(ew[pos[1]]),
            "lowest_gap": float(ew[pos[1]] - ew[pos[0]]),
            "lowest_eigenspace_projector_rank": 1,
        },
        "ZS_support": zs_support,
        "ZA_left_singular_support": za_support,
        "support_comparisons": {
            "ZS_vs_lowest_K0": compare(P_zs, P_low),
            "ZA_vs_lowest_K0": compare(P_za, P_low),
            "ZS_vs_ZA": compare(P_zs, P_za),
        },
        "K0_restrictions": {
            "ZS_support_invariance_commutator_fro": float(np.linalg.norm(K @ P_zs - P_zs @ K, "fro")),
            "ZS_support_residual_from_half_fro": float(np.linalg.norm((K - 0.5 * I) @ P_zs, "fro")),
            "ZS_restricted_symmetric_spectrum": np.linalg.eigvalsh(sym(Uz.T @ K @ Uz)).tolist(),
            "ZA_support_invariance_commutator_fro": float(np.linalg.norm(K @ P_za - P_za @ K, "fro")),
            "ZA_support_residual_from_half_fro": float(np.linalg.norm((K - 0.5 * I) @ P_za, "fro")),
            "ZA_restricted_symmetric_spectrum": np.linalg.eigvalsh(sym(Ua.T @ K @ Ua)).tolist(),
        },
        "normalization_checks": {
            "four_ZS_squared_projector_residual_fro": float(np.linalg.norm(4 * ZS @ ZS - P_zs, "fro")),
            "ZA_left_support_projector_idempotence_fro": float(np.linalg.norm(P_za @ P_za - P_za, "fro")),
        },
        "interpretation_guard": (
            "Even exact support coincidence would establish an algebraic relation only. "
            "A physical zero-point, Maslov, spinorial or APS interpretation requires "
            "independent canonical, symplectic, group-action or boundary-Dirac data."
        ),
    }
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
