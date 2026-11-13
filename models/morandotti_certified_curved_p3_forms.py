"""Exact-rational local C0-IPDG forms for curved triangular P3 cells.

The volume Hessian form is rational and enclosed by Bernstein integration.
The facet normal-normal Hessian form is algebraic: its arclength factor
contains |F'|. It is enclosed with rational Bernstein bounds for
p/(q*sqrt(s)**3), never by floating-point quadrature.

This module deliberately exposes local certified blocks first. Global
interval assembly and quotient PSD propagation consume these blocks.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial
from typing import Mapping, Sequence

from models.morandotti_exact_geometry import (
    _add, _derivative, _mul, _p3_lagrange_basis, _scale,
)
from models.morandotti_certified_rational_integration import (
    integrate_rational_triangle,
)

BPoly = Mapping[tuple[int, int], F]
SPoly = Mapping[int, F]
Point = tuple[F, F]
Triangle = tuple[Point, Point, Point]
Interval = tuple[F, F]

_REF_VERTICES = ((F(0), F(0)), (F(1), F(0)), (F(0), F(1)))
_VERTEX_MULTI = ((3, 0, 0), (0, 3, 0), (0, 0, 3))


def _as_fraction(x):
    if isinstance(x, F):
        return x
    if isinstance(x, int):
        return F(x)
    if isinstance(x, float):
        return F.from_float(x)
    raise TypeError("geometry and scale inputs must be exact rationals or binary64 floats")


def _clean(p):
    return {k: v for k, v in p.items() if v}


def _add1(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return _clean(out)


def _mul1(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i+j] = out.get(i+j, F(0)) + x*y
    return _clean(out)


def _scale1(a, c):
    return _clean({k: v*c for k, v in a.items()})


def _pow1(a, n):
    out = {0: F(1)}
    for _ in range(n):
        out = _mul1(out, a)
    return out


def _compose_line(p: BPoly, a: Point, b: Point) -> dict[int, F]:
    """Substitute (x,y)=a+t(b-a) into a bivariate polynomial."""
    x = {0: a[0], 1: b[0]-a[0]}
    y = {0: a[1], 1: b[1]-a[1]}
    out = {}
    for (i, j), c in p.items():
        term = _mul1(_pow1(x, i), _pow1(y, j))
        out = _add1(out, _scale1(term, c))
    return out


def _bernstein_bounds_1d(p: SPoly):
    if not p:
        return F(0), F(0)
    n = max(p)
    coeffs = []
    for k in range(n+1):
        value = F(0)
        for i, c in p.items():
            if i <= k:
                falling_k = factorial(k)//factorial(k-i)
                falling_n = factorial(n)//factorial(n-i)
                value += c * F(falling_k, falling_n)
        coeffs.append(value)
    return min(coeffs), max(coeffs)


def _restrict_half(p: SPoly, left: bool):
    # Exact affine substitutions t=s/2 and t=(1+s)/2.
    a = F(0) if left else F(1, 2)
    b = F(1, 2)
    out = {}
    for degree, c in p.items():
        term = {0: F(1)}
        linear = {0: a, 1: b}
        for _ in range(degree):
            term = _mul1(term, linear)
        out = _add1(out, _scale1(term, c))
    return out


def integrate_rational_sqrt_segment(
    numerator: SPoly,
    denominator: SPoly,
    radicand: SPoly,
    *,
    absolute_tolerance=F(1, 10**8),
    max_depth=24,
):
    """Enclose integral_0^1 p(t)/(q(t)*sqrt(s(t))^3) dt exactly.

    Positivity of q and s is certified on every leaf by univariate
    Bernstein coefficients. The returned interval is rational. Failure
    to prove positivity or meet the requested width raises ArithmeticError.
    """
    tol = _as_fraction(absolute_tolerance)
    if tol <= 0 or not isinstance(max_depth, int) or max_depth < 0:
        raise ValueError("positive tolerance and nonnegative max_depth required")
    p = {int(k): _as_fraction(v) for k, v in numerator.items() if v}
    q = {int(k): _as_fraction(v) for k, v in denominator.items() if v}
    s = {int(k): _as_fraction(v) for k, v in radicand.items() if v}
    if not q or not s:
        raise ZeroDivisionError("denominator and square-root radicand must be nonzero")
    stack = [(p, q, s, F(1), 0)]
    lower = upper = F(0)
    leaves = 0
    used = 0
    while stack:
        pp, qq, ss, length, depth = stack.pop()
        used = max(used, depth)
        qlo, qhi = _bernstein_bounds_1d(qq)
        slo, shi = _bernstein_bounds_1d(ss)
        if qlo <= 0 or slo <= 0:
            if depth >= max_depth:
                raise ArithmeticError("facet denominator/radicand positivity not certified")
            stack.extend((
                (_restrict_half(pp, True), _restrict_half(qq, True),
                 _restrict_half(ss, True), length/2, depth+1),
                (_restrict_half(pp, False), _restrict_half(qq, False),
                 _restrict_half(ss, False), length/2, depth+1),
            ))
            continue
        plo, phi = _bernstein_bounds_1d(pp)
        quotients = (plo/qlo, plo/qhi, phi/qlo, phi/qhi)
        rlo, rhi = min(quotients), max(quotients)
        sqrt_lo = _sqrt_lower(slo)
        sqrt_hi = _sqrt_upper(shi)
        # Reciprocal of s^(3/2) is positive and decreasing in s.
        factors = (F(1)/(sqrt_hi**3), F(1)/(sqrt_lo**3))
        vals = (rlo*factors[0], rlo*factors[1],
                rhi*factors[0], rhi*factors[1])
        flo, fhi = min(vals), max(vals)
        if length*(fhi-flo) > 2*tol*length:
            if depth >= max_depth:
                raise ArithmeticError("facet integral enclosure width not reached")
            stack.extend((
                (_restrict_half(pp, True), _restrict_half(qq, True),
                 _restrict_half(ss, True), length/2, depth+1),
                (_restrict_half(pp, False), _restrict_half(qq, False),
                 _restrict_half(ss, False), length/2, depth+1),
            ))
            continue
        lower += length*flo
        upper += length*fhi
        leaves += 1
    return lower, upper, leaves, used


def _sqrt_upper(x: F, digits=40) -> F:
    from math import isqrt
    if x < 0:
        raise ValueError("negative radicand")
    if x == 0:
        return F(0)
    scale = 10**digits
    n = isqrt((x.numerator*scale*scale)//x.denominator)
    if n*n*x.denominator < x.numerator*scale*scale:
        n += 1
    return F(n, scale)


def _sqrt_lower(x: F, digits=40) -> F:
    from math import isqrt
    if x < 0:
        raise ValueError("negative radicand")
    scale = 10**digits
    return F(isqrt((x.numerator*scale*scale)//x.denominator), scale)


def _reconstruct_map(node_coordinates, interpolation_points):
    if len(node_coordinates) != 10 or len(interpolation_points) != 10:
        raise ValueError("P3 triangle requires exactly ten geometry nodes")
    alpha_to_index = {}
    for index, point in enumerate(interpolation_points):
        i, j = round(3*float(point[0])), round(3*float(point[1]))
        alpha = (3-i-j, i, j)
        if min(alpha) < 0 or alpha in alpha_to_index:
            raise ValueError("invalid equispaced P3 interpolation lattice")
        alpha_to_index[alpha] = index
    expected = {(3-i-j, i, j) for i in range(4) for j in range(4-i)}
    if set(alpha_to_index) != expected:
        raise ValueError("interpolation points are not the equispaced P3 lattice")
    coords = [[_as_fraction(x) for x in node_coordinates[k][:2]]
              for k in range(10)]
    maps = []
    for component in range(2):
        poly = {}
        for alpha, index in alpha_to_index.items():
            poly = _add(poly, _scale(_p3_lagrange_basis(alpha),
                                     coords[index][component]))
        maps.append(poly)
    basis = [None]*10
    for alpha, index in alpha_to_index.items():
        basis[index] = _p3_lagrange_basis(alpha)
    return maps, basis


def _geometry_data(node_coordinates, interpolation_points):
    maps, basis = _reconstruct_map(node_coordinates, interpolation_points)
    xmap, ymap = maps
    j = ((_derivative(xmap, 0), _derivative(xmap, 1)),
         (_derivative(ymap, 0), _derivative(ymap, 1)))
    det = _add(_mul(j[0][0], j[1][1]),
               _scale(_mul(j[0][1], j[1][0]), F(-1)))
    adj = ((j[1][1], _scale(j[0][1], F(-1))),
           (_scale(j[1][0], F(-1)), j[0][0]))
    return maps, basis, j, adj, det


def _physical_hessian_numerators(basis_poly, maps, adj, det):
    """Return P_ij with D_x^2(phi)_ij = P_ij/det(J)^3."""
    second_map = [[[
        _derivative(_derivative(maps[r], a), b)
        for b in range(2)] for a in range(2)] for r in range(2)]
    grad = [_derivative(basis_poly, a) for a in range(2)]
    hess = [[_derivative(_derivative(basis_poly, a), b)
             for b in range(2)] for a in range(2)]
    corrected = [[_scale(hess[a][b], det) for b in range(2)]
                 for a in range(2)]
    for a in range(2):
        for b in range(2):
            for r in range(2):
                for s in range(2):
                    term = _mul(_mul(grad[r], adj[r][s]),
                                second_map[s][a][b])
                    corrected[a][b] = _add(
                        corrected[a][b], _scale(term, F(-1)))
    out = [[{} for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            value = {}
            for a in range(2):
                for b in range(2):
                    value = _add(value, _mul(
                        _mul(adj[a][i], adj[b][j]), corrected[a][b]))
            out[i][j] = value
    # Enforce exact symmetry, guarding only algebraic index symmetry.
    for i in range(2):
        for j in range(i):
            if out[i][j] != out[j][i]:
                raise ArithmeticError("physical Hessian numerator lost symmetry")
    return out


def _det_power(det, exponent):
    out = {(0, 0): F(1)}
    for _ in range(exponent):
        out = _mul(out, det)
    return out


def assemble_cell_volume_interval(
    node_coordinates,
    interpolation_points,
    *,
    absolute_tolerance=F(1, 10**9),
    max_depth=12,
):
    """Certified 10x10 local D_K matrix for integral_K D²phi_i:D²phi_j.

    Geometry coordinates are interpreted as exact binary64 dyadic rationals.
    Every returned matrix entry is a rigorous rational interval.
    """
    maps, basis, jac, adj, det = _geometry_data(node_coordinates, interpolation_points)
    det5 = _det_power(det, 5)
    hessians = [_physical_hessian_numerators(phi, maps, adj, det)
                for phi in basis]
    result = [[None for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(i, 10):
            numerator = {}
            for a in range(2):
                for b in range(2):
                    numerator = _add(numerator, _mul(
                        hessians[i][a][b], hessians[j][a][b]))
            lo, hi, leaves, depth = integrate_rational_triangle(
                numerator, det5, absolute_tolerance=absolute_tolerance,
                max_depth=max_depth,
            )
            result[i][j] = result[j][i] = (lo, hi)
    return {
        "matrix_interval": result,
        "determinant_polynomial": det,
        "basis_count": 10,
        "integration": "exact-rational Bernstein enclosure of rational physical Hessian products",
    }


def _edge_polynomial_data(maps, det, hessian, edge_vertices):
    a, b = (_REF_VERTICES[k] for k in edge_vertices)
    tangent = []
    direction = (b[0]-a[0], b[1]-a[1])
    for component in range(2):
        deriv = _add(
            _scale(_derivative(maps[component], 0), direction[0]),
            _scale(_derivative(maps[component], 1), direction[1]),
        )
        tangent.append(_compose_line(deriv, a, b))
    tx, ty = tangent
    radicand = _add1(_mul1(tx, tx), _mul1(ty, ty))
    normal_numerator = (ty, _scale1(tx, F(-1)))
    det_line = _compose_line(det, a, b)
    q_numerators = []
    for P in hessian:
        value = {}
        for r in range(2):
            for s in range(2):
                entry = _compose_line(P[r][s], a, b)
                value = _add1(value, _mul1(
                    _mul1(normal_numerator[r], normal_numerator[s]), entry))
        q_numerators.append(value)
    return q_numerators, _pow1(det_line, 3), radicand


def assemble_boundary_edge_interval(
    node_coordinates,
    interpolation_points,
    edge_vertices: tuple[int, int],
    h_weight,
    *,
    absolute_tolerance=F(1, 10**9),
    max_depth=24,
):
    """Certified 10x10 boundary-facet block h*int_F(q_i*q_j) ds."""
    maps, basis, _, adj, det = _geometry_data(node_coordinates, interpolation_points)
    hessians = [_physical_hessian_numerators(phi, maps, adj, det)
                for phi in basis]
    qnums, det3, radicand = _edge_polynomial_data(
        maps, det, hessians, edge_vertices)
    h = _as_fraction(h_weight)
    matrix = [[None for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(i, 10):
            numerator = _scale1(_mul1(qnums[i], qnums[j]), h)
            denominator = _pow1(det3, 2)
            lo, hi, leaves, depth = integrate_rational_sqrt_segment(
                numerator, denominator, radicand,
                absolute_tolerance=absolute_tolerance,
                max_depth=max_depth,
            )
            matrix[i][j] = matrix[j][i] = (lo, hi)
    return {
        "matrix_interval": matrix,
        "edge_vertices": tuple(edge_vertices),
        "integration": "exact-rational Bernstein enclosure with certified positive arclength radicand",
    }


def interval_matrix_add(target, source):
    """Add two square rational interval matrices in place."""
    n = len(target)
    if len(source) != n:
        raise ValueError("interval matrix dimensions differ")
    for i in range(n):
        for j in range(n):
            if target[i][j] is None:
                target[i][j] = source[i][j]
            else:
                target[i][j] = (target[i][j][0]+source[i][j][0],
                                target[i][j][1]+source[i][j][1])


def certify_interval_psd(matrix_interval):
    """Sufficient exact PSD certificate for every symmetric matrix in an interval.

    Let M0 be the rational midpoint matrix and eps the largest entrywise
    radius. Then ||M-M0||_2 <= n*eps. If M0-n*eps*I is exactly PSD,
    every matrix in the interval is PSD. This is conservative but rigorous.
    """
    from models.morandotti_exact_integration import certify_rational_psd
    n = len(matrix_interval)
    if any(len(row) != n for row in matrix_interval):
        raise ValueError("interval matrix must be square")
    midpoint = [[None]*n for _ in range(n)]
    radius = F(0)
    for i in range(n):
        for j in range(n):
            lo, hi = matrix_interval[i][j]
            if lo > hi:
                raise ValueError("invalid interval endpoint order")
            if matrix_interval[j][i] != matrix_interval[i][j]:
                raise ValueError("interval matrix must be exactly symmetric")
            midpoint[i][j] = (lo+hi)/2
            radius = max(radius, (hi-lo)/2)
    shifted = [[midpoint[i][j] - (n*radius if i == j else 0)
                for j in range(n)] for i in range(n)]
    positive, pivots = certify_rational_psd(shifted)
    return {
        "certified": bool(positive),
        "dimension": n,
        "entrywise_radius": radius,
        "spectral_error_bound": n*radius,
        "midpoint_shifted_psd": bool(positive),
        "exact_schur_pivots": pivots,
        "method": "rational midpoint plus n*entry-radius Weyl/Gershgorin perturbation bound",
    }
