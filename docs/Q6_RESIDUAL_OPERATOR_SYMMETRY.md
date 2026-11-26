# Q6 residual operator-symmetry audit

**Status:** numerical audit, not a theorem.

## Question

Among the 48 signed coordinate permutations preserving the reconstructed 64-point
cloud, which also preserve the Q6 graph and the stored RGS operators?

## Method

For each signed permutation matrix (M\in O_h), match (X M^T) back to the
64 rows of `X_Oh_reconstructed`, obtaining a state permutation (P). Test
`P.T @ Q6_adjacency @ P = Q6_adjacency`.

For the 188D operators, let (B=`A_geometry_orthonormal`\in\mathbb R^{188\times64}).
Its columns are orthonormal. We declare the extension
[
U(P)=BPB^T+(I-BB^T),
]
which acts by (P) on `range(B)` and by the identity on its 124D orthogonal
complement. This extension is a convention: the stored 64D state action alone
does not uniquely determine an action on the complement.

We test (U^T O U=O) for `K0`, `R_geo_tangent`, `T_transport`, and `P_G`.
We additionally test the compressed 64D matrices (B^T O B), independently
of the chosen complement extension.

## Numerical outcome

The audit enumerates all 48 coordinate signed permutations. Exactly 16 preserve
Q6 adjacency. All 16 preserve `R_geo_tangent` under the declared extension.
Only the identity among those 16 preserves `K0`, `T_transport`, or `P_G`;
the same identity-only result holds for their 64D compressions.

Consequently, no nontrivial common symmetry of the tested complete operator
data is established. This is not evidence that the C60 face representation is
false: it says the proposed state-coordinate action does not extend to a
nontrivial symmetry of these stored operators under the specified convention.

## Reproducibility

```bash
python scripts/audit_q6_residual_operator_symmetry.py \
  data/RGS_PSU_all_matrices.npz \
  --out audits/Q6_residual_operator_symmetry.json
```

Threshold: relative Frobenius residual (10^{-10}).
