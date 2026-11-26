# T130 — Q6 discrete gradients, barycentres, traction moments and resistance assembly

**Status:** [P] finite-dimensional identities; [N] unit tests; [O] hydrodynamic calibration and continuum convergence.  
**Depends on:** T128–T129.

## 1. Discrete shape gradients on Q6

Let \(x_v=\Phi(v)\in\mathbb R^2\) be the calibrated shape coordinate of vertex \(v\), and let \(f_v\) be a scalar field on the 64 vertices. Estimate its local shape gradient by weighted least squares over the six incident edges:

\[
G_v=\sum_{w\sim v}\omega_{vw}(x_w-x_v)(x_w-x_v)^T,\qquad
b_v=\sum_{w\sim v}\omega_{vw}(x_w-x_v)(f_w-f_v),
\]
\[
\nabla_{Q6}f(v)=G_v^{-1}b_v.
\]

The formula is defined when the six projected edge directions span the two-dimensional shape tangent plane, equivalently \(G_v\) is positive definite. The implementation reports the local condition number and rejects collapsed edges or rank-deficient stars. For an affine field \(f(x)=a\cdot x+c\), reconstruction is exact up to floating-point roundoff whenever the local star spans \(\mathbb R^2\).

## 2. Geometric barycentre and moment arms

For boundary/body quadrature points \(x_i\in\mathbb R^2\) with positive weights \(w_i\), define

\[
x_c=\frac{\sum_iw_ix_i}{\sum_iw_i}.
\]

For local hydrodynamic tractions \(t_i\), the resultant force and planar moment are

\[
F_h=\sum_iw_it_i,\quad
M_o=\sum_iw_i(x_i-o)\times t_i,\quad
M_c=\sum_iw_i(x_i-x_c)\times t_i.
\]
The change-of-origin identity is
\[
M_c=M_o-(x_c-o)\times F_h.
\]
The geometric barycentre is a declared reference point, not automatically the centre of resistance or centre of mass.

## 3. Resistance from local kinematic Jacobians

At quadrature point \(i\), let \(J_i\) map generalized velocities \(qdot=(\xi_x,\xi_y,\omega,\dot r)\) to local boundary velocity, and let \(D_i\) be a symmetric positive-definite local drag tensor. The finite local-drag model assembles

\[
R_h=\sum_iw_iJ_i^TD_iJ_i.
\]

Consequently \(R_h=R_h^T\) and
\[
qdot^TR_hqdot=\sum_iw_i(J_iqdot)^TD_i(J_iqdot)\ge0.
\]
This is a positive-dissipation identity for the declared local drag model. It is not a general Stokes/BEM discretization: nonlocal hydrodynamic interactions require a mobility/resistance kernel coupling distinct quadrature points.

Partitioning \(R_h\) into body and shape blocks gives

\[
A_h=-R_{bb}^{-1}R_{bs},\qquad
g_{S,h}=R_{ss}-R_{sb}R_{bb}^{-1}R_{bs}.
\]

If \(R_{bb}\) is positive definite, the Schur complement is positive semidefinite (positive definite when the full resistance has no nontrivial zero-dissipation shape mode). The force-free body velocity is \(\xi=A_h\dot r\).

## 4. Implementation and tests

Implementation: audits/purcell_swimmer_wall/discrete_geometry.py.  
Tests: tests/test_purcell_discrete_geometry.py.

The tests cover affine-gradient recovery on the Q6 shape graph, weighted barycentre and moment-origin shift, symmetry/positive semidefiniteness of a synthetic local resistance assembly, nonnegative dissipation, and force/torque-free elimination through the Schur complement.

## 5. Evidence limits

- **Exact algebraic identities [P]:** barycentre, moment-origin shift, resistance symmetry/positive semidefiniteness, and Schur-complement reduction under the stated hypotheses.
- **Finite numerical tests [N]:** affine gradient recovery and a synthetic positive local-drag model.
- **Open [O]:** physical quadrature weights and shape Jacobians for the Purcell arms; calibrated six-axis Q6-to-shape map; wall-corrected nonlocal Stokes/BEM resistance; comparison against the T128 continuous connection; convergence of discrete gradients, forces, moments and holonomy.
- **Not claimed:** the geometric vertex barycentre equals the hydrodynamic centre; local resistive-force theory captures nonlocal Stokes interactions; or this finite assembly validates a physical swimmer.

## References

1. Micalizio, Morandotti, Shum & Zoppello (2026), Purcell swimmer near a wall, DOI: 10.1007/s11012-026-02136-0.
2. Shapere & Wilczek (1987), Self-propulsion at low Reynolds number, Phys. Rev. Lett. 58, 2051–2054.
