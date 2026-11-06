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
1. historical diagonal weights (retain only for reproducibility; top-degree scaling is nonstandard for integral cochains);
2. top-corrected primal DEC diagonal weights with M_d(K)=1/vol_g(K);
3. consistent tensor-product cubical FEEC mass matrices;
4. a documented golden/supergolden positive-weight variant only after positivity and uniform equivalence are proved/verified.

For each: positivity, condition number, adjoint consistency, co-closed sector, eigenvalue trajectories, eigenvector reconstruction and subspace angles. The legacy-versus-corrected top-degree control is mandatory before any compactness interpretation.

## F. What can currently be stated

- **Exact algebraic:** incidence (d_{k+1}d_k=0), by the cubical chain construction.
- **Numerically reported:** matrix residuals, Jacobian samples, spectra and condition numbers on the finite meshes in the archived run.
- **Numerically established on tested affine and fixed-amplitude sinusoidal meshes:** the historical M_d(K)=vol_g(K) convention produces the h^(2d) collapse; replacing only the top-degree diagonal weight by 1/vol_g(K) removes it, and consistent cubical FEEC masses show the same non-collapse.
- **Not established:** uniform discrete compactness on general curvilinear meshes, no spectral pollution for arbitrary maps, Mosco convergence, norm-resolvent convergence, or a continuum spectral theorem.
- **Revised interpretation:** the previously proposed compactness-failure mechanism is withdrawn for the tested collapse. The primary identified cause is the historical top-degree mass normalization.

This file is a gate list for the next research pass, not an endorsement of every value or interpretation in the uploaded report.


## Degree-wise mode audit added

Run `python degreewise_audit.py --dim 2 --N 8` and `python degreewise_audit.py --dim 3 --N 5`. The audit normalizes the co-closedness defect using the Hodge energy, computes the grad/curl energy fractions in the correct (M)-norms, and evaluates distance to `im d_{k-1}` in the (M_k)-norm. It includes top degree, where every positive mode must have grad fraction 1 and curl fraction 0.


## Consistent-mass audit completed

The three-way control (historical diagonal / top-corrected DEC / consistent cubical FEEC) is implemented in `compare_mass_matrices.py` and `mass_refinement_study.py`. Flat 2D/3D refinement and fixed-amplitude sinusoidal 2D/3D refinement passed CI. On flat affine meshes the top-corrected DEC diagonal matrices equal the row-sum lumping of the consistent FEEC matrices in every degree. See `docs/CONSISTENT_FEEC_MASS.md` and §1.7 of `REPORT.md` for numerical values and the revised scientific status.
