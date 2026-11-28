"""Exact rational homology audit for the Q6 raw 4-skeleton vertex link.

The link is the 3-skeleton of the 5-simplex on six inward coordinate
directions. This script uses Fraction Gaussian elimination, not floating
rank thresholds.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def simplices_on_six_vertices():
    vertices = tuple(range(6))
    return {
        k: tuple(combinations(vertices, k + 1))
        for k in range(4)
    }


def boundary_matrix(k: int, simplices):
    """Integer simplicial boundary matrix C_k -> C_(k-1)."""
    if k < 1 or k > 3:
        raise ValueError("k must be 1, 2, or 3")
    rows = simplices[k - 1]
    cols = simplices[k]
    row_index = {face: i for i, face in enumerate(rows)}
    matrix = [[0 for _ in cols] for _ in rows]
    for j, simplex in enumerate(cols):
        for omitted in range(k + 1):
            face = simplex[:omitted] + simplex[omitted + 1 :]
            matrix[row_index[face]][j] = (-1) ** omitted
    return matrix


def rank_over_q(matrix):
    """Exact matrix rank over Q using Fraction row reduction."""
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    nrows, ncols = len(a), len(a[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next((r for r in range(pivot_row, nrows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(nrows):
            if r == pivot_row or not a[r][col]:
                continue
            factor = a[r][col]
            a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def audit_q6_vertex_link():
    simplices = simplices_on_six_vertices()
    ranks = {
        k: rank_over_q(boundary_matrix(k, simplices))
        for k in (1, 2, 3)
    }
    counts = {k: len(simplices[k]) for k in range(4)}
    betti = {
        0: counts[0] - ranks[1],
        1: counts[1] - ranks[1] - ranks[2],
        2: counts[2] - ranks[2] - ranks[3],
        3: counts[3] - ranks[3],
    }
    euler = sum((1 if k % 2 == 0 else -1) * counts[k] for k in range(4))
    return {
        "f_vector": tuple(counts[k] for k in range(4)),
        "boundary_ranks": ranks,
        "betti_numbers_over_q": betti,
        "euler_characteristic": euler,
        "is_s3_homology": betti == {0: 1, 1: 0, 2: 0, 3: 1},
        "is_3_ball_homology": betti == {0: 1, 1: 0, 2: 0, 3: 0},
        "status": "RAW_Q6_VERTEX_LINK_NOT_A_PL_3_SPHERE_OR_BALL",
    }


if __name__ == "__main__":
    print(audit_q6_vertex_link())
