import numpy as np
import pytest

from audits.phonon_phason.normal_modes_kubo import (
    generalized_normal_modes,
    green_kubo_stress,
    polarization_weights,
)


def test_generalized_modes_are_mass_normalized_and_solve_eigenproblem():
    k = np.array([[4.0, -1.0], [-1.0, 3.0]])
    m = np.diag([2.0, 1.0])
    values, modes, stable = generalized_normal_modes(k, m)
    assert np.all(stable)
    assert np.allclose(modes.T @ m @ modes, np.eye(2), atol=1e-12)
    assert np.allclose(k @ modes, m @ modes @ np.diag(values), atol=1e-11)


def test_negative_mode_is_reported_as_unstable_not_relabelled():
    values, _, stable = generalized_normal_modes(np.diag([-1.0, 2.0]), np.eye(2))
    assert values[0] == pytest.approx(-1.0)
    assert not stable[0]
    assert stable[1]


def test_generalized_modes_reject_nonpositive_mass():
    with pytest.raises(ValueError, match="positive definite"):
        generalized_normal_modes(np.eye(2), np.diag([1.0, 0.0]))


def test_polarization_weights_distinguish_longitudinal_and_transverse():
    longitudinal = polarization_weights(np.array([[1.0, 0.0], [2.0, 0.0]]), [1.0, 0.0])
    transverse = polarization_weights(np.array([[0.0, 1.0], [0.0, -2.0]]), [1.0, 0.0])
    assert longitudinal["longitudinal"] == pytest.approx(1.0)
    assert longitudinal["transverse"] == pytest.approx(0.0)
    assert transverse["longitudinal"] == pytest.approx(0.0)
    assert transverse["transverse"] == pytest.approx(1.0)


def test_green_kubo_scalar_is_centered_and_finite_window():
    stress = np.array([0.0, 1.0, 0.0, -1.0, 0.0])
    result = green_kubo_stress(stress, dt=0.1, temperature=300.0, volume=2.0,
                               max_lag=2)
    assert result["correlation"].shape == (3,)
    assert np.isfinite(result["integral"])
    assert np.isfinite(result["viscosity"])
    assert result["max_lag"] == 2


def test_green_kubo_tensor_shape_and_validation():
    stress = np.column_stack(([0., 1., 0., -1.], [1., 0., -1., 0.]))
    result = green_kubo_stress(stress, dt=0.2, temperature=2.0, volume=3.0,
                               max_lag=2)
    assert result["correlation"].shape == (3, 2, 2)
    assert result["viscosity"].shape == (2, 2)
    with pytest.raises(ValueError):
        green_kubo_stress(stress, dt=0.0, temperature=2.0, volume=3.0)
