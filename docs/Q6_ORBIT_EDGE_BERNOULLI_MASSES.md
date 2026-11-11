# Q6 D4 orbit graph: geometric edge masses and Bernoulli moments

**Status:** exact construction at the metric-graph (1-skeleton) level. This is a geometry-derived mass construction for the 256-edge D4 orbit graph, not yet a full two-dimensional Bernoulli–Hodge discretization.

## 1. Euclidean realization

Embed each six-bit label as its coordinate vector in [0,1]^6. The D4 orbit graph has 64 vertices and 256 unoriented edges. In this embedding the orbit-edge directions have squared Euclidean lengths 1 or 2.

The construction is metric-graph finite elements on the actual orbit edges, rather than an assumed planar realization of every cyclic square boundary.

## 2. Degree-zero mass

On an edge of length L, use the linear nodal basis. Its exact consistent local mass matrix is

\[
M_e^{(0)}=\frac L6
\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]

Assemble these local matrices over the 256 orbit edges to obtain W0 in M64(Q(sqrt(2))). For a nodal vector u, the local energy is

\[
u_e^TM_e^{(0)}u_e=\frac L3(u_0^2+u_0u_1+u_1^2)>0
\]

unless both endpoint values vanish. Since every vertex is incident to orbit edges, the assembled matrix is symmetric positive definite.

## 3. Degree-one mass

Represent an edge cochain by the integral of a constant 1-form along the edge. If its value is a_e, the tangential coefficient is a_e/L, so

\[
\int_e |a_e/L|^2\,ds=\frac{a_e^2}{L}.
\]

Thus W1 is diagonal, with entries 1 for unit edges and sqrt(2)/2 for edges of length sqrt(2). Both W0 and W1 are exact over Q(sqrt(2)).

## 4. Bernoulli moments along an edge

Parametrize an edge by arclength centred at its midpoint:

\[
x=c+Lt,\qquad t\in[-1/2,1/2].
\]

For normalized uniform measure,

\[
\mathbb E[t^{2r}]=\frac{1}{2^{2r}(2r+1)},\qquad
\mathbb E[t^{2r+1}]=0.
\]

The moment-generating function and its cumulant generating function are

\[
M(z)=\frac{\sinh(z/2)}{z/2},\qquad
\log M(z)=\sum_{r\geq1}\frac{B_{2r}}{2r(2r)!}z^{2r}.
\]

The first cumulants are kappa2=1/12, kappa4=-1/120, kappa6=1/252 and kappa8=-1/240. For a physical edge, order-2r moments and cumulants scale by L^(2r).

These are exact segment moment data for every edge in the orbit graph. They do not assert that a general orbit square has a product-parallelepiped moment law.

## 5. Why no face mass is claimed yet

The cyclic square boundaries in the orbit complex are combinatorial 2-cells. Under the six-bit-to-cube embedding, their four vertices need not form a planar Euclidean square or parallelogram. Assigning a Euclidean area, a 2-form mass, or a two-dimensional Bernoulli tensor without specifying a geometric filling would introduce an unsupported assumption.

Accordingly, this construction stops at the metric graph. A full weighted 2-complex requires an explicit choice and audit of each face realization (for example, a planar polygonal filling or a chosen triangulation), together with compatible pullbacks and face mass matrices.

## 6. Reproducibility

Run the following commands:

    python audits/audit_q6_orbit_edge_moments.py
    pytest -q tests/test_q6_orbit_edge_moments.py

The audit uses the canonical Q6 vertex/edge ordering and constructs the D4 orbit independently. It records exact lengths, W0, W1, and segment moments/cumulants. It intentionally does not claim W2, a weighted 2D Hodge spectrum, or Mosco convergence.
