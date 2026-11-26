# Nine-to-three reduction from the three-channel pointwise algebra

**Date:** 24 November 2026  
**Classification:** exact algebraic construction; lossy quotient of the 64-state space; RGS dynamical intertwining remains open.

## 1. Why an extra structure is needed

The nine-dimensional paired moment space is
\[
V_3\otimes V_3,\qquad V_3=\operatorname{span}(f_0,f_+,f_-),
\]
with reflection \(D=\operatorname{diag}(1,1,-1)\) on each factor. The physical Minkowski reflection acts diagonally, hence as \(D\otimes D\).

Reflection equivariance alone does not select a unique map \(V_3\otimes V_3\to V_3\). Under the diagonal \(\mathbb Z_2\), the source has parity dimensions \((5,4)\) and the target \((2,1)\); therefore the space of equivariant linear maps has dimension
\[
2\cdot5+1\cdot4=14.
\]
A reduction must use additional structure.

## 2. The additional structure: pointwise multiplication on the three marked channels

In the labelled basis \((e_-,e_0,e_+)\), equip the channels with the pointwise algebra
\[
(x_-,x_0,x_+)\cdot(y_-,y_0,y_+)
=(x_-y_-,x_0y_0,x_+y_+).
\]
The reflection swaps \(e_-\leftrightarrow e_+\) and fixes \(e_0\), and is an algebra automorphism.

Use the orthonormal reflection-adapted basis
\[
f_0=e_0,\qquad f_+=(e_-+e_+)/\sqrt2,\qquad
f_-=(e_--e_+)/\sqrt2.
\]
In this basis the reflection is \(D\). Transporting pointwise multiplication to this basis gives the bilinear map
\[
\mu:V_3\otimes V_3\to V_3
\]
with matrix (columns ordered lexicographically as \(00,0+,0-,+0,++,+-,-0,-+,--\)):
\[
M=\begin{pmatrix}
1&0&0&0&0&0&0&0&0\\
0&0&0&0&1/\sqrt2&0&0&0&1/\sqrt2\\
0&0&0&0&0&1/\sqrt2&0&1/\sqrt2&0
\end{pmatrix}.
\]
It has rank three, \(MM^T=I_3\), and
\[
\boxed{M(D\otimes D)=DM.}
\]
Thus this is a natural nine-to-three map for the single diagonal spacetime reflection.

It does not intertwine either independent factor flip with the same target action \(D\). That is consistent with the geometry: the two independent flips are abstract product-space symmetries, while only their diagonal product is the one ambient Minkowski reflection.

## 3. Composition with the eight-sample moment map

With the already constructed trigram moment map \(C:\mathbb R^8\to V_3\), define
\[
T=M(C\otimes C):\mathbb R^{64}\to V_3.
\]
The composite has rank three and kernel dimension 61. On the 64 standard basis states, its images fall into **23 distinct vectors**, with collision multiplicities:
- 2 classes of size 1;
- 12 classes of size 2;
- 2 classes of size 3;
- 6 classes of size 4;
- 1 class of size 8.

Therefore this nine-to-three quotient is not a lossless encoding of the 64 hexagrams. The complete image vector and collision-class table is stored in results/json/vesica_hexagram_9_to_3_algebra_reduction_2026-11-24.json.

The correct data architecture is consequently:
- retain all 64 labelled states and their nine-component \(C\otimes C\) features as the lossless labelled lookup;
- use \(M\) only as a derived three-channel algebraic observable/quotient;
- never replace the 64-state table by the 3-vector quotient.

## 4. Comparison with the RGS half-scale carrier

The target of \(M\) carries exactly the reflection involution \(D\) found in the RGS half-scale carrier. The original 188D arrays independently give the gauged blocks
\[
Z_A^{BA}=+\tfrac12D,\qquad Z_S^{BA}=-\tfrac12D.
\]
The present construction therefore matches the channel parity structure of the RGS block.

It does not derive the coefficient \(1/2\), and it does not define an operator on the full RGS 188D space. In particular, it does not yet intertwine \(K_0,Z_A,Z_S\). The simple-spectrum obstruction previously found for nontrivial \(C_3\) actions remains in force. The full dynamical bridge is still open.

## 5. Reproducibility

Run from the repository root:
    python audits/audit_vesica_hexagram_9_to_3_algebra_reduction.py

The audit checks the parity basis, coisometry, diagonal-reflection equivariance, failure of the two independent factor flips with target \(D\), rank, kernel dimension, and all 64 collision classes.

**Conclusion:** a natural algebraic nine-to-three map exists once pointwise multiplication on the three marked channels is supplied. It is a lossy quotient, not a canonical consequence of reflection alone and not yet an RGS operator intertwiner.


## Subsequent operator test: this is not the preferred RGS quotient

The pointwise multiplication map M above is a valid algebra homomorphism and diagonal-reflection intertwiner, but it is not an invariant quotient for the Q6 Laplacian compressed to the nine-dimensional moment sector. Its Laplacian leakage is nonzero (Frobenius norm 2). It must therefore remain classified as an algebraic quotient, not the operator-derived Q6–RGS reduction.

The later construction in research/Q6_VESICA_RGS_SPECTRAL_INTERTWINER_2026-11-24.md replaces it for the RGS bridge: it uses the invariant symmetric one-excitation subspace E of the Q6-compressed Laplacian and the coisometry F=E^T(C_Q tensor C_Q). This F intertwines the Q6 Laplacian and the diagonal reflection, and matches the RGS channel involution D.
