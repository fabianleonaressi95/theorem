# T023 — Exact Gamma reflection identities for the Rumin torsion on S³/2I

**Status:** all nine finite Gamma products reduce exactly to the algebraic torsion table by Euler's reflection formula, one Gamma recurrence in the trivial representation, and exact rational-angle sine identities. The reductions are implemented in a SymPy audit over exact algebraic numbers. This closes the Gamma-product simplification obligation left open in T021/T022, conditional on the Kitaoka spectral input and the nine Molien numerators established there.

## 1. Input from T022

For each irreducible (\rho\) of (2I\), T022 gives the corrected eventual-period expression
\[
\log T_\rho=
\sum_r d_{r,\rho}\left[
(\log4-2\log60)\left(\frac12-\frac{N_{r,\rho}}{60}\right)
+2\log\Gamma\!\left(\frac{N_{r,\rho}}{60}\right)
-\log(2\pi)
\right],
\]
with the finite initial segment absent for all nine Molien covariants. The exact tail starts and coefficients are reconstructed from
\[
P_\rho(t)=(1-t^{60})\left((t^2-1)M_\rho(t)+b_{0,\rho}(1-t^2)\right).
\]
For every row,
\[
\sum_r d_{r,\rho}\left(\frac12-\frac{N_{r,\rho}}{60}\right)=0,
\qquad
\sum_r d_{r,\rho}=-\dim\rho.
\]
Thus the explicit scale term cancels.

## 2. Gamma reflection and the exceptional trivial tail

For complementary arguments, Euler reflection gives
\[
\Gamma(x)\Gamma(1-x)=\frac{\pi}{\sin(\pi x)}.
\]
All nontrivial rows pair (N) with (60-N), with equal coefficients. If (N=30), the self-complementary factor is (\Gamma(1/2)=\sqrt\pi\); if (N=60), it is (\Gamma(1)=1\).

The trivial row has one shifted representative: (N=62), paired with (N=58). Here
\[
\Gamma(31/30)=\frac1{30}\Gamma(1/30),
\qquad
\Gamma(1/30)\Gamma(29/30)=\frac{\pi}{\sin(\pi/30)}.
\]
This is the source of the factor (30^{-2}) in its sine product. Omitting this recurrence would give an incorrect result.

After the reflection/recurrence reductions, the torsions take the form
\[
T_1=2\pi^2 S_1,
\qquad
T_\rho=2^{\dim\rho}S_\rho
\quad(\rho\ne1),
\]
where the exact sine products are:

| (\rho\) | (S_\rho) |
|---|---:|
| (1) | (1/15) |
| (2) | ((3-\sqrt5)/16) |
| (2'\) | ((3+\sqrt5)/16) |
| (3) | ((5-\sqrt5)/40) |
| (3'\) | ((5+\sqrt5)/40) |
| (4) | (5/48) |
| (4'\) | (1/16) |
| (5) | (3/64) |
| (6) | (1/32) |

These values are exact identities in (\mathbb Q(\sqrt5)\), obtained by reducing rational-angle sines (angles with denominator 60). In particular, the trivial product includes the shifted (31/30) Gamma factor and is (1/15), yielding the contact-metric volume (2\pi^2/15).

## 3. Resulting torsion table

Substitution gives:

| (\rho) | (T_\rho) |
|---|---:|
| (1) | (2\pi^2/15) |
| (2) | ((3-\sqrt5)/4) |
| (2'\) | ((3+\sqrt5)/4) |
| (3) | (1-1/\sqrt5) |
| (3'\) | (1+1/\sqrt5) |
| (4) | (5/3) |
| (4'\) | (1) |
| (5) | (3/2) |
| (6) | (2) |

The (3,3'\) names are interchanged relative to the convention in Dowker–Chang. The numerical values are unaffected by that relabeling.

## 4. Exact reproducibility

Run:
```bash
python bibliography/spin-geometry-quaternionic/RUMIN_2I_T023_GAMMA_SINE_IDENTITIES.py
```
Requires SymPy. The audit:
1. rebuilds each (P_\rho\) from the Molien numerator and verifies polynomiality over (\mathbb Q\);
2. extracts the eventual tails and checks all complementary coefficient pairs;
3. checks the scale-cancellation identity exactly;
4. applies the exceptional (\Gamma(31/30)\) recurrence for the trivial row;
5. simplifies all nine sine products exactly and asserts equality with the listed elements of (\mathbb Q(\sqrt5)\);
6. reconstructs all nine torsions and checks \(\sum_\rho(\dim\rho)^2=120\).

No floating-point approximation is used in this proof certificate.

## 5. Scope and remaining open problem

**Now established within the spectral setup:** the finite Gamma products from the corrected T022 continuation reduce exactly to the nine algebraic torsion values. The Gamma simplification is no longer merely a high-precision numerical match.

**Still open:** the operator-level comparison between Kitaoka's modified Rumin Laplacians and the Rumin–Seshadri contact complex, including grading, determinant-line metric, and sign/inverse convention. The present calculation does not prove that convention-matching step, nor does it establish any PRISM/Q6 continuum or physical claim.

## References

- A. Kitaoka, *Analytic Torsions associated with the Rumin Complex on Contact Spheres*, arXiv:1911.03092.
- M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), 727–782.
- J. S. Dowker and P. Chang, *Analytic torsion on spherical factors and tessellations*, arXiv:0904.0744.
