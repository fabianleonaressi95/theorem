# Post-reorganisation consistency audit — 2026-11-27

Follow-up to `REPOSITORY_REORGANIZATION_AUDIT_2026-11-26.md` (PR #548, merged
as `8477df3`). Scope: mechanical consistency only — no theorem statement, proof
or numerical result was modified. Branch: `chore/post-reorg-consistency`.

## 0. Inventory correction discovered during this pass

The reorg register was generated against a `main` snapshot containing **272**
cards. Seven cards were merged afterwards (EQC-RGS-Q6-minimal-gates,
T113I-ekn, T124-mixed-tensor, T155-rhombic, T157, T158, T159). The register has
been **regenerated**: it now covers **279 cards** (all `theorems/**/*.md`).
Status distribution after regeneration: PROVED 45, EXACT_CERTIFICATE 14,
NUMERICALLY_VERIFIED 85, CONDITIONAL 83, CANDIDATE 6, HYPOTHESIS 2, OPEN 44.
`check_theorem_register.py` reports **0 errors** (was 7 before regeneration).

## 1. Dependency graph synchronisation (WP1)

**Source of stale counts:** `docs/UNIFIED_THEOREM_EDGES.json` is a
hand/tool-generated artifact (no generator script existed in the repo); its
`coverage` block still claimed 263 records / 317 nodes / 353 edges, and
`UNIFIED_THEOREM_DEPENDENCY_GRAPH.md` contained a duplicated intro paragraph
(248- and 263-record versions — a merge artifact).

**Action:** new reproducible generator
`scripts/build_unified_theorem_graph.py` reconciles the JSON against the live
`theorems/` tree **by file path** (stable identifier; node ids embed unique
filename stems, so duplicated T-prefixes cannot collide). Result:

- 16 cards were missing from the graph → added as `theorem-record` nodes with
  standard provisional classification edges.
- 0 stale nodes, 0 dangling edges after sync.
- New totals: **279 theorem records, 333 nodes, 369 edges**
  (279 classification + 30 hub-to-companion + 60 typed crosswalk arrows —
  all pre-existing edges preserved verbatim; **no dependency was invented**).
- The 16 new records are parked under hub `H-OTHER` with an explicit caveat:
  the original hub assignments were per-record judgements, not a reproducible
  rule, so guessing hubs would fabricate classification. **Author topic
  assignment required** (list in §6).
- `.md` updated: duplicate paragraph removed, counts corrected, sync date noted.

Idempotent: second run adds 0 nodes.

## 2. Duplicate theorem identifiers (WP2)

`scripts/build_duplicate_id_map.py` → `docs/project/DUPLICATE_CARD_ID_MAP.json`.

- 279 cards, **225 unique id prefixes, 33 duplicated prefixes covering 87 cards**
  (up from the 29 groups estimated in the reorg audit — the recount includes
  non-T prefixes: EQC-*, MQM*, S*, T*, TSMR-*).
- Largest groups: T113 ×10, T049 ×6, MQM1 ×5, T143 ×4, T071/T099 ×3, and 27
  groups of ×2.
- **No renumbering, no cross-reference rewrite.** File paths are documented as
  the stable identifiers until the author approves a canonical numbering policy.

## 3. Duplicate NPZ provenance (WP3)

`scripts/build_npz_provenance_manifest.py` → `docs/NPZ_PROVENANCE_MANIFEST.json`.
Scanned 26 `.npz`/`.npy` files under `artifacts/ data/ audits/ archive/
results/ output/`; 20 unique MD5s; **3 duplicate groups, all
`artifacts/two_time_kernel_*.npz`**:

| MD5 | Files | Arrays |
|---|---|---|
| `3e277947…` | `two_time_kernel_N{16,24,48}_J0_0.004.npz` | times, Gamma_M2, Gamma_M1 |
| `a58090f4…` | `two_time_kernel_N{16,24,48}_J0_0.001.npz` | same |
| `f93bd544…` | `two_time_kernel_N{16,32,64}_J0_0.002.npz` | same |

Byte-identical files carry **different N labels** — the filename parameter does
not correspond to distinct content. Classification: `alias-candidate`
(repeated exports or mislabeled artifacts). **Unresolved provenance — flagged
for author review; nothing deleted or renamed.** Which N value (if any) is
correct cannot be determined from the files alone.

## 4. Legacy `dec_se3` (WP4)

- `archive/dec_se3_legacy/` left unchanged.
- Reference scan: **no active `.py`, workflow or test** imports or invokes
  `dec_se3` outside `archive/`. Only prose mentions remain
  (`docs/C60_DPO_INTERVALS_AND_T_BIANCHI_REFINEMENT_2026-11-21.md` references
  `output/dec_se3/src/dec_se3/refinement.py` — a path that does not exist in
  the repo; `docs/project/*` and README describe the archival itself).
- Conclusion: no evidence of an active requirement → stays archived. The stale
  `output/dec_se3/...` path mention in the C60 doc is a documentation defect,
  not a code dependency; left for author decision (fix vs annotate).

## 5. Missing C60 producer `build_truncated_icosahedron_transports.py` (WP5)

- `git log --all -S` and name-only history searches: the file **never existed
  in git history**. It is referenced only by docs
  (`TRUNCATED_ICOSAEDRON_TRANSPORTS_2026-11-21.md`,
  `C60_TRANSPORTS_GH_CROSSAUDIT_2026-11-21.md` — which labels it "pipeline GH,
  non in repo" / local construction) and by archived orphans.
- The committed `scripts/c60_truncated_icosahedron_transports.py` implements
  the same documented contract: truncated icosahedron (60 vertices, 32 faces,
  90 edges), face-to-face SO(2) transports, gauge field, holonomy checks,
  JSON+NPZ output. All 8 repaired drivers `exec()` its prefix (before
  `# ---------- 7. Verifiche`) — verified working (`exec` exposes NF, FN, A,
  D, PTS, VID, …).
- **Gap that remains:** equivalence between the committed script's output and
  the original `truncated_icosahedron_transports_2026-11-21.{npz,json}`
  artifacts (produced by the never-committed script) was not re-verified
  array-by-array in this pass. No speculative replacement created; the five
  repaired drivers were not touched (no reproducible defect found; C60 tests
  19/19 pass).

## 6. Epistemic-status safeguards (WP6)

- All register statuses preserved; regeneration is deterministic and changed
  only by adding the 7 new cards.
- `build_theorem_register.py` now emits a caveat block in the generated MD:
  heuristic statuses are not author-certified; rows flagged `no status` /
  `audit/benchmark card (heuristic)` must not be externally cited without
  author sign-off; no heuristic was promoted to PROVED.
- `status_note` evidence strings remain in the CSV for traceability.

## 7. Validation commands and results

| Command | Exit | Result |
|---|---|---|
| `python3 scripts/build_theorem_register.py` | 0 | 279 rows regenerated |
| `python3 scripts/check_theorem_register.py` | 0 | **0 errors**, 64 warnings |
| `python3 scripts/build_unified_theorem_graph.py` (×2) | 0 | +16 nodes; idempotent |
| `python3 scripts/build_duplicate_id_map.py` | 0 | map written |
| `python3 scripts/build_npz_provenance_manifest.py` | 0 | manifest written |
| `python3 -m pytest tests/test_register_graph_consistency.py -q` | 0 | **8 passed** |

Remaining checker warnings (64): missing test/script paths referenced inside
card bodies, and duplicate card-id groups — all genuine findings documented in
`DUPLICATE_CARD_ID_MAP.json`, not checker defects. Full `pytest tests/` suite
intentionally not run (>40 min; per mandate). C60 files unchanged → C60
targeted tests not re-run in this pass (19/19 passed during the reorg pass).

## 8. Items requiring explicit author decision

1. **Canonical numbering policy** for the 33 duplicated id groups (87 cards) —
   renumber, alias, or keep path-keyed forever.
2. **Hub assignment** for the 16 newly indexed graph records (currently
   `H-OTHER`, provisional).
3. **`two_time_kernel_*` NPZ labels** — which N is authentic, or mark all
   three groups as unverified duplicates.
4. **Stale `output/dec_se3/...` path** mention in
   `docs/C60_DPO_INTERVALS_AND_T_BIANCHI_REFINEMENT_2026-11-21.md`.
5. **Array-level equivalence check** between `c60_truncated_icosahedron_transports.py`
   output and the 2026-11-21 transport artifacts.
6. **Author sign-off** on heuristic register statuses before external citation
   (111 rows flagged low-confidence).
