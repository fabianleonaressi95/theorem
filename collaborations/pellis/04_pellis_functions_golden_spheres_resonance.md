# Document C — Pellis Functions and Golden Spheres Resonance: an independent mathematical audit

**Status: DRAFT — working audit version tracked in `main`; mathematical and physical claims retain the classifications stated below.**

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

## C.12 Vesica Piscis: exact geometry, multi-circle constructions, and the boundary of physical interpretation

### C.12.1 Source scope and evidence policy

A supplementary source supplied for this audit is the *Rapporto Vesica* (reported in the supplied extract as a 2,566-page interdisciplinary report). Its extract groups material into: (i) logical and statistical tools; (ii) standard physics, including relativity and quantum mechanics; (iii) extended or non-mainstream proposals, including scalar/torsion waves, morphic fields, quaternionic reformulations of electromagnetism, zero-point energy and over-unity devices; and (iv) an integrated interpretive chain culminating in the thesis of an artificial holographic prison.

The extract itself explicitly distinguishes standard physics from the extended claims and states that the holographic-prison thesis is interpretive rather than a verifiable derivation. This document adopts that distinction. The report is used here as a source of geometric constructions and research questions, not as evidence that its global ontological or conspiratorial thesis is true.

In particular, the following are not consequences of the standard mathematical statements listed in the report:
- that quantum entanglement establishes telepathy or a morphic information field;
- that the Born rule or Hilbert-space formalism implies that spacetime is an artificial projection;
- that zero-point energy permits a device to deliver net energy without an accounted input;
- that scalar/torsion waves, over-unity devices, or the listed technological claims are experimentally established;
- that the Vesica Piscis, golden ratio, or Platonic solids encode an intentional artificial control structure.

These claims would require separate operational definitions, measurements, and falsifiable predictions. They are not used as premises in the Pellis analysis.

### C.12.2 Definition and exact Euclidean geometry

Let two Euclidean circles have equal radius \(R>0\), with centres \(O_1,O_2\) satisfying
\[
|O_1O_2|=R.
\]
Their intersection is the classical Vesica Piscis. The two intersection points are symmetric about the line \(O_1O_2\). The common chord is perpendicular to \(O_1O_2\) and bisects it. Its half-length is
\[
\sqrt{R^2-(R/2)^2}=\frac{\sqrt3}{2}R,
\]
so the full common-chord length is
\[
\boxed{L_{\mathrm{Vesica}}=\sqrt3\,R.}
\]
Each centre subtends an angle \(2\pi/3\) at the two intersection points. The lens is the union of two circular segments, each equal to a \(120^\circ\) sector minus the corresponding isosceles triangle. Hence
\[
\boxed{
A_{\mathrm{Vesica}}
=2\left(\frac{\pi R^2}{3}-\frac{\sqrt3}{4}R^2\right)
=\left(\frac{2\pi}{3}-\frac{\sqrt3}{2}\right)R^2.
}
\]
The overlap area fraction relative to one circle is
\[
\frac{A_{\mathrm{Vesica}}}{\pi R^2}
=\frac23-\frac{\sqrt3}{2\pi}.
\]
These are exact Euclidean identities. They do not depend on a physical field theory.

The equal-radius condition and centre separation are essential. For unequal radii or a different centre distance, the intersection chord and lens area change; the formulas above must not be carried over unchanged.

### C.12.3 Multi-circle extensions: what must be fixed

The terms *Bi-Veca* and *Tri-Veca* occur in the supplied report material, but a name alone does not specify a unique geometric object. To make a reproducible construction, one must state:
1. the number and locations of circle centres;
2. each radius (equal or unequal);
3. which pairwise intersections are retained;
4. whether the object is the union, intersection, nerve, or incidence graph of the disks;
5. the orientation and scale conventions.

A canonical three-circle model can be defined by placing three equal-radius circles of radius \(R\) at the vertices of an equilateral triangle of side \(R\). Each pair then forms a Vesica Piscis with the chord and lens area calculated in C.12.2. This defines three pairwise lenses, but it does not by itself define a unique “Tri-Veca region”: the triple intersection, union of pairwise lenses, and full union of disks are different sets with different areas and topology.

Accordingly, no area, volume, field, or topological invariant is attributed to “Tri-Veca” until the intended set or cell complex is specified. The report's named construction is a prompt for formalization, not a substitute for that definition.

### C.12.4 Relation to the golden ratio and to the Krystallo spiral

The Vesica construction above has a direct \(\sqrt3\) chord ratio:
\[
L_{\mathrm{Vesica}}/R=\sqrt3.
\]
The appearance of \(\sqrt3\) is forced by the \(60^\circ\) equilateral-triangle geometry. It is not a derivation of the golden ratio
\[
\phi=(1+\sqrt5)/2.
\]
A further construction may introduce \(\phi\), for example by selecting a diagonal, a nested scale rule, or a fivefold symmetry, but that additional rule must be stated and proved. The mere presence of intersecting circles does not imply a golden-ratio scaling.

Likewise, the Krystallo angular law already audited elsewhere in this project,
\[
K(\theta)=2^{2\theta/\pi},
\]
has \(K(\pi/4)=\sqrt2\) and \(K(\pi/2)=2\). It is a logarithmic-spiral scaling law and is mathematically distinct from both the Vesica chord ratio \(\sqrt3\) and the golden ratio \(\phi\). No identity among \(\sqrt2,\sqrt3,\phi\) is asserted here.

The supplied report also places Fibonacci/golden-ratio material alongside the Krystallo construction. They must remain separate:
- Fibonacci ratios converge to \(\phi\);
- the Krystallo law has a constant multiplicative factor \(2\) per quarter-turn;
- the equal-circle Vesica has chord-to-radius ratio \(\sqrt3\).

A relation between these objects would require an explicit geometric map or a common variational/spectral construction. A visual overlay is not a proof.

### C.12.5 Relation to the Pellis golden-sphere hierarchy

The Pellis preprint proposes
\[
R_n=R_0\phi^{-n}.
\]
This is a scale hierarchy with ratio \(R_{n+1}/R_n=\phi^{-1}\). The Vesica construction supplies a possible local geometric cell at any chosen scale \(R_n\), but the combination is an additional model, not a consequence of either construction alone.

For example, if at each level one places a pair of equal circles with radius \(R_n\) and centre separation \(R_n\), then
\[
L_n=\sqrt3\,R_0\phi^{-n},\qquad
A_n=\left(\frac{2\pi}{3}-\frac{\sqrt3}{2}\right)R_0^2\phi^{-2n}.
\]
Consequently, the formal sums over levels converge:
\[
\sum_{n=0}^{\infty}L_n
=\frac{\sqrt3 R_0}{1-\phi^{-1}},
\qquad
\sum_{n=0}^{\infty}A_n
=\left(\frac{2\pi}{3}-\frac{\sqrt3}{2}\right)
\frac{R_0^2}{1-\phi^{-2}}.
\]
These sums describe a prescribed collection of independent geometric cells. They are not automatically the length or area of a single embedded union: overlap between levels, placement, and multiplicity must be handled before interpreting them as geometric measure of a combined object.

This construction gives a clean test case for a future Vesica–GSR model:
- specify the placement and incidence of the circles at every level;
- define the resulting domain or cell complex;
- choose a metric and boundary conditions;
- define the relevant Laplace, Hodge, or wave operator;
- compute its spectrum and multiplicities;
- only then compare its spectral data with the \(S^3/2I\) spectrum in Document A or the Pellis operator proposed in this document.

No spectral equivalence, fine-structure derivation, or physical resonance follows from the scale sums alone.

### C.12.6 Information theory, quantum mechanics, and the “holographic” interpretation

The supplied report lists Shannon theory, Fourier analysis, Hilbert spaces, Born probabilities, decoherence, entanglement, and holographic/holonomic interpretations as parts of one proposed explanatory chain. The mathematical formalisms are not interchangeable:
- Shannon entropy and channel capacity concern probability distributions and communication channels;
- Fourier analysis decomposes functions or signals relative to a specified measure and domain;
- a quantum state is a vector or density operator in a specified Hilbert space, and Born probabilities are defined relative to measurement operators;
- entanglement is a property of a specified composite quantum state and tensor-product structure;
- holographic principles in theoretical physics require a precise bulk/boundary model and a quantitative correspondence.

None of these definitions, separately or together, proves that the brain is an artificial hologram reader or that spacetime is an artificial vector field. Those statements remain interpretive claims in the supplied report unless a concrete model supplies variables, dynamics, observables, and tests that could falsify them.

For the Pellis collaboration, the useful mathematical bridge is narrower: a geometric configuration can define a metric space or cell complex; that space can support a self-adjoint operator once its Hilbert space, inner product, domain, and boundary conditions are fixed; its spectral projections can then define basis-independent weights as in Document B. Any proposed physical meaning for those weights must be added as a separate model and tested independently.

### C.12.7 Evidence ledger for the Vesica material

| Statement | Classification in this audit |
|---|---|
| Two equal circles of radius \(R\), centre distance \(R\) | Exact geometric definition |
| Common chord length \(\sqrt3R\) | Exact Euclidean theorem |
| Lens area \((2\pi/3-\sqrt3/2)R^2\) | Exact Euclidean theorem |
| Three-circle construction with equilateral centres | Explicit model definition introduced here |
| Pairwise Vesica areas in the three-circle model | Exact consequence of the model definition |
| A unique “Tri-Veca” region | Underspecified until union/intersection/incidence is fixed |
| Fibonacci limit \(\phi\) | Standard limit theorem; distinct from the Vesica \(\sqrt3\) ratio |
| Krystallo law \(2^{2\theta/\pi}\) | Separate stipulated/project law; not derived from Vesica geometry |
| Vesica cells placed at Pellis scales \(R_n=R_0\phi^{-n}\) | Conditional geometric construction |
| Spectral correspondence with \(S^3/2I\) or Pellis resonance | Open; requires an operator and a proved spectral map |
| Artificial holographic prison, morphic control, telepathy via entanglement, over-unity energy claims | Not established by the mathematical material reviewed; excluded as premises |

### C.12.8 Reproducibility tasks

The following exact checks should be added to the Pellis audit suite before the construction is promoted beyond a mathematical appendix:
1. symbolic verification of the common-chord and lens-area formulas;
2. exact or interval-certified checks of the three-circle incidence relations;
3. for any nested-scale realization, separate verification of the scalar geometric series from the measure of the actual union;
4. once a domain is fixed, independent matrix construction and spectral computation, with convergence and self-adjointness diagnostics.

Until those checks and definitions exist, C.12.2 is an exact geometric result, C.12.3 is a model specification, and C.12.5 is a conditional scale construction. No physical interpretation is claimed.

---

## References

1. S. Pellis, *Fine-Structure Constant via the Golden Spheres Resonance*, 11 September 2025, DOI [10.13140/RG.2.2.35410.00968](https://doi.org/10.13140/RG.2.2.35410.00968), especially §§2–3, §§4–7, and §§10–11. The public full-text record identifies it as a preprint.
2. S. Pellis, same work, SSRN record [5473588](https://ssrn.com/abstract=5473588), posted 2 October 2025.
3. CODATA 2022 and electron-\(g\)-factor central values and uncertainties are quoted as printed in the Pellis preprint; the comparisons above are arithmetic checks of those printed inputs, not an independent metrology update.
4. Document A — [Exact scalar spectral geometry of \(S^3/2I\)](01_exact_scalar_spectrum_poincare_sphere.md).
5. *Rapporto Vesica*, supplied structured extract (2,566-page report; author, publication date, and stable public identifier not supplied in the extract). Used only for the report's stated organization and claims summarized in C.12.1 and C.12.6.
6. Document B — [Geometric self-adjoint operators and spectral weights](https://github.com/fabianleonaressi95/theorem/blob/collaboration/pellis-document-2-self-adjoint-operators/collaborations/pellis/03_geometric_self_adjoint_operators.md).

**Classification:** exact algebraic core; exact convergence statements under stated hypotheses; conditional cavity scaling; operator realization and physical derivation remain open.


## C.13 Golden rectangles and the 8×10, 10×12, 14×18 ray grids: structural audit of the proposed link

### C.13.1 The rectangle construction on p. 2091

Let the initial rectangle have short side $B_0=1$ and long side $A_0=\phi$, where \(\phi=(1+\sqrt5)/2\). Its aspect ratio is $A_0/B_0=\phi$.

If the next rectangle is attached so that the previous long side becomes the new short side, then
\[
B_{n+1}=A_n,\qquad A_{n+1}=\phi B_{n+1}=\phi A_n.
\]
Consequently,
\[
B_n=\phi^n,\qquad A_n=\phi^{n+1}
\]
for this indexing convention. Every rectangle is similar to the first, and each step scales its linear dimensions by \(\phi\). A quarter-turn changes orientation but does not change this scale law.

The phrase “80° perpendicolare” is internally inconsistent: perpendicular directions differ by 90°. Unless the source defines a non-Euclidean or otherwise specialized angle convention, 80° must be treated as a likely typographical error, not silently used as a right angle.

**Important distinction:** iterating similar rectangles by attaching a new rectangle along the previous long side does not, by itself, define a spiral curve. A spiral requires an explicit curve, such as specified circular arcs, or a continuous law such as $r(\theta)=r_0e^{b\theta}$. The familiar golden-rectangle construction instead removes a square from a golden rectangle, leaving a smaller golden rectangle with side ratio \(\phi\); repeated square removal gives a sequence of squares whose quarter-circle arcs form the conventional golden-spiral approximation. That construction is not identical to an unspecified chain of whole golden rectangles rotated by 90°.

Thus the exact conclusion from the stated side rule is **a self-similar sequence of golden rectangles with scale ratio \(\phi\)**. A “golden spiral” conclusion requires the additional arc/curve prescription.

### C.13.2 The ray-count grids on p. 2103

The supplied description identifies three pairs of ray counts:
\[
(8,10),\qquad (10,12),\qquad (14,18).
\]
Their ratios are
\[
\frac{10}{8}=\frac54=1.25,\qquad
\frac{12}{10}=\frac65=1.2,\qquad
\frac{18}{14}=\frac97\approx1.285714.
\]
None equals \(\phi\), and the three ratios are not equal to one another. Therefore the pairs cannot, on their own, be interpreted as successive exact samples of one fixed \(\phi\)-ratio.

A golden-ratio relationship could still enter through the radii of the underlying circles, angular offsets, a projection, or a separate mapping from continuous geometry to integer counts. But that map must be stated. In particular, “circles are nested in ratio \(\phi\)” does not imply that their ray counts have ratio \(\phi\): ray counts are integers and require a rule specifying how directions are selected, counted, identified, or rounded.

The phrase “8×10”, etc., must also be defined: it could denote an ordered pair of ray counts on two circles, a rectangular array with those dimensions, or a product. These are different mathematical objects. This audit uses the neutral notation “pair of ray counts” until the report's construction rule resolves the ambiguity.

### C.13.3 What a Vesica-intersection rasterization would require

The assertion that intersections of Vesica Piscis regions “directly generate” an 8×10 grid is a geometrical construction claim, not yet an algebraic derivation. To make it reproducible, the construction must specify at least:
1. the centres and radii of every generating circle;
2. the exact centre-distance rule for each Vesica;
3. which circle pairs are intersected and which of their two intersection points or common-chord lines are retained;
4. how those points or lines are converted into rays;
5. the centre from which each ray is measured and the angular interval used;
6. the rule that yields exactly 8 and 10 distinct rays, including treatment of coincident or symmetry-equivalent directions.

Without these data, infinitely many circle arrangements can produce different intersection patterns. The exact two-circle formula in C.12.2 supplies a local chord length, but does not select an 8×10 incidence pattern.

The proposed “continuous-to-discrete sampling” interpretation is therefore a plausible research program, not a proved consequence of the Vesica definition. A valid proof would define a map from a continuous configuration (circles, chords, or an embedded arrangement) to a finite incidence structure and establish that its image has the claimed cardinalities.

### C.13.4 The proposed common matrix: Flower of Life and Metatron's Cube

The report's description of the Flower of Life / Metatron's Cube as a common “matrix” for both constructions is a source-level interpretive claim. To turn it into a mathematical statement, one must define the underlying point set, graph, cell complex, or tiling and then exhibit:
- an embedding of the golden-rectangle sequence into that object;
- an embedding or incidence realization of each ray-count grid into the same object;
- a specified action or transformation relating the two embeddings;
- invariants preserved by that transformation (for example, incidence, distances, angles, or a group action).

The visual fact that two diagrams can be drawn over the same background is not sufficient to show that one tiles the other, that they are generated by the same matrix, or that either is a substructure of the other. The phrase “universal matrix” is not used as a mathematical premise in this audit.

### C.13.5 Why a right-angle rectangle is not a degenerate Vesica Piscis

A golden rectangle with a 90° orientation change is not a degenerate case of two intersecting equal circles. The primitive data differ: a rectangle is defined by four line segments and right angles, while a Vesica is the lens intersection of two disks, defined by radii and centre separation. No continuous deformation or incidence-preserving map between these objects is supplied by the report excerpt.

A bridge could be constructed—for example, by mapping selected circle-intersection chords to rectangle edges or by defining a common cell complex—but it would be a new theorem/model. It must state the map and prove which quantities it preserves. In particular, the Vesica chord ratio \(\sqrt3\) and the golden-rectangle aspect ratio \(\phi\) are distinct invariants of the two respective constructions.

### C.13.6 “Levels of consciousness” and degrees of freedom

The report associates the pairs 8×10, 10×12, and 14×18 with successive “levels of consciousness” and interprets added rays as added degrees of freedom. The integer counts can be recorded as source claims. Their interpretation as physical or cognitive degrees of freedom does not follow from the counts alone.

A mathematical degrees-of-freedom claim requires a defined state space and a dimension or rank calculation. A consciousness claim additionally requires an operational definition, measurable variables, and a testable relation between the geometric count and those variables. No such derivation is supplied by the ray-count pairs themselves. The analogy between “one more rectangle per iteration” and “more rays per level” is therefore descriptive, not a proof that the two sequences encode the same hierarchy.

### C.13.7 Evidence ledger and next exact checks

| Statement | Classification |
|---|---|
| Initial rectangle has side ratio \(\phi\) | Exact definition |
| Repeatedly using the previous long side as the next short side | Exact recurrence; produces similar rectangles scaled by \(\phi\) |
| A 90° rotation changes orientation | Exact Euclidean fact |
| “80° perpendicolare” | Source inconsistency; likely typo, not a valid perpendicular angle |
| The rectangle chain alone is a golden spiral | Not established; a curve/arc rule is missing |
| Square-removal recursion inside a golden rectangle | Standard construction; distinct from the whole-rectangle attachment rule above |
| Ray-count pairs (8,10), (10,12), (14,18) | Source-reported integers |
| Those pairs are in exact golden ratio | False for the displayed count ratios |
| Underlying circle radii are in ratio \(\phi\) | Source-reported construction claim; requires exact centre/radius data |
| Vesica intersections generate exactly 8×10 rays | Open; incidence and ray-selection rule missing |
| Both constructions embed in a common Metatron/Flower-of-Life matrix | Open; common object and embeddings not defined |
| A right-angle rectangle is a degenerate Vesica | Not established; no map or limiting construction supplied |
| Ray increments are consciousness degrees of freedom | Interpretive claim; no state-space or measurement model supplied |

The next computational audit should not fit \(\phi\) to the integer pairs. It should first transcribe the exact circle-centre/radius configuration from the source, construct the resulting intersection graph, deduplicate directions under the stated symmetries, and only then check whether the graph has the claimed ray counts. If the source does not provide those coordinates or a construction algorithm, the claim remains underdetermined rather than numerically verified.

**Conclusion:** the two passages may be related by a common intended visual language, but the supplied definitions do not yet prove that they are two representations of one \(\phi\)-generated hierarchy. The exact rectangle recurrence is established; the ray-count construction, common-matrix claim, Vesica conversion, and consciousness interpretation remain separate claims with the statuses above.


## C.14 An explicit three-circle benchmark and the obstruction from pure golden scaling

To avoid guessing the geometry of the report's missing illustration, a separate exact benchmark has been defined in [the three-circle / golden-homothety audit](../../audits/VESICA_THREE_CIRCLE_GOLDEN_HOMOTHETY_2026-11-23.md).

The benchmark consists of three equal circles of radius (R), with centres at the vertices of an equilateral triangle of side (R). The six distinct pairwise intersection points, viewed from the triangle centroid, determine six equally spaced outward ray directions. The corresponding angular graph is (C_6), with combinatorial Laplacian spectrum
[
0,1,1,3,3,4.
]
These are exact statements for this explicitly defined model; they do not reconstruct the unspecified source diagram.

Under the golden hierarchy (R_n=R_0phi^{-n}), each level is a homothetic copy. Homothety preserves angular directions and incidence, so the ray count remains six at every level. A metric graph Laplacian with inverse-square edge weights scales spectrally by (phi^{2n}) (with a fixed vertex-measure convention), but its number of vertices and directions does not change.

**Consequence:** the reported sequence ((8,10),(10,12),(14,18)) cannot be obtained merely by applying golden homotheties to one fixed three-circle configuration. A level-dependent change of circle centres, incidence pattern, rotation, or ray-selection rule is necessary. The supplied report extract does not specify which one.

**Classification:** exact geometric/operator benchmark for the chosen model; obstruction to count growth under pure homothety; reconstruction of the report's 8×10 / 10×12 / 14×18 grids remains open. No physical interpretation or equivalence with Pellis's resonance operator is claimed.


## C.15 Exact incidence complex of the 19-circle Flower of Life

The traditional 19-circle arrangement is formalized independently of the three-circle angular benchmark. The full construction, exact intersection classification, \(31\times19\) incidence matrix, \(D_6\)-orbit decomposition, and characteristic polynomial of \(B^\mathsf TB\) are recorded in [the exact 19-circle incidence audit](../../audits/FLOWER_OF_LIFE_19_EXACT_INCIDENCE_2026-11-23.md). A reproducible SymPy script is stored beside the audit.

For common radius \(R=1\), the 19 centres form the hexagonal radius-two patch of the triangular lattice. The arrangement has 99 intersecting circle pairs but only 31 distinct intersection points, because some points are shared by three, four, or six circles. The point multiplicity distribution is \(2:12,\ 3:6,\ 4:6,\ 6:7\), giving 108 circle-point incidences.

With \(B\) the binary point-circle incidence matrix, the exact Gram operator \(G=B^\mathsf TB\) has rank 19 and characteristic polynomial
\[
\begin{aligned}
\chi_G(\lambda)={}&(\lambda-6)^2(\lambda-3)^2(\lambda-2)^3
(\lambda^2-8\lambda+11)\\
&\cdot(\lambda^3-19\lambda^2+78\lambda-76)^2\\
&\cdot(\lambda^4-38\lambda^3+375\lambda^2-1350\lambda+1584).
\end{aligned}
\]
The 31 intersection points split into \(D_6\)-orbits of sizes \(1,6,6,6,12\).

This is not the same operator as the \(C_6\) angular Laplacian in C.14: the latter is a six-direction graph Laplacian, while \(B^\mathsf TB\) acts on the 19 circle labels and records shared intersection points. Their spectra must not be conflated. The 19-circle construction gives a global incidence model; an angular-ray graph still requires an explicit origin and ray-selection convention.

The exact incidence structure is invariant under golden homothety, so scaling all radii by \(\phi^{-n}\) cannot change the counts 19 centres, 31 intersection points, or 108 incidences. No derivation of the Rapporto Vesica's \(8\times10\), \(10\times12\), or \(14\times18\) ray pairs is claimed.

**Classification:** exact finite geometry and exact symbolic computation for the specified 19-circle arrangement; relation to the source's ray-count sequence remains open; no physical identification with Partiki, the 12 Tree Grid, or 15-dimensional fields is asserted.
