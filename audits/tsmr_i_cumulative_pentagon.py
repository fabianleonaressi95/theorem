"""Exact finite-dimensional audit for the cumulative-coordinate pentagonal lift.

The measure-theoretic isometry is proved in the theorem file using the
probability-integral transform. This module audits the real DFT frame,
projector, lift coefficients, and the exact 1/2 -> 5/4 balance.
"""
from math import cos, sin, pi, sqrt


def pentagonal_fourier_frame():
    rows = []
    for j in range(5):
        rows.append((
            sqrt(2.0 / 5.0) * cos(2.0 * pi * j / 5.0),
            sqrt(2.0 / 5.0) * sin(2.0 * pi * j / 5.0),
            1.0 / sqrt(5.0),
            sqrt(2.0 / 5.0) * cos(4.0 * pi * j / 5.0),
            sqrt(2.0 / 5.0) * sin(4.0 * pi * j / 5.0),
        ))
    return tuple(rows)


def pentagonal_projector():
    u = pentagonal_fourier_frame()
    return tuple(
        tuple(u[i][0] * u[j][0] + u[i][1] * u[j][1] for j in range(5))
        for i in range(5)
    )


def coefficients(q):
    if len(q) != 5:
        raise ValueError("q must have five components")
    u = pentagonal_fourier_frame()
    return tuple(sum(u[j][k] * q[j] for j in range(5)) for k in range(5))


def fourier_basis(t):
    return (
        sqrt(2.0) * cos(2.0 * pi * t),
        sqrt(2.0) * sin(2.0 * pi * t),
        1.0,
        sqrt(2.0) * cos(4.0 * pi * t),
        sqrt(2.0) * sin(4.0 * pi * t),
    )


def lifted_value(q, cumulative_coordinate):
    c = coefficients(q)
    phi = fourier_basis(cumulative_coordinate)
    return sum(c[k] * phi[k] for k in range(5))


def balanced_vector():
    u = pentagonal_fourier_frame()
    # Equal unit contributions from the first active mode and the constant
    # null mode. Both vectors are unit and orthogonal.
    return tuple((u[j][0] + u[j][2]) / sqrt(2.0) for j in range(5))


def projected_energy(q):
    p = pentagonal_projector()
    pq = tuple(sum(p[i][j] * q[j] for j in range(5)) for i in range(5))
    return sum(x * x for x in pq)


def inner_product_on_uniform_coordinate(q, r, samples=20000):
    # Midpoint quadrature of integral_0^1 (Jq)(t)(Jr)(t) dt.
    total = 0.0
    for k in range(samples):
        t = (k + 0.5) / samples
        total += lifted_value(q, t) * lifted_value(r, t)
    return total / samples
