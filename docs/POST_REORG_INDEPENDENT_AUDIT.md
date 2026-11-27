# Independent audit — PR #555 post-reorganisation consistency

- **Commit examined:** `ec71084` on `chore/post-reorg-consistency` (PR #555, base `8477df3`), plus this audit commit. During the audit the branch merged `main`, which added card `MQ-T005`; register/graph/manifests were regenerated to **280 cards** and all checks re-run.
- **Date:** 2026-11-27
- **Scope:** verification only; no theorem statement, proof or numerical result modified. One mechanical doc annotation added (§6).
- **Method:** independent reconstruction of invariants from primary sources (filesystem, JSON/CSV/MD artifacts, git history) — generator internals were not reused for the graph/register checks.
- **Integration note (2026-11-27):** this document and its test file are ported to `main` unchanged in substance; the regenerated register/graph/manifest artifacts were **not** re-applied because `main` already carries the 280-card sync via #555 plus the MQ-T005 `H-RGS` reconciliation in #561.

## 1. Register verification

| Check | Result |
|---|---|
| Regeneration from `theorems/**/*.md` | 280 rows, deterministic (re-run produced zero diff) |
| File↔card bijection | **280 = 280**, no duplicates, no omissions |
| `check_theorem_register.py` | exit 0 — **0 errors, 63 warnings** |
| Heuristic→PROVED promotion | **none** — all 45 PROVED rows carry `explicit proof claim, no open qualifier found`; 0 PROVED rows with heuristic/`no status` notes |
| Author sign-off obligation | preserved — caveat block present in generated MD header |

### Warning analysis (64 total)

| Class | Count | Nature |
|---|---|---|
| Duplicate card-id groups | 32 | Structural — ID collisions, documented in `DUPLICATE_CARD_ID_MAP.json` |
| Missing referenced paths inside cards | 27 | Structural — cards cite `tests/test_*.py` / `scripts/` / `reports/` paths absent from repo (pre-existing card-content gaps; e.g. `tests/test_holonomies.py`, `tests/test_discrete_dirac.py` never committed) |
| Unresolved dependency T095 | 4 | Epistemic/content — T096–T099 reference a non-existent predecessor card |

One stale path is a **relocation**, not a loss: card T099 cites
`artifacts/bicircular_annular_audit.json`, which actually lives at
`reports/bicircular_annular_audit.json`. Card-content corrections are left to
the author (they touch theorem records).

## 2. Independent graph audit

`docs/UNIFIED_THEOREM_EDGES.json` was audited against git history
(`git show 8477df3:docs/UNIFIED_THEOREM_EDGES.json`), not just re-run:

- **Edge preservation:** all 353 pre-existing edges present in the new graph;
  **0 removed, 0 modified**. Exactly **17 edges added** (16 initial + MQ-T005 after main merge) — all
  `thematic-index-classification` → `H-OTHER`, `status: provisional`, with an
  explicit "post-reorg graph sync / pending author topic assignment" caveat.
- **Node preservation:** 0 nodes removed, 0 nodes modified; 17 theorem-record
  nodes added, ids `THM:<unique filename stem>`.
  **0 removed, 0 modified**. Exactly **17 edges added** by the sync runs —
  16 `thematic-index-classification` → `H-OTHER` (`status: provisional`,
  explicit "post-reorg graph sync / pending author topic assignment" caveat).
  The 17th (MQ-T005) was subsequently assigned `H-RGS` with a proper topical
  caveat by PR #561 on `main`; it is no longer parked at `H-OTHER`.
- **Node preservation:** 0 nodes removed, 0 nodes modified; 17 theorem-record
  nodes added (16 still provisional H-OTHER, MQ-T005 since assigned H-RGS), ids `THM:<unique filename stem>`.
- **Counts:** 280 records / 334 nodes / 370 edges — verified by independent
  recount; `coverage` block, `.md` prose and JSON all agree.
- **Dangling edges:** 0. **Duplicate node ids:** 0. **Duplicate intro
  paragraph** in `.md`: fixed (was a merge artifact).
- **Determinism/idempotence:** 3 consecutive generator runs → zero diff.
- **Independent tests:** `tests/test_post_reorg_independent_audit.py`
  (11 tests) reconstructs bijectivity, hub-edge uniqueness, coverage
  consistency, md/json agreement, duplicate-map reconciliation and NPZ hash
  re-verification **without importing the generator scripts**.

## 3. Duplicate-ID reconciliation

- `DUPLICATE_CARD_ID_MAP.json` cross-validated two ways: every listed path
  exists on disk; groups exactly equal the duplicate `id` groups in the
  regenerated register CSV (independent test).
- **No renumbering introduced:** diff of register CSV vs pre-PR version shows
  **0 id changes** across the common files; only newly merged cards added.
- **Proposed canonical policy (NOT applied — author decision):**
  1. Keep `theorems/` file paths as the sole stable identifiers (status quo,
     zero migration cost);
  2. Or adopt `T###-<slug>` composite keys where slug disambiguates
     (e.g. `T113I-…` already does this informally);
  3. Or a one-time author-approved renumbering with a redirect table —
     highest cost, breaks external citations.
  Recommendation: option 1 + mandatory slug-in-id convention for *new* cards.

## 4. NPZ provenance — deep check

SHA-256 (identical within each group):

| Group | SHA-256 prefix | Files | Arrays |
|---|---|---|---|
| J0=0.001 | `609aa7ee…` | N16, N24, N48 | times(401), Γ_M2(401×401), Γ_M1(401×401), float64 |
| J0=0.002 | `a284838e…` | N16, N32, N64 | same |
| J0=0.004 | `033b354d…` | N16, N24, N48 | same |

- Content depends on **J0 only**; the `N` label has **no effect** on bytes.
- Kernel is symmetric, smooth, numerically near rank-4; `times ∈ [0,8]`, 401
  samples. No array or metadata encodes N.
- Git history: files entered at root in `07d9325` ("Retain T149 full FEEC
  report as workflow artifact"); `" (1)"` download-duplicates were verified
  byte-identical and correctly removed in the reorg. **No producer script,
  card or doc in the repo defines what N parameterises** — provenance of the
  labels is not reconstructible from repository evidence.
- **Status: `unresolved`** for all three groups (alias-candidate for two of
  three names per group; which N — if any — is authentic cannot be
  determined). Nothing renamed, deleted or promoted.

## 5. C60 producer contract — resolved

- `build_truncated_icosahedron_transports.py` confirmed **absent from all git
  history** — it was an uncommitted local name.
- `scripts/c60_truncated_icosahedron_transports.py` was executed end-to-end in
  a sandboxed OUT_DIR and its output compared against the committed
  `artifacts/truncated_icosahedron_transports_2026-11-21.{npz,json}`:
  **every array identical (maxdiff = 0.0)** — vertices (60,3), faces (32,6),
  normals, bases, D_bfs, D_dfs, vertex_holonomy; all JSON checks identical
  (vertex holonomy = 12° × 60 = 720°, gauge consistency ~2.3e-15).
- The 8 drivers' contract is `exec()` of the script prefix before
  `# ---------- 7. Verifiche`; verified the marker exists and the prefix
  exposes the required namespace (NF, FN, A, D, PTS, VID, …). C60 targeted
  tests passed 19/19 during the reorg pass; files unchanged since.
- **Conclusion:** the committed script is a bit-exact producer of the
  2026-11-21 artifacts — the "missing producer" gap is closed. No semantic
  difference found; no speculative replacement created.

## 6. dec_se3 and stale references

- `archive/dec_se3_legacy/` unchanged; grep confirms **zero** active
  `.py`/workflow/test references outside `archive/`.
- Sole stale doc reference (`output/dec_se3/src/dec_se3/refinement.py` in
  `docs/C60_DPO_INTERVALS_AND_T_BIANCHI_REFINEMENT_2026-11-21.md`) annotated
  in a separate mechanical commit — the item remains an open requirement,
  history preserved.

## 7. Commands executed

| Command | Exit | Result |
|---|---|---|
| `python3 scripts/build_theorem_register.py` | 0 | 280 rows, deterministic |
| `python3 scripts/check_theorem_register.py` | 0 | 0 errors, 63 warnings |
| `python3 scripts/build_unified_theorem_graph.py` (×4 total) | 0 | idempotent |
| `python3 scripts/build_duplicate_id_map.py` | 0 | map regenerated, no diff |
| `python3 scripts/build_npz_provenance_manifest.py` | 0 | manifest regenerated, no diff |
| `pytest -q tests/test_register_graph_consistency.py tests/test_post_reorg_independent_audit.py` | 0 | **19 passed** |
| `pytest tests/` (full suite) | — | **not run** (>40 min budget; pre-existing collection errors documented in reorg audit) |

## 8. Anomaly table

| # | Anomaly | Severity | Disposition |
|---|---|---|---|
| 1 | 32 duplicated card-id prefixes (85 cards) | Medium | Documented; author numbering policy required |
| 2 | 27 card-referenced test/script paths absent | Low-Medium | Pre-existing card gaps; author to reconcile |
| 3 | T095 dependency unresolved (T096–T099) | Medium | Author decision |
| 4 | `two_time_kernel` N labels unverifiable | Medium | `unresolved`; data preserved |
| 5 | 17 new graph nodes parked at H-OTHER | Low | Provisional by design; author topic assignment |
| 5 | 16 new graph nodes parked at H-OTHER (MQ-T005 later assigned H-RGS by #561) | Low | Provisional by design; author topic assignment for the remaining 16 |
| 6 | 112 low-confidence heuristic register statuses | Medium | Sign-off caveat in place; no promotion |

## 9. Acceptance criteria

| Criterion | Status |
|---|---|
| Register and graph coherent | ✅ verified independently |
| Independent tests pass | ✅ 19/19 |
| No invented dependencies | ✅ verified vs git history (+17 provisional only) |
| No invented dependencies | ✅ verified vs git history (+17 provisional; 16 still H-OTHER, MQ-T005 → H-RGS by #561) |
| No ambiguous data deleted/promoted | ✅ NPZ preserved, statuses unchanged |
| Scientific decisions under author control | ✅ all open items documented |

## Recommendation: **READY**

All mechanical consistency guarantees verified independently; every residual
item is explicitly documented as an author decision rather than silently
resolved. The only caveat is that card-content path fixes (27 missing test
references) and the duplicate-ID numbering policy remain author-domain work —
but they are tracked, not hidden.
