import math

import pytest

from scripts.audit_t113_quasicrystal_phonon_gravity import (
    gravitational_mass,
    logarithmic_slope,
    audit,
)


def test_positive_sound_speed_density_slope_gives_negative_mass():
    mass = gravitational_mass(energy=2.0, sound_speed=4.0,
                              dlogc_dlogrho=0.5)
    assert mass == pytest.approx(-0.0625)


def test_negative_slope_gives_positive_mass():
    mass = gravitational_mass(energy=2.0, sound_speed=4.0,
                              dlogc_dlogrho=-0.5)
    assert mass == pytest.approx(0.0625)


def test_logarithmic_slope_power_law():
    alpha = 0.37
    c_of_rho = lambda rho: 7.0 * rho**alpha
    assert logarithmic_slope(2.0, c_of_rho) == pytest.approx(alpha, rel=1e-8)


def test_invalid_inputs():
    with pytest.raises(ValueError):
        gravitational_mass(1.0, 0.0, 0.2)
    with pytest.raises(ValueError):
        logarithmic_slope(-1.0, lambda rho: math.sqrt(rho))


def test_reference_audit():
    result = audit()
    assert result["slope_error"] < 1e-8
    assert result["mass_error"] < 1e-15
    assert result["negative_for_positive_slope"]
