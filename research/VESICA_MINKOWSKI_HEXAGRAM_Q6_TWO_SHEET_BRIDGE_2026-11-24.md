# Vesica Piscis, Minkowski cones and the two-trigram decomposition of Q6

**Date:** 24 November 2026  
**Status:** exact combinatorial identification + exact (2+1)-dimensional geometry; geometric realization of Q6 as the two conic sheets remains a construction target.

## 1. The 64 vertices are the 64 hexagrams

A hexagram consists of six binary line values. With a fixed convention (lower trigram first, upper trigram second), write
[
H=(L,U),qquad L,Uinmathbb F_2^3.
]
The eight possible lower trigrams and eight possible upper trigrams give
[
mathcal H=mathbb F_2^3	imesmathbb F_2^3,qquad |mathcal H|=8cdot8=64.
]
Thus the vertex set of the six-bit cube (Q_6) is canonically identified with the set of six-line patterns, once the bit-to-line convention and bit order are declared. This is a bijection of sets; it does not by itself identify every chosen Q6 edge, face, operator or metric with a traditional I Ching relation.

The lower/upper split is structural, not a numerical convenience:
[
mathbb F_2^6=V_{m lower}oplus V_{m upper},qquad
V_{m lower}simeq V_{m upper}simeqmathbb F_2^3.
]
The Gray-code order used in some computational tables is only an enumeration convention. It must not be conflated with the intrinsic six line bits or with the lower/upper trigram decomposition.

## 2. The exact affine-filtration result

For the ordered-prefix filtration (E_j), an affine map (T(x)=Px+b) commutes with (E_j) exactly when the upper-right (j	imes(6-j)) block of (P) vanishes (with the row/column convention of the audited implementation). Equivalently, (P) preserves the corresponding prefix subspace. The translation (b) does not affect the conditional-expectation sigma-algebra.

At the trigram boundary (j=3), every block-diagonal transformation
[
P=\begin{pmatrix}A&0\\0&D\end{pmatrix},
qquad A,Din GL(3,2),
]
preserves the split and commutes with (E_3). The subgroup (GL(3,2)\times GL(3,2)) has (168^2=28,224) elements; the reported exhaustive enumeration finds 16 full commutator profiles and zero commutator at (j=3) for every element. More generally, the exact criterion also permits lower block-triangular mixing from the first block into the second; block diagonal maps are the subgroup preserving both trigram factors separately.

The exhaustive/census details, sampled (GL(6,2)) results, natural Q6 automorphisms, and regression tests are recorded in [PR #437](https://github.com/fabianleonaressi95/theorem/pull/437) and its associated research record. These are finite algebraic results. They do not yet select a physical evolution or a unique geometric embedding.

## 3. Vesica geometry and two null cones in Minkowski (2+1)

Use coordinates ((t,x,y)) and metric (ds^2=-dt^2+dx^2+dy^2). Take two cone vertices
[
p_A=(0,0,0),qquad p_B=(0,1,0).
]
Their null cones are
[
mathcal C_A: t^2=x^2+y^2,qquad
mathcal C_B: t^2=(x-1)^2+y^2.
]
On the slice (t=-1), their spatial sections are the unit circles
[
x^2+y^2=1,qquad (x-1)^2+y^2=1.
]
The corresponding closed disks intersect in the Vesica Piscis. Their boundary circles meet at
[
C,D=\left(\frac12,\pm\frac{\sqrt3}{2}\right).
]
The common chord is (x=1/2), of length (\sqrt3) for unit radius.

The two cone *surfaces* intersect where (x=1/2) and (t^2=1/4+y^2). Their intersection is a spacetime curve; the chord (CD) is only its intersection with the slice (t=-1). Therefore the cone-surface intersection, the spatial Vesica, and the common chord are three distinct objects and must not be identified.

## 4. What is established, and what is not

| Statement | Status |
|---|---|
| Six binary line values are equivalent to an ordered pair of three-bit trigrams | Exact bijection after fixing the line/bit convention |
| The (j=3) prefix boundary is preserved by (GL(3,2)\times GL(3,2)) | Exact finite algebra; exhaustive enumeration reported in PR #437 |
| The two unit circles and their lens-shaped intersection form a Vesica Piscis | Exact Euclidean geometry |
| The two null cones have the stated circular sections and common spacetime intersection | Exact Minkowski (2+1) geometry |
| The two trigram factors are literally the two conic sheets, or Q6 vertices lie on those sheets with a specified incidence/metric | **Open:** requires an explicit map and compatibility proofs |

In particular, “two sheets” is currently a proposed geometric interpretation of the lower/upper trigram factors. The set-theoretic (3+3) split alone does not construct a Lorentzian metric, a causal order, or a map from the 64 hexagrams to points on the cones.

## 5. Required construction to close the bridge

1. Fix the six-bit convention against the traditional lower/upper trigram ordering and publish the lookup table for all 64 hexagrams.
2. Define explicit maps (\Phi_-,\Phi_+) from the two trigram spaces (or from the 64 paired states) into the proposed geometric sheets.
3. State whether the image is a set of points, cells, directions, or labels; these are not interchangeable.
4. Specify the metric and causal relation on the target and test which Q6 adjacency relations map to geometric incidence or causal adjacency.
5. Prove equivariance for the claimed symmetry subgroup. At minimum, verify that the action of (GL(3,2)\times GL(3,2)) on the two trigram factors agrees with the induced action on the two geometric sectors.
6. Compare the construction with the existing Vesica/Jitterbug records and preserve the distinction between point-set congruence and incidence embedding.

## 6. Monograph links

This record belongs to the common programme:
- chapters 2–5: Q6, binary vertices, Walsh filtration and finite cube symmetries;
- chapters 12–14: Anti-Twin, Vesica Piscis, two-sector geometry and Jitterbug;
- chapters 15–17: only if a compatible frame/coframe or Lorentzian structure is actually constructed.

Cross-links: T137 (Vesica), T142 (antipodal (3+3)), T143 (six-state isometric embedding), the Q6 affine/Walsh theorem record, and [PR #437](https://github.com/fabianleonaressi95/theorem/pull/437).

**No new theorem number is assigned here.** The exact combinatorial and Minkowski identities are recorded separately from the still-open Q6-to-cone geometric realization.
