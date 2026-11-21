# Q6 tangent representation: irreducible decomposition and operator blocks

**Status:** numerical representation-theoretic audit of the reconstructed action.

## 1. Group

The 16 transformations preserving both the reconstructed point cloud and Q6 adjacency form a closed group. Its element-order distribution is 1 identity, 11 elements of order 2, and 4 of order 4. Its center has order 4, its derived subgroup order 2, and its abelianization order 8. The resulting group is
\[
G\cong D_8\times C_2.
\]

The multiplication table is reconstructed from the signed coordinate transformations and their induced vertex permutations; all 256 products close.

## 2. Irreducible decomposition

The real irreducibles consist of eight one-dimensional characters and two two-dimensional characters. The labels \(\chi_{01},\ldots,\chi_{10}\) are computational labels, not conventional Mulliken labels.

| Irrep | Dimension | Multiplicity | Isotypic dimension |
|---|---:|---:|---:|
| \(\chi_{01}\) | 1 | 13 | 13 |
| \(\chi_{02}\) | 1 | 10 | 10 |
| \(\chi_{03}\) | 1 | 14 | 14 |
| \(\chi_{04}\) | 1 | 10 | 10 |
| \(\chi_{05}\) | 1 | 10 | 10 |
| \(\chi_{06}\) | 1 | 14 | 14 |
| \(\chi_{07}\) | 1 | 10 | 10 |
| \(\chi_{08}\) | 1 | 13 | 13 |
| \(\chi_{09}\) | 2 | 23 | 46 |
| \(\chi_{10}\) | 2 | 24 | 48 |
| **Total** | | | **188** |

The character row-orthogonality residual is zero in floating-point arithmetic. The ten isotypic projectors have idempotence residuals of order \(10^{-14}\), and commute with the representation to the same precision.

## 3. Operator covariance and block coupling

For each operator \(M\), covariance means \(U(g)^T M U(g)=M\) for every \(g\in G\). The off-isotypic block ratio is
\[
\frac{\left(\sum_{\alpha\ne\beta}\|P_\alpha M P_\beta\|_F^2\right)^{1/2}}{\|M\|_F},
\]
where \(P_\alpha\) are the ten isotypic projectors.

| Operator | Rank | Covariant elements | Off-isotypic ratio | Change under group average |
|---|---:|---:|---:|---:|
| \(K_0\) | 124 | 1/16 | 0.642681 | 0.675716 |
| \(P_G\) | 64 | 1/16 | 0.748115 | 0.786763 |
| \(T_{transport}\) | 64 | 1/16 | 0.846345 | 0.905705 |
| \(R_{geo,tangent}\) | 188 | 16/16 | \(1.39\times10^{-15}\) | \(1.36\times10^{-15}\) |

The change under group averaging is the relative Frobenius distance from \(M\) to its Reynolds average
\[
\mathcal R_G(M)=\frac1{|G|}\sum_{g\in G}U(g)^T M U(g),
\]
which is the Frobenius-orthogonal projection onto the invariant operator subspace. It is not a harmless basis change. In particular, the averaged ranks of \(K_0,P_G,T_{transport}\) are respectively 188, 188, and 128, rather than their original ranks 124, 64, and 64.

## 4. Interpretation

1. The tangent representation itself is now decomposed into its irreducible isotypic sectors.
2. \(R_{geo,tangent}\) is block diagonal across isotypic sectors and satisfies the full group covariance test to numerical precision.
3. \(K_0,P_G,T_{transport}\) contain substantial couplings between inequivalent isotypic sectors. Their failure is therefore structural for the archived matrices under the reconstructed action, not a mere coordinate relabeling.
4. The data do not yet identify whether these defects arise from a deliberate symmetry-breaking construction, a gauge choice, or a bug in the original operator-generation pipeline. That requires tracing the definitions of those three matrices.
5. Do not replace the archived matrices by their Reynolds averages without a separate mathematical decision: the averages materially change their ranks and values.

## 5. Reproduction

```bash
python scripts/audit_q6_irreducible_operator_decomposition.py \
  data/RGS_PSU_all_matrices.npz \
  --out audits/Q6_D8xC2_irreducible_operator_decomposition.json \
  --projectors audits/Q6_D8xC2_isotypic_projectors.npz
```

The script reconstructs the group, builds its character projectors, audits the operator blocks, writes the JSON report, and saves the ten projectors and four Reynolds averages in the NPZ output.
