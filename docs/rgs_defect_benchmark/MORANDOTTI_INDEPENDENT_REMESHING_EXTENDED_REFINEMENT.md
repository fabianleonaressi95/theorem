# Morandotti extended refinement with independent remeshing

**Status:** protocol prepared; the 98 finite-element realizations have not yet been executed.

## Objective

Test whether the five-level traction-jump trend and the two-core interaction diagnostics remain stable under both additional mesh refinement and independent Gmsh realizations. This extends the fixed-connectivity study without confusing its mesh deformation with a fresh remeshing ensemble.

## Fixed experiment

| Parameter | Values |
|---|---|
| Target mesh sizes | h = 0.080, 0.060, 0.045, 0.035, 0.027, 0.022, 0.018 |
| Core separations | d = 0.48, 0.56 |
| Independent mesh seeds | 11, 17, 23, 29, 37, 47, 59 |
| Core radius / outer radius | a = 0.12, R = 1 |
| Material | E = 1, nu = 0 |
| C0-IPDG penalty | alpha = 10 |
| Meshes per (h,d) | 7 |
| Total FEM realizations | 7 x 2 x 7 = 98 |

Each (h,d,seed) triple creates a fresh Gmsh model. The six embedded seed-dependent interior vertices enforce distinct mesh fingerprints within each fixed (h,d) group. The geometry is not inherited from a different separation or mesh level.

The campaign is sharded by mesh size, with one workflow job per h and up to four jobs in parallel. Each shard writes its own report, checkpoint, progress log, diagnostics, decomposition and finite-element field exports.

## Resume and artifact integrity

The workflow artifact name is keyed by the shard identifier, and the restore step uses the same key. This fixes the previous mismatch between the uploaded artifact name and the resume lookup. A rerun can pass the previous workflow run ID and restore the matching shard checkpoint. The Python runner refuses a resume if the numerical configuration differs or if a referenced field export is absent.

## Reported quantities

- Signed directional anisotropy of the cross-core Burgers coupling.
- Normalized cross-core coupling.
- Ensemble mean and sample standard deviation of each scalar observable.
- Mean interaction matrix, entrywise standard deviation and relative Frobenius deviations.
- Per-realization traction-jump norms, mesh Jacobian checks and interaction-matrix symmetry.
- Separate between-resolution and within-resolution sums of squares.
- Core-exchange mismatch, reciprocity, corner quality and boundary/interior flux diagnostics.

Within-resolution spread combines seed, topology and node-placement effects. It is not interpreted as pure random-seed error or as a confidence interval. Between-resolution shifts are descriptive and do not establish an asymptotic order.

## Reproduction

After merging this protocol, start the Morandotti independent-remeshing audit workflow with a manual dispatch. The full campaign consists of 98 FEM solves. If interrupted, rerun with the prior workflow run ID in the resume_from_run_id input; each shard restores only its own checkpoint artifact.

## Acceptance and interpretation

The campaign must contain exactly 98 records, seven distinct fingerprints for every (h,d), and all expected field exports. Non-positive sampled Jacobians or loss of interaction-matrix symmetry remain hard failures.

A stable ensemble mean across the finest levels would strengthen the numerical evidence, but would not alone prove a continuum limit. The interpretation must keep distinct:

1. Source quadratic Frank/Burgers decomposition.
2. Interior-facet traction-jump norm.
3. Mesh-realization dispersion.
4. Resolution-dependent shift.
5. Core-separation dependence.

No nonzero limiting traction jump, universal decay exponent, constitutive Frank–Burgers law, force-balance theorem, or material validation is asserted by this finite campaign.

Reference: Cesana, Fabbrini, León Baldelli and Morandotti (2026), arXiv:2609.29614.
