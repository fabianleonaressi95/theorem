# K0 original producer recovery — 2026-11-21

## Result

**The original producer of the archived 188×188 matrix K0 has not been recovered. Do not synthesize a replacement and label it original.**

The exact matrix itself is not missing: its copies in the canonical NPZ, the A13 bundle, the fibre archive, and the 188D final bundle were already shown to be bitwise-identical as arrays (same shape, dtype, and entries). This note concerns only the missing upstream construction.

## New source-level findings

The archived notebook dump `formule.pdf` contains a later pipeline section (printed source lines 45711–45742):

1. If `K_field` exists, the pipeline sets `K = K_field` and labels the source `K_field`.
2. Otherwise, if `Kinv` exists, it symmetrizes that input, computes `K = safe_inverse(Kinv_in)`, and labels the source `Kinv`.
3. Only if neither exists, it generates a synthetic positive-definite test matrix by QR conjugation of `linspace(0.5, 5.0, 188)`.

The recorded `audit_ABC_corrected_results.json` reports `kernel_source: Kinv`. This identifies the input path used by that later audit, but **does not establish that its derived `K` equals the archived `K0`**. In particular, the archived K0 has 64 zero modes and 124 positive eigenvalues spanning approximately 0.5–12.8, so it cannot equal the positive-definite 0.5–5.0 synthetic fallback.

A separate later loader (source lines 45398–45413) tries to load `K0_kernel_188.npy`; if absent, it calls `generate_mock_kernel_188d()`. The mock generator is not the archived K0: its documented construction is a 185D Gram-based fallback with repeated 37×37 blocks, and it is spectrally incompatible with the archived 188D matrix.

The checkpoint manifest records `/kaggle/working/188D_CHECKPOINT/AUTO_DUMP/K0.npy` as a 188×188 float64 array. The notebook's source-scan report also identifies `__notebook_source__.ipynb` and `01_kernel_recovery.json` as scanned files, but the available dump does not expose the cell that first creates or assigns this checkpoint K0. A manifest entry proves that an array was checkpointed, not how it was generated.

## Rejected identifications

- Coulomb constrained Hessian (Q^T(H_E+\lambda I)Q): distinct indefinite 188D operator (29 negative, 3 quasi-zero, 156 positive).
- T2u illustrative synthetic Gram kernel: positive definite and not the archived spectrum.
- 188D mock fallback: 185D/repeated-block construction; incompatible shape/spectrum.
- Later synthetic QR fallback: positive definite with spectrum 0.5–5.0; incompatible nullity and upper spectrum.
- Later `K = inverse(Kinv)` audit input: a distinct pipeline variable unless a direct array comparison proves equality; no such equality is documented in the available notebook dump.

## What is established

- Archived K0 identity across the recovered bundles: exact.
- Archived K0 shape/dtype: (188,188), float64.
- Symmetry: exact.
- Spectrum: 64 numerical zero modes, 124 positive modes; positive spectrum on the 0.5–12.8 grid (step 0.1, within floating-point tolerance).
- The original creation cell / formula / input data: **not present in the currently recovered source dump**.
- Physical/action-based interpretation: **not established**.

## Exact next recovery target

Recover the original Kaggle working artifact or notebook cell that wrote
`/kaggle/working/188D_CHECKPOINT/AUTO_DUMP/K0.npy`, together with its upstream inputs and execution order. The source-scan output names `/kaggle/working/.virtual_documents/__notebook_source__.ipynb` and `/kaggle/working/188D_PROJECT/reports/01_kernel_recovery.json` as the most direct leads. The actual `.ipynb`, checkpoint directory, or original Kaggle session export is required.

**Classification:** archived numerical object = verified; exact producer = open; physical derivation = unproved.
