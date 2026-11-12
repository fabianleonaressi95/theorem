# THEOREM — RGS–PSU–PRISM–Q6 Mathematical Research Programme

**THEOREM** is the central research repository for a structured programme in discrete geometry, spectral analysis, gauge theory, spin geometry, quantum-light models, and mathematical physics.

It brings together source literature, manuscript records, reproducible computational audits, theorem statements, model implementations, and explicitly tracked open problems. The repository is intended to make each mathematical claim traceable to its assumptions, derivation, implementation, and verification status.

> **Scientific-status policy.** A symbolic proof, a numerical verification, a model-dependent conclusion, and a research hypothesis are different kinds of evidence. This repository labels them separately and does not treat computational agreement as a substitute for proof or physical validation.

## Research scope

The main research strands include:

- **RGS–PSU–PRISM:** discrete geometric structures, variable-space limits, Dirichlet forms, Hodge operators, and candidate continuum descriptions.
- **Q6 and QLG:** the 64-state six-bit configuration space, its graph and cell structures, discrete Dirac constructions, and the question of how quaternionic or two-component fibres can be related to Lorentzian spinors.
- **Binary icosahedral geometry:** the group (2I), its irreducible representations, the Poincaré quotient (S^3/2I), and Rumin-type spectral and analytic-torsion calculations.
- **Gauge theory and QFT:** Wilson operators, gauge-covariant discrete operators, QCD-related constructions, and continuum-resolvent questions.
- **Einstein–Cartan and teleparallel gravity:** algebraic torsion, spin currents, Weyssenhoff-fluid assumptions, and the distinction between phenomenological closures and field-equation-derived results.
- **Quantum-light and emergent-spacetime foundations:** a critical mathematical review of candidate geometric models, with conjectural physical interpretations kept separate from established results.

These strands are connected only where an explicit mathematical map, shared operator, or derivation is available. Similar terminology or numerical coincidences alone do not establish equivalence.

## Repository map

The tree below summarizes the principal areas. The live repository may contain additional scripts, data, tests, and theorem records.

```text
theorem/
├── .github/workflows/       # Continuous-integration workflows
├── archive/                 # Quarantined source files retained for provenance
├── audits/                  # Reproducible mathematical/computational audits
├── bibliography/             # Source literature and formula audits
├── data/                    # Machine-readable data and audit outputs
├── docs/                    # User and research documentation
├── models/                  # Explicit mathematical and phenomenological models
├── open-problems/           # Validation matrices and unresolved questions
├── projects/                # Research-strand index
├── scripts/                 # Executable research and verification scripts
├── tests/                   # Automated tests
└── theorems/                # Numbered theorem statements and proof records
```

### Main indexes

- **[Ricostruzione dalle fondamenta](monographs/00_FROM_FIRST_PRINCIPLES_LIGHT_CUBE_SPHERE_PHI_PSU_QAT.md)** — luce e unità di Planck, cubo-sfera, derivazione π→φ, icosaedro/quaternioni/2I, PSU–Anti-Twin, Q-ball, QAT e interfaccia Calabi–Yau. È il punto di partenza della ricostruzione; Q6 e PRISM vengono dopo.

- [Morandotti benchmark I — discrete Saint-Venant KKT specification](manuscripts/MORANDOTTI_BENCHMARK_I_DISCRETE_SAINT_VENANT_KKT.md) — finite-dimensional constrained energy, implemented generic KKT solver and energy assembly, D1–D3 defect tests and Airy/CIP-DG comparison gates; CI execution, continuum convergence and physical validation remain open.
- **[Integrated 27-chapter monograph](monographs/RGS_PSU_PRISM_Q6_QLG_MONOGRAPH_27_CHAPTERS.md)** — consolidated reference for Q6, Q6-D5/Wilson, 2I/Rumin, RGS 188D, PRISM/Krist-All, FEEC/Mosco, QLG, Einstein–Cartan/teleparallelism, QAT, XCont and hysteresis. Includes explicit epistemic status and recovery caveats.
- [Canonical synthesis and closure programme](manuscripts/SINTESI_CANONICA_RGS_PSU_PRISM_Q6_QLG.md) — short strategic overview.

- [Bibliography and source catalogue](bibliography/README.md)
- [Special functions and Morandotti bibliography](bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md)
- [Repository PDF inventory and source audit (13 PDFs)](audits/2026-11-10_pdf_repository_audit.md)
- [Unitary theory: truncated-icosahedral shell, Gamma–Beta–zeta, Morandotti and RGS–PRISM–Q6](docs/UNIFIED_THEORY_FOOTBALL_GAMMA_BETA_ZETA_MORANDOTTI_RGS_PRISM_Q6_2026-11-10.md) — canonical dependency map for all 10 November results, including the football geometry, barycentric moments, special functions, phases, fourth moments, Q6 and spherical spectra.
- [Integrated synthesis: moments, barycentres, Gamma–Beta–zeta and Morandotti](docs/SYNTHESIS_MOMENTS_BARYCENTRES_GAMMA_BETA_ZETA_MORANDOTTI_2026-11-10.md)
- [Unified Dedekind–Dirichlet eta, Weber–supergolden, barycentric and RGS–Morandotti construction](docs/UNITARY_DEDEKIND_DIRICHLET_ETA_BARYCENTRIC_RGS_MORANDOTTI_2026-11-10.md) — integrates the exact modular/class-field bridge at discriminant −31 with Dirichlet (L)-functions, Beta/Gamma cumulants, barycentric quadrature, Q6 and fourth moments.
- [10 November independent numerical replay report](reports/2026-11-10_integrated_synthesis_numerical_replay.md) — seed moments, Walsh sectors, Duffy–Jacobi checks, fourth-moment variations and Q6 cubical chain identities; explicitly not a pytest/CI pass.
- [Digamma–supergolden–Q6 analytic dossier](docs/DIGAMMA_SUPERGOLDEN_Q6_PROGRAM_2026-11-10.md)
- [Formula extraction register](bibliography/FORMULA_EXTRACTION_REGISTER.md)
- [Cleaned research notes and manuscript editorial register](manuscripts/README.md)
- [Toroidal unification: GEM–MHD–QHD and superconducting fluxons](research/GRAVITOMAGNETISM_MHD_QHD_FLUXON_BRIDGE.md) — treats the torus as the proposed common geometry for football-shell, Q-ball, FDT/QAT, PSU/Anti-Twin, QLG and field/fluid sectors; distinguishes superconducting Josephson fluxons from other topological winding defects and records the proof obligations.
- [XCont emergent-dynamics integration](manuscripts/XCONT_EMERGENT_DYNAMICS_INTEGRATION.md) — external cellular-automata, symbolic-billiard and graph-convolution methods mapped to PRISM/Q6 as testable research interfaces.
  - X6 symbolic rotation coding: [model](models/prism_billiard_coding.py), [JSON runner](scripts/run_prism_billiard_coding.py), [tests](tests/test_prism_billiard_coding.py), [research note](manuscripts/X6_SYMBOLIC_BILLIARD_CODING.md).
  - Implemented: [PRISM CA engine](models/prism_cellular_automata.py), [rule/initial-state genetic search](models/prism_ca_evolution.py), [single-run CLI](scripts/run_prism_ca_evolution.py), [multi-seed benchmark](scripts/run_prism_ca_benchmark.py), [two-population co-evolution CLI](scripts/run_prism_ca_coevolution.py), [regression tests](tests/test_prism_cellular_automata.py) / [GA and co-evolution tests](tests/test_prism_ca_evolution.py), and [dedicated CI workflow](.github/workflows/prism-ca.yml).
- [Inhomogeneous spin-chain model note](manuscripts/INHOMOGENEOUS_SPIN_CHAIN.md)
- [Scalar–torsion variational identity](manuscripts/SCALAR_TORSION_VARIATIONAL_IDENTITY.md)
- [Quarantined source files](archive/README.md)
- [External manuscript provenance notes](bibliography/source-bibliographies/)
- [Project map](projects/README.md)
- [S.9 — Three-phase rotating fields, Ferraris' two-coil construction, and the coframe/tetrad](theorems/S009-three-phase-ferraris-coframe-tetrad-bridge.md) — exact two-coil and three-phase rotating-field identities, coframe/tetrad component maps, electromagnetic field-strength decomposition, and explicit separation of electrical phase from spin connection; [finite audit](scripts/audit_s009_ferraris_tetrad_bridge.py).
- [T102 — Cubical supersymmetric quantum mechanics, heat supertrace and the Sakharov boundary](theorems/T102-cubical-supersymmetry-heat-kernel-sakharov.md) — exact cubical de Rham/Hodge complex on the six-cube, Q6 heat trace, finite-dimensional SUSY algebra and McKean–Singer supertrace; explicitly separates this result from N=4 SYM and leaves continuum Sakharov induction open. Reproducible audit: [script](scripts/audit_t102_cubical_susy_heat.py), [tests](tests/test_t102_cubical_susy_heat.py).
- [Notation policy: supergolden constant, special functions and GP field](docs/NOTATION_SUPERGOLDEN_SPECIAL_FUNCTIONS_GP.md) — reserves \\(\\psi_{\\rm SA}\\) for the supergolden constant and \\(\\Psi_{\\rm GP}\\) for the Gross–Pitaevskii order parameter; records the already-established Weber–Dedekind–digamma arithmetic network without conflating its objects.
- [T111 — GP order-parameter zeros and T110 plaquette-vortex refinement](theorems/T111-gp-zero-vortex-refinement.md)
- [T112 — Golden-ratio geometry and KTHNY defect lattices](theorems/T112-golden-ratio-kthny-defect-geometry.md) — exact golden unimodular map on Burgers coordinates, triangular-crystal control, coordinate-covariance null test, separate quasicrystal/phason gate, and falsifiable finite-size criteria; [audit](scripts/audit_t112_golden_kthny.py), [tests](tests/test_t112_golden_kthny.py).
- [T113 — Gravitational mass of phonon–phason modes in quasiperiodic media](theorems/T113-quasicrystal-phonon-phason-gravitational-mass.md) — published fluid/solid acoustic control and open metric-variation programme for coupled quasicrystal modes. [T113-A metric-action derivation](theorems/T113A-metric-action-phonon-phason-mode-sensitivity.md), [T113-D Q6/RGS phonon–internal-mode framework](theorems/T113D-q6-rgs-phonon-internal-mode.md), [T113-E Q6/RGS T2u stability](theorems/T113E-q6-rgs-t2u-triplet-stability.md) [Q6/RGS induced-symmetry audit](scripts/audit_t113d_q6_rgs_oh.py), [tests](tests/test_t113d_q6_rgs_oh.py), [T113-C generic icosahedral construction (superseded for this programme)](theorems/T113C-icosahedral-phonon-phason-elasticity.md), [T113-G cut-and-project symmetry and rank-two isotropy](theorems/T113G-cut-project-symmetry-rank-two-isotropy.md), [T113-G finite symmetry audit](scripts/audit_t113g_cut_project_symmetry.py), [isotropic-limit audit](scripts/audit_t113_quasicrystal_phonon_gravity.py), [tests](tests/test_t113_quasicrystal_phonon_gravity.py). — manufactured static unit-vortex benchmark, exact plaquette index, O(h) zero localization, and explicit separation from time-dependent GP dynamics; [audit script](scripts/audit_t110_gp_zero_vortex.py), [tests](tests/test_t110_gp_zero_vortex.py).
- [T113 — Gravitational mass of phonon–phason modes in quasiperiodic media](theorems/T113-quasicrystal-phonon-phason-gravitational-mass.md) — published fluid/solid acoustic control and open metric-variation programme for coupled quasicrystal modes. [T113-A metric-action derivation](theorems/T113A-metric-action-phonon-phason-mode-sensitivity.md), [T113-D Q6/RGS phonon–internal-mode framework](theorems/T113D-q6-rgs-phonon-internal-mode.md), [T113-E Q6/RGS T2u stability](theorems/T113E-q6-rgs-t2u-triplet-stability.md) [T113-F Q6 graph-elastic stabilization](theorems/T113F-q6-graph-elastic-stabilization.md), [Q6 graph-stiffness audit](scripts/audit_t113f_q6_graph_stabilization.py), [Q6/RGS induced-symmetry audit](scripts/audit_t113d_q6_rgs_oh.py), [tests](tests/test_t113d_q6_rgs_oh.py), [T113-C generic icosahedral construction (superseded for this programme)](theorems/T113C-icosahedral-phonon-phason-elasticity.md), [isotropic-limit audit](scripts/audit_t113_quasicrystal_phonon_gravity.py), [tests](tests/test_t113_quasicrystal_phonon_gravity.py). — manufactured static unit-vortex benchmark, exact plaquette index, O(h) zero localization, and explicit separation from time-dependent GP dynamics; [audit script](scripts/audit_t110_gp_zero_vortex.py), [tests](tests/test_t110_gp_zero_vortex.py).
- [T113 — Gravitational mass of phonon–phason modes in quasiperiodic media](theorems/T113-quasicrystal-phonon-phason-gravitational-mass.md) — published fluid/solid acoustic control and open metric-variation programme for coupled quasicrystal modes. [T113-A metric-action derivation](theorems/T113A-metric-action-phonon-phason-mode-sensitivity.md), [T113-D Q6/RGS phonon–internal-mode framework](theorems/T113D-q6-rgs-phonon-internal-mode.md), [T113-E Q6/RGS T2u stability](theorems/T113E-q6-rgs-t2u-triplet-stability.md) [Q6/RGS induced-symmetry audit](scripts/audit_t113d_q6_rgs_oh.py), [tests](tests/test_t113d_q6_rgs_oh.py), [T113-C generic icosahedral construction (superseded for this programme)](theorems/T113C-icosahedral-phonon-phason-elasticity.md), [isotropic-limit audit](scripts/audit_t113_quasicrystal_phonon_gravity.py), [tests](tests/test_t113_quasicrystal_phonon_gravity.py). — manufactured static unit-vortex benchmark, exact plaquette index, O(h) zero localization, and explicit separation from time-dependent GP dynamics; [audit script](scripts/audit_t110_gp_zero_vortex.py), [tests](tests/test_t110_gp_zero_vortex.py).
- [T113 — Gravitational mass of phonon–phason modes in quasiperiodic media](theorems/T113-quasicrystal-phonon-phason-gravitational-mass.md) — published fluid/solid acoustic control and open metric-variation programme for coupled quasicrystal modes. [T113-A metric-action derivation](theorems/T113A-metric-action-phonon-phason-mode-sensitivity.md), [isotropic-limit audit](scripts/audit_t113_quasicrystal_phonon_gravity.py), [tests](tests/test_t113_quasicrystal_phonon_gravity.py). — manufactured static unit-vortex benchmark, exact plaquette index, O(h) zero localization, and explicit separation from time-dependent GP dynamics; [audit script](scripts/audit_t110_gp_zero_vortex.py), [tests](tests/test_t110_gp_zero_vortex.py).
- [T113-B — Explicit EKN acoustic gravitational-mass control](theorems/T113B-ekn-acoustic-gravitational-mass-control.md) — derives the published fluid formula from the metric-coupled EFT and records the isotropic-solid longitudinal/transverse control; quasicrystal use remains an open extension.
- [Three defect gases and QLG–RGS–N=4 SYM–IIB bridge](docs/THREE_DEFECT_GASES_QLG_N4_IIB_BRIDGE.md) — separate calculation protocols for 2D XY/BKT, 3D XY dual vortex loops, and 2D KTHNY vector Coulomb gas; explicit derivation gates for QLG, N=4 SYM, and type-IIB AdS/CFT.

- [Theorem records](theorems/)
- [S011 — Binary tetrahedral spherical spectrum (Ikeda 1995)](theorems/S011-ikeda-binary-tetrahedral-spectrum.md) — Ikeda source formulas separated from the reconstructed eigenvalue indexing, Poincaré simplification and independent Molien multiplicity check.
- [S012 — Ikeda cyclic and binary-polyhedral spectra (1995)](theorems/S012-ikeda-cyclic-binary-polyhedral-spectra.md) — independent derivations for Theorem 4.2, the three-dimensional parts of Theorems 4.3–4.6, and the first-eigenvalue table; higher-dimensional binary cases remain explicitly open.
- [S013 — General spherical-space-form Molien theory and diagonal SU(2) actions](theorems/S013-general-spherical-space-form-molien-diagonal-actions.md) — exact Reynolds/Molien and SU(2)×SU(2) framework, corrected Ikeda propagation audit, two proved finite diagonal actions, and explicit separation of numerical coefficient lists from open exact-arithmetic work.
- [T073 — Unified football-shell / RGS–PRISM–Q6 limit programme](theorems/T073-unified-football-shell-rgs-prism-limit-program.md) — formal open target theorem separating the local results already proved from the global homogenisation and spectral limits still to prove.
- [Physical seams and interfaces — literature audit](audits/2026-11-10_physical_seams_interfaces_literature_audit.md) — JRC guidance on textile membrane seams, experimental seam failure, cohesive/contact laws, and the carefully delimited connection to grain boundaries and domain walls.
- [T075 — Seam-aware ellipsoidal reduction and ovaloid realization](theorems/T075-seam-aware-ellipsoidal-ovaloid-reduction.md) — formulates the ellipsoid as global reference geometry while retaining all 90 physical seams, panel orthotropy and interface mechanics; general ovaloid realization and numerical fitting remain open.
- [T076 — Constitutive mechanics, damage and cyclic response of the 90 physical football seams](theorems/T076-constitutive-mechanics-fatigue-hysteresis-football-seams.md) — separates reversible traction, cohesive peel/damage, contact/friction, fatigue and hysteresis; gives a construction-specific test programme and leaves football parameters open pending coupons.
- [T074 — Icosahedral shell, binary lift, and Hopf–Seifert spectral bridge](theorems/T074-icosahedral-shell-binary-lift-hopf-seifert-bridge.md) — proves the group-theoretic and Hopf/Seifert bridge between the football's rotational symmetry A5 and the Poincaré quotient S³/2I; keeps shell permutation representations and curved-shell spectral convergence explicitly open.
- [Open-problem and external-validation matrix](open-problems/EXTERNAL_MATHEMATICAL_VALIDATION_MATRIX.md)
- [Q6 T012–T017 compatibility matrix](open-problems/Q6-T012-T017-COMPATIBILITY-MATRIX.md)

The bibliography distinguishes published literature, manuscripts, non-standard sources, and material requiring further bibliographic verification. Missing metadata are left unresolved rather than guessed.

## Theorem and result register

The table is a navigation index, not a claim that every item is a theorem in the same sense. The individual record controls the precise assumptions and status.

| ID | Subject | Current scope and status |
|---|---|---|
| T001 | Liouville theorem | Classical theorem; the PSU application is conditional on its stated hypotheses. |
| T002 | Bergman density on (D_5) | Geometric calculation; the domain definition remains subject to audit. |
| T003 | Atomic marginal no-go result | Proved for an exact atomic push-forward; does not exclude weak limits. |
| T004 | Riemann sums and Bergman limits | Proved under compactness and null-boundary assumptions; not a Wilson derivation. |
| T005 | Wilson Q6 marginal support | Formula and positivity result; no hard cutoff at finite beta follows. |
| T006 | Gauge quotient on a 5-torus | Character-lattice identification. |
| T007 | Gauge-averaged series | Absolutely convergent Fourier expansion under the stated assumptions. |
| T008 | Wilson–Bergman criterion | Quantitative sufficient criterion; the Q6 application remains open. |
| T009 | Effective Wilson quadratic form | Rank identity established; Q6 rank and theta-limit hypotheses require verification. |
| [T010](theorems/T010-rumin-spectrum-poincare-sphere.md) | Rumin spectral reduction on (S^3/2I) | Finite-quotient projection theorem and scalar benchmark; the full Rumin spectrum remains to be computed. |
| T016 | Nielsen–Ninomiya and Q6 audit | Relevant hypotheses and topology reconstructed; finite Q6 identities checked; no evasion of the no-go theorem is claimed. |
| [T017](theorems/T017-q6-dirac-refinement.md) | Cubic Q6–Dirac refinement | Explicit ((C_{2n})^{square 6}) refinement, 64 naive corner zeros, Wilson lift, and symbol-limit result; full spectral convergence remains open. |
| [T019](theorems/T019-q6-free-strong-resolvent.md) | Free Q6–Wilson strong-resolvent limit | Generalized strong-resolvent convergence on a flat torus of side 2; not norm convergence or an interacting gauge limit. |
| [T020](theorems/T020-gauge-covariant-q6-strong-resolvent.md) | Gauge-covariant Q6–Wilson resolvent limit | Cell-average consistency with (O(h)) error and generalized strong-resolvent limit for fixed smooth SU(3) connections, under the stated assumptions. |
| [T021](theorems/T021-rumin-analytic-torsion-2I.md) | Rumin analytic torsion on (S^3/2I) | Molien and Hurwitz-continuation framework; see T022–T024 for subsequent corrections and operator conventions. |
| [T022](theorems/T022-eventual-hurwitz-rumin-2I.md) | Eventual Hurwitz-tail correction | Exact-arithmetic decomposition and scale check; torsions compared at high precision. |
| [T023](theorems/T023-gamma-reflection-rumin-2I.md) | Exact Gamma–sine identities for (2I) twists | Symbolic reduction over (mathbb Q(sqrt5)), including the exceptional tail; review status is recorded in the PR history. |
| [T024](theorems/T024-rumin-kitaoka-operator-matching-3d.md) | Kitaoka–Rumin–Seshadri operator matching in dimension 3 | Scaling, Laplacians, Hodge duality, and torsion conventions reconciled under the stated definitions. |
| [T031](theorems/T031-rumin-2i-equivariance.md) | Rumin-complex equivariance under binary icosahedral action | Geometric descent and unitary twists; explicit irreducible models are developed in T034–T036. |
| [T032](theorems/T032-2i-irrep-molien-projectors.md) | Exact Molien covariants and isotypic projectors for (2I) | Integer coefficients and dimension decompositions checked; explicit matrix models are treated separately. |
| [T033](theorems/T033-equivariant-rumin-torsion-synthesis.md) | Isotypic Rumin-complex decomposition | Finite-group synthesis under explicit hypotheses; introduces no independent torsion value. |
| [T034](theorems/T034-exact-2i-character-table.md) | Exact character table of (2I) | Reconstruction over (mathbb Q(sqrt5)); orthogonality and Molien averages are checked exactly. |
| [T035](theorems/T035-exact-binary-icosahedral-model.md) | Exact quaternionic model of (2I) | 120 vertices of the 600-cell, multiplication table, conjugacy classes, and fundamental representation. |
| [T036](theorems/T036-explicit-2i-irreducible-models.md) | Explicit matrix models of the nine irreducible representations of (2I) | Symmetric-power construction, central projectors, and invariant Hermitian metrics; CI certification and downstream Rumin matrices remain tracked separately. |
| [T047](theorems/T047-ec-weyssenhoff-spin-scaling.md) | Einstein–Cartan Weyssenhoff spin scaling | Under the stated minimal assumptions, (n\propto a^{-3}), (s^2\propto a^{-6}), and the effective spin correction is negative and stiff. This is not a dust-like (a^{-3}) component. |
| [T048](theorems/T048-rgs-prism-mosco-changing-spaces.md) | Mosco convergence on varying RGS–PRISM spaces | Sets comparison maps and compactness requirements; periodic-cycle calibration is not a proof for the actual RGS–PRISM refinement sequence. |
| [T049](theorems/T049-microscopic-spin-correlation-invariant.md) | Microscopic spin current and quadratic invariant | Self/pair decomposition framework; physical RGS–PSU correlator and normalization remain outstanding. |
| [T049A](theorems/T049A-q6-prism-spin-correlator.md) | Q6/PRISM microscopic spin correlator | Shell correlators and self/pair decomposition; current numerical inputs do not constitute physical spin data. |
| [T049B](theorems/T049B-rgs-ec-q6-prism-axial-current.md) | Lorentzian EC–Dirac axial current on Q6/PRISM | Dirac axial-current moments, shell-resolved tensor correlators, EC contact term, and provenance limitations. |
| [T049C](theorems/T049C-qlg-dirac-intertwiner-classification.md) | QLG-to-Dirac intertwiner classification | A two-complex-dimensional family of Spin(3)-equivariant isometric embeddings; no canonical embedding is selected. |
| [T049D](theorems/T049D-lorentz-chiral-qlg-embedding.md) | Lorentz-covariant QLG–Dirac embedding | The two Weyl embeddings are the (gamma^5) eigenspaces; parity exchanges them. Lorentz covariance does not select one chirality sign. |
| [T050](theorems/T050-geometric-spin-chain-bounds.md) | Geometric spin-chain summability and operator bound | Exact geometric-series identity and uniform-in-chain-length bound for the exchange part of the stated finite Hamiltonian. |
| [T051](theorems/T051-crank-nicolson-unitarity.md) | Crank–Nicolson unitarity | Norm preservation for a fixed finite-dimensional Hermitian Hamiltonian; no coupled-energy or breather claim. |
| [T052](theorems/T052-scalar-torsion-variation.md) | Scalar variation of a scalar–torsion action | Conditional Euler–Lagrange identity for the explicitly displayed action with geometry held fixed. |
| [T053](theorems/T053-exterior-square-projector-lemma.md) | Exterior-square projector lemma | Conditional abstract theorem; exact source-derived (C_6/C_{15}) matrix check in [audit](audits/audit_t053_exterior_square.py); group equivariance/irreducibility remain unverified. |
| [T054](theorems/T054-static-radial-klein-gordon.md) | Static radial Klein–Gordon reduction | Exact reduction for a minimally coupled static radial scalar on the stated spherical metric ansatz. |
| [T055](theorems/T055-q6-dyadic-subdivision-chain-map.md) | Exact dyadic subdivision chain map for the Q6 2-skeleton | Proved finite cubical midpoint subdivision with 496/1344/960 refined cells and exact boundary-commuting maps; not a Kathara/Krist-All identification. |
| [T056](theorems/T056-phase21-trigram-supergolden-permutation-conjugacy.md) | Phase 21–trigram supergolden matrix conjugacy | Exact permutation similarity of the two 3-state transfer matrices; same polynomial and Perron root, but no geometric cell intertwiner is established. |
| [T057](theorems/T057-kathara-square-similarity-center-overlay.md) | Kathara square similarity and center-overlay relation | Exact 45° clockwise / √2 map, two-stage 90° / ×2 relation, and center 6–9–12 overlay coordinates under the stated 2:1 geometry. |
| [T058](theorems/T058-kathara-15-line-planar-face-audit.md) | Kathara 12-center / 15-line planar face audit | Conditional exact graph theorem: 12 vertices, 21 elementary edges, 10 bounded faces, connected planar embedding and Euler characteristic 2. |
| [T059](theorems/T059-kathara-cellular-chain-hodge-audit.md) | Kathara cellular chain complex and Hodge operators | Exact integer incidence construction conditional on filling the 10 bounded faces: B1B2=0, ranks (11,10), Betti numbers (1,0,0), Euler characteristic 1; no Krist-All or Q3/Q6 identification claimed. |
| [T060](theorems/T060-kathara-q3-chain-map.md) | Coordinate-defined Kathara–Q3 chain map | Coarse candidate into the b₂=0 square of the Q₃ 2-skeleton; chain-map test execution remains pending. |
| [T061](theorems/T061-kathara-q3-chain-homotopy.md) | Chain homotopy between the two Kathara–Q3 path conventions | Explicit homotopy between b₀-first and b₁-first maps; the selected Kathara face is convention-dependent, while induced homology maps agree. Corrects the claim [K,Q₃] ≅ ℤ for a contractible disk source. |
| [T062](theorems/T062-kathara-q6-integral-chain-map.md) | Explicit integral Kathara–Q6 chain map | Proves existence under a declared integer-coordinate code using root-path differences; injective on vertices but collapses all ten 2-cells, so it is not a cellular embedding or an RGS-canonical map. |
| [T063](theorems/T063-quaternion-su2-so3-double-cover.md) | Quaternionic realization of SU(2) and the double cover of SO(3) | Proves the scalar-first Hamilton-quaternion isomorphism with SU(2), and the conjugation homomorphism onto SO(3) with kernel {±1}; fixes the active column-vector convention used by the bridge implementation. |
| [T064](theorems/T064-finite-su2-lattice-holonomy-gauge-covariance.md) | Gauge covariance of finite SU(2) lattice transport and Wilson traces | Proves endpoint covariance of path transport, conjugation of closed holonomy, Wilson-trace invariance and the real normalized SU(2) trace bound. |
| [T065](theorems/T065-cubical-subdivision-chain-map-and-naturality.md) | Exact cubical subdivision chain map and signed-permutation naturality | Proves the integral boundary-commuting subdivision map and its naturality under all 48 signed-permutation symmetries in 3D. |
| [T066](theorems/T066-herasymov-parity-affine-shared-face-conformity.md) | Herasymov parity-cell affine shared-face conformity | Proves, under the explicit cellwise-affine interpretation and N≥2, that conformity holds iff all eight parity classes use the same affine coordinate map. |
| [T067](theorems/T067-stokes-commuting-cubical-face-integral-interpolation.md) | Stokes commutation of cubical face-integral interpolation | Proves exact commutation of the face-integral interpolator with the cellular exterior derivative; numerical quadrature checks remain finite. |
| [T068](theorems/T068-barycentric-covariance-quadrature-law.md) | Barycentric–covariance quadrature on a planar triangle | Exact local Taylor identity, triangle covariance formula and (A_F h_F^3\sup\|D^3g\|/6) remainder bound; global refinement and Bernoulli asymptotics remain open. |
| [T069](theorems/T069-q6-antipodal-walsh-covariance.md) | Q6 antipodality, RGS coordinate inversion, Walsh sectors and covariance | Separates the global Q6 antipode (XOR 63) from the RGS seed's coordinate inversion (XOR 7); records the exact covariance decomposition and finite numerical/Walsh audit. Phase dynamics and cell-covariance transport remain open. |
| [T070](theorems/T070-dirichlet-barycentric-phase-moments.md) | Dirichlet barycentres, covariance and phase moments on triangular cells | Exact Gamma/Beta normalization, weighted centroid and covariance, cubic Taylor remainder, affine-phase moment bound; football-shell global refinement and Bernoulli asymptotics remain open. |

**Dirichlet quadrature implementation:** [Duffy–Gauss–Jacobi derivation and normalization](docs/DIRICHLET_DUFFY_JACOBI_QUADRATURE.md), [source](src/dirichlet_triangle_quadrature.py), [A1–A3 tests](tests/test_dirichlet_triangle_quadrature.py).
| [S.1](theorems/S001-silver-ratio-square-corner-tangency.md) | Silver-ratio square-corner tangency | Exact Euclidean scale identities for the stated two-circle configuration; no general packing/refinement law. |
| [S.2](theorems/S002-square-pentagon-supergolden-synthesis.md) | Square, pentagon, hexagon and supergolden geometry | Exact component identities; labelled incidence and a construction deriving the supergolden ratio remain open. |
| [S.3](theorems/S003-dirichlet-log-partition-gradient-cumulants.md) | Dirichlet log-partition gradient and cumulants | Exact digamma/trigamma parameter derivatives; Bernoulli/zeta mesh asymptotics remain open. |
| [S.4](theorems/S004-rgs-seed-fourth-moment-anisotropy.md) | RGS 64-site fourth-moment anisotropy | Hash-checked seed reconstruction and independent numerical replay of raw moments, isotropic projection, cubic residual and Eg/T2g spectrum; full pytest execution remains separate. |
| [S.5](theorems/S005-fourth-jump-moment-graph-laplacian-consistency.md) | Fourth-jump-moment consistency | Conditional Taylor expansion and O(a²) graph-Laplacian consistency; application to the actual RGS refinement remains open. |
| [S.6](theorems/S006-fourth-moment-so3-connection-current.md) | Fourth-moment SO(3) connection current | Proved local variational identity for the connection current; flatness constraint and full TEGR equations remain open. |
| [S.7](theorems/S007-fourth-moment-maxwell-and-a4-bridge.md) | Fourth-moment Maxwell obstruction and A4 bridge | Exact tensor no-go and subgroup representation result; Maxwell constitutive law is a candidate and the explicit intertwiner is open. |
| [S.8](theorems/S008-fourth-moment-coframe-variation.md) | Fourth-moment algebraic coframe variation | Exact first variations for the displayed action; no torsion generation or complete gravitational equation is claimed. |
| [S.9](theorems/S009-weber-dedekind-eta-supergolden-class-invariant.md) | Weber–Dedekind eta class invariant and supergolden root | Reciprocal Weber class invariant at discriminant −31 gives the supergolden root; class-polynomial provenance and CM-point conventions are explicit. |
| [S.10](theorems/S010-dirichlet-eta-lambert-series-quadratic-zeta.md) | Dirichlet eta, Dedekind eta coefficients and quadratic zeta | Exact Lambert-series Dirichlet products, ζ_K factorization, class-number value and Bernoulli/polygamma links. |
| [S011](theorems/S011-ikeda-binary-tetrahedral-spectrum.md) | Binary tetrahedral spherical spectrum | Ikeda's (S^3/T^*) eigenvalue and multiplicity formula, subgroup inclusion–exclusion and independent Molien check; separate from (S^3/2I). |
| [T071](theorems/T071-q6-cubical-topological-synchronization-audit.md) | Q6 cubical chain complex, Anti-Twin lift and synchronization benchmark | Exact finite chain identities; exploratory synchronization/hysteresis model, with physical and continuum claims open. |
| [T072](theorems/T072-q6-mobius-phase-flat-connection.md) | Möbius phase action and canonical flat Q6 connection | Exact phase-translation Möbius action, pure-gauge vertex-phase connection, Q6 Laplacian spectrum and antipodal 32+32 decomposition; nontrivial RGS–PSU transport remains open. |
| [T073](theorems/T073-unified-football-shell-rgs-prism-limit-program.md) | Unified football-shell / RGS–PRISM–Q6 limit programme | Open conditional target: global barycentric quadrature, curved-shell structured-deformation Gamma limit, changing-space Mosco convergence and spectral convergence; no global theorem is claimed. |

**Numbering note.** The T068 collision between the barycentric theorem and two Q6 records has been resolved: T068 is the barycentric theorem, T071 is the cubical synchronization audit, and T072 is the Möbius/flat-connection theorem. Historical overlapping T034 labels are a separate legacy issue.

The file `001-fixed-lattice-temporal-wilson-limit.md` is a pre-existing result and is not part of the T001–T007 numbering sequence.

## Exact geometric lemmas

- [Lemma S.1 — Silver-ratio scaling in a square-corner tangency configuration](theorems/S001-silver-ratio-square-corner-tangency.md) — proves the exact relations `d/R = 1/(1+sqrt(2))` and `r/R = 1/(1+sqrt(2))^2` for the incircle/corner-circle tangency geometry. This is a local Euclidean lemma; no Q6 refinement or infinite self-similarity is claimed.
- [S.2 — Unified square–triangle–pentagon–hexagon and supergolden geometry](theorems/S002-square-pentagon-supergolden-synthesis.md) — places the square's silver-ratio diagonal/tangency geometry, an inscribed regular pentagon's golden-ratio chords, and an inscribed regular hexagon's bronze-ratio metric on the same circle; records the supergolden rectangle and the still-open incidence/construction bridges.
- [S.3 — Dirichlet log-partition gradient and cumulants](theorems/S003-dirichlet-log-partition-gradient-cumulants.md) — identifies parameter-gradients with mean logarithmic barycentric coordinates and the Hessian with their covariance; gives the exact digamma/trigamma and Bernoulli/zeta asymptotic link.
- [S.4 — RGS 64-site fourth-moment anisotropy](theorems/S004-rgs-seed-fourth-moment-anisotropy.md) — separates the fully symmetric seed fourth moment into isotropic and cubic-anisotropic parts; reports the prior numerical Eg/T2g decomposition and explicitly excludes torsion identification.
- [S.5 — Fourth-jump-moment graph Laplacian consistency](theorems/S005-fourth-jump-moment-graph-laplacian-consistency.md) — gives the Taylor expansion through order four and a conditional O(a²) consistency criterion under first/third-moment cancellation and uniform fourth-moment bounds.
- [S.6 — Fourth-moment SO(3) connection current](theorems/S006-fourth-moment-so3-connection-current.md) — proves the positive shifted constitutive operator, covariant STF derivative and antisymmetric connection current; complete teleparallel field equations remain open.
- [S.7 — Fourth-moment Maxwell obstruction and A4 bridge](theorems/S007-fourth-moment-maxwell-and-a4-bridge.md) — proves the direct RFF contraction vanishes and records the common A4 representation route; constitutive response and explicit intertwiner remain candidates/open.
- [S.8 — Algebraic fourth-moment coframe variation](theorems/S008-fourth-moment-coframe-variation.md) — gives the exact coframe, lapse and STF variations of the displayed algebraic action; it does not generate torsion.

## Selected research records

### RGS cellular dynamics benchmark

- [Python benchmark](scripts/rgs_cellular_dynamics_benchmark.py)
- [Automated tests](tests/test_rgs_cellular_dynamics_benchmark.py)
- [User guide](docs/RGS_CELLULAR_DYNAMICS_README.md)
- [Research roadmap](docs/RGS_CELLULAR_DYNAMICS_ROADMAP.md)

**Status:** initial implementation and smoke-test stage. This is not yet a theoretical result or a statistical validation of genetic evolution. The next methodological requirements include paired random seeds, independent validation, and multi-objective evaluation.

### Phenomenological torsion–Lambda FLRW closure

The [torsion–Lambda dust closure](models/TORSION_LAMBDA_DUST_CLOSURE.md) is implemented in `scripts/torsion_lambda_dust_closure.py` and tested in `tests/test_torsion_lambda_dust_closure.py`.

**Status:** a phenomenological consistency model. It is not presented as a derivation from algebraic Einstein–Cartan torsion field equations.

### Einstein–Cartan spin-scaling audit

Under the minimal Weyssenhoff assumptions recorded in T047—conserved spin per particle and local isotropic averaging—the number density scales as (a^{-3}), the spin-squared term as (a^{-6}), and the effective correction has stiff equation of state. Consequently, this term cannot be identified directly with the dust-like (a^{-3}) component of the phenomenological closure in PR #77 under those same assumptions.

See [T047](theorems/T047-ec-weyssenhoff-spin-scaling.md), `scripts/ec_spin_fluid_scaling.py`, and `tests/test_ec_spin_fluid_scaling.py`.

### RGS–PRISM forms and changing spaces

T048 formulates the requirements for Mosco convergence on varying Hilbert spaces. It distinguishes comparison maps, strong-resolvent convergence, and spectral convergence, and identifies uniform compactness/tightness as a necessary additional issue before eigenvalue convergence with multiplicities can be concluded.

The periodic-cycle example is a calibration model only. A standalone [open-problem dossier for curved cubical refinements](manuscripts/MOSCO_CURVED_CUBICAL_REFINEMENT_OPEN_PROBLEM.md) now specifies a five-factor product-grid baseline, non-affine cell-map hypotheses, identification maps, candidate M1/M2 proof routes, uniform compactness obligations, and questions for external review. The actual curved RGS–PRISM refinement sequence and its compactness proof remain open.

See [T048](theorems/T048-rgs-prism-mosco-changing-spaces.md), [the curved-cubical dossier](manuscripts/MOSCO_CURVED_CUBICAL_REFINEMENT_OPEN_PROBLEM.md), `scripts/rgs_prism_mosco_calibration.py`, and `tests/test_t048_rgs_prism_mosco_calibration.py`.

### QLG–Dirac embedding and Lorentz chirality

T049C classifies the Spin(3)-equivariant embeddings of a two-component QLG fibre into the spatial restriction of the four-component Dirac representation. The family is not canonical.

T049D then imposes Lorentz covariance using the Clifford convention documented in the source implementation, with signature ((-+++)). With the commutator normalization used by the record, the boost generators are \(\mathcal K_i=\tfrac{i}{2}\gamma^0\gamma^i\), inducing \(K_i^{(s)}=-is\sigma_i/2\) on the two Weyl fibres. The two invariant embeddings are the two Weyl sectors, represented by
[
K_s=\frac{1}{\sqrt{2}}\begin{pmatrix}I_2\\sI_2\end{pmatrix},
\qquad s=\pm1.
]
Parity exchanges the two sectors. Thus Lorentz covariance identifies the two chiral representation choices but does not dynamically select the sign. A parity-invariant theory must retain both sectors unless an additional parity-breaking mechanism or boundary condition is supplied.

The QLG SU(2) fibre by itself does not determine a unique Spin(1,3) extension. No physical chirality-selection mechanism or new cosmological spin law is claimed.

See [T049C](theorems/T049C-qlg-dirac-intertwiner-classification.md), [T049D](theorems/T049D-lorentz-chiral-qlg-embedding.md), and the corresponding scripts and tests under `scripts/` and `tests/`.



### Q6–D5 Wilson fibre marginal: exact construction and open quantitative control

The Q6–D5 Wilson fibre specifications have been transferred into this central repository: [integer-fibre quotient](docs/Q6_D5_INTEGER_FIBER_QUOTIENT.md), [saturated kernel and factorial tail bound](docs/Q6_D5_SATURATED_KERNEL_AND_TAIL_BOUND.md), and [five-torus Wilson marginal](docs/Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md). The associated theorem records are [T005](theorems/T005-q6-wilson-fiber-marginal-support.md)–[T009](theorems/T009-effective-wilson-fiber-quadratic-form.md). The implementation-port and certified-evaluation task is tracked in [Issue #84](https://github.com/fabianleonaressi95/theorem/issues/84).

**Current boundary:** the rank-five rational quotient, rank-124 integer kernel, positive fibre-summed weight and exact Fourier/Haar identities are mathematical constructions under their stated hypotheses. The complete 124-dimensional fibre sum has **not** been numerically evaluated with a certified enclosure, and no Wilson-to-Bergman/Hua measure identification is established. The source implementation is being consolidated into THEOREM; the transferred specifications are not a runtime dependency on the bridge repository.


### Curvilinear cubical de Rham / FEEC benchmark

The finite benchmark and its mathematical status are now indexed centrally:
- [T065 — exact cubical subdivision and signed-permutation naturality](theorems/T065-cubical-subdivision-chain-map-and-naturality.md)
- [T066 — Herasymov parity-cell shared-face conformity](theorems/T066-herasymov-parity-affine-shared-face-conformity.md)
- [T067 — Stokes commutation of cubical face-integral interpolation](theorems/T067-stokes-commuting-cubical-face-integral-interpolation.md)
- [CI evidence record, 9 November 2026](audits/DE_RHAM_BENCHMARK_CI_2026-11-09.md)
- [Benchmark theorematic foundations](projects/de_rham_benchmark/docs/THEOREMATIC_FOUNDATIONS.md)
- [Uniform FEEC projection stability theorem](projects/de_rham_benchmark/docs/PROJECTION_STABILITY_THEOREM.md)
- [Independent mathematical audit](projects/de_rham_benchmark/docs/INDEPENDENT_MATHEMATICAL_AUDIT.md)

**Boundary:** the successful CI run certifies the configured finite audits and regression checks. It does not prove uniform FEEC projection stability, discrete compactness, Mosco convergence, norm-resolvent convergence, or spectral convergence on the curved RGS–PRISM refinement sequence. Those remain open under the assumptions and obligations recorded in T048 and the benchmark dossier.

## Connection to the Nielsen/Hopf research thread

The bibliography cited in Jennifer Lorraine Nielsen's manuscript is catalogued separately in [nielsen-hopf-manuscript.md](bibliography/source-bibliographies/nielsen-hopf-manuscript.md). T010 develops an independent mathematical result concerning the Hopf/Seifert quotient (S^3/2I). It does not attribute that theorem to Nielsen, and the manuscript is not treated as validation of the results proved here.

## Research and verification principles

1. **One claim at a time.** A theorem record should state definitions, hypotheses, lemmas, proof, and consequences.
2. **Proofs are not replaced by scripts.** Code supports reproducibility and checks; it does not substitute for a mathematical argument.
3. **Evidence is labelled.** Use precise categories such as proved, conditional, numerically verified, candidate, conjectural, and open.
4. **No unsupported physical interpretation.** A discrete identity or numerical fit does not by itself establish a physical law.
5. **Sources are traceable.** A source is used in a proof only when it supports a specific mathematical step.
6. **No invented bibliographic metadata.** Missing authors, titles, dates, and identifiers remain explicitly unresolved.
7. **Critical treatment of non-standard sources.** Such material is preserved for analysis, but neither assumed true nor dismissed without examination.
8. **Reproducibility matters.** Scripts, tests, data provenance, conventions, and residuals should be recorded alongside computational claims.

## Repository status and next priorities

The repository contains a growing bibliography, theorem records, numerical audits, and model implementations. It is still an evolving research workspace rather than a completed monograph or a blanket validation of the RGS–PSU programme.

Current priorities include:

- completing the bibliographic inventory and resolving duplicate or ambiguous theorem numbering;
- keeping theorem statements, scripts, tests, and README indexes synchronized;
- establishing the actual RGS–PRISM refinement sequence and proving the required compactness for a Mosco/continuum limit;
- supplying physically normalized four-component spinor data and deriving the Noether normalization needed for a physical spin invariant;
- deriving, rather than postulating, any QLG mechanism that could select a Lorentzian chirality;
- separating model-level consistency from empirical or phenomenological validation.

Contributions and critical mathematical feedback are welcome, especially when they identify a precise statement, missing hypothesis, counterexample, or reproducible verification.


## Related implementation repository: RGS–QLG Quaternion Bridge

The [RGS–QLG Quaternion Bridge](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge) is a complementary implementation- and experiment-oriented repository for quaternionic geometry, SU(2)/SO(3), Q6 structures, spinorial operators and related computational audits. It is connected to this central research index, but it is **not a required dependency** for the mathematical statements or verification workflows maintained here.

Use this repository (**THEOREM**) as the authoritative programme-wide index for theorem statements, assumptions, proof status, open problems and cross-project research priorities. Use the bridge repository for its own implementation details and experiments; when citing a computational result, identify the exact source path and commit. A result in either repository does not automatically validate claims in the other.

- [RGS–QLG Quaternion Bridge — repository](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge)
- [RGS–QLG Quaternion Bridge — README](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/README.md)
- [Bridge's statement of its relationship to THEOREM](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/README.md#relationship-to-the-central-theorem-research-repository)


## Kathara chain-map bridge

- [T060 — Coordinate-defined Kathara to Q3 chain map](theorems/T060-kathara-q3-chain-map.md)
- [T061 — Chain homotopy between the two path conventions](theorems/T061-kathara-q3-chain-homotopy.md)
- [T062 — Explicit integral Kathara to Q6 chain map](theorems/T062-kathara-q6-integral-chain-map.md)

**Status:** T060 records the coordinate-defined chain-map candidate into one square face of Q3; T061 records the explicit homotopy between its two path conventions. T062 proves an integral Kathara-to-Q6 chain map under an explicit integer-coordinate code, but its 2-cell map is zero on all ten source faces. It is an existence result for a degenerate chain map, not a cellular embedding, not RGS-equivariant, and not a canonical identification. Independent test execution remains pending. None of these records identifies Kathara with the full trigram cube or derives Krist-All.

A separate implementation-level **Gate D candidate** is being audited in the [RGS–QLG Quaternion Bridge, PR #195](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/195). It uses nonzero cubical face fillings and a declared, non-RGS-canonical Q6 path-order convention. It must not be conflated with T062: T062 remains the proved degenerate map above. Gate D's full repository CI passed on 10 November 2026 at bridge commit `a4ccaff06b90eea0270d982ec154338a3610d048`, including the exact chain-map and rank tests. Gate D still does not establish RGS equivariance, a cellular embedding, or Ellis/SU(2) transport, so it remains an implementation-level noncanonical construction and is not promoted to a theorem record.

## Curvilinear cubical de Rham benchmark

A reproducible numerical benchmark for discrete Hodge–de Rham complexes on curvilinear cubical meshes is maintained in [`projects/de_rham_benchmark/`](projects/de_rham_benchmark/). It includes mesh/incidence construction, pullback geometry, diagonal Hodge weights, spectral diagnostics, pollution analysis, assumptions and report.

- [Benchmark README](projects/de_rham_benchmark/README.md)
- [Assumptions and conventions](projects/de_rham_benchmark/ASSUMPTIONS.md)
- [Benchmark report](projects/de_rham_benchmark/REPORT.md)
- [Results and plots](projects/de_rham_benchmark/results/run1/)

**Status:** computational investigation only. The reported collapse of positive eigenvalues is an observed benchmark phenomenon; its interpretation as discrete-compactness failure is a conjecture pending independent reproduction and comparison with consistent FEEC mass matrices. No Mosco-convergence theorem is claimed.


## RGS–PRISM recovery audits for the Morandotti dossier

- [Technical appendix](manuscripts/APPENDICE_TECNICA_MORANDOTTI_RGS_PRISM.md)
- [Audit records index](reports/README.md)
- [PRISM 69,120 incidence audit](reports/prism_69120_audit.json)
- [188D Anti-Twin recovered-matrix audit](reports/188d_antitwin_audit.json)
- [Krist-All recovery status and missing evidence](reports/KRISTALL_RECOVERY_STATUS.md)
- [Recovery provenance manifest](reports/RECOVERY_MANIFEST.md)

Reproduction:
```bash
python -m pip install -r requirements-audit.txt
python -m pytest -q tests/test_prism_audit.py tests/test_188d_antitwin_audit.py
python scripts/audit_prism_69120.py
python scripts/audit_188d_antitwin.py --input /path/to/actual_original_X_report_matrices.npz
```

The 188D matrix NPZ is not committed in this release; its SHA-256 and recovered source provenance are recorded in the manifest. The script requires that exact archive as input and does not substitute synthetic data for the research matrices.


### Recovered 188D Anti-Twin source

- [Original geometry-driven intertwiner construction script](archive/recovered_188d/RGS_PSU_construct_geometric_intertwiner.py)
- [Corrected basis-aware audit report](reports/188d_antitwin_audit.json)
- [Updated recovery provenance and basis caveats](reports/RECOVERY_MANIFEST.md)
- [Expanded Morandotti appendix, including the corrected equivariance statement](manuscripts/APPENDICE_TECNICA_MORANDOTTI_RGS_PRISM.md)


### Pentagon–hexagon anisotropy in a pressurised football

- [Research and model note](docs/FOOTBALL_PENTAGON_HEXAGON_ANISOTROPY.md)
- [Panel-network implementation](models/football_anisotropy.py)
- [Reproducible audit runner](scripts/run_football_anisotropy_audit.py)
- [Automated tests](tests/test_football_anisotropy.py)
- [JSON audit output](reports/football_anisotropy_audit.json)
- [Panel displacement SVG](reports/football_anisotropy_displacement.svg)

**Status:** the truncated-icosahedron incidence counts and the linear panel-network equilibrium are implemented and tested. The panel model is phenomenological; it is not yet a nonlinear shell/finite-element model and has no experimental material calibration. See the note for the exact scope and next validation requirements.


### Orthotropic discrete shell and cube–sphere coupling

- [Discrete shell implementation](models/football_shell.py)
- [Shell audit and scan runner](scripts/run_football_shell_audit.py)
- [Technical note: cube/sphere, orthotropy, seams and scan validation](docs/FOOTBALL_ORTHOTROPIC_DISCRETE_SHELL.md)
- [Shell tests](tests/test_football_shell.py)
- [Experimental scan input instructions](data/scans/README.md)

The current implementation is a linearised triangular membrane + signed-dihedral bending shell. It includes panel-wise orthotropy, seam reinforcement, the existing cube/sphere radial field and the cubic H4 mode. Experimental scan comparison is implemented, but no real scan or material coupon data has yet been supplied; CI uses a synthetic ICP registration test only.


### Morandotti planar incompatibility: first H2-conforming assembly

The weak Saint-Venant/KKT benchmark has a first rectangular Bogner–Fox–Schmit implementation: `models/morandotti_bfs_kkt.py`, with tests in `tests/test_morandotti_bfs_kkt.py`. It assembles globally H2-conforming scalar test Hessians, the cellwise-constant symmetric strain basis, the isotropic plane-stress stiffness tensor, and the finite-dimensional matrices A_h and M_h. The 2x2 mesh prototype has four clamped-interior test DOFs and twelve strain DOFs. Pointwise Burgers/Frank source evaluation and a normalized Gaussian-core prototype are implemented with D1/D2 KKT regression tests; the Gaussian core convention, D3, h/epsilon-separated refinement, and comparison with the Airy/CIP-DG baseline remain open. This KKT/BFS track is distinct from the executed two-core C0-IPDG reconstruction audit below. See [the benchmark specification](manuscripts/MORANDOTTI_BENCHMARK_I_DISCRETE_SAINT_VENANT_KKT.md) and [technical appendix](manuscripts/APPENDICE_TECNICA_MORANDOTTI_RGS_PRISM.md).

### T094 — Numerical Cartan holonomy and Morandotti source adapter

- [T094 theorem and audit specification](theorems/T094-se2-holonomy-morandotti-audit.md)
- [Manufactured noncommuting SE(2) audit runner](scripts/rgs_se2_holonomy_audit.py)
- [Regression tests](tests/test_rgs_se2_holonomy_audit.py)
- [Dedicated GitHub Actions workflow](.github/workflows/t094-se2-holonomy-audit.yml)

The implementation integrates ordered edge transports for a smooth noncommuting SE(2) connection, compares face holonomy with the analytic Cartan curvature, and exports an optional adapter from measured integrated core-loop data to the existing Morandotti Frank/Burgers source-vector convention. **Execution and numerical verification are pending; no convergence result is claimed yet.**

### T099 — Shao–Yong hexagram product and Kirchhoff network

- [T099 theorem record](theorems/T099-shao-yong-q6-kirchhoff-network.md) formalizes the 8×8 lower/upper-trigram product as the exact graph identity (Q_6=Q_3^{\mathrm{inf}}\square Q_3^{\mathrm{sup}}).
- It proves the 64 vertices, degree six, 192 edges split into 96 lower-line and 96 upper-line edges, and the binomial Laplacian spectrum.
- The weighted Kirchhoff/RC system is a conditional circuit model. The precise 64-label circular transcription and any physical charge law remain open; a circular drawing is not identified with an extra cycle graph.
- [Reproducible audit](scripts/audit_t099_shao_yong_q6.py) and [tests](tests/test_t099_shao_yong_q6.py).

### T105 — Hexagram-resolved charge, two-field moiré coupling, and circuit response

- [T105 theorem record](theorems/T105-hexagram-charge-moire-circuit-law.md) connects the 64 individually measured hexagram charges to the two registered circle-phase fields, Kirchhoff edge currents, node-charge correlations, moiré reconstruction, Green–Kubo response, and defect diagnostics.
- Preserves all 64 charge sites and the two phase components on each site; explicitly keeps phase winding, Burgers closure, Frank holonomy, and T104 \\(\\mathbb F_2\) flux distinct.
- The constitutive phase-to-charge law, spatial embedding, reciprocal vectors, Green–Kubo coefficient, and material defect labels remain conditional on calibrated measurements. No physical charge values or moiré scale are invented.
- [Audit script](scripts/audit_t105_hexagram_moire_circuit.py), [tests](tests/test_t105_hexagram_moire_circuit.py), and [dedicated CI workflow](.github/workflows/t105-hexagram-moire-circuit.yml).

### T109 — General Q_n influence identities and the dimension gap

- [T109 theorem record](theorems/T109-qn-dimension-uniform-influence-gap.md) extends the exact Walsh influence and Laplacian identities from Q6 to every Q_n.
- Proves the degree-d total-influence bounds and the dimension-dependent estimate \(\max_i\mathcal I_i(f)\ge 4\operatorname{Var}(f)/n\).
- Gives a bounded degree-one family showing that no *linear-in-variance* lower bound can be dimension-free. This does not contradict Aaronson–Ambainis, whose target is nonlinear in the variance.
- Precisely isolates the missing ingredient: a degree-sensitive mechanism controlling concentration on individual coordinates. No independent proof of the dimension-free Aaronson–Ambainis theorem is claimed.

### T107 — Gray-torus geometry, reversible Q6 Gibbs dynamics, and preregistered FDT tests

- [T107 theorem record](theorems/T107-q6-gray-torus-gibbs-fdt-defect-test.md) uses the graph-preserving Gray map \(Q_6\cong C_4^3\) and the existing exact quotient onto a periodic \(C_4\times C_4\) cell with a four-state internal fibre.
- Specifies a Gibbs interaction \(H_J=-J\sum_{e\in E(Q_6)}\operatorname{Re}(z_h\bar z_k)\) on \(S^{127}\), a reversible overdamped generator, and the exact zero-coupling edge-coherence susceptibility \(\partial_J\langle c_e\rangle|_{0}=\beta/8320\).
- Separates translational Burgers cochains from rotational Frank holonomy and pre-registers held-out cross-prediction and FDT checks. The model is mathematical; no physical circuit or material validation is claimed.
- [Audit](scripts/audit_t107_gray_torus_gibbs_fdt.py), [tests](tests/test_t107_gray_torus_gibbs_fdt.py), and [focused CI](.github/workflows/t107-gray-torus-gibbs-fdt.yml) verify the Gray graph map, quotient chain maps, and analytic susceptibility.

### T110 — XY vortices on 2D/3D tori and the KTHNY boundary

- [T110 theorem record](theorems/T110-xy-torus-vortex-kthny-bkt.md) defines integer plaquette winding on the 2D torus, harmonic winding sectors, and divergence-free dual-link vortex flux on the 3D torus.
- Distinguishes the 2D XY/BKT helicity-modulus jump from KTHNY dislocation unbinding (\\(K_R=16\\pi\\)) and from 3D vortex-loop proliferation. The logarithmic pair potential is not identified with the signed charge correlator.
- [Metropolis audit](scripts/audit_xy_torus_kthny_bkt.py), [tests](tests/test_xy_torus_kthny_bkt.py), and [focused CI](.github/workflows/t110-xy-torus-vortex-kthny-bkt.yml) check 2D neutrality, 3D dual-flux closure, winding integrality, and finite-size smoke runs. No transition temperature or material KTHNY bridge is claimed.

### T108 — Boolean influences, the Q6 Laplacian, and cubical cohomology

- [T108 theorem record](theorems/T108-boolean-influences-q6-laplacian-cohomology.md) derives the exact Walsh influence identity on the six-cube and the fixed-dimension estimate \\(\\max_i\\operatorname{Inf}_i(f)\\ge(2/3)\\operatorname{Var}(f)\).
- Identifies each influence with the squared norm of a coordinate component of the exact edge gradient; verifies zero square circulation and keeps graph cycles (dimension 129) distinct from cubical cohomology (\\(H^1=0\)).
- This is a finite Q6 Poincaré result, **not** a dimension-uniform proof or improvement of the Aaronson–Ambainis theorem.
- [Exact-rational audit](scripts/audit_t108_boolean_influence_q6.py), [tests](tests/test_t108_boolean_influence_q6.py), and [focused CI](.github/workflows/t108-q6-boolean-influence.yml).

### T106 — Born measure, Q6 phase torus, FDT, and Frank–Burgers defects

- [T106 theorem record](theorems/T106-born-measure-q6-fdt-frank-burgers.md) specializes the known Haar/Born push-forward theorem to the 64 hexagram outcomes, records exact Dirichlet moments and the \(\\mathbb Z_4^3\) indexing, and separates Born/Haar measure from thermal equilibrium.
- Adds the conditional classical Kubo/FDT bridge and a falsifiable response matrix for translational/dislocation and orientational/disclination observables; Burgers and Frank data remain conditional on calibrated spatial and frame fields.
- [Exact audit](scripts/audit_t106_born_fdt_defects.py) and [tests](tests/test_t106_born_fdt_defects.py) check the 64-outcome moments, the \(\\mathbb Z_4^3\) bijection, and the distinction between branch winding and pure-gauge \(U(1)\) holonomy. They do not claim physical FDT or material-defect validation.

### T104 — Q6 cycle–cocycle–holonomy law

- [T104 theorem record](theorems/T104-q6-cycle-cocycle-holonomy-law.md) proves the cycle–cocycle–holonomy correspondence on the contractible cubical six-cube over \\(\\mathbb F_2\).
- The 129-dimensional graph cycle space is generated by the 240 square boundaries; the 240 generators have 111 independent relations. The 63-dimensional cut/cocycle space is its orthogonal complement and equals the cubical 1-cocycle space.
- A \\(\\mathbb Z_2\) gauge class is uniquely encoded either by its 129 fundamental-cycle holonomies or by its 240 plaquette fluxes subject to 111 independent cube constraints. Flatness is therefore equivalent to trivial holonomy and a pure-gauge connection on this contractible cube.
- [Cycle/cocycle audit](scripts/audit_t103_cycle_cocycle.py) and [regression tests](tests/test_t103_cycle_cocycle.py) provide the finite exact-algebra certificate. Physical charge assignment to individual hexagrams remains open pending a calibrated measurement map.

### T103 — Q6 Z2 magnetic holonomy and twisted heat trace

- [T103 theorem record](theorems/T103-q6-z2-magnetic-holonomy.md) defines Z2 link variables on the 192 Q6 edges, gauge transformations, all 240 plaquette fluxes, and the magnetic graph Laplacian.
- The exact cubical audit verifies cell counts (64, 192, 240, 160), boundary ranks (63, 129, 111), the 111 independent 3-cell flux constraints, and the (2^{129}) gauge classes. The plaquette-flux map is injective on gauge classes; a flat connection is gauge-trivial on the contractible cube.
- [Audit script](scripts/audit_t103_q6_z2_magnetic_holonomy.py) and [regression tests](tests/test_t103_q6_z2_magnetic_holonomy.py) compute spectra and heat traces for a finite representative set and check gauge invariance. **Exhaustive enumeration of all gauge classes is not attempted.** No supersymmetry in the curved sector, physical hexagram-charge map, continuum limit, or induced-gravity claim is made.

### T101 — Trigram angular phases and Q6 plaquette holonomy

- [T101 theorem record](theorems/T101-trigram-angular-phases-q6-plaquette-holonomy.md) starts from measured phases of all eight trigrams on each of two opposite circles, registers their angular frames, and compares each trigram with its linewise complement on the other circle. It constructs both 64-point Q6 layers on paired two-tori.
- The exact combinatorial audit enumerates all 192 Q6 edges and 240 square plaquettes per layer, reporting the eight cross-circle trigram residuals, all 64 complementary-hexagram mismatches, phase increments, and plaquette holonomies. See [audit script](scripts/audit_t101_trigram_phase_holonomy.py) and [tests](tests/test_t101_trigram_phase_holonomy.py).
- The lifted two-component complement-mismatch field is also evaluated around all 240 Q6 squares. Nonzero integer winding is a candidate phase vortex; it can be interpreted as Frank/disclination or Burgers/dislocation data only after calibrating the phase as a local-frame orientation or translational density-wave phase.
- **Critical identifiability boundary:** endpoint phase differences within either circle layer form a pure-gauge U(1) connection, so their Wilson plaquette holonomies are trivial. This does not erase winding in the *cross-circle mismatch field*. Physical Frank angles and Burgers vectors still require frame or spatial calibration.

### T100 — Hypercube–moiré response, Green–Kubo transport, and geometric defects

- [T100 theorem record](theorems/T100-hypercube-moire-green-kubo-defects.md) treats the 64 individual hexagrams as the primary charge-bearing degrees of freedom; node-charge correlations are primary, while edge currents encode transfers.
- The 64-component charge assignment has an exact Walsh decomposition. Full Q6-automorphism invariance forces a scalar assignment to be constant; a nonconstant law needs justified symmetry-breaking or additional physical structure.
- Ordered-line symmetry classification gives 64 unrestricted values, 36 under line reversal, 7 under arbitrary line permutations, 20 under reversal plus global yin-yang exchange, and 1 under the full cube automorphism group. These are alternative hypotheses, not imposed physical symmetries; the audit compares a measured 64-vector against each invariant subspace.
- A concrete net-polarity candidate q(h)=q0 sum_a epsilon_a has seven binomially degenerate levels and an exact single-walker correlation 6 q0^2 exp(-2 gamma |t|), but its commutator with L(Q6) is nonzero: it is not conserved by one-line hopping. It remains a candidate observable, not an established electric charge.
- An exactly solvable homogeneous thermal-RC benchmark gives time-correlations as a function of Hamming distance. See `scripts/audit_t100_q6_charge_correlations.py` and `tests/test_t100_q6_charge_correlations.py`.
- **Evidence boundary:** the intrinsic charge law and units, physical realization, spatial embedding, transport validation, and defect extraction remain open; the RC kernel is conditional on its declared model assumptions.

### T098 — Universal two-circle positive-gradient / negative-barycentre duality

- [T098](theorems/T098-two-circle-positive-gradient-negative-barycentre-duality.md) is the foundational geometric law: the two equal-radius circles generate the positively oriented gradient triangle and the negatively oriented barycentre triangle as one reflected pair.
- It proves the exact paired-centroid separation, reflection law, positive-triangle mean-gradient boundary identity, covariance transport and Euclidean scale covariance.
- **Derived RGS–Morandotti inheritance:** T098.2 derives the rotational sector from the gradient polar frame (T097), the translational sector from structured-gradient mismatch and Stokes (T079–T080), their ordered closure from Cartan/SE(2) transport (T092–T094), and the barycentric/anisotropic response from T068–T070, T082 and T091.
- No ad hoc Frank-to-Burgers map or universal residual PDE is introduced. The identities are inherited under the precise hypotheses of their source theorems; extraction and validation on the same measured two-core FEM fields remain open.

### T099 — Non-affine vesica and parameter-Koopman bridge

- [T099](theorems/T099-nonaffine-vesica-parameter-koopman-bridge.md) defines the two-ellipse lens with distinct shape matrices, gives its affine classification and exact area/centroid/covariance shape derivatives under transverse boundary intersection.
- It combines those geometric derivatives with the existing T091 Morandotti matrix/residual sensitivity to define a **parameter-Koopman** generator along a declared continuation coordinate (currently the core-separation parameter). This is not presented as physical time evolution.
- [Regression tests](tests/test_t099_nonaffine_vesica_koopman.py) check the exact triangle–disk overlap benchmark, including h = 1 and h = sqrt(3).
- **Open:** extraction of a genuinely non-proportional ellipse path from the same RGS two-core solve, multi-mesh EDMD data and spectral stability, and any autonomous physical-time Koopman flow.

### T099 — Bicircular-annular deformation measurement

- [T099](theorems/T099-bicircular-annular-deformation-reconstruction.md) extends the existing T092/T097/T098 two-circle programme with unequal-radius lens geometry, annular sampling around both centres, least-squares deformation-gradient recovery, Green strain and controlled loop-closure diagnostics.
- [Operational note](docs/BICIRCULAR_ANNULAR_DEFORMATION.md), [implementation](models/bicircular_annular_geometry.py), [five-experiment runner](scripts/run_bicircular_annular_audit.py), and [tests](tests/test_bicircular_annular_geometry.py).
- [Numerical replay report](reports/bicircular_annular_audit.json) — five manufactured checks; independent numerical replay, not CI or physical validation.
- Status: exact lens identities and finite-dimensional affine fitting; manufactured numerical checks; continuum recovery, measured Morandotti fields, Möbius chart transport and constitutive interpretation remain conditional/open.

### T097 — Morandotti Frank–Burgers application of the two-circle programme

- [T097](theorems/T097-barycentric-kinematic-frank-burgers-law.md) is a downstream reconstruction layer, not the foundational two-circle law.
- It combines gradient-derived rotation, structured-mismatch Burgers circulation, barycentric covariance correction and ordered SE(2) composition, using T068–T070, T079–T080, T082 and T091–T095.
- [Component tests](tests/test_t097_barycentric_kinematic_law.py) and [dedicated workflow](.github/workflows/t097-barycentric-kinematic-law.yml) check the component identities. Extraction from the actual two-core Morandotti FE fields remains open.

### T096 — Airy-strain holonomy identifiability gate

- [T096 theorem](theorems/T096-airy-strain-holonomy-nonidentifiability.md) proves that symmetric strain recovered from Airy stress does not determine the skew elastic-distortion field or its Burgers loop closure.
- [Audit runner](scripts/rgs_airystress_holonomy_identifiability.py) and [regression tests](tests/test_rgs_airystress_holonomy_identifiability.py) construct two equal-strain fields with different loop closures; [dedicated workflow](.github/workflows/t096-airy-holonomy-identifiability.yml) checks the witness.
- **Consequence:** measured SE(2) holonomy requires an independently defined displacement/plastic-distortion field, a microrotation model, or an explicitly specified skew-field recovery problem. No loop integral of symmetric strain alone is labelled a Burgers vector.

### Two-Circle geometry to Frank–Burgers holonomy

- [T093 — Conforming global assembly and Cartan-holonomy consistency](theorems/T093-conforming-global-assembly-cartan-holonomy.md) — proves finite seed-cell insertion into a conforming polygonal triangulation and seed-preserving midpoint refinement; establishes a local (O(h_K)) consistency estimate for smooth (SE(2))/Cartan face holonomy, recovering curvature and torsion densities. Singular-core and coupled elasticity convergence remain open.
- [T092 — Local two-circle geometry and the Frank–Burgers holonomy bridge](theorems/T092-local-two-circle-frank-burgers-holonomy-bridge.md) — proves the arbitrarily small local equilateral construction on open planar domains, defines discrete Frank/Burgers closure through ordered $SE(2)$ holonomy, and states the conditional Cartan curvature/torsion bridge. Global assembly, refinement convergence and the elastic continuum limit remain open.

### Morandotti two-core C0-IPDG: Frank–Burgers interaction law and refinement

The two-core reconstruction has passed two successive GitHub Actions audits and both changes are merged:

- [PR #161](https://github.com/fabianleonaressi95/theorem/pull/161) adds the interior-facet traction-jump decomposition into Frank/disclination, Burgers/dislocation, and the signed mixed cross term. It records the additivity residual and total/sector second-moment tensors in laboratory and longitudinal/transverse frames. See [MORANDOTTI_ANISOTROPY.md](MORANDOTTI_ANISOTROPY.md). The [PR audit run](https://github.com/fabianleonaressi95/theorem/actions/runs/43051485760) completed successfully.
- [PR #162](https://github.com/fabianleonaressi95/theorem/pull/162) adds a dedicated DOLFINx 0.11.0 refinement workflow at five mesh sizes, h = 0.08, 0.06, 0.045, 0.035, 0.027, retains the 13 algebraic reconstruction tests, and uploads the JSON report and per-level FE fields. The [five-level refinement run](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448456) and [base two-core audit run](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448351) both completed successfully.

The five-level report records a nonzero signed Frank–Burgers traction cross term in the mixed-source case, with additivity residuals at roundoff level. The exact tensor composition identity, normalized axis-resolved anisotropy formula, and operator variation–residual sensitivity identity are formalized in [T091 — Frank–Burgers tensorial interaction and anisotropy composition law](theorems/T091-frank-burgers-tensorial-anisotropy-composition-law.md). These finite-dimensional identities are proved under their stated hypotheses; the continuum limit, constitutive interpretation and universal distance law remain open. The numerical evidence and limitations are documented in [the two-core audit](docs/rgs_defect_benchmark/MORANDOTTI_TWO_CORE_AUDIT.md).

### FDT / Ratti comparative bibliography

A separate critical appendix integrates S. P. Ratti's supplied primary-document bibliography (D1–D7), the standard physics references on pair production, antimatter, Casimir/Lamb effects and gravitomagnetism, and a falsifiability protocol. It is classified as a comparative case study—not as evidence supporting FDT or RGS–PRISM. D7 remains unread and several source-level metadata items remain unverified. See [Ratti bibliography and critical integration](research/FDT_RATTI_BIBLIOGRAPHY_AND_CRITICAL_INTEGRATION.md).


### T100 — Hypercube–moiré response, Green–Kubo transport, and geometric defects

- [T100](theorems/T100-hypercube-moire-green-kubo-defects.md) treats the 64 individual hexagrams as charge-bearing degrees of freedom: node charges and their pair/time correlations are primary; edge currents encode charge transfer; graph-mode and spatial structure factors test for emergent moiré order; Green–Kubo and Burgers/Frank diagnostics are built from the corresponding dynamical and spatial data.
- **Evidence boundary:** Q6 graph identities are inherited from T099. The charge assignment and its physical units, equilibrium noise/FDT model, mode-to-space embedding, transport validation, and extraction of dislocations/disclinations remain to be derived or measured. The graph Green operator is distinct from the Green–Kubo correlation integral.


### Q6 / Möbius / SU(2) theorem records — 12 November 2026

The implementation source is [rgs-qlg-quaternion-bridge](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge), tracked from [issue #3](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/issues/3). The mathematical results are recorded here:

- [T114 — Q6 gauge-covariant cubical Dirac–Kähler differential](theorems/T114-q6-gauge-covariant-cubical-dirac-kaehler.md): all-degree gauge covariance and spectral invariance, with curvature and Clifford-factor limits stated.
- [T115 — RGS curved Clifford coframe identity](theorems/T115-rgs-curved-clifford-coframe-identity.md): pointwise curved Clifford relation from an invertible coframe; no torsion or field equation inferred.
- [T116 — Non-degenerate integral Kathara-to-Q6 chain map](theorems/T116-nondegenerate-kathara-q6-integral-chain-map.md): exact finite chain identities and modular rank certificate under a declared path-order convention.
- [T117 — Six-square Möbius subcomplex of Q6](theorems/T117-six-square-mobius-subcomplex-of-q6.md): cell structure, homology and non-orientability for the six specified square patterns.
- [T118 — SU(2) path transport and Wilson holonomy](theorems/T118-su2-path-transport-wilson-holonomy.md): open-path covariance, closed-loop conjugation and Wilson-trace invariance on any finite graph.

**Status boundary:** these are finite algebraic/combinatorial results. The Pin/spin lift, torsion, RGS-metric canonicality, continuum limit and physical gauge dynamics remain separate open questions.

### Q6–2I representation compatibility — 12 November 2026

- [T123 — Central-character obstruction and an explicit 2I twist of the Q6 exterior module](https://github.com/fabianleonaressi95/theorem/blob/formalize/q6-2i-central-character-t123-clean-2026-11-12/theorems/T123-q6-2i-central-character-intertwiner.md): proves that the untwisted fundamental-doublet intertwiner vanishes; constructs an explicit embedding into the 128-dimensional doublet-twisted module.

**Status boundary:** the zero-intertwiner result is exact. The tensor twist is an explicit representation-theoretic repair, not a derived physical coupling. A common Pin+(4)/2I bundle structure remains unconstructed.

### 2I / Möbius / Clifford theorem records — 12 November 2026

- [T119 — Binary icosahedral group and selected representations](theorems/T119-binary-icosahedral-group-and-selected-representations.md): 120-element quaternion model, central characters and selected Schur intertwiners.
- [T120 — Möbius orientation cocycle and independent SU(2) fibre](theorems/T120-mobius-orientation-cocycle-and-independent-su2-fibre.md): nontrivial dual-cycle orientation holonomy, separated from the internal gauge field.
- [T121 — Icosahedral A5 action on Q6 and its exterior Clifford module](theorems/T121-icosahedral-a5-action-on-q6-clifford-module.md): signed-axis action and induced 64-dimensional exterior Clifford module.
- [T122 — Pin+(4) lift and Möbius Clifford transport](https://github.com/fabianleonaressi95/theorem/blob/formalize/mobius-pin-plus-clifford-t122-2026-11-12/theorems/T122-pin-plus-mobius-clifford-transport.md): Pin+ lift and Clifford-compatible transport of the specified six-face dual-graph transitions.

**Status boundary:** T119–T122 distinguish exact algebraic statements from floating-point source audits. T122 is a lift of the specified dual-graph transition system, not yet a full tangent-bundle Pin structure over the 2-complex. Torsion, continuum limit and physical gauge dynamics remain separate open questions.

### Frank–Read dislocation source and atomistic core — 12 November 2026

- [T124 — Frank–Read source: line-tension threshold, pinned-curve evolution and atomistic core input](theorems/T124-frank-read-source-line-tension-atomistic-core.md): derives the circular-arc threshold \(\tau_c=2T/(bL)\), audits the factor of two in the common estimate, and separates line-tension mechanics, topological loop emission, atomistic core parameters and possible quantum tunnelling.
- **Critical formula audit:** if \(T=Gb^2/2\), then \(\tau_c=Gb/L\); \(2Gb/L\) requires the alternative convention \(T=Gb^2\). The material-specific threshold needs character-dependent elasticity and core/pinning corrections.
- **Open RGS–PRISM bridge:** encode dislocation lines as Burgers-labelled 1-chains, derive energy and configurational force, and prove convergence of the constrained evolution. No Frank–Read source or tunnelling rate is claimed to have been derived from Q6.

- [T125 — Q6/PRISM Burgers-labelled chains and the variational Frank–Read interface](theorems/T125-q6-prism-burgers-chain-frank-read-variational-interface.md): proves the finite-graph first-variation/nodal force-balance identity and the energy-dissipation identity for an explicitly chosen autonomous gradient flow; closed Burgers-labelled cycles preserve endpoint content. The embedding, Burgers lattice, energy, mobility and pinning law are model inputs; reconnection, Frank–Read emission and mesh-independent convergence remain open.


- [T126 — Exact Burgers conservation under a local equal-vector reconnection](theorems/T126-exact-burgers-conserving-local-reconnection.md): proves that exchanging the heads of two disjoint oriented strands preserves the complete vertex-valued boundary exactly when their Burgers vectors agree; unequal-vector exchange is rejected, and general junctions must satisfy vector-sum conservation. Source implementation and tests are proposed in [source PR #199](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/199); CI is pending. This is a restricted graph rewrite, not a physical reconnection trigger.


- [T127 — Variational acceptance and energy dissipation for Burgers-conserving topology events](theorems/T127-variational-energy-acceptance-topology-events.md): proves that autonomous fixed-topology gradient flow dissipates energy and that a topology update accepted by \(E_{after}+C_{event}\le E_{before}\) has a non-positive energy jump. Together they give a non-increasing hybrid energy and a bound on cumulative event costs. The event cost is a declared model input, not an activation barrier; implementation/tests are proposed in [source PR #200](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/200), CI pending.

### T124 integrated with the verified Morandotti Frank–Burgers Actions

T124 is now connected to the existing Frank–Burgers reconstruction chain in [Chapter 27, §27.5 C1](monographs/RGS_PSU_PRISM_Q6_QLG_MONOGRAPH_27_CHAPTERS.md). The verified computational anchors are [PR #161 / Action run 43051485760](https://github.com/fabianleonaressi95/theorem/actions/runs/43051485760) for the Frank/Burgers/mixed traction-jump decomposition and [PR #162 / five-level refinement run 43052448456](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448456), with [base audit run 43052448351](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448351). T096 and T097 add their dedicated identifiability and kinematic-regression workflows.

**Evidence boundary:** these Actions verify the existing Morandotti reconstruction/decomposition pipeline, not a Frank–Read source simulation. T124's circular-arc threshold is analytic under constant line tension; material-specific activation, loop cutting/reconnection, atomistic calibration, quantum tunnelling and RGS–PRISM continuum convergence remain open.

## Unified programme update — 12 November 2026

The canonical integration is maintained **inside the 27-chapter monograph**, not as a parallel theory: [Chapter 27 — unified RGS–PSU–PRISM–Q6–QLG programme](monographs/RGS_PSU_PRISM_Q6_QLG_MONOGRAPH_27_CHAPTERS.md). Its sections 27.5–27.9 integrate the Morandotti Frank–Burgers chain (T091–T099), the 64-hexagram charge/moiré and FDT chain (T100–T107), the Boolean influence records (T108–T109), KTHNY melting theory, and the toroidal compactification / S-duality interface of \(\mathcal N=4\) SYM.

**The unifying route:** Q6/PRISM cellular geometry → cochains and holonomies → calibrated phase/charge fields → Frank/Burgers defects → Morandotti elasticity → equilibrium correlations/FDT/Green–Kubo → KTHNY defect-unbinding RG. The \(\mathcal N=4\) SYM branch meets this route through toroidal compactification and momentum/winding charge lattices; the matching map is explicitly an open problem.

The finite cubical supersymmetry in T102 is **not** identified with \(\mathcal N=4\) SYM. No direct identification is made between Wilson–'t Hooft charges and Burgers/Frank charges. The note [KTHNY_N4_SYM_RGS_PRISM.md](docs/KTHNY_N4_SYM_RGS_PRISM.md) is a subordinate literature/technical appendix; the monograph and theorem records remain canonical.
