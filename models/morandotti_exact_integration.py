"""Exact rational integration primitives for polynomial reference-cell forms.

This module deliberately handles only polynomial integrands with rational
coefficients on the reference triangle/segment. Curved P3 physical Hessian
forms are generally rational (and curved-edge metric factors may be algebraic),
so callers must not pass sampled or floating-point quadrature data here and
claim an exact curved-cell certificate.
"""
from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Iterable, Mapping

Rational = Fraction
Polynomial = Mapping[tuple[int, int], Rational]


def _fraction(value) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    raise TypeError("exact integration accepts only int or Fraction coefficients")


def integrate_reference_triangle(poly: Polynomial) -> Fraction:
    """Integrate sum(c[i,j] x**i y**j) over x>=0, y>=0, x+y<=1.

    Uses the exact identity integral(x**i y**j) = i! j!/(i+j+2)!.
    """
    total = Fraction(0)
    for powers, coefficient in poly.items():
        if (not isinstance(powers, tuple) or len(powers) != 2
                or any(not isinstance(k, int) or k < 0 for k in powers)):
            raise ValueError(f"invalid monomial multi-index: {powers!r}")
        i, j = powers
        c = _fraction(coefficient)
        total += c * Fraction(factorial(i) * factorial(j),
                              factorial(i + j + 2))
    return total


def integrate_reference_segment(poly: Mapping[int, Rational]) -> Fraction:
    """Integrate sum(c[k] t**k) exactly over the unit segment [0,1]."""
    total = Fraction(0)
    for degree, coefficient in poly.items():
        if not isinstance(degree, int) or degree < 0:
            raise ValueError(f"invalid segment monomial degree: {degree!r}")
        total += _fraction(coefficient) * Fraction(1, degree + 1)
    return total


def _as_symmetric_fraction_matrix(matrix: Iterable[Iterable[object]]) -> list[list[Fraction]]:
    rows = [list(row) for row in matrix]
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise ValueError("matrix must be square")
    result = [[_fraction(value) for value in row] for row in rows]
    for i in range(n):
        for j in range(i):
            if result[i][j] != result[j][i]:
                raise ValueError("matrix must be exactly symmetric")
    return result


def certify_rational_psd(matrix: Iterable[Iterable[object]]) -> tuple[bool, tuple[Fraction, ...]]:
    """Decide positive semidefiniteness of a rational symmetric matrix exactly.

    Symmetric Schur-complement elimination uses a positive diagonal pivot.
    If no positive diagonal remains, PSD requires the remaining block to be
    identically zero; any nonzero off-diagonal entry would give a negative
    2x2 principal minor. Returns exact pivots for the audit record.
    """
    a = _as_symmetric_fraction_matrix(matrix)
    pivots: list[Fraction] = []
    while a:
        n = len(a)
        if any(a[i][i] < 0 for i in range(n)):
            return False, tuple(pivots)
        pivot_index = next((i for i in range(n) if a[i][i] > 0), None)
        if pivot_index is None:
            if any(a[i][j] != 0 for i in range(n) for j in range(i + 1, n)):
                return False, tuple(pivots)
            return True, tuple(pivots)
        if pivot_index:
            a[0], a[pivot_index] = a[pivot_index], a[0]
            for row in a:
                row[0], row[pivot_index] = row[pivot_index], row[0]
        pivot = a[0][0]
        pivots.append(pivot)
        if n == 1:
            return True, tuple(pivots)
        a = [
            [a[i][j] - a[i][0] * a[0][j] / pivot
             for j in range(1, n)]
            for i in range(1, n)
        ]
    return True, tuple(pivots)


def certify_trace_upper_bound(
    h_form: Iterable[Iterable[object]],
    d_form: Iterable[Iterable[object]],
    bound: object,
) -> tuple[bool, tuple[Fraction, ...]]:
    """Certify H <= bound*D by the exact rational PSD test on bound*D-H.

    Matrices must already represent the exact forms on the same quotient
    basis (with the common kernel removed). This routine does not assemble
    finite-element forms or certify that a chosen quotient basis is correct.
    """
    h = _as_symmetric_fraction_matrix(h_form)
    d = _as_symmetric_fraction_matrix(d_form)
    if len(h) != len(d):
        raise ValueError("H and D must have the same dimensions")
    c = _fraction(bound)
    difference = [
        [c * d[i][j] - h[i][j] for j in range(len(h))]
        for i in range(len(h))
    ]
    return certify_rational_psd(difference)
