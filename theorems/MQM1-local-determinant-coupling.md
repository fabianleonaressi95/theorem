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
