import numpy as np
import pytest

from audits.morphodynamics.q6_rgs_berry_cycle import (
    berry_holonomy, deformed_metric_hamiltonian,
)


def test_deformed_metric_hamiltonian_is_symmetric_positive():
    H = deformed_metric_hamiltonian(0.37, amplitude=0.02)
    assert H.shape == (64, 64)
    assert np.allclose(H, H.T, atol=1e-12)
    assert np.linalg.eigvalsh(H).min() > -1e-10
    assert np.linalg.norm(H @ np.ones(64)) < 1e-9


def test_berry_cycle_reports_only_isolated_eigenlines():
    # The constant ground state is exactly isolated but geometrically trivial.
    result = berry_holonomy(band_index=0, amplitude=0.02, steps=48)
    assert result["minimum_spectral_gap"] > 1e-9
    assert abs(result["berry_phase_radians"]) < 1e-7
    assert result["minimum_neighbor_overlap"] > 0.99


def test_berry_rejects_nonisolated_band():
    with pytest.raises(ValueError, match="not isolated"):
        berry_holonomy(band_index=1, amplitude=0.0, steps=32)
