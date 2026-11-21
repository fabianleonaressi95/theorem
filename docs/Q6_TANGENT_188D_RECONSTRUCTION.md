# Exact reconstruction of the Q6 action on the 188D tangent space

**Status:** reconstructed representation; numerical verification.

## Correction of the row interpretation

The 192 rows of `Q_tangent` are not the 192 edges of Q6. They are the
192 Cartesian displacement coordinates of the 64 embedded vertices:
[
\mathbb R^{192}=(\mathbb R^3)^{64},\qquad
\delta X=(\delta X_1,\ldots,\delta X_{64}).
]
This follows directly from the A14 constraint Jacobian: its first three rows
are the uniform x-, y-, and z-translation covectors in vertex-major
((x_i,y_i,z_i)) order, and its fourth row is (X_{flat}^T).
The equality between 192 coordinate degrees of freedom and 192 graph edges
was only a dimensional coincidence.

## Reconstructed action

For each signed coordinate permutation (T\in O_h), recover the unique
vertex permutation (p) by matching (XT^T) to (X). Retain the
transformations that preserve Q6 adjacency. The ambient action (S) is
defined by
[
x'_{p(i)}=T x_i
]
and acts on each vertex displacement triple by the same (T). Its induced
tangent representation is
[
U(T,p)=Q^T S(T,p)Q.
]
The test is basis-independent at the subspace level:
[
SQQ^TS^T=QQ^T,
]
with the equivalent intertwining check (SQ=QU).

## Numerical result

- 48 signed coordinate permutations tested.
- 16 preserve both the reconstructed point cloud and Q6 adjacency.
- All 16 preserve the 188D tangent subspace.
- Maximum projector-invariance residual: (1.34\times10^{-14}).
- Maximum intertwiner residual: (1.95\times10^{-14}).
- Maximum induced orthogonality residual: (3.86\times10^{-14}).
- Group closure: 0 failures among all 256 pairwise products.

## Operator covariance

| Operator | Covariant elements |
|---|---:|
| (R_{geo,tangent}) | 16/16 |
| (K_0) | 1/16 |
| (P_G) | 1/16 |
| (T_{transport}) | 1/16 |

Thus the tangent representation is now explicitly reconstructed. The
operator failures are genuine failures under this action; they are not
artifacts of guessing an edge ordering or extending the action arbitrarily
to a complement.

## Reproduction

```bash
python scripts/reconstruct_q6_tangent_188d_action.py \
  data/RGS_PSU_all_matrices.npz \
  --out audits/Q6_tangent_188D_reconstruction.json \
  --matrices audits/Q6_tangent_188D_actions.npz
```
