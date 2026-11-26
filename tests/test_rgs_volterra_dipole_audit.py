import pytest

from scripts.rgs_volterra_dipole_audit import profile_audit


@pytest.mark.parametrize("profile", ["gaussian", "sech2"])
def test_dipole_profile_has_zero_resultant_and_unit_burgers_moment(profile):
    result = profile_audit(profile, d_over_h=2.0, sigma_over_h=6.4)
    assert abs(result["zeroth_moment"]) < 1e-10
    assert abs(result["first_moment"] - 1.0) < 2e-4


@pytest.mark.parametrize("profile", ["gaussian", "sech2"])
def test_dipole_profile_converges_to_edge_derivative_at_second_order(profile):
    errors = [
        profile_audit(profile, d_over_h=d, sigma_over_h=64.0)["relative_L2_error"]
        for d in (8.0, 4.0, 2.0, 1.0)
    ]
    # Halving d/sigma should reduce the leading O((d/sigma)^2) error
    # by approximately four once in the asymptotic regime.
    assert errors[1] < errors[0] / 3.5
    assert errors[2] < errors[1] / 3.5
    assert errors[3] < errors[2] / 3.5


def test_grid_alignment_is_not_a_continuum_special_case():
    aligned = profile_audit("gaussian", d_over_h=2.0, sigma_over_h=3.2)
    non_aligned = profile_audit("gaussian", d_over_h=2.5, sigma_over_h=3.2)
    assert aligned["relative_L2_error"] > 0
    assert non_aligned["relative_L2_error"] > 0
    assert aligned["relative_L2_error"] != pytest.approx(
        non_aligned["relative_L2_error"], rel=1e-3
    )
