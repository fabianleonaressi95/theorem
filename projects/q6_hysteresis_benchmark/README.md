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
2-skeleton is zero. Because C3 is omitted, the truncated 2-skeleton has b2 = 240 - 129 = 111.
These classes are killed when the 3-cells of the full cube are restored.
2-skeleton is zero. The 2-skeleton has nontrivial H2 because 3-cells are
omitted; no claim of contractibility is made.

Bitwise complement Anti-Twin lifts to signed permutation maps J0,J1,J2.
The audit checks J0 B1 = B1 J1, J1 B2 = B2 J2 and Jk^2 = I.

## Dynamical layer

NL and NLT vector fields are transcribed from Eqs. (12)-(13) and (16)-(17)
of the 2021 paper. Triangular faces are replaced by Q6 square cells. Order
parameters are computed from node phases, B1 phi and B2^T phi. The runner
uses a continuation sweep in sigma and starts the reverse sweep from the
terminal forward state, with exactly the same intrinsic frequencies. The
frequency sampler follows the source-paper convention: node frequencies
N(Omega0, 1/tau0) and link frequencies N(Omega1, 1/tau1), with the common
node drift removed by a co-rotating node frame and the link-frequency mean
retained. Separate random streams ensure branch initialization cannot change
the intrinsic frequency samples.
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
RMSE and loading/unloading branch separation), plus executable reference
implementations of discrete Preisach relays, Prandtl-Ishlinskii play operators
and Bouc-Wen dynamics. Linear operator weights can be fitted by least squares
for fixed threshold dictionaries. This is a software benchmark on synthetic
signals, not an industrial validation. Jiles-Atherton is a material-specific
ferromagnetic comparator and remains to be added with a clearly specified
convention and measured B-H data.

Every model must use identical training/validation splits and excitation
protocols. Report prediction error, loop-area/energy error, reversal-point
error, unseen-cycle generalization, computational cost and compensation
residual. The present tests only check implementation and synthetic fit
plumbing; they do not establish that any model outperforms another. No
industrial performance is claimed without experimental data.

## Reproduction

From repository root:

    python -m pytest -q tests/test_q6_topological_synchronization.py tests/test_hysteresis_metrics.py tests/test_constitutive_hysteresis.py tests/test_q6_hysteresis_sweep_study.py
    python scripts/run_q6_hysteresis_benchmark.py --output /tmp/q6-hysteresis.json
    python scripts/run_q6_hysteresis_sweep_study.py --seeds 11,23,37,51,67 --dwell-steps 10,40,160,640 --sigma-max 2 --sigma-count 21 --dt 0.025 --omega0 2 --omega1 2 --tau0 1 --tau1 1 --output results/q6_hysteresis_sweep_study.json --plot-prefix results/q6_hysteresis_sweep

## Latest corrected production results

See [corrected five-seed, four-rate results and interpretation](RESULTS_2026-11-09.md). The production workflow artifact contains the full JSON branches and NL/NLT plots. The earlier sweep performed before the frequency-stream audit is superseded and must not be cited.
    python -m pytest -q tests/test_q6_topological_synchronization.py tests/test_hysteresis_metrics.py
    python scripts/run_q6_hysteresis_benchmark.py --output /tmp/q6-hysteresis.json

## Status

- Exact finite incidence identity and Anti-Twin chain identities: implemented
  and tested.
- NL/NLT vector fields: implemented on the cubical Q6 complex.
- Q6 dynamical hysteresis: multi-seed/multi-dwell finite-size protocol study implemented; robust transition remains open pending production sweeps and initialization controls.
- Industrial constitutive prediction: open pending experimental datasets and
  parameter identification.
- PSU, QCD or gravitational interpretation: not established here.


## Multi-seed and multi-rate protocol study

Run the controlled finite-size sweep study:

    python scripts/run_q6_hysteresis_sweep_study.py \
      --seeds 11,23,37,51,67 --dwell-steps 10,40,160 \
      --sigma-max 2 --sigma-count 21 --dt 0.025 \
      --output results/q6_hysteresis_sweep_study.json \
      --plot-prefix results/q6_hysteresis_sweep

The effective parameter sweep rate is Delta_sigma/(dwell_steps * dt). The
same seed reproduces the same initial phases and source-paper frequency samples across
dwell settings; forward and backward branches share exactly the same frequencies. The backward branch begins at the terminal forward state.
The JSON stores every branch, per-seed branch-gap/loop-area metrics, and
mean/standard deviation across seeds. Two PNGs compare forward and backward
branches for NL and NLT, showing mean curves and seed dispersion.

These controls test protocol sensitivity at one fixed Q6 size. They do not
establish a thermodynamic limit. Different seeds jointly change intrinsic
frequencies and initial phases; a separate fixed-frequency/multiple-initial-
condition study remains a useful next control.
- Q6 dynamical hysteresis: open pending convergence and finite-size controls.
- Industrial constitutive prediction: open pending experimental datasets and
  parameter identification.
- PSU, QCD or gravitational interpretation: not established here.


## Industrial constitutive models and experimental data

The synchronization experiment above is a finite graph-dynamics study; it is not a material test. The repository now also includes independent constitutive baselines:

- Preisach relay model and Prandtl–Ishlinskii play-operator model;
- Bouc–Wen rate-dependent phenomenological model;
- scalar quasi-static Jiles–Atherton magnetic model.

See [public experimental dataset registry and validation protocol](../../docs/INDUSTRIAL_HYSTERESIS_DATASETS.md). A non-destructive [CSV schema/quality auditor](../../scripts/audit_hysteresis_csv.py) records headers, missing values, numeric ranges and SHA-256 without guessing units or channel semantics.

No experimental model fit has yet been performed in this repository. The first priority is to audit the Zenodo hydrogel-based pneumatic bending-actuator dataset (0.05 Hz triangular excitation; source article reports asymmetric loops) and then compare models on complete held-out cycles. The current PI implementation is a classical play-operator baseline, not the Generalized Prandtl–Ishlinskii model; an asymmetric/GPI extension is required before claiming parity with the strongest model reported in the source article.
