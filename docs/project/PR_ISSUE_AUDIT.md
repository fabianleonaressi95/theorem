# PR and issue audit — 26 November 2026

Policy: nothing merged or closed by the audit itself; recommendations only.

## Registry publication

The documentation bundle introduced by theorem PR **#464** is now **MERGED** into `main`.
- Merge commit: `8d379ac191db24123db014973b9e2de44d9795df`
- Head commit: `9db111f131e462e9538f2b618f52cedc9f4eebae`
- Files: the five project-registry documents under `docs/project/`.
- This publication merge does not imply that any scientific claim was upgraded or that any cleanup recommendation was executed.

## Open pull requests

*Updated 2026-11-26 (second delta pass, verified against GitHub API): #468, #470, #472, #473 and registry PR #475 were all MERGED (~17:44–17:47Z). Open PRs are now #471, #476, #477 (draft), #478 (draft), #479. Verified counts: 428 merged PRs, 29 closed-unmerged, 10 open issues; main @ `38d139c`.*

### theorem — open PRs

| PR | Title | State | CI | Assessment |
|---|---|---|---|---|
| #471 | Audit oriented circumcentric dual edges in Ellis icosphere | OPEN, mergeable | `test` SUCCESS | +9/−0 across T049/T070 docs + prototype script/tests. Small scoped correction. **Recommend: merge after owner review.** |
| #476 | Derive discrete coframe from the RGS geometric carrier | OPEN, mergeable | No checks reported | +491/−0: new audit JSON, 2 docs, 1 script — directly relevant to the RGS coframe/spin-connection thread (theorem #321 merged). **Recommend: confirm CI coverage, then merge.** |
| #477 | Record Q6 NL/NLT sigma-1.25 pilot and correct T1 quotient Jacobian | OPEN **DRAFT**, mergeable | `cubical-and-syntax` SUCCESS | +336/−5: pilot artifact + protocol doc + workflow/script changes. Draft — owner review pending. |
| #478 | Add Sangaku circle-geometry classification workstream | OPEN **DRAFT**, mergeable | No checks reported | +284/−0: new `research/sangaku_geometry/` workstream (protocol, manuscript, case sheets). Draft — owner review pending. |
| #479 | Formalize Volterra dipole-to-edge theorem and C0-IPDG comparison | OPEN, mergeable | No checks reported | +149/−0: single manuscript doc. Low risk; **recommend merge after review.** |

### Merged since first audit pass (2026-11-26 ~17:17–17:47Z)

| PR | Title | Merged at (UTC) |
|---|---|---|
| #449 | C60 Stone–Wales 90° dual-flip + vesica bridge | 17:17 |
| #450 | Volterra dipole-to-edge stress/energy limit | 17:17 |
| #458 | RGS defect benchmark (Torino/Morandotti) | 17:17 |
| #461 | SE(3) tetrahedral non-Abelian Bianchi | 17:23 |
| #464 | Master project registry | ~17:23 |
| #468 | Q6–C60 equivariance on Klein-four subgroup | 17:44 |
| #470 | EG-01 bottleneck benchmark | 17:44 |
| #472 | T154 In2Infinity Extended Jitterbug audit | 17:46 |
| #473 | Theorem graph inventory / T152 crosswalk repair | 17:46 |
| #475 | Registry delta update | 17:46 |

## Scientific content and CI audit — PRs #449, #450, #458, #461

The four PR head commits were checked through GitHub check-runs on 2026-11-26. All four PRs are merged; all reported checks on their respective PR head commits concluded successfully.

| PR | Head commit | PR-head checks | Evidence actually established | Remaining boundary |
|---|---|---|---|---|
| #449 | `850d6945e60d745b48b6e86c5ce75f871c9ae7ef` | `audit`: success | Dual-triangulation enumeration reports 30 labelled admissible C60 flips; exact graph invariants and the two integer chain-map identities are checked for the selected representative. MMFF94s nuclear-coordinate covariance changes are reported for one selected relaxation. | No electronic-density calculation, DFT, transition-state barrier, Kathara/Q6 intertwiner, or universal vesica/fullerenic law. The covariance result is a one-case geometric proxy; nonzero final gradient norms are recorded. |
| #450 | `0adc60a7a99ed8d4ddfba355875cbdaf9b28b859` | `audit`: success | Matched Volterra dipole and edge incompatibility sources are passed through the same periodic Fourier Airy solver. Tests cover residuals, source means, (b=\Omega d), and monotonic reduction of stress/strain/energy discrepancies in a fixed-core small-separation comparison. | A passing test is not a proof of a continuum theorem. No displacement-FEM cross-check, singular-core renormalization, Mosco convergence, or Gamma convergence. The full uploaded sweep artifact was not independently inspected in this audit. |
| #458 | `1618f4d22fd4ca5b5a66cb538fcbb1ac5992ecd4` | `two-core-p3-c0-ipdg`, `trace-constant`, `independent-remeshing`, `distance-refinement`, `cubical-and-syntax`, `defect-benchmark-tests`: all success | The merged benchmark and its listed PR-head checks pass. T3/T4 and the separate robustness scripts are added with explicit preregistered criteria and reproducible commands. | The PR text explicitly says the full T3/T4 execution and robustness artifact are still outstanding. Bistability remains **not demonstrated**; script presence is not numerical evidence. |
| #461 | `91e34047accf509ed83e7af8bfa9792f0ab377a6` | `audit`: success | The tetrahedral ordered non-Abelian curvature identity is derived algebraically under stated orientation/base-point conventions; the script specifies 1,000 seeded SE(3) assignments and gauge-covariance checks. | This is not a discrete torsion Bianchi identity. No Cartan torsion, deWit/Nye identification, continuum limit, or general 3-complex extension is established. |

### Separate post-merge main workflow observation

A separate `push` workflow on `main`, run [45866447326](https://github.com/fabianleonaressi95/theorem/actions/runs/45866447326), was still **in progress** at the time of this audit. Its Morandotti FEM matrix included completed failures for three `d=0.48/0.56, h=0.08` cases, several cancelled jobs, and several jobs still running; the trace-constant, distance-refinement, and independent-remeshing jobs shown in that run had succeeded. This is a post-merge main workflow, not the PR-head check result for #458. It must be triaged separately; do not describe the overall main workflow as green.

**Classification rule:** merge status and CI success certify repository integration and the specified software checks only. They do not automatically promote the scientific statements beyond the evidence and limitations recorded above.

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
