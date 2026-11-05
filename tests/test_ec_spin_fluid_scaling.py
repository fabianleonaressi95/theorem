import math
import pytest

from scripts.ec_spin_fluid_scaling import WeyssenhoffScaling


def test_number_density_scales_as_a_minus_three():
    model = WeyssenhoffScaling(10.0, 2.0, 0.5)
    assert model.number_density(2.0) == pytest.approx(10.0 / 8.0)


def test_spin_invariant_scales_as_a_minus_six():
    model = WeyssenhoffScaling(10.0, 2.0, 0.5)
    assert model.spin_invariant(2.0) == pytest.approx(2.0 / 64.0)
    assert model.spin_invariant(3.0) / model.spin_invariant(1.0) == pytest.approx(3.0**-6)


def test_effective_spin_sector_is_negative_stiff_fluid():
    model = WeyssenhoffScaling(1.0, 4.0, 0.25)
    for a in (0.2, 0.5, 1.0, 2.0, 5.0):
        rho = model.rho_spin_effective(a)
        assert rho < 0
        assert model.p_spin_effective(a) == pytest.approx(rho)
        assert model.equation_of_state(a) == pytest.approx(1.0)


def test_spin_sector_continuity_identity():
    model = WeyssenhoffScaling(1.0, 4.0, 0.25)
    for a in (0.1, 0.5, 1.0, 10.0):
        assert model.continuity_residual_over_H(a) == pytest.approx(0.0, abs=1e-12)


def test_ec_spin_term_cannot_equal_dust_term_over_an_interval():
    model = WeyssenhoffScaling(1.0, 4.0, 0.25)
    r1 = model.dust_identification_ratio(1.0, 0.2)
    r2 = model.dust_identification_ratio(2.0, 0.2)
    assert r2 / r1 == pytest.approx(2.0**-3)
    assert not math.isclose(r1, r2)


@pytest.mark.parametrize("a", [0.0, -1.0, math.inf, math.nan])
def test_invalid_scale_factor_rejected(a):
    model = WeyssenhoffScaling(1.0, 1.0, 1.0)
    with pytest.raises(ValueError):
        model.spin_invariant(a)


def test_zero_spin_has_no_effective_correction():
    model = WeyssenhoffScaling(1.0, 0.0, 1.0)
    assert model.rho_spin_effective(1.0) == 0.0
    with pytest.raises(ZeroDivisionError):
        model.equation_of_state(1.0)
