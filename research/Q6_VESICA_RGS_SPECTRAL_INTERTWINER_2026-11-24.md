# Q6–Vesica–RGS spectral intertwiner on a three-dimensional invariant sector

**Date:** 24 November 2026  
**Classification:** exact finite graph construction + numerical RGS carrier match  
**Status:** Q6 side independently checked; combined RGS-array audit script supplied; quadratic spectral law is an interpolation candidate, not a first-principles theorem.

## 1. Split Q6 into its two trigram factors

The six-cube graph is the Cartesian product \(Q_6=Q_3\square Q_3\), with 64 vertices labelled by ordered pairs of three-bit words \((L,U)\). Let \(L_3\) be the combinatorial Laplacian of \(Q_3\), in binary order \(000,\ldots,111\). Then
\[
L_6=L_3\otimes I_8+I_8\otimes L_3.
\]
The antipodal reflection on each trigram is \(P_8:k\mapsto7-k\), and the single geometric Minkowski reflection on the paired state space is
\[
R_6=P_8\otimes P_8.
\]

## 2. Operator-adapted trigram compression

Use the three orthonormal row vectors
\[
C_Q=\begin{pmatrix}
\frac1{\sqrt8}(1,1,1,1,1,1,1,1)\\[1mm]
\frac1{\sqrt{168}}(7,1,-3,-5,-5,-3,1,7)\\[1mm]
\frac1{\sqrt8}(1,-1,-1,1,-1,1,1,-1)
\end{pmatrix}.
\]
They are eigenvectors of \(L_3\), with eigenvalues \(0,4,6\), respectively. The third row is the unique top Walsh-parity mode of the three-cube. The second row is the angular-even mode already present in the Vesica moment construction; its choice fixes one direction inside the three-dimensional eigenvalue-4 eigenspace.

The checks give
\[
C_QC_Q^T=I_3,\qquad
C_QL_3C_Q^T=\operatorname{diag}(0,4,6),\qquad
C_QP_8=DC_Q,
\]
where \(D=\operatorname{diag}(1,1,-1)\). The selected row space is exactly \(L_3\)-invariant to numerical precision.

The tensor map \(K=C_Q\otimes C_Q\) has orthonormal rows. Its 64 columns are pairwise distinct, so the full nine-component lookup still distinguishes all 64 labelled hexagrams.

## 3. The canonical symmetric one-excitation sector

In \(V_3\otimes V_3\), with ordered basis \((e_0,e_4,e_6)\) corresponding to the three rows of \(C_Q\), let \(E:\mathbb R^3\to\mathbb R^9\) have columns
\[
u_0=e_0\otimes e_0,
\]
\[
u_4=\frac{e_0\otimes e_4+e_4\otimes e_0}{\sqrt2},\qquad
u_6=\frac{e_0\otimes e_6+e_6\otimes e_0}{\sqrt2}.
\]
This is the symmetric one-excitation sector over the constant mode. It is fixed by factor exchange and is invariant under both the compressed Q6 Laplacian and the diagonal reflection:
\[
E^TE=I_3,\qquad
L_9E=E L_{\rm red},\qquad
(D\otimes D)E=ED,
\]
with
\[
L_9=K L_6 K^T,\qquad
L_{\rm red}=E^TL_9E=\operatorname{diag}(0,4,6).
\]

Define the explicit 3-by-64 coisometry
\[
\boxed{F=E^T(C_Q\otimes C_Q).}
\]
It obeys
\[
FF^T=I_3,\qquad
FL_6=L_{\rm red}F,\qquad
FR_6=DF.
\]
Thus the selected three-dimensional Q6 sector is simultaneously invariant for the graph Laplacian and the geometric antipodal reflection. The 64 labelled states remain distinct in the nine-component lookup; after projection by \(F\), there are 27 distinct three-vectors. The rank-three map is intentionally lossy on the full 64-dimensional space (kernel dimension 61).

## 4. Match to the original RGS half-scale carrier

The original stored RGS arrays independently determine the six-dimensional carrier with lower and upper triplets
\[
K_0J_A=J_A\operatorname{diag}(0.5,0.6,0.7),\qquad
K_0J_B=J_B\operatorname{diag}(0.8,0.9,1.0),
\]
and
\[
Z_AJ_A=-\tfrac12J_B,\quad Z_AJ_B=+\tfrac12J_A,\qquad
Z_SJ_A=+\tfrac12J_B,\quad Z_SJ_B=+\tfrac12J_A.
\]
Use the already recovered channel-sign gauge \(J_B^\sharp=-J_BD\). Define the maps from all 64 Q6 labels into the RGS carrier by
\[
\Phi_A=J_AF,\qquad \Phi_B^\sharp=J_B^\sharp F.
\]

The unique polynomial of degree at most two taking the selected Q6 eigenvalues \(0,4,6\) to the RGS lower-triplet eigenvalues \(0.5,0.6,0.7\) is
\[
\boxed{f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}.}
\]
It is increasing for \(x\ge0\), and
\[
f(0,4,6)=(0.5,0.6,0.7),\qquad
f(0,4,6)+0.3=(0.8,0.9,1.0).
\]
Using \(FL_6=L_{\rm red}F\), the RGS eigen-relations imply the composite intertwining identities
\[
K_0\Phi_A\ \simeq\ \Phi_A f(L_6),\qquad
K_0\Phi_B^\sharp\ \simeq\ \Phi_B^\sharp\big(f(L_6)+0.3I\big).
\]
The symbol \(\simeq\) records the floating-point status of the original RGS arrays, not an exact theorem about arbitrary RGS data.

The half-scale operators also transport through the same map and reflection:
\[
Z_A\Phi_A\simeq+\tfrac12\Phi_B^\sharp R_6,\qquad
Z_S\Phi_A\simeq-\tfrac12\Phi_B^\sharp R_6,
\]
\[
Z_A\Phi_B^\sharp\simeq-\tfrac12\Phi_A R_6,\qquad
Z_S\Phi_B^\sharp\simeq-\tfrac12\Phi_A R_6.
\]
Equivalently, in the RGS channel basis the gauged BA blocks remain \(+D/2\) and \(-D/2\). The Q6 antipodal reflection induces exactly the same \(D\) on the selected sector.

This is the sought finite-dimensional operator bridge: a rank-three invariant sector of the full 64-state Q6 graph maps into the original RGS six-dimensional carrier, with the graph Laplacian, reflection, and half-scale couplings all represented.

## 5. What is established, and what is not

**Established on the Q6 side:** the exact product-graph Laplacian, the operator-adapted row space, the symmetric one-excitation sector, the 3-by-64 coisometry, its reflection and Laplacian intertwining identities, and the 64/27 feature counts.

**Numerically established previously from the original RGS arrays:** the six-dimensional carrier, the lower/upper spectra, the \(Z_A,Z_S\) pairing, and the gauged BA blocks. The new combined audit script reconstructs the RGS basis from the original four arrays and checks the composite identities directly.

**Candidate rather than derived law:** the polynomial \(f\) is the unique quadratic interpolation through three already known eigenvalue pairs. It is not yet derived from an independent physical principle. The result is a finite spectral correspondence, not a continuum limit or a claim of full 64-dimensional equivalence.

## 6. Why the earlier pointwise-product quotient is not the RGS reduction

The alternative pointwise multiplication map on the three marked channels is reflection-equivariant, but it is not an invariant quotient for the compressed Q6 Laplacian: its operator leakage is nonzero (Frobenius norm 2). The present symmetric one-excitation projection \(E^T\), by contrast, is an invariant spectral projection. Therefore \(F=E^T(C_Q\otimes C_Q)\) is the preferred operator-derived reduction for the RGS bridge. The pointwise-product construction remains a separate algebraic quotient and must not be conflated with this spectral map.

## 7. Reproduction

Run from the repository root:
    python audits/audit_q6_vesica_rgs_spectral_intertwiner.py

The script loads the original K0.npy, P_G.npy, Z_A.npy and Z_S.npy files, reconstructs the RGS basis deterministically, builds the Q6 maps, checks the combined intertwining residuals, and writes results/json/q6_vesica_rgs_spectral_intertwiner_2026-11-24.json.

**Classification:** exact finite graph identities + numerical RGS intertwining on a selected three-dimensional invariant sector + quadratic spectral interpolation candidate. Full 64-dimensional equivalence remains false and is not claimed.
