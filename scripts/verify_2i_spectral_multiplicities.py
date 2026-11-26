#!/usr/bin/env python3
"""Exact character/Molien verification for scalar harmonics on S^3 / 2I.

Requires: sympy
Run: python scripts/verify_2i_spectral_multiplicities.py

The class data are SU(2) conjugacy angles alpha = pi*p/q and class sizes.
All character evaluations are exact SymPy algebraic expressions; no floating
point trigonometry or rounding is used.
"""
from __future__ import annotations

import sympy as sp

# (p, q, class_size), where an element has eigenvalues exp(+-i*pi*p/q).
# The nine conjugacy classes of the binary icosahedral group 2I.
CLASSES = (
    (0, 1, 1),    # identity
    (1, 1, 1),    # central element -1
    (1, 2, 30),   # order 4
    (2, 3, 20),   # order 3
    (1, 3, 20),   # order 6
    (2, 5, 12),   # order 5
    (4, 5, 12),   # order 5
    (1, 5, 12),   # order 10
    (3, 5, 12),   # order 10
)
GROUP_ORDER = 120
assert sum(size for _, _, size in CLASSES) == GROUP_ORDER


def su2_character(two_j: int, p: int, q: int) -> sp.Expr:
    """Character of spin j=two_j/2 at SU(2) angle alpha=pi*p/q."""
    n = two_j + 1
    if p == 0:
        return sp.Integer(n)
    if p == q:
        return sp.Integer(n * (-1) ** two_j)
    alpha = sp.pi * sp.Rational(p, q)
    return sp.simplify(sp.sin(n * alpha) / sp.sin(alpha))


def invariant_dimension(two_j: int) -> int:
    """dim(V_{two_j/2}^{2I}), evaluated exactly by character averaging."""
    total = sum(
        size * su2_character(two_j, p, q)
        for p, q, size in CLASSES
    )
    value = sp.simplify(total / GROUP_ORDER)
    if value.is_Integer is not True:
        raise ArithmeticError(
            f"Character average is not an integer for 2j={two_j}: {value}"
        )
    return int(value)


def molien_coefficients(max_degree: int) -> list[int]:
    """Coefficients of M_2I(t)=(1+t^30)/((1-t^12)(1-t^20))."""
    t = sp.symbols("t")
    molien = (1 + t**30) / ((1 - t**12) * (1 - t**20))
    series = sp.series(molien, t, 0, max_degree + 1).removeO()
    return [int(series.coeff(t, degree)) for degree in range(max_degree + 1)]


def spectral_multiplicity(k: int, molien: list[int]) -> int:
    """Multiplicity of lambda_k=k(k+2) on S^3/2I."""
    # The central element -1 acts on V_{k/2} by (-1)^k.
    # Hence odd k have no invariant vectors.
    if k % 2:
        return 0
    n = invariant_dimension(k)  # V_{k/2}=Sym^k(C^2)
    return (k + 1) * n


def main() -> None:
    max_k = 120
    molien = molien_coefficients(max_k)

    # Compare the exact character average with the Molien coefficient
    # degree by degree. For S^3 harmonics, polynomial degree equals k.
    for k in range(max_k + 1):
        character_value = invariant_dimension(k)
        if character_value != molien[k]:
            raise AssertionError(
                f"Mismatch at k={k}: characters={character_value}, "
                f"Molien={molien[k]}"
            )

    print(f"PASS: exact character averages agree with Molien through degree {max_k}.")
    print("Nonzero invariant dimensions n_{k/2}:")
    for k in range(max_k + 1):
        if molien[k]:
            print(f"  k={k:3d}, j={k/2:5.1f}, n={molien[k]}")

    print()
    print(f"{'k':>4} {'lambda=k(k+2)':>15} {'multiplicity':>14}")
    for k in range(max_k + 1):
        d_k = spectral_multiplicity(k, molien)
        if d_k:
            print(f"{k:4d} {k * (k + 2):15d} {d_k:14d}")

    first_positive = next(
        (k for k in range(1, max_k + 1)
         if spectral_multiplicity(k, molien)),
        None,
    )
    if first_positive is None:
        raise AssertionError("No positive eigenvalue found in verification range.")
    print(
        "First positive eigenvalue:",
        f"k={first_positive}, lambda={first_positive * (first_positive + 2)},",
        f"multiplicity={spectral_multiplicity(first_positive, molien)}",
    )


if __name__ == "__main__":
    main()
