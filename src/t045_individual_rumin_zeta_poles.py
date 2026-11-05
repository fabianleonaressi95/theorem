"""T045-R1: corrected local meromorphic audit of the separate Rumin zeta functions.

The previous T045 residue calculation assigned singular contributions to the
wrong binomial indices.  With the stated Hurwitz expansion, the only possible
simple pole comes from k=1 and is proportional to sum_r(beta_r-alpha_r).
The exact Molien moment identity makes this sum zero in every 2I sector.
"""
from __future__ import annotations
from fractions import Fraction
import sympy as sp
from src.t032_2i_molien import IRREP_DIMENSIONS, IRREP_NUMERATORS, molien_coefficients

PERIOD_M = 60
PERIOD_ODD = 120
ODD_RESIDUES = tuple(range(1, PERIOD_ODD, 2))


def _molien_rational_function(label):
    t = sp.symbols("t")
    numerator = sum(t**j for j in IRREP_NUMERATORS[label])
    return t, numerator / ((1-t**12)*(1-t**20))


def quasipolynomial_data(label, verify_steps=4):
    """Return exact b_(m,r)=alpha_r*m+beta_r beyond a certified cutoff."""
    if label not in IRREP_DIMENSIONS:
        raise KeyError(label)
    t, A = _molien_rational_function(label)
    Q = sp.cancel((1-t**PERIOD_M)**2 * A)
    Qpoly = sp.Poly(Q, t)
    if Qpoly.is_zero or any(not c.is_Integer for c in Qpoly.all_coeffs()):
        raise AssertionError("Molien denominator did not yield an integer polynomial")
    cutoff = int(Qpoly.degree()) + 1
    coeff = molien_coefficients(label, cutoff + (verify_steps+3)*PERIOD_M)
    alpha, beta, starts = {}, {}, {}
    for r in range(PERIOD_M):
        m = cutoff + (r-cutoff) % PERIOD_M
        a = Fraction(coeff[m+PERIOD_M]-coeff[m], PERIOD_M)
        b = Fraction(coeff[m])-a*m
        alpha[r], beta[r], starts[r] = a, b, m
        for j in range(verify_steps+1):
            n = m+j*PERIOD_M
            if Fraction(coeff[n]) != a*n+b:
                raise AssertionError(f"quasi-polynomial check failed: {label}, m={n}")
    return {
        "cutoff": cutoff, "polynomial_degree": int(Qpoly.degree()),
        "alpha": alpha, "beta": beta, "starts": starts,
        "sum_alpha": sum(alpha.values(), Fraction(0)),
        "sum_beta": sum(beta.values(), Fraction(0)),
    }


def hurwitz_odd_progression(residue, z):
    """Sum n^(-z) over n>=3 odd and n=residue (mod 120)."""
    if residue not in ODD_RESIDUES:
        raise ValueError("residue must be an odd class modulo 120")
    first = residue if residue >= 3 else residue + PERIOD_ODD
    return sp.Integer(PERIOD_ODD)**(-z) * sp.zeta(z, sp.Rational(first, PERIOD_ODD))


def interior_hurwitz_expansion(label):
    """Return the exact Hurwitz-series specification and correct pole ledger."""
    data = quasipolynomial_data(label)
    return {
        "cutoff": data["cutoff"],
        "period_in_m": PERIOD_M,
        "odd_variable_period": PERIOD_ODD,
        "odd_residues": list(ODD_RESIDUES),
        "m_residue": "r=((A+B-2)/2) mod 60",
        "weight": "alpha_r*(a+b)/2 + beta_r-alpha_r",
        "base_change": "Lambda=(ab-1)^2/16, a=2p+1, b=2q+1",
        "binomial": "(ab-1)^(-2s)=(ab)^(-2s)*sum_{k>=0}(2s)_k/(k!*(ab)^k)",
        "hurwitz_progression": "U_A(z)=120^(-z)*zeta_H(z,a_A/120)",
        "double_series": (
            "H_finite(s)+16^s*sum_k (2s)_k/k!*sum_(A,B)["
            "alpha_r/2*(U_A(2s+k-1)U_B(2s+k)+U_A(2s+k)U_B(2s+k-1))"
            "+(beta_r-alpha_r)*U_A(2s+k)U_B(2s+k)]"
        ),
        "pole_terms": {
            "k1_beta_minus_alpha": (
                "the only possible simple pole: (2s)_1*(beta-alpha)*"
                "U_A(1+2s)*U_B(1+2s); total residue=sum(beta-alpha)/480"
            ),
            "k1_alpha_terms": "at most one Hurwitz pole, killed by (2s)_1=O(s)",
            "k_ge_2": "at most one Hurwitz pole in alpha terms and none in beta terms; (2s)_k=O(s)",
            "k0": "Hurwitz arguments are 0; regular at s=0",
        },
        "uniformity": "a,b>=3 gives 1/(ab)<=1/9; the binomial tail is locally uniformly geometric near s=0",
    }


def sector_residues(label):
    data = quasipolynomial_data(label)
    d = IRREP_DIMENSIONS[label]
    expected_sum = Fraction(d, 2)
    if data["sum_alpha"] != expected_sum or data["sum_beta"] != expected_sum:
        raise AssertionError(f"Molien moment identity failed in sector {label}")
    residue = (data["sum_beta"]-data["sum_alpha"])/480
    if residue != 0:
        raise AssertionError(f"individual zeta residue did not cancel in sector {label}")
    return {
        "dimension": d, "cutoff": data["cutoff"],
        "sum_alpha": str(data["sum_alpha"]), "sum_beta": str(data["sum_beta"]),
        "sum_beta_minus_alpha": str(data["sum_beta"]-data["sum_alpha"]),
        "residue_interior_H": str(residue),
        "residue_zeta0": str(residue), "residue_zeta1": str(2*residue),
        "residue_kappa": str(-2*residue+2*residue),
    }


def audit():
    sectors = {label: sector_residues(label) for label in IRREP_NUMERATORS}
    return {
        "task": "T045-R1",
        "passed": True,
        "individual_zeta_status": "regular at s=0 under the stated Hurwitz continuation",
        "residue_formulas": {
            "Res_zeta0_rho_at_0": "0",
            "Res_zeta1_rho_at_0": "0",
            "Res_minus2zeta0_plus_zeta1": "0",
        },
        "sectors": sectors,
        "analytic_method": {
            "interior_indices": "p,q>=1",
            "odd_substitution": "a=2p+1,b=2q+1",
            "eigenvalue": "Lambda=(ab-1)^2/16",
            "eventual_multiplicity": "b_(m,rho)=alpha_(m mod 60)*m+beta_(m mod 60)",
            "periodicity_proof": "(1-t^60)^2*A_rho(t) is a polynomial",
            "hurwitz_progressions": "U_A(z)=120^(-z)*zeta_H(z,a_A/120)",
            "only_candidate_pole": "k=1 beta-alpha double-Hurwitz term",
            "candidate_residue": "sum_r(beta_r-alpha_r)/480=0",
            "boundary_terms": "B_rho and C_rho are regular at zero",
            "uniform_expansion_region": "a,b>=3 implies 1/(ab)<=1/9",
        },
        "status": {
            "proved_exact": [
                "eventual affine quasi-polynomial multiplicities in all nine sectors",
                "sum(alpha)=sum(beta)=dim(rho)/2",
                "cancellation of the only candidate Hurwitz residue in all nine sectors",
                "regularity at zero of the two separate degree zeta functions, subject to the stated locally uniform continuation",
            ],
            "not_yet_computed": [
                "individual Laurent constants C_0 and C_1",
                "individual derivatives D_0 and D_1",
                "individual zeta determinant values",
            ],
        },
    }


if __name__ == "__main__":
    import json
    print(json.dumps(audit(), indent=2))
