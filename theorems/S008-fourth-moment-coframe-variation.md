# S.8 — Algebraic fourth-moment coframe variation

**Status: PROVED conditional Euler derivatives for the displayed local action.** The finite-difference implementation checks are separate evidence and have not been run as part of this edit. This is an algebraic constitutive source, not a complete gravitational field equation.

## 1. Action density and variables

Let \(e^a{}_i\) be an orientation-preserving nonsingular spatial coframe, let
\[
h_{ij}=\delta_{ab}e^a{}_ie^b{}_j,
\]
and let \(N>0\) be a lapse. Let \(Q_{ab}\in\operatorname{Sym}_0(3)\) be independent of the coframe and let \(R_{abcd}\) be the material fourth-moment residual. Define
\[
V(Q)=\frac{\lambda}{2}R_{abcd}Q^{ab}Q^{cd},
\qquad
\mathcal L_{\mathrm{aniso}}=N\sqrt h\,V(Q).
\]
For an orientation-preserving coframe, \(\sqrt h=\det(e)>0\).

## 2. Exact first variations

Since
\[
\delta\sqrt h=\sqrt h\,e_a{}^i\,\delta e^a{}_i,
\]
and \(R,Q\) are held fixed under the coframe variation,
\[
\boxed{\frac{\partial\mathcal L_{\mathrm{aniso}}}{\partial e^a{}_i}
=N\sqrt h\,V(Q)e_a{}^i.}
\]
The lapse derivative is
\[
\boxed{\frac{\partial\mathcal L_{\mathrm{aniso}}}{\partial N}
=\sqrt h\,V(Q),}
\]
and the symmetric-trace-free \(Q\)-derivative is
\[
\boxed{\frac{\partial V}{\partial Q^{ab}}=\lambda R_{abcd}Q^{cd}.}
\]

### Proof

For \(h=e^Te\) in internal/spatial index notation, the determinant variation gives
\[
\delta\det(e)=(\det e)\operatorname{tr}(e^{-1}\delta e)
=\sqrt h\,e_a{}^i\delta e^a{}_i.
\]
The potential \(V(Q)\) has no explicit dependence on \(e\) or \(N\), so the first two formulae follow by product differentiation. Full symmetry of \(R\) gives the \(Q\)-derivative; because \(R\) has vanishing pair contractions, the result remains symmetric and trace-free.

## 3. Why this does not generate torsion

The displayed action contains no derivatives of \(e\). It therefore cannot by itself generate a Weitzenböck torsion contribution. Torsion remains a separately defined differential object,
\[
T^a=de^a+\omega^a{}_b\wedge e^b.
\]
A torsion response or spin current requires a derivative coupling and a consistent variation of the flat spin connection (or a specified covariant teleparallel formulation). There is no admissible direct map from the fully symmetric \(R_{abcd}\) to the antisymmetric torsion index pair.

The derivative connection coupling and its current are treated separately in S.6. TEGR/Einstein terms, matter, constraints, boundary terms and any flat-connection condition must be included before deriving a complete gravitational Euler equation.

## 4. Evidence classification

- **PROVED:** the local algebraic first variations for the displayed action under the stated independent-variable convention.
- **IMPLEMENTED, NOT EXECUTION-CERTIFIED HERE:** central finite-difference checks of coframe, lapse and trace-free \(Q\) derivatives, plus simultaneous internal-frame covariance of \(R\) and \(Q\), are supplied by the companion source/tests.
- **CANDIDATE:** the algebraic fourth-moment constitutive sector.
- **OPEN:** complete coframe field equations; derivative/spin-connection coupling; teleparallel torsion dynamics; Q6/Yang–Mills coupling; continuum/Mosco convergence.

Companion source and tests are imported into this repository as src/rgs_fourth_moment_variation.py and tests/test_rgs_fourth_moment_variation.py.
