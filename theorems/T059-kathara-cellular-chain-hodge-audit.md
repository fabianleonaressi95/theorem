# T059 — Cellular chain complex and Hodge operators of the filled Kathara planar graph

**Status:** exact finite-dimensional theorem, conditional on the explicit cell-filling convention below. This is a theorem about the reconstructed combinatorial object, not a physical claim about Kathara, Krist-All, or RGS–PSU.

## 1. Definitions

Take the 12-center, 21-edge planar graph of T058. Vertices are labeled 1,...,12. Each edge is oriented from its smaller endpoint to its larger endpoint. Declare the ten bounded planar regions to be 2-cells, with cyclic boundaries:

- F1=(1,2,3), F2=(1,4,2)
- F3=(2,4,7,5), F4=(2,5,6,3)
- F5=(5,7,10,8), F6=(5,8,9,6)
- F7=(8,10,11), F8=(8,11,9)
- F9=(9,11,12), F10=(10,12,11)

The source diagram supplies the graph/line inventory; declaring bounded regions to be 2-cells is an additional mathematical convention. The resulting finite CW complex is a disk.

Let C2 --B2--> C1 --B1--> C0 have dimensions 10, 21, 12. Columns of B1 are -e_u+e_v for each edge u→v. Each column of B2 is the signed oriented edge boundary of one face.

## 2. Boundary identity

Every oriented face boundary is a closed cycle, hence its vertex boundary vanishes:
B1 B2 = 0.
The implementation constructs integer matrices and checks this identity entry by entry.

## 3. Ranks, homology, and Euler characteristic

The graph is connected, so rank(B1)=12-1=11. The ten bounded face boundaries are linearly independent, so rank(B2)=10. Thus
(b0,b1,b2) = (12-11, 21-11-10, 10-10) = (1,0,0).
The Euler characteristic is chi=12-21+10=1=b0-b1+b2.

This is the homology of a disk. Do not confuse it with the graph-only cycle rank 21-12+1=10: those ten graph cycles are filled by the ten declared 2-cells.

## 4. Hodge Laplacians

For standard Euclidean inner products define
Delta0=B1 B1^T,
Delta1=B1^T B1+B2 B2^T,
Delta2=B2^T B2.
The audit constructs exact integer matrices of sizes 12x12, 21x21, and 10x10. They are symmetric positive semidefinite. Their harmonic kernel dimensions are b0,b1,b2, namely 1,0,0, by finite-dimensional Hodge theory.

Approximate spectral values may be added as numerical diagnostics, but the theorem relies on exact incidence identities and ranks, not floating-point diagonalization.

## 5. Consequences and limits

1. The filled Kathara graph is contractible as a 2-dimensional cell complex under the stated embedding and face convention.
2. The graph alone has cycle rank 10; filling its ten bounded faces kills first homology.
3. This gives a precise candidate cellular complex on which a Krist-All-type Hodge operator could be defined. It does not identify these operators with the previously named Krist-All operator.
4. No incidence-preserving chain map to the Q3 trigram cube or Q6 cubical complex has yet been constructed. The counts 12→8 vertices and 10→6 square faces do not define such a map.
5. Geometric/energetic interpretations in the source are not consequences of this theorem.

## 6. Reproducibility

Implementation: src/kathara_cellular_complex.py in the RGS–QLG Quaternion Bridge repository.
Tests: tests/test_kathara_cellular_complex.py.
The exact audit uses integer incidence matrices and rank elimination over Q; no external numerical package is required.
