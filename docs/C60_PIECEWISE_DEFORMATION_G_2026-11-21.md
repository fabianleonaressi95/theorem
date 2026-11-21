# Piecewise-affine candidate g on the ideal truncated icosahedron (C60)

Date: 2026-11-21
Scripts: `scripts/c60_truncated_icosahedron_transports.py`,
`scripts/c60_piecewise_deformation.py`
Outputs: `audits/c60_piecewise_deformation_2026-11-21.{json,npz}`

## Motivation

The discrete connection audit (`C60_DEVIN_GH_TRANSPORTS_CROSSAUDIT`) verified
`A_fg`, `D_f` and the 12-degree vertex holonomies, but left `G_f = B_f D_f`
and `M_f = ∇g|_f − B_f D_f` as algebraic candidates: no global `g` had been
constructed. This note constructs the canonical piecewise-affine candidate and
quantifies the obstruction.

## Construction

For each face `f` (32 faces: 12 pentagons + 20 hexagons):

- `D_f ∈ SO(2)` from the dual-tree transport field (`D_g = A_fg D_f`).
- `Q_f = B_f D_f B_f^T + n_f n_f^T ∈ SO(3)`: rotation by `θ_f = arg(D_f)`
  about the outward normal `n_f`. Verified: `Q_f B_f = B_f D_f`, so the
  facewise gradient of `g` is `dg|_f = B_f D_f = G_f` (3x2).
- `g_f(x) = Q_f x + t_f`: affine isometry per face. The translations `t_f`
  are pure gauge; they are fixed by least squares on the dual graph so that
  edge jumps are minimized (`t_f − t_g = (Q_g − Q_f)·midpoint`).

## The obstruction is real

A *globally compatible* `g` (continuous across edges with `∇g|_f = B_f`)
does not exist: the vertex holonomy is 12 degrees on all 60 vertices. The
piecewise `g` above therefore has jump discontinuities — which is precisely
the setting where Del Piero–Owen disarrangements live (g only needs to be
bounded, discontinuities on a negligible set are admissible).

## Numerical results (Devin BFS gauge)

| Quantity | Value |
|---|---|
| Edge jump ‖·‖ mean / max | 0.745 / 1.497 (edge length = 2/3) |
| Jump on tree edges mean / max | 0.705 / 0.944 |
| Jump on non-tree edges mean / max | 0.766 / 1.152 |
| Vertex image spread mean / max | 0.557 / 0.917 |
| Vertex holonomy | 12.000000000 deg on all 60 vertices |
| `M_f = ∇g|_f − G_f` | 0 identically (by construction) |

Under the DFS gauge the mean jump changes (0.745 → 0.755): **the jump field
is gauge-dependent**, like `D_f` itself. The gauge-invariant content is the
holonomy (12 deg per vertex, 4π total).

## Interpretation — careful

- `g` is now an explicit piecewise-affine map with `∇g|_f = G_f = B_f D_f`.
- The disarrangement candidate is carried by the **jumps**, not by
  `M_f = ∇g − G_f` (which vanishes identically for this g).
- Jumps are large because the tree-propagated `D_f` field varies strongly
  between adjacent faces; a gauge minimizing total jump is an open
  optimization problem (the "closest flat connection" analogue).
- DPO admissibility (existence of determining sequence of injective
  approximants, orientation conditions on the 3x2 gradients) remains
  **open**.

## Relation to previous audits

- Connection + holonomies: verified, independent replica (see
  `C60_DEVIN_GH_TRANSPORTS_CROSSAUDIT_2026-11-21.md`).
- `M_f` norm: gauge-dependent, not an invariant.
- This note: first explicit `g` candidate; disarrangement = edge jumps,
  still gauge-dependent pending a gauge-invariant formulation.
