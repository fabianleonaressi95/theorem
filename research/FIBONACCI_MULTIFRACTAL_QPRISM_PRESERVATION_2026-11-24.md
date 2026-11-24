# Preservation record — Fibonacci multifractal concavity and Q-PRISM protocol

**Date:** 24 November 2026  
**Repository:** `fabianleonaressi95/theorem`  
**Purpose:** preserve the earlier Fibonacci multifractal result and quantum-protocol design as a distinct workstream. This record does not replace TSMR-F and does not reinterpret the standard Q6 Walsh baseline as multifractal.

## 1. Why this record exists

The 24 November quantum–fractal interface initially emphasized the exact standard-Q6 Walsh calculation. That calculation is only a finite-graph control. It must not erase the earlier RGS–PRISM Fibonacci multifractal investigation and the Q-PRISM quantum-readout protocol discussed on 19 October 2026.

Three objects must remain separate:

1. **Fibonacci approximant multifractal analysis** — scale-dependent IPR/moment analysis on a family of Fibonacci lengths.
2. **Q-PRISM quantum protocol** — proposed quantum encoding, Hamiltonian evolution and randomized measurement/readout of moments.
3. **Q6/Xc geometric test** — a separate finite graph/geodesic-mass diagnostic, whose negative concavity flag does not refute the Fibonacci result.

## 2. Earlier Fibonacci multifractal record (19 October 2026)

The historical RGS–PRISM analysis used Fibonacci approximant lengths
[
Lin{144,233,377,610,987,1597},
]
and a local effective exponent convention denoted (	au_q^{mathrm{eff}}). The work investigated the curvature/concavity of the multifractal scaling curve rather than relying on the one-size Q6 Walsh IPR.

The conversation record also preserves the following later verdict:
- a nonlinear limiting (	au_infty(q)) was **compatible with** the finite data;
- asymptotic nonlinearity was **not established**;
- the reported data-collapse score (R^2=0.032733) was poor and does not support a successful collapse;
- consequently, the concavity result is a finite-family numerical observation, not an asymptotic theorem.

A prior conversational summary reported sampled (	au(q)), (alpha(q)), and negative second differences/second derivatives. Those individual table entries are **historical values pending provenance replay**: the current repository snapshot does not contain the raw Fibonacci eigenvector arrays, the exact script that generated that table, or a machine-readable report tying each value to a commit and fit window. They must not be silently promoted to canonical reproducible numbers. Preserve the result and its qualification; recover the raw arrays/script/report before publishing a definitive numerical table.

### Correct mathematical protocol

For a normalized eigenstate (psi^{(L)}), define
[
P_q(L)=sum_{i=1}^{L}|psi_i^{(L)}|^{2q}.
]
A scaling fit across lengths is
[
log P_q(L)= -	au(q)log L + c_q + epsilon_{q,L}.
]
The finite-size estimate (	au_q^{m eff}) depends on the selected length window and fit convention. The spectrum is then estimated by
[
alpha(q)=rac{d	au}{dq},qquad f(alpha(q))=qalpha(q)-	au(q),
]
subject to the chosen sign convention and the validity of the multifractal formalism.

For concavity, use a declared q-grid and report both:
- discrete second differences (Delta^2	au(q)), with grid-spacing normalization;
- uncertainty/sensitivity under changes in length window, q-grid, fit weights, eigenstate selection and degeneracy treatment.

Concavity of a finite fitted curve is not proof that a limiting (	au(q)) exists. A Legendre spectrum is a candidate spectrum unless the relevant multifractal formalism hypotheses are established.

## 3. Q-PRISM protocol already proposed (19 October 2026)

The earlier protocol proposal is retained as a design, not as a completed quantum experiment:

1. Encode an (L)-site Fibonacci approximant in (n=lceillog_2 Lceil) qubits. In particular, (L=17711) requires (n=15) address qubits.
2. Specify the Fibonacci tight-binding Hamiltonian and generate the quasiperiodic potential through a reversible on-the-fly oracle/ancilla, rather than storing an exponentially large dense matrix.
3. Prepare the target eigenstate or a spectrally filtered state. This is a critical unresolved circuit-design stage; an oracle and a Hamiltonian simulation alone do not prepare the desired eigenstate.
4. Implement real-time evolution/spectral filtering using a declared Trotter or Quantum Signal Processing construction, with error budgets and resource estimates.
5. Estimate site probabilities and moments (P_q) using randomized measurements / classical-shadow-style estimators. State the estimator, measurement ensemble, shot budget, bias and variance.
6. Repeat across a Fibonacci family of sizes and compare the quantum estimates with the classical exact-diagonalization reference.
7. Report resource estimates, state-preparation cost, circuit depth, shots, error bars and classical baselines. No quantum advantage is claimed without a like-for-like benchmark.

The earlier proposal mentioned lengths up to (F_{21}=17711), corresponding to 15 address qubits. The currently preserved historical finite-size analysis explicitly lists (144,233,377,610,987,1597); the larger (F_{21}) value is a proposed/mentioned scale, not evidence that a 17,711-site quantum run was executed.

**Status:** protocol architecture proposed; no gate-level circuit, shot-based run, hardware execution, or measured quantum multifractal spectrum is established by this record.

## 4. The separate Q6/Xc test (21 October 2026)

A distinct test used 440 sampled local/geodesic mass exponents on a finite Q6/Xc construction and returned `concavity=False`. That flag refers to that test's finite sample and estimator. It does not negate the Fibonacci IPR result because:
- the underlying object is different (geodesic mass sample versus Fibonacci Hamiltonian eigenstates);
- the observable and partition/scaling procedure differ;
- the finite-size family and q-grid differ.

The Q6 test should be retained as a negative/diagnostic result, not generalized to all PRISM or Fibonacci multifractality.

## 5. Repository crosswalk and non-duplication

Canonical related records:
- `audits/tsmr_f_multifractal.py` — exact separated Cantor–Bernoulli `tau(q)` and generalized dimensions, plus finite-level self-affine pressure diagnostic. This is not the Fibonacci tight-binding eigensolver.
- `tests/test_tsmr_f_multifractal.py` — regression tests for those exact model identities and finite pressure implementation.
- `theorems/TSMR-F_multifractal_morphological_equation.md` — exact separated Bernoulli model and proposed general TSMR-F framework.
- `theorems/T056-phase21-trigram-supergolden-permutation-conjugacy.md` — exact three-state transfer-matrix permutation conjugacy; not a Fibonacci quantum Hamiltonian and not a Q6 geometric refinement theorem.
- `research/QUANTUM_FRACTAL_PRISM_Q6_INTERFACE_2026-11-24.md` — Q6/Walsh and cross-model interface note.

Do not overwrite or relabel the Cantor–Bernoulli audit as Fibonacci data. Do not treat the Phase-21 Perron root (psi) or the finite Q6 Walsh spectrum as evidence for Fibonacci eigenstate multifractality.

## 6. Required recovery/replay before upgrading the numerical record

Recover the 19 October source script, raw eigenvectors or moment arrays, exact Fibonacci word/potential convention, hopping and coupling parameters, eigenstate/energy-window selection, normalization, q-grid, fit windows and uncertainty procedure. Replay the fits and concavity checks from those sources. If the original data cannot be recovered, retain the numerical result as a historical conversation-reported observation and rerun a separately labelled reproducibility study; do not claim it reproduces the old table.

For Q-PRISM, write a separate gate-level resource specification only after fixing the target state-preparation method and observable estimator. The first practical benchmark should compare a small classical Fibonacci approximant against an explicit quantum-circuit simulation with finite shots; it must not be described as a hardware result.

## 7. Classification

| Item | Classification | What is supported |
|---|---|---|
| Separated Cantor–Bernoulli (	au(q)) | Exact model identity | Implemented and regression-tested in TSMR-F |
| Fibonacci finite-family concavity | Historical numerical result; provenance replay pending | Earlier analysis reported concavity on finite Fibonacci approximants |
| Nonlinear asymptotic (	au_infty(q)) | Open | Finite compatibility only; asymptotic limit not established |
| (R^2=0.032733) data collapse | Historical diagnostic | Poor collapse; no positive scaling-collapse claim |
| Q-PRISM | Proposed quantum protocol | Architecture proposed; no executed quantum experiment |
| Q6/Xc `concavity=False` | Separate finite diagnostic | Does not refute Fibonacci result |
| Transfer-matrix conjugacy T056 | Exact finite algebra | No geometric/quantum equivalence implied |


## 8. Companion-repository records recovered on 24 November

The companion repository `fabianleonaressi95/rgs-qlg-quaternion-bridge` contains additional multifractal infrastructure that must also be preserved:
- `docs/RGS_PSU_MULTIFRACTAL_VECTOR_BUNDLE.md` and `src/rgs_psu_multifractal_bundle.py` define a rank-three bundle over the eight Q3 labels, a metric-compatible seed-induced GL(3) connection, and a nested-measure multifractal slope diagnostic. The canonical connection is explicitly flat/pure gauge; it does not supply nonzero Yang–Mills curvature.
- `tests/test_rgs_psu_multifractal_bundle.py` verifies flatness/gauge covariance and two synthetic controls: a uniform measure and a nonuniform binomial cascade. These tests validate the estimator on synthetic data; they do not establish that the RGS seed itself is multifractal.
- `data/prism_fibonacci/` contains Fibonacci-labelled geometric/PRISM audits (including window, center-placebo, block-sector and phase audits). These are not automatically the missing Fibonacci tight-binding eigenvector/IPR arrays from the 19 October analysis; their observable and provenance must be matched before use.
- `experiments/rgs_psu_core/RGS_PSU_Multifractal_Cascade_Viscosity.py` and `RGS_PSU_Multifractal_Shear_Bridge_Integrated.py` contain older cascade/shear prototypes. Their comments assert physical viscosity/cascade interpretations that are not derived by the code: the scripts use prescribed exponents/scales and synthetic action/Langevin models. Treat them as exploratory prototypes, not as validated multifractal or Navier–Stokes/gauge results.

These companion records complement, but do not replace, the missing provenance for the historical Fibonacci eigenstate concavity table and the Q-PRISM gate-level circuit specification.
