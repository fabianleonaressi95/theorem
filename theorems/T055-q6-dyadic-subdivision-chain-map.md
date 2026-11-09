# T055 — Exact dyadic subdivision chain map for the canonical Q6 2-skeleton

**Status:** proved finite combinatorial/geometric theorem.  
**Scope:** the standard midpoint subdivision of the embedded cubical 2-skeleton of ([0,1]^6). This is a reference refinement, not a Kathara/Krist-All identification.

## 1. Coarse oriented complex

Let (K) be the 2-skeleton of the unit six-cube. Its cells are the vertices, edges and square faces, with
[
(|K_0|,|K_1|,|K_2|)=(64,192,240).
]
Use the canonical orientations: an edge is oriented in the increasing coordinate direction, equivalently from the smaller six-bit integer to the larger; a square in axes (a<b) has orientation (+e_a,+e_b,-e_a,-e_b). Let
[
B_1:C_1(K)	o C_0(K),qquad B_2:C_2(K)	o C_1(K)
]
be the resulting integer boundary matrices, so (B_1B_2=0).

## 2. Midpoint-refined complex

Embed (K) in ([0,1]^6) and represent coordinates in doubled units ({0,1,2}), corresponding to (0,1/2,1).

Define (K') as follows.

- A refined vertex is a point of ({0,1,2}^6) with at most two coordinates equal to (1), all other coordinates being (0) or (2).
- A refined edge is an axis-parallel unit grid segment whose varying coordinate runs from (s) to (s+1), (sin{0,1}), and whose other five coordinates have at most one entry equal to (1).
- A refined square is specified by two axes (a<b), two segment indices (s_a,s_bin{0,1}), and four remaining fixed coordinates in ({0,2}). It is oriented by (+e_a,+e_b,-e_a,-e_b).

The counts are
[
|K'_0|=sum_{j=0}^2inom6j2^{6-j}=64+192+240=496,
]
[
|K'_1|=6cdot2left(2^5+5cdot2^4ight)=1344,
]
[
|K'_2|=inom62,2^4,2^2=960.
]
Let (B'_1,B'_2) be the oriented boundary matrices of (K').

## 3. Subdivision maps

Define integer cellular maps (S_k:C_k(K)	o C_k(K')):

- (S_0) sends each coarse vertex to the same geometric vertex in (K');
- (S_1) sends each coarse oriented edge to the sum of its two positively oriented half-edges;
- (S_2) sends each coarse oriented square to the sum of its four positively oriented child squares.

Every child has the orientation induced by its parent. By cancellation of the internal subdivision edges and preservation of the outer oriented boundary,
[
oxed{B'_1S_1=S_0B_1,qquad B'_2S_2=S_1B_2.}
]
These are exact integer identities. Also (B'_1B'_2=0), since every fine square has zero boundary boundary.

The column sums of (S_0,S_1,S_2) are respectively (1,2,4): every parent vertex, edge and square has exactly one, two and four children in the corresponding dimensions.

## 4. Proof

The vertex count follows by choosing (jle2) midpoint coordinates and assigning each of the remaining (6-j) coordinates either endpoint value. For an edge, choose its axis (6 choices), its half-segment (2 choices), and either no midpoint among the five fixed coordinates ((2^5) choices) or one midpoint coordinate (5 choices) with the remaining four endpoint values ((2^4) choices). For a square, choose its two axes, its four fixed endpoint coordinates and its two half-segment indices.

For (S_1), the boundary of the two consecutive oriented half-edges is the terminal fine vertex minus the initial fine vertex; this equals (S_0) applied to the coarse edge boundary. This proves (B'_1S_1=S_0B_1) on the edge basis and hence on all of (C_1(K)).

For (S_2), the four child squares have the same positive axis-pair orientation as the parent. Their internal edges occur twice with opposite signs and cancel. The remaining eight half-edges are exactly the subdivision (S_1) of the four oriented parent boundary edges. Thus (B'_2S_2=S_1B_2) on the face basis and hence on all of (C_2(K)). Each fine square separately satisfies the boundary-of-boundary identity, giving (B'_1B'_2=0). (square)

## 5. Corollary — axis-direction transfer

Each of the six coordinate directions contains 32 coarse edges. Aggregate the columns of \(S_1\) by parent direction and its rows by child direction, dividing by 32. Since each parent edge is replaced by exactly two half-edges parallel to the same axis, the resulting \(6\times6\) direction-count matrix is
\[
\boxed{D=2I_6.}
\]
Consequently, under an identification of three ordered trigram lines with any three fixed coordinate axes, this midpoint subdivision induces \(2I_3\) on **axis-direction counts**, not the tribonacci matrix. This is not a statement about the Walsh-character compression \(E^T\mathcal R E\); identifying those two representations would require an additional map.

## 6. Interpretation and non-conclusions

This theorem supplies an actual oriented parent-to-child refinement for the standard dyadic subdivision of the existing Q6 square complex. It is stronger than the bare incidence data because the child cells and subdivision maps are now explicitly specified.

It does **not** identify this standard cubical subdivision with Kathara/Krist-All. It also does not define a map from the refined chain groups to the three first-order trigram Walsh channels. Consequently it does not derive
[
M_\psi=\begin{pmatrix}0&0&1\\1&0&0\\0&1&1\end{pmatrix}
]
or the supergolden growth factor from Kathara geometry. The axis-aligned midpoint rule preserves the coordinate-axis labels; no asymmetric three-channel transfer is asserted.

The implementation-level exact integer audit is in the companion repository:
- `src/q6_dyadic_refinement.py`;
- `tests/test_q6_dyadic_refinement.py`;
- `examples/q6_dyadic_refinement_audit.py`;
- [specification](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/Q6_DYADIC_SUBDIVISION_CHAIN_MAP.md).

The mathematical theorem is independent of a successful run of that code; the code and tests are reproducibility checks for the stated finite construction.
