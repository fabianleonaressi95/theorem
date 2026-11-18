# Document B — Geometric self-adjoint operators and spectral weights

**Prepared for discussion with Stergios Pellis**

**Scope:** rigorous operator-theoretic framework on the compact spherical space form
\[
M=S^3/2I
\]
with the unit round quotient metric. The scalar Laplacian is the operator already treated in Document A. This note establishes the self-adjoint realization, its spectral projections, and the meaning of state weights. Hodge and Rumin operators are separated according to what is established and what still requires a specific domain construction.

**Evidence policy:** no Pellis resonance operator, golden-sphere operator, or physical state is identified with a geometric Laplacian by assumption.

---

## B.1 Definitions and conventions

Let \(M\) be a smooth compact Riemannian manifold without boundary. In the application below, \(M=S^3/2I\), where \(2I\) acts freely by left multiplication and the metric is induced from the unit round metric on \(S^3\).

The scalar Hilbert space is
\[
\mathcal H_0=L^2(M,d\mathrm{vol}_g),
\qquad
\langle u,v\rangle=\int_M\overline{u}\,v\,d\mathrm{vol}_g.
\]
The inner product is conjugate-linear in its first argument.

The positive Laplace–Beltrami operator on smooth functions is
\[
\Delta_0=-\operatorname{div}_g\nabla_g.
\]
On \(C^\infty(M)\), it is symmetric and nonnegative:
\[
\langle u,\Delta_0v\rangle
=\int_M\langle du,dv\rangle_g\,d\mathrm{vol}_g,
\qquad
\langle u,\Delta_0u\rangle\geq0.
\]

For \(p\)-forms, define
\[
\mathcal H_p=L^2(M;\Lambda^pT^*M\otimes\mathbb C),
\qquad
\Delta_p=dd^*+d^*d
\]
on smooth forms. Here \(d^*\) is the formal \(L^2\)-adjoint of the exterior derivative \(d\).

The Sobolev space \(H^s(M)\), or \(H^s(M;\Lambda^pT^*M)\), is defined using any smooth auxiliary connection and a finite atlas. On a compact manifold, different such choices give equivalent norms.

## B.2 Scalar Laplacian: self-adjoint realization

### Definition B.1 — Energy form

On \(L^2(M)\), define
\[
q_0[u,v]=\int_M\langle du,dv\rangle_g\,d\mathrm{vol}_g,
\qquad
D(q_0)=H^1(M).
\]
This is a densely defined, closed, nonnegative sesquilinear form.

The associated operator \(A_0\) is defined by
\[
\begin{aligned}
D(A_0)=\{u\in H^1(M):\ &\exists f\in L^2(M)
\\[-2mm]
& q_0[u,v]=\langle f,v\rangle
\quad\forall v\in H^1(M)\},
\end{aligned}
\]
and \(A_0u=f\).

### Theorem B.2 — Self-adjointness and compact resolvent

For a smooth compact Riemannian manifold without boundary, the operator associated with \(q_0\) is the unique nonnegative self-adjoint realization of the positive scalar Laplace–Beltrami operator obtained by closing its action on \(C^\infty(M)\). Its operator domain is
\[
D(A_0)=H^2(M),
\]
and \(A_0u=-\operatorname{div}_g\nabla_gu\) in the distributional sense.

Moreover, \(A_0\) has compact resolvent. Its spectrum consists of real nonnegative eigenvalues of finite multiplicity, with no finite accumulation point:
\[
0=\lambda_0\leq\lambda_1\leq\lambda_2\leq\cdots,
\qquad \lambda_j\longrightarrow+\infty,
\]
where eigenvalues are repeated according to multiplicity.

### Proof

The form \(q_0\) is densely defined, closed, and nonnegative on \(H^1(M)\). The representation theorem for closed nonnegative forms therefore gives a unique nonnegative self-adjoint operator \(A_0\). Integration by parts on the closed manifold identifies its distributional action with \(-\operatorname{div}_g\nabla_g\). Elliptic regularity for the smooth uniformly elliptic Laplace–Beltrami operator gives \(D(A_0)=H^2(M)\). The embedding \(H^1(M)\hookrightarrow L^2(M)\) is compact by Rellich's theorem; equivalently, the resolvent maps bounded subsets of \(L^2\) into bounded subsets of \(H^1\), so the resolvent is compact. The spectral theorem for compact self-adjoint resolvents gives the stated discrete spectrum. \(\square\)

**Hypotheses matter.** The absence of boundary is used here. If a domain has a boundary, a boundary condition (for example Dirichlet, Neumann, or a specified Robin condition) is part of the operator definition and changes its domain and spectrum.

## B.3 Application to the Poincaré spherical space

For the unit round quotient \(M=S^3/2I\), Document A establishes
\[
\lambda_k=k(k+2),\qquad k\geq0,
\]
and
\[
d_k=(k+1)\dim\bigl(\operatorname{Sym}^k(\mathbb C^2)^{2I}\bigr)
=(k+1)[t^k]\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]

The corresponding eigenspace is
\[
E_k=\ker(A_0-\lambda_k I),
\qquad \dim E_k=d_k.
\]
Let \(P_k\) denote the orthogonal projection in \(L^2(M)\) onto \(E_k\). The index \(k\) labels the harmonic degree, not the order of distinct eigenvalues in an arbitrary sorted list. If an eigenvalue has multiplicity greater than one, \(P_k\) projects onto the entire eigenspace.

The first positive eigenvalue and multiplicity are
\[
\lambda_{\min}^+=168,\qquad \dim E_{12}=13.
\]
The scalar spectrum is not the spectrum of the Hodge Laplacian on one-forms, the Dirac operator, or the Rumin Laplacian. Those are different operators on different Hilbert spaces.

## B.4 Spectral projections and state weights

### Definition B.3 — State and spectral weight

A state for the scalar problem is a vector
\[
\psi\in\mathcal H_0=L^2(M).
\]
It is normalized when \(\|\psi\|_{L^2}=1\).

For each eigenspace projection \(P_k\), define its spectral weight in the state \(\psi\) by
\[
\boxed{
w_k(\psi)=\langle\psi,P_k\psi\rangle
=\|P_k\psi\|_{L^2}^2.
}
\]
This definition uses the full eigenspace projection and is independent of the choice of orthonormal basis inside a degenerate eigenspace.

### Proposition B.4 — Positivity and normalization

For every \(\psi\in L^2(M)\),
\[
w_k(\psi)\geq0,
\qquad
\sum_{k\geq0}w_k(\psi)=\|\psi\|_{L^2}^2.
\]
In particular, for a normalized state the weights are nonnegative and sum to one.

### Proof

An orthogonal projection is self-adjoint and idempotent, so
\[
\langle\psi,P_k\psi\rangle
=\langle P_k\psi,P_k\psi\rangle
=\|P_k\psi\|^2\geq0.
\]
The eigenspaces of a self-adjoint operator with distinct eigenvalues are orthogonal. Compact resolvent gives a complete orthogonal decomposition of the Hilbert space into these eigenspaces. Parseval's identity therefore yields the sum rule. \(\square\)

The associated scalar spectral measure is
\[
\mu_\psi=\sum_{k\geq0}w_k(\psi)\,\delta_{\lambda_k}.
\]
For any bounded Borel function \(F\),
\[
\langle\psi,F(A_0)\psi\rangle
=\int_{\mathbb R}F(\lambda)\,d\mu_\psi(\lambda)
=\sum_{k\geq0}F(\lambda_k)w_k(\psi).
\]
For unbounded \(F\), this formula is valid when \(\psi\) belongs to the domain of the corresponding functional calculus expression (or when the relevant integral is finite).

### Degeneracy and basis independence

If \(\{e_{k,a}\}_{a=1}^{d_k}\) is any orthonormal basis of \(E_k\), then
\[
P_k\psi=\sum_{a=1}^{d_k}e_{k,a}\langle e_{k,a},\psi\rangle,
\qquad
w_k(\psi)=\sum_{a=1}^{d_k}|\langle e_{k,a},\psi\rangle|^2.
\]
The sum is invariant under unitary changes of basis in \(E_k\). A weight assigned to an individual basis vector is not invariant under such changes when \(d_k>1\). Thus a proposed state-selection rule must specify additional commuting observables if it intends to resolve a degenerate eigenspace into smaller channels.

## B.5 Hodge Laplacians: established operator framework

On complex \(p\)-forms, the quadratic form
\[
q_p[\omega,\eta]
=\langle d\omega,d\eta\rangle_{L^2}
+\langle d^*\omega,d^*\eta\rangle_{L^2}
\]
has its natural closed extension to the first-order Sobolev form domain. On a smooth compact manifold without boundary, the associated Hodge Laplacian
\[
\Delta_p=dd^*+d^*d
\]
is nonnegative and self-adjoint, has domain \(H^2(M;\Lambda^pT^*M)\), and has compact resolvent.

Its spectral projections and weights are defined exactly as in B.4, now with
\[
\psi\in L^2(M;\Lambda^pT^*M).
\]
The Hodge decomposition and the zero eigenspace encode de Rham cohomology; this is a separate statement from the scalar invariant-harmonic calculation in Document A.

**What is not claimed:** no numerical \(p\)-form spectrum or multiplicity table for \(S^3/2I\) is supplied here. The scalar values \(k(k+2)\) and \(d_k\) cannot be copied to \(p>0\).

## B.6 Rumin operators: a separate domain and order problem

The Rumin complex is a differential complex adapted to a contact structure. Its middle-degree differential has a different differential order from the ordinary de Rham differential. A Rumin Laplacian is therefore not obtained by merely relabelling the Hodge Laplacian.

For a specific compact contact manifold, a self-adjoint spectral problem requires all of the following to be stated:

1. the contact form and contact distribution;
2. the graded Rumin bundles and their Hermitian metrics;
3. the differential operators and formal adjoints in the chosen conventions;
4. the positive Rumin Laplacian in each degree, including its differential order;
5. its closed quadratic form or a proved self-adjoint operator domain;
6. the compactness or subelliptic estimate needed to establish compact resolvent;
7. the precise quotient action and its invariant subspaces.

The analytic torsion formulas of Kitaoka and the Rumin–Seshadri framework concern additional spectral and determinant data. They do not, by themselves, supply every fixed-basis matrix or every operator-domain identification required for the present \(S^3/2I\) model.

**Current classification:** the scalar and ordinary Hodge Laplacian statements above are standard elliptic operator results on a closed compact manifold. A complete fixed-convention Rumin operator/domain audit on the chosen quotient remains a separate task. No Rumin eigenvalue or torsion value is inferred in this document.

## B.7 Important distinction: eigenvalues, spectral weights, and resonances

The word *resonance* is used in several mathematically different ways.

- **Eigenvalue of a self-adjoint operator:** a real spectral point with a nonzero Hilbert-space eigenspace.
- **Spectral weight:** the nonnegative number \(\langle\psi,P_\lambda\psi\rangle\) associated with the orthogonal projection onto that eigenspace (or, more generally, the spectral measure of a Borel set).
- **Scattering resonance:** typically a pole of a meromorphically continued resolvent for a noncompact or open problem. Such a pole is generally not an eigenvalue of a self-adjoint operator on the original Hilbert space, and its residue is not automatically an orthogonal projection.
- **Damped or non-self-adjoint mode:** a spectral value of a non-self-adjoint generator may be complex. The orthogonal-projection formula in B.4 does not apply without additional structure.

Consequently, if a Golden Spheres Resonance model uses the term *resonance*, its operator, Hilbert space, boundary/open-system conditions, and spectral notion must be specified before its modes can be compared with the compact self-adjoint spectrum of \(S^3/2I\).

## B.8 Verification and reproducibility

The operator-theoretic assertions in B.2 and B.5 follow from the closed-form representation theorem, elliptic regularity, Rellich compactness, and the spectral theorem. They are not numerical discoveries of the repository.

The quotient-specific scalar multiplicities are verified in Document A by exact arithmetic. Reproduce the finite audit from the repository root:
\`\`\`bash
python -m audits.a1_poincare_scalar_spectrum --max-degree 120
python -m unittest tests.test_a1_poincare_scalar_spectrum -v
\`\`\`
The recorded A1/T035 workflow run is [43891483378](https://github.com/fabianleonaressi95/theorem/actions/runs/43891483378). The A1 exact comparison checks all 121 degrees from 0 through 120; it does not numerically approximate eigenfunctions or compute Hodge/Rumin spectra.

A future numerical spectral-weight experiment must publish, at minimum:
- the Hilbert-space discretization and inner product;
- the operator matrix and its symmetry/self-adjointness residual in that inner product;
- the eigenvalue clusters and orthogonal spectral projectors;
- the state \(\psi\), its normalization, and the method used to project it;
- convergence under mesh/basis refinement and stability under basis changes within degenerate eigenspaces.

## B.9 Limits and physical interpretation

The present result gives a mathematically controlled meaning to geometric spectral channels and their state weights on a compact quotient. It does not identify a physical excitation, a particle, a coupling constant, or a Pellis resonance.

The quantity \(w_k(\psi)\) can be interpreted as the fraction of the squared Hilbert norm of a specified state lying in the \(k\)-th scalar eigenspace. A physical interpretation requires an independently defined state-preparation rule, observable, dynamics, and measurement map. The geometry alone determines the operator and its spectral subspaces; it does not select a preferred \(\psi\).

The next document can compare Pellis Functions and Golden Spheres Resonance with these definitions. The comparison must first define Pellis's functions and resonance operator independently, then test whether a map intertwines the operators or their spectral measures. A matching numerical value alone is not an equivalence.

---

## References

1. M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, revised and enlarged edition, Academic Press, 1980 — closed quadratic forms and the representation theorem.
2. M. Reed and B. Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators*, Academic Press, 1978 — self-adjoint operators and spectral theory.
3. M. E. Taylor, *Partial Differential Equations II: Qualitative Studies of Linear Equations*, 2nd ed., Springer, 2011 — elliptic regularity and elliptic operators on compact manifolds.
4. A. Ikeda, “On the spectrum of a Riemannian manifold of positive constant curvature,” *Osaka Journal of Mathematics* 17 (1980), 75–93 — spherical space-form spectral analysis.
5. A. Kitaoka, “Analytic torsions associated with the Rumin complex on contact spheres,” *International Journal of Mathematics* 31 (2020), 2050112, arXiv:1911.03092.
6. M. Rumin and N. Seshadri, “Analytic torsions on contact manifolds,” *Annales de l’Institut Fourier* 62 (2012), 727–782, DOI: 10.5802/aif.2693.

**Classification:** B.2–B.5 are established operator-theoretic results under the stated compactness, smoothness, and no-boundary hypotheses; the quotient-specific scalar multiplicities are exact finite-audit results from Document A; the fixed-convention Rumin realization and all Pellis/Golden-Spheres identifications remain open.
