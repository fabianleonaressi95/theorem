# T040 — Exceptional Rumin boundary spectrum as Barnes double zeta

## Objective

Continue T039 from finite-group multiplicities to an exact spectral-zeta representation for the two exceptional Rumin boundary families. The two orientations VI and VII are kept distinct throughout; no torsion sign or complexification convention is silently inserted.

## 1. Exact multiplicity generating function

For either boundary family, T039 identifies the SU(2) degree as \(m=n-1\), where \(n\geq1\) is the positive boundary index. On the untwisted spherical space form \(S^3/2I\), the multiplicity is the trivial-irrep multiplicity

\[
a_m=[t^m]M_{\mathbf 1}(t),\qquad
M_{\mathbf 1}(t)=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]

Equivalently,

\[
a_m=\#\{(r,s)\in\mathbb Z_{\geq0}^2:12r+20s=m\}
+\#\{(r,s)\in\mathbb Z_{\geq0}^2:30+12r+20s=m\}.
\]

The two supports do not overlap: the first contains degrees divisible by 4, while the second contains degrees congruent to 2 modulo 4. Thus every contribution is counted once.

The exceptional boundary eigenvalue is

\[
\lambda_n=\frac{(n+1)^2}{4}=\frac{(m+2)^2}{4}.
\]

## 2. Spectral zeta and Barnes representation

For one boundary orientation define, initially for \(\Re(s)>1\),

\[
Z_{\partial}(s)=\sum_{n=1}^{\infty}a_{n-1}\lambda_n^{-s}
=4^s\sum_{r,s'\geq0}(2+12r+20s')^{-2s}
+4^s\sum_{r,s'\geq0}(32+12r+20s')^{-2s}.
\]

Using the Barnes double zeta

\[
\zeta_2(z,a\mid\omega_1,\omega_2)
=\sum_{r,s'\geq0}(a+r\omega_1+s'\omega_2)^{-z},
\]

this becomes the exact identity

\[
\boxed{
Z_{\partial}(s)=4^s\left[
\zeta_2(2s,2\mid12,20)+
\zeta_2(2s,32\mid12,20)
\right].
}
\]

The series is absolutely convergent for \(\Re(s)>1\): the number of lattice points with \(r+s'\) of order \(R\) grows linearly in \(R\), while each summand is of order \(R^{-2\Re(s)}\). The standard meromorphic continuation of the Barnes double zeta therefore supplies a meromorphic continuation of this boundary spectral zeta.

The two boundary orientations have the same scalar spectrum and multiplicities, but are retained as separate geometric sectors. If a later complex or torsion convention counts both with equal weight, their combined zeta is twice the one-orientation expression. That factor must be fixed from the full Rumin complex and its grading, not assumed here.

## 3. Determinant versus analytic torsion

The one-orientation zeta-regularized log determinant, if the regularized value is defined by this continuation, is

\[
\log\det_{\zeta}(\Delta_{\partial})=-Z'_{\partial}(0).
\]

T040 does not numerically evaluate this derivative and does not identify this single boundary determinant with the analytic torsion of the full Rumin complex. The latter requires all degrees, the correct alternating weights, zero-mode treatment, and the boundary-to-middle matching.

## 4. Implementation and checks

- \`src/t040_boundary_barnes_zeta.py\`: exact Molien multiplicities, boundary levels, Barnes parameters, finite partial sums, JSON audit.
- \`tests/test_t040_boundary_barnes_zeta.py\`: direct lattice-count comparison through degree 120, exact eigenvalue checks in both orientations, first invariant degrees, Barnes starts/periods, and orientation separation.
- \`data/t040_boundary_barnes_zeta.json\`: reproducible audit output.

Commands:

\`\`\`bash
python -m pytest tests/test_t040_boundary_barnes_zeta.py -q
python -m src.t040_boundary_barnes_zeta --max-index 40
\`\`\`

## 5. Status ledger

| Statement | Status |
|---|---|
| Boundary degree \(m=n-1\) and eigenvalue \((m+2)^2/4\) | Exact source-derived result, T039 |
| Untwisted multiplicity generating function | Exact T032 Molien coefficient |
| Barnes double-zeta identity | Exact rearrangement of the absolutely convergent series for \(\Re(s)>1\) |
| Meromorphic continuation | Inherited from Barnes double zeta |
| Numerical value of \(Z'_{\partial}(0)\) | Not evaluated here |
| Full Rumin analytic torsion | Open; requires complete graded spectrum and sign/zero-mode conventions |

## References

1. T039, \`theorems/T039-rumin-boundary-2i-sectors.md\`.
2. T032, \`src/t032_2i_molien.py\`, trivial-irrep numerator \(1+t^{30}\).
3. A. Kitaoka, *Analytic torsions associated with the Rumin complex on contact spheres*, arXiv:1911.03092, Proposition 1.1 cases VI/VII and section 2.3.
4. Barnes double zeta: standard definition and meromorphic continuation; the identity above is derived directly from the two-generator Molien denominator.

## Classification

This task closes the exact one-orientation untwisted boundary spectral-zeta reduction. It does not close the analytic torsion problem for the entire Rumin complex.
