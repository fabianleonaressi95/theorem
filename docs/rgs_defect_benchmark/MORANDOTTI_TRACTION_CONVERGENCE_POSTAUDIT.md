# Morandotti traction-jump convergence post-audit

**Status:** post-processing implementation and regression tests added; numerical conclusions below are descriptive for the archived five-level artifact.

## Why this audit

The five-level C0-IPDG run established algebraic Frank/Burgers additivity to roundoff, while the interior-facet traction-jump norms continued to decrease. The next question is whether the observed sequence supports a stable empirical scaling and whether the second-moment tensors stabilize at the same rate. These are separate questions: source quadratic energies are not the same observable as facet traction-jump norms.

## Reproduction

Extract the artifact from the five-level workflow, then run:

```bash
python3 scripts/morandotti_loglog_convergence_audit.py \
  --input artifacts/morandotti_traction_refinement/report.json \
  --out artifacts/morandotti_traction_refinement/convergence_audit.json
```

The script reports, for every reconstruction case:

- local adjacent-mesh log-log exponents for total, Frank and Burgers jump norms;
- ordinary least-squares log-log fits over all levels and over the finest three levels;
- adjacent-level relative Frobenius changes of total, Frank, Burgers and mixed second-moment tensors;
- absolute and scale-normalized residuals for both source-energy and facet-jump squared decompositions.

The fits are descriptive only. No confidence intervals are attached to a deterministic five-mesh sequence, and the fitted exponent is not promoted to an a priori FEM convergence order.

## Mixed disclination–dislocation case: observed values

| (h) | Total jump (L^2) | Frank jump (L^2) | Burgers jump (L^2) |
|---:|---:|---:|---:|
| 0.080 | 9.92050e-3 | 7.44476e-3 | 3.99027e-3 |
| 0.060 | 4.84400e-3 | 3.19501e-3 | 2.83490e-3 |
| 0.045 | 3.68644e-3 | 2.45707e-3 | 2.28552e-3 |
| 0.035 | 2.99162e-3 | 1.98428e-3 | 1.83678e-3 |
| 0.027 | 2.37536e-3 | 1.53709e-3 | 1.49122e-3 |

The adjacent-mesh empirical exponents (coarse-to-fine) are:

| Transition | Total | Frank | Burgers |
|---|---:|---:|---:|
| 0.080 → 0.060 | 2.492 | 2.940 | 1.188 |
| 0.060 → 0.045 | 0.949 | 0.913 | 0.749 |
| 0.045 → 0.035 | 0.831 | 0.850 | 0.870 |
| 0.035 → 0.027 | 0.889 | 0.984 | 0.803 |

The coarsest interval is not representative of the final three intervals. On the finest three intervals the observed exponents are near, but not equal to, one. This is not sufficient to assert first-order convergence: the mesh sequence is short, the mesh generator changes topology, and no independent remeshing ensemble is included in this fit.

The total, Frank and Burgers jump norms all decrease at the finest level. Thus the current data do **not** support a nonzero limiting facet-jump norm. A vanishing limit remains plausible, but must be checked with further refinement and independent mesh realizations.

## Algebraic checks

For the mixed-source case at (h=0.027):

- source quadratic decomposition: Frank (2.33582318\times10^{-4}), Burgers (1.09128321\times10^{-4}), signed cross term (1.35936402\times10^{-4}), total (4.78647040\times10^{-4});
- facet-jump squared decomposition: Frank (2.36264641\times10^{-6}), Burgers (2.22375158\times10^{-6}), signed cross term (1.05593878\times10^{-6}), total (5.64233677\times10^{-6});
- additivity residuals: approximately (10^{-20}) for the source decomposition and (5.3\times10^{-18}) for the facet-jump decomposition.

The source quadratic decomposition and facet-jump decomposition must not be conflated. The former concerns the reconstructed source quadratic form; the latter concerns the interior-facet traction jump.

## Classification

- **Proved algebraically:** the finite-dimensional tensor and squared-norm expansion under linear reconstruction and a common jump convention (T091).
- **Numerically verified:** additivity residuals at the five reported mesh levels.
- **Observed, not proved:** decreasing jump norms and finest-interval empirical exponents around 0.8–1.0 for the mixed case.
- **Open:** asymptotic convergence order; continuum trace/jump limit; robustness under independent remeshing, core-radius refinement and separation refinement; physical force-balance interpretation.

## Guardrails

A small algebraic residual verifies the bookkeeping identity, not convergence. A decreasing jump norm does not establish a nonzero limiting jump. A high (R^2) in log space does not establish an asymptotic law. The report's own limitations on the two-core geometry and static Airy reconstruction continue to apply.

**FLN**
