# PR and issue audit — 26 November 2026

Policy: nothing merged or closed by the audit itself; recommendations only.

## Registry publication

The documentation bundle introduced by theorem PR **#464** is now **MERGED** into `main`.
- Merge commit: `8d379ac191db24123db014973b9e2de44d9795df`
- Head commit: `9db111f131e462e9538f2b618f52cedc9f4eebae`
- Files: the five project-registry documents under `docs/project/`.
- This publication merge does not imply that any scientific claim was upgraded or that any cleanup recommendation was executed.

## Open pull requests

*Updated 2026-11-26 (delta pass): the four PRs audited earlier today (#449, #450, #458, #461) were all **MERGED** at ~17:17–17:23Z by the owner, together with registry PR #464. Five new open PRs (#468–#473) appeared subsequently.*

### theorem

| PR | Title | State | CI | Assessment |
|---|---|---|---|---|
| #468 | Test Q6–C60 equivariance on the Klein-four subgroup | OPEN, mergeable | `v4-equivariance` SUCCESS (×2) | +610/−0: new workflow, audit JSON, doc, script. Bounded test/audit artifact. **Recommend: merge after owner review.** |
| #470 | Add EG-01 bottleneck benchmark | OPEN **DRAFT** | No checks reported | +395/−0: `research/` docs + `benchmarks/eg01_bottleneck.py`. Draft — owner review pending. |
| #471 | Audit oriented circumcentric dual edges in Ellis icosphere | OPEN **DRAFT**, mergeable | No checks reported | +149/−4: extends T049/T070 scripts/tests/docs. Draft — owner review pending. |
| #472 | Add T154: In2Infinity Extended Jitterbug source and geometry audit | OPEN, mergeable | No checks reported at audit time | +308/−0: T154 theorem doc, audit script, test, source-review note. **Recommend: confirm a workflow covers the new test, then merge.** |
| #473 | Reconcile theorem graph inventory and repair T152 crosswalk | OPEN, mergeable | No checks reported at audit time | +1308/−1117 across README, `UNIFIED_THEOREM_DEPENDENCY_GRAPH.md`, `UNIFIED_THEOREM_EDGES.json`, `UNIFIED_TWO_REPOSITORY_THEOREM_PROGRAM.md`. Large doc/JSON restructure — **recommend careful review before merge** (touches canonical cross-repo graph). |

### Merged since first audit pass (2026-11-26 ~17:17–17:23Z)

| PR | Title | Notes |
|---|---|---|
| #449 | C60 Stone–Wales 90° dual-flip + vesica bridge | MERGED — results preserved on main |
| #450 | Volterra dipole-to-edge stress/energy limit | MERGED (was draft) |
| #458 | RGS defect benchmark (Torino/Morandotti) | MERGED |
| #461 | SE(3) tetrahedral non-Abelian Bianchi | MERGED |
| #464 | Master project registry (this audit's docs) | MERGED |

### fullerene-c64-audit

| PR | Title | State | CI | Assessment |
|---|---|---|---|---|
| #1 | C64 fullerene computational audit | OPEN, mergeable | **No CI configured** | `c64-audit`→`main`, +46,885/−1 (bulk is data/logs under `data/`). Self-contained repo; acceptance tests exist (`tests/test_audit.py`, reported 11 pass locally). Large diff is mostly generated artifacts — acceptable for an audit-data repo but consider whether `data/` logs belong in git. **Recommend: merge after owner confirms artifact policy; optionally add a minimal CI running `pytest tests/test_audit.py`.** |

### rheomarine — verification result

PRs **#20, #21, #22 are MERGED** into `main` (`eca7b9a`, verified 2026-11-26): Eulerian `wet`/`active`/`open_edges` solver + `qc_holes` policy, HFR input recovery/reproduction record, and status docs are all on main. Suite: 64 tests (45 baseline preserved). No action needed.

## Verified merged (results preserved)

- theorem **#344** (SE(3) tetrahedral defect fixture, merged 2026-11-21), **#131** (Volterra dipole-to-edge elastic limit, merged 2026-11-11), **#232** (T103/T105/T107 Actions hardening, merged 2026-11-12) — all MERGED; content present on main.
- theorem recent merges #413–#460 cover the Q6/TSMR/Jitterbug/FEEC programme (see REPOSITORY_MAP.md).

## Closed-unmerged PRs

theorem: 7 closed PRs (superseded iterations — normal). rgs-qlg: 10 closed. No action.

## Open issues

- **theorem (10):** #409 Jitterbug eight-panel coupling; #402 unified theorem graph expansion; #401 64-TG/FCC-D3→Jitterbug immersion; #400 Cartan torsion/coframe; #399 mixed frame field A_a{}^m; #398 Vesica phase↔Jitterbug frame map; #114 JA vs measured loops; #113 actuator hysteresis fit; #109 188D/Krist-All source-data import; #84 Q6–D5 Wilson integer fibre port.
- **rgs-qlg:** #3 QLG gauge-equivariant roadmap.
- **kilaw:** #1 "this is the repo" (trivial — close candidate).
- **rheomarine:** #2 HFR–M0 (open by design; validation gates DATA-BLOCKED).

## Branch hygiene

- theorem: ~393 branches vs 4 open PRs → large stale-branch accumulation; most are likely merged/superseded. Recommend an owner-approved branch audit (list → confirm → delete) rather than blanket deletion.
- rgs-qlg: ~200 branches vs 1 open issue, 0 open PRs → same recommendation.
- rheomarine: 21 branches ≈ merged PR heads; candidates for cleanup after confirmation.
- fullerene-c64-audit: 2 branches (main + c64-audit) — clean.
