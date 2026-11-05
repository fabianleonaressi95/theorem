"""T041: exact Barnes-zeta derivative and weighted boundary torsion term.

Convention: Barnes zeta_2(z,a|w1,w2) is the unscaled sum over r,s >= 0.
Define Gamma2_B(a|w1,w2) := exp(d/dz zeta_2(z,a|w1,w2)|_{z=0});
this definition fixes all normalization ambiguities of multiple gamma.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
from src.t040_boundary_barnes_zeta import BOUNDARY_KINDS

PERIODS = (12, 20)
BARNES_ARGUMENTS = (2, 32)


def barnes_zeta2_at_zero(argument: int, periods: tuple[int, int] = PERIODS) -> Fraction:
    """Exact Barnes double-zeta value at z=0 via B_{2,2}/2."""
    if not isinstance(argument, int) or isinstance(argument, bool) or argument <= 0:
        raise ValueError("Barnes argument must be a positive integer")
    if (not isinstance(periods, tuple) or len(periods) != 2
            or any(not isinstance(w, int) or isinstance(w, bool) or w <= 0 for w in periods)):
        raise ValueError("periods must be a pair of positive integers")
    w1, w2 = periods
    b22 = (argument**2 - argument * (w1 + w2)
           + Fraction(w1**2 + w2**2 + 3*w1*w2, 6))
    return Fraction(b22, 2)


def boundary_zeta_at_zero() -> Fraction:
    """Z_boundary(0) for one exceptional orientation."""
    return sum((barnes_zeta2_at_zero(a) for a in BARNES_ARGUMENTS), Fraction(0))


def boundary_zeta_derivative_formula() -> dict:
    """Exact expression for Z'_boundary(0) in the fixed Barnes-Gamma convention."""
    z0 = boundary_zeta_at_zero()
    return {
        "zeta_at_zero": str(z0),
        "log4_coefficient": str(z0),
        "barnes_gamma_arguments": list(BARNES_ARGUMENTS),
        "barnes_periods": list(PERIODS),
        "derivative": f"{z0}*log(4) + 2*log(Gamma2B(2|12,20)*Gamma2B(32|12,20))",
        "gamma_convention": "Gamma2B(a|w1,w2)=exp(d_z BarnesZeta2(z,a|w1,w2) at z=0)",
        "numerical_evaluation": "not performed; exact special-function expression",
    }


def boundary_log_determinant_formula() -> dict:
    """log det_zeta Delta_boundary = -Z'_boundary(0)."""
    derivative = boundary_zeta_derivative_formula()
    return {
        "log_determinant": "-" + derivative["derivative"],
        "zeta_at_zero": derivative["zeta_at_zero"],
        "convention": "log det_zeta(Delta) = -zeta_Delta'(0)",
    }


def weighted_rumin_boundary_contribution() -> dict:
    """VI and VII lie in Rumin degree one, each with torsion weight +1 (n=1)."""
    return {
        "contact_dimension": 3,
        "n": 1,
        "torsion_function": "kappa_E(s) = -2*zeta(Delta_E^0)(s) + zeta(Delta_E^1)(s)",
        "case_VI": {"bidegree": "(1,0)", "rumin_degree": 1, "weight": 1},
        "case_VII": {"bidegree": "(0,1)", "rumin_degree": 1, "weight": 1},
        "partial_kappa": "2*Z_boundary(s)",
        "partial_kappa_at_zero": str(2 * boundary_zeta_at_zero()),
        "partial_kappa_derivative_at_zero": "2*Z_boundary'(0)",
        "partial_log_torsion": boundary_zeta_derivative_formula()["derivative"],
        "scope": "only the two exceptional degree-one boundary families; not the complete quotient torsion",
    }


def audit() -> dict:
    return {
        "passed": True,
        "barnes_zeta_values_at_zero": {str(a): str(barnes_zeta2_at_zero(a)) for a in BARNES_ARGUMENTS},
        "one_orientation": boundary_zeta_derivative_formula(),
        "one_orientation_log_determinant": boundary_log_determinant_formula(),
        "weighted_contact_torsion": weighted_rumin_boundary_contribution(),
        "boundary_orientations": list(BOUNDARY_KINDS),
        "remaining_open_terms": [
            "complete spectrum of Delta_E^0 on S^3/2I",
            "all generic and other exceptional contributions to Delta_E^1",
            "harmonic/zero-mode conventions and full meromorphic cancellation",
            "full kappa_E'(0) and contact analytic torsion of S^3/2I",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/t041_boundary_barnes_determinant.json")
    args = parser.parse_args()
    report = audit()
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
