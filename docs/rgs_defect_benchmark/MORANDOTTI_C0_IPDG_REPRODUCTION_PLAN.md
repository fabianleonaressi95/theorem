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


## 14. DOLFINx 0.11 runtime compatibility audit

The first executions reached the variational-form JIT and exposed a further issue: FFCx 2026.1.0 does not lower UFL `CellDiameter` for the curved P3 geometry element (warning: only P1/Q1 cell diameter is supported; fatal `Not handled: ufl.geometry.CellDiameter`). The driver now stores the actual mesh cell-size values returned by `mesh.h(tdim, cells)` in a DG0 coefficient and uses that coefficient in the interior and boundary penalty terms. This preserves cellwise (h_T) scaling rather than substituting one global target mesh size.

The other runtime fixes already applied are the DOLFINx 0.11 Gmsh import (`dolfinx.io.gmsh`) and the explicit function-space argument for the active-core Dirichlet condition. These were discovered from actual container traces, not guessed. The DG0 implementation is committed; its DOLFINx workflow is pending. No P3 numerical output is accepted until the form compiles, all three cell solves complete, and the report artifact is uploaded.


## 15. First successful P3 C0-IPDG execution — single-core annulus

The first DOLFINx 0.11.0 run completed successfully:
- Workflow: [run 42661115929](https://github.com/fabianleonaressi95/theorem/actions/runs/42661115929)
- Artifact: [morandotti-p3-c0-ipdg-report, ID 13693913162](https://github.com/fabianleonaressi95/theorem/actions/runs/42661115929/artifacts/13693913162)
- Mesh targets: (h=0.22,0.14,0.09); polynomial degree (P_3); (alpha=10); one concentric core (a=0.2), outer radius (R=1); serial MPI.
- All three cell problems (kappa_0,kappa_1,kappa_2) were assembled and solved at each level.

| target h | cells | relative H2 error (kappa_0) | (kappa_1) | (kappa_2) | relative (M_H-M_Delta) |
|---:|---:|---:|---:|---:|---:|
| 0.22 | 196 | 17.74% | 22.66% | 22.13% | 0.1142% |
| 0.14 | 400 | 12.74% | 16.22% | 16.43% | 0.1314% |
| 0.09 | 920 | 6.70% | 8.12% | 9.29% | 0.1584% |
| 0.06 | 2030 | 3.46% | 4.47% | 4.60% | 0.0881% |

The core value traces are enforced to residuals (<1.4	imes10^{-16}). The core normal-derivative residuals decrease with refinement:
- (kappa_0): 0.2465, 0.1574, 0.0670;
- (kappa_1): 0.1352, 0.0867, 0.0352;
- (kappa_2): 0.1335, 0.0889, 0.0411.

Both interaction matrices are symmetric to assembly precision and positive definite at all three levels. Their condition numbers are approximately 5.3–5.4.

**Important unresolved signal:** the relative Hessian/Laplacian matrix discrepancy is small (0.11–0.16%) but is not monotone decreasing on these three meshes. The cell-field (H^2) errors and boundary normal residuals decrease, but the matrix identity has not yet passed a convergence gate. A finer (h=0.06) level has been added to the dedicated workflow to determine whether this is pre-asymptotic geometry/quadrature behavior or a formulation/assembly issue. Until that result is checked, do not claim convergence of (M_H-M_Delta).

This is the first actual execution of the single-core P3 C0-IPDG port, not yet the full multi-core reconstruction algorithm of the paper. The multi-core matrix (mathcal M), reconstruction for arbitrary defect data, off-centre cores and singular-core limit remain open.


### 15.1 Finer P3 level h=0.06

The finer run is [CI 42661368865](https://github.com/fabianleonaressi95/theorem/actions/runs/42661368865), success, with artifact [13695060857](https://github.com/fabianleonaressi95/theorem/actions/runs/42661368865/artifacts/13695060857). It contains 2,030 cells. The relative Hessian/Laplacian matrix discrepancy drops to (8.8091\times10^{-4}) (0.0881%), while the relative H2 errors fall to 3.46%, 4.47% and 4.60% for (kappa_0,kappa_1,kappa_2). Core normal-derivative residuals are 0.0281, 0.0158 and 0.0163.

The trend is now consistent with convergence after the pre-asymptotic coarse levels, but it is not sufficient to assert an asymptotic order. The next check is a finer (h) level plus the boundary identity residual computed from the discrete fields.


### 15.2 Discrete Hessian–Laplacian identity including interior facets

The P3 driver now assembles the full flux decomposition
[
M_\Delta-M_H=B_{\partial\Omega_\varepsilon}+B_{\mathcal F_h^i},
]
where the first term is the physical-boundary flux and the second is the sum of the two-sided fluxes across all interior facets. The interior contribution is essential because the C0-IPDG fields are continuous but their gradients/Hessians are not globally smooth; using only the outer/core boundary flux leaves the interior jumps unaccounted for.

The refined CI [42662098640](https://github.com/fabianleonaressi95/theorem/actions/runs/42662098640) passed and uploaded artifact [13693953816](https://github.com/fabianleonaressi95/theorem/actions/runs/42662098640/artifacts/13693953816). Relative Frobenius residuals for the full identity are:
- (h=0.22): (4.69\times10^{-7});
- (h=0.14): (6.00\times10^{-8});
- (h=0.09): (2.91\times10^{-9});
- (h=0.06): (2.55\times10^{-10}).

The total-flux matrix symmetry residual decreases from (2.26\times10^{-5}) to (2.04\times10^{-8}). The physical-boundary flux matrix alone is not symmetric; the interior-facet contribution is required for the full discrete identity.

**Conclusion:** the observed (M_H) versus (M_\Delta) discrepancy is accounted for by the discrete boundary-plus-interior flux identity to high accuracy, with residual decreasing by roughly three orders of magnitude across the four levels. This validates the matrix assembly identity for the computed P3 cell fields. It does not yet establish the full multi-core reconstruction or the singular-core limit.

## 16. Second reproduction gate: two-core interaction matrix

The single-core gate is now followed by a controlled two-core problem. The new driver `scripts/rgs_morandotti_two_core_c0_ipdg.py` builds an outer disk with two equal, separated circular cores and solves the six P3 cell problems
\[
\kappa_{i,0},\;\kappa_{i,1},\;\kappa_{i,2},\qquad i=1,2.
\]
For each field, affine value data are imposed on its active core and zero values on the other core and outer boundary; the active-core normal derivative data are (0,n_1,n_2). The code assembles the full 6×6 Hessian and Laplacian interaction matrices from the same six discrete fields, together with physical-boundary and interior-facet flux matrices.

The acceptance checks are:
1. all six linear systems solve at each of three mesh sizes;
2. the two core boundary tags are geometrically distinct and correctly classified;
3. value and active normal-derivative residuals are finite and reported separately by core/mode;
4. both interaction matrices are symmetric to assembly tolerance and have positive minimum eigenvalue;
5. the full flux identity \(M_\Delta-M_H=B_{\partial\Omega}+B_{\mathcal F_h^i}\) closes to a refinement-stable residual;
6. conditioning and all matrix entries are retained in the JSON artifact.

Dedicated workflow: `.github/workflows/morandotti-two-core-c0-ipdg.yml`, using the same pinned DOLFINx 0.11.0 container. Initial execution is [run 42667732997](https://github.com/fabianleonaressi95/theorem/actions/runs/42667732997) and is queued; no two-core numerical result is claimed yet.

**Scope:** this is the first non-concentric two-core interaction-matrix test (two cores centred at (-0.28,0) and (0.28,0), radius 0.12, outer radius 1). It is still a controlled finite-core test, not the arbitrary-N reconstruction algorithm, singular-core limit, dynamics, or material validation. There is no analytic off-centre exact field, so this gate tests algebraic, boundary, spectral and flux identities rather than claiming an H² convergence rate against a closed-form solution.
