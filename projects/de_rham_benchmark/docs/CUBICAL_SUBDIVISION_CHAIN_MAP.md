# Exact cubical subdivision chain map

## Construction

Let the coarse cubical grid be (K_N=[0,N]^3), and the fine grid be
(K_{2N}=[0,2N]^3). For a positively oriented coarse (k)-cell
[
c=(v; i_1,ldots,i_k), qquad i_1<cdots<i_k,
]
define
[
S_k(c)=
sum_{epsilonin{0,1}^k}
(2v+epsilon_{i_1}e_{i_1}+cdots+epsilon_{i_k}e_{i_k};
 i_1,ldots,i_k).
]
The coordinates not in the active axes are doubled without an offset.
Every fine subcell inherits the orientation of the coarse cell.

Thus a vertex maps to one fine vertex, an edge to two edges, a square
to four squares, and a cube to eight cubes. The coefficients are integers.

## Exact identities

The audit checks, cell by cell and over integer chains,
[
partial_{2N}S_k=S_{k-1}partial_N,qquad k=1,2,3.
]
It also checks naturality under every signed permutation matrix (T)
(the 48 symmetries of the cube):
[
T_{2N}S_k=S_kT_N.
]
This is stronger than checking only the 32 distinct coordinate maps
observed in Herasymov's rotation-enhanced source.

## Scope and limitations

This is the standard cubical subdivision operator. It is an exact
coarse-to-fine chain map and is equivariant under the full signed-permutation
symmetry group. It is **not** yet a reconstruction of the mixed
parity-selected Herasymov recursion as a geometric subdivision.

To identify that recursion with (S_k), one still needs explicit cell
images and shared-face restrictions for all eight parity rules. The
remaining FEEC obligations include bounded commuting projections,
uniform metric/Jacobian bounds, discrete compactness, and a Mosco or
norm-resolvent convergence argument. No such convergence theorem is
claimed here.

## Reproducibility

```bash
python projects/de_rham_benchmark/audits/audit_cubical_subdivision_chain_map.py --size 2
pytest -q projects/de_rham_benchmark/tests/test_cubical_subdivision_chain_map.py
```
