"""Numerical regression helpers for TSMR-H.

The theorem file contains the analytic proofs. This module only checks
finite-precision identities and representative parameter regimes.
"""
from math import cos, sin, pi, log, sqrt


def signed_first_level_gap(lam):
    if not 0.0 < lam < 1.0:
        raise ValueError("lambda must lie in (0, 1)")
    return 2.0 * (1.0 - 2.0 * lam) / (1.0 - lam)


def binary_entropy(p):
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must lie in [0, 1]")
    if p in (0.0, 1.0):
        return 0.0
    return -p * log(p) - (1.0 - p) * log(1.0 - p)


def pentagonal_frame():
    return tuple(
        (cos(2.0 * pi * j / 5.0), sin(2.0 * pi * j / 5.0))
        for j in range(5)
    )


def pentagonal_gram():
    e = pentagonal_frame()
    return tuple(
        tuple(e[i][0] * e[j][0] + e[i][1] * e[j][1] for j in range(5))
        for i in range(5)
    )


def pentagonal_projector():
    gram = pentagonal_gram()
    return tuple(tuple(0.4 * gram[i][j] for j in range(5)) for i in range(5))


def matvec(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def projected_norm_squared(vector):
    if len(vector) != 5:
        raise ValueError("q must have five components")
    p = pentagonal_projector()
    pq = matvec(p, vector)
    return sum(x * x for x in pq)


def balanced_unit_vector():
    # u is a unit vector in the pentagonal row space; v is the normalized
    # all-ones vector, which lies in ker(E). They are orthogonal.
    e = pentagonal_frame()
    u = tuple(sqrt(2.0 / 5.0) * e[j][0] for j in range(5))
    v = (1.0 / sqrt(5.0),) * 5
    return tuple((u[j] + v[j]) / sqrt(2.0) for j in range(5))


def golden_contraction():
    return (sqrt(5.0) - 1.0) / 2.0
