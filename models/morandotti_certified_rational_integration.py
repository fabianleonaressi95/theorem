"""Certified rational-function integration on the reference triangle.

All arithmetic is exact over Fraction. On each subtriangle, Bernstein
coefficients enclose numerator and denominator; positivity of the denominator
is certified before taking quotient bounds. The integral is enclosed by
(subtriangle area) times the range enclosure. This is rigorous but may be
conservative; failure to certify positivity or meet the requested width raises.
"""
from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Mapping

Poly = Mapping[tuple[int, int], Fraction]
Point = tuple[Fraction, Fraction]
Triangle = tuple[Point, Point, Point]


def _f(x):
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x)
    raise TypeError("certified integration accepts only int/Fraction data")


def _clean(p):
    return {k: v for k, v in p.items() if v}


def _add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
    return _clean(out)


def _scale(p, c):
    return _clean({k: v*c for k, v in p.items()})


def _mul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i+k, j+l)
            out[key] = out.get(key, Fraction(0)) + x*y
    return _clean(out)


def _pow(p, n):
    out = {(0, 0): Fraction(1)}
    for _ in range(n):
        out = _mul(out, p)
    return out


def _compose_on_triangle(poly: Poly, tri: Triangle):
    a, b, c = tri
    u = {(1, 0): Fraction(1)}
    v = {(0, 1): Fraction(1)}
    xpoly = _add({(0, 0): a[0]}, _add(
        _scale(u, b[0]-a[0]), _scale(v, c[0]-a[0])))
    ypoly = _add({(0, 0): a[1]}, _add(
        _scale(u, b[1]-a[1]), _scale(v, c[1]-a[1])))
    out = {}
    for (i, j), coeff in poly.items():
        coeff = _f(coeff)
        out = _add(out, _scale(_mul(_pow(xpoly, i), _pow(ypoly, j)), coeff))
    return out


def _bernstein_bounds(poly):
    """Return min/max degree-n simplex Bernstein coefficients."""
    if not poly:
        return Fraction(0), Fraction(0)
    n = max(i+j for i, j in poly)
    coeffs = []
    falling = lambda x, k: (factorial(x)//factorial(x-k)) if x >= k else 0
    den = factorial(n)//factorial(n-(i+j)) if n >= i+j else 1
    for k in range(n+1):
        for l in range(n-k+1):
            value = Fraction(0)
            for (i, j), c in poly.items():
                if i <= k and j <= l and i+j <= n:
                    d = factorial(n)//factorial(n-i-j)
                    value += c * Fraction(falling(k, i)*falling(l, j), d)
            coeffs.append(value)
    return min(coeffs), max(coeffs)


def _split4(t: Triangle):
    a, b, c = t
    ab = ((a[0]+b[0])/2, (a[1]+b[1])/2)
    bc = ((b[0]+c[0])/2, (b[1]+c[1])/2)
    ca = ((c[0]+a[0])/2, (c[1]+a[1])/2)
    return ((a, ab, ca), (ab, b, bc), (ca, bc, c), (ab, bc, ca))


def _area(t):
    a, b, c = t
    return abs((b[0]-a[0])*(c[1]-a[1]) -
               (b[1]-a[1])*(c[0]-a[0])) / 2


def integrate_rational_triangle(
    numerator: Poly,
    denominator: Poly,
    *,
    absolute_tolerance=Fraction(1, 10**8),
    max_depth=12,
):
    """Enclose integral_K numerator/denominator using exact rational bounds.

    Returns (lower, upper, leaves, max_depth_used). The reference triangle is
    {(x,y): x>=0,y>=0,x+y<=1}. No floating-point arithmetic is used.
    """
    tol = _f(absolute_tolerance)
    if tol <= 0 or not isinstance(max_depth, int) or max_depth < 0:
        raise ValueError("positive tolerance and nonnegative integer max_depth required")
    p = {(k): _f(v) for k, v in numerator.items()}
    q = {(k): _f(v) for k, v in denominator.items()}
    if not q:
        raise ZeroDivisionError("zero denominator polynomial")
    root = ((Fraction(0), Fraction(0)),
            (Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(1)))
    stack = [(root, 0)]
    lower = upper = Fraction(0)
    leaves = 0
    used = 0
    while stack:
        tri, depth = stack.pop()
        used = max(used, depth)
        pp = _compose_on_triangle(p, tri)
        qq = _compose_on_triangle(q, tri)
        qlo, qhi = _bernstein_bounds(qq)
        if qhi < 0:
            pp, qq = _scale(pp, -1), _scale(qq, -1)
            qlo, qhi = -qhi, -qlo
        if qlo <= 0:
            if depth >= max_depth:
                raise ArithmeticError("denominator positivity not certified by Bernstein subdivision")
            stack.extend((child, depth+1) for child in _split4(tri))
            continue
        plo, phi = _bernstein_bounds(pp)
        candidates = (plo/qlo, plo/qhi, phi/qlo, phi/qhi)
        rlo, rhi = min(candidates), max(candidates)
        area = _area(tri)
        local_width = area * (rhi-rlo)
        if local_width > tol and depth < max_depth:
            stack.extend((child, depth+1) for child in _split4(tri))
            continue
        if local_width > tol:
            raise ArithmeticError("requested integral enclosure width not reached")
        lower += area*rlo
        upper += area*rhi
        leaves += 1
    return lower, upper, leaves, used
