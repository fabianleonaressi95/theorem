# Law catalogue — established results and RGS–PSU–Q6 claims

**Purpose.** This document is the dependency map for the RGS–PSU–PRISM–Q6 programme. The objective is not to decorate a model with famous equations, but to identify which established laws constrain it, which original identities have actually been derived, and what remains to be proved for the proposed structure to follow.

**Epistemic labels**
- **E — Established:** standard theorem or experimentally established physical framework, with primary/review source.
- **D — Derived here:** follows mathematically from explicitly stated definitions and hypotheses.
- **N — Numerically audited:** computed for a specified finite dataset or implementation; not a theorem unless accompanied by a proof.
- **C — Conjectural bridge:** a proposed identification between frameworks.
- **O — Open:** required derivation or validation not yet supplied.

## 1. Established mathematical laws to use as constraints

### M1. Clifford relations [E]
For Euclidean generators,
\[
\{\Gamma_\mu,\Gamma_\nu\}=2\delta_{\mu\nu}I.
\]
They determine the local algebraic structure of a Dirac symbol. They do not by themselves define a derivative, a spin structure, or a continuum limit on a finite graph.

**RGS/Q6 use:** T015 supplies an explicit six-generator representation on \(\mathbb C^8\). The representation is exact; the choice of graph difference operator is an independent modelling decision.

### M2. Lie-group gauge covariance [E]
For a local gauge group G and link variables,
\[
U_{vw}\mapsto g_vU_{vw}g_w^{-1},\qquad
\psi(v)\mapsto g_v\psi(v),
\]
a covariant edge transport transforms at its endpoint. This is the algebraic foundation of lattice gauge theory.

**RGS/Q6 use:** T013 proves color-singlet invariance of the epsilon contraction; T014 proves covariance of the specified link-coupled graph operator. Neither result supplies a Yang–Mills action or a QCD path integral.

### M3. Yang–Mills curvature and action [E]
For a connection A,
\[
F=dA+A\wedge A,\qquad
S_{YM}=\frac{1}{2g^2}\int \mathrm{tr}(F\wedge *F).
\]
The Bianchi identity is \(D_AF=0\). In a lattice formulation, parallel transport around a plaquette is the holonomy; the Wilson plaquette action is a gauge-invariant discretization.

**RGS/Q6 use:** a list of 240 Q6 plaquettes is only combinatorial data. To claim a gauge theory, assign SU(3) links, define oriented plaquette holonomies, choose an action/measure, and derive its gauge variation and continuum scaling.

### M4. Noether's theorem and gauge constraints [E]
Continuous symmetries of an action yield conserved currents; local gauge symmetry entails constraints (Gauss law in Hamiltonian form). The graph model must distinguish global flavor symmetry from local color gauge redundancy.

**RGS/Q6 use:** color SU(3)_C acts at vertices; flavor SU(3)_F acts on (u,d,s) labels. They are not interchangeable. A baryon is a color singlet while its octet/decuplet labels belong to flavor-spin representation theory.

### M5. Representation theory of SU(3) and permutation symmetry [E]
For three fundamental flavor triplets,
\[
3\otimes3\otimes3=10_S\oplus8_M\oplus8_M\oplus1_A.
\]
The two octet copies carry mixed permutation symmetry; the decuplet is fully symmetric in flavor. The full baryon wavefunction must also satisfy fermionic antisymmetry, including color, spin, flavor, and spatial parts.

**RGS/Q6 use:** T012 records the octet/decuplet decomposition. T013 provides color-singlet interpolator templates. A Q6 implementation must build the spin-flavor projectors explicitly; a dimension count alone does not construct the physical baryon spectrum.

### M6. Hodge theory and discrete cohomology [E]
For a finite oriented cell complex with boundary maps \(\partial_k\), the chain condition is \(\partial_k\partial_{k+1}=0\); Betti numbers are ranks of homology groups. With inner products, the Hodge Laplacian is
\[
\Delta_k=\partial_{k+1}\partial_{k+1}^{*}+\partial_k^{*}\partial_k.
\]
Its kernel represents cohomology for a finite Hilbert complex.

**RGS/PRISM use:** claimed Betti numbers and Hodge spectra must be recomputed from the actual boundary matrices and rank certificates. Graph cycle rank is not automatically the same as higher-dimensional cell-complex homology.

### M7. Spectral graph theory [E]
For a finite graph, adjacency and Laplacian spectra encode combinatorial information. For the hypercube Q6, adjacency eigenvalues are \(6-2m\) with multiplicity \(\binom6m\), and Laplacian eigenvalues are \(2m\) with the same multiplicity.

**RGS/Q6 use:** these are exact checks on the 64-vertex, 192-edge graph. They do not identify the graph Laplacian with a physical Dirac or Yang–Mills operator without additional construction.

### M8. Nielsen–Ninomiya obstruction [E]
Under the theorem's hypotheses (including locality, translation invariance, suitable regularity and exact chiral symmetry for a conventional lattice fermion operator), chiral fermions cannot be represented as an isolated unpaired species: species doubling or relaxation of a hypothesis is required.

**RGS/Q6 use:** T015's finite Q6 spectrum is not a bypass. Q6 is a \(\mathbb Z_2^6\) graph, not a periodic discretization of \(\mathbb R^6\) with a standard Brillouin torus and continuum scaling. Any chiral claim must state exactly which Nielsen–Ninomiya hypothesis is absent or modified.

### M9. Cartan's formula and Liouville theorem [E]
For a vector field X and differential form α,
\[
\mathcal L_X\alpha=d(i_X\alpha)+i_X(d\alpha).
\]
A Hamiltonian flow preserves a symplectic form ω and hence its Liouville volume \(\omega^n/n!\). In para-Kähler geometry the corresponding statement requires the full para-Kähler hypotheses, not merely an involution.

**RGS/PSU use:** T011 is valid under its stated para-Kähler assumptions. Whether the PSU phase-space construction satisfies those assumptions remains open.

### M10. Equivalence of formulations requires a map [E]
A discrete model and a continuum field theory are not equivalent merely because they share a symmetry or a similar spectrum. One needs a specified sequence of spaces/operators/actions and a convergence theorem (e.g. resolvent, Mosco, or correlation-function convergence, depending on the claim).

**RGS/PRISM use:** this is the governing standard for the proposed PRISM-to-Laplace–Beltrami–Yang–Mills passage.

## 2. Original results currently recorded in this programme

These are not all at the same epistemic level. Each must remain attached to its definitions, input files, and reproducible audit.

| ID | Result | Status | What it establishes / does not establish |
|---|---|---|---|
| T002 | Type-IV D5 Bergman density formula \(\det g=10^5/N^5\) | D, conditional on domain/metric convention | Exact complex-geometric density; no Wilson marginal identity |
| T003 | Atomic finite push-forward cannot equal a nonzero absolutely continuous density | D | Exact finite equality obstruction; weak convergence remains possible |
| T004 | Weighted Riemann samples of \(N^{-5}\) converge to truncated Bergman measure | D, under refinement assumptions | Geometric quadrature convergence, not a Wilson derivation |
| T005–T007 | Wilson Bessel/Fourier–Haar marginal and gauge averaging | D for specified finite setup | No hard Hua cutoff at finite coupling |
| T008 | Weak-convergence criterion via mesh, cell-mass error, and tail | D, conditional | A criterion; Q6 application still needs estimates |
| T009 | \(\mathrm{rank}(CPC^T)=\mathrm{rank}(C)-\mathrm{rank}(RC)\) for the specified orthogonal projection | D, subject to stated matrix dimensions/projection definition | If ranks 129 and 124 are independently certified, effective rank is 5; Q6 input matrices still require verification |
| T011 | Para-Kähler Hamiltonian flow preserves Liouville volume | D under para-Kähler hypotheses | Does not prove PSU realizes those hypotheses |
| T012 | SU(3)_F baryon octet/decuplet decomposition | E/D representation-theoretic derivation | Does not give Q6 masses or confinement |
| T013 | Local epsilon color-singlet baryon operator; Wilson-line dressing | D | Gauge invariance, not baryon dynamics |
| T014 | Link-coupled graph operator transforms covariantly | D | Gauge covariance, not a complete fermion action |
| T015 | Explicit Cl(6) representation and spectrum of the defined forward operator on Q6 | D | Exact finite spectrum; not a continuum Dirac spectrum |

### Recorded RGS/PRISM numerical claims requiring provenance bundles [N]
The programme has reported the following finite computations: PRISM graph \(C_{64}\square C_6^3\square C_5\) with 69,120 vertices and degree 10; 108 fundamental cycles of length 640; Hodge Betti claims \(b_1=5,b_2=10\); spectral gap approximately 0.009630546656; Krist-All residual approximately \(5.22\times10^{-16}\); and 188-dimensional tangent/Hessian audits with specified near-zero and negative modes.

These are **numerical/finite-structure claims**, not universal laws. Before they support a theorem, the repository must carry: exact input-generation code, matrix conventions, rank tolerances, machine-readable outputs, independent recomputation, and stability checks under precision/tolerance changes. In particular, a small residual verifies an equation numerically, not the physical interpretation assigned to it.

## 3. The dependency chain we must actually prove

The intended architecture is:

1. **Combinatorial substrate:** define Q6, PRISM, cells, orientations, incidence maps and automorphism groups.
2. **Geometric structure:** define metric, coframe/vierbein, connection, torsion and curvature on that substrate.
3. **Gauge structure:** assign SU(3)_C links, plaquette holonomies, gauge action, gauge transformations and Gauss constraints.
4. **Fermions:** define a Dirac operator with a declared spin module, adjoint properties, chirality operator and fermion action.
5. **Matter representations:** construct color-singlet three-quark operators and project flavor-spin sectors into octet/decuplet.
6. **Dynamics:** define the transfer matrix/path integral and compute gauge-invariant correlators.
7. **Continuum/physical claims:** prove a scaling/convergence result and compare dimensionless observables with QCD/GR/known physics.

Each arrow is a separate theorem or controlled numerical test. No later layer can be inferred from an earlier layer by terminology alone.

## 4. Required proof obligations and falsification tests

| Layer | Required proof/test | Failure condition |
|---|---|---|
| Cell complex | \(\partial^2=0\), exact ranks, homology certificates | Inconsistent incidence matrices or unstable ranks |
| Metric/coframe | nondegeneracy, signature, transformation law | Degenerate metric or wrong signature |
| Connection | transformation law, curvature/torsion identities, Bianchi | Violated identities beyond numerical error |
| Gauge theory | exact local invariance of action and measure | Gauge variation nonzero |
| Fermions | adjoint/\(\gamma_5\)-adjoint identities, free spectrum, doubling analysis | Uncontrolled extra zeros or wrong symmetry |
| Baryons | color singlet, Pauli symmetry, correlator covariance | Non-singlet contamination or wrong exchange symmetry |
| Dynamics | positive transfer matrix/reflection positivity where required | Negative-norm states or no controlled evolution |
| Continuum | convergence of operators/correlators and universality tests | No scaling window or persistent regulator dependence |

## 5. Primary references for the established layer

1. C. N. Yang and R. L. Mills, “Conservation of Isotopic Spin and Isotopic Gauge Invariance,” *Phys. Rev.* 96 (1954), 191. DOI: https://doi.org/10.1103/PhysRev.96.191
2. K. G. Wilson, “Confinement of quarks,” *Phys. Rev. D* 10 (1974), 2445. DOI: https://doi.org/10.1103/PhysRevD.10.2445
3. J. Kogut and L. Susskind, “Hamiltonian formulation of Wilson's lattice gauge theories,” *Phys. Rev. D* 11 (1975), 395. DOI: https://doi.org/10.1103/PhysRevD.11.395
4. J. B. Kogut, “An introduction to lattice gauge theory and spin systems,” *Rev. Mod. Phys.* 51 (1979), 659. DOI: https://doi.org/10.1103/RevModPhys.51.659
5. K. Osterwalder and E. Seiler, “Gauge field theories on a lattice,” *Ann. Phys.* 110 (1978), 440. DOI: https://doi.org/10.1016/0003-4916(78)90039-8
6. H. B. Nielsen and M. Ninomiya, “A no-go theorem for regularizing chiral fermions,” *Phys. Lett. B* 105 (1981), 219. DOI: https://doi.org/10.1016/0370-2693(81)91026-1
7. C. Gattringer and C. B. Lang, *Quantum Chromodynamics on the Lattice*, Springer (2010).

## 6. Immediate work order

Do not add another speculative physical layer yet. First create a reproducible **law-to-model verification suite**:
- exact Q6 incidence/adjacency/Clifford tests;
- SU(3) random-gauge covariance test for T013/T014;
- explicit adjoint and chirality tests for candidate fermion operators;
- independent reconstruction of the Q6/PRISM homology and spectral claims;
- machine-readable JSON report with residuals, tolerances, seeds, and code commit.

Only claims that pass these tests should be promoted from N to D. A physical interpretation requires the additional continuum/dynamical proof obligations above.
