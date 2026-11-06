#!/usr/bin/env python3
"""Independent algebraic audit for the W(G2) planar-to-3D lift and Mobius seam.

Input JSON schema:
{
  "rho": 1.618033988749895,
  "alpha": 1.0,
  "triples": [
    [[x1,y1], [x2,y2], [x3,y3]],
    ...
  ],
  "expected_triples": 216,
  "expected_gram_classes": 20,
  "mobius_levels": [1,2,3,4]
}

The triple list is deliberately supplied as data: this program does not invent
which 216 triples the historical construction selects. It audits the supplied
enumeration, its Gram classes, rank completion, determinant identity, and seam
involution. It does not certify a conforming volume mesh or FEEC convergence.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np

Q_G2 = np.array([[2.0, -3.0], [-3.0, 6.0]], dtype=float)
DEFAULT_TOL = 1.0e-10


def cofactor_vector(R: np.ndarray) -> np.ndarray:
    """For R=[r_x r_y r_z] in R^(2x3), return its signed 2x2 minors."""
    return np.array([
        np.linalg.det(R[:, [1, 2]]),
        np.linalg.det(R[:, [2, 0]]),
        np.linalg.det(R[:, [0, 1]]),
    ])


def canonical_symmetric_key(G: np.ndarray, tol: float) -> tuple[int, ...]:
    """Absolute-tolerance key; class counts depend on the declared tolerance."""
    return tuple(np.rint(G / tol).astype(np.int64).ravel())


def audit_one(triple: Any, rho: float, alpha: float, tol: float) -> dict[str, Any]:
    R = np.asarray(triple, dtype=float).T
    if R.shape != (2, 3) or not np.all(np.isfinite(R)):
        raise ValueError("each triple must contain exactly three finite 2D vectors")
    if rho <= 0 or not math.isfinite(rho):
        raise ValueError("rho must be finite and positive")
    S = np.diag([math.sqrt(rho), 1.0 / math.sqrt(rho)])
    c = cofactor_vector(R)
    annihilation = float(np.linalg.norm(R @ c))
    E = np.array([[1., 0.], [0., 1.], [0., 0.]])
    n = np.array([0., 0., 1.])
    V = E @ S @ R + alpha * np.outer(n, c)
    G = V.T @ V
    G_planar = R.T @ S.T @ Q_G2 @ S @ R
    G_lift = R.T @ S.T @ S @ R + alpha * alpha * np.outer(c, c)
    det_v = float(np.linalg.det(V))
    det_g = float(np.linalg.det(G))
    det_expected = float(alpha * alpha * np.dot(c, c) ** 2)
    eig = np.linalg.eigvalsh(G)
    singular = np.linalg.svd(V, compute_uv=False)
    rank = int(np.linalg.matrix_rank(V, tol=tol))
    return {
        "R": R.tolist(),
        "c": c.tolist(),
        "Rc_norm": annihilation,
        "rank_R": int(np.linalg.matrix_rank(R, tol=tol)),
        "rank_V": rank,
        "det_V": det_v,
        "det_G": det_g,
        "det_G_expected": det_expected,
        "det_identity_abs_error": abs(det_g - det_expected),
        "gram_lift_identity_error": float(np.linalg.norm(G - G_lift)),
        "gram_planar": G_planar.tolist(),
        "gram_lift": G.tolist(),
        "gram_eigenvalues": eig.tolist(),
        "singular_values_V": singular.tolist(),
        "positive_definite": bool(eig[0] > tol),
        "rank_three": bool(rank == 3),
    }


def mobius_seam_audit(level: int) -> dict[str, Any]:
    """Check the two-sided boundary involution and local 3D transition."""
    if level < 1:
        raise ValueError("Mobius levels must be positive integers")
    m = 2 ** level
    # Keep side labels explicit so the seam is a genuine two-sided involution.
    pi = {}
    for j in range(m):
        pi[("R", j)] = ("L", m - 1 - j)
        pi[("L", j)] = ("R", m - 1 - j)
    involution_ok = all(pi[pi[p]] == p for p in pi)
    Rm = np.diag([1.0, -1.0, -1.0])
    tangent = np.diag([1.0, -1.0])
    return {
        "level": level,
        "m": m,
        "boundary_pairs": m,
        "involution_ok": bool(involution_ok),
        "normal_reversal": bool(Rm[2, 2] == -1.0),
        "Rm_squared_identity": bool(np.array_equal(Rm @ Rm, np.eye(3))),
        "Rm_determinant": float(np.linalg.det(Rm)),
        "tangent_transition_determinant": float(np.linalg.det(tangent)),
        "warning": "index involution only; geometric face-trace matching is not tested",
    }


def audit_payload(data: dict[str, Any], tol: float = DEFAULT_TOL) -> dict[str, Any]:
    triples = data.get("triples")
    if not isinstance(triples, list) or not triples:
        raise ValueError("input must contain a non-empty 'triples' array")
    rho = float(data["rho"])
    alpha = float(data["alpha"])
    rows = [audit_one(t, rho, alpha, tol) for t in triples]
    # The 20-class statement refers to Gamma_p, not the lifted metric G.
    grams = [np.asarray(r["gram_planar"], dtype=float) for r in rows]
    keys = [canonical_symmetric_key(G, tol) for G in grams]
    class_counts = Counter(keys)
    nclasses = len(class_counts)
    expected_n = data.get("expected_triples")
    expected_c = data.get("expected_gram_classes")
    seam = [mobius_seam_audit(int(n)) for n in data.get("mobius_levels", [1, 2, 3])]
    checks = {
        "all_Rc_zero": all(r["Rc_norm"] <= 100 * tol for r in rows),
        "all_determinant_identities": all(r["det_identity_abs_error"] <= 1000 * tol for r in rows),
        "all_gram_lift_identities": all(r["gram_lift_identity_error"] <= 100 * tol for r in rows),
        "all_rank_three": all(r["rank_three"] for r in rows),
        "all_gram_positive_definite": all(r["positive_definite"] for r in rows),
        "expected_triple_count": None if expected_n is None else len(rows) == int(expected_n),
        "expected_gram_class_count": None if expected_c is None else nclasses == int(expected_c),
        "all_mobius_involutions": all(s["involution_ok"] for s in seam),
    }
    return {
        "schema": "rgs-g2-mobius-lift-audit-v1",
        "parameters": {"rho": rho, "alpha": alpha, "tolerance": tol},
        "summary": {
            "triple_count": len(rows),
            "planar_gram_class_count": nclasses,
            "rank_three_count": sum(r["rank_three"] for r in rows),
            "positive_definite_lift_count": sum(r["positive_definite"] for r in rows),
            "minimum_lift_eigenvalue": min(min(r["gram_eigenvalues"]) for r in rows),
            "maximum_determinant_identity_error": max(r["det_identity_abs_error"] for r in rows),
        },
        "checks": checks,
        "mobius_seams": seam,
        "triples": rows,
        "limitations": [
            "Gram class count depends on the declared absolute tolerance; matrices are not rescaled before comparison.",
            "The script does not generate or authenticate the historical 216 W(G2) triple selection.",
            "It does not test shared-face geometry, cell injectivity, positive cell Jacobians, or global mesh conformity.",
            "It does not prove FEEC stability, discrete compactness, Mosco convergence, or spectral convergence.",
        ],
    }


def self_test() -> dict[str, Any]:
    # Three independent planar vectors with all 2x2 minors nonzero.
    triple = [[1., 0.], [0., 1.], [1., 1.]]
    row = audit_one(triple, (1. + math.sqrt(5.)) / 2., 0.7, DEFAULT_TOL)
    assert row["Rc_norm"] < 1e-12
    assert row["rank_R"] == 2
    assert row["rank_V"] == 3
    assert row["det_identity_abs_error"] < 1e-10
    assert row["positive_definite"]
    for level in range(1, 7):
        assert mobius_seam_audit(level)["involution_ok"]
    return {"self_test": "PASS", "synthetic_rank": row["rank_V"],
            "determinant_identity_abs_error": row["det_identity_abs_error"],
            "mobius_levels_checked": list(range(1, 7))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="input JSON file")
    parser.add_argument("--output", help="write report JSON to this path")
    parser.add_argument("--tol", type=float, default=DEFAULT_TOL)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        report = self_test()
    elif args.input:
        report = audit_payload(json.loads(Path(args.input).read_text()), args.tol)
    else:
        parser.error("provide input JSON or --self-test")
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(rendered + "\n")
    print(rendered)
    if args.self_test:
        return 0
    hard_checks = [v for v in report["checks"].values() if v is not None]
    return 0 if all(hard_checks) else 2


if __name__ == "__main__":
    sys.exit(main())
