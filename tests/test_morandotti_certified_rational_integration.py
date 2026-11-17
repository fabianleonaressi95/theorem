from fractions import Fraction as F

import pytest

from models.morandotti_certified_rational_integration import (
    integrate_rational_triangle, integrate_rational_triangle_many,
)


def test_exact_constant_and_linear_integrals_are_enclosed():
    lo, hi, leaves, _ = integrate_rational_triangle(
        {(0, 0): 2}, {(0, 0): 1}, absolute_tolerance=F(1, 10**12)
    )
    assert lo == hi == 1
    assert leaves == 1

    lo, hi, _, _ = integrate_rational_triangle(
        {(1, 0): 1}, {(0, 0): 1}, absolute_tolerance=F(1, 10**5), max_depth=18
    )
    assert lo <= F(1, 6) <= hi
    assert hi-lo <= F(1, 10**5)


def test_rational_integral_with_positive_denominator():
    # The rational Neumann enclosure certifies this mildly varying denominator
    # on the root triangle, without unnecessary geometric subdivision.
    lo, hi, leaves, depth = integrate_rational_triangle(
        {(0, 0): 1}, {(0, 0): 1, (1, 0): 1},
        absolute_tolerance=F(1, 5), max_depth=2,
    )
    assert lo < hi
    assert hi-lo <= F(1, 5)
    assert leaves == 1
    assert depth == 0


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



def test_shared_triangle_integrator_overlaps_scalar_enclosures():
    numerators = [
        {(0, 0): F(1)},
        {(1, 0): F(1)},
        {(0, 1): F(1)},
    ]
    denominator = {(0, 0): F(1), (1, 0): F(1)}
    kwargs = {"absolute_tolerance": F(1, 5), "max_depth": 4}
    batch = integrate_rational_triangle_many(numerators, denominator, **kwargs)
    scalar = [
        integrate_rational_triangle(p, denominator, **kwargs)
        for p in numerators
    ]
    for (blo, bhi, _, _), (slo, shi, _, _) in zip(batch, scalar):
        assert blo <= shi
        assert slo <= bhi


def test_shared_tree_uses_signed_neumann_enclosure_without_forced_refinement():
    # The numerator changes sign on the root triangle.  A direct quotient
    # range forces subdivision; the signed Neumann expansion certifies it
    # on the root using an L-infinity/Bernstein remainder bound.
    numerator = {(1, 0): F(1), (0, 0): -F(1, 3)}
    denominator = {(0, 0): F(1), (1, 0): F(1)}
    # Keep the remaining entries small enough that they do not force
    # unrelated refinement of the shared tree.
    numerators = [numerator] + [
        {(0, 0): F(1, 100), (1, 0): F(1, 100)}
        for _ in range(54)
    ]
    result = integrate_rational_triangle_many(
        numerators, denominator,
        absolute_tolerance=F(1, 5), max_depth=8,
    )
    lo, hi, leaves, depth = result[0]
    assert lo < hi
    assert hi-lo <= F(1, 5)
    assert leaves == 1
    assert depth == 0

    scalar_lo, scalar_hi, _, _ = integrate_rational_triangle(
        numerator, denominator,
        absolute_tolerance=F(1, 5), max_depth=8,
    )
    assert lo <= scalar_hi
    assert scalar_lo <= hi


def test_batch_refinement_is_local_to_the_numerator_that_needs_it():
    denominator = {(0, 0): F(1), (1, 0): F(1)}
    numerators = [
        {(0, 0): F(1)},  # Needs subdivision to meet this tight tolerance.
        {},              # Identically zero: certified exactly on the root.
    ]
    result = integrate_rational_triangle_many(
        numerators, denominator,
        absolute_tolerance=F(1, 1000), max_depth=8,
    )
    hard_lo, hard_hi, hard_leaves, hard_depth = result[0]
    easy_lo, easy_hi, easy_leaves, easy_depth = result[1]
    scalar_lo, scalar_hi, _, _ = integrate_rational_triangle(
        numerators[0], denominator,
        absolute_tolerance=F(1, 1000), max_depth=8,
    )
    assert hard_lo <= scalar_hi and scalar_lo <= hard_hi
    assert hard_lo < hard_hi
    assert hard_hi-hard_lo <= F(1, 1000)
    assert hard_leaves > 1
    assert hard_depth > 0
    assert easy_lo == easy_hi == 0
    assert easy_leaves == 1
    assert easy_depth == 0



def test_bernstein_residual_integrator_certifies_nonconstant_rational_integral():
    from models.morandotti_certified_rational_integration import (
        integrate_rational_triangle_bernstein_residual,
    )

    lo, hi, leaves, depth = integrate_rational_triangle_bernstein_residual(
        {(0, 0): F(1)},
        {(0, 0): F(1), (1, 0): F(1)},
        absolute_tolerance=F(1, 100000),
        max_depth=12,
        expansion_order=2,
    )
    # Integral = 2*log(2)-1; these rational bounds are deliberately wider
    # than the requested enclosure to avoid floating-point test oracles.
    assert lo <= F(3862, 10000)
    assert hi >= F(3862, 10000)
    assert hi-lo <= F(1, 100000)
    assert leaves >= 1
    assert depth <= 12


def test_bernstein_residual_integrator_handles_sign_changing_numerator():
    from models.morandotti_certified_rational_integration import (
        integrate_rational_triangle_bernstein_residual,
    )

    numerator = {(1, 0): F(1), (0, 0): -F(1, 3)}
    denominator = {(0, 0): F(1), (1, 0): F(1)}
    lo, hi, leaves, depth = integrate_rational_triangle_bernstein_residual(
        numerator, denominator,
        absolute_tolerance=F(1, 10000),
        max_depth=12,
        expansion_order=2,
    )
    scalar_lo, scalar_hi, _, _ = integrate_rational_triangle(
        numerator, denominator,
        absolute_tolerance=F(1, 10000),
        max_depth=12,
    )
    assert lo <= scalar_hi and scalar_lo <= hi
    assert hi-lo <= F(1, 10000)
    assert leaves >= 1
    assert depth <= 12


def test_bernstein_residual_integrator_rejects_uncertified_denominator():
    from models.morandotti_certified_rational_integration import (
        integrate_rational_triangle_bernstein_residual,
    )

    with pytest.raises(ArithmeticError):
        integrate_rational_triangle_bernstein_residual(
            {(0, 0): F(1)}, {(1, 0): F(1)}, max_depth=0
        )
