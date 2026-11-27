# T124 — Mixed tensor product of the two icosahedral three-dimensional modules

**Status:** character-theoretic decomposition proved; explicit 9×9 projector realization is pending.
**Depends on:** T121 (the exact signed-axis action of A5 on Q6 and the splitting 6 = 3 ⊕ 3′).
**Scope:** this record does not modify or subsume T123.

## Statement

Let \(V_3\) and \(V_{3'}\) be the two inequivalent three-dimensional irreducible real representations of \(A_5\) obtained in T121. Then
\[
V_3\otimes V_{3'}\cong V_4\oplus V_5,
\]
where \(V_4\) and \(V_5\) are the irreducible representations of dimensions four and five.

## Exact character verification

Order the conjugacy classes as \(1A,2A,3A,5A,5B\), with sizes
\[
(1,15,20,12,12).
\]
Write \(\phi=(1+\sqrt5)/2\) and \(\phi'=(1-\sqrt5)/2\). T121 fixes
\[
\chi_3=(3,-1,0,\phi,\phi'),\qquad
\chi_{3'}=(3,-1,0,\phi',\phi).
\]
The pointwise product is
\[
\chi_{3\otimes3'}=(9,1,0,\phi\phi',\phi'\phi)
=(9,1,0,-1,-1),
\]
since \(\phi\phi'=-1\).

The relevant irreducible characters are
\[
\chi_4=(4,0,1,-1,-1),\qquad
\chi_5=(5,1,-1,0,0).
\]
Consequently
\[
\chi_4+\chi_5=(9,1,0,-1,-1)=\chi_3\chi_{3'}.
\]
By complete reducibility and uniqueness of irreducible character decomposition, this proves the stated direct-sum decomposition, with multiplicity one for each summand. The dimension check is \(4+5=9=3\cdot3\).

## Central projectors to be realized in the T124 matrix audit

For the tensor representation \(D(g)=D_3(g)\otimes D_{3'}(g)\), the central idempotents are
\[
P_4=\frac4{60}\sum_{g\in A_5}\chi_4(g^{-1})D(g),\qquad
P_5=\frac5{60}\sum_{g\in A_5}\chi_5(g^{-1})D(g).
\]
The matrix-level audit must establish exactly
\[
P_4^2=P_4,\quad P_5^2=P_5,\quad P_4P_5=0,\quad
P_4+P_5=I_9,
\]
and \(\operatorname{rank}P_4=4\), \(\operatorname{rank}P_5=5\), together with commutation with all 60 tensor-action matrices.

## Verification boundary

The character identity above is an exact proof of the representation decomposition, conditional only on the T121 identification of the two three-dimensional irreducibles. This PR does **not** claim that the 9×9 matrices, central projectors, or their exact ranks have already been computed. Those explicit matrix checks remain a separately identifiable implementation task; they must not be reported as passed until a reproducible exact-arithmetic audit is committed and run.

T123 is intentionally untouched.
