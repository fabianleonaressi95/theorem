# T065 — Exact cubical subdivision chain map and signed-permutation naturality

**Status:** proved for the standard oriented cubical grid.

## 1. Setting

Let (K_N) be the cubical cell complex of the grid ([0,N]^d), with integer cellular chains (C_k(K_N;mathbb Z)). Orient each (k)-cell by the increasing order of its active coordinate axes. Let
[
c=(v;i_1,ldots,i_k),qquad i_1<cdots<i_k
]
be an oriented coarse cell.

The doubled grid is (K_{2N}). Define (S_k:C_k(K_N;mathbb Z)	o C_k(K_{2N};mathbb Z)) by
[
S_k(c)=sum_{epsilonin{0,1}^k}
left(2v+sum_{r=1}^kepsilon_r e_{i_r};,i_1,ldots,i_kight).
]
Coordinates not belonging to the active axes are doubled without an offset. Every fine subcell inherits the orientation of (c).

## 2. Theorem

For every (k),
[
oxed{partial_{2N}S_k=S_{k-1}partial_N.}
]
Thus (S=(S_k)_k) is an integral chain map. Each coarse (k)-cell is subdivided into exactly (2^k) fine (k)-cells.

Let (P) be any signed permutation matrix and let (T_N,T_{2N}) be the induced oriented cellular maps on the coarse and fine grids, including the corresponding reflection offsets. Then
[
oxed{T_{2N}S_k=S_kT_N.}
]
The subdivision is therefore natural under the full signed-permutation symmetry group of the cube, of order (3!,2^3=48) in dimension three.

## 3. Proof

Apply the cellular boundary operator to the sum defining (S_k(c)). Every fine face internal to the coarse cell is incident to exactly two fine subcells. Their induced orientations are opposite, so these terms cancel. The uncancelled faces lie on the boundary of the coarse cell. For each such face, the remaining fine faces are exactly the subdivision of that coarse boundary face, with the same induced orientation. Hence
[
partial_{2N}S_k(c)=S_{k-1}(partial_Nc).
]
Linearity gives the chain identity on all chains.

A signed coordinate permutation sends the active axes of a coarse cell bijectively to the active axes of its image. It sends the fine subcells bijectively to the fine subcells of that image. The orientation sign of the permutation is the same on the coarse cell and on each of its fine subcells. The two compositions therefore have identical cells and coefficients, proving (T_{2N}S_k=S_kT_N). (square)

## 4. Finite computational verification

The implementation audit enumerates the oriented cells of ([0,N]^3), constructs all subdivision chains over integers, and checks both identities cell by cell. It also checks all 48 signed-permutation symmetries. The CI run #92 (9 November 2026, commit `6fd5ab9`) completed the subdivision/naturality audit and its regression tests successfully.

The finite audit is a reproducibility check. The universal statements above follow from the boundary-cancellation and symmetry arguments, not from the finite enumeration.

## 5. Scope and non-conclusions

This theorem concerns the standard cubical subdivision (K_N	o K_{2N}). It does **not** prove that:

- a mixed-parity voxel recursion is this cubical subdivision;
- Herasymov's source recursion defines a conforming geometric mesh;
- a Kathara, Krist-All, Q6, or RGS–PRISM complex is canonically identified with this grid;
- FEEC stability, discrete compactness, Mosco convergence, norm-resolvent convergence, or spectral convergence holds for a curved refinement family.

Those are separate statements requiring their own maps and hypotheses.
