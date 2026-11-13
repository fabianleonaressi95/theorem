from fractions import Fraction

import numpy as np
import pytest

from models.morandotti_exact_geometry import certify_p3_cell_geometry


ALPHAS = [
    (3 - i - j, i, j)
    for i in range(4)
    for j in range(4 - i)
]
POINTS = [(i / 3.0, j / 3.0) for _, i, j in ALPHAS]


def nodal_map(function):
    return np.asarray([function(x, y) for x, y in POINTS], dtype=np.float64)


def test_exact_p3_certificate_accepts_affine_orientation_preserving_map():
    nodes = nodal_map(lambda x, y: (x, y))
    result = certify_p3_cell_geometry(nodes, POINTS)

    assert result["positive"]
    assert result["subdivision_depth_max"] == 0
    assert result["j0_lower_bound"] > 0.24
    assert result["j1_upper_bound"] < 1.01
    assert result["M1_upper_bound"] < 1.42
    assert result["M2_upper_bound"] < 1e-12
    assert result["M_minus1_upper_bound"] < 2.84
    assert len(result["coordinate_sha256"]) == 64
    assert result["determinant_lower_scaled_exact"][1] > 0


def test_exact_p3_certificate_bounds_a_curved_map():
    nodes = nodal_map(
        lambda x, y: (x + 0.04 * x * y, y + 0.03 * x * (1.0 - x - y))
    )
    result = certify_p3_cell_geometry(nodes, POINTS)

    assert result["positive"]
    assert result["M2_upper_bound"] > 0.0
    assert result["M1_upper_bound"] > 1.0
    assert result["j0_lower_bound"] > 0.0


def test_exact_p3_certificate_rejects_orientation_reversal():
    nodes = nodal_map(lambda x, y: (-x, y))
    result = certify_p3_cell_geometry(nodes, POINTS)
    assert not result["positive"]


def test_exact_p3_certificate_rejects_non_equispaced_nodes():
    nodes = nodal_map(lambda x, y: (x, y))
    bad_points = list(POINTS)
    bad_points[4] = (0.31, 0.33)
    with pytest.raises(ValueError, match="equispaced"):
        certify_p3_cell_geometry(nodes, bad_points)


def test_exact_bernstein_bounds_are_rationally_reproducible():
    nodes = nodal_map(lambda x, y: (x + 0.02 * x * y, y))
    first = certify_p3_cell_geometry(nodes, POINTS)
    second = certify_p3_cell_geometry(nodes.copy(), POINTS)
    assert first == second
    numerator, denominator = first["determinant_lower_scaled_exact"]
    assert Fraction(numerator, denominator) > 0
