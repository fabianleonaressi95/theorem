# T061 — Chain homotopy between the two Kathara–Q3 path conventions

**Status:** explicit finite chain-homotopy result, conditional on the incidence data and the two path maps specified below. The identities are algebraic and admit exact integer verification. The independent execution of the accompanying computational checks is not claimed here.

## 1. Context and conventions

Let K be the filled Kathara planar CW complex of T059, with
\[
(C_0,C_1,C_2)=(\mathbb Z^{12},\mathbb Z^{21},\mathbb Z^{10}),
\]
and let Q3^{(2)} be the cubical 2-skeleton of the three-cube, with
\[
(C_0,C_1,C_2)=(\mathbb Z^8,\mathbb Z^{12},\mathbb Z^6).
\]
The target has no 3-cells. Its six square faces are oriented by the standard cubical product orientation.

Use the vertex projection of T060:
\[
b_0(v)=\mathbf 1_{x_v>0},\qquad
b_1(v)=\mathbf 1_{y_v\geq4},\qquad b_2(v)=0.
\]
Thus all images lie in the square face b2=0.

For an edge whose endpoints differ in one bit, both conventions use the unique target edge with the appropriate sign. For an edge whose endpoints differ in both b0 and b1, define:
- Convention A (b0-first): flip b0, then b1;
- Convention B (b1-first): flip b1, then b0.

With the stated Kathara coordinates and edge list, the only source edge whose image changes two bits is (5,7).

## 2. Theorem: explicit chain homotopy

Let S and S' be the chain maps obtained from conventions A and B, respectively, including their induced face maps S2 and S2'. Then S0=S0', and the only differing column of S1 and S1' is the column indexed by the source edge (5,7).

With target edge notation
- e0: 000 -> 100,
- e1: 010 -> 110,
- e4: 000 -> 010,
- e5: 100 -> 110,

the difference on that source edge is
\[
(S_1-S'_1)(5,7)=e_0-e_1-e_4+e_5.
\]
This is the oriented boundary of the square face Q with b2=0:
\[
e_0-e_1-e_4+e_5=\partial_2^{Q_3}Q.
\]

Define a degree +1 chain homotopy H by
\[
H_0:C_0(K)\to C_1(Q_3)=0,
\]
and
\[
H_1:C_1(K)\to C_2(Q_3),
\qquad H_1((5,7))=Q,
\]
with H1 zero on the other 20 source edges. Since the target is the 2-skeleton, set H2=0.

Then
\[
S_0-S'_0=\partial_1 H_0+H_{-1}\partial_0=0,
\]
\[
S_1-S'_1=\partial_2^{Q_3}H_1+H_0\partial_1^K
=\partial_2^{Q_3}H_1,
\]
and
\[
S_2-S'_2=\partial_3^{Q_3}H_2+H_1\partial_2^K
=H_1B_2^K.
\]
Consequently
\[
\boxed{S-S'=\partial H+H\partial.}
\]
In particular, S and S' induce the same homomorphisms on homology.

The face coefficient transferred by S2 need not be attached to the same named Kathara face under the two path conventions: the reported construction assigns the nonzero coefficient to F5 for convention A and F3 for convention B. This is a chain-level, convention-dependent description, not an intrinsic designation of a preferred Kathara face.

## 3. What is invariant

The following distinctions are essential:

1. The matrices S1 and S1' are different.
2. Their difference is the boundary of the explicit square 2-cell, supported on the source edge (5,7).
3. The two chain maps are chain-homotopic.
4. Therefore their induced maps on homology agree.
5. The identity of the Kathara face receiving a nonzero S2 coefficient is not invariant under this change of path convention.

The result establishes equivalence of these two specified constructions. It does not establish that every possible chain map with the same vertex map is chain-homotopic to them.

## 4. Homotopy classification: correction to an overstrong claim

The source K is the cellular chain complex of a disk and is contractible. The target Q3^{(2)} is connected and has homology
\[
H_0(Q_3^{(2)};\mathbb Z)=\mathbb Z,\quad
H_1(Q_3^{(2)};\mathbb Z)=0,\quad
H_2(Q_3^{(2)};\mathbb Z)=\mathbb Z.
\]
For maps from a contractible disk to a connected target, the induced H0 map determines the homotopy class of continuous maps, and in the corresponding free cellular-chain setting the chain-homotopy class is likewise determined by the augmentation/H0 map under the standard projective-complex hypotheses.

**Do not state** \([K,Q_3]\cong\mathbb Z\) for this disk source. That assertion is incompatible with contractibility of K: the unbased homotopy classes of maps from a contractible space to a connected space form a singleton. The integer \(H_2(Q_3^{(2)})\cong\mathbb Z\) is a target homology group, not a set of homotopy classes of maps out of K.

A fully general algebraic classification for arbitrary chain complexes requires care with projectivity, boundedness, and the relevant derived/Hom groups. The explicit H above proves the equivalence needed here without relying on a general Ext slogan.

## 5. Orientations

Reversing a source edge changes the corresponding basis vector in C1(K) by a sign; the corresponding columns of B1^K and the edge-map matrix S1 must be transformed consistently. Reversing a source face changes the corresponding C2(K) basis vector and the matching column of B2^K and S2. These are basis changes in the chain complex. They do not alter the underlying chain-homotopy class when all matrices are transformed coherently.

The exact entries of incidence and chain-map matrices are orientation-convention dependent; homology and the induced map, up to the corresponding basis identifications, are invariant.

## 6. Extension to Q6

The cubical product Q6=Q3 x Q3 admits factor inclusions, for example
\[
\iota:Q_3^{(2)}\hookrightarrow Q_3\times Q_3,
\qquad x\mapsto(x,x_*),
\]
where x_* is a fixed vertex in the second factor. This induces a cellular chain map. Composing gives a chain-map candidate
\[
K\xrightarrow{S}Q_3^{(2)}\xrightarrow{\iota}Q_6.
\]
The choice of factor and fixed vertex is additional data. This construction proves existence of a noncanonical extension by inclusion; it does not assign 64 specific hexagrams to the 12 Kathara centers and does not use both Q3 factors nontrivially.

## 7. Status and open questions

**Established for the stated constructions**
- The two path conventions differ on the single edge (5,7).
- Their difference is the boundary of the b2=0 square.
- The displayed H gives an explicit chain homotopy, provided the face-map matrices satisfy the stated degree-2 identity.
- The two maps induce identical homology maps.

**Not established**
- A canonical or symmetry-selected Kathara-to-Q3 map.
- Uniqueness among all chain maps with the given vertex projection.
- A nontrivial use of all three trigram bits.
- A canonical extension to Q6.
- An identification with Krist-All or a physical interpretation.

The next problem is to identify additional geometric or variational structure that could select a representative, and to prove uniqueness or exhibit degeneracy for that selection principle.

## 8. Reproducibility and verification boundary

The exact chain-homotopy check consists of verifying the matrix identities
\[
B_2^{Q_3}H_1=S_1-S'_1,
\qquad
H_1B_2^K=S_2-S'_2.
\]
A reproducible script should construct both path conventions and H over the integers, then check these equalities entry by entry. No test execution is claimed by this theorem record.
