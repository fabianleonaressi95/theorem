"""Finite-depth diagnostics for TSMR-C cumulative measures.

These routines are deliberately labelled approximations. In particular, a
finite golden Bernoulli convolution is atomic and cannot prove that its limit
has a singular continuous distribution function.
"""
from __future__ import annotations

import math
from itertools import product


def golden_parameter() -> float:
    return (math.sqrt(5.0) - 1.0) / 2.0


def golden_support_radius() -> float:
    lam = golden_parameter()
    return 1.0 / (1.0 - lam)


def finite_bernoulli_atoms(lam: float, depth: int) -> list[float]:
    """Return all 2**depth equally weighted atoms of the truncated sum."""
    if not (0.0 < lam < 1.0):
        raise ValueError("lam must lie in (0, 1)")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return [
        sum(sign * lam**k for k, sign in enumerate(signs))
        for signs in product((-1.0, 1.0), repeat=depth)
    ]


def empirical_cdf(sorted_atoms: list[float], x: float) -> float:
    """Right-continuous empirical CDF for an already sorted atom list."""
    if not sorted_atoms:
        raise ValueError("at least one atom is required")
    lo, hi = 0, len(sorted_atoms)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_atoms[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo / len(sorted_atoms)


def uniform_half_cdf(x: float) -> float:
    """CDF of the symmetric Bernoulli convolution at lambda=1/2."""
    if x <= -2.0:
        return 0.0
    if x >= 2.0:
        return 1.0
    return (x + 2.0) / 4.0


def golden_identity_residual() -> float:
    lam = golden_parameter()
    return lam * lam + lam - 1.0
