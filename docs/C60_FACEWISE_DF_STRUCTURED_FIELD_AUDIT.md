# C60 facewise field D_f and candidate structured field

## Purpose

This audit constructs the matrices left implicit in Appendix A.8--A.10 of
`Relazione_Morandotti.pdf`, using the exact ideal truncated icosahedron and
the face connection already implemented in
`scripts/audit_c60_icosahedral_connection.py`.

## Construction

For each face f, the script uses the oriented orthonormal tangent frame
\(B_f\in\mathbb R^{3\times2}\). The edge transport in these coordinates is
\(A_{fg}=B_g^T T_{fg}B_f\in SO(2)\).

A deterministic breadth-first spanning tree of the dual graph is rooted at
face 0. The face field is propagated by

\[
D_{f_0}=I_2,\qquad D_g=A_{fg}D_f
\]

when g is a child of f. Thus 32 explicit matrices \(D_f\in SO(2)\) are
generated. Their values depend on the root, tree and local frame gauge.

For the immersion candidate, define

\[
\nabla g|_f=B_f\in\mathbb R^{3\times2},\qquad
G_f=B_fD_f,\qquad
M_f=B_f-G_f=B_f(I_2-D_f).
\]

The script saves every D_f, G_f and M_f as NPZ arrays and a face-indexed CSV.

## Independent local checks

The program reconstructs the three faces incident to each of the 60 vertices,
orders them around the radial direction and computes the 3-face cycle holonomy.
It checks that the absolute rotation angle is 12 degrees at every vertex.
It also checks orthogonality of every D_f, the tree propagation identity,
and orthonormality of every face frame.

## Interpretation limits

This is a **candidate matrix realization**, not a proof that the pair (g,G)
is admissible in the classical Del Piero--Owen theory. Here the gradients are
3x2 because the local object is an immersion of a two-dimensional face into
R3. The classical determinant accommodation condition for square N x N
gradients therefore does not apply unchanged. Moreover, the code does not
construct a globally injective planar development or a determining sequence
of injective approximants. The distinction between a bulk M field and
distributional jump measures on cuts remains open.

## Reproduction

```bash
python scripts/audit_c60_facewise_Df.py --out-dir c60_facewise_Df
```

The workflow uploads the NPZ, CSV and JSON reports as artifacts. Numerical
claims are accepted only after inspecting the workflow result and artifacts.
