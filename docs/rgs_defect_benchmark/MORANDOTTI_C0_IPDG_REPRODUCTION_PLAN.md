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
