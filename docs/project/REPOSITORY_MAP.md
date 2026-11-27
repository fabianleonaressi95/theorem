# Repository map — fabianleonaressi95 (audit 2026-11-26)

## theorem (canonical mathematics)

- **HEAD:** `main` @ `38d139c` ("Update T149 index after T155 connection construction", 2026-11-26). CI on main: latest runs green.
- **Scale:** ~85 MB, 1,419 files at depth-1 clone; **428 merged PRs**, 29 closed unmerged, **5 open PRs** (#471, #476, #477 draft, #478 draft, #479 — see PR_ISSUE_AUDIT.md); **10 open issues** (#84, #109, #113, #114, #398–#402, #409); **~393 branches** (large stale-branch accumulation — see PR_ISSUE_AUDIT.md).
- **Key directories:** `docs/` (~120 audit/theorem notes), `theorems/`, `models/`, `experiments/`, `scripts/`, `tests/`, `reports/`, `research/`, `applications/`, `manuscripts/`, `monographs/`, `bibliography/`, `data/`, `evidence/`, `verification/`.
- **Root hygiene (resolved 2026-11-26):** root cleaned — `.pyc`/`__pycache__` removed, `" (N)"` duplicates deleted or archived, loose `.npy`/`.npz` → `artifacts/`, `.zip` → `archive/`, K0 JSON reports → `audits/`, legacy `dec_se3` package + orphan root tests → `archive/dec_se3_legacy/`, orphan C60 driver scripts → `archive/orphan_scripts_2026-11-26/`, T-* spec docs → `theorems/`, `Hysteresis_datasets.xlsx` → `data/`, PDFs → `bibliography/`. See reorganization audit report.
- **Recent merged work (2026-11-24→26):** Q6/Walsh filtration, TSMR/Jitterbug Green–Kubo, Q6–PRISM obstruction programme, Q6–C60 equivariance, Pellis D6 decomposition, RGS Killing geometry, Q4–Q6 NL/NLT audits, Jiles–Atherton local identifiability, supergolden dodecahedral Whitney–Hodge (T149 FEEC).

## rgs-qlg-quaternion-bridge (QLG/quaternionic track)

- **HEAD:** `main`; CI "RGS-QLG Quaternion Bridge — Full Audit" + "Python tests" green on recent runs.
- **Scale:** 90 merged PRs, 10 closed, 1 open issue (#3 QLG roadmap), **~200 branches**.
- **Key directories:** `docs/` (~100 notes incl. `UNIFIED_THEOREM_DEPENDENCY_GRAPH.md`, `UNIFIED_THEOREM_EDGES.json`, Kathara/Q6 audits, WYLER theorems, flat-torus G-series, FSS protocol), `src/`, `tests/`, `experiments/`, `papers/`, `references/`, `reports/`, `PROVENANCE_STATUS.json`, `RGS_PSU_FILE_INVENTORY.json`.
- **Overlap with theorem:** Q6 lattice, RGS/PSU, Pellis, Jitterbug-adjacent topics appear in both repos — see OPEN_WORKSTREAMS.md for canonical-ownership proposal.

## rheomarine (applied transport modelling)

- **HEAD:** `main` @ `eca7b9a` — PRs #20 (Eulerian wet/QC-barrier/open-edge solver), #21 (HFR pilot input recovery + bit-identical reproduction), #22 (status docs) **all merged 2026-11-26**; verified on `origin/main`.
- **State:** 21 merged PRs, 0 open. Suite 64/64 locally + CI. Raw HFR inputs published as release `hfr-m0-pilot-inputs-2026-11-25`.
- **Status:** Lagrangian pilot PILOT-REPRODUCED; independent validation DATA-BLOCKED (issue #2 open).

## fullerene-c64-audit

- **HEAD:** default branch `c64-audit`; **PR #1 OPEN** (`c64-audit`→`main`, +46,885/−1, mergeable, **no CI checks configured**).
- Contents: `scripts/fullerene_lib.py`, `scripts/run_audit.py`, `scripts/sw_benchmark_c60.py`, `tests/test_audit.py`, `results/C64/*`, `docs/C64_FULLERENE_COMPUTATIONAL_AUDIT.md`, `docs/KRIST_ALL_KATHARA_Q6_INTERFACE.md`, plantri/fullgen data + logs.
- Claims (per PR body): 3,465 C64 isomers enumerated, cross-validated vs Massey CTCP; Hückel spectra; nauty orbits; SW graph 8,550 links/70 components; C60 benchmark 1,710-isomer component. Krist-All/Q6 interface explicitly conjectural.

## Smaller / stale repositories

| Repo | HEAD | Content | Notes |
|---|---|---|---|
| `biverse` | `main` | README only | Claims PSU/Anti-Twin Yang–Mills gap "formal proof" — **no code, no proof document found; claim quarantined as HYPOTHESIS until substantiated** |
| `naressi-golden-resonance` | `main` | `naressi_law.py`, `golden/`, `mu/`, `simulation.json`, Italian README | Golden-ratio photon–phonon coupling; last activity 2026-09-08 |
| `naressi-zuliani-law-quantum-morphodynamics` | `main` | `toy_monte_carlo.py`, `montecarlo.png`, requirements | Toy MC only |
| `quantum-lindblad` | `main` | `main_simulation.py`, `download.py`, `ecoli_cds_data.txt` | Lindblad + ecoli data; last 2026-09-13 |
| `q-proof` | `main` | `simulazione{3,6,8,11,14,19,21,22}.py` | Unstructured scripts; 2 branches |
| `kilaw` | `main` | `algebra/`, `morphodynamic/`, `quantum/`, `naressilaw/`, `krasilnikov*`, figures, notebooks | Krasilnikov morphodynamics; issue #1 trivial; last 2026-10-30 |
| `ASTRAQ` | `main` | `astraq_engine.py`, SSA scripts, scaling-law analysis, streamlit app | SSA demonstrator + RG-flow analysis; last 2026-08-25 |
| `cosmodex` | `main` | Galaxy-map app, gradle/android files, `node_modules`, `android.keystore`, 153 MB | Hygiene: keystore + node_modules committed; last 2026-07-28 |
| `cosmodex-pwa` | — | empty | unused |
| `astra-q-core` | — | empty | unused |
