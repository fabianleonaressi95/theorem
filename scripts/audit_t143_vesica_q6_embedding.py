#!/usr/bin/env python3
"""Numerical audit of the exact T143 Vesica-to-Q6 isometric embedding."""

from __future__ import annotations

import cmath
import math


CODES = (3, 5, 9, 60, 58, 54)
REPRESENTATIVES = (3, 5, 9)
N_Q6 = 64
N_VESICA = 6
TOL = 1e-10


def zeros(rows, cols):
    return [[0.0 for _ in range(cols)] for _ in range(rows)]


def eye(n):
    a = zeros(n, n)
    for i in range(n):
        a[i][i] = 1.0
    return a


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(c, a):
    return [[c * value for value in row] for row in a]


def max_abs(a):
    return max(abs(value) for row in a for value in row)


def max_error(a, b):
    return max_abs(sub(a, b))


def rank(a, tol=TOL):
    m = [list(map(float, row)) for row in a]
    rows, cols = len(m), len(m[0])
    r = 0
    for col in range(cols):
        if r >= rows:
            break
        pivot = max(range(r, rows), key=lambda i: abs(m[i][col]))
        if abs(m[pivot][col]) <= tol:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        p = m[r][col]
        m[r] = [x / p for x in m[r]]
        for i in range(rows):
            if i != r:
                q = m[i][col]
                m[i] = [m[i][j] - q * m[r][j] for j in range(cols)]
        r += 1
    return r


def permutation_involution():
    j = zeros(N_Q6, N_Q6)
    for c in range(N_Q6):
        j[c ^ 63][c] = 1.0
    return j


def build():
    omega = cmath.exp(2j * math.pi / 3)
    points = (1 + 0j, omega, omega ** 2, -1 + 0j, -omega, -(omega ** 2))
    x = zeros(6, 6)
    y = zeros(6, 6)
    for k, z in enumerate(points):
        x[k][k] = z.real
        y[k][k] = z.imag

    # Columns are the six embedded point basis vectors in T142 order.
    iota = zeros(N_Q6, N_VESICA)
    for col, code in enumerate(CODES):
        iota[code][col] = 1.0

    jq = permutation_involution()
    j6 = zeros(6, 6)
    for k in range(3):
        j6[k + 3][k] = 1.0
        j6[k][k + 3] = 1.0

    it = transpose(iota)
    pi = matmul(iota, it)
    x0 = matmul(matmul(iota, x), it)
    y0 = matmul(matmul(iota, y), it)
    return points, x, y, iota, it, jq, j6, pi, x0, y0


def build_full_diagonal_extension(angles):
    """Build one member of the 29-angle full diagonal extension family."""
    if len(angles) != 29:
        raise ValueError("exactly 29 complementary-pair angles are required")
    a = [0.0] * N_Q6
    b = [0.0] * N_Q6
    selected = {
        3: (1.0, 0.0),
        5: (-0.5, math.sqrt(3.0) / 2.0),
        9: (-0.5, -math.sqrt(3.0) / 2.0),
    }
    angle_iter = iter(angles)
    for representative in range(32):
        if representative in selected:
            ca, sb = selected[representative]
        else:
            theta = next(angle_iter)
            ca, sb = math.cos(theta), math.sin(theta)
        partner = representative ^ 63
        a[representative], b[representative] = ca, sb
        a[partner], b[partner] = -ca, -sb
    xq = [[a[i] if i == j else 0.0 for j in range(N_Q6)]
          for i in range(N_Q6)]
    yq = [[b[i] if i == j else 0.0 for j in range(N_Q6)]
          for i in range(N_Q6)]
    return xq, yq


def run_audit():
    points, x, y, iota, it, jq, j6, pi, x0, y0 = build()
    ident6 = eye(6)
    ident64 = eye(64)
    x2y2 = add(matmul(x, x), matmul(y, y))
    x0_2_y0_2 = add(matmul(x0, x0), matmul(y0, y0))
    sample_angles = [0.137 * (k + 1) for k in range(29)]
    xq, yq = build_full_diagonal_extension(sample_angles)

    errors = {
        "isometry_iota_star_iota": max_error(matmul(it, iota), ident6),
        "antipodal_intertwining": max_error(matmul(jq, iota),
                                              matmul(iota, j6)),
        "X_hermitian": max_error(transpose(x0), x0),
        "Y_hermitian": max_error(transpose(y0), y0),
        "X_odd": max_error(matmul(matmul(jq, x0), jq), scale(-1.0, x0)),
        "Y_odd": max_error(matmul(matmul(jq, y0), jq), scale(-1.0, y0)),
        "zero_extension_sum_is_projection": max_error(x0_2_y0_2, pi),
        "projection_idempotence": max_error(matmul(pi, pi), pi),
        "projection_rank_six": abs(rank(pi) - 6),
        "T142_unit_circle_identity": max_error(x2y2, ident6),
        "full_extension_X_hermitian": max_error(transpose(xq), xq),
        "full_extension_Y_hermitian": max_error(transpose(yq), yq),
        "full_extension_X_odd": max_error(matmul(matmul(jq, xq), jq), scale(-1.0, xq)),
        "full_extension_Y_odd": max_error(matmul(matmul(jq, yq), jq), scale(-1.0, yq)),
        "full_extension_unit_circle": max_error(
            add(matmul(xq, xq), matmul(yq, yq)), ident64),
        "extension_restricts_to_embedded_X": max_error(
            [[xq[CODES[i]][CODES[i]] if i == j else 0.0 for j in range(6)]
             for i in range(6)], x),
        "extension_restricts_to_embedded_Y": max_error(
            [[yq[CODES[i]][CODES[i]] if i == j else 0.0 for j in range(6)]
             for i in range(6)], y),
    }

    # Pull the Q6 even/odd basis from each selected antipodal pair.
    # The six embedded points are ordered as representatives then complements.
    x_block = [[x[k][k] if i == k else 0.0 for k in range(3)]
               for i in range(3)]
    y_block = [[y[k][k] if i == k else 0.0 for k in range(3)]
               for i in range(3)]

    ranks = {
        "embedded_X_even_to_odd": rank(x_block),
        "embedded_Y_even_to_odd": rank(y_block),
        "full_zero_extension_X": rank(x0),
        "full_zero_extension_Y": rank(y0),
        "orthogonal_complement_dimension": 64 - rank(pi),
    }
    parity_counts = {
        "even_codes": sum(c.bit_count() % 2 == 0 for c in CODES),
        "distinct_codes": len(set(CODES)),
        "complement_pairs": all((CODES[k] ^ 63) == CODES[k + 3]
                                for k in range(3)),
    }
    expected = {
        "embedded_X_even_to_odd": 3,
        "embedded_Y_even_to_odd": 2,
        "full_zero_extension_X": 6,
        "full_zero_extension_Y": 4,
        "orthogonal_complement_dimension": 58,
    }
    status = (
        max(errors.values()) < TOL
        and ranks == expected
        and parity_counts["even_codes"] == 6
        and parity_counts["distinct_codes"] == 6
        and parity_counts["complement_pairs"]
    )
    return {
        "codes": CODES,
        "errors": errors,
        "ranks": ranks,
        "parity_counts": parity_counts,
        "full_extension_complementary_angles": len(sample_angles),
        "full_extension_ranks": {"X": rank(xq), "Y": rank(yq)},
        "status": "PASS" if status and max(errors.values()) < TOL else "FAIL",
    }


if __name__ == "__main__":
    result = run_audit()
    for key, value in result.items():
        print(f"{key}: {value}")
    raise SystemExit(0 if result["status"] == "PASS" else 1)
