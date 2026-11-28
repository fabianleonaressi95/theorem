# T164 — Quaternionic resolution of the Q6 three-branch incidence

**Status:** exact local quaternionic and spin-lift identities; local PL junction model defined. Global assembly over all Q6 branch faces remains OPEN.

## 11. Vertex-link obstruction audit — T166

T166 now computes the vertex link of the unmodified cubical 4-skeleton (K=I^6_{(4)}). At every cube vertex,
\[
\operatorname{Lk}_K(v)=(\Delta^5)^{(3)},\qquad
(f_0,f_1,f_2,f_3)=(6,15,20,15),
\]
and
\[
H_3(\operatorname{Lk}_K(v);\mathbb Z)\cong\mathbb Z^5.
\]
Thus the raw 4-skeleton is not a PL 4-manifold at its vertices (the link is neither (S^3) nor a 3-ball). This is an exact obstruction, not a no-go theorem for a modified resolution.

Consequently, the 160 local wedge replacements and the 480 pairwise-interface sign assignments do not yet establish global PL gluing. A new complex (K') must specify compatible subdivisions at all lower-dimensional intersections and certify every vertex link. Ordinary barycentric subdivision alone cannot remove the obstruction because it preserves the underlying PL type. See the file theorems/T166-q6-vertex-link-pl-obstruction.md for the chain-level proof.

**Updated status:** local quaternionic junction and incidence-level spin cocycle are established; global PL 4-manifold resolution remains OPEN, with the raw vertex-link obstruction now explicitly identified.


## 12. Manifold carrier alternative — T167

T167 constructs a smooth compact 4-manifold with boundary whose handle spine is homotopy equivalent to the Q6 square 2-skeleton. It retains the 64/192/240 data and gives H1=0, H2=Z^111. This is a genuine manifold carrier for the lower-dimensional Q6 data, but the 160 triple 3-faces, 60 four-cells, T164 interface graph and quaternionic transports have not yet been lifted to it. The original 4-skeleton obstruction in T166 therefore remains valid. T167 is a candidate route for the next extension, not a closure of T164 global PL gluing.
