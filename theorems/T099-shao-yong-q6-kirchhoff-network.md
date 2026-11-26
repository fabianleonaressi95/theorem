# T099 — Shao–Yong hexagram product structure and Kirchhoff network

**Status:** proved finite combinatorial theorem; conditional circuit model; circular-order transcription open.  
**Scope:** the 64 six-line configurations represented by the eight lower and eight upper trigrams.

## 1. Conventions and definitions

Encode a broken line by \(0\) and a solid line by \(1\). Read the six lines from bottom to top. Write a hexagram as
\[
H=(\ell_0,\ell_1,\ell_2\mid u_0,u_1,u_2)=(\ell,u),
\qquad \ell,u\in\{0,1\}^3.
\]
The lower trigram is \(\ell\), the upper trigram is \(u\). Choose the vertex index
\[
\iota(\ell,u)=\sum_{r=0}^2 2^r\ell_r+
8\sum_{r=0}^2 2^r u_r\in\{0,\ldots,63\}.
\]
Thus rows of the \(8\times8\) matrix are indexed by lower trigrams and columns by upper trigrams. This is a coordinate convention; changing the ordering of the eight trigrams only permutes rows or columns.

Define the six-bit Hamming graph \(Q_6\): two vertices are adjacent exactly when their six-bit strings differ in one coordinate. Let \(Q_3^-\) act on the lower three coordinates and \(Q_3^+\) on the upper three coordinates.

## 2. Theorem: product decomposition

**Theorem T099.1.** With the preceding convention,
\[
\boxed{Q_6\cong Q_3^-\square Q_3^+.}
\]
Equivalently, under the tensor-product ordering,
\[
\boxed{L_6=L_3\otimes I_8+I_8\otimes L_3,}
\]
where \(L_3=3I_8-A(Q_3)\). If the lower coordinate is the fastest index, the displayed Kronecker factors are exchanged; the graph and spectrum are unchanged.

**Proof.** A vertex is a pair \((\ell,u)\). A one-bit change either changes exactly one coordinate of \(\ell\), leaving \(u\) fixed, or changes exactly one coordinate of \(u\), leaving \(\ell\) fixed. These are precisely the two edge classes in the Cartesian product. The Cartesian-product Laplacian is the sum of the two factor Laplacians acting on their respective tensor factors. \(\square\)

**Corollary 1 (counts).**
\[
|V|=8\cdot8=64,\qquad \deg(v)=3+3=6,
\]
\[
|E|=8|E(Q_3)|+8|E(Q_3)|=8(12)+8(12)=192.
\]
There are exactly 96 edges changing one of the three lower lines and 96 changing one of the three upper lines. Each of the eight fixed-lower-trigram rows and each fixed-upper-trigram column contains a copy of \(Q_3\) as its induced subgraph.

**Corollary 2 (spectrum).** The adjacency eigenvalues of \(Q_6\) are \(6-2k\), and the Laplacian eigenvalues are \(2k\), for \(k=0,\ldots,6\), with multiplicity \(\binom6k\). In particular the Laplacian spectrum is
\[
0^1,2^6,4^{15},6^{20},8^{15},10^6,12^1.
\]
This follows either from the tensor sum or from the Walsh characters of \(\{0,1\}^6\).

## 3. The 8×8 array and the circular diagram

The array is the Cartesian product of the two trigram sets:
\[
\mathcal H=\mathcal T_{\rm inf}\times\mathcal T_{\rm sup},
\qquad |\mathcal T_{\rm inf}|=|\mathcal T_{\rm sup}|=8.
\]
Each cell contains one ordered pair of trigrams. Fixing a row fixes the lower trigram; fixing a column fixes the upper trigram (or vice versa if the source diagram transposes its axes).

A circular arrangement of the same 64 hexagrams is, at the level of labels alone, a permutation
\[
\pi:\{0,\ldots,63\}\to\{0,\ldots,63\}.
\]
A permutation changes the displayed order, not the abstract graph. If \(P_\pi\) is its permutation matrix, the relabelled Laplacian is \(P_\pi L_6P_\pi^{T}\), hence has the same spectrum and is graph-isomorphic to \(Q_6\).

**Important limitation.** The cited śūnyatāQi article describes the 8×8 lower/upper-trigram array and its circular representation. It does not, by itself, specify a new electrical edge set, edge conductances, or a physical charge law. The actual circular order must be transcribed from the primary diagram with an explicit line-order and orientation convention before a concrete permutation \(\pi\) can be claimed. A circular drawing is not automatically the cycle graph \(C_{64}\), and visual crossings are not electrical junctions. The “32 + 32” split is not the lower/upper-trigram decomposition: there are eight possible lower and eight possible upper trigrams, with 64 pairings.

## 4. Conditional Kirchhoff network

Take the 64 hexagrams as circuit nodes. For every edge changing a lower line assign conductance \(g_-\ge0\); for every edge changing an upper line assign conductance \(g_+\ge0\). For \(g_-,g_+>0\), the weighted graph Laplacian is
\[
L(g_-,g_+)=g_-(I_8\otimes L_3)+g_+(L_3\otimes I_8),
\]
for the declared index \(\iota(\ell,u)=\ell+8u\), in which the lower index is fastest. With the opposite tensor ordering, the two tensor factors are exchanged.

For nodal potentials \(V\in\mathbb R^{64}\) and injected currents \(J\in\mathbb R^{64}\), Kirchhoff's current law is
\[
L(g_-,g_+)V=J.
\]
Because the graph is connected, this equation is solvable exactly when
\[
\mathbf1^T J=0,
\]
and its potential is unique up to an additive constant. With the zero-mean gauge \(\mathbf1^TV=0\),
\[
V=L(g_-,g_+)^\dagger J.
\]
If a specified node-capacitance matrix \(C\) is used, the stored charge is \(q=CV\). The corresponding linear RC dynamics are
\[
C\dot V+L(g_-,g_+)V=J(t),
\]
for a time-independent positive capacitance matrix \(C\).

These are standard network equations on the defined graph. They do **not** establish that I Ching symbols determine an experimentally existing charge. That physical interpretation requires a realizable circuit, a justified mapping from hexagram transitions to components, measured conductances/capacitances, and comparison with predictions.

## 5. Reproducible finite audit

The companion audit \`scripts/audit_t099_shao_yong_q6.py\` checks:
- 64 distinct pair states and the 8×8 indexing;
- degree six at every vertex;
- 96 lower-line and 96 upper-line edges;
- the 192-edge total;
- the binomial Laplacian spectrum;
- validation of a supplied circular ordering as a permutation, without fabricating one.

Run:
\`\`\`bash
python scripts/audit_t099_shao_yong_q6.py
pytest -q tests/test_t099_shao_yong_q6.py
\`\`\`

## 6. Evidence classification

| Claim | Classification |
|---|---|
| 8 lower and 8 upper trigram labels yield 64 ordered pairs | Exact combinatorial identity |
| \(Q_6=Q_3^-\square Q_3^+\), 192 edges split 96+96 | Proved finite graph identity |
| Laplacian spectrum and multiplicities | Proved finite graph identity |
| Shao–Yong circular diagram is a permutation of the same 64 labels | Structural description; exact permutation awaits transcription |
| Weighted Kirchhoff and RC equations on this graph | Standard conditional circuit model |
| Hexagram geometry physically determines electric charge | Open physical hypothesis; no empirical evidence asserted |

## 7. Source

- śūnyatāQi, “Hexagramas, números y cosmología: Leibniz y el sistema binario inspirado en el I Ching”, https://www.sunyataqi.com/blog/general/hexagramas-numeros-y-cosmologia-leibniz-y-el-sistema-binario-inspirado-en-el-i-ching (accessed 2026-11-12). Used for the described 8×8 lower/upper-trigram arrangement and circular representation, not as evidence for an electrical law.
