# Golden / supergolden synthesis for curvilinear de Rham–FEEC

**Status:** mathematical synthesis and theorem programme. Algebraic identities below are proved under their stated assumptions; the geometric refinement proposal is conditional; Mosco, compactness, norm-resolvent, and harmonic-kernel conclusions are not claimed for the repository benchmark until the listed lemmas are established.

## 1. Governing principle

The curvilinear de Rham benchmark, consistent cubical FEEC masses, and independent audit form one problem: construct uniformly stable finite-dimensional Hilbert complexes on curvilinear meshes, identify their adjoints through metric mass matrices, and prove convergence of the associated closed quadratic forms to the continuum Hodge form.

The golden ratio and supergolden constant do not alter the exterior derivative and are not extra physical axioms. Their legitimate role is to organize candidate mesh families, scale recurrences, and explicit constants. Every claim must be classified as proved identity, conditional theorem, numerical observation, or open conjecture.

The simplification is to factor the programme into (A) geometric scale law, (B) uniformly stable Hilbert-complex approximation, and (C) form convergence. No spectral computation replaces (B) or (C).

## 2. Exact de Rham–FEEC core

On the reference cube [0,1]^d, use the lowest-order tensor-product cubical spaces
\[
\widehat V^k=\bigoplus_{|I|=k}
\left(\bigotimes_{j\notin I}Q_1(\widehat x_j)\right)
\otimes\left(\bigotimes_{i\in I}Q_0(\widehat x_i)\right)d\widehat x^I,
\quad I=(i_1<\cdots<i_k).
\]
For an orientation-preserving cell diffeomorphism F_K, define the physical space by the covariant pullback: F_K^* V_h^k(K)=\widehat V^k. Naturality gives F_K^*(d\omega)=d(F_K^*\omega). This is exact for sufficiently regular maps and explains why incidence matrices are topological. It does not imply projection stability or approximation.

With A=DF_K, ambient metric G, and pullback metric g=A^TGA, the exact local Gram matrix is
\[
(M_K^k)_{ab}=\int_{\widehat K}
\widehat\phi_a^T\Lambda^k(g^{-1})\widehat\phi_b\sqrt{\det g}\,d\widehat x.
\]
For k=0 the exterior-power factor is 1; for k=d it is (det g)^(-1). For unit-integral top-form DoFs and an orientation-preserving affine map, the top mass is 1/vol_g(K). Curved-cell integration retains the pointwise metric density.

For coefficient inner products (u,v)_{h,k}=u^T M_{h,k}v and incidence D_{k-1}:V_h^{k-1}->V_h^k, the Hilbert adjoint is exactly
\[
\delta_h^k=M_{h,k-1}^{-1}D_{k-1}^TM_{h,k},
\]
provided the masses are symmetric positive definite and the domain/codomain convention for D is fixed.

### Orientation prerequisite

The merged independent audit identifies a sign mismatch between the current incidence convention in ddr/mesh.py and the ordered coordinate-wedge convention used for the FEEC basis. Before claiming a commuting diagram, choose one convention globally:
1. standard cubical coefficient (-1)^p(2s-1), with zero-based removed-axis position p; or
2. retain current matrices but change every degree-wise face orientation and basis/DoF sign consistently.

Add a local regression test for d(phi_sigma)=sum_tau D[tau,sigma]phi_tau in every degree. D_{k+1}D_k=0 alone cannot detect a global sign reversal. Spectra may also remain unchanged while the declared differential/basis identification is wrong.

## 3. Legitimate roles of phi and psi

Let phi=(1+sqrt(5))/2, so phi^2=phi+1. Let psi>1 solve psi^3-psi^2-1=0, so psi^3=psi^2+1. These give exact algebraic recurrences, not automatic mesh properties.

### 3.1 Supergolden scale schedule

A candidate isotropic schedule h_n=h_0 psi^(-n) obeys
\[
h_{n-3}=h_{n-2}+h_n.
\]
This is exact scale bookkeeping, not proof that conforming cubical meshes exist at these scales. A mesh construction must specify integer subdivisions, cell maps, interface conformity, and realization of non-integer ratios.

If a concrete refinement operator R on geometric data is constructed and satisfies R^3=R^2+I, then R^(n+3)=R^(n+2)+R^n. This follows by multiplying the operator identity by R^n. It becomes a mesh law only after invariance and conformity of the admissible mesh family are proved.

### 3.2 Golden internal proportions

A candidate cell template may split with t=phi^(-1) and 1-t=phi^(-2), since 1=phi^(-1)+phi^(-2). Repeated golden splits can create nonuniform sizes. Shape regularity therefore requires explicit lower bounds on child aspect ratios and Jacobian singular values; phi alone does not guarantee it.

### 3.3 Route to useful FEEC constants

Assume uniformly over cells and levels
\[
c_A h_K|\xi|\le |DF_K(\hat x)\xi|\le C_A h_K|\xi|,
\quad 0<c_J\le h_K^{-d}|\det DF_K|\le C_J,
\]
with normalized map derivatives bounded to the order required by approximation theory. Then scaled pullback metrics are uniformly elliptic. Mass norm equivalence and approximation constants depend on these geometric bounds, not on the label of the refinement ratio.

Golden/supergolden geometry is useful only if it yields explicit level-independent constants or sharper recurrences for them. Otherwise it is decorative and should not enter the proof.

## 4. Conditional FEEC–Mosco theorem

Let H^k be continuum L2 k-forms on a fixed compact Lipschitz domain/manifold with uniformly elliptic metric. Let V^bullet be the closed de Rham Hilbert complex, with form
\[
q_k(u)=\|d_ku\|^2+\|\delta_ku\|^2
\]
on the joint graph domain. For each n let V_n^bullet be a finite-dimensional subcomplex with discrete differential d_n, positive masses, and reconstruction maps J_n:V_n^k->H^k.

Assume:

**H1 Geometry.** Cell maps are orientation-preserving diffeomorphisms; scaled Jacobians and inverse Jacobians are uniformly bounded; pullback metrics are uniformly elliptic; face maps and traces match across cells.

**H2 Complex and orientation.** d_n^2=0, local basis/DoF orientations agree with incidence matrices, and pullback commutes with d.

**H3 Uniform norm equivalence.** Reconstructed mass inner products are uniformly equivalent to continuum L2 norms.

**H4 Commuting bounded projections.** Projections pi_n^k exist on the relevant graph domains, satisfy d_n pi_n^k=pi_n^{k+1}d, have sup_n ||pi_n^k|| bounded, and converge strongly to identity.

**H5 Joint graph recovery.** For every u in the continuum form domain there are u_n with J_nu_n->u and reconstructed d_nu_n, delta_nu_n converging weakly to du, delta u, with energy limsup no greater than q_k(u).

**H6 Liminf.** If J_nu_n converges weakly to u and discrete energies are bounded, then u is in the continuum form domain and q_k(u)<=liminf q_{n,k}(u_n).

**H7 Compactness.** Bounded discrete graph-energy sequences are precompact after reconstruction on the co-closed subspaces needed for Hodge decomposition.

**H8 Topology and gap.** Discrete cohomology dimensions eventually equal continuum Betti numbers; harmonic projections are controlled and the positive spectrum has a uniform gap away from zero.

Then H5-H6 give generalized Mosco convergence of the reconstructed forms; the associated operators converge in strong resolvent sense. With H7-H8, isolated bounded positive spectral windows converge with multiplicity and harmonic subspaces converge in gap.

This is a conditional theorem programme, not a result already proved for the repository benchmark. Norm-resolvent convergence is not included: it needs additional uniform collective compactness/equicontinuity of reconstructed resolvents, or an appropriate uniform compact embedding.

### Why commutation alone is insufficient

d_n pi_n=pi_n d controls only d. It gives no uniform bound on ||pi_n||, no graph-norm approximation, no control of delta, no convergence of mass inner products, no compactness, and no topology/kernel stability. Since delta_n is defined by M_n and D_n together, convergence of the algebraic differential alone cannot imply convergence of adjoints.

## 5. Keep convergence notions separate

1. Mosco convergence requires a liminf inequality and recovery sequences in a common (possibly generalized) Hilbert-space framework.
2. Discrete compactness requires precompactness of bounded graph-energy sequences, usually after removing exact components or restricting to co-closed spaces.
3. Strong-resolvent convergence follows from suitable closed-form convergence and compatible identification maps.
4. Norm-resolvent convergence is stronger and typically requires collective compactness of resolvents; strong convergence is insufficient.
5. Harmonic-kernel stability requires cohomology control and a uniform positive gap. Mosco convergence alone does not preclude spurious small eigenvalues or changing kernel dimension.

## 6. Candidate laws, explicitly conditional

**Law A — scale cocycle.** If a conforming refinement operator R is actually defined and R^3=R^2+I, then every linear observable s_n=L(R^n x) satisfies s_{n+3}=s_{n+2}+s_n. Proof: apply L to R^(n+3)x=(R^(n+2)+R^n)x. This may simplify cell-count or estimator recurrences, but only after R is constructed.

**Law B — metric mass scaling.** Under a similarity F_h(xhat)=x0+hB xhat, with fixed invertible B, a covariant k-form L2 Gram matrix scales as h^(d-2k): volume contributes h^d and the squared covector norm contributes h^(-2k). This exponent is dimensional, not golden. A phi/psi schedule changes h between levels, not the local exponent.

**Law C — finite-template shape regularity.** If a golden split uses finitely many child templates whose normalized singular values lie in [c,C], and templates are reused by similarities, the shape constants are uniform across levels. This follows from finite template bounds and composition estimates. The bounds must be calculated; phi alone is insufficient.

**Law D — spectral rate conversion.** If a proven eigenvalue estimate is |lambda_{n,j}-lambda_j|<=C h_n^r, then h_n=h0 psi^(-n) gives error <=C h0^r psi^(-rn). The approximation order r comes from polynomial degree, regularity, and spectral theory, not from psi.

## 7. Counterexample logic

- Commuting projections can have diverging operator norms; commutation does not imply uniform stability.
- Varying inner products can change adjoints while leaving the algebraic differential fixed; convergence of d_n does not imply convergence of delta_n.
- Strong-resolvent convergence does not imply norm-resolvent convergence; high-frequency subspaces can obstruct operator-norm convergence.
- Form convergence without topology control does not by itself stabilize kernel dimensions; a uniform gap and cohomology control are needed.
- Global reversal of all D_k preserves D_{k+1}D_k=0 and many quadratic spectra but conflicts with fixed basis orientations unless DoF signs are also reversed.

These are logical obstructions. The repository should record explicit finite-dimensional/operator examples as theorem tests, not misrepresent them as numerical evidence about the current mesh family.

## 8. Lemma programme, in efficient order

1. Orientation lemma: local incidence/exterior-derivative identity in every degree.
2. Pullback lemma: F_K^*d=dF_K^* and trace compatibility.
3. Mass lemma: symmetry/positive definiteness of exact Gram matrices and uniform quadrature perturbation.
4. Metric equivalence lemma: uniform L2 norm equivalence from singular-value/Jacobian bounds.
5. Adjoint lemma: derive the M^(-1)D^TM formula from coefficient inner products and verify matrix ordering.
6. Commuting projection lemma: construct pi_n on the actual curvilinear family.
7. Projection stability lemma: prove sup_n ||pi_n||<infinity.
8. Graph recovery lemma: approximation in the joint graph norm of d and delta.
9. Liminf lemma: weak lower semicontinuity of reconstructed energies.
10. Discrete compactness lemma: precompactness of bounded-energy co-closed sequences.
11. Cohomology lemma: identify discrete and continuum cohomology.
12. Gap lemma: uniform lower bound on the first positive eigenvalue.
13. Mosco theorem: combine liminf and recovery.
14. Resolvent theorem: strong resolvent; add collective compactness for norm resolvent.
15. Optional golden refinement lemma: construct a conforming finite-template operator with exact phi/psi recurrence and prove uniform shape regularity. Pursue only if it improves constants or construction complexity.

## 9. Immediate research actions

1. Treat merged PR #87 and merged independent audit as the baseline.
2. Do not change incidence signs until a local basis-derivative test fixes the convention; then correct all degrees consistently.
3. Keep historical diagonal, top-degree-corrected diagonal, and consistent FEEC masses distinct.
4. State exact Jacobian, derivative, and face-matching assumptions for every mesh family.
5. Do not label finite-level spectral stabilization as Mosco convergence or discrete compactness.
6. Use psi scales only after a conforming refinement construction exists; use phi splits only after child-shape bounds are proved.

## 10. Status table

| Claim | Status |
|---|---|
| Covariant pullback commutes with exterior derivative | Proved identity under smooth diffeomorphism assumptions |
| FEEC Gram formula | Correct under declared metric and basis conventions |
| Discrete codifferential formula | Exact finite-dimensional identity |
| Current incidence orientation | Mismatch reported by independent audit; local regression/correction required |
| phi^2=phi+1 and psi^3=psi^2+1 | Exact algebra |
| Conforming phi/psi cubical refinement family | Open construction |
| Uniform commuting projections on benchmark family | Open |
| Mosco convergence for benchmark family | Open |
| Discrete compactness and harmonic stability | Open |
| Strong-/norm-resolvent convergence | Open; norm resolvent needs extra compactness |
| Golden/supergolden improvement of FEEC constants | Candidate; requires explicit template estimates |

This note supplements, and does not replace, INDEPENDENT_MATHEMATICAL_AUDIT.md and CONSISTENT_FEEC_MASS.md. Golden and supergolden constants are exact algebraic tools for a possible refinement family, not unexplained weights in the metric, mass matrices, or differential.
