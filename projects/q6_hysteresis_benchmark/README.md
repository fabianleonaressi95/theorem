# Q6 topological synchronization and industrial hysteresis benchmark

## Scope

This project implements a finite-cell benchmark inspired by Ghorbanchian et
al., "Higher-order simplicial synchronization of coupled topological
signals", Communications Physics 4, 120 (2021),
https://doi.org/10.1038/s42005-021-00605-4.

The paper defines NL and NLT dynamics on nodes and links of a simplicial
complex. Here Q6 is represented by the 2-skeleton of the six-dimensional
cube: 64 vertices, 192 edges and 240 square 2-cells. This is an explicit
cubical extension, not a claim that the paper studied Q6.

## Exact combinatorial layer

B1 has shape 64 x 192 and B2 has shape 192 x 240. Their entries are integers
and B1 B2 = 0 is checked exactly. The graph cycle rank is 129. The square
boundaries span the full graph cycle space (rank B2 = 129), so b1 of the
2-skeleton is zero. The 2-skeleton has nontrivial H2 because 3-cells are
omitted; no claim of contractibility is made.

Bitwise complement Anti-Twin lifts to signed permutation maps J0,J1,J2.
The audit checks J0 B1 = B1 J1, J1 B2 = B2 J2 and Jk^2 = I.

## Dynamical layer

NL and NLT vector fields are transcribed from Eqs. (12)-(13) and (16)-(17)
of the 2021 paper. Triangular faces are replaced by Q6 square cells. Order
parameters are computed from node phases, B1 phi and B2^T phi. The runner
uses a continuation sweep in sigma and starts the reverse sweep from the
terminal forward state, with the same intrinsic frequencies.

This is a finite-size exploratory numerical benchmark. A hysteresis claim
requires longer relaxation, sweep-rate controls, multiple seeds, and
robustness to initialization. It is not a thermodynamic-limit proof.

## Industrial hysteresis is a separate validation track

Explosive synchronization hysteresis is a bifurcation/continuation phenomenon.
Constitutive hysteresis is path dependence in measured input/output response,
for example magnetization, strain or actuator displacement. They are not
interchangeable.

The repository supplies model-independent loop metrics (closed-loop area,
RMSE and loading/unloading branch separation). It does not yet identify a
constitutive law. Industrial comparisons must include established baselines:
Preisach, Prandtl-Ishlinskii, Bouc-Wen and, for ferromagnets, Jiles-Atherton.

Every model must use identical training/validation splits and excitation
protocols. Report prediction error, loop-area/energy error, reversal-point
error, unseen-cycle generalization, computational cost and compensation
residual. No industrial performance is claimed without experimental data.

## Reproduction

From repository root:

    python -m pytest -q tests/test_q6_topological_synchronization.py tests/test_hysteresis_metrics.py
    python scripts/run_q6_hysteresis_benchmark.py --output /tmp/q6-hysteresis.json

## Status

- Exact finite incidence identity and Anti-Twin chain identities: implemented
  and tested.
- NL/NLT vector fields: implemented on the cubical Q6 complex.
- Q6 dynamical hysteresis: open pending convergence and finite-size controls.
- Industrial constitutive prediction: open pending experimental datasets and
  parameter identification.
- PSU, QCD or gravitational interpretation: not established here.
