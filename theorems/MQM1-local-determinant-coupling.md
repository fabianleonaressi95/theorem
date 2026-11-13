# MQM-1: local scalar coupling to fermion and boson determinants

**Classification:** exact finite-matrix extension, conditional on supplied A13 operators and on the explicit local-field promotion below. The implementation does not fabricate or claim to reconstruct missing A13 matrices.

## 1. Promotion of the collective scalar

The recovered A13 SEA construction has
\[
D_F(q)=D_{\rm kin}+\operatorname{diag}(m_F+g_Fq\tau_g),
\quad
K_B(q)=K_{B,0}+\lambda_Bq\,\operatorname{diag}(\tau,\tau).
\]
The local extension is defined by replacing the collective \(q\) with the vertex field \(\phi_g\):
\[
D_F[\phi]=D_{\rm kin}+
\operatorname{diag}_{g,s}(m_F+g_F\phi_g\tau_g),
\]
\[
K_B[\phi]=K_{B,0}+
\operatorname{diag}_{g,\sigma}(\lambda_B\phi_g\tau_g),
\]
where \(s\) indexes fermionic internal degrees of freedom and \(\sigma\) the two bosonic sheets. Thus constant \(\phi_g=q\) recovers the original collective operators exactly.

## 2. Effective action and exact derivatives

On the domain where \(D_F[\phi]\) is invertible and \(K_B[\phi]\) is positive definite, define
\[
\Gamma_{\rm det}[\phi]=-\frac12\operatorname{Tr}\log(D_F^\dagger D_F)
+\frac12\operatorname{Tr}\log K_B
=-\log|\det D_F|+\frac12\log\det K_B.
\]
Let \(V_g=\partial_{\phi_g}D_F\) and \(W_g=\partial_{\phi_g}K_B\). They are constant diagonal matrices:
\[
(V_g)_{(h,s),(h,s)}=\delta_{gh}g_F\tau_g,
\quad
(W_g)_{(h,\sigma),(h,\sigma)}=\delta_{gh}\lambda_B\tau_g.
\]
The exact finite-dimensional gradient is
\[
\boxed{
\partial_g\Gamma_{\rm det}
=-\operatorname{Re}\operatorname{Tr}(D_F^{-1}V_g)
+\frac12\operatorname{Tr}(K_B^{-1}W_g)
}
\]
and the full Hessian is
\[
\boxed{
\partial_h\partial_g\Gamma_{\rm det}
=\operatorname{Re}\operatorname{Tr}(D_F^{-1}V_hD_F^{-1}V_g)
-\frac12\operatorname{Tr}(K_B^{-1}W_hK_B^{-1}W_g).
}
\]
No derivative-of-\(V_g\) or derivative-of-\(W_g\) term appears because the promoted operators depend affinely on \(\phi\).

Add these terms to the local PSU scalar action:
\[
\Gamma_{\rm MQM}[\phi]=S_\phi[\phi]+\Gamma_{\rm det}[\phi].
\]
The combined gradient and Hessian are sums of the corresponding scalar and determinant expressions.

## 3. Variational dynamics

For positive mobility matrix \(M\), the local dissipative evolution
\[
\dot\phi=-M\nabla\Gamma_{\rm MQM}[\phi]
\]
satisfies
\[
\frac{d\Gamma_{\rm MQM}}{dt}
=-\nabla\Gamma_{\rm MQM}^{T}M\nabla\Gamma_{\rm MQM}\le0
\]
as long as the trajectory remains in the domain where the fermion matrix is nonsingular and the boson Hessian positive definite. The domain boundary is a genuine constraint; no continuation through a zero fermion singular value or boson eigenvalue is implied.

## 4. Evidence and limits

**Exact:** determinant gradient/Hessian identities for the stated affine finite-matrix operators; reduction to the collective \(q\) operators for constant \(\phi\).

**Numerically tested:** finite-difference agreement of the full gradient and Hessian on small synthetic matrices; Hessian symmetry; rejection of singular/non-positive domains.

**Model extension:** the replacement \(q\mapsto\phi_g\) in both determinant operators. This is a natural local promotion but not uniquely forced by the existing collective A13 model. In particular, the bosonic diagonal profile \(\phi_g\tau_g\) is an explicit local ansatz.

**Not claimed:** a new derivation of the archived A13 matrices, physical calibration of \(m_F,g_F,m_B,\lambda_B,\mu,\kappa\), continuum renormalization, four-dimensional FEEC/DEC convergence, or QCD color dynamics. The archived SU(2) connection is a geometric spin-fibre connection, not SU(3) color.

## 5. Reproduction

\`python -m unittest discover -s tests -p test_mqm_local_determinants.py -v\`


## 6. Audit on the archived A13 operators (64 local degrees of freedom)

The source bundle contains the actual finite operators, so the preceding synthetic-matrix tests have now been supplemented by a reconstruction from the archived data:

- \(D_{\rm kin}\in\mathbb C^{512\times512}\), using four Euclidean Clifford matrices and the 192 stored SU(2) geometric spin-fibre links;
- \(K_{B,0}\in\mathbb R^{128\times128}\), using the Q6 Laplacian, mass term, and torsion-weighted antipodal exchange on the two sheets;
- \(\tau_g\) on all 64 vertices, with \(\tau_{\min}=0.0783438675\), mean \(0.1761407260\), maximum \(0.4502753725\), and exact antipodal residual zero.

The dimensionless parameters are those in the archived SEA derivation:
\[
\kappa=1,\quad m_F=0.5,\quad g_F=0.35,\quad
m_B=0.6,\quad\lambda_B=0.4,\quad\mu=0.2.
\]
The local scalar potential uses \(\lambda=1,\phi_v=1,V_0=0\). These are model parameters, not experimentally calibrated quantities.

### 6.1 Actual-operator derivative check

At a deterministic nonuniform field, the complete 64-component gradient agrees with centered finite differences to maximum absolute error \(1.67\times10^{-8}\). The full Hessian agrees with finite differences of the gradient to maximum absolute error \(2.44\times10^{-11}\); its symmetry residual is \(9.32\times10^{-19}\).

### 6.2 Uniform background and local stability

For \(\phi_g=q\), the uniform field is not stationary in the full 64-dimensional problem. At \(q=1\), the gradient norm is \(0.63369\), and its nonuniform RMS component is \(0.04253\). Thus solving only the collective one-dimensional equation would miss a genuine local force generated by the inhomogeneous torsion profile and determinant response.

Starting from \(\phi_g=1\), a damped Newton solve using the exact analytic Hessian converges in six iterations to a nonuniform stationary field:
\[
\min_g\phi_g=1.8583839853,\quad
\max_g\phi_g=1.9098098882,\quad
\bar\phi=1.8700400992,\quad
\sigma_\phi=0.0161991714.
\]
The residual gradient norm is \(1.25\times10^{-14}\). The Hessian spectrum is strictly positive in this finite model:
\[
\lambda_{\min}(\nabla^2\Gamma_{\rm MQM})=0.1418533417,
\quad
\lambda_{\max}=16.7189762063.
\]
The bosonic minimum eigenvalue at this point is \(0.4558040911\), and the fermionic minimum singular value is \(0.9478604514\); hence the stationary point lies inside the operator domain.

The field is strongly correlated with the recovered torsion proxy (\(\operatorname{corr}(\phi,\tau)=0.9269816741\)). This is a numerical property of the declared model and parameters, not evidence by itself for a universal torsion law or a physical condensate.

### 6.3 Classification

**Numerically verified on archived finite matrices:** the local gradient/Hessian, a nonuniform stationary point, and positive local Hessian spectrum.

**Model-dependent result:** the uniform scalar background is not stationary and the selected minimum is nonuniform. This depends on the stated local promotion, the two-sheet bosonic ansatz, the metric-edge scalar action, and the dimensionless parameter values.

**Still open:** parameter sensitivity and uniqueness of the minimum; derivation of the local bosonic coupling from the microscopic RGS-EMS action; physical-unit calibration; continuum/refinement convergence and renormalization. The result is not a prediction of a physical phase transition.

Reproduction from the original archive:
\`python audits/morphodynamics/mqm_a13_local_backreaction.py --bundle A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip --output audits/morphodynamics/mqm_a13_local_backreaction.json\`
