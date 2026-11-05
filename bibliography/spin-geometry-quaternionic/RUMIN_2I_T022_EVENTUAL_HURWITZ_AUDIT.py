#!/usr/bin/env python3
"""T022: exact eventual-period Hurwitz audit for all 2I Rumin twists.

Requires sympy. Builds D_rho from the nine Molien covariant numerators,
forms P_rho=(1-t^60)D_rho, separates every finite initial segment from
its eventual period-60 tail, and evaluates the corrected Hurwitz/Gamma
continuation. No floating-point arithmetic is used until final reporting.

Crucial scaling:
  sum_{k>=0} (N+60k)^(-2s) = 60^(-2s) zeta_H(2s,N/60).
The prefactor is 60^(-2s), not N^(-2s).
"""
import json
import sympy as sp

t, s = sp.symbols("t s")
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


def eventual_data(label):
    """Return exact polynomial P, finite coefficients and tail starts."""
    numerator = NUMERATORS[label]
    b0 = sp.Poly(numerator, t).coeff_monomial(1)
    molien = numerator / DEN
    # The b_0 correction removes the m=0 term from sum_{m>=1}.
    D = sp.cancel((t**2 - 1) * molien + b0 * (1 - t**2))
    P_expr = sp.cancel(sp.together((1 - t**60) * D))
    P = sp.Poly(P_expr, t, domain="QQ")
    assert sp.denom(P_expr) == 1, (label, P_expr)
    p = {monom[0]: coeff for monom, coeff in P.terms()}
    degree = max(p, default=0)

    # c_n=[t^n]D=sum_{j>=0}p_(n-60j), evaluated exactly.
    c = {}
    for n in range(1, degree + 61):
        c[n] = sp.simplify(sum(
            coeff for exponent, coeff in p.items()
            if exponent <= n and (n - exponent) % 60 == 0
        ))

    finite = []
    tails = []
    for residue in range(60):
        exponents = [e for e, coeff in p.items()
                     if coeff != 0 and e % 60 == residue]
        if not exponents:
            continue
        N = max(exponents)
        d = sp.simplify(sum(p[e] for e in exponents))
        finite.extend((n, c[n]) for n in range(1, N)
                      if n % 60 == residue and c.get(n, 0) != 0)
        tails.append((N, d, residue))

        # Check the eventual coefficient identity beyond the last p-term.
        for n in range(N, degree + 61):
            if n % 60 == residue:
                assert sp.simplify(c[n] - d) == 0, (label, residue, n)

    finite.sort()
    tails.sort()
    return P, finite, tails, c


def log_torsion(label):
    """Compute log T=1/2 kappa'(0), with the correctly scaled tails."""
    P, finite, tails, _ = eventual_data(label)
    value = sp.Integer(0)
    # Genuine initial Dirichlet segment: keep n itself, not a Hurwitz term.
    for n, coeff in finite:
        value += coeff * (sp.log(4) - 2*sp.log(n))
    # Tail n=N+60k: scale by 60^(-2s), not N^(-2s).
    for N, d, _residue in tails:
        value += d * (
            (sp.log(4) - 2*sp.log(60)) * (sp.Rational(1, 2) - sp.Rational(N, 60))
            + 2*sp.loggamma(sp.Rational(N, 60)) - sp.log(2*sp.pi)
        )
    return sp.simplify(value)


def audit(precision=60):
    if precision < 30:
        raise ValueError("precision must be at least 30 digits")
    report = {}
    for label in NUMERATORS:
        P, finite, tails, _ = eventual_data(label)
        actual = sp.N(sp.exp(log_torsion(label)), precision)
        expected = sp.N(EXPECTED[label], precision)
        residual = sp.N(actual - expected, precision)
        assert abs(residual) < sp.Float(10) ** (-(precision // 2)), (
            label, actual, expected, residual
        )
        report[label] = {
            "P_degree": P.degree(),
            "finite_initial_terms": [[int(n), str(v)] for n, v in finite],
            "tail_starts": [[int(N), str(d)] for N, d, _ in tails],
            "torsion": str(actual),
            "benchmark": str(expected),
            "absolute_residual": str(abs(residual)),
        }
    return report


if __name__ == "__main__":
    result = audit(70)
    print(json.dumps(result, indent=2))
    print("PASS: all nine eventual-period decompositions match the independent algebraic benchmarks at 70-digit precision.")
