# T139 — Convex-hull audit of the supergolden icosahedral deformation

**Status:** [N] reproducible numerical construction for the specified parameter; [P] combinatorial identities conditional on the computed hull; [O] canonical lift to Q6 and a geometrically derived mixing operator. This record does not assert a new regular icosahedron or a physical PSU–Anti-Twin coupling.

## 1. Vertex set

For a real parameter \(t>1\), define the twelve points
\[
P_t=\operatorname{conv}\{(0,\pm1,\pm t),\ (\pm1,\pm t,0),\ (\pm t,0,\pm1)\}.
\]
The parameter used here is the positive supergolden root
\[
t=\psi_{\rm sg},\qquad \psi_{\rm sg}^3-\psi_{\rm sg}^2-1=0,
\qquad \psi_{\rm sg}\simeq1.465571231876768.
\]
The control value is \(t=\varphi=(1+\sqrt5)/2\). At \(t=\varphi\), the same coordinate construction is the regular icosahedron.

The RenderHub wireframe model linked in the research discussion is retained as a **visual reference only**: [Wireframe Icosahedron — MRAnyCAD](https://www.renderhub.com/mranycad/wireframe-icosahedron). Its page identifies a 7,220-vertex, 4,816-polygon downloadable model and a “Personal Use Only” licence. No model file, mesh, or image from that listing is copied into this repository. The numerical construction below is generated independently from the twelve coordinates above.

## 2. Hull construction and audit

The script constructs the convex hull from the twelve points using scipy.spatial.ConvexHull; it does not infer adjacency by selecting pairs at a guessed distance. The hull simplices generate the triangular facets, and their unique undirected edges define the 1-skeleton.

For \(t=\psi_{\rm sg}\), the reproducible numerical audit gives:

- 12 extreme vertices, 30 unique edges, 20 triangular facets;
- Euler characteristic \(12-30+20=2\);
- 24 short edges and 6 long edges;
- 8 equilateral triangular facets and 12 isosceles facets.

The two edge lengths follow directly from the coordinate differences:
\[
\ell_{\rm short}=\sqrt{2(t^2-t+1)},\qquad
\ell_{\rm long}=2.
\]
At \(t=\psi_{\rm sg}\), these are approximately \(1.8342997595\) and \(2\), respectively. The face classes found by the hull agree with the side-length patterns: 8 faces \((s,s,s)\), and 12 faces \((s,s,2)\).

The computed Euclidean surface area and volume are
\[
A(P_{\psi})\simeq30.1084330157,\qquad
\operatorname{Vol}(P_{\psi})\simeq14.1221281904.
\]
These are floating-point outputs of the specified hull construction, not exact algebraic evaluations.

For the control \(t=\varphi\), the hull has 30 equal edges of length 2 and 20 equilateral facets; its area and volume are approximately \(34.6410161514\) and \(17.4535599250\).

## 3. Metric-weighted graph Laplacian

For the hull graph \(G_t=(V,E)\), define the declared discrete Dirichlet weights
\[
w_{ij}=\ell_{ij}^{-2}\quad (\{i,j\}\in E),\qquad
w_{ij}=0\quad (\{i,j\}\notin E),
\]
and
\[
L_t=\operatorname{diag}(W\mathbf1)-W.
\]
This is one natural metric-weighted graph Laplacian; the choice \(w=\ell^{-2}\) is a modelling convention, not a uniquely forced physical law.

At \(t=\psi_{\rm sg}\), the weights are
\[
w_{\rm short}=\frac{1}{2(t^2-t+1)},\qquad
w_{\rm long}=\frac14.
\]
The numerical spectrum, including multiplicities, is
\[
0^{(1)},\quad
0.793981242^{(3)},\quad
1.68882895^{(3)},\quad
1.78324343^{(2)},\quad
2.08367666^{(3)}.
\]

Let \(J_\psi\) be the vertex antipodal permutation \(X\mapsto-X\). The hull graph, its metric weights, and \(L_\psi\) are antipodally invariant, so
\[
[L_\psi,J_\psi]=0.
\]
Consequently \(L_\psi\) preserves the \(J_\psi=\pm1\) sectors. It is **not** a sheet-mixing operator: this construction does not yield \(\{J_\psi,T\}=0\).

## 4. What this audit does not establish

1. It does not define a map from the 12 hull vertices or 30 hull edges to the 64 vertices or 192 links of Q6.
2. It does not define orientations, incidence signs, or a transport law on that map.
3. It therefore does not construct \(T_{\rm geom}\), and does not establish hermiticity, anticommutation with the Q6 antipodal involution, or any rank/spectrum comparison with \(DAD\).
4. It does not establish that the two coordinate sets at \(t=\varphi\) and \(t=\psi_{\rm sg}\) are related by a particular global linear map. Any claimed correspondence must specify the vertex permutation and test the resulting map explicitly. Groupwise coordinate relabellings are not to be silently treated as one global linear transformation.

The next mathematical input is an explicit incidence-preserving lift
\[
\iota:V(P_\psi)\sqcup E(P_\psi)\longrightarrow V(Q_6)\sqcup E(Q_6),
\]
together with orientations and transport data. Only after those data are fixed can a candidate \(T_{\rm geom}\) be assembled and tested against the Q6 involution.

## 5. Reproduction

Run:

    python scripts/audit_t139_supergolden_icosahedron.py
    python -m unittest tests.test_t139_supergolden_icosahedron

The tests verify the hull counts, edge/face classes, metric Laplacian spectrum within stated numerical tolerances, and antipodal commutation. They do not test a Q6 lift or a mixing operator.
