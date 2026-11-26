# K0 source trace — 2026-11-21

## Question

Recover the exact source cell or script that generated the archived (188\times188) matrix (K_0), and certify the coordinate basis in which it acts.

## Result

**Exact generating cell: NOT RECOVERED.** The search has narrowed the provenance and ruled out one tempting synthetic generator, but the archived matrix remains a loaded binary input rather than a source-reconstructed physical Hessian.

## Evidence recovered

1. The source repository `fabianleonaressi95/rgs-qlg-quaternion-bridge` tracks:
   - `data/rgs_188d/K0.npy` (188×188 binary array; Git blob SHA `235813e428c48718b9f4b55b98afe047160c007e`, 282,880 bytes);
   - `archive/bundles/188D_FINAL_BUNDLE.zip` (Git blob SHA `7823fa102a13c09aef4c95430b57902077c62de9`);
   - `archive/bundles/A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip` (Git blob SHA `4ec53f8d4df933ca50517287e2e205c25b2bd98e`).
   These are Git blob identities, **not** SHA-256 hashes of the underlying file bytes.

2. The recovered A13 consumer `A13_RGS_PSU_QLG_TWINE_ANTITWIN.py` loads `Q` and `K0` from the same `psu_fibre_connection_matrices.npz` member. This is evidence that this A13 operator is intended to be interpreted in its bundled tangent frame. The A13/A14 cross-check reports equality of the tangent-subspace projectors (Frobenius difference 0). It does **not yet prove** that this bundled `K0` is byte-for-byte or numerically identical to the `K0` in `RGS_PSU_all_matrices.npz`; that comparison is the remaining basis gate.

3. The `188D_FINAL_BUNDLE.zip` is treated by the recovered reconstruction code as a source of already-existing `K0.npy`, `Kinv.npy`, `P_G.npy`, `J.npy`, `J_A.npy), and `J_B.npy`. The reconstruction script loads these arrays; it does not generate the original (K_0).

4. The recovered spectral reports certify properties/reconstructions of the stored matrix:
   - 64 numerical zero modes and 124 positive modes;
   - positive ladder 0.5, 0.6, …, 12.8;
   - `P_G` agrees with the numerical kernel projector;
   - a spectral reconstruction residual is reported at approximately (8.0\times10^{-12}).
   These are validations of the archived array, not evidence for the original variational or geometric formula that produced it.

## Synthetic generator ruled out

The mock block in `formule.pdf` is **not** the generator of the archived (K_0):

- it defines an internal block of dimension 185 and forms `K_int = K_int @ K_int.T + 2 I`;
- it copies a 37×37 principal block into five diagonal positions;
- its fallback uses that mock only if `K0_kernel_188.npy` is missing;
- the associated illustrative projector selects every other eigenvector, i.e. 94 columns in dimension 188.

That code path is incompatible with the archived (K_0)'s 64-dimensional kernel, 124 positive modes, and positive spectrum beginning at 0.5. It must not be cited as the source of the current archived matrix. The PDF proves that a mock path existed, not that it produced this (K_0).

## Coordinate-basis status

- A14 establishes the geometric constraint Jacobian and a 188D tangent basis (Q).
- The A13 fibre archive contains its own (Q) alongside its (K_0); the reported A13/A14 tangent projectors agree exactly.
- The equality of the A13 bundled (K_0) and the target (RGS\_PSU\_all\_matrices.npz::K0) has not yet been directly certified. Until that comparison is performed, the target operator's basis identification remains **PARTIAL**, not complete.
- The 188D source bundle and A13 bundle are available as tracked binary artifacts in the source repository, but the exact producer cell/script and immutable SHA-256 of the extracted target matrix are not documented in the recovered trace.

## Required final gate

1. Extract `K0.npy` from the A13 fibre archive and from `188D_FINAL_BUNDLE.zip`.
2. Compare each against `RGS_PSU_all_matrices.npz::K0` by shape, dtype, exact bytes, Frobenius norm and maximum absolute difference.
3. Compare the accompanying (Q) arrays by exact equality and tangent-projector equality; if (Q) differs by a right orthogonal change of basis, recover and record that change of basis (O), then test (K_0^{(2)}=O^T K_0^{(1)}O).
4. Search the original notebook source and Kaggle execution history for the first creation/save of the exact array. A consumer/load statement is not a producer.
5. Recover the functional/action and unconstrained Hessian (H) before identifying (K_0) with (Q^THQ).

## Classification

| Object | Status |
|---|---|
| Archived (K_0) matrix and spectrum | Recovered / numerically certified |
| (P_G) as kernel spectral projector | Numerically verified |
| A13 bundled (K_0) coordinate frame | Bundled with (Q); tangent subspace cross-check reported |
| Identity of A13 (K_0) with target NPZ (K_0) | Open comparison |
| Exact producer cell/script | Not recovered |
| (K_0=Q^THQ) for a physical constrained Hessian | Not established |
| Mock kernel in `formule.pdf` as source of current (K_0) | Ruled out by dimension/rank/spectrum mismatch |

**Disposition:** retain (K_0) as an archived spectral operator with unresolved physical provenance. Do not label it a geometry-derived Hessian or use the mock notebook code as its provenance.
