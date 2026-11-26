# PR and issue audit — 26 November 2026

Policy: nothing merged or closed by the audit itself; recommendations only.

## Registry publication

The documentation bundle introduced by theorem PR **#464** is now **MERGED** into `main`.
- Merge commit: `8d379ac191db24123db014973b9e2de44d9795df`
- Head commit: `9db111f131e462e9538f2b618f52cedc9f4eebae`
- Files: the five project-registry documents under `docs/project/`.
- This publication merge does not imply that any scientific claim was upgraded or that any cleanup recommendation was executed.

## Open pull requests

### theorem

| PR | Title | State | CI | Assessment |
|---|---|---|---|---|
| #449 | C60 Stone–Wales 90° dual-flip + vesica bridge | OPEN, mergeable=UNKNOWN | `audit` SUCCESS | Diff adds `scripts/audit_c60_stone_wales.py`, `tests/test_c60_stone_wales.py`, 3 docs (+158/−31). Claims are scoped: dual-graph reconstruction, 30 labelled flips, integer chain-map identities, MMFF94s covariance proxy with explicit "not DFT/not barrier" caveat. **Recommend: review then merge** — consistent with repo conventions, claims properly bounded. |
| #450 | Volterra dipole-to-edge stress/energy limit | OPEN **DRAFT**, mergeable | `audit` SUCCESS (run 45864849396, head 0adc60a) | Extends merged #131 work to matched Airy elasticity comparison; sweep artifact uploaded; residuals ~1e-16. Draft status may be intentional pending owner review of the sweep tables. **Recommend: owner review of draft → merge if satisfied; otherwise mark ready.** |
| #458 | RGS defect benchmark (Torino/Morandotti) | OPEN, mergeable, **UNSTABLE** | Mixed: `trace-constant`, `independent-remeshing`, `cubical-and-syntax`, `defect-benchmark-tests` SUCCESS; `distance-refinement` and `two-core-p3-c0-ipdg` showed no conclusion (queued/running at audit time); PR body empty | +386/−12 across 6 files incl. 3 new workflow files and 2 scripts + 1 test + 1 protocol doc. Empty PR body is a documentation gap. **Recommend: wait for pending checks, require PR description, then merge.** |
| #461 | SE(3) tetrahedral non-Abelian Bianchi | OPEN, mergeable | **No checks reported** | +284/−0: one script `audit_se3_tetrahedral_bianchi.py` + one doc. Claims strictly bounded (curvature Bianchi only; explicitly not torsion/deWit/Nye). **Recommend: verify a workflow runs the script (no CI seen) or add one; then merge.** |

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
