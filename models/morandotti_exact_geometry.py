"""Exact-rational Bernstein certificates for cubic triangular geometry maps.

Stored IEEE-754 geometry coordinates are interpreted as exact dyadic rationals.
The P3 coordinate map is reconstructed from nodal values with the exact
equispaced triangular Lagrange basis. All polynomial arithmetic uses Fraction.
"""
from __future__ import annotations
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import isqrt

Poly = dict[tuple[int, int], Fraction]

def _add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Fraction(0)) + value
        if out[key] == 0:
            del out[key]
    return out

def _scale(a: Poly, c: Fraction) -> Poly:
    return {key: value * c for key, value in a.items() if value * c}

def _mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for (i, j), u in a.items():
        for (k, ell), v in b.items():
            key = (i + k, j + ell)
            out[key] = out.get(key, Fraction(0)) + u * v
    return {key: value for key, value in out.items() if value}

def _derivative(a: Poly, axis: int) -> Poly:
    out: Poly = {}
    for (i, j), value in a.items():
        if axis == 0 and i:
            out[(i - 1, j)] = i * value
        elif axis == 1 and j:
            out[(i, j - 1)] = j * value
    return out

_LAMBDA: tuple[Poly, ...] = (
    {(0, 0): Fraction(1), (1, 0): Fraction(-1), (0, 1): Fraction(-1)},
    {(1, 0): Fraction(1)},
    {(0, 1): Fraction(1)},
)

@lru_cache(maxsize=None)
def _p3_lagrange_basis(alpha: tuple[int, int, int]) -> Poly:
    result: Poly = {(0, 0): Fraction(1)}
    for lam, count in zip(_LAMBDA, alpha):
        for r in range(count):
            factor = _add(_scale(lam, Fraction(3)), {(0, 0): Fraction(-r)})
            result = _mul(result, _scale(factor, Fraction(1, count - r)))
    return result

def _falling(n: int, k: int) -> int:
    if k > n:
        return 0
    value = 1
    for r in range(k):
        value *= n - r
    return value

def _bernstein_coefficients(power: Poly, degree: int) -> list[Fraction]:
    denominator = [_falling(degree, k) for k in range(degree + 1)]
    result: list[Fraction] = []
    for a in range(degree + 1):
        for b in range(degree + 1 - a):
            c = degree - a - b
            value = Fraction(0)
            for (i, j), coefficient in power.items():
                if i + j <= degree and b >= i and c >= j:
                    value += coefficient * Fraction(
                        _falling(b, i) * _falling(c, j), denominator[i + j]
                    )
            result.append(value)
    return result

def _power(poly: Poly, exponent: int) -> Poly:
    result: Poly = {(0, 0): Fraction(1)}
    for _ in range(exponent):
        result = _mul(result, poly)
    return result

def _compose_affine(power: Poly, triangle) -> Poly:
    (x0, y0), (x1, y1), (x2, y2) = triangle
    x = {(0, 0): x0, (1, 0): x1 - x0, (0, 1): x2 - x0}
    y = {(0, 0): y0, (1, 0): y1 - y0, (0, 1): y2 - y0}
    result: Poly = {}
    for (i, j), coefficient in power.items():
        term = _mul(_power(x, i), _power(y, j))
        result = _add(result, _scale(term, coefficient))
    return result

def _certify_positive_exact(power: Poly, degree: int = 4,
                            max_depth: int = 8, max_nodes: int = 4096):
    """Prove positivity by exact Bernstein convex-hull bounds/subdivision."""
    root = ((Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(1)))
    leaves: list[tuple[Fraction, Fraction, int]] = []
    visited = 0

    def visit(triangle, depth: int) -> bool:
        nonlocal visited
        visited += 1
        if visited > max_nodes:
            return False
        local = _compose_affine(power, triangle)
        coefficients = _bernstein_coefficients(local, degree)
        lower, upper = min(coefficients), max(coefficients)
        if lower > 0:
            leaves.append((lower, upper, depth))
            return True
        if upper <= 0:
            return False
        if depth >= max_depth:
            return False
        v0, v1, v2 = triangle
        def midpoint(p, q):
            return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        m01, m12, m20 = midpoint(v0, v1), midpoint(v1, v2), midpoint(v2, v0)
        children = ((v0, m01, m20), (m01, v1, m12),
                    (m20, m12, v2), (m01, m12, m20))
        for child in children:
            if not visit(child, depth + 1):
                return False
        return True

    success = visit(root, 0)
    return {
        "positive": success,
        "lower": min((leaf[0] for leaf in leaves), default=None),
        "upper": max((leaf[1] for leaf in leaves), default=None),
        "depth": max((leaf[2] for leaf in leaves), default=0),
        "nodes": visited,
    }

def _sqrt_upper_fraction(value: Fraction, decimal_places: int = 30) -> Fraction:
    """A rational upper bound for sqrt(value), using integer arithmetic."""
    if value < 0:
        raise ValueError("cannot bound the square root of a negative rational")
    if value == 0:
        return Fraction(0)
    scale = 10 ** decimal_places
    numerator = value.numerator * scale * scale
    denominator = value.denominator
    root = isqrt(numerator // denominator)
    if root * root * denominator < numerator:
        root += 1
    return Fraction(root, scale)

def _float_upper(value: Fraction) -> float:
    import math
    return math.nextafter(float(value), math.inf)

def _float_lower(value: Fraction) -> float:
    import math
    return math.nextafter(float(value), -math.inf)

def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]

def certify_p3_cell_geometry(node_coordinates, interpolation_points, max_depth: int = 8):
    """Return exact Bernstein bounds for one equispaced P3 triangle.

    Coordinates must be in coordinate-element basis/dof order. The scale s is
    the maximum coordinate-component span of the three physical vertices;
    for the cell diameter h measured over all geometry nodes, s <= h <= sqrt(2)*s*M1,
    where M1 is the certified Frobenius bound for J/s.
    """
    if len(node_coordinates) != 10 or len(interpolation_points) != 10:
        raise ValueError("a cubic triangular coordinate map must have 10 nodes")
    alpha_to_index: dict[tuple[int, int, int], int] = {}
    for index, point in enumerate(interpolation_points):
        x, y = float(point[0]), float(point[1])
        i, j = round(3 * x), round(3 * y)
        a = 3 - i - j
        if min(a, i, j) < 0 or abs(3 * x - i) > 1e-12 or abs(3 * y - j) > 1e-12:
            raise ValueError("coordinate element is not the equispaced triangular P3 lattice")
        alpha = (a, i, j)
        if alpha in alpha_to_index:
            raise ValueError("duplicate P3 coordinate interpolation point")
        alpha_to_index[alpha] = index
    expected = {(3 - i - j, i, j)
                for i in range(4) for j in range(4 - i)}
    if set(alpha_to_index) != expected:
        raise ValueError("coordinate element does not cover the equispaced P3 lattice")

    coordinates = [
        [Fraction.from_float(float(value)) for value in node_coordinates[k][:2]]
        for k in range(10)
    ]
    digest = sha256()
    for point in node_coordinates:
        for value in point[:2]:
            digest.update(float(value).hex().encode("ascii"))
            digest.update(b";")

    maps: list[Poly] = []
    for component in range(2):
        polynomial: Poly = {}
        for alpha, index in alpha_to_index.items():
            polynomial = _add(
                polynomial,
                _scale(_p3_lagrange_basis(alpha), coordinates[index][component]),
            )
        maps.append(polynomial)

    xmap, ymap = maps
    jacobian = ((_derivative(xmap, 0), _derivative(xmap, 1)),
                (_derivative(ymap, 0), _derivative(ymap, 1)))
    determinant = _add(
        _mul(jacobian[0][0], jacobian[1][1]),
        _scale(_mul(jacobian[0][1], jacobian[1][0]), Fraction(-1)),
    )

    vertex_coordinates = [
        coordinates[alpha_to_index[alpha]]
        for alpha in ((3, 0, 0), (0, 3, 0), (0, 0, 3))
    ]
    scale = max(
        abs(vertex_coordinates[i][axis] - vertex_coordinates[j][axis])
        for i in range(3) for j in range(i) for axis in range(2)
    )
    if scale <= 0:
        raise ValueError("degenerate physical vertex scale")

    jacobian_component_bounds = [
        max(abs(value) for value in _bernstein_coefficients(entry, 2))
        for row in jacobian for entry in row
    ]
    m1_squared = sum(value * value for value in jacobian_component_bounds) / (scale * scale)

    hessian_component_bounds = []
    for polynomial in maps:
        hessian_component_bounds.extend((
            max(abs(value) for value in _bernstein_coefficients(
                _derivative(_derivative(polynomial, 0), 0), 1)),
            max(abs(value) for value in _bernstein_coefficients(
                _derivative(_derivative(polynomial, 0), 1), 1)),
            max(abs(value) for value in _bernstein_coefficients(
                _derivative(_derivative(polynomial, 1), 1), 1)),
        ))
    m2_squared = (
        hessian_component_bounds[0] ** 2 + 2 * hessian_component_bounds[1] ** 2
        + hessian_component_bounds[2] ** 2 + hessian_component_bounds[3] ** 2
        + 2 * hessian_component_bounds[4] ** 2 + hessian_component_bounds[5] ** 2
    ) / (scale * scale)

    det_cert = _certify_positive_exact(determinant, 4, max_depth=max_depth)
    if not det_cert["positive"]:
        return {
            "positive": False,
            "failure": "exact Bernstein subdivision did not prove det(J)>0",
            "subdivision_depth_max": det_cert["depth"],
            "subdivision_nodes": det_cert["nodes"],
            "coordinate_sha256": digest.hexdigest(),
        }

    j_lower = det_cert["lower"] / (scale * scale)
    j_upper = det_cert["upper"] / (scale * scale)
    m1_upper = _sqrt_upper_fraction(m1_squared)
    m2_upper = _sqrt_upper_fraction(m2_squared)
    # The curved-cell diameter may include all high-order geometry nodes.
    # Since diam(reference triangle)=sqrt(2), h <= sqrt(2)*s*M1.
    # Also h >= s from the physical vertices.
    mminus1_upper = _sqrt_upper_fraction(Fraction(2)) * m1_upper * m1_upper / j_lower

    return {
        "positive": True,
        "determinant_lower_scaled_exact": _fraction_pair(j_lower),
        "determinant_upper_scaled_exact": _fraction_pair(j_upper),
        "M1_upper_scaled_exact": _fraction_pair(m1_upper),
        "M2_upper_scaled_exact": _fraction_pair(m2_upper),
        "M_minus1_upper_scaled_exact": _fraction_pair(mminus1_upper),
        "M1_upper_bound": _float_upper(m1_upper),
        "M2_upper_bound": _float_upper(m2_upper),
        "M_minus1_upper_bound": _float_upper(mminus1_upper),
        "j0_lower_bound": _float_lower(j_lower / (2 * m1_upper * m1_upper)),
        "j1_upper_bound": _float_upper(j_upper),
        "subdivision_depth_max": det_cert["depth"],
        "subdivision_nodes": det_cert["nodes"],
        "coordinate_sha256": digest.hexdigest(),
    }
