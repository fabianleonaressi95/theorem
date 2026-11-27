# A18c — Explicit integral primitive for the Q6 branch-defect cocycle

**Classification:** NUMERICAL_VERIFICATION + exact integer cochain identity.

Let (m\in C^3(I^6;\mathbb Z)) be the A18 integer cube-charge cochain reconstructed from principal plaquette angles. Solve
\[
D_2\beta=m,\qquad D_2:C^2(I^6;\mathbb Z)\to C^3(I^6;\mathbb Z),
\]
with rows indexed by 160 oriented 3-cells and columns by 240 oriented square faces:
\[
(D_2\beta)_{g;abc}=\Delta_a\beta_{g;bc}-\Delta_b\beta_{g;ac}+\Delta_c\beta_{g;ab}.
\]

An integer mixed-integer optimization (HiGHS) minimizes \(\|\beta\|_1\). It returns an optimum with L1 norm 18, 18 nonzero coefficients (all ±1), and exact residual \(\max|D_2\beta-m|=0\) on all 160 cube equations.

Face notation `(g;a,b)` denotes the positively oriented square based at bit-vertex (g), (a<b). One explicit primitive is
\[
\begin{aligned}
\beta={}&+[(0;0,1)+(8;0,1)+(16;0,1)+(28;0,1)\\
&+(32;0,1)+(40;0,1)+(48;0,1)+(56;0,1)]\\
&-[(0;0,2)+(8;0,2)+(18;0,2)+(24;0,2)\\
&+(32;0,2)+(40;0,2)+(48;0,2)+(56;0,2)]\\
&-[(8;1,2)]+[(9;1,2)].
\end{aligned}
\]
Direct integer recomputation verifies \(D_2\beta=m\) exactly on all 160 3-cells.

## Nonuniqueness and interpretation

This primitive is not unique. If \(\gamma\in C^2(I^6;\mathbb Z)\) is closed, then \(\beta+\gamma\) has the same coboundary. The L1 minimizer is one sparse representative for the fixed cubical orientation and principal-branch convention, not a canonical physical gauge choice.

The integer 2-cochain is not identified with a physical Dirac sheet. No physical monopole, continuum magnetic source, or continuum limit is established.

## Reproduction

Requires Python, NumPy, and SciPy with `scipy.optimize.milp` (HiGHS):
```bash
python scripts/solve_rgs_q6_u1_defect_primitive_a18c.py --npz /path/to/psu_fibre_connection_matrices.npz --out reports/RGS_A18C_U1_EXPLICIT_PRIMITIVE_2026-11-27.json
```
