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

A finite-difference Airy-stress reference is now included in `scripts/rgs_airy_reference.py`. The defect cases in the Q1 and cochain solvers use natural traction-free boundaries with a three-DOF rigid-motion gauge; the manufactured affine patch retains Dirichlet data. The Airy reference solves the clamped biharmonic problem corresponding, on the straight square boundary and modulo the affine gauge, to zero traction. It compares stress and strain fields on interior cells. This remains a reference comparison, not a reproduction of the published CIP-DG method.

The next mathematical step is to compare the Airy and displacement fields over core-width and mesh-refinement sequences, then define a chain map/intertwiner from the RGS cochain variables to continuum-compatible kinematic variables.

## Run

```bash
python scripts/rgs_defect_benchmark.py --self-test
python scripts/rgs_defect_benchmark.py --out artifacts/rgs_defect_benchmark
python scripts/rgs_airy_reference.py --out artifacts/rgs_airy_comparison
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


## Morandotti C0-IPDG cell reconstruction

The exact finite-dimensional postprocessing step from Theorem 2.2 is implemented in `models/morandotti_cell_reconstruction.py`: it builds the Frank/Burgers vector `Phi`, solves `M a = Phi`, and reconstructs the Airy potential from the `3N` cell fields. See [MORANDOTTI_RECONSTRUCTION_GATE.md](MORANDOTTI_RECONSTRUCTION_GATE.md) for sign conventions, the two-core mixed regression case, and the remaining traction/stress validation gates. The algebraic layer is separate from the DOLFINx cell-field solve and does not claim end-to-end validation.


The two-core C0-IPDG driver now exports the six FE cell fields and mesh/dof metadata, and performs the four algebraic Airy reconstructions against the assembled Laplacian-product matrix. Run in the DOLFINx 0.11 / Gmsh / PETSc-MUMPS environment:

```bash
python scripts/rgs_morandotti_two_core_c0_ipdg.py \
  --mesh-sizes 0.24 0.16 0.11 \
  --young-modulus 1.0 --poisson-ratio 0.0 \
  --out artifacts/morandotti_two_core/report.json
```

Each mesh level writes a `cell_fields_h*.npz` artifact beside the report. The archive contains the six FE coefficient vectors, dof and geometry metadata, and the Hessian/Laplacian/flux matrices. The JSON report includes the four defect-data cases, boundary value/normal-derivative diagnostics, elementwise Airy stress, traction L2 norms on the outer boundary and both cores, and the interior-facet traction jump. These are implemented diagnostics, not yet validated numerical results: the driver still must be executed in the target DOLFINx environment, its mesh trends inspected, and its stress compared with an independent analytic benchmark. See [MORANDOTTI_TWO_CORE_AUDIT.md](MORANDOTTI_TWO_CORE_AUDIT.md) and [MORANDOTTI_RECONSTRUCTION_GATE.md](MORANDOTTI_RECONSTRUCTION_GATE.md).


## Morandotti–vorticity research bridge

A scoped geometric note separates Cartan torsion/curvature (elastic dislocations/disclinations) from ordinary kinematic or medium vorticity 2-forms. It defines the circulation and Cartan quantities that could be measured around the two cores, and records the numerical gates and the separate superconducting extension. No FDT–torsion identification or dynamic coupling is assumed: [MORANDOTTI_VORTICITY_BRIDGE.md](MORANDOTTI_VORTICITY_BRIDGE.md).
