from fractions import Fraction as F

import pytest

from models.morandotti_exact_integration import (
    certify_rational_psd,
    certify_trace_upper_bound,
    integrate_reference_segment,
    integrate_reference_triangle,
)


def test_triangle_monomials_are_integrated_exactly():
    assert integrate_reference_triangle({(0, 0): 1}) == F(1, 2)
    assert integrate_reference_triangle({(1, 0): 1}) == F(1, 6)
    assert integrate_reference_triangle({(1, 1): 1}) == F(1, 24)
    assert integrate_reference_triangle({(2, 0): 3, (0, 1): -2}) == F(-1, 12)


def test_segment_polynomial_is_integrated_exactly():
    assert integrate_reference_segment({0: 2, 1: 3, 3: -4}) == F(1, 1)


def test_exact_integrator_rejects_floating_coefficients():
    with pytest.raises(TypeError, match="only int or Fraction"):
        integrate_reference_triangle({(0, 0): 0.5})


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 1], [1, 1]], True),
        ([[2, 1], [1, 2]], True),
        ([[1, 2], [2, 1]], False),
        ([[0, 0], [0, 0]], True),
        ([[0, 1], [1, 0]], False),
        ([[1, 0], [0, -1]], False),
    ],
)
def test_rational_psd_decision(matrix, expected):
    assert certify_rational_psd(matrix)[0] is expected


def test_trace_upper_bound_is_exact_matrix_inequality():
    d = [[F(2), F(0)], [F(0), F(1)]]
    h = [[F(3), F(0)], [F(0), F(1)]]
    assert certify_trace_upper_bound(h, d, F(2))[0]
    assert not certify_trace_upper_bound(h, d, F(1))[0]


def test_psd_requires_exact_symmetry():
    with pytest.raises(ValueError, match="exactly symmetric"):
        certify_rational_psd([[1, 0], [1, 1]])
