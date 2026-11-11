# M3 D4 orbit-edge Hodge: independent verification record

**Scope:** independent reconstruction of the orbit-edge two-dimensional cell complex on the PR #139 branch. This record distinguishes exact integer/rational checks from floating-point spectral reconnaissance.

## Construction and exact checks

Starting from the 64 Q6 vertices, the generators
```
R(b1,b2,b3,s1,s2,s3) = (b1,b2,b3 xor b1 xor b2,s2,1 xor s1,s3)
S(b1,b2,b3,s1,s2,s3) = (b1,b2,b3,1 xor s1,s2,s3)
```
generate a group of order 8.

Taking the orbit of the 192 original unoriented edges and of the 240 original cyclic square boundaries gives:

| Quantity | Result |
|---|---:|
| vertices | 64 |
| orbit edges | 256 |
| distinct cyclic square 2-cells | 384 |
| rank(B1) over Q | 63 |
| rank(B2) over Q | 190 |
| beta1 = 256 - rank(B1) - rank(B2) | **3** |

The 384 cells retain distinct cyclic boundaries even when their four-vertex sets coincide.

The following were checked exactly with integer matrices / rational rank:
- B1 B2 = 0;
- all eight signed D4 actions are chain maps: J0 B1 = B1 J1 and J1 B2 = B2 J2;
- rank(B1)=63 and rank(B2)=190.

Consequently the first homology of this finite chain complex has dimension 3 over Q. This is a homology statement about the specified chain complex; it does not by itself establish that the cell structure is a regular CW complex.

## Coexact spectrum: numerical reconnaissance

For Hco = B2 B2^T, a symmetric floating-point eigensolver gives the following clustered spectrum:

| Approximate eigenvalue | Multiplicity |
|---:|---:|
| 0 | 66 |
| 2 | 11 |
| 4 | 20 |
| 6 | 29 |
| 8 | 50 |
| 10 | 53 |
| 12 | 24 |
| 14 | 3 |

The positive multiplicities sum to 190, agreeing with the exact rank of B2. No positive eigenvalue cluster has multiplicity 5.

**Status of this spectral table:** numerical, not yet a rational characteristic-polynomial certificate. The exact rank and chain-map results above do not depend on this numerical diagonalization.

## Consequence for the D5 search

The particular orbit-edge complex defined here does **not** reproduce a positive five-dimensional coexact eigenspace. Therefore the proposed direct route from this complex to a five-mode D5 chart is not supported by the current spectrum.

The earlier five-dimensional vertex-Laplacian eigenspace at eigenvalue 4 remains a separate exact result. The original Q6 coexact five-dimensional eigenspace at eigenvalue 12 also remains separate, with the previously established D4 intertwiner obstruction.

## Reproduction boundary

The exact construction/rank/chain-map checks were independently reconstructed using the same six-bit generators and cyclic-square convention. The floating spectrum was computed from the resulting 256 by 256 coexact Hodge matrix. The repository's full SymPy audit script and pytest file have not been executed in the GitHub Actions environment; in particular, the exact algebraic spectrum and per-eigenspace D4 character table remain open.
