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

## Gaps found by source inspection

1. **The six cell fields are not exported.**  
   `solve_level` keeps the six DOLFINx Functions in memory and returns only scalar diagnostics and matrices. Consequently, the output cannot yet be passed to the Airy postprocessor, which requires the actual six fields (or their FE coefficient vectors and mesh/dof metadata).

2. **No defect-data cases are reconstructed.**  
   The script solves the geometry-dependent cell problems, but it does not build `Phi`, solve the assembled `M a = Phi` system, or construct the resulting Airy potential for a disclination, dislocation, opposite-sign dipole, or mixed source.

3. **Boundary checks are incomplete.**  
   The report records value and normal-derivative residuals only on the *active* core for each cell problem. It does not report those residuals on the outer boundary and on the inactive core(s). It also does not reconstruct `sigma_h = cof(D^2 v_h)` or evaluate `sigma_h n` on any boundary.

4. **The refinement study is not yet a convergence study.**  
   Multiple mesh sizes are solved, and per-level eigenvalue/condition diagnostics are recorded. The script does not compare matrices, cell fields, reconstructed stresses, or energies between successive levels, nor does it report observed rates.

5. **The algebraic tests do not exercise the assembled operator.**  
   The SPD matrix in the reconstruction test is randomly generated. This checks the linear algebra implementation, not positive definiteness, conditioning, or reconstruction accuracy of the actual C0-IPDG interaction matrix.

6. **Parallel execution is explicitly unsupported.**  
   The script raises for communicator size greater than one. This is an honest limitation; no multi-core/MPI scalability claim should be made.

## Required next implementation increment

- Save, for each mesh level, the six FE coefficient vectors, dof coordinates, mesh geometry/topology metadata, and the assembled Laplacian-product matrix. Keep the Hessian-product and flux matrices as independent diagnostics.
- Add a postprocessing stage that builds `Phi` for: (i) one wedge disclination, (ii) one edge dislocation, (iii) an opposite-sign disclination dipole, and (iv) the mixed two-core datum already documented in the reconstruction gate.
- Reconstruct `v_h` and the elementwise Hessian/stress. Report the residual `||M a-Phi||`, matrix symmetry and spectrum/condition number, plus value and normal-derivative residuals on every boundary component.
- Report traction residuals `||sigma_h n||` separately on the outer boundary and each core. For C0-IPDG, document the elementwise Hessian convention and facet treatment.
- Compare fields, stresses, and energies across mesh levels and against an independent analytic benchmark on identical geometry, core radius, material parameters, and boundary conditions.

## Acceptance rule

Until these gates pass, classify the result as **algebraic reconstruction implemented + two-core cell-matrix audit scaffold**. Do not classify it as validated two-core Airy reconstruction, physical validation, or a proof of Mosco/Γ convergence.
