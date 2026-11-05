from fractions import Fraction
import pytest
from src.t032_2i_molien import IRREP_DIMENSIONS, IRREP_NUMERATORS
from src.t045_individual_rumin_zeta_poles import (
    ODD_RESIDUES, hurwitz_odd_progression, interior_hurwitz_expansion,
    quasipolynomial_data, sector_residues,
)

@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_affine_quasipolynomial_molien_tail(label):
    data = quasipolynomial_data(label, verify_steps=5)
    assert data["sum_alpha"] == Fraction(IRREP_DIMENSIONS[label], 2)
    assert data["sum_beta"] == Fraction(IRREP_DIMENSIONS[label], 2)

@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_individual_zeta_residues(label):
    d = IRREP_DIMENSIONS[label]
    result = sector_residues(label)
    assert result["residue_interior_H"] == str(Fraction(d, 2560))
    assert result["residue_zeta0"] == str(Fraction(d, 2560))
    assert result["residue_zeta1"] == str(Fraction(d, 1280))
    assert result["residue_kappa"] == "0"

def test_odd_residue_classes_are_all_present():
    assert len(ODD_RESIDUES) == 60
    assert ODD_RESIDUES[0] == 1 and ODD_RESIDUES[-1] == 119

def test_hurwitz_progression_formula():
    import sympy as sp
    z = sp.symbols("z")
    expr = hurwitz_odd_progression(1, z)
    expected = 120**(-z)*sp.zeta(z, sp.Rational(121,120))
    assert sp.simplify(expr-expected) == 0

@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_hurwitz_expansion_contains_only_expected_double_poles(label):
    spec = interior_hurwitz_expansion(label)
    assert "k2_beta" in spec["pole_terms"]
    assert "k3_alpha" in spec["pole_terms"]
    assert spec["odd_variable_period"] == 120
