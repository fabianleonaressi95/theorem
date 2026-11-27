# Unified research programme — 27-chapter crosswalk and preservation register

**Snapshot:** 24 November 2026  
**Canonical monograph:** monographs/RGS_PSU_PRISM_Q6_QLG_MONOGRAPH_27_CHAPTERS.md  
**Primary repository:** fabianleonaressi95/theorem  
**Companion repository:** fabianleonaressi95/rgs-qlg-quaternion-bridge

This is an integration index, not a new theorem. It connects the 27-chapter monograph, prior research strands, theorem records, companion documents, audits, scripts, data and external literature. It does not replace canonical sources or independently re-prove every statement.

## 0. Preservation and evidence rules

1. The 27-chapter monograph remains the canonical narrative. Do not create a parallel monograph or renumber records.
2. Preserve existing theorem files, source documents, data, scripts, tests, audit outputs and archived material at their canonical paths. This file points to them; it does not replace them.
3. Label every statement as one of: standard theorem/formula; proved internal theorem; exact finite identity; numerical verification; source-reported result; conditional result; candidate bridge; physical hypothesis; open problem.
4. Passing tests verify only the tested implementation and inputs. They do not prove continuum convergence or physical validity.
5. Shared vocabulary, visual similarity, numerical coincidence or a common finite graph is not a proof dependency.
6. Keep eta_D (Dirichlet eta), eta_Ded (Dedekind eta), eta_GK/eta_shear (viscosity) distinct. Keep FDT_geom (project geometric FDT) separate from FDT_fluct (fluctuation-dissipation theorem). Keep D2, d_s, D_H and D_w distinct.
7. PSU expansions (Planck Scale Units / Phase-Space Units / Planck Spherical Units) and the several uses of Anti-Twin are source/model-specific. Do not impose a single meaning without a defining record.
8. Historical values are retained even if provenance is incomplete; label them historical/unverified rather than deleting or upgrading them.

## 1. Snapshot and inventory reconciliation

The default-branch Git tree inspected for this integration has root tree SHA c3331c9ea2d3be56fefeefdd60028a3f0f042f5c. The live tree contains 239 Markdown paths under theorems/, 94 docs paths, 8 monograph/research top-level files, 145 scripts and 108 audit paths (path counts, not counts of executed tests).

The initial graph snapshot listed 236 theorem records, while the live tree contained 239. This discrepancy has now been reconciled: the three omitted paths are TSMR-C-I_iching_golden_q6_lift.md, TSMR-C_cumulative_morphodynamics.md and TSMR-F_multifractal_morphological_equation.md. They were added as theorem-record nodes with provisional thematic-index edges only. The updated registry now has 239 theorem records, 14 companion-catalogue entries, 8 topic hubs, 292 nodes and 323 edges; the 54 reviewed direct crosswalk edges are unchanged. The graph itself warns that filename-derived thematic arrows are not proof dependencies.

The companion repository tree returned 1,192 paths and includes RGS 188D data/provenance, Q6/D5/Wilson, Dirac/QLG, FEEC/Mosco, experiments, reports, scripts and tests. Its reciprocal graph and catalogue must be preserved and reconciled with the primary repository.

## 2. Crosswalk to all 27 canonical chapters

### PART I — Discrete and algebraic foundations

**1. RGS–PSU–PRISM–Q6 architecture.** Connect the whole programme: RGS geometry, PSU variables, Q6 finite complex, PRISM refinement/coding, QLG spinorial sector, QAT as a separately audited physical proposal. Anchors: docs/RGS_PSU_PRISM_QLG_UNIFIED_GEOMETRIC_THEORY.md; docs/UNIFIED_THEOREM_DEPENDENCY_GRAPH.md; docs/UNIFIED_THEOREM_EDGES.json; monographs/00_FROM_FIRST_PRINCIPLES_LIGHT_CUBE_SPHERE_PHI_PSU_QAT.md. Open: common action, state space, observable map and commuting diagram.

**2. Boolean cube Q6: graph, Fourier and Laplacian.** Connect 64 binary states/I Ching hexagrams, 192 edges, degree 6, 240 square faces, Walsh characters, Laplacian, heat kernel and spectral zeta. Anchors: T015–T020, T069, T071, T108; docs/Q6_COMBINATORIAL_HODGE_LAPLACIANS.md; theorems/Q6_GREEN_KUBO_KRYSTALLO_SCALE_BRIDGE_2026-11-23.md; theorems/Q6_GREEN_KUBO_KRYSTALLO_SCALE_BRIDGE_2026-11-23.md. For the standard graph cube, eigenvalues are 2k with multiplicities binomial(6,k), k=0,...,6, so K_Q6(t)=Tr(exp(-tL))=(1+exp(-2t))^6 and Z_Q6(s)=sum_{k=1}^6 binomial(6,k)(2k)^(-s). These are exact for the standard combinatorial vertex Laplacian, not the face Hodge Laplacian.

**3. Cubical 2-skeleton and cellular Anti-Twin.** Connect incidence matrices B1,B2,B3, chain identities, ranks, cohomology, face geometry and antipodal maps. Anchors: T055, T060, T062, T068, T069, T071, T116, T117; theorems/Q6_FACE_COCHAINS_HODGE_GREEN_KUBO_2026-11-23.md; audits/T143B-original-archive-q6-plaquette-certificate.md. The 6-cube has (N0,N1,N2,N3)=(64,192,240,160); the face-cochain record gives ranks 63,129,111, closed 2-cochain dimension 129 and H2=0. Closed cochains are not harmonic cohomology. Distinguish graph antipode XOR 63, recovered coordinate inversion XOR 7 and other model-specific involutions.

**4. Trigrams, bit coding and Kathara geometry.** Connect lower/upper trigrams, I Ching ordering, Q3/Q6 maps, Walsh refinement, Kathara chain constructions and biverso/Möbius coding. Anchors: T060, T062, T116, T117; theorems/TSMR-C-I_iching_golden_q6_lift.md; docs/KATHARA_15_LINE_Q6_CHAIN_LIFT.md; docs/KATHARA_Q6_CHAIN_MAP_GATE_C.md; docs/KATHARA_Q6_NONDEGENERATE_GATE_D.md; docs/TRIGRAM_Q3_WALSH_REFINEMENT_THEOREMS.md. Open: canonicality, nondegenerate cellular lift and preservation of 2-cells; a Q3 map is not automatically a Q6 identification.

**5. Q6 complex, cohomology and Hodge.** Connect cellular de Rham, Hodge Laplacians, Whitney/FEEC maps, heat kernels, spectral dimensions and resolvents. Anchors: T015–T020, T048, T055, T062, T071, T102, T108, T114–T117; docs/Q6_WHITNEY_GEOMETRIC_HODGE.md; docs/Q6_GEOMETRIC_WHITNEY_HODGE.md; docs/Q6_CUBICAL_FIVE_MODE_REFINEMENT.md. Open: weighted inner products, uniform estimates, compatible refinement and continuum convergence. D2 of a measure is not d_s of a heat kernel.

**6. SU(2), SU(3), links and gauge covariance.** Connect link variables, Wilson loops, plaquette holonomy, gauge transformations, quaternionic SU(2), QCD/Yang–Mills and electric flux. Anchors: T013, T014, T020, T049A–T049D, T063, T064, T118, T121, T123; docs/Q6_SU2_CONNECTION_DIRAC_KAEHLER.md; docs/RGS_Q6_SU2_WILSON_BRIDGE.md; docs/RGS_Q6_GAUGED_FULL_CLIFFORD_TRANSPORT.md; docs/Q6_U1_CHARACTER_ELECTRIC_FLUX.md. Open: derive link connection from RGS coframe and prove continuum gauge limit.

**7. Q6–D5: integer quotient, Wilson fibres and annihilator torus.** Connect D5=SO0(5,2)/(SO(5)×SO(2)), Liouville measure, Bergman/Hua density, integer fibre quotient, Wilson integration and annihilator torus. Anchors: T002–T009; docs/Q6_D5_LITERATURE_AND_REPOSITORY_EVIDENCE_MAP.md; docs/Q6_D5_INTEGER_FIBER_QUOTIENT.md; docs/Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md; docs/Q6_D5_BERGMAN_LIOUVILLE_MEASURE_LAW.md; docs/WYLER_D5_INVARIANT_MEASURE_AND_SCALE_THEOREM.md. Preserve no-go and conditional criteria; do not assert Wilson–Bergman identity without its hypotheses.

**8. Wilson, marginal, Bergman and Hua.** Connect gauge averaging, fibre Hessian, Hua normalization, atomic-marginal no-go, five-torus marginal and weak convergence. Anchors: T002–T009 and companion src/scripts/tests for Q6-D5. Open: exact measure pullback and physical interpretation of fibre variables.

**9. Clifford, discrete Dirac and Nielsen–Ninomiya.** Connect cubical Dirac, Dirac–Kähler, Clifford modules, overlap, chirality, spin connection and strong-resolvent refinement. Anchors: T014–T020, T049C–T049D, T114, T115, T118, T123; src/dirac_kahler.py; src/discrete_dirac.py; src/overlap_dirac.py. Finite Q6 is not itself a continuum Nielsen–Ninomiya counterexample; Hilbert spaces and spinor maps must be explicit.

### PART II — Spinorial and spectral geometry

**10. Binary icosahedral group 2I and Poincaré quotient.** Connect 2I, A5, McKay/E8, irreducible representations, S3/2I, Molien series, Reynolds projectors and exact scalar harmonic multiplicities. Anchors: T021–T027, T032–T036, T045, T063, T121, T123; documents/DOCUMENT_A1_EXACT_SPECTRAL_GEOMETRY_S3_2I.md; GAP_sessione_2A5_McKay_2I.html and exact GAP audits. Keep scalar, spinorial, equivariant-bundle and Rumin spectra distinct.

**11. Rumin complex, analytic torsion and determinants.** Connect contact complex, Rumin differential, 2I equivariance, harmonic blocks, Barnes/Hurwitz zeta, finite parts, determinants and twisted torsion. Anchors: T010, T021–T046 (including repeated identifiers with different filenames); audits/results/RUMIN_2I_EXACT_VERIFICATION_2026-11-16.md; src/t032_2i_molien.py through src/t046_hadamard_finite_part_determinants.py where present. Proof order: define complex; prove equivariance; decompose irreps; determine kernels; construct zeta/continuation; compute finite parts; audit full/twisted torsion. Multiplicities alone are not torsion.

**12. Quaternions, SU(2), SO(3) and intertwiners.** Connect unit quaternions, double cover, spatial intertwiners, Weyl/Lorentz extension, spin transport and C6 two-sheet matrix constructions. Anchors: T063, T064, T049C, T049D, T118, T138, T142–T143. SU(2) spatial representation does not determine a Lorentz boost. C6 conference matrix C6²=5I and its 3+3 eigenspaces do not alone prove intrinsic quaternionic structure or compatibility with 2I*.

### PART III — RGS, PSU and spacetime geometry

**13. RGS 188D reconstruction and coordinate audit.** Connect constraint manifold, Jacobian rank, tangent/normal decomposition, Oh action, T2u/T1u sectors, matrix lineage, tetrad/coframe and operator provenance. Anchors: docs/Q6_TANGENT_188D_RECONSTRUCTION.md; docs/RGS_188D_K0_SOURCE_TRACE.md; docs/RGS_188D_OPERATOR_PROVENANCE.md; audits/RGS_188D_K0_SOURCE_TRACE.json; audits/RGS_188D_OPERATOR_PROVENANCE.json; data/rgs_188d/. The recovered audit supports rank-4 constraint Jacobian and 188D tangent kernel for stated data; it does not certify every historical Hessian/eigenspectrum. Equivariance and membership in the proposed kernel are separate tests.

**14. PSU, Anti-Twin and Lorentz symmetry.** Connect two-sheet models, Möbius/biverso, antipodal involutions, phase transport, Lorentz covariance, Q-ball/superfluid and QAT interface. Anchors: T068–T073, T103–T107, T113D–T113F, T118, T123, T142–T143D; docs/PSU_TWO_SHEET_DIRAC_SPECTRAL_BRIDGE.md; docs/RGS_PSU_ANTITWIN_SUPERFLUID_QBALL_BLACK_WHITE_HOLE_ARCHITECTURE.md; docs/RGS_PSU_MULTIFRACTAL_VECTOR_BUNDLE.md. Cellular antipode, 188D geometric antipode and physical two-sheet spacetime are different until a map preserves metric, operators and action. Discrete involution does not imply Lorentz invariance.

**15. PRISM product graph and scale 69,120.** Connect C64 □ C6 □ C6 □ C6 □ C5, periodic product graph, refinement, Fourier symbol, Betti numbers, cycle families, gap and coding dynamics. Anchors: T048, T073, T112–T113F, T125–T127; scripts/rgs_prism_product_refinement.py; scripts/audit_prism_69120.py; reports/prism_69120/. Preserve historical values N=69,120, degree 10, 345,600 edges, active 1,920, 108 cycles length 640, b1=5, b2=10, gap 0.009630546656, omega 0.098135, residual 5.22e-16, 11,725 classes and K³=K²+I, but label them historical/unverified until canonical generator, equivalence relation and representative table are recovered and replayed.

**16. Krist-All: recovery, classes and provenance.** Connect square geometry, trigram classes, finite automata, coding, symbolic dynamics and Merkle/Q-PROOF. Anchors: reports/KRISTALL_RECOVERY_STATUS.md; reports/RECOVERY_MANIFEST.md; PRISM scripts and bundles. The 14-site cube–octahedron graph (48 edges) is distinct from the 69,120-site graph and the 11,725-class classification. Do not merge their data.

**17. FEEC, cubical de Rham and curved geometry.** Connect Whitney forms, FEEC, cochain maps, Hodge, Morandotti meshes, barycentric moments and curved refinement. Anchors: T068, T070, T079–T082, T091–T097, T133–T136; companion docs/Q6_BARYCENTRIC_P1_FEM.md; docs/Q6_WHITNEY_GEOMETRIC_HODGE.md; docs/RGS_MOSCO_CURVED_REFINEMENT_PROGRAM.md; docs/FLAT_TORUS_G6_P1_MOSCO_PROOF.md. Commuting maps, finite identities and flat-torus Mosco do not prove curved Ellis–RGS Mosco; shape regularity, compactness, liminf and recovery sequence remain separate gates.

**18. Golden and supergolden refinements: φ and ψ.** Connect golden ratio φ, supergolden ψ³−ψ²−1=0, Fibonacci/quasicrystal scales, Weber functions, Dedekind eta, discriminant −31, Dirichlet eta, zeta, Gamma/digamma and theta modularity. Anchors: T078, T081–T084, T112, S009, S010; docs/DIGAMMA_SUPERGOLDEN_Q6_PROGRAM_2026-11-10.md; docs/UNITARY_DEDEKIND_DIRICHLET_ETA_BARYCENTRIC_RGS_MORANDOTTI_2026-11-10.md; docs/SYNTHESIS_MOMENTS_BARYCENTRES_GAMMA_BETA_ZETA_MORANDOTTI_2026-11-10.md; docs/GOLDEN_ZETA_MAXWELL_FULLERENE_PROGRAM.md. S009 records the Weber class invariant at D=−31 and reciprocal relation to ψ; CM points of discriminants −31 and −124 are distinct. S010 separates Dirichlet eta, Dedekind eta, L(s,χ−31), Dedekind zeta, Lambert series and Dirichlet/Beta simplex distributions. These are arithmetic identities, not physical laws.

**19. Mosco and geometric continuum limit.** Connect graph/mesh refinement, Dirichlet forms, strong-resolvent and Mosco convergence, spectral convergence, homogenization and possible multifractal measure limits. Anchors: T017–T020, T048, T073, T079, T133–T135; companion RGS_MOSCO_CURVED_REFINEMENT_PROGRAM.md, MOSCO_PROTOTYPE_REGULAR_TORUS.md, FLAT_TORUS_G6_P1_MOSCO_PROOF.md. Open: curved refinement under verified hypotheses and persistence of finite spectral/measure properties. No gap or curvature limit follows from a finite graph alone.

### PART IV — Fields, gravity and phenomenology

**20. Einstein–Cartan, spin and Weyssenhoff fluid.** Connect tetrad/coframe, spin current, contorsion, algebraic torsion, Dirac coupling, four-fermion effective terms and Weyssenhoff assumptions. Anchors: T091, T113A–T113F, T115, T125–T127; docs/EC_DIRAC_ACTION_DERIVATION_AND_CONVENTIONS.md; docs/EC_DIRAC_CONTORSION_AND_INVARIANT_AUDIT.md; docs/EC_DIRAC_FOUR_FERMION_EFFECTIVE_ACTION.md; docs/EC_SPIN_ENSEMBLE_AND_COSMOLOGICAL_ADAPTER.md. A symmetric fourth-moment tensor is not torsion; a Frank–Burgers stress-jump law is not automatically an Einstein–Cartan constitutive equation.

**21. Teleparallelism, vierbein and scalar–torsion actions.** Connect TEGR, spin connection, coframe variation, torsion scalar, boundary terms and comparison with Einstein–Cartan. Anchors: T115 and companion EC/teleparallel dossiers; docs/LEVI_CIVITA_SPIN_CONNECTION_CORE.md; docs/ELLIS_RGS_LEVI_CIVITA_SPIN_CONNECTION.md; docs/RGS_ELLIS_ANALYTIC_SPIN_CONNECTION.md. Open: derive 4D Lorentzian metric, spin connection, action and field equations from RGS data. Nonorientability alone does not prove Pin structure or physical torsion.

**22. QLG: spinorial interface and axial current.** Connect QLG, quaternionic spinors, Dirac–Kähler, SU(2) parallel transport, axial current, Kirchhoff and gauge/fluid sectors. Anchors: T049A–T049D, T113D–T113F, T114–T123; docs/RUBINO_QAT_QUATERNIONIC_SU2_BRIDGE.md; docs/QAT_RGS_KIRCHHOFF_FLUID_GAUGE_AUDIT.md; docs/UNIFIED_MATTER_SPINOR_KIRCHHOFF_MONOPOLE_QCD_MHD.md. Kirchhoff conductances g−,g+ are not automatically gauge coupling, viscosity or inter-sheet polariton coupling; QAT four-current is not automatically the SU(2) connection.

**23. QAT, topological light and cube–sphere geometry.** Connect Quantum Atom Theory (QAT), spherical propagation, phase, photon exchange, cube/sphere and icosahedral geometry, Mandelbrot/Gardi, Maxwell limit and electromagnetic stress. Anchors: T118, T137, T142–T143; monographs/00_FROM_FIRST_PRINCIPLES_LIGHT_CUBE_SPHERE_PHI_PSU_QAT.md; docs/QAT_PSU_Q6_ENTANGLEMENT_EMERGENT_GEOMETRY.md; docs/RGS_FOURTH_MOMENT_MAXWELL_BRIDGE.md; docs/GOLDEN_ZETA_MAXWELL_FULLERENE_PROGRAM.md. Gardi (2013), DOI 10.1117/12.2023739, is a speculative cosmological proposal. Distinguish Mandelbrot parameter set, filled Julia set and Julia boundary. Open: field equation/action, conservation, covariance, Newton/Maxwell/GR limits and falsifiable predictions. Conserved isotropic flux gives 1/(4πr²) in 3D but does not derive mass or gravity.

**24. Wormholes, EMS models and stability.** Connect Ellis geometry, Einstein–Maxwell–scalar models, Q-ball/Q-shell, two-sheet PSU, parameter recovery, stability and energy conditions. Anchors: docs/RGS_PSU_WORMHOLE_PARAMETER_RECOVERY_AUDIT.md; docs/RGS_PSU_QBALL_STATIONARY_AND_COUPLED_ACTION.md; docs/RGS_PSU_GAUGED_QBALL_MAXWELL_BVP.md; docs/RGS_PSU_GAUGE_CLIFFORD_QLG_RESEARCH_PROPOSAL.md. Open: recover parameters, derive BVP equations and stability; a two-sheet drawing is not evidence of a physical wormhole.

**25. Spin glass, correlators and cellular dynamics.** Connect TSMR, Markov measures, Bernoulli convolution, pair automata, multifractal spectra, Koopman, correlations, relaxation-rate measures and Green–Kubo. Anchors: T069, T072, T078, T099–T108, T110–T113, T131–T132; theorems/TSMR-C-I_iching_golden_q6_lift.md; theorems/TSMR-F_multifractal_morphological_equation.md; docs/TSMR-FDT_comparative_note.md; docs/PHASE27_KOOPMAN_RGS_PSU.md. TSMR-F gives exact definitions and separated Cantor–Bernoulli special cases; anisotropic pressure is a finite-level diagnostic. The project lower correlation dimension D2≈0.6041966 requires its exact measure definition, data and reproducible audit with every use. A Legendre transform is not automatically the true Hausdorff spectrum. Green–Kubo inverse-rate formulas require a suitable positive spectral representation, no problematic zero mode and finite inverse moment; open/nonreversible systems require a separate response theory.

**26. Topological synchronization, hysteresis and industrial applications.** Connect cycle/cocycle holonomy, phase synchronization, XY/BKT/KTHNY, vortex defects, hysteresis, fatigue, seams, Morandotti mechanics and industrial datasets. Anchors: T076, T078–T082, T091–T097, T100–T110, T112–T113, T125–T136; docs/INDUSTRIAL_HYSTERESIS_DATASETS.md; docs/KTHNY_N4_SYM_RGS_PRISM.md; docs/rgs_defect_benchmark/; docs/64TG_VESICA_MORANDOTTI_BRIDGE.md. Open: calibrated observables and independent validation.

### PART V — Synthesis

**27. Unified theory: requirements and order of work.** Preserve existing sections 27.1–27.10, the T091–T109 register, reuse of previous results, physical bridge references and XY/BKT programme. The unifying question remains:
\[
\boxed{\text{Can geometry and invariant measures determine operator spectra,}\\
\text{relaxation correlations and quantitative response laws?}}
\]
Research chain:
\[
\text{geometry/symbolic dynamics}\to\text{measure and transfer operator}
\to\text{spectrum/zeta/heat kernel}\to\text{correlation/relaxation}
\to\text{response/transport}\to\text{experiment}.
\]
Every arrow must have a relation type, assumptions, evidence and proof obligation.

## 3. Cross-cutting connections that must not be lost

### A. Vesica, equilateral geometry, Eisenstein integers, φ and ψ
Preserve T137 (Vesica filename), T142, T143 and T143D; docs/VESICA_NEEDHAM_BONILLA_SQRT3_PHI_DOSSIER_2026-11-18.md; docs/VESICA_PENTAGON_FRAME_BRIDGE.md; docs/VESICA_STAR_DAVID_JITTERBUG_PHASE_BRIDGE.md; docs/VESICA_ANISOTROPIC_DTN_MODEL.md; docs/64TG_VESICA_MORANDOTTI_BRIDGE.md. Equal-circle separation r gives common chord √3r. The normalized intersection points realize cube roots of unity and the Eisenstein lattice Z[ω], ω=exp(2πi/3). This is an exact triangular/hexagonal arithmetic bridge, not an identification with Q(√5). The golden/icosahedral and supergolden/Weber branches remain distinct until a map is proved. The DtN and holonomy gates remain open.

### B. Dirichlet eta, Dedekind eta, Gamma/Beta, zeta and barycentres
Preserve
\[
\eta_D(s)=(1-2^{1-s})\zeta(s),\quad
\eta_{Ded}(\tau)=q^{1/24}\prod_{n\ge1}(1-q^n).
\]
Also preserve L(s,χ−31), ζ_K(s)=ζ(s)L(s,χ−31), Euler Gamma/digamma, Euler Beta and Dirichlet simplex distributions. Anchors: S009, S010, T070, T078, T081–T084, T068 and the 10-November synthesis dossiers. The Mellin identity Γ(s)η_D(s)=integral x^(s−1)/(e^x+1) dx for Re(s)>0; divisor-sum Dirichlet series; and quadratic factorization at discriminant −31 are analytic/arithmetic identities. They do not define a physical partition function without a physical measure and observable. Fredholm determinant identities require trace-class or explicitly regularized operators and a specified Hilbert space/domain.

### C. Mandelbrot, Minkowski–Farey and multifractality
Mandelbrot: P_c(z)=z²+c; distinguish M, filled Julia K_c and Julia boundary J_c. Shishikura proves dim_H(∂M)=2; this is not cosmological dimension. Minkowski question-mark is strictly increasing and singular; its conjugacy with a tent map is valid only for a specified Farey map, branches and endpoint conventions (Panti is a key precise reference). The project h(α)=α/(2−α) and G=h^−1∘F∘h are an additional coordinate conjugacy, not part of Panti's theorem. TSMR-F defines IFS, invariant measure, partition sum, τ(q), D_q and candidate Legendre spectrum; verify separation/overlap and limit existence. Q6 D2≈0.6041966, polariton contour 7/4, Mandelbrot boundary dimension 2, d_s and D_w are not interchangeable.

### D. Dynamical zeta and transfer operators
The rigorous bridge is periodic orbits → transfer/Ruelle operator → dynamical zeta/Fredholm determinant → resonances and decay of correlations. References: Ruelle; Baladi, Periodic Orbits and Dynamical Spectra; Liverani (2005), DOI 10.3934/dcds.2005.13.1203; Giulietti–Liverani–Pollicott (2013), DOI 10.4007/annals.2013.178.2.6; Lapidus–van Frankenhuijsen, Fractal Geometry, Complex Dimensions and Zeta Functions. A project transfer operator needs a function space, domain, trace/determinant class and dynamical hypotheses.

### E. Green–Kubo, Koopman and polaritons
T131 records phonon/phason normal modes, stress correlations and tensorial Green–Kubo; finite dissipative transport requires a justified relaxation mechanism. T132 gives a coupled phonon–phason OU benchmark. The 23-November face-cochain record gives exact cubical incidence, closed 2-cochain sector and OU/GK functional, but does not identify the observable as physical shear stress. The 23-November Krystallo bridge gives K(nπ/2)=2^n=|V(Q_n)| and a reversible OU inverse-spectral sum; it explicitly obstructs identifying the reversible relaxation generator with a supergolden companion matrix having non-real eigenvalues. Koopman U_tA=A∘Φ_t requires specified invariant state, centered subspace and generator conventions. Carati–Galgani (2014), DOI 10.1140/epjd/e2014-50549-8, supplies a classical microscopic dielectric Green–Kubo bridge. Panico et al. (2023), DOI 10.1063/5.0167655, report conformal/fractal scaling in exciton-polariton turbulence, including 7/4 contour dimension. Modern polaritons are driven-dissipative; equilibrium GK/FDT cannot be assumed. Comparison must align observable, measure, finite-size window, estimator, uncertainty, pumping/loss and time window.

### F. Geometric FDT, fluctuation-dissipation and Schwarzschild
T106–T107 are project Q6/FDT defect and Gibbs tests. Keep FDT_geom distinct from FDT_fluct. Schwarzschild gives Rs=2GM/c² and r_ph=3GM/c², hence Rs/r_ph=2/3. This does not identify α with Rs/r. The project h and h(2/3)=1/2 are exact algebra once defined; the physical mapping remains open. Deformed photon-sphere literature (e.g. Shoom) and EFT corrections are comparisons, not proof of this map.

### G. Morandotti, Frank–Burgers, moments and FEEC
Preserve T068/T070 → T079–T084 → T091–T099 → T124–T136. T068 is a local triangle centroid/covariance identity; T070 uses Dirichlet weighted barycentres; fixed-cloud fourth moments and fourth jump moments of refinement stencils are distinct tensors. A fully symmetric fourth-moment residual is not torsion. Airy stress does not determine Burgers holonomy alone (T096). Finite mesh tests do not prove curved Mosco or physical constitutive laws.

### H. QCD, MHD, entanglement and nonstandard source dossiers
Preserve Q6 gauge/Wilson and Yang–Mills; QLG spinor/Kirchhoff/monopole; QHD–Euler–MHD and vortical flows; PSU–Anti-Twin two-sheet Dirac; QAT–PSU–Q6 entanglement/emergent geometry. Van Raamsdonk, Ryu–Takayanagi, Maldacena, Swingle and Tononi are comparison frameworks, not identifications with Q6. De Aquino, Rauscher, Fortunadrago–Ighina and other nonstandard proposals remain critical-source dossiers, not established evidence. Anchors: docs/QAT_PSU_Q6_ENTANGLEMENT_EMERGENT_GEOMETRY.md; docs/UNIFIED_MATTER_SPINOR_KIRCHHOFF_MONOPOLE_QCD_MHD.md; docs/RGS_PSU_HILBERT_CANTOR_QHD_MONOPOLE_MHD.md; docs/PHASE27_KOOPMAN_RGS_PSU.md.

## 4. Theorem cluster navigation

| Cluster | Records / materials | Caution |
|---|---|---|
| Q6 Boolean/Fourier/Dirac | T013–T020, T055, T069, T071, T108, T114–T117 | finite exactness vs continuum |
| Q6–D5/Wilson/Bergman | T002–T009; D5 docs/scripts | no-go and conditional criteria remain |
| 2I/Poincaré/Rumin | T010, T021–T046, T063, T121, T123; A1/GAP | scalar/spinorial/contact spectra differ |
| RGS 188D/PSU | T049, T068–T073, T113D–T113F, T115 | provenance and kernel identification |
| PRISM/Krist-All | T048, T073, T112–T113F, T125–T127 | graph vs 14-site model; historical class data |
| Morandotti/moments | T068, T070, T079–T084, T091–T099, T124–T136 | exact local identities vs numerics/continuum |
| FDT/cycles/holonomy | T100–T110 | project FDT vs response FDT |
| Phonon/phason/GK | T113A–T113F, T131–T132; 23-November Q6 records | physical stress map open |
| Vesica | T137 Vesica file, T142, T143, T143D | exact geometry vs conditional embeddings |
| Arithmetic/special functions | S009, S010, T078, T081–T084, T070 | identities do not imply physical laws |
| TSMR/fractals | TSMR-C-I, TSMR-F, T072, T078, T099, T108 | D2 provenance and multifractal limits |
| QAT/Maxwell/QLG/gravity | T118, T113*, T114–T123; QAT audits | field derivation and falsifiable predictions |

**Identifier collision:** several identifiers are reused by distinct files (including T137, T099, T024, T030, T032, T033, T034 and T045). Always cite full filename and title, never a bare number.

## 5. External bibliography — core anchors

**Fractal/complex dynamics:** Douady–Hubbard, Étude dynamique des polynômes complexes (1984–85); Shishikura (1998), Annals of Mathematics 147, 225–267, DOI 10.2307/121009; Lapidus–van Frankenhuijsen, Fractal Geometry, Complex Dimensions and Zeta Functions; Gardi (2013), SPIE 8832, 883210, DOI 10.1117/12.2023739 (speculative cosmology only).

**Minkowski/Farey:** Denjoy (1938); Salem (1943); Panti (2008), DOI 10.1007/s00605-008-0535-3; Rockett–Szüsz, Continued Fractions.

**Dynamical zeta:** Ruelle, Dynamical zeta functions and transfer operators; Baladi, Periodic Orbits and Dynamical Spectra; Liverani (2005), DOI 10.3934/dcds.2005.13.1203; Giulietti–Liverani–Pollicott (2013), DOI 10.4007/annals.2013.178.2.6.

**Response/transport:** Kubo (1957), JPSJ 12, 570–586, DOI 10.1143/JPSJ.12.570; Kubo–Yokota–Nakajima (1957), DOI 10.1143/JPSJ.12.1203; Forster (1975), Hydrodynamic Fluctuations, Broken Symmetry, and Correlation Functions; Hayashi–Sasa (2006), DOI 10.1016/j.physa.2006.03.007; Carati–Galgani (2014), DOI 10.1140/epjd/e2014-50549-8.

**Polaritons:** Panico et al. (2023), Applied Physics Reviews 10, 041418, DOI 10.1063/5.0167655; Panico et al. (2023), Nature Photonics, DOI 10.1038/s41566-023-01174-4; Koniakhin et al. (2020), DOI 10.1016/j.chaos.2019.109574; Claude et al. (2023), PRB 107, 174507, DOI 10.1103/PhysRevB.107.174507.

**Vesica:** M. M. Baldi (2020), On a Property of the Vesica Piscis, Zenodo DOI 10.5281/zenodo.4273133 (working-paper/preprint status); Barrallo–González-Quintial–Sánchez-Beitia (2015), DOI 10.1007/s00004-015-0253-9; Needham, Visual Complex Analysis (1997), cube roots of unity/equilateral geometry, not unrelated circle-mapping exercises.

**Modular/arithmetic:** Yui–Zagier (1997), Weber class invariants/class polynomials; preserve the exact source-check provenance in S009. Use standard primary references for Dedekind eta, Dirichlet eta/L, Hurwitz zeta, Gamma/digamma, Euler Beta and Dirichlet simplex distributions. Do not conflate the eta functions.

## 6. Required evidence schema for each new connection

Each graph edge or matrix row must record: stable ID; full source path; monograph chapter; internal theorem endpoints (filename/title/repository); external citation and exact page/theorem; shared mathematical object; relation type (proves, implements, uses-definition, representation-input, discretizes, candidate-successor, application-of, comparison-only, open-obligation); evidence available; assumptions; epistemic status; reproduction command; input version; SHA-256 and commit SHA; explicit non-implications and next proof gate.

## 7. Reconciliation queue

1. Resolve live 239 theorem paths vs graph's 236-record inventory; classify the three-path delta.
2. Compare every theorem path with the master catalogue and 14 companion entries; retain duplicate-number records as separate path-addressed nodes.
3. Attach every theorem/dossier to one or more of the 27 chapters; add cross-references, not copied theorem text.
4. Integrate S009/S010 with chapters 11 and 18 and cross-reference chapters 2, 5, 7, 8 and 25.
5. Integrate Vesica T137/T142/T143/T143D with Morandotti T091–T099, Needham/Eisenstein geometry, √3 and separate DtN/holonomy gates.
6. Integrate Mandelbrot, Minkowski/Farey, TSMR-C-I, TSMR-F, Q6 D2 and PRISM coding while preserving dimension distinctions.
7. Integrate T100–T107, T131–T132 and both 23-November Q6 Green–Kubo records with Koopman, Carati–Galgani and polariton experiments; keep physical stress identification open.
8. Integrate QAT with Maxwell, quaternionic SU(2), Kirchhoff, entanglement, Einstein–Cartan and teleparallel records only through explicit field/action maps and falsifiable predictions.
9. Verify reciprocal graph, companion catalogue, linked source files and provenance of RGS 188D/Q6-D5/FEEC/Mosco/QLG material.
10. Avoid bulk rewrite and oversized CI. Make small traceable patches after endpoint audits.

## 8. Synthesis

The defensible common programme is not an asserted equality among Vesica, Mandelbrot, zeta, Q6, polaritons and gravity. It is the testable research chain
\[
\boxed{\text{geometry/combinatorics/symbolic dynamics}
\to\text{measures and transfer operators}
\to\text{Hodge, Dirac and Koopman spectra}
\to\text{zeta, heat kernels and resonances}
\to\text{correlations and relaxation}
\to\text{linear response and transport}
\to\text{measurable predictions}.}
\]
The monograph already contains most of the mathematical and computational sectors needed to investigate it. The next work is to complete the crosswalk, reconcile inventory drift and prove each connecting map at its proper level, preserving every prior result and every open caveat.


## 9. Supplemental strands recovered from the 23–24 November conversations

These items extend the chapter crosswalk and must remain linked to their existing source records. They are included because they were developed in prior conversations and should not disappear merely because they sit in appendices or newer research branches.

### 9.1 Fullerene C60/C64, Stone–Wales 90° and Vesica–Kathara–Q6

**Existing dossiers:** research/FULLERENE_STONE_WALES_90_DEGREE_VESICA_BRIDGE.md; docs/VESICA_NEEDHAM_BONILLA_SQRT3_PHI_DOSSIER_2026-11-18.md; docs/VESICA_STAR_DAVID_JITTERBUG_PHASE_BRIDGE.md; docs/64TG_VESICA_MORANDOTTI_BRIDGE.md; C60 transport cross-audits in C60_TRANSPORTS_GH_CROSSAUDIT_2026-11-21.md and the associated JSON.

Preserve the exact graph/fullerene counts:
- C60 truncated icosahedron: 60 vertices, 90 edges, 32 faces = 12 pentagons + 20 hexagons.
- Classical C64 fullerene: 64 vertices, 96 edges, 34 faces = 12 pentagons + 22 hexagons.
- C60→C64 requires ΔV=4, ΔE=6, ΔF=2 and carbon insertion/growth. It is not a Stone–Wales move.
- Stone–Wales 90° is a local bond reconnection; it conserves atom/vertex count and is distinct from growth. The move redistributes local connectivity and face structure; the IPR is impossible for C64 with 12 pentagons.

The candidate crosswalk to Kathara–Q6 is the commutative condition R' S90 = Q90 R, with the existing chain maps R0∈Z^(64×12), R1∈Z^(192×21), R2∈Z^(240×10). Their chain identities and T116 nondegenerate rank condition rank(R2)=10 are already reported as satisfied for the original construction. The new obligation is to verify the chain identities after the Stone–Wales move and build explicit pre/post incidence matrices. A rigid rotation Q'=U90 Q U90^T preserves eigenvalues; a Stone–Wales reconnection changes connectivity and relaxed electronic density, so spectral invariance cannot be inferred from rigid rotation.

**Status:** geometric/counting identities exact; Stone–Wales ↔ Kathara–Q6 map candidate; C60→C64 selective conversion unproved; electronic tensor/transport bridge requires pre/post graph, incidence matrices and a defined electronic model. The article branch research/h2-de-aquino-response was merged through PR #403 on 23 November 2026 (merge commit a07c2fea55484c1ce16cec87ddc538bc0401bc6b). Its reported 8/8 regression result and claim ledger are software/research evidence, not a physical validation. The earlier branch commit 15fd00f140b8afba78795afaf02007cc5a56edc5 is retained as provenance.

### 9.2 Q6–I Ching golden lift, cumulative morphodynamics and TSMR-F

Three previously unindexed theorem files were reconciled into the 239-record dependency graph:
- TSMR-C-I_iching_golden_q6_lift.md → provisional Q6 thematic hub.
- TSMR-C_cumulative_morphodynamics.md → provisional PRISM/symbolic-dynamics hub.
- TSMR-F_multifractal_morphological_equation.md → provisional PRISM/symbolic-dynamics hub.

**TSMR-C-I exact finite coding:** lines are read bottom-to-top, yang=1 and yin=0. 100 is Zhen (Thunder), 011 is Xun (Wind/Wood). With λ=φ^−1 and λ²=1−λ, the trigram observable π3(g)=d0+d1λ+d2λ² has the exact collision π3(100)=π3(011)=1. The six-line observable π6(h)=Σ d_k λ^k maps 64 hexagrams to 33 values. This scalar partition is not strongly lumpable for the Q6 random walk: 21 of the 33 classes have differing transition profiles. The 64-state lift must be retained, or sufficient memory added.

**TSMR-C cumulative morphodynamics:** for atomless Borel probability μ on [a,b], Fμ(x)=μ([a,x]) is continuous and nondecreasing; it is strictly increasing iff every nonempty open interval has positive μ-mass (full support). Then Fμ pushes μ to uniform Lebesgue measure. If μ is singular, F'μ=0 Lebesgue-a.e. Full support and singularity are independent properties. The golden Bernoulli application at λ=φ^−1 is conditional on the required non-atomicity, full-support and singularity results; it is not identified with the Minkowski question-mark measure. A conjugacy transported by Fμ requires Fμ to be a homeomorphism and the dynamics to be specified on both spaces.

**TSMR-F:** the IFS attractor and self-similar measure equations are exact; separated two-branch Cantor–Bernoulli generalized dimensions are exact under separation. The anisotropic singular-value pressure in the record is a finite-level diagnostic; existence of a limiting pressure, equality with Hausdorff dimensions and the multifractal formalism need additional assumptions. A fractal support alone does not imply a multifractal measure.

**Recent Q6 automaton evidence from 24 November:** the project audit reports 5,566 pair-automaton states, 34,762 transitions and 13 golden differences; the certificate ||A^20||∞=9412274067081088; atomlessness and the lower bound D2≥0.6041966 are reported as proved in the project record. The support interval, singularity versus absolute continuity, existence of exact local dimension and full f(α) remain open. This is project-specific and must always be cited with the precise measure definition, automaton construction, data and audit. Do not restate the lower bound as an exact value D2=0.6041966.

**Test provenance:** earlier TSMR-02 work reports test suites A/B/C (8+6+7=21 checks) on controlled IFS, vesica and discrete-complex examples. These tests do not prove that the real Q6/PRISM measure is multifractal or that a Vesica attractor has a physical interpretation. PR #405 was verified merged on 24 November 2026 (merge commit 8e9cedd1269a78bae5058d093f5738166e9bc2b0). PR #406, the comparative TSMR-Q6/FDT research note, was also verified merged on 24 November 2026 (merge commit 5717f954c28b386b07071ee54394d0279d1573e9). These merges preserve the research records; they do not promote open physical interpretations to established laws.

### 9.3 Minkowski M1–M3, Farey, singular functions and SLE

Preserve the three project records M1/M2/M3 separately:
- M1: Q6 Hölder/gauge/strong-resolvent question. A proposed Hölder counterexample does not refute the theorem; Q6 finiteness does not itself imply continuum Nielsen–Ninomiya.
- M2: Minkowski–Q6 one-axis reflection.
- M3: Minkowski–Q6 D4 cell-orbit closure.

M2/M3 are exact finite symmetry/closure audits under their declared actions, not a proof that the classical Minkowski question-mark function is the cumulative distribution of the golden Bernoulli measure. The latter is a separate measure-theoretic problem (TSMR-C).

The polariton comparison uses Panico et al.'s 7/4 contour scaling and SLE/percolation interpretation. This must be compared to Q6 only after matching the random object, observable, measure, finite-size scaling and universality class. Do not compare 7/4 directly to the Q6 lower correlation dimension, the Hausdorff dimension 2 of the Mandelbrot boundary, or the spectral dimension of a graph.

### 9.4 PRISM Fibonacci/QVSM and the R0/R1/R2 maps

The previously obtained R0, R1 and R2 results are to be reused, not rediscovered. The Kathara–Q6 chain maps have declared shapes 64×12, 192×21 and 240×10; their chain identities were already checked, with T116 recording the nondegenerate lift and rank(R2)=10. The next task is a post-move comparison for Stone–Wales, not a fresh derivation of the original maps.

The PRISM Fibonacci/QVSM branch contains exact algebraic scale identities and separate numerical phase/sector audits. Keep the 69,120-site graph, Fibonacci block data, QVSM phases and the 14-site cube–octahedron model distinct. The supergolden companion matrix Aψ and its characteristic polynomial λ³−λ²−1=0 are an algebraic object; its non-real eigenvalues obstruct identifying it directly with a reversible self-adjoint relaxation generator. Historical R0/R1/R2 values and phase scans must retain their input hashes and scripts.

### 9.5 Golden zeta, cotangent, Fibonacci transfer and fullerene/Maxwell bridge

The 23-November golden-zeta dossier reports exact identities including
\[
\Delta_5=\pi\sqrt{25+10\sqrt5}=\pi\sqrt{15+20\varphi},
\]
and the standard expansion of π cot(πx) in even zeta values for 0<|x|<1 (x=0 is a pole). The constant Cφ=8.0802127733210986785… and Fibonacci transfer roots (2.611461069, 5.222922137, …) are recorded numerical values, not independent physical constants. The zeta–φ–cotangent identities are analytic; the Maxwell/fullerenes connection remains a programme until the electromagnetic tensor is derived from the fullerene graph and calibrated.

### 9.6 Bibliographic originality and finite-type overlap literature

The finite-type/graph-directed overlap framework is established in the literature (including work by Lau–Ngai, Ngai–Wang–Dong, Feng–Feng, Rutar and Xie). The specific Q6–I Ching golden Markov construction may be a novel model, but its originality is not bibliographically certified by the existence of general finite-type machinery. The comparative literature review must identify the precise object, transition matrix, overlap type and theorem that is new.

### 9.7 Other preserved physical and historical strands

Keep the following as linked comparative dossiers, not as unverified consequences of RGS:
- Wyler/D5/fine-structure constant: invariant measure and normalization audit, ETH/IAS archive trail and correspondence; no claim that a numerical match alone derives α.
- Ratti vacuum-extraction proposal: critical bibliography and quantitative falsifiability audit; not evidence for vacuum energy extraction, FDT or RGS.
- De Aquino, Rauscher, Fortunadrago–Ighina and related nonstandard claims: source-provenance and critical audit only.
- Florenskij's reverse perspective and icosahedral/C6 comparisons: geometric/art-historical analogy and exact finite matrix identities kept separate from physical spin.
- Pellis scalar spectrum and 2I representation dossiers; Morandotti collaboration; QCD/Yang–Mills, monopole, QHD–Euler–MHD, Q-ball and wormhole branches; entanglement/AdS-CFT comparisons (Van Raamsdonk, Ryu–Takayanagi, Maldacena, Swingle, Tononi); De Aquino threshold and other proposed physical correspondences.
- The network-dynamics application (knowledge/resilience/competence models) remains an application programme with its own source register, model specification, data dictionary, tests and implementation status; it is not a theorem of the 27-chapter physical monograph.

## 10. Conversation-to-repository preservation principle

Conversation summaries are useful discovery indexes, not substitutes for the canonical source files. Where a prior chat reports a result, this register preserves the exact claim and its reported status, but the current theorem file, audit, commit and data hash take precedence. The full conversation archive is not represented as exhaustively re-read in one operation; this is a consolidated recovery from available prior-chat context plus the live repository snapshots. New recovered strands should be appended here and cross-linked to their canonical records rather than copied into theorem statements.


## 11. Live GitHub issue register and Jitterbug–coil work package (checked 24 November 2026)

This section records actionable open work, not merely thematic connections. Issue state was fetched from GitHub on 24 November 2026. Closing an issue requires its acceptance criteria and reproducible evidence, not just a related PR merge.

### 11.1 Jitterbug geometry and electromechanical coil

**Merged source work — do not redo:**
- [PR #202 — Exact quaternionic symmetric Jitterbug kinematics](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/202), merged 23 November 2026, merge commit 4a26e44b7ed3caaa27b3c1d31832f2426e4de03f. Records the symmetric cuboctahedron-to-octahedron vertex path, rigid-face quaternion pose and translation, with separate ellipse parameter θ and face rotation γ. Reported prototype residuals were about 4.4×10⁻¹⁶ over 101 parameter samples. The committed audit/CI provenance must be checked before describing this as fully CI-certified.
- [PR #390 — Explicit Jitterbug panel-to-coil Faraday model](https://github.com/fabianleonaressi95/theorem/pull/390), merged 23 November 2026, merge commit d7ee4c6e6447944574e2b8236f8a5760805b85d6. A circular N-turn coil is rigidly mounted in one labelled triangular panel ε=(+1,+1,+1); panel pose is recovered by proper Kabsch fit from its three labelled vertices. Given a declared physical traversal speed, the model computes flux linkage, midpoint Faraday emf from the SO(3) increment, and series RL current response. Five unit tests are included, but the PR states they were not run in its authoring environment. Reproduce with:
  python3 audits/jitterbug_coil_coupling.py --output jitterbug_coil_report.json
  python3 -m unittest discover -s tests -p 'test_jitterbug_coil_coupling.py' -v
- [PR #394 — Vesica, Star-of-David, Q6 phases and Jitterbug bridges](https://github.com/fabianleonaressi95/theorem/pull/394), merged 23 November 2026, merge commit f3599b388309abce08a86c1e82edbf7e777193e1. Reuses T091/T092/T097–T101 and T142/T143; the Möbius sector map and boundary phase identity are established on their stated domain. It explicitly leaves the six-planar-sector/eight-panel incidence map, full mixed frame and torsion coupling open.

**Gray geometry baseline:** the standard symmetric Jitterbug uses eight rigid equilateral triangular panels, 12 vertices and 24 rods/edges; its principal motion connects the cuboctahedral/Vector Equilibrium and octahedral configurations, with the icosahedral intermediate. The Gray curve constraint is \(3Y^2+Z^2=L^2\); θ and γ are distinct and, under the PR #202 convention, \(\gamma=\arctan(\sqrt3\tan\theta)\). Do not conflate this with the separate 64-TG cellulation or planar six-sector Star of David.

**Coil physics boundary:** this is a conditional electromechanical realization requiring explicit B-field, N, coil radius, panel geometry, traversal speed, resistance and inductance. Geometry alone does not predict voltage or current. The continuation parameter is not physical time until a speed law is declared. The one-panel coil is not yet a complete eight-panel generator, measured experiment or new electromagnetic law. Next: reproduce tests; sweep θ/γ and verify flux/emf/RL energy balance; compare symmetry-related panel placements and signs; then formulate multi-coil wiring, mutual inductance and phase sequence; finally add measured field/coil/drive data.

### 11.2 Four coupled open derivation issues

- [#398 — Vesica phase ↔ eight-panel Jitterbug frame map](https://github.com/fabianleonaressi95/theorem/issues/398). Define eight panel labels and oriented hinge-incidence graph; map Vesica/hexagram phase branches without forcing a 6↔8 bijection; derive panel frames and transitions; test rigidity and endpoint configurations. Depends on T098/T099, PR #394 and Gray/Verheyen/Matsumoto–Segerman. **Open.**
- [#399 — Complete mixed-frame field A_a^m](https://github.com/fabianleonaressi95/theorem/issues/399). Derive the Ehresmann connection from the phase-to-panel embedding, including coordinate transformation, curvature F_ab^m, horizontal/vertical brackets and a variational or kinematic selection principle. Do not identify Ehresmann curvature with Cartan torsion. **Open.**
- [#400 — Cartan torsion and T B_perp variation](https://github.com/fabianleonaressi95/theorem/issues/400). Differentiate the complete coframe retaining e, φ and A; define B_perp as a representation-carrying tensor/bivector; construct a dimensionally consistent invariant action; vary independently in all fields. A symbolic product T B_perp is not yet an action. **Open.**
- [#401 — Dynamic 64-TG/FCC-D3 immersion into Jitterbug](https://github.com/fabianleonaressi95/theorem/issues/401). Start from the static 63-vertex, 240-edge, 64-tetrahedron reconstruction (56 internal + 8 external), 14 octahedral cavities and 24 square pyramids. Construct the configuration-space map; certify incidence, Jacobian rank/nullity and finite-branch continuation through VE, icosahedral and octahedral poses. Add masses, inertia and coil/RL dynamics only after kinematics. **Open.**

Proposed work order: #398 → #399 → #400, with #401 consuming the phase/frame map and merged static 64-TG and one-panel coil submodels. This is a work-order proposal; only proved dependencies become proof edges.

### 11.3 Unified provenance and source-data issues

- [#402 — Expand unified theorem graph with prior-chat provenance and bibliography](https://github.com/fabianleonaressi95/theorem/issues/402). **Open at this audit.** Covers conversation-to-theorem provenance, bibliography, warning register, Pellis/Morandotti, Vesica/gradient/barycentre, Frank–Burgers, Jitterbug, 64-TG/FCC-D3, coil/RL and Q6 Clifford/2I. This document addresses part of #402 but does not close it until citations, provenance, graph endpoints and warning closure criteria are audited.
- [#109 — Import original source data for 188D and Krist-All](https://github.com/fabianleonaressi95/theorem/issues/109). **Open.** Original NPZ and bundle hashes are recorded in the issue; original 64×3 X_Oh coordinates remain to be recovered from generator/source. Krist-All still lacks the 11,725-class enumerator/table, formal equivalence relation and K/W0 source data. Do not fit or fabricate.
- [Companion issue #3 — Gauge-equivariant QLG and Clifford-steerable operators](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/issues/3). **Open.** Tracks Q6 complex, Möbius subcomplex, gauge covariance, 2I representations, Pin+ lift scope, Clifford grade actions and Mosco/continuum questions. T114–T123 and source PRs are milestones, not closure of continuum or physical-coupling questions.

### 11.4 Experimental validation issues

- [#113 — Open experimental actuator hysteresis data and asymmetric GPI baseline](https://github.com/fabianleonaressi95/theorem/issues/113). **Open.** Requires licensed raw actuator cycles, checksum/schema, held-out complete-cycle fits and uncertainty; compare Preisach, PI, asymmetric GPI and Bouc–Wen. Do not confuse pneumatic actuator hysteresis with magnetic loops or Cartan torsion.
- [#114 — Jiles–Atherton against measured ferromagnetic loops](https://github.com/fabianleonaressi95/theorem/issues/114). **Open.** Verify dataset version, checksum, licence, units, frequency and geometry; fit/validate on held-out loops; report coercivity, remanence, saturation, loop area and errors. Keep INRIM first-magnetization curves distinct from the HEFMAG main loop archive and separate NO/GO sample archive. Quasi-static fits do not establish dynamic losses or FDT–Maxwell coupling.

### 11.5 Q6–D5 and Wilson computational issue

- [#84 — Port and certify Q6–D5 Wilson integer-fibre computation](https://github.com/fabianleonaressi95/theorem/issues/84). **Open.** Requires exact Smith normal form, saturated rank-124 kernel, rank-5 quotient, certified positive fibre sum and rigorous tail interval, plus Poisson/Gaussian comparison. No Hua/Bergman limit or physical 3+1D reduction follows automatically.

### 11.6 Current open-issue inventory

GitHub returned nine open issues in the primary repository at this check: #398, #399, #400, #401, #402, #109, #113, #114 and #84. The companion repository returned open issue #3. This is a live snapshot, not a permanent status guarantee. The four Jitterbug derivation issues are the immediate geometric chain; the coil model is already merged as a conditional one-panel calculation and should be validated/reused rather than reimplemented.


### 11.7 Eight-coil coupled-circuit implementation draft — PR #411

- [PR #411 — eight-panel Jitterbug coil coupling](https://github.com/fabianleonaressi95/theorem/pull/411) adds `audits/jitterbug_eight_coil_coupling.py`, one circular coil per rigid triangular panel, proper Kabsch panel poses, imposed-field flux linkage, external Faraday emf, polygonal regularized Neumann mutual inductances, thin-wire self-inductance approximation and an implicit-midpoint solver for \(d(Li)/dt+Ri=e_{ext}\).
- [Primitive tests](../tests/test_jitterbug_eight_coil_coupling.py) cover polygon closure, mutual-inductance reciprocity, positive thin-wire self-inductance, matrix symmetry, zero-emf/zero-current and a finite one-coil RL response.
- [Technical note](JITTERBUG_EIGHT_COIL_COUPLING.md) states approximations and reproduction commands.

**Status:** draft PR, not merged; no clean-run test evidence yet. The full model has not passed segment/softening convergence, a trusted two-loop benchmark, positive-semidefinite verification across the path, wiring/polarity comparison or complete mechanical/electromagnetic energy balance. No experiment or generator performance is claimed. PR #411 does not close #398–#401 or #409. The 64-TG/FCC-D3 embedding remains separate.

### 11.8 Actual eight-panel flux, Neumann kernel and Dirichlet–Neumann bridge — PR #414

- [PR #414 — actual Jitterbug motion and finite-surface magnetic coupling](https://github.com/fabianleonaressi95/theorem/pull/414) uses the Gray/Jitterbug path and Kabsch rigid-panel frames directly. It replaces the prescribed sinusoidal angular probe with the actual panel poses.
- The source winding is a fixed-current circular filament. Its spatially varying field is computed by polygonal Biot–Savart quadrature; flux linkage is integrated over each finite receiver-coil disk. The eight-coil inductance matrix uses a single finite-core regularized Neumann Green kernel for both self and mutual entries. This replaces the inconsistent mix of thin-wire self terms and separately softened mutual terms that produced a negative eigenvalue in the first audit.
- The receiver circuit is integrated with the implicit-midpoint scheme. The audit verifies the exact discrete receiver-side energy identity, including the finite-step midpoint cross correction: electrical port input = magnetic-energy change + Joule dissipation + variable-inductance mechanical transfer. The balance residual is at floating-point roundoff.
- **Successful CI:** [actual-field / DN run](https://github.com/fabianleonaressi95/theorem/actions/runs/45360396702), with tests, model execution and JSON artifact uploaded. The latest PR head also has successful actual-field checks; see [PR #414](https://github.com/fabianleonaressi95/theorem/pull/414).
- **Measured numerical result for the declared default configuration:** 23 frames over 17.6242 s; panel-fit residual 5.02e-17 m; minimum inductance eigenvalue 2.8390e-3 H; reciprocity residual 0. However, the chosen centred 500-turn, 0.20 m primary loop at 1 A gives only 3.8510e-9 V maximum receiver emf and 3.8738e-10 A maximum current. This is a valid low-coupling result for that symmetric source placement, not evidence of useful generation. Source placement/orientation and field/mesh convergence must be studied before engineering conclusions.
- Receiver-side energy audit: port input 8.8182e-17 J, Joule loss 8.8181e-17 J, magnetic-energy change 1.2645e-21 J, variable-inductance mechanical transfer -3.9831e-24 J, relative balance residual 1.95e-16. This is not the full machine balance: primary supply, actuator dynamics and complete Maxwell force law remain open.
- **Neumann–Dirichlet connection:** the Neumann coil-coupling integral and the Dirichlet-to-Neumann map are distinct operators built from the same Laplace Green kernel G(x,y)=1/(4π|x-y|). The former is the line-current energy pairing; the latter maps scalar-potential boundary values to normal derivatives in a current-free domain. The Neumann-to-Dirichlet map is the inverse on compatible mean-zero trace spaces after fixing the additive constant. For linked current filaments, use a cut domain with circulation data or the Coulomb-gauge vector potential; a globally single-valued scalar magnetic potential is not available.
- Keep this magnetic DN map separate from the hydrodynamic traction map Lambda_eta:g -> (2 eta D(u)-pI)n on the boundary, which follows the Green–Kubo -> eta(omega) -> Stokes boundary-response chain. Shared Green-operator/boundary-response architecture is a research bridge, not an identity between magnetic coupling and viscosity.
- **Monograph crosswalk:** chapters 13–14 (Jitterbug/Vesica/RGS geometry), 20–22 (fields, transport and boundary response), with hydrodynamic Green–Kubo material retained in its existing location. This is a computational/structural connection, not a new proved physical theorem.
- **Still open:** source placement optimization; source and receiver quadrature convergence; coil leads and wiring; primary supply and actuator dynamics; Maxwell-stress generalized forces; full machine energy closure; experimental validation. PR #414 does not close issues #398–#401 or #409.
- **Still open:** source placement optimization; source and receiver quadrature convergence; coil leads and wiring; primary supply and actuator dynamics; Maxwell-stress generalized forces; full machine energy closure; experimental validation. PR #414 does not close issues #398–#401 or #409.
### 11.9 Q6 hypercube gradients, Green operators, Green–Kubo and Jitterbug Neumann–Dirichlet response

**Existing anchors (do not duplicate or rediscover):** [PR #75](https://github.com/fabianleonaressi95/theorem/pull/75), `projects/Q6-HYPERCUBE-STORA-ZUMINO-GREEN-KUBO.md`; T099–T100; T130 `theorems/T130-q6-discrete-gradients-barycentres-resistance.md`; T131 `theorems/T131-q6-phonon-phason-green-kubo-transport.md`; T132; `theorems/Q6_GREEN_KUBO_KRYSTALLO_SCALE_BRIDGE_2026-11-23.md`; `theorems/Q6_FACE_COCHAINS_HODGE_GREEN_KUBO_2026-11-23.md`; [Jitterbug PR #414](https://github.com/fabianleonaressi95/theorem/pull/414) and its Neumann–Dirichlet research note.

**The exact discrete-gradient layer.** For the Q6 graph let B1 be the oriented vertex-edge boundary matrix and d0=B1^T the vertex-to-edge gradient. Then L0=d0* d0=B1 B1^T, and the Dirichlet form is E(u)=1/2||d0u||²=1/2 u^T L0u. On mean-zero data the graph Green operator is L0†. This is the vertex-space inverse-Laplacian object; it must not be confused with the face Hodge operator Δ2|ker(B3^T), which acts on the 129-dimensional closed face-cochain sector.

**The exact Green–Kubo/resolvent layer.** Let \(H_0=\mathbf1^\perp\subset\mathbb R^{64}\). The specified reversible OU process is
\[
dX_t=-\gamma L_0X_t\,dt+\sqrt{2\gamma\sigma^2L_0}\,dW_t,\qquad X_t\in H_0.
\]
Its backward generator is \(\mathscr Lf=-\gamma\langle L_0x,\nabla f\rangle+\gamma\sigma^2\operatorname{Tr}(L_0\nabla^2f)\), with derivatives on \(H_0\). Its invariant law is \(N_{H_0}(0,\sigma^2I_{H_0})\), or covariance \(\Sigma=\sigma^2P_{H_0}\) in \(\mathbb R^{64}\), where \(P_{H_0}=I-\mathbf1\mathbf1^T/64\). For the centered linear observable \(J_b(t)=\langle b,X_t\rangle\), with \(b\in H_0\), the correlation is \(C_b(t)=\sigma^2\langle b,e^{-\gamma L_0t}b\rangle\), and
\[
\int_0^\infty C_b(t)\,dt=\frac{\sigma^2}{\gamma}\langle b,L_0^\dagger b\rangle=\frac{\sigma^2}{2\gamma}\sum_{k=1}^6\frac{\|P_kb\|^2}{k}.
\]
For arbitrary \(b\), replace it by \(P_{H_0}b\). The isotropic Q6 vertex-space mean is \(1517\sigma^2/(7560\gamma)\). Separately, the exact closed-face OU construction gives \(2263\sigma^2/(15480\gamma)\), using eigenvalues 4,6,8,10,12 with multiplicities 15,40,45,24,5. These are two different model benchmarks, not physical viscosities.

**The independent hypercube fourth-moment law.** The scalar/commuting-flux identity Δμ4=−8w⁴FQ6, FQ6=Σp(1−cos Ωp), is exact in its original finite Q6 construction. It is a static curvature/moment relation, not a Green–Kubo formula. A derivation connecting FQ6 or its metric/strain variation to the microscopic stress entering T131 is still required.

**The gradient/resistance branch.** T130 defines a local weighted least-squares shape gradient on the six incident Q6 edges and proves affine recovery when the local 2D star spans the tangent plane. It also proves symmetry and nonnegative dissipation for the declared local resistance assembly R_h=Σ_i w_i J_i^T D_i J_i. Its calibrated Q6-to-material embedding and nonlocal Stokes/BEM limit remain open. This is the geometric-gradient/Dirichlet-form side of the programme.

**The Jitterbug boundary-response branch.** PR #414 now gives actual Gray/Jitterbug panel poses, finite-surface magnetic flux, a common finite-core Neumann kernel for the inductance matrix, and a receiver-side energy audit. The Neumann coil integral is a current-current Green pairing; magnetic scalar DN/ND and hydrodynamic Stokes traction DN are separate boundary operators. Their defensible common structure with Q6 is: discrete gradient/incidence → positive Laplacian or energy form → Green/inverse operator → boundary or time-dependent response. The Q6 graph Green operator, the magnetic Neumann inductance form, and the Stokes traction DN map are not equal.

**Target constitutive diagram (partly proved, partly open):**

1. Q6 geometry → discrete gradient \(d_0=B_1^T\) → vertex Laplacian \(L_0=d_0^*d_0\) → graph Green operator \(L_0^\dagger\).
2. Q6/material Hamiltonian → variational stress \(\Pi_{ij}=-\delta H/\delta\varepsilon_{ij}\) (including gradient/hyperstress boundary terms) → equilibrium stress correlations → \(\eta_{GK}(\omega)\).
3. Jitterbug panel kinematics → Biot–Savart field and finite-surface flux → \(e_{ext},L,R\) → circuit response plus Maxwell generalized forces.
4. Continuum Stokes boundary-value problem → boundary velocity \(g\) → traction \(\Lambda_\eta g=(2\eta D(u)-pI)n\).

The consistency target η_GK ↔ η entering Λ_η must be derived from one constitutive model and a controlled limit. The missing Q6/64-TG-to-eight-panel configuration-space map is still tracked by issues #398–#401; no automatic identification of the 64-vertex hypercube with the eight Jitterbug panels is permitted.

**Monograph placement:** chapters 13–14 for Jitterbug/Vesica and configuration geometry; chapters 20–22 for gradients, Green operators, transport and boundary response. Keep the original Q6 fourth-moment theorem and T131/T132 as separate theorem records; this crosswalk is a bridge index, not a merged theorem.

**Status:** exact finite combinatorics/gradient/Dirichlet-form identities [P]; exact OU Green–Kubo inverse-spectral identities under declared reversible dynamics [P]; finite numerical implementation checks [N]; physical stress identification, material calibration, Q6–Jitterbug chain map, Green–Kubo-to-Stokes equality and full electromechanical closure [O].
**Status:** exact finite combinatorics/gradient/Dirichlet-form identities [P]; exact OU Green–Kubo inverse-spectral identities under declared reversible dynamics [P]; finite numerical implementation checks [N]; physical stress identification, material calibration, Q6–Jitterbug chain map, Green–Kubo-to-Stokes equality and full electromechanical closure [O].

### 11.10 Explicit Q6–Jitterbug quotient, strain-derived stress and conditional Stokes limit

New derivation note: research/Q6_JITTERBUG_MICROSCOPIC_STRESS_GREEN_KUBO_STOKES_2026-11-24.md.

**Exact panel incidence.** The eight Gray/Jitterbug triangular panels are indexed by sign triples \(\varepsilon\in\{\pm1\}^3\). Their reference vertices are \(2^{-1/2}(\varepsilon_1,\varepsilon_2,0)\), \(2^{-1/2}(\varepsilon_1,0,\varepsilon_3)\), \(2^{-1/2}(0,\varepsilon_2,\varepsilon_3)\). Two panels share a vertex iff their sign triples differ in one coordinate. Thus the panel-contact graph is exactly \(Q_3\), with 8 panel nodes and 12 shared-vertex contacts.

**Explicit Q6 quotient.** Write \(Q_6=Q_3^{\rm panel}\square Q_3^{\rm fibre}\), \(x=(a,b)\in\mathbb F_2^3\times\mathbb F_2^3\), and \(\pi(a,b)=((-1)^{a_1},(-1)^{a_2},(-1)^{a_3})\). This is an exact surjective 8:1 graph quotient. First-three-coordinate edges project to panel contacts; last-three-coordinate edges are collapsed inside each 8-state fibre. Each panel contact has eight horizontal Q6 edge lifts, so this is not a graph covering or edge bijection. The chain-map identity holds on the graph 1-skeleton with horizontal edges projected and fibre edges sent to zero. This does not yet give a map on Q6 squares/cubes or a geometric Q6/64-TG immersion.

**Moving frame assignment.** Attach each fibre label \(a\) to the existing Gray/Jitterbug Kabsch frame \((R_a(t),c_a(t),n_a(t))\). This is an explicit label-to-frame candidate; the within-fibre coordinates and higher-cell lift remain open. Continue issues #398 and #401; do not close them on the quotient alone.

**Microscopic stress correction.** For \(H(q,\varepsilon)=\tfrac12q^TK(\varepsilon)q\), \(K(\varepsilon)=K_0+\varepsilon_{ij}A^{ij}+\cdots\), the total stress is \(\Pi_{ij}=-\partial_{\varepsilon_{ij}}H|_0=-\tfrac12q^TA^{ij}q\). It is quadratic, not the previously used arbitrary linear OU observable \(b^TX\). Under the declared mean-zero Q6 OU process, Wick's identity gives
\[
\int_0^\infty\langle\delta\Pi_A(t)\delta\Pi_A(0)\rangle\,dt
=\frac{\sigma^4}{2\gamma}\sum_{\alpha,\beta}
\frac{|A_{\alpha\beta}|^2}{\lambda_\alpha+\lambda_\beta}.
\]
This is exact for that finite Gaussian model. Physical calibration of \(A^{ij}\), energy, volume and dynamics remains open.

**Green–Kubo/Stokes theorem status.** A conditional theorem is recorded: if the same microscopic energy/stress has equilibrium linear response, uniform Green–Kubo convergence, a Newtonian incompressible hydrodynamic limit, and convergence of boundary traction maps, then the limiting coefficient in \(\tau=2\eta D(u)\) equals the Green–Kubo coefficient and the Stokes traction DN coefficient. The proof is the identification of the same coefficient through bulk constitutive response and boundary traction. Those hypotheses are not yet established for Q6/Jitterbug; hence the unconditional physical equality remains open.

**Monograph:** chapters 13–14 (panel/phase geometry) and 20–22 (stress, Green–Kubo, transport and boundary response). No theorem number is assigned and no existing T130/T131/PR #414/#419 result is duplicated.


### 11.11 Central-force energy and stress from an embedded Q6 graph

Companion derivation: `research/Q6_CENTRAL_FORCE_STRAIN_ENERGY_2026-11-24.md`; finite-difference tests: `tests/test_q6_central_force_stress.py`.

For any explicitly supplied embedding y:V(Q6)->R^d and positive edge spring constants, the note defines one central-force energy H=1/2 sum_e kappa_e(|(I+epsilon)r_e+(Bu)_e|-ell_e)^2 and derives total stress by -partial_epsilon H. Its harmonic Hessian is the rigidity matrix form K=R^T diag(kappa_e)R, and the leading stress is linear in displacement for a stress-free reference. A matching overdamped OU benchmark is derived on the full positive subspace of K. This is distinct from the bare graph-Laplacian OU model and from the earlier generic quadratic-stress Wick ansatz.

The canonical six-dimensional hypercube embedding is retained only as an anisotropic control; it has zero off-diagonal shear coefficient and is not a 3D material model. The physical Q6/Jitterbug embedding still requires the within-fibre lift y(a,b;t), which the 8:1 panel quotient does not supply. Therefore physical shear calibration, hydrodynamic limit and eta_GK=eta_Stokes remain open. Monograph: chapters 13–14 (geometric lift) and 20–22 (stress/transport/continuum limit).


### 11.11 Central-force Q6 energy, derived Aij and microscopic stress

Derivation: `research/Q6_CENTRAL_FORCE_STRAIN_ENERGY_2026-11-24.md`; finite-difference tests: `tests/test_q6_central_force_stress.py`.

For any supplied embedding y:V(Q6)->R^d and positive edge spring constants, the note defines a central-force energy and derives exact strain-conjugate virial stress. The Hessian is K=R^T diag(kappa_e)R. Crucially, the strain derivative A^{ij}=partial_{xi_ij}K|_0 is derived explicitly, including geometric stiffness from affine prestress. The stress expansion is Pi_ij=c_ij^T u-(1/2)u^T A^{ij}u+O(|u|^3); the matching finite OU Green–Kubo tensor includes linear and quadratic stress correlations. This is distinct from the bare graph-Laplacian OU model.

The canonical Q6 subset R^6 embedding is an anisotropic control, not a 3D material. The physical Q6/Jitterbug model still requires the within-fibre lift y(a,b;t), calibrated spring constants and dynamics. The Newtonian hydrodynamic limit and unconditional eta_GK=eta_Stokes remain open. Monograph: chapters 13–14 and 20–22.


## 12. Evidence-status register: TSMR, De Aquino and the two distinct quarter factors

**Purpose.** This is a classification and dependency crosswalk, not a new theorem and not a claim that every arrow below has been proved. It preserves the existing TSMR, Anti-Twin, PSU, photon/QAT, Q-ball and transport work while distinguishing exact algebra from physical interpretation.

### 12.1 Four evidence classes

Use these labels when linking the records:

- **A — exact algebra / finite theorem:** identity proved from stated definitions, finite matrices, finite complexes or exact geometry.
- **B — conditional theorem / model theorem:** proved after explicit hypotheses, such as a specified energy, OU dynamics, invariant covariance, projection of null modes or a continuum-limit assumption.
- **C — numerical or structural correspondence:** reproducible finite computation, numerical coincidence, design correspondence or candidate map; not by itself a theorem about a physical system.
- **D — physical bridge open:** requires a derived action/energy, calibrated observable, physical dynamics, a map preserving the relevant structures, or a controlled limit.

These labels supplement rather than replace each theorem file's own status. A theorem record remains authoritative for its hypotheses and proof.

### 12.2 TSMR and the geometric one-quarter

The TSMR records are to be read together, not collapsed into a single unqualified physical law:

- **TSMR-F** (theorems/TSMR-F_multifractal_morphological_equation.md): exact definitions and the stated finite-level/multifractal identities belong to **A** where proved in that record; measure-dependent dimension and spectrum claims retain their own hypotheses and numerical/provisional labels.
- **TSMR-C** (theorems/TSMR-C_cumulative_morphodynamics.md): cumulative morphodynamic construction and its exact algebraic consequences belong to **A** only to the extent proved in the record.
- **TSMR-C-I** (theorems/TSMR-C-I_iching_golden_q6_lift.md): the Q6/I-Ching/golden lift must distinguish exact finite coding identities from nondegeneracy, cellular-lift and physical-geometry obligations; the latter remain **C/D** until the required chain maps and geometric realization are supplied.
- **TSMR-H** and **TSMR-I** retain their own model assumptions and open invariance/transfer checks; do not infer a physical constitutive law merely from an algebraic transfer relation.

The elementary identity
\[
x(1-x)=\frac14-\left(x-\frac12\right)^2\leq\frac14
\]
is **A**. Its equality case is \(x=1/2\). This is the *geometric/binary one-quarter*: it is the maximum of the concave quadratic on \([0,1]\). It is not a Wick factor and does not enter the Gaussian covariance calculation unless a separate derivation explicitly identifies the variables and observables.

### 12.3 Pentagon projection and the De Aquino threshold

The pentagonal frame identities recorded in the existing TSMR/RGS material, including
\[
EE^T=\frac52 I_2,\qquad P=\frac25E^TE,
\]
are **A** for the specified frame and normalization. Under the separately stated condition \(\|Pq\|^2=1/2\), one obtains
\[
q^TG_5q=\frac52\|Pq\|^2=\frac54.
\]
The implication to the numerical threshold \(5/4\) is therefore **A** under those definitions and that condition.

The further identification with De Aquino's parameter,
\[
\frac{m_g}{m_{i0}}=3-2\sqrt{1+\xi^2},\qquad
m_g=0\Longrightarrow\xi^2=\frac54,
\]
is algebraically **A** within that phenomenological formula. Identifying the pentagonal quadratic form with the physical \(\xi^2\), or interpreting the threshold as a measured gravitational/inertial mass effect, is **C/D**, not established by the algebra alone. The proposed calibration \(p_0=m_{i0}c\) must be stated as an additional physical assumption, not silently built into the geometric identity.

The historical relation \(\xi_k^2=(k^TQk)/4\) remains a **C** correspondence unless its normalization, domain and derivation are independently supplied. Do not use it as a proof of the pentagonal projection identity or of the De Aquino calibration.

### 12.4 The distinct Gaussian/Wick one-quarter

For a centered stationary Gaussian OU mode with
\[
\langle q(t)q(0)\rangle=\sigma^2e^{-\gamma\lambda t},
\qquad \Pi_A=-\frac12Aq^2,
\]
the centered covariance is
\[
\operatorname{Cov}(\Pi_A(t),\Pi_A(0))
=\frac{A^2\sigma^4}{2}e^{-2\gamma\lambda t},
\]
and hence
\[
\int_0^\infty\operatorname{Cov}(\Pi_A(t),\Pi_A(0))\,dt
=\frac{A^2\sigma^4}{4\gamma\lambda}.
\]
The monomode factor \(1/4\) is **B** (exact under the stated Gaussian OU model). For a symmetric matrix \(A\), with the sum over all ordered pairs \((\alpha,\beta)\),
\[
\int_0^\infty\langle\delta\Pi_A(t)\delta\Pi_A(0)\rangle\,dt
=\frac{\sigma^4}{2\gamma}
\sum_{\alpha,\beta}
\frac{|A_{\alpha\beta}|^2}{\lambda_\alpha+\lambda_\beta}.
\]
The coefficient in the full ordered-pair sum is \(1/(2\gamma)\), not \(1/(4\gamma)\). The single-mode result has \(1/(4\gamma\lambda)\) because its decay rate is \(2\gamma\lambda\). This is the *Wick/OU one-quarter*, distinct in origin and meaning from the binary maximum \(x(1-x)\leq1/4\).

For the central-force Q6 energy in research/Q6_CENTRAL_FORCE_STRAIN_ENERGY_2026-11-24.md, the stress contains both a linear term and a derived quadratic term:
\[
\Pi_{ij}=c_{ij}^Tu-\frac12u^TA^{ij}u+O(\|u\|^3).
\]
Under the overdamped OU dynamics with covariance \(k_BT K_{\mathcal H}^{-1}\), decay rates \(\mu\lambda_\alpha\), and Green--Kubo normalization \(1/(k_BTV)\), the quadratic contribution is
\[
\frac{k_BT}{2\mu V}
\sum_{\alpha,\beta}
\frac{A_{\alpha\beta}^{ij}A_{\alpha\beta}^{kl}}
{\lambda_\alpha\lambda_\beta(\lambda_\alpha+\lambda_\beta)}.
\]
This is **B**, exact for the quadratic-truncated stress in the declared finite OU model, with symmetric \(A^{ij}\), all ordered mode pairs, and the full positive subspace. The linear contribution is separately
\[
\frac{1}{\mu V}c_{ij}^TK_{\mathcal H}^{-2}c_{kl}.
\]
Do not substitute the generic quadratic-observable Wick formula for the strain-derived central-force stress, and do not drop the linear term for a stress-free central-force network.

### 12.5 Anti-Twin, PSU, photons/QAT and Q-ball: preserve the interfaces

- **Anti-Twin / T142–T143:** exact involution, rank and intertwining identities belong to **A** under the finite-dimensional definitions in the corresponding records. Their interpretation as a physical two-sheet spacetime, photon sector or Lorentz-covariant field remains **D** until metric, action, observable and dynamics are shown to be preserved.
- **PSU:** retain the source-specific expansion of the acronym and the distinct PSU state/phase spaces. A map into PSU is **A/B** only where its domain, codomain, metric or inner product, and intertwining identities are explicitly stated. Physical Planck-scale interpretation remains **D** unless independently calibrated.
- **Photons / QAT / quaternionic transport:** SU(2), quaternionic and holonomy identities in T118–T120 are algebraic/geometric results at their stated level (**A/B**). Identifying them with a physical photon propagation law, electromagnetic stress tensor or measured coupling is **D** pending a field action, Maxwell limit, conservation law and testable observable.
- **Q-ball / Q-shell:** preserve the existing stationary/coupled-action and boundary-value dossiers. A solution of a specified stationary equation is **B**; stability, parameter recovery and identification with the PSU/Anti-Twin or photon sectors require their own proofs and calibration (**C/D**).
- **Gardi:** cite the paper only as speculative paradigm/context for fractal cosmological ideas. It is not independent evidence for the central-force energy, the Q6 chain map, the De Aquino calibration, the photon/QAT coupling, Q-ball stability or a Green--Kubo/Stokes limit.

### 12.6 Q6-to-panel quotient: combinatorics is not yet a geometric chain lift

The \(8{:}1\) map from Q6 vertices to the eight Jitterbug panel labels is an exact combinatorial quotient under the specified sign-triple labelling. A graph map on vertices alone does not define a cellular chain map. For the 1-skeleton, edge orientations and multiplicities must be fixed and the boundary identity
\[
\Pi_0\partial_1=\partial_1^{\rm panel}\Pi_1
\]
must be checked on every oriented edge, including the treatment of edges collapsed within a fibre. For a higher-dimensional cellular map, the corresponding \(k\)-cell maps and
\[
\Pi_{k-1}\partial_k=\partial_k^{\rm panel}\Pi_k
\]
must also be supplied. Any edge weights used after collapse must be derived from the push-forward energy/action or explicitly declared as a new model; they cannot be chosen merely to make a desired response coefficient.

Thus: vertex quotient and enumerative panel incidence are **A/C** as specified; a full oriented weighted chain map is **B/D** until the matrices and identities are exhibited; the within-fibre coordinate lift \(y(a,b;t)\) and physical 3D embedding remain **D**.

### 12.7 Transport chain and proof obligations

Keep the following dependency sequence, but annotate every arrow by its evidence class:

\[
\text{Q6 finite complex / TSMR coding}
\xrightarrow{A/B}\text{Vesica, pentagonal frame, Anti-Twin}
\xrightarrow{A/B}\text{PSU and spinorial/QAT interfaces}
\xrightarrow{C/D}\text{photon and Q-ball physical sectors}
\xrightarrow{D}\text{calibrated deformable energy and microscopic stress}
\xrightarrow{B}\text{finite-model Green--Kubo response}
\xrightarrow{D}\text{hydrodynamic/Stokes limit}.
\]

The arrows are not transitive proof dependencies. In particular, the exact T142/T143 finite identities do not prove a photon or Q-ball constitutive law; a finite OU Green--Kubo identity does not prove a physical viscosity; and a conditional Green--Kubo/Stokes theorem does not verify its own hydrodynamic hypotheses.

**Confirmed repository state at this snapshot:** PR #428, *Complete and audit derived Q6 central-force stress tensor*, is merged. It adds the full strain-Hessian derivative \(A^{ij}\), including geometric stiffness, the linear-plus-quadratic stress expansion and finite-difference tests. The 3D Q6/Jitterbug within-fibre lift, physical calibration and hydrodynamic/Stokes limit remain open. PR #428 does not close those obligations.

**Monograph placement:** preserve the existing 27 chapter numbers. The principal cross-links are chapters 2–5 (Q6, cochains and TSMR), 12–14 (quaternions, Vesica, Anti-Twin and PSU), 23–25 (QAT, Q-ball, multifractal dynamics and Green--Kubo), and 20–22 (stress, field equations, traction and transport). This is an index update, not a new chapter or theorem number.


### 12.8 Field-theoretic Q-ball / PSU–Anti-Twin / radion reconstruction

The Q-ball programme predates this crosswalk update and must not be restarted from a generic one-field Coleman ansatz. The reconstructed prior work is recorded in [PSU–Anti-Twin Q-ball and radion reconstruction](PSU_ANTITWIN_QBALL_RADION_RECONSTRUCTION_2026-11-24.md).

That record distinguishes two repository uses of “Q-ball”: (i) the two-complex-field non-topological soliton with common global \(U(1)\) and exchange \(Z_2\), and (ii) the 32-panel football/Q-ball shell of T080/T088. T080 supplies an exact finite discrete Stokes complex; T088 supplies panel-frame seam transport, holonomy and a geometric anisotropy ansatz. Neither is itself a proof of a charged scalar soliton.

The prior PSU–Anti-Twin field model already has a shared-vierbein action, common-phase Noether charge, coupled radial equations for a sextic self-potential, and the symmetric/antisymmetric Hessian eigenvalues \(\kappa_\pm=V_{PP}\pm V_{PA}\). Its interaction \(V_{\rm int}\) was intentionally left unspecified. The previously recorded interval \(0.6614378<\omega<1\) and single-profile benchmark \((\omega,E/Q)=(0.905607329,0.988291616)\) are retained with their distinct provenance; the latter is not a coupled two-field result.

The radion coupling \(gW(R_{\rm th})\mathcal C(q_+,q_-)\) remains a phenomenological ansatz. The radion kinetic term, stabilization potential and coupling to the two scalar profiles must come from dimensional reduction of a specified action. Likewise, the common global \(U(1)\) is not automatically electromagnetic gauge symmetry or photon number.

The historical finite PSU–Anti-Twin audit recorded \(J_{\rm AT}^2=I\), a \(128\to4\times32\) spectral split and the bosonic/fermionic determinant benchmarks. The historical script derive_rgs_psu_sea.py was not present in the current default-branch tree during reconstruction; the exact source/artifact must be restored before claiming a fresh replay.

**Classification:** symmetry and Noether identities are exact/conditional within the declared two-field action; radial solutions and stability require the explicit interaction and numerical replay; radion stabilization, photon/QAT gauging and the field-theory-to-shell/Q6 discretization remain open. This branch is cross-linked to monograph chapters 12–14 (PSU/Anti-Twin and geometry) and 23–25 (QAT, Q-ball and field dynamics), while T080/T088 remain in the shell/structured-deformation chapters.


### 12.9 Correction: the two-field Q-ball interaction was already specified

The statement in §12.8 that \(V_{\rm int}\) remained unspecified is superseded by the recovered, already-merged PR #87 in the companion repository fabianleonaressi95/rgs-qlg-quaternion-bridge. The prior model fixes
\[
I=|\Phi_+|^2+|\Phi_-|^2,\quad J=|\Phi_+|^2-|\Phi_-|^2,\quad
V=m^2I-\lambda I^2+gI^3+\alpha J^2
-\kappa(\Phi_+^*\Phi_-+\Phi_-^*\Phi_+).
\]
Only the numerical/physical calibration of \(\alpha,\kappa\) remains open.

The exact in-phase exchange-symmetric branch has \(m_{\rm eff}^2=m^2-\kappa\), necessary frequency window
\[
\sqrt{m^2-\kappa-\lambda^2/(4g)}<\omega<\sqrt{m^2-\kappa},
\]
and a relative-amplitude Hessian curvature shifted by \(4\alpha F^2\). A new two-field electrostatic Maxwell BVP, including both scalar equations, Noether/electric charge, Gauss-flux audit and local even/odd amplitude curvatures, is under PR #220 in the companion repository:
https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/220
It is open and unmerged; no CI pass or full fluctuation stability is claimed. The radion reduction/stabilization, asymmetric branches and vierbein backreaction remain open.


### 12.10 Two-field Q-ball Maxwell branch and charge turning point

The symmetric two-field BVP is now implemented in the companion repository under PR #220:
https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/220

For the already specified interaction, the symmetric branch is \(f_+=f_-=F/\sqrt2\), with \(m_{\rm eff}^2=m^2-\kappa\). The implementation solves both scalar Euler–Lagrange equations and the electrostatic Maxwell equation, and audits the common Noether charge, electric charge, energy and Gauss flux. The \(q=0\) limit is tested against the existing global Q-ball with mass \(m_{\rm eff}\).

A finite six-point scan at \(m=1,\lambda=1.5,g=1,\alpha=0.2,\kappa=0.1,q=0.05,R_{\max}=20\) indicates a candidate local minimum of \(Q(\omega)\) around \(\omega\approx0.905\)–\(0.906\). This is a branch-fold diagnostic, not a stability theorem. The sign change of finite-difference \(dQ/d\omega\) must be refined and compared with the full charge-constrained scalar–phase–Maxwell fluctuation operator.

PR #220 is open and unmerged at this snapshot. Its flat-space electrostatic model does not yet include the radion action, asymmetric branches, magnetic fields or vierbein/TEGR backreaction. The radion kinetic term, stabilization and coupling must still be derived from the PSU–Anti-Twin geometric action.


### 12.11 Quantum-fractal interface: Q6, Walsh, Cantor and Fibonacci

The new research specification [Quantum–fractal interface for PRISM / Kathara–Q6](QUANTUM_FRACTAL_PRISM_Q6_INTERFACE_2026-11-24.md) reuses the existing TSMR-F multifractal record, Cantor–supergolden Phase 21, Fibonacci/golden-zeta model, Q6 Walsh spectrum and exact dyadic subdivision benchmark. It does not add a monograph chapter.

The exact Q6 Walsh spectrum and heat trace are finite-graph identities, not evidence of a fractal spectral dimension. The Cantor coding of six-bit prefixes is a labelling, not an operator equivalence: the finite group \((\mathbb Z/2)^6\) is not the profinite group \(\mathbb Z_2\), and Hamming adjacency is not the Euclidean Cantor metric. The existing cubical midpoint chain map is a control refinement, not a Kathara/Krist-All fractal rule.

The first finite-filtration result is already exact for the standard Cartesian-product Q6 Laplacian: conditional-expectation projections onto the first j bits commute with L6 for every j=0,...,6, with ranks 2^j. This is the zero-coupling baseline, not multifractal evidence. The next nontrivial test must use a provenance-identified weighted/coupled Q6 or PRISM operator. Multifractal eigenstate scaling requires a genuine hierarchy with multiple levels, IPR fits, and uniform/localized/binomial controls. Fibonacci spectra and the Sierpiński gasket are separate comparison models, not identifications with Q6.

**Classification:** Q6/Walsh identities, Cantor–Bernoulli formulas and existing dyadic chain-map identities are exact within their definitions; the Q6 filtration audit will be finite numerical evidence; PRISM/Kathara multifractal scaling and any physical quantum interpretation remain candidates/open. Gardi's Mandelbrot/IFS proposal is not a Schrödinger derivation.


## 12.12 Fibonacci multifractality and Q-PRISM preservation (24 November 2026)

The earlier 19 October RGS–PRISM Fibonacci analysis and its Q-PRISM quantum-readout proposal are preserved in [FIBONACCI_MULTIFRACTAL_QPRISM_PRESERVATION_2026-11-24.md](FIBONACCI_MULTIFRACTAL_QPRISM_PRESERVATION_2026-11-24.md). Keep this strand distinct from the exact Cantor–Bernoulli implementation in `audits/tsmr_f_multifractal.py`, the Phase-21 three-state transfer identity T056, and the standard finite Q6 Walsh calculation. The historical Fibonacci approximant family explicitly recorded is 144, 233, 377, 610, 987, 1597, with local effective exponents `tau_q^eff`; the prior verdict was that nonlinear `tau_infty(q)` is compatible with finite data but not asymptotically established, and the reported data-collapse `R^2=0.032733` is poor. The earlier concavity observation is preserved as a finite numerical result, but its raw arrays/script/fit provenance must be recovered before its detailed table is upgraded to reproducible repository evidence. Q-PRISM remains a proposed architecture (15 address qubits for L=17711; state preparation, Hamiltonian simulation and randomized-moment readout still need a gate-level specification); no quantum hardware execution or advantage is claimed. The separate Q6/Xc finite test with `concavity=False` does not refute the Fibonacci result because it uses a different object and observable.



## 12.13 Jitterbug eight-panel coil extension and geometric dependencies (24 November 2026)

Issue [#409](https://github.com/fabianleonaressi95/theorem/issues/409) is advanced by [JITTERBUG_EIGHT_PANEL_COIL_GEOMETRY_AUDIT_2026-11-24.md](JITTERBUG_EIGHT_PANEL_COIL_GEOMETRY_AUDIT_2026-11-24.md). The eight rigid triangular panels admit exact sign-triple labels \(\varepsilon\in\{\pm1\}^3\); their shared-vertex graph is \(Q_3\) (8 panels, 12 contacts, degree 3). A shared-vertex contact is not automatically a shared hinge edge. The current one-panel coil script remains the baseline; the eight-panel Kabsch frames, flux channels, mutual-inductance matrix and coupled RL dynamics are specified but not yet implemented or numerically certified.

Keep the dependency order explicit: #398 resolves Vesica/phase-to-panel incidence and panel frames; #401 addresses the dynamic 64-TG/Jitterbug immersion; #409 uses panel frames to build the eight-coil electromagnetic model; #399 derives the Ehresmann mixed-frame field law; #400 derives Cartan torsion from the full coframe and tests any proposed \(T B_\perp\) action. These are linked work packages, not a single theorem and not interchangeable evidence. The coil model does not establish torsion, hydrodynamic viscosity, generator output or energy gain.

**Monograph placement:** chapters 13–14 for Vesica/Jitterbug kinematics and panel geometry; chapters 15–17 for frame/coframe and torsion; chapters 20–22 for the separate transport/Green–Kubo/Stokes programme. The present coil audit is an engineering-model specification, not a new theorem number.


## 12.14 Exact static 64-TG/Jitterbug boundary identification (24 November 2026)

The record [64TG_JITTERBUG_EXACT_INCIDENCE_AND_DYNAMIC_BOUNDARY_2026-11-24.md](64TG_JITTERBUG_EXACT_INCIDENCE_AND_DYNAMIC_BOUNDARY_2026-11-24.md) establishes an exact scale-normalized geometric bijection between the 12 distinguished FCC/D3 points and the 12 Jitterbug joints, but **not** a cuboctahedral subcomplex isomorphism. A direct comparison of incidence lists finds 0/24 Jitterbug rods among the 240 FCC edges: the Jitterbug rod pairs have integer-coordinate squared distance 8, while the stored FCC graph edges have squared distance 2. The eight sign-triple panels and 24 rods are therefore Jitterbug linkage data on the matched point set, not inherited 64-TG cells/edges. The two chiral four-panel families are selected by the sign product; the panel shared-vertex graph is Q3, not the rod/hinge graph.

The merged Jitterbug continuation independently verifies the finite 12-joint/24-rod branch. The full 64-TG dynamic immersion remains open because no motion has yet been assigned to the other 51 FCC vertices and all 64 tetrahedral cells. Likewise, no map from Vesica/T101 phase data to Jitterbug theta/gamma follows from the point-set congruence. This distinction governs issues #398 and #401; #409 may reuse the eight Jitterbug panel frames as a separate linkage model, while #399–#400 still require a derived base/fibre geometry and full coframe.

**Monograph placement:** chapters 13–14 (Vesica/Jitterbug and geometric incidence), with the full moving-cell extension remaining a chapter 15–17 dependency rather than a new theorem claim.


## 12.15 GL(6,2)-affine Walsh-filtration mixing audit (24 November 2026)

The Q6/Walsh filtration audit was extended from stored involutions to the full affine class T(x)=Px+b, P in GL(6,2). Exact block criterion [U_T,E_j]=0 iff P[0:j,j:]=0 (500/500 verified); pure translations preserve every level; S6 gives 51 distinct profiles with only the identity fully preserving; trigram block GL(3,2)^2 gives 16 profiles with exact zeros at the j=3 trigram boundary; the EQC/Aut(Q6) generators REV and ROT supply naturally distinguished nontrivial profiles. Generic GL(6,2) mixing remains an algebraic counterexample class, not a physical operator; no coupled weighted vertex operator was identified. Report: docs/QUANTUM_FRACTAL_Q6_GL2_AFFINE_AUDIT.md; data: results/quantum_fractal_q6/gl2_affine_audit.json; tests: tests/test_q6_gl2_affine.py (7 passed). Monograph placement: chapter 2 (Q6 Fourier/Laplacian) and chapter 4 (trigrams/bit coding), as finite algebraic filtration evidence only.
### 12.15 Exact affine Q6/Walsh commutator theorem (24 November 2026)

The ordered-prefix Walsh filtration is not invariant under the full cube automorphism group. The theorem record [Q6 affine Walsh mixing theorem](Q6_AFFINE_WALSH_MIXING_THEOREM_2026-11-24.md) proves, for T(x)=Px+b, the exact commutator law in terms of r_j=dim(V_j intersect P^{-T}V_j): ||[U_T,E_j]||_F^2=2^(j+1)-2^(r_j+1), while the spectral norm is 0 iff r_j=j, otherwise 1. The translation b changes only Walsh phases and cannot cause mixing. The natural graph automorphism group is (F_2)^6 semidirect S_6, order 46,080; all 720 coordinate permutations were enumerated and yield 51 distinct commutator profiles. Coordinate swaps are genuine Q6 graph automorphisms and can break the ordered filtration, but no stored Anti-Twin/PRISM operator selects such a swap. In particular, Pi_AT and Q6_antipodal are bit-flip translations and preserve every level. This is an exact finite theorem plus exhaustive group census, not evidence of multifractal scaling or physical memory decay. Cross-links: monograph chapters 2–5 (Q6, Walsh/cubical structure) and 12–14 (Anti-Twin/RGS interface); no new chapter number.


### 12.16 Vesica–Minkowski–hexagram bridge (24 November 2026)

The research record [VESICA_MINKOWSKI_HEXAGRAM_Q6_TWO_SHEET_BRIDGE_2026-11-24.md](VESICA_MINKOWSKI_HEXAGRAM_Q6_TWO_SHEET_BRIDGE_2026-11-24.md) makes explicit that the 64 six-bit Q6 vertices can be identified with the 64 hexagrams after fixing the line-bit convention: each hexagram is an ordered pair of lower and upper three-bit trigrams. This gives the intrinsic set decomposition \(\mathbb F_2^6=\mathbb F_2^3\oplus\mathbb F_2^3\), and the (GL(3,2)\times GL(3,2)) subgroup preserves the (j=3) trigram boundary in the affine-filtration audit of PR #437.

The same record gives the exact (2+1)-dimensional Minkowski construction of two null cones whose (t=-1) sections are unit circles; their disk intersection is the Vesica Piscis. It carefully distinguishes the cone-surface intersection curve from the spatial common chord. The proposed identification of the lower/upper trigram factors with the two conic sheets is **open**: it requires explicit maps, a target metric/causal relation, incidence compatibility and equivariance. The 64-hexagram bijection does not by itself identify Q6 edges or operators with I Ching relations, nor does the (3+3) split alone produce Lorentzian geometry.

**Placement:** chapters 2–5 (Q6 and binary filtration), 12–14 (Vesica/Anti-Twin/two-sector geometry); chapters 15–17 only after a frame/coframe construction. Cross-links: T137, T142, T143 and PR #437. No new theorem number is assigned.


### 12.17 Explicit two-cone realization of the 64 hexagrams (24 November 2026)

The bridge record now includes an explicit finite map of the 64 hexagrams into the product of two sampled future-null-cone patches in Minkowski (2+1). The two unit-circle arcs are chosen as the portions of each circle lying inside the other disk; hence both sampled arcs lie on the Vesica boundary. Each hexagram maps injectively to an ordered pair of cone points, one selected by the lower trigram and one by the upper trigram. Their spatial midpoint lies in the Vesica by convexity, while the relative displacement retains the information lost by the midpoint projection. The Q6 graph incidence factors as (Q_3\square Q_3), with each edge changing one conic-sheet factor.

This is an exact finite geometric realization once the trigram-to-angle bijection is fixed. The angular assignment is a model choice; Q6 edge lengths are not automatically uniform, and (GL(3,2)\times GL(3,2)) is not automatically an isometry group of the arcs. The construction does not yet derive physical dynamics, an action, or a continuum spacetime theory. See [the detailed construction and status gates](VESICA_MINKOWSKI_HEXAGRAM_Q6_TWO_SHEET_BRIDGE_2026-11-24.md). Placement: chapters 2–5 and 12–14; later frame/torsion chapters only after a separate derivation.


The reproducible implementation and numerical checks are in [the audit script](../audits/audit_vesica_hexagram_two_cone.py) and [its JSON result](../results/json/vesica_hexagram_two_cone_audit.json). The corrected eight-point sampling covers each full 120-degree arc with angular step (2\pi/21); all 64 pairs and 192 Q6 edges pass the finite checks. The midpoint projection has 57 distinct values (eight equal-index pairs coincide), so the relative displacement is required to retain the full state.


### 12.18 Equivariant C3×C3 extension and invariant Q6 operator (24 November 2026)

The follow-up record [C3×C3 equivariant sphere/null-cone and Q6 operator](C3X_C3_EQUIVARIANT_SPHERE_NULL_CONES_Q6_OPERATOR_2026-11-24.md) resolves the planar fixed-point obstruction by embedding the eight trigram states into S²: the two fixed trigrams occupy the poles and the two three-cycles occupy equilateral triangles at latitudes z=±1/2. The map intertwines the finite-field action T(a,b,c)=(b,a+b,c) with a 120-degree rotation about the z-axis. Two copies of these sections give an injective 64-state product embedding into two 3+1D null-cone sections.

This is an enlarged 3+1D construction, **not** an equivariant realization on the earlier 2+1D Vesica arcs or a proof that all eight states lie in the old Vesica lens. The ordinary cross-sheet distance is not invariant under independent rotations; its Reynolds average is invariant but discards relative azimuthal phase.

The standard Q6 Laplacian is also not invariant under this GL(3,2) element, since T does not preserve Hamming adjacency. The research note defines instead the Reynolds-averaged product operator Lbar6=Lbar3⊗I8+I8⊗Lbar3. Its support has 256 weighted edges (versus 192 standard Q6 edges); it is positive semidefinite and C3×C3 invariant. This is a new operator on the same 64 states, not a replacement for the standard Q6 Laplacian. The finite identities and orbit counts are audited separately. Placement: chapters 2–5 (finite Q6/operator structure), 12–14 (Vesica/two-sheet geometry), and 15–17 only as a higher-dimensional null-cone extension pending a physical frame/action derivation. No new theorem number is assigned.


### 12.19 Exact spectrum of the C3×C3-invariant Q6 operator (24 November 2026)

The equivariant-operator note now records the exact rational spectrum. The factor operator has characteristic polynomial
\[
\chi_{\overline L_3}(\lambda)
=\lambda(\lambda-2)(3\lambda-8)^3(3\lambda-14)^3/729,
\]
so its eigenvalues are 0, 2, 8/3 (multiplicity 3), and 14/3 (multiplicity 3). The product operator has eigenvalues 0, 2, 8/3, 4, 14/3, 16/3, 20/3, 22/3, 28/3 with multiplicities 1, 2, 6, 1, 12, 9, 6, 18, 9 respectively. Its kernel is one-dimensional and its spectral gap is exactly 2, matching the standard Q6 gap while the remaining spectra differ. This equality of gaps is a finite operator fact, not a continuum or physical equivalence. The standard-library audit now checks the rational factor eigenvalue multiplicities by exact Gaussian elimination and builds the product spectrum. Cross-link: [equivariant sphere/null-cone and Q6 operator](C3X_C3_EQUIVARIANT_SPHERE_NULL_CONES_Q6_OPERATOR_2026-11-24.md). No new theorem number is assigned.


### 12.20 The recurring one-half: spherical geometry versus the RGS stepping block

The C3-equivariant sphere construction contains the exact axial coordinates \(z=\pm1/2\), with latitude radius \(\sqrt3/2\) and triangle side \(3/2\). The value is fixed by the chosen 120-degree orbit geometry; it is not a fitted parameter. It must be distinguished from the earlier Vesica midpoint coordinate \(1/2\) and from the RGS stepping-operator block recorded on 6 October 2026:
\[
Z_A^{BA}=\frac12D,\qquad Z_S^{BA}=-Z_A^{BA},\qquad
D=\operatorname{diag}(1,1,-1),\quad z_A=(1/2,1/2,-1/2).
\]
The original four 188D arrays have now been recovered. They reproduce this historical BA block under the explicit upper-triplet gauge \(J_B^\sharp=-J_BD\); the same \(D\) is the lower-triplet spectral involution. The block-level identification is therefore **NUMERICALLY VERIFIED**. The remaining comparison with the spherical \(C_3\) action is subject to the symmetry obstruction recorded in sections 15–16 of the [C3×C3 sphere/null-cone note](C3X_C3_EQUIVARIANT_SPHERE_NULL_CONES_Q6_OPERATOR_2026-11-24.md).


**Correction 2026-11-24:** the four original 188D arrays have now been recovered from the repository root. Their audit and deterministic carrier-basis reconstruction are in [the original-array audit](RGS_HALF_ORIGINAL_ARRAYS_AUDIT_2026-11-24.md) and [the basis reconstruction script](../audits/reconstruct_rgs_half_carrier_basis.py). The six-dimensional carrier is (K_0)-invariant and splits into (J_A) (eigenvalues 0.5, 0.6, 0.7) and (J_B) (0.8, 0.9, 1.0), paired by (Z_AJ_A=-\tfrac12J_B). The low-triplet involution is exactly (operatorname{diag}(1,1,-1)). This confirms the spectral half/sign pattern, but does not yet prove an intertwiner with the spherical (C_3\times C_3) action. The natural paired basis has BA block \(-\tfrac12I_3\) for the original \(Z_A\). The explicit upper-triplet gauge \(J_B^\sharp=-J_BD\) below converts it to the historical \(+\tfrac12D\) block, with the matching \(Z_S^{BA}=-\tfrac12D\).


**Compatibility gate:** the recovered 188D carrier also yields a conditional no-go for an intertwiner preserving the entire original RGS triple. The coupling (Z_A) forces the two triplet (C_3) actions to be diagonal (independent factor rotations fail), while the simple spectra of (K_0|_{J_A}) and (K_0|_{J_B}) rule out any nontrivial order-three orthogonal symmetry commuting with (K_0). Thus the spherical (C_3\times C_3) geometry cannot be intertwined with ((K_0,Z_A,Z_S)) as a symmetry-preserving triple without modifying the operator or weakening the intertwining requirement. Full conditional proof and commutator audit: [original-array audit, section 9](RGS_HALF_ORIGINAL_ARRAYS_AUDIT_2026-11-24.md#9-symmetry-obstruction-for-the-spherical-c3-times-c3-action).


**Resolution of the historical BA block:** the original arrays reproduce the recorded \(Z_A^{BA}=\tfrac12D\), \(Z_S^{BA}=-\tfrac12D\), \(D=\operatorname{diag}(1,1,-1)\), after the explicit upper-triplet channel gauge \(J_B^\sharp=-J_BD\). The same \(D\) is the low-triplet spectral involution. This closes the former coefficient/sign-pattern ambiguity at the \(3\times3\) block level; it does not identify the full 188D operators with their BA blocks. See [original-array audit, section 10](RGS_HALF_ORIGINAL_ARRAYS_AUDIT_2026-11-24.md#10-exact-recovery-of-the-historical-ba-half-sign-block).


### Vesica–Minkowski realization of the RGS half-sign involution

The RGS \(D=\operatorname{diag}(1,1,-1)\) is now represented geometrically as the parity operator of a reflection on three paired channels of the two \(2+1\)-dimensional null cones. The selected channels are the two endpoints and midpoint of each Vesica-facing arc. Pairing corresponding channels across the two sheets gives three ordered pairs whose midpoints all equal the Vesica center \((1/2,0)\). The ambient Lorentz reflection \((t,x,y)\mapsto(t,x,-y)\) swaps the endpoint channels and fixes the central channel; in the reflection-adapted basis its matrix is exactly \(D\). This realizes the recovered \(Z_A^{BA}=D/2\), \(Z_S^{BA}=-D/2\) after the already established upper-triplet channel gauge. It is a three-channel subrepresentation, not a map of all 64 hexagrams and not an intertwiner of the full \(K_0,Z_A,Z_S\) triple. Details and coordinate audit: [Vesica–Minkowski D-reflection representation](VESICA_MINKOWSKI_RGS_D_REFLECTION_CHANNEL_REPRESENTATION_2026-11-24.md), [audit script](../audits/audit_vesica_minkowski_D_reflection.py).


## Vesica–hexagram nine-to-three algebra quotient (24 Nov 2026)

The full 64-state moment lookup remains at results/json/vesica_hexagram_moment_compression_2026-11-24.json. A pointwise algebra on the three marked channels induces a reflection-equivariant map from the paired nine-dimensional moment space to one three-channel copy. This quotient has rank 3, kernel 61 on the 64-state input, and only 23 distinct images of the 64 basis states. It is therefore an observable/quotient, not a lossless encoding. It matches the RGS reflection involution D but does not yet intertwine K0, ZA, ZS or derive the half-scale coefficient. See research/VESICA_HEXAGRAM_9_TO_3_POINTWISE_ALGEBRA_REDUCTION_2026-11-24.md.


## Operator-derived Q6–Vesica–RGS bridge (24 Nov 2026)

The preferred RGS reduction is now the invariant symmetric one-excitation sector of the compressed Q6 Laplacian, not the earlier pointwise-product quotient. The operator-adapted trigram map uses Q3 Laplacian eigenmodes 0, 4, 6 and is antipodal-reflection equivariant. The 9D tensor sector contains a canonical 3D symmetric one-excitation subspace with reduced Laplacian diag(0,4,6) and reflection D. Its coisometry F from all 64 Q6 labels intertwines both L_Q6 and the diagonal reflection. The full nine-component table retains 64 distinct labels; the rank-three sector quotient has 27 distinct images. The RGS carrier spectra are matched by the unique quadratic interpolation f(x)=1/2+x/120+x^2/240, with upper branch f+0.3; this polynomial is a candidate matching law, not a first-principles derivation. The combined audit script reconstructs the carrier from the original arrays. See research/Q6_VESICA_RGS_SPECTRAL_INTERTWINER_2026-11-24.md.


## 13. T161 interface crosswalk to all 27 chapters — 27 November 2026

T161 is the geometric spine of the programme, not a theorem from which every chapter follows. The table below assigns each chapter its actual interface to the Q6–golden cut-and-project–rhombic triacontahedron–IVM–Lorentzian spin construction. “Programme/interface” is organizational or model-level; it is not a proof arrow.

| Ch. | Chapter domain | T161 interface | Relation and evidence boundary |
|---:|---|---|---|
| 1 | RGS–PSU–PRISM–Q6 architecture | Global carrier and integration diagram | Programme-level; common action and commuting diagram remain open |
| 2 | Boolean Q6, Walsh and Laplacian | 64 labelled cube states and antipodal complement | Exact finite combinatorics; projected point cloud is not the triacontahedron graph |
| 3 | Cubical 2-skeleton and cellular Anti-Twin | Chain incidence and antipodal action on the Q6 carrier | Exact finite chain identities; distinguish graph cycle rank from filled-complex homology |
| 4 | Trigrams, bit coding and Kathara | Coordinate/coding realization of the Q6 labels | Finite maps are record-specific; no automatic metric identification with IVM |
| 5 | Q6 cohomology and Hodge | Discrete differential forms and refinement interface | Finite Hodge results; continuum convergence remains a separate Mosco/FEEC obligation |
| 6 | SU(2), SU(3), links and gauge covariance | Gauge transport on the carrier and future spin connection | Finite gauge covariance; continuum gauge limit not supplied by T161 |
| 7 | Q6–D5 integer quotient and Wilson fibres | Parallel measure/spectral sector | Programme-level connection only; D5/Wilson–Bergman claims retain their own hypotheses |
| 8 | Wilson, marginal, Bergman and Hua | Parallel harmonic-analysis and measure sector | No geometric implication from the triacontahedron; preserve no-go and conditional results |
| 9 | Clifford, discrete Dirac and Nielsen–Ninomiya | Spinorial endpoint and refinement gate | T147 is Euclidean Spin(6); T149 is an exact gapped obstruction; Lorentzian Dirac limit open |
| 10 | Binary icosahedral group and Poincaré quotient | Icosahedral symmetry and possible spin representation input | Group/representation theory is established in its own records; no automatic Spin(6)→Spin(1,3) map |
| 11 | Rumin complex and analytic torsion | Spectral/topological companion sector | Independent theorem family; connection is through shared 2I representation data, not a T161 consequence |
| 12 | Quaternions, SU(2), SO(3), intertwiners | Spatial spin lift and double-cover conventions | Standard finite/group theory; boosts and Lorentzian lift require an extra construction |
| 13 | RGS 188D reconstruction | Candidate spatial coframe and constraint data | Dataset-specific rank/equivariance audits; physical tetrad derivation remains open |
| 14 | PSU, Anti-Twin and Lorentz symmetry | Candidate time leg from two-sheet fluid modes | Conditional on common metric and future unit-timelike four-velocities; not yet derived from fluid equations |
| 15 | PRISM product graph | Refinement and scale hierarchy | Finite graph/coding results; mesh-compatible continuum limit remains open |
| 16 | Krist-All | Symbolic dynamics and class/coding layer | Separate finite automata/provenance interface; not a metric map to the triacontahedron |
| 17 | FEEC, cubical de Rham and curved geometry | Discrete coframe, chain maps and compatible forms | Commuting finite maps do not prove curved Mosco convergence |
| 18 | Golden and supergolden refinements | \\(\\phi\\) defines the golden 6D frame; \\(\\psi\\) remains a separate scale/arithmetic branch | Golden projection is direct; supergolden/eta/zeta physical interpretation remains conditional/open |
| 19 | Mosco and geometric continuum limit | Required refinement gate from finite carrier to continuum | Open analytic obligation; no finite spectrum alone proves convergence |
| 20 | Einstein–Cartan and Weyssenhoff fluid | Independent Cartan connection with curvature and torsion | Conditional field-theory interface; spin current/action and physical source assumptions must be explicit |
| 21 | Teleparallelism and scalar–torsion actions | Flat-connection branch of the Cartan geometry | Distinct constrained branch; do not identify with generic Riemann–Cartan connection |
| 22 | QLG spinorial interface | Local \\(\\mathrm{Spin}^+(1,3)\\) module and gauge/fluid coupling | Four complex spinor components per site; lattice operator and continuum limit still open |
| 23 | QAT, topological light and cube–sphere geometry | Spatial geometry and Maxwell/coframe comparison | Model-level comparison; QAT physical claims remain separately audited hypotheses |
| 24 | Wormholes, EMS and stability | Lorentzian metric/Cartan applications | Application layer only after field equations and matter content are derived |
| 25 | Spin glass, correlators and cellular dynamics | Q6/PRISM carrier for correlations and Green–Kubo observables | Finite statistical identities; thermodynamic/material limit and calibration open |
| 26 | Synchronization, hysteresis and industrial applications | Geometric carrier for defects, phases and mechanical response | Application/benchmark interface; material constitutive laws require independent calibration |
| 27 | Unified theory and work order | Full synthesis and dependency governance | T161 organizes interfaces; it does not collapse distinct proofs into one theorem |

### Record-level audit companion

The current branch contains 289 theorem Markdown files: 284 on primary `main` plus five branch-only proposals (T146–T149 and T161). The generated register has 280 valid rows and omits four main-tree cards T157–T160. Its 410 declared dependency tokens resolve as 306 unique IDs, 101 ambiguous IDs and 3 unresolved IDs. The 306 unique declarations are now preserved in the companion graph as **unreviewed declarations**, not proof dependencies. Full details and file-path candidates are in:

- `docs/T161_RECORD_LEVEL_INTEGRATION_AUDIT_2026-11-27.md`
- `docs/T161_REGISTER_DEPENDENCY_AUDIT_2026-11-27.json`

No existing theorem has been renumbered, deleted or promoted in status.
