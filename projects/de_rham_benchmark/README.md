# Discrete de Rham benchmark on curvilinear cubical meshes

Computational research benchmark investigating numerical stability and
possible failure mechanisms of discrete Hodge–de Rham complexes under
mesh refinement, in dimensions 2 and 3.

## Layout

```
ddr/
  mesh.py        cubical mesh + oriented incidence complex (d_k matrices)
  geometry.py    cell maps Phi, pullback metric g_K = DF^T G DF, quadrature,
                 historical diagonal Hodge weights M_k
  hodge.py       codifferentials, Hodge Laplacian, spectral analysis,
                 algebraic residuals, Betti numbers
  experiment.py  experiment driver (refinement sequences + sweeps)
  plotting.py    convergence / spectral / geometry plots
configs/default.json   reproducible experiment configuration
run_benchmark.py       CLI entry point
ASSUMPTIONS.md         all modelling conventions (read first)
REPORT.md              verified observations vs conjectures
results/               JSON output + plots
```

## Run

```bash
cd projects/de_rham_benchmark
python3 run_benchmark.py --config configs/default.json --out results/run1
```

Requires `numpy`, `scipy`, `matplotlib` (Python 3.10+).

## What is measured

* exactness residuals `||d_{k+1} d_k||` (always 0 by construction, verified)
* symmetry/adjointness/self-adjointness residuals of the discrete operators
* partition-of-unity `sum_v M0[v] = total vol_g`
* Betti numbers from incidence ranks vs numerical `dim ker Delta_k`
* Jacobian diagnostics: `det D Phi`, singular values of `D Phi`,
  `cond g_K`, minimum volume element — all refinement-independent
  quantities, plus their behaviour under amplitude/frequency sweeps
* spectra: smallest positive and largest eigenvalues of the Hodge
  Laplacian per level `k`, kernel dimensions, effective condition
  numbers, `cond(M_k)`

See `ASSUMPTIONS.md` for conventions and `REPORT.md` for the separation
between verified numerical observations and conjectures.


## Audit status

Read the [independent audit checklist](docs/INDEPENDENT_AUDIT_CHECKLIST.md) before interpreting the spectra. The original archived collapse used the historical top-degree weight M_d=vol_g(K); for integral top-degree cochains the corrected primal DEC weight is 1/vol_g(K). The three-way control and revised interpretation are in REPORT.md §1.7.


## Degree-wise diagnostic

To distinguish co-closed and top-degree modes, run the normalized energy audit in the actual Hodge inner products:

```bash
python degreewise_audit.py --dim 2 --N 8
python degreewise_audit.py --dim 3 --N 5
```

This reports the grad/curl energy fractions, normalized co-closedness defect, weighted distance to exact cochains, and generalized eigenpair residual for every degree. In top degree, positive modes are necessarily grad-only because the outgoing differential vanishes. See [the corrected report](docs/REPORT.md#16-independent-degree-wise-audit-and-correction).


## Consistent FEEC mass control

The next spectral control compares three variants on the same mesh and incidence complex: historical diagonal weights, top-corrected primal DEC weights, and full consistent tensor-product cubical FEEC Gram matrices. The affine and fixed-amplitude curved tests show that the archived h^(2d) collapse disappears with corrected top-degree normalization. See [the method and assumptions](docs/CONSISTENT_FEEC_MASS.md).

```bash
python compare_mass_matrices.py --dim 2 --N 8
python compare_mass_matrices.py --dim 3 --N 4
python compare_mass_matrices.py --dim 2 --N 8 --amplitude 0.05
python mass_refinement_study.py --dim 2 --levels 4,8,16
python mass_refinement_study.py --dim 3 --levels 2,3,4,5
python test_consistent_mass.py
```

## FEEC projections and discrete adjoints

The projection/adjoint benchmark measures de Rham face-integral projections `pi_h`, the commutator `d_h pi_h = pi_h d`, `L^2`/`H-Lambda` approximation errors, the discrete codifferential `delta_h = M^{-1} D^T M` against the continuous codifferential on analytic test forms, mass stability, and spectral indicators — on affine, sinusoidal and `axis_bump` curvilinear maps in 2D and 3D. The unconstrained complex develops an `O(1/h)` boundary layer in `delta_h pi_h u` near `dOmega`; interior and compactly-supported residuals are reported separately. See [the method, assumptions and limitations](docs/FEEC_PROJECTIONS.md).

```bash
python run_feec_study.py configs/feec_default.json --out results/feec
python test_feec_study.py
```

## Golden / supergolden synthesis

The conditional synthesis connecting the de Rham–FEEC complex, curvilinear geometry, Mosco convergence, and the exact algebraic scale identities for the golden ratio and supergolden constant is in [PHI_PSI_FEEC_SYNTHESIS.md](docs/PHI_PSI_FEEC_SYNTHESIS.md). It distinguishes proved identities from candidate refinement laws and open convergence results.

## Independent mathematical audit

A source-level audit of the cubical FEEC mass construction, incidence orientations, discrete adjoints, commuting projections, Mosco convergence, discrete compactness, norm-resolvent convergence, and harmonic-kernel stability is available in [INDEPENDENT_MATHEMATICAL_AUDIT.md](docs/INDEPENDENT_MATHEMATICAL_AUDIT.md). It records a concrete incidence-orientation mismatch and separates verified algebraic facts from convergence hypotheses that remain open.


### Independent audit: W(G2) lift and Möbius seam

The algebraic audit is available at
[`audits/audit_g2_mobius_lift.py`](audits/audit_g2_mobius_lift.py), with regression
tests in [`tests/test_g2_mobius_lift_audit.py`](tests/test_g2_mobius_lift_audit.py).

Run the synthetic self-test:

```bash
python projects/de_rham_benchmark/audits/audit_g2_mobius_lift.py --self-test
```

Run the full built-in audit. The program generates the order-12 Weyl group,
its six-element short-root orbit, all 216 ordered triplettes, and the 20 exact
Gram/Weyl classes. Supply only the geometric parameters:

```json
{
  "rho": 1.465571231876768,
  "alpha_star": 0.7,
  "mobius_levels": [1, 2, 3, 4, 5, 6]
}
```

The repository includes an illustrative parameter file at
`audits/g2_mobius_parameters.example.json` (`alpha_star=1) is a unit normalization
for exercising the candidate formula, not a physically calibrated value). Run:

```bash
python projects/de_rham_benchmark/audits/audit_g2_mobius_lift.py projects/de_rham_benchmark/audits/g2_mobius_parameters.example.json --output audit_report.json
```

The sine formula for `alpha(rho)` is explicitly marked as a candidate interpolation;
the audit does not claim it is derived from the Weyl group.

The report checks (R_Tc_T=0), rank completion, the determinant identity,
positive definiteness, planar Gram classes, and the two-sided Möbius boundary
involution. It explicitly does **not** certify face-trace matching, a conforming
3D volume mesh, or FEEC/Mosco convergence.


### Serhii Herasymov: symbolic billiards, curved surfaces, and recursive 3D fields

The source-based integration is documented in
[\`docs/HERASYMOV_SYMBOLIC_GEOMETRY_INTEGRATION.md\`](docs/HERASYMOV_SYMBOLIC_GEOMETRY_INTEGRATION.md).
It keeps separate (i) the billiard-to-symbolic-sequence construction,
(ii) the graph embedding and induced surface metric,
(iii) the recursive 3D voxel/perfect-shuffle construction, and
(iv) the RGS \(W(G_2)\) geometric lift and Möbius seam.

Run the source-faithful finite/algebraic audit:

\`\`\`bash
python projects/de_rham_benchmark/audits/audit_herasymov_symbolic.py --self-test
\`\`\`

Regression tests are in
\`tests/test_herasymov_symbolic_audit.py\`.
The Boolean and rotation-enhanced 3D sources both select rules on eight interleaved parity sublattices, not contiguous octants. The audit exhausts all 256 rotation-generator modes and separates coordinate action from scalar increments. In addition, all 32 distinct uniform signed-permutation maps are checked as exact chain automorphisms of a fixed cubical grid. This does not establish a coarse-to-fine refinement map for mixed parity rules or FEEC convergence.


### Exact cubical subdivision chain map

The standard coarse-to-fine cubical subdivision operator is audited over
integer chains, including boundary commutation and naturality under all 48
signed-permutation symmetries of the cube. See
[the construction and limitations](docs/CUBICAL_SUBDIVISION_CHAIN_MAP.md).

Run:

```bash
python projects/de_rham_benchmark/audits/audit_cubical_subdivision_chain_map.py --size 2
pytest -q projects/de_rham_benchmark/tests/test_cubical_subdivision_chain_map.py
```

This is a mathematically exact subdivision operator, not yet an identification
of Herasymov's mixed parity recursion with a conforming geometric subdivision.


### Herasymov parity rules: exact shared-face criterion

The rotation-enhanced generator's eight parity-selected affine cube maps
are now audited for pointwise conformity on every internal shared face.
For refinement levels N>=2, the necessary and sufficient condition is
that all eight continuous affine cube isometries are identical. The audit
compares face traces exactly over doubled integer coordinates and keeps
the scalar increment bit separate from geometry.

See [the theorem and proof](docs/HERASYMOV_PARITY_FACE_CONFORMITY.md).

Run:

~~~bash
python projects/de_rham_benchmark/audits/audit_herasymov_parity_face_conformity.py --self-test
pytest -q projects/de_rham_benchmark/tests/test_herasymov_parity_face_conformity.py
~~~

This characterizes the explicit cellwise-affine geometric interpretation;
it does not assert that the original voxel-value recursion alone defines
that geometry, nor does it prove FEEC stability or Mosco convergence.
