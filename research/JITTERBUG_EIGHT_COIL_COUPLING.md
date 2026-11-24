# Jitterbug eight-coil coupling: implementation note

**Status:** implementation draft; numerical and physical validation pending.

## Scope

This extension reuses the standard 12-vertex Gray Jitterbug path and attaches one circular multi-turn coil to each of its eight rigid triangular panels. Each coil is defined in its panel-local frame; the panel pose is reconstructed from its three labelled vertices by a proper Kabsch fit. This is a distinct extension of the existing one-panel Model A in `audits/jitterbug_coil_coupling.py`.

The implementation is in `audits/jitterbug_eight_coil_coupling.py`; primitive regression tests are in `tests/test_jitterbug_eight_coil_coupling.py`.

## Geometry and external flux

For each sign triple \(\varepsilon\in\{\pm1\}^3\), let \(R_\varepsilon(t)\) and \(c_\varepsilon(t)\) be the proper rigid pose of the corresponding triangular panel, and let \(n_{\varepsilon,0}\) be its oriented reference normal. A circular coil of radius \(r\), area \(A=\pi r^2\), and turn count \(N_\varepsilon\) is fixed in that panel. For a uniform static imposed field \(B\),

\[
\lambda_{\varepsilon}^{\rm ext}(t)
=N_\varepsilon A\,B\cdot R_\varepsilon(t)n_{\varepsilon,0},
\qquad
e_{\varepsilon}^{\rm ext}(t)
=-\frac{d\lambda_{\varepsilon}^{\rm ext}}{dt}.
\]

The chosen radius is constrained to the inradius of an equilateral panel,
\(0<r<a_J/(2\sqrt3)\). The path parameter is converted to time by an explicit constant speed; this is a user-declared drive, not an intrinsic Jitterbug frequency.

## Inductance matrix

For distinct loops, the code approximates the Neumann integral by polygonal segment quadrature:

\[
M_{ij}\approx \frac{\mu_0N_iN_j}{4\pi}
\sum_{a,b}\frac{\Delta\ell_{i,a}\cdot\Delta\ell_{j,b}}
{\sqrt{|r_{i,a}-r_{j,b}|^2+\delta^2}}.
\]

The softening \(\delta\) regularizes near intersections and is an explicit numerical parameter. The diagonal uses the thin-wire circular-loop approximation

\[
L_{ii}=\mu_0N_i^2r_i\left[\log\left(\frac{8r_i}{a_w}\right)-2\right],
\]

where \(a_w\) is the wire radius. This diagonal approximation assumes a thin isolated circular wire; it is not a substitute for a detailed conductor cross-section model. Mutual terms are reciprocal by construction. Positive semidefiniteness of the full matrix is reported as a diagnostic, not imposed by projection; a negative eigenvalue beyond discretization tolerance is a failed model check.

## Coupled circuit evolution

With \(L(t)\) the full 8-by-8 inductance matrix, \(R\) the resistance matrix, \(i\) the coil-current vector, and \(\lambda^{\rm ext}\) the imposed-field flux-linkage vector, the sign convention is

\[
\frac{d}{dt}\bigl(L(t)i(t)\bigr)+R i(t)
=-\frac{d\lambda^{\rm ext}}{dt}=e^{\rm ext}(t).
\]

The implementation uses an implicit-midpoint discretization of this equation. It does not replace the system with eight independent RL circuits: off-diagonal mutual terms and the time variation of \(L\) are retained.

## Reproduction

From the repository root:

```bash
python3 audits/jitterbug_coil_coupling.py --output jitterbug_one_coil_report.json
python3 -m unittest discover -s tests -p 'test_jitterbug_coil_coupling.py' -v
python3 audits/jitterbug_eight_coil_coupling.py --output jitterbug_eight_coil_report.json
python3 -m unittest discover -s tests -p 'test_jitterbug_eight_coil_coupling.py' -v
```

The multi-coil script currently reports panel-fit residuals, inductance reciprocity, minimum inductance-matrix eigenvalue, external emf and current extrema, and full time series.

## Validation still required

1. Run both legacy one-coil and new primitive test suites in a clean environment; archive interpreter and NumPy versions and report hashes.
2. Perform segment-count convergence for mutual inductances (e.g. 48, 96, 192, 384) and softening sensitivity. The current default regularization is a numerical control, not a measured wire model.
3. Compare a separated, coaxial two-loop result with a trusted analytic/reference calculation.
4. Confirm the inductance matrix is positive semidefinite over the complete motion. The present diagonal thin-wire approximation and softened off-diagonal quadrature may not guarantee this.
5. Add physically meaningful resistance, wire cross-section, lead routing, capacitive effects if relevant, magnetic-field source and load data.
6. Derive and test a complete mechanical/electromagnetic energy balance, including the generalized mechanical force associated with \(\partial L/\partial q\), external-field work and Joule heating. This energy audit is **not yet implemented**.
7. Compare wiring/polarity configurations only after explicit winding orientation and electrical interconnection are specified.

## Scientific boundary

This is a conditional quasi-static lumped-circuit calculation. It does not demonstrate a working generator, useful power, energy gain, self-sustaining operation, a torsion-induced voltage, or a new electromagnetic law. The eight-panel Jitterbug is not yet embedded in the separate 64-TG/FCC-D3 realization. The Vesica/Q6 correspondence and the Cartan-torsion issue remain separate geometric/theoretical questions.

## Links

- [Issue #409 — eight-coil extension](https://github.com/fabianleonaressi95/theorem/issues/409)
- [Issue #398 — Vesica to eight Jitterbug panels](https://github.com/fabianleonaressi95/theorem/issues/398)
- [Issue #399 — geometric connection](https://github.com/fabianleonaressi95/theorem/issues/399)
- [Issue #400 — Cartan torsion and variation](https://github.com/fabianleonaressi95/theorem/issues/400)
- [Issue #401 — dynamic 64-TG/FCC-D3 embedding](https://github.com/fabianleonaressi95/theorem/issues/401)
- [PR #390 — original one-panel coil model](https://github.com/fabianleonaressi95/theorem/pull/390)
