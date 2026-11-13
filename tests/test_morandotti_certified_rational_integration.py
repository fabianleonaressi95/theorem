from fractions import Fraction as F

import pytest

from models.morandotti_certified_rational_integration import (
    integrate_rational_triangle,
)


def test_exact_constant_and_linear_integrals_are_enclosed():
    lo, hi, leaves, _ = integrate_rational_triangle(
        {(0, 0): 2}, {(0, 0): 1}, absolute_tolerance=F(1, 10**12)
    )
    assert lo == hi == 1
    assert leaves == 1

    lo, hi, _, _ = integrate_rational_triangle(
        {(1, 0): 1}, {(0, 0): 1}, absolute_tolerance=F(1, 10**5)
    )
    assert lo <= F(1, 6) <= hi
    assert hi-lo <= F(1, 10**5)


def test_rational_integral_with_positive_denominator():
    # Integral 1/(1+x) over the reference triangle; enclosure is rigorous.
    lo, hi, _, _ = integrate_rational_triangle(
        {(0, 0): 1}, {(0, 0): 1, (1, 0): 1},
        absolute_tolerance=F(1, 10**4), max_depth=12,
    )
    assert lo < hi
    assert hi-lo <= F(1, 10**4)


def test_denominator_zero_or_uncertified_is_rejected():
    with pytest.raises(ZeroDivisionError):
        integrate_rational_triangle({(0, 0): 1}, {})
    with pytest.raises(ArithmeticError):
        integrate_rational_triangle(
            {(0, 0): 1}, {(1, 0): 1}, max_depth=0
        )


def test_float_coefficients_are_rejected():
    with pytest.raises(TypeError):
        integrate_rational_triangle({(0, 0): 0.5}, {(0, 0): 1})
