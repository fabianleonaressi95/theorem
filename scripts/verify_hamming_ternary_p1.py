#!/usr/bin/env python3
"""Exact, dependency-free structural verifier for the H(2,3) P1 graph."""

from fractions import Fraction
from itertools import product


ALPHABET = (-1, 0, 1)
VERTICES = tuple(product(ALPHABET, repeat=2))


def matmul(a, b):
    n = len(a)
    m = len(b[0])
    k = len(b)
    return [
        [sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
        for i in range(n)
    ]


def matsub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def matadd(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scalar_mul(c, a):
    return [[c * x for x in row] for row in a]


def rank_over_q(matrix):
    """Gaussian elimination over Q; avoids floating-point rank decisions."""
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot_row = 0

    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [
                    x - factor * y
                    for x, y in zip(a[r], a[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def main():
    n = len(VERTICES)
    index = {v: i for i, v in enumerate(VERTICES)}
    adjacency = [[0] * n for _ in range(n)]

    for i, u in enumerate(VERTICES):
        for j in range(i + 1, n):
            v = VERTICES[j]
            if sum(x != y for x, y in zip(u, v)) == 1:
                adjacency[i][j] = adjacency[j][i] = 1

    degrees = [sum(row) for row in adjacency]
    laplacian = [
        [
            (degrees[i] if i == j else 0) - adjacency[i][j]
            for j in range(n)
        ]
        for i in range(n)
    ]

    assert n == 9, f"expected 9 vertices, got {n}"
    assert sum(degrees) // 2 == 18, "expected 18 undirected edges"
    assert degrees == [4] * 9, f"unexpected degree sequence: {degrees}"
    assert all(
        laplacian[i][j] == laplacian[j][i]
        for i in range(n) for j in range(n)
    ), "Laplacian is not symmetric"
    assert all(sum(row) == 0 for row in laplacian), "nonzero Laplacian row sum"

    l2 = matmul(laplacian, laplacian)
    l3 = matmul(l2, laplacian)
    polynomial = matadd(
        matsub(l3, scalar_mul(9, l2)),
        scalar_mul(18, laplacian),
    )
    assert all(x == 0 for row in polynomial for x in row), (
        "L(L-3I)(L-6I) is not the zero matrix"
    )

    trace_l = sum(laplacian[i][i] for i in range(n))
    trace_l2 = sum(l2[i][i] for i in range(n))
    rank_l = rank_over_q(laplacian)

    assert rank_l == 8, f"expected Laplacian rank 8, got {rank_l}"
    assert trace_l == 36, f"expected trace(L)=36, got {trace_l}"
    assert trace_l2 == 180, f"expected trace(L^2)=180, got {trace_l2}"

    # The polynomial identity restricts eigenvalues to {0, 3, 6}.
    # Rank 8, trace 36 and trace(L^2)=180 then force multiplicities 1,4,4.
    print("PASS: H(2,3) has 9 vertices, 18 edges and degree 4.")
    print("PASS: exact Laplacian identity L(L-3I)(L-6I)=0.")
    print("PASS: rank(L)=8, trace(L)=36, trace(L^2)=180.")
    print("CERTIFIED SPECTRUM: 0^1, 3^4, 6^4.")
    print("NOTE: this verifies the graph model, not a physical circuit.")


if __name__ == "__main__":
    main()
