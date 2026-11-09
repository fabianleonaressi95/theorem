# Industrial hysteresis: public experimental datasets and validation protocol

Status: **dataset candidates identified; no experimental fit or validation claim is made yet**.

This registry separates (i) measured actuator data, (ii) measured magnetic material data, and (iii) synthetic model checks. Raw data are not copied into the repository until the file schema, licence, attribution and preprocessing are checked.

## Priority A — actuator experiments

### Soft pneumatic actuators (Zenodo)

- Record: https://doi.org/10.5281/zenodo.15584329
- Landing page: https://zenodo.org/records/15584329
- Dataset file: `data.csv` (10.4 MB; MD5 listed by Zenodo: `654c05be81fa60391e4b481787c320d3`)
- Licence: CC BY 4.0.
- Description: dataset accompanying an experimental review of hysteresis models for soft pneumatic actuators.
- Intended use: identify input/output channels, group experiments by actuator and loading protocol, reconstruct pressure–displacement and, where present, force loops. Compare Preisach, Prandtl–Ishlinskii and Bouc–Wen only on identical train/test splits.
- Gate before fitting: inspect CSV header, units, missing values, sample ordering, cycle boundaries and whether repeated trials are independent. Do not treat review-derived or simulated columns as measurements without checking the data dictionary.

## Priority B — piezoelectric actuator benchmark

### Piezoelectric micromanipulator dataset (Data in Brief, 2020)

- Article / data description: https://doi.org/10.1016/j.dib.2020.105175
- Open article: https://pmc.ncbi.nlm.nih.gov/articles/PMC6997478/
- Licence of article: CC BY 4.0; confirm the supplementary-data terms before redistributing the archive.
- Two input/output experiments are described: 150 V, 1 Hz and 5 V, 300 Hz. The CSV files contain time, displacement and voltage; the 150 V / 1 Hz record has 50,001 samples and the 5 V / 300 Hz record has 200,001 samples. The article notes drift in the high-rate record and an initial transient in the other record.
- Intended use: rate/amplitude generalization test for PI/Preisach/Bouc–Wen and dynamic residual analysis. Preserve the authors' stated preprocessing and compare both raw and corrected data.

### Piezoelectric actuator Preisach identification dataset (Mendeley Data)

- Record: https://doi.org/10.17632/kzf668wggx.9
- Landing page: https://data.mendeley.com/datasets/kzf668wggx/9
- Description: measured voltage/displacement experiments over 0–5 V, including sinusoidal and triangular excitation files and identified Preisach density data.
- Licence shown by the repository: CC BY-NC 3.0. This is suitable for research comparison subject to attribution and non-commercial restrictions; it is not automatically suitable for commercial product training or redistribution.
- Intended use: independent Preisach baseline and frequency/amplitude comparisons.

## Magnetic material datasets for Jiles–Atherton

### INRIM first magnetization curves

- Record: https://zenodo.org/records/10725890
- Dataset describes measured H, B and J curves for multiple ferromagnetic materials.
- Intended use: first-magnetization / anhysteretic-curve checks and material-unit consistency. It is not, by itself, a closed-loop validation set for hysteresis loss.

### EMPIR HEFMAG NO/GO steel-sheet loops

- Record: https://doi.org/10.5281/zenodo.5910893
- Landing page: https://zenodo.org/records/5910893
- File: `EMPIR 19ENG06 HEFMAG dataset loops NO and GO.zip` (318.9 kB; Zenodo MD5 `2ae32cfbcf0841e4a320d0adaf4e6355`).
- Description: sample measured hysteresis loops for non-oriented and grain-oriented FeSi steel, used in power-loss work.
- Rights: Zenodo's record leaves the Rights/License field blank. Do not redistribute or commit the archive until the rights are clarified with the depositor; access for analysis is distinct from redistribution permission.
- Intended use: fit and test Jiles–Atherton loop shape and energy-loss metrics after inspecting the archive's units, waveform, frequency, sample metadata and loop segmentation.
- The HEFMAG project site separately lists the main Hysteresis Loops Dataset as DOI `10.5281/zenodo.5910892`; it should be evaluated as a separate source, not conflated with this 5910893 sample archive.

### Magnetic powders / magnetorheological elastomers

- Record: https://doi.org/10.5281/zenodo.17053338
- Landing page: https://zenodo.org/records/17053338
- File: `Hysteresis_datasets.xlsx` (721.3 kB; Zenodo MD5 `f2284f438b4d54282ae893dec4697a29`).
- Description: measured JH/BH hysteresis data for 50 wt% magnetorheological elastomers filled with carbonyl iron (SQ/HS), Fe85Si15, NdFeB, strontium ferrite, Fe3O4 or Fe2O3.
- Rights: Zenodo's record leaves the Rights/License field blank. A third-party catalog reports CC BY 4.0, but that is not treated here as a substitute for the depositor's licence metadata. Clarify rights before redistribution.
- Intended use: exploratory material comparison; inspect worksheet schema, units, sample geometry and measurement conditions before fitting.

## Required validation protocol

1. **Data audit:** preserve source files; record DOI, version, checksum, licence, units, sampling rate, channels, missing values and preprocessing.
2. **Cycle segmentation:** identify full and minor loops from measured input reversals; do not close open trajectories artificially for fitting.
3. **Leakage prevention:** split by complete cycle / trial / specimen, never random individual samples across the same loop.
4. **Baselines:** PI, Preisach and Bouc–Wen for actuator displacement/force; Jiles–Atherton for magnetic M(H) or B(H) loops. Do not compare models across incompatible physical output variables.
5. **Metrics:** held-out RMSE/normalized RMSE, loop-area error, branch-separation error, reversal-point error and rate dependence where the protocol supports it.
6. **Uncertainty:** report parameter identifiability, sensitivity to initialization, confidence intervals across independent trials and convergence under time-step / discretization refinement.
7. **Industrial relevance:** report cycle energy loss, repeatability, drift, temperature/rate dependence and control implications. A successful synthetic test is not experimental validation; a good fit to one public dataset is not industrial qualification.

## Current implementation boundary

The repository contains synthetic/reference implementations of Preisach, Prandtl–Ishlinskii and Bouc–Wen. The Jiles–Atherton scalar quasi-static model is being added with unit-consistent parameters. No model has yet been fitted to the datasets above in this repository. No industrial performance, cost reduction or actuator lifetime claim is made.
