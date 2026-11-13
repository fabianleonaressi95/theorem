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
from functools import lru_cache
from math import factorial
from typing import Mapping, Sequence

from models.morandotti_exact_geometry import (
    _add, _derivative, _mul, _p3_lagrange_basis, _scale,
    _certify_positive_exact,
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


@lru_cache(maxsize=131072)
def _compose_line_cached(poly_items, a: Point, b: Point):
    p = dict(poly_items)
    x = {0: a[0], 1: b[0]-a[0]}
    y = {0: a[1], 1: b[1]-a[1]}
    out = {}
    for (i, j), c in p.items():
        term = _mul1(_pow1(x, i), _pow1(y, j))
        out = _add1(out, _scale1(term, c))
    return out


def _compose_line(p: BPoly, a: Point, b: Point) -> dict[int, F]:
    """Substitute (x,y)=a+t(b-a) into a bivariate polynomial."""
    return _compose_line_cached(tuple(sorted(p.items())), a, b)


@lru_cache(maxsize=131072)
def _bernstein_bounds_1d_cached(poly_items):
    p = dict(poly_items)
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


def _bernstein_bounds_1d(p: SPoly):
    return _bernstein_bounds_1d_cached(tuple(sorted(p.items())))


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
    if len(q) == 1 and len(s) == 1:
        q0, s0 = next(iter(q.values())), next(iter(s.values()))
        if q0 <= 0 or s0 <= 0:
            raise ArithmeticError("constant facet denominator or metric is not positive")
        integral_p = sum((coefficient/F(degree+1)
                          for degree, coefficient in p.items()), F(0))
        root_lo, root_hi = _sqrt_lower(s0), _sqrt_upper(s0)
        factor_lo = F(1)/(q0*root_hi**3)
        factor_hi = F(1)/(q0*root_lo**3)
        if integral_p >= 0:
            return integral_p*factor_lo, integral_p*factor_hi, 1, 0
        return integral_p*factor_hi, integral_p*factor_lo, 1, 0
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
        # Integrate the polynomial numerator exactly on the leaf. Only the
        # positive denominator and square-root metric are interval-bounded.
        integral_p = sum((coefficient/F(degree+1)
                          for degree, coefficient in pp.items()), F(0))
        if plo < 0 < phi:
            quotients = (plo/qlo, plo/qhi, phi/qlo, phi/qhi)
            rlo, rhi = min(quotients), max(quotients)
            sqrt_lo = _sqrt_lower(slo)
            sqrt_hi = _sqrt_upper(shi)
            factors = (F(1)/(sqrt_hi**3), F(1)/(sqrt_lo**3))
            vals = (rlo*factors[0], rlo*factors[1],
                    rhi*factors[0], rhi*factors[1])
            flo, fhi = min(vals), max(vals)
            if fhi-flo > 2*tol:
                if depth >= max_depth:
                    raise ArithmeticError("facet integral enclosure width not reached on sign-changing numerator")
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
            continue
        sqrt_lo = _sqrt_lower(slo)
        sqrt_hi = _sqrt_upper(shi)
        factor_lo = F(1)/(qhi*sqrt_hi**3)
        factor_hi = F(1)/(qlo*sqrt_lo**3)
        if integral_p >= 0:
            flo, fhi = integral_p*factor_lo, integral_p*factor_hi
        else:
            flo, fhi = integral_p*factor_hi, integral_p*factor_lo
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
    det_certificate = _certify_positive_exact(det, 4, max_depth=8)
    if not det_certificate["positive"]:
        raise ArithmeticError("cell Jacobian positivity is not certified exactly")
    return maps, basis, j, adj, det


def _physical_hessian_numerators(basis_poly, maps, adj, det):
    """Return P_ij with D_x^2(phi)_ij = P_ij/det(J)^3."""
    second_map = [[[
        _derivative(_derivative(maps[r], a), b)
        for b in range(2)] for a in range(2)] for r in range(2)]
    grad = [_derivative(basis_poly, a) for a in range(2)]
    hess = [[_derivative(_derivative(basis_poly, a), b)
             for b in range(2)] for a in range(2)]
    corrected = [[_mul(hess[a][b], det) for b in range(2)]
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
    """Sufficient exact PSD certificate for every symmetric interval matrix.

    The midpoint matrix is shifted by the maximum row sum of entry radii.
    For symmetric perturbations this bounds the spectral norm. A sparse
    exact-rational LDL^T elimination then certifies the shifted midpoint PSD.
    Input may be a dense list-of-lists or a sparse {(i,j): (lo,hi)} mapping.
    """
    if isinstance(matrix_interval, Mapping):
        entries = dict(matrix_interval)
        indices = [i for key in entries for i in key]
        n = max(indices, default=-1) + 1
        get_interval = lambda i, j: entries.get((i, j), (F(0), F(0)))
        for (i, j), value in entries.items():
            if entries.get((j, i), (F(0), F(0))) != value:
                raise ValueError("interval matrix must be exactly symmetric")
    else:
        n = len(matrix_interval)
        if any(len(row) != n for row in matrix_interval):
            raise ValueError("interval matrix must be square")
        get_interval = lambda i, j: matrix_interval[i][j]
        for i in range(n):
            for j in range(n):
                if matrix_interval[j][i] != matrix_interval[i][j]:
                    raise ValueError("interval matrix must be exactly symmetric")

    radius = F(0)
    row_radii = [F(0) for _ in range(n)]
    midpoint = {}
    for i in range(n):
        for j in range(i, n):
            lo, hi = get_interval(i, j)
            if lo > hi:
                raise ValueError("invalid interval endpoint order")
            entry_radius = (hi-lo)/2
            radius = max(radius, entry_radius)
            row_radii[i] += entry_radius
            if j != i:
                row_radii[j] += entry_radius
            mid = (lo+hi)/2
            if mid:
                midpoint[(i, j)] = mid
    # For symmetric E with entry bounds eps_ij, ||E||_2 <= ||E||_infinity
    # <= max_i sum_j eps_ij. This sparse row-sum bound is much sharper than
    # n*max(eps_ij), while remaining a rigorous spectral perturbation bound.
    perturbation = max(row_radii, default=F(0))
    for i in range(n):
        key = (i, i)
        midpoint[key] = midpoint.get(key, F(0)) - perturbation
        if midpoint[key] == 0:
            midpoint.pop(key, None)

    # Sparse symmetric Schur-complement elimination. Positive pivots prove
    # positive definiteness; zero pivots are allowed only for zero rows.
    pivots = []
    for k in range(n):
        pivot = midpoint.get((k, k), F(0))
        if pivot < 0:
            return {
                "certified": False, "dimension": n,
                "entrywise_radius": radius,
                "spectral_error_bound": perturbation,
                "failed_pivot_index": k, "failed_pivot": pivot,
                "exact_schur_pivots": tuple(pivots),
                "method": "sparse exact-rational LDL^T with symmetric row-sum interval perturbation shift",
            }
        neighbors = [
            i for i in range(k+1, n)
            if midpoint.get((k, i), F(0)) != 0
        ]
        if pivot == 0:
            if neighbors:
                return {
                    "certified": False, "dimension": n,
                    "entrywise_radius": radius,
                    "spectral_error_bound": perturbation,
                    "failed_pivot_index": k, "failed_pivot": pivot,
                    "exact_schur_pivots": tuple(pivots),
                    "method": "sparse exact-rational LDL^T with interval perturbation shift",
                }
            continue
        pivots.append(pivot)
        column = {i: midpoint[(k, i)] for i in neighbors}
        for ii, i in enumerate(neighbors):
            for j in neighbors[ii:]:
                key = (i, j)
                updated = midpoint.get(key, F(0)) - column[i]*column[j]/pivot
                if updated:
                    midpoint[key] = updated
                else:
                    midpoint.pop(key, None)
        for i in neighbors:
            midpoint.pop((k, i), None)
        midpoint.pop((k, k), None)

    return {
        "certified": True,
        "dimension": n,
        "entrywise_radius": radius,
        "spectral_error_bound": perturbation,
        "midpoint_shifted_psd": True,
        "exact_schur_pivots": tuple(pivots),
        "method": "sparse exact-rational LDL^T with interval perturbation shift",
    }

def _edge_q_data(maps, det, hessians, edge_vertices, normal_numerator):
    a, b = (_REF_VERTICES[k] for k in edge_vertices)
    det_line = _compose_line(det, a, b)
    q_numerators = []
    for P in hessians:
        value = {}
        for r in range(2):
            for s in range(2):
                entry = _compose_line(P[r][s], a, b)
                value = _add1(value, _mul1(
                    _mul1(normal_numerator[r], normal_numerator[s]), entry))
        q_numerators.append(value)
    return q_numerators, _pow1(det_line, 3)


def _map_trace_on_edge(maps, edge_vertices):
    a, b = (_REF_VERTICES[k] for k in edge_vertices)
    return tuple(_compose_line(component, a, b) for component in maps)


def _integrate_facet_pair(numerator, det3_a, det3_b, radicand,
                          h_weight, tolerance, max_depth):
    denominator = _mul1(det3_a, det3_b)
    return integrate_rational_sqrt_segment(
        _scale1(numerator, _as_fraction(h_weight)/4),
        denominator, radicand,
        absolute_tolerance=tolerance, max_depth=max_depth,
    )[:2]


def assemble_interior_facet_interval(
    node_coordinates_a,
    node_coordinates_b,
    interpolation_points,
    edge_a: tuple[int, int],
    edge_b_matched: tuple[int, int],
    h_average,
    *,
    absolute_tolerance=F(1, 10**9),
    max_depth=24,
):
    """Certified 20x20 two-sided interior-facet block.

    edge_b_matched must list the B reference-edge endpoints in the same
    physical endpoint order as edge_a. The two exact cubic edge traces are
    compared coefficient-by-coefficient before any integration.
    """
    maps_a, basis_a, _, adj_a, det_a = _geometry_data(
        node_coordinates_a, interpolation_points)
    maps_b, basis_b, _, adj_b, det_b = _geometry_data(
        node_coordinates_b, interpolation_points)
    trace_a = _map_trace_on_edge(maps_a, edge_a)
    trace_b = _map_trace_on_edge(maps_b, edge_b_matched)
    if trace_a != trace_b:
        raise ValueError("neighboring P3 maps do not define the same exact curved facet trace")

    hess_a = [_physical_hessian_numerators(phi, maps_a, adj_a, det_a)
              for phi in basis_a]
    hess_b = [_physical_hessian_numerators(phi, maps_b, adj_b, det_b)
              for phi in basis_b]

    # The physical tangent and arclength metric are taken from side A.
    a0, a1 = (_REF_VERTICES[k] for k in edge_a)
    direction = (a1[0]-a0[0], a1[1]-a0[1])
    tangent = []
    for component in range(2):
        deriv = _add(
            _scale(_derivative(maps_a[component], 0), direction[0]),
            _scale(_derivative(maps_a[component], 1), direction[1]),
        )
        tangent.append(_compose_line(deriv, a0, a1))
    tx, ty = tangent
    radicand = _add1(_mul1(tx, tx), _mul1(ty, ty))
    normal_numerator = (ty, _scale1(tx, F(-1)))
    qa, da3 = _edge_q_data(maps_a, det_a, hess_a, edge_a, normal_numerator)
    qb, db3 = _edge_q_data(maps_b, det_b, hess_b, edge_b_matched, normal_numerator)

    AA = [[None]*10 for _ in range(10)]
    AB = [[None]*10 for _ in range(10)]
    BB = [[None]*10 for _ in range(10)]
    tol = _as_fraction(absolute_tolerance)
    for i in range(10):
        for j in range(10):
            if j >= i:
                lo, hi = _integrate_facet_pair(
                    _mul1(qa[i], qa[j]), da3, da3, radicand,
                    h_average, tol, max_depth)
                AA[i][j] = AA[j][i] = (lo, hi)
                lo, hi = _integrate_facet_pair(
                    _mul1(qb[i], qb[j]), db3, db3, radicand,
                    h_average, tol, max_depth)
                BB[i][j] = BB[j][i] = (lo, hi)
            lo, hi = _integrate_facet_pair(
                _mul1(qa[i], qb[j]), da3, db3, radicand,
                h_average, tol, max_depth)
            AB[i][j] = (lo, hi)
    return {
        "block_AA": AA,
        "block_AB": AB,
        "block_BB": BB,
        "edge_a": tuple(edge_a),
        "edge_b_matched": tuple(edge_b_matched),
        "integration": "exact-rational two-sided curved-facet enclosure with shared certified metric",
    }


def _zero_interval_matrix(n):
    # Sparse dictionary: (global_i, global_j) -> rational interval.
    return {}


def _accumulate(global_matrix, i, j, interval):
    lo, hi = interval
    if lo == 0 and hi == 0:
        return
    old = global_matrix.get((i, j), (F(0), F(0)))
    value = (old[0]+lo, old[1]+hi)
    if value == (F(0), F(0)):
        global_matrix.pop((i, j), None)
    else:
        global_matrix[(i, j)] = value


def _add_block(global_matrix, block, dofs):
    for i, gi in enumerate(dofs):
        for j, gj in enumerate(dofs):
            _accumulate(global_matrix, gi, gj, block[i][j])


def assemble_global_interval_forms(
    cell_node_coordinates,
    interpolation_points,
    cell_dofs,
    cell_diameters,
    boundary_facets,
    interior_facets,
    number_of_dofs,
    *,
    absolute_tolerance=F(1, 10**9),
    max_depth=24,
):
    """Assemble global D and H interval matrices from exact local blocks.

    boundary_facets entries: (cell, (local_vertex_0, local_vertex_1)).
    interior_facets entries: (cell_a, edge_a, cell_b, edge_b_matched).
    The edge_b_matched ordering must correspond to edge_a's physical endpoints.
    """
    nc = len(cell_node_coordinates)
    if not (len(cell_dofs) == len(cell_diameters) == nc):
        raise ValueError("cell geometry, dof maps, and diameters must have equal lengths")
    if any(len(dofs) != 10 for dofs in cell_dofs):
        raise ValueError("each P3 cell must provide ten scalar dofs")
    D = _zero_interval_matrix(number_of_dofs)
    H = _zero_interval_matrix(number_of_dofs)
    tol = _as_fraction(absolute_tolerance)
    for cell in range(nc):
        local = assemble_cell_volume_interval(
            cell_node_coordinates[cell], interpolation_points,
            absolute_tolerance=tol, max_depth=max_depth,
        )["matrix_interval"]
        _add_block(D, local, cell_dofs[cell])
    for cell, edge in boundary_facets:
        local = assemble_boundary_edge_interval(
            cell_node_coordinates[cell], interpolation_points, tuple(edge),
            _as_fraction(cell_diameters[cell]),
            absolute_tolerance=tol, max_depth=max_depth,
        )["matrix_interval"]
        _add_block(H, local, cell_dofs[cell])
    for ca, ea, cb, eb in interior_facets:
        local = assemble_interior_facet_interval(
            cell_node_coordinates[ca], cell_node_coordinates[cb],
            interpolation_points, tuple(ea), tuple(eb),
            (_as_fraction(cell_diameters[ca])+_as_fraction(cell_diameters[cb]))/2,
            absolute_tolerance=tol, max_depth=max_depth,
        )
        _add_block(H, local["block_AA"], cell_dofs[ca])
        _add_block(H, local["block_BB"], cell_dofs[cb])
        for i, gi in enumerate(cell_dofs[ca]):
            for j, gj in enumerate(cell_dofs[cb]):
                lo, hi = local["block_AB"][i][j]
                _accumulate(H, gi, gj, (lo, hi))
                _accumulate(H, gj, gi, (lo, hi))
    return {"D_interval": D, "H_interval": H, "dofs": number_of_dofs}


def certify_global_trace_bound(D_interval, H_interval, free_dofs, bound):
    """Propagate sparse form intervals to an exact quotient PSD certificate."""
    c = _as_fraction(bound)
    if c <= 0:
        raise ValueError("trace bound must be positive")
    free = list(map(int, free_dofs))
    if len(set(free)) != len(free) or any(i < 0 for i in free):
        raise ValueError("free_dofs must be unique nonnegative global indices")
    index = {global_dof: local for local, global_dof in enumerate(free)}
    M = {(i, i): (F(0), F(0)) for i in range(len(free))}
    keys = set(D_interval) | set(H_interval)
    for i, j in keys:
        if i not in index or j not in index:
            continue
        dlo, dhi = D_interval.get((i, j), (F(0), F(0)))
        hlo, hhi = H_interval.get((i, j), (F(0), F(0)))
        lo, hi = c*dlo-hhi, c*dhi-hlo
        if lo or hi:
            M[(index[i], index[j])] = (lo, hi)
    certificate = certify_interval_psd(M)
    certificate.update({
        "trace_bound": c,
        "quotient_dimension": len(free),
        "matrix": "C*D-H",
        "integration_uncertainty_propagated": True,
    })
    return certificate


def assemble_dolfinx_mesh_interval_forms(
    mesh,
    function_space,
    *,
    absolute_tolerance=F(1, 10**9),
    max_depth=24,
):
    """Extract a serial DOLFINx equispaced-P3 mesh and assemble sparse intervals.

    The coordinate and solution elements must have identical equispaced P3
    reference-node ordering. Facet traces are matched by their shared global
    vertex IDs and then checked as exact cubic physical polynomials.
    Returns sparse D/H intervals and the homogeneous-Dirichlet subspace.
    The physical Hessian kernel consists of global physical affine functions,
    not the reference C0-P1 space on a curved isoparametric mesh. Homogeneous
    boundary values eliminate that affine kernel on a nondegenerate domain;
    interior vertex degrees of freedom must therefore remain unconstrained.
    """
    import numpy as np
    import basix
    from dolfinx import fem
    from dolfinx.mesh import exterior_facet_indices

    if mesh.comm.size != 1:
        raise RuntimeError("certified global interval assembly currently requires a serial mesh")
    tdim = mesh.topology.dim
    if tdim != 2 or mesh.geometry.dim != 2:
        raise ValueError("T134 certified form assembly requires a planar triangular mesh in R^2")
    cmap = mesh.geometry.cmaps[0]
    if cmap.degree != 3 or cmap.dim != 10:
        raise ValueError("geometry coordinate map must be triangular P3 with ten nodes")
    # DOLFINx CoordinateElement exposes degree and variant directly.
    # It does not expose the underlying Basix element.
    try:
        coordinate_variant = basix.LagrangeVariant(cmap.variant)
    except (AttributeError, TypeError, ValueError) as exc:
        raise RuntimeError(
            "cannot verify DOLFINx coordinate-element Lagrange variant"
        ) from exc
    if coordinate_variant != basix.LagrangeVariant.equispaced:
        raise ValueError("geometry coordinate map must use equispaced P3 nodes")
    coordinate_element = basix.create_element(
        basix.ElementFamily.P, basix.CellType.triangle, 3,
        basix.LagrangeVariant.equispaced,
    )
    points = np.asarray(coordinate_element.points, dtype=float)
    try:
        solution_basix = function_space.element.basix_element
        solution_points = np.asarray(solution_basix.points, dtype=float)
        solution_interpolation = np.asarray(
            solution_basix.interpolation_matrix, dtype=float
        )
        solution_family = solution_basix.family
        solution_degree = solution_basix.degree
    except AttributeError as exc:
        raise RuntimeError(
            "cannot inspect the P3 solution element family, degree, nodes, and interpolation matrix"
        ) from exc
    if solution_family != basix.ElementFamily.P or solution_degree != 3:
        raise ValueError("solution element must be scalar Lagrange P3")
    if solution_points.shape != points.shape:
        raise ValueError("solution element must have the ten P3 reference nodes")
    if solution_interpolation.shape != (10, 10) or not np.allclose(
        solution_interpolation, np.eye(10), rtol=0.0, atol=1e-12
    ):
        raise ValueError("solution P3 element must have identity nodal interpolation")
    if solution_points.shape != points.shape:
        raise ValueError("solution and geometry P3 elements have different node counts")
    solution_order = []
    used_solution_nodes = set()
    for point in points:
        distances = np.linalg.norm(solution_points-point, axis=1)
        index = int(np.argmin(distances))
        if float(distances[index]) > 1e-12 or index in used_solution_nodes:
            raise ValueError(
                "solution and geometry P3 elements do not use the same equispaced reference-node set"
            )
        solution_order.append(index)
        used_solution_nodes.add(index)
    solution_order_for_geometry = np.asarray(solution_order, dtype=np.int64)

    nc = mesh.topology.index_map(tdim).size_local
    geometry_dofmap = np.asarray(mesh.geometry.dofmaps[0], dtype=np.int32)
    if geometry_dofmap.shape != (nc, 10):
        raise ValueError("expected ten coordinate nodes per owned P3 triangle")
    cell_nodes = [mesh.geometry.x[geometry_dofmap[c], :2].copy()
                  for c in range(nc)]
    cell_dofs = [
        np.asarray(function_space.dofmap.cell_dofs(c), dtype=np.int64)[solution_order_for_geometry]
        for c in range(nc)
    ]
    if any(len(dofs) != 10 for dofs in cell_dofs):
        raise ValueError("solution space is not scalar P3 on every triangle")
    cells = np.arange(nc, dtype=np.int32)
    diameters = np.asarray(mesh.h(tdim, cells), dtype=float)

    mesh.topology.create_connectivity(tdim, 0)
    mesh.topology.create_connectivity(1, 0)
    mesh.topology.create_connectivity(1, tdim)
    cell_vertices = mesh.topology.connectivity(tdim, 0)
    facet_vertices = mesh.topology.connectivity(1, 0)
    facet_cells = mesh.topology.connectivity(1, tdim)
    nfacets = mesh.topology.index_map(1).size_local
    boundary_facets = []
    interior_facets = []
    for facet in range(nfacets):
        adjacent = list(map(int, facet_cells.links(facet)))
        if len(adjacent) not in (1, 2):
            continue
        fv = list(map(int, facet_vertices.links(facet)))
        if len(fv) != 2:
            raise RuntimeError("triangular facet does not have exactly two vertices")
        ca = adjacent[0]
        va = list(map(int, cell_vertices.links(ca)))
        edge_a = tuple(va.index(vertex) for vertex in fv)
        if len(adjacent) == 1:
            boundary_facets.append((ca, edge_a))
        else:
            cb = adjacent[1]
            vb = list(map(int, cell_vertices.links(cb)))
            edge_b = tuple(vb.index(vertex) for vertex in fv)
            interior_facets.append((ca, edge_a, cb, edge_b))

    assembled = assemble_global_interval_forms(
        cell_nodes, points, cell_dofs, diameters,
        boundary_facets, interior_facets,
        int(function_space.dofmap.index_map.size_local),
        absolute_tolerance=absolute_tolerance, max_depth=max_depth,
    )
    exterior = exterior_facet_indices(mesh.topology)
    boundary_dofs = fem.locate_dofs_topological(function_space, 1, exterior)
    free = np.setdiff1d(
        np.arange(function_space.dofmap.index_map.size_local, dtype=np.int64),
        boundary_dofs,
    )
    assembled.update({
        "free_dofs": free.tolist(),
        "cell_count": nc,
        "interior_facet_count": len(interior_facets),
        "boundary_facet_count": len(boundary_facets),
        "quotient_definition": (
            "homogeneous physical Dirichlet trace; no interior vertex constraints; "
            "the only zero-Hessian modes are global physical affine functions, "
            "which are eliminated by zero trace on the full nondegenerate boundary"
        ),
        "coordinate_nodes": "stored IEEE-754 binary64 interpreted as exact dyadic rationals",
    })
    return assembled


def certify_dolfinx_mesh_trace_bound(
    mesh,
    function_space,
    bound,
    *,
    absolute_tolerance=F(1, 10**9),
    max_depth=24,
):
    """End-to-end finite-mesh assembly, interval propagation, and PSD test."""
    assembled = assemble_dolfinx_mesh_interval_forms(
        mesh, function_space, absolute_tolerance=absolute_tolerance,
        max_depth=max_depth,
    )
    certificate = certify_global_trace_bound(
        assembled["D_interval"], assembled["H_interval"],
        assembled["free_dofs"], bound,
    )
    certificate.update({
        "cell_count": assembled["cell_count"],
        "interior_facet_count": assembled["interior_facet_count"],
        "boundary_facet_count": assembled["boundary_facet_count"],
        "assembly": "exact-rational local curved-P3 Hessian blocks with certified volume/facet integral enclosures",
    })
    return certificate
