# T140 — Incidence lift of the supergolden icosahedral graph into Q6

**Status:** [N] explicit finite combinatorial construction; [P] chain-map identity; [O] antipodally equivariant lift and geometrically derived Q6 mixing operator. This record does not claim a PSU–Anti-Twin coupling.

## 1. Bipartite obstruction

The icosahedral 1-skeleton contains triangles, whereas Q6 is bipartite. Therefore no graph homomorphism can send every icosahedral edge to one Q6 edge while preserving endpoints. In particular, a direct edge-preserving map of the icosahedral graph into Q6 is impossible.

## 2. A two-step incidence lift

Use the fixed vertex ordering of T139. An explicit injective map of the 12 icosahedral vertices into the even-parity vertices of Q6 is:

| Icosahedron vertex | Q6 bit string |
|---:|:---:|
| 0 | 000000 |
| 1 | 000011 |
| 2 | 100001 |
| 3 | 000101 |
| 4 | 100010 |
| 5 | 100111 |
| 6 | 001010 |
| 7 | 101101 |
| 8 | 100100 |
| 9 | 000110 |
| 10 | 101000 |
| 11 | 001001 |

Every icosahedral edge has endpoints at Hamming distance 2. It can therefore be represented by a two-edge path in Q6 through a common odd-parity neighbor. The script chooses the numerically smallest such intermediate vertex, deterministically.

This gives a map on vertices and a path-valued lift of every edge. It is not an embedding of the full subdivided graph: intermediate vertices and Q6 links may be reused. The overlap is measured by the script and is part of the data, not hidden.

## 3. Chain-map identity

Orient every icosahedral edge from its lower to its higher vertex index. For an edge (e=(u,v)), let (a=iota(u)), (b=iota(v)), and let (z_e) be the selected common neighbor. Define
[
iota_1(e)=[a,z_e]+[z_e,b].
]
With each Q6 link oriented from the smaller to the larger integer code, signs are inserted accordingly. By construction,
[
partial_1^{Q_6},iota_1(e)
=[b]-[a]
=iota_0,partial_1^{P_psi}(e).
]
Thus the vertex map and path lift define a chain map on the 1-skeleton.

## 4. What remains open

The displayed lift is not antipodally equivariant: the table does not establish
[
iota_0(-x)=iota_0(x)+mathbf 1.
]
Consequently it does not yet intertwine (J_psi) with the Q6 complement involution (J). It cannot be used to claim an odd operator, anticommutation, or PSU–Anti-Twin mixing.

The next constraint-solving problem is to find an injective lift satisfying antipodal equivariance, then transport orientations and the archived Q6 connection data. Only after that can an operator on Q6 be defined and tested for adjointness, support, ({T,J}=0), rank, and spectrum.

## 5. Reproduction

Run:
```bash
python scripts/audit_t140_icosahedron_q6_lift.py
python -m unittest tests.test_t140_icosahedron_q6_lift
```
The tests certify the explicit vertex injection, parity, Hamming-distance-two condition, existence of each two-step path, and the chain-boundary identity. They do not certify antipodal equivariance or a mixing operator.
