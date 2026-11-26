# Finite-dimensional RGS half-scale carrier and recovered BA block

**Date:** 24 November 2026  
**Classification:** numerical proposition on the four stored 188D arrays  
**Status:** **NUMERICALLY VERIFIED**; no continuum or physical interpretation claimed

## Data and hypotheses

Take the four real \(188\times188\) float64 arrays at repository root:
\[
K_0,\quad P_G,\quad Z_A,\quad Z_S.
\]
All claims below refer to these stored arrays and their stated numerical precision. They are not universal statements about arbitrary RGS matrices.

## Proposition

The arrays determine a six-dimensional subspace \(\mathcal W\subset\mathbb R^{188}\) with orthogonal projector
\[
Q=4Z_S^2=-4Z_A^2,\qquad \operatorname{rank}Q=6.
\]
The matrix \(Z_S\) is symmetric with eigenvalues \(+1/2\) and \(-1/2\), each of multiplicity three on \(\mathcal W\), and zero on \(\mathcal W^\perp\). The matrix \(Z_A\) is skew-symmetric and anticommutes with \(Z_S\).

Let
\[
P_+=2Z_S^2+Z_S
\]
be the projector onto the \(+1/2\) eigenspace. Choose an orthonormal basis \(V\) of \(\operatorname{ran}P_+\) and put \(W=2Z_AV\). Then \(U=(V,W)\) is an orthonormal basis of \(\mathcal W\), with
\[
U^TZ_SU=\frac12\begin{pmatrix}I&0\\0&-I\end{pmatrix},\qquad
U^TZ_AU=\frac12\begin{pmatrix}0&-I\\I&0\end{pmatrix}.
\]

The carrier is \(K_0\)-invariant to numerical precision. Its compression is
\[
U^TK_0U=\begin{pmatrix}H&-0.15I\\-0.15I&H\end{pmatrix},
\qquad
\operatorname{spec}(H)=\{0.65,0.75,0.85\}.
\]
Consequently the six eigenvalues of \(K_0|_{\mathcal W}\) are
\[
0.5,\ 0.6,\ 0.7,\ 0.8,\ 0.9,\ 1.0.
\]

Let \(R\) diagonalize \(H\), and define
\[
J_A=\frac{(V+W)R}{\sqrt2},\qquad
J_B=\frac{(V-W)R}{\sqrt2}.
\]
Then
\[
K_0J_A=J_A\operatorname{diag}(0.5,0.6,0.7),\quad
K_0J_B=J_B\operatorname{diag}(0.8,0.9,1.0),
\]
\[
Z_AJ_A=-\frac12J_B,\qquad Z_AJ_B=+\frac12J_A.
\]

Finally, with
\[
D=\operatorname{diag}(1,1,-1),\qquad J_B^\sharp=-J_BD,
\]
the historical three-dimensional blocks are recovered:
\[
(J_B^\sharp)^TZ_AJ_A=+\frac12D,\qquad
(J_B^\sharp)^TZ_SJ_A=-\frac12D.
\]
The same \(D\) is the lower-triplet spectral involution
\[
P_{0.5}+P_{0.6}-P_{0.7}.
\]
Thus the old \(BA\) half-sign block is reproduced by an explicit orthogonal channel-sign gauge. The full \(188\times188\) operators are not equal to their \(3\times3\) blocks.

## Numerical evidence

- \(P_G\) is an orthogonal projector of rank 64, and \(\operatorname{ran}P_G=\ker K_0\) to numerical precision.
- \(K_0\mathcal W\subset\mathcal W\) with Frobenius leakage approximately \(3.1\times10^{-12}\).
- The gauged block residuals are approximately \(6.7\times10^{-16}\) for \(Z_A^{BA}-D/2\) and \(6.1\times10^{-16}\) for \(Z_S^{BA}+D/2\).
- The deterministic reconstruction and checks are implemented in audits/reconstruct_rgs_half_carrier_basis.py; the source-array audit is research/RGS_HALF_ORIGINAL_ARRAYS_AUDIT_2026-11-24.md.

## Conditional symmetry obstruction

In the ordered \((J_A,J_B)\) basis, a diagonal cyclic \(C_3\) action on both triplets commutes with \(Z_A,Z_S\) but not \(K_0\). Independent cyclic actions on the two triplets already fail to commute with \(Z_A\). Moreover, the simple spectra of \(K_0|_{J_A}\) and \(K_0|_{J_B}\) imply that their real orthogonal centralizers contain no nontrivial element of order three.

Therefore no nontrivial factorwise \(C_3\times C_3\) action can preserve the full triple \((K_0,Z_A,Z_S)\) in this carrier. This is a conditional obstruction to an intertwiner that preserves all three operators. It does not prohibit a geometric map that does not intertwine \(K_0\), a Reynolds-averaged replacement operator, or a covariant transformation law for \(K_0\).

## Proof status and limitations

This is a **finite numerical proposition** for the four stored arrays. The identities are verified to floating-point tolerance, not proved as exact rational identities for an abstract family. The deterministic script must be run to regenerate the basis NPZ and JSON report. No physical interpretation, continuum limit, or universal theorem is claimed.


## Geometric realization of the channel involution

The involution \(D=\operatorname{diag}(1,1,-1)\) has an exact realization as the parity representation of the Minkowski reflection \((t,x,y)\mapsto(t,x,-y)\) on three paired channels of the two null cones defining the Vesica. The reflection swaps the two endpoint channels and fixes the central channel; in the orthonormal even/odd basis its matrix is \(D\). Under the recovered upper-triplet gauge \(J_B^\sharp=-J_BD\), this is the geometric channel interpretation of the numerical BA blocks \(\pm D/2\). This identifies the finite-dimensional coupling block with a Vesica–Minkowski reflection representation, but does not extend to a full 188D intertwiner or encode all 64 hexagrams. See [the explicit construction](../research/VESICA_MINKOWSKI_RGS_D_REFLECTION_CHANNEL_REPRESENTATION_2026-11-24.md).


## Algebraic nine-to-three quotient of the paired hexagram moments

The complete eight-sample trigram moment map and its 64-state tensor table are documented separately. A further map from the nine-dimensional paired channel space to one three-channel copy is obtained by supplying the pointwise algebra on the three marked labels (-,0,+). In the reflection-adapted basis (f0,f+,f-), its multiplication matrix M has rank three, satisfies M M^T=I3, and obeys
\[
M(D\otimes D)=DM.
\]
This is equivariance for the single physical diagonal Minkowski reflection.

The composite M(C tensor C): R^64 -> R^3 has rank three and kernel dimension 61. It maps the 64 labelled basis states to only 23 distinct three-vectors; collision multiplicities are 1:2 classes, 2:12 classes, 3:2 classes, 4:6 classes, 8:1 class. It is therefore a lossy algebraic quotient, not a replacement for the full 64-state lookup or the nine-component feature table.

The reduction is not selected by reflection alone: the space of linear maps equivariant for the diagonal Z2 has dimension 14. The pointwise channel algebra is the additional structure selecting this particular M. The map matches the RGS channel involution D, but it does not derive the coefficient 1/2 in the already verified BA blocks and does not intertwine the full 188D triple (K0, ZA, ZS). The latter dynamical bridge remains open.

Details and complete collision table: research/VESICA_HEXAGRAM_9_TO_3_POINTWISE_ALGEBRA_REDUCTION_2026-11-24.md and results/json/vesica_hexagram_9_to_3_algebra_reduction_2026-11-24.json.


## Operator-derived Q6 spectral sector and composite RGS intertwiner

The six-cube graph is \(Q_6=Q_3\square Q_3\). An operator-adapted trigram coisometry \(C_Q\) is formed from Q3 Laplacian eigenmodes with eigenvalues \(0,4,6\): the constant mode, the selected angular-even mode, and the top Walsh-parity mode. It satisfies
\[
C_Q L_3 C_Q^T=\operatorname{diag}(0,4,6),\qquad C_QP_8=DC_Q.
\]
The full tensor feature map \(C_Q\otimes C_Q\) has 64 distinct basis-state columns.

Inside the nine-dimensional tensor sector, let E select the symmetric one-excitation subspace over the constant mode:
\[
e_0\otimes e_0,\quad
(e_0\otimes e_4+e_4\otimes e_0)/\sqrt2,\quad
(e_0\otimes e_6+e_6\otimes e_0)/\sqrt2.
\]
It is invariant under the compressed Q6 Laplacian and the diagonal reflection, with reduced Laplacian \(\operatorname{diag}(0,4,6)\) and reflection D. Thus
\[
F=E^T(C_Q\otimes C_Q):\mathbb R^{64}\to\mathbb R^3
\]
satisfies \(FF^T=I_3\), \(FL_6=\operatorname{diag}(0,4,6)F\), and \(FR_6=DF\). The full 64-state, nine-component lookup remains pairwise distinct; the selected rank-three quotient has 27 distinct basis-state images and is intentionally lossy.

Let \(f(x)=1/2+x/120+x^2/240\). It maps the selected Q6 eigenvalues \(0,4,6\) to the original RGS lower-triplet eigenvalues \(0.5,0.6,0.7\); \(f+0.3\) maps them to the upper triplet \(0.8,0.9,1.0\). This is the unique quadratic interpolation through the three known spectral pairs, not yet a first-principles law.

With \(\Phi_A=J_AF\) and \(\Phi_B^\sharp=J_B^\sharp F\), \(J_B^\sharp=-J_BD\), the existing RGS carrier identities and the new Q6 identities give the composite intertwining relations
\[
K_0\Phi_A\simeq\Phi_A f(L_6),\qquad
K_0\Phi_B^\sharp\simeq\Phi_B^\sharp(f(L_6)+0.3I),
\]
\[
Z_A\Phi_A\simeq+\tfrac12\Phi_B^\sharp R_6,\quad
Z_S\Phi_A\simeq-\tfrac12\Phi_B^\sharp R_6,
\]
\[
Z_A\Phi_B^\sharp\simeq-\tfrac12\Phi_A R_6,\quad
Z_S\Phi_B^\sharp\simeq-\tfrac12\Phi_A R_6.
\]
Here \(\simeq\) is numerical because the original RGS arrays are floating-point data. The combined reproducible audit is audits/audit_q6_vesica_rgs_spectral_intertwiner.py. Full details and the 64-state table are in research/Q6_VESICA_RGS_SPECTRAL_INTERTWINER_2026-11-24.md and results/json/q6_vesica_rgs_spectral_intertwiner_2026-11-24.json.

This establishes a finite-dimensional operator bridge on one selected three-dimensional Q6 invariant sector, not an equivalence of the full 64-dimensional Q6 state space with the 188-dimensional RGS system. The quadratic spectral law remains a matching candidate.
