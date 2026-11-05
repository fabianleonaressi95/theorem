#!/usr/bin/env python3
"""Archive-aware finite audits for recovered Q6 and RGS 188D bundles.

Requires Python 3.10+ and NumPy. The two source archives are external inputs:
Q6_K_J_reconstruction.zip and 188D_FINAL_BUNDLE.zip.
"""
from __future__ import annotations
import argparse
import json
import math
import platform
import zipfile
import numpy as np


def load_array(archive, name):
    return np.load(archive.open(name), allow_pickle=False)


def fro(a):
    return float(np.linalg.norm(a, ord="fro"))


def audit_q6(path):
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        required = {"states_Q6.npy", "A_Q6.npy", "K6_laplacian.npy",
                    "J_antipodal.npy", "R_bit_rotation.npy"}
        if not required <= names:
            raise ValueError(f"Q6 archive missing {sorted(required - names)}")
        S = load_array(z, "states_Q6.npy")
        A = load_array(z, "A_Q6.npy")
        L = load_array(z, "K6_laplacian.npy")
        J = load_array(z, "J_antipodal.npy")
        R = load_array(z, "R_bit_rotation.npy")
        eig = np.linalg.eigvalsh(L)
        vals, counts = np.unique(np.round(eig, 8), return_counts=True)
        tests = {
            "states_64x6": S.shape == (64, 6),
            "adjacency_64x64": A.shape == (64, 64),
            "edge_count_192": int(np.sum(A) / 2) == 192,
            "six_regular": bool(np.all(A.sum(axis=1) == 6)),
            "adjacency_symmetric": fro(A - A.T) == 0,
            "laplacian_is_D_minus_A": fro(L - (6*np.eye(64) - A)) < 1e-12,
            "J_involution": fro(J@J - np.eye(64)) < 1e-12,
            "J_orthogonal": fro(J.T@J - np.eye(64)) < 1e-12,
            "J_commutes_L": fro(J@L - L@J) < 1e-12,
            "R_orthogonal": fro(R.T@R - np.eye(64)) < 1e-12,
            "R_commutes_L": fro(R@L - L@R) < 1e-12,
        }
        return {
            "shapes": {"states": list(S.shape), "A": list(A.shape),
                       "L": list(L.shape), "J": list(J.shape), "R": list(R.shape)},
            "spectrum": {str(float(v)): int(c) for v, c in zip(vals, counts)},
            "residuals": {
                "A_sym": fro(A-A.T), "L_DminusA": fro(L-(6*np.eye(64)-A)),
                "J2_I": fro(J@J-np.eye(64)), "J_L_comm": fro(J@L-L@J),
                "R_orth": fro(R.T@R-np.eye(64)), "R_L_comm": fro(R@L-L@R),
            },
            "checks": tests, "all_checks_pass": all(tests.values()),
            "interpretation": "Q6 graph and archived involution/bit rotation only; not the Krist-All K or a physical silicon Hamiltonian.",
        }


def audit_188d(path):
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        required = {"K0.npy", "Kinv.npy", "P_G.npy", "J.npy", "J_A.npy", "J_B.npy"}
        if not required <= names:
            raise ValueError(f"188D archive missing {sorted(required - names)}")
        K = load_array(z, "K0.npy")
        Ki = load_array(z, "Kinv.npy")
        P = load_array(z, "P_G.npy")
        J = load_array(z, "J.npy")
        JA = load_array(z, "J_A.npy")
        JB = load_array(z, "J_B.npy")
        I = np.eye(188)
        eig = np.linalg.eigvalsh(K)
        tol = 1e-8
        tests = {
            "K0_188x188": K.shape == (188, 188),
            "Kinv_188x188": Ki.shape == (188, 188),
            "PG_188x188": P.shape == (188, 188),
            "finite": all(np.isfinite(x).all() for x in (K, Ki, P, J, JA, JB)),
            "K0_symmetric": fro(K-K.T) < 1e-12,
            "Kinv_symmetric": fro(Ki-Ki.T) < 1e-10,
            "PG_symmetric": fro(P-P.T) < 1e-12,
            "PG_idempotent": fro(P@P-P) < 1e-10,
            "PG_rank_64": int(np.linalg.matrix_rank(P, tol=1e-8)) == 64,
            "K0_rank_124": int(np.linalg.matrix_rank(K, tol=1e-8)) == 124,
            "K0_PG_annihilation": fro(K@P) < 1e-9 and fro(P@K) < 1e-9,
            "K0_Kinv_inverse_on_complement": fro(K@Ki-(I-P)) < 1e-9 and fro(Ki@K-(I-P)) < 1e-9,
            "J_frame_188x6": J.shape == (188, 6),
            "JA_frame_188x3": JA.shape == (188, 3),
            "JB_frame_188x3": JB.shape == (188, 3),
        }
        return {
            "shapes": {"K0": list(K.shape), "Kinv": list(Ki.shape), "P_G": list(P.shape),
                       "J": list(J.shape), "J_A": list(JA.shape), "J_B": list(JB.shape)},
            "spectrum_K0": {
                "min": float(eig.min()), "max": float(eig.max()),
                "negative": int((eig < -tol).sum()), "near_zero": int((abs(eig) <= tol).sum()),
                "positive": int((eig > tol).sum()), "tolerance": tol,
            },
            "residuals": {
                "K0_sym": fro(K-K.T), "Kinv_sym": fro(Ki-Ki.T), "PG_sym": fro(P-P.T),
                "PG_idempotence": fro(P@P-P), "K0PG": fro(K@P), "PGK0": fro(P@K),
                "K0Kinv_minus_IminusPG": fro(K@Ki-(I-P)),
                "KinvK0_minus_IminusPG": fro(Ki@K-(I-P)),
            },
            "checks": tests, "all_checks_pass": all(tests.values()),
            "limitations": [
                "The archived bundle contains K0/Kinv/P_G and J frames, but not Q_tangent, X_Oh_reconstructed, or B_T2U_TAN.",
                "No tangent-basis geometry or vierbein audit is claimed from this bundle alone.",
            ],
        }


def audit_prism():
    dims = (64, 6, 6, 6, 5)
    n = math.prod(dims)
    gap = 4 * math.sin(math.pi / 64) ** 2

    def index(g, l, c, t, b):
        return ((((g*6+l)*6+c)*6+t)*5+b)

    ids = [index(g, l, c, t, b)
           for g in range(64) for l in range(6)
           for c in range(6) for t in range(6) for b in range(5)]
    roots = np.roots([1, -1, 0, -1])
    psi = float(roots[np.isreal(roots)].real.max())
    shift_order = math.lcm(*dims)
    tests = {
        "vertices_69120": n == 69120,
        "edges_345600": n*10//2 == 345600,
        "gap_match": abs(gap-0.009630546655606228) < 1e-15,
        "mixed_radix_index_bijective": len(ids) == len(set(ids)) == n and min(ids) == 0 and max(ids) == n-1,
        "supergolden_cubic": abs(psi**3-psi**2-1) < 1e-12,
        "simultaneous_shift_order_960": shift_order == 960,
    }
    return {
        "vertices": n, "degree": 10, "undirected_edges": n*10//2,
        "laplacian_gap": gap,
        "mixed_radix_index": {"bijection": tests["mixed_radix_index_bijective"], "min": min(ids), "max": max(ids)-0},
        "supergolden_root": psi, "cubic_residual": psi**3-psi**2-1,
        "simultaneous_shift_order": shift_order, "checks": tests,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--q6-zip", required=True)
    ap.add_argument("--188d-zip", required=True)
    ap.add_argument("--output", default="")
    args = ap.parse_args()
    q6 = audit_q6(args.q6_zip)
    rgs = audit_188d(args.__dict__["188d_zip"])
    prism = audit_prism()
    checks = {"q6_"+k: v for k, v in q6["checks"].items()}
    checks.update({"188d_"+k: v for k, v in rgs["checks"].items()})
    checks.update({"prism_"+k: v for k, v in prism["checks"].items()})
    report = {
        "schema": "rgs-prism-archived-verification/v1",
        "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "sources": {"q6_archive": args.q6_zip, "188d_archive": args.__dict__["188d_zip"]},
        "q6": q6, "rgs_188d": rgs, "prism": prism,
        "checks": checks, "all_checks_pass": all(checks.values()),
        "not_established": [
            "Krist-All 11,725-class construction or its K^3=K^2+I matrix identity: no such K matrix is in these archives; the recovered source-level index/root/shift identities are checked.",
            "188D coordinate embedding X_Oh, tangent basis Q, B_T2U, vierbein or teleparallel connection.",
            "PRISM filtered active-subgraph spectrum/homology.",
            "Mosco-2 compactness or continuum Laplace-Beltrami-Yang-Mills limit.",
        ],
    }
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(rendered + "\n")
    print(rendered)
    if not report["all_checks_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
