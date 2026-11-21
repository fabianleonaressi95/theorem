# C60 constrained Coulomb equilibrium audit

**Purpose.** This is a second-stage calculation, separate from the MMFF94s relaxation audit. It minimizes the all-pairs unit-charge Coulomb energy while fixing the center of mass and the total squared radius (equivalently, the RMS radius) to those of the MMFF94s-relaxed starting geometry.

## Mathematical problem

For 60 points \(x_i\in\mathbb R^3\), minimize
\[
E_C(X)=\sum_{i<j}\frac{1}{\lVert x_i-x_j\rVert}
\]
subject to
\[
\sum_i x_i=0,\qquad \sum_i\lVert x_i\rVert^2=R^2.
\]
The fixed radius removes the dilation direction; the center-of-mass constraints remove translations. Rotations remain unconstrained and should generate three zero modes at a regular stationary configuration.

The SLSQP run uses the analytic Coulomb gradient. The four equality-constraint multipliers are recovered from the KKT least-squares system. With \(\lambda_R\) the radius multiplier, the constrained Lagrangian Hessian is
\[
K=Q^T(H_C+\lambda_R I)Q,
\]
where the columns of \(Q\) span the orthogonal complement of the three translation vectors and the radial vector \(X\).

## Acceptance criteria

Do not interpret the Hessian as a constrained second variation unless:
- optimizer reports success;
- \(\lVert Q^T\nabla E_C\rVert <10^{-7}\);
- full KKT residual is below \(10^{-7}\);
- radius and center-of-mass constraints are satisfied.

A local-minimum classification additionally requires no negative eigenvalues, allowing for the three rotational zero modes. The script reports inertia without silently removing or relabeling modes.

## Symmetry audit

The script reconstructs the 120 orthogonal symmetries of the ideal icosahedron from its vertex Gram data. For each operation it applies the transformation to the relaxed point cloud and solves an optimal assignment problem. It reports the number of operations preserving the relaxed coordinates at maximum pointwise residual thresholds \(10^{-6}\) and \(10^{-4}\). No exact \(I_h\) symmetry or irrep decomposition is assumed.

## Reproduction

Install NumPy and SciPy; the MMFF starting geometry additionally requires RDKit.

Using the already-produced first-stage artifact:
```bash
python scripts/audit_c60_coulomb_constrained_equilibrium.py \
  --input-npz C60_MMFF94s_relaxed_coulomb.npz \
  --out-dir c60_coulomb_equilibrium_audit
```

Or regenerate the MMFF94s starting geometry:
```bash
python scripts/audit_c60_coulomb_constrained_equilibrium.py
```

Outputs:
- `C60_Coulomb_constrained_equilibrium.npz`: starting/equilibrium coordinates, constraints, gradient, Hessians and spectrum;
- `report.json`: optimizer, KKT, spectrum, and symmetry diagnostics.

**Classification before execution:** proposed numerical audit protocol. No equilibrium or stability result is claimed until its artifact is inspected.
