# Jitterbug eight-coil: numerical validation extension

**Status:** reproducible validation fixtures added; results are pending the first CI run on this branch. No physical apparatus is validated by these calculations.

## 1. Mutual-inductance reference benchmark

The polygonal Neumann sum is compared with the exact mutual inductance of two separated coaxial circular filaments. For radii (a,b), axial separation (z>0), and (k^2=4ab/((a+b)^2+z^2)),

[
M=\mu_0N_1N_2\sqrt{ab}
\left[\left(\frac{2}{k}-k\right)K(k^2)-\frac{2}{k}E(k^2)\right],
]

where (K,E) are complete elliptic integrals. The reference implementation evaluates them with the arithmetic-geometric mean, independently of the polygonal Neumann quadrature.

The fixture uses (a=0.03\,\mathrm m), (b=0.025\,\mathrm m), (z=0.04\,\mathrm m), (N_1=100), (N_2=80), and reports segment counts 48, 96, 192, 384 plus softening sensitivity. For this separated geometry the expected polygonal error decreases approximately quadratically with segment count; the report records the actual errors rather than treating that expectation as a pass result.

## 2. Nonzero flux-drive probe

A second controlled fixture has eight separated circular coils in a static uniform field (B=(0,0,B_z)). Each coil undergoes a prescribed rotation about its local (y)-axis, with phase offsets between coils:

[
\theta_j(t)=\frac{\pi}{3}\frac{1-\cos(2\pi t+\varphi_j)}{2},
\qquad
\lambda_j(t)=N A B_z\cos\theta_j(t),
\qquad e_j=-\dot\lambda_j.
]

The resulting eight-component emf drives the full coupled midpoint RL solver with the time-dependent inductance matrix. The audit reports emf/current maxima, the minimum inductance eigenvalue, and reciprocity residual. This is a deliberate excitation fixture demonstrating that changing coil orientation in a static field produces nonzero flux derivative. It is **not** yet the actual eight-panel Jitterbug trajectory: the angular law is prescribed independently to avoid claiming that the existing Gray path already supplies a useful flux sweep.

## 3. Reproduction

```bash
python -m unittest tests.test_jitterbug_eight_coil_validation -v
python audits/jitterbug_eight_coil_validation.py --output jitterbug-eight-coil-validation.json
```

The GitHub Actions workflow runs these checks alongside the original six primitive tests and the reduced-resolution Jitterbug geometry run. Both JSON reports are archived together.

## 4. Interpretation and remaining work

- The coaxial benchmark tests the numerical Neumann implementation against a closed-form reference for a nonintersecting pair; it does not validate the regularized integral at intersecting/near-touching panel loops.
- Softening is a numerical regularizer, not a substitute for conductor cross-section and insulation geometry.
- The driven probe establishes a nonzero Faraday excitation for a prescribed rotating-loop geometry. It does not demonstrate that the unmodified Jitterbug mechanism produces this motion, nor that the eight coils can be wired to yield a useful output.
- Next physical-model step: derive the actual panel pose/normal histories from the Jitterbug mechanism, choose a realizable field-source geometry, calculate the field over each finite coil surface, and close the mechanical/electromagnetic energy balance including Joule loss and actuator work.
- No claim of energy gain, self-sustaining operation, generator performance, torsion-induced emf, or new electromagnetic law is made.

## Files

- `audits/jitterbug_eight_coil_validation.py`
- `tests/test_jitterbug_eight_coil_validation.py`
- `audits/jitterbug_eight_coil_coupling.py`
- `tests/test_jitterbug_eight_coil_coupling.py`
