"""T044: exact reduction of T043 Barnes/Hurwitz Gamma products.

Only exact rational arithmetic and SymPy's exact cyclotomic/trigonometric
simplifier are used.  The T043 spectral input is imported unchanged.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp
from src.t043_twisted_2i_rumin_torsion import LABELS, tail_data

PERIOD = 60
SQ5 = sp.sqrt(5)
EXPECTED = {
    "1": 2*sp.pi**2/15,
    "2": (3-SQ5)/4,
    "2'": (3+SQ5)/4,
    "3": 1-SQ5/5,
    "3'": 1+SQ5/5,
    "4": sp.Rational(5,3),
    "4'": sp.Integer(1),
    "5": sp.Rational(3,2),
    "6": sp.Integer(2),
}


def _pow(base, exponent):
    """Exact rational base to an exact rational exponent."""
    return sp.Pow(sp.Rational(base), sp.Rational(exponent))


def gamma_reflection_data(label):
    """Return exact prefactor, pi exponent and sine exponents.

    Starting from T043's finite Hurwitz derivative, use
      Gamma(q+r/60) = (prod_{j=0}^{q-1}(r/60+j))*Gamma(r/60),
    then pair r with 60-r using Euler reflection.  The returned identity is
      T_rho = prefactor * pi**pi_exponent *
              prod_{1<=r<30} sin(pi*r/60)**sine_exponent[r].
    """
    cutoff, _poly, finite, tails = tail_data(label)
    prefactor = sp.Integer(1)
    pi_exponent = sp.Integer(0)
    residues = {}

    # Finite Dirichlet terms in the T043 log-Gamma formula.
    for n, d in finite.items():
        prefactor *= _pow(4, d) * _pow(n, -2*d)

    # Hurwitz tail: recurrence to arguments in (0,1], and the
    # (4/60^2)^(e*(1/2-n/60)) (2*pi)^(-e) factors.
    for n, e in tails.items():
        x = sp.Rational(n, PERIOD)
        a = sp.Rational(1, 2) - x
        prefactor *= _pow(4, e*a) * _pow(PERIOD, -2*e*a)
        r = n % PERIOD or PERIOD
        q = (n-r)//PERIOD
        recurrence = sp.prod(sp.Rational(r, PERIOD)+j for j in range(q))
        prefactor *= _pow(recurrence, 2*e)
        prefactor *= _pow(2, -e)
        pi_exponent -= e
        if r in residues:
            raise AssertionError(f"duplicate residue {r} in sector {label}")
        residues[r] = e

    sine_exponents = {}
    for r in range(1, 30):
        left, right = residues.get(r, 0), residues.get(PERIOD-r, 0)
        if left != right:
            raise AssertionError(
                f"reflection pairing fails for {label}, residues {r}/{PERIOD-r}: "
                f"{left} != {right}"
            )
        if left:
            # Gamma(r/60) Gamma(1-r/60) = pi/sin(pi*r/60).
            pi_exponent += 2*left
            sine_exponents[r] = -2*left

    # Self-complementary argument 1/2: Gamma(1/2)^2 = pi.
    middle = residues.get(30, 0)
    if middle:
        pi_exponent += middle

    # Residue 60 is Gamma(1)=1; its (2*pi)^(-e) factor remains.
    expression = prefactor * sp.pi**pi_exponent
    for r, exponent in sine_exponents.items():
        expression *= sp.sin(sp.pi*r/PERIOD)**exponent
    expression = sp.factor(sp.simplify(expression))
    return {
        "cutoff": cutoff,
        "prefactor": sp.factor(sp.simplify(prefactor)),
        "pi_exponent": int(pi_exponent),
        "sine_exponents": sine_exponents,
        "expression": expression,
    }


def exact_sector_value(label):
    data = gamma_reflection_data(label)
    return sp.simplify(data["expression"])


def verify_all():
    results = {}
    for label in LABELS:
        data = gamma_reflection_data(label)
        reduced = sp.simplify(data["expression"])
        residual = sp.simplify(reduced-EXPECTED[label])
        if residual != 0:
            raise AssertionError(f"exact reduction failed in sector {label}: {residual}")
        results[label] = {
            "dimensionless_exact_value": str(reduced),
            "expected_exact_value": str(EXPECTED[label]),
            "exact_symbolic_residual": str(residual),
            "pi_exponent_after_reflection": data["pi_exponent"],
            "rational_prefactor": str(data["prefactor"]),
            "sine_exponents": {str(k): int(v) for k,v in data["sine_exponents"].items()},
            "cutoff": data["cutoff"],
        }
    return results


def audit():
    return {
        "task": "T044",
        "passed": True,
        "method": [
            "exact T043 finite Hurwitz/Gamma formula",
            "Gamma recurrence to residues modulo 60",
            "Euler reflection for complementary residues",
            "exact cyclotomic trigonometric simplification",
        ],
        "sectors": verify_all(),
        "status": {
            "proved_exact": [
                "all nine Gamma products reduce to the listed exact values",
                "the eight nontrivial twisted torsions are algebraic in Q(sqrt(5)) or Q",
                "the trivial sector is 2*pi^2/15 and agrees with T042",
            ],
            "still_open": [
                "separate meromorphic continuations and derivatives of zeta_0,rho and zeta_1,rho",
                "the individual degree determinants rather than their alternating combination",
            ],
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/t044_exact_twisted_gamma_reduction.json")
    args = parser.parse_args()
    report = audit()
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"task": report["task"], "passed": report["passed"],
                      "exact_values": {k:v["dimensionless_exact_value"]
                                       for k,v in report["sectors"].items()}}, indent=2))


if __name__ == "__main__":
    main()
