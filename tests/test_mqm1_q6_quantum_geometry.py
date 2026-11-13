import numpy as np
import pytest

from audits.morphodynamics.q6_quantum_geometry import (
    coupled_rhs,
    energy_dissipation_rate,
    geometry_gradient,
    hamiltonian,
    joint_energy,
    q6_incidence,
)


def sample():
    rng = np.random.default_rng(20261113)
    x = rng.normal(scale=0.08, size=192)
    x0 = np.zeros(192)
    z = rng.normal(size=64) + 1j * rng.normal(size=64)
    psi = z / np.linalg.norm(z)
    return x, psi, x0


def test_q6_incidence_has_expected_counts_and_rank():
    b = q6_incidence()
    assert b.shape == (64, 192)
    assert np.allclose(b.sum(axis=0), 0.0)
    assert np.linalg.matrix_rank(b) == 63


def test_weighted_hamiltonian_is_hermitian_positive_and_has_constant_kernel():
    x, _, _ = sample()
    h = hamiltonian(x, coupling=1.7)
    assert np.allclose(h, h.T.conj(), atol=1e-12)
    assert np.linalg.eigvalsh(h)[0] > -1e-10
    assert np.linalg.norm(h @ np.ones(64)) < 1e-10


def test_geometry_gradient_matches_centered_finite_difference():
    x, psi, x0 = sample()
    grad = geometry_gradient(x, psi, x0, stiffness=1.3, coupling=0.7)
    rng = np.random.default_rng(17)
    direction = rng.normal(size=192)
    direction /= np.linalg.norm(direction)
    eps = 1e-6
    plus = joint_energy(x + eps * direction, psi, x0, stiffness=1.3, coupling=0.7)
    minus = joint_energy(x - eps * direction, psi, x0, stiffness=1.3, coupling=0.7)
    numerical = (plus - minus) / (2 * eps)
    assert numerical == pytest.approx(float(grad @ direction), rel=2e-7, abs=2e-8)


def test_rhs_preserves_quantum_norm_differentially_and_dissipates_energy():
    x, psi, x0 = sample()
    xdot, psidot = coupled_rhs(
        x, psi, x0, stiffness=1.2, coupling=0.8, mobility=0.3, hbar=1.1
    )
    norm_rate = 2 * np.real(np.vdot(psi, psidot))
    assert norm_rate == pytest.approx(0.0, abs=1e-12)
    predicted = energy_dissipation_rate(
        x, psi, x0, stiffness=1.2, coupling=0.8, mobility=0.3
    )
    assert predicted <= 0.0
    assert predicted == pytest.approx(-float(xdot @ xdot) / 0.3, abs=1e-11)


def test_joint_energy_is_nonnegative_for_normalized_states():
    x, psi, x0 = sample()
    assert joint_energy(x, psi, x0, stiffness=1.0, coupling=1.0) >= 0.0


def test_rejects_non_normalized_state_and_invalid_parameters():
    x, psi, x0 = sample()
    with pytest.raises(ValueError, match="unit norm"):
        coupled_rhs(x, 2 * psi, x0)
    with pytest.raises(ValueError, match="positive"):
        hamiltonian(x, coupling=0.0)
