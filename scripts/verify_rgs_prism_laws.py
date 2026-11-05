#!/usr/bin/env python3
"""Finite structural audits for the PRISM product graph and optional RGS/Krist-All data.

Requires Python 3.10+ and NumPy.
Core PRISM checks need no external files. Optional numerical audits accept an NPZ
archive with keys documented in verification/RGS_PRISM_SUITE.md.

This is a finite-data verification tool, not a proof of a continuum limit or
physical interpretation.
"""
from __future__ import annotations
import argparse
import json
import math
import platform
import numpy as np

DIMS = (64, 6, 6, 6, 5)
N = math.prod(DIMS)
DEGREE = 2 * len(DIMS)


def encode(x):
    g, l, c, t, b = x
    return ((((g * 6 + l) * 6 + c) * 6 + t) * 5 + b)


def decode(k):
    b = k % 5; k //= 5
    t = k % 6; k //= 6
    c = k % 6; k //= 6
    l = k % 6; k //= 6
    g = k
    return (g, l, c, t, b)


def neighbors(k):
    x = list(decode(k))
    out = []
    for axis, modulus in enumerate(DIMS):
        for step in (-1, 1):
            y = x.copy()
            y[axis] = (y[axis] + step) % modulus
            out.append(encode(y))
    return out


def prism_audit():
    seen = set()
    degree_ok = True
    inverse_ok = True
    for k in range(N):
        ns = neighbors(k)
        degree_ok &= len(ns) == DEGREE and len(set(ns)) == DEGREE
        for q in ns:
            inverse_ok &= k in neighbors(q)
            seen.add((k, q))
    # Cartesian-product Laplacian spectrum: sum_j 4 sin^2(pi n_j / L_j).
    # The smallest nonzero eigenvalue is attained in the length-64 factor.
    gap = 4.0 * math.sin(math.pi / 64.0) ** 2
    return {
        "vertices": N,
        "degree": DEGREE,
        "directed_adjacencies": len(seen),
        "undirected_edges": len(seen) // 2,
        "laplacian_gap": gap,
        "expected_laplacian_gap": 0.009630546656,
        "checks": {
            "vertex_count_69120": N == 69120,
            "degree_10": degree_ok and DEGREE == 10,
            "undirected_edge_count_345600": len(seen) == 2 * N * DEGREE // 2,
            "adjacency_reciprocity": inverse_ok,
            "product_graph_gap": abs(gap - 0.009630546656) < 5e-13,
        },
        "scope": "Full Cartesian product C64 □ C6 □ C6 □ C6 □ C5; not a separately filtered active subgraph."
    }


def load_npz(path):
    with np.load(path, allow_pickle=False) as z:
        return {k: z[k] for k in z.files}


def rgs_audit(data):
    required = ("Q", "K_tangent", "B_T2U_TAN")
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError("RGS NPZ missing required arrays: " + ", ".join(missing))
    Q = np.asarray(data["Q"], dtype=float)
    K = np.asarray(data["K_tangent"], dtype=float)
    B = np.asarray(data["B_T2U_TAN"], dtype=float)
    if Q.shape != (192, 188):
        raise ValueError(f"Q must have shape (192,188), got {Q.shape}")
    if K.shape != (188, 188):
        raise ValueError(f"K_tangent must have shape (188,188), got {K.shape}")
    if B.shape != (188, 3):
        raise ValueError(f"B_T2U_TAN must have shape (188,3), got {B.shape}")
    qgram = Q.T @ Q
    q_res = float(np.max(np.abs(qgram - np.eye(188))))
    k_sym = float(np.max(np.abs(K - K.T)))
    eig = np.linalg.eigvalsh((K + K.T) / 2)
    tol = 1e-8
    inertia = {
        "negative": int(np.count_nonzero(eig < -tol)),
        "near_zero": int(np.count_nonzero(np.abs(eig) <= tol)),
        "positive": int(np.count_nonzero(eig > tol)),
    }
    checks = {
        "finite_arrays": bool(np.isfinite(Q).all() and np.isfinite(K).all() and np.isfinite(B).all()),
        "Q_orthonormal_columns": q_res < 1e-10,
        "K_symmetric": k_sym < 1e-10,
        "tangent_dimensions": Q.shape[1] == 188 and B.shape == (188, 3),
    }
    optional = {}
    if "X_Oh_reconstructed" in data:
        X = np.asarray(data["X_Oh_reconstructed"], dtype=float)
        optional["X_Oh_shape"] = list(X.shape)
        checks["X_Oh_shape_64x3"] = X.shape == (64, 3)
    return {
        "shapes": {"Q": list(Q.shape), "K_tangent": list(K.shape), "B_T2U_TAN": list(B.shape)},
        "residuals": {"Q_gram_max_abs": q_res, "K_symmetry_max_abs": k_sym},
        "K_eigenvalues": {"min": float(eig[0]), "max": float(eig[-1]), "inertia_tol_1e-8": inertia},
        "optional": optional,
        "checks": checks,
        "scope": "Numerical audit of supplied finite arrays; eigenvalue inertia depends on the stated tolerance."
    }


def kristall_audit(matrix):
    K = np.asarray(matrix, dtype=float)
    if K.ndim != 2 or K.shape[0] != K.shape[1]:
        raise ValueError("Krist-All K must be a square 2D matrix")
    residual = K @ K @ K - K @ K - np.eye(K.shape[0])
    denom = max(1.0, float(np.linalg.norm(K @ K @ K, ord="fro")),
                float(np.linalg.norm(K @ K, ord="fro")))
    rel = float(np.linalg.norm(residual, ord="fro") / denom)
    return {
        "shape": list(K.shape),
        "polynomial": "K^3 - K^2 - I",
        "relative_frobenius_residual": rel,
        "checks": {"kristall_polynomial_identity": rel < 1e-10},
        "scope": "Checks the stated matrix identity on the supplied matrix; does not certify the class construction."
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rgs-npz", default="", help="Optional NPZ with Q, K_tangent, B_T2U_TAN and optionally X_Oh_reconstructed")
    ap.add_argument("--kristall-matrix", default="", help="Optional .npy square matrix K for K^3=K^2+I")
    ap.add_argument("--output", default="")
    args = ap.parse_args()

    prism = prism_audit()
    sections = {"prism_product_graph": prism}
    checks = dict(prism["checks"])
    if args.rgs_npz:
        rgs = rgs_audit(load_npz(args.rgs_npz))
        sections["rgs_188d"] = rgs
        checks.update({"rgs_" + k: v for k, v in rgs["checks"].items()})
    if args.kristall_matrix:
        kristall = kristall_audit(np.load(args.kristall_matrix, allow_pickle=False))
        sections["kristall"] = kristall
        checks.update({"kristall_" + k: v for k, v in kristall["checks"].items()})

    report = {
        "schema": "rgs-prism-finite-verification/v1",
        "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "sections": sections,
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "limitations": [
            "The PRISM result concerns the full Cartesian product graph, not any filtered active subgraph.",
            "RGS checks apply only to arrays explicitly supplied by the user; this repository does not bundle those data.",
            "Floating-point residuals are numerical evidence, not exact arithmetic certificates.",
            "The Krist-All polynomial test does not verify the 11725-class enumeration or its construction.",
            "No Mosco convergence, second-order continuum limit, Laplace-Beltrami-Yang-Mills limit, or physical claim is established."
        ]
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
