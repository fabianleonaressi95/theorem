import mpmath as mp
import pytest
from src.t032_2i_molien import IRREP_DIMENSIONS, verify_dimension_decomposition, verify_sum_of_squares
from src.t043_twisted_2i_rumin_torsion import (
    LABELS, audit, difference_polynomial, eigenvalue, kappa_boundary_partial,
    kappa_direct_partial, log_torsion, multiplicities, verify_sector,
)

def test_nine_irreducibles_and_dimension_sum():
    assert len(LABELS) == 9
    assert verify_sum_of_squares()
    assert sum(d*d for d in IRREP_DIMENSIONS.values()) == 120
    assert verify_dimension_decomposition(120)

def test_spectral_eigenvalue_specialization():
    assert eigenvalue(12, 0) == 36
    assert eigenvalue(12, 13) == 49
    assert eigenvalue(0, 1) == 1
    with pytest.raises(ValueError):
        eigenvalue(2, 4)

@pytest.mark.parametrize("label", LABELS)
def test_exact_periodic_difference_polynomial(label):
    P = difference_polynomial(label)
    assert P
    assert verify_sector(label)

@pytest.mark.parametrize("label", LABELS)
@pytest.mark.parametrize("s", [1.25, 2.0])
def test_twisted_alternating_cancellation(label, s):
    with mp.workdps(60):
        direct = kappa_direct_partial(label, mp.mpf(s), 35)
        boundary = kappa_boundary_partial(label, mp.mpf(s), 35)
        assert abs(direct-boundary) < mp.mpf("1e-50")

def test_trivial_sector_reproduces_t042():
    with mp.workdps(50):
        assert abs(log_torsion("1", 50) - mp.log(2*mp.pi**2/15)) < mp.mpf("1e-45")

def test_nontrivial_sector_algebraic_values_numerically():
    with mp.workdps(50):
        expected = {
            "2": (3-mp.sqrt(5))/4,
            "2'": (3+mp.sqrt(5))/4,
            "3": (5-mp.sqrt(5))/5,
            "3'": (5+mp.sqrt(5))/5,
            "4": mp.mpf(5)/3,
            "4'": mp.mpf(1),
            "5": mp.mpf(3)/2,
            "6": mp.mpf(2),
        }
        for label, value in expected.items():
            assert abs(mp.exp(log_torsion(label,50))-value) < mp.mpf("1e-45")

def test_regular_representation_weighted_product():
    with mp.workdps(50):
        report = audit(70, 50)
        got = mp.mpf(report["regular_representation_check"]["weighted_torsion"])
        assert abs(got-16*mp.pi**2) < mp.mpf("1e-40")
