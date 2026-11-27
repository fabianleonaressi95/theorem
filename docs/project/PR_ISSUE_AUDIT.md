# PR and issue audit — 27 November 2026

Policy: nothing merged or closed by the audit itself; recommendations only.

## Registry publication and subsequent reconciliations

The original project-registry bundle **#464** and its delta updates **#475** and **#480** are merged. PR #508 reconciled the theorem-record inventory and graph counts; its stated validation is 263/263 theorem records indexed, zero missing indexed records, zero stale graph paths, 317 nodes and 353 directed edges. These are inventory checks, not mathematical proof upgrades.

Subsequent verified merges include #487 (Ellis circumcentric cleanup), #514 (Ellis audit v2), #516 (T156 incidence audit), #517 (In2Infinity T154/T155 source and transition work), #518 (C60 pyracylene patch clarification), #519 (SGC-003 / Ohsu Kannon source audit), #520 (T124 character proof), #521 (Q6 many-body / RGS Berry audits), and #523 (T099 reproducibility workflow). Direct commits also document T157/T158 covariant Whitney constructions and the T156 FEEC draft withdrawal. T158 reports order-8/order-12 quadrature agreement near 10^-14 while leaving mesh-refinement convergence open. The duplicate T156 FEEC draft was removed; work continues in the existing T149–T158 sequence. Latest main commit observed: `520cf684148272a2be9932e1a50d5fe6659162cc`.

This registry pass is documentation-only. It does not promote scientific claims, alter theorem proofs, or perform branch/issue cleanup.

## Live pull-request state — 2026-11-27

A fresh GitHub PR search returned **five open research PRs in `theorem`: #524–#528**. Their diffs and CI were not independently assessed in this registry pass. The merged-PR search is capped, so no new total merged or closed-unmerged count is published. This registry reconciliation will be submitted as a separate documentation-only PR.

### theorem — open PRs

| PR | Title | State | CI | Assessment |
|---|---|---|---|---|
| [#524](https://github.com/fabianleonaressi95/theorem/pull/524) | Audit Pellis GSR register and correct T150/T151 statements | OPEN | Not independently assessed in this registry pass | Owner review; verify source provenance and exact statement corrections. |
| [#525](https://github.com/fabianleonaressi95/theorem/pull/525) | Develop PEL-05: independent spectral-state selection criteria | OPEN | Not independently assessed in this registry pass | Owner review; check independent criteria and avoid circular spectral selection. |
| [#526](https://github.com/fabianleonaressi95/theorem/pull/526) | Add matched Volterra dipole-to-edge Morandotti C0-IPDG benchmark | OPEN | Not independently assessed in this registry pass | Owner review; a separate Morandotti FEM workflow had four ARPACK residual-certification failures and eight cancellations; do not treat those uncertified eigenpairs as physical/model falsification. |
| [#527](https://github.com/fabianleonaressi95/theorem/pull/527) | Audit carrier-derived coframe on the full Q6 PSU connection | OPEN | Not independently assessed in this registry pass | Owner review; verify the carrier-to-connection construction and avoid assuming the coframe identity. |
| [#528](https://github.com/fabianleonaressi95/theorem/pull/528) | Refine Q6 mean-field and Berry audits with verified controls | OPEN | Not independently assessed in this registry pass | Owner review; preserve separation between finite benchmark controls and physical interpretation. |
| [#531](https://github.com/fabianleonaressi95/theorem/pull/531) | Reconcile project registry with live theorem audit | OPEN, documentation-only | Checks pending | This registry update; owner review before merge. |

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
| #471 | Ellis oriented circumcentric dual audit | 2026-11-27 |
| #476 | RGS carrier-derived discrete coframe | 2026-11-27 |
| #477 | Q6 NL/NLT sigma-1.25 pilot and T1 quotient Jacobian | 2026-11-27 |
| #478 | Sangaku circle-geometry classification workstream | 2026-11-27 |
| #479 | Volterra dipole-to-edge C0-IPDG comparison | 2026-11-27 |
| #480 | Post-merge registry synchronization | 2026-11-26 |
| #487 | Ellis circumcentric dual audit cleanup | 2026-11-27 |
| #508 | Live theorem inventory and graph-count reconciliation | 2026-11-27 |
| #514 | Ellis circumcentric dual audit v2 | 2026-11-27 |
| #516 | T156 rhombicuboctahedron–snub-cube incidence audit | 2026-11-27 |
| #517 | In2Infinity T154/T155 source and transition audit | 2026-11-27 |
| #518 | C60 pyracylene Stone–Wales patch clarification and regression test | 2026-11-27 |
| #519 | SGC-003 / 1837 Ohsu Kannon source audit | 2026-11-27 |
| #520 | T124 mixed tensor character proof | 2026-11-27 |
| #521 | Q6 many-body mean-field and RGS Berry-cycle audits | 2026-11-27 |
| #523 | T099 bicircular-annular reproducibility CI audit | 2026-11-27 |

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

## Follow-up diagnostic — Morandotti FEM and Q6 NL/NLT (2026-11-27)

### Morandotti FEM workflow 45866447326

The workflow is now **completed with conclusion FAILURE**, not merely in progress. Its 12 independent FEM case jobs ended as follows: **4 failed, 8 cancelled**; the global assembly/statistics job was skipped. The four failures all stop inside `models/morandotti_trace_constant.py::largest_generalized_eigenvalue`, after mesh assembly and environment checks, because ARPACK's generalized eigenpair fails the independent residual certification. The dense fallback is intentionally unavailable for these reduced spaces (`n=5228`–`5345`, fallback limit 3000).

| Distance | Mesh size | Seed | Reduced dimension | Best relative residual | Solver eigenvalue | Rayleigh quotient |
|---:|---:|---:|---:|---:|---:|---:|
| 0.48 | 0.08 | 11 | 5282 | 0.2910198 | 20645.8943 | 9.0441 |
| 0.48 | 0.08 | 29 | 5228 | 0.3826930 | 11293.9807 | 14.9979 |
| 0.48 | 0.08 | 47 | 5282 | 0.2335914 | 25564.9069 | 9.1081 |
| 0.56 | 0.08 | 29 | 5345 | 0.2754461 | 3655.0909 | 5.9221 |

Interpretation: these are **uncertified numerical eigenpairs**, not evidence that the Morandotti model or the trace inequality is false. The failure is in the sparse generalized eigensolver/certification path. The eight cancelled cases have no numerical outcome; the aggregate stage did not run. Re-running unchanged jobs would repeat the same failure and is not a scientific remedy. Next technical task is a better-conditioned/generalized eigensolver strategy with an independently checked residual and a regression fixture at these four parameter/seed combinations. No solver patch or successful rerun is claimed here.

### Q6 NL/NLT pilot: repaired artifact and evidence boundary

The pilot artifact `artifacts/q6_nl_nlt_candidate_sigma_1p25_pilot_2026-11-26.json` contained duplicated lines and was not valid JSON. The duplicated copies were removed without changing the retained measurements or classifications; the corrected file was parsed successfully before publication (commit `55753bc57ff564a0d69787949a72904b1f7eadac`).

The machine-readable pilot reports:

- **T1:** only the origin fixed point was verified stable. The 200 random Newton starts per model did not converge to a second root. T1's bistability criterion is **not passed**.
- **T3:** in the local three-point window `sigma = 1.20, 1.25, 1.30`, 20 seeds and dwell values 640/2560/10240, NLT's mean hysteresis gap is non-decreasing and its long/short ratio is 3.550896 (local criterion passed). NL's ratio is 0.235084 and is not non-decreasing (criterion failed).
- **T4:** at dwell 640 only, NLT's Q6/Q4 gap ratio is 0.609829 at sigma 1.20 and 0.516773 at 1.25 (threshold 0.50 passed), but 0.407291 at 1.30 (failed). NL fails at all three tested sigma values.
- **Robustness:** at sigma 1.25 only, 80/80 cases (NL/NLT × 20 seeds × aligned/random initial families) pass the 10% comparison threshold for both RK4 step halving and DOP853. Maximum relative differences are 0.001624 for step halving and 0.001642 for DOP853.

The workflow `.github/workflows/qn-nl-nlt-t3-t4.yml` performs compilation and cubical-complex tests; it does **not** execute the T3/T4 numerical sweep. Therefore the full 41-point sigma sweep, T4 across all dwell values, and robustness across the preregistered sigma subset remain outstanding. The pilot's own overall decision remains **NON DIMOSTRATA** because T1 did not find a second stable fixed point and T2/T3/T4/robustness are not complete at their full prescribed scope. The local NLT hysteresis signal is evidence for initial-condition separation, not proof of two stable attractors or bistability.

### fullerene-c64-audit

| PR | Title | State | CI | Assessment |
|---|---|---|---|---|
| #1 | C64 fullerene computational audit | OPEN, mergeable | **No CI configured** | `c64-audit`→`main`, +46,885/−1 (bulk is data/logs under `data/`). Self-contained repo; acceptance tests exist (`tests/test_audit.py`, reported 11 pass locally). Large diff is mostly generated artifacts — acceptable for an audit-data repo but consider whether `data/` logs belong in git. **Recommend: merge after owner confirms artifact policy; optionally add a minimal CI running `pytest tests/test_audit.py`.** |

### rheomarine — verification result

PRs **#20, #21, #22 are MERGED** into `main` (`eca7b9a`, verified 2026-11-26): Eulerian `wet`/`active`/`open_edges` solver + `qc_holes` policy, HFR input recovery/reproduction record, and status docs are all on main. Suite: 64 tests (45 baseline preserved). No action needed.

## Verified merged (results preserved)

- theorem **#344** (SE(3) tetrahedral defect fixture, merged 2026-11-21), **#131** (Volterra dipole-to-edge elastic limit, merged 2026-11-11), **#232** (T103/T105/T107 Actions hardening, merged 2026-11-12) — all MERGED; content present on main.
- theorem recent merges #413–#523 cover Q6/TSMR/Jitterbug/FEEC, geometry, graph inventory, In2Infinity, C60, T124, Q6 many-body/Berry and T099 reproducibility (see REPOSITORY_MAP.md).

## Closed-unmerged PRs

theorem: historical closed-unmerged count from the 2026-11-26 audit is not refreshed here. rgs-qlg: historical count 10. No cleanup action authorized.

## Open issues

- **theorem (10):** #409 Jitterbug eight-panel coupling; #402 unified theorem graph expansion; #401 64-TG/FCC-D3→Jitterbug immersion; #400 Cartan torsion/coframe; #399 mixed frame field A_a{}^m; #398 Vesica phase↔Jitterbug frame map; #114 JA vs measured loops; #113 actuator hysteresis fit; #109 188D/Krist-All source-data import; #84 Q6–D5 Wilson integer fibre port.
- **rgs-qlg:** #3 QLG gauge-equivariant roadmap.
- **kilaw:** #1 "this is the repo" (trivial — close candidate).
- **rheomarine:** #2 HFR–M0 (open by design; validation gates DATA-BLOCKED).

## Branch hygiene

- theorem: historical census recorded ~393 branches; branch count not refreshed in this pass. Recommend an owner-approved branch audit (list → confirm → delete) rather than blanket deletion.
- rgs-qlg: ~200 branches vs 1 open issue, 0 open PRs → same recommendation.
- rheomarine: 21 branches ≈ merged PR heads; candidates for cleanup after confirmation.
- fullerene-c64-audit: 2 branches (main + c64-audit) — clean.
