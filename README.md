# Discrete de Rham benchmark on curvilinear cubical meshes

Computational research benchmark investigating numerical stability and
possible failure mechanisms of discrete Hodge–de Rham complexes under
mesh refinement, in dimensions 2 and 3.

## Layout

```
ddr/
  mesh.py        cubical mesh + oriented incidence complex (d_k matrices)
  geometry.py    cell maps Phi, pullback metric g_K = DF^T G DF, quadrature,
                 diagonal Hodge weights M_k
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
cd de_rham_benchmark
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
