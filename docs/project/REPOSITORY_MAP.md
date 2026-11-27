# Repository map — fabianleonaressi95 (audit 2026-11-27)

## theorem (canonical mathematics)

- **HEAD:** `main` @ `0b5e7b23` (T157 numerical-table synchronization, 2026-11-27), latest commit returned by repository commit search at audit time.
- **Scale:** ~85 MB and 1,419 files are the previous depth-1 census (not remeasured). Live PR search (2026-11-27): **3 open PRs** (#518, #519, and this registry update #522); 10 open issues (#84, #109, #113, #114, #398–#402, #409). Merged-PR, closed-unmerged, and branch totals are deliberately not repeated: the available search result is capped and no complete branch census was run.
- **Key directories:** `docs/` (~120 audit/theorem notes), `theorems/`, `models/`, `experiments/`, `scripts/`, `tests/`, `reports/`, `research/`, `applications/`, `manuscripts/`, `monographs/`, `bibliography/`, `data/`, `evidence/`, `verification/`.
- **Root hygiene problems (documented, not yet fixed):** committed `__pycache__`/`.pyc` files, duplicate `" (1)"`/`" (2)"` filenames (`README (6).md` … `README (8).md`, `bianchi (1).py`, `test_*.py` duplicates), loose `.npy`/`.npz`/`.zip` artifacts at root. Cleanup candidate — preserve before deleting.
- **Recent merged work (2026-11-26→27):** registry sync (#480), Ellis circumcentric audit cleanup (#487), live theorem-graph inventory repair (#508; 263 theorem records, 317 nodes, 353 directed edges), updated Ellis circumcentric audit (#514), T156 incidence audit (#516), In2Infinity T154/T155 source and transition work (#517), and T157 covariant Whitney curvature construction, regression test, workflow and numerical report. The T157 model explicitly retains a nonzero curvature defect and is not identified with a smooth continuum connection.

## rgs-qlg-quaternion-bridge (QLG/quaternionic track)

- **HEAD:** `main`; CI "RGS-QLG Quaternion Bridge — Full Audit" + "Python tests" green on recent runs.
- **Scale:** 90 merged PRs, 10 closed, 1 open issue (#3 QLG roadmap), **~200 branches**.
- **Key directories:** `docs/` (~100 notes incl. `UNIFIED_THEOREM_DEPENDENCY_GRAPH.md`, `UNIFIED_THEOREM_EDGES.json`, Kathara/Q6 audits, WYLER theorems, flat-torus G-series, FSS protocol), `src/`, `tests/`, `experiments/`, `papers/`, `references/`, `reports/`, `PROVENANCE_STATUS.json`, `RGS_PSU_FILE_INVENTORY.json`.
- **Overlap with theorem:** Q6 lattice, RGS/PSU, Pellis, Jitterbug-adjacent topics appear in both repos — see OPEN_WORKSTREAMS.md for canonical-ownership proposal.

## rheomarine (applied transport modelling)

- **HEAD:** `main` @ `eca7b9a` — PRs #20 (Eulerian wet/QC-barrier/open-edge solver), #21 (HFR pilot input recovery + bit-identical reproduction), #22 (status docs) **all merged 2026-11-26**; verified on `origin/main`.
- **State:** PRs #20–#22 remain merged; live open-PR search returned none. The earlier 21-merged-PR total and 64/64 suite result are retained as the 2026-11-26 audit, not independently recounted in this pass. Raw HFR inputs published as release `hfr-m0-pilot-inputs-2026-11-25`.
- **Status:** Lagrangian pilot PILOT-REPRODUCED; independent validation DATA-BLOCKED (issue #2 open).

## fullerene-c64-audit

- **HEAD:** default branch `c64-audit`; **PR #1 remains OPEN** (`c64-audit`→`main`); no CI checks were reported in the previous audit. Current open-PR search confirms it remains open.
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
