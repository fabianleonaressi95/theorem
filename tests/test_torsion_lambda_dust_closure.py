import math
import pytest

from scripts.torsion_lambda_dust_closure import TorsionLambdaModel


def test_dust_like_torsion_is_separately_conserved():
    model = TorsionLambdaModel(0.00005, 0.25, 0.2, 0.69995)
    for a in (0.2, 0.5, 1.0, 2.0, 5.0):
        assert model.p_torsion(a) == 0.0
        assert model.torsion_continuity_residual(a) == 0.0
        assert model.w_torsion(a) == 0.0


def test_flat_factory_uses_effective_matter_density():
    model = TorsionLambdaModel.flat(0.00005, 0.25, 0.2)
    assert model.lambda_ == pytest.approx(0.69995)
    assert model.e2(1.0) == pytest.approx(1.0, abs=1e-14)
    assert model.closure_residual() == pytest.approx(0.0, abs=1e-14)


def test_lambda_zero_boundary_solves_corrected_matter_density():
    model = TorsionLambdaModel.einstein_cartan_lambda_zero(0.45, 0.1)
    assert model.lambda_ == 0.0
    assert model.omega_m0 == pytest.approx(0.5)
    assert model.e2(1.0) == pytest.approx(1.0, abs=1e-14)


def test_generalized_friedmann_background_and_pressure():
    model = TorsionLambdaModel(0.1, 0.2, 0.5, 0.59)
    a = 2.0
    expected_e2 = 0.1 * a**-4 + 0.2 * 1.5 * a**-3 + 0.59
    assert model.e2(a) == pytest.approx(expected_e2)
    assert model.p_effective(a) == pytest.approx(0.1 * a**-4 / 3.0 - 0.59)


def test_gr_limit_beta_zero():
    model = TorsionLambdaModel.flat(0.00005, 0.3, 0.0)
    assert model.e2(1.0) == pytest.approx(1.0)
    assert model.rho_torsion(1.0) == 0.0
    assert model.e2(0.5) == pytest.approx(
        0.00005 * 0.5**-4 + 0.3 * 0.5**-3 + model.lambda_
    )


@pytest.mark.parametrize("a", [0.0, -1.0, math.inf, math.nan])
def test_invalid_scale_factor_rejected(a):
    model = TorsionLambdaModel(0.01, 0.2, 0.1, 0.7)
    with pytest.raises(ValueError):
        model.e2(a)


def test_invalid_beta_rejected():
    with pytest.raises(ValueError):
        TorsionLambdaModel(0.01, 0.2, -1.0, 0.79)
