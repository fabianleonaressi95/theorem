# Direct comparison target: Morandotti-group C0-IPDG Airy solver

**Purpose.** Specify the next reproducible benchmark against Cesana, Fabbrini, León Baldelli and Morandotti, *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation* (arXiv:2609.29614, 2026). This note is a specification, not a claim that the published solver has already been reproduced.

Reference:
- Preprint: https://arxiv.org/abs/2609.29614
- CVGMT record: https://cvgmt.sns.it/paper/7600/
- Published earlier variational theory: Cesana, De Luca, Morandotti (2024), DOI 10.1137/22M1523443.

## 1. Mathematical target

For plane-strain isotropic elasticity, the incompatible strain satisfies

\[
\operatorname{inc}\epsilon
=\sum_{j=1}^{J}|b^j|\,\partial_{(b^j)^\perp/|b^j|}\delta_{x^j}
-\sum_{k=1}^{K}s^k\delta_{y^k}
=:\zeta.
\]

With the Airy potential, \(\sigma=\operatorname{cof}(\nabla^2v)\), and

\[
\frac{1-\nu^2}{E}\Delta^2v=\zeta.
\]

The regularized geometry is \(\Omega_\varepsilon=\Omega\setminus\cup_i\overline{B_\varepsilon(\xi^i)}\), with disjoint cores. The variational functional is the Hessian energy

\[
\mathcal G(v)=\frac{1+\nu}{2E}
\int_{\Omega_\varepsilon}
\left(|\nabla^2v|^2-\nu(\Delta v)^2\right)\,dx
\]

plus the core boundary terms encoding Frank angles and Burgers vectors. The admissible Airy potential is affine in each core and satisfies the outer clamped gauge; the induced mechanical boundary condition is traction-free.

## 2. Published numerical architecture to reproduce

The 2026 paper does not merely solve one fourth-order PDE per defect configuration. For a fixed domain, mesh, core locations and core radius, it computes **3N cell problems**:

- \(\kappa_0^i\): active core boundary value 1, normal derivative 0;
- \(\kappa_1^i\): active core boundary value \(x_1\), normal derivative \(n_1\);
- \(\kappa_2^i\): active core boundary value \(x_2\), normal derivative \(n_2\).

All other cores and the outer boundary carry homogeneous conditions. These basis fields are then combined through the finite-dimensional matrix \(\mathcal M\) and defect-data vector \(\Phi\) in Theorem 2.2 to reconstruct the Airy potential for arbitrary Burgers vectors and Frank angles at the fixed core geometry. This geometry/defect-data separation is the key algorithmic feature to reproduce.

Discretization details stated in Section 3:
- triangulation of the perforated domain;
- globally continuous piecewise-cubic \(P_3\) scalar functions;
- \(C^0\) interior-penalty DG formulation for the fourth-order biharmonic cell problems;
- facet jump/average terms for normal-gradient jumps and Hessian traces;
- penalty parameter \(\alpha=10\) in the reported experiments;
- DOLFINx/FEniCSx and PETSc in the published implementation.

## 3. What the current RGS benchmark does — and does not do

Current PR #119 has:
- displacement Q1 quadrilateral elasticity;
- displacement P1 edge-cochain elasticity with exact incidence maps;
- an independent finite-difference clamped-biharmonic Airy reference;
- smooth finite-core eigenstrain/cut sources;
- a regularized fixed-grid dipole-to-edge source/stress comparison.

It **does not** yet implement:
- a perforated \(\Omega_\varepsilon\) with explicit circular cores;
- the three \(P_3\) Airy cell problems per core;
- the published \(C^0\)-IPDG facet bilinear form and penalty terms;
- the matrix \(\mathcal M\) and reconstruction formula;
- a like-for-like comparison using the same core geometry, source moments, boundary conditions and constitutive parameters.

Therefore the existing finite-difference Airy reference must not be described as the Morandotti-group solver.

## 4. Implementation sequence and acceptance tests

1. **Single circular core, one defect.** Reproduce the three radial cell solutions \(\kappa_0,\kappa_1,\kappa_2\) on the unit disk minus a radius-\(\varepsilon\) disk, and compare the computed fields and Hessian energy against the paper's analytical expressions.
2. **One off-centre core.** Validate the reconstructed Airy field and verify zero normal traction on both the external boundary and the core boundary.
3. **Two opposite wedge disclinations.** Sweep separation at fixed \(\varepsilon\); compare stress, energy, Frank moments and annihilation/near-collision behavior with the paper's exact/analytical references where available.
4. **One edge dislocation.** Compare Burgers moment, Airy stress and energy against the analytical benchmark.
5. **Mixed disclination–dislocation configuration.** Only after the single-defect tests pass, compare interactions and superposition.
6. **Cross-solver comparison.** On matched geometry and parameters, compare C0-IPDG Airy, current finite-difference Airy, Q1 displacement FEM and P1 cochain fields. Report relative \(L^2\) stress/strain errors, energy differences, core moment errors, traction residuals, weak residuals and convergence rates.

Acceptance requires:
- exact source moments (within quadrature error);
- convergence of each of the three cell problems in the \(H^2\)-energy norm;
- traction-free residuals on all physical boundaries;
- agreement with radial analytical solutions under mesh refinement;
- reproducible mesh/core/penalty/material metadata;
- no claim of physical Q6/PRISM realization until an explicit chain map to the perforated physical mesh is supplied.

## 5. RGS extension — kept separate from reproduction

Only after the published benchmark is independently reproduced should RGS be tested as a new discretization. The candidate research question is whether the Q6/PRISM cochain complex can supply a structure-preserving discrete kinematic map and defect-source representation that couples to the Airy energy without checkerboard/hourglass modes. This is an extension to be tested against the established C0-IPDG reference, not an interpretation of the paper's method.

## 6. CI evidence already available

The latest PR #119 regression, [run #69](https://github.com/fabianleonaressi95/theorem/actions/runs/42657016309), completed successfully. It ran the defect benchmark, Q1/P1 comparison, nine Airy tests, seven Q6 quotient tests and uploaded the numerical artifact. The non-grid-locked fixed-grid dipole sweep at \(n=129\), \(h=1/128\) reduced incompatibility relative \(L^2\) error from 70.12% to 4.74% and Airy-stress relative \(L^2\) error from 23.76% to 1.26% as separation decreased from 0.1 to 0.025. This remains a regularized fixed-grid trend, not a continuum-limit proof.

The wedge-dipole energy discrepancy at \(n=129\) remains material: Q1/cochain 12.12%, Q1/Airy 7.28%, cochain/Airy 18.52%. This is an explicit blocker to claiming energetic validation.

## 7. Public implementation source inspected

The paper links a public implementation: [EdoardoF1993/planar_elasticity_dislocations_disclinations](https://github.com/EdoardoF1993/planar_elasticity_dislocations_disclinations). The following source files have been inspected directly:

- [`scripts/models/__init__.py`](https://github.com/EdoardoF1993/planar_elasticity_dislocations_disclinations/blob/main/scripts/models/__init__.py): `Biharmonic` assembles the cell-problem volume term as \(\int D^2u:D^2v\), symmetric facet consistency terms involving jumps of normal gradients and averages of normal-normal Hessians, and interior/boundary penalty terms proportional to \(\alpha/h\). It uses the parameter `alpha_penalty`.
- [`scripts/cellFormulas.py`](https://github.com/EdoardoF1993/planar_elasticity_dislocations_disclinations/blob/main/scripts/cellFormulas.py): constructs the perforated Gmsh mesh, identifies outer and core boundary DOFs, and solves the three cell problems for each core.
- [`scripts/airy.py`](https://github.com/EdoardoF1993/planar_elasticity_dislocations_disclinations/blob/main/scripts/airy.py): loads the 3N cell fields, assembles the interaction matrix using \(\int \Delta\kappa_i\,\Delta\kappa_j\), solves \(M a=\Phi\), and reconstructs \(v=-E/(1-\nu^2)\sum_i a_i\kappa_i\).
- [`scripts/meshes/primitives.py`](https://github.com/EdoardoF1993/planar_elasticity_dislocations_disclinations/blob/main/scripts/meshes/primitives.py): creates circular domains with circular cores through the Gmsh Python API.

### 7.1 Hessian-product versus Laplacian-product matrix: identity resolved

The source difference is real but is **not, by itself, evidence of a coding inconsistency**. The cell solver assembles the Hessian product, while the Airy postprocessor assembles the Laplacian product for the interaction matrix. For sufficiently regular cell fields \(u,v\), in two dimensions,

\[
\operatorname{div}\!\left((\operatorname{cof}D^2u)\nabla v\right)
=(\operatorname{cof}D^2u):D^2v
=\Delta u\,\Delta v-D^2u:D^2v,
\]

because \(\operatorname{div}(\operatorname{cof}D^2u)=0\). Therefore

\[
\int_{\Omega_\varepsilon}
\left(\Delta u\,\Delta v-D^2u:D^2v\right)dx
=\int_{\partial\Omega_\varepsilon}
(\operatorname{cof}D^2u\,n)\cdot\nabla v\,ds.
\]

On every boundary component, each cell field has affine Dirichlet trace and the matching normal derivative (the active core has data 1/0, \(x_1/n_1\), or \(x_2/n_2\); inactive cores and the outer boundary have zero data). These imply \(D^2u\,t=0\) on that component. In the orthonormal \((n,t)\) frame, this means \(D^2u=\operatorname{diag}(a,0)\), hence \((\operatorname{cof}D^2u)n=0\). The boundary integral vanishes, giving

\[
\boxed{\int_{\Omega_\varepsilon}D^2u:D^2v\,dx
=\int_{\Omega_\varepsilon}\Delta u\,\Delta v\,dx.}
\]

Thus the two continuum bilinear forms coincide on the cell-function space under the stated affine boundary traces. This is the mathematical reason the postprocessor's Laplacian-product matrix can agree with the Hessian-product cell energy.

**Discrete verification still required:** the finite-element cell fields satisfy the affine traces and normal derivatives only to the accuracy of the discrete boundary enforcement and approximation. The implementation audit must therefore report, for every mesh level, (i) the relative matrix difference \(\|M_{\Delta}-M_{H}\|_F/\|M_H\|_F\), (ii) symmetry residuals, (iii) smallest eigenvalue / conditioning, and (iv) the boundary identity residual. This is a convergence check, not a reason to alter the published implementation.

## 8. Reproduction status

**Source-level audit completed; numerical reproduction not yet run.** The exact operator, facet terms, boundary data, matrix postprocessing and reconstruction are now mapped to public source. The next executable task is a matched-mesh implementation of the published C0-IPDG cell problems, followed by the four matrix/energy checks in §7.1 and the radial benchmarks in §4. The published solver depends on DOLFINx/FEniCSx, Gmsh, PETSc/MUMPS and ADIOS4Dolfinx; no claim is made that these dependencies or the original run have been executed in the present environment.


## 9. P2 discrete matrix-identity patch test

A separate executable patch test has now been added:
- `scripts/rgs_airy_cell_matrix_p2.py`
- `tests/test_rgs_airy_cell_matrix_p2.py`

It samples the three exact annular cell fields at the vertices and edge midpoints of a structured triangular annulus, reconstructs their local quadratic (P_2) interpolants, and assembles both elementwise matrices:
[
(M_H)_{ij}=\sum_T |T|\,D^2\kappa_i^h:D^2\kappa_j^h,
\qquad
(M_\Delta)_{ij}=\sum_T |T|\,\Delta\kappa_i^h\,\Delta\kappa_j^h.
]
The CI report records the full matrices, relative Frobenius discrepancy, symmetry residuals, smallest eigenvalues, and observed refinement rates on four mesh levels.

**Interpretation limit:** this is a (P_2) interpolation patch test on a polygonal annulus, not a variationally constrained (P_2) solve and not the paper's (P_3) C0-IPDG implementation. It tests whether the matrix identity is recovered under polynomial interpolation/refinement; it does not establish equivalence of the published discrete bilinear forms. The actual C0-IPDG reproduction remains a separate task.


## 10. P2 annular matrix-identity results — CI run #97

The corrected full regression completed successfully:
- Workflow run: https://github.com/fabianleonaressi95/theorem/actions/runs/42659504594
- Run number: 97
- Tested commit: `98e2b3949d52f18290e65ddaaf4e7b5daf298356`
- All workflow steps passed, including the P2 matrix audit and the periodic Q6/FEM/Airy comparison.
- Artifact: `rgs-cochain-defect-report`, artifact ID `13693762589`.

The P2 annular interpolation audit produced the following relative Frobenius discrepancies:
| radial × angular cells | triangles | \\(\\|M_H-M_\\Delta\\|_F/\\|M_H\\|_F\\) |
|---:|---:|---:|
| 4 × 16 | 128 | 5.5539998 × 10⁻² |
| 8 × 32 | 512 | 1.3881021 × 10⁻² |
| 16 × 64 | 2,048 | 3.4584608 × 10⁻³ |
| 32 × 128 | 8,192 | 8.6316931 × 10⁻⁴ |

Observed halving rates: 2.0004, 2.0049, 2.0024. Both matrices are symmetric to assembly precision and have positive smallest eigenvalues in all reported cases.

**Interpretation:** the discrete matrix discrepancy decreases by approximately a factor of four per mesh halving in this (P_2) interpolation experiment. This is evidence that the continuum identity is recovered under this particular interpolation/refinement procedure. It is not evidence that the published P3 C0-IPDG bilinear form has been independently reproduced, nor does it prove a general convergence rate for the method. The nonzero coarse-grid discrepancy is important and is retained rather than hidden.

## 11. Exact published C0-IPDG operator to be ported

The source-level formula in `scripts/models/__init__.py` is now transcribed explicitly. With (H(u)=D^2u), (h) the cell diameter, (n) the facet normal, and (alpha=10), the symmetric form is

[
\begin{aligned}
a_h(u,v)={}&\sum_{T}\int_T H(u):H(v)\,dx\\
&-\sum_{F\in\mathcal F_h^i}\int_F
\left(\llbracket\nabla u\rrbracket_n\,\{H(v)_{nn}\}
+\llbracket\nabla v\rrbracket_n\,\{H(u)_{nn}\}\right)ds\\
&-\sum_{F\in\mathcal F_h^b}\int_F
\left(\partial_nu\,H(v)_{nn}
+\partial_nv\,H(u)_{nn}\right)ds\\
&+\sum_{F\in\mathcal F_h^i}\int_F
\frac{\alpha}{\{h\}}\llbracket\nabla u\rrbracket_n
\llbracket\nabla v\rrbracket_n\,ds
+\sum_{F\in\mathcal F_h^b}\int_F
\frac{\alpha}{h}\partial_nu\,\partial_nv\,ds.
\end{aligned}
]

For the active core, the Nitsche load is
[
\ell_h(v)=-\int_{\Gamma_i}g_N H(v)_{nn}\,ds
+\int_{\Gamma_i}\frac{\alpha}{h}g_N\partial_nv\,ds,
]
with (g_N=0,n_1,n_2) for the (\kappa_0,\kappa_1,\kappa_2) problems, respectively. The value traces are imposed strongly; outer and inactive-core value and normal-derivative data are zero. This is the operator to match, not a generic biharmonic penalty form.

**Implementation caution:** the published script uses `jump(grad(u), n)` and `avg(dot(dot(hessian(v), n), n))`; the port must preserve UFL's scalar normal-jump convention and the same boundary-facet treatment. Any refactoring into alternative jump notation must be checked against the source expression and tested on a two-cell patch.

## 12. Next reproduction gate

The next deliverable is a DOLFINx/Gmsh/PETSc execution environment for the single-core annulus, polynomial degree 3, (alpha=10), followed by:
1. all three cell fields;
2. the full (3\times3) Hessian and Laplacian matrices assembled from the same discrete fields;
3. boundary normal-derivative residuals;
4. matrix symmetry, smallest eigenvalue and condition number;
5. mesh refinement and comparison against the radial continuum cell fields.

This gate is deliberately separate from the lightweight NumPy/SciPy CI. Until the DOLFINx environment executes the driver, the P3 C0-IPDG solver remains **specified from source but not independently reproduced**.


## 13. First executable P3 C0-IPDG driver added

A DOLFINx implementation has been added in `scripts/rgs_morandotti_c0_ipdg.py`. It is scoped to the first controlled reproduction gate: one concentric circular core in a circular outer domain, with three P3 cell problems and \\(\\alpha=10\\). The implementation transcribes the public source's Hessian volume term, symmetric interior and boundary consistency terms, normal-gradient penalties, strong value traces, and active-core normal-derivative load.

For each mesh size it is designed to report:
- relative (H^2)-seminorm error against the analytic annular cell fields;
- core value and normal-derivative residuals for all three cell problems;
- Hessian and Laplacian interaction matrices from the same discrete fields;
- symmetry, minimum eigenvalue and condition number.

A dedicated workflow, `.github/workflows/morandotti-c0-ipdg.yml`, uses the official DOLFINx v0.11.0 container image and installs the Gmsh Python bindings. The workflow is intentionally separate from the lightweight regression because DOLFINx/PETSc is a large native dependency stack. The official DOLFINx project documents the stable Docker image as its recommended route when PETSc is required. See https://github.com/FEniCS/dolfinx#installation.

**Execution status:** driver and dedicated workflow have been committed; the first container execution is pending. No numerical P3 result is claimed until that workflow finishes. If the container exposes API or mesh-generation incompatibilities, they must be fixed against the pinned DOLFINx 0.11.0 environment before the driver is accepted.
