import math

import pytest

from src.rgs_q6_d5_schur_bessel_bridge import (
    q6_d5_bessel_gaussian_slice,
    q6_d5_exact_schur_complement,
)


def test_exact_schur_complement_and_determinant_factorization():
    result = q6_d5_exact_schur_complement(rank=3, split=1)
    assert result["determinant_identity_residual"] == 0
    assert all(result["exact_checks"].values())
    assert result["schur_complement"].is_symmetric()


def test_bessel_wilson_weights_are_compared_to_gaussian_on_finite_slice():
    result = q6_d5_bessel_gaussian_slice(beta=25.0, rank=2, cutoff=2)
    assert result["vectors_enumerated"] == 25
    assert result["wilson_bessel_slice_sum"] > 0
    assert result["gaussian_slice_sum"] > 0
    assert math.isfinite(result["max_pointwise_relative_error"])
    assert "complete rank-124 fibre sum" in result["scope"]["not_claimed"]


def test_gaussian_asymptotic_improves_at_large_beta_for_fixed_slice():
    low = q6_d5_bessel_gaussian_slice(beta=15.0, rank=1, cutoff=2)
    high = q6_d5_bessel_gaussian_slice(beta=150.0, rank=1, cutoff=2)
    assert high["max_pointwise_relative_error"] < low["max_pointwise_relative_error"]


@pytest.mark.parametrize("beta", [0.0, -1.0, float("nan")])
def test_bessel_gaussian_rejects_invalid_beta(beta):
    with pytest.raises(ValueError):
        q6_d5_bessel_gaussian_slice(beta=beta)
