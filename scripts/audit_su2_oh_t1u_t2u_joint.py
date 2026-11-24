#!/usr/bin/env python3
"""Joint K0 spin-ladder / O_h T1u,T2u audit.

The script deliberately requires an independently certified orthogonal basis map.
It never fits that map by minimizing commutators. No cross-basis claim is emitted
when the certificate is absent.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from itertools import permutations, product

import numpy as np


def signed_permutations():
    out = []
    for perm in permutations(range(3)):
        P = np.zeros((3, 3))
        for row, col in enumerate(perm):
            P[row, col] = 1.0
        for signs in product((-1.0, 1.0), repeat=3):
            out.append(P @ np.diag(signs))
    return out


def t2g_character(R):
    # Character on (xy,yz,zx), the off-diagonal quadratic forms.
    return float(sum(R[i, i] * R[j, j] + R[i, j] * R[j, i]
                     for i, j in ((0, 1), (1, 2), (2, 0))) / 1.0)


def tangent_action(X, Q, G, tol=1e-8):
    transformed = X @ G.T
    distances = np.linalg.norm(transformed[:, None, :] - X[None, :, :], axis=2)
    p = np.argmin(distances, axis=1)
    if distances[np.arange(len(X)), p].max() > tol or len(np.unique(p)) != len(X):
        raise ValueError("O_h element does not preserve the point cloud")
    D = np.zeros((3 * len(X), 3 * len(X)))
    for source, target in enumerate(p):
        D[3*target:3*target+3, 3*source:3*source+3] = G
    R = Q.T @ D @ Q
    residual = np.linalg.norm(D @ Q - Q @ R)
    if residual > 1e-7:
        raise ValueError(f"tangent action residual {residual:g}")
    return R


def cubic_projector(X, Q, irrep):
    terms = []
    for G in signed_permutations():
        parity = int(round(np.linalg.det(G)))
        Rproper = parity * G
        chi = np.trace(Rproper) if irrep == "T1u" else t2g_character(Rproper)
        chi *= parity
        terms.append((chi, tangent_action(X, Q, G)))
    P = (3.0 / 48.0) * sum(chi * R for chi, R in terms)
    return 0.5 * (P + P.T)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def rank(A, tol=1e-8):
    return int(np.linalg.matrix_rank(A, tol=tol))


def intersection_dimension(A, B, tol=1e-7):
    # A and B have orthonormal columns; singular values 1 correspond to
    # common subspace directions. This avoids treating AB^T as a projector.
    s = np.linalg.svd(A.T @ B, compute_uv=False)
    return int(np.sum(s >= 1.0 - tol)), s.tolist()


def block_report(P, B):
    I = np.eye(P.shape[0])
    Q = I - P
    blocks = {
        "kernel_to_kernel": P @ B @ P,
        "kernel_from_complement": P @ B @ Q,
        "complement_from_kernel": Q @ B @ P,
        "complement_to_complement": Q @ B @ Q,
    }
    return {k: {"rank": rank(v), "frobenius": float(np.linalg.norm(v, "fro")),
                "spectral_norm": float(np.linalg.norm(v, 2))}
            for k, v in blocks.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--npz", default="data/RGS_PSU_all_matrices.npz")
    ap.add_argument("--k0", default="K0.npy")
    ap.add_argument("--zs", default="Z_S.npy")
    ap.add_argument("--za", default="Z_A.npy")
    ap.add_argument("--pg", default="P_G.npy")
    ap.add_argument("--basis-map", required=True,
                    help="188x188 orthogonal C mapping geometric tangent coordinates to K0-array coordinates")
    ap.add_argument("--out", default="audits/SU2_OH_DOUBLE_GROUP_T1U_T2U_NUMERICAL.json")
    args = ap.parse_args()

    Cpath = Path(args.basis_map)
    if not Cpath.exists():
        raise SystemExit(f"Missing independent basis-map certificate: {Cpath}")
    C = np.load(Cpath)
    if C.shape != (188, 188):
        raise SystemExit("basis map must be 188x188")
    orth = float(np.linalg.norm(C.T @ C - np.eye(188), "fro"))
    if orth > 1e-8:
        raise SystemExit(f"basis map is not orthogonal: residual={orth:g}")

    z = np.load(args.npz)
    X = np.asarray(z["X_Oh_reconstructed"], float)
    Q = np.asarray(z["Q_tangent"], float)
    K0, ZS, ZA, PG = (np.load(args.k0), np.load(args.zs),
                      np.load(args.za), np.load(args.pg))
    if any(a.shape != (188, 188) for a in (K0, ZS, ZA, PG)):
        raise SystemExit("all operator arrays must be 188x188")

    # The group projectors are built in the geometric Q_tangent coordinates,
    # then transported only through the user-supplied certified map C.
    P1g = cubic_projector(X, Q, "T1u")
    P2g = cubic_projector(X, Q, "T2u")
    P1, P2 = C @ P1g @ C.T, C @ P2g @ C.T
    I = np.eye(188)
    Pperp = I - PG

    # Verify the claimed 39D/30D isotypic ranks before using the projectors.
    p1err = float(np.linalg.norm(P1 @ P1 - P1, "fro"))
    p2err = float(np.linalg.norm(P2 @ P2 - P2, "fro"))
    r1, r2 = rank(P1), rank(P2)
    if (r1, r2) != (39, 30) or max(p1err, p2err) > 1e-7:
        raise SystemExit(f"cubic projector check failed: ranks={(r1,r2)}, idem={(p1err,p2err)}")

    # Principal-angle intersections with the kernel and its complement.
    w, V = np.linalg.eigh(0.5 * (PG + PG.T))
    UG = V[:, w > 0.5]
    w, V = np.linalg.eigh(0.5 * (Pperp + Pperp.T))
    Uperp = V[:, w > 0.5]
    intersections = {}
    for name, P in (("T1u", P1), ("T2u", P2)):
        w, V = np.linalg.eigh(0.5 * (P + P.T))
        U = V[:, w > 0.5]
        dg, sg = intersection_dimension(U, UG)
        dp, sp = intersection_dimension(U, Uperp)
        intersections[name] = {
            "kernel_intersection_dim": dg,
            "complement_intersection_dim": dp,
            "kernel_principal_cosines": sg,
            "complement_principal_cosines": sp,
            "projector_kernel_commutator_fro": float(np.linalg.norm(P @ PG - PG @ P, "fro")),
        }

    # Canonical spin-61/2 ladder in the ordered positive K0 eigenspace.
    evals, evecs = np.linalg.eigh(0.5 * (K0 + K0.T))
    pos = np.flatnonzero(evals > 1e-8)
    if len(pos) != 124:
        raise SystemExit(f"expected 124 positive modes, got {len(pos)}")
    order = pos[np.argsort(evals[pos])]
    Vp = evecs[:, order]
    expected = (np.arange(124) + 5.0) / 10.0
    spectrum_error = float(np.max(np.abs(evals[order] - expected)))
    if spectrum_error > 1e-7:
        raise SystemExit(f"K0 positive ladder mismatch: {spectrum_error:g}")
    j = 61.5
    m = -j + np.arange(124)
    Jz = np.diag(m)
    Jplus = np.zeros((124, 124))
    for n in range(123):
        Jplus[n+1, n] = np.sqrt((j - m[n]) * (j + m[n] + 1))
    Jminus = Jplus.T
    Jz188, Jp188, Jm188 = (Vp @ A @ Vp.T for A in (Jz, Jplus, Jminus))
    ladder = {
        "spectrum_max_abs_error": spectrum_error,
        "Jz_Jplus_commutator_fro": float(np.linalg.norm(Jz @ Jplus - Jplus @ Jz - Jplus)),
        "Jz_Jminus_commutator_fro": float(np.linalg.norm(Jz @ Jminus - Jminus @ Jz + Jminus)),
        "Jplus_Jminus_commutator_fro": float(np.linalg.norm(Jplus @ Jminus - Jminus @ Jplus - 2*Jz)),
        "casimir_fro": float(np.linalg.norm(0.25*(Jplus+Jminus)@(Jplus+Jminus)
            - 0.25*(Jplus-Jminus)@(Jplus-Jminus) + Jz@Jz
            - j*(j+1)*np.eye(124), "fro")),
    }

    def delta_profile(B):
        M = Vp.T @ B @ Vp
        profile = {}
        for delta in range(-123, 124):
            vals = np.diag(M, k=-delta) if delta >= 0 else np.diag(M, k=-delta)
            profile[str(delta)] = float(np.linalg.norm(vals))
        total = float(np.linalg.norm(M, "fro"))
        outside3 = sum(v*v for k, v in profile.items() if abs(int(k)) != 3)
        return {"frobenius_total": total, "delta_m_frobenius": profile,
                "fractional_norm_outside_abs_delta_3": float(np.sqrt(outside3)/total) if total else 0.0}

    # Operator blocks are computed in the certified K0 coordinate system.
    ops = {"Z_S": ZS, "Z_A": ZA, "T_transport": np.asarray(z["T_transport"], float)}
    operator_report = {}
    for name, B in ops.items():
        operator_report[name] = {
            "kernel_complement_blocks": block_report(PG, B),
            "T1u_T2u_block_norms": {
                "T1u_to_T1u": float(np.linalg.norm(P1 @ B @ P1, "fro")),
                "T1u_to_T2u": float(np.linalg.norm(P1 @ B @ P2, "fro")),
                "T2u_to_T1u": float(np.linalg.norm(P2 @ B @ P1, "fro")),
                "T2u_to_T2u": float(np.linalg.norm(P2 @ B @ P2, "fro")),
            },
        }
        if name in ("Z_S", "Z_A"):
            operator_report[name]["ladder_basis_delta_m"] = delta_profile(B)

    report = {
        "classification": "numerical audit conditional on supplied orthogonal common-basis map",
        "basis_map": {"path": str(Cpath), "sha256": sha256(Cpath),
                      "orthogonality_fro": orth,
                      "convention": "operator_coordinates = C @ geometric_coordinates"},
        "cubic_projectors": {
            "T1u_rank": r1, "T2u_rank": r2,
            "T1u_idempotence_fro": p1err, "T2u_idempotence_fro": p2err,
            "intersection_data": intersections,
        },
        "spin_61_2_ladder": ladder,
        "operators": operator_report,
        "double_group_note": (
            "This script audits the ordinary O_h isotypic blocks and the K0 ladder. "
            "It does not yet claim a binary-octahedral character decomposition; "
            "that requires an explicit double-group character table/restriction audit."
        ),
        "input_hashes": {p: sha256(p) for p in (args.npz,args.k0,args.zs,args.za,args.pg)},
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
