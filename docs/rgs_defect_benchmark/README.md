# RGS–PRISM defect benchmark: first computational baseline

This prototype establishes a deliberately modest B0–B4 baseline for discussion with DISMA.

## What it does

- **B0:** builds integer incidence matrices on a square cell complex and checks the exact identity `d1 @ d0 == 0`.
- **B1:** checks a manufactured affine displacement under Dirichlet boundary data and the zero-source zero-energy case.
- **B2:** solves isotropic 2D linear elasticity with a smooth, localized prescribed plastic eigenstrain.
- **B3:** solves a pair of opposite smooth eigenstrain inclusions.
- **B4:** repeats the single-source case over mesh levels and records the empirical energy refinement trend.

The element energy uses Q1 bilinear quadrilaterals with full 2x2 Gauss integration and isotropic Lamé elasticity. The local strain vector is `[epsilon_xx, epsilon_yy, gamma_xy]`.

## Important scientific boundary

The single/dipole fields are **regularized eigenstrain inclusions**, not singular Volterra dislocations and not a reproduction of the Airy-stress-function model in Cesana–De Luca–Morandotti (2024). This is a reference/prototype baseline only. It is not yet the RGS/Q6 discretization, contains no disclination connection, and proves no Mosco or Gamma convergence.

The next mathematical step is to define a chain map/intertwiner from the RGS cochain variables to the continuum-compatible kinematic variables, then replace the Q1 reference assembly with the proposed RGS operator while retaining this code as a comparator.

## Run

```bash
python scripts/rgs_defect_benchmark.py --self-test
python scripts/rgs_defect_benchmark.py --out artifacts/rgs_defect_benchmark
```

Dependencies: NumPy and SciPy. Matplotlib is optional and only used for the refinement plot.

Outputs: `report.json`, `results.csv`, and (when Matplotlib is installed) `single_source_refinement.png`.

## Acceptance criteria for this prototype

1. Exact integer B0 identity.
2. Manufactured affine field relative error below `1e-9`.
3. Zero-source energy below `1e-20`.
4. Free-DOF relative residual below `1e-8`.
5. Finite nonnegative energies for single and dipole sources.

Passing these tests validates only this baseline implementation, not a physical dislocation model or the RGS continuum limit.
