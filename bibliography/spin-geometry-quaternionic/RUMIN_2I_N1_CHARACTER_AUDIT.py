#!/usr/bin/env python3
"""Exact character audit for the n=1 Rumin decomposition on S^3/2I.

Requires sympy. Uses the nine conjugacy classes of the binary icosahedral
subgroup 2I < SU(2). No floating-point character arithmetic is used.
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
class_sizes = (1, 1, 20, 30, 12, 12, 20, 12, 12)
chi_fundamental = (
    sp.Integer(2), sp.Integer(-2), sp.Integer(-1), sp.Integer(0),
    phi - 1, -phi, sp.Integer(1), phi, 1 - phi,
)

def invariant_multiplicities(max_degree: int):
    """Return dim(Sym^m(C^2)^{2I}) for 0 <= m <= max_degree."""
    prev2 = [sp.Integer(1)] * len(class_sizes)  # chi_0
    prev1 = list(chi_fundamental)               # chi_1
    result = []
    for m in range(max_degree + 1):
        if m == 0:
            chi = prev2
        elif m == 1:
            chi = prev1
        else:
            chi = [sp.simplify(chi_fundamental[k] * prev1[k] - prev2[k])
                   for k in range(len(class_sizes))]
            prev2, prev1 = prev1, chi
        multiplicity = sp.simplify(
            sum(class_sizes[k] * chi[k] for k in range(len(class_sizes))) / 120
        )
        assert multiplicity.is_integer
        assert multiplicity >= 0
        result.append(int(multiplicity))
    return result

def n1_bidegree_counts(max_degree: int):
    """Multiplicity by SU(2)-degree m in the three n=1 bidegrees.

    E^(0,0): q,p >= 0, q+p=m.
    E^(1,0): q >= -1, p >= 1, q+p=m.
    E^(0,1): q >= 1, p >= -1, q+p=m.
    Each allowed pair contributes one U(2) irrep; on SU(2) it restricts
    to Sym^m(C^2). Thus each bidegree has m+1 allowed pairs for m>=0.
    """
    a = invariant_multiplicities(max_degree)
    rows = []
    for m, inv_dim in enumerate(a):
        allowed_pairs = m + 1
        rows.append({
            "m": m,
            "SU2_invariant_dimension_per_irrep": inv_dim,
            "allowed_U2_weights_per_bidegree": allowed_pairs,
            "2I_invariant_multiplicity_per_bidegree": allowed_pairs * inv_dim,
        })
    return rows


def rumin_eigenvalue_n1(q: int, p: int):
    """Theorem 0.1 specialized to n=1, i=j=0.

    Boundary weights are independently checked below from Cases VI and VII.
    """
    return sp.Rational((p * (q + 1) + q * (p + 1)) ** 2, 4)


def boundary_eigenvalue_case_vi(p: int):
    """Case VI: n=1, q=-1, p>=1; eigenvalue of D^dagger D."""
    if p < 1:
        raise ValueError("Case VI requires p >= 1")
    return sp.Rational((p + 1) ** 2, 4)


def boundary_eigenvalue_case_vii(q: int):
    """Case VII: n=1, p=-1, q>=1; conjugate of Case VI."""
    if q < 1:
        raise ValueError("Case VII requires q >= 1")
    return sp.Rational((q + 1) ** 2, 4)


def zeta_zero_mode_contribution_e0():
    """Kitaoka's convention is 0**s = 1: one constant mode in E^0."""
    return sp.Integer(1)


def scalar_spectral_zeta_terms(max_degree: int):
    """Positive-spectrum terms of the quotient E^0 zeta.

    Returns (m,p,eigenvalue,multiplicity); add zeta_zero_mode_contribution_e0()
    separately to reproduce Kitaoka's explicit convention 0**s = 1.
    """
    a = invariant_multiplicities(max_degree)
    terms = []
    for m, inv_dim in enumerate(a):
        if inv_dim == 0 or m == 0:
            continue
        for p in range(m + 1):
            lam = rumin_eigenvalue_n1(m - p, p)
            terms.append((m, p, lam, inv_dim))
    return terms


def middle_spectral_zeta_terms(max_degree: int):
    """Finite truncation of E^1; E^(1,0) and E^(0,1) are conjugate."""
    a = invariant_multiplicities(max_degree)
    terms = []
    for m, inv_dim in enumerate(a):
        if inv_dim == 0:
            continue
        for p in range(1, m + 2):
            lam = rumin_eigenvalue_n1(m - p, p)
            terms.append((m, p, lam, 2 * inv_dim))
    return terms


def spectral_zeta_dirichlet_term(eigenvalue, multiplicity, s):
    """One term multiplicity * eigenvalue^(-s), for positive eigenvalues."""
    if eigenvalue <= 0 or multiplicity < 0:
        raise ValueError("Require positive eigenvalue and nonnegative multiplicity")
    return sp.Integer(multiplicity) * sp.Pow(sp.sympify(eigenvalue), -s)

def first_invariant_level_spectra():
    """Eigenvalues on invariant copies at m=12 in the three n=1 bidegrees."""
    m = 12
    scalar = [rumin_eigenvalue_n1(m - p, p) for p in range(m + 1)]
    e10 = [rumin_eigenvalue_n1(m - p, p) for p in range(1, m + 2)]
    e01 = [rumin_eigenvalue_n1(q, m - q) for q in range(1, m + 2)]
    assert scalar == [36, 289, 676, 1089, 1444, 1681, 1764,
                      1681, 1444, 1089, 676, 289, 36]
    assert e10 == [289, 676, 1089, 1444, 1681, 1764, 1681,
                   1444, 1089, 676, 289, 36, 49]
    assert e01 == e10
    # Independent boundary derivations: Case VI and its conjugate, Case VII.
    assert boundary_eigenvalue_case_vi(13) == 49
    assert boundary_eigenvalue_case_vi(13) == rumin_eigenvalue_n1(-1, 13)
    assert boundary_eigenvalue_case_vii(13) == 49
    assert boundary_eigenvalue_case_vii(13) == rumin_eigenvalue_n1(13, -1)
    return scalar, e10, e01

if __name__ == "__main__":
    max_degree = 80
    a = invariant_multiplicities(max_degree)
    nonzero = [(m, v) for m, v in enumerate(a) if v]
    expected = {0: 1, 12: 1, 20: 1, 24: 1, 30: 1,
                32: 1, 36: 1, 40: 1, 42: 1, 44: 1,
                48: 1, 50: 1, 52: 1, 54: 1, 56: 1,
                60: 2, 62: 1, 64: 1, 66: 1, 68: 1,
                70: 1, 72: 2, 74: 1, 76: 1, 78: 1, 80: 2}
    assert dict(nonzero) == expected
    assert sum(class_sizes) == 120
    scalar, e10, e01 = first_invariant_level_spectra()
    z0 = scalar_spectral_zeta_terms(12)
    z1 = middle_spectral_zeta_terms(12)
    assert zeta_zero_mode_contribution_e0() == 1
    assert len(z0) == 13
    assert len(z1) == 28
    assert sum(term[3] for term in z0) == 13
    assert sum(term[3] for term in z1) == 28
    print("m=12 scalar eigenvalues:", scalar)
    print("m=12 E^(1,0) eigenvalues:", e10)
    print("m=12 E^(0,1) eigenvalues:", e01)
    print("Case VI boundary p=13:", boundary_eigenvalue_case_vi(13))
    print("Case VII boundary q=13:", boundary_eigenvalue_case_vii(13))
    print("E^0 zero-mode contribution (Kitaoka convention 0**s=1):",
          zeta_zero_mode_contribution_e0())
    print("E^0 positive spectral terms through m=12:", len(z0))
    print("E^1 spectral terms through m=12:", len(z1))
    rows = n1_bidegree_counts(max_degree)
    print("nonzero invariant degrees:", nonzero)
    print("n=1 bidegree invariant multiplicities at first levels:")
    for row in rows:
        if row["SU2_invariant_dimension_per_irrep"]:
            print(row)
    print("PASS: exact character average, integrality, nonnegativity, and n=1 weight counts")
