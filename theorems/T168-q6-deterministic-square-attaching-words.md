# T168 — Deterministic Q6 square attaching words

**Status:** exact combinatorial construction and exact rational rank audit. Geometric realization of the framed attaching link and its Q6-canonical framings remain open.

## 1. Canonical combinatorial choices

Encode the 64 vertices of Q6 by integers \(v\in\{0,\ldots,63\}\), with coordinate flips \(v\mapsto v\oplus2^k\). Order vertices and edges lexicographically. Choose the breadth-first spanning tree rooted at \(0\), visiting each vertex's six neighbors in increasing integer order.

The tree has 63 edges. The remaining 129 edges are oriented from their smaller to larger endpoint and define free generators \(g_0,\ldots,g_{128}\) of the fundamental group of the graph.

For every pair of coordinates \(i<j\) and every base vertex with both bits zero, orient the square
\[
v\to v+2^i\to v+2^i+2^j\to v+2^j\to v.
\]
There are exactly 240 such faces. Suppress tree-edge letters and replace each chord traversal by \(g_k^{\pm1}\), with sign determined by its orientation. This gives a deterministic cyclic attaching word for every Q6 plaquette.

## 2. Exact chain audit

The oriented cellular boundary matrix \(\partial_2:C_2\to C_1\) has 192 rows and 240 columns. Exact sparse Gaussian elimination over \(\mathbb Q\) gives
\[
\operatorname{rank}_{\mathbb Q}\partial_2=129.
\]
Since the graph is connected, \(\operatorname{rank}\partial_1=63\). Thus
\[
H_1(Q_6^{(2)};\mathbb Z)=0,\qquad
H_2(Q_6^{(2)};\mathbb Z)\cong\mathbb Z^{111},
\]
and \(\chi=64-192+240=112\).

The script scripts/audit_q6_handle_words_t168.py implements the deterministic tree, all 240 words, and the rational rank computation using only the Python standard library. The test tests/test_q6_handle_words_t168.py checks the counts and ranks.

## 3. Relation to the 4D handlebody T167

T167's 0/1/2-handle construction can now use these explicit square words as its attaching-map input. The words determine the free homotopy classes of the attaching circles, not their embeddings or framings. In the oriented 3-manifold boundary of the 1-handlebody, the finitely many loops can be represented by a disjoint link after general-position perturbation. Each component then requires an integer framing to attach a 2-handle.

No canonical integer framing is selected by the Q6 combinatorics alone in this audit. A Q6-induced framing must be derived from an explicitly specified embedding/normal framing, not set to zero by convention and then called geometric.

The 240 square relations normally generate the fundamental group because the Q6 square 2-skeleton is simply connected: attaching cells of dimension at least three to it gives the contractible 6-cube and does not change \(\pi_1\). This is stronger than merely observing that their abelianized boundary vectors span the 129-dimensional cycle space.

## 4. What this does not prove

- It does not construct an explicit polygonal link in a triangulated \(\partial H_1\).
- It does not compute the boundary 3-manifold after the 240 framed 2-handle attachments.
- It does not give canonical Q6 framings.
- It does not add the 160 triple 3-faces or 60 four-cells.
- It does not yet transport T164's quaternionic cocycle or T165's \(SL(2,\mathbb C)\) data.

## 5. Classification

- **PROVED EXACTLY:** deterministic spanning tree with 63 edges and 129 chord generators.
- **PROVED EXACTLY:** 240 explicit square attaching words.
- **PROVED EXACTLY:** \(\operatorname{rank}_{\mathbb Q}\partial_2=129\), \(H_2\cong\mathbb Z^{111}\), and \(\chi=112\).
- **OPEN:** explicit framed link, Q6-canonical framings, boundary homology, 3-/4-handle extension, and global Lorentzian Cartan coupling.
