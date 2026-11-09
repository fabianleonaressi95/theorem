# T058 — Planar face audit of the source-transcribed Kathara 12-center / 15-line graph

**Status:** exact finite graph theorem conditional on the incidence transcription of the published Level-1 Kathara diagram.  
**Scope:** graph connectedness, planar straight-line embedding, orientation and face count. No energetic, cosmological or physical interpretation is asserted.

## 1. Graph data

Let the vertices be \(V=\{1,\ldots,12\}\), with integer coordinates
\[
\begin{array}{c|rrrrrrrrrrrr}
v&1&2&3&4&5&6&7&8&9&10&11&12\\\hline
x&0&0&-1&1&0&-1&1&0&-1&1&0&0\\
y&0&1&2&2&3&4&4&5&6&6&7&8
\end{array}
\]
The 15 named primary lines are the three paths
\[
L_1=(1,2,5,8,11,12),\quad
L_2=(3,6,9),\quad
L_3=(4,7,10)
\]
and the twelve cross-links
\[
\begin{split}
L_4&=(1,3),&L_5&=(2,3),&L_6&=(1,4),&L_7&=(2,4),\\
L_8&=(9,12),&L_9&=(9,11),&L_{10}&=(10,12),&L_{11}&=(10,11),\\
L_{12}&=(8,9),&L_{13}&=(8,10),&L_{14}&=(5,6),&L_{15}&=(5,7).
\end{split}
\]
Expanding the three paths into elementary segments and adjoining \(L_4,\ldots,L_{15}\) gives 21 distinct undirected edges. Orient every elementary edge from the smaller to the larger center label.

This is the explicit incidence transcription audited in the companion implementation. The source manual states that the grid has 12 centers and 15 primary lines, that lines 1–3 are vertical and line 1 is central; the endpoint list above is the diagram-level transcription adopted here. If a higher-resolution original diagram reveals a different endpoint assignment, the theorem's hypotheses and graph must be revised accordingly.

## 2. Theorem

For the above graph and straight-line embedding:

1. the graph is connected;
2. no two nonincident edges cross properly;
3. the increasing-label orientation is acyclic;
4. the planar rotation system has 11 face boundary walks, one unbounded and 10 bounded;
5. Euler's formula holds:
\[
\boxed{|V|-|E|+|F|=12-21+11=2.}
\]

The bounded face boundaries are
\[
\begin{aligned}
&(1,2,3),\quad (1,4,2),\\
&(2,4,7,5),\quad (2,5,6,3),\\
&(5,7,10,8),\quad (5,8,9,6),\\
&(8,10,11),\quad (8,11,9),\\
&(9,11,12),\quad (10,12,11).
\end{aligned}
\]
The exterior face boundary is \((1,3,6,9,12,10,7,4)\), up to cyclic starting point and orientation.

## 3. Proof

Connectedness follows because each of the three vertical paths is connected to the central path by the listed cross-links. Direct integer orientation tests on every pair of nonincident segments show no proper crossings. The rotation system is obtained by sorting the incident edge directions around each vertex; tracing each directed half-edge to the next clockwise half-edge gives the 11 listed boundary walks. The bounded face list contains ten cycles and the exterior walk one cycle. The edge and vertex counts are 21 and 12, so the Euler characteristic is \(12-21+11=2\). Since every oriented edge points from a lower to a higher vertex label, a directed cycle is impossible. \(\square\)

## 4. Cellular and physical non-conclusions

The ten bounded regions can be used as 2-cells of a planar CW complex if that is the intended convention. This does not imply that the original source assigns physical or energetic meaning to these planar regions. Nor does the graph identify with the trigram cube \(Q_3\), whose data are 8 vertices, 12 edges and 6 square faces, or with the Q6 cubical 2-skeleton.

The graph audit is reproducible in:
https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/KATHARA_15_LINE_GRAPH_FACE_AUDIT.md
