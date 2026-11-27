# Jiles–Atherton local identifiability audit — Zenodo 17053338

**Date:** 2026-11-26  
**Input:** the `hysteresis_analysis_report.json` and `reconstructed_BH_loops.csv` files in GitHub Actions artifact [hysteresis-audit, run 42653094685](https://github.com/fabianleonaressi95/theorem/actions/runs/42653094685).  
**Dataset:** Sodomka, *Magnetic hysteresis dataset of magnetic powders*, Zenodo [10.5281/zenodo.17053338](https://zenodo.org/records/17053338), version 1. The landing page lists `Hysteresis_datasets.xlsx` and MD5 `f2284f438b4d54282ae893dec4697a29`; the Rights/License field is blank. The workbook is not redistributed in this repository.

## Scope

The original audit detected one complete max-to-max loop in each of seven material sheets. The existing Jiles–Atherton fits are therefore **single-loop in-sample calibrations**, not held-out validation.

This supplementary diagnostic evaluates the local residual Jacobian at each archived optimizer solution. Parameters are dimensionlessly scaled, central finite differences are used, and the singular spectrum, numerical rank, condition number, and proximity to the original optimizer bounds are reported. The diagnostic does not refit parameters and does not establish global identifiability, confidence intervals, or physical validity.

## Results

| Material | Local rank | Scaled Jacobian condition number | Parameters within 1% of optimizer bound |
|---|---:|---:|---|
| CIPSQ | 5/5 | 8.39×10³ | α lower; c upper |
| CIPHS | 5/5 | 7.08×10³ | α lower; k lower |
| Fe85Si15 | 5/5 | 9.44×10³ | α lower |
| NdFeB | 5/5 | 1.21×10⁴ | α upper; c lower |
| SF-D360 | 5/5 | 1.07×10⁴ | α upper; c lower |
| Fe3O4 | 5/5 | 8.68×10³ | a lower; α lower |
| Fe2O3 | 5/5 | 4.91×10⁴ | α upper; c upper; k upper |

All seven numerical Jacobians have full rank at the selected finite-difference tolerance, but **all seven fits place α at or extremely close to an imposed bound**. Several fits also place c, k, or a at a bound. Condition numbers range from approximately 7.1×10³ to 4.9×10⁴. These are warnings of poor practical conditioning and optimizer-bound dependence. Full local numerical rank does not make fitted parameters uniquely or physically identified.

## Timing metadata

Extracted max-to-max segment durations range from approximately 25.9 to 78.4 s. Their inverse durations range from approximately 0.0128 to 0.0386 Hz. Median sample intervals are approximately 0.0200 s, with within-segment coefficients of variation around 2.9–4.2%. These are descriptive quantities derived from the workbook's `t [s]` column. The inverse duration is **not** promoted to a source-documented excitation frequency. The Zenodo landing page does not specify the measurement frequency, waveform protocol, specimen geometry, conductivity, or density convention.

## Consequences

1. Retain all seven JA results as `IN_SAMPLE_CALIBRATION_ONLY`.
2. Do not compare their in-sample NRMSE values as predictive rankings across materials.
3. Do not interpret fitted α, c, or k as material constants while estimates are pinned to optimizer bounds and local conditioning is poor.
4. Independent repeated loops/specimens, a documented magnetic history/initial-state protocol, and physically justified parameter constraints are needed before held-out validation and physical parameter interpretation.
5. Bertotti/dynamic-loss fitting remains out of scope until frequency, waveform, geometry/thickness, conductivity, and density are independently documented.

## Reproduction

Run:

```bash
python scripts/audit_ja_local_identifiability.py \
  hysteresis_audit/hysteresis_analysis_report.json \
  hysteresis_audit/reconstructed_BH_loops.csv \
  --out results/ja_local_identifiability.json
pytest -q tests/test_ja_local_identifiability.py
```

The input is the existing Actions artifact `hysteresis-audit` from run `42653094685`. It is not committed because the Zenodo record does not state a redistribution licence.
