"""Certified rational-function integration on the reference triangle.

All arithmetic is exact over Fraction. On each subtriangle, Bernstein
coefficients enclose numerator and denominator; positivity of the denominator
is certified before taking quotient bounds. The integral is enclosed by
(subtriangle area) times the range enclosure. This is rigorous but may be
conservative; failure to certify positivity or meet the requested width raises.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
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


@lru_cache(maxsize=131072)
def _compose_on_triangle_cached(poly_items, tri: Triangle):
    poly = dict(poly_items)
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


def _compose_on_triangle(poly: Poly, tri: Triangle):
    return _compose_on_triangle_cached(tuple(sorted(poly.items())), tri)


@lru_cache(maxsize=131072)
def _bernstein_bounds_cached(poly_items):
    poly = dict(poly_items)
    if not poly:
        return Fraction(0), Fraction(0)
    n = max(i+j for i, j in poly)
    coeffs = []
    falling = lambda x, k: (factorial(x)//factorial(x-k)) if x >= k else 0
    for k in range(n+1):
        for l in range(n-k+1):
            value = Fraction(0)
            for (i, j), c in poly.items():
                if i <= k and j <= l and i+j <= n:
                    d = factorial(n)//factorial(n-i-j)
                    value += c * Fraction(falling(k, i)*falling(l, j), d)
            coeffs.append(value)
    return min(coeffs), max(coeffs)


def _bernstein_bounds(poly):
    return _bernstein_bounds_cached(tuple(sorted(poly.items())))


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



def integrate_rational_triangle_many(
    numerators, denominator, *, absolute_tolerance=Fraction(1, 10**8),
    max_depth=12, progress_callback=None, max_triangles=512,
):
    """Enclose many rational integrals with numerator-specific subdivisions.

    Denominator composition/Bernstein bounds are shared through the exact
    composition cache, but a numerator that needs refinement cannot force
    already-certified numerators to subdivide their triangles.
    """
    tol = _f(absolute_tolerance)
    if tol <= 0 or not isinstance(max_depth, int) or max_depth < 0:
        raise ValueError("positive tolerance and nonnegative integer max_depth required")
    if not isinstance(max_triangles, int) or max_triangles < 1:
        raise ValueError("max_triangles must be a positive integer")
    ps = [{k: _f(v) for k, v in p.items()} for p in numerators]
    q = {k: _f(v) for k, v in denominator.items()}
    if not q:
        raise ZeroDivisionError("zero denominator polynomial")
    if len(q) == 1 and (0, 0) in q:
        return [integrate_rational_triangle(
            p, q, absolute_tolerance=tol, max_depth=max_depth
        ) for p in ps]
    if not ps:
        return []

    root = ((Fraction(0), Fraction(0)),
            (Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(1)))
    lower = [Fraction(0) for _ in ps]
    upper = [Fraction(0) for _ in ps]
    leaves = [0 for _ in ps]
    used = [0 for _ in ps]
    # Each work item belongs to exactly one numerator.  This is the key
    # distinction from the former shared tree: refinement is local to the
    # numerator whose Neumann remainder fails.
    stack = [(root, 0, i) for i in range(len(ps))]
    processed = [0 for _ in ps]
    split_count = [0 for _ in ps]
    pending = [1 for _ in ps]
    while stack:
        tri, depth, index = stack.pop()
        if processed[index] >= max_triangles:
            raise ArithmeticError(
                "rational Neumann integration exceeded max_triangles="
                f"{max_triangles} for numerator {index + 1}; "
                "increase the budget only after inspecting the enclosure behavior"
            )
        pending[index] -= 1
        processed[index] += 1
        used[index] = max(used[index], depth)
        if progress_callback:
            progress_callback({
                "integration_stage": "triangle_start",
                "integration_numerator_index": index + 1,
                "integration_numerator_total": len(ps),
                "integration_triangles_processed": processed[index],
                "integration_pending_triangles": pending[index],
                "integration_accepted_leaves": leaves[index],
                "integration_split_triangles": split_count[index],
                "integration_max_depth": used[index],
            })

        qq = _compose_on_triangle(q, tri)
        qlo, qhi = _bernstein_bounds(qq)
        negate = qhi < 0
        if negate:
            qq = _scale(qq, -1)
            qlo, qhi = -qhi, -qlo
        if qlo <= 0:
            if depth >= max_depth:
                raise ArithmeticError(
                    "denominator positivity not certified by numerator-specific Bernstein subdivision"
                )
            split_count[index] += 1
            pending[index] += 4
            stack.extend((child, depth+1, index) for child in _split4(tri))
            continue

        pp = _compose_on_triangle(ps[index], tri)
        if negate:
            pp = _scale(pp, -1)
        area = _area(tri)
        midpoint_q = (qlo+qhi)/2
        relative_radius = (qhi-qlo)/(qhi+qlo)
        delta_q = _add(qq, {(0, 0): -midpoint_q})
        plo, phi = _bernstein_bounds(pp)
        # The Bernstein sup norm bounds |p| even when p changes sign.
        max_abs_numerator = max(abs(plo), abs(phi))
        term_poly = pp
        series = Fraction(0)
        certified = False
        for order in range(3):
            term_ref = sum(
                (coefficient * Fraction(factorial(i)*factorial(j),
                                        factorial(i+j+2))
                 for (i, j), coefficient in term_poly.items()),
                Fraction(0),
            )
            term_integral = 2*area*term_ref
            series += ((-1)**order)*term_integral/(midpoint_q**(order+1))
            remainder = (
                area * max_abs_numerator * relative_radius**(order+1)
                /(midpoint_q*(1-relative_radius))
            )
            if remainder <= tol*area:
                certified = True
                break

            # Sharpen the geometric tail with the actual polynomial
            # p*(q-midpoint)^(order+1), rather than the product of two
            # independent sup-norm bounds. Bernstein coefficients enclose
            # this polynomial exactly, so the improved bound is rigorous.
            next_term_poly = _mul(term_poly, delta_q)
            rlo, rhi = _bernstein_bounds(next_term_poly)
            residual_sup = max(abs(rlo), abs(rhi))
            polynomial_remainder = (
                area * residual_sup
                /(midpoint_q**(order+2)*(1-relative_radius))
            )
            remainder = min(remainder, polynomial_remainder)
            if remainder <= tol*area:
                certified = True
                break
            term_poly = next_term_poly

        if not certified:
            if depth >= max_depth:
                raise ArithmeticError(
                    "rational Neumann enclosure width not reached for numerator "
                    f"{index + 1}"
                )
            split_count[index] += 1
            pending[index] += 4
            stack.extend((child, depth+1, index) for child in _split4(tri))
            continue

        lower[index] += series-remainder
        upper[index] += series+remainder
        leaves[index] += 1
        if progress_callback:
            progress_callback({
                "integration_stage": "triangle_leaf_accepted",
                "integration_numerator_index": index + 1,
                "integration_numerator_total": len(ps),
                "integration_triangles_processed": processed[index],
                "integration_pending_triangles": pending[index],
                "integration_accepted_leaves": leaves[index],
                "integration_split_triangles": split_count[index],
                "integration_max_depth": used[index],
                "integration_remainder": str(remainder),
            })
    return [
        (lower[i], upper[i], leaves[i], used[i])
        for i in range(len(ps))
    ]

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
    if len(q) == 1 and (0, 0) in q:
        constant = q[(0, 0)]
        if constant == 0:
            raise ZeroDivisionError("zero constant denominator")
        exact = sum(
            (coefficient * Fraction(factorial(i)*factorial(j),
                                    factorial(i+j+2))
             for (i, j), coefficient in p.items()),
            Fraction(0),
        ) / constant
        return exact, exact, 1, 0
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
        area = _area(tri)
        if plo < 0 < phi:
            candidates = (plo/qlo, plo/qhi, phi/qlo, phi/qhi)
            rlo, rhi = min(candidates), max(candidates)
            local_width = area*(rhi-rlo)
            if local_width > 2*tol*area and depth < max_depth:
                stack.extend((child, depth+1) for child in _split4(tri))
                continue
            if local_width > 2*tol*area:
                raise ArithmeticError("requested integral enclosure width not reached on sign-changing numerator")
            lower += area*rlo
            upper += area*rhi
            leaves += 1
            continue
        # Integrate the polynomial numerator against a rational Neumann
        # expansion of 1/q. The exact polynomial moments are summed, while
        # the geometric-series remainder is bounded rationally. This avoids
        # uniform 2-D subdivision merely to resolve a mildly varying Jacobian.
        integral_ref = sum(
            (coefficient * Fraction(factorial(i)*factorial(j),
                                    factorial(i+j+2))
             for (i, j), coefficient in pp.items()),
            Fraction(0),
        )
        integral_poly = 2*area*integral_ref
        midpoint_q = (qlo+qhi)/2
        relative_radius = (qhi-qlo)/(qhi+qlo)
        delta_q = _add(qq, {(0, 0): -midpoint_q})
        term_poly = pp
        series = Fraction(0)
        remainder = abs(integral_poly) / midpoint_q
        certified = False
        # Keep the exact polynomial expansion short: high powers inflate
        # Fraction numerators/denominators dramatically. The geometric
        # remainder remains rigorous; if three terms are insufficient, the
        # triangle is subdivided and the same bound is recomputed locally.
        for order in range(3):
            term_ref = sum(
                (coefficient * Fraction(factorial(i)*factorial(j),
                                        factorial(i+j+2))
                 for (i, j), coefficient in term_poly.items()),
                Fraction(0),
            )
            term_integral = 2*area*term_ref
            series += ((-1)**order) * term_integral / (midpoint_q**(order+1))
            remainder = (
                abs(integral_poly) * relative_radius**(order+1)
                / (midpoint_q*(1-relative_radius))
            )
            if remainder <= tol*area:
                certified = True
                break
            term_poly = _mul(term_poly, delta_q)
        if not certified:
            if depth >= max_depth:
                raise ArithmeticError("rational Neumann enclosure width not reached")
            stack.extend((child, depth+1) for child in _split4(tri))
            continue
        lower += series-remainder
        upper += series+remainder
        leaves += 1
    return lower, upper, leaves, used



def integrate_rational_triangle_bernstein_residual(
    numerator: Poly,
    denominator: Poly,
    *,
    absolute_tolerance=Fraction(1, 10**8),
    max_depth=12,
    expansion_order=2,
):
    """Enclose integral(p/q) by integrating a polynomial approximation exactly.

    On each leaf, let m be the midpoint of the positive Bernstein range of q
    and form s = p * sum_{k=0}^N (-(q-m))^k / m^(k+1).  The polynomial
    integral of s is evaluated exactly.  The remaining rational function
    (p-q*s)/q is enclosed by Bernstein bounds for its numerator and q.
    Unlike a pointwise Neumann remainder, this uses the actual residual
    polynomial and can exploit cancellation.  All operations are Fraction.

    Returns (lower, upper, leaves, max_depth_used).  The requested tolerance
    bounds the total interval width (the local test is width <= 2*tol*area).
    """
    tol = _f(absolute_tolerance)
    if tol <= 0 or not isinstance(max_depth, int) or max_depth < 0:
        raise ValueError("positive tolerance and nonnegative integer max_depth required")
    if not isinstance(expansion_order, int) or expansion_order < 0:
        raise ValueError("expansion_order must be a nonnegative integer")
    p = {k: _f(v) for k, v in numerator.items()}
    q = {k: _f(v) for k, v in denominator.items()}
    if not q:
        raise ZeroDivisionError("zero denominator polynomial")
    if len(q) == 1 and (0, 0) in q:
        return integrate_rational_triangle(
            p, q, absolute_tolerance=tol, max_depth=max_depth
        )

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
        negate = qhi < 0
        if negate:
            pp, qq = _scale(pp, -1), _scale(qq, -1)
            qlo, qhi = -qhi, -qlo
        if qlo <= 0:
            if depth >= max_depth:
                raise ArithmeticError(
                    "denominator positivity not certified by Bernstein subdivision"
                )
            stack.extend((child, depth+1) for child in _split4(tri))
            continue

        area = _area(tri)
        midpoint = (qlo + qhi) / 2
        delta = _add(qq, {(0, 0): -midpoint})
        term = pp
        polynomial_approximation = {}
        for k in range(expansion_order + 1):
            polynomial_approximation = _add(
                polynomial_approximation,
                _scale(term, Fraction((-1)**k, 1) / midpoint**(k+1)),
            )
            term = _mul(term, delta)

        # Exact integral of the polynomial approximation on this physical
        # subtriangle, using exact reference-triangle monomial moments.
        polynomial_moment = sum(
            (coefficient * Fraction(factorial(i)*factorial(j),
                                    factorial(i+j+2))
             for (i, j), coefficient in polynomial_approximation.items()),
            Fraction(0),
        )
        polynomial_integral = 2 * area * polynomial_moment

        residual_numerator = _add(
            pp, _scale(_mul(qq, polynomial_approximation), -1)
        )
        rlo, rhi = _bernstein_bounds(residual_numerator)
        quotient_candidates = (rlo/qlo, rlo/qhi, rhi/qlo, rhi/qhi)
        residual_lo = min(quotient_candidates)
        residual_hi = max(quotient_candidates)
        local_lo = polynomial_integral + area * residual_lo
        local_hi = polynomial_integral + area * residual_hi

        if local_hi - local_lo > 2 * tol * area:
            if depth >= max_depth:
                raise ArithmeticError(
                    "Bernstein residual enclosure width not reached"
                )
            stack.extend((child, depth+1) for child in _split4(tri))
            continue

        lower += local_lo
        upper += local_hi
        leaves += 1

    return lower, upper, leaves, used



def integrate_rational_triangle_bernstein_residual_many(
    numerators,
    denominator,
    *,
    absolute_tolerance=Fraction(1, 10**8),
    max_depth=12,
    expansion_order=2,
    progress_callback=None,
):
    """Apply the residual integrator to a matrix batch with one denominator.

    Each entry retains its own adaptive cover, matching the current volume
    batch semantics. The denominator polynomial is shared as input; no
    unsupported common-tree assumption is made.
    """
    results = []
    total = len(numerators)
    for index, numerator in enumerate(numerators):
        if progress_callback:
            progress_callback({
                "integration_stage": "bernstein_residual_entry_start",
                "integration_numerator_index": index + 1,
                "integration_numerator_total": total,
            })
        result = integrate_rational_triangle_bernstein_residual(
            numerator, denominator,
            absolute_tolerance=absolute_tolerance,
            max_depth=max_depth,
            expansion_order=expansion_order,
        )
        results.append(result)
        if progress_callback:
            progress_callback({
                "integration_stage": "bernstein_residual_entry_complete",
                "integration_numerator_index": index + 1,
                "integration_numerator_total": total,
                "integration_accepted_leaves": result[2],
                "integration_max_depth": result[3],
                "integration_interval_width": str(result[1]-result[0]),
            })
    return results
