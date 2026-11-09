# T062 — Explicit integral chain map from the filled Kathara complex to the Q6 2-skeleton

**Status:** proved algebraically for the explicit coordinate code and root-path construction below. This is an existence theorem for a degenerate chain map, not a cellular embedding and not a canonical RGS identification. The implementation and tests are in the companion bridge repository; their execution is not claimed by this record.

## 1. Complexes and conventions

Let \(K\) be the filled Kathara complex of T059:
\[
(C_0(K),C_1(K),C_2(K))=(\mathbb Z^{12},\mathbb Z^{21},\mathbb Z^{10}).
\]
Its vertices are numbered \(1,\ldots,12\), with integer drawing coordinates
\[
\begin{array}{c|rrrrrrrrrrrr}
v&1&2&3&4&5&6&7&8&9&10&11&12\\
\hline
(x_v,y_v)&(0,0)&(0,1)&(-2,2)&(2,2)&(0,3)&(-2,4)&(2,4)&(0,5)&(-2,6)&(2,6)&(0,7)&(0,8).
\end{array}
\]
The ten 2-cells are the bounded faces in T059. Their orientation and the orientation of the 21 edges are fixed by the incidence matrices \(B_1^K,B_2^K\).

Let \(Q_6^{(2)}\) be the canonical cubical 2-skeleton with chain groups
\[
(C_0,C_1,C_2)=(\mathbb Z^{64},\mathbb Z^{192},\mathbb Z^{240}),
\]
using integer vertex labels \(0,\ldots,63\), six-bit big-endian bit order, lexicographically oriented edges, and the standard cubical square orientations.

## 2. Coordinate code

Define \(c(-2)=0,\ c(0)=1,\ c(2)=2\), and
\[
g(v)=16c(x_v)+y_v\in\{0,\ldots,63\}.
\]
The twelve values are pairwise distinct, so this defines an injective vertex map. The code is exact and contains no floating-point threshold or nearest-neighbour choice.

It is nevertheless a chosen coordinate chart: the Kathara drawing coordinates alone do not prove that this particular encoding is selected by the RGS metric, the \(O_h\) action, or a variational principle.

## 3. Root-path chain

For \(g\in\{0,\ldots,63\}\), let \(P(g)\in C_1(Q_6;\mathbb Z)\) be the edge chain of the path from 0 to \(g\) obtained by flipping the six bits in the fixed axis order \(0,1,\ldots,5\). Orient each target edge according to the canonical Q6 convention and insert a sign when the path traverses it against that orientation. Then
\[
\partial_1P(g)=[g]-[0].
\]

For every oriented Kathara edge \(e=(u,v)\), set
\[
R_0([v])=[g(v)],\qquad
R_1(e)=P(g(v))-P(g(u)),\qquad R_2=0.
\]
In matrix form,
\[
R_0\in\mathbb Z^{64\times12},\quad
R_1\in\mathbb Z^{192\times21},\quad
R_2\in\mathbb Z^{240\times10}.
\]

## 4. Theorem: chain identities

For an oriented source edge \(e=(u,v)\),
\[
\partial_1R_1(e)
=\big([g(v)]-[0]\big)-\big([g(u)]-[0]\big)
=[g(v)]-[g(u)]
=R_0\partial_1e.
\]
By linearity,
\[
\boxed{B_1^{Q6}R_1=R_0B_1^K.}
\]

Let \(f\) be any oriented Kathara 2-cell. Its cellular boundary is a closed 1-cycle, so the sum of the edge differences \(P(g(v))-P(g(u))\) around its oriented boundary telescopes to zero. Hence
\[
R_1\partial_2f=0.
\]
Since \(R_2=0\), also \(B_2^{Q6}R_2=0\), and therefore
\[
\boxed{B_2^{Q6}R_2=R_1B_2^K.}
\]
Thus \(R=(R_0,R_1,R_2)\) is an integral chain map.

## 5. Degeneracy and limits

The map is injective on vertices, but it sends all ten source 2-cells to zero. It therefore does **not** define a cellular embedding of the Kathara disk into \(Q_6^{(2)}\), does not preserve its face geometry, and cannot be used as a nondegenerate area/Hodge/Krist-All lift.

The implementation additionally retains the 15 primary-line membership data and pulls back the hash-checked RGS coordinates \(X_{g(v)}\). This records the RGS geometry at the chosen labels; it does not prove those labels are preferred by that geometry.

Consequently T062 establishes only:
- existence of an explicit integral chain map under a declared coordinate chart;
- exact boundary commutation;
- injectivity on the 0-cells.

It does **not** establish:
- RGS or \(O_h\) equivariance;
- a canonical or unique Kathara-to-Q6 map;
- a nonzero 2-cell map or cellular embedding;
- a lift into the A14 tangent or Q6–D5 spectral sector;
- selection of either Kathara–Q3 path convention.

## 6. Implementation and evidence

Companion implementation:
- src/kathara_q6_chain_map.py
- tests/test_kathara_q6_chain_map.py
- docs/KATHARA_Q6_CHAIN_MAP_GATE_C.md

The tests check both chain identities, matrix dimensions, vertex injectivity, retention of the 15 primary lines, and the explicit collapse of the ten 2-cells. They are supplied for execution; this theorem record does not claim they have been run.

**Next open problem:** construct a nondegenerate, geometrically and equivariantly justified chain lift \(K\to Q_6^{(2)}\), or prove an obstruction under clearly stated hypotheses.
