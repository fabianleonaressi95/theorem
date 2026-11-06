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
from itertools import product
from pathlib import Path
from typing import Any

import numpy as np

Q_G2 = np.array([[2.0, -3.0], [-3.0, 6.0]], dtype=float)
DEFAULT_TOL = 1.0e-10
PHI = (1.0 + math.sqrt(5.0)) / 2.0
# Supergolden constant: the real root > 1 of x^3 - x^2 - 1 = 0.
PSI_SUPERGOLDEN = 1.465571231876768


def wg2_group() -> list[np.ndarray]:
    """Generate W(G2) in the simple-root basis with Gram matrix Q_G2."""
    s1 = np.array([[-1, 3], [0, 1]], dtype=int)
    s2 = np.array([[1, 0], [1, -1]], dtype=int)
    pending = [np.eye(2, dtype=int)]
    found: dict[tuple[int, ...], np.ndarray] = {}
    while pending:
        M = pending.pop()
        key = tuple(M.ravel())
        if key in found:
            continue
        found[key] = M
        pending.extend((s1 @ M, s2 @ M))
    group = [found[k] for k in sorted(found)]
    if len(group) != 12:
        raise AssertionError(f"W(G2) must have order 12, got {len(group)}")
    for M in group:
        if not np.array_equal(M.T @ Q_G2.astype(int) @ M, Q_G2.astype(int)):
            raise AssertionError("a generated Weyl matrix does not preserve Q_G2")
    if not all(round(np.linalg.det(M)) in (-1, 1) for M in group):
        raise AssertionError("W(G2) matrix determinant is not ±1")
    return group


def enumerate_wg2_triples() -> dict[str, Any]:
    """Enumerate 6^3 ordered triples from one six-element short-root orbit."""
    group = wg2_group()
    seed = np.array([1, 0], dtype=int)
    roots = sorted({tuple((M @ seed).tolist()) for M in group})
    if len(roots) != 6:
        raise AssertionError(f"short-root orbit must contain 6 roots, got {len(roots)}")
    root_index = {root: i for i, root in enumerate(roots)}
    triples = list(product(range(6), repeat=3))
    unseen = set(triples)
    orbits: list[list[tuple[int, int, int]]] = []
    while unseen:
        t = min(unseen)
        orbit = {
            tuple(root_index[tuple((M @ np.asarray(roots[i], dtype=int)).tolist())] for i in t)
            for M in group
        }
        if not orbit.issubset(unseen):
            raise AssertionError("W(G2) action produced overlapping non-identical orbits")
        unseen.difference_update(orbit)
        orbits.append(sorted(orbit))
    orbits.sort(key=lambda orb: orb[0])

    def gram_key(t: tuple[int, int, int]) -> tuple[int, ...]:
        R = np.asarray([roots[i] for i in t], dtype=int).T
        G = R.T @ Q_G2.astype(int) @ R
        return tuple(int(x) for x in G.ravel())

    orbit_gram_keys = []
    for orbit in orbits:
        keys = {gram_key(t) for t in orbit}
        if len(keys) != 1:
            raise AssertionError("Gram matrix is not invariant on a W(G2) orbit")
        orbit_gram_keys.append(next(iter(keys)))
    gram_to_orbit = {}
    for i, key in enumerate(orbit_gram_keys):
        gram_to_orbit.setdefault(key, []).append(i)
    if len(gram_to_orbit) != len(orbits):
        raise AssertionError("distinct W(G2) orbits share a Gram matrix")
    sizes = Counter(len(orb) for orb in orbits)
    return {
        "group_order": len(group),
        "simple_reflection_s1": [[-1, 3], [0, 1]],
        "simple_reflection_s2": [[1, 0], [1, -1]],
        "Q_G2": Q_G2.astype(int).tolist(),
        "det_Q_G2": int(round(np.linalg.det(Q_G2))),
        "short_root_orbit": [list(r) for r in roots],
        "triple_count": len(triples),
        "orbit_count": len(orbits),
        "orbit_size_histogram": {str(k): int(v) for k, v in sorted(sizes.items())},
        "gram_class_count": len(gram_to_orbit),
        "gram_classes_equal_weyl_orbits": True,
        "degenerate_triples": sum(
            np.linalg.matrix_rank(np.asarray([roots[i] for i in t]).T) < 2
            for t in triples
        ),
        "nondegenerate_triples": sum(
            np.linalg.matrix_rank(np.asarray([roots[i] for i in t]).T) == 2
            for t in triples
        ),
        "triples": [
            {
                "indices": list(t),
                "vectors": [list(roots[i]) for i in t],
                "orbit_id": next(j for j, orb in enumerate(orbits) if t in set(orb)),
                "gram": (
                    np.asarray([roots[i] for i in t], dtype=int).T
                    @ Q_G2.astype(int)
                    @ np.asarray([roots[i] for i in t], dtype=int)
                ).tolist(),
            }
            for t in triples
        ],
    }


def alpha_supergolden_candidate(rho: float, alpha_star: float) -> float:
    """Candidate interpolation only; not a derived geometric law."""
    if not math.isfinite(rho) or not math.isfinite(alpha_star):
        raise ValueError("rho and alpha_star must be finite")
    return alpha_star * math.sin(
        0.5 * math.pi * (rho - PHI) / (PSI_SUPERGOLDEN - PHI)
    )


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
    # L^T L = Q_G2: the same G2 metric is used in the planar Gram
    # and in the tangent part of the spatial lift.
    L = np.linalg.cholesky(Q_G2).T
    V = E @ L @ S @ R + alpha * np.outer(n, c)
    G = V.T @ V
    G_planar = R.T @ S.T @ Q_G2 @ S @ R
    G_lift = G_planar + alpha * alpha * np.outer(c, c)
    det_v = float(np.linalg.det(V))
    det_g = float(np.linalg.det(G))
    det_expected = float(np.linalg.det(Q_G2) * alpha * alpha * np.dot(c, c) ** 2)
    det_v_expected = float(math.sqrt(np.linalg.det(Q_G2)) * alpha * np.dot(c, c))
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
        "det_V_expected": det_v_expected,
        "det_V_identity_abs_error": abs(det_v - det_v_expected),
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
    rho = float(data["rho"])
    if "alpha" in data:
        alpha = float(data["alpha"])
        alpha_source = "explicit"
    elif "alpha_star" in data:
        alpha = alpha_supergolden_candidate(rho, float(data["alpha_star"]))
        alpha_source = "candidate_alpha_supergolden_interpolation"
    else:
        raise ValueError("provide either 'alpha' or candidate parameter 'alpha_star'")

    generated = None
    triples = data.get("triples")
    if triples is None:
        generated = enumerate_wg2_triples()
        triples = [item["vectors"] for item in generated["triples"]]
    if not isinstance(triples, list) or not triples:
        raise ValueError("the 'triples' array must be non-empty")
    rows = [audit_one(t, rho, alpha, tol) for t in triples]
    grams = [np.asarray(r["gram_planar"], dtype=float) for r in rows]
    keys = [canonical_symmetric_key(G, tol) for G in grams]
    nclasses = len(Counter(keys))
    expected_n = data.get("expected_triples", 216 if generated else None)
    expected_c = data.get("expected_gram_classes", 20 if generated else None)
    seam = [mobius_seam_audit(int(n)) for n in data.get("mobius_levels", [1, 2, 3])]
    nondegenerate = [r for r in rows if r["rank_R"] == 2]
    degenerate = [r for r in rows if r["rank_R"] < 2]
    checks = {
        "all_Rc_zero": all(r["Rc_norm"] <= 100 * tol for r in rows),
        "all_determinant_identities": all(
            r["det_identity_abs_error"] <= 1000 * tol
            and r["det_V_identity_abs_error"] <= 1000 * tol for r in rows
        ),
        "all_gram_lift_identities": all(r["gram_lift_identity_error"] <= 100 * tol for r in rows),
        "rank_three_on_every_nondegenerate_triple": all(r["rank_three"] for r in nondegenerate),
        "degenerate_triples_remain_rank_two": all(r["rank_V"] == 2 for r in degenerate),
        "positive_definite_on_every_nondegenerate_triple": all(r["positive_definite"] for r in nondegenerate),
        "expected_triple_count": None if expected_n is None else len(rows) == int(expected_n),
        "expected_gram_class_count": None if expected_c is None else nclasses == int(expected_c),
        "all_mobius_involutions": all(s["involution_ok"] for s in seam),
    }
    return {
        "schema": "rgs-g2-mobius-lift-audit-v1",
        "parameters": {"rho": rho, "alpha": alpha, "alpha_source": alpha_source, "tolerance": tol},
        "wg2_enumeration": generated,
        "summary": {
            "triple_count": len(rows),
            "planar_gram_class_count": nclasses,
            "nondegenerate_triples": len(nondegenerate),
            "degenerate_triples": len(degenerate),
            "rank_three_count": sum(r["rank_three"] for r in rows),
            "positive_definite_lift_count": sum(r["positive_definite"] for r in rows),
            "minimum_lift_eigenvalue": min(min(r["gram_eigenvalues"]) for r in rows),
            "maximum_determinant_identity_error": max(
                max(r["det_identity_abs_error"], r["det_V_identity_abs_error"]) for r in rows
            ),
        },
        "checks": checks,
        "mobius_seams": seam,
        "triples": rows,
        "limitations": [
            "The built-in W(G2) construction uses the orbit of the short simple root (1,0) under the generated order-12 Weyl group.",
            "The alpha(rho) sine interpolation is a candidate parametrization, not a theorem derived from W(G2).",
            "Gram class count depends on the declared absolute tolerance; matrices are not rescaled before comparison.",
            "The index seam test does not test shared-face geometry, cell injectivity, positive cell Jacobians, or global mesh conformity.",
            "No FEEC stability, discrete compactness, Mosco convergence, or spectral convergence is claimed.",
        ],
    }

def self_test() -> dict[str, Any]:
    generated = enumerate_wg2_triples()
    assert generated["group_order"] == 12
    assert generated["triple_count"] == 216
    assert generated["orbit_count"] == 20
    assert generated["orbit_size_histogram"] == {"6": 4, "12": 16}
    assert generated["gram_class_count"] == 20
    assert generated["gram_classes_equal_weyl_orbits"]
    assert generated["degenerate_triples"] == 24
    assert generated["nondegenerate_triples"] == 192
    payload = audit_payload({
        "rho": PSI_SUPERGOLDEN,
        "alpha_star": 0.7,
        "mobius_levels": list(range(1, 7)),
    })
    assert all(payload["checks"].values())
    assert payload["summary"]["rank_three_count"] == 192
    assert payload["summary"]["positive_definite_lift_count"] == 192
    return {
        "self_test": "PASS",
        "wg2_group_order": generated["group_order"],
        "short_root_count": len(generated["short_root_orbit"]),
        "triple_count": generated["triple_count"],
        "gram_class_count": generated["gram_class_count"],
        "orbit_size_histogram": generated["orbit_size_histogram"],
        "degenerate_triples": generated["degenerate_triples"],
        "rank_three_nondegenerate_triples": payload["summary"]["rank_three_count"],
        "mobius_levels_checked": list(range(1, 7)),
        "alpha_candidate_at_psi": payload["parameters"]["alpha"],
    }

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
