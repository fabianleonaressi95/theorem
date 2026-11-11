# Morandotti two-core C0-IPDG audit: current implementation and evidence

**Updated:** 2026-11-11  
**Repository:** \`fabianleonaressi95/theorem\`  
**Scope:** finite-dimensional Frank/Burgers reconstruction, interior-facet traction jumps, and mesh-refinement execution.

## Merged implementation

### PR #161 — Frank–Burgers traction-jump decomposition

[PR #161](https://github.com/fabianleonaressi95/theorem/pull/161) was merged as \`d43b6906ef88840f0688b8939045fbc8900110e7\`.

The implementation computes the interior-facet traction jump from the reconstructed stress as
\[
j=\llbracket\sigma n\rrbracket=j_\Omega+j_B.
\]
It records the Frank and Burgers L2 norms and independently assembles the signed mixed term
\[
2\int_{\mathcal F_h^{\rm int}}j_\Omega\cdot j_B\,dS,
\]
together with the squared-norm additivity residual. It also records total, Frank, Burgers, and mixed second-moment tensors in laboratory coordinates and in the longitudinal/transverse core frame, plus the total directional anisotropy.

The [DOLFINx two-core audit run #46](https://github.com/fabianleonaressi95/theorem/actions/runs/43051485760) completed successfully. Its algebraic tests, numerical audit, and artifact upload all passed.

### PR #162 — five-level traction-jump refinement

[PR #162](https://github.com/fabianleonaressi95/theorem/pull/162) was merged as \`e88da3e16257a9ab3a867e3b72e97fbd70a2d943\`.

It adds a dedicated DOLFINx 0.11.0 workflow and executes the two-core audit at
\[
h\in\{0.08,\ 0.06,\ 0.045,\ 0.035,\ 0.027\},
\]
with the existing material and penalty settings. The workflow reruns the 13 algebraic reconstruction tests and uploads the JSON report and per-level FE fields.

Both the [base two-core audit run #47](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448351) and the [dedicated five-level refinement run](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448456) completed successfully. The five-level artifact is available through the latter workflow run.

## What the successful runs establish

- The configured DOLFINx/Gmsh/PETSc environment was initialized successfully.
- The 13 algebraic reconstruction tests passed in the five-level workflow.
- The five-level finite-element audit completed without workflow failure.
- The JSON report and per-level FE fields were uploaded successfully.
- The Frank/Burgers/mixed traction-jump quantities and their directional second moments are part of the recorded output.

## What remains open

The successful workflow is evidence that the configured computation ran; it is not, by itself, a convergence theorem. The numerical report and FE fields must be inspected before assigning an observed rate or claiming stabilization of the traction-jump norms. In particular:

1. Compare each traction-jump norm and the signed mixed term across all five mesh sizes.
2. Check the additivity residual and symmetry/positive-semidefinite properties of the second-moment tensors at every level.
3. Separate stabilization of the total jump from stabilization of its Frank, Burgers, and mixed components.
4. Avoid fitting a continuum decay law unless the five-level data and further refinement support it.
5. Keep mesh-coordinate anisotropy separate from defect-induced stress anisotropy.
6. Do not infer physical force balance, a material constitutive law, circulation, or a Möbius/topological contribution from these static Airy-stress diagnostics.

## Reproduction

The five-level command used by the dedicated workflow is:

\`\`\`bash
python3 scripts/rgs_morandotti_two_core_c0_ipdg.py \\
  --mesh-sizes 0.08 0.06 0.045 0.035 0.027 \\
  --alpha 10 \\
  --young-modulus 1.0 \\
  --poisson-ratio 0.0 \\
  --out artifacts/morandotti_traction_refinement/report.json
\`\`\`

See also [MORANDOTTI_ANISOTROPY.md](../../MORANDOTTI_ANISOTROPY.md) for the definitions of the longitudinal/transverse frame, the Frank–Burgers split, and the signed mixed traction-jump contribution.

---
**FLN**
