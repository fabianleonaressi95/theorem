# Q6 D4 orbit: exact W2 on admissible parallelogram faces

**Status:** exact construction and tests added; execution remains pending.

## 1. Scope

The full D4 orbit contains 384 distinct cyclic 2-cell boundaries. We do not
assume that every cycle is a Euclidean square or even a planar polygon.

This construction assigns a face metric only to the subfamily that is a
nondegenerate parallelogram in the canonical embedding of the six-bit vertices
in Euclidean R^6. Such a face is planar and simple by construction.

## 2. Exact admissibility criterion

For the ordered cycle F=(v0,v1,v2,v3), with coordinates x_i in {0,1}^6,
require

\[
x_0+x_2=x_1+x_3
\]

and require the area bivector to be nonzero. Set u=x_1-x_0 and v=x_3-x_0.
Then

\[
A_F^2=\lVert u\wedge v\rVert^2
=\sum_{1\leq i<j\leq6}(u_iv_j-u_jv_i)^2>0.
\]

All tests and A_F^2 are exact integer calculations.

## 3. Face space and mass convention

On each admissible face use one constant integrated 2-form degree of freedom.
If its coefficient is the total flux a_F, its constant density is a_F/A_F.
Its squared L2 norm is

\[
\int_F |a_F/A_F|^2\,dA=a_F^2/A_F.
\]

Therefore the local mass is exactly

\[
(W_2)_{FF}=1/A_F=1/\sqrt{A_F^2}.
\]

With one independent degree of freedom per admissible face, W2 is diagonal
and positive definite. This is a declared lowest-order face model; it is not
the Whitney mass matrix for an arbitrary triangulated nonplanar surface.

## 4. Incidence and chain identity

The audit assembles the 64-by-256 vertex-edge boundary B1 and the
256-by-m admissible-edge-face boundary B2. It verifies exactly

\[
B_1B_2=0.
\]

Thus the selected faces form a valid 2-chain family with the inherited
oriented boundaries. The metric W2 does not alter this identity.

## 5. Hodge operator available after this construction

Together with positive W0 and W1 from the orbit metric-graph construction,
the degree-one stiffness is

\[
K_1=B_1^T W_0 B_1+W_1 B_2 W_2 B_2^T,
\]

and the degree-one weighted Laplacian is

\[
\Delta_1=W_1^{-1}K_1.
\]

This formula is valid for the selected face subcomplex, provided W0 and W1
are the positive matrices on the same 64 vertices and 256 orbit edges.
The audit here constructs B1, B2 and W2; it does not yet assemble the full
weighted Hodge spectrum.

## 6. Bernoulli boundary

No Bernoulli correction is inserted into W2 by analogy. The exact face
covariance and higher moments must first be computed on each actual
parallelogram, then a specified face quadrature must produce the correction.
The current W2 is the geometric base mass.

## 7. Reproduction

    python audits/audit_q6_admissible_face_w2.py
    pytest -q tests/test_q6_admissible_face_w2.py

The audit reports the exact number of admissible faces, rejected categories,
area-squared values, exact chain closure, and the W2 diagonal.
