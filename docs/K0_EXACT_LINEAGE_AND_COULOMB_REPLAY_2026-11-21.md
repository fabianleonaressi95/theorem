# Exact K0 lineage comparison and producer audit

Date: 2026-11-21

## 1. Exact identity: passed

The following three archived matrices were loaded and compared directly:

- `RGS_PSU_all_matrices.npz::K0`;
- `A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip` → nested `RGS_PSU_all_matrices.npz::K0`;
- `A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip` → nested `psu_fibre_connection_matrices.npz::K0`;
- `188D_FINAL_BUNDLE.zip::K0.npy`.

All four arrays have shape 188×188, dtype float64, and are **exactly elementwise identical**. For each comparison:

- Frobenius difference = 0;
- maximum absolute difference = 0;
- exact array equality = true.

SHA-256 of the canonical K0's contiguous float64 data bytes:

`d7e70c87d1f068af9399be231f95f5f7b09e70ba1d444df52bc70c19011bb614`

The tangent bases also match exactly:

- canonical `Q_tangent` = A13 `Q_tangent`;
- canonical `Q_tangent` = fibre archive `Q`.

Both comparisons have zero Frobenius and maximum absolute difference. The tangent projector difference is consequently exactly zero. Thus the K0 identity is not merely spectral or up to a basis rotation: the matrix and its 192×188 frame are shared exactly across these archives.

Canonical Q array SHA-256 (contiguous float64 data bytes):

`829f9fa5be27fb93db91252f60381e1af6803e6629fa5a586b023b851088e6a2`

## 2. Spectral fingerprint

The canonical K0 is exactly symmetric at stored precision. Its eigenspectrum has:

- 64 numerical zero modes;
- 124 positive modes;
- positive ladder 0.5, 0.6, …, 12.8;
- maximum deviation of adjacent positive eigenvalue gaps from 0.1: approximately 3.98×10⁻¹⁴.

This is a reproducible property of the archived matrix. It is not, by itself, evidence of a physical derivation.

## 3. Distinguish K0 from the Coulomb constrained Hessian

The recovered `188D_FORENSIC_REPLAY.py` and embedded notebook source in `formule.pdf` define a different operator:

[
K_{\mathrm{Coulomb}}=Q^T(H_{\mathrm{Coulomb}}+\lambda I_{192})Q,
]

where (H_{\mathrm{Coulomb}}) is the Hessian of (sum_{i<j}1/\|X_i-X_j\|), and (lambda) is the radial Lagrange multiplier. Using the exact same archived (X) and exact same (Q), this replay gives:

- 29 negative modes;
- 3 near-zero modes;
- 156 positive modes;
- minimum eigenvalue approximately −2.776862326;
- maximum eigenvalue approximately 15.575302443.

The archived K0 instead has 64 zero and 124 positive modes, with spectrum 0.5–12.8 on its positive subspace. The matrices differ substantially (Frobenius difference approximately 79.56974154; maximum entrywise difference approximately 3.13635739). Therefore the documented Coulomb Hessian replay is **not** the producer of the archived K0. It is a distinct 188D operator, consistent with the separate indefinite-Hessian record.

## 4. What the notebook actually says about K0

The extracted notebook dump has two other K0-related code paths:

1. A T2u illustrative cell explicitly labels its matrix a synthetic kernel and constructs it as (R^TR+0.1I), then tunes a 3×3 block. This is positive definite and is not the archived rank-124 K0.
2. A separate audit's `load_or_create_data()` attempts to load `K0_kernel_188.npy`; only if that file is missing does it call `generate_mock_kernel_188d()`. The mock uses an internal dimension 185, a (+2I) Gram shift, repeated 37×37 diagonal blocks, and a rank-94 illustrative spectral projector. This fallback is incompatible with the archived K0's 64-dimensional kernel and 0.5–12.8 positive ladder.

The PDF's checkpoint manifest lists an already-existing `188D_CHECKPOINT/AUTO_DUMP/K0.npy` (188×188 float64), but the manifest is an inventory of a saved array, not its producer. The notebook's load-or-create branch confirms that at least one path treated K0 as an external input. The exact contents and provenance of the original `K0_kernel_188.npy` input, or the first cell that created it, are not present in the recovered trace.

## 5. Provenance verdict

**Resolved:** the canonical K0 is the exact same matrix in the A13 and 188D archives, and all these copies use the exact same Q frame.

**Ruled out:** the recovered constrained Coulomb Hessian replay; the T2u random-SPD illustrative kernel; and the 185D/37-block mock fallback.

**Still open:** the original producer of the archived PSD K0, including its mathematical definition, source input, and whether it is a physically derived operator. No evidence recovered so far establishes (K_0=Q^THQ) for the Coulomb Hessian or for any other specified physical action.

## 6. Reproduction

Run:

```bash
python scripts/reproduce_k0_lineage_audit.py \
  --canonical-npz data/RGS_PSU_all_matrices.npz \
  --a13-zip A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip \
  --188d-zip 188D_FINAL_BUNDLE.zip \
  --out audits/K0_lineage_exact_comparison.json
```

The script compares the arrays and independently replays the documented Coulomb constrained Hessian. It never substitutes a mock or regenerates K0.

## Classification

| Claim | Status |
|---|---|
| Identity of archived K0 copies | Exact numerical identity verified |
| Identity of archived Q frames | Exact numerical identity verified |
| K0 spectral fingerprint | Numerically verified |
| Coulomb constrained Hessian = K0 | Ruled out |
| Notebook mock fallback = K0 | Ruled out |
| Exact original K0 producer | Not recovered |
| Physical Hessian interpretation of K0 | Not established |

Disposition: retain K0 as a shared archived PSD spectral operator with a verified common coordinate frame, but unresolved producer and physical interpretation.
