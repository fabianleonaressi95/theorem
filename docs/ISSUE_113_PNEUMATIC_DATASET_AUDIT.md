# Issue #113 — pneumatic actuator dataset audit

**Status:** audit implementation added; full source-file verification remains a separate reproducibility gate.

## Primary sources

- Dataset: de la Morena Duque, Ramos de la Flor and Vázquez Fernández-Pacheco, Zenodo record [10.5281/zenodo.15584329](https://doi.org/10.5281/zenodo.15584329), version v1, file `data.csv`, MD5 `654c05be81fa60391e4b481787c320d3`, CC BY 4.0.
- Article: de la Morena, J.; Ramos, F.; Vázquez, A. S., “Hysteresis Modeling of Soft Pneumatic Actuators: An Experimental Review”, *Actuators* 2025, 14(7), 321, [10.3390/act14070321](https://doi.org/10.3390/act14070321).

## What the article actually specifies

The experimental object is a pneumatic bending actuator with a hollow CANESHA hydrogel chamber and a 3D-printed TPU Recreus Filaflex 82A reinforcement. Curvature is measured by a camera/marker pipeline: the curvature is the inverse radius of the circle fitted to the detected markers. Thus the CSV output is curvature, not force.

The input is the voltage applied to the electronic pressure regulator; the article uses a positive triangular waveform with amplitude 2 V and reports (f=0.05\,\mathrm{Hz}), i.e. a 20 s period. It says four cycles were recorded to inspect drift. The output has a nonzero rest curvature, corrected by subtracting a constant offset. The paper then normalizes both input and output to the unit interval for its model comparisons. The raw repository data must remain unchanged; any offset correction or normalization must be a separately named preprocessing transform.

The paper's model comparison is not just “PI versus Bouc–Wen”. It distinguishes:
- Preisach with a factorized density in (H_M=(\alpha+\beta)/2) and (H_C=(\alpha-\beta)/2), using Gaussian/Cauchy density choices;
- classical PI (CPI), a weighted sum of symmetric play operators;
- generalized PI (GPI), whose two odd envelope functions (\alpha_R,\alpha_L) alter the play operator and permit asymmetric loops, with an order-preservation constraint;
- Maxwell–Slip, whose operator orientation is reported to oppose the measured loop direction for this specimen;
- classical Bouc–Wen (CBW), which the authors find unable to represent the measured asymmetry;
- two asymmetric Bouc–Wen variants (ABW1 and ABW2), where ABW1 achieves a high GOF but produces a physically inconsistent crossing, while ABW2 is reported as consistent.

The paper reports in-sample GA fits, with three repeated optimization runs. Its GOF is (1-\mathrm{NRMSE}) computed over the fitted signal. Those published scores are reference results, not held-out-cycle performance and must not be used as validation targets.

## Time-axis discrepancy: do not overstate

The article reports 0.05 Hz and hence a 20 s period. The repository-side CSV audit previously reported a Time span of 0–8000 and a cycle period near 2000 *Time units*. The header is simply `Time`; it does not encode seconds. Therefore the numerical value 0.0005 Hz is valid **only if** the time unit is independently confirmed to be seconds. This audit deliberately leaves frequency unset unless run with `--time-unit s`.

The immediate task is to verify the Zenodo file byte-for-byte against the repository copy, then establish the Time unit from source metadata or the authors. A factor-of-1000 conversion (e.g. milliseconds) must not be silently applied.

## Implementation in this PR

`scripts/audit_pneumatic_actuator_csv.py`:
- verifies the expected `Input,Output,Time` schema;
- rejects non-finite samples and non-monotone time;
- records MD5/SHA-256, row count, ranges, sample-step statistics and reversal indices;
- records the article's frequency separately from any dataset-derived frequency;
- reports Hz only when the caller explicitly confirms seconds;
- applies no normalization or offset correction.

The tests cover checksums, schema rejection, monotone-time validation and the explicit time-unit gate.

## Not claimed by this PR

- No model fitting, LOCO score, uncertainty interval or predictive performance claim.
- No confirmation that the CSV in the repository is byte-identical to Zenodo.
- No interpretation of the output as force or dissipated energy.
- No industrial qualification, controller benefit or lifetime claim.

## Next gate

After byte-level provenance and time-unit resolution, implement a dataset-specific preprocessing manifest and complete-cycle segmentation. Then conduct cycle-held-out fits for Preisach, CPI, GPI and Bouc–Wen/ABW using identical folds. Report measured and predicted branch separation separately, together with RMSE, GOF, loop-area error, reversal error, parameter count and repeated-fit variability.
