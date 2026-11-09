# T056 — Permutation conjugacy of the Phase 21 and trigram supergolden matrices

**Status:** exact finite-dimensional algebraic identity.  
**Scope:** equivalence of two explicitly displayed \(3\times3\) matrices under a change of state ordering. This is not a geometric subdivision theorem.

## 1. Matrices

The Phase 21 symbolic transfer model uses
\[
A_\psi=\begin{pmatrix}
1&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}.
\]
The trigram three-channel programme uses the target matrix
\[
M_T=\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&1
\end{pmatrix}.
\]
Define the permutation matrix
\[
P=\begin{pmatrix}
0&1&0\\
0&0&1\\
1&0&0
\end{pmatrix}.
\]
Then
\[
P^{-1}=P^T,\qquad P^TP=I,\qquad P^3=I.
\]

## 2. Theorem

The two transfer matrices are permutation-conjugate:
\[
\boxed{M_T=P A_\psi P^{-1}.}
\]
Consequently they have the same characteristic polynomial,
\[
\boxed{\det(\lambda I-A_\psi)
=\det(\lambda I-M_T)
=\lambda^3-\lambda^2-1.}
\]
Their spectra and spectral radii therefore agree. In particular, the positive Perron root is
\[
\psi=1.465571231876768\ldots.
\]

## 3. Proof

Direct multiplication gives
\[
P A_\psi P^T
=\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&1
\end{pmatrix}
=M_T.
\]
Since \(P^{-1}=P^T\), this is a similarity transformation. Similar matrices have identical characteristic polynomials and spectra. Expanding the determinant of either matrix gives \(\lambda^3-\lambda^2-1\). \(\square\)

## 4. Interpretation and non-conclusions

This identity resolves a matrix-ordering discrepancy between the existing Phase 21 model and the trigram target: they encode the same finite-dimensional linear dynamics after a cyclic relabeling of the three states.

It does **not** identify the Phase 21 states with the lower, middle and upper trigram lines. It does not construct an intertwiner between Cantor branches, Q6 cells, Kathara cells and Krist-All cells. In particular, it is not evidence that the geometric refinement operator has been derived.

The actual oriented cubical midpoint subdivision of Q6 is a separate construction recorded in T055. The missing Kathara/Krist-All geometric parent-to-child map remains open.

The implementation-level exact matrix audit is maintained in the companion repository:
https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/TRIGRAM_KRISTALL_SUPERGOLDEN_CROSSWALK.md.
