# Integrating XCont's Emergent-Dynamics Work into RGS–PRISM

**Document type:** comparative research and implementation plan  
**External author:** Serhii Herasymov (`xcontcom`)  
**Primary portfolio:** https://xcont.com/  
**Status:** research integration proposal; no collaboration, endorsement, or mathematical equivalence is implied.

## 1. Purpose and scope

This note identifies mathematically testable interfaces between the public projects presented by XCont and the RGS–PSU–PRISM–Q6 programme. The goal is not to absorb visual demonstrations as physical evidence. It is to translate selected computational ideas into explicit finite-state models, operators, invariants, and reproducible tests on the PRISM/Q6 structures.

The external repositories are independent works. Their authorship and provenance must remain visible. The MIT licences stated by the relevant repositories permit reuse subject to their licence terms; this note does not copy their source code. Any later code port must retain the original copyright and licence notices and must be separately audited.

## 2. External projects and their actual computational content

| XCont project | Publicly described method | RGS–PRISM interface | Initial status |
|---|---|---|---|
| [Evolving Cellular Automata](https://github.com/xcontcom/evolving-cellular-automata) | Genetic search over binary Moore-neighbourhood CA rules (512-bit rule tables), toroidal grids, fitness evaluation, selection, crossover and mutation | Evolve local update rules on a finite PRISM product graph; replace the 8-neighbour Moore stencil by the ten oriented nearest-neighbour slots of the degree-10 graph | X1–X3 implemented: deterministic engine and rule-search GA |
| [Initial-State Evolution](https://github.com/xcontcom/initial-state-evolution) | Rule fixed to Conway's Life; genetic search over initial fields; two fields interact across a toroidal combined grid and are scored by their effect on one another | Evolve initial configurations on PRISM/Q6 while keeping the transition operator fixed; compare single-population and paired/co-evolutionary objectives | X4 single-population fixed-rule search implemented; paired co-evolution pending |
| [Billiard Fractals](https://github.com/xcontcom/billiard-fractals) | Symbolic coding of billiard trajectories, irrational steps/modular thresholds and nonlinear discretizations | Compare irrational-rotation codings and rational periodic approximants with cycle factors, Q6 bit strings and symbolic paths on PRISM | Mathematical comparison; no equivalence asserted |
| [Fractogenesis: CA vs Conv](https://github.com/xcontcom/fractogenesis) | Iterated local CA rules and convolution kernels, in 2D and 3D, including genetic optimization of kernels | Compare Boolean local maps with graph filters/polynomials in the PRISM adjacency or Laplacian; study scaling and spectral response | Candidate operator study |
| [Perfect Shuffle Fractals](https://github.com/xcontcom/perfect-shuffle) | Recursive deterministic permutations of spatial arrays | Test recursive permutations as explicit bijections of finite Q6/PRISM state arrays; audit cycle structure and invariant subspaces | Exploratory |
| [NeuroParticles](https://github.com/xcontcom/neuroparticles) | Grid-based interacting agents controlled by neural networks and evolutionary search | Possible later comparison with interacting particle systems on a graph; not part of the first implementation | Deferred |

The descriptions above summarize the public project pages and repository documentation. They are not independent validation of every claim made in those repositories.

## 3. First integration: cellular automata on the PRISM graph

The deterministic base engine is in [models/prism_cellular_automata.py](../models/prism_cellular_automata.py), with tests in [tests/test_prism_cellular_automata.py](../tests/test_prism_cellular_automata.py). It implements the five-cycle product graph, the fixed ten-neighbour ordering, the 2048-bit local truth table, synchronous updates, elementary zero/one/identity/negation controls, trajectory generation, density/activity and graph Dirichlet observables.

The first genetic-search layer is now implemented in [models/prism_ca_evolution.py](../models/prism_ca_evolution.py), with tests in [tests/test_prism_ca_evolution.py](../tests/test_prism_ca_evolution.py) and a reproducible CLI in [scripts/run_prism_ca_evolution.py](../scripts/run_prism_ca_evolution.py). The code is independent and does not copy XCont source code.

Two optimization problems are intentionally separated:

1. **Rule search:** a genome is a 2048-bit truth table. A fixed bank of initial fields is shared by every candidate, so fitness comparisons use common initial conditions.
2. **Initial-state search:** a genome is a binary field on a fixed graph. One local rule is held fixed throughout the search.

Both paths use seeded initialization, tournament selection, elitism, uniform crossover and bit-flip mutation. The current default population and mutation settings are prototype settings, not a reproduction of XCont's numerical settings. XCont's documented 2D CA project uses a 512-bit Moore-neighbourhood rule and reports a population of 200; the PRISM model has a different neighbourhood and hence a different genotype dimension.

The implemented fitness is a transparent finite-horizon diagnostic:
\[
J=w_a\,\bar a-w_\rho|\bar\rho-\rho_*|-w_\partial\,\bar e_\partial,
\]
where \(\bar a\) is mean temporal activity, \(\bar\rho\) is mean density, and \(\bar e_\partial\) is the mean fraction of cut graph edges. All components are logged separately. This is an optimization objective selected for controlled experiments; it is not a validated measure of complexity, emergence, physical relevance, or computational universality.

### PRISM automorphism audit

The evolutionary module now includes \`rule_symmetry_report\`. It checks the local truth table against the product-graph automorphism subgroup generated by independent cycle reflections and permutations of equal-length factors. For the base factors \((64,6,6,6,5)\), this subgroup has order
\[
2^5\,3!=192.
\]
A rule is counted as invariant under a transformation only if its output agrees on every one of the 2048 local input configurations after the corresponding oriented-neighbour permutation. The CLI records the exact invariant count and fraction for the best evolved rule (or the fixed rule in initial-state search).

This is a finite exact combinatorial audit of the specified subgroup, not a proof that a rule is physically isotropic, nor a complete classification of all possible continuum symmetries. In particular, the three equal \(C_6\) factors may be permuted, while the \(C_{64}\) and \(C_5\) factors cannot be exchanged with them.

The separate two-field co-evolution mechanism described in XCont's initial-state project is **not** yet implemented: the current initial-state search has one evolving population under one fixed rule. Billiard coding and graph-convolution experiments are also pending.

### Reproducible smoke runs

The default CLI graph is deliberately small, \(C_3^{\square 5}\), so the first experiments are computationally manageable. These commands write a complete JSON record:

    python -m pytest tests/test_prism_cellular_automata.py tests/test_prism_ca_evolution.py -q
    python -m scripts.run_prism_ca_evolution --mode rules --population 8 --generations 3 --steps 6 --seed 2026 --output prism_rule_search.json
    python -m scripts.run_prism_ca_evolution --mode initial --fixed-rule 0 --population 8 --generations 3 --steps 6 --seed 2026 --output prism_initial_search.json

The JSON record includes the graph factors, search and fitness settings, time horizon, seed, evaluation history, and (for rule search) the initial-condition bank seed and SHA-256 hashes. The last command uses the all-zero rule only as an interface smoke test; it is not a meaningful dynamical benchmark. For scientific experiments, select and record a nontrivial fixed rule, graph factors, objective weights, initial-state bank, seed and time horizon. Increasing to the full 69,120-vertex PRISM graph should be deferred until profiling and vectorized/local-neighbourhood optimization have been performed.

### 3.1 Fixed graph

Use the existing finite product graph
\[
G_{m PRISM}=C_{64}\square C_6\square C_6\square C_6\square C_5,
\qquad |V|=69120,\qquad \deg(G)=10.
\]
At refinement level \(r\), use
\[
G_r=C_{64r}\square C_{6r}^{\square 3}\square C_{5r},
\qquad |V_r|=69120r^5.
\]
The first computational prototype should use small test graphs or a reduced quotient before attempting a full population search on 69,120 vertices.

### 3.2 Local rule convention

Fix an explicit ordering of the ten neighbours:
\[
(v-e_1,v+e_1,\ldots,v-e_5,v+e_5).
\]
For binary states \(x_v(t)\in\{0,1\}\), define
\[
x_v(t+1)=F_\theta\bigl(x_v(t),x_{v-e_1}(t),x_{v+e_1}(t),\ldots,
x_{v-e_5}(t),x_{v+e_5}(t)\bigr).
\]
A completely general deterministic Boolean rule has \(2^{11}=2048\) output bits, because the local input contains the central state and ten oriented neighbour states. This is not the 512-bit Moore rule used in the external 2D project: the neighbourhood and rule-space dimension differ.

The ordering is part of the model. Unless the rule is constrained to be invariant under coordinate reflections/permutations, it can distinguish directions and break graph automorphisms. A symmetry-restricted rule family should therefore be a separate experiment, not silently assumed.

### 3.3 Evolutionary search

A candidate genome is the 2048-bit truth table \(\theta\), or a compressed/symmetry-restricted encoding declared explicitly. The search loop may use:
- a seeded initial population;
- deterministic evaluation for each genome and initial field;
- elitist selection;
- explicitly defined crossover;
- bit-flip mutation with recorded probability and count;
- immutable experiment configuration and saved random seeds.

The initial XCont-style genetic algorithm is an optimization heuristic. It does not prove that a global optimum has been found, that an evolved rule is unique, or that the resulting patterns are physically realized.

### 3.4 Fitness must be an explicit functional

For a trajectory \(x(0),\ldots,x(T)\), candidate diagnostics include:
\[
\rho_t=\frac1{|V|}\sum_v x_v(t),qquad
a_t=\frac1{|V|}\sum_v |x_v(t+1)-x_v(t)|,
\]
\[
\mathcal{E}_G(t)=x(t)^\top L_Gx(t)
=\sum_{\{v,w\}\in E}(x_v(t)-x_w(t))^2.
\]
Here \(\rho_t\) is density, \(a_t\) is temporal activity, and \(\mathcal{E}_G\) is the graph Dirichlet energy. Other measurable targets may include period, recurrence, component counts, correlation functions, and the distribution of activity across the five coordinate directions.

A fitness objective must state its target and normalization. For example, maximizing activity alone can select noisy or unstable rules; maximizing low Dirichlet energy alone can select constant configurations. Multi-objective or constrained fitness should report all component scores rather than hide them in one opaque scalar.

### 3.5 Separate rule evolution from initial-state evolution

Two experiments must remain distinct:
1. **Rule search:** vary \(\theta\), hold the initial-state distribution and graph fixed.
2. **Initial-state search:** hold \(\theta\) fixed, evolve \(x(0)\).

A third, paired experiment may use two fields \(A,B\) whose fitnesses depend on each other's measured response, inspired by the co-evolutionary project. The coupling map and boundary identification must be stated explicitly. The external project's two-field toroidal construction is not automatically identical to the PRISM graph or to the PSU biverse.

## 4. Second integration: symbolic billiards and irrational discretization

The relevant mathematical object is a coding of a dynamical system, not the appearance of a fractal image.

A basic calibration is the irrational circle rotation
\[
T_\alpha(x)=x+\alpha\pmod 1,\qquad \alpha
\notin\mathbb{Q},
\]
with a declared partition, for example
\[
s_n(x)=\mathbf{1}_{[0,1-\alpha)}(T_\alpha^n x).
\]
This produces a binary symbolic sequence. Rational approximants \(p_k/q_k\to\alpha\) give periodic comparison sequences. The programme should compare:
- symbolic word frequencies and complexity;
- return times and periodic approximants;
- finite-cycle discretizations \(C_n\);
- projections or coordinate codings on Q6 and PRISM;
- dependence on the partition boundary and initial phase.

This provides a controlled bridge to the user's Q6 binary-state language and to PRISM cycle factors. It does **not** show that a particular irrational coding is a physical trajectory, that its visual rendering is a geometric fractal in a metric sense, or that it yields a continuum spacetime.

For genuine billiards, the phase space, collision map, boundary conditions, invariant measure, and symbolic partition must be specified. Rectangular billiards, polygonal billiards and billiards on curved surfaces are different dynamical systems and should not be conflated.

## 5. Third integration: CA versus convolution as graph operators

A convolutional update on a graph can be written as
\[
u^{t+1}=\sigma(K_\vartheta u^t),
\]
where \(K_\vartheta\) is an explicitly defined graph filter, such as a polynomial in adjacency or Laplacian:
\[
K_\vartheta=\sum_{j=0}^{m}c_j L_G^j.
\]
A Boolean CA update is instead a local nonlinear map on a finite neighbourhood. These systems can be compared through:
- support/radius of dependence;
- symmetries and equivariance under graph automorphisms;
- linearization around fixed points where defined;
- spectral response of \(K_\vartheta\);
- stability, periodic orbits and attractors;
- continuum scaling under a specified refinement.

A convolution kernel is not automatically a cellular automaton, and a graph filter is not automatically a discretization of a physical field equation. Any claimed continuum operator must be derived by a consistency and compactness argument.

## 6. Relationship to the current RGS–PRISM/Mosco programme

The cellular-automaton layer is a finite-state dynamical system on a graph. The Mosco dossier concerns convergence of quadratic Dirichlet forms on varying spaces. These are related but distinct mathematical objects.

A legitimate bridge could be developed by studying the graph Laplacian energy (\mathcal{E}_G), its refinement scaling, and suitable observables of CA trajectories. To infer a continuum evolution, one would need a specified rescaling, tightness/compactness of trajectories or measures, identification of a limiting generator, and a convergence theorem. The Fourier-mode consistency of the flat PRISM refinement is only a calibration; it does not supply these dynamical convergence results.

Likewise, graph Dirichlet energy is a scalar diagnostic. It is not the RGS Hodge energy, a Yang–Mills action, or a torsion invariant unless a separate construction proves that identification.

## 7. Reproducible experiment protocol

Every experiment should save:
1. graph definition, vertex ordering and adjacency convention;
2. rule encoding and complete truth table or genome hash;
3. initial state(s), random seed and generator;
4. population size, selection, crossover and mutation settings;
5. time horizon, boundary conditions and all fitness definitions;
6. raw fitness components and best/median/worst population statistics;
7. trajectory summaries, recurrence checks and failure cases;
8. software version, command line and machine-readable JSON output.

Required controls:
- constant-zero and constant-one rules;
- identity and negation rules;
- random rules with matched density;
- random initial states with matched density;
- fixed rule versus evolved rule;
- fixed initial state versus evolved initial state;
- multiple independent random seeds;
- graph-size/refinement comparisons;
- symmetry-preserving versus symmetry-breaking rule classes.

Do not report only the best run. Report distributions over seeds and preserve negative or null results.

## 8. Work packages

| ID | Work package | Deliverable | Acceptance criterion |
|---|---|---|---|
| X1 | PRISM CA definition | Formal update convention and 2048-bit rule encoder | Implemented; test execution pending |
| X2 | Small-graph CA engine | Deterministic simulator with trajectory and observables | Implemented; test execution pending |
| X3 | Evolutionary rule search | Seeded GA, fixed initial-state bank, JSON-ready history | Implemented; test execution pending |
| X4 | Initial-state evolution | Seeded GA with one fixed rule and binary-field genomes | Implemented; test execution pending |
| X5 | Co-evolution | Explicit two-field coupling and two populations | Not implemented |

| X6 | Billiard coding | Irrational rotation and rational approximants | Exact symbolic tests and frequency convergence |
| X7 | Graph convolution comparison | Polynomial graph filters and CA comparison | Spectral and locality audits |
| X8 | Refinement study | Compare dynamics over (G_r) | Scaling hypotheses stated and tested; no automatic continuum claim |

## 9. Attribution and source links

The following are independent external projects by Serhii Herasymov:
- [XCont portfolio](https://xcont.com/)
- [Evolving Cellular Automata](https://github.com/xcontcom/evolving-cellular-automata)
- [Initial-State Evolution](https://github.com/xcontcom/initial-state-evolution)
- [Billiard Fractals](https://github.com/xcontcom/billiard-fractals)
- [Fractogenesis: CA vs Conv](https://github.com/xcontcom/fractogenesis)
- [Perfect Shuffle Fractals](https://github.com/xcontcom/perfect-shuffle)
- [NeuroParticles](https://github.com/xcontcom/neuroparticles)

The external repositories identify their respective licences; the cited CA and fractal projects declare MIT licensing. Any code reuse must comply with the licence file in the exact source repository and retain required copyright/permission notices. This integration note is a comparative research plan, not a claim of authorship, collaboration, endorsement, or transfer of ownership.

## 10. Evidence ledger

| Statement | Status |
|---|---|
| XCont portfolio describes the listed projects | Source-documented |
| Evolving CA uses genetic search over a 512-bit binary Moore rule table | Source-documented for that 2D implementation |
| Initial-state project evolves fields under a fixed Game of Life rule and couples two fields | Source-documented |
| Billiard Fractals uses symbolic billiard coding and irrational/modular discretization | Source-documented at project-description level |
| A PRISM degree-10 local binary CA has 2048 input configurations | Exact combinatorial consequence of the stated 11-bit local input |
| Evolved PRISM rules generate interesting patterns | To be tested |
| Any evolved pattern has physical significance | Not established |
| Irrational symbolic codings provide a rigorous bridge to Q6/PRISM | Open; requires explicit maps and proofs |
| CA/convolution refinement converges to a continuum field equation | Open |
| These systems derive RGS, PSU, Yang–Mills, gravity or quantum matter | Not established |

## 11. Immediate next step

X1–X4 have now been implemented as independent deterministic modules. The local-rule automorphism audit is also implemented and its exact finite-group checks are covered by regression tests. A dedicated [GitHub Actions workflow](../.github/workflows/prism-ca.yml) runs their regression tests on relevant pushes and pull requests. The immediate next step is to inspect the first CI result and archive a baseline run with its seed, graph size, fitness weights and JSON output. After that, add graph-automorphism diagnostics and only then implement X5, the genuinely coupled two-field co-evolution. This order isolates errors in the graph dynamics and objective from stochastic search effects.
