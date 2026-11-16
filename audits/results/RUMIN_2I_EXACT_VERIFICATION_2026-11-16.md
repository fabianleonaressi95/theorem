# Rumin / Poincaré-sphere exact verification record

**Date:** 2026-11-16  
**Repository:** `fabianleonaressi95/theorem`  
**Branch:** `main`  
**Commit:** `e6f9bbb0ca13fa3c839c3b3f7d66e9704bdb9201`  
**CI:** [Run 43909122496 — successful](https://github.com/fabianleonaressi95/theorem/actions/runs/43909122496)

## Verified executions

| Item | Executed check | Result |
|---|---|---|
| T022 | `RUMIN_2I_T022_EVENTUAL_HURWITZ_AUDIT.py`, 70-digit precision, all nine irreducibles | PASS |
| T023 | `RUMIN_2I_T023_GAMMA_SINE_IDENTITIES.py`, exact SymPy identities | PASS |
| T032 | `t032_rumin_fixed_harmonic_matrix.py --max-p 20 --max-q 20` | PASS — 400 blocks |

## What the checks assert

- **T022:** exact rational construction of each (P_\rho=(1-t^{60})D_\rho); separation of finite preperiods from period-60 tails; correct global (60^{-2s}) Hurwitz scaling; 70-digit agreement of all nine torsions with their algebraic benchmarks.
- **T023:** no nonzero finite preperiod remains for the nine audited covariants; complementary-tail coefficient pairing; cancellation of the scale term; Euler reflection and the exceptional (Gamma(31/30)=\Gamma(1/30)/30) recurrence; exact sine products in (\mathbb Q(\sqrt5)); reconstruction of all nine torsions; (\sum_\rho(\dim\rho)^2=120).
- **T032:** for every (1\le p,q\le20), exact verification of (S=L/2), (A'=-L/2), (B'=L/2), (D^*D=G), rank one, determinant zero, trace (L^2/4), (G^2=(L^2/4)G), kernel vector ((A,B)^T), and target (U(1))-phase invariance.

## Stored machine-readable output

The successful run uploaded the three JSON reports as the artifact:

- **Name:** `rumin-exact-audit-results`
- **Artifact ID:** `14246139326`
- **SHA-256:** `b2ddb335a6af5aa2b5c56d5d6e92491f88d3236abf7ca4a8f31e86824f1c30ef`
- **Retention:** until 2027-02-14

## Scope and remaining work

These checks close the specific computational and symbolic obligations T022, T023, and T032. T024 remains a separate dimension-three operator/convention theorem under its stated common-metric and unitary-flat-coefficient hypotheses. The results do not establish a higher-dimensional extension, nor any Q6/PRISM continuum or physical consequence.
