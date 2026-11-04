# Theorem 001 — Fixed-lattice temporal Wilson limit

**Status:** proved under the hypotheses below.  
**Scope:** temporal continuum limit at fixed spatial lattice. This is not a spatial continuum-limit theorem.

## 1. Setting

Let \(G=(V,E)\) be a finite oriented graph with \(|E|=M<\infty\). Fix spatial spacing \(a_s>0\) and coupling \(g^2>0\). The electric-flux Hilbert space is
\[
\mathcal H=\ell^2(\mathbb Z^E).
\]
A flux configuration is \(n=(n_e)_{e\in E}\). If Gauss constraints are imposed, let \(\mathcal H_{\rm phys}\subseteq\mathcal H\) be the closed span of flux configurations satisfying them.

For temporal spacing \(a_t>0\), put
\[
\beta_t=\frac{a_s^4}{g^2a_t},\qquad
r_{a_t}(n)=\prod_{e\in E}\frac{I_{|n_e|}(\beta_t)}{I_0(\beta_t)},
\]
where \(I_k\) is the modified Bessel function of the first kind. Define the diagonal contraction \(K_{a_t}\) by
\[
(K_{a_t}\psi)(n)=r_{a_t}(n)\psi(n).
\]

## 2. Theorem

For every fixed finite graph \(G\), every \(a_s,g^2>0\), and every \(t\geq0\),
\[
\boxed{\quad
K_{a_t}^{\lfloor t/a_t\rfloor}
\xrightarrow[a_t\downarrow0]{\rm strong}
e^{-tH_E}
\quad}
\]
on \(\mathcal H\), where
\[
(H_E\psi)(n)=
\frac{g^2}{2a_s^4}
\left(\sum_{e\in E}n_e^2\right)\psi(n).
\]
The same strong convergence holds on any closed Gauss-law subspace \(\mathcal H_{\rm phys}\).

Equivalently, the limiting electric Hamiltonian is
\[
H_E=\frac{g^2}{2a_s^4}\sum_{e\in E}\hat n_e^2.
\]

## 3. Proof

Fix a flux configuration \(n\). Since \(\beta_t\to\infty\), the fixed-order Bessel asymptotic gives, for every fixed integer \(k\),
\[
\frac{I_k(\beta)}{I_0(\beta)}
=1-\frac{k^2}{2\beta}+O(\beta^{-2}),
\qquad \beta\to\infty.
\]
Because \(E\) is finite, multiplying these expansions yields
\[
r_{a_t}(n)
=1-\frac{1}{2\beta_t}\sum_e n_e^2+O(\beta_t^{-2}),
\]
and therefore
\[
-\frac{1}{a_t}\log r_{a_t}(n)
\longrightarrow
\frac{g^2}{2a_s^4}\sum_e n_e^2=:\mathcal E(n).
\]
It follows, since \(a_t\lfloor t/a_t\rfloor\to t\), that
\[
r_{a_t}(n)^{\lfloor t/a_t\rfloor}
\longrightarrow e^{-t\mathcal E(n)}.
\]

For integer \(k\), \(0<I_k(\beta)\leq I_0(\beta)\). Hence
\[
0\leq r_{a_t}(n)^{\lfloor t/a_t\rfloor}\leq1.
\]
For any \(\psi\in\ell^2(\mathbb Z^E)\), the squared norm of the difference is
\[
\sum_{n\in\mathbb Z^E}|\psi(n)|^2
\left|r_{a_t}(n)^{\lfloor t/a_t\rfloor}
-e^{-t\mathcal E(n)}\right|^2.
\]
The summand converges pointwise to zero and is bounded by \(4|\psi(n)|^2\), a summable sequence. Dominated convergence for counting measure proves strong convergence.

Both operators are diagonal in the flux basis. Thus every subspace spanned by a subset of flux basis vectors, in particular the Gauss-law subspace, is invariant, and the same argument applies to its restriction. \(\square\)

## 4. What this theorem does not prove

It does **not** establish any of the following:

- a spatial continuum limit \(a_s\downarrow0\);
- convergence of the magnetic Wilson term or of the full interacting transfer operator;
- a non-Abelian \(SU(3)\) continuum limit;
- convergence of a five-mode marginal or identification with a Bergman/D5 measure.

Those are separate statements and must each receive their own theorem and proof. No numerical fit or adjustable cutoff enters this theorem.

## 5. Minimal reproducibility check

The proof is analytic. A numerical check may compare
\[
-\frac{1}{a_t}\log\frac{I_k(\beta_t)}{I_0(\beta_t)}
\quad\text{with}\quad
\frac{g^2k^2}{2a_s^4}
\]
for fixed integers \(k\), but such a check is not a substitute for the proof above.
