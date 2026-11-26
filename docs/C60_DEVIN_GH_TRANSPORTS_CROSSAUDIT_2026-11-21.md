# Cross-audit: Devin vs GH transports on the ideal truncated icosahedron (C60)

Date: 2026-11-21
Script: `scripts/audit_c60_devin_gh_transports_crosscheck.py`
Output: `audits/C60_DEVIN_GH_TRANSPORTS_CROSSAUDIT.json`

## Scope

Two independent implementations of the discrete `SO(2)` connection on the
ideal truncated icosahedron (geometric C60 model, `p_ij = (2u_i+u_j)/3`):

- **devin**: self-contained construction inside the crosscheck script
  (icosahedron -> truncation -> Newell normals -> first-edge tangent frames
  -> `T_fg = t t^T + m_g m_f^T` -> `A_fg = B_g^T T_fg B_f` -> `D_f` on BFS/DFS
  dual spanning trees).
- **gh**: the repository pipeline `audit_c60_facewise_Df.py`, which builds the
  same objects via `audit_c60_icosahedral_connection.connection_data`
  (ConvexHull face reconstruction, SVD normals, seed-based frames) and
  `dual_tree`/`build_D` on root face 0.

The Devin `A_fg` are expressed in the GH frame gauge,
`A'_{p->g} = R_g^T A_fg R_p` with `R_f = B_devin,f^T B_GH,f`, then propagated
on the **same** GH tree with the same root. With frames, tree and root fixed,
no free gauge remains.

## Verified results

| Quantity | Residual |
|---|---|
| Vertex matching (60 vertices) | max distance 0.0 |
| Face matching | 32/32, all frame gauges proper rotations (`det R_f = +1`) |
| `A_fg` on GH tree edges, GH gauge | max residual **6.7e-16** |
| `D_f` on GH tree, GH gauge vs GH `D_f` | max residual **1.8e-15** (no free gauge) |
| Vertex holonomies: angle | max diff **2.8e-14 deg**, all exactly 12.000000000 deg |
| Vertex holonomies: trace / det | max diff ~3e-15 |
| Vertex holonomies: full `SO(2)` matrices | max diff **1.7e-15**, signs 60/60 |

The holonomy comparison uses full matrices, traces, determinants and signs —
not only angles — so it excludes distinct matrices with equal trace.

## The global gauge `C = -108 deg`: explained

When Devin's `D_f` is kept in **Devin frames** and compared to GH's `D_f`, a
single global rotation `C` is needed. Analytically `C = R_{f0}`, the frame
gauge at the shared root face: from `B'_f = B_f R_f` and
`A'_fg = R_g^T A_fg R_f`, tree propagation gives `D'_f = R_f^T D_f R_{f0}`.

Numerically the fitted `C` is exactly `-108.000000 deg`, equal to the angle
of `R_0` (GH root face 0, a pentagon, in Devin-vs-GH frame gauge). The
coincidence with the pentagon's interior angle is a convention artifact:
pentagon frame gauges take only multiples of 36 deg, and GH selected that
root/frame. `C` is covariant under root/frame changes, not an invariant.

## `M_f` norm is gauge-dependent (negative result)

Mean `||M_f|| = ||B_f (I_2 - D_f)||_F` under three gauges:

| Gauge | mean `||M_f||` |
|---|---|
| Devin `A_fg` in GH gauge on GH tree | 1.30293 (= GH value, diff 2e-15) |
| GH (`audit_c60_facewise_Df`) | 1.30293 |
| Devin BFS tree | 1.58822 |
| Devin DFS tree | 1.87006 |

`||M_f||` changes with tree/frame/root: it is **not** an invariant of the
connection and cannot be read as a physical disarrangement density.

Note: artifacts previously exported under `~/Immagini/` were produced by an
earlier frame convention of the GH pipeline; they differ from the current
in-repo frames by a pure per-face gauge (3 distinct angles, residual 4e-16)
and yield `mean ||M_f|| = 1.2014`. Both values are gauge artifacts; the
in-repo numbers above are the canonical comparison.

## Classification

| Result | Status |
|---|---|
| C60 geometry reconstruction | verified numerically |
| Discrete connection `A_fg` | **independent replica verified** |
| Local 12 deg holonomies (full matrices) | **independent replica verified** |
| Total curvature 4 pi | discrete Gauss-Bonnet check |
| Global gauge `-108 deg` | explained: `C = R_{f0}`, convention artifact |
| Mean `||M_f||` | gauge-dependent, not an invariant |
| `G_f`, `M_f` fields | algebraic candidates pending a global `g` |
| Del Piero-Owen admissibility | **open problem** |

The discrete connection and its holonomies are consolidated as a verified
result, independent of the open DPO question.
