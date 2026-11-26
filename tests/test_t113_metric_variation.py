import numpy as np
import pytest

from scripts.audit_t113_metric_variation import (
    coupled_sectors,
    generalized_modes,
    hellmann_feynman,
    lapse_variation_energy,
    logarithmic_sensitivity,
    power_law_sector,
    audit,
)


@pytest.mark.parametrize("alpha", [0.25, 0.20, -0.10])
def test_scalar_fluid_and_solid_sensitivity(alpha):
    result = logarithmic_sensitivity(power_law_sector(alpha))
    assert result["candidate_log_speed_slope"][0] == pytest.approx(alpha, abs=1e-8)
    assert result["max_hf_fd_error"] < 1e-7


def test_r_zero_separates_phonon_and_phason_sectors():
    K, M = coupled_sectors(0.2, -0.1, 0.0)(1.0)
    values, _ = generalized_modes(K, M)
    assert values == pytest.approx([0.7, 1.5])
    result = logarithmic_sensitivity(coupled_sectors(0.2, -0.1, 0.0))
    assert result["candidate_log_speed_slope"] == pytest.approx([-0.1, 0.2], abs=1e-8)


def test_nonzero_coupling_preserves_hf_identity_and_positive_modes():
    result = logarithmic_sensitivity(coupled_sectors(0.2, -0.1, 0.2))
    assert min(result["omega_squared"]) > 0
    assert result["max_hf_fd_error"] < 1e-7


def test_hellmann_feynman_generalized_eigenvalue():
    K = np.diag([4.0, 9.0])
    M = np.diag([2.0, 3.0])
    dK = np.diag([1.0, 2.0])
    dM = np.diag([0.5, 0.25])
    assert hellmann_feynman(K, M, dK, dM, 0) == pytest.approx(0.0)


def test_lapse_variation_gives_quadratic_hamiltonian():
    q = np.array([0.3, -0.2])
    velocity = np.array([0.4, 0.1])
    M = np.diag([2.0, 1.5])
    K = np.array([[3.0, 0.2], [0.2, 2.0]])
    energy = lapse_variation_energy(q, velocity, M, K)
    eps = 1e-6
    L = lambda N: (velocity @ M @ velocity)/(2*N) - N*(q @ K @ q)/2
    assert energy == pytest.approx(-(L(1+eps)-L(1-eps))/(2*eps), abs=1e-9)


def test_audit_explicitly_does_not_claim_gravitational_mass():
    result = audit()
    assert result["acceptance"]["all_hf_fd_errors_below_1e-7"]
    assert "not identified" in result["scope_limit"]
