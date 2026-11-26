# Q6 embedded-sector / 188D operator block audit

**Classification:** numerical structural audit.

Let (B=`A_geometry_orthonormal`\in\mathbb R^{188\times64}), with
(B^TB=I_{64}), and (C=I_{188}-BB^T). This defines an embedded 64D
sector and its 124D orthogonal complement.

For each archived operator (O), the cross-blocks
[
B^TOC,\qquad COB
]
measure coupling between the embedded sector and its complement. The audit
uses relative Frobenius norms, normalized by (|O|_F).

## Results

| Operator | (\|B^TOC\|/\|O\|) | (\|COB\|/\|O\|) | Interpretation |
|---|---:|---:|---|
| (K_0) | 0.3314135 | 0.3314135 | couples both ways |
| (R_{geo}) | approximately 0 | approximately 0 | reduces the decomposition |
| (T_{transport}) | approximately 0 | 0.8171329 | one-way coupling |
| (P_G) | 0.3850532 | 0.3850532 | couples both ways |

Thus only (R_{geo}) is block diagonal with respect to this embedding.
In particular, the 64D embedding is not a reducing subspace for (K_0),
(T_{transport}), or (P_G).

## Consequence

A 64D permutation representation cannot be promoted to a canonical 188D
representation from (B) alone. The earlier extension
(U=BPB^T+(I-BB^T)) is a useful declared test convention, but is not a
geometrically derived action. A genuine lift requires the missing geometric
action on the 124D complement, or a documented row-to-edge map for
`Q_tangent` from which the 188D subspace action can be derived.

The archive does not currently supply that row-to-edge map. We therefore do
not claim to have reconstructed a full 188D (T_h) or (I_h) representation.

## Reproduce

```bash
python scripts/audit_q6_embedding_operator_block_structure.py \
  data/RGS_PSU_all_matrices.npz \
  --out audits/Q6_embedding_operator_block_structure.json
```
