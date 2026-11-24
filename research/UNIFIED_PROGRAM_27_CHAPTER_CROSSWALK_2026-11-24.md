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

**2. Boolean cube Q6: graph, Fourier and Laplacian.** Connect 64 binary states/I Ching hexagrams, 192 edges, degree 6, 240 square faces, Walsh characters, Laplacian, heat kernel and spectral zeta. Anchors: T015–T020, T069, T071, T108; docs/Q6_COMBINATORIAL_HODGE_LAPLACIANS.md; docs/Q6_HYPERCUBE_GREEN_KUBO_SUPERGOLDEN.md; theorems/Q6_GREEN_KUBO_KRYSTALLO_SCALE_BRIDGE_2026-11-23.md. For the standard graph cube, eigenvalues are 2k with multiplicities binomial(6,k), k=0,...,6, so K_Q6(t)=Tr(exp(-tL))=(1+exp(-2t))^6 and Z_Q6(s)=sum_{k=1}^6 binomial(6,k)(2k)^(-s). These are exact for the standard combinatorial vertex Laplacian, not the face Hodge Laplacian.

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
