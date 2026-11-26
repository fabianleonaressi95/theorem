"""Regression checks for the exact geometric benchmark in T099."""

from math import asin, isclose, pi, sqrt


def triangle_disk_overlap(h: float) -> float:
    if h <= 0:
        raise ValueError("h must be positive")
    if h <= 1:
        return h
    q = h * (h - 1.0) / (h * h + 1.0)
    return q * sqrt(1.0 - q * q) + asin(q) + h * (1.0 - q) ** 2


def test_triangle_disk_overlap_unit_height():
    assert isclose(triangle_disk_overlap(1.0), 1.0, rel_tol=0.0, abs_tol=1e-14)


def test_triangle_disk_overlap_sqrt_three():
    assert isclose(
        triangle_disk_overlap(sqrt(3.0)),
        1.4312041746394546,
        rel_tol=0.0,
        abs_tol=2e-14,
    )


def test_triangle_disk_overlap_large_height_limit():
    # The formula approaches the upper half-disk area from finite heights.
    assert abs(triangle_disk_overlap(1.0e7) - pi / 2.0) < 1.0e-3


def test_triangle_disk_overlap_is_continuous_at_one():
    eps = 1.0e-7
    assert abs(triangle_disk_overlap(1.0 + eps) - 1.0) < 1.0e-6


def test_nonpositive_height_is_rejected():
    try:
        triangle_disk_overlap(0.0)
    except ValueError:
        pass
    else:
        raise AssertionError("nonpositive height must be rejected")
