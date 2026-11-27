# Master project registry — fabianleonaressi95

**Audit date:** 27 November 2026
**Scope:** all accessible repositories of `fabianleonaressi95` (public and private), reconciled with the active research threads.
**Rule:** repository organization is not scientific proof. Status labels below are evidence classes, not quality judgments; see `SCIENTIFIC_STATUS_MATRIX.md` for per-topic detail.

## Status label definitions

| Label | Meaning |
|---|---|
| PROVED | Formal proof exists in-repo or in cited literature, verified by audit |
| ANALYTICALLY VERIFIED | Derivation checked analytically; residual assumptions documented |
| NUMERICALLY VERIFIED | Computation reproduces documented reference values |
| SOFTWARE VERIFIED | Code/tests/CI pass; says nothing about physical truth |
| EXPERIMENTALLY VALIDATED | Compared against independent real measurements |
| CANDIDATE | Promising result awaiting verification |
| HYPOTHESIS | Stated conjecture, not yet tested |
| OPEN | Work identified but not started or incomplete |
| BLOCKED | Cannot proceed without external data/decision |

## Repository census

| Repository | Visibility | Default branch | Purpose / canonical role | Status |
|---|---|---|---|---|
| `theorem` (formerly `theroem` — GitHub redirect confirmed) | public | `main` | **Canonical home for theorem-level mathematics**: Q6/QXL/QLG, RGS, PSU/Anti-Twin, Vesica/Jitterbug, SE(3)/Cartan, C60/fullerenes, FEEC/discretization, hysteresis datasets. Live PR check (2026-11-27): three open research PRs (#524, #525, #526); registry reconciliation PR to be opened after this update; merged-PR and branch totals are not restated because the search result is capped. 10 open issues | ACTIVE — consolidation target |
| `rgs-qlg-quaternion-bridge` | public | `main` | Quaternionic SU(2)/SO(3), lattice holonomies, QLG gauge-equivariant operators, Wilson/Kirchhoff fluid audits, Pellis/Q6 programme. 90 merged PRs, ~200 branches | ACTIVE — overlaps theorem on Q6/RGS topics |
| `rheomarine` | public | `main` | Microplastic transport modelling: HFR ingestion (IZOL/PIRA), Lagrangian + Eulerian M0, lab datasets DS1/DS2, RISTANC application support. 21 merged PRs | ACTIVE — applied/experimental track |
| `fullerene-c64-audit` | private | `c64-audit` | Reproducible enumeration/analysis of all 3,465 C64 fullerene isomers (plantri/fullgen, Hückel, nauty, Stone–Wales graph) | ACTIVE — PR #1 open |
| `biverse` | private | `main` | PSU + Anti-Twin → Yang–Mills gap claim (README only, size ~0) | STUB — claim quarantined, no implementation found |
| `naressi-golden-resonance` | private | `main` | Naressi Quantum Field Law: golden-resonance photon-phonon coupling simulation (Italian docs) | STALE (last push 2026-09-08) |
| `naressi-zuliani-law-quantum-morphodynamics` | private | `main` | Monte-Carlo toy simulation related to quantum morphodynamics | STALE (2026-07-21) |
| `quantum-lindblad` | private | `main` | Lindblad simulation + ecoli CDS data | STALE (2026-09-13) |
| `q-proof` | private | `main` | Loose simulation scripts (`simulazione*.py`) | STALE (2026-10-29) |
| `kilaw` | private | `main` | Krasilnikov/Killa morphodynamic algebra, entanglement, figures, CSV scans | STALE (2026-10-30); 1 trivial open issue |
| `ASTRAQ` | private | `main` | SSA demonstrator + universal scaling-law/perturbation analysis (Streamlit) | STALE (2026-08-25) |
| `cosmodex` | private | `main` | CosModex galaxy map / PWA-ish app (153 MB repo, includes node_modules, android.keystore, .gradle) | STALE (2026-07-28); hygiene issues |
| `cosmodex-pwa` | private | — | **EMPTY repository** | UNUSED |
| `astra-q-core` | private | — | **EMPTY repository** | UNUSED |

**Total: 14 repositories: 12 non-empty and 2 empty.** `theroem` is not a separate repository — it is the pre-rename name of `theorem` (GitHub API redirect verified 2026-11-26).

## Canonical ownership rules (proposed)

1. **Theorem mathematics** (statements, proofs, audits, dependency graphs): canonical in `theorem`. `rgs-qlg-quaternion-bridge` keeps its quaternionic/QLG-specific proofs but must cross-reference `theorem` identifiers rather than redefining them.
2. **Experimental/software artifacts** (HFR data pipelines, lab datasets, apps): stay in their own repos (`rheomarine`, `ASTRAQ`, `cosmodex`, `kilaw`, `quantum-lindblad`, `q-proof`, `naressi-*`).
3. **Fullerene enumeration data**: canonical in `fullerene-c64-audit`; theorem keeps theorem-level consequences (C60 audits, Q6–C60 equivariance) and cites the audit repo.
4. **Empty repos** (`astra-q-core`, `cosmodex-pwa`): archive or delete candidates — owner decision required.

See `REPOSITORY_MAP.md`, `OPEN_WORKSTREAMS.md`, `PR_ISSUE_AUDIT.md`, `SCIENTIFIC_STATUS_MATRIX.md`.
