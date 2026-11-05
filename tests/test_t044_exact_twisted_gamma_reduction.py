import sympy as sp
import pytest
from src.t044_exact_twisted_gamma_reduction import (
    EXPECTED, LABELS, exact_sector_value, gamma_reflection_data, verify_all,
)

def test_all_nine_exact_gamma_reductions():
    results = verify_all()
    assert set(results) == set(LABELS)
    assert all(item["exact_symbolic_residual"] == "0" for item in results.values())

@pytest.mark.parametrize("label", LABELS)
def test_sector_matches_exact_value(label):
    assert sp.simplify(exact_sector_value(label)-EXPECTED[label]) == 0

@pytest.mark.parametrize("label", LABELS[1:])
def test_nontrivial_sectors_have_no_pi_factor(label):
    data = gamma_reflection_data(label)
    assert data["pi_exponent"] == 0

@pytest.mark.parametrize("label", LABELS)
def test_reflection_pairs_are_exact(label):
    data = gamma_reflection_data(label)
    exponents = data["sine_exponents"]
    assert all(isinstance(k, int) and 1 <= k < 30 for k in exponents)

def test_regular_representation_product_is_exact():
    from src.t032_2i_molien import IRREP_DIMENSIONS
    product = sp.prod(EXPECTED[label]**IRREP_DIMENSIONS[label] for label in LABELS)
    assert sp.simplify(product-16*sp.pi**2) == 0
