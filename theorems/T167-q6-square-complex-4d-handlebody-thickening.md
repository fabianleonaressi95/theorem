# T167 — A 4D handlebody thickening of the Q6 square complex

**Status:** explicit smooth/PL 4-manifold-with-boundary construction at the level of a 2-dimensional spine; the extension carrying the 160 triple 3-faces and 60 four-cells is OPEN. This is a genuine manifold replacement candidate, not a proof that the original cubical 4-skeleton is resolved.

## 1. The retained Q6 data

Let \(G=Q_6^{(1)}\) be the 1-skeleton of the six-dimensional cube. It has
\[
V=2^6=64,\qquad E=6\,2^5=192,\qquad \deg(v)=6.
\]
It is connected, so its cycle rank is
\[
\beta_1(G)=E-V+1=129.
\]

Let \(X=Q_6^{(2)}\) be the square 2-skeleton. It has 240 square 2-cells. Since attaching cells of dimension at least three does not change \(H_1\), and the full cube is contractible,
\[
H_1(X;\mathbb Z)=0.
\]
The cellular chain groups have ranks \(64,192,240\). The boundary \(\partial_1\) has rank 63, and exactness at \(C_1\) gives
\[
\operatorname{rank}\partial_2
=\dim\ker\partial_1
=192-63=129.
\]
There are no 3-cells in \(X\), hence
\[
H_2(X;\mathbb Z)\cong\ker\partial_2,\qquad
\beta_2(X)=240-129=111.
\]
Thus
\[
(\beta_0,\beta_1,\beta_2)(X)=(1,0,111),\qquad \chi(X)=112.
\]

## 2. Handlebody construction

Choose a spanning tree \(T\subset G\). It has 63 edges; the remaining 129 edges give free generators for \(\pi_1(G)\).

1. Start with one 4-dimensional 0-handle \(B^4\).
2. Attach 129 4-dimensional 1-handles. The resulting 1-handlebody \(H_1\) has spine homotopy equivalent to \(G\), and \(\partial H_1\) is a connected orientable 3-manifold.
3. For each of the 240 square faces \(\sigma\) of Q6, take its attaching word \(w_\sigma\) in the 129 free generators, obtained by reading its four oriented edges and cancelling tree paths.
4. Represent the 240 conjugacy classes by a disjoint framed link \(L=\bigsqcup_\sigma L_\sigma\) in \(\partial H_1\). In a 3-manifold, finitely many 1-dimensional loops can be put in general position and made pairwise disjoint while retaining their individual free homotopy classes.
5. Attach one 4-dimensional 2-handle \(D^2\times D^2\) along each framed component \(S^1\times D^2\subset\partial H_1\).

The resulting compact smooth 4-manifold \(W^{(2)}\) has boundary. Its handle spine is the CW complex with the Q6 graph as 1-skeleton and the 240 square attaching words as 2-cells; therefore it is homotopy equivalent to \(X=Q_6^{(2)}\).

The framing of each attaching component is extra integer data. This construction proves existence after choosing such framings, but it does not select a canonical Q6-induced framing.

## 3. Topological checks

The handle counts are
\[
(h_0,h_1,h_2)=(1,129,240),
\]
so
\[
\chi(W^{(2)})=1-129+240=112=\chi(X).
\]
Since \(W^{(2)}\) has the homotopy type of \(X\),
\[
H_0(W^{(2)};\mathbb Z)=\mathbb Z,\quad
H_1(W^{(2)};\mathbb Z)=0,\quad
H_2(W^{(2)};\mathbb Z)=\mathbb Z^{111},
\]
and \(H_k(W^{(2)};\mathbb Z)=0\) for \(k\ge3\).

Because it is built by standard smooth handles with disjoint attaching regions, \(W^{(2)}\) is a smooth 4-manifold with boundary. Its interior points have local links \(S^3\); boundary points have local links \(B^3\). A compatible PL triangulation therefore has the required vertex-link type after subdivision.

This avoids the T166 singular link \((\Delta^5)^{(3)}\), but does so by replacing the raw 4-skeleton with a different 4-manifold whose spine is the Q6 2-skeleton.

## 4. What this does and does not resolve

**Retained exactly**
- the Q6 graph: 64 vertices, 192 edges, degree six;
- the 240 square boundary words;
- the 129 independent graph cycles;
- the 2-complex homotopy type and its \(H_2\cong\mathbb Z^{111}\).

**Not yet retained or constructed**
- the 160 coordinate 3-faces and their triple incidence with 4-cells;
- the 60 coordinate 4-cells;
- a canonical framing determined by the Q6 geometry;
- a global \(SL(2,\mathbb C)\) edge connection, spin structure, or Lorentzian coframe;
- a map from the T164 480 pairwise interfaces into this handlebody;
- a 4-manifold filling/capping that recovers the intended 4D cell content.

In particular, this is not yet a global resolution of the T164 three-branch junctions. It is a manifold carrier for the Q6 square complex on which those data can be reintroduced only after specifying attaching maps for the 3- and 4-dimensional strata.

## 5. Next exact obligations

1. Choose and publish a spanning tree and the 240 square words.
2. Specify the 240 attaching curves and integer framings algorithmically; verify their words in \(\pi_1(H_1)\).
3. Compute the boundary 3-manifold and its homology for the chosen framed link.
4. Determine whether the 160 triple 3-faces can be represented by compatible 3-handle attaching spheres, and whether the 60 four-cells can be represented by 4-handle attachments.
5. Only after these steps, transport the T164 quaternionic lift and T165 \(SL(2,\mathbb C)\) data to the resolved interfaces and construct independent Cartan coframe/connection fields.

## 6. Classification

- **PROVED:** Q6 graph cycle rank is 129.
- **PROVED:** Q6 square 2-skeleton has \(H_1=0\), \(H_2\cong\mathbb Z^{111}\), and Euler characteristic 112.
- **CONSTRUCTED (existence, noncanonical choices):** a smooth compact 4D 0/1/2-handlebody with boundary and homotopy type \(Q_6^{(2)}\).
- **OPEN:** canonical Q6 framing, 3-/4-handle extension, preservation of the 160/60 higher-cell incidence, global T164/T165 transport, and Lorentzian Cartan dynamics.

T167 is deliberately a first manifold carrier and not a claim that the full Q6 4-skeleton has become a 4-manifold.
