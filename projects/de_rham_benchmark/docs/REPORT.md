# REPORT — discrete de Rham complexes on curvilinear cubical meshes

Benchmark code: `ddr/` (see `README.md`, conventions in `ASSUMPTIONS.md`).
Data: `results/run1/results.json`, diagnostics `results/pollution.json`,
plots `results/run1/plots/`. Config: `configs/default.json`.

This report separates **verified numerical observations** (direct outputs of
the code on fixed meshes) from **conjectures** (interpretation). Nothing here
is a proof of Mosco or variational convergence.

---

## 1. Verified numerical observations

### 1.1 Algebraic identities (all runs, all levels)

| identity | worst residual observed |
|---|---|
| `d_{k+1} d_k = 0` | `0` (exact, integer arithmetic) |
| `B_k = M_k Delta_k` symmetric | `<= 3.6e-15` |
| adjointness `<d a, b>_M = <a, delta b>_M` | `<= 5.6e-17` (relative) |
| self-adjointness of `Delta_k` w.r.t. `M_k` | `<= 3.7e-16` (relative) |
| partition of unity `sum_v M0[v] = sum_K vol_g(K)` | `0` |
| eigenpair residuals `||Bx - lambda Mx||` | `<= ~1e-13` (dense levels) |

Betti numbers from ranks of the incidence matrices are `(1,0,...)` in every
run, matching `dim ker Delta_k` at coarse levels (see §1.4 for fine levels).

### 1.2 Geometry: uniform Jacobian bounds are preserved under refinement

`min/max det D Phi` and singular values of `D Phi` are mesh-independent
quantities (D Phi does not contain `h`). For every fixed-amplitude curved
map they are **constant across the whole refinement sequence**:

| experiment | min det D Phi (N=4 … N=32) |
|---|---|
| 2D sinusoid a=0.05 | 0.8654 → 0.8653 |
| 2D sinusoid a=0.15 | 0.5961 → 0.5959 |
| 2D sinusoid a=0.25 | 0.3269 → 0.3265 |
| 3D sinusoid a=0.10 | 0.7622 → 0.7619 |
| 3D sinusoid a=0.20 | 0.5245 → 0.5239 |

With `amplitude_h = a0 h^gamma` schedules, `min det D Phi -> 1` as `h -> 0`
(the distortion is washed out), e.g. 2D a=0.15·h^0.5: 0.798 → 0.929.

### 1.3 Fold threshold (amplitude sweep, N=12, 2D)

`det D Phi` crosses zero between `a = 0.40` (min det = +0.057) and
`a = 0.45` (min det = −0.077); `bad_jac_cells` (cells with `det D Phi <= 0`
or degenerate face measure) grows 0 → 24 across the sweep. For the
frequency sweep at `a = 0.12`: `m = 1,2` keep `det > 0`, `m = 4` already
folds (min det = −0.29, 48 bad cells), `m = 8,16` are deeply folded
(144 bad cells, min det = −1.6 / −4.0). **Once `det D Phi < 0` the map is
not a diffeomorphism; spectra reported there are formal algebraic output
of the same formulas, not a discretization of a Riemannian manifold.**

Spectral indicators degrade *before* the fold: `cond(M_0)` rises from 4
(affine) to ~90 near `a ≈ 0.40`, and `lambda_min^+(k=0)` drops
9.81 → 7.79 over the sweep. Under high-frequency maps (`m=4, a=0.10`)
`cond(M_0)` jumps to ~57 at N=32 (vs ~4–6 for low-frequency maps) and
`lambda_min^+(k=0)` falls to ~5.5 instead of converging near π².

### 1.4 Historical spectral collapse under the archived diagonal convention

This section records the original output using the historical assignment
`M_d(K)=vol_g(K)`. Section 1.7 below supersedes its interpretation: for
integral top-degree cochains this is not the standard primal DEC Hodge weight,
and correcting it removes the reported collapse in the tested affine meshes.

The smallest positive eigenvalues of the Hodge Laplacian behaved very
differently by level `k` under that historical convention:

* **k = 0** (and the exact sector of k = 1 in 3D): `lambda_min^+`
  converges smoothly. 2D affine: 9.373, 9.743, 9.838, 9.862 → ≈ π²
  (first Neumann eigenvalue of the square). 3D affine: 8.0, 9.0, 9.373,
  9.549, still converging. Curved maps converge to *different* limits
  (2D a=0.15 → ≈ 9.40; a=0.25 → ≈ 8.68; aniso metric → ≈ 4.91),
  consistent with geometry-dependent continuum eigenvalues.
* **k ≥ d−1** (k=1,2 in 2D; k=2,3 in 3D): the smallest eigenvalues
  **collapse toward zero** under refinement, at an empirically clean
  rate `lambda ~ h^{2d}`:
  - 2D k=1 affine: 7.32e-2, 4.76e-3, 3.00e-4, 1.88e-5 for
    N = 4, 8, 16, 32 — ratio ≈ 16 per halving of h (= h⁴).
  - 3D k=2 affine: 3.75e-1, 3.70e-2, 6.87e-3, 1.83e-3 for
    N = 2, 3, 4, 5 — consistent with ~h⁶.
  - k=2 in 2D and k=3 in 3D reproduce the same values (discrete Hodge
    duality of the weights).
* For the degrees actually covered by `results/pollution.json` (2D k=1
  and 3D k=2), the reported small modes have a negligible grad-energy
  fraction and essentially all energy in the curl term. This does **not**
  establish the same characterization in the top degree. The old wording
  that generalized exact co-closedness and curl-dominance to every
  `k >= d-1` was too broad and is corrected in §1.6 below.
* The coefficient ratio `|x|_inf/|x|_2` is only a coordinate-vector
  indicator. Without a stable reconstruction into a common function space,
  it does not prove physical delocalization, smoothness, or compactness.
* At N=32 (2D) the 12 smallest k=1 eigenvalues all lie below
  `tol_rel * lambda_max` and `kernel_num` is reported as 12 — this is a
  **tolerance artefact**: `lambda_max ~ h^{-2}` inflates the absolute
  kernel tolerance while the genuine eigenvalues decay like h⁴. The
  eigenvalue lists in the JSON are the reliable data; `kernel_num`
  should be read together with `eigs_small`.

### 1.5 Inner product conditioning

`cond(M_k)` stays bounded under refinement for fixed-amplitude maps
(e.g. 2D a=0.15: 6.45 → 5.79 as N grows — actually *decreasing* toward
the continuum weight ratio) but grows with amplitude and frequency:
a=0.25 gives ~10; m=4, a=0.10 gives ~57; near the fold it peaks ~90.
Nonuniform ambient metrics raise `cond(M_0)` moderately (~7–11).

---

## 2. Conjectures (interpretation, not verified)

1. **The collapsing eigenvalues indicate a loss of discrete compactness /
   inf-sup stability of the diagonal-weight discretization** in the
   coexact sector for `k >= d-1`. The weights `M_k ~ h^{d-k}` make the
   curl penalty `d_k^T M_{k+1} d_k` too weak relative to the `M_k` norm,
   admitting co-closed cochains with curl energy `O(h^{2d})`. This is a
   property of *this* choice of inner products, not of the cubical
   complex itself (`d^2 = 0` and Betti numbers remain exact).
2. The phenomenon is plausibly related to the **codifferential
   consistency** problem studied analytically: `delta_k` built from
   diagonal Hodge weights is not a stable approximation of the continuum
   codifferential in the coexact sector. A consistent (non-diagonal,
   e.g. Whitney/FEEC) mass matrix is the natural candidate fix — *not
   tested here*.
3. `lambda ~ h^{2d}` suggests the pollution modes are "long-wavelength"
   coexact fields whose discrete curl sees only the `O(h^{d})`-weighted
   top-form mass; the exponent `2d` is empirical (2D: h⁴ over N=4…32;
   3D: ≈h⁶ over N=2…5) and deserves a proof or a finer 3D sequence.
4. Spectral degradation (`cond(M_k)` growth, `lambda_min^+` drift)
   *precedes* the geometric fold threshold; near-fold meshes are the
   most dangerous regime even before `det D Phi < 0`.
5. The k=0 spectrum converging to π² (2D) and the curved-map limits being
   geometry-dependent are *consistent with* eigenvalue convergence of a
   stable scheme, but with the coexact-sector pollution observed, any
 *global* claim of spectral/Mosco convergence for this discretization is
   premature — the k≥d−1 sectors violate it at the rates above.

## 3. Counterexample search — status

The clearest counterexample candidate produced by this benchmark is the
**flat affine mesh itself**: even with `Phi = id`, `G = I`, the k=1 (2D)
and k=2 (3D) Hodge Laplacians develop eigenvalues `~ h^{2d} -> 0` while
`beta_k = 0`. This is a purely algebraic property of the
incidence + diagonal-weight pair and is documented numerically in
`results/run1/results.json` (`spectra.*.eigs_small`) and
`results/pollution.json`. It does not require curved meshes; curvature
only perturbs the constants.

## 4. Reproduction

```bash
cd de_rham_benchmark
python3 run_benchmark.py --config configs/default.json --out results/run1
python3 diagnose_pollution.py results
```

All random inputs are seeded (`default_rng(0)`); no other stochasticity.


## 1.6 Independent degree-wise audit and correction

An independent reconstruction of the affine cubical incidence matrices and
historical diagonal weights, followed by dense generalized symmetric diagonalization
of (B_k x=\lambda M_k x), reproduces the archived small eigenvalues:

| case | degree | smallest positive eigenvalue |
|---|---:|---:|
| 2D, N=4 | 1 | 0.07322330470336 |
| 2D, N=8 | 1 | 0.00475752921807 |
| 2D, N=16 | 1 | 0.00030022999373 |
| 2D, N=32 | 1 | 0.00001880966128 |
| 3D, N=2 | 2 | 0.37500000000000 |
| 3D, N=3 | 2 | 0.03703703703704 |
| 3D, N=4 | 2 | 0.00686468481593 |
| 3D, N=5 | 2 | 0.00183343685372 |

A log-log fit gives empirical exponents 3.9766 in 2D and 5.8052 in 3D,
consistent with the conjectured (h^{2d}) scaling over these finite ranges.
This remains a numerical scaling observation, not an asymptotic proof.

The degree-wise energy split exposes the reporting error. For an eigenvector
(x\in C^k), use the invariant energy components
[
E_{\mathrm{grad}}=\|\delta_k x\|_{M_{k-1}}^2,\qquad
E_{\mathrm{curl}}=\|d_kx\|_{M_{k+1}}^2.
]
The normalized co-closedness defect is
[
\eta_{\mathrm{cc}}(x)=
\sqrt{E_{\mathrm{grad}}/(E_{\mathrm{grad}}+E_{\mathrm{curl}})}.
]
For the first four small positive modes, independent calculations give
`eta_cc < 3e-13` for 2D k=1 at N=8 and 3D k=2 at N=5; their curl
energy fraction is 1 to numerical precision.

In contrast, for top degree (k=d), (d_d=0) identically, so
(E_{\mathrm{curl}}=0). Every positive top-degree eigenmode has
(E_{\mathrm{grad}}=E_{\mathrm{total}}), hence
`eta_cc = 1`: it is not co-closed. The archived spectra also show
the same small eigenvalues in 2D k=2 and 3D k=3, but those are top-degree
modes and have the opposite Hodge-energy characterization. Thus the
claim "all collapsing modes for k >= d-1 are co-closed and curl-dominated"
is false as written. The spectral collapse itself is independently
reproduced; the blanket mode interpretation is not.

The new `degreewise_audit.py` computes this split in the actual (M_k)
norm, checks the generalized eigenpair residual, and measures distance to
`im d_{k-1}` in the weighted norm. Run, for example:

```bash
python degreewise_audit.py --dim 2 --N 8
python degreewise_audit.py --dim 3 --N 5
```

### Other audit qualifications

- `kernel_num` uses `tol_rel * lambda_max`. At 2D N=32, k=1,
  `lambda_max=8192`, so the threshold is (8.192\times10^{-4}), much
  larger than the smallest positive eigenvalue (1.881\times10^{-5}).
  The reported count 12 is therefore a relative-threshold near-zero count,
  not the algebraic nullity (which is `beta_1=0`). Do not use
  `kernel_num` as a Betti estimator at this refinement.
- Positive Jacobian values in the report are quadrature-sample diagnostics.
  They do not by themselves prove `det D Phi > 0` everywhere or global
  injectivity of the map.
- The archived experiment alone did not prove loss of discrete compactness.
  The consistent-mass control in §1.7 now shows that the principal affine
  collapse disappears after correcting the top-degree normalization; the
  original compactness-failure interpretation is therefore withdrawn for
  this tested mechanism. Curved-mesh compactness remains a separate open issue.


## 1.7 Consistent cubical FEEC mass control: the collapse is a normalization artifact

A controlled three-way comparison was added. It holds fixed the cubical mesh,
oriented face degrees of freedom, incidence matrices, affine map, ambient
metric and quadrature. Only the inner products change:

1. **Legacy diagonal:** the historical `PullbackGeometry.M`, including
   `M_d(K)=vol_g(K)`.
2. **Top-corrected primal DEC:** all lower-degree diagonal weights unchanged,
   but `M_d(K)=1/vol_g(K)`.
3. **Consistent cubical FEEC:** full tensor-product cubical de Rham Gram
   matrices, with local integrals of the exterior-power metric
   `Lambda^k(g^{-1})).

For an integral top-degree cochain, the primal DEC Hodge weight is the
dual 0-volume divided by the primal d-volume, hence `1/vol_g(K)`.
The consistent top-form mass on a curved reference cell integrates
`1/sqrt(det(g))`; on an affine cell it is exactly `1/vol_g(K)`.
The legacy `M_d=vol_g(K)` therefore uses the opposite volume scaling.
Since `M_d` enters `D_{d-1}^T M_d D_{d-1}`, the mismatch directly
changes the degree-(d-1) Hodge Laplacian.

### 1.7.1 Affine refinement results

| dimension / degree | N | legacy diagonal | corrected DEC | consistent FEEC |
|---|---:|---:|---:|---:|
| 2D, k=1 | 4 | 0.0732233 | 9.372583 | 10.386642 |
| 2D, k=1 | 8 | 0.00475753 | 9.743420 | 9.997081 |
| 2D, k=1 | 16 | 0.000300230 | 9.837936 | 9.901354 |
| 3D, k=2 | 2 | 0.375000 | 16.000000 | 24.000000 |
| 3D, k=2 | 3 | 0.0370370 | 18.000000 | 21.600000 |
| 3D, k=2 | 4 | 0.00686468 | 18.745166 | 20.773284 |
| 3D, k=2 | 5 | 0.00183344 | 19.098301 | 20.396780 |

Empirical log-log slopes over these finite ranges:

| sector | legacy diagonal | corrected DEC | consistent FEEC |
|---|---:|---:|---:|
| 2D, k=1 | +3.9650 | −0.0350 | +0.0345 |
| 3D, k=2 | +5.8052 | −0.1948 | +0.1792 |

Thus the historical convention reproduces the apparent `h^{2d}`
collapse, while the top-corrected DEC and consistent FEEC sequences remain
bounded away from zero and approach finite positive limits in these tests.
The original `h^{2d}` observation is real for the archived matrix family,
but it is not evidence of a de Rham discrete-compactness failure: it is
generated by the legacy top-degree mass normalization in this experiment.

### 1.7.2 Lumped-versus-consistent identity

On flat affine cubical meshes, the top-corrected diagonal DEC matrices are
exactly the row-sum lumping of the assembled tensor-product FEEC mass matrices
in every degree. This identity is checked in CI in both 2D and 3D. The
consistent FEEC spectra differ modestly from the corrected lumped spectra
at coarse resolution and move toward them under refinement.

The implementation is in `ddr/feec_mass.py`, the three-way comparison in
`compare_mass_matrices.py`, and the refinement driver in
`mass_refinement_study.py`. The reproducible method and limitations are
documented in `docs/CONSISTENT_FEEC_MASS.md`.

### 1.7.3 Revised scientific status

- **Verified numerically:** the legacy diagonal convention produces the
  archived collapse; correcting only `M_d` removes it on the tested affine
  sequences; consistent FEEC masses give the same qualitative non-collapse.
- **Not proved:** asymptotic convergence of either corrected sequence,
  discrete compactness on general curvilinear meshes, Mosco convergence,
  or spectral convergence on non-affine refinements.
- **Next valid question:** repeat the three-way comparison on fixed-amplitude
  curved maps with verified global diffeomorphism, quadrature convergence,
  and uniform metric bounds. Only a residual collapse there would motivate
  a separate compactness investigation.
