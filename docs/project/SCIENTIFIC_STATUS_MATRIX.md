# Scientific status matrix — 26 November 2026

Conservative labeling. "Per repo" = claimed in that repository's own audit documents with passing CI; it is NOT independent verification. Nothing below is upgraded on the basis of code/CI alone.

| # | Topic / claim | Canonical repo | Status | Evidence pointer | Caveat |
|---|---|---|---|---|---|
| 1 | HFR→Lagrangian M0 pilot (IZOL/PIRA 7d) | rheomarine | **PILOT-REPRODUCED** (K=0 sensitivity only) | `docs/hfr/M0_PILOT_REPRODUCED…` → `M0_PILOT_REPRODUCTION_2026-11-26.md`, release `hfr-m0-pilot-inputs-2026-11-25` | not physical validation |
| 2 | Eulerian solver masks/open boundaries | rheomarine | **SOFTWARE VERIFIED** | PR #20 merged; `tests/test_eulerian_boundaries.py`; 64/64 CI | coastline mask still caller-supplied |
| 3 | Independent transport validation | rheomarine | **BLOCKED** | validation gate §8 data requests | no observations in hand |
| 4 | Q6 lattice / Wilson / D5 fibre | theorem + rgs-qlg | ANALYTICALLY VERIFIED + NUMERICALLY VERIFIED (per repo) | `docs/Q6_*`, `rgs-qlg/docs/RGS_Q6_*` | issue #84 port OPEN |
| 5 | Q6–PRISM correspondence/obstructions | rgs-qlg | NUMERICALLY VERIFIED (per repo, PRs #207–213) | merged PRs | — |
| 6 | PSU–Anti-Twin Q-ball | rgs-qlg | NUMERICALLY VERIFIED (PR #220) | merged | — |
| 7 | Yang–Mills gap via PSU/Anti-Twin | biverse | **HYPOTHESIS** (quarantined) | README claim only; no artifact | needs proof or archive |
| 8 | SE(3) tetrahedral defects / Bianchi | theorem | SOFTWARE VERIFIED (PRs #344, #461 merged) | `se3.py`, tests | torsion Bianchi OPEN (#400) |
| 9 | Volterra dipole→edge elasticity | theorem | NUMERICALLY VERIFIED (PRs #131, #450 merged) | merged | — |
| 10 | Cartan torsion / frame field laws | theorem | OPEN | issues #398–#400 | — |
| 11 | Vesica/Jitterbug geometry + immersion | theorem | NUMERICALLY VERIFIED (kinematics); immersion OPEN | `docs/VESICA_*`, `JITTERBUG_*`; issues #401/#409 | — |
| 12 | 2I / Poincaré / McKay | theorem + rgs-qlg | ANALYTICALLY VERIFIED (per repo; PR #444) | merged docs | — |
| 13 | FEEC/DEC/Hodge spectral (T149 etc.) | theorem | SOFTWARE + NUMERICALLY VERIFIED | workflows green on main | — |
| 14 | Mosco/graph Γ-limit | rgs-qlg + theorem | ANALYTICALLY VERIFIED (per repo) | `FLAT_TORUS_G6_P1_MOSCO_PROOF.md`, PR #451 | — |
| 15 | Rumin/Kitaoka spectral geometry | theorem | PARTIALLY MAPPED | `K0_SPECTRAL_*` audits | needs dedicated inventory |
| 16 | Lindblad / FSS | rgs-qlg (FSS) + quantum-lindblad (stale) | SOFTWARE VERIFIED (rgs-qlg); quantum-lindblad STALE | `FSS_FIB_PROTOCOL.md`, PR #232 | canonical home undecided |
| 17 | C60 fullerene audits | theorem | NUMERICALLY + SOFTWARE VERIFIED (PR #449 merged) | `docs/C60_*`, SW audit scripts | MMFF94s proxy ≠ DFT |
| 18 | C64 enumeration/SW graph | fullerene-c64-audit | NUMERICALLY VERIFIED (per PR #1; no CI) | `results/C64/*` | PR #1 unmerged |
| 19 | Fullerene↔Q6/Kathara | theorem + fullerene | HYPOTHESIS | `KRIST_ALL_KATHARA_Q6_INTERFACE.md` | explicitly conjectural |
| 20 | Hysteresis (188D/JA/actuator) | theorem | NUMERICALLY VERIFIED (per repo; PR #452) | `Hysteresis_datasets.xlsx`, issues #113/#114 open | — |
| 21 | Naressi golden-resonance / morphodynamics | naressi-* repos | SOFTWARE (toy sims) — STALE | repo scripts | unverified claims in READMEs |
| 22 | SSA + scaling laws | ASTRAQ | SOFTWARE VERIFIED — STALE | repo scripts | — |
| 23 | CosModex | cosmodex | SOFTWARE — STALE | repo | hygiene: keystore/node_modules committed |
| 24 | Shape–Field electrostatic discharge FEM | `theorem` (protocol) | OPEN — protocol only, no results | `docs/SHAPE_FIELD_CADFEM_ELECTROSTATIC_PROTOCOL_2026-11-26.md` | CADFEM/Fuger ref; RGS link exploratory |

**Explicit non-claims:** no item above is EXPERIMENTALLY VALIDATED except where a repo documents an actual comparison with independent measurements (none found for transport; rheomarine lab datasets are calibration inputs, not field validation). All "per repo" numerical claims await the owner's confirmation before external citation.
