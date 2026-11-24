# T146 — Dodecahedral dual-face barycentres lifted into Q6: exact incidence and spectral obstruction

**Date:** 24 November 2026  
**Classification:** exact finite incidence construction + antipodal-equivariant Q6 barycentre lift + reproducible numerical operator audit.  
**Result:** the canonical constructions tested here do **not** produce the Q6 selected spectrum \(0,4,6\), and do not derive \(f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}\).

## 1. Dual dodecahedron from the T139 icosahedron

Use the fixed twelve-vertex ordering of T139 at
\[
t=\psi_{\rm sg},\qquad \psi_{\rm sg}^3-\psi_{\rm sg}^2-1=0.
\]
The convex hull has 20 triangular facets. The polar dual has one vertex for each icosahedral facet, hence 20 vertices. Two dual vertices are adjacent precisely when their icosahedral facets share an edge. This gives 30 dual edges and a cubic graph.

If a triangular facet \(f\) has outward supporting-plane equation
\[
n_f\cdot x+c_f=0,\qquad n_f\cdot x+c_f\le0
\]
on the icosahedron, its polar-dual vertex is
\[
y_f=\frac{n_f}{-c_f}.
\]
This fixes the scale and the polar convention; no post-hoc rescaling is used.

## 2. Antipodal face map

Let \(\bar v\) be the antipodal vertex of \(v\) in the T139 ordering. For a triangular face \(f=\{v_1,v_2,v_3\}\), define
\[
\bar f=\{\bar v_1,\bar v_2,\bar v_3\}.
\]
The resulting map on the 20 dual vertices is an involution and an automorphism of the 30-edge dual graph.

## 3. Q6 barycentre lift

Use exactly the T141 vertex codes
\[
\iota=(3,5,58,60,9,17,46,54,33,6,57,30).
\]
Let \(e_g\) denote the standard basis of \(\mathbb R^{64}\), indexed by the Q6 states. For each dodecahedral vertex \(f\), corresponding to an icosahedral triangle \(\{v_1,v_2,v_3\}\), define its Q6 barycentre
\[
b_f=\frac13\left(e_{\iota(v_1)}+e_{\iota(v_2)}+e_{\iota(v_3)}\right).
\]
Collect these row vectors in \(B\in\mathbb R^{20\times64}\). Then
\[
B\mathbf1_{64}=\mathbf1_{20},\qquad
B_{\bar f,:}=B_{f,:}J_6,
\]
where \(J_6 e_g=e_{g\oplus63}\). These identities are checked exactly up to floating-point representation (zero residual in the archived run). The row map has rank 12.

This is a barycentric lift into the Q6 vertex-function space. It is not an edge embedding: T141's path lifts remain path-valued and the icosahedral face boundaries are not claimed to map to Q6 2-cells.

## 4. Two independently specified Dirichlet operators

### 4.1 Q6-pulled-back energy

Let \(L_6\) be the unweighted combinatorial Laplacian of the six-cube. Define
\[
\boxed{L_{\rm pull}=B L_6 B^T.}
\]
This is the canonical pullback of the Q6 Dirichlet form through the declared barycentre map:
\[
u^T L_{\rm pull}u=(B^Tu)^T L_6(B^Tu)\ge0.
\]
No edge weights are fitted. The operator is positive semidefinite, has rank 12 and nullity 8. Its spectrum, with multiplicity, is
\[
\begin{aligned}
&0^{(8)},\\
&0.351909363333614^{(3)},\\
&2^{(5)},\\
&6.31475730333305^{(3)},\\
&10^{(1)}.
\end{aligned}
\]
In particular, it does not contain the selected Q6 eigenvalue triple \((0,4,6)\).

### 4.2 Polar-dual metric Laplacian

For each dual edge \(\{f,g\}\), use the actual polar-dual Euclidean length
\[
\ell_{fg}=\|y_f-y_g\|,\qquad w_{fg}=\ell_{fg}^{-2},
\]
and set
\[
L_{\rm pol}=\operatorname{diag}(W\mathbf1)-W.
\]
At \(t=\psi_{\rm sg}\), the edge-length classes are
\[
0.4335131439\quad(6\text{ edges}),\qquad
0.5260629999\quad(24\text{ edges}).
\]
The resulting spectrum is
\[
\begin{aligned}
0,\;&2.9633975573^{(3)},\;7.2269405352^{(2)},\;
8.1527205510^{(3)},\\
&10.8404108027,\;11.9525963777^{(3)},\;
18.0673513379,\\
&20.5566847418^{(3)},\;21.0203518930^{(3)}.
\end{aligned}
\]
This is a geometrically defined metric operator, but it also does not have eigenvalues \(0,4,6\).

For comparison, the unweighted dodecahedral graph Laplacian has spectrum
\[
0,\;(3-\sqrt5)^{(3)},\;2^{(5)},\;3^{(4)},\;5^{(4)},\;(3+\sqrt5)^{(3)}.
\]

## 5. Direct test against the selected Q6 sector

Let \(F:\mathbb R^{64}\to\mathbb R^3\) be the archived Q6 coisometry with
\[
F L_6=\Lambda F,\qquad \Lambda=\operatorname{diag}(0,4,6).
\]
The dodecahedron-to-sector map is
\[
\Phi=F B^T\in\mathbb R^{3\times20}.
\]
It has rank 3. The decisive intertwining test is
\[
\Lambda\Phi\stackrel{?}{=}\Phi L_{\rm pull}.
\]
The Frobenius residual is
\[
\boxed{\|\Lambda\Phi-\Phi L_{\rm pull}\|_F
=5.709918966428033,}
\]
whereas the independent Q6 identity \(FL_6-\Lambda F=0\) has residual \(7.73\times10^{-16}\). Thus the Q6 sector itself is correctly reconstructed, but the barycentric dodecahedral pullback does not intertwine with it.

The distinction matters: \(F L_6=\Lambda F\) is an identity on Q6; it does not imply that the compressed dodecahedral operator \(B L_6 B^T\) is intertwined by \(F B^T\). The latter requires an additional compatibility of the face-barycentre map with the selected invariant subspace, and this test fails for the T141 assignment.

## 6. What is now established, and what remains open

**Established:**
1. the 20-vertex/30-edge polar-dual incidence structure;
2. its antipodal involution and graph equivariance;
3. the T141-compatible Q6 face-barycentre map \(B\);
4. the Q6-pulled-back positive energy \(B L_6 B^T\);
5. the polar-dual inverse-square metric Laplacian;
6. the numerical spectra and failed selected-sector intertwining test.

**Not established:**
- a chain map on 2-cells or a compatible Q6 face-boundary filling;
- a dodecahedral discrete gradient whose adjoint yields the selected Q6 operator;
- an intertwiner with spectrum \(0,4,6\);
- a derivation of \(1/240\), \(1/120\), or \(1/2\) from the dodecahedral geometry;
- a first-principles dodecahedral derivation of \(f\).

The failure is informative rather than terminal: it rules out the simplest equal-face-barycentre lift with either the Q6-pulled-back energy or the polar-dual inverse-square metric. The next construction must add independently justified face-frame transport or a compatible discrete de Rham/FEEC complex. It must not tune edge weights merely to force \(0,4,6\).

## 7. Reproduction

Run:
\`\`\`bash
python scripts/audit_t146_dodecahedron_q6_dual_barycentre.py
python -m unittest tests.test_t146_dodecahedron_q6_dual_barycentre
\`\`\`

Workflow: [T146 dodecahedron–Q6 audit](https://github.com/fabianleonaressi95/theorem/actions/runs/45450509876). All 11 structural assertions and both regression tests pass. The JSON artifact is retained for 30 days at
\`results/json/dodecahedron_q6_dual_barycentre_audit_2026-11-24.json\`.

**Status label:** exact incidence and equivariant barycentre lift; numerical operator obstruction for the canonical choices tested. The geometric derivation of \(f\) remains open.
