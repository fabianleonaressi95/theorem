# Geometric and antipodal tests for magnetic hysteresis — RGS/Anti-Twin research bridge

**Status:** exploratory numerical diagnostic and falsifiable research proposal; not a theorem and not evidence for a new magnetic mechanism.  
**Data:** the seven measured J-H loops exported by audit run [42653094685](https://github.com/fabianleonaressi95/theorem/actions/runs/42653094685), Zenodo [10.5281/zenodo.17053338](https://zenodo.org/records/17053338).

## 1. What the current workbook can and cannot test

The workbook supplies scalar H, J, B and t traces for seven filler families, with one extracted complete loop per material. It does not document field-orientation sweeps, repeated specimens/loops, conductivity, specimen geometry/thickness, or an independently stated excitation frequency. Consequently:

- scalar loop geometry and branch asymmetry can be measured;
- an anisotropy tensor cannot be identified from these seven single-orientation loops;
- no orientation-dependent RGS constitutive law can be validated;
- no dynamic eddy-current/excess-loss model can be identified;
- no map from the measured variables to PSU units or Q6 states is currently derived.

## 2. Geometric observables

Represent each measured loop as a path \\(\gamma(t)=(H(t),J(t))\\). Candidate observables include the loop area, branch separation, and curvature with respect to arc length. For example, on a common field interval:

\\[
S(H)=J_{\uparrow}(H)-J_{\downarrow}(H).
\\]

These are coordinate-level descriptors. They become physically interpretable only after the field and polarization units, offsets, and measurement protocol are controlled.

## 3. Candidate Anti-Twin involution

Define the central inversion on loop state and branch by

\\[
\tau(H,J,\mathrm{branch})=(-H,-J,\mathrm{opposite\ branch}).
\\]

A centrally symmetric major loop would satisfy

\\[
J_{\downarrow}(H)+J_{\uparrow}(-H)=0
\\]

over the common symmetric field interval. The implemented diagnostic reports the RMS defect and normalizes it by the measured J peak-to-peak range. Minor field reversals are handled by sorting each branch by H and averaging duplicate H values before interpolation; this is a branch-envelope comparison, not a reconstruction of minor-loop dynamics.

### Observed descriptive defects

| Material | RMS defect (mT) | Normalized defect |
|---|---:|---:|
| CIPSQ | 1.704 | 0.345% |
| CIPHS | 3.601 | 0.711% |
| Fe85Si15 | 10.715 | 3.927% |
| NdFeB | 28.328 | 9.555% |
| SF-D360 | 6.488 | 4.190% |
| Fe3O4 | 2.672 | 1.477% |
| Fe2O3 | 5.973 | 67.643% |

Fe2O3 has only 8.83 mT peak-to-peak J in this workbook, so its normalized defect is amplified by the small signal; the absolute residual must be considered. These numbers are descriptive, not statistical evidence of symmetry or symmetry breaking: there is only one loop per material and no repeated-loop/instrument uncertainty estimate.

### Falsifiable test

Acquire repeated full loops for the same specimen, at matched temperature and field protocol, with independently calibrated H/J offsets. Estimate the repeatability distribution of the antipodal defect. Then test the null hypothesis that the measured defect is consistent with that uncertainty. A proposed Anti-Twin symmetry prediction is supported only if its quantitative tolerance is specified before examining the repeated data and survives held-out specimens. The current workbook alone cannot pass this test.

## 4. Anisotropy hypothesis

A future orientation-resolved experiment could measure loop observables at field angle \\(\theta\\) and test, as a first low-order model,

\\[
A(\theta)=A_0+A_2\cos 2(\theta-\theta_0)+\varepsilon(\theta),
\\]

where \\(A\\) may be loop area or another pre-registered geometric observable. Compare a scalar JA model against a tensorial/orientation-dependent extension, training on some orientations and predicting held-out angles and specimens. The anisotropy claim is falsified if the tensorial model does not improve held-out prediction beyond measurement uncertainty and model-complexity penalties.

## 5. Q6 / PRISM / PSU admissibility conditions

No six-bit encoding or cubical weighting is introduced here. A Q6 connection would require a physically derived state map that:
1. maps measured reversal/branch states to discrete states without arbitrary thresholds fitted to the desired result;
2. preserves the experimentally observed transition relation;
3. is equivariant under the proposed antipodal involution;
4. predicts held-out transitions or loop features better than scalar JA and simpler discrete controls.

Likewise, a PSU normalization requires an independently derived dimensional map from measured field, polarization and energy scales. A Planck-scale conversion cannot be inserted as a fitted scale factor.

## 6. Relation to S011

This is a material-response benchmark only. JA parameters remain constitutive fit parameters; they are not identified with \\(g_{T\alpha}\\), \\(m_T\\), or \\(\lambda_{BF}\\). No torsion propagation, aether effect, or FDT-Maxwell coupling follows from these loop measurements.

## Reproduction

```bash
python scripts/audit_hysteresis_antipodal_symmetry.py \
  hysteresis_audit/reconstructed_BH_loops.csv \
  --out results/antipodal_symmetry_2026-11-26.json
pytest -q tests/test_hysteresis_antipodal_symmetry.py
```

The raw workbook and curve-point CSV are not committed: Zenodo's Rights/License field is blank.
