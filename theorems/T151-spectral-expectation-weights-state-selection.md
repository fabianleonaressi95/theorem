# T151 — Spectral expectation values do not determine modal weights without state selection

**Date:** 25 November 2026  
**Classification:** exact operator-theoretic lemma and source-level application audit.  
**Status:** proved for discrete diagonal self-adjoint operators; the application identifies a non-uniqueness in the expectation-value construction used in the Golden Spheres Resonance preprint.

## 1. Discrete spectral setup

Let \(\mathcal H=\ell^2(I)\) with orthonormal basis \(\{e_i\}_{i\in I}\), where \(I\) is finite or countable. Let \(G\) be a bounded self-adjoint diagonal operator
\[
Ge_i=\lambda_i e_i,\qquad \lambda_i\in\mathbb R.
\]
For a normalized state
\[
\psi=\sum_{i\in I}c_i e_i,\qquad \sum_i|c_i|^2=1,
\]
the expectation is
\[
\boxed{\langle\psi,G\psi\rangle
=\sum_i |c_i|^2\lambda_i.}
\]
Thus the expectation depends on the probability weights \(w_i=|c_i|^2\), not only on the operator eigenvalues.

## 2. Realizability lemma

**Theorem.** For every probability distribution \(w=(w_i)_{i\in I}\), \(w_i\ge0\), \(\sum_iw_i=1\), the normalized state
\[
\psi_w=\sum_i\sqrt{w_i}\,e_i
\]
satisfies
\[
\langle\psi_w,G\psi_w\rangle=\sum_iw_i\lambda_i.
\]
Consequently, if \(I\) is finite, the set of all possible expectation values is exactly the finite convex hull of the eigenvalues. If \(I\) is countably infinite, it is exactly the set of probability barycentres
\[
\mathcal E_G=\left\{\sum_{i\in I}w_i\lambda_i:
w_i\ge0,\quad\sum_iw_i=1\right\}.
\]
Its closure is the closed convex hull:
\[
\overline{\mathcal E_G}
=\overline{\operatorname{conv}\{\lambda_i:i\in I\}}.
\]
The countable expectation set need not itself be closed.

**Proof.** Orthonormality gives \(\|\psi_w\|^2=\sum_iw_i=1\). Since \(G\) is diagonal,
\[
\langle\psi_w,G\psi_w\rangle
=\sum_{i,j}\sqrt{w_iw_j}\langle e_i,Ge_j\rangle
=\sum_iw_i\lambda_i.
\]
Every normalized state supplies a probability distribution \(w_i=|c_i|^2\), so the converse inclusion also holds. In the countable case boundedness of \(G\) makes the barycentre absolutely convergent. Finite-support distributions give the ordinary convex hull; truncation and renormalization approximate every countably supported barycentre, proving the closure identity. \(\square\)

## 3. Non-uniqueness of the inverse expectation problem

A single scalar constraint
\[
\sum_iw_i\lambda_i=P,\qquad
w_i\ge0,\quad\sum_iw_i=1
\]
does not in general determine the weights. With at least three distinct eigenvalues, any target in the interior of their convex hull typically admits infinitely many probability distributions. Degenerate eigenspaces add further freedom.

For a finite-dimensional example with three distinct eigenvalues \(\lambda_1<\lambda_2<\lambda_3\), the normalization and expectation equations are two independent affine constraints on three weights. Whenever the target lies in the interior of the convex hull, the admissible weights form a nontrivial line segment. More modes increase the freedom.

Therefore:
- the operator spectrum fixes the allowed eigenvalues;
- a chosen state fixes its spectral measure;
- the expectation value alone does not uniquely determine the state or its weights.

## 4. Application to a \(\varphi\)-weighted resonance series

Suppose a proposed Golden Resonance Operator is diagonal in modes \(\psi_n\), with real eigenvalues \(\lambda_n(\varphi)\), and a normalized collective state has coefficients \(c_n\). Then
\[
\langle\Psi,G_\varphi\Psi\rangle
=\sum_n|c_n|^2\lambda_n(\varphi).
\]
If the modal weights are chosen proportional to a target coefficient sequence \(a_n\), with a normalization constant, the target series can be encoded as an expectation value. This proves representability of that series in the chosen diagonal model. It does not derive the coefficients \(a_n\) from the operator.

If some target coefficients are negative, they cannot directly be probabilities \(|c_n|^2\). Such signs must instead arise from signed eigenvalues, an additional observable, or a different operator construction; that additional structure must be independently specified.

## 5. What would make the weights predictive?

A non-circular spectral derivation needs an independent state-selection principle. For example:
1. specify a self-adjoint selection Hamiltonian \(H_\varphi\) on a stated Hilbert space and domain;
2. derive its potential/inter-mode coupling from geometry or an action, rather than fitting the desired coefficients;
3. prove existence and uniqueness (or a controlled finite-dimensional eigenspace) of the selected ground state;
4. derive the weights from the spectral projections of that state;
5. show stability under truncation and refinement.

Merely proposing that the state be a ground collective resonance is not enough until the functional, domain, boundary conditions and uniqueness conditions are stated.

## 6. Source-level application to Golden Spheres Resonance

Stergios Pellis, *Fine-Structure Constant via the Golden Spheres Resonance* (11 September 2025; DOI 10.13140/RG.2.2.35410.00968; SSRN 5473588), introduces a Golden Resonance Operator on \(\varphi\)-scaled sphere modes. Its expectation-value discussion explicitly allows the modal weights to be selected proportional to the coefficients one wants to reproduce and then normalized. The paper also proposes a possible ground-state/variational selection through inter-shell coupling, but the corresponding selection functional and uniqueness theorem must be specified before the coefficients can be regarded as operator-derived.

The present theorem does not refute the possibility of a later variational derivation. It identifies precisely why the expectation-value representation by itself is insufficient.

## 7. Scope

- The diagonal expectation identity and the finite/countable convex-hull statements are proved.
- For a countably infinite index set, the attainable set is a barycentre set whose closure, not necessarily the set itself, is the closed convex hull.
- The non-uniqueness statement applies whenever the number of independently variable modes exceeds the number of independent constraints.
- The application concerns the expectation-value construction in the cited GSR preprint; it is not a claim about every possible future version of the Pellis operator.
- No identification with the Q6, PRISM or Fibonacci \(D_6\) operators is asserted.
