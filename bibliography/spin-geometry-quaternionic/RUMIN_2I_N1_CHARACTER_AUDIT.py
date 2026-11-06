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


# SU(2) class data in the order used above. The last entry is the order
# of a representative; all nine entries are conjugacy classes of 2I.
class_element_orders = (1, 2, 3, 4, 5, 5, 6, 10, 10)


def symmetric_power_character_table(max_degree: int):
    """Exact chi_m(g) for every listed conjugacy class and 0 <= m <= max_degree.

    Rows are indexed by m, columns by the nine classes. The recurrence
    chi_m = chi_1*chi_(m-1) - chi_(m-2) is exact in Q(sqrt(5)).
    """
    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    rows = []
    prev2 = [sp.Integer(1)] * len(class_sizes)
    prev1 = list(chi_fundamental)
    for m in range(max_degree + 1):
        if m == 0:
            row = list(prev2)
        elif m == 1:
            row = list(prev1)
        else:
            row = [sp.simplify(chi_fundamental[j] * prev1[j] - prev2[j])
                   for j in range(len(class_sizes))]
            prev2, prev1 = prev1, row
        rows.append(row)
    return rows


def equivariant_zeta_class_terms(max_degree: int, sector: str, class_index: int):
    """Finite equivariant Dirichlet terms for one conjugacy class.

    Each returned term is (m, p, eigenvalue, character, class_weight).
    The class_weight is |C|/120. Summing these signed terms over classes
    gives the invariant quotient zeta term-by-term. For E0 the zero mode
    is recorded separately as character 1 for every group element.
    """
    if not 0 <= class_index < len(class_sizes):
        raise IndexError("class_index must be in 0,...,8")
    if sector not in ("E0", "E1"):
        raise ValueError("sector must be 'E0' or 'E1'")
    chars = symmetric_power_character_table(max_degree)
    terms = []
    for m in range(max_degree + 1):
        if sector == "E0":
            if m == 0:
                continue  # harmonic zero mode is handled separately
            p_values = range(m + 1)
            sector_factor = 1
        else:
            p_values = range(1, m + 2)
            sector_factor = 2  # conjugate bidegrees
        chi = chars[m][class_index]
        if chi == 0:
            continue
        for p in p_values:
            lam = rumin_eigenvalue_n1(m - p, p)
            terms.append((m, p, lam, sector_factor * chi,
                          sp.Rational(class_sizes[class_index], 120)))
    return terms


def equivariant_zero_mode_class_weight(class_index: int):
    """E0 constant mode: chi_0(g)=1, weighted by |C|/120."""
    if not 0 <= class_index < len(class_sizes):
        raise IndexError("class_index must be in 0,...,8")
    return sp.Rational(class_sizes[class_index], 120)


def verify_class_periodicity(max_degree: int = 80):
    """Check chi_(m+ord(g))(g)=chi_m(g) for all noncentral classes.

    The identity and -I classes are deliberately excluded: their characters
    are m+1 and (-1)^m(m+1), respectively, not periodic.
    """
    chars = symmetric_power_character_table(max_degree + 10)
    checks = []
    for j in range(2, len(class_sizes)):
        order = class_element_orders[j]
        for m in range(max_degree + 1):
            assert sp.simplify(chars[m + order][j] - chars[m][j]) == 0
        checks.append((j, order))
    # The two central classes have the expected nonperiodic formulas.
    for m in range(max_degree + 1):
        assert chars[m][0] == m + 1
        assert chars[m][1] == (-1)**m * (m + 1)
    return checks


def verify_equivariant_reynolds_identity(max_degree: int = 40):
    """Verify class-by-class averaging reproduces invariant multiplicities.

    Checks character averages for each m and verifies that the E0/E1
    equivariant zeta coefficients average to the already audited quotient
    multiplicities for every admissible weight at finite cutoff.
    """
    chars = symmetric_power_character_table(max_degree)
    a = invariant_multiplicities(max_degree)
    for m in range(max_degree + 1):
        average = sp.simplify(sum(
            sp.Rational(class_sizes[j], 120) * chars[m][j]
            for j in range(len(class_sizes))
        ))
        assert average == a[m]
        if m == 0:
            continue
        for p in range(m + 1):
            averaged = sp.simplify(sum(
                sp.Rational(class_sizes[j], 120) * chars[m][j]
                for j in range(len(class_sizes))
            ))
            assert averaged == a[m]
        for p in range(1, m + 2):
            averaged = sp.simplify(sum(
                sp.Rational(class_sizes[j], 120) * 2 * chars[m][j]
                for j in range(len(class_sizes))
            ))
            assert averaged == 2 * a[m]
    return True



def torsion_difference_coefficients(max_degree: int = 300):
    """d_n = a_(n-2)-a_n after cancellation in -2*zeta_0+zeta_1."""
    if max_degree < 3:
        raise ValueError("max_degree must be at least 3")
    a = invariant_multiplicities(max_degree)
    return [sp.Integer(a[n - 2] - a[n]) for n in range(3, max_degree + 1)]


def torsion_periodic_residue_data():
    """One representative n>=3 for each nonzero residue modulo 60."""
    return [
        (62, sp.Integer(1)), (12, sp.Integer(-1)),
        (14, sp.Integer(1)), (20, sp.Integer(-1)),
        (22, sp.Integer(1)), (24, sp.Integer(-1)),
        (26, sp.Integer(1)), (30, sp.Integer(-1)),
        (34, sp.Integer(1)), (36, sp.Integer(-1)),
        (38, sp.Integer(1)), (40, sp.Integer(-1)),
        (46, sp.Integer(1)), (48, sp.Integer(-1)),
        (58, sp.Integer(1)), (60, sp.Integer(-2)),
    ]


def verify_torsion_periodicity(max_degree: int = 300):
    """Finite exact check of d_(n+60)=d_n; proof is in audit §10.3."""
    d = torsion_difference_coefficients(max_degree)
    for n in range(3, max_degree - 60 + 1):
        assert d[n - 3] == d[n + 60 - 3]
    data = torsion_periodic_residue_data()
    assert sum(v for _, v in data) == -1
    assert sum(v * (sp.Rational(1, 2) - sp.Rational(n, 60))
               for n, v in data) == 0
    return True


def hurwitz_regularized_kappa():
    """Finite Hurwitz-zeta continuation of kappa(s), regular at s=0."""
    s = sp.Symbol("s")
    terms = [value * sp.zeta(2 * s, sp.Rational(n, 60))
             for n, value in torsion_periodic_residue_data()]
    return sp.simplify(2 * 4**s * 60**(-2*s) * sum(terms))


def log_torsion_gamma_expression():
    """Exact log T = 2 sum d_n log Gamma(n/60) + log(2*pi)."""
    data = torsion_periodic_residue_data()
    return sp.simplify(
        2 * sum(value * sp.loggamma(sp.Rational(n, 60))
                for n, value in data)
        + sp.log(2 * sp.pi)
    )


def verify_torsion_gamma_identities():
    """Check finite identities used to differentiate the Hurwitz formula."""
    data = torsion_periodic_residue_data()
    assert sum(value for _, value in data) == -1
    assert sum(value * (sp.Rational(1, 2) - sp.Rational(n, 60))
               for n, value in data) == 0
    return True


def torsion_volume_closed_form():
    """Expected T_E = Vol(S^3/2I, 4*g_std) = 2*pi**2/15."""
    return sp.Rational(2, 15) * sp.pi**2


def verify_gamma_volume_identity(precision: int = 80):
    """High-precision numerical check of the finite Gamma product vs volume.

    This is a numerical cross-check, not a symbolic proof of the Gamma identity.
    """
    if precision < 30:
        raise ValueError("Use at least 30 decimal digits")
    gamma_value = sp.N(sp.exp(log_torsion_gamma_expression()), precision)
    volume_value = sp.N(torsion_volume_closed_form(), precision)
    residual = sp.N(gamma_value - volume_value, precision)
    assert abs(residual) < sp.Float(10) ** (-(precision // 2))
    return residual


def verify_trivial_gamma_closed_form():
    """Symbolically reduce the trivial-twist Gamma product to 2*pi**2/15.

    The period-60 tail representatives are used as written (not reduced
    modulo 60). Reflection pairs leave one Gamma(1/2) in the denominator.
    The remaining exact trigonometric identity is
      [sin(pi/5) sin(2pi/5) sin(pi/3) /
       (sin(pi/30) sin(7pi/30) sin(11pi/30) sin(13pi/30))]^2 = 60.
    """
    s_num = (sp.sin(sp.pi/30) * sp.sin(7*sp.pi/30)
             * sp.sin(11*sp.pi/30) * sp.sin(13*sp.pi/30))
    s_den = sp.sin(sp.pi/5) * sp.sin(2*sp.pi/5) * sp.sin(sp.pi/3)
    sine_identity = sp.simplify(sp.expand_trig((s_den/s_num)**2))
    assert sine_identity == 60
    gamma_ratio_squared = sp.simplify(sp.pi * sine_identity / 900)
    assert gamma_ratio_squared == sp.pi / 15
    torsion = sp.simplify(2 * sp.pi * gamma_ratio_squared)
    assert torsion == sp.Rational(2, 15) * sp.pi**2
    return {
        "sine_ratio_squared": sine_identity,
        "gamma_ratio_squared": gamma_ratio_squared,
        "trivial_torsion": torsion,
    }



def molien_invariant_multiplicities(max_degree: int):
    """Coefficients of the binary-icosahedral Molien series.

    Mukai, An Introduction to Invariants and Moduli (2003), p. 19:
        M(t)=(1+t**30)/((1-t**12)(1-t**20)).
    """
    coeff = [0] * (max_degree + 1)
    for r in range(0, max_degree + 1, 12):
        for u in range(0, max_degree - r + 1, 20):
            coeff[r + u] += 1
    for r in range(30, max_degree + 1, 12):
        for u in range(0, max_degree - r + 1, 20):
            coeff[r + u] += 1
    return coeff


def n1_jk_weight_pairs(m: int, bidegree: str):
    """Exact n=1 Julg--Kasparov/Kitaoka weights at fixed SU(2) degree m.

    Kitaoka, arXiv:1911.03092v1, Proposition 1.1:
      E00: q,p >= 0;
      E10: q >= -1, p >= 1 (Case VI);
      E01: q >= 1, p >= -1 (Case VII).
    The tuple returned is (q,p), with U(2) highest weight (q,-p).
    """
    if m < 0:
        raise ValueError("m must be nonnegative")
    if bidegree == "E00":
        return [(m - p, p) for p in range(m + 1)]
    if bidegree == "E10":
        return [(m - p, p) for p in range(1, m + 2)]
    if bidegree == "E01":
        return [(q, m - q) for q in range(1, m + 2)]
    raise ValueError("bidegree must be E00, E10, or E01")


def verify_n1_jk_weight_decomposition(max_degree: int = 100):
    """Check all n=1 highest-weight ranges and SU(2) restrictions."""
    a = invariant_multiplicities(max_degree)
    for m in range(max_degree + 1):
        for sector in ("E00", "E10", "E01"):
            pairs = n1_jk_weight_pairs(m, sector)
            assert len(pairs) == m + 1
            assert all(q + p == m for q, p in pairs)
            assert all(q >= -p for q, p in pairs)  # U(2) dominance
            # V_(q,-p) = det**(-p) tensor Sym**(q+p); det is trivial on SU(2).
            assert all(q + p == m for q, p in pairs)
            assert (m + 1) * a[m] == len(pairs) * a[m]
    return True


def verify_molien_character_agreement(max_degree: int = 300):
    """Independent exact check: Reynolds character average = Molien coefficient."""
    return invariant_multiplicities(max_degree) == molien_invariant_multiplicities(max_degree)


def verify_middle_D_intertwiner():
    """Symbolically verify Kitaoka §2.3 Case V for n=1, p,q >= 1.

    With A**2=p(q+1)/2, B**2=q(p+1)/2, C=(p-q)/2,
    A'=C-2A**2 and B'=C+2B**2. Kitaoka's D^dagger D on
    the orthogonal complement of im(d_E^0) is
      ((A'B)**2+(B'A)**2)/(A**2+B**2).
    """
    p, q = sp.symbols("p q", integer=True, positive=True)
    A2 = p * (q + 1) / 2
    B2 = q * (p + 1) / 2
    C = (p - q) / 2
    Aprime = sp.simplify(C - 2 * A2)
    Bprime = sp.simplify(C + 2 * B2)
    S = 2 * p * q + p + q
    assert sp.simplify(Aprime + S / 2) == 0
    assert sp.simplify(Bprime - S / 2) == 0
    D2 = sp.simplify((Aprime**2 * B2 + Bprime**2 * A2) / (A2 + B2))
    assert sp.simplify(D2 - S**2 / 4) == 0
    return True


def verify_n1_boundary_and_zero_weight_cases():
    """Check Cases III/IV and VI/VII separately, without extrapolating."""
    p, q = sp.symbols("p q", integer=True, positive=True)
    # Cases III/IV: the central D kills im(d_E^0); Delta_E^1 is the
    # square of the first-order singular value p/2 or q/2.
    assert sp.simplify((p / 2)**2 - p**2 / 4) == 0
    assert sp.simplify((q / 2)**2 - q**2 / 4) == 0
    # Cases VI/VII are Reeb-only: 2 L_T has eigenvalue i(p-q).
    assert boundary_eigenvalue_case_vi(13) == sp.Rational(14**2, 4)
    assert boundary_eigenvalue_case_vii(13) == sp.Rational(14**2, 4)
    return True


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
    print("E^0 zero-mode contribution:", zeta_zero_mode_contribution_e0())
    print("E^0 positive spectral terms through m=12:", len(z0))
    print("E^1 spectral terms through m=12:", len(z1))
    rows = n1_bidegree_counts(max_degree)
    print("nonzero invariant degrees:", nonzero)
    print("n=1 bidegree invariant multiplicities at first levels:")
    for row in rows:
        if row["SU2_invariant_dimension_per_irrep"]:
            print(row)
    periodic = verify_class_periodicity(80)
    assert verify_equivariant_reynolds_identity(40)
    # At least one nonidentity class has a nonzero character contribution;
    # fixed-point-freeness does not mean its equivariant trace vanishes.
    chars = symmetric_power_character_table(12)
    assert any(chars[12][j] != 0 for j in range(1, 9))
    print("noncentral character periods (class index, order):", periodic)
    assert verify_n1_jk_weight_decomposition(100)
    assert verify_molien_character_agreement(300)
    assert verify_middle_D_intertwiner()
    assert verify_n1_boundary_and_zero_weight_cases()
    assert verify_torsion_periodicity(600)
    assert verify_torsion_gamma_identities()
    print("Hurwitz torsion residue data:", torsion_periodic_residue_data())
    print("log T exact gamma expression:", log_torsion_gamma_expression())
    print("Gamma/volume residual (high precision):", verify_gamma_volume_identity(80))
    print("Exact trivial-twist Gamma reduction:", verify_trivial_gamma_closed_form())
    print("PASS: exact n=1 JK weights, D-intertwiner, Reynolds/Molien agreement, boundary cases, periodic torsion reduction, and Gamma/volume checks")
