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

The period-60 formula below gives kappa_rho(0)=0 exactly in all nine sectors. Therefore the scale terms cancel in the alternating combination and

    log det_FP,1,rho(mu) - 2 log det_FP,0,rho(mu)
      = -2 log(T_rho),

or

    det_FP,1,rho(mu) / det_FP,0,rho(mu)^2 = T_rho^(-2).

This ratio is independent of mu, even though each individual finite-part determinant can depend on mu.

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

The implementation evaluates this expression with fractions only. Exact arithmetic gives kappa_rho(0)=0 for every one of the nine irreducible sectors. No numerical continuation is needed.

## 5. What T046 does and does not determine

The alternating torsion determines D_1-2D_0, and its value at zero determines C_1-2C_0. It does not determine C_0, C_1, D_0, and D_1 separately. In particular, it does not determine either individual finite-part determinant.

T046 therefore does not invent individual determinant numbers. It provides:
- an explicit finite-part prescription;
- its exact scale law;
- exact residues in all nine 2I sectors;
- exact kappa_rho(0)=0 in all nine sectors;
- the exact, scale-independent relation between the two finite-part determinants and the known T044 torsion.

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
# T046-R1 — Determinant consequences after the corrected T045 audit

## 1. Corrected analytic premise

The original T046 adopted a Hadamard finite-part prescription because T045 claimed nonzero simple poles for the two separate degree zeta functions. T045-R1 corrects the binomial-index classification: the only candidate residue is proportional to \(\sum_r(\beta_r-\alpha_r)\), which vanishes exactly in every irreducible 2I sector.

Thus
\[
R_{0,\rho}=R_{1,\rho}=0.
\]
Under the locally uniform Hurwitz continuation established in T045-R1, both separate zeta functions are regular at zero. Their ordinary derivatives are therefore the natural determinant inputs. The finite-part convention remains an optional scale-dependent reparameterization, not a required pole subtraction.

## 2. Optional scale convention

For a regular expansion
\[
\zeta_{k,\rho}(s)=C_{k,\rho}+D_{k,\rho}s+O(s^2),
\]
one may still define
\[
\log\det_\mu\Delta_{k,\rho}
=-\left[D_{k,\rho}+2C_{k,\rho}\log\mu\right].
\]
At \(\mu=1\), this is the ordinary zeta determinant \(-\zeta'_{k,\rho}(0)\). The scale law follows by differentiating \(\mu^{2s}\zeta(s)\); there is no \(\log^2\mu\) term because the residue is zero.

## 3. What the alternating torsion determines

With \(\kappa_\rho(s)=-2\zeta_{0,\rho}(s)+\zeta_{1,\rho}(s)\), T043/T044 give
\[
\kappa_\rho(0)=0,\qquad \kappa'_\rho(0)=2\log T_\rho.
\]
Consequently
\[
C_{1,\rho}-2C_{0,\rho}=0,\qquad
D_{1,\rho}-2D_{0,\rho}=2\log T_\rho.
\]
The same derivative relation holds at every scale because the constant combination also vanishes:
\[
D_{1,\rho}(\mu)-2D_{0,\rho}(\mu)=2\log T_\rho.
\]
This determines only the alternating combination, not the two individual values.

## 4. Status

| Claim | Status |
|---|---|
| Individual residues at zero | Exactly zero by corrected T045 |
| Separate zeta regularity at zero | Analytic conclusion under the locally uniform continuation |
| Ordinary individual zeta determinants | Well-defined if the stated continuation is accepted |
| Individual Laurent constants \(C_0,C_1\) | Not computed |
| Individual derivatives \(D_0,D_1\) | Not computed |
| Alternating derivative relation | Exact from T043/T044 |
| Optional scaled finite-part convention | Defined; no pole subtraction required |

## 5. Reproducibility

\`\`\`bash
python -m pytest tests/test_t045_individual_rumin_zeta_poles.py tests/test_t046_hadamard_finite_part_determinants.py -q
python -m src.t046_hadamard_finite_part_determinants --log-mu 0 --dps 60
\`\`\`

The updated tests are added in this correction branch and still require execution by CI. No individual determinant values are claimed.
