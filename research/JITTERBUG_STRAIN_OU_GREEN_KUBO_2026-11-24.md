# Jitterbug strain energy, microscopic stress and finite OU Green–Kubo audit

**Date:** 2026-11-24  
**Classification:** [P] energy-to-stress/Hessian derivative identities under the declared central-force model; [N] finite 36-DOF matrix and OU calculations; [O] stationary dynamics on mechanisms, physical phonon/phason interpretation, material viscosity and continuum limit.

## 1. Model and scope

Use the existing cuboctahedral Jitterbug reference geometry: 12 joints, 24 unit rods, 8 triangular panels. The coordinates and edge list are imported from audits/jitterbug_gray_kinematics.py; no alternative embedding or spring constants are introduced. Every rod has unit rest length and unit spring constant.

For displacements u_i and symmetric affine strain epsilon, define one energy:
\[
H(u,\epsilon)=\frac12\sum_{(i,j)\in E_J}
\left(\left|(I+\epsilon)(x_j-x_i)+u_j-u_i\right|-1\right)^2.
\]
The reference state is stress-free. Strain coordinates are independent components xi_ij, with epsilon=sum xi_ij S^ij; for i<j, S^ij=(e_i e_j^T+e_j e_i^T)/2. The stress is not chosen separately:
\[
\Pi_{ij}(u)=-\left.\frac{\partial H(u,\epsilon(\xi))}
{\partial \xi_{ij}}\right|_{\xi=0}.
\]

## 2. Derived Hessian and stress coefficients

For each oriented rod let b_e be its incidence vector, n_e=(x_j-x_i) its unit direction, and ell_e=1. The rigidity matrix has row b_e^T tensor n_e^T. Thus
\[
K=R^TR,\qquad H(u,0)=\tfrac12u^TKu+O(\|u\|^3).
\]
For each of the six independent strain coordinates, put
\[
q_e^{ij}=n_e^TS^{ij}n_e,\qquad
m_e^{ij}=S^{ij}n_e-q_e^{ij}n_e.
\]
Differentiation of the same energy gives the linear stress coefficient and strain-Hessian derivative:
\[
c_{ij}=-\sum_e \ell_e q_e^{ij}(b_e\otimes n_e),
\]
\[
A^{ij}=\sum_e b_eb_e^T\otimes
\left[m_e^{ij}n_e^T+n_e(m_e^{ij})^T+
q_e^{ij}(I-n_en_e^T)\right].
\]
Consequently the stress through quadratic displacement order is
\[
\Pi_{ij}(u)=c_{ij}^Tu-\frac12u^TA^{ij}u+O(\|u\|^3).
\]
The linear term is retained; this is not the quadratic-only stress shortcut. The geometric-stiffness term in A is included.

## 3. Nullspace and the conditional OU process

The existing mechanical audit gives rank(K)=24, nullity(K)=12: six rigid-body modes and six internal infinitesimal mechanisms. The harmonic energy supplies no restoring force along any of these 12 directions.

For a finite stationary OU benchmark, restrict explicitly to
\[
\mathcal H=(\ker K)^\perp=\operatorname{Ran}K
\]
and define
\[
du_t=-\mu K_{\mathcal H}u_t\,dt+
\sqrt{2\mu k_BT}\,dW_t^{\mathcal H}.
\]
This is a conditional mathematical construction on the stiff subspace. It is not a claim that the six internal mechanisms are physically absent or thermally equilibrated. A physical model must constrain, stabilize, or dynamically describe them.

Let lambda_alpha>0 and A^ij_ab be matrix elements in an orthonormal eigenbasis of K_H. The integrated linear-stress covariance is
\[
\int_0^\infty C^{\rm lin}_{ij,kl}(t)\,dt
=\frac{k_BT}{\mu}\sum_\alpha
\frac{c^{ij}_\alpha c^{kl}_\alpha}{\lambda_\alpha^2}.
\]
For the centered quadratic stress, Gaussian Wick contraction gives
\[
\int_0^\infty C^{\rm quad}_{ij,kl}(t)\,dt
=\frac{(k_BT)^2}{2\mu}\sum_{\alpha,\beta}
\frac{A^{ij}_{\alpha\beta}A^{kl}_{\alpha\beta}}
{\lambda_\alpha\lambda_\beta(\lambda_\alpha+\lambda_\beta)}.
\]
The linear–quadratic cross term vanishes for this centered Gaussian OU process. The total integrated covariance through quadratic stress order is the sum of these two tensors. A viscosity-like coefficient would additionally divide by a specified physical volume; no material volume is assigned here.

## 4. Reproducible numerical audit

Run:

    python audits/jitterbug_mechanical_hessian.py
    python audits/jitterbug_strain_ou_green_kubo.py
    python -m pytest -q tests/test_jitterbug_strain_ou_green_kubo.py

The new script computes all six strain components, the projected c and A, and the complete 6x6 integrated linear, quadratic and total covariance matrices with kBT=mu=1 as reporting units. It checks symmetry and positive semidefiniteness. The output matrices are finite-model values, not universal constants. The dedicated workflow is the reproducibility record.


### 4.1 Canonical numerical output

The first successful CI evaluation (unit spring, unit rest length, kBT=mu=1) gives the same result for the three diagonal components:
- linear contribution: 2;
- centered quadratic contribution: 6.50606398809524;
- total integrated autocorrelation: 8.50606398809524.

For each of the three independent off-diagonal shear coordinates:
- linear contribution: 2;
- centered quadratic contribution: 3.18718998015873;
- total: 5.18718998015873.

The projected strain-Hessian Frobenius norms squared are 77.375 for each diagonal component and 19.125 for each shear component. The unprojected and projected linear-stress coefficient norms agree: sqrt(8) for diagonal components and 2 for shear components, so these c vectors have no component in the 12-dimensional nullspace. The positive eigenvalues are the same six-value multiset already recorded in the rigidity audit: 2-sqrt(2) (3), 1 (5), 2 (9), 3 (3), 2+sqrt(2) (3), 4 (1).

These are unit-normalized finite-model integrated covariance coefficients. Restore physical factors as
linear = (kBT/mu) times the reported linear number, and quadratic = ((kBT)^2/mu) times the reported quadratic number. A division by a physical volume is not included.

## 5. Interpretation and next mathematical obstruction

- [N] The stiffness range supports a well-defined finite OU covariance and Green–Kubo integral.
- [N] The six internal mechanisms remain zero modes of the declared energy; they are not removed by a physical derivation, only excluded to define the conditional OU benchmark.
- [O] A coupled phonon/phason theory needs new internal coordinates and a potential H(u,w,epsilon) whose Hessian and both conjugate stresses are derived together.
- [O] If the mechanisms are to be stabilized, the stabilizing constraints/potential must come from independently justified Jitterbug panel hinges, contact geometry, or a measured constitutive law—not arbitrary diagonal regularization.
- [O] A material viscosity requires calibrated units, volume, masses/mobility, a physically justified stationary dynamics, and a continuum/thermodynamic limit.

**Conclusion:** this is the first strain-derived Green–Kubo calculation for the 3D Jitterbug linkage, but only on the 24-dimensional positive-stiffness subspace. It does not yet establish physical phonons, phasons, or viscosity.
