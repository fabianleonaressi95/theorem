# PEL-05 — Independent spectral-state selection: criteria and no-go boundary

**Date:** 27 November 2026  
**Classification:** operator-theoretic framework; conditional criteria proved; physical selection principle **OPEN**.  
**Parent register:** [PELLIS_GSR_OPEN_PROBLEMS.md](../open-problems/PELLIS_GSR_OPEN_PROBLEMS.md)  
**Related result:** [T151 — Spectral expectation values do not determine modal weights without state selection](../theorems/T151-spectral-expectation-weights-state-selection.md)

## 1. Question and exclusion principle

Let \(\mathcal R\) be the proposed self-adjoint resonance operator and let \(E_{\mathcal R}\) be its projection-valued spectral measure. A normalized state \(\Psi\) determines the scalar spectral measure
\[
\mu_\Psi(B)=\langle\Psi,E_{\mathcal R}(B)\Psi\rangle.
\]
The operator alone does not determine \(\mu_\Psi\). In particular, selecting \(\Psi\) by requiring its expectation to reproduce the target fine-structure expression is excluded: that is an inverse fit, not an independent prediction (T151).

This note records what a legitimate state-selection theorem would have to prove. It does **not** introduce a fitted operator or claim that Pellis's physical state has been identified.

## 2. Conditional ground-state selection theorem

**Proposition (simple isolated ground state gives a unique ray).**  
Let \(H_{\rm sel}\) be a self-adjoint, lower-bounded operator on a Hilbert space \(\mathcal H\). Suppose its spectral bottom
\[
E_0=\inf\sigma(H_{\rm sel})
\]
is an isolated eigenvalue of multiplicity one. Then the normalized ground states are exactly \(e^{i\theta}\Psi_0\), where \(\Psi_0\) is one fixed unit vector. Consequently, every spectral weight
\[
w_j=\langle\Psi_0,P_j\Psi_0\rangle
\]
for any fixed family of orthogonal projections \(P_j\) is uniquely determined.

**Proof.** The eigenspace \(\ker(H_{\rm sel}-E_0I)\) is one-dimensional by the multiplicity-one assumption. Its unit vectors differ only by a phase. The expectation of each projection is phase invariant, hence independent of the chosen normalized representative. \(\square\)

The hypotheses are substantive. Lower boundedness alone does not guarantee an attained ground state; an isolated simple eigenvalue is a sufficient condition, not an automatic consequence of symmetry or geometry.

## 3. Degeneracy obstruction

If the ground eigenspace \(G_0=\ker(H_{\rm sel}-E_0I)\) has dimension \(d>1\), then ground-state selection by energy alone determines only the unit sphere in \(G_0\), modulo phase. In general, the weights \(\langle\Psi,P_j\Psi\rangle\) vary with \(\Psi\in G_0\). A symmetry-invariant operator can therefore leave a nontrivial family of admissible states.

A further selector is then required (for example, a specified commuting observable with a simple eigenvalue inside \(G_0\), or a physically justified symmetry-breaking condition). Such a selector must itself be fixed independently of the target constant. Choosing a preferred vector by matching the desired Pellis coefficients merely moves the inverse fit to a second stage.

## 4. Minimal data required for a non-circular construction

A candidate PEL-05 solution must supply, in this order:

1. **Configuration space:** the geometric space or graph, its measure, and the Hilbert space \(\mathcal H\).
2. **Selection dynamics:** an explicit quadratic form or operator \(H_{\rm sel}\), including all couplings and coefficients. Every coefficient must be derived from geometry, symmetry, or an independently stated physical law; none may be chosen from the target constant or target modal weights.
3. **Operator realization:** a dense domain and a proof of self-adjointness (or a specified closed semibounded form and its associated self-adjoint operator).
4. **Existence:** proof that the spectral bottom is attained by an eigenvector, not merely approached by continuous spectrum.
5. **Uniqueness:** proof of a simple ground eigenvalue, or an independently justified secondary selector resolving the degeneracy.
6. **Observable map:** explicit resonance projections \(P_j\) and the derived weights \(w_j=\langle\Psi_0,P_j\Psi_0\rangle\).
7. **Stability:** estimates showing that the state and weights are stable under mode truncation, geometric refinement, and admissible perturbations.
8. **Blind validation:** compute the target expression only after the preceding data and weights have been fixed.

## 5. Symmetry does not by itself select a state

Let a group \(G\) act unitarily on \(\mathcal H\), and suppose \(H_{\rm sel}\) commutes with that action. Then each eigenspace is a representation of \(G\), but symmetry alone does not select a vector within a nontrivial irreducible or multiplicity space. In particular:

- an invariant ground-state subspace need not be one-dimensional;
- Schur's lemma constrains operators on irreducible representation factors, but does not choose a vector in a degenerate eigenspace;
- averaging a state over the group produces an invariant density operator in general, not necessarily a unique pure state.

Thus a proposed \(2I\), \(D_6\), or \(SO(3)\) symmetry can constrain admissible states and degeneracies, but cannot be cited as a unique state-selection principle without an additional argument.

## 6. Candidate routes to investigate (not established)

These are research routes, not asserted solutions:

- **Geometric Laplacian / Dirichlet form:** derive a positive form from a specified metric or graph conductance and test whether its lowest eigenspace is simple. If the constant mode is the unique ground state, determine whether it has any nontrivial resonance content; do not assume that it yields the desired hierarchy.
- **Coupled-shell operator:** derive inter-shell couplings from a fixed geometric matching law, then prove semiboundedness and simplicity. The couplings must not be tuned to the Pellis coefficients.
- **Symmetry-sector selection:** use exact projectors to identify invariant sectors, then test whether the lowest eigenvalue in a physically justified sector is simple. The choice of sector must be independently motivated.
- **Variational entropy or free-energy principle:** admissible only if the functional, constraints, temperature/scale, and measure are independently fixed. Maximizing an entropy with constraints built from the target weights is circular.

No route can be promoted until its operator and hypotheses are explicit.

## 7. Immediate audit checklist

| Test | Required evidence | Present status |
|---|---|---|
| Is \(H_{\rm sel}\) explicitly defined by Pellis's physical geometry? | Formula, Hilbert space, domain/form | **Missing** |
| Is it self-adjoint and lower bounded? | Proof or cited theorem with verified hypotheses | **Missing** |
| Is the ground energy attained and isolated? | Spectral argument | **Missing** |
| Is the ground eigenspace one-dimensional? | Simplicity proof | **Missing** |
| Are modal projections fixed independently? | Explicit \(P_j\) and mode identification | **Partial / model-dependent** |
| Are weights obtained without target fitting? | Blind derivation and independent reproduction | **Missing** |
| Are weights stable under refinement? | Uniform estimates/convergence | **Missing** |

## 8. Conclusion and status

**PEL-05 remains OPEN.** What is established here is a precise conditional route: an independently defined self-adjoint, lower-bounded selection operator with an isolated simple ground eigenvalue would determine a unique state ray and hence unique modal weights. What is not established is the existence of such an operator derived from the Pellis geometry, or that its ground state yields the proposed resonance hierarchy.

T151 remains the exact obstruction to extracting weights from a target expectation alone. This note sharpens the missing step; it does not solve it.
