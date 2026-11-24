"""Finite, reproducible geometry checks for circular and affine vesicae.

This module samples the exact lens boundary (two equal intersecting disks)
and applies invertible affine maps to obtain elliptical vesicae. Box counts
are finite-resolution diagnostics; they are not proofs of fractality.
"""
from __future__ import annotations

import math
from typing import Iterable


Point = tuple[float, float]


def circular_vesica_boundary(radius: float = 1.0, center_distance: float = 1.0,
                              samples_per_arc: int = 2000) -> list[Point]:
    """Sample the boundary of the intersection of two equal disks.

    The disk centres are (-d/2, 0) and (d/2, 0). The returned boundary is
    the two inward-facing circular arcs, with endpoints included.
    """
    if radius <= 0 or not 0 < center_distance < 2 * radius:
        raise ValueError("require radius > 0 and 0 < center_distance < 2*radius")
    if samples_per_arc < 2:
        raise ValueError("samples_per_arc must be at least 2")
    half = center_distance / 2.0
    alpha = math.acos(half / radius)
    points: list[Point] = []
    # Right circle's left-facing arc.
    for j in range(samples_per_arc):
        theta = math.pi - alpha + (2 * alpha) * j / (samples_per_arc - 1)
        points.append((half + radius * math.cos(theta),
                       radius * math.sin(theta)))
    # Left circle's right-facing arc closes the lens.
    for j in range(samples_per_arc):
        theta = -alpha + (2 * alpha) * j / (samples_per_arc - 1)
        points.append((-half + radius * math.cos(theta),
                       radius * math.sin(theta)))
    return points


def affine_transform(points: Iterable[Point], matrix: tuple[tuple[float, float],
                                                              tuple[float, float]]) -> list[Point]:
    """Apply a 2x2 linear map to points."""
    (a, b), (c, d) = matrix
    det = a * d - b * c
    if abs(det) < 1e-14:
        raise ValueError("affine linear part must be invertible")
    return [(a*x + b*y, c*x + d*y) for x, y in points]


def ellipse_deform(points: Iterable[Point], axis_x: float, axis_y: float,
                   angle: float = 0.0) -> list[Point]:
    """Apply rotation(angle) @ diag(axis_x, axis_y) to a vesica boundary."""
    if axis_x <= 0 or axis_y <= 0:
        raise ValueError("ellipse axes must be positive")
    co, si = math.cos(angle), math.sin(angle)
    return affine_transform(points, ((co*axis_x, -si*axis_y),
                                     (si*axis_x, co*axis_y)))


def box_count(points: Iterable[Point], epsilon: float) -> int:
    """Count occupied square boxes of side epsilon for a finite point set."""
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    occupied = set()
    for x, y in points:
        occupied.add((math.floor(x / epsilon), math.floor(y / epsilon)))
    return len(occupied)


def effective_box_dimension(points: Iterable[Point], scales: Iterable[float]) -> float:
    """Least-squares slope of log N(eps) against log(1/eps), finite-scale only."""
    scales = list(scales)
    if len(scales) < 2:
        raise ValueError("at least two scales are required")
    pairs = [(math.log(1.0 / eps), math.log(box_count(points, eps)))
             for eps in scales]
    xbar = sum(x for x, _ in pairs) / len(pairs)
    ybar = sum(y for _, y in pairs) / len(pairs)
    denominator = sum((x - xbar) ** 2 for x, _ in pairs)
    if denominator == 0:
        raise ValueError("scales must be distinct")
    return sum((x - xbar) * (y - ybar) for x, y in pairs) / denominator


def vesica_family(radius: float = 1.0, center_distance: float = 1.0,
                  samples_per_arc: int = 1000) -> dict[str, list[Point]]:
    """Return circular, elliptic, bivesica and trivesica point clouds.

    Bivesica/trivesica here mean unions of two/three translated lens boundaries;
    they are finite geometric configurations, not asserted fractals.
    """
    base = circular_vesica_boundary(radius, center_distance, samples_per_arc)
    ellipse = ellipse_deform(base, 1.4, 0.65, angle=math.pi / 7)
    def shift(points: list[Point], dx: float, dy: float) -> list[Point]:
        return [(x + dx, y + dy) for x, y in points]
    return {
        "vesica": base,
        "elliptic_vesica": ellipse,
        "bivesica": base + shift(base, 1.2, 0.0),
        "trivesica": (base + shift(base, 1.2, 0.0)
                      + shift(base, 0.6, 1.0)),
    }
