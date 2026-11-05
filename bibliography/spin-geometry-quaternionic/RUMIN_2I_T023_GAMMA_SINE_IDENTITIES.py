#!/usr/bin/env python3
"""T023: exact Gamma-to-sine reduction for the nine 2I Rumin torsions.

Requires SymPy. This script starts from the nine exact Molien numerators,
reconstructs the eventual-period tails, applies Gamma recurrence/reflection,
and reduces the resulting rational-angle sine products exactly in Q(sqrt(5)).

No floating-point arithmetic is used. The only exceptional tail is the
trivial representation's N=62 term:
  Gamma(31/30) = Gamma(1/30)/30,
paired with Gamma(29/30). All other complementary tails use Euler reflection.
"""
import json
import sympy as sp

t = sp.symbols("t")
DEN = (1 - t**12) * (1 - t**20)
NUMERATORS = {
    "1": 1 + t**30,
    "2": t + t**11 + t**19 + t**29,
    "2'": t**7 + t**13 + t**17 + t**23,
    "3": t**2 + t**10 + t**12 + t**18 + t**20 + t**28,
    "3'": t**6 + t**10 + t**14 + t**16 + t**20 + t**24,
    "4": t**6 + t**8 + t**12 + t**14 + t**16 + t**18 + t**22 + t**24,
    "4'": t**3 + t**9 + t**11 + t**13 + t**17 + t**19 + t**21 + t**27,
    "5": t**4 + t**8 + t**10 + t**12 + t**14 + t**16 + t**18 + t**20 + t**22 + t**26,
    "6": t**5 + t**7 + t**9 + t**11 + t**13 + 2*t**15 + t**17 + t**19 + t**21 + t**23 + t**25,
}
EXPECTED = {
    "1": 2*sp.pi**2/15,
    "2": (3-sp.sqrt(5))/4,
    "2'": (3+sp.sqrt(5))/4,
    "3": 1-1/sp.sqrt(5),
    "3'": 1+1/sp.sqrt(5),
    "4": sp.Rational(5, 3),
    "4'": sp.Integer(1),
    "5": sp.Rational(3, 2),
    "6": sp.Integer(2),
}
EXPECTED_SINE = {
    "1": sp.Rational(1, 15),
    "2": (3-sp.sqrt(5))/16,
    "2'": (3+sp.sqrt(5))/16,
    "3": (5-sp.sqrt(5))/40,
    "3'": (5+sp.sqrt(5))/40,
    "4": sp.Rational(5, 48),
    "4'": sp.Rational(1, 16),
    "5": sp.Rational(3, 64),
    "6": sp.Rational(1, 32),
}


def residue_tail_data(label):
    """Exact P=(1-t^60)D coefficients and maximal exponent per residue."""
    numerator = NUMERATORS[label]
    b0 = sp.Poly(numerator, t).coeff_monomial(1)
    molien = numerator / DEN
    D = sp.cancel((t**2 - 1)*molien + b0*(1 - t**2))
    P_expr = sp.cancel((1 - t**60)*D)
    p_num, p_den = sp.fraction(P_expr)
    assert p_den == 1, (label, p_den)
    P = sp.Poly(p_num, t, domain="QQ")
    p = {monom[0]: coeff for monom, coeff in P.terms() if coeff != 0}
    degree = P.degree()

    # Verify that the exact coefficient sequence is eventually constant
    # on each residue class and retain any genuine finite preperiod.
    c = {}
    for n in range(1, degree + 61):
        c[n] = sp.simplify(sum(
            coeff for exponent, coeff in p.items()
            if exponent <= n and (n-exponent) % 60 == 0
        ))
    finite, tails = [], []
    for residue in range(60):
        exponents = [e for e in p if e % 60 == residue]
        if not exponents:
            continue
        N = max(exponents)
        d = sp.simplify(sum(p[e] for e in exponents))
        finite.extend((n, c[n]) for n in range(1, N)
                      if n % 60 == residue and c.get(n, 0) != 0)
        tails.append((N, d))
        for n in range(N, degree + 61):
            if n % 60 == residue:
                assert sp.simplify(c[n] - d) == 0
    return P, sorted(finite), sorted(tails)


def sine_reduction(label):
    """Apply recurrence/reflection and return the exact residual sine product.

    For N<30, pair Gamma(N/60) with Gamma(1-N/60).
    N=30 contributes Gamma(1/2); N=60 contributes Gamma(1)=1.
    The trivial N=62 term is first shifted by Gamma(31/30)=Gamma(1/30)/30.
    """
    _P, finite, tails = residue_tail_data(label)
    assert finite == [], (label, finite)
    dmap = dict(tails)
    dim = -sum(dmap.values())
    assert dim in (1, 2, 3, 4, 5, 6)

    # Reflection requires equal coefficients at complementary arguments.
    for N, d in tails:
        if N == 62:
            assert label == "1" and dmap.get(58) == d
        elif 1 <= N < 60 and N != 30:
            assert dmap.get(60-N) == d, (label, N, d, dmap.get(60-N))

    S = sp.Integer(1)
    for N, d in tails:
        if N < 30:
            S *= sp.sin(sp.pi*N/60)**(-2*d)
        elif N == 62:
            # Gamma(31/30)=Gamma(1/30)/30; reflect against Gamma(29/30).
            S *= sp.Integer(30)**(-2*d) * sp.sin(sp.pi/30)**(-2*d)

    S = sp.simplify(sp.expand_trig(S))
    assert sp.simplify(S - EXPECTED_SINE[label]) == 0, (
        label, S, EXPECTED_SINE[label]
    )

    # The zeta-derivative scale term vanishes: sum d_N(1/2-N/60)=0.
    scale_sum = sp.simplify(sum(
        d*(sp.Rational(1, 2)-sp.Rational(N, 60)) for N, d in tails
    ))
    assert scale_sum == 0

    # Gamma reflection plus the (2*pi)^dim factor gives:
    # T_1=2*pi^2*S_1; for every nontrivial irrep T=2^dim*S.
    reconstructed = (2*sp.pi**2*S if label == "1" else 2**dim*S)
    assert sp.simplify(reconstructed - EXPECTED[label]) == 0
    return {
        "dimension": int(dim),
        "P_degree": int(_P.degree()),
        "tail_starts": [[int(N), str(d)] for N, d in tails],
        "scale_sum": str(scale_sum),
        "sine_product": str(S),
        "torsion": str(sp.simplify(reconstructed)),
    }


def audit():
    report = {label: sine_reduction(label) for label in NUMERATORS}
    assert sum(int(report[k]["dimension"])**2 for k in report) == 120
    return report


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
    print("PASS: all nine Gamma products reduce exactly to the stated torsions.")
