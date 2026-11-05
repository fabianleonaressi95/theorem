# T046 — Hadamard finite-part determinants and their scale law

## 1. Objective and convention

T045 proved that the two degree zeta functions have simple poles at the origin. An individual determinant therefore requires a renormalization prescription. T046 fixes one explicit convention: the scale-dependent Hadamard finite part of the derivative of the dimensionally scaled zeta function.

Write the Laurent expansion

    zeta_(k,rho)(s) = R_(k,rho)/s + C_(k,rho)
                     + D_(k,rho)*s + O(s^2).

For a positive scale mu, define

    log det_FP,k,rho(mu)
      = - FP_(s=0) d/ds [mu^(2s) zeta_(k,rho)(s)]
      = -[D_(k,rho) + 2*C_(k,rho)*log(mu)
                       + 2*R_(k,rho)*log(mu)^2].

This is the convention used throughout T046. It is not asserted to be the unique possible renormalization.

## 2. Scale transformation

Expanding mu^(2s) and differentiating gives

    mu^(2s) zeta(s)
      = R/s + (C+2R L)
        + (D+2C L+2R L^2)*s + O(s^2),
    L=log(mu).

Consequently,

    FP d/ds[mu^(2s)zeta(s)]|_(s=0)
       = D+2C L+2R L^2.

This specifies the scheme unambiguously once the Laurent coefficients and mu are specified.

## 3. Exact residues and the alternating constraint

T045 gives, for d_rho=dim(rho),

    R_(0,rho)=d_rho/960,
    R_(1,rho)=d_rho/480=2*R_(0,rho).

Thus the alternating zeta

    kappa_rho(s)=-2*zeta_(0,rho)(s)+zeta_(1,rho)(s)

has zero residue and is regular at s=0.

Let C_kappa=kappa_rho(0) and D_kappa=kappa'_rho(0). Since the T043/T044 convention is 2 log(T_rho)=kappa'_rho(0),

    D_(1,rho)-2*D_(0,rho)=2 log(T_rho),
    C_(1,rho)-2*C_(0,rho)=kappa_rho(0).

At scale mu the logarithms of the finite-part determinants obey the exact relation

    log det_FP,1,rho(mu)
      - 2 log det_FP,0,rho(mu)
      = -2 log(T_rho)-2*kappa_rho(0)*log(mu).

Equivalently,

    det_FP,1,rho(mu) / det_FP,0,rho(mu)^2
      = T_rho^(-2) * mu^(-2*kappa_rho(0)).

This is the strongest individual-determinant statement fixed by the alternating torsion without computing the two separate Laurent coefficients.

## 4. Exact value of kappa_rho(0)

T043 writes

    kappa_rho(s)=2*4^s [
      sum_(n<c) d_(n,rho)*n^(-2s)
      + 60^(-2s) sum_(r=1)^60 e_(r,rho)
          zeta_H(2s,n_r/60)
    ].

Using zeta_H(0,x)=1/2-x gives the exact rational number

    kappa_rho(0)
      = 2 * [
          sum_(n<c) d_(n,rho)
          + sum_(r=1)^60 e_(r,rho)*(1/2-n_r/60)
        ].

The implementation evaluates this expression with fractions only. No numerical continuation is needed for kappa_rho(0).

## 5. What T046 does and does not determine

The alternating torsion determines D_1-2D_0, and its value at zero determines C_1-2C_0. It does not determine C_0, C_1, D_0, and D_1 separately. In particular, it does not determine either individual finite-part determinant.

T046 therefore does not invent individual determinant numbers. It provides:
- an explicit finite-part prescription;
- its exact scale law;
- exact residues in all nine 2I sectors;
- exact rational kappa_rho(0);
- the exact relation between the two finite-part determinants and the known T044 torsion.

To obtain both individual values one must continue the two separate double spectral sums far enough to determine C_0 and D_0 (or C_1 and D_1) individually. The alternating sum alone cannot supply the missing data.

## 6. Reproducibility

Files:
- src/t046_hadamard_finite_part_determinants.py
- tests/test_t046_hadamard_finite_part_determinants.py

Run:

    python -m pytest tests/test_t046_hadamard_finite_part_determinants.py -q
    python -m src.t046_hadamard_finite_part_determinants --log-mu 0 --dps 60

The tests cover the Laurent finite-part formula, scale dependence, exact rational kappa(0), and the cancellation of residues in all nine sectors. Tests have been added but have not yet been executed in the repository; no CI pass is claimed.

## Status ledger

| Statement | Status |
|---|---|
| Hadamard finite-part convention | Defined exactly |
| Scale transformation law | Exact |
| Individual zeta residues | Exact from T045 |
| kappa_rho(0) | Exact rational finite Hurwitz expression |
| Alternating finite-part determinant relation | Exact |
| Individual finite-part determinant values | Not determined yet |
| Separate Laurent constants and linear coefficients | Open |

## Dependencies

T032 exact Molien multiplicities; T042 trivial-sector torsion; T043 period-60 Hurwitz formula; T044 exact twisted torsions; T045 individual zeta residues.
