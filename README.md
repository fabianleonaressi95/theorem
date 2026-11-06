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

- [Bibliography and source catalogue](bibliography/README.md)
- [Formula extraction register](bibliography/FORMULA_EXTRACTION_REGISTER.md)
- [Cleaned research notes and manuscript editorial register](manuscripts/README.md)
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
| [T053](theorems/T053-exterior-square-projector-lemma.md) | Exterior-square projector lemma | Conditional linear-algebra theorem assuming symmetry and the exact quadratic matrix identity; no group irreducibility claim. |
| [T054](theorems/T054-static-radial-klein-gordon.md) | Static radial Klein–Gordon reduction | Exact reduction for a minimally coupled static radial scalar on the stated spherical metric ansatz. |

**Numbering note.** Historical records include overlapping T034 labels in the repository's development history. The linked files identify the intended record; the numbering conflict is not silently resolved by this index and should be handled in a dedicated renumbering change.

The file `001-fixed-lattice-temporal-wilson-limit.md` is a pre-existing result and is not part of the T001–T007 numbering sequence.

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

The periodic-cycle example is a calibration model only. The actual RGS–PRISM refinement sequence and its compactness proof remain open.

See [T048](theorems/T048-rgs-prism-mosco-changing-spaces.md), `scripts/rgs_prism_mosco_calibration.py`, and `tests/test_t048_rgs_prism_mosco_calibration.py`.

### QLG–Dirac embedding and Lorentz chirality

T049C classifies the Spin(3)-equivariant embeddings of a two-component QLG fibre into the spatial restriction of the four-component Dirac representation. The family is not canonical.

T049D then imposes Lorentz covariance using the Clifford convention documented in the source implementation, with signature ((-+++)). In the Hermitian-generator commutator convention used by the record, the boost generators are \(\mathcal K_i=\tfrac{i}{2}\gamma^0\gamma^i\), inducing \(K_i^{(s)}=-is\sigma_i/2\) on the two Weyl fibres. The two invariant embeddings are the two Weyl sectors, represented by
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
