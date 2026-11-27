# A18c — Explicit integral primitive for the Q6 branch-defect cocycle

**Classification:** NUMERICAL_VERIFICATION + exact integer cochain identity  
**Parent:** A18/A18b, Q6 finite compact-`U(1)` audit.

## Constructive result

Let (m\in C^3(I^6;\mathbb Z)) be the integer cube-charge cochain reconstructed from the principal plaquette angles in A18. We solve the integer system
\[
D_2\,\beta=m,\qquad
D_2:C^2(I^6;\mathbb Z)\longrightarrow C^3(I^6;\mathbb Z),
\]
where rows are the 160 oriented 3-cells, columns are the 240 oriented square faces, and
\[
(D_2\beta)_{g;abc}
=\Delta_a\beta_{g;bc}-\Delta_b\beta_{g;ac}
 +\Delta_c\beta_{g;ab}.
\]

An integer mixed-integer optimization (HiGHS) minimizes \(\|\beta\|_1\). It returns an optimum with
- \(\|\beta\|_1=18\);
- 18 nonzero face coefficients, each equal to \(+1\) or \(-1\);
- exact residual \(\max|D_2\beta-m|=0\) on all 160 cube equations.

The solver reports an optimal solution for this L1 objective. The explicit primitive is listed below. Face notation `(g;a,b)` means the positively oriented square based at bit-vertex (g), with (a<b).

## Explicit primitive

\[
\begin{aligned}
\beta={}&+[(0;0,1)+(8;0,1)+(16;0,1)+(28;0,1)\\
&+(32;0,1)+(40;0,1)+(48;0,1)+(56;0,1)]\\
&-[(0;0,2)+(8;0,2)+(18;0,2)+(24;0,2)\\
&+(32;0,2)+(40;0,2)+(48;0,2)+(56;0,2)]\\
&-[(8;1,2)]+[(9;1,2)].
\end{aligned}
\]

The direct recomputation gives
\[
\boxed{D_2\beta=m\quad\text{exactly on all 160 3-cells}.}
\]

## Gauge / representative freedom

This is one integral primitive, not a unique or canonical one. If \(\gamma\in C^2(I^6;\mathbb Z)\) is closed ((d\gamma=0)), then \(\beta+\gamma\) has the same coboundary. The L1 minimizer selects a sparse representative relative to the chosen cubical orientations and principal-branch charge convention; it is not a physical gauge choice.

The calculation also does **not** identify \(\beta\) with a physical Dirac sheet. It is an integer 2-cochain whose coboundary reproduces the compact-angle branch defects. No physical monopole, continuum magnetic source, or continuum limit is established.

## Reproduction

Requires Python, NumPy, and SciPy with `scipy.optimize.milp` (HiGHS):
```bash
python scripts/solve_rgs_q6_u1_defect_primitive_a18c.py \
  --npz /path/to/psu_fibre_connection_matrices.npz \
  --out reports/RGS_A18C_U1_EXPLICIT_PRIMITIVE_2026-11-27.json
```
