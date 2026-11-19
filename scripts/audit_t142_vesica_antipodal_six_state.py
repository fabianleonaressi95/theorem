#!/usr/bin/env python3
"""Finite numerical audit for T142: antipodal Vesica hexagon operators."""

from __future__ import annotations

import cmath
import math


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b)))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a):
    return [list(row) for row in zip(*a)]


def identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def max_error(a, b):
    return max(abs(a[i][j] - b[i][j])
               for i in range(len(a)) for j in range(len(a[0])))


def numerical_rank(a, tol=1e-10):
    """Gaussian-elimination rank with a declared numerical tolerance."""
    m = [list(map(float, row)) for row in a]
    rows, cols = len(m), len(m[0])
    rank = 0
    for col in range(cols):
        pivot = max(range(rank, rows), key=lambda r: abs(m[r][col]),
                    default=rank)
        if rank >= rows or abs(m[pivot][col]) <= tol:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        p = m[rank][col]
        m[rank] = [x / p for x in m[rank]]
        for r in range(rows):
            if r != rank:
                q = m[r][col]
                m[r] = [m[r][c] - q * m[rank][c] for c in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def build_matrices():
    # Ordering: 1, omega, omega^2, -1, -omega, -omega^2.
    omega = cmath.exp(2j * math.pi / 3)
    points = [1 + 0j, omega, omega**2, -1 + 0j, -omega, -omega**2]
    j = [[0.0] * 6 for _ in range(6)]
    for k in range(3):
        j[k][k + 3] = 1.0
        j[k + 3][k] = 1.0
    x = [[(points[i].real if i == j else 0.0)
          for j in range(6)] for i in range(6)]
    y = [[(points[i].imag if i == j else 0.0)
          for j in range(6)] for i in range(6)]
    p_plus = scale(0.5, add(identity(6), j))
    p_minus = scale(0.5, add(identity(6), scale(-1.0, j)))
    return points, j, x, y, p_plus, p_minus


def run_audit():
    points, j, x, y, p_plus, p_minus = build_matrices()
    ident = identity(6)
    jxj = matmul(matmul(j, x), j)
    jyj = matmul(matmul(j, y), j)
    x2_y2 = add(matmul(x, x), matmul(y, y))
    x_block = matmul(matmul(p_minus, x), p_plus)
    y_block = matmul(matmul(p_minus, y), p_plus)

    # Express the off-diagonal maps in the +/- pair bases:
    # their matrices are diagonal with entries Re(z_k), Im(z_k).
    x_coeffs = [points[k].real for k in range(3)]
    y_coeffs = [points[k].imag for k in range(3)]
    x_diag = [[x_coeffs[i] if i == j else 0.0 for j in range(3)]
              for i in range(3)]
    y_diag = [[y_coeffs[i] if i == j else 0.0 for j in range(3)]
              for i in range(3)]

    errors = {
        "J^T-J": max_error(transpose(j), j),
        "J^2-I": max_error(matmul(j, j), ident),
        "JXJ+X": max_error(jxj, scale(-1.0, x)),
        "JYJ+Y": max_error(jyj, scale(-1.0, y)),
        "X^2+Y^2-I": max_error(x2_y2, ident),
        "P-X-P+": max_error(matmul(matmul(p_plus, x), p_plus),
                            [[0.0] * 6 for _ in range(6)]),
        "P-Y-P+": max_error(matmul(matmul(p_plus, y), p_plus),
                            [[0.0] * 6 for _ in range(6)]),
    }
    ranks = {
        "rank(P-X-P+)": numerical_rank(x_diag),
        "rank(P-Y-P+)": numerical_rank(y_diag),
    }
    expected_x = [1.0, -0.5, -0.5]
    expected_y = [0.0, math.sqrt(3.0) / 2.0, -math.sqrt(3.0) / 2.0]
    coefficient_error = max(
        max(abs(a - b) for a, b in zip(x_coeffs, expected_x)),
        max(abs(a - b) for a, b in zip(y_coeffs, expected_y)),
    )
    return {
        "point_count": len(points),
        "errors": errors,
        "max_identity_error": max(errors.values()),
        "coefficient_error": coefficient_error,
        "block_coefficients_X": x_coeffs,
        "block_coefficients_Y": y_coeffs,
        "block_ranks": ranks,
        "status": "PASS" if max(errors.values()) < 1e-10
        and coefficient_error < 1e-10
        and ranks == {"rank(P-X-P+)": 3, "rank(P-Y-P+)": 2}
        else "FAIL",
    }


if __name__ == "__main__":
    result = run_audit()
    for key, value in result.items():
        print(f"{key}: {value}")
    raise SystemExit(0 if result["status"] == "PASS" else 1)
