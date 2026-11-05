# T021 — Character-twisted Rumin analytic torsion on the Poincaré sphere

**Status:** exact finite-group/Molien reduction established. T022 supplies the corrected eventual Hurwitz decomposition; T023 supplies exact Gamma-to-sine reductions (currently under review in PR #20); T024 proves the three-dimensional Kitaoka/Rumin–Seshadri operator and torsion-convention matching. The determinant-line volume normalization for the trivial local system is treated below. This remains an audit theorem with explicit hypotheses and does not imply any Q6/PRISM continuum result.

**Object:** the quotient (M=S^3/2I), where (2I\subset SU(2)) is the binary icosahedral group of order 120.

**Depends on:** [T010 — Rumin spectral reduction](T010-rumin-spectrum-poincare-sphere.md), and the detailed derivation in [Kitaoka–Rumin formula audit](../bibliography/spin-geometry-quaternionic/KITAOKA_RUMIN_FORMULA_AUDIT.md).

## 1. Spectral input from Kitaoka

For the three-dimensional case (n=1), the eigenvalue in the interior (i=j=0) sector of Kitaoka's Theorem 0.1 is

\[
\lambda_{q,p}
=\frac{(p(q+1)+q(p+1))^2}{4}
=\frac{(2pq+p+q)^2}{4}.
\]

Put (m=p+q\). Then

\[
\boxed{\Lambda_m(p)=\frac{(m+2p(m-p))^2}{4}.}
\]

On restriction from (U(2)) to (SU(2)), the type with highest weight ((q,-p)) becomes

\[
V(q,-p)|_{SU(2)}\cong \operatorname{Sym}^{m}(\mathbb C^2).
\]

For an irreducible representation \(\rho\) of (2I\), let

\[
b_{m,\rho}
=\dim\operatorname{Hom}_{2I}
\bigl(V_\rho,\operatorname{Sym}^{m}(\mathbb C^2)\bigr)
=\frac1{120}\sum_{[g]}|[g]|\,
\overline{\chi_\rho(g)}\chi_m(g).
\]

Here \(\chi_m\) is the (SU(2)) character of \(\operatorname{Sym}^m\). The bar is harmless for the real-valued character table of (2I), but is retained to make the projection convention explicit.

For the trivial representation, \(b_{m,1}=\dim(\operatorname{Sym}^m\mathbb C^2)^{2I}\).

## 2. The paired zeta combination and its correction term

Using Kitaoka's convention (0^s=1), the scalar and middle-degree zeta sums for the \(\rho\)-isotypic multiplicities take the form

\[
\zeta_{0,\rho}(s)
= b_{0,\rho}
+\sum_{m\ge1}b_{m,\rho}
\sum_{p=0}^{m}\Lambda_m(p)^{-s},
\]

\[
\zeta_{1,\rho}(s)
=2\sum_{m\ge0}b_{m,\rho}
\sum_{p=1}^{m+1}\Lambda_m(p)^{-s}.
\]

The (m=0) contribution must be treated with the stated zero-mode convention; it is not legitimate to silently discard it. Pairing the interior terms gives

\[
\boxed{
\kappa_\rho(s)
=-2\zeta_{0,\rho}(s)+\zeta_{1,\rho}(s)
=2\,4^s\sum_{m\ge1}b_{m,\rho}
\bigl((m+2)^{-2s}-m^{-2s}\bigr).
}
\]

Define the Molien covariant series

\[
M_\rho(t)=\sum_{m\ge0}b_{m,\rho}t^m
=\frac{N_\rho(t)}{(1-t^{12})(1-t^{20})}.
\]

The correct generating function for the paired difference is

\[
\boxed{
D_\rho(t)
=\sum_{m\ge1}b_{m,\rho}(t^{m+2}-t^m)
=(t^2-1)M_\rho(t)+b_{0,\rho}(1-t^2).
}
\]

The final correction term is essential. Omitting it produces incorrect torsion values for representations with \(b_{0,\rho}\ne0\).

## 3. Molien covariants for all nine irreducibles

Use the irreducible labels and character-row ordering fixed in the accompanying audit. All nine covariant Hilbert series have the common denominator \((1-t^{12})(1-t^{20})\). Their numerators are:

| \(\rho\) | \(N_\rho(t)\) |
|---|---|
| \(1\) | \(1+t^{30}\) |
| \(2\) | \(t+t^{11}+t^{19}+t^{29}\) |
| \(2'\) | \(t^7+t^{13}+t^{17}+t^{23}\) |
| \(3\) | \(t^2+t^{10}+t^{12}+t^{18}+t^{20}+t^{28}\) |
| \(3'\) | \(t^6+t^{10}+t^{14}+t^{16}+t^{20}+t^{24}\) |
| \(4\) | \(t^6+t^8+t^{12}+t^{14}+t^{16}+t^{18}+t^{22}+t^{24}\) |
| \(4'\) | \(t^3+t^9+t^{11}+t^{13}+t^{17}+t^{19}+t^{21}+t^{27}\) |
| \(5\) | \(t^4+t^8+t^{10}+t^{12}+t^{14}+t^{16}+t^{18}+t^{20}+t^{22}+t^{26}\) |
| \(6\) | \(t^5+t^7+t^9+t^{11}+t^{13}+2t^{15}+t^{17}+t^{19}+t^{21}+t^{23}+t^{25}\) |

These are covariant multiplicity series, not merely the invariant series for the trivial representation. They were obtained by the finite character average and checked in exact arithmetic over \(\mathbb Q(\sqrt5)\).

## 4. Meromorphic continuation by a finite Hurwitz-zeta sum

Since both 12 and 20 divide 60, the denominator of \(M_\rho\) divides \(1-t^{60}\). Therefore

\[
P_\rho(t)=(1-t^{60})D_\rho(t)
\]

is a polynomial. Write

\[
P_\rho(t)=\sum_{n\ge0}p_{n,\rho}t^n,
\qquad
d_{r,\rho}=\sum_{n\equiv r\ (\mathrm{mod}\ 60)}p_{n,\rho},
\quad 1\le r\le60.
\]

Then the coefficient sequence of \(D_\rho\) is periodic with period 60, and

\[
\boxed{
\kappa_\rho(s)
=2\,4^s\,60^{-2s}
\sum_{r=1}^{60}d_{r,\rho}
\zeta_H\!\left(2s,\frac r{60}\right).
}
\]

This is a finite meromorphic continuation. The only possible poles are inherited from the Hurwitz zeta factors; the expression is regular at (s=0) after the finite combination is taken.

With the convention \(\log T_\rho=\tfrac12\kappa_\rho'(0)\), differentiation yields

\[
\boxed{
\log T_\rho
=\sum_{r=1}^{60}d_{r,\rho}
\left[
(\log4-2\log60)\left(\frac12-\frac r{60}\right)
+2\log\Gamma\!\left(\frac r{60}\right)
-\log(2\pi)
\right].
}
\]

This formula is an exact finite Gamma-product expression. The numerical evaluations below verify the resulting values to high precision; a separate symbolic reduction of every Gamma product to the displayed algebraic number is still desirable.

## 5. Torsion values and independent benchmark

The 50-digit evaluations of the finite Gamma products give:

| (2I)-irrep | (T_\rho) from the finite Hurwitz/Gamma sum | Algebraic benchmark |
|---|---:|---:|
| (1) | 1.315947253478581149177932… | \(2\pi^2/15\) in the contact metric |
| (2\) | 0.190983005625052575897707… | \((3-\sqrt5)/4\) |
| (2'\) | 1.309016994374947424102293… | \((3+\sqrt5)/4\) |
| (3\) | 0.552786404500042060718165… | \(1-1/\sqrt5\) |
| (3'\) | 1.447213595499957939281835… | \(1+1/\sqrt5\) |
| (4\) | 1.666666666666666666666667… | \(5/3\) |
| (4'\) | 1 | (1) |
| (5\) | 1.5 | (3/2\) |
| (6\) | 2 | (2\) |

**Label convention:** the rows called (3) and (3') here are interchanged relative to Dowker–Chang's naming convention. The values, not the bare labels, are the comparison invariant. The spinorial (4') row is Dowker's (4_s).

For the trivial representation, the unit round metric gives \(T=|S^3|/120=\pi^2/60\). Kitaoka's contact metric is (4g_{\rm std}); in dimension three its volume is multiplied by (4^{3/2}=8), giving \(2\pi^2/15\). This metric scaling must be stated whenever the trivial-twist value is compared.

Dowker–Chang independently report the same algebraic torsion values for the spherical space form, including the two conjugate quaternionic two-dimensional twists. Their real-versus-complex bundle convention is explained in their footnote: do not square the values a second time when using their stated real-twist convention.

## 6. What this establishes — and what it does not

**Established algebraically / by finite character computation**
1. The (2I)-multiplicities are finite character averages.
2. The nine covariant Molien series above have the stated common denominator and numerators.
3. The paired zeta series has the corrected generating function \(D_\rho(t)\), including the \(b_{0,\rho}\) correction.
4. The period-60 reduction to a finite Hurwitz-zeta sum follows exactly.
5. High-precision Gamma-product evaluations agree with the independent Dowker–Chang torsion table, with the label and metric conventions stated above.

**Remaining qualifications**
1. The exact Gamma-to-sine proof is recorded in T023 and awaits review/merge of PR #20.
2. The operator and sign-convention identification is proved separately in [T024](T024-rumin-kitaoka-operator-matching-3d.md); it uses the special fact that all Kitaoka rescaling factors equal one when the contact dimension is three.
3. No theorem about PRISM/Q6 continuum limits, Yang–Mills, or physical matter follows from this finite-group torsion calculation.

## 7. Reproducibility and next proof obligations

The detailed source extraction and character calculation are maintained in:

- [KITAOKA_RUMIN_FORMULA_AUDIT.md](../bibliography/spin-geometry-quaternionic/KITAOKA_RUMIN_FORMULA_AUDIT.md)
- [RUMIN_2I_N1_CHARACTER_AUDIT.py](../bibliography/spin-geometry-quaternionic/RUMIN_2I_N1_CHARACTER_AUDIT.py)

Acceptance tests for the next iteration:

1. Re-run the script at 80+ decimal digits and export every \(N_\rho\), \(P_\rho\), and residue vector \((d_{1,\rho},\ldots,d_{60,\rho})\).
2. Verify the nine character projections against orthogonality of the full (2I) character table and \(\sum_\rho (\dim\rho)^2=120\).
3. Prove the Gamma-product simplifications symbolically, or explicitly retain them as exact finite products without claiming the algebraic simplification.
4. Match Kitaoka's \(\kappa\), Rumin–Seshadri's torsion, and Ray–Singer's determinant-line conventions term by term.
5. Keep the central Rumin differential/intertwiner construction as a separate open task; the scalar spectral calculation alone does not determine the full differential complex.

## References

1. A. Kitaoka, *Analytic torsions associated with the Rumin complex on contact spheres*, Int. J. Math. 31 (2020), 2050112, [arXiv:1911.03092](https://arxiv.org/abs/1911.03092).
2. M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), 727–782, [DOI: 10.5802/aif.2693](https://doi.org/10.5802/aif.2693).
3. J. S. Dowker and P. Chang, *Analytic torsion on spherical factors and tessellations*, [arXiv:0904.0744](https://arxiv.org/abs/0904.0744).
4. A. Kitaoka, *Ray–Singer Torsion and the Rumin Laplacian on Lens Spaces*, SIGMA 18 (2022), 091, [arXiv:2009.03276](https://arxiv.org/abs/2009.03276).

## Classification

- **Exact derivation:** character projection, Molien covariants, period-60 Hurwitz reduction.
- **High-precision numerical verification:** all nine torsion values and the contact-volume scaling.
- **Independent published benchmark:** Dowker–Chang spherical-space-form table.
- **Open/review:** acceptance of the exact Gamma identities in T023 (PR #20). The dimension-three operator and torsion-convention matching is proved in T024.


## 8. Erratum: eventual period versus the initial Dirichlet segment

The period-60 statement above must be interpreted as an **eventual** period, not necessarily a period beginning at the first representative (r\in\{1,\ldots,60\}). Let
\[
P_\rho(t)=(1-t^{60})D_\rho(t)=\sum_n p_{n,\rho}t^n,
\qquad
c_{n,\rho}=[t^n]D_\rho(t)=\sum_{j\ge0}p_{n-60j,\rho}.
\]
For each residue class with nonzero eventual tail, set
\[
N_{r,\rho}=\max\{n:p_{n,\rho}\ne0,\ n\equiv r\pmod{60}\},
\qquad
d_{r,\rho}=\sum_{n\equiv r\pmod{60}}p_{n,\rho}.
\]
Then (c_{n,\rho}=d_{r,\rho}) only for (n\ge N_{r,\rho}) in that residue class. Consequently the exact decomposition is
\[
\kappa_\rho(s)=2\,4^s\left[
\sum_r\sum_{\substack{n<N_{r,\rho}\\n\equiv r\ (60)}}
c_{n,\rho}n^{-2s}
+
\sum_r d_{r,\rho}N_{r,\rho}^{-2s}
\zeta_H\!\left(2s,\frac{N_{r,\rho}}{60}\right)
\right],
\]
with residue classes having no tail kept wholly in the finite sum. Differentiating at zero gives
\[
\begin{aligned}
\log T_\rho={}&
\sum_r\sum_{\substack{n<N_{r,\rho}\\n\equiv r\ (60)}}
c_{n,\rho}(\log4-2\log n)\\
&+\sum_r d_{r,\rho}\left[
(\log4-2\log N_{r,\rho})
\left(\frac12-\frac{N_{r,\rho}}{60}\right)
+2\log\Gamma\!\left(\frac{N_{r,\rho}}{60}\right)
-\log(2\pi)
\right].
\end{aligned}
\]
For the trivial representation the residue class (r=2) has tail start (N=62), so its Hurwitz parameter is (31/30), not (1/30). The earlier compact formula with (zeta_H(2s,r/60)) and (Gamma(r/60)) omits the initial-segment correction and must not be used as written. The 50-digit values remain to be accepted only after this corrected decomposition is applied to all nine representations. This erratum supersedes the unqualified period-60 formula in §§4–5.


## 9. Erratum II: correct scaling of the eventual Hurwitz tail

A second correction is required in the displayed formula of §8. If a residue-class tail begins at (N_{r,\rho}), its terms are
\[
\sum_{k\ge0}(N_{r,\rho}+60k)^{-2s}
=60^{-2s}\zeta_H\!\left(2s,\frac{N_{r,\rho}}{60}\right),
\]
not (N_{r,\rho}^{-2s}\zeta_H(2s,N_{r,\rho}/60)). The latter inserts an erroneous extra scale factor. Thus the corrected continuation is
\[
\kappa_\rho(s)=2,4^s\left[
\sum_r\sum_{\substack{n<N_{r,\rho}\\n\equiv r\ (60)}}
c_{n,\rho}n^{-2s}
+60^{-2s}\sum_r d_{r,\rho}
\zeta_H\!\left(2s,\frac{N_{r,\rho}}{60}\right)
\right].
\]
Its derivative, with \(\log T_\rho=\tfrac12\kappa_\rho'(0)\), is
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
The finite initial segment is unchanged; only the scale in the eventual tail is corrected. In particular, the trivial representation has the tail start \(N=62\) in residue 2, with Hurwitz parameter \(31/30\), while the global scaling remains \(60^{-2s}\).

The new standalone audit
`bibliography/spin-geometry-quaternionic/RUMIN_2I_T022_EVENTUAL_HURWITZ_AUDIT.py`
implements the nine Molien numerators, constructs each polynomial \(P_\rho=(1-t^{60})D_\rho\), checks every finite preperiod and eventual tail coefficient, and compares the resulting 70-digit torsions with the independent algebraic benchmark. This is a **high-precision numerical verification** of the corrected finite decomposition; it is not a symbolic proof of all nine Gamma-product identities, nor does it settle the operator-convention matching described in §6.
