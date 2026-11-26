import pytest

from scripts.rgs_volterra_elastic_limit import solve_pair


@pytest.mark.parametrize("n", [64, 96])
def test_matched_volterra_sources_have_small_airy_residuals(n):
    result = solve_pair(n, d_over_h=2.0, sigma_over_h=4.0)
    assert result["dipole_airy_residual"] < 1e-10
    assert result["edge_airy_residual"] < 1e-10
    assert abs(result["dipole_source_mean"]) < 1e-14
    assert abs(result["edge_source_mean"]) < 1e-14


def test_stress_and_energy_converge_in_small_separation_limit():
    # Keep n and sigma/h fixed; reduce d/sigma without changing the core.
    coarse = solve_pair(128, d_over_h=2.0, sigma_over_h=8.0)
    fine = solve_pair(128, d_over_h=0.5, sigma_over_h=8.0)
    assert fine["relative_stress_l2_difference"] < coarse["relative_stress_l2_difference"]
    assert fine["relative_strain_l2_difference"] < coarse["relative_strain_l2_difference"]
    assert fine["relative_energy_difference"] < coarse["relative_energy_difference"]


def test_burgers_magnitude_is_frank_times_separation():
    result = solve_pair(96, d_over_h=2.0, sigma_over_h=4.0)
    assert result["burgers_magnitude"] == pytest.approx(
        result["frank_magnitude"] * result["d_over_h"] * result["h"]
    )
