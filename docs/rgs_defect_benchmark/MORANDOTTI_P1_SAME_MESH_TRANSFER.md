# Morandotti P1 displacement transfer on the two-core P3 mesh

**Status:** implementation added; numerical status is determined by the dedicated GitHub Actions run. This is the first displacement-side cross-discretization gate, not the complete Q1/P1 comparison.

## What the run does

1. Executes the existing two-core P3 C0-IPDG cell-field computation at (h=0.06), (R=1), (a=0.12), core centres ((-0.28,0)), ((0.28,0)), (E=1), and (
u=0).
2. Regenerates the same Gmsh mesh and refuses to proceed unless the geometry coordinates, geometry dofmap, and P3 dof coordinates match the P3 artifact.
3. Reconstructs the mixed Frank/Burgers Airy potential using the archived Laplacian-product interaction matrix.
4. Builds the stress-equivalent plane-strain eigenstrain (arepsilon^*=-Ssigma_A) and solves the P1 triangular displacement problem on that mesh. Three point constraints remove the two translations and in-plane rotation.
5. Reports relative stress error, complementary-energy difference, outer/core traction norms, and the broken cellwise incompatibility identity residual.

## Interpretation boundary

The eigenstrain is manufactured from the Airy stress itself. This calculation therefore tests transfer between P3 Airy and P1 displacement discretizations; it does **not** independently validate the physical Frank/Burgers source. The broken incompatibility residual excludes distributional inter-element jump terms and must not be presented as a global distributional residual.

The P1 solve is only one part of the requested comparison. **Q1 quadrilateral displacement is not yet implemented.** A second mesh family must be generated on the same CAD domain, with its geometry approximation and boundary tags recorded explicitly; it must not be described as the same mesh.

The historical 18.52% energy discrepancy remains open. This run reports two energies computed from the same stress-compliance functional and normalization. It does not silently compare this value with a differently normalized source quadratic form or with the Hessian-product matrix.

## Acceptance and next gates

- **Mesh identity:** exact geometry dofmap and tolerance-controlled coordinate/P3-dof checks must pass before solving.
- **P1 numerical result:** report stress, energy, traction, and broken incompatibility diagnostics without imposing an arbitrary pass threshold on discretization error.
- **Still required:** Q1 quadrilateral comparison; independent Frank/Burgers eigenstrain source; distributional incompatibility including inter-element terms; refinement and remeshing study; forensic reconstruction of the 18.52% discrepancy.

Reproduce with the workflow **Morandotti P1 same-mesh transfer audit** or:

```bash
python -c "from scripts.rgs_morandotti_two_core_c0_ipdg import solve_level; solve_level(0.06, alpha=10.0, young_modulus=1.0, poisson_ratio=0.0, args_artifact_path='artifacts/cell_fields_h0.0600.npz')"
python scripts/rgs_morandotti_p1_same_mesh.py --input artifacts/cell_fields_h0.0600.npz --out artifacts/report.json
```
