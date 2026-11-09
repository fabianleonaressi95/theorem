# Recovered RGS–PRISM audit sources — provenance and status

## 188D / Anti-Twin

Recovered Library artifacts:
- `188D_FINAL_BUNDLE.zip` (K0, Kinv, P_G, J, J_A, J_B; no X_Oh file)
- `actual_original_X_report_matrices.npz` (stored Q_tangent, K0, P_G, R_geo_tangent, Pi_AT, A_raw, polar frames and kernel extension)
- `actual_original_X_report.json`
- `reconstruction_report.json`
- `ANALYTIC_STATUS.md`
- archived notebook/code printouts `formule.pdf` and `array.pdf`

SHA-256:
- 188D_FINAL_BUNDLE.zip: `a2660035925a63e04e63ba2ccf15496fb2ef76be75dd3ad9c814977324b76aa2`
- actual_original_X_report_matrices.npz: `74b3654b472815300fbe9171fac6961effa2fcccc5a2148533a211d5ba36d0e8`
- actual_original_X_report.json: `181044d6705f4f22cba53b80f597bb5ab8b9b7601bcc90ef7ef34db61d8ad1a5`

The stored matrices permit a reproducible intrinsic 188D audit, but the NPZ does not contain the original 64x3 X_Oh coordinates or their generator. The current release therefore verifies the kernel/projector and reproduces the failure of stored R_geo_tangent to commute with P_G/K0; it does not certify a canonical geometric Anti-Twin intertwiner. The algebraic kernel extension is valid but is not independent geometric evidence.

## PRISM 69,120

The corrected incidence audit regenerates B1 and B2 from C64 □ C6 □ C6 □ C5, checks B1 B2 = 0 exactly, and writes sparse incidence arrays and JSON. Cell counts and Betti numbers are those of the product torus. The script does not compute all boundary ranks B_k, k=1,...,5.

## Krist-All recovery package

Recovered archive: `PRISM_KristAll_recovered_sources.zip` (SHA-256 `fd2ddd0e61ef52d9b7d0ba12cdc6c9ca6e149619d59caa77649a3259079939ac`). It contains a 64-state coding-layer manuscript, a 69,120-state section, a schematic Merkle pipeline, plotting scripts and recovered supplementary notes.

It does **not** contain a machine-readable enumeration of 11,725 Krist-All equivalence classes, a canonical equivalence relation/class representative table, or a reproducible derivation of the reported W0 residual and K^3=K^2+I identity. Those claims remain **unverified in this recovered source package** and are not promoted in this audit.


## Additional recovered 188D sources and corrected interpretation

Further Library sources inspected:
- `RGS_PSU_construct_geometric_intertwiner.py`
- `RGS_PSU_AntiTwin_tangent_audit.py`
- `RGS_PSU_AntiTwin_next_audit.py`
- `188D_FORENSIC_REPLAY.py`
- `formule.pdf`, `array.pdf`, `formule(1).pdf`, `array(1).pdf`
- `actual_original_X_report_matrices.npz`
- `actual_original_X_report.json`

The recovered construction script explicitly separates the original 64x3 geometry from proxy geometry and records the basis-alignment caveat for the direct commutator with K0. It computes the antipodal involution and the geometry-map equivariance identity `R_geo_tangent A = A Pi_AT`. The archived matrix NPZ reproduces this identity with Frobenius residual 1.6473e-14.

The same data do **not** show that the unprojected geometry map lies in the K0 kernel: `||P_G A-A||_F = 6.53706`, and principal-angle cosines range from 0.00265018 to 0.93108124. The projected polar extension maps into the kernel, but its K0 commutator is a consequence of its construction. Raw commutators `[R_geo_tangent,P_G]` and `[R_geo_tangent,K0]` are conditional diagnostics only, because the archive does not establish that these matrices use the same tangent-coordinate basis.

The original `X_Oh_reconstructed.npy` has now been located in the user's Library and materialized at `/mnt/data/files/X_Oh_reconstructed.npy` (Library file ID `file_000000005bcc81f4bea800dd7f5e1fe8`; 1,664 bytes). This changes the recovery status from **missing** to **recovered, pending numerical inspection**. Its shape, dtype, finite-value check, SHA-256, centroid, second moment, radial range, antipodal pairing and provenance have not yet been independently audited in the current execution. The exact geometric reconstruction script has not yet been rerun against this file. Therefore the previously archived NPZ results remain results from the archived matrix package; they must not yet be attributed to a fresh run from the recovered coordinate array. No numerical properties of the newly found file are asserted here.

## Krist-All

The recovered archive `PRISM_KristAll_recovered_sources.zip` includes a 64-state/69,120-state manuscript source and bibliography, figure source files, a recovered supplementary Python-notes artifact with a distinct cube–octahedron 14-site model and historical diagnostics, and supplementary PDFs.

The recovered material does not include a deterministic enumerator, full canonical representative table, or formal equivalence relation for the reported 11,725 Krist-All classes. Nor does it provide a complete independent derivation of the reported `W0` residual and `K^3=K^2+I`. These remain unverified. The 14-site cube–octahedron notes are a separate finite model and must not be conflated with the 11,725-class PRISM/Krist-All enumeration.


## Recovery status update — original 64-site coordinates located

On 2026-11-09, the Library search located `X_Oh_reconstructed.npy` (Library file ID `file_000000005bcc81f4bea800dd7f5e1fe8`; 1,664 bytes), and the file was materialized at `/mnt/data/files/X_Oh_reconstructed.npy`. This is a genuine recovery milestone: the original coordinate artifact is no longer classified as missing. The binary has not yet been opened or hashed, and the recovered geometric intertwiner script has not yet been rerun with it and the `K0.npy`/`P_G.npy` matrices from `188D_FINAL_BUNDLE.zip`. Consequently, shape/content checks, geometric invariants, exact antipodal matching, regenerated matrices and comparisons against `actual_original_X_report_matrices.npz` remain **pending**. The earlier numerical conclusions in this manifest remain tied to the archived NPZ only.


## Independent replay update — 2026-11-09 (supersedes the pending-coordinate paragraphs above)

The recovered original binary was opened and independently checked:
- `X_Oh_reconstructed.npy`: shape `(64,3)`, dtype `float64`, all finite; SHA-256 `4792f7003a30d07d0b48fdcef90a6dac74a4a907f2aa5cfb8d417f66aaa6519f`.
- Exact antipodal matching under nearest `-X_i`: maximum residual `0.0`; induced permutation is bijective and involutive.
- Centroid is numerically zero; centered coordinate rank is 3; second moment is `1.25 I_3` to floating-point precision; radial range is `[0.829027345109799, 2.185129251114611]`.
- Text representation committed at `data/rgs_188d/X_Oh_reconstructed.csv` (SHA-256 `e03096d6c6bb05ee0b44507eb66855fac9b5957a98e7c7eabd70771ad45ae568`).
- Archived geometry-driven intertwiner script rerun against original coordinate binary and `K0.npy`/`P_G.npy` extracted from `188D_FINAL_BUNDLE.zip` (bundle SHA-256 `a2660035925a63e04e63ba2ccf15496fb2ef76be75dd3ad9c814977324b76aa2`). Result: ambient antipodal equivariance residual 0; `R_geo A - A Pi_AT` residual `1.647294145743781e-14`; `P_G` rank 64; projected rank 64.
- Crucial negative result: the unprojected geometry-generated 64-space is **not** identified with `Im(P_G)`: `||P_G A-A||_F = 6.537062941350011`; principal-angle cosines range from `0.002650180290793834` to `0.9310812434297996`. The projected-polar extension's near-zero `K0` commutator is construction-induced, not independent geometric evidence. Direct `[K0,R_geo]` remains conditional on a common 188D tangent-coordinate basis.
- Machine-readable results: `reports/188d_recovered_geometry_audit_2026-11-09.json`.

This closes the **coordinate recovery and numerical replay** subtask, but does not close the entire 188D/Krist-All issue: binary `K0/P_G` source bundle and full recovered NPZ are still not committed in a clean-checkout reproducible form, and the 11,725-class Krist-All enumerator/equivalence relation/`K,W0` definitions remain absent. No missing data were synthesized.


## Authoritative geometry replay update — 2026-11-09

The original coordinate artifact has now been independently inspected and its geometry-only audit is committed in the repository.

- Original source: `X_Oh_reconstructed.npy`, SHA-256 `4792f7003a30d07d0b48fdcef90a6dac74a4a907f2aa5cfb8d417f66aaa6519f`.
- Reproducible text representation: `data/rgs_188d/X_Oh_reconstructed.csv`, SHA-256 `e03096d6c6bb05ee0b44507eb66855fac9b5957a98e7c7eabd70771ad45ae568`.
- Shape `(64,3)`, dtype float64, all finite, centered rank 3.
- Centroid is zero to roundoff; second moment is `1.25 I_3` to roundoff.
- Radial range: 0.8290273451–2.1851292511.
- Antipodal matching is bijective and involutive, with maximum pair residual exactly zero in the stored decimal representation.
- Geometry-only regression tests: `tests/test_188d_recovered_geometry_source.py`; recovery workflow run 42645820312 completed successfully, including these tests and the PRISM audit.

This closes the missing-coordinate and geometry-only verification subtask. It does **not** close the full 188D replay: `K0.npy`, `P_G.npy`, and the archived matrix NPZ/bundle are not yet committed as repository artifacts. The original-input replay has now been executed locally using the recovered bundle, but the generated full report and matrices still need to be committed and the run repeated from a clean checkout. The historical geometric map residual and kernel-alignment results remain tied to the archived matrix package. The distinction is binding: verified coordinate geometry is not proof that the geometry-generated 64-space equals `Im(P_G)`.

Krist-All remains separate and open: no deterministic 11,725-class enumerator, canonical representative table, or independent `K`/`W0` source has been recovered.


## Geometric intertwiner replay — local execution result, 2026-11-09

The original-input script `RGS_PSU_construct_geometric_intertwiner.py` was executed with the recovered `X_Oh_reconstructed.npy` and `188D_FINAL_BUNDLE.zip` (including the original `K0.npy` and `P_G.npy`), not with the proxy embedding.

Reported diagnostics from that execution:

- Antipodal geometric equivariance residual: \\(1.65\\times10^{-14}\\).
- Raw geometric map/kernel distance: \\(\\|P_GA-A\\|_F=6.53706\\).
- Minimum principal cosine: \\(0.00265018\\).
- Projected-polar extension commutator residual: \\(1.42\\times10^{-14}\\).

Interpretation: the geometric map is antipodally equivariant to numerical precision, but its raw image is not the 64-dimensional kernel image of \\(P_G\\). The projected-polar extension has a small commutator because it is constructed inside that image; this is not an independent proof of geometric identification. Therefore the proposed canonical geometric intertwiner is **not established** by this replay.

Artifact status: the replay output was generated in the working environment, but its full JSON report and matrix NPZ have not yet been committed. The values above are a recorded local execution result, not a clean-checkout CI certificate. To close this gate, commit the report and matrices, add regression tests against the original bundle, and rerun the workflow from a clean checkout.
