# Q6 D4 orbit graph: geometric edge masses and Bernoulli moments

**Status:** exact metric-graph (1-skeleton) construction; not yet a full two-dimensional Bernoulli–Hodge discretization.

## Euclidean realization

Embed each six-bit label as its coordinate vector in [0,1]^6. The D4 orbit graph has 64 vertices and 256 unoriented edges. In this embedding the orbit-edge squared lengths are 1 or 2.

## Degree-zero mass

On an edge of length L, the linear nodal basis has exact consistent mass

\[
M_e^{(0)}=\frac L6\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]

Assembly over all orbit edges gives W0 in M64(Q(sqrt(2))). Each local matrix is positive definite, and every vertex is incident to an edge; hence the assembled W0 is symmetric positive definite.

## Degree-one mass

Represent an edge cochain by its integral a_e of a constant 1-form. Its tangential coefficient is a_e/L, so

\[
\int_e |a_e/L|^2\,ds=\frac{a_e^2}{L}.
\]

Thus W1 is diagonal, with entries 1 for unit edges and sqrt(2)/2 for edges of length sqrt(2). These are exact metric-graph mass matrices.

## Bernoulli moments

For arclength parameterization x=c+Lt with t uniform on [-1/2,1/2],

\[
\mathbb E[t^{2r}]=\frac{1}{2^{2r}(2r+1)},\quad
\mathbb E[t^{2r+1}]=0.
\]

The moment and cumulant generating functions are

\[
M(z)=\frac{\sinh(z/2)}{z/2},\qquad
\log M(z)=\sum_{r\geq1}\frac{B_{2r}}{2r(2r)!}z^{2r}.
\]

The first cumulants are 1/12, -1/120, 1/252 and -1/240. Physical edge moments of order 2r scale by L^(2r).

## Why W2 is not assigned

The cyclic square boundaries are combinatorial 2-cells. Their four vertices need not form planar Euclidean squares or parallelograms in the six-bit cube embedding. Assigning an area or a 2-form mass without specifying and auditing a geometric filling would add an unsupported assumption. This construction therefore stops at the metric graph.

A full 2-complex requires an explicit face realization (such as audited planar fillings or a chosen triangulation), followed by compatible face moments and W2 assembly.

## Reproduction

    python audits/audit_q6_orbit_edge_moments.py
    pytest -q tests/test_q6_orbit_edge_moments.py

The audit reports exact edge lengths, W0/W1 definitions, and segment moments/cumulants. It does not claim a full 2D Hodge spectrum or Mosco convergence.
