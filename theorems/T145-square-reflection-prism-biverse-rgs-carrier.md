# T145 — Intrinsic \(\mathbb Z_2\) grading of the RGS half-scale carrier

**Date:** 24 November 2026  
**Classification:** exact algebraic consequences conditional on the archived matrix identities; numerical verification on the stored \(188\times188\) arrays.

**Correction notice.** This record supersedes the previous T145 draft. The previous draft incorrectly fitted a sheet-exchange operator to the compressed \(K_0\) blocks and reported a two-branch \(K_0\) decomposition. The intrinsic grading is instead defined by \(S=2Z_S|_{\mathcal W}\). The audit shows that \(K_0\) mixes its two sectors and does not commute with this \(S\).

## 1. Carrier and intrinsic grading

Define
\[
P_{\mathcal W}:=4Z_S^2,\qquad \mathcal W:=\operatorname{ran}P_{\mathcal W}.
\]
The archived arrays give a rank-six carrier, with \(Z_S\) eigenvalues \(+\frac12\) and \(-\frac12\), each of multiplicity three, and zero on the orthogonal complement. On the carrier,
\[
Z_S^2=\frac14P_{\mathcal W}.
\]
Set
\[
S:=2Z_S|_{\mathcal W}.
\]
Then
\[
\boxed{S=S^*,\quad S^2=I_{\mathcal W}},
\qquad
\boxed{P_\pm=\frac12(I_{\mathcal W}\pm S),\quad
\operatorname{rank}P_+=\operatorname{rank}P_-=3.}
\]
This is the intrinsic two-sheet \(\mathbb Z_2\)-graded carrier. It is not an exchange operator chosen to force \(K_0\) into biverso block form.

## 2. \(Z_A\) is odd with respect to the grading

In an orthonormal basis ordered by the \(+\frac12\) and \(-\frac12\) eigenspaces of \(Z_S\), the numerical compression has zero diagonal blocks and off-diagonal blocks whose singular values are all (1/2). After an independent orthogonal basis choice in the minus sheet, it can be written
\[
Z_A|_{\mathcal W}\simeq
\frac12\begin{pmatrix}0&-I_3\\ I_3&0\end{pmatrix}.
\]
The diagonal blocks vanish, and each cross-sheet block has Frobenius norm
\[
\left\|\frac12I_3\right\|_F=\frac{\sqrt3}{2}.
\]
Equivalently,
\[
\boxed{SZ_A+Z_AS=0\quad\text{on }\mathcal W.}
\]
Thus \(Z_S\) is the grading/sign operator, whereas \(Z_A\) is an inter-sheet odd operator.

## 3. \(K_0\) mixes the intrinsic sheets

Let \(K_{\mathcal W}=\Pi_{\mathcal W}K_0|_{\mathcal W}\). In the \(S\)-eigenbasis its cross-sheet blocks are nonzero, and
\[
\boxed{[K_{\mathcal W},S]\ne0}
\]
for the archived arrays. Therefore neither parity sector is invariant under \(K_{\mathcal W}\).

This corrects the earlier proposed formula
\[
K_{\mathcal W}=I_2\otimes L_\Omega+\kappa(I-S).
\]
That model commutes with the sheet exchange and preserves parity sectors; the actual compressed \(K_0\) does not. No \(\kappa=0.15\) two-branch decomposition, no \(0.30\) branch separation, and no \(K_0\)-intertwiner of that form are asserted. The eigenvalues of the full six-dimensional compression are (0.5,0.6,0.7,0.8,0.9,1.0). In the (Z_S)-eigenbasis its diagonal entries are not these eigenvalues: they lie approximately between (0.658) and (0.841), with nonzero cross-sheet entries. The exact compression and residuals are stored in the JSON audit.

## 4. Four distinct occurrences of one half

| Occurrence | Origin | Status |
|---|---|---|
| \(j=\frac12\) for \(U\cong\mathbb C^2\) | Spin label, \(\dim U=2j+1\) | Exact |
| \(-I\in2I\) acts on \(\operatorname{Sym}^m(U)\) as \((-1)^m\) | Central character of the binary lift | Exact |
| Eigenvalues \(\pm\frac12\) of \(Z_S|_{\mathcal W}\) | Normalization \(Z_S=S/2\) of the grading | Numerically verified |
| \(+\frac12 I\) in \(K_0=N/10+\frac12I\) | Affine spectral offset | Open; not explained here |

These are related through order-two structures, double covers and grading conventions, but they are not the same operator or the same physical mechanism.

## 5. Vesica, square, gradients, barycentres and dodecahedron

For the standard vesica of two equal circles of radius \(R\), with centre separation \(R\), the two intersection points and the two centres form two equilateral triangles sharing the centre-to-centre segment. Their union is a rhombus with angles \(60^\circ\) and \(120^\circ\), not a square.

A square can be built after an additional construction is chosen (for example, a specified inscribed square or a square erected on a specified segment), but “the square from the vesica” is not yet unique. The next links also need explicit data:
1. the four square vertices and the construction rule from the vesica;
2. the scalar/vector field, domain and boundary conditions whose gradient is used;
3. the point set and weights defining each barycentre;
4. the incidence rule mapping those points to dodecahedral vertices, edges or faces;
5. the metric/combinatorial operator on the dodecahedron;
6. the exact definition of the recovered function \(f\), including a derivation of \(1/240\), \(1/120\) and \(1/2\).

The two equilateral triangles are a sound geometric starting point, but do not alone determine these later objects. No theorem recovering \(f\) from the dodecahedron is claimed.

### Numerical certificate

The focused workflow [45449413001](https://github.com/fabianleonaressi95/theorem/actions/runs/45449413001) completed successfully on the archived root arrays. All 11 assertions passed. In particular:
- \(Z_S\) has three eigenvalues \(+1/2\), three \(-1/2\), and the remaining 182 eigenvalues are numerically zero;
- the carrier projector has trace \(6\), and \(Z_S^2-\frac14P_{\mathcal W}\) has Frobenius residual \(0\);
- \(S^2-I_{\mathcal W}\) has residual \(6.04\times10^{-15}\);
- the two \(Z_A\) cross-blocks each have Frobenius norm \(0.866025403784438\), and their singular values are \((0.5,0.5,0.5)\), with singular-value residual \(1.36\times10^{-16}\);
- the \(Z_A\) diagonal-block norms are \(1.10\times10^{-16}\) and \(2.15\times10^{-16}\);
- the \(K_0\) carrier leakage is \(1.27\times10^{-14}\), while its cross-sheet block norm is \(0.2598076211\) and its commutator with \(S\) has norm \(0.7348469228\).

The eigenvalues of the full six-dimensional compression are \(0.5,0.6,0.7,0.8,0.9,1.0\). The diagonal entries seen in the \(Z_S\)-eigenbasis lie approximately between \(0.658\) and \(0.841\); they are not the eigenvalues of the compression. The JSON artifact is retained for 30 days.

## 6. Reproducibility

Run:
~~~bash
python scripts/audit_t145_square_biverse_rgs.py
~~~
The script uses the original \(Z_S\) eigenspaces, ordered \(+\frac12\) then \(-\frac12\), and checks the rank-six carrier, \(S^2=I\), the ranks of \(P_\pm\), the off-diagonal structure and \(\sqrt3/2\) norm of \(Z_A\), and the cross-sheet blocks and commutator of \(K_0\). It writes results/json/rgs_intrinsic_z2_carrier_audit_2026-11-24.json. This is a floating-point verification of archived arrays, not an exact-arithmetic proof about their provenance.

## 7. McKay, the central involution and T144

For \(2I\subset SU(2)\), the defining representation \(U\cong\mathbb C^2\) has spin \(j=\frac12\). The central element \(-I\in2I\) acts on \(\operatorname{Sym}^m(U)\) by \((-1)^m\). This is the canonical central \(\mathbb Z_2\) parity of the binary lift \(2I\to A_5\). It is a representation-theoretic two-sector grading, but acts on symmetric powers of \(U\), not automatically on the RGS carrier.

The McKay graph of \(2I\) is affine \(E_8\). The Coxeter number of \(E_8\) is \(30\); the period-30 recurrence in T144 is an arithmetic consequence of the Molien/Hilbert denominator and cumulative counting formula. Period \(30\) and central parity are different structures and must not be conflated.

T144 compares the odd-degree cumulative invariant count with
\[
f(m)=\frac{m^2}{240}+\frac{m}{120}+\frac12.
\]
Its nonconstant coefficients have the stated arithmetic correspondence; its constant \(1/2\) remains unexplained in T144. The present grading result supplies no derivation of that constant.

**References.** J.-P. Serre, *Linear Representations of Finite Groups*, Springer (1977); C. Godsil and G. Royle, *Algebraic Graph Theory*, GTM 207, Springer (2001); repository record theorems/spectral/mckay_affine_e8_binary_icosahedral.md.
