# T045 — The individual Rumin degree zeta functions have poles at zero

## 1. Main result

The request to compute the two separate ordinary zeta determinants exposes an analytic obstruction: the individual degree zeta functions are not regular at s=0.

For every irreducible 2I representation rho, with dimension d_rho,

    Res_(s=0) zeta_(0,rho)(s) = d_rho/960,
    Res_(s=0) zeta_(1,rho)(s) = d_rho/480.

Both residues are nonzero. Therefore the ordinary derivatives zeta'_(0,rho)(0) and zeta'_(1,rho)(0) do not exist, and the standard individual determinants exp(-zeta'_k(0)) are not defined without an additional finite-part/renormalization prescription.

The alternating combination is nevertheless regular:

    Res_(s=0) [-2 zeta_(0,rho)(s)+zeta_(1,rho)(s)]
      = -2*d_rho/960 + d_rho/480 = 0.

This explains analytically why the Rumin torsion combination in T042–T044 is well-defined although its two constituent zeta functions have poles.

## 2. Split into interior and boundary sums

Write m=p+q. The n=1 Rumin eigenvalue is

    Lambda_(p,q) = (2*p*q+p+q)^2/4.

Let

    H_rho(s) = sum_(p,q>=1) b_(p+q,rho) Lambda_(p,q)^(-s),
    B_rho(s) = sum_(m>=1) b_(m,rho) (m^2/4)^(-s),
    C_rho(s) = sum_(m>=0) b_(m,rho) ((m+2)^2/4)^(-s).

The scalar degree has two equal boundary faces p=0 and q=0, while the middle degree has one q=0 face and the exceptional q=-1 face. With the m=0 scalar zero mode separated,

    zeta_(0,rho)(s) = delta_(rho,1) + 2 B_rho(s) + H_rho(s),
    zeta_(1,rho)(s) = 2 [B_rho(s)+C_rho(s)+H_rho(s)].

The one-dimensional boundary sums B and C have finite Hurwitz-zeta continuations regular at s=0. Thus all possible poles at zero come from H_rho.

## 3. Affine quasi-polynomial multiplicities

The Molien series is

    A_rho(t) = N_rho(t)/[(1-t^12)(1-t^20)].

Since both 12 and 20 divide 60,

    (1-t^60)^2 A_rho(t)

is a polynomial. Consequently, beyond an explicit finite cutoff, the coefficient sequence is affine on every residue class modulo 60:

    b_(m,rho) = alpha_(r,rho)*m + beta_(r,rho),
    r = m mod 60.

The exact coefficients are computed from rational Molien coefficients in the source module. For all nine irreps, exact arithmetic verifies

    sum_(r=0)^59 alpha_(r,rho)
      = sum_(r=0)^59 beta_(r,rho) = d_rho/2.

These two moments also follow from the pole expansion at t=1. The numerator support in T032 is symmetric about degree 15, so N_rho(1)=2*d_rho and N'_rho(1)=15*N_rho(1). Comparing the double- and simple-pole coefficients of A_rho(t) at t=1 gives the two identities above.

## 4. Hurwitz continuation of the interior double sum

Set

    a=2p+1, b=2q+1, with a,b odd and >=3.

Then

    2*p*q+p+q = (a*b-1)/2,
    Lambda_(p,q) = (a*b-1)^2/16,
    m=p+q=(a+b-2)/2.

For each odd residue A modulo 120, let

    U_A(z) = sum_(a>=3 odd, a=A mod 120) a^(-z)
           = 120^(-z) zeta_H(z,a_A/120),

where a_A is the least integer at least 3 in that residue class. In particular,

    Res_(z=1) U_A(z)=1/120.

Replace b_m, after its exact quasi-polynomial cutoff, by alpha_r*m+beta_r and subtract the finite set of exceptional low m terms. The interior series then has the exact binomial/Hurwitz representation

    H_rho(s) = H_finite(s) + 16^s
      * sum_(k>=0) (2s)_k/k!
        * sum_(A,B odd mod 120) [
          alpha_r/2 * {
            U_A(2s+k-1) U_B(2s+k)
            + U_A(2s+k) U_B(2s+k-1)
          }
          + (beta_r-alpha_r)
            U_A(2s+k) U_B(2s+k)
        ],

with r=((A+B-2)/2) mod 60 and (x)_k the rising factorial.

The expansion is absolutely and locally uniformly convergent after Hurwitz continuation: a,b>=3 implies 1/(ab)<=1/9, so the k-tail decays geometrically up to polynomial factors. Only the k=2 constant-weight term and the k=3 linear-weight terms have double Hurwitz poles at s=0. Terms with at most one Hurwitz pole are multiplied by (2s)_k=O(s) and have no residue.

## 5. Exact residue calculation

For every odd residue class,

    U_A(1+2s) = 1/(240s) + O(1).

At k=2, the double pole in the (beta-alpha) term contributes

    sum_(r)(beta_r-alpha_r)/480.

At k=3, the two symmetric alpha terms contribute

    sum_(r) alpha_r/480.

Therefore

    Res_(s=0) H_rho(s)
      = [sum(beta-alpha)+sum(alpha)]/480
      = sum(beta)/480
      = d_rho/960.

The boundary sums B and C are regular at zero. Substitution into the degree split gives

    Res zeta_(0,rho) = d_rho/960,
    Res zeta_(1,rho) = 2*d_rho/960 = d_rho/480.

Their cancellation in -2*zeta_0+zeta_1 is exact.

## 6. Nine-sector residue table

| rho | dimension | Res zeta_0(0) | Res zeta_1(0) |
|---|---:|---:|---:|
| 1 | 1 | 1/960 | 1/480 |
| 2 | 2 | 1/480 | 1/240 |
| 2' | 2 | 1/480 | 1/240 |
| 3 | 3 | 1/320 | 1/160 |
| 3' | 3 | 1/320 | 1/160 |
| 4 | 4 | 1/240 | 1/120 |
| 4' | 4 | 1/240 | 1/120 |
| 5 | 5 | 1/192 | 1/96 |
| 6 | 6 | 1/160 | 1/80 |

## 7. Consequence for determinants

There is no ordinary zeta-regularized determinant for either degree separately under the unmodified definition exp(-zeta'_k(0)), because each zeta function has a simple pole at zero. A finite-part determinant could be introduced, but it requires an explicit subtraction and scale convention; it is not canonical from the alternating torsion alone.

The combined torsion derivative remains well-defined. T044's exact algebraic sector values are therefore the natural invariant delivered by the Rumin alternating complex, not the difference of two already-defined ordinary determinants.

## 8. Reproducibility

Files:
- src/t045_individual_rumin_zeta_poles.py
- tests/test_t045_individual_rumin_zeta_poles.py

Run:

    python -m pytest tests/test_t045_individual_rumin_zeta_poles.py -q
    python -m src.t045_individual_rumin_zeta_poles

The implementation verifies the exact affine tails, the two Molien moment identities, and the residues in all nine sectors. Tests have been added; repository pytest and GitHub Actions have not yet been run.

## Status ledger

| Claim | Status |
|---|---|
| Affine period-60 Molien tails | Exact polynomial consequence |
| Sum alpha = sum beta = dim(rho)/2 | Exact |
| Hurwitz/binomial representation near zero | Exact locally convergent continuation |
| Interior residue dim(rho)/960 | Exact |
| Separate degree-zeta residues | Exact |
| Pole cancellation in alternating torsion | Exact |
| Individual ordinary determinants | Not defined without renormalization |
| Hadamard finite-part determinants | Open; convention must be fixed |

## References

1. A. Kitaoka, *Analytic Torsions Associated with the Rumin Complex on Contact Spheres*, arXiv:1911.03092.
2. T032, exact Molien numerators and dimensions for the nine irreducible 2I representations.
3. T042–T044, alternating Rumin torsion, Hurwitz continuation, and exact Gamma reductions.
