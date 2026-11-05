"""Exact checks for T041 Barnes values and the partial Rumin torsion weight."""
from fractions import Fraction
import pytest
from src.t041_boundary_barnes_determinant import (
    audit, barnes_zeta2_at_zero, boundary_log_determinant_formula,
    boundary_zeta_at_zero, boundary_zeta_derivative_formula,
    weighted_rumin_boundary_contribution,
)


def test_barnes_double_zeta_zero_equal_periods_known_special_case():
    assert barnes_zeta2_at_zero(1, (1, 1)) == Fraction(-1, 12)
    assert barnes_zeta2_at_zero(2, (1, 1)) == Fraction(11, 12)


def test_exact_barnes_values_for_periods_12_20():
    assert barnes_zeta2_at_zero(2) == Fraction(226, 3)
    assert barnes_zeta2_at_zero(32) == Fraction(316, 3)
    assert boundary_zeta_at_zero() == Fraction(542, 3)


def test_exact_derivative_and_determinant_conventions():
    data = boundary_zeta_derivative_formula()
    assert data["zeta_at_zero"] == "542/3"
    assert data["log4_coefficient"] == "542/3"
    assert data["barnes_gamma_arguments"] == [2, 32]
    assert "2*log(Gamma2B" in data["derivative"]
    assert boundary_log_determinant_formula()["log_determinant"] == "-" + data["derivative"]


def test_both_exceptional_cases_enter_degree_one_with_positive_weight():
    data = weighted_rumin_boundary_contribution()
    assert data["case_VI"]["rumin_degree"] == 1
    assert data["case_VI"]["weight"] == 1
    assert data["case_VII"]["rumin_degree"] == 1
    assert data["case_VII"]["weight"] == 1
    assert data["partial_kappa"] == "2*Z_boundary(s)"
    assert data["partial_kappa_at_zero"] == str(Fraction(1084, 3))


def test_full_torsion_is_not_claimed():
    report = audit()
    assert report["passed"]
    assert len(report["remaining_open_terms"]) >= 4
    assert "not the complete quotient torsion" in report["weighted_contact_torsion"]["scope"]


@pytest.mark.parametrize("argument", [0, -1, 1.5, True])
def test_invalid_barnes_argument(argument):
    with pytest.raises(ValueError):
        barnes_zeta2_at_zero(argument)


def test_invalid_periods():
    with pytest.raises(ValueError):
        barnes_zeta2_at_zero(2, (12, 0))
