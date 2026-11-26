# Cymatics and wave morphogenesis — research programme

**Status:** research programme / benchmark implementation  
**Scope:** mathematical spectral theory, elastic-wave morphology, discrete geometry, and a separately gated plasma application.

## Purpose

This programme studies how excitation, boundary conditions, material parameters, geometry, and dissipation shape observable spatial patterns of oscillating systems. “Cymatics” is used here in its experimentally grounded sense (patterns associated with vibrational fields); the broader mathematical subject is **wave morphogenesis**.

The programme does not assume that visual similarity between Chladni patterns, helicon fields, and RGS/PRISM structures establishes a physical equivalence. Each bridge requires an explicit operator, units, boundary conditions, and validation data.

## Work packages

| ID | Work package | Deliverable | Status |
|---|---|---|---|
| C01 | Simply supported square Kirchhoff–Love plate benchmark | Discrete spectrum and analytic convergence check | Implemented baseline |
| C02 | Square symmetry and modal degeneracy | Degeneracy/symmetry regression | Implemented baseline |
| C03 | Perturbation and mode mixing | Controlled symmetry-breaking experiment | Implemented baseline |
| C04 | Q6 hypercube graph spectral control | Exact graph-Laplacian multiplicity check | Implemented baseline; not a plasma model |
| C05 | Helicon wave propagation | Geometry-aware electromagnetic eigenmode model | Open |
| C06 | Plasma current-drive coupling | Kinetic/EM coupling and comparison with published measurements | Open |

C01–C04 are mathematical/computational controls. They do **not** yet establish predictive superiority of RGS or PRISM over classical spectral methods. C05–C06 remain separate physics work packages.

## Governing model

For a linear second-order system,
[
M\ddot u+D\dot u+Ku=f(t),
]
a harmonic response (u(t)=\Re(Ue^{-i\omega t})) satisfies
[
(K-\omega^2M-i\omega D)U=F_\omega.
]
This is a common abstract form, not a claim that the same (M,D,K) apply unchanged to plates, acoustic media, electromagnetic plasmas, and kinetic models.

For a homogeneous, simply supported Kirchhoff–Love plate on a square of side (L),
[
D_b\Delta^2 w+\rho h\,\partial_t^2w=0,
qquad
w=\Delta w=0\quad\text{on the boundary}.
]
The separated modes are
[
w_{mn}(x,y)=\sin(m\pi x/L)\sin(n\pi y/L),
quad
\omega_{mn}=\sqrt{D_b/(\rho h)}\,\pi^2(m^2+n^2)/L^2.
]
The C01 implementation uses a dimensionless finite-difference Laplacian and its square, with (D_b/(\rho h)=1) and (L=1).

## RGS / PRISM integration rules

1. Reuse existing Q6, RGS 188D, (O_h), PSU, and PRISM/Krist-All records only through explicit maps and compatible inner products.
2. Do not infer that the Q6 hypercube graph is a discretization of a vibrating plate or a helicon plasma.
3. Do not import arbitrary cube–sphere weights. Any weight must follow from a stated action, metric, or discretization.
4. Record the operator domain, boundary conditions, units/scales, symmetry group, and normalization for every comparison.
5. Compare against classical FEM/finite-difference baselines before claiming an RGS/PRISM advantage.

## Epistemic classification

- **Proved/classical:** the stated separated spectrum for the ideal simply supported square plate; Courant's nodal-domain theorem under its hypotheses; standard finite-dimensional self-adjoint perturbation results.
- **Numerically verified by this PR:** the finite-difference plate eigenvalues against their discrete analytic values; square-mode degeneracy; splitting under an asymmetric perturbation; Q6 graph-Laplacian multiplicities.
- **Candidate:** stability and topology of nodal sets under perturbations for specified operator families.
- **Hypothesis:** an RGS/PRISM geometric operator can predict experimentally observed morphology beyond a matched classical baseline.
- **Open:** a validated helicon operator lift and prediction of plasma current drive from the proposed discrete geometry.

## Reproduction

Requirements: Python 3.10+ and NumPy.

```bash
python scripts/cymatics_wave_benchmarks.py --output results/cymatics_baseline.json
python -m unittest discover -s tests -p 'test_cymatics_wave_benchmarks.py' -v
```

The script emits deterministic JSON metrics. It does not retrieve experimental data or claim a fit to DIII-D.

## Next steps

- Extend C01 to rectangular domains and convergence under grid refinement.
- Add a Kirchhoff–Love plate model with experimentally specified supports and damping.
- Add measured Chladni nodal-set extraction with uncertainty estimates.
- Define a geometry-derived RGS/PRISM operator and test it against the same benchmarks.
- Only then formulate C05; C06 requires a kinetic/electromagnetic model and source-resolved experimental data.
