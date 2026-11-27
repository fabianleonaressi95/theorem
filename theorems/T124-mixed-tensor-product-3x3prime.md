# T124 — Mixed tensor product of the two icosahedral three-dimensional modules

**Status:** character-theoretic decomposition proved; an exact-arithmetic 9×9 matrix audit has now been added, but its execution result is not yet certified in this PR.
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

## Matrix realization and verification boundary

The companion audit `audits/t124_mixed_tensor_character_check.py` now constructs exact bases from the columns of the T121 projectors, computes the restricted 3×3 matrices for all 60 group elements, forms the 9×9 Kronecker-product action, and constructs the central projectors P4 and P5. It is designed to check the representation laws, invariance, idempotence, mutual orthogonality, completeness, ranks 4 and 5, and centrality.

The T121 audit now exports the signed actions and conjugacy-class membership as an exact data interface for this downstream calculation. The matrix audit has been committed but has **not yet been executed in this environment**; therefore its checks are implementation assertions, not a reported passing test run. Run `python audits/t124_mixed_tensor_character_check.py` from the repository root before promoting this PR from draft. The character identity above independently proves the decomposition, conditional only on the T121 identification of the two three-dimensional irreducibles.

T123 is intentionally untouched.
