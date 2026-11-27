import numpy as np
import pytest

from audits.morphodynamics.q6_rgs_berry_cycle import (
    berry_holonomy, deformed_metric_hamiltonian, wilson_phase,
)


def test_deformed_metric_hamiltonian_is_symmetric_positive():
    H = deformed_metric_hamiltonian(0.37, amplitude=0.02)
    assert H.shape == (64, 64)
    assert np.allclose(H, H.T, atol=1e-12)
    assert np.linalg.eigvalsh(H).min() > -1e-10
    assert np.linalg.norm(H @ np.ones(64)) < 1e-9


def test_ground_state_control_has_trivial_holonomy():
    result = berry_holonomy(band_index=0, amplitude=0.02, steps=48)
    assert result["minimum_spectral_gap"] > 1e-9
    assert abs(result["berry_phase_radians"]) < 1e-7
    assert result["minimum_neighbor_overlap"] > 0.99


def test_rgs_strain_cycle_has_pi_holonomy_for_isolated_band_eight():
    result = berry_holonomy(band_index=8, amplitude=0.04, steps=240)
    assert result["minimum_spectral_gap"] > 1e-4
    assert result["minimum_neighbor_overlap"] > 0.9
    assert abs(abs(result["berry_phase_radians"]) - np.pi) < 1e-7


def test_wilson_phase_is_invariant_under_independent_gauge_phases():
    rng = np.random.default_rng(20261127)
    theta = np.linspace(0, 2 * np.pi, 40, endpoint=False)
    vectors = [np.array([np.cos(t), np.sin(t)], dtype=complex) for t in theta]
    phase, _ = wilson_phase(vectors)
    gauged = [np.exp(1j * rng.uniform(-np.pi, np.pi)) * v for v in vectors]
    phase_gauged, _ = wilson_phase(gauged)
    assert abs(np.angle(np.exp(1j * (phase - phase_gauged)))) < 1e-12


def test_berry_rejects_nonisolated_band():
    with pytest.raises(ValueError, match="not isolated"):
        berry_holonomy(band_index=1, amplitude=0.0, steps=32)
