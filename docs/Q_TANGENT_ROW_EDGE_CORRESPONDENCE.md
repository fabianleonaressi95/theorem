# Q_tangent row / Q6 edge correspondence audit

**Classification:** structural numerical audit; row-edge map unresolved.

The archive stores `Q_tangent` with shape (192\times188) and
`Q6_adjacency) with 192 undirected edges. The matching count is suggestive,
but it is not a mathematical identification of row (r) with graph edge (e_r).

## Verified matrix structure

Numerically,
[
\|Q^TQ-I_{188}\|_F=1.31\times10^{-14}.
]
Thus (Q) has full column rank 188 and is an isometric embedding of the
188D tangent-coordinate space into (mathbb R^{192}). Its row-space projector
(H=QQ^T) is idempotent to approximately (2.2\times10^{-14}). The
orthogonal complement (I-H) has rank 4.

The row leverage scores of this complement have six distinct values at
(10^{-8}) rounding, with multiplicities (48,48,24,24,24,24). These
basis-independent row invariants describe the 192 row positions, but do not
identify them with named Q6 edges.

## Why the lift cannot yet be computed

To induce a state-graph symmetry on the tangent frame, one needs a specific
edge permutation matrix (S) acting on the 192 row coordinates. The induced
188D action would then be
[
U=Q^TSQ,
]
provided (S) preserves the column space of (Q), equivalently
[
S(QQ^T)S^T=QQ^T.
]
But constructing (S) requires the missing row-to-edge correspondence. The
archive contains no `row_to_edge` array and no construction metadata that
specifies the ordering. Equal cardinalities alone do not supply that map.

## Required input

Add a 192-entry `row_to_edge` array of canonical endpoint pairs
((i,j)), (i<j), each an edge of `Q6_adjacency`, plus the orientation/sign
convention used when constructing each row of `Q_tangent`. With those data,
the induced actions and operator commutators can be computed without arbitrary
extensions.

## Reproduce

```bash
python scripts/audit_q_tangent_row_edge_correspondence.py \
  data/RGS_PSU_all_matrices.npz \
  --out audits/Q_tangent_row_edge_correspondence.json
```
