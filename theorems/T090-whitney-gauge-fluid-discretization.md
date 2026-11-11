# T090 — Whitney discretization of the gauge–fluid Q-ball energy

**Date:** 11 November 2026  
**Status:** exact cochain gauge invariance; explicit conforming lowest-order Whitney discretization; finite-mesh variational audit supplied, execution pending.

**Dependencies:** T080, T088, T089.

## 1. Discrete spaces and incidence

Let \(K=(V,E,F)\) be the oriented triangular Q-ball shell. Let \(B_1\in\mathbb R^{|V|\times|E|}\) and \(B_2\in\mathbb R^{|E|\times|F|}\) be the vertex-edge and edge-face incidence matrices, with \(B_1B_2=0\).

Use:
- nodal \(P_1\) density \(\rho_h=\sum_i\rho_i\lambda_i\), with \(\rho_i>0\);
- nodal phase \(\theta_h=\sum_i\theta_i\lambda_i\);
- edge cochain \(a\in C^1(K;\mathbb R)\) for the \(U(1)\) connection;
- lowest-order Whitney 1-form reconstruction for the covariant velocity cochain \(v=B_1^T\theta-q a\).

For an oriented local edge \(i\to j\), the Whitney basis is
\[
w_{ij}=\lambda_i\,d\lambda_j-\lambda_j\,d\lambda_i.
\]
The global edge orientation is fixed once; a local edge basis is multiplied by \(+1\) or \(-1\) according to orientation agreement. Thus
\[
v_h=\sum_{e\in E}v_e w_e,\qquad
F_h=d a_h,\qquad
\int_f F_h=(B_2^Ta)_f.
\]
The face curvature is represented as a constant 2-form density \((B_2^Ta)_f/|f|\) on each flat triangle.

## 2. Tangent anisotropy

For each triangle \(f\), take the panel label from the shell generator and its orthonormal tangent frame \(Q_p\). Evaluate the T088 cubic-harmonic gradient at the normalized panel centroid direction and define \(A_p(\alpha)\) as in T088. The triangle energy uses the induced quadratic form on the triangle tangent plane, represented in the panel frame.

This is a panelwise piecewise-constant coefficient. The parameter \(\alpha\) remains a geometric demonstration parameter, not a calibrated material coefficient.

## 3. Discrete energy

Let \(\lambda_i\) be the barycentric coordinates on each triangle, \(A_f\) its area, and \(\nabla\lambda_i\) the constant surface gradients. Let \(s_i=\sqrt{\rho_i}\) and \(s_h=\sum_i s_i\lambda_i\). For a prescribed scalar potential \(V\), internal energy \(W\), density-gradient coefficient \(\kappa\), gauge stiffness \(g>0\), and charge \(q\), define
\[
\begin{aligned}
\mathcal E_h(\rho,\theta,a)=
&\frac{\kappa}{2}\sum_f A_f
 \langle\nabla s_h,A_f^{\rm tan}\nabla s_h\rangle\\
&+\frac12\sum_f\int_f\rho_h
 \langle v_h,A_f^{\rm tan}v_h\rangle\,dA
+\sum_f\int_f\big(W(\rho_h)+V\rho_h\big)\,dA\\
&+\frac1{2g^2}\sum_f
 \frac{\big((B_2^Ta)_f-\int_fF_{\rm ext}\big)^2}{A_f}.
\end{aligned}
\tag{90.1}
\]
Here \(A_f^{\rm tan}\) denotes the positive tangent tensor on face \(f\), not the scalar area \(A_f\); the notation is distinguished by the superscript. Integrals of the cubic kinetic and polynomial density terms are evaluated with a degree-three exact triangle quadrature. The density-gradient term is exact for the stated \(P_1\) interpolation of \(\sqrt{\rho_i}\).

## 4. Exact discrete gauge symmetry

For any nodal gauge parameter \(\chi\), transform
\[
\theta'=\theta+q\chi,\qquad a'=a+B_1^T\chi.
\]
Then
\[
v'=B_1^T\theta'-qa'=v,
\qquad B_2^Ta'=B_2^Ta+B_2^TB_1^T\chi=B_2^Ta.
\]
All terms in (90.1) are therefore exactly gauge invariant (up to floating-point assembly error). This is an algebraic identity, not an asymptotic statement.

## 5. Discrete first variations

Let \(M_\rho\) be the assembled Whitney 1-form mass matrix with the \(\rho_h A_f^{\rm tan}\) weight, and let \(c=B_2^Ta-f_{\rm ext}\) be the face curvature-flux residual. Then the phase and connection gradients are
\[
\nabla_\theta\mathcal E_h=B_1M_\rho v,
\qquad
\nabla_a\mathcal E_h=-qM_\rho v+
\frac1{g^2}B_2\,\operatorname{diag}(A_f^{-1})c.
\tag{90.2}
\]
The phase equation is the discrete weak continuity law. The connection equation is the discrete gauge-field equation. These are the exact derivatives of the assembled quadratic dependence on \((\theta,a)\).

For the nodal density, with \(s_i=\sqrt{\rho_i}\), the derivative is the sum of:
- the derivative of the density-gradient quadratic form through \(ds_i/d\rho_i=1/(2s_i)\);
- the quadrature derivative \(\frac12\int_f\lambda_i|v_h|_{A_f}^2\);
- \(\int_f\lambda_i(W'(\rho_h)+V)\).

The accompanying audit compares the analytic phase and connection gradients to centred finite differences and checks the density derivative independently.

## 6. Scope

This is a lowest-order conforming discrete model on the existing fixed shell mesh. It does not establish mesh-refinement convergence, a \(\Gamma\)- or Mosco-limit, nonlinear fluid dynamics, or a calibrated seam law. The physical seam set remains available for a later discontinuous-trace/cohesive extension, but no seam penalty is inserted into (90.1). In particular, a panel boundary that is only a chart transition is not automatically a physical crack or disarrangement.

**Classification:** Whitney reconstruction and discrete gauge invariance — exact; discrete variational derivatives — derived; finite-mesh numerical checks — pending execution; continuum convergence and material calibration — open.
