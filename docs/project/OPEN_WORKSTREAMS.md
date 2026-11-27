# Open workstreams registry — 27 November 2026

Maps each active research thread to its canonical repository, key files, verification status, missing work and dependencies. Statuses are conservative: "per repo docs/CI" means the repository's own audit documents claim the result and CI passes; it does not constitute independent re-verification.

## A. Quantum Morphodynamics / RGS / PSU / Anti-Twin / biverse

| Thread | Canonical repo | Key locations | Status | Missing / dependencies |
|---|---|---|---|---|
| RGS–PSU operator lineage, K0 audits, 188D provenance | `theorem` (+ `rgs-qlg` for QLG side) | `theorem/docs/RGS_*`, `K0_*.json`, `rgs-qlg/docs/RGS_*` | NUMERICALLY VERIFIED (per repo audits); PROVED only where a formal doc exists | issue #109: 188D/Krist-All source-data import incomplete |
| PSU + Anti-Twin two-field Q-ball | `rgs-qlg` | PR #220 merged (symmetric PSU–Anti-Twin Maxwell BVP) | SOFTWARE VERIFIED / NUMERICALLY VERIFIED per repo | biverse README claims Yang–Mills gap "formal proof" — **no supporting artifact found in `biverse`; quarantined as HYPOTHESIS pending substantiation** |
| Möbius biverse / PSU spherical units | `biverse` | README only | HYPOTHESIS (claim quarantined) | needs actual proof document or code; otherwise archive repo |
| Q6–NL/NLT T1–T4 hysteresis protocols | `theorem` | `docs/Q6_NL_NLT_T1_T2_PROTOCOL_2026-11-09.md`, `scripts/run_qn_nl_nlt_t3_t4.py`, PR #477 merged | SOFTWARE VERIFIED (merged software/protocol artifacts; scientific robustness remains separately bounded) | complete outstanding T3/T4 and robustness execution records; do not infer bistability from script presence |
| Morandotti defect benchmark (Torino) | `theorem` | `docs/rgs_defect_benchmark/`, PR #458 merged; follow-on remeshing audit #501 merged | SOFTWARE VERIFIED (benchmark artifacts integrated) | retain the distinction between reproducible benchmark results and any physical/continuum claim |

## B. Q6 / QLG / PRISM / Krist-All / Kathara

| Thread | Canonical repo | Key locations | Status | Missing |
|---|---|---|---|---|
| Q6 lattice gauge / Wilson / D5 integer fibre | `theorem` + `rgs-qlg` (shared) | `theorem/docs/Q6_*` (~30 notes), `rgs-qlg/docs/RGS_Q6_*`, `KATHARA_*` | ANALYTICALLY VERIFIED + NUMERICALLY VERIFIED per repo audits | **issue #84: port & certify Q6–D5 Wilson integer-fibre computation in THEOREM — OPEN** |
| Q6–PRISM obstruction programme | `rgs-qlg` (PRs #207–#213 merged) | `rgs-qlg/docs` PRISM/Q6 bridge notes | NUMERICALLY VERIFIED (obstructions proved per repo) | issue #402 unified theorem graph expansion OPEN |
| Krist-All / Kathara chain maps | `theorem` + `rgs-qlg` + `fullerene-c64-audit` (interface doc) | `rgs-qlg/docs/KATHARA_*`, `theorem/docs/KTHNY_N4_SYM_RGS_PRISM.md`, fullerene `docs/KRIST_ALL_KATHARA_Q6_INTERFACE.md` | CANDIDATE — interface explicitly conjectural | issue #109 source-data import; fullerene PR #1 unmerged |
| Pellis Fibonacci two-sheet / D6 | `rgs-qlg` + `theorem` | `rgs-qlg` PRs #223–#226, `theorem/docs/PELLIS_*` | NUMERICALLY VERIFIED per repo | — |
| Supergolden special functions / dodecahedral Hodge | `theorem` | PRs #460, #451 merged; `docs/DIGAMMA_SUPERGOLDEN_*` | SOFTWARE VERIFIED | — |

## C. Geometry / defects / elasticity / Cartan–SE(3)

| Thread | Canonical repo | Key locations | Status | Missing |
|---|---|---|---|---|
| SE(3) connection, tetrahedral defects, Bianchi | `theorem` | `se3.py`, `test_se3_connection.py`, PRs #344, #461 merged; issue #400 torsion OPEN | SOFTWARE VERIFIED | torsion Bianchi + deWit/Nye identification OPEN |
| Volterra dipole→edge dislocation elasticity | `theorem` | PRs #131, #450 merged; PR #479 merged (C0-IPDG comparison manuscript) | NUMERICALLY VERIFIED | PR #479 review pending |
| Cartan torsion / mixed frame field / Vesica–Jitterbug phase map | `theorem` | issues #398, #399, #400 | OPEN | derivations not started |
| Vesica Piscis / Jitterbug / 64-TG immersion | `theorem` | `docs/VESICA_*`, `JITTERBUG_*`, issues #401, #409 | NUMERICALLY VERIFIED (kinematics); immersion OPEN | #401, #409 open |
| 2I / Poincaré quotient / McKay correspondence | `theorem` + `rgs-qlg` | `theorem/docs/binary-icosahedral-2i.md`? (rgs-qlg `docs/binary-icosahedral-2i.md`), PR #444 (binary McKay–ADE) | ANALYTICALLY VERIFIED per repo | — |

## D. Spectral / FEEC / discretization / statistical mechanics

| Thread | Canonical repo | Key locations | Status | Missing |
|---|---|---|---|---|
| FEEC exterior calculus, DEC, Hodge, T149 dodecahedron | `theorem` | `test_volumetric_complex.py`, `holonomy.py`, `connection.py`, PR #460/#445 | SOFTWARE VERIFIED + NUMERICALLY VERIFIED | — |
| Mosco convergence / graph Γ-limits | `rgs-qlg` (PR #230 formalization) + `theorem` PR #451 | `rgs-qlg/docs/FLAT_TORUS_G6_P1_MOSCO_PROOF.md`, `theorem` PR #451 | ANALYTICALLY VERIFIED per repo | — |
| Rumin / Kitaoka / spectral geometry | `theorem` (DEC/spectral zeta in description) | search `theorem/docs` for spectral notes; `K0_SPECTRAL_*` audits | PARTIALLY MAPPED — needs dedicated inventory pass | dedicated sub-audit recommended |
| Quantum Lindblad / FSS | `quantum-lindblad` (stale) + `rgs-qlg` (`FSS_FIB_PROTOCOL.md`, Fibonacci Aubry–André PR #232) | split across repos | SOFTWARE VERIFIED in rgs-qlg; `quantum-lindblad` repo STALE | decide canonical home for Lindblad work; consider archiving `quantum-lindblad` |

## E. Fullerenes / molecules

| Thread | Canonical repo | Status | Missing |
|---|---|---|---|
| C60 audits (TH comparison, Coulomb, DPO, local defects, Stone–Wales) | `theorem` (`docs/C60_*`, PR #449 merged) | NUMERICALLY VERIFIED + SOFTWARE VERIFIED | PR #449 pending |
| C64 enumeration/audit | `fullerene-c64-audit` | NUMERICALLY VERIFIED (per PR #1 body; tests reported passing; **no CI**) | PR #1 unmerged; add CI |
| Fullerene↔Q6/Kathara interface | `theorem` + `fullerene-c64-audit` doc | HYPOTHESIS (explicitly conjectural) | needs theorem + data bridge |

## F. Experimental / applied

| Thread | Canonical repo | Status | Missing |
|---|---|---|---|
| RheoMarine HFR–M0 transport | `rheomarine` | PILOT-REPRODUCED (Lagrangian); solver masks SOFTWARE VERIFIED; validation DATA-BLOCKED (issue #2) | independent ADCP/drifter/particle observations; coastline mask; longer HFR windows |
| DS1/DS2 lab rheology analysis | `rheomarine` | ANALYZED (derived CSVs/JSON committed) | absolute z-calibration for DS1; DS2 recipes |
| Hysteresis datasets (188D, JA, actuator) | `theorem` (`Hysteresis_datasets.xlsx`, `INDUSTRIAL_HYSTERESIS_DATASETS.md`, PR #452) | NUMERICALLY VERIFIED per repo | issues #113, #114 open |
| Shape–Field / electrostatic discharge FEM | `theorem` (protocol); dedicated app repo TBD | `docs/SHAPE_FIELD_CADFEM_ELECTROSTATIC_PROTOCOL_2026-11-26.md` (CADFEM/Fuger 2026-04-10 reference) | OPEN — protocol only | FEM implementation, §8 verification tests, inception-voltage module |
| SSA / scaling laws | `ASTRAQ` | SOFTWARE VERIFIED (stale since Aug) | — |
| CosModex galaxy map | `cosmodex` | SOFTWARE (stale; hygiene issues) | — |

## G. Orphaned / unassigned

- `naressi-golden-resonance`, `naressi-zuliani-law-quantum-morphodynamics`, `q-proof`, `kilaw`, `quantum-lindblad`: small stale repos whose topics overlap the Naressi-law/morphodynamics threads. No canonical mapping to theorem topics found — recommend owner review: either link into the registry or archive.
- `biverse`: single-README Yang–Mills claim — quarantine pending evidence.
- `astra-q-core`, `cosmodex-pwa`: empty — archive candidates.

## Cross-cutting dependencies

- `theorem` ↔ `rgs-qlg`: heavy topical overlap (Q6, RGS, PSU, Pellis). Risk of divergent duplicate formulations — canonical-ownership rule proposed in MASTER_PROJECT_REGISTRY.md.
- `fullerene-c64-audit` → `theorem`/`rgs-qlg`: C64 data feeds C60/Q6-equivariance theorems; interface currently conjectural.
- `rheomarine` ↔ `theorem`: independent tracks (applied vs pure math); Morandotti microswimmer note already cross-references appropriately.
