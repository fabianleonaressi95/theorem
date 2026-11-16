#!/usr/bin/env python3
"""Exact audit of the real four-dimensional Molien series of the binary icosahedral group.

Uses only the Python standard library for the group construction, closure test,
4x4 left-multiplication matrices, determinant polynomials, and coefficients.
All arithmetic is exact in Q(sqrt(5)).  If SymPy is installed, the optional
symbolic check also simplifies the complete rational Molien sum.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

Q5 = tuple[Fraction, Fraction]  # a + b*sqrt(5)
ZERO: Q5 = (Fraction(0), Fraction(0))
ONE: Q5 = (Fraction(1), Fraction(0))


def qadd(x: Q5, y: Q5) -> Q5:
    return (x[0] + y[0], x[1] + y[1])


def qneg(x: Q5) -> Q5:
    return (-x[0], -x[1])


def qsub(x: Q5, y: Q5) -> Q5:
    return qadd(x, qneg(y))


def qmul(x: Q5, y: Q5) -> Q5:
    return (x[0] * y[0] + 5 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def qscale(x: Q5, s: Fraction | int) -> Q5:
    s = Fraction(s)
    return (x[0] * s, x[1] * s)


def permutation_sign(p: tuple[int, ...]) -> int:
    inversions = sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i + 1, len(p)))
    return -1 if inversions % 2 else 1


def quaternion_product(p: tuple[Q5, ...],
                       q: tuple[Q5, ...]) -> tuple[Q5, ...]:
    a, b, c, d = p
    e, f, g, h = q
    return (
        qsub(qsub(qsub(qmul(a, e), qmul(b, f)), qmul(c, g)), qmul(d, h)),
        qadd(qadd(qsub(qmul(a, f), qmul(d, g)), qmul(b, e)), qmul(c, h)),
        qadd(qsub(qadd(qmul(a, g), qmul(c, e)), qmul(b, h)), qmul(d, f)),
        qadd(qsub(qadd(qmul(a, h), qmul(b, g)), qmul(c, f)), qmul(d, e)),
    )


def build_2i() -> list[tuple[Q5, ...]]:
    """The 120 standard 600-cell vertices, with signs on every nonzero entry."""
    phi = (Fraction(1, 2), Fraction(1, 2))
    phi_inv = (Fraction(-1, 2), Fraction(1, 2))
    base = (ZERO, ONE, phi_inv, phi)
    elements: set[tuple[Q5, ...]] = set()

    # Eight coordinate units.
    for i in range(4):
        for sign in (1, -1):
            v = [ZERO] * 4
            v[i] = qscale(ONE, sign)
            elements.add(tuple(v))

    # Sixteen half-coordinate vertices.
    for signs in product((1, -1), repeat=4):
        elements.add(tuple(qscale(ONE, Fraction(s, 2)) for s in signs))

    # Ninety-six vertices: 12 even coordinate permutations and 8 sign choices
    # on the three nonzero coordinates, wherever those coordinates occur.
    for p in permutations(range(4)):
        if permutation_sign(p) != 1:
            continue
        values = [base[i] for i in p]
        nonzero = [i for i, value in enumerate(values) if value != ZERO]
        for signs in product((1, -1), repeat=3):
            v = list(values)
            for index, sign in zip(nonzero, signs):
                v[index] = qscale(v[index], Fraction(sign, 2))
            elements.add(tuple(v))

    return sorted(elements)


def quaternion_norm_squared(q: tuple[Q5, ...]) -> Q5:
    total = ZERO
    for x in q:
        total = qadd(total, qmul(x, x))
    return total


def left_matrix(q: tuple[Q5, ...]) -> tuple[tuple[Q5, ...], ...]:
    """Matrix of x -> q*x in the ordered real basis (1,i,j,k)."""
    a, b, c, d = q
    return (
        (a, qneg(b), qneg(c), qneg(d)),
        (b, a, qneg(d), c),
        (c, d, a, qneg(b)),
        (d, qneg(c), b, a),
    )


# Polynomials in t with Q(sqrt(5)) coefficients, low degree first.
Poly = tuple[Q5, ...]


def poly_trim(p: list[Q5] | tuple[Q5, ...]) -> Poly:
    p = list(p)
    while len(p) > 1 and p[-1] == ZERO:
        p.pop()
    return tuple(p)


def poly_add(p: Poly, q: Poly) -> Poly:
    n = max(len(p), len(q))
    return poly_trim([
        qadd(p[i] if i < len(p) else ZERO,
             q[i] if i < len(q) else ZERO)
        for i in range(n)
    ])


def poly_neg(p: Poly) -> Poly:
    return tuple(qneg(x) for x in p)


def poly_mul(p: Poly, q: Poly) -> Poly:
    out = [ZERO] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = qadd(out[i + j], qmul(x, y))
    return poly_trim(out)


def determinant_polynomial(matrix: tuple[tuple[Q5, ...], ...]) -> Poly:
    """Exact det(I - t*matrix), by the 24-term Leibniz formula."""
    entries = []
    for i in range(4):
        row = []
        for j in range(4):
            constant = ONE if i == j else ZERO
            row.append((constant, qneg(matrix[i][j])))
        entries.append(row)

    determinant: Poly = (ZERO,)
    for p in permutations(range(4)):
        term: Poly = (ONE,)
        for i, j in enumerate(p):
            term = poly_mul(term, entries[i][j])
        if permutation_sign(p) < 0:
            term = poly_neg(term)
        determinant = poly_add(determinant, term)
    return poly_trim(determinant)


def reciprocal_series(poly: Poly, degree_count: int) -> list[Q5]:
    """Coefficients of 1/poly(t), assuming poly[0] = 1."""
    if poly[0] != ONE:
        raise ValueError("Molien denominator must have constant term one")
    coeffs = [ONE]
    for n in range(1, degree_count):
        total = ZERO
        for k in range(1, min(n, len(poly) - 1) + 1):
            total = qadd(total, qmul(poly[k], coeffs[n - k]))
        coeffs.append(qneg(total))
    return coeffs


def klein_coefficient(n: int) -> int:
    """c_n = [t^n](1+t^30)/((1-t^12)(1-t^20))."""
    return sum(
        1
        for epsilon in (0, 1)
        for p in range(n // 12 + 1)
        for q in range(n // 20 + 1)
        if 12 * p + 20 * q + 30 * epsilon == n
    )


def expected_real_molien_coefficient(n: int) -> int:
    """Coefficient of (sum_l (l+1)c_l t^l)/(1-t^2)."""
    return sum(
        (n - 2 * j + 1) * klein_coefficient(n - 2 * j)
        for j in range(n // 2 + 1)
    )


def audit(degree: int = 60) -> dict:
    group = build_2i()
    group_set = set(group)
    if len(group) != 120:
        raise AssertionError(f"Expected 120 distinct elements, got {len(group)}")
    if any(quaternion_norm_squared(q) != ONE for q in group):
        raise AssertionError("A listed quaternion is not unit")

    identity = (ONE, ZERO, ZERO, ZERO)
    if identity not in group_set:
        raise AssertionError("Identity is missing")

    # Exact closure: 120^2 products in Q(sqrt(5)).
    for p in group:
        for q in group:
            if quaternion_product(p, q) not in group_set:
                raise AssertionError("The 120-element set is not multiplicatively closed")
        inverse = (p[0], qneg(p[1]), qneg(p[2]), qneg(p[3]))
        if inverse not in group_set:
            raise AssertionError("Quaternionic inverse is missing")

    molien = [(ZERO) for _ in range(degree + 1)]
    determinant_polynomials = []
    for q in group:
        matrix = left_matrix(q)
        det_poly = determinant_polynomial(matrix)
        a = q[0]
        expected_det = poly_mul(
            (ONE, qscale(a, -2), ONE),
            (ONE, qscale(a, -2), ONE),
        )
        if det_poly != expected_det:
            raise AssertionError("det(I - t L_q) identity failed")
        determinant_polynomials.append(det_poly)
        reciprocal = reciprocal_series(det_poly, degree + 1)
        for n, coefficient in enumerate(reciprocal):
            molien[n] = qadd(molien[n], qscale(coefficient, Fraction(1, 120)))

    coefficients = []
    for n, coefficient in enumerate(molien):
        if coefficient[1] != 0:
            raise AssertionError(f"Non-rational Molien coefficient at degree {n}")
        if coefficient[0].denominator != 1:
            raise AssertionError(f"Non-integral Molien coefficient at degree {n}")
        value = coefficient[0].numerator
        if value != expected_real_molien_coefficient(n):
            raise AssertionError(
                f"Mismatch at degree {n}: direct={value}, "
                f"Fischer/Klein={expected_real_molien_coefficient(n)}"
            )
        coefficients.append(value)

    return {
        "group_order": len(group),
        "closure_products_checked": len(group) ** 2,
        "unit_norms_checked": len(group),
        "left_matrices_checked": len(group),
        "determinants_checked": len(group),
        "degrees_checked": degree + 1,
        "coefficients": coefficients,
        "scalar_part_multiplicities": scalar_part_multiplicities(group),
    }


def scalar_part_multiplicities(group: list[tuple[Q5, ...]]) -> dict[Q5, int]:
    counts: dict[Q5, int] = {}
    for q in group:
        counts[q[0]] = counts.get(q[0], 0) + 1
    return counts


def symbolic_rational_check() -> str:
    """Optional exact simplification of the complete finite Molien sum (SymPy)."""
    import sympy as sp

    t = sp.symbols("t")
    sqrt5 = sp.sqrt(5)

    def to_sympy(x: Q5):
        return sp.Rational(x[0].numerator, x[0].denominator) + (
            sp.Rational(x[1].numerator, x[1].denominator) * sqrt5
        )

    group = build_2i()
    counts = scalar_part_multiplicities(group)
    molien = sum(
        sp.Rational(count, 120) / (1 - 2 * to_sympy(a) * t + t**2) ** 2
        for a, count in counts.items()
    )
    klein = (1 + t**30) / ((1 - t**12) * (1 - t**20))
    harmonic = sp.cancel(klein + t * sp.diff(klein, t))
    expected = sp.cancel(harmonic / (1 - t**2))
    difference = sp.cancel(molien - expected)
    if difference != 0:
        raise AssertionError(f"Exact rational Molien identity failed: {difference}")
    return str(sp.factor(molien))


def main() -> None:
    result = audit(240)
    print("2I exact quaternionic real-Molien audit: PASS")
    for key in (
        "group_order", "closure_products_checked", "unit_norms_checked",
        "left_matrices_checked", "determinants_checked", "degrees_checked",
    ):
        print(f"{key}: {result[key]}")
    print("scalar_part_multiplicities:")
    for scalar, count in sorted(result["scalar_part_multiplicities"].items()):
        print(f"  {scalar}: {count}")
    print("Molien coefficients (degrees 0..240):")
    print(result["coefficients"])
    try:
        print("Exact simplified rational Molien function:")
        print(symbolic_rational_check())
        print("SymPy rational identity: PASS")
    except ImportError:
        print("SymPy not installed: skipped optional full rational simplification")


if __name__ == "__main__":
    main()
