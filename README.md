# THEOREM — RGS–PSU–PRISM–Q6 Mathematical Research Programme

**THEOREM** is the central research repository for a structured programme in discrete geometry, spectral analysis, gauge theory, spin geometry, quantum-light models, and mathematical physics.

It brings together source literature, manuscript records, reproducible computational audits, theorem statements, model implementations, and explicitly tracked open problems. The repository is intended to make each mathematical claim traceable to its assumptions, derivation, implementation, and verification status.

> **Scientific-status policy.** A symbolic proof, a numerical verification, a model-dependent conclusion, and a research hypothesis are different kinds of evidence. This repository labels them separately and does not treat computational agreement as a substitute for proof or physical validation.

## Repository status at a glance (reorganized 2026-11-26)

- **Purpose:** canonical home for theorem-level mathematics of the RGS–PSU–PRISM–Q6 programme — statements, proofs, audits, dependency graphs. Experimental software, datasets and application code live in companion repositories (see `docs/project/`).
- **Theorem register:** every card under `theorems/` is inventoried in **[docs/THEOREM_MASTER_REGISTER.md](docs/THEOREM_MASTER_REGISTER.md)** / **[.csv](docs/THEOREM_MASTER_REGISTER.csv)** — one row per card, with epistemic status, proof type, verification scripts/tests, dependencies and limits. Regenerate with `python3 scripts/build_theorem_register.py`; validate with `python3 scripts/check_theorem_register.py`.
- **Cards:** 280 markdown records in `theorems/` (incl. `theorems/spectral/`). Status distribution (heuristic classification, see register `status_note` column): **PROVED 45, EXACT_CERTIFICATE 14, NUMERICALLY_VERIFIED 86, CONDITIONAL 83, CANDIDATE 6, HYPOTHESIS 2, OPEN 44**. SUPERSEDED/QUARANTINED: 0. *Classification is conservative and machine-assisted; ~100 rows carry a low-confidence note pending author review.*
- **Known numbering issue:** some legacy card prefixes are reused by multiple files, including T154 and T155. The register preserves display IDs but now adds a unique `record_key` (the full filename stem) alongside the file path; graph node IDs use the same slug-based distinction. Renumbering theorem titles remains an author decision.
- **Reproduce checks:** `python3 -m pytest tests/` (unit tests), `python3 scripts/check_theorem_register.py` (register consistency), plus per-workflow audit scripts under `scripts/` and `audits/`.
- **Declared limits:** no card is EXPERIMENTALLY VALIDATED; numerical audits are not proofs; quarantined/unverified material is preserved under `archive/` rather than deleted.

## Research scope
- [Q6–C60 restriction to V4](docs/Q6_C60_V4_EQUIVARIANCE.md) — verified 64D representation equivalence with an explicit orthogonal intertwiner (maximum residual 6.63e-15); all four V4 actions preserve Q6 adjacency. Only R_geo_tangent, not K0/P_G/T_transport, is V4-covariant on the archived 188D space. [Machine-readable audit](audits/Q6_C60_V4_equivariance.json).
- [Q6–C60 V4 face-locality diagnostic](docs/Q6_C60_V4_LOCALITY.md) — transports the archived Q6 adjacency to the 32 C60 face-tangent fibres and measures block support against actual face adjacency; explicitly records the unresolved O(16)^4 intertwiner freedom.
- [Q6–C60 restriction to V4](docs/Q6_C60_V4_EQUIVARIANCE.md) — verified 64D representation equivalence with an explicit orthogonal intertwiner; all four V4 actions preserve Q6 adjacency. Only R_geo_tangent is V4-covariant on the archived 188D space. [Machine-readable audit](audits/Q6_C60_V4_equivariance.json).
- [Q6–C60 V4 face-locality and commutant optimization](docs/Q6_C60_V4_LOCALITY.md) — initial intertwiner has 76.73% nonadjacent energy; numerical optimization over O(16)^4 reduces this to 2.10% while preserving V4 intertwining (6.18e-15), but exact locality remains open. [Optimization report](audits/Q6_C60_V4_locality_optimization.json).
- [Consolidated Q6–C60 equivariance audit (2026-11-26)](docs/Q6_C60_EQUIVARIANCE_CONSOLIDATED_2026-11-26.md) — consolidates the existing O_h/T_h character and 188D tangent-action audits. The actual 32-face C60 tangent representation is not equivalent to the tested Q6 64-state representation; spectral comparison is not authorized.
- [T143 follow-up — antipodal connection and holonomy audit](audits/T143-antipodal-connection-holonomy.md) — reconstructs the minimal SO(3) connection from the archived embedding, checks antipodal link/plaquette equivariance, and tests whether the Spin(3) holonomies admit a common invariant complex line. It separates the exact conditional connection theorem from reconstructed-embedding results; the original-archive certificate covers direct archived-link and all-240-plaquette replay. Direct replay of archived U_SU2 remains open.

The main research strands include:

- [RGS–Ellis radial reparametrization audit (2026-11-27)](audits/RGS_ELLIS_RADIAL_REPARAMETRIZATION_2026-11-27.md) — proves the unique global minimum of the stated areal-radius profile and the exact monotone reparametrization to the Ellis radial form, while explicitly classifying the wormhole identification as conditional on a separately chosen spatial metric. It does not claim that the original RGS ansatz derives the Ellis metric, lapse, Einstein source, or a valid global raccordo.

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
├── .github/workflows/       # Continuous-integration workflows (80)
├── theorems/                # 272 numbered/themed result cards (+ spectral/)
├── foundations/             # Established definitions, laws, results
├── conjectures/             # Unproved hypotheses (reserved; see register)
├── proofs/                  # Standalone formal proofs/certificates (reserved)
├── verification/            # Symbolic/numerical verification suites
├── scripts/                 # Executable research and verification scripts
├── tests/                   # Automated tests (pytest)
├── src/                     # Reusable library modules (dec-se3, RGS, Q6)
├── data/                    # Source datasets (incl. Hysteresis_datasets.xlsx)
├── artifacts/               # Generated results and binary arrays (K0/P_G/Z_*/npz)
├── audits/                  # Reproducible mathematical/computional audits + K0 JSON reports
├── docs/                    # User and research documentation (+ project/ registry)
├── research/                # Dossiers and in-progress research
├── models/                  # Explicit mathematical and phenomenological models
├── experiments/             # Computational experiments
├── reports/                 # Generated report collections
├── manuscripts/             # Manuscript records
├── monographs/              # Book-length syntheses
├── bibliography/            # Source literature, PDFs, formula audits
├── applications/            # Application-specific records
├── collaborations/          # External collaboration records
├── documents/               # Formal documents (e.g. Document A1)
├── evidence/                # Evidence bundles
├── projects/                # Research-strand index (e.g. de Rham benchmark)
├── herasymov_audit/         # Herasymov-related audit material
├── morfodinamica-quantistica/ # Quantum morphodynamics material
├── open-problems/           # Validation matrices and unresolved questions
├── results/                 # Machine-readable JSON/NPZ results
├── library-inventory/       # Library/source inventory
├── archive/                 # Historical/superseded material (dec_se3_legacy, zips, orphans)
├── conftest.py              # pytest configuration
├── pyproject.toml           # Package metadata (dec-se3)
└── requirements-audit.txt   # Pinned audit dependencies
```

### Main indexes
- **[In2Infinity technical contact brief](collaborations/in2infinity/01-initial-technical-contact-brief-2026-11-26.md)** — prepares the independently reconstructed five-solid coordinate/radius results, the unresolved multi-face IN convention, targeted questions for Colin Power and Dr Heike Bielek, and a carefully separated optional (S^3/2I) / Stergios Pellis discussion.
- **[T155-RC→SC — Rhombic cuboctahedron to snub cube](theorems/T155-rhombic-cuboctahedron-snub-cube-transition.md)** — proves exact V/E/F and face-size compatibility of the reported twelve-square split; treats the 22.5° hinge motion, vertex correspondence and chirality as open. [incidence-count test](tests/test_t155_rhombic_cuboctahedron_snub_cube.py).
- **[Sangaku Geometry — circle-construction classification](research/sangaku_geometry/README.md)** — independent workstream classifying marked circle configurations by incidence/tangency structure, Euclidean symmetry and normalized coordinate/distance fields. Includes the proved quadratic-tower theorem for intersection constructions, exact Vesica Piscis and pentagon records, a clearly conditional tangency model, SymPy checks and a source-verification protocol.
- **[In2Infinity technical contact brief](collaborations/in2infinity/01-initial-technical-contact-brief-2026-11-26.md)** — prepares the independently reconstructed five-solid coordinate/radius results, the unresolved multi-face IN convention, targeted questions for Colin Power and Dr Heike Bielek, and a carefully separated optional (S^3/2I) / Stergios Pellis discussion.
- **[T154-I2I — In2Infinity Extended Jitterbug source and geometry audit](theorems/T154-in2infinity-extended-jitterbug-audit.md)** — records the source's five-solid sequence, IN/MID/OUT sphere model, truncation and 81-element radius claims; proves the explicit cuboctahedron decomposition and its polar rhombic-dodecahedron coordinates; keeps the five-solid interpolation and physical claims open. [source review and validation protocol](audits/in2infinity/T154-source-review-2026-11-26.md).
- **[T156 — Rhombicuboctahedron-to-snub-cube incidence correspondence](theorems/T156-rhombicuboctahedron-snub-cube-incidence.md)** — identifies the 12 lateral squares in the cupola/prism decomposition and exhaustively checks all 4096 diagonal assignments; exactly the two alternating patterns reproduce the snub-cube vertex-face incidence structure. The 22.5° rigid motion and chirality map remain open. [audit](scripts/audit_t156_jitterbug_incidence.py) · [test](tests/test_t156_jitterbug_incidence.py).
- [Vesica–Moiré TM_z Maxwell polarization audit](docs/VESICA_MOIRE_TMZ_MAXWELL_AUDIT.md) — a 2-D TM_z polarization-reduced Maxwell generalized eigenproblem with an explicitly assumed positive dielectric modulation, PEC boundary conditions, an exact uniform-grid spectral control, focused tests and a small CI workflow. This is not a full 3-D solver and does not derive optical frequencies from Vesica geometry. [solver](audits/vesica_moire_tmz_maxwell.py) · [tests](tests/test_vesica_moire_tmz_maxwell.py) · [workflow](.github/workflows/vesica-moire-tmz.yml).
- [Vesica Piscis–Moiré–RGS research note](docs/VESICA_MOIRE_RGS_RESEARCH.md) — exact \(\sqrt3\) Vesica geometry, radial-grating phase difference and local fringe-spacing derivation; includes a reproducible scalar graph-Laplacian audit and a carefully delimited open programme for compatible discrete Maxwell. The scalar model is not a Maxwell solver and makes no optical-spectrum prediction. [audit script](audits/vesica_moire_2d.py) · [tests](tests/test_vesica_moire_2d.py).
- [Vesica–square–barycentre–dodecahedron–Q6 bridge](research/VESICA_SQUARE_BARYCENTRE_DODECAHEDRON_Q6_BRIDGE_2026-11-24.md) — exact inscribed-square, triangle-centroid and barycentric-gradient construction; isolates the missing dodecahedral-to-Q6 operator lift needed to derive the existing interpolation polynomial geometrically.

- **[T155-DG — Dodecahedral Gauss-map Levi-Civita connection and covariant Hodge operator](theorems/T155-dodecahedral-gauss-map-levi-civita-hodge.md)** — constructs the 12-face SO(2) connection by minimal rotations of the primal icosahedral face normals; verifies antipodal frame covariance, each triangle's holonomy/area identity and the 4π Gauss–Bonnet total; the spectrum is regression-tested against both recorded controls. It assembles a geometric finite-volume Hodge operator. Its spectrum remains distinct from Q6 (0,4,6); extension to the full 32–90–60 Whitney complex and derivation of f remain open. [script](scripts/audit_t155_dodecahedral_levi_civita_hodge.py) · [tests](tests/test_t155_dodecahedral_levi_civita_hodge.py) · [workflow](.github/workflows/t155-levi-civita-hodge.yml).
- **[T157 — Full 32–90–60 link-covariant Whitney model with curvature defect](theorems/T157-full-covariant-whitney-curvature.md)** — extends the T155 Gauss-map connection to all 32 centroid-fan nodes and 90 edges; constructs link-transported Whitney masses and a curvature-aware (D_0^A,D_1^A) sequence. The exact curvature identity `D_1^A D_0^A u=(1-H_{ijk})U_{ji}u_j` is audited on all 60 triangles; holonomies sum to (4\pi), gauge/antipodal covariance and positive masses pass. This is intentionally not a flat cochain complex; continuum connection, refinement convergence and the Q6/RGS map remain open. [script](scripts/audit_t157_full_covariant_whitney_curvature.py) · [tests](tests/test_t157_full_covariant_whitney_curvature.py) · [workflow](.github/workflows/t157-covariant-whitney.yml).
- **[T158 — Interior pullback Levi-Civita connection and path-transported Whitney masses](theorems/T158-interior-pullback-covariant-whitney.md)** — specifies the piecewise-smooth normal map inside every 32–90–60 triangle, pulls back the unit-sphere Levi-Civita connection, and integrates path-transported Whitney masses. Order-8/order-12 quadrature agrees at about 10⁻¹⁴; T155 edge links, curvature defect, gauge covariance, positive masses and Hodge spectra pass. the covariant Whitney commuting-defect estimate, mesh-refinement convergence, a curved-FEEC error theorem and the Q6/RGS map remain open. [script](scripts/audit_t158_interior_covariant_whitney.py) · [tests](tests/test_t158_interior_covariant_whitney.py) · [workflow](.github/workflows/t158-interior-covariant-whitney.yml).
- **[T159 — Curved dodecahedral FEEC mesh-refinement audit](theorems/T159-curved-feec-mesh-refinement.md)** — refines the fixed T158 parent normal map through factors 1–4 (32–90–60 to 482–1,440–960); antipodal covariance, curvature identity, Gauss-map holonomy and order-8/order-12 quadrature checks pass. The lowest covariant Hodge-0 triplet stabilizes numerically, but the covariant Whitney consistency defect, spectral convergence, Q6 intertwiner and derivation of f remain open. [script](scripts/audit_t159_curved_feec_refinement.py) · [tests](tests/test_t159_curved_feec_refinement.py) · [workflow](.github/workflows/t159-curved-feec-refinement.yml).
- **[T156 — Vesica–Möbius elastic torsion and Farey half-threshold](theorems/T156-vesica-mobius-elastic-farey-half.md)** — separates the three half-thresholds and records the exact projective conjugacy. Adds a candidate Vesica aspect-ratio map and a finite-width symmetric Möbius BVP implementation with regularized switching-point continuation; physical selection and FDT identification remain open. [algebra audit](scripts/audit_t156_vesica_mobius_farey.py) · [elastic BVP](scripts/solve_t156_mobius_elastic_bvp.py) · [tests](tests/test_t156_vesica_mobius_farey.py) · [BVP tests](tests/test_t156_mobius_elastic_bvp.py) · [workflow](.github/workflows/t156-mobius-elastic-bvp.yml).
- **[T149 — Supergolden dodecahedral Whitney–Hodge construction](theorems/T149-supergolden-dodecahedral-whitney-hodge.md)** — executes the 32–90–60 centroid-fan FEEC assembly at the supergolden parameter and the regular φ control; verifies incidence, antipodal mass invariance, positive Whitney masses, parity spectra and scalar Schur condensation. The canonical Q6 intertwiner fails (residuals 5.7099 and 2.1937); T155 constructs the face-centred Levi-Civita connection and T157 extends it to a finite link-covariant Whitney model on all 32–90–60 cells. T158 now specifies a piecewise-smooth pullback connection inside each triangle; mesh-refinement convergence, a curved-FEEC error theorem, the Q6/RGS map and derivation of f remain open. [script](scripts/audit_t149_dodecahedron_feec_hodge.py) · [tests](tests/test_t149_dodecahedron_feec_hodge.py) · [workflow](.github/workflows/t149-feec-hodge.yml).\n- **[T146 — Dodecahedral dual-face barycentres lifted into Q6](theorems/T146-dodecahedral-dual-q6-barycentre-spectral-audit.md)** — exact 20-vertex/30-edge polar-dual incidence, antipodal-equivariant T141 face-barycentre lift, Q6-pulled-back and polar-metric Laplacians; records the failed ((0,4,6)) intertwining test rather than fitting weights. [script](scripts/audit_t146_dodecahedron_q6_dual_barycentre.py) · [tests](tests/test_t146_dodecahedron_q6_dual_barycentre.py) · [workflow](https://github.com/fabianleonaressi95/theorem/actions/runs/45452516147).
- **[T147 — Golden tangential spectrum of the Fibonacci period-two trace orbit](theorems/T147-golden-tangential-spectrum-fibonacci-period-two.md)** — exact period-two branch, corrected monodromy, invariant limiting Fricke tangent plane, golden restricted spectrum \(\varphi^{\pm4}\), quadratic Fricke-level asymptotics, and convergence of regular tangential Floquet multipliers. Symbolic theorem; no numerical fitting.
- **[T148 — Elliptic order-three tangential spectrum at the singular Fibonacci period-two endpoint](theorems/T148-elliptic-order-three-fibonacci-period-two-singularity.md)** — exact analysis of the other endpoint \(p_0=(0,0,0)\): invariant limiting tangent plane, order-three orthogonal restriction with eigenvalues \(e^{\pm2\pi i/3}\), and quadratic scaling \(I(p(x))+1\sim3x^2\). Symbolic theorem; no numerical fitting.
- **[T145 — intrinsic ℤ₂ grading of the RGS carrier](theorems/T145-square-reflection-prism-biverse-rgs-carrier.md)** — verifies (S=2Z_S|_{\mathcal W}), rank-three parity projectors and the off-diagonal (Z_A) coupling; explicitly records that (K_0) mixes the grading sectors, so the grading does not explain its affine half-offset.

- **[Factor 1/2, Liouville and literature dossier](theorems/FACTOR_HALF_ORIGINS_LIOUVILLE_LITERATURE_2026-11-24.md)** — integrates the established Liouville theorem, the D5 Bergman density, the Q6 Wilson marginal chain T003–T009, the PSU para-Kähler bridge, the RGS six-dimensional half-scale carrier, and the distinct algebraic, geometric, analytic and physical origins of 1/2. Separates proved results, numerical evidence and open identifications.

- **[Unified 27-chapter crosswalk and preservation register](research/UNIFIED_PROGRAM_27_CHAPTER_CROSSWALK_2026-11-24.md)** — connects all 27 chapters to theorem clusters, companion-repository materials, arithmetic/special-function results, Vesica, fractals, Minkowski–Farey, QAT, Green–Kubo and polariton literature; records epistemic caveats and the 236/239 inventory reconciliation.


- **[TSMR-I — Singular cumulative-coordinate pentagonal lift](theorems/TSMR-I_singular_cumulative_pentagonal_lift.md)** — constructs an isometry from the regular-pentagon real DFT decomposition into L² of an atomless interval-supported measure via its cumulative distribution; proves the exact projector intertwining JνP=Πν,1Jν. For the golden Bernoulli measure, its singular CDF supplies the uniform probability coordinate. The exact isometric lift is proved; a reproducible finite-sample audit finds nonzero Markov off-diagonal blocks (so dynamical invariance is numerically falsified, pending an exact non-vanishing proof). Audit and tests: `audits/tsmr_i_cumulative_pentagon.py`, `tests/test_tsmr_i_cumulative_pentagon.py`.

- **[TSMR-I Markov block audit](results/tsmr_i_golden_markov_blocks.json)** — deterministic-seed empirical-CDF evaluation of the golden Markov operator; both off-diagonal blocks are nonzero, distinguishing the exact projection lift from a false dynamical-intertwining claim. Source and tests: `audits/tsmr_i_markov_blocks.py`, `tests/test_tsmr_i_markov_blocks.py`.


- **[TSMR-I finite memory reduction](theorems/TSMR-I_singular_cumulative_pentagonal_lift.md#8-feshbachmori-reduction-finite-harmonic-memory-model)** — finite 2+2 Feshbach reduction after separating the invariant constant mode; records the frequency-dependent self-energy and decaying second-harmonic memory kernels. Audit/tests: `audits/tsmr_i_memory_reduction.py`, `tests/test_tsmr_i_memory_reduction.py`.


- **[TSMR-I finite memory reduction results](results/tsmr_i_memory_reduction.json)** — stored (2+2) Galerkin/Feshbach values: second-harmonic spectral radius, memory-kernel decay, and self-energy at (z=1). Scope is explicitly finite-dimensional.

- **[TSMR-H — Half-balance principle](theorems/TSMR-H_half_balance_fractal_pentagon.md)** — proves the Bernoulli first-level overlap threshold at λ=1/2, the maximum-entropy probability p=1/2, and the pentagonal projector balance ||Pq||²=1/2; distinguishes the golden singular Bernoulli regime λ=φ⁻¹ from the uniform critical model and keeps the De Aquino coupling conditional. Reproducible audit: `audits/tsmr_h_half_balance.py`; tests: `tests/test_tsmr_h_half_balance.py`.

- **[Unified theorem dependency graph](docs/UNIFIED_THEOREM_DEPENDENCY_GRAPH.md)** — all 280 theorem records and 14 companion catalogue entries are represented in a 334-node, 370-edge graph; see the machine-readable [edge registry](docs/UNIFIED_THEOREM_EDGES.json).
- **[Unified two-repository theorem programme](docs/UNIFIED_TWO_REPOSITORY_THEOREM_PROGRAM.md)** — master architecture for the theorem inventory, proof-status schema, cross-repository dependencies, and the shared Pellis/Morandotti workstreams. The current revision inventories 280 theorem Markdown records in this repository; the companion RGS–QLG repository is linked by explicit typed arrows in the dependency graph.
- **[Unified two-repository theorem programme](docs/UNIFIED_TWO_REPOSITORY_THEOREM_PROGRAM.md)** — master architecture for the theorem inventory, proof-status schema, cross-repository dependencies, and the shared Pellis/Morandotti workstreams. The current revision inventories 280 theorem Markdown records in this repository; the companion RGS–QLG repository is linked by explicit typed arrows in the dependency graph.


- **[Ricostruzione dalle fondamenta](monographs/00_FROM_FIRST_PRINCIPLES_LIGHT_CUBE_SPHERE_PHI_PSU_QAT.md)** — luce e unità di Planck, cubo-sfera, derivazione π→φ, icosaedro/quaternioni/2I, PSU–Anti-Twin, Q-ball, QAT e interfaccia Calabi–Yau. È il punto di partenza della ricostruzione; Q6 e PRISM vengono dopo.

- [Morandotti benchmark I — discrete Saint-Venant KKT specification](manuscripts/MORANDOTTI_BENCHMARK_I_DISCRETE_SAINT_VENANT_KKT.md) — finite-dimensional constrained energy, implemented generic KKT solver and energy assembly, D1–D3 defect tests and Airy/CIP-DG comparison gates; CI execution, continuum convergence and physical validation remain open.
- **[Integrated 27-chapter monograph](monographs/RGS_PSU_PRISM_Q6_QLG_MONOGRAPH_27_CHAPTERS.md)** — consolidated reference for Q6, Q6-D5/Wilson, 2I/Rumin, RGS 188D, PRISM/Krist-All, FEEC/Mosco, QLG, Einstein–Cartan/teleparallelism, QAT, XCont and hysteresis. Includes explicit epistemic status and recovery caveats.
- **[Rubino–QAT–quaternionic SU(2) bridge](docs/RUBINO_QAT_QUATERNIONIC_SU2_BRIDGE.md)** — source audit of Rubino's tensorial parallel-transport discussion, quaternionic QAT-current covariance, the coframe/spin-connection reduction, and the exact finite-graph result already proved in T118; the Q6 continuum limit and unified field equations remain open.
- [Canonical synthesis and closure programme](manuscripts/SINTESI_CANONICA_RGS_PSU_PRISM_Q6_QLG.md) — short strategic overview.

- **[Document A1 — Exact scalar spectrum of the Poincaré spherical space](documents/DOCUMENT_A1_EXACT_SPECTRAL_GEOMETRY_S3_2I.md)** — exact (2I)-invariant harmonic multiplicities on (S^3/2I), derived from the binary Molien series and independently checked by the nine-class Reynolds character average through degree 120.
- [A1 exact character/Molien audit](audits/a1_poincare_scalar_spectrum.py) and [regression tests](tests/test_a1_poincare_scalar_spectrum.py).
- [Bibliography and source catalogue](bibliography/README.md)
- [Special functions and Morandotti bibliography](bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md)
- [PDF master inventory (30 PDFs; organized 18 November 2026)](audits/PDF_MASTER_INVENTORY.md) — complete file map, provenance classes and quarantine register.
- [Focused mathematical/source audit (13 PDFs; 10 November 2026)](audits/2026-11-10_pdf_repository_audit.md) — detailed source and formula audit for the original 13-file snapshot.
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

- [Vesica Piscis–Needham–Bonilla dossier: \u221a3, cube roots of unity, hexagon, pentagon and \u03a6](docs/VESICA_NEEDHAM_BONILLA_SQRT3_PHI_DOSSIER_2026-11-18.md) — exact Vesica ratio and converse-source audit, Needham's third-roots geometry, and the carefully delimited construction chain to the pentagon/hexagon discussion.
- [T137 — Exact geometry of the Vesica Piscis and the \(\sqrt3\) hexagonal chord](theorems/T137-vesica-piscis-two-circle-hexagon-pi-sqrt3.md) — proves the chord, arc-length and area formulae for the equal-circle Vesica and identifies its common chord with the short diagonal of a regular hexagon; a new DtN spectral identity remains open.
- [64-TG–Vesica–Morandotti audit](docs/64TG_VESICA_MORANDOTTI_BRIDGE.md) — audits Galeffi's 14-octahedron/64-tetrahedron geometry, corrects the tetrahedral face-area arithmetic, and sets out the conditional circumsphere–Vesica, barycentric-covariance and phase-gradient bridge.
- [64-TG exact FCC/D3 coordinates](data/64tg_fcc_coordinates.json) — explicit 63-vertex coordinate set reproducing 240 edges, 64 regular tetrahedra, 14 octahedra, 24 square pyramids, 360 pairwise circumsphere lenses and 648 common triple overlaps; includes exact barycentres/covariance tensors and the [audit script](scripts/audit_64tg_fcc_coordinates.py), [unit tests](tests/test_64tg_fcc_coordinates.py) and [GitHub Action](.github/workflows/64tg-fcc-coordinates.yml).
- [T142 — Antipodal six-state model of the Vesica hexagon and geometric mixing](theorems/T142-vesica-antipodal-six-state-mixing.md) — proves the exact even/odd decomposition and the coordinate-operator block ranks 3 (real part) and 2 (imaginary part); the isometric Q6 transfer and physical PSU–Anti-Twin interpretation remain open. [audit](scripts/audit_t142_vesica_antipodal_six_state.py), [tests](tests/test_t142_vesica_antipodal_six_state.py).
- [T143 — Vesica embedding with the geometric RGS AntiTwin](theorems/T143-vesica-q6-isometric-antipodal-embedding.md) — corrects the involution to the archive-documented rule g ↦ g ⊕ 7, lists all 32 canonical representatives, fixes the Vesica pairs (2,5), (3,4), (9,14), and defines the unambiguous 29-angle diagonal family. SO(3)/SU(2) holonomy-based phase selection remains open. [audit](scripts/audit_t143_vesica_q6_embedding.py), [tests](tests/test_t143_vesica_q6_embedding.py).
- [T143-A — Antipodal equivariance of the minimal SO(3)/SU(2) connection](theorems/T143A-antipodal-equivariance-minimal-so3-su2-connection.md) — proves exact link, path/cycle holonomy and quotient-connection equivariance under the antipodal-normal and canonical-lift hypotheses.
- [T143-B — Original archive and 240 Q6 plaquette certificate](audits/T143B-original-archive-q6-plaquette-certificate.md) — direct numerical formula fit, all 192 archived links, all 240 original plaquette holonomies, 32-vertex quotient graph, and the K_fibre Anti-Twin commutator audit. Generator provenance remains open.
- [T143-C — Clifford symmetry of the fibre operator](theorems/T143C-clifford-symmetry-fibre-operator.md) — conditional algebraic theorem: three anticommuting involutions imply Anti-Twin commutation and even eigenvalue multiplicity in each parity sector; the archived K_fibre realization is numerically audited in T143-B.
- [T143-D — Anti-Twin isospectrality from the normal operator](theorems/T143D-antitwin-isospectrality-normal-operator.md) — proves that a covariantly constant normal operator, anticommuting with the deck involution, unitarily identifies the two parity-sector restrictions of a compatible Hermitian operator.
- [Vesica anisotropic multimode operator and DtN audit](docs/VESICA_ANISOTROPIC_DTN_MODEL.md) — full-domain moving transverse basis, corrected variational index contractions, Hamiltonian transfer system, reproducible quadrature audit and explicit high-mode conditioning limits; [audit script](scripts/audit_vesica_anisotropic_dtn.py), [tests](tests/test_vesica_anisotropic_dtn.py).\n- [Theorem records](theorems/)
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

- [PR #161](https://github.com/fabianleonaressi95/theorem/pull/161) adds the interior-facet traction-jump decomposition into Frank/disclination, Burgers/dislocation, and the signed mixed cross term. It records the additivity residual and total/sector second-moment tensors in laboratory and longitudinal/transverse frames. See [MORANDOTTI_ANISOTROPY.md](docs/MORANDOTTI_ANISOTROPY.md). The [PR audit run](https://github.com/fabianleonaressi95/theorem/actions/runs/43051485760) completed successfully.
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
- [Exact quaternionic 2I real Molien audit](audits/2i_real_molien_exact/README.md): exact Q(√5) construction and closure of all 120 elements, 4×4 left-multiplication determinant audit, and real Molien coefficients through degree 60.
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


### T128 — Purcell swimmer and the Q6 geometric-control interface

[T128](theorems/T128-purcell-swimmer-q6-geometric-control.md) records the continuous Purcell-swimmer connection/holonomy framework and the exact requirements for a Q6 discretization. A first-pass quadrature reconstruction is stored in [the audit directory](audits/purcell_swimmer_wall/README.md). The corrected reconstruction reproduces the published leading coefficient: at amplitude 10^-3 it gives approximately 0.06172485, approaching 5/81 ≈ 0.0617284, with stable results for quadrature orders 16–96. The initial control vector fields also match the analytic values. The Q6-to-shape-space map and discrete swimmer remain open. The article documents MATLAB/ode45, not DOLFINx or PyTorch.


- **T129 — Icosahedral equivariance obstruction and calibrated Q6–Purcell map:** [theorem record](theorems/T129-a5-equivariance-obstruction-and-calibrated-q6-purcell-map.md). The recovered golden internal projection retains all six Q6 edge directions (192 edges). Under the standard irreducible icosahedral \(A_5\) action, no nonzero linear globally equivariant map from the internal 3-space to a real 2D control space exists. A nonzero shape map therefore requires an explicit calibration frame \(B\) and scale \(\kappa\); the candidate \(\Phi_{B,\kappa}(v)=\kappa B P_\perp(v-\tfrac12\mathbf1)\bmod 2\pi\) uses every Q6 direction. The local edge transport is a one-step midpoint approximation in \(SE(2)\), not yet a convergent discrete connection. Audit code and tests are in the Purcell swimmer audit directory.
### T129 — Golden Q6 cut-and-project map and Purcell edge transport

[T129](theorems/T129-q6-cut-project-purcell-shape-map.md) now constructs a parameterized map from all 64 Q6 vertices through the recovered golden internal projection (P_\perp\) into the two-angle shape chart: \(\Phi(v)=s_0+\sigma C P_\perp(v-\frac12\mathbf1)\). All six cut-and-project axes and all 192 edges are retained (32 edges per axis), and the six projected vectors and their Gram matrix are exported so anisotropy can be measured rather than assumed. The calibration \(C\in\mathbb R^{2\times3}\) is explicitly left as an input: the 3D internal space does not select a canonical 2D shape plane; the icosahedral A5 symmetry also forbids a nonzero equivariant projection onto a 2D module. The wall-dependent swimmer connection also produces state-dependent edge transport by integrating the continuous connection along each shape edge; a fixed universal \(U_e\) is not assumed. Finite structural and reversibility tests are added. Physical calibration, 192-edge holonomy, and refinement convergence remain open.


### T130 — Q6 gradients, barycentres, moments and resistance

[T130](theorems/T130-q6-discrete-gradients-barycentres-resistance.md) adds a local least-squares shape-gradient reconstruction on the Q6 graph, weighted geometric barycentres, traction resultants and moment-origin shifts, and a positive local-drag resistance assembly (R_h=\sum_i w_iJ_i^TD_iJ_i). Its Schur complement gives the finite force-free connection and shape dissipation metric. This is an algebraic/local-drag interface, not a nonlocal Stokes or BEM solver; physical quadrature, shape Jacobians, wall-corrected hydrodynamics and continuum convergence remain open.

- [T131 — Q6 phonon–phason normal modes and Green–Kubo transport](theorems/T131-q6-phonon-phason-green-kubo-transport.md) — finite generalized normal modes, polarization diagnostics and finite-window stress Green–Kubo estimator; explicitly separates the bare Q6 graph spectrum from material dispersion and leaves physical Hessian, phason kinetics, anharmonic relaxation and converged transport open. [audit](audits/phonon_phason/normal_modes_kubo.py), [tests](tests/test_t131_phonon_phason_kubo.py).


### T132 — Exact coupled phonon–phason OU benchmark

[T132](theorems/T132-coupled-phonon-phason-ou-green-kubo.md) adds an exactly solvable two-coordinate reversible Ornstein–Uhlenbeck benchmark with coupled phonon/phason coordinates and three declared stress sectors (phonon, phason, interaction). Wick's identity gives every ordered correlation block analytically; the nine blocks recombine exactly into the total-stress correlation, and zero-field reciprocal symmetry is checked against a seeded exact-step stochastic trajectory. This validates sector bookkeeping and the numerical benchmark only: the OU bath and synthetic stress matrices are not a calibrated material relaxation model or a material viscosity. [implementation](audits/phonon_phason/coupled_ou_green_kubo.py), [tests](tests/test_t132_coupled_ou_green_kubo.py).


### 12 November 2026 — finite audit execution record

The following theorem-associated GitHub Actions runs completed successfully:

- T103/T104 Q6 cycle-cocycle: 11 tests; cycle rank 129, cocycle rank 63, H1=0. [Run #43245722504](https://github.com/fabianleonaressi95/theorem/actions/runs/43245722504).
- T105 hexagram/moiré circuit: 8 tests; deterministic audit PASS. [Run #43245721916](https://github.com/fabianleonaressi95/theorem/actions/runs/43245721916).
- T107 Gray-torus Gibbs/FDT: 5 tests; deterministic audit PASS and Gray graph isomorphism true. [Run #43245722241](https://github.com/fabianleonaressi95/theorem/actions/runs/43245722241).
- T131/T132 phonon-phason benchmark: module compilation and 11 tests passed. [Run #43245274034](https://github.com/fabianleonaressi95/theorem/actions/runs/43245274034).

These are finite mathematical/software checks. They do not establish physical calibration, material transport coefficients, or experimental validation.

### T135 — Bernstein–Neumann certified rational integration

- [T135](theorems/T135-morandotti-bernstein-neumann-certified-rational-integration.md) formalizes rational integration on triangles by integrating a finite Neumann polynomial exactly and enclosing its rational residual with Bernstein coefficient ratios. It proves local and global inclusion, the geometric width bound
  \\[
  \\operatorname{wid}(\\mathbf I_{T,N})\\leq
  \\frac{2|T|A_T}{\\gamma_T}\\rho_T^{N+1},
  \\]
  exact width additivity for the usual sum of intervals, and finite-order termination on an already certified finite partition. Degree-elevation conventions for both numerator and denominator are explicit. The Bernstein quotient enclosure is attributed to the pre-existing 2022 paper; novelty and complexity claims remain open. The 55 actual curved-P3 entries, complete IPDG assembly and LDL propagation are separate validation gates.

### T136 — Tetrahedral volume moments and conditional Ricci reconstruction

- [T136 — Tetrahedral volume moments, local Ricci reconstruction, and the Q6 curvature gate](theorems/T136-tetrahedral-volume-moment-reconstruction-ricci-q6.md) records the normal-coordinate expansion, conditional six-component Ricci inverse problem, and separation of Regge from Q6 curvature functionals. Finite audits cover constant-curvature, anisotropic, and smooth non-quadratic metrics; the 12-probe D-optimal design improves conditioning and finite-test bias/noise sensitivity. A Frobenius-weighted covariance audit selects grid scales 0.00375 (six probes) and 0.00210 (twelve probes) for one manufactured metric and relative-volume noise level $10^{-9}$; these are not universal scales. General-metric stability, universal scale selection, Regge convergence, and the Q6 continuum correspondence remain open.



### T138 — Exact C6 two-sheet decomposition and the Spin(3) distinction

### Fibonacci–Fricke periodic orbits and Q6 antipodal hexagrams — 25 November 2026

- [Pellis / Golden Spheres Resonance — open-problems register](open-problems/PELLIS_GSR_OPEN_PROBLEMS.md) — 11 prioritized questions covering the Pellis coefficients, operator/state selection, golden scale, binary-icosahedral selection rules, two-sheet geometry, three-mode symmetry, and continuum limits; all unresolved gates remain explicitly open.
- [Pellis correspondence — Fibonacci transfer, Fricke dynamics, and the Q6 antipodal orbit](docs/PELLIS_FIBONACCI_Q6_TWO_SHEET_BRIDGE.md): records the exact `SL(2)` Fibonacci trace recursion, the corrected orientation-reversing Jacobian determinant `det DT=-1`, the neck matching factor `2bd=0`, the D6/two-triangle and Q6 antipodal structures, and the remaining operator-intertwining requirements. It separates trace dynamics from the full matrix-entry data needed for Pellis resonances.

- [T149 — Exact symmetric period-three and period-six Fibonacci–Fricke orbits](theorems/T149-symmetric-fibonacci-fricke-period-three-period-six-orbits.md): corrects the Jacobian determinant to `det DT=-1`, factors the symmetric `T^6`-fixed locus into branches A (period six), B (period two), and C (period six), records the A/C endpoint collisions at `p_0` and the period-three orbit, and proves the exact trace-cube identity linking the C period-six traces at `c=4` to the period-two traces. The classification is restricted to the reversor-symmetric locus; the singular period-three spectrum is ambient.
- [T150 — D6-equivariant Fibonacci hexagonal orbit and Q6 antipodal two-sheet correspondence](theorems/T150-d6-fibonacci-hexagram-antipodal-two-sheet-correspondence.md): proves an explicit `D_6`-equivariant bijection between a reversor-symmetric Fibonacci period-six orbit and the six-state Q6 orbit of `000|111`, with `T^3=J` on that suborbit. It distinguishes the two alternating vertex triangles of the geometric Star of David from the consecutive lower/upper trigram blocks of an I Ching hexagram, and identifies the ambient order-three linearization at `p_0` with the real three-vertex `C_3` representation. Globally Q6 has 32 antipodal pairs. The full 64-state/Q6-operator and physical Pellis intertwiners remain open.

**Connection to T147–T148:** T147 and T148 are the two distinct singular endpoint limits (p_1=(1,1,1)) and (p_0=(0,0,0)) of the same period-two branch. T149 adds other symmetric periodic families; T150 supplies the exact orbit-level D6/hexagram bridge. None of these finite dynamical results alone identifies the physical Pellis transfer operator.

- [T138 — Exact two-sheet decomposition of the six-dimensional icosahedral matrix](theorems/T138-c6-exact-two-sheet-spin3-decomposition.md) proves over the integers that the displayed symmetric matrix satisfies \(C_6^2=5I_6\), establishes its \(3+3\) orthogonal eigenspace splitting, gives the graph parametrization of both sheets and records the induced \(\Lambda^2\) spectrum. It distinguishes a real Euclidean 3-space and its \(SO(3)\)/Spin(3) frame symmetry from an intrinsic quaternionic module.
- Reproducibility: [exact integer audit](scripts/audit_t138_c6_two_sheet_spin3.py) and [regression tests](tests/test_t138_c6_two_sheet_spin3.py).
- **Open gate:** no six-index \(2I^*\) generator action has yet been supplied or shown to commute with \(C_6\). The representation types of the sheets, a specific \(2I^*\) lift, and any physical/De Aquino interpretation remain open.


- **T151 — Spectral expectation weights:** an exact lemma showing that a diagonal spectral expectation is a convex combination of eigenvalues and that a target value does not uniquely determine modal weights without an independent state-selection principle. This audits the expectation-value construction in the Golden Spheres Resonance preprint without ruling out a future variational derivation.


### T152 — Binary McKay–ADE, Calabi–Yau orbifolds and crepant resolutions

- **Graph reconciliation (27 November 2026):** the live inventory contains 280 theorem records, 14 companion catalogue entries, 334 graph nodes and 370 directed edges. MQ-T005 is indexed under RGS; both T154 records and both T155 records remain distinct by canonical filename stem. The Liouville half-factor literature dossier is excluded. The 60 direct typed crosswalks are unchanged; provisional topic arrows are not proof dependencies.

- [T152 — Binary McKay–ADE correspondence, Calabi–Yau orbifolds and crepant resolutions](theorems/T152-mckay-ade-calabi-yau-crepant-resolutions.md) — integrates the \(2I\subset SU(2)\), \(\mathbb C^2/2I\), affine \(\widetilde E_8\) and minimal crepant resolution chain; distinguishes the surface theorem from the threefold \(G\)-Hilb/BKR derived equivalence and the special, non-general existence problem in dimensions \(n>3\). Cross-links T119, T121, T144, T146, A1 and T027 without duplicating their audits or claiming an unproved RGS/Q6 operator identification.


### T153 — Pyramid bisection, polyhedral duality and the inter-sheet complex structure

- [T153](theorems/T153-pyramid-cuboctahedron-rhombic-dodecahedron-j-complex-connection.md) formalizes the exact bisection of a square pyramid into two equal-volume tetrahedra, the cuboctahedron's tetrahedron/half-octahedron decomposition, cuboctahedron–rhombic-dodecahedron duality, Euler/angle-defect relations, and the distinction between soap-film form-finding and geometric torsion. It audits the supplied In2Infinity molecular/quantum/orbital claims without promoting them to established physics.
- The central (J)-question is answered conditionally: (J) may be required to be parallel under a discrete connection, but this alone does not define torsion. A coframe, connection, discrete torsion operator and convergent refinement are still required. If the two sheets carry the inequivalent (A_5) modules (3) and (3'), ordinary (A_5)-equivariance of an inter-sheet exchange is obstructed by Schur's lemma; outer-automorphism covariance is a separate test.
- [T153 source review](docs/T153-source-review-geometric-physics-claims.md) records access limitations and separates established geometry from unsupported physical extrapolations. No new numerical audit or continuum result is claimed.


### Companion-repository crosswalk

- [GEC-6 and RGS vierbein evidence crosswalk](research/COMPANION_RGS_GEC6_VIERBEIN_CROSSWALK_2026-11-27.md) — maps merged companion PRs #233–#235 to Q6/GEC-6, antipodal action and T154 without duplicating theorem statements.

### T154-RGS — RGS spatial coframe and labelled constraint splitting

- [T154-RGS](theorems/T154-rgs-spatial-coframe-constraint-splitting.md) proves the exact finite decomposition of the four constraint normals into three uniform Cartesian translations and one fixed-radius/radial normal, and the \(SO(3)\)-equivariant split \(\mathbb R^4=\mathbb R^3\oplus\mathbb R\) of the archived edge feature.
- A13/A14 reports numerically verify the 188D tangent projector, the labelled 3+1 constraint-normal decomposition, common edge indexing, and the active \(SU(2)\to SO(3)\) lift. The fourth edge component is a radial scalar singlet, **not Lorentz time**.
- The nonzero covariant face-torsion diagnostic is finite-graph evidence only. The raw edge coframe is used for the integrated cochain; the normalized edge feature is not. No continuum tetrad, Levi-Civita connection, teleparallel GR, or \(K_0\)-factorization theorem is claimed.


### Cymatics and wave morphogenesis

- [Cymatics / wave-morphogenesis research programme](projects/CYMATICS_WAVE_MORPHOGENESIS.md) — defines C01–C06, the scientific-status policy, the RGS/PRISM integration gates, and the separate helicon/plasma work packages.
- [Monograph chapter: Cymatics and wave morphogenesis](docs/CYMATICS_WAVE_MORPHOGENESIS_CHAPTER.md) — distinguishes mechanical Chladni patterns from electromagnetic helicon modes and specifies the falsifiable validation protocol.
- [CYM-T001 — Courant nodal-domain bound](theorems/CYM-T001-courant-nodal-domain-bound.md) is a classical theorem used as a scalar-mode constraint. [CYM-T002](open-problems/CYM-T002-spectral-morphology-stability.md) and [CYM-T003](open-problems/CYM-T003-rgs-prism-mode-compatibility.md) remain open; no new RGS morphogenesis theorem is claimed.
- [C01–C04 numerical controls](scripts/cymatics_wave_benchmarks.py) and [regression tests](tests/test_cymatics_wave_benchmarks.py) cover a simply supported square Kirchhoff–Love plate, square-mode degeneracy, controlled symmetry breaking, and the exact Q6 hypercube graph spectrum. These controls are not experimental Chladni data or a plasma simulation.

## Morfodinamica Quantistica — quantum geometry

- [MQ research index](morfodinamica-quantistica/README.md) — MQ-002 proves the dimension-two four-valent spin-1/2 SU(2) intertwiner space; MQ-003 proves invariance under one-link gluing and distinguishes area matching from shape matching. Includes explicit flux matrices, NumPy audit, regression tests, and an explicit open gate for the RGS–QLG identification.


## Morfodinamica Quantistica

The MQ programme records exact quantum-tetrahedron results (MQ-002/003) and a finite RGS-carrier classical-flux construction (MQ-005), with explicit limits on Q6 incidence and spin quantization. See [morfodinamica-quantistica/README.md](morfodinamica-quantistica/README.md).
