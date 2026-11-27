# Unified theorem programme — cross-repository master index

**Purpose.** This is the common scientific index for the two-repository programme. The repository containing this index is `fabianleonaressi95/theorem`. The companion repository available in the connected GitHub installation is `fabianleonaressi95/rgs-qlg-quaternion-bridge` (README title: RGS–QLG Quaternion Bridge). It has been inspected and is linked through the directed cross-repository graph.

**No repository is being merged or renamed.** Original theorem IDs, file paths, proofs, numerical audits, data provenance, and historical PR records must remain stable. The unification is a crosswalk and dependency graph, not a blind file copy.

## 1. Canonical record schema

Every theorem or result from either repository must have one canonical registry entry with:

| Field | Required content |
|---|---|
| Canonical key | Original theorem ID plus repository namespace; never renumber |
| Source | Exact repository, path, commit, and originating PR when known |
| Mathematical object | Definitions, spaces, maps, operators, hypotheses |
| Result type | Law / definition / lemma / theorem / proposition / numerical result / model / conjecture |
| Evidence status | Proved / conditional proof / exact finite identity / numerical audit / candidate / hypothesis / open / superseded |
| Proof dependencies | Explicit theorem/lemma IDs and external results used |
| Computational evidence | Script, tests, data, precision, tolerance, reproducibility status |
| Limitations | Missing hypotheses, non-uniqueness, provenance, continuum/physical gaps |
| Application links | Pellis, Morandotti, both, or foundational/no direct application |
| Next gate | One concrete proof, audit, benchmark, or source-recovery task |

A filename, title, merged PR, or successful numerical test is not by itself evidence that a statement is proved. The registry must classify the mathematical statement after reading its content.

## 2. Current inventory of the accessible repository

The curated link list below preserves the original **236-record baseline** and its canonical names. It is not the complete live inventory: as of 27 November 2026, the machine-readable unified graph indexes **280 theorem records** in `theorem/theorems/`. Neither count is a blanket certification of proof status.


## Foundations, Liouville, Bergman, Wilson and Q6

- [EQC-MQM1-anisotropic-stabilizer](theorems/EQC-MQM1-anisotropic-stabilizer.md)
- [M1-q6-holder-gauge-strong-resolvent](theorems/M1-q6-holder-gauge-strong-resolvent.md)
- [M2-minkowski-q6-one-axis-reflection](theorems/M2-minkowski-q6-one-axis-reflection.md)
- [M3-minkowski-q6-d4-cell-orbit-closure](theorems/M3-minkowski-q6-d4-cell-orbit-closure.md)
- [MQM-Q6-symmetry-stabilizer](theorems/MQM-Q6-symmetry-stabilizer.md)
- [MQM-multidimensional-structure](theorems/MQM-multidimensional-structure.md)
- [MQM1-discriminant-analysis](theorems/MQM1-discriminant-analysis.md)
- [MQM1-local-determinant-coupling](theorems/MQM1-local-determinant-coupling.md)
- [MQM1-local-psu-scalar-field](theorems/MQM1-local-psu-scalar-field.md)
- [MQM1-q6-quantum-geometry-backreaction](theorems/MQM1-q6-quantum-geometry-backreaction.md)
- [MQM1-rgs-metric-reference](theorems/MQM1-rgs-metric-reference.md)
- [T001-liouville-theorem](theorems/T001-liouville-theorem.md)
- [T002-d5-bergman-volume-density](theorems/T002-d5-bergman-volume-density.md)
- [T003-wilson-atomic-marginal-no-go](theorems/T003-wilson-atomic-marginal-no-go.md)
- [T004-riemann-sums-bergman-weak-limit](theorems/T004-riemann-sums-bergman-weak-limit.md)
- [T005-q6-wilson-fiber-marginal-support](theorems/T005-q6-wilson-fiber-marginal-support.md)
- [T006-q6-wilson-five-torus-quotient](theorems/T006-q6-wilson-five-torus-quotient.md)
- [T007-q6-gauge-average-fourier-marginal](theorems/T007-q6-gauge-average-fourier-marginal.md)
- [T008-wilson-to-bergman-weak-convergence-criterion](theorems/T008-wilson-to-bergman-weak-convergence-criterion.md)
- [T009-effective-wilson-fiber-quadratic-form](theorems/T009-effective-wilson-fiber-quadratic-form.md)
- [T010-para-kahler-liouville-psu](theorems/T010-para-kahler-liouville-psu.md)
- [T010-rumin-spectrum-poincare-sphere](theorems/T010-rumin-spectrum-poincare-sphere.md)
- [T011-para-kahler-liouville-psu](theorems/T011-para-kahler-liouville-psu.md)
- [T012-su3-baryon-octet-decuplet](theorems/T012-su3-baryon-octet-decuplet.md)
- [T013-q6-gauge-invariant-baryon-operators](theorems/T013-q6-gauge-invariant-baryon-operators.md)
- [T014-q6-graph-dirac-gauge-covariance](theorems/T014-q6-graph-dirac-gauge-covariance.md)
- [T015-q6-clifford-free-spectrum](theorems/T015-q6-clifford-free-spectrum.md)
- [T016-nielsen-ninomiya-q6-audit](theorems/T016-nielsen-ninomiya-q6-audit.md)
- [T017-q6-dirac-refinement](theorems/T017-q6-dirac-refinement.md)
- [T019-q6-free-strong-resolvent](theorems/T019-q6-free-strong-resolvent.md)
- [T020-gauge-covariant-q6-strong-resolvent](theorems/T020-gauge-covariant-q6-strong-resolvent.md)

## Rumin, Poincaré sphere, binary icosahedral group and spectral determinants

- [T021-critical-sobolev-gauge-trace-audit](theorems/T021-critical-sobolev-gauge-trace-audit.md)
- [T021-rumin-analytic-torsion-2I](theorems/T021-rumin-analytic-torsion-2I.md)
- [T022-eventual-hurwitz-rumin-2I](theorems/T022-eventual-hurwitz-rumin-2I.md)
- [T023-gamma-reflection-rumin-2I](theorems/T023-gamma-reflection-rumin-2I.md)
- [T024-reynolds-intertwiners-rumin-2I](theorems/T024-reynolds-intertwiners-rumin-2I.md)
- [T024-rumin-kitaoka-operator-matching-3d](theorems/T024-rumin-kitaoka-operator-matching-3d.md)
- [T025-rumin-middle-degree-blocks](theorems/T025-rumin-middle-degree-blocks.md)
- [T026-mckay-e8-2i-multiplicities](theorems/T026-mckay-e8-2i-multiplicities.md)
- [T027-mckay-molien-rumin-bridge](theorems/T027-mckay-molien-rumin-bridge.md)
- [T028-nine-twist-torsion-closure](theorems/T028-nine-twist-torsion-closure.md)
- [T029-rumin-gram-matrices-2i](theorems/T029-rumin-gram-matrices-2i.md)
- [T030-rumin-explicit-central-differential](theorems/T030-rumin-explicit-central-differential.md)
- [T030-rumin-polar-factorization](theorems/T030-rumin-polar-factorization.md)
- [T031-rumin-2i-equivariance](theorems/T031-rumin-2i-equivariance.md)
- [T032-2i-irrep-molien-projectors](theorems/T032-2i-irrep-molien-projectors.md)
- [T032-rumin-fixed-harmonic-matrix](theorems/T032-rumin-fixed-harmonic-matrix.md)
- [T033-2i-exact-matrix-units](theorems/T033-2i-exact-matrix-units.md)
- [T033-equivariant-rumin-torsion-synthesis](theorems/T033-equivariant-rumin-torsion-synthesis.md)
- [T034-exact-2i-character-table](theorems/T034-exact-2i-character-table.md)
- [T034-explicit-2i-representations](theorems/T034-explicit-2i-representations.md)
- [T035-exact-binary-icosahedral-model](theorems/T035-exact-binary-icosahedral-model.md)
- [T036-explicit-2i-irreducible-models](theorems/T036-explicit-2i-irreducible-models.md)
- [T037-harmonic-multiplicity-spaces](theorems/T037-harmonic-multiplicity-spaces.md)
- [T038-rumin-reduced-differential](theorems/T038-rumin-reduced-differential.md)
- [T039-rumin-boundary-2i-sectors](theorems/T039-rumin-boundary-2i-sectors.md)
- [T040-boundary-barnes-zeta](theorems/T040-boundary-barnes-zeta.md)
- [T041-boundary-barnes-determinant](theorems/T041-boundary-barnes-determinant.md)
- [T042-full-rumin-torsion-audit](theorems/T042-full-rumin-torsion-audit.md)
- [T043-twisted-2i-rumin-torsion](theorems/T043-twisted-2i-rumin-torsion.md)
- [T044-exact-twisted-gamma-reduction](theorems/T044-exact-twisted-gamma-reduction.md)
- [T045-exact-2i-representation-certificate](theorems/T045-exact-2i-representation-certificate.md)
- [T045-individual-rumin-zeta-poles](theorems/T045-individual-rumin-zeta-poles.md)
- [T046-hadamard-finite-part-determinants](theorems/T046-hadamard-finite-part-determinants.md)
- [T123-q6-2i-central-character-intertwiner](theorems/T123-q6-2i-central-character-intertwiner.md)
- [mckay_affine_e8_binary_icosahedral](theorems/spectral/mckay_affine_e8_binary_icosahedral.md)
- [poincare_s3_2i_multiplicities](theorems/spectral/poincare_s3_2i_multiplicities.md)

## Q6, Kathara, chain complexes, cohomology and quaternionic transport

- [EQC-4-hamming-automorphism-clifford](theorems/EQC-4-hamming-automorphism-clifford.md)
- [Q6_FACE_COCHAINS_HODGE_GREEN_KUBO_2026-11-23](theorems/Q6_FACE_COCHAINS_HODGE_GREEN_KUBO_2026-11-23.md)
- [Q6_GREEN_KUBO_KRYSTALLO_SCALE_BRIDGE_2026-11-23](theorems/Q6_GREEN_KUBO_KRYSTALLO_SCALE_BRIDGE_2026-11-23.md)
- [S010-kathara-quaternionic-rgs-triplet-response](theorems/S010-kathara-quaternionic-rgs-triplet-response.md)
- [S011-fdt-density-cone-riemann-cartan-kathara-maxwell](theorems/S011-fdt-density-cone-riemann-cartan-kathara-maxwell.md)
- [T049A-q6-prism-spin-correlator](theorems/T049A-q6-prism-spin-correlator.md)
- [T049B-rgs-ec-q6-prism-axial-current](theorems/T049B-rgs-ec-q6-prism-axial-current.md)
- [T050-geometric-spin-chain-bounds](theorems/T050-geometric-spin-chain-bounds.md)
- [T055-q6-dyadic-subdivision-chain-map](theorems/T055-q6-dyadic-subdivision-chain-map.md)
- [T057-kathara-square-similarity-center-overlay](theorems/T057-kathara-square-similarity-center-overlay.md)
- [T058-kathara-15-line-planar-face-audit](theorems/T058-kathara-15-line-planar-face-audit.md)
- [T059-kathara-cellular-chain-hodge-audit](theorems/T059-kathara-cellular-chain-hodge-audit.md)
- [T060-kathara-q3-chain-map](theorems/T060-kathara-q3-chain-map.md)
- [T061-kathara-q3-chain-homotopy](theorems/T061-kathara-q3-chain-homotopy.md)
- [T062-kathara-q6-integral-chain-map](theorems/T062-kathara-q6-integral-chain-map.md)
- [T063-quaternion-su2-so3-double-cover](theorems/T063-quaternion-su2-so3-double-cover.md)
- [T064-finite-su2-lattice-holonomy-gauge-covariance](theorems/T064-finite-su2-lattice-holonomy-gauge-covariance.md)
- [T065-cubical-subdivision-chain-map-and-naturality](theorems/T065-cubical-subdivision-chain-map-and-naturality.md)
- [T067-stokes-commuting-cubical-face-integral-interpolation](theorems/T067-stokes-commuting-cubical-face-integral-interpolation.md)
- [T069-q6-antipodal-walsh-covariance](theorems/T069-q6-antipodal-walsh-covariance.md)
- [T071-q6-cubical-topological-synchronization-audit](theorems/T071-q6-cubical-topological-synchronization-audit.md)
- [T072-q6-mobius-phase-flat-connection](theorems/T072-q6-mobius-phase-flat-connection.md)
- [T099-shao-yong-q6-kirchhoff-network](theorems/T099-shao-yong-q6-kirchhoff-network.md)
- [T101-trigram-angular-phases-q6-plaquette-holonomy](theorems/T101-trigram-angular-phases-q6-plaquette-holonomy.md)
- [T102-cubical-supersymmetry-heat-kernel-sakharov](theorems/T102-cubical-supersymmetry-heat-kernel-sakharov.md)
- [T103-q6-z2-magnetic-holonomy](theorems/T103-q6-z2-magnetic-holonomy.md)
- [T104-q6-cycle-cocycle-holonomy-law](theorems/T104-q6-cycle-cocycle-holonomy-law.md)
- [T106-born-measure-q6-fdt-frank-burgers](theorems/T106-born-measure-q6-fdt-frank-burgers.md)
- [T107-q6-gray-torus-gibbs-fdt-defect-test](theorems/T107-q6-gray-torus-gibbs-fdt-defect-test.md)
- [T108-boolean-influences-q6-laplacian-cohomology](theorems/T108-boolean-influences-q6-laplacian-cohomology.md)
- [T113D-q6-rgs-phonon-internal-mode](theorems/T113D-q6-rgs-phonon-internal-mode.md)
- [T113E-q6-rgs-t2u-triplet-stability](theorems/T113E-q6-rgs-t2u-triplet-stability.md)
- [T113F-q6-graph-elastic-stabilization](theorems/T113F-q6-graph-elastic-stabilization.md)
- [T114-q6-gauge-covariant-cubical-dirac-kaehler](theorems/T114-q6-gauge-covariant-cubical-dirac-kaehler.md)
- [T115-rgs-curved-clifford-coframe-identity](theorems/T115-rgs-curved-clifford-coframe-identity.md)
- [T116-nondegenerate-kathara-q6-integral-chain-map](theorems/T116-nondegenerate-kathara-q6-integral-chain-map.md)
- [T117-six-square-mobius-subcomplex-of-q6](theorems/T117-six-square-mobius-subcomplex-of-q6.md)
- [T118-su2-path-transport-wilson-holonomy](theorems/T118-su2-path-transport-wilson-holonomy.md)
- [T120-mobius-orientation-cocycle-and-independent-su2-fibre](theorems/T120-mobius-orientation-cocycle-and-independent-su2-fibre.md)
- [T121-icosahedral-a5-action-on-q6-clifford-module](theorems/T121-icosahedral-a5-action-on-q6-clifford-module.md)
- [T122-pin-plus-mobius-clifford-transport](theorems/T122-pin-plus-mobius-clifford-transport.md)
- [T125-q6-prism-burgers-chain-frank-read-variational-interface](theorems/T125-q6-prism-burgers-chain-frank-read-variational-interface.md)
- [T128-purcell-swimmer-q6-geometric-control](theorems/T128-purcell-swimmer-q6-geometric-control.md)
- [T129-a5-equivariance-obstruction-and-calibrated-q6-purcell-map](theorems/T129-a5-equivariance-obstruction-and-calibrated-q6-purcell-map.md)
- [T129-q6-cut-project-purcell-shape-map](theorems/T129-q6-cut-project-purcell-shape-map.md)
- [T130-q6-discrete-gradients-barycentres-resistance](theorems/T130-q6-discrete-gradients-barycentres-resistance.md)
- [T131-q6-phonon-phason-green-kubo-transport](theorems/T131-q6-phonon-phason-green-kubo-transport.md)
- [T136-tetrahedral-volume-moment-reconstruction-ricci-q6](theorems/T136-tetrahedral-volume-moment-reconstruction-ricci-q6.md)
- [T137-q6-real-weighted-hodge-green-resolvent](theorems/T137-q6-real-weighted-hodge-green-resolvent.md)
- [T140-icosahedron-q6-incidence-lift](theorems/T140-icosahedron-q6-incidence-lift.md)
- [T141-antipodal-icosahedron-q6-lift](theorems/T141-antipodal-icosahedron-q6-lift.md)
- [T142-vesica-antipodal-six-state-mixing](theorems/T142-vesica-antipodal-six-state-mixing.md)
- [T143-vesica-q6-isometric-antipodal-embedding](theorems/T143-vesica-q6-isometric-antipodal-embedding.md)
- [T143A-antipodal-equivariance-minimal-so3-su2-connection](theorems/T143A-antipodal-equivariance-minimal-so3-su2-connection.md)
- [T143C-clifford-symmetry-fibre-operator](theorems/T143C-clifford-symmetry-fibre-operator.md)

## RGS, PRISM, FEEC/Mosco, continuum limits and mechanics

- [B1-B3-bernoulli-rgs-hodge](theorems/B1-B3-bernoulli-rgs-hodge.md)
- [C60_CF_ACTUAL_JUMP_MEASURE_DECOMPOSITION_OPEN_2026-11-23](theorems/C60_CF_ACTUAL_JUMP_MEASURE_DECOMPOSITION_OPEN_2026-11-23.md)
- [C60_CF_DETERMINING_SEQUENCE_M0_2026-11-21](theorems/C60_CF_DETERMINING_SEQUENCE_M0_2026-11-21.md)
- [C60_CF_EXTENSIONS_STUDY_2026-11-21](theorems/C60_CF_EXTENSIONS_STUDY_2026-11-21.md)
- [C60_CF_EXTENSIONS_VARIABLE_M_ANISOTROPIC_2026-11-21](theorems/C60_CF_EXTENSIONS_VARIABLE_M_ANISOTROPIC_2026-11-21.md)
- [C60_CF_EXTENSIONS_VARIABLE_M_ANISOTROPIC_AUDIT_2026-11-21](theorems/C60_CF_EXTENSIONS_VARIABLE_M_ANISOTROPIC_AUDIT_2026-11-21.md)
- [C60_CF_FINITE_JUMP_GRAPH_GEOMETRY_2026-11-22](theorems/C60_CF_FINITE_JUMP_GRAPH_GEOMETRY_2026-11-22.md)
- [C60_CF_GENERAL_ISOTROPIC_RECOVERY_2026-11-21](theorems/C60_CF_GENERAL_ISOTROPIC_RECOVERY_2026-11-21.md)
- [C60_CF_GEOMETRY_A_TERMINAL_TRACE_AND_STRIP_SEPARATION_2026-11-23](theorems/C60_CF_GEOMETRY_A_TERMINAL_TRACE_AND_STRIP_SEPARATION_2026-11-23.md)
- [C60_CF_GTILDE_OPTIMIZATION_NUMERICAL_2026-11-21](theorems/C60_CF_GTILDE_OPTIMIZATION_NUMERICAL_2026-11-21.md)
- [C60_CF_LOCALIZATION_LEMMA_2026-11-21](theorems/C60_CF_LOCALIZATION_LEMMA_2026-11-21.md)
- [C60_CF_MINIMALITY_CONVEX_BULK_NORM_JUMP_2026-11-21](theorems/C60_CF_MINIMALITY_CONVEX_BULK_NORM_JUMP_2026-11-21.md)
- [C60_CF_NONZERO_BULK_DISARRANGEMENT_2026-11-21](theorems/C60_CF_NONZERO_BULK_DISARRANGEMENT_2026-11-21.md)
- [C60_CF_NUCLEAR_NORM_CELL_AND_BULK_OPTIMIZATION_2026-11-21](theorems/C60_CF_NUCLEAR_NORM_CELL_AND_BULK_OPTIMIZATION_2026-11-21.md)
- [C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21](theorems/C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21.md)
- [C60_CF_PARTITION_RECOVERY_AND_CELL_FORMULA_2026-11-21](theorems/C60_CF_PARTITION_RECOVERY_AND_CELL_FORMULA_2026-11-21.md)
- [C60_CF_POLYHEDRAL_AFFINE_THEOREM_2026-11-21](theorems/C60_CF_POLYHEDRAL_AFFINE_THEOREM_2026-11-21.md)
- [C60_CF_POLYHEDRAL_CFI_TRANSFER_AUDIT_2026-11-23](theorems/C60_CF_POLYHEDRAL_CFI_TRANSFER_AUDIT_2026-11-23.md)
- [C60_CF_POLYHEDRAL_GENERAL_RECOVERY_2026-11-21](theorems/C60_CF_POLYHEDRAL_GENERAL_RECOVERY_2026-11-21.md)
- [C60_CF_QUADRATIC_JUMP_GENERAL_2026-11-21](theorems/C60_CF_QUADRATIC_JUMP_GENERAL_2026-11-21.md)
- [C60_CF_QUADRATIC_JUMP_RELAXATION_2026-11-21](theorems/C60_CF_QUADRATIC_JUMP_RELAXATION_2026-11-21.md)
- [C60_CF_QUADRATIC_RECOVERY_DIAGONAL_2026-11-23](theorems/C60_CF_QUADRATIC_RECOVERY_DIAGONAL_2026-11-23.md)
- [C60_CF_SBV_DENSITY_ATTEMPT_2026-11-21](theorems/C60_CF_SBV_DENSITY_ATTEMPT_2026-11-21.md)
- [C60_CF_SBV_ISOTROPIC_THEOREM_2026-11-21](theorems/C60_CF_SBV_ISOTROPIC_THEOREM_2026-11-21.md)
- [C60_CF_SKELETON_INTERIOR_LAMINATE_ESTIMATE_2026-11-23](theorems/C60_CF_SKELETON_INTERIOR_LAMINATE_ESTIMATE_2026-11-23.md)
- [C60_CF_SPLITTING_LEMMA_FRAMEWORK_2026-11-21](theorems/C60_CF_SPLITTING_LEMMA_FRAMEWORK_2026-11-21.md)
- [C60_CF_VARIABLE_GRADIENT_RECOVERY_PROOF_2026-11-21](theorems/C60_CF_VARIABLE_GRADIENT_RECOVERY_PROOF_2026-11-21.md)
- [C60_CF_VARIABLE_M_ANALYTICAL_RECOVERY_2026-11-21](theorems/C60_CF_VARIABLE_M_ANALYTICAL_RECOVERY_2026-11-21.md)
- [C60_SURFACE_STRUCTURED_DEFORMATION_2026-11-21](theorems/C60_SURFACE_STRUCTURED_DEFORMATION_2026-11-21.md)
- [EQC-3-rgs-native-symmetry-gates](theorems/EQC-3-rgs-native-symmetry-gates.md)
- [S004-rgs-seed-fourth-moment-anisotropy](theorems/S004-rgs-seed-fourth-moment-anisotropy.md)
- [S008-fourth-moment-coframe-variation](theorems/S008-fourth-moment-coframe-variation.md)
- [S009-three-phase-ferraris-coframe-tetrad-bridge](theorems/S009-three-phase-ferraris-coframe-tetrad-bridge.md)
- [T048-rgs-prism-mosco-changing-spaces](theorems/T048-rgs-prism-mosco-changing-spaces.md)
- [T049-ellis-rgs-radial-icosphere-discretization](theorems/T049-ellis-rgs-radial-icosphere-discretization.md)
- [T049D-lorentz-chiral-qlg-embedding](theorems/T049D-lorentz-chiral-qlg-embedding.md)
- [T052-scalar-torsion-variation](theorems/T052-scalar-torsion-variation.md)
- [T073-unified-football-shell-rgs-prism-limit-program](theorems/T073-unified-football-shell-rgs-prism-limit-program.md)
- [T080-exact-discrete-stokes-qball-structured-gradient](theorems/T080-exact-discrete-stokes-qball-structured-gradient.md)
- [T086-discrete-structured-deformation-hodge-seam-energy](theorems/T086-discrete-structured-deformation-hodge-seam-energy.md)
- [T099-bicircular-annular-deformation-reconstruction](theorems/T099-bicircular-annular-deformation-reconstruction.md)

## Morandotti, Vesica, barycentres, gradients, defects and shell geometry

- [S003-dirichlet-log-partition-gradient-cumulants](theorems/S003-dirichlet-log-partition-gradient-cumulants.md)
- [T068-barycentric-covariance-quadrature-law](theorems/T068-barycentric-covariance-quadrature-law.md)
- [T070-dirichlet-barycentric-phase-moments](theorems/T070-dirichlet-barycentric-phase-moments.md)
- [T075-seam-aware-ellipsoidal-ovaloid-reduction](theorems/T075-seam-aware-ellipsoidal-ovaloid-reduction.md)
- [T076-constitutive-mechanics-fatigue-hysteresis-football-seams](theorems/T076-constitutive-mechanics-fatigue-hysteresis-football-seams.md)
- [T077-bernoulli-gradient-barycentre-gauge-fluid-bridge](theorems/T077-bernoulli-gradient-barycentre-gauge-fluid-bridge.md)
- [T078-phase-theta-zeta-barycentric-spectral-bridge](theorems/T078-phase-theta-zeta-barycentric-spectral-bridge.md)
- [T079-morandotti-surface-gradient-barycentre-bridge](theorems/T079-morandotti-surface-gradient-barycentre-bridge.md)
- [T081-morandotti-gamma-euler-barycentric-energy](theorems/T081-morandotti-gamma-euler-barycentric-energy.md)
- [T082-morandotti-second-order-first-variation-dirichlet-anisotropy](theorems/T082-morandotti-second-order-first-variation-dirichlet-anisotropy.md)
- [T087-covariant-discrete-hodge-curvature-seams](theorems/T087-covariant-discrete-hodge-curvature-seams.md)
- [T088-qball-panel-frames-holonomy-anisotropy](theorems/T088-qball-panel-frames-holonomy-anisotropy.md)
- [T092-local-two-circle-frank-burgers-holonomy-bridge](theorems/T092-local-two-circle-frank-burgers-holonomy-bridge.md)
- [T093-conforming-global-assembly-cartan-holonomy](theorems/T093-conforming-global-assembly-cartan-holonomy.md)
- [T094-se2-holonomy-morandotti-audit](theorems/T094-se2-holonomy-morandotti-audit.md)
- [T096-airy-strain-holonomy-nonidentifiability](theorems/T096-airy-strain-holonomy-nonidentifiability.md)
- [T097-barycentric-kinematic-frank-burgers-law](theorems/T097-barycentric-kinematic-frank-burgers-law.md)
- [T098-two-circle-positive-gradient-negative-barycentre-duality](theorems/T098-two-circle-positive-gradient-negative-barycentre-duality.md)
- [T099-nonaffine-vesica-parameter-koopman-bridge](theorems/T099-nonaffine-vesica-parameter-koopman-bridge.md)
- [T133-morandotti-finite-dimensional-kkt-existence-uniqueness](theorems/T133-morandotti-finite-dimensional-kkt-existence-uniqueness.md)
- [T134-morandotti-c0-ipdg-conditional-coercivity](theorems/T134-morandotti-c0-ipdg-conditional-coercivity.md)
- [T135-morandotti-bernstein-neumann-certified-rational-integration](theorems/T135-morandotti-bernstein-neumann-certified-rational-integration.md)
- [T137-vesica-piscis-two-circle-hexagon-pi-sqrt3](theorems/T137-vesica-piscis-two-circle-hexagon-pi-sqrt3.md)

## Phases, special functions, golden/supergolden structures and statistical physics

- [S002-square-pentagon-supergolden-synthesis](theorems/S002-square-pentagon-supergolden-synthesis.md)
- [S009-weber-dedekind-eta-supergolden-class-invariant](theorems/S009-weber-dedekind-eta-supergolden-class-invariant.md)
- [S010-dirichlet-eta-lambert-series-quadratic-zeta](theorems/S010-dirichlet-eta-lambert-series-quadratic-zeta.md)
- [T056-phase21-trigram-supergolden-permutation-conjugacy](theorems/T056-phase21-trigram-supergolden-permutation-conjugacy.md)
- [T083-supergolden-digamma-zeta-gamma-identity](theorems/T083-supergolden-digamma-zeta-gamma-identity.md)
- [T084-supergolden-digamma-odd-zeta-accelerated-formula](theorems/T084-supergolden-digamma-odd-zeta-accelerated-formula.md)
- [T085-supergolden-weber-hurwitz-digamma-bridge](theorems/T085-supergolden-weber-hurwitz-digamma-bridge.md)
- [T089-gauge-fluid-bernoulli-variational-coupling](theorems/T089-gauge-fluid-bernoulli-variational-coupling.md)
- [T100-hypercube-moire-green-kubo-defects](theorems/T100-hypercube-moire-green-kubo-defects.md)
- [T110-xy-torus-vortex-kthny-bkt](theorems/T110-xy-torus-vortex-kthny-bkt.md)
- [T111-gp-zero-vortex-refinement](theorems/T111-gp-zero-vortex-refinement.md)
- [T112-golden-ratio-kthny-defect-geometry](theorems/T112-golden-ratio-kthny-defect-geometry.md)
- [T132-coupled-phonon-phason-ou-green-kubo](theorems/T132-coupled-phonon-phason-ou-green-kubo.md)
- [T139-supergolden-icosahedron-convex-hull-audit](theorems/T139-supergolden-icosahedron-convex-hull-audit.md)

## Geometry, Vesica–hexagram, icosahedron and later synthesis

- [EQC-1-ternary-hexagram-qutrit-register](theorems/EQC-1-ternary-hexagram-qutrit-register.md)
- [EQC-2-instruction-algebra-compiler](theorems/EQC-2-instruction-algebra-compiler.md)
- [EQC-3-hexagram-geometry-gates](theorems/EQC-3-hexagram-geometry-gates.md)
- [S001-silver-ratio-square-corner-tangency](theorems/S001-silver-ratio-square-corner-tangency.md)
- [S005-fourth-jump-moment-graph-laplacian-consistency](theorems/S005-fourth-jump-moment-graph-laplacian-consistency.md)
- [S006-fourth-moment-so3-connection-current](theorems/S006-fourth-moment-so3-connection-current.md)
- [S007-fourth-moment-maxwell-and-a4-bridge](theorems/S007-fourth-moment-maxwell-and-a4-bridge.md)
- [T074-icosahedral-shell-binary-lift-hopf-seifert-bridge](theorems/T074-icosahedral-shell-binary-lift-hopf-seifert-bridge.md)
- [T105-hexagram-charge-moire-circuit-law](theorems/T105-hexagram-charge-moire-circuit-law.md)
- [T113C-icosahedral-phonon-phason-elasticity](theorems/T113C-icosahedral-phonon-phason-elasticity.md)
- [T119-binary-icosahedral-group-and-selected-representations](theorems/T119-binary-icosahedral-group-and-selected-representations.md)
- [T138-c6-exact-two-sheet-spin3-decomposition](theorems/T138-c6-exact-two-sheet-spin3-decomposition.md)
- [T143D-antitwin-isospectrality-normal-operator](theorems/T143D-antitwin-isospectrality-normal-operator.md)

## Other theorem records

- [001-fixed-lattice-temporal-wilson-limit](theorems/001-fixed-lattice-temporal-wilson-limit.md)
- [KRYSTALLO_SUPERGOLDEN_FINE_STRUCTURE_BRIDGE_AUDIT_2026-11-23](theorems/KRYSTALLO_SUPERGOLDEN_FINE_STRUCTURE_BRIDGE_AUDIT_2026-11-23.md)
- [S011-ikeda-binary-tetrahedral-spectrum](theorems/S011-ikeda-binary-tetrahedral-spectrum.md)
- [S012-ikeda-cyclic-binary-polyhedral-spectra](theorems/S012-ikeda-cyclic-binary-polyhedral-spectra.md)
- [S013-general-spherical-space-form-molien-diagonal-actions](theorems/S013-general-spherical-space-form-molien-diagonal-actions.md)
- [T047-ec-weyssenhoff-spin-scaling](theorems/T047-ec-weyssenhoff-spin-scaling.md)
- [T049-microscopic-spin-correlation-invariant](theorems/T049-microscopic-spin-correlation-invariant.md)
- [T049C-qlg-dirac-intertwiner-classification](theorems/T049C-qlg-dirac-intertwiner-classification.md)
- [T051-crank-nicolson-unitarity](theorems/T051-crank-nicolson-unitarity.md)
- [T053-exterior-square-projector-lemma](theorems/T053-exterior-square-projector-lemma.md)
- [T054-static-radial-klein-gordon](theorems/T054-static-radial-klein-gordon.md)
- [T066-herasymov-parity-affine-shared-face-conformity](theorems/T066-herasymov-parity-affine-shared-face-conformity.md)
- [T090-whitney-gauge-fluid-discretization](theorems/T090-whitney-gauge-fluid-discretization.md)
- [T091-frank-burgers-tensorial-anisotropy-composition-law](theorems/T091-frank-burgers-tensorial-anisotropy-composition-law.md)
- [T109-qn-dimension-uniform-influence-gap](theorems/T109-qn-dimension-uniform-influence-gap.md)
- [T113-quasicrystal-phonon-phason-gravitational-mass](theorems/T113-quasicrystal-phonon-phason-gravitational-mass.md)
- [T113A-metric-action-phonon-phason-mode-sensitivity](theorems/T113A-metric-action-phonon-phason-mode-sensitivity.md)
- [T113B-ekn-acoustic-gravitational-mass-control](theorems/T113B-ekn-acoustic-gravitational-mass-control.md)
- [T113G-cut-project-symmetry-rank-two-isotropy](theorems/T113G-cut-project-symmetry-rank-two-isotropy.md)
- [T124-frank-read-source-line-tension-atomistic-core](theorems/T124-frank-read-source-line-tension-atomistic-core.md)
- [T126-exact-burgers-conserving-local-reconnection](theorems/T126-exact-burgers-conserving-local-reconnection.md)
- [T127-variational-energy-acceptance-topology-events](theorems/T127-variational-energy-acceptance-topology-events.md)
- [T134-exact-integration-certification-gap](theorems/T134-exact-integration-certification-gap.md)


## 3. Cross-program dependency architecture

The programme should be represented as a directed acyclic dependency graph wherever possible. Cycles in research dependencies must be marked as feedback/consistency loops, not disguised as proof dependencies.

### A. Foundational geometry and finite structures
- Vesica Piscis, two-circle geometry, triangles, hexagram/Star of David, pentagonal construction.
- Q3/Q6 cubical complexes, Kathara incidence structures, PRISM product graphs, 64-TG/FCC-D3 and polyhedral shells.
- Exact chain maps, homology, barycentric coordinates, moment tensors, incidence and symmetry actions.

### B. Algebra, representation theory and spectral theory
- Clifford/quaternionic/SU(2) structures and spin lifts.
- Binary icosahedral group 2I, McKay correspondence, Rumin complex and Poincaré sphere spectra.
- Wilson/Bergman/Liouville structures, Dirichlet forms, Hodge and graph Laplacians, determinants and special functions.

### C. Differential geometry, transport and defects
- Frames/coframes, connections, torsion, curvature, holonomy.
- Frank/Burgers closure, structured deformations, barycentric and gradient reconstructions.
- Phase fields, cocycles, plaquette winding, Möbius orientation and internal fibres.

### D. Variational analysis, continuum limits and dynamics
- FEEC, Mosco and Γ-convergence, coercivity, compactness, consistency.
- KKT systems, Airy stress, C0-IPDG, seam/shell mechanics, hysteresis and constitutive laws.
- Jitterbug kinematics, non-affine geometric continuation, Koopman generators and coupled dynamics.

### E. Physical interpretation
- Einstein–Cartan/teleparallel models, QLG, quantum geometry and field-theoretic proposals.
- Every physical claim must be downstream of a defined action, variables, variation, units, boundary conditions and independently testable prediction. Mathematical identities do not automatically establish physical interpretation.

## 4. Two application programmes — one mathematical base

### Pellis workstream

Build a focused dossier from the common theorem graph, not from a detached PRISM-only branch:

1. **Exact scalar spectrum on (S^3/2I):** Rumin/Poincaré/McKay/Molien records, exact multiplicities, determinant and torsion records. Keep the scalar spectrum distinct from twisted and Rumin spectra.
2. **PRISM and Krist-All:** the (C_{64}square C_6^3square C_5) product graph, 108-cycle construction, cycle-cover provenance, operator polynomial (K^3=K^2+I), class enumeration and residual certificate. A constructive cycle cover is not automatically the historical distinguished cycle family; Krist-All's class count/operator require the original data and independent replay.
3. **Kathara–Q3–Q6:** retain all existing (R_0,R_1,R_2) constructions as distinct maps. Compare chain-map identities, non-degeneracy, equivariance and geometric realization; do not redo already completed maps.
4. **Quaternionic/RGS bridge:** identify the exact quaternionic representation, SU(2) transport, Q6 fibre and any claimed Lorentz/spinor map. State the representation and intertwiner explicitly.
5. **Pellis deliverable:** a concise theorem-by-theorem technical dossier, each claim linked to source code/data and a sharply formulated question for review.

### Morandotti workstream

Use the same base, prioritizing the Vesica and rigorous geometric generalizations:

1. **Vesica and barycentric geometry:** T098, T099, T137 Vesica, T142–T143; the two opposite triangles, gradients, barycentres, covariance and non-affine lens moments.
2. **Frank–Burgers and structured deformation:** T091–T097, T080, T086–T090; exact discrete closure, interface terms, cochain maps and conditions for continuum interpretation.
3. **Q-ball/shell and FEEC:** T073–T079, T082, T086–T090, T093–T096; distinguish flat benchmark, curved shell extension, seam constitutive law and Mosco/Γ-limit obligations.
4. **Vesica–Star-of-David–pentagon–Jitterbug:** connect T101/T142/T143 and the existing crosswalk with the pentagonal construction and verified Jitterbug kinematics. Keep pentagonal phases, trigram phases, gradient polar angle and Jitterbug angles distinct until an incidence-compatible transition map is proved.
5. **Nonlinear dynamics and applications:** only after the geometric/variational core is explicit, connect the derived state variables to nonlinear dynamics, economic models or other applications.
6. **Morandotti deliverable:** start from Vesica geometry and its rigorous generalizations, followed by a small number of reproducible benchmarks and open mathematical questions.

## 5. Shared proof gates

These are programme-wide gates, not claims that the results already pass:

- **G1 — Definitions:** all spaces, orientations, metrics, measures, units and boundary conditions fixed.
- **G2 — Algebraic exactness:** incidence, chain, symmetry, intertwining and polynomial identities checked exactly where possible.
- **G3 — Analytic proof:** domains, regularity, coercivity, compactness, uniqueness and limiting arguments stated.
- **G4 — Numerical audit:** independent implementation, tests, conditioning, error/tolerance and data checksums.
- **G5 — Geometric realization:** abstract maps shown to arise from the declared geometry, not merely chosen by coordinates.
- **G6 — Physical interpretation:** action/constitutive law, variation, dimensions, observables and falsifiable predictions.
- **G7 — External presentation:** a compact dossier that reports proved results, conditional results, numerical evidence and open questions separately.

## 6. Immediate integration tasks

1. Replace the provisional filename-based classification edges with theorem-body-verified dependency edges.
2. Add a claim-level registry with exact source paths, commit hashes, assumptions and proof status.
3. Deduplicate only by mathematical equivalence; retain distinct formulations and proofs as linked variants.
4. Generate Pellis and Morandotti dossiers from the same graph.
5. Add a lightweight consistency audit for broken paths, duplicate canonical keys, missing status labels and unresolved dependency IDs.

## 7. Integrity note for this revision

The live main-branch registry is now maintained in `docs/UNIFIED_THEOREM_EDGES.json`: it indexes 280 theorem records from `fabianleonaressi95/theorem`, 14 companion catalogue entries from `fabianleonaressi95/rgs-qlg-quaternion-bridge`, and the typed cross-repository/document links. The 236-record figure above is retained only as the historical curated-list baseline. The two T154 records (In2Infinity and RGS spatial coframe) and the two T155 records (dodecahedral Gauss map and rhombic-cuboctahedron-to-snub-cube transition) have distinct canonical slugs. MQ-T005 is included in the live graph. The register now exposes a unique `record_key` from each full filename stem. Filename-derived classification edges remain provisional and do not certify theorem status.
