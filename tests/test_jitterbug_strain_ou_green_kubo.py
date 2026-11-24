"""Regression tests for the strain-derived Jitterbug OU Green--Kubo audit."""
import numpy as np
from audits.jitterbug_strain_ou_green_kubo import audit


def test_strain_stress_and_ou_green_kubo_are_finite_on_ran_k():
    result = audit()
    assert result["dof"] == 36
    assert result["edges"] == 24
    assert result["rank_K"] == 24
    assert result["nullity_K"] == 12
    assert result["rigid_body_modes"] == 6
    assert result["internal_mechanisms"] == 6
    assert len(result["components"]) == 6
    for component in result["components"]:
        assert np.isfinite(component["GK_total_kBT_mu1"])
        assert component["GK_linear_kBT_over_mu"] >= -1e-10
        assert component["GK_quadratic_kBT2_over_mu"] >= -1e-10
        assert component["A_projected_frobenius_squared"] >= 0


def test_integrated_gk_tensors_are_positive_semidefinite():
    result = audit()
    for key in (
        "integrated_GK_linear_matrix_kBT_over_mu",
        "integrated_GK_quadratic_matrix_kBT2_over_mu",
        "integrated_GK_total_matrix_kBT_mu1",
    ):
        matrix = np.asarray(result[key], dtype=float)
        assert np.allclose(matrix, matrix.T, atol=1e-9)
        assert np.linalg.eigvalsh(matrix).min() >= -1e-8


def test_internal_mechanisms_are_not_mislabeled_as_phasons():
    result = audit()
    assert "not a material viscosity" in result["interpretation"]
    assert "physical phason" not in result["interpretation"]
