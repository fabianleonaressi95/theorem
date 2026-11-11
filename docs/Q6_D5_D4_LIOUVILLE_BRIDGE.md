# Q6–D5–D4 bridge to the Liouville–Bergman law

**Status:** exact conditional invariance lemma; the identification of the Q6-induced D4 action with the five-dimensional Q6 D5 spectral sector remains open.

## 1. Previously established Q6–D5 data

Let \(D_0\) and \(D_1\) be the Q6 incidence matrices, and let
\[
H_1=D_1^T D_1.
\]
The selected five-dimensional rational mode space is
\[
E_5=\ker_{\mathbb Q}(H_1-12I),\qquad \dim E_5=5.
\]
If \(C\in\mathbb Z^{129\times192}\) is the integral fundamental-cycle matrix and \(V\in\mathbb Q^{192\times5}\) is a basis matrix for \(E_5\), the mode map is
\[
\Pi_5(c)=cCV.
\]
The exact repository audit establishes rank five, saturated integer kernel rank 124, and the torsion-free quotient
\[
\mathbb Z^{129}/K_{\mathbb Z}\simeq\Pi_5(\mathbb Z^{129}).
\]
The pointwise Wilson weight does not descend to this quotient. The positive effective weight is the complete fibre sum
\[
W_{\rm eff}([c])=\sum_{k\in K_{\mathbb Z}}
\prod_{e=1}^{192}\frac{I_{|(c+k)C)_e|}(\beta_t)}{I_0(\beta_t)},
\]
where the intended flux index is \(|((c+k)C)_e|\). The sum is absolutely convergent, but its complete numerical value is not yet enclosed by a useful certified interval. No Wilson-to-Bergman limit is established by the integer quotient alone.

## 2. The D5 Liouville–Bergman chart

For the isotropic five-mode Hamiltonian
\[
H_5(q,\pi)=\frac{\|\pi\|^2}{2\beta_{\rm eff}}
+\frac{\beta_{\rm eff}\lambda_{\rm eff}}2\|q\|^2,
\quad
\beta_{\rm eff}=\frac{a_s^4}{g_7^2},
\quad
\lambda_{\rm eff}=\frac{12}{a_s^2},
\quad
\Omega=\sqrt{\beta_{\rm eff}\lambda_{\rm eff}}/\beta_{\rm eff}
=\frac{\sqrt{12}}{a_s},
\]
define
\[
z_j=\frac{\sqrt{\beta_{\rm eff}\Omega}\,q_j
+i\pi_j/\sqrt{\beta_{\rm eff}\Omega}}{\sqrt{20}},
\quad j=1,\ldots,5.
\]
Then
\[
d\mu_L=\prod_{j=1}^5dq_j\,d\pi_j
=20^5\,d^{10}z,
\]
and on the type-IV domain
\[
D_5=\{z:N(z)>0,\ |z^Tz|<1\},
\qquad
N(z)=1-2z^\dagger z+|z^Tz|^2,
\]
the Bergman volume density in this chart is
\[
dV_B=N(z)^{-5}d\mu_L.
\]
This is the geometric Liouville–Bergman law already recorded in the Q6–D5 work. It is distinct from a claim that the finite-coupling Wilson marginal equals this measure.

## 3. Exact D4 invariance lemma on the phase-space chart

Take
\[
R_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
S_2=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
\]
and extend them to five dimensions by
\[
U_R=R_2\oplus I_3,\qquad U_S=S_2\oplus I_3.
\]
They are real orthogonal matrices and satisfy
\[
U_R^4=U_S^2=I_5,\qquad
U_SU_RU_S=U_R^{-1}.
\]
Thus they define an orthogonal five-dimensional representation of \(D_4\).

For any such real orthogonal \(U\), let
\[
(q,\pi)\mapsto(Uq,U\pi),\qquad z\mapsto Uz.
\]
The canonical symplectic form and Liouville measure are invariant:
\[
\sum_j d(Uq)_j\wedge d(U\pi)_j
=\sum_jdq_j\wedge d\pi_j,
\qquad U^*d\mu_L=d\mu_L.
\]
Since \(U^TU=I\) and \(U\) is real,
\[
(Uz)^\dagger(Uz)=z^\dagger z,
\qquad
(Uz)^T(Uz)=z^Tz.
\]
Consequently \(N(Uz)=N(z)\), and hence
\[
\boxed{U^*dV_B=dV_B.}
\]
The isotropic Hamiltonian \(H_5\) is invariant as well. This proves an exact D4 symmetry of the *five-dimensional Liouville–Bergman chart* for the specified representation.

## 4. The missing Q6 intertwining statement

The preceding lemma does **not** yet prove that this representation is the one induced by the D4 action on the 64 RGS/Q6 seed points.

In particular, the Q6 label map \(R\) sends two standard cube-edge directions to diagonals (the directions \(e_1+e_3\) and \(e_2+e_3\)). Therefore \(R\) is not an automorphism of the original cubical Q6 graph and cannot simply be applied to the original Q6 cochain complex or its eigenvalue-12 sector.

The M3 orbit graph, with the eight directions
\[
\{e_1,e_2,e_3,e_4,e_5,e_6,e_1+e_3,e_2+e_3\},
\]
is D4-invariant at the graph level. To identify its action with the five-mode D5 representation, a subsequent exact construction must:
1. build a D4-equivariant cell/cochain complex on the orbit closure (after resolving any non-regular square intersections);
2. construct its exact Hodge operator and determine the relevant five-dimensional invariant spectral subspace;
3. compute the induced matrices \(\rho_5(R),\rho_5(S)\) in an orthonormal rational/real frame;
4. exhibit an explicit intertwiner between that representation and \(R_2\oplus I_3,S_2\oplus I_3\), or replace the block representation by the actual induced one if they differ.

Until these steps are completed, the relation between the M3 D4 action and the previously established Q6 D5 eigenspace is a **candidate bridge**, not a proved identification.

## 5. Status table

- **Exact:** Q6 rational five-mode quotient and saturated rank-124 integer kernel (repository audit).
- **Exact:** Liouville–Bergman density formula in the stated D5 chart.
- **Exact conditional lemma:** any real orthogonal five-dimensional D4 representation acting diagonally on \((q,\pi)\) preserves the canonical Liouville measure, \(N\), and the Bergman density.
- **Open:** deriving the relevant five-dimensional representation from the M3 Q6 orbit complex and constructing an explicit intertwiner.
- **Open:** deriving the Bergman density or its Hua generic-norm regulator as a limit/pushforward of the finite-coupling Wilson fibre marginal.

The formula \(dV_B=N^{-5}d\mu_L\) must not be presented as the evaluation of \(W_{\rm eff}\), nor as a consequence of the rank-five integer quotient.
