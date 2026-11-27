# Repository reorganization audit — 2026-11-26

Branch: `chore/theorem-register-restructure`. Scope: full-repository inventory, folder reorganization, theorem master register, README update, lightweight consistency check. No scientific result was modified; no card content was rewritten.

## 1. Preliminary audit findings

- `theorems/` contained **268 markdown files** before reorganization (266 at top level + 2 under `theorems/spectral/`), of which **4 SE(3) specification documents** (`T-BIANCHI.md`, `T-DEC-SE3.md`, `T-DEWIT.md`, `T-H2-DISLOC.md`) were misplaced at repository root and have been moved in → **272 cards** now.
- The premise "268 schede Txxx" is inaccurate: cards use heterogeneous prefixes (`T###`, `S###`, `C60_*`, `EQC-*`, `TSMR-*`, `MQM*`, named slugs). The register covers **all** files, not only `T\d+` names.
- **29 card-id prefixes are reused** by multiple files (T113×9, T049×6, T143×4, T071/T099/T156×3, and others). These are distinct documents sharing a numbering prefix — an author-level numbering decision, not fixed unilaterally (renumbering would break cross-references across docs, PRs and the dependency graph).
- Root contained **118 files**: 57 unreferenced, 40 referenced. Duplicates found by content hash (11 groups), including byte-identical `" (N)"` copies and — notably — several `two_time_kernel_*.npz` files with **different names but identical content** (possible historical mislabeling; preserved under `artifacts/`, flagged for author review, not deleted).
- The legacy `dec_se3` package (`se3.py`, `bianchi.py`, `connection.py`, `holonomy.py`, `covariant_derivative.py`, `mesh.py`, `__init__.py`) used relative imports and was importable only as a broken top-level package; its root `test_*.py` files imported the non-existent `dec_se3.*` namespace and were not collected by pytest (`testpaths=["tests"]`). Archived intact.
- **Pre-existing breakage found and fixed:** five `scripts/` drivers (`certify_c60_dpo_cap_rank.py`, `prove_c60_dpo_vertex_immersed.py`, `c60_dpo_energy.py`, `certify_c60_dpo_bernstein.py`, `certify_c60_dpo_immersed.py`) executed a non-existent `build_truncated_icosahedron_transports.py`; repointed to the existing `c60_truncated_icosahedron_transports.py` (same `# ---------- 7. Verifiche` split contract). Two archived root copies of these drivers were already broken the same way and remain archived as orphans.
- Count divergences: README/unified-graph documents cite 248 and 263 "theorem records"; the register now reports **272 cards**. The dependency-graph edge set predates this count (not regenerated here — flagged).

## 2. Files moved / deleted / archived

| Action | Items | Destination |
|---|---|---|
| Deleted | 20 `*.pyc`, 1 `__pycache__/` tree | — (regenerable; already gitignored patterns) |
| Deleted | byte-identical duplicates: `conftest (1).py`, `se3 (1).py`, `bianchi (1).py`, `connection (1).py`, `README (8).md`, `q6-d5-integer-fiber.yml` (identical to workflow copy), 3 `two_time_kernel_* (1).npz` | — |
| Moved → `theorems/` | `T-BIANCHI.md`, `T-DEC-SE3.md`, `T-DEWIT.md`, `T-H2-DISLOC.md` | theorem spec cards |
| Moved → `artifacts/` | 12 `*.npy` (K0, K0_inv, P_G, Z_A, Z_S, D_bfs, D_dfs, faces, face_bases, face_normals, vertices, vertex_holonomy_deg), 11 `*.npz` (two_time_kernel×10, truncated_icosahedron), `report.md/.json`, 4 `c60_*_2026-11-21.json`, `truncated_icosahedron_transports_2026-11-21.json`, `C60_TRANSPORTS_GH_CROSSAUDIT_2026-11-21.json` | generated data/results |
| Moved → `audits/` | 10 `K0_*REPORT/CERTIFICATION/GEOMETRY_AUDIT/SU2_ALGEBRA.json` | audit reports |
| Moved → `archive/` | 6 `*.zip` bundles, `GAP_sessione_2A5_McKay_2I.html`, `data (1).csv` → `archive/data_1_stray.csv` | historical material |
| Moved → `archive/dec_se3_legacy/` | `se3.py`, `bianchi.py`, `connection.py`, `holonomy.py`, `covariant_derivative.py`, `mesh.py`, `__init__.py`, 8 root `test_*.py` (+ `" (N)"` variants), `README (6).md`, `README (7).md` | broken legacy package |
| Moved → `archive/orphan_scripts_2026-11-26/` | `optimize_c60_g_tradeoff.py`, `prove_dpo_vertex_immersed.py` (depend on missing `build_truncated_icosahedron_transports.py`) | orphan drivers |
| Moved → `docs/` | `MORANDOTTI_ANISOTROPY.md`, `TRUNCATED_ICOSAEDRON_TRANSPORTS_2026-11-21.md`, `C60_TRANSPORTS_GH_CROSSAUDIT_2026-11-21.md`, `note_al_relatorio.md` | documentation |
| Moved → `data/` | `Hysteresis_datasets.xlsx` (Zenodo MD5 `f2284f…` per `docs/INDUSTRIAL_HYSTERESIS_DATASETS.md`) | dataset |
| Moved → `bibliography/` | `2412.0104v1.pdf`, `jbCurve (1).pdf` | source literature |
| Created | `conjectures/README.md`, `proofs/README.md` | reserved structure dirs |

Nothing scientific was deleted: every non-identical file is preserved under `archive/` or its proper category directory.

## 3. Reference updates

- `.github/workflows/k0-binary-audit.yml` — path triggers and inline Python updated (`artifacts/`, `audits/`, `archive/`).
- `.github/workflows/hysteresis-audit.yml` — dataset path → `data/Hysteresis_datasets.xlsx`.
- `.github/workflows/q6-vesica-rgs-audit.yml`, `t145-square-biverse-rgs.yml` — trigger paths → `artifacts/*.npy`.
- `scripts/` + `audits/` — 12 files updated to load arrays from `artifacts/`; `audit_hysteresis_dataset.py` default → `data/…xlsx`.
- `audits/K0_SU2_LADDER_GEOMETRIC_COMPATIBILITY_PROTOCOL_2026-11-24.md` — path table and prose updated.
- `README.md` — new status section, accurate directory tree, register links, fixed `MORANDOTTI_ANISOTROPY.md` link.
- `docs/project/{REPOSITORY_MAP,OPEN_WORKSTREAMS,SCIENTIFIC_STATUS_MATRIX}.md` — hygiene section marked resolved; legacy paths pointed to `archive/dec_se3_legacy/`.

## 4. Theorem master register

- `docs/THEOREM_MASTER_REGISTER.csv` — 272 rows × 18 columns (16 required + `file`, `status_note`).
- `docs/THEOREM_MASTER_REGISTER.md` — human-readable index + status distribution.
- `scripts/build_theorem_register.py` — deterministic regenerator (heuristic epistemic classification; `status_note` records the rule that fired).
- `scripts/check_theorem_register.py` — consistency check: card↔row coverage, taxonomy, referenced path existence, dependency resolution, duplicate-id report. **Result: 0 errors, 61 warnings** (mostly cards referencing test files that do not exist — genuine documentation gaps; and the 29 duplicate-id groups).

### Status distribution (machine-assisted, conservative)

| Status | Count |
|---|---:|
| PROVED | 44 |
| EXACT_CERTIFICATE | 14 |
| NUMERICALLY_VERIFIED | 80 |
| CONDITIONAL | 83 |
| CANDIDATE | 6 |
| HYPOTHESIS | 2 |
| OPEN | 43 |
| SUPERSEDED / QUARANTINED | 0 |

~100 rows carry a low-confidence `status_note` (heuristic fallback) and are listed for author review — classification was **not** manually verified card-by-card; PROVED was assigned only on explicit proof language without open qualifiers.

## 5. Test report

- Baseline (main, before reorganization): CI green; local `pytest tests/` could not run cleanly before dependency install (`sympy` missing locally — environment issue, unrelated to reorganization).
- After reorganization: `python3 -m pytest tests/ -q` — see PR body for final counts; `python3 scripts/check_theorem_register.py` → **0 errors**.
- Moved files were not imported by `tests/` or active workflows (verified by reference scan); the only code-path changes are the `artifacts/` prefixes above and the 5 `build_truncated` repoints.

## 6. Cards not classifiable with certainty

All rows whose `status_note` begins with `no status evidence found` or `audit/benchmark card (heuristic)` — approximately 100 rows — defaulted to `OPEN`/`NUMERICALLY_VERIFIED` conservatively and require author review. They are identifiable in the CSV via the `status_note` column.

## 7. Questions requiring author decision

1. **Card-id renumbering:** 29 duplicated prefixes (T113×9 etc.) — keep file-path keys or assign canonical T-numbers?
2. **Dependency graph regeneration:** `docs/UNIFIED_THEOREM_*` counts (248/263) predate the 272-card register.
3. **`two_time_kernel_*.npz` identical-content groups:** several distinct filenames share one MD5 — confirm whether they are intentional aliases or mislabeled exports.
4. **dec_se3 legacy package:** archive vs. restore as `src/dec_se3/` if still needed (currently unreferenced by tests).
5. **Orphan C60 drivers:** `build_truncated_icosahedron_transports.py` is referenced by name in docs as "pipeline GH, non in repo" — confirm whether the canonical producer should be committed.
6. **Status upgrades:** ~100 heuristic classifications need author sign-off before external citation.
