# C60 to the spherical Kathara completion: degree-one existence theorem

**Status:** proved topological existence; explicit label-level matrices and metric canonicality remain open.

## 1. The two source and target complexes

Let (X_{60}) be the oriented cellular surface of the truncated-icosahedral C60 cage, with
[
(C_0,C_1,C_2)=(60,90,32),qquad chi(X_{60})=2.
]
Let (K^+) be the Kathara spherical completion: the 12-vertex, 21-edge planar graph with all ten bounded faces and the outer 8-gon attached as an eleventh face. Its oriented face boundaries cancel and
[
(C_0,C_1,C_2)=(12,21,11),qquad chi(K^+)=2.
]
Both are finite regular polygonal CW decompositions of the oriented 2-sphere. The ten-face Kathara disk is **not** the target considered here: its (H_2) vanishes and it cannot carry a degree-one map from (X_{60}).

## 2. Existence theorem

**Theorem.** There exists an orientation-preserving cellular map
[
f:X_{60}longrightarrow K^+
]
whose induced map on second homology is multiplication by (+1). Consequently there exist integer matrices
[
P_0inmathbb Z^{12	imes60},quad
P_1inmathbb Z^{21	imes90},quad
P_2inmathbb Z^{11	imes32}
]
satisfying the exact chain-map identities
[
B_1^{K^+}P_1=P_0B_1^{C60},qquad
B_2^{K^+}P_2=P_1B_2^{C60},
]
and, for coherently oriented fundamental cycles (c_{60}) and (c_K),
[
P_2c_{60}=c_K.
]
In particular, (deg(f)=+1).

**Proof.** By the exact homology audits, (X_{60}) and (K^+) are connected, closed, orientable surfaces with Euler characteristic 2; hence each is homeomorphic to (S^2). Choose orientation-preserving homeomorphisms (a:X_{60}	o S^2) and (b:K^+	o S^2). Then (f=b^{-1}circ a) is an orientation-preserving homeomorphism. The cellular approximation theorem gives a cellular map (f_c) homotopic to (f). Homotopic maps induce the same map on homology, so ((f_c)_*:H_2(X_{60};mathbb Z)	o H_2(K^+;mathbb Z)) sends the oriented generator to the oriented generator. The induced cellular chain maps are represented by integer matrices (P_i) and commute with the cellular boundary operators, giving the two displayed identities. (square)

## 3. What this proves — and what it does not

The theorem closes the **pure existence** gap: a degree-one C60-to-(K^+) cellular chain map is not topologically obstructed. It also shows why the ten-face disk result cannot be carried over: the target must retain the outer face.

It does **not** select a unique map. The homeomorphisms (a) and (b), the cellular approximation, and the subdivisions used in a constructive PL realization are choices. The theorem does not establish that a particular map is induced by the C60 embedding in (mathbb R^3), by the Kathara drawing, by the RGS metric, or by a Stone–Wales operation.

In particular, a degree-one map must not be manufactured by adding the target fundamental cycle to an arbitrary (P_2) column after the fact. That would satisfy an algebraic equation but would not identify a continuous or geometrically selected map.

## 4. Constructive route to explicit matrices

A reproducible implementation should:

1. Fix orientations of the C60 and (K^+) surfaces and record their polygonal attaching maps.
2. Triangulate every pentagon/hexagon of C60 and every polygonal face of (K^+), recording each subdivision map back to the original cells.
3. Specify an orientation-preserving PL homeomorphism between the two triangulated spheres, for example by a documented common-refinement/vertex-correspondence construction.
4. Apply cellular approximation relative to the chosen CW filtrations and derive (P_0,P_1,P_2) from signed cell incidences.
5. Verify both chain identities over the integers and compute the degree independently by comparing (P_2c_{60}) with (c_K). Require degree (+1), not merely a nonzero column rank.
6. Compose with the already audited (K^+	o Q6) map and verify that the C60 fundamental class has the predicted nonzero image in the Q6 2-skeleton.

The existing (K^+	o Q6) construction uses the declared axis order ((1,2,0,3,4,5)). Its nonzero H2 image is exact, but that path convention is not RGS-metric canonical. A degree-one (X_{60}	o K^+) map would therefore produce a nonzero composite H2 lift, while leaving metric canonicality as a separate question.

## 5. Evidence classification

| Statement | Status |
|---|---|
| (X_{60}) is a cellular 2-sphere | Exact homology/Euler audit plus closed connected orientable surface structure |
| (K^+) is a cellular 2-sphere | Exact face-boundary cancellation and homology/Euler audit |
| A degree-(+1) cellular map (X_{60}	o K^+) exists | **Proved** by homeomorphism + cellular approximation |
| Explicit label-level (P_0,P_1,P_2) matrices | Open; not supplied by the existence proof |
| A canonical map from the physical C60 embedding to the Kathara/RGS geometry | Open |
| Degree-one composite (X_{60}	o K^+	o Q6) | Follows once the explicit degree-one cellular map is constructed and composed with the audited nonzero-degree (K^+	o Q6) map; matrices not yet generated here |
| Stone–Wales/Q6 commuting square | Open; target action still needs definition |

## Reproduction and relation to prior audits

The input cell structures and the spherical completion are documented in:
- `docs/C60_KATHARA_Q6_CHAIN_BRIDGE_AUDIT.md`
- `docs/KATHARA_SPHERICAL_COMPLETION_Q6_H2_LIFT.md`
- `scripts/audit_c60_q6_bridge.py`
- `scripts/audit_kathara_spherical_q6_lift.py`

This note adds a topological existence theorem; it does not claim that explicit (P_i) arrays have already been computed.
