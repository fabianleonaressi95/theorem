# Purcell swimmer near a wall — reproducibility audit

This directory contains an independent Python reconstruction of the published
wall-corrected resistive-force model.

## Run

Dependencies: Python 3.10+, NumPy, SciPy.

```bash
python benchmark.py --amplitude 1e-3 --order 64
```

The script builds the generalized resistance matrix by Gauss–Legendre quadrature
of Jᵀ D J, with D = C_perp(I − eeᵀ/2), and integrates the four-stage
shape-velocity gait using DOP853. The outer-link arclength is integrated on
[0,L], while the central-link coordinate is integrated on [-L0/2,L0/2].
The geometric parameters match the article's example: unit link lengths,
initial wall distance 10^-2, and link radius 10^-4.

## Reproduced benchmark

For amplitude ξ = 10^-3, quadrature orders 16, 32, 48, 64 and 96 give
Δx/ξ² ≈ 0.06172485, approaching the published small-amplitude prediction
5/81 ≈ 0.06172840. The residual is consistent with finite-amplitude
corrections of order ξ. The initial control vector fields also reproduce
the analytic values reported in the article for L = λ = 1:

h¹ = (0, 1/6, −7/27, 1, 0),
h² = (0, −1/6, −7/27, 0, 1).

The structural test checks symmetry and positive definiteness of the
resistance matrix; the numerical test checks quadrature stability and
agreement with the published leading-order coefficient. This is a numerical
reproduction of the stated benchmark, not a proof of the paper's local
controllability theorem.

## Scope limit

No Q6-to-shape-space map is introduced. A discrete connection and a
refinement/holonomy statement remain open.

Primary source:
Micalizio et al. (2026), DOI 10.1007/s11012-026-02136-0,
https://link.springer.com/article/10.1007/s11012-026-02136-0
