# T053 — Projectors from an involutive exterior-square operator

**Status:** proved under the explicit matrix hypotheses.  
**Scope:** finite-dimensional linear algebra only. No group equivariance or geometric interpretation is assumed.

## 1. Setting

Let \(V=\mathbb R^6\), let \(C_6:V\to V\) be a specified linear map, and let
\[
C_{15}=\Lambda^2 C_6:\Lambda^2V\to\Lambda^2V.
\]
The space \(\Lambda^2V\) has dimension \(\binom62=15\). In a basis indexed by ordered pairs \(i<j\), the induced matrix is
\[
(C_{15})_{[ij],[kl]}
=(C_6)_{ik}(C_6)_{jl}-(C_6)_{il}(C_6)_{jk}.
\]

## 2. Theorem

Assume that \(C_{15}\) is real symmetric and satisfies
\[
C_{15}^2=25I_{15}.
\]
Then
\[
P_\pm=\frac12\left(I_{15}\pm\frac{C_{15}}5\right)
\]
are orthogonal complementary projectors:
\[
P_\pm^2=P_\pm,\quad P_+P_-=0,\quad
P_++P_-=I_{15},\quad P_\pm^\mathsf T=P_\pm.
\]
Their ranks equal the multiplicities of the eigenvalues \(+5\) and \(-5\), respectively. In particular, if those multiplicities are 6 and 9, then
\[
\operatorname{rank}P_+=6,\qquad\operatorname{rank}P_-=9.
\]

## 3. Proof

Set \(A=C_{15}/5\). Then \(A^\mathsf T=A\) and \(A^2=I\). Direct multiplication gives
\[
\left(\frac{I\pm A}{2}\right)^2
=\frac{I\pm2A+A^2}{4}
=\frac{I\pm A}{2}.
\]
Also
\[
\frac{I+A}{2}\frac{I-A}{2}
=\frac{I-A^2}{4}=0,
\qquad
P_++P_-=I.
\]
Symmetry of \(A\) gives symmetry of both projectors. By the spectral theorem, the eigenvalues of \(A\) are \(\pm1\), and \(P_\pm\) project onto the corresponding eigenspaces. Their ranks are therefore the respective multiplicities. \(\square\)

## 4. Crucial conditional status

This theorem does **not** verify that a particular proposed \(C_6\) produces a symmetric \(C_{15}\) with \(C_{15}^2=25I\). Those are hypotheses to be checked from the exact matrix entries, preferably with exact arithmetic or certified bounds.

It also does not prove that either image is irreducible under a group action. If a representation \(\rho\) is supplied and \(P_\pm\) commute with every \(\rho(g)\), their images are invariant subspaces; irreducibility requires an additional argument (for example, character inner products or a commutant calculation).

No curvature, bundle connection, Yang–Mills field equation, or relation to the \(Q_6\) cell complex follows from this matrix lemma.

**Source:** [consolidated audit of the exploratory exterior-square PDF](../manuscripts/FOUR_PDF_CONSOLIDATED_AUDIT.md).
