from fractions import Fraction
import sympy as sp
import pytest
from src.t032_2i_molien import IRREP_DIMENSIONS, IRREP_NUMERATORS
from src.t032_2i_molien import IRREP_NUMERATORS
from src.t043_twisted_2i_rumin_torsion import tail_data
from src.t045_individual_rumin_zeta_poles import sector_residues
from src.t046_hadamard_finite_part_determinants import (
    alternating_constraint, finite_part_derivative, kappa_at_zero, residues,
)

@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_finite_part_residues_cancel(label):
    r=residues(label)
    assert r["zeta0"] == Fraction(IRREP_DIMENSIONS[label],960)
    assert r["zeta1"] == Fraction(IRREP_DIMENSIONS[label],480)
    assert -2*r["zeta0"]+r["zeta1"] == 0

@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_kappa_zero_is_exact_rational(label):
    cutoff, poly, finite, tails=tail_data(label)
    expected=2*(sum(finite.values(),Fraction(0))+
                sum((Fraction(c)*(Fraction(1,2)-Fraction(n,60))
                     for n,c in tails.items()),Fraction(0)))
    assert kappa_at_zero(label)==expected

def test_scale_dependent_hadamard_finite_part_formula():
    R=Fraction(1,7); C=Fraction(3,5); D=Fraction(11,13)
    L=sp.log(2)
    got=finite_part_derivative(C,D,R,L)
    assert sp.simplify(got-(D+2*C*L+2*R*L**2))==0

@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_alternating_determinant_constraint(label):
    data=alternating_constraint(label,log_mu=0,dps=40)
    assert data["residue_alternating"]=="0"
    assert data["kappa_zero_exact"] is not None
    assert data["identity"].startswith("D1_mu - 2*D0_mu")

@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_t045_residue_interface_consistent(label):
    a=sector_residues(label); b=residues(label)
    assert a["residue_zeta0"]==str(b["zeta0"])
    assert a["residue_zeta1"]==str(b["zeta1"])

@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_alternating_zeta_value_at_zero_vanishes(label):
    assert kappa_at_zero(label) == 0

@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_corrected_individual_residues_are_zero(label):
    r = residues(label)
    assert r["zeta0"] == Fraction(0)
    assert r["zeta1"] == Fraction(0)
    a = sector_residues(label)
    assert a["residue_zeta0"] == "0"
    assert a["residue_zeta1"] == "0"


@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_kappa_zero_is_exact_rational(label):
    cutoff, poly, finite, tails = tail_data(label)
    expected=2*(sum(finite.values(),Fraction(0))+
                sum((Fraction(c)*(Fraction(1,2)-Fraction(n,60))
                     for n,c in tails.items()),Fraction(0)))
    assert kappa_at_zero(label)==expected==0


def test_zero_residue_scaled_derivative_formula():
    C=sp.Rational(3,5); D=sp.Rational(11,13); L=sp.log(2)
    got=finite_part_derivative(C,D,Fraction(0),L)
    assert sp.simplify(got-(D+2*C*L))==0


@pytest.mark.parametrize("label", tuple(IRREP_NUMERATORS))
def test_alternating_derivative_constraint(label):
    data=alternating_constraint(label,log_mu=0,dps=40)
    assert data["residue_zeta0"]=="0"
    assert data["residue_zeta1"]=="0"
    assert data["residue_alternating"]=="0"
    assert data["kappa_zero_exact"]=="0"
    assert data["identity"].startswith("D1_mu - 2*D0_mu")
