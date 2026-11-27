# Volterra dipole-to-edge: periodic Airy stress and energy test

## Purpose

This test advances the comparison from source profiles to the elastic response. It solves the same periodic Airy problem for an opposite wedge-disclination pair and a matched edge-dislocation source. The pair is assigned Frank magnitude `Omega`; the edge source is assigned Burgers magnitude `b = Omega*d`.

## Matched incompatibility sources

With normalized periodized Gaussian core profiles `delta_rho(x-x0)` and `f_sigma(y)`, the two incompatibilities are

\[
\zeta_d(x,y)=\Omega\,\delta_\rho(x-x_0)
 [f_\sigma(y-d/2)-f_\sigma(y+d/2)],
\]

and

\[
\zeta_e(x,y)=-b\,\delta_\rho(x-x_0)f_\sigma'(y),
\qquad b=\Omega d.
\]

The finite-dipole source converges to the edge source as `d/sigma -> 0`. Both are passed to the same Fourier Airy solver, with identical periodic domain, plane-strain Lamé parameters, core width, zero-mean stress convention and spectral discretization.

For each source the solver computes the Airy potential, stress, elastic strain and energy. The report compares relative L2 stress and strain differences and relative energy difference. It also records the spectral compatibility residual and source mean.

## Reproduction

Run:

```bash
python scripts/rgs_volterra_elastic_limit.py --out artifacts/volterra_elastic_limit
```

The sweep includes `d/h = 1, 1.5, 2, 2.5, 3, 4, 8`, `sigma/h = 2, 3.2, 4, 6.4`, and mesh sizes `64, 96, 128, 192, 256`. A separate fixed-grid small-separation sequence reduces `d/sigma` while holding the core fixed. Output is written to JSON and CSV.

The dedicated GitHub Actions workflow runs both source-profile tests and elastic-limit tests, then uploads the stress/energy report.

## Interpretation and limitations

- This is an elasticity-level comparison: stress and energy are computed from both matched incompatibility sources, not inferred from source-profile error.
- `d=2h` is only one grid-alignment case. The continuum parameter controlling the dipole approximation is `d/sigma`.
- The solver is Fourier-spectral on a periodic torus. It is not yet a displacement-Q1/P1 cross-check or the perforated-domain C0-IPDG solver of Cesana–Fabbrini–León Baldelli–Morandotti.
- The core is smooth and finite. No singular-core limit, renormalized energy, atomistic interpretation, Mosco convergence or Gamma convergence is claimed.
- The zero Fourier mode is fixed to zero mean stress. Applied macroscopic stress and non-periodic traction-free boundaries are outside this test.

The numerical conclusion must be taken from the CI artifact after the workflow passes. The code and tests alone are not numerical evidence that the limit has passed.
