# Document C — Pellis Functions and Golden Spheres Resonance: an independent mathematical audit

**Status: DRAFT — working document, not merged into `main`.**

**Prepared for discussion with Stergios Pellis**

**Primary source:** Stergios Pellis, *Fine-Structure Constant via the Golden Spheres Resonance*, dated 11 September 2025, DOI [10.13140/RG.2.2.35410.00968](https://doi.org/10.13140/RG.2.2.35410.00968); SSRN record [5473588](https://ssrn.com/abstract=5473588). The public record identifies this as a preprint. This note treats it as a research proposal, not an established derivation.

**Purpose:** separate the exact algebraic content of the Pellis Function from the proposed geometric and operator interpretations. The goal is a fair, reproducible comparison, without assuming that the proposal is true or dismissing it because some steps remain open.

---

## C.1 Source definitions and notation

The paper uses *Pellis Function* for a family of related constructions, not for one uniquely specified function throughout. Its core fine-structure expression is
\[
P_{\mathrm{core}}(x)=360x^{-2}-2x^{-3}+(3x)^{-5}.
\]
At
\[
\phi=\frac{1+\sqrt5}{2},
\]
the proposed value is \(P_{\mathrm{core}}(\phi)\).

The paper also introduces general sparse or hierarchical expansions, schematically
\[
P_{\mathbf a}(x)=\sum_{k\in S}a_kx^{-k}.
\]
These general families must be distinguished from the fixed three-term expression. Unless the index set \(S\), coefficients \(a_k\), and their selection rule are fixed independently, the general expansion is a parameterized ansatz rather than a unique prediction.

The source interprets the terms as follows:
- \(\phi^{-2}\): surface-like contribution;
- \(\phi^{-3}\): volume-like contribution;
- \((3\phi)^{-5}\): higher-order wave or harmonic correction.

These are interpretations proposed in the source. The exponents alone do not prove that the coefficients \(360,-2,1\), or the factor \(3\), follow from a boundary-value problem or a symmetry principle.

## C.2 Exact algebraic evaluation

### Proposition C.1 — The core expression is an exact quadratic-algebraic number

For \(\phi=(1+\sqrt5)/2\),
\[
\boxed{
P_{\mathrm{core}}(\phi)
=360\phi^{-2}-2\phi^{-3}+(3\phi)^{-5}
=\frac{264373-88447\sqrt5}{486}.
}
\]

### Proof

Use \(\phi^2=\phi+1\), hence
\[
\phi^{-1}=\phi-1,\qquad
\phi^{-2}=2-\phi,\qquad
\phi^{-3}=2\phi-3.
\]
Substitution and reduction in \(\mathbb Q(\sqrt5)\) gives the displayed rational expression. No floating-point fitting is involved. \(\square\)

Its decimal value is
\[
137.0359991647656393450572356414\ldots.
\]
The individual terms are
\[
360\phi^{-2}=137.5077640500378546\ldots,
\]
\[
-2\phi^{-3}=-0.4721359549995794\ldots,
\]
\[
(3\phi)^{-5}=0.0003710697273641\ldots.
\]
The first term is the golden angle in degrees, \(360\phi^{-2}=137.507764\ldots^\circ\). This observation does not by itself derive the two correction terms.

## C.3 Comparison with values quoted in the preprint

The paper quotes the CODATA 2022 inverse fine-structure constant as
\[
\alpha^{-1}=137.035999177(21)
\]
and an electron-\(g\)-factor determination as
\[
\alpha^{-1}=137.035999166(15).
\]
Using those central values as printed, the exact Pellis expression gives:

| Reference value | Absolute difference | Relative absolute difference | Within quoted uncertainty? |
|---|---:|---:|---|
| CODATA 2022: \(137.035999177(21)\) | \(1.2234360655\times10^{-8}\) | \(8.92784431\times10^{-11}\) | Yes |
| Electron-\(g\) value: \(137.035999166(15)\) | \(1.2343606549\times10^{-9}\) | \(9.00756489\times10^{-12}\) | Yes |

The arithmetic confirms close numerical agreement with both values as printed in the source. Compatibility within an experimental uncertainty interval is not a derivation of the measured constant.

### Two numerical statements in the source need correction

1. The preprint reports an absolute CODATA-2022 difference of \(1.12344\times10^{-8}\) and a relative difference of \(8.2\times10^{-11}\). Direct evaluation of its displayed three-term formula against its displayed central value \(137.035999177\) gives \(1.2234360655\times10^{-8}\) and \(8.92784431\times10^{-11}\). The reported pair does not match that arithmetic.
2. The text states \((3\phi)^5\approx6158.64\). Direct calculation gives
   \[
   (3\phi)^5=2694.9112963311\ldots,\qquad
   (3\phi)^{-5}=0.0003710697273641\ldots.
   \]
   The displayed Pellis value is consistent with the reciprocal, not with the quoted fifth-power number.

These are reproducible numerical discrepancies in the explanatory text; they do not change the exact evaluation of the displayed core formula.

## C.4 The general Pellis series: what is mathematically defined

A finite expression
\[
P(x)=\sum_{k\in S}a_kx^{-k}
\]
is an ordinary finite linear combination of powers. For fixed rational coefficients \(a_k\) and \(x=\phi\), its value is an exact element of \(\mathbb Q(\sqrt5)\).

An infinite expansion
\[
P(x)=\sum_{k\geq k_0}a_kx^{-k}
\]
requires a convergence condition. A sufficient condition is
\[
\sum_{k\geq k_0}|a_k|\phi^{-k}<\infty.
\]
If the coefficients are unrestricted, convergence is not automatic. The fact that \(\phi^{-k}<1\) is not sufficient by itself: the coefficient sequence must also be controlled.

For the hierarchy \(R_n=R_0\phi^{-n}\), surface areas scale as \(\phi^{-2n}\) and volumes as \(\phi^{-3n}\). Thus
\[
\sum_{n=0}^{\infty}\phi^{-2n}=\frac{1}{1-\phi^{-2}},
\qquad
\sum_{n=0}^{\infty}\phi^{-3n}=\frac{1}{1-\phi^{-3}}
\]
converge. A weighted sum requires its own summability condition, for example
\[
\sum_{n\geq0}|w_n|\phi^{-2n}<\infty.
\]

**Classification:** the finite core formula and elementary geometric-series identities are exact mathematics. A general Pellis expansion becomes a theorem-producing model only after its coefficient space, convergence hypotheses, and coefficient-selection mechanism are specified.

## C.5 Golden Spheres Resonance: geometric scaling versus a wave spectrum

The paper proposes nested radii
\[
R_n=R_0\phi^{-n},\qquad n=0,1,2,\ldots.
\]
This gives
\[
\operatorname{Area}(S_n)=4\pi R_0^2\phi^{-2n},
\qquad
\operatorname{Vol}(B_n)=\frac{4\pi}{3}R_0^3\phi^{-3n}.
\]
The sums of these separate area or volume contributions converge over \(n\geq0\).

A wave spectrum requires more data than the radii. One must specify whether each object is a two-dimensional spherical surface, a three-dimensional ball cavity, a shell, or a coupled region in one physical domain. One must also specify the field equation, propagation speed, boundary conditions, mode labels, and coupling between levels.

For example, if every level is an independent cavity with the same dimensionless boundary spectrum \(\{\zeta_m\}\), then a conditional frequency law is
\[
\omega_{n,m}=\frac{v\zeta_m}{R_n}
=\frac{v\zeta_m}{R_0}\phi^n.
\]
Here \(\zeta_m\) depends on the chosen geometry and boundary condition. For a ball, it is determined by the relevant spherical-Bessel roots; for a field on a spherical surface, it is determined by spherical-harmonic eigenvalues. These are different spectral problems.

Thus inverse-radius scaling is a valid conditional consequence of dimensional analysis. It does not determine \(\zeta_m\), modal degeneracies, or interactions of nested spheres. With shrinking radii, frequencies increase as \(\phi^n\) when wave speed and dimensionless mode label are fixed. Any formula using the opposite power must explain a different convention or physical quantity.

## C.6 A precise operator model for an uncoupled hierarchy

Once a cavity model fixes \(\zeta_m\), one consistent uncoupled model is
\[
\mathcal H_{\mathrm{GSR}}=\ell^2(\mathbb N_0\times\mathcal M),
\]
with orthonormal basis \(e_{n,m}\) and diagonal frequency operator
\[
\Omega e_{n,m}=\omega_{n,m}e_{n,m},
\qquad
\omega_{n,m}=\frac{v\zeta_m}{R_0}\phi^n.
\]
Its natural domain is
\[
D(\Omega)=
\left\{c=(c_{n,m}):
\sum_{n,m}|\omega_{n,m}|^2|c_{n,m}|^2<\infty
\right\}.
\]
For real \(\omega_{n,m}\), this diagonal operator is self-adjoint on the stated domain. It is a direct sum of independent resonators, not yet a model of coupled nested spheres.

A coupled GSR model needs an interaction operator \(V\), specified in the \((n,m)\) basis, and a proof that \(\Omega+V\) is self-adjoint. The coupling must be derived from the geometry or a physical interaction law, not chosen after seeing the desired constant.

This is a possible rigorous completion of the operator language in the preprint; it is not claimed to be the unique operator already defined by that paper.

## C.7 Spectral weights do not automatically generate an arbitrary Pellis sum

For a self-adjoint operator \(A\) with spectral projections \(P_j\), a normalized state \(\Psi\) has
\[
p_j=\langle\Psi,P_j\Psi\rangle\geq0,\qquad \sum_jp_j=1.
\]
Its expectation is
\[
\langle\Psi,A\Psi\rangle=\sum_jp_j\lambda_j,
\]
when \(\Psi\in D(A)\). This is a convex average of the eigenvalues.

Consequently:

1. If the operator eigenvalues are only \(\phi^{-n}\), then \(0\leq\langle A\rangle\leq1\); such an operator cannot have expectation \(137.035999\ldots\).
2. A negative term such as \(-2\phi^{-3}\) cannot be represented as a nonnegative probability weight. It must instead appear in a signed eigenvalue, an interaction term, or a separately defined observable.
3. Choosing modal probabilities after fixing the target value can reproduce a desired expectation, but it is not a prediction. The state must be selected independently by a variational principle, dynamical equation, symmetry rule, or experimental preparation protocol.
4. For a degenerate eigenvalue, the invariant quantity is the weight of the full spectral projection, not a basis-dependent coefficient assigned to one vector.

The preprint's operator discussion (Sections 10–11, equations 112–130) introduces a φ-scaled mode space, weighting coefficients, and a collective state. The mathematical ingredients needed for a definite operator model are still missing from the source as presented: a complete Hilbert-space definition, exact operator domain, normalized mode basis, explicit eigenvalues, and an independently derived state-selection rule.

## C.8 Comparison with the exact \(S^3/2I\) spectrum

Document A gives the scalar Laplacian on the unit round quotient:
\[
\lambda_k=k(k+2),\qquad
d_k=(k+1)[t^k]\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]
Its first positive eigenvalue is \(168\), with multiplicity \(13\). The invariant degrees are controlled by the binary icosahedral invariant ring, with generator degrees \(12,20,30\).

The GSR hierarchy instead starts from \(R_n=R_0\phi^{-n}\) and, after a cavity model is fixed, produces frequencies proportional to \(\phi^n\) times boundary-mode data.

There is no automatic equivalence between these spectra. A rigorous identification would require:
- a common Hilbert space or an explicitly defined unitary map between the two Hilbert spaces;
- a precise GSR operator and a precise geometric operator;
- an intertwining relation, such as \(UA_{\mathrm{GSR}}U^{-1}=cA_0\), or a justified relation between squared frequencies and Laplace eigenvalues;
- matching eigenvalue sets and multiplicities, including zero modes;
- a map preserving the relevant group action, or an explanation of why equivariance is not required.

The appearance of \(\sqrt5\) in the character field of \(2I\), and the appearance of \(\phi\) in the GSR scale factor, are compatible mathematical facts. They do not alone establish a spectral correspondence.

## C.9 Verification and reproducibility

The exact arithmetic is implemented in:
- audits/pellis_gsr_exact_audit.py
- tests/test_pellis_gsr_exact_audit.py

Run from the repository root:

    python -m audits.pellis_gsr_exact_audit
    python -m unittest tests.test_pellis_gsr_exact_audit -v

The audit checks the exact reduction to \((264373-88447\sqrt5)/486\), high-precision evaluation of all three terms, differences from the two central values quoted in the preprint, the discrepancy in its stated absolute/relative errors, and the discrepancy in its stated value of \((3\phi)^5\).

It does not validate a physical resonator, derive the coefficients, establish the Golden Resonance Operator, or derive \(\alpha\).

## C.10 Evidence ledger

| Claim | Classification |
|---|---|
| Core Pellis expression | Definition transcribed from the preprint |
| Exact value \((264373-88447\sqrt5)/486\) | Exact algebraic identity |
| Decimal value \(137.0359991647656\ldots\) | Exact expression numerically evaluated |
| Agreement with quoted \(\alpha^{-1}\) values within quoted uncertainties | Numerical comparison, not derivation |
| \(R_n=R_0\phi^{-n}\) | Proposed geometric scaling law |
| Area and volume sums over the hierarchy | Exact convergent geometric series |
| Cavity frequency \(\omega_{n,m}\propto\phi^n\) | Conditional on fixed boundary spectrum and wave speed |
| Complete GSR mode spectrum and inter-sphere coupling | Not specified sufficiently in the source |
| Golden Resonance Operator with self-adjoint domain | Not yet fully defined in the source |
| Modal weights selected independently by dynamics | Open |
| Equivalence with \(S^3/2I\) spectral geometry | Open; no intertwiner or multiplicity match supplied |

## C.11 Limits and physical interpretation

The exact core expression is a compact algebraic identity in \(\mathbb Q(\sqrt5)\). The geometric hierarchy has convergent area and volume sums. A self-adjoint diagonal model can be constructed after a cavity spectrum is specified.

None of these facts alone establishes that the fine-structure constant is caused by golden-sphere resonance. To reach that conclusion, the coefficients, boundary conditions, mode degeneracies, interactions, and state-selection rule must be derived independently of the target value. The same model should then produce predictions beyond the single number used to motivate it.

The constructive route is:
1. obtain a precise definition of the general Pellis Function and Golden Resonance Operator;
2. freeze one physical cavity model and its boundary conditions;
3. derive the mode spectrum and inter-level coupling;
4. prove self-adjointness and determine the spectral measure;
5. derive the state weights without using \(\alpha^{-1}\) as an input;
6. only then compare the predicted dimensionless observable with experiment and with the \(S^3/2I\) spectrum.

This preserves the mathematical content of Pellis's proposal while identifying exactly which steps would turn it into a reproducible spectral theory.

---

## References

1. S. Pellis, *Fine-Structure Constant via the Golden Spheres Resonance*, 11 September 2025, DOI [10.13140/RG.2.2.35410.00968](https://doi.org/10.13140/RG.2.2.35410.00968), especially §§2–3, §§4–7, and §§10–11. The public full-text record identifies it as a preprint.
2. S. Pellis, same work, SSRN record [5473588](https://ssrn.com/abstract=5473588), posted 2 October 2025.
3. CODATA 2022 and electron-\(g\)-factor central values and uncertainties are quoted as printed in the Pellis preprint; the comparisons above are arithmetic checks of those printed inputs, not an independent metrology update.
4. Document A — [Exact scalar spectral geometry of \(S^3/2I\)](01_exact_scalar_spectrum_poincare_sphere.md).
5. Document B — [Geometric self-adjoint operators and spectral weights](https://github.com/fabianleonaressi95/theorem/blob/collaboration/pellis-document-2-self-adjoint-operators/collaborations/pellis/03_geometric_self_adjoint_operators.md).

**Classification:** exact algebraic core; exact convergence statements under stated hypotheses; conditional cavity scaling; operator realization and physical derivation remain open.
