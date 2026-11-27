# Pellis / Golden Spheres Resonance — open-problems register

**Date:** 25 November 2026  
**Scope:** mathematical and operator-theoretic questions arising from the correspondence with Stergios Pellis and the *Fine-Structure Constant via the Golden Spheres Resonance* preprint.  
**Status:** research register only. No open item below is promoted to a theorem or to an experimentally validated physical claim.

The independent H4 rotation investigation is recorded in [the 600-cell two-plane cyclotomic audit](../docs/H4_600_CELL_TWO_PLANE_CYCLOTOMIC_AUDIT_2026-11-26.md). The independent mathematical review of PEL-01–PEL-11 is recorded in [the 27 November audit](../docs/PELLIS_GSR_REGISTER_AUDIT_2026-11-27.md); it corrects the countable-spectrum wording in T151 and the ambient-group label in T150 §9 without closing any PEL item. This register complements [the Fibonacci–Fricke/Q6 two-sheet bridge](../docs/PELLIS_FIBONACCI_Q6_TWO_SHEET_BRIDGE.md), [T138](../theorems/T138-c6-exact-two-sheet-spin3-decomposition.md), [T150](../theorems/T150-d6-fibonacci-hexagram-antipodal-two-sheet-correspondence.md), and [T151](../theorems/T151-spectral-expectation-weights-state-selection.md). T151 proves a limitation on spectral-expectation inverse design; it does **not** solve the independent state-selection problem.

## Epistemic labels

- **PROVED / EXACT FINITE:** a derivation or identity is complete under stated assumptions.
- **NUMERICALLY VERIFIED:** a reproducible finite computation supports the stated result.
- **CONDITIONAL:** valid if explicitly listed hypotheses hold.
- **OPEN:** a definition, proof, uniqueness result, convergence theorem, or independent validation is missing.
- **NOT ESTABLISHED:** no evidence currently justifies the stronger interpretation.

## Priority register

| ID | Open problem | Required mathematical deliverable | Current status |
|---|---|---|---|
| PEL-01 | Independent derivation of the Pellis Function coefficients | Derive each coefficient and exponent from a fixed geometry/operator, without choosing weights to reproduce the target constant | **OPEN** |
| PEL-02 | Geometric origin of the surface, volume, and wave/quantum terms | Define the three contributions invariantly and derive their scaling laws, including the roles assigned to \(\varphi^{-2n}\), \(\varphi^{-3n}\), and \((3\varphi)^{-5n}\) | **OPEN** |
| PEL-03 | Geometric meaning of the factor \(360\) | Identify the exact geometric, group-theoretic, or measure-theoretic count/normalization producing 360; prove it is not an adjustable prefactor | **OPEN** |
| PEL-04 | Complete definition of the Golden Resonance Operator | Specify Hilbert space, inner product/measure, dense domain, boundary conditions, self-adjoint realization, spectrum, and spectral multiplicities | **OPEN** |
| PEL-05 | Independent selection of the physical state | Give a variational, symmetry, or geometric principle selecting \(\Psi_0\); prove existence, uniqueness (or controlled degeneracy), and derive its modal weights without fitting | **OPEN — highest priority** |
| PEL-06 | Independent derivation of the golden semigroup scale | Derive \(s=2\ln\varphi\) from an extremality, geometric-length, renormalization, or spectral condition; otherwise label it as a model parameter | **OPEN** |
| PEL-07 | Link between binary-icosahedral invariants and exponents \(2,3,5\) | Construct an explicit map/selection theorem connecting the \(2I\) invariant degrees \(12,20,30\), irreducible representations, or spectral operators to the three exponents; no numerical analogy alone | **OPEN** |
| PEL-08 | \(2I\)-derived spectral multiplicities and selection rules | Derive admissible modes and multiplicities from the \(2I\) action (e.g. Reynolds/character projectors and the \(S^3/2I\) spectrum), then show how they constrain the resonance functional | **PARTLY ESTABLISHED / BRIDGE OPEN** |
| PEL-09 | Exact two-sheet / Anti-Twin operator model | Specify both sheet spaces, exchange involution, metric and measure, coupling, operator domains, boundary/neck conditions, and a well-defined continuum/refinement limit | **FINITE ALGEBRA AVAILABLE; PHYSICAL OPERATOR OPEN** |
| PEL-10 | Three-mode decomposition and possible \(SO(3)\) symmetry | Identify the actual group representation on the three modes; prove operator/domain/boundary invariance. A \(1\oplus2\) decomposition under a discrete dihedral group does not by itself imply full \(SO(3)\) symmetry or equality of the two blocks | **OPEN** |
| PEL-11 | Discrete-to-continuum and physical interpretation | Prove a controlled operator/form/resolvent limit, identify physical degrees of freedom and gauge covariance, and distinguish the Q6/PRISM model from continuum gauge theory or QCD until such a bridge exists | **OPEN** |

## Technical decomposition and acceptance criteria

### PEL-01–PEL-03 — Derive the target rather than reconstruct it

The preprint's target expression includes the combination
\[
360\varphi^{-2}-2\varphi^{-3}+(3\varphi)^{-5}.
\]
The exact expression and its numerical use are not, by themselves, a derivation of the coefficients. In particular, a construction that selects modal weights or a penalty functional to reproduce the target is an inverse-design procedure, not an independent prediction.

Acceptance requires:
1. a fixed geometric/operator construction specified before evaluating the target;
2. a derivation of each coefficient and exponent from that construction;
3. a proof that no free normalization, fitted weight, or target-dependent penalty remains;
4. an independent symbolic or numerical reproduction from the stated definitions.

### PEL-04–PEL-06 — Operator, state, and semigroup

The spectral programme should be stated in the order
\[
(\mathcal H,\langle\cdot,\cdot\rangle),\quad
\mathcal D(\mathcal R),\quad
\mathcal R=\mathcal R^*,\quad
E_{\mathcal R}(\cdot),\quad
\Psi_0,\quad
\mu_{\Psi_0}(B)=\langle\Psi_0,E_{\mathcal R}(B)\Psi_0\rangle.
\]
The spectral measure is state-dependent. Thus specifying a self-adjoint operator does not, alone, determine resonance weights. T151 formalizes the finite-dimensional convex-combination obstruction: a target expectation generally does not uniquely determine its modal weights.

Acceptance requires a state-selection principle independent of the target constant, with existence and uniqueness/degeneracy proved. The scale \(s=2\ln\varphi\) must then follow from an independent condition; until then it remains an assumption/parameter, not a theorem.

### PEL-07–PEL-08 — Binary icosahedral invariant theory

The binary icosahedral group \(2I\subset SU(2)\) has order 120. The invariant-theory data used in this programme include the Molien series
\[
M(t)=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]
The degrees \(12,20,30\) are exact invariant-theory data. Their relation to the exponents \(2,3,5\) in the proposed resonance hierarchy is **not** automatic.

Acceptance requires an explicit equivariant construction: identify the relevant representation spaces, projectors and operator, then prove a selection rule or spectral identity that yields the proposed exponents. Existing exact scalar spectral multiplicity calculations on \(S^3/2I\) are supporting infrastructure, not the missing correspondence.

### PEL-09–PEL-10 — Two sheets and three modes

The finite results must remain distinct from the physical operator claim:
- T138 gives an exact \(3+3\) eigenspace splitting for a specified integer matrix.
- T150 gives an exact \(D_6\)-equivariant correspondence between a six-state Fibonacci orbit and a selected six-state Q6 antipodal orbit.
- The Fibonacci/Q6 note records the neck factorization \(2b(E)d(E)=0\) under its stated matching convention.
- None of these facts alone defines the full Pellis Hilbert space, its self-adjoint operator, or the physical sheet intertwiner.

For the three-mode question, the permutation representation \(1\oplus2\) under a dihedral action must not be conflated with the restriction of the standard \(SO(3)\) vector representation. Full \(SO(3)\) degeneracy follows only if the actual physical three-dimensional subspace carries an irreducible vector representation and the operator, domain, and boundary conditions strongly respect that action.

Acceptance requires explicit spaces, maps, domains, inner products, and commutation/intertwining equations—not a dimension count or a symmetry label alone.

### PEL-11 — Continuum and gauge-theory bridge

A finite graph identity or finite-dimensional spectral match is not a continuum-limit theorem. A valid bridge must state the refinement parameter, Hilbert-space identifications, discrete and continuum operators/forms, convergence mode (e.g. Mosco or strong-resolvent convergence), gauge-covariant degrees of freedom, and uniform estimates needed to pass spectra or observables to the limit.

The following identifications remain open unless separately proved:
- Q6/PRISM discrete operators with continuum gauge theory or QCD;
- the finite two-sheet construction with a continuum PSU/Anti-Twin geometry;
- the Q6 Green–Kubo benchmark with a material/physical Stokes viscosity;
- the integer-flux Wilson marginal with the D5 Bergman measure.

## Work order

1. **PEL-05:** settle state selection first; it controls whether the spectral weights are predictions or fitted inputs.
2. **PEL-04:** specify the operator and its self-adjoint domain.
3. **PEL-01–PEL-03:** derive the Pellis coefficients from the fixed operator/geometry.
4. **PEL-06:** derive the golden semigroup scale independently.
5. **PEL-07–PEL-08:** establish the \(2I\) invariant-theory selection mechanism.
6. **PEL-09–PEL-10:** complete the physical two-sheet and three-mode operator definitions.
7. **PEL-11:** only then attempt the continuum/gauge-theory identification.

This order is a dependency recommendation, not a claim that the earlier items have been solved.

## Source and correspondence record

- Stergios Pellis, *Fine-Structure Constant via the Golden Spheres Resonance*, ResearchGate record, DOI [10.13140/RG.2.2.35410.00968](https://doi.org/10.13140/RG.2.2.35410.00968), September 2025.
- Stergios Pellis, *Fine-Structure Constant via the Golden Spheres Resonance*, SSRN abstract [5473588](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5473588), posted 2 October 2025.
- Correspondence dated 16 November 2026: questions on the \(2I\) invariant bridge, self-adjoint resonance operator, spectral measures, golden scale, Q6/discrete differential geometry, two-sheet geometry, and controlled continuum limit. This register records the questions; it does not imply external validation or agreement.

## Update protocol

For every item, record (i) the precise new definition or theorem, (ii) assumptions, (iii) proof or reproducible audit, (iv) counterchecks/limitations, and (v) commit or PR. Change a status only when its acceptance criteria are met. Do not turn an email exchange, numerical coincidence, or prepared draft into evidence of proof or external endorsement.
