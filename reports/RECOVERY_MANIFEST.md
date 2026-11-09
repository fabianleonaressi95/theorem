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

The original `X_Oh_reconstructed.npy` (64x3) is referenced by source and historical logs, but is not present in the recovered binary bundle or the currently materialized Library files. The PDFs contain code and references to the saved coordinate file, not the coordinate array itself. No coordinates have been fabricated.

## Krist-All

The recovered archive `PRISM_KristAll_recovered_sources.zip` includes a 64-state/69,120-state manuscript source and bibliography, figure source files, a recovered supplementary Python-notes artifact with a distinct cube–octahedron 14-site model and historical diagnostics, and supplementary PDFs.

The recovered material does not include a deterministic enumerator, full canonical representative table, or formal equivalence relation for the reported 11,725 Krist-All classes. Nor does it provide a complete independent derivation of the reported `W0` residual and `K^3=K^2+I`. These remain unverified. The 14-site cube–octahedron notes are a separate finite model and must not be conflated with the 11,725-class PRISM/Krist-All enumeration.
