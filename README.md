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

- **[Integrated 27-chapter monograph](monographs/RGS_PSU_PRISM_Q6_QLG_MONOGRAPH_27_CHAPTERS.md)** — consolidated reference for Q6, Q6-D5/Wilson, 2I/Rumin, RGS 188D, PRISM/Krist-All, FEEC/Mosco, QLG, Einstein–Cartan/teleparallelism, QAT, XCont and hysteresis. Includes explicit epistemic status and recovery caveats.
- [Canonical synthesis and closure programme](manuscripts/SINTESI_CANONICA_RGS_PSU_PRISM_Q6_QLG.md) — short strategic overview.

- [Bibliography and source catalogue](bibliography/README.md)
- [Special functions and Morandotti bibliography](bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md)
- [Integrated synthesis: moments, barycentres, Gamma–Beta–zeta and Morandotti](docs/SYNTHESIS_MOMENTS_BARYCENTRES_GAMMA_BETA_ZETA_MORANDOTTI_2026-11-10.md)
- [Digamma–supergolden–Q6 analytic dossier](docs/DIGAMMA_SUPERGOLDEN_Q6_PROGRAM_2026-11-10.md)
- [Formula extraction register](bibliography/FORMULA_EXTRACTION_REGISTER.md)
- [Cleaned research notes and manuscript editorial register](manuscripts/README.md)
- [XCont emergent-dynamics integration](manuscripts/XCONT_EMERGENT_DYNAMICS_INTEGRATION.md) — external cellular-automata, symbolic-billiard and graph-convolution methods mapped to PRISM/Q6 as testable research interfaces.
  - X6 symbolic rotation coding: [model](models/prism_billiard_coding.py), [JSON runner](scripts/run_prism_billiard_coding.py), [tests](tests/test_prism_billiard_coding.py), [research note](manuscripts/X6_SYMBOLIC_BILLIARD_CODING.md).
  - Implemented: [PRISM CA engine](models/prism_cellular_automata.py), [rule/initial-state genetic search](models/prism_ca_evolution.py), [single-run CLI](scripts/run_prism_ca_evolution.py), [multi-seed benchmark](scripts/run_prism_ca_benchmark.py), [two-population co-evolution CLI](scripts/run_prism_ca_coevolution.py), [regression tests](tests/test_prism_cellular_automata.py) / [GA and co-evolution tests](tests/test_prism_ca_evolution.py), and [dedicated CI workflow](.github/workflows/prism-ca.yml).
- [Inhomogeneous spin-chain model note](manuscripts/INHOMOGENEOUS_SPIN_CHAIN.md)
- [Scalar–torsion variational identity](manuscripts/SCALAR_TORSION_VARIATIONAL_IDENTITY.md)
- [Quarantined source files](archive/README.md)
- [External manuscript provenance notes](bibliography/source-bibliographies/)
- [Project map](projects/README.md)
- [Theorem records](theorems/)
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
| [S.1](theorems/S001-silver-ratio-square-corner-tangency.md) | Silver-ratio square-corner tangency | Exact Euclidean scale identities for the stated two-circle configuration; no general packing/refinement law. |
| [S.2](theorems/S002-square-pentagon-supergolden-synthesis.md) | Square, pentagon, hexagon and supergolden geometry | Exact component identities; labelled incidence and a construction deriving the supergolden ratio remain open. |
| [S.3](theorems/S003-dirichlet-log-partition-gradient-cumulants.md) | Dirichlet log-partition gradient and cumulants | Exact digamma/trigamma parameter derivatives; Bernoulli/zeta mesh asymptotics remain open. |
| [S.4](theorems/S004-rgs-seed-fourth-moment-anisotropy.md) | RGS 64-site fourth-moment anisotropy | Raw second/fourth moments, isotropic projection, cubic residual and Eg/T2g seed spectrum; prior numerical record, independent replay still required. |
| [S.5](theorems/S005-fourth-jump-moment-graph-laplacian-consistency.md) | Fourth-jump-moment consistency | Conditional Taylor expansion and O(a²) graph-Laplacian consistency; application to the actual RGS refinement remains open. |
| [S.6](theorems/S006-fourth-moment-so3-connection-current.md) | Fourth-moment SO(3) connection current | Proved local variational identity for the connection current; flatness constraint and full TEGR equations remain open. |
| [S.7](theorems/S007-fourth-moment-maxwell-and-a4-bridge.md) | Fourth-moment Maxwell obstruction and A4 bridge | Exact tensor no-go and subgroup representation result; Maxwell constitutive law is a candidate and the explicit intertwiner is open. |
| [S.8](theorems/S008-fourth-moment-coframe-variation.md) | Fourth-moment algebraic coframe variation | Exact first variations for the displayed action; no torsion generation or complete gravitational equation is claimed. |
| [T071](theorems/T071-q6-cubical-topological-synchronization-audit.md) | Q6 cubical chain complex, Anti-Twin lift and synchronization benchmark | Exact finite chain identities; exploratory synchronization/hysteresis model, with physical and continuum claims open. |
| [T072](theorems/T072-q6-mobius-phase-flat-connection.md) | Möbius phase action and canonical flat Q6 connection | Exact phase-translation Möbius action, pure-gauge vertex-phase connection, Q6 Laplacian spectrum and antipodal 32+32 decomposition; nontrivial RGS–PSU transport remains open. |

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
