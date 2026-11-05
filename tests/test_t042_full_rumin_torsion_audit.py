import mpmath as mp
import pytest
from src.t042_full_rumin_torsion_audit import (
    D_SUPPORT, audit, finite_hurwitz_data, gamma_log_torsion, gamma_torsion,
    invariant_multiplicities, kappa_boundary_partial, kappa_direct_partial,
    rumin_eigenvalue, verify_generating_function_identity, verify_period_60,
)

def test_exact_boundary_eigenvalues():
    assert rumin_eigenvalue(12, 0) == 36
    assert rumin_eigenvalue(12, 13) == 49
    assert rumin_eigenvalue(0, 1) == 1
    with pytest.raises(ValueError):
        rumin_eigenvalue(2, 4)

def test_molien_invariants():
    a = invariant_multiplicities(80)
    assert a[0] == 1
    assert [m for m in range(1, 31) if a[m]] == [12, 20, 24, 30]
    assert (a[60], a[72], a[80]) == (2, 2, 2)

@pytest.mark.parametrize("s", [1.25, 2.0])
def test_spectral_cancellation(s):
    with mp.workdps(60):
        assert abs(kappa_direct_partial(s, 80) - kappa_boundary_partial(s, 80)) < mp.mpf("1e-55")

def test_generating_function():
    assert verify_generating_function_identity()

def test_periodicity():
    assert verify_period_60(600)

def test_hurwitz_coefficients():
    data = finite_hurwitz_data()
    assert data["sum_d"] == -1
    assert data["hurwitz_zero_moment"] == "0"
    assert len(D_SUPPORT) == 16

def test_gamma_volume_identity():
    with mp.workdps(60):
        assert abs(gamma_torsion(60) - 2 * mp.pi**2 / 15) < mp.mpf("1e-55")
        assert abs(gamma_log_torsion(60) - mp.log(2 * mp.pi**2 / 15)) < mp.mpf("1e-55")

def test_audit_scope():
    report = audit(80, 40)
    assert report["passed"]
    assert report["torsion"]["exact_target"] == "2*pi^2/15"


def test_exact_sine_product_identity():
    import sympy as sp
    ratio = (sp.sin(sp.pi/5)*sp.sin(sp.pi/3)*sp.sin(2*sp.pi/5) /
             (sp.sin(sp.pi/30)*sp.sin(7*sp.pi/30)*sp.sin(11*sp.pi/30)*sp.sin(13*sp.pi/30)))
    assert sp.simplify(ratio**2 - 60) == 0
