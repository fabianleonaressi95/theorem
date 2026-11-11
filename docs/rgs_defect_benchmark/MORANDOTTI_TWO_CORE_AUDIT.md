# Morandotti two-core audit: implementation gaps

**Audit date:** 2026-11-11  
**Target:** `work/morandotti-cell-reconstruction`, PR #149  
**Audit type:** source inspection. No DOLFINx/Gmsh numerical run was executed in this audit.

## What is already implemented

- The finite-dimensional map `Phi -> a -> v_h` is implemented in `models/morandotti_cell_reconstruction.py`.
- The signs and ordering of the two-core mixed datum are covered by a unit test.
- The algebraic tests cover a synthetic SPD matrix, linearity, and invalid matrix/data shapes.
- The C0-IPDG script assembles six cell fields and reports both Hessian- and Laplacian-product matrices, together with boundary/interior flux terms.

These are useful algebraic and assembly components, but they are not yet an end-to-end defect computation.

## Gaps found by source inspection and implementation status

1. **Resolved in the current branch: FE field export.**  
   The driver now saves the six FE coefficient vectors, dof coordinates, geometry coordinates/dofmap, and interaction matrices in one compressed `.npz` artifact per mesh level. The run remains serial-only.

2. **Resolved at source level: four defect-data reconstructions.**  
   The driver builds `Phi`, solves the actual assembled Laplacian-product system, and reconstructs Airy FE values for a single disclination, a single edge dislocation, an opposite-sign disclination dipole, and the mixed two-core source. Each case records the linear-system residual.

3. **Resolved at source level: boundary and stress diagnostics.**  
   Value and normal-derivative residuals are now recorded on the outer boundary and both cores for every cell field. For each reconstructed Airy potential, the driver forms the elementwise cofactor Hessian stress, reports traction L2 norms on all three boundary components, and reports the interior-facet traction jump. These diagnostics have not yet been executed or independently validated.

4. **Still open: actual mesh-convergence analysis.**  
   Multiple mesh sizes are solved and per-level matrices, fields, reconstructed stress diagnostics, eigenvalue and condition diagnostics are recorded. The report does not yet compare these quantities between successive levels or report observed rates.

5. **Still open: execute the actual assembled operator.**  
   Existing unit tests use a synthetic SPD matrix. The new driver now exercises the actual assembled Laplacian-product matrix, but it has not yet been run in the required DOLFINx environment; positive definiteness, conditioning, and reconstruction accuracy are therefore unverified.

6. **Parallel execution is explicitly unsupported.**  
   The script raises for communicator size greater than one. This is an honest limitation; no multi-core/MPI scalability claim should be made.

## Required next validation increment

- Save, for each mesh level, the six FE coefficient vectors, dof coordinates, mesh geometry/topology metadata, and the assembled Laplacian-product matrix. Keep the Hessian-product and flux matrices as independent diagnostics.
- Add a postprocessing stage that builds `Phi` for: (i) one wedge disclination, (ii) one edge dislocation, (iii) an opposite-sign disclination dipole, and (iv) the mixed two-core datum already documented in the reconstruction gate.
- Reconstruct `v_h` and the elementwise Hessian/stress. Report the residual `||M a-Phi||`, matrix symmetry and spectrum/condition number, plus value and normal-derivative residuals on every boundary component.
- Report traction residuals `||sigma_h n||` separately on the outer boundary and each core. For C0-IPDG, document the elementwise Hessian convention and facet treatment.
- Compare fields, stresses, and energies across mesh levels and against an independent analytic benchmark on identical geometry, core radius, material parameters, and boundary conditions.

## Acceptance rule

Until these gates pass, classify the result as **algebraic reconstruction implemented + two-core cell-matrix audit scaffold**. Do not classify it as validated two-core Airy reconstruction, physical validation, or a proof of Mosco/Γ convergence.
