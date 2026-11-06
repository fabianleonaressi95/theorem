# Independent audit checklist — de Rham curvilinear benchmark

**Status: review required.** This checklist does not invalidate the stored runs; it identifies statements that must be rechecked before being used as mathematical evidence.

## A. First reproducibility gates

- [ ] Run `python run_benchmark.py --config configs/default.json --out results/reproduction` on a clean environment.
- [ ] Record Python, NumPy, SciPy, BLAS/LAPACK versions and platform.
- [ ] Compare the regenerated JSON against the archived `results/run1/results.json`; do not overwrite the archived data.
- [ ] Confirm the configuration file, code revision and output hash are attached to each run.
- [ ] Verify all cell Jacobians remain positive and geometry maps are globally injective; a local positive determinant is necessary, not sufficient, for global injectivity.

## B. Generalized eigenproblem and spectral interpretation

The stated problem is (B_k x=\lambda M_kx), with (M_k) SPD. Independently check:
- [ ] The solver uses the generalized symmetric problem (e.g. `scipy.linalg.eigh(B, M)`) or a symmetric transformation (M^{-1/2}BM^{-1/2}).
- [ ] Eigenvectors are normalized in the (M_k)-inner product.
- [ ] Residuals are reported in both absolute and scale-aware form:
  (|B x-\lambda Mx|/(|B||x|+|\lambda||M||x|)).
- [ ] Kernel threshold is not chosen as `tol_rel * lambda_max` alone: `lambda_maxsim h^{-2}) can make the absolute tolerance grow while genuine small eigenvalues shrink.
- [ ] Compare direct generalized eigenvalues to the symmetrized operator spectrum.

## C. Critical co-closed/top-degree consistency check

The report describes small modes as co-closed and positive-energy. This wording must be checked carefully:

[
\Delta_k=d_{k-1}\delta_k+\delta_{k+1}d_k,qquad
\langle \Delta_k u,u\rangle=\|\delta_k u\|^2+\|d_k u\|^2.
]

If (\delta_k u=0) **and** (d_k u=0), then (u) is harmonic and its eigenvalue is zero. In top degree (k=d), (d_d=0); therefore a top-degree co-closed vector ((\delta_d u=0)) must be in the kernel. A positive top-degree eigenmode cannot simultaneously be exactly co-closed.

- [ ] Verify whether “co-closed” means (\delta_k u\approx0), the wrong-index operator, or a component of a Hodge splitting.
- [ ] Verify “grad part/curl part” definitions and index conventions from source, not report prose.
- [ ] Test the top-degree (k=d) data separately. If the stored diagnostic claims (\delta_d u\approx0) while (\lambda>0), resolve the discrepancy before calling the mode co-closed.
- [ ] Repeat the check in the (M)-norm, not only the Euclidean norm of coefficient vectors.

## D. Topology versus spectral pollution

- [ ] Compute Betti numbers from exact/rational incidence ranks where feasible.
- [ ] Keep (dim\ker\Delta_k) separate from near-zero positive eigenvalues.
- [ ] Check kernel dimensions using a fixed physically/numerically justified absolute threshold and a relative residual criterion.
- [ ] Track spectral projectors/subspaces across refinement, not only the smallest eigenvalue.

## E. Inner-product comparison experiment

Use identical mesh, map, metric, quadrature, boundary convention and incidence complex for:
1. diagonal DEC-like Hodge weights (current benchmark);
2. consistent Whitney/FEEC mass matrix;
3. a documented golden/supergolden positive-weight variant only after positivity and uniform equivalence are proved/verified.

For each: positivity, condition number, adjoint consistency, discrete compactness proxy, co-closed sector, eigenvalue trajectories, eigenvector concentration and subspace angles.

## F. What can currently be stated

- **Exact algebraic:** incidence (d_{k+1}d_k=0), by the cubical chain construction.
- **Numerically reported:** matrix residuals, Jacobian samples, spectra and condition numbers on the finite meshes in the archived run.
- **Not established:** uniform discrete compactness, no spectral pollution, Mosco convergence, norm-resolvent convergence, FEEC equivalence, or a continuum spectral theorem.
- **Candidate explanation:** instability/compactness failure caused by the chosen diagonal inner products. This is a hypothesis until consistent-mass controls and independent reproductions are completed.

This file is a gate list for the next research pass, not an endorsement of every value or interpretation in the uploaded report.


## Degree-wise mode audit added

Run `python degreewise_audit.py --dim 2 --N 8` and `python degreewise_audit.py --dim 3 --N 5`. The audit normalizes the co-closedness defect using the Hodge energy, computes the grad/curl energy fractions in the correct (M)-norms, and evaluates distance to `im d_{k-1}` in the (M_k)-norm. It includes top degree, where every positive mode must have grad fraction 1 and curl fraction 0.
