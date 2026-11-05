# T043 — Twisted Rumin torsion on the nine 2I sectors

T043 extends T042 to the nine irreducible 2I sectors, using the exact Molien multiplicities in T032. The eigenvalue is Lambda_m(p)=(m+2p(m-p))^2/4.

For each irrep rho, write A_rho(t)=sum_m b_(m,rho)t^m=N_rho(t)/((1-t^12)(1-t^20)). The alternating zeta functions are zeta_0,rho=b_(0,rho)+sum_(m>=1)b_(m,rho)sum_(p=0)^m Lambda_m(p)^(-s), and zeta_1,rho=2sum_(m>=0)b_(m,rho)sum_(p=1)^(m+1)Lambda_m(p)^(-s).

The interior terms cancel exactly in kappa_rho=-2zeta_0,rho+zeta_1,rho. The zero mode also cancels the two unit middle modes. Thus kappa_rho(s)=2*4^s*sum_(n>=1)d_(n,rho)n^(-2s), where D_rho(t)=(t^2-1)(A_rho(t)-b_(0,rho)).

Because the Molien denominator divides 1-t^60, P_rho=(1-t^60)D_rho is an integer polynomial. Each sector therefore has an exact finite Hurwitz-zeta continuation and a finite Gamma-product formula for T_rho, with 2log(T_rho)=kappa_rho'(0).

The code, tests, complete sector polynomials, finite terms, and residue-class representatives are in the accompanying source and JSON report. The numerical sector values and the regular-representation check are tabulated in the next sections.

## Sector values

High-precision evaluation:

| rho | dimension | T_rho |
|---|---:|---:|
| 1 | 1 | 1.3159472534785811492 |
| 2 | 2 | 0.1909830056250525759 |
| 2' | 2 | 1.3090169943749474241 |
| 3 | 3 | 0.5527864045000420607 |
| 3' | 3 | 1.4472135954999579393 |
| 4 | 4 | 1.6666666666666666667 |
| 4' | 4 | 1 |
| 5 | 5 | 1.5 |
| 6 | 6 | 2 |

The trivial sector reproduces T042: T_1=2 pi^2/15. The eight nontrivial decimal values match the candidates (3-sqrt(5))/4, (3+sqrt(5))/4, (5-sqrt(5))/5, (5+sqrt(5))/5, 5/3, 1, 3/2, 2, in the order 2,2',3,3',4,4',5,6. These are numerical recognitions; independent exact Gamma-product proofs remain open.

## Regular-representation check

The regular representation is the direct sum of dim(rho) copies of each rho, with sum dim(rho)^2=120. The weighted product product_rho T_rho^dim(rho) agrees at 50-digit precision with 16 pi^2, the covering-sphere volume in Kitaoka's normalization. This is a numerical consistency check, not a replacement for the sectorwise derivation.

## Reproducibility and status

Files:
- src/t043_twisted_2i_rumin_torsion.py
- tests/test_t043_twisted_2i_rumin_torsion.py
- data/t043_twisted_2i_rumin_torsion.json

Run:
    python -m pytest tests/test_t043_twisted_2i_rumin_torsion.py -q
    python -m src.t043_twisted_2i_rumin_torsion --max-degree 100 --dps 50

Preparation checks: nine exact polynomial identities and period tails; dimension decomposition through degree 120; finite-cutoff cancellation at s=5/4 and s=2, cutoff 35, in all sectors; 60-digit Gamma-product evaluation and regular weighted product. Repository pytest and GitHub Actions have not yet been run.

Exact: Molien sectors, cancellation, period-60 polynomials, finite Hurwitz continuations, Gamma-product formulas.
Numerical: decimal torsion values and regular product versus 16 pi^2.
Open: exact proofs of the eight algebraic reductions; separate degree zeta derivatives; non-flat or non-unitary coefficients.

References: Kitaoka, Analytic Torsions Associated with the Rumin Complex on Contact Spheres, arXiv:1911.03092; T032 Molien multiplicities; T037 isotypic decomposition; T040-T042 boundary and trivial-sector audits.
