# Morandotti benchmark I — discrete Saint-Venant operator and variational closure

**Status:** research specification derived from the existing weak-operator prototype. This is not a convergence theorem, a completed Airy/CIP-DG comparison, or a validated material model.

**Purpose:** close the next mathematical gap between the existing weak assembly of the planar incompatibility operator and a solvable finite-dimensional variational problem.

Related records:
- `OPERATORE_INCOMPATIBILITA_TANGENTI_QUATERNIONI_MORANDOTTI.md`
- `APPENDICE_TECNICA_MORANDOTTI_RGS_PRISM.md`
- `models/discrete_incompatibility_weak.py`
- `tests/test_discrete_incompatibility_weak.py`

## 1. Fixed planar reference problem

Let \(\Omega\subset\mathbb R^2\) be a bounded polygonal domain. For a symmetric strain field
\[
\epsilon=\begin{pmatrix}\epsilon_{11}&\epsilon_{12}\\
\epsilon_{12}&\epsilon_{22}\end{pmatrix},
\]
use the convention
\[
\operatorname{inc}\epsilon
=\partial_{22}\epsilon_{11}
+\partial_{11}\epsilon_{22}
-2\partial_{12}\epsilon_{12}.
\]
For every sufficiently regular displacement \(u\),
\[
\operatorname{inc}(\operatorname{sym}\nabla u)=0
\]
in the distributional sense. This is the compatibility regression that must pass before defect loads are introduced.

For a test function \(\varphi\in H^2_0(\Omega)\), the weak pairing is
\[
\langle\operatorname{inc}\epsilon,\varphi\rangle
=\int_\Omega\epsilon:\operatorname{cof}(D^2\varphi)\,dx.
\]
The current prototype assembles this pairing on a cellwise strain basis and an \(H^2\)-conforming test basis.

## 2. Discrete constrained minimization

Choose:
- a finite-dimensional symmetric-strain space \(E_h=\operatorname{span}\{\psi_a\}_{a=1}^{n_e}\);
- a finite-dimensional scalar test space \(V_h=\operatorname{span}\{\varphi_i\}_{i=1}^{n_v}\subset H^2_0(\Omega)\);
- a positive-definite compliance tensor \(\mathbb S=\mathbb C^{-1}\), with the plane-stress or plane-strain convention stated explicitly.

Write \(\epsilon_h=\sum_a e_a\psi_a\). Define
\[
A_{ia}=\sum_{K\in\mathcal T_h}\int_K
\psi_a:\operatorname{cof}(D^2\varphi_i)\,dx,
\qquad
(M_{\mathbb S})_{ab}
=\int_\Omega\psi_a:\mathbb S:\psi_b\,dx.
\]
For a prescribed discrete defect source \(z\in\mathbb R^{n_v}\), the first RGS-compatible variational problem is
\[
\boxed{\quad
\min_{e\in\mathbb R^{n_e}}
\frac12 e^T M_{\mathbb S}e
\quad\text{subject to}\quad Ae=z.
\quad}
\]
Its KKT system is
\[
\boxed{
\begin{pmatrix}
M_{\mathbb S}&A^T\\
A&0
\end{pmatrix}
\begin{pmatrix}e\\\lambda\end{pmatrix}
=
\begin{pmatrix}0\\z\end{pmatrix}.}
\]
Here \(\lambda\) is the discrete Airy-type multiplier. It must not be identified with the continuum Airy potential until the sign, normalization, constitutive convention and boundary conditions have been matched.

If \(M_{\mathbb S}\) is positive definite and \(A\) has full row rank, the KKT matrix is nonsingular. More generally, feasibility requires \(z\in\operatorname{Ran}A\); redundant test constraints must be removed or handled on the quotient/range. The reduced dual operator is
\[
L_h=A M_{\mathbb S}^{-1}A^T,
\]
and, when the stated rank conditions hold,
\[
L_h\lambda=z,\qquad
e=M_{\mathbb S}^{-1}A^T\lambda.
\]
This is the finite-dimensional fourth-order operator to compare with the biharmonic Airy equation. It is a derived Schur complement of the chosen discrete energy and incompatibility constraint, not an assumed Laplacian stencil.

## 3. Defect loads and sign convention

For a dislocation at \(x_j\) with nonzero Burgers vector \(b^j=(b_1^j,b_2^j)\), set
\[
n_j=\frac{(b^j)^\perp}{|b^j|}
=\frac{(-b_2^j,b_1^j)}{|b^j|}.
\]
For a disclination at \(y_k\) with Frank parameter \(s^k\), use the source convention
\[
\zeta=
\sum_j |b^j|\,\partial_{n_j}\delta_{x_j}
-\sum_k s^k\delta_{y_k}.
\]
Since \(\langle\partial_n\delta_x,\varphi\rangle=-\partial_n\varphi(x)\), the load entries are
\[
z_i=
-\sum_j |b^j|\,\nabla\varphi_i(x_j)\cdot n_j
-\sum_k s^k\varphi_i(y_k).
\]
Equivalently, the dislocation contribution for one \(b=(b_1,b_2)\) is
\[
b_2\,\partial_1\varphi_i(x)-b_1\,\partial_2\varphi_i(x).
\]
This is exactly the sign convention implemented by `assemble_burgers_frank_load`; it must be retained in analytic and regression tests.

For a finite core, replace each point distribution by a specified mollifier \(\rho_\varepsilon\), normalized by \(\int\rho_\varepsilon=1\):
\[
z_i^\varepsilon=
-\sum_j |b^j|\int_\Omega
\rho_\varepsilon(x-x_j)\,\nabla\varphi_i(x)\cdot n_j\,dx
-\sum_k s^k\int_\Omega
\rho_\varepsilon(x-y_k)\,\varphi_i(x)\,dx.
\]
The mollifier profile, support, normalization and boundary truncation are part of the model definition. They cannot be hidden inside a quadrature choice.

## 4. Required verification gates

### Gate 1 — operator and compatibility

1. Reproduce the existing test that the weak operator annihilates a globally continuous P1 displacement's piecewise symmetric gradient.
2. Add polynomial patch tests for affine and quadratic displacements on a multi-triangle mesh.
3. Check invariance under a rigid displacement and under a change of element numbering/orientation.
4. Compare assembled entries against direct high-order quadrature of the defining integral.
5. Report the residual separately from quadrature error.

The identity \(\operatorname{inc}(\operatorname{sym}\nabla u)=0\) is exact in the continuum. A finite test only verifies the selected discrete spaces, assembly and quadrature.

### Gate 2 — constitutive energy and KKT system

1. Assemble \(M_{\mathbb S}\) from one explicitly declared plane-stress or plane-strain tensor.
2. Check symmetry and positive definiteness on the chosen strain space.
3. Check the KKT residual and constraint residual \(\|Ae-z\|\).
4. Check feasibility of each source vector before solving.
5. Compare the primal energy \(\tfrac12e^TM_{\mathbb S}e\) with the dual value \(-\tfrac12 z^T\lambda\), using the same sign convention.
6. Record condition numbers, solver tolerances, rank decisions and mesh/core parameters.

The dual-energy identity follows from the KKT equations when the constraint is feasible and the stated rank assumptions hold. It is a useful independent implementation check.

### Gate 3 — analytic defect benchmarks

Use three separate configurations:
- **D1:** one edge dislocation, \(s=0\), with prescribed Burgers vector;
- **D2:** one wedge disclination, \(b=0\), with prescribed Frank parameter;
- **D3:** a disclination dipole with separation \(d_\varepsilon\) and fixed dipole strength, compared with the corresponding edge-dislocation source.

For D3, the limiting statement must be matched to the renormalized energies and core conventions in the reference model. Do not assert
\(\lim_{\varepsilon\to0}E_\varepsilon^{\rm dipole}=E^{\rm dislocation}\)
without reproducing the precise normalization and any subtracted core terms of that theorem.

### Gate 4 — mesh/core separation

For each fixed \(\varepsilon>0\), refine the mesh until the discretization error is separated from the core regularization error. Then vary \(\varepsilon\) in a second sequence. At minimum report:
- \(h\), \(\varepsilon\), and \(h/\varepsilon\);
- primal and dual energies;
- \(L^2\)-stress error against the reference solution where available;
- constraint and equilibrium residuals;
- matrix condition number, runtime and memory.

A diagonal sequence with \(h\) and \(\varepsilon\) changing simultaneously is not sufficient to identify which error is converging.

### Gate 5 — comparison with Airy/CIP-DG

The comparison must use identical:
- domain and boundary conditions;
- elastic constants and plane-stress/plane-strain convention;
- defect positions, Burgers/Frank data and core regularization;
- quadrature accuracy and stopping tolerances.

Compare the Airy potential (after fixing its gauge), stress, energy, residuals, conditioning and computational cost. The 2026 CIP-DG formulation is an existing finite-element baseline; the RGS construction is an alternative geometric/variational encoding to test, not a claim to be the first FEM treatment.

## 5. Cartan–quaternionic extension: keep it as a separate gate

The planar source problem above can be solved without introducing a quaternionic connection. The geometric extension is a distinct calibration task.

On oriented dual links introduce independent \(U_{fg}\in SU(2)\), with \(U_{gf}=U_{fg}^{-1}\), and gauge transformation
\[
U_{fg}\mapsto g_f^{-1}U_{fg}g_g.
\]
For a dual plaquette \(p\), its ordered holonomy \(H_p\) transforms by conjugation. With the fundamental SU(2) trace convention, the principal SO(3) rotation angle is
\[
\theta_p=2\arccos\!\left(\frac{|\operatorname{tr}H_p|}{2}\right)
\in[0,\pi].
\]
The absolute value accounts for the double cover \(SU(2)\to SO(3)\); the rotation axis is obtained from the traceless part after fixing a local branch. This gives a candidate Frank observable, not yet the Airy source.

A translational defect requires a discrete coframe \(\vartheta_e\). Its transported closure around a dual plaquette is a candidate Burgers vector:
\[
B_p=\sum_{e\subset\partial p}
\mathcal P_{e\to f_0}\,\vartheta_e.
\]
The coframe, reference/deformed split, link orientations and transport paths must be specified. Frame-derived links \(q_f^{-1}q_g\) alone are pure gauge and have trivial closed holonomy; they cannot supply independent disclination curvature.

The remaining calibration is a dimensionally consistent map
\[
\mathcal S_h:(B_p,\theta_p,\text{axis}_p,\text{cell geometry})
\longrightarrow z_h,
\]
tested first on D1 and D2. Burgers has dimensions of length and Frank is dimensionless, whereas \(z_h\) inherits the dimensions of the chosen Airy/elasticity convention. No direct sum \(B_p+\Omega_p\) is meaningful without a derived dimensional conversion.

## 6. What this closes — and what remains open

This specification closes the algebraic formulation of the finite-dimensional constrained energy problem associated with the existing weak matrix \(A_h\), and gives a concrete verification sequence. It does **not** close:
- implementation of \(M_{\mathbb S}\), KKT solve and Airy comparison;
- convergence/stability of the chosen discrete spaces;
- the singular dipole-to-dislocation energy limit for the chosen discrete core;
- the curved-surface incompatibility operator;
- calibration from Cartan torsion/curvature to the planar Airy source;
- validation on additive-manufacturing data or any industrial material.

The next implementation should therefore be a small planar KKT solver with one declared constitutive convention and D1–D3 regression cases. Only after that solver agrees with the Airy/CIP-DG reference should the independent SU(2)-coframe calibration be coupled to it.

**Classification:** derived finite-dimensional formulation / implementation specification; numerical validation pending; continuum convergence open; physical validation absent.

**FLN**
