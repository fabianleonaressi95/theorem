# T022 — Eventual-period Hurwitz audit for all Rumin twists on S³/2I

**Status:** corrected finite Hurwitz decomposition established algebraically from the Molien numerators; all nine resulting torsion values independently reproduced at high precision and agree with the Dowker–Chang algebraic benchmark. The standalone script is committed with this note. Symbolic reduction of all nine Gamma products and operator-level convention matching remain open.

## 1. Purpose

T021 §§4 and 8 contained an unqualified period-60 formula. The period is eventual, and a second scaling correction is necessary: for a tail beginning at (N),
\[
\sum_{k\ge0}(N+60k)^{-2s}
=60^{-2s}\zeta_H(2s,N/60).
\]
It is not (N^{-2s}\zeta_H(2s,N/60)). T021 §9 records this second erratum.

## 2. Exact coefficient construction

For each irreducible (\rho\), use the Molien covariant series
\[
M_\rho(t)=\sum_{m\ge0}b_{m,\rho}t^m
=\frac{N_\rho(t)}{(1-t^{12})(1-t^{20})}.
\]
The paired spectral series is
\[
D_\rho(t)=\sum_{m\ge1}b_{m,\rho}(t^{m+2}-t^m)
=(t^2-1)M_\rho(t)+b_{0,\rho}(1-t^2).
\]
Since (12,20\mid60),
\[
P_\rho(t)=(1-t^{60})D_\rho(t)=\sum_np_{n,\rho}t^n
\]
is a polynomial. Its coefficient sequence satisfies
\[
c_{n,\rho}=[t^n]D_\rho
=\sum_{j\ge0}p_{n-60j,\rho}.
\]
For each residue class (r\pmod{60}) with nonzero tail define
\[
N_{r,\rho}=\max\{n:p_{n,\rho}\ne0,\ n\equiv r\pmod{60}\},
\qquad d_{r,\rho}=\sum_{n\equiv r\pmod{60}}p_{n,\rho}.
\]
Then (c_{n,\rho}=d_{r,\rho}) only for (n\ge N_{r,\rho}). Coefficients below that threshold remain in the finite Dirichlet segment.

## 3. Correct continuation and torsion derivative

The exact continuation is
\[
\kappa_\rho(s)=2,4^s\left[
\sum_r\sum_{\substack{n<N_{r,\rho}\\n\equiv r\ (60)}}
c_{n,\rho}n^{-2s}
+60^{-2s}\sum_r d_{r,\rho}
\zeta_H\!\left(2s,\frac{N_{r,\rho}}{60}\right)
\right].
\]
With (\log T_\rho=\frac12\kappa_\rho'(0)),
\[
\begin{aligned}
\log T_\rho={}&
\sum_r\sum_{\substack{n<N_{r,\rho}\\n\equiv r\ (60)}}
c_{n,\rho}(\log4-2\log n)\\
&+\sum_r d_{r,\rho}\left[
(\log4-2\log60)\left(\frac12-\frac{N_{r,\rho}}{60}\right)
+2\log\Gamma\!\left(\frac{N_{r,\rho}}{60}\right)
-\log(2\pi)
\right].
\end{aligned}
\]

## 4. Numerical results

The corrected computation gives the following values (the 70-digit audit is in the script; rounded here):

| (\rho\) | (T_\rho) | Algebraic benchmark |
|---|---:|---:|
| (1) | 1.315947253478581149177932… | (2\pi^2/15) |
| (2) | 0.190983005625052575897707… | ((3-\sqrt5)/4) |
| (2'\) | 1.309016994374947424102293… | ((3+\sqrt5)/4) |
| (3) | 0.552786404500042060718165… | (1-1/\sqrt5) |
| (3'\) | 1.447213595499957939281835… | (1+1/\sqrt5) |
| (4) | 1.666666666666666666666667… | (5/3) |
| (4'\) | 1 | (1) |
| (5) | 1.5 | (3/2) |
| (6) | 2 | (2) |

The (3,3'\) labels are interchanged relative to Dowker–Chang. The trivial twist uses the contact metric normalization (4g_{\rm std}), hence (T_1=2\pi^2/15), eight times the unit-round quotient volume (\pi^2/60).

## 5. Reproducibility

Run:
```bash
python bibliography/spin-geometry-quaternionic/RUMIN_2I_T022_EVENTUAL_HURWITZ_AUDIT.py
```
Requires SymPy. The script:
- reconstructs all nine (D_\rho) from their exact Molien numerators;
- proves (P_\rho\) is a polynomial in exact rational arithmetic;
- extracts finite initial coefficients and tail starts separately;
- checks the eventual coefficient identity in every residue class;
- evaluates the corrected Gamma expression and compares it with the independent algebraic benchmarks at 70-digit precision;
- emits JSON containing polynomial degrees, finite segments, tail starts, values, and residuals.

## 6. Status and remaining proof obligations

**Established exactly:** the coefficient identity, polynomiality of (P_\rho), eventual-period decomposition, and corrected Hurwitz representation, conditional on the Molien numerators already audited in T021.

**Numerically verified:** all nine torsion values agree with the independent Dowker–Chang benchmarks at high precision under the corrected scaling.

**Not claimed:** a symbolic proof of all nine Gamma-product simplifications; an operator-level identification of Kitaoka's modified Rumin Laplacians with the Rumin–Seshadri contact complex, including grading, determinant-line metric, and sign/inverse convention; or any implication for PRISM/Q6 continuum physics.

## References

- A. Kitaoka, *Analytic Torsions associated with the Rumin Complex on Contact Spheres*, arXiv:1911.03092.
- M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), 727–782.
- J. S. Dowker and P. Chang, *Analytic torsion on spherical factors and tessellations*, arXiv:0904.0744.
