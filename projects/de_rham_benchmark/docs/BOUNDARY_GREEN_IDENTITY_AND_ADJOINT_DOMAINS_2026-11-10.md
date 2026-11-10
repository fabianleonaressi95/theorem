# Boundary Green identity and the discrete codifferential: analytical status

**Date:** 10 November 2026  
**Project:** `projects/de_rham_benchmark`  
**Purpose:** identify precisely which continuous operator is approximated by the unconstrained algebraic FEEC adjoint and specify the boundary-compatible convergence problem.

## 1. The issue

The benchmark defines
\[
\delta_h^k=M_{k-1}^{-1}D_{k-1}^{T}M_k.
\]
This is, by construction, the Hilbert-space adjoint of the discrete exterior derivative on the *unconstrained finite-dimensional cochain spaces*. It is not automatically a consistent approximation of the strong codifferential on a domain with boundary.

The numerical boundary layer reported in `FEEC_PROJECTIONS.md` is therefore not a small implementation detail. It signals a mismatch between the operator domain used for the algebraic adjoint and the boundary domain of the intended continuous operator.

## 2. Continuous Green identity

Let \(\Omega\subset\mathbb R^d\) be a bounded Lipschitz domain with smooth metric \(g\), and let \(u\) be a smooth \((k-1)\)-form and \(v\) a smooth (k)-form. The formal codifferential \(\delta\) is the (L^2)-formal adjoint of (d). The integration-by-parts identity has the form
\[
(d u,v)_{L^2\Lambda^k(\Omega)}
-(u,\delta v)_{L^2\Lambda^{k-1}(\Omega)}
=\mathcal B_{\partial\Omega}(u,v),
\tag{2.1}
\]
where the boundary pairing is the metric trace pairing between the tangential trace of (u) and the appropriate normal trace of (v). In Euclidean notation it can be written, up to the conventional orientation sign, as
\[
\mathcal B_{\partial\Omega}(u,v)
=\int_{\partial\Omega}
\langle \operatorname{tr}_{\tan}u,
\operatorname{tr}_{\nor}v\rangle\,dS.
\tag{2.2}
\]
The exact trace spaces are the (H\Lambda) and (H^*\Lambda) trace spaces; for nonsmooth forms (2.1) is interpreted by continuous extension/duality, not by assuming pointwise boundary values.

Thus the Hilbert adjoint of (d) depends on the domain assigned to (d). If (d) is taken on the maximal domain, its adjoint is the codifferential on the corresponding minimal domain, and conversely. The boundary condition is part of the operator, not an optional numerical correction.

## 3. Why the unconstrained matrix adjoint contains a boundary layer

Let (V_h^{k-1}\xrightarrow{D_{k-1}}V_h^k) be the full, unconstrained cochain complex with positive definite mass matrices (M_{k-1},M_k). For every cochain pair (x,y),
\[
(D_{k-1}x)^TM_k y
=x^TM_{k-1}(\delta_h^k y).
\tag{3.1}
\]
There is no boundary restriction in (3.1): it is the adjoint identity on the entire finite-dimensional spaces.

The continuous identity (2.1), however, has a nonzero boundary functional unless the chosen traces vanish or the relevant natural boundary condition is imposed. Therefore the consistency target cannot be selected independently of the discrete operator domain.

For a smooth form with nonzero boundary flux, the interpolated cochain can produce a residual concentrated on boundary degrees of freedom. Since the boundary has codimension one, its number of degrees of freedom scales like (h^{-(d-1)}), while the volume scales like (h^{-d}). A boundary-supported coefficient can consequently grow as the mesh is refined even when its action on test functions has a finite boundary-functional limit. This explains why a pointwise or global coefficient norm can fail to converge while an interior residual converges.

This scaling argument is explanatory, not a proof of the precise (O(h^{-1})) coefficient amplitude for every mesh family. That rate must be established for the actual basis, mass scaling and trace convention.

## 4. Operator-domain choices that must be kept separate

There are at least two mathematically distinct formulations.

### A. Relative / essential complex

Choose the closed realization of (d) with the relevant tangential trace constrained (the relative de Rham complex). At the discrete level, restrict the cochain spaces to the corresponding boundary subcomplex and form the adjoint using the restricted mass matrices and incidence operator.

The discrete adjoint is then the adjoint of the *restricted* discrete differential. Its continuous limit must be compared with the codifferential on the dual boundary domain. The boundary condition must be stated degree by degree; simply zeroing all boundary DOFs is not a valid universal prescription for every form degree.

### B. Absolute / natural complex

Keep the maximal de Rham domain and use its Hilbert adjoint, which has the complementary natural trace condition. At the discrete level, retain the full cochain complex, but compare the discrete adjoint through the weak Green identity, including the boundary pairing. A strong pointwise comparison with \(\delta u\) alone is not the correct global consistency statement when the trace term is nonzero.

These two formulations are dual alternatives, not two numerical settings that may be mixed in a single convergence proof.

## 5. What the existing benchmark does and does not show

The current implementation establishes algebraic adjointness exactly up to solver accuracy and reports global, interior, core and boundary residuals. It also observes that compactly supported test forms avoid the boundary layer and that the fixed-core residual decreases under refinement.

These observations support the diagnosis of a boundary-domain mismatch. They do **not** establish:
- convergence of the full unconstrained adjoint in the global graph norm;
- convergence of the boundary residual to the correct trace functional;
- equivalence of the relative and absolute discrete complexes;
- discrete compactness or Mosco convergence.

## 6. A falsifiable next experiment

The next code change should not silently impose a boundary condition. It should implement and compare two separately named complexes:

1. **Full complex:** current spaces and matrices, unchanged.
2. **Relative complex:** boundary trace subspaces selected from the relative de Rham complex, with restricted incidence and restricted consistent mass matrices.

For each refinement level and each form, report:
- Betti numbers of the full and relative complexes;
- dimensions of every constrained cochain space;
- exactness residual (D_{k+1}D_k);
- symmetry and smallest eigenvalue of every restricted mass matrix;
- algebraic adjoint residual for the restricted matrices;
- strong codifferential residual on forms satisfying the corresponding continuous boundary condition;
- weak Green-identity residual including the computed boundary pairing;
- global, boundary and fixed-core norms separately.

Required test forms:
- a constant form with nonzero boundary trace/flux;
- a smooth form satisfying the selected relative boundary condition;
- a compactly supported smooth form;
- an exact form and its exterior derivative.

The two complexes must be reported separately. A smaller residual obtained by constraining DOFs is not evidence of convergence unless the continuous operator domain and the expected cohomology are also matched.

## 7. Acceptance criteria

The experiment is successful only if:
1. the constrained incidence matrices still form a complex to machine precision;
2. restricted masses are symmetric positive definite on the retained spaces;
3. the restricted matrix adjoint identity holds to the linear-solver tolerance;
4. the strong codifferential residual decreases for test forms in the matching continuous domain;
5. the full-complex weak Green identity converges when the boundary functional is included;
6. the computed cohomology agrees with the topology and the selected relative/absolute boundary problem.

No universal rate is predeclared. Rates must be measured across at least three refinement levels and checked against quadrature refinement.

## 8. Scientific status

**Established analytically:** the matrix `M^{-1}D^T M` is the adjoint of the chosen finite-dimensional differential on the chosen finite-dimensional spaces. The continuous Green identity contains a boundary functional, so the continuous adjoint depends on the operator domain.

**Observed numerically:** the unconstrained benchmark exhibits a boundary-localized residual for forms with nonzero boundary flux; compactly supported forms and fixed-core residuals behave better under refinement.

**Not yet established:** convergence of either a correctly constrained relative/absolute discrete codifferential or the full weak Green identity with its boundary trace pairing. This note specifies the comparison needed to settle that question without conflating boundary conditions.
