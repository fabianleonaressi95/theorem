# Morandotti reconstruction gate: from cell fields to the Airy potential

**Status:** algebraic postprocessing implemented and unit-tested in this branch; no new DOLFINx run or end-to-end physical benchmark is claimed.

## Exact target from Theorem 2.2

For \(N\) distinct defect cores, the published cell-field order is
\[
\kappa=(\kappa_0^1,\kappa_1^1,\kappa_2^1,\ldots,
        \kappa_0^N,\kappa_1^N,\kappa_2^N).
\]
The defect-data vector is
\[
\Phi=(s^1,\ s^1\xi_1^1+b_2^1,\ s^1\xi_2^1-b_1^1,\ldots,
s^N,\ s^N\xi_1^N+b_2^N,\ s^N\xi_2^N-b_1^N).
\]
The finite-dimensional coefficients solve
\[
\mathcal M a=\Phi,
\]
and the Airy potential is reconstructed as
\[
\boxed{v_h(x)=-\frac{E}{1-\nu^2}
       \sum_{i=1}^{3N}a_i\kappa_i^h(x).}
\]
This is the explicit geometry/data separation: the \(3N\) cell fields and interaction matrix depend on the fixed perforated geometry; Burgers vectors and Frank angles enter later through \(\Phi\).

Primary reference: Cesana, Fabbrini, León Baldelli and Morandotti, *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, Theorem 2.2, equations (2.17)–(2.18), arXiv:2609.29614.

## Implementation added here

- models/morandotti_cell_reconstruction.py: builds \(\Phi\), solves \(\mathcal M a=\Phi\), and reconstructs \(v_h\).
- tests/test_morandotti_cell_reconstruction.py: checks the signs/order of \(\Phi\), the linear solve, the reconstruction factor, superposition, and rejection of invalid matrices.

The interaction matrix passed to the postprocessor is the **Laplacian-product matrix**
\[
\mathcal M_{ij}=\int_{\Omega_\varepsilon}
       \Delta\kappa_i\,\Delta\kappa_j\,dx,
\]
which is what the authors' public postprocessing code assembles. The two-core audit also records the Hessian-product matrix
\(\int D^2\kappa_i:D^2\kappa_j\) and the boundary-plus-interior flux identity. Their continuum equality under the cell boundary conditions does not license silently replacing one discrete matrix by the other at finite mesh size. For reproducing the published reconstruction, use the Laplacian-product matrix and report the Hessian/Laplacian discrepancy separately.

## Two-core regression target

For the current two-core geometry
\[
\xi^1=(-0.28,0),\qquad \xi^2=(0.28,0),
\]
a mixed input can be represented by a wedge disclination at core 1 and an edge dislocation at core 2:
\[
s^1=0.2,\quad b^1=(0,0),\qquad
s^2=0,\quad b^2=(0.03,-0.04).
\]
This gives
\[
\Phi=(0.2,-0.056,0,\ 0,-0.04,-0.03).
\]
The signs follow the convention \(\Pi b=(b_2,-b_1)\) in the theorem.

## Remaining numerical acceptance gates

1. Feed the actual \(6\times6\) Laplacian matrix from scripts/rgs_morandotti_two_core_c0_ipdg.py and the six computed cell fields into this postprocessor.
2. Reconstruct the Airy potential for at least: one disclination, one edge dislocation, one opposite-sign disclination dipole, and one mixed disclination–dislocation configuration.
3. Check \(\mathcal M a-\Phi\), matrix symmetry/positive definiteness, and sensitivity to mesh refinement.
4. Reconstruct \(\sigma_h=\operatorname{cof}(D^2v_h)\) and check the traction residual \(\|\sigma_h n\|\) on the outer boundary and every core. For P3 C0-IPDG, evaluate elementwise Hessians and account for the facet traces; do not report only active-core value/normal-derivative residuals.
5. Compare stress and energy with an independent analytic case. The existing manufactured two-core test is an operator patch test; it is not yet an independent analytic defect solution.
6. Only after these checks, compare the reconstructed solution with Q1/P1/Airy references on identical geometry, material parameters, core radius, and boundary conditions.

## Scope boundary

The algebraic reconstruction functions are a direct implementation of the published finite-dimensional formula. They do not prove convergence of the C0-IPDG approximation, reproduce arbitrary \(N\), establish the singular-core limit, or validate a material model. The curved-shell and Q6/PRISM transfer questions remain separate.
