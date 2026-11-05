import math

import pytest

from scripts.microscopic_spin_correlations import (
    SpinCorrelationScaling,
    spin_current_decomposition,
)


def test_spin_current_splits_exactly_into_self_and_pair():
    result = spin_current_decomposition([(1, 0, 0), (-1, 0, 0), (0, 2, 0)])
    assert result["self"] == pytest.approx(6.0)
    assert result["pair"] == pytest.approx(-2.0)
    assert result["total"] == pytest.approx(4.0)
    assert result["identity_residual"] == pytest.approx(0.0, abs=1e-14)


def test_weighted_spin_current_decomposition():
    result = spin_current_decomposition([(1, 0, 0), (0, 1, 0)], [2, 3])
    assert result["current"] == pytest.approx((2, 3, 0))
    assert result["self"] == pytest.approx(13.0)
    assert result["pair"] == pytest.approx(0.0)
    assert result["total"] == pytest.approx(13.0)


def test_standard_pair_closure_is_a_minus_six_and_stiff():
    model = SpinCorrelationScaling(2.0, pair_amplitude=0.5)
    assert model.pair_invariant(2.0) / model.pair_invariant(1.0) == pytest.approx(2**-6)
    assert model.effective_exponent(1.0) == pytest.approx(6.0)
    assert model.equation_of_state(1.0) == pytest.approx(1.0)


def test_self_channel_scales_as_a_minus_three_and_is_dust_like():
    model = SpinCorrelationScaling(2.0, self_amplitude=3.0, pair_amplitude=0.0)
    assert model.self_invariant(2.0) / model.self_invariant(1.0) == pytest.approx(2**-3)
    assert model.effective_exponent(1.0) == pytest.approx(3.0)
    assert model.equation_of_state(1.0) == pytest.approx(0.0)


def test_pair_channel_needs_gamma_minus_three_for_dust_scaling():
    model = SpinCorrelationScaling(
        2.0, pair_amplitude=0.5, pair_correlation_exponent=-3.0
    )
    assert model.pair_invariant(2.0) / model.pair_invariant(1.0) == pytest.approx(2**-3)
    assert model.effective_exponent(1.0) == pytest.approx(3.0)
    assert model.equation_of_state(1.0) == pytest.approx(0.0)


def test_mixed_self_pair_sector_has_running_effective_equation_of_state():
    model = SpinCorrelationScaling(1.0, self_amplitude=1.0, pair_amplitude=1.0)
    assert model.equation_of_state(1.0) == pytest.approx(2 / 3)
    assert model.equation_of_state(2.0) != pytest.approx(model.equation_of_state(1.0))


def test_separate_continuity_is_satisfied():
    model = SpinCorrelationScaling(
        1.0, self_amplitude=0.3, pair_amplitude=0.7,
        pair_correlation_exponent=0.4,
    )
    for a in (0.1, 0.5, 1.0, 4.0, 20.0):
        assert model.continuity_residual_over_H(a) == pytest.approx(0.0, abs=1e-12)


@pytest.mark.parametrize("a", [0.0, -1.0, math.inf, math.nan])
def test_invalid_scale_factor_rejected(a):
    model = SpinCorrelationScaling(1.0)
    with pytest.raises(ValueError):
        model.spin_invariant(a)


def test_empty_spin_ensemble_has_zero_current_and_invariant():
    result = spin_current_decomposition([])
    assert result["total"] == 0.0
    assert result["self"] == 0.0
    assert result["pair"] == 0.0


def test_mismatched_weights_rejected():
    with pytest.raises(ValueError):
        spin_current_decomposition([(1, 0, 0)], [1, 2])
