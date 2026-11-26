# D4-Reynolds weighted Hodge operator on Q6

**Status:** exact assembly algorithm and tests added; execution pending. No eigenvalues are claimed.

## 1. Why a Reynolds average is needed

The six-bit embedding in Euclidean R^6 is a convenient geometric realization,
but the stated D4 generators include a Boolean XOR coordinate. They are
permutations of the 64 vertices, not automatically Euclidean isometries.
Consequently the raw edge lengths and face areas cannot simply be declared
D4-invariant.

Starting from the positive geometric masses W0_raw, W1_raw and W2_raw, define
for each degree k the Reynolds average

\[
\overline W_k=\frac1{|D_4|}\sum_{g\in D_4}P_k(g)^T
W_{k,\mathrm{raw}}P_k(g).
\]

Every average is positive definite because it is an average of positive
definite matrices. It is D4-invariant by reindexing the finite group sum.
For diagonal W1 and W2, the signed orientation factors square to one.

## 2. Geometric input masses

- W0_raw is assembled from P1 edge masses
  \(L_e/6\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\).
- W1_raw is diagonal, with \((W_1)_{ee}=1/L_e\), for constant Whitney
  1-form coefficients on each straight edge.
- W2_raw is diagonal on the selected nondegenerate parallelogram faces,
  with \((W_2)_{FF}=1/A_F\), for one constant integrated 2-form flux per face.

Only complete D4-orbits for which every face is a nondegenerate parallelogram are included. This orbit-closure condition is essential: the Boolean-coordinate action is not automatically affine in the ambient Euclidean embedding, so selecting individual parallelograms could break equivariance.

## 3. Correct weighted Hodge formulation

Let B1:C1->C0 and B2:C2_adm->C1 be the boundary matrices. The coboundary
operators are D0=B1^T and D1=B2^T. With inner products W0,W1,W2, the
degree-one stiffness matrix is

\[
K_1=D_0^T W_0D_0+D_1^T W_2D_1
=B_1^TW_0B_1+B_2W_2B_2^T.
\]

The self-adjoint degree-one Hodge operator is represented by the generalized
eigenproblem

\[
\boxed{K_1x=\lambda W_1x.}
\]

This is the symmetric formulation. In particular, W1 must not be inserted
on only one side of the second stiffness term. This note supersedes any
preliminary nonsymmetric expression of that type.

## 4. Exact checks

The audit first partitions the 384 cycles into D4-orbits and retains only complete orbits whose every member is a nondegenerate parallelogram. It then constructs the Reynolds masses and K1 using SymPy exact arithmetic.
It checks:

- B1 B2=0;
- exact D4 invariance of each averaged mass;
- equivariance of the oriented incidence;
- symmetry of K1;
- positivity of W1 and W2, and positivity of W0 by its P1 assembly and
  connected orbit graph.

The full spectrum is deliberately not computed or claimed in this change.
The next numerical stage should solve the symmetric conjugate problem
\(W_1^{-1/2}K_1W_1^{-1/2}\), while preserving an exact rank/Betti audit.

## 5. Bernoulli continuation

Bernoulli corrections should be introduced only after moments of the actual
parallelogram face measure and the chosen face quadrature are specified.
For a perturbation Wk(epsilon)=Wk(0)+epsilon^(2r) Ck, positivity holds for
sufficiently small epsilon whenever Wk(0) is positive definite and Ck is
bounded symmetric. The topological Betti number is unchanged as long as
incidence is unchanged and the masses remain positive definite; eigenvalues
may move.

## Reproduction

    python audits/audit_q6_reynolds_weighted_hodge.py
    pytest -q tests/test_q6_reynolds_weighted_hodge.py
