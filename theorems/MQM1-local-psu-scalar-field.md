# MQM-1: local PSU scalar-field extension

**Classification:** exact finite metric-graph variational construction, conditional on the raw PSU coframe norm as the edge metric. This is a proposed local-field extension of the A13 collective-scalar model, not a claim that the current A13 SEA action already contains the weighted kinetic term.

## 1. Identify the scalar sector

The recovered RGS-EMS continuum action contains a real scalar field with
\[
\mathcal L_\phi=-\frac12 g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi
-V(\phi),\qquad
V(\phi)=V_0+\frac{\lambda}{4}(\phi^2-\phi_v^2)^2.
\]
The A13 finite SEA construction instead uses a collective scalar parameter \(q\), coupled through the vertex profile \(\tau_g\):
\[
D_F(q)=D_{\rm kin}+\operatorname{diag}(m_F+g_Fq\tau_g),
\]
\[
K_B(q)=K_{B,0}+\lambda_Bq\,\operatorname{diag}(\tau,\tau).
\]
The finite SEA construction does not by itself specify a local field \(q_g\). We therefore define a local vertex field \(\phi_g\) as an explicit extension, with the constant configuration \(\phi_g=q\) as the collective-mode restriction.

## 2. Metric-graph kinetic action

For each Q6 edge \(e=(u,v)\), let
\[
C_e^{\rm raw}=(X_v-X_u,\|X_v\|-\|X_u\|),\quad
L_e=\|C_e^{\rm raw}\|,\quad
\ell_{\rm rms}=\sqrt{\frac1{192}\sum_eL_e^2}.
\]
Linear interpolation of a scalar field along the metric edge gives
\[
\frac12\int_0^{L_e}\left|\frac{d\phi}{ds}\right|^2ds
=\frac{|\phi_v-\phi_u|^2}{2L_e}.
\]
With the dimensionless global normalization, \(w_e=\ell_{\rm rms}/L_e\), the graph kinetic operator is
\[
K_{\rm PSU}=B\,\operatorname{diag}(w_e)B^T.
\]

This step is an exact one-dimensional metric-edge Dirichlet identity. It is not yet a four-dimensional FEEC/DEC discretization: Q6 has no recovered dual volumes or full 4D cell metric in this construction.

## 3. Local scalar action and variation

For \(n=64\) vertices, use the normalized uniform vertex quadrature as the explicit finite-graph convention:
\[
S_\phi[\phi]=\frac12\phi^TK_{\rm PSU}\phi+
\frac1n\sum_{g=1}^n\left[
V_0+\frac\lambda4(\phi_g^2-\phi_v^2)^2
\right].
\]
The normalization \(1/n\) makes the potential a mean per vertex; it is a declared finite-graph convention, not a recovered PSU dual-volume measure.

The exact gradient and Hessian are
\[
\nabla S_\phi=K_{\rm PSU}\phi+
\frac\lambda n\,\phi\odot(\phi^2-\phi_v^2\mathbf1),
\]
\[
\nabla^2S_\phi=K_{\rm PSU}+
\frac\lambda n\operatorname{diag}(3\phi_g^2-\phi_v^2).
\]
The Euler-Lagrange equation is \(\nabla S_\phi=0\). The gradient flow \(\dot\phi=-M\nabla S_\phi\), for positive mobility \(M\), satisfies
\[
\frac{dS_\phi}{dt}=-\nabla S_\phi^TM\nabla S_\phi\le0.
\]

## 4. Relation to the A13 collective parameter

On the constant subspace \(\phi=q\mathbf1\),
\[
B^T\phi=0,\qquad
S_\phi[q\mathbf1]=V_0+\frac\lambda4(q^2-\phi_v^2)^2.
\]
Thus the metric-edge kinetic term vanishes on the collective mode, while the local potential reduces to a scalar bare potential \(V_{\rm bare}(q)\). The A13 fermionic and bosonic determinant terms can then be coupled to this same collective \(q\) using the existing \(D_F(q)\) and \(K_B(q)\).

For nonconstant \(\phi_g\), a genuinely local SEA extension must replace \(q\tau_g\) by \(\phi_g\tau_g\) in the fermion mass profile and replace the uniform bosonic perturbation by the corresponding vertex-diagonal operator on both sheets. Those local determinant variations are not asserted to be present in the archived A13 implementation and are not silently inferred from the collective-\(q\) calculation.

## 5. What is established and what remains open

**Exact:** the metric-edge interpolation identity; the finite action's gradient and Hessian; the constant-mode restriction; symmetry covariance whenever edge lengths and vertex fields are transformed together.

**Numerically verified:** finite-difference agreement of gradient and Hessian on a test graph; positivity of conductances; symmetry of the Hessian.

**Model extension:** identifying the RGS-EMS scalar \(\phi\) with a local Q6 vertex field and adding the weighted graph kinetic term to the A13 SEA effective action.

**Open:** recover the authoritative RGS-EMS action source documents and exact PSU metric; derive dual-volume weights from a higher-dimensional complex; couple local \(\phi_g\) into the fermion/boson determinants and rederive their variations; calibrate dimensions/couplings; prove refinement and continuum convergence. The recovered closure script itself flags the source action documents and some field-equation terms as missing, so the present bridge must remain conditional.

## 6. Reproduction

Run:
\`python -m unittest discover -s tests -p test_mqm_local_scalar.py -v\`.
