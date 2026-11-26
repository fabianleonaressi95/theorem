#!/usr/bin/env python3
"""Exact finite Q6 Walsh-influence and cubical-gradient audit for T108."""
from __future__ import annotations

import json
from fractions import Fraction
from itertools import product


N = 6
SIZE = 1 << N


def mean(values):
    return sum(values, Fraction(0)) / SIZE


def variance(values):
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / SIZE


def influences(values):
    out = []
    for i in range(N):
        out.append(sum(
            (values[x] - values[x ^ (1 << i)]) ** 2
            for x in range(SIZE)
        ) / SIZE)
    return out


def walsh_coefficients(values):
    coeffs = {}
    for mask in range(SIZE):
        total = sum(
            values[x] * (-1 if (mask & x).bit_count() % 2 else 1)
            for x in range(SIZE)
        )
        coeffs[mask] = total / SIZE
    return coeffs


def face_curl(values):
    """Return all oriented square circulations of the exact gradient."""
    curls = []
    for i in range(N):
        for j in range(i + 1, N):
            for x in range(SIZE):
                if (x >> i) & 1 or (x >> j) & 1:
                    continue
                xi, xj, xij = x ^ (1 << i), x ^ (1 << j), x ^ (1 << i) ^ (1 << j)
                circulation = (
                    (values[xi] - values[x])
                    + (values[xij] - values[xi])
                    - (values[xij] - values[xj])
                    - (values[xj] - values[x])
                )
                curls.append(circulation)
    return curls


def audit():
    # A deterministic nontrivial integer-valued function on all 64 vertices.
    values = [
        Fraction(((x * 37 + (x ^ (x >> 1)) * 11 + 19) % 101) - 50)
        for x in range(SIZE)
    ]
    inf = influences(values)
    coeffs = walsh_coefficients(values)
    var = variance(values)
    spectral_sum = 4 * sum(
        Fraction(mask.bit_count()) * coeffs[mask] ** 2
        for mask in range(1, SIZE)
    )
    expected = 4 * var
    return {
        "status": "PASS" if (
            sum(inf) == spectral_sum
            and sum(inf) >= expected
            and max(inf) >= Fraction(2, 3) * var
            and all(c == 0 for c in face_curl(values))
        ) else "FAIL",
        "vertices": SIZE,
        "edges": N * SIZE // 2,
        "variance": str(var),
        "coordinate_influences": [str(v) for v in inf],
        "sum_influences": str(sum(inf)),
        "fourier_weighted_sum": str(spectral_sum),
        "poincare_lower_bound_4_variance": str(expected),
        "max_influence_ge_2_over_3_variance": bool(max(inf) >= Fraction(2, 3) * var),
        "square_curl_count": len(face_curl(values)),
        "all_square_curls_zero": all(c == 0 for c in face_curl(values)),
        "arithmetic": "exact rational",
        "scope": "finite Q6 regression only; no dimension-uniform AA proof",
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
