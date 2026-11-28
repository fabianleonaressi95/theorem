# T166 — Q6 vertex-link obstruction to a direct PL 4-manifold assembly

**Status:** exact combinatorial obstruction for the unmodified Q6 4-skeleton. This does not rule out a different, fully specified resolution; it proves that the 160 local three-branch replacements and their edge-level spin signs are not, by themselves, a global PL-manifold construction.

## 1. Complex being audited

Let (I^6=[0,1]^6), and let (K=I^6_{(4)}) be its cubical 4-skeleton: all coordinate faces of dimension at most four, with their ordinary face identifications.

The number of coordinate 4-cells is
\[
\binom64 2^{6-4}=15\cdot4=60.
\]
The number of coordinate 3-faces is
\[
\binom63 2^{6-3}=20\cdot8=160.
\]
Each coordinate 3-face is incident to three coordinate 4-faces, obtained by freeing one of its three fixed coordinates. These are the 60/160 counts used in T163–T164.

## 2. Link at any cube vertex

Fix a vertex (v\in I^6). Exactly one of the six coordinate directions points from (v) into the cube. The link of (v) in the full cube is the 5-simplex on those six directions.

A (k)-simplex in the link corresponds to a ((k+1))-dimensional cube face through (v). Since (K) contains faces only through dimension four, its vertex link is precisely
\[
\operatorname{Lk}_K(v)=\big(\Delta^5\big)^{(3)},
\]
the 3-skeleton of the 5-simplex, not its boundary.

Its face numbers are
\[
(f_0,f_1,f_2,f_3)=
\left(\binom61,\binom62,\binom63,\binom64\right)
=(6,15,20,15).
\]
Thus
\[
\chi(\operatorname{Lk}_K(v))=6-15+20-15=-4.
\]

## 3. Exact homology of the link

The full simplex (Delta^5) is contractible. Its simplicial chain complex is exact in positive degrees. Truncating it above degree three removes the (C_4\to C_3) boundary map, so
\[
H_3\left((\Delta^5)^{(3)};\mathbb Z\right)
=\ker(\partial_3:C_3\to C_2).
\]
In the full simplex, (ker\partial_3=\operatorname{im}\partial_4). The group (C_4) has rank six (one 4-face for each omitted vertex), and (partial_5:C_5\to C_4) is injective of rank one. Exactness therefore gives
\[
\operatorname{rank}\operatorname{im}\partial_4=6-1=5,
\qquad
H_3(\operatorname{Lk}_K(v);\mathbb Z)\cong\mathbb Z^5.
\]
The link is connected and has no other reduced homology. In particular it is not (S^3), for which (H_3(S^3;\mathbb Z)\cong\mathbb Z).

A vertex of a closed PL 4-manifold must have link PL-homeomorphic to (S^3); for a manifold with boundary the link must be a 3-ball. The link above is neither. Hence the unmodified Q6 cubical 4-skeleton is not a PL 4-manifold at its cube vertices.

## 4. Consequence for T164's three-sector replacement

T164 resolves each triple 3-face locally by replacing its transverse three-branch incidence with three pairwise interfaces around a 2D core. T164's 160 independent (mathbb Z_2) lift-sign assignments close the spin products on the pairwise-interface graph.

Neither fact changes the vertex-link calculation unless the construction also specifies how the replacement modifies and subdivides the links at every lower-dimensional intersection. In particular:

- a barycentric subdivision alone cannot help: it preserves the underlying PL homeomorphism type and therefore preserves the non-manifold obstruction;
- resolving the 160 triple faces independently is insufficient, because several such faces meet at lower-dimensional cells and their induced link patches must themselves assemble into (S^3) (or a 3-ball at a boundary vertex);
- the local (mathbb R^{1,1}\times D^2) model proves a valid local junction, not a global triangulation.

## 5. Required next construction

A valid global resolution must give, explicitly:

1. a new cell/triangulated complex (K') and a subdivision map on each of the 60 original 4-cells;
2. compatible induced subdivisions on every shared 3-, 2-, 1- and 0-cell;
3. a complete list or algorithm for all vertex links of (K'), with homology and PL-sphere/ball certification;
4. an orientation and (SL(2,mathbb C)) transition assignment on the new 3D interfaces, satisfying inverse-edge and cocycle conditions;
5. only then, the independent Cartan coframe and connection on (K').

The link audit must be rerun on (K'); the old link (mathbb Z^5) is a baseline obstruction, not a claim about a yet-unconstructed (K').

## 6. Classification

- **PROVED EXACTLY:** the raw 4-skeleton has 60 four-cells and 160 triple 3-faces; every cube-vertex link is the 3-skeleton of (Delta^5) with (H_3\cong\mathbb Z^5).
- **PROVED EXACTLY:** the raw complex is not a PL 4-manifold at its vertices.
- **NOT REFUTED:** existence of a different global PL resolution after additional compatible cell modifications.
- **OPEN:** explicit global (K'), its vertex-link certificates, global spin structure, Lorentzian Cartan fields and convergence.

This theorem deliberately separates the exact obstruction from the still-open construction.