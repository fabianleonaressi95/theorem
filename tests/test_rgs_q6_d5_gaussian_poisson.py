import math

import pytest
import sympy as sp

from src.rgs_q6_d5_gaussian_poisson import (
    q6_d5_fiber_gaussian_gram,
    q6_d5_gaussian_poisson_crosscheck,
)


def test_q6_d5_fiber_slice_gram_is_exact_positive_definite():
    data = q6_d5_fiber_gaussian_gram(rank=2)
    gram = data["gram"]
    assert gram.shape == (2, 2)
    assert gram == gram.T
    assert gram.det() > 0
    assert gram * data["gram_inverse"] == sp.eye(2)
    assert data["exact_positive_definite"]


def test_gaussian_poisson_direct_and_dual_enclosures_overlap():
    result = q6_d5_gaussian_poisson_crosscheck(rank=2, t=1.0, cutoff=5)
    assert result["rank"] == 2
    assert result["full_fiber_rank"] == 124
    assert result["enclosures_overlap"], result
    assert all(math.isfinite(x) and x >= 0 for x in (
        result["direct_partial_sum"],
        result["direct_tail_envelope"],
        result["dual_partial_sum_with_prefactor"],
        result["dual_tail_envelope_with_prefactor"],
    ))
    assert "full rank-124 Gaussian theta sum evaluated" in result["scope"]["not_claimed"]


def test_invalid_gaussian_poisson_parameters_are_rejected():
    with pytest.raises(ValueError):
        q6_d5_gaussian_poisson_crosscheck(rank=0)
    with pytest.raises(ValueError):
        q6_d5_gaussian_poisson_crosscheck(rank=2, t=0.0)
    with pytest.raises(ValueError):
        q6_d5_gaussian_poisson_crosscheck(rank=2, cutoff=-1)
