# T138 — The exact two-sheet decomposition of the six-dimensional icosahedral matrix

**Status:** [P] exact finite-dimensional algebra; [O] equivariance under a specified binary-icosahedral action. No physical interpretation is assumed.

## 1. Matrix and block form

\[
C_6=\begin{pmatrix}
0&1&1&-1&-1&1\\
1&0&1&1&-1&-1\\
1&1&0&-1&1&-1\\
-1&1&-1&0&-1&-1\\
-1&-1&1&-1&0&-1\\
1&-1&-1&-1&-1&0
\end{pmatrix}
=\begin{pmatrix}U&S\\S^T&-U\end{pmatrix},
\]
where
\[
U=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},\qquad
S=\begin{pmatrix}-1&-1&1\\1&-1&-1\\-1&1&-1\end{pmatrix}.
\]

## 2. Exact square identity

\[
U^2=I_3+J_3,\qquad
SS^T=S^TS=4I_3-J_3,\qquad US=SU.
\]
Thus the diagonal blocks of \(C_6^2\) are \(U^2+SS^T=5I_3\) and \(U^2+S^TS=5I_3\), while the off-diagonal blocks vanish. Hence, in exact integer arithmetic,
\[
\boxed{C_6^2=5I_6.}
\]
The displayed matrix and the block decomposition agree entrywise. Since \(C_6\) is symmetric, its eigenvalues are \(\pm\sqrt5\); since its trace is zero, each has multiplicity three.

## 3. Two orthogonal sheets

\[
V_+=\ker(C_6-\sqrt5I_6),\qquad
V_-=\ker(C_6+\sqrt5I_6),\qquad
\mathbb R^6=V_+\mathbin{\perp}\oplus V_-,\quad \dim V_\pm=3.
\]
The orthogonal spectral projections are
\[
P_\pm=\frac12\left(I_6\pm\frac{C_6}{\sqrt5}\right),
\]
and satisfy \(P_\pm^T=P_\pm\), \(P_\pm^2=P_\pm\), \(P_+P_-=0\), \(P_++P_-=I_6\).

For \(\lambda=\pm\sqrt5\), writing a vector as \((x,y)\in\mathbb R^3\oplus\mathbb R^3\), the eigenvalue equation becomes
\[
(U-\lambda I_3)x+Sy=0,\qquad S^Tx-(U+\lambda I_3)y=0.
\]
The eigenvalues of \(U\) are \(2,-1,-1\), so \(\lambda I_3-U\) is invertible. Therefore
\[
V_\lambda=\left\{\begin{pmatrix}(\lambda I_3-U)^{-1}Sy\\y\end{pmatrix}:y\in\mathbb R^3\right\}.
\]
Choosing \(y=e_1,e_2,e_3\) gives an explicit basis of each sheet (not necessarily orthonormal).

## 4. Correct rotation/quaternionic interpretation

Each \(V_\pm\), with its inherited Euclidean inner product, is a real three-dimensional Euclidean space. Its orientation-preserving orthogonal transformations form \(SO(3)\). The standard spin double cover is
\[
\operatorname{Spin}(3)\simeq SU(2)\simeq Sp(1)\longrightarrow SO(3).
\]
Unit quaternions realize this cover by conjugation on the three-dimensional space of purely imaginary quaternions.

This does **not** make either \(V_+\) or \(V_-\) a quaternionic module. No endomorphisms \(I,J,K\) on either three-space satisfying the quaternion relations are constructed or asserted. An identification with \(\operatorname{Im}\mathbb H\) requires a choice of oriented orthonormal frame; it does not provide intrinsic quaternionic multiplication on the sheet.

## 5. Exterior-square consequence

\[
\Lambda^2\mathbb R^6=\Lambda^2V_+\oplus(V_+\wedge V_-)\oplus\Lambda^2V_-,
\]
with dimensions \(3+9+3\). The induced operator \(\Lambda^2C_6\) has eigenvalue \(+5\) on the first and third summands (multiplicity 6), and \(-5\) on the mixed summand (multiplicity 9).

## 6. Open 2I* compatibility test

A specific six-dimensional action must first be supplied as matrices \(R_6(g)\) for generators of \(2I^*\) (or for a precisely specified representation of \(2I\)). The required test is
\[
[C_6,R_6(g)]=0
\]
for every generator. If it holds, then \(P_\pm R_6(g)=R_6(g)P_\pm\), and each sheet is an invariant subrepresentation. Their representation types can then be identified by characters/intertwiners.

No such six-index generator action is specified or verified here. Thus 2I*-equivariance, the representation type of each sheet, and identification with a particular quaternionic 2I module remain open.

## 7. Evidence register

| Claim | Status |
|---|---|
| Matrix/block agreement and \(C_6^2=5I_6\) | [P] exact integer identity |
| Spectrum \(\pm\sqrt5\), multiplicity 3 each | [P] |
| Orthogonal splitting and projectors | [P] |
| Graph parametrization of both sheets | [P] |
| \(\operatorname{Spin}(3)\simeq SU(2)\to SO(3)\) | [E] standard |
| Intrinsic quaternionic module on \(V_\pm\) | Not asserted; unsupported |
| Specified commuting \(2I^*\) action | [O] |
| Physical/De Aquino identification | [O]; no physical variable map supplied |

## Reproducibility

Run \`python scripts/audit_t138_c6_two_sheet_spin3.py\` and \`python -m unittest tests.test_t138_c6_two_sheet_spin3\`. The audit checks all 36 entries of the square and the block identities using integer arithmetic. It does not test a \(2I^*\) action because its six-dimensional representation matrices have not been supplied.
