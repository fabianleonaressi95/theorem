import numpy as np
import pytest

from audits.phonon_phason.coupled_ou_green_kubo import (
    green_kubo_blocks,
    sector_stress_correlations,
    simulate_ou,
    total_correlation,
)


def model():
    # Positive-definite coupled Hessian: the off-diagonal term couples u and w.
    stiffness = np.array([[2.0, 0.45], [0.45, 1.4]])
    stress = {
        "ph": np.array([[1.0, 0.0], [0.0, 0.0]]),
        "pha": np.array([[0.0, 0.0], [0.0, 0.8]]),
        "int": np.array([[0.0, 0.35], [0.35, 0.0]]),
    }
    return stiffness, stress


def test_exact_sector_correlations_are_reciprocal_at_zero_field():
    stiffness, stress = model()
    times = np.linspace(0.0, 8.0, 401)
    result = sector_stress_correlations(stiffness, stress, times)
    corr = result["correlation"]
    assert corr.shape == (401, 3, 3)
    assert np.allclose(corr, corr.transpose(0, 2, 1), atol=2e-12)
    assert np.all(np.isfinite(corr))


def test_total_stress_is_exact_sum_of_nine_ordered_blocks():
    stiffness, stress = model()
    times = np.linspace(0.0, 10.0, 501)
    corr = sector_stress_correlations(stiffness, stress, times)["correlation"]
    total_matrix = sum(stress.values())
    direct = sector_stress_correlations(
        stiffness, {"total": total_matrix}, times
    )["correlation"][:, 0, 0]
    assert np.allclose(total_correlation(corr), direct, atol=2e-12)


def test_green_kubo_integral_preserves_sector_block_sum():
    stiffness, stress = model()
    times = np.linspace(0.0, 20.0, 2001)
    corr = sector_stress_correlations(stiffness, stress, times)["correlation"]
    blocks = green_kubo_blocks(times, corr, kbt=1.0)
    total = green_kubo_blocks(times, total_correlation(corr)[:, None, None], kbt=1.0)
    assert blocks.shape == (3, 3)
    assert np.allclose(blocks.sum(), total[0, 0], atol=2e-10)
    assert np.allclose(blocks, blocks.T, atol=2e-10)


def test_exact_ou_simulation_reproduces_equilibrium_lag_zero_stress_covariance():
    stiffness, stress = model()
    times = np.array([0.0])
    exact = sector_stress_correlations(stiffness, stress, times)["correlation"][0]
    simulated = simulate_ou(
        stiffness, stress, dt=0.02, n_steps=180_000, seed=131
    )["lag0_correlation"]
    # Monte Carlo tolerance; this tests the stochastic sampler, not a material fit.
    assert np.allclose(simulated, exact, rtol=0.055, atol=0.012)


def test_rejects_unstable_hessian_and_bad_time_grid():
    _, stress = model()
    with pytest.raises(ValueError, match="positive definite"):
        sector_stress_correlations(np.array([[1.0, 2.0], [2.0, 1.0]]), stress, [0.0])
    with pytest.raises(ValueError, match="strictly increasing"):
        green_kubo_blocks([0.0, 1.0, 1.0], np.zeros((3, 2, 2)))
