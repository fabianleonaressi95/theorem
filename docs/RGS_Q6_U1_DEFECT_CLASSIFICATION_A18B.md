# A18b — Classification of compact-U(1) branch defects on Q6

**Status:** NUMERICAL_VERIFICATION (finite archived data)  
**Input:** A13 archived `psu_fibre_connection_matrices.npz` (`X`, `edges`, `R_SO3`).  
**Complex:** the full, non-periodic cubical 6-cube (I^6), not a 6-torus.

## Result

The 160 oriented 3-cells carry integer principal-branch defects
\[
m_{g;abc}=\operatorname{round}\!\left(
\frac{\Delta_a\bar\Theta_{g;bc}-\Delta_b\bar\Theta_{g;ac}
+\Delta_c\bar\Theta_{g;ab}}{2\pi}\right).
\]

| Charge | Number of 3-cells |
|---:|---:|
| -2 | 5 |
| -1 | 9 |
| 0 | 137 |
| +1 | 9 |

There are 23 nonzero cells and the signed sum is -10.

## Incidence components

Adjacency means that two charged 3-cells share an actual square 2-face in the cubical complex.

1. **Component C1:** 22 cells; charge sum -8; histogram `{-2:4, -1:9, +1:9}`.
2. **Component C2:** one isolated cell; base vertex 32, axes (0,1,2), charge -2; charge sum -2.

Thus the support has **two components** under square-face adjacency. This is a combinatorial classification of the support, not a claim that the components are physical objects.

## Integer closure and cohomology

The integer coboundary was evaluated on all 60 four-cells:
- maximum absolute value of (dm): **0**;
- nonzero four-cell boundaries: **0**.

Hence (m\in C^3(I^6;\mathbb Z)) is a cocycle. The full 6-cube is contractible, so
\[
H^3(I^6;\mathbb Z)=0.
\]
Consequently every closed integral 3-cochain is exact: (m=d\beta) for some integral 2-cochain \(\beta\). There is no nontrivial **absolute** degree-three cohomology obstruction on this non-periodic complex. This topological statement does not by itself construct a preferred \(\beta\), identify a physical monopole, or imply a continuum magnetic charge.

## Scope / limitations

- The 23 nonzero values are compact-angle principal-branch defects (lattice-monopole *candidates* only).
- The total charge -10 is not a neutrality violation: the domain is a finite cube with boundary, not a periodic torus.
- No continuum Bianchi equation, continuum limit, physical source interpretation, or monopole dynamics is established.
- The result is gauge-frame independent at the level of plaquette holonomy/branch charge, subject to the fixed principal-branch convention; the component graph uses cubical face incidence.

## Reproduction

Run `scripts/audit_rgs_q6_u1_defect_classification.py --npz PATH --out reports/RGS_A18B_U1_DEFECT_CLASSIFICATION_2026-11-26.json`.
