#!/usr/bin/env python3
"""Deterministic symmetry audit for the 3D Herasymov-style totalistic CA.

Dependencies: numpy
Run: python audit_symmetry.py
The script checks all 24 proper cubic rotations on small periodic tori.
It also checks the origin-anchored kk=0 padding intertwining identity.
"""
from __future__ import annotations
import itertools
import json
import numpy as np


def cubic_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3), dtype=int)
        for i, j in enumerate(perm):
            P[i, j] = 1
        for signs in itertools.product((-1, 1), repeat=3):
            R = np.diag(signs) @ P
            if round(np.linalg.det(R)) == 1:
                out.append(R)
    assert len(out) == 24
    return out


def rotate_periodic(a: np.ndarray, R: np.ndarray) -> np.ndarray:
    """Active action: (R a)(R x) = a(x), indices modulo side length."""
    L = a.shape[0]
    assert a.shape == (L, L, L)
    out = np.zeros_like(a)
    for x in np.ndindex(a.shape):
        y = tuple((R @ np.asarray(x, dtype=int) % L).tolist())
        out[y] = a[x]
    return out


def padding_kk0(a: np.ndarray) -> np.ndarray:
    L = a.shape[0]
    out = np.zeros((2 * L, 2 * L, 2 * L), dtype=a.dtype)
    out[::2, ::2, ::2] = a
    return out


def totalistic_update(a: np.ndarray, rule: np.ndarray) -> np.ndarray:
    """q=27*c+sum(26 Moore neighbors); periodic boundaries."""
    assert rule.shape == (54,)
    neighbors = np.zeros_like(a, dtype=np.int16)
    for dz, dy, dx in itertools.product((-1, 0, 1), repeat=3):
        if (dz, dy, dx) == (0, 0, 0):
            continue
        neighbors += np.roll(a, shift=(dz, dy, dx), axis=(0, 1, 2))
    q = 27 * a.astype(np.int16) + neighbors
    assert int(q.min()) >= 0 and int(q.max()) <= 53
    return rule[q]


def main():
    rng = np.random.default_rng(20261106)
    rotations = cubic_rotations()
    # A nontrivial periodic configuration; test multiple side lengths.
    cases = []
    for L in (2, 3, 4):
        a = rng.integers(0, 2, size=(L, L, L), dtype=np.uint8)
        rule = rng.integers(0, 2, size=54, dtype=np.uint8)
        F_a = totalistic_update(a, rule)
        max_update_residual = 0
        max_padding_residual = 0
        for R in rotations:
            lhs_update = totalistic_update(rotate_periodic(a, R), rule)
            rhs_update = rotate_periodic(F_a, R)
            max_update_residual = max(
                max_update_residual, int(np.count_nonzero(lhs_update != rhs_update))
            )
            lhs_pad = padding_kk0(rotate_periodic(a, R))
            rhs_pad = rotate_periodic(padding_kk0(a), R)
            max_padding_residual = max(
                max_padding_residual, int(np.count_nonzero(lhs_pad != rhs_pad))
            )
        cases.append({
            "L": L,
            "rotations_tested": len(rotations),
            "update_mismatches_max": max_update_residual,
            "padding_mismatches_max": max_padding_residual,
            "q_min": int((27 * a.astype(np.int16)).min()),
            "q_max_bound": 53,
        })
        assert max_update_residual == 0
        assert max_padding_residual == 0

    # Explicitly test the full index range for the local coding formula.
    q_values = {
        27 * c + s
        for c in (0, 1)
        for s in range(27)
    }
    assert q_values == set(range(54))
    result = {
        "status": "PASS",
        "seed": 20261106,
        "dimension": 3,
        "totalistic_index": "q=27*c+s26",
        "number_of_classes": len(q_values),
        "cubic_proper_rotations": len(rotations),
        "cases": cases,
        "interpretation": [
            "The local update is equivariant under all 24 proper cubic rotations.",
            "The kk=0 padding is equivariant for the origin-anchored index action.",
            "This numerical test supplements, but does not replace, the analytic proof in REPORT.md.",
        ],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
