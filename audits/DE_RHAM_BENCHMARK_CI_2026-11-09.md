# de Rham benchmark — CI evidence record (9 November 2026)

## Latest successful run

- Workflow: **de Rham benchmark smoke checks**
- Run: [#92](https://github.com/fabianleonaressi95/theorem/actions/runs/42623232284)
- Commit: [6fd5ab9](https://github.com/fabianleonaressi95/theorem/commit/6fd5ab95dc2c21752397412ca6104c175b7dc41b)
- Trigger: push to `main`
- Result: **success**, job `smoke`, duration approximately 43 seconds.

The same workflow also completed successfully for PR #106 (run #91), PR #105 (run #89), commit #90, PR #104 (run #87), commit #88, PR #104 open event (run #87), and commit #86. The current record lists the seven user-supplied run IDs without interpreting repeated PR/push runs as independent mathematical proofs.

## Checks executed by run #92

The job completed every configured step:

1. Python 3.11 environment and dependency installation.
2. Compilation of the benchmark Python sources.
3. Herasymov symbolic and parity-lattice audit.
4. Herasymov regression tests.
5. Exact shared-face conformity audit.
6. Exact cubical subdivision and signed-permutation naturality audit.
7. CLI entry-point check.
8. Cubical incidence chain identity.
9. Degree-wise Hodge checks on small affine meshes in dimensions 2 and 3.
10. Historical diagonal DEC versus top-corrected DEC versus consistent cubical FEEC mass comparison.
11. DEC/FEEC refinement controls in 2D and 3D.
12. FEEC projection and adjoint smoke tests.
13. Fixed-amplitude curved-map mass controls in 2D and 3D.

All listed steps completed with conclusion `success` in the GitHub job summary. This is evidence that the configured finite computations and assertions passed for the inputs used by the workflow.

## The mathematical results promoted to the central theorem register

- [T065 — Exact cubical subdivision chain map and signed-permutation naturality](../theorems/T065-cubical-subdivision-chain-map-and-naturality.md).
- [T066 — Herasymov parity-cell affine shared-face conformity](../theorems/T066-herasymov-parity-affine-shared-face-conformity.md).
- [T067 — Stokes commutation of cubical face-integral interpolation](../theorems/T067-stokes-commuting-cubical-face-integral-interpolation.md).

The pre-existing [T048](../theorems/T048-rgs-prism-mosco-changing-spaces.md) and the project's [theorematic foundations](../projects/de_rham_benchmark/docs/THEOREMATIC_FOUNDATIONS.md) retain the conditional Mosco framework and the analytic obligations. No new theorem of Mosco, discrete compactness, norm-resolvent, or spectral convergence is claimed by this CI run.

## Important numerical interpretation

The fixed-amplitude curved-map study reports finite refinement tables and finite-range log-log slopes. The script itself labels these slopes descriptive, not asymptotic proofs. The observed contrast between the historical top-degree diagonal weight, the corrected primal DEC weight, and the consistent FEEC mass is a finite benchmark result. It is not a proof of spectral convergence or absence of pollution for arbitrary curvilinear families.

The project-level report and audit checklist remain the sources for exact configurations, output fields, numerical caveats, and open analytical tasks.

## Warnings in the latest log

The successful job log contains environment/dependency warnings:
- Node.js 20 deprecation notice for the GitHub Actions versions `actions/checkout@v4` and `actions/setup-python@v5`, which are being forced to Node.js 24 by the runner.
- Python's `punycode` deprecation warning during job cleanup.

Neither warning caused a failed step. They are maintenance warnings, not mathematical or test failures. The workflow can be updated to action releases targeting the supported runner runtime when available.

## What this CI does not establish

- It does not prove that the Herasymov voxel recursion itself defines a geometric refinement.
- It does not identify Herasymov parity refinement with the standard cubical subdivision map.
- It does not prove FEEC projection stability or discrete compactness uniformly in (h).
- It does not prove Mosco/(Gamma)-convergence for the curved benchmark or the RGS–PRISM sequence.
- It does not prove norm-resolvent or spectral convergence.
- It does not supply a canonical Kathara/Krist-All/Q6/RGS–PRISM identification.

## Verification policy

The theorem repository is the canonical location for theorem statements and proof records. Implementations and finite audits remain in the project directory, with exact paths, commits, and CI run links. The bridge repository should cite these central records rather than duplicating the same full benchmark suite as a prerequisite. Its own implementation-specific tests remain appropriate.
