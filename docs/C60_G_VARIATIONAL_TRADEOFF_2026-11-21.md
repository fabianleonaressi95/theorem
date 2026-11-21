# Variational trade-off for the piecewise-affine candidate g on C60

Date: 2026-11-21
Script: `scripts/c60_g_variational_tradeoff.py`
Output: `audits/c60_g_variational_tradeoff_2026-11-21.json`
Depends on: `scripts/c60_truncated_icosahedron_transports.py`

## Problem

The connection fixes the elastic candidate `G_f = B_f D_f`. Two extremes:

- `g` = identity (`∇g|_f = B_f`, `E_f = I`): zero edge jumps, but
  `M_f = B_f(I − D_f)` large.
- `g` following the connection (`E_f = D_f`): `M_f = 0`, but edge jumps
  from the 12-degree vertex holonomy.

Well-posed version: let `φ_f ∈ SO(2)` be **free** per face
(`∇g|_f = B_f rot(φ_f)`), `g_f(x) = Q_f(φ_f) x + t_f` with translations `t_f`
fixed by least squares on the dual graph, and minimize

```
F(φ; μ) = J(φ) + μ · Σ_f ‖B_f(E_f − D_f)‖²_F
        = J(φ) + 2μ Σ_f (1 − cos(φ_f − θ_f))
```

`J(φ)` = sum of squared minimal edge jumps (180 endpoint residuals,
90 dual edges). `μ → 0` gives the identity; `μ → ∞` forces `φ → θ_D`.

## Pareto frontier (Devin BFS reference field)

| μ | J (jump energy) | M-term (Σ‖M_f‖²) | rms jump |
|---|---|---|---|
| 0 | 0.000 | 53.245 | 0.000 |
| 1e-3 | 0.000 | 53.237 | 0.000 |
| 0.01 | 0.0004 | 53.164 | 0.0015 |
| 0.1 | 0.040 | 52.439 | 0.015 |
| 0.3 | 0.357 | 50.852 | 0.045 |
| 1 | 3.919 | 45.373 | 0.148 |
| 3 | 104.3 | 2.473 | 0.761 |
| 10 | 113.6 | 0.051 | 0.795 |
| 100 | 114.49 | 0.0004 | 0.798 |

References: `J(identity) = 0`, `J(D_BFS) = 114.56`, `J(D_DFS) = 116.05`.

## Reading

- The transition is sharp between μ ≈ 1 and μ ≈ 3.
- At μ = 100 the optimizer converges to `J = 114.49 < J(D_BFS) = 114.56`:
  the tree-propagated `D_f` is **not** the jump-minimizing section of the
  connection — the optimal φ improves it only marginally (~0.06%), so the
  tree gauge is already near-optimal for this functional.
- **Minimal jump energy at M = 0 is ≈ 114.5** — this is the quantitative
  form of the holonomy obstruction: any g whose facewise gradient follows
  the connection must pay ~114 units of squared jump (rms ≈ 0.80 per
  endpoint, larger than the 2/3 edge length).
- Conversely, allowing `Σ‖M_f‖² ≈ 50` (i.e. `⟨‖M_f‖⟩ ≈ 1.25`) buys perfect
  continuity. The frontier quantifies the price of the disarrangement.

## Status

- `g(φ*(μ))` is an explicit piecewise-affine map for every μ — a one-parameter
  family interpolating identity ↔ connection-following deformation.
- Still open: gauge-invariant formulation, Del Piero–Owen admissibility
  (determining sequence of injective approximants), and the RGS–PRISM
  analogue (no canonical transports defined there yet).
