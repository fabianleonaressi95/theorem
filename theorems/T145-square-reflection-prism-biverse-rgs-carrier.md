# T145 — Square reflection, PRISM biverso and the RGS six-dimensional carrier

**Date:** 24 November 2026  
**Type:** exact geometric and operator identities, plus a numerical identification on the archived RGS carrier  
**Status:** square/\(\mathbb Z_2\) and biverso algebra **proved**; RGS carrier realization **numerically verified** from the archived \(188\times188\) arrays; extension to the full \(188\)-dimensional operator and identification with the scalar Euclidean square Laplacian **not claimed**.

## 1. The square supplies the geometric \(\mathbb Z_2\) action

Let \(Q=[0,1]^2\), and divide it along the diagonal \(x=y\):
\[
T_1=\{(x,y)\in Q:y\le x\},\qquad
T_2=\{(x,y)\in Q:x\le y\}.
\]
The orthogonal reflection
\[
r(x,y)=(y,x),\qquad
R=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
satisfies \(R^2=I\), \(R^TR=I\), \(\det R=-1\), and exchanges \(T_1,T_2\). Both triangles have area \(1/2\) of the square.

Let \(\mathcal H_1=L^2(T_1)\), \(\mathcal H_2=L^2(T_2)\). Pullback by \(r\) defines a unitary identification \(J:\mathcal H_1\to\mathcal H_2\). After using \(J\) to identify the two spaces, the reflection acts on \(\mathcal H_1\oplus\mathcal H_1\) as
\[
S_\square=\begin{pmatrix}0&I\\I&0\end{pmatrix},\qquad S_\square^2=I.
\]
Therefore
\[
P_\pm=\frac{I\pm S_\square}{2}
\]
are orthogonal projections onto the even and odd sectors. This is the precise square-to-two-sheet correspondence. The area split \(1/2\) and the projector normalization \(1/2\) are related by the same order-two symmetry, but are different statements: one is a measure partition, the other an operator identity.

## 2. PRISM biverso: exact two-sector reduction

Let \(L_\Omega=L_\Omega^T\) act on one sheet and let \(\kappa\ge0\) be the inter-sheet coupling. With
\[
\sigma=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
S=\sigma\otimes I_n,\qquad
L_{K_2}=I_2-\sigma,\\
L_{\rm bi}=I_2\otimes L_\Omega+\kappa\bigl((I_2-\sigma)\otimes I_n\bigr)
=I_2\otimes L_\Omega+\kappa(I_{2n}-S).
\]
we have \([L_{\rm bi},S]=0\). Since \(P_\pm=(I\pm S)/2\),
\[
L_{\rm bi}P_+=P_+(I_2\otimes L_\Omega),\qquad
L_{\rm bi}P_-=P_-(I_2\otimes L_\Omega+2\kappa I).
\]
The restrictions are consequently
\[
\boxed{L_+=L_\Omega,\qquad L_-=L_\Omega+2\kappa I.}
\]
Equivalently, the orthogonal Hadamard map
\[
H_2=\frac1{\sqrt2}\begin{pmatrix}I&I\\I&-I\end{pmatrix}
\]
diagonalizes the two sheets:
\[
H_2^TL_{\rm bi}H_2=
\begin{pmatrix}L_\Omega&0\\0&L_\Omega+2\kappa I\end{pmatrix}.
\]
This is the standard \(K_2\)-product/symmetric-block spectral splitting. The coupling contributes the factor \(2\kappa\) because \(L_{K_2}\) has eigenvalues \(0,2\).

**Geometric qualification.** The reflection of the cut square gives the exchange involution. The term \(\kappa(I-S)\) is an additional graph/PRISM coupling between the two copies. The scalar Euclidean Laplacian on a square, with its usual domain and interface conditions, is not asserted to equal \(L_{\rm bi}\). A continuous square realization requires a separately specified quadratic form and transmission/coupling law.

## 3. Exact numerical identification with the RGS carrier

Use the original archived matrices \(K_0,Z_A,Z_S\in\mathbb R^{188\times188}\). The established carrier reconstruction defines
\[
Q=4Z_S^2,\qquad P_+=2Z_S^2+Z_S,
\]
chooses an orthonormal basis \(V\) of \(\operatorname{ran}P_+\), and sets \(W=2Z_AV\). The matrix \(U=(V,W)\) is an orthonormal basis of the six-dimensional carrier \(\mathcal W\).

In this basis the original-array audit gives, to numerical precision,
\[
U^TZ_SU=\frac12\begin{pmatrix}I_3&0\\0&-I_3\end{pmatrix},\qquad
U^TZ_AU=\frac12\begin{pmatrix}0&-I_3\\I_3&0\end{pmatrix},
\]
and
\[
U^TK_0U=
\begin{pmatrix}H&-\kappa I_3\\-\kappa I_3&H\end{pmatrix},
\qquad
\operatorname{spec}(H)=\{0.65,0.75,0.85\},\quad
\kappa=0.15.
\]
Apply the same orthogonal eigenbasis change of \(H\) to both sheets (which leaves the sheet-exchange matrix unchanged), and set
\[
L_\Omega=H-\kappa I_3,
\qquad \operatorname{spec}(L_\Omega)=\{0.50,0.60,0.70\}.
\]
In that common channel eigenbasis, \(L_\Omega=\operatorname{diag}(0.50,0.60,0.70)\). Define the carrier exchange involution
\[
S_{\rm RGS}=\begin{pmatrix}0&I_3\\I_3&0\end{pmatrix}
\]
in the ordered \((V,W)\) coordinates. Then the compression has the exact biverso form
\[
\boxed{
U^TK_0U=I_2\otimes L_\Omega+0.15(I_6-S_{\rm RGS}).
}
\]
In particular,
\[
[K_0|_{\mathcal W},S_{\rm RGS}]=0.
\]
and its parity restrictions are
\[
\boxed{
\operatorname{spec}(K_0|_{\mathcal W,+})=(0.5,0.6,0.7),\quad
\operatorname{spec}(K_0|_{\mathcal W,-})=(0.8,0.9,1.0).
}
\]
The parity subspaces are precisely the already reconstructed \(J_A\) and \(J_B\) triplets. Thus the observed \(0.30\) separation of the two triplets is \(2\kappa\), with \(\kappa=0.15\), in this six-dimensional effective biverso operator.

The basis map \(U:\mathbb R^2\otimes\mathbb R^3\to\mathcal W\subset\mathbb R^{188}\) is the concrete finite-dimensional intertwiner:
\[
K_0U=U L_{\rm bi}
\]
up to the measured carrier leakage (about \(1.18\times10^{-14}\) in Frobenius norm). This is stronger than a matching of spectra: it identifies the full compressed block operator and its two parity sectors.

## 4. Relation between the biverso exchange and the original half-scale pair

There are two distinct involutions on the carrier; they must not be conflated.

In the \((V,W)\) basis,
\[
S_{\rm RGS}=\begin{pmatrix}0&I\\I&0\end{pmatrix}
\]
is the biverso sheet exchange and commutes with the compressed \(K_0\). Meanwhile
\[
2U^TZ_SU=\begin{pmatrix}I&0\\0&-I\end{pmatrix}
\]
is the sheet-sign involution. They anticommute. The skew operator satisfies
\[
2U^TZ_AU=
\begin{pmatrix}0&-I\\I&0\end{pmatrix}
=S_{\rm RGS}\,(2U^TZ_SU).
\]
Consequently \(2Z_S\) and \(2Z_A\) encode the two complementary parity/sign operations on the same carrier, with the same half-scale normalization. In particular, \(Z_A,Z_S\) individually do **not** commute with \(K_0\); it is \(S_{\rm RGS}\), reconstructed as the sheet-exchange involution in the carrier, that commutes with the compressed operator.

This distinction resolves a potential confusion: the biverso parity projections \(P_\pm=(I\pm S_{\rm RGS})/2\) select the lower and upper \(K_0\) triplets, whereas the original \(Z_S\)-eigenspaces define the sheet-coordinate splitting \((V,W)\). Both are order-two structures, but they are not the same operator in the same basis.

### Numerical certificate from GitHub Actions

The focused workflow [45446809835](https://github.com/fabianleonaressi95/theorem/actions/runs/45446809835) completed successfully on the original root arrays. Its JSON artifact reports:

| Check | Residual |
|---|---:|
| Carrier basis orthogonality (Frobenius) | \(1.45\times10^{-15}\) |
| \(K_0\)-invariant carrier leakage (Frobenius) | \(1.18\times10^{-14}\) |
| Equality of the two diagonal blocks | \(8.36\times10^{-16}\) |
| Off-diagonal block versus \(-0.15I_3\) | \(4.48\times10^{-16}\) |
| Full biverso block reconstruction | \(1.02\times10^{-15}\) |
| Exchange commutator | \(1.31\times10^{-15}\) |
| Hadamard block diagonalization | \(1.09\times10^{-15}\) |
| Canonical \(Z_S\) carrier form | \(9.86\times10^{-16}\) |
| Canonical \(Z_A\) carrier form | \(7.23\times10^{-16}\) |

The two compressed parity spectra returned by the run are
\[
(0.5,0.6,0.7),\qquad(0.8,0.9,1.0),
\]
and the fitted scalar coupling is \(0.1499999999999999\). The JSON artifact is named \`t145-square-biverse-rgs-audit\` and is retained for 30 days.

## 5. What is and is not proved

| Statement | Status |
|---|---|
| Diagonal reflection exchanges the two congruent square triangles | Exact geometry |
| The reflection gives \(S^2=I\) and \(P_\pm=(I\pm S)/2\) | Exact |
| PRISM \(K_2\) coupling splits into \(L_\Omega\) and \(L_\Omega+2\kappa I\) | Exact algebra |
| The original RGS carrier compression has \(\kappa=0.15\) and the stated two triplets | Numerically verified from original arrays |
| The carrier basis map intertwines the compressed RGS operator with the biverso block | Numerically verified; leakage \(\sim1.18\times10^{-14}\) |
| The full \(188D\) operator is a two-sheet biverso product | Not claimed |
| The scalar Euclidean square Laplacian equals the PRISM biverso operator | Not claimed |
| The same derivation explains every occurrence of \(1/2\) in physics | False / not claimed |
| The physical origin of the affine \(1/2\) offset in the full \(K_0\) ladder is thereby settled | Not claimed |

## 6. Reproducibility

Run:
\`\`\`bash
python scripts/audit_t145_square_biverse_rgs.py
\`\`\`
The script loads only the original root arrays, reconstructs the carrier deterministically, and writes the JSON audit in audits/T145_SQUARE_BIVERSE_RGS_CARRIER_2026-11-24.json. It checks square reflection, carrier leakage, the biverso reconstruction, projector identities, parity spectra, and the \(Z_A,Z_S\) relations. The result is a numerical certificate for the stored arrays, not an exact-arithmetic proof of the source matrices.

## 7. Literature and relation to established mathematics

The decomposition is an instance of the standard representation-theoretic splitting for an involution: the representation of \(\mathbb Z_2\) separates into its trivial and sign representations, with orthogonal projections \((I\pm S)/2\). The graph operator is the Laplacian of a two-layer product with \(K_2\); its two branches are the \(K_2\) eigenmodes \(0\) and \(2\).

Relevant references:
1. C. Godsil and G. Royle, *Algebraic Graph Theory*, Graduate Texts in Mathematics 207, Springer, 2001, especially Chapter 14, “The Laplacian of a Graph”, pp. 279–306, DOI: 10.1007/978-1-4613-0163-9.
2. R. Merris, “Laplacian matrices of graphs: a survey,” *Linear Algebra and its Applications* 197–198 (1994), 143–176, DOI: 10.1016/0024-3795(94)90486-3.
3. J.-P. Serre, *Linear Representations of Finite Groups*, Springer, 1977, for the decomposition into irreducible representations and averaging/projector constructions.

The literature supplies the general \(\mathbb Z_2\)/\(K_2\) machinery. The new program-specific content is the measured identification of the original RGS six-dimensional carrier with this biverso block, including the numerical value \(\kappa=0.15\) and the recovered \(0.30\) spectral branch shift.
