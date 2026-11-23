# Document 2 — PRISM cycles, Krist-All, Kathara, and multidimensional analysis

**Prepared for discussion with Stergios Pellis**  
**Purpose:** address the request to examine the 108 distinguished cycles of length 640 and the Krist-All residual, and place these questions alongside the Kathara/Q3/Q6 chain constructions and the existing multidimensional Q6 analysis.

**Status:** source-grounded technical map of existing constructions, numerical records, and unresolved provenance. It does not claim that the 108-cycle construction or the 11,725-class Krist-All operator has been independently reproduced.

---

## 1. Why this is separate from the scalar spectrum note

Document 1 concerns the scalar Laplace spectrum of the spherical space form \(S^3/2I\). The present objects have different state spaces and operators:

- PRISM is a finite five-factor Cartesian-product graph/cell complex;
- the 108 cycles are a proposed distinguished cycle cover of its 69,120 states;
- Krist-All is a proposed finite propagation/classification operator;
- Kathara is a source-transcribed planar 12-centre/15-line configuration and its associated cellular complex;
- Q3 and Q6 are cubical complexes;
- multidimensional analysis is a structured statistical description of fields and operators on these finite spaces.

No equality or canonical map between these objects is assumed. Every transition requires an explicit incidence map, chain map, intertwiner, or operator construction.

## 2. PRISM: the ambient five-dimensional product structure

The canonical product graph currently specified in the repository is
\[
G_{\mathrm{PRISM}}=C_{64}\square C_6\square C_6\square C_6\square C_5.
\]
Its state count is
\[
N=64\cdot6^3\cdot5=69\,120.
\]
A state is indexed by a mixed-radix tuple \((g,\ell,c,t,b)\), with
\[
\operatorname{ind}(g,\ell,c,t,b)
=((((g\cdot6+\ell)\cdot6+c)\cdot6+t)\cdot5+b).
\]
The product graph has degree \(2+2+2+2+2=10\) and
\[
|E|=\frac{10N}{2}=345\,600.
\]

For the standard unweighted graph Laplacian, separation of variables gives the exact eigenvalue formula
\[
\lambda(k_1,\ldots,k_5)
=4\sum_{r=1}^{5}\sin^2\!\left(\frac{\pi k_r}{n_r}\right),
\quad (n_1,\ldots,n_5)=(64,6,6,6,5).
\]
In particular,
\[
\lambda_1=4\sin^2(\pi/64)
=0.009630546655606143,
\]
with multiplicity two. This is a theorem about the Cartesian-product graph and its combinatorial Laplacian. It does not by itself identify a physical five-dimensional spacetime.

The repository's PRISM incidence audit constructs
\[
B_1:C_1\to C_0,\qquad B_2:C_2\to C_1
\]
with shapes
\[
B_1\in\mathbb Z^{69\,120\times345\,600},\qquad
B_2\in\mathbb Z^{345\,600\times691\,200},
\]
and checks the exact identity \(B_1B_2=0\). The product-cell counts are
\[
(69\,120,\ 345\,600,\ 691\,200,\ 691\,200,\ 345\,600,\ 69\,120),
\]
and the standard product-torus Betti vector is
\[
(b_0,\ldots,b_5)=(1,5,10,10,5,1).
\]
The committed audit explicitly notes that it does not compute every higher boundary rank \(B_k\); the Betti vector is the standard product-torus result, not an output of a complete rank computation in that script.

Do not conflate this full product graph with the separately reported 1,920-state active subset, with the 64-state Q6 graph, or with a filtered operator used in another experiment.

## 3. The 108 distinguished cycles of length 640

The historical research record reports 108 disjoint cycles, each of length 640, covering the 69,120 PRISM states. The elementary count is consistent:
\[
108\cdot640=69\,120.
\]
If “disjoint” means vertex-disjoint and every state occurs exactly once, the claim is a cycle-cover (a spanning 2-factor) of the PRISM vertex set. It is not an edge decomposition of the degree-10 product graph: the 108 cycles would use 69,120 cycle-edges, whereas the full graph has 345,600 edges.

### 3.1 Constructive exact cycle cover

A deterministic cycle cover can now be constructed directly from the stated Cartesian-product graph; it does not require the missing historical generator.

First construct a Hamiltonian cycle \(H\) of \(C_{64}\square C_5\), of length 320, by the column snake
\[
(g,b)=(0,0),(0,1),\ldots,(0,4),(1,4),\ldots,(1,0),(2,0),\ldots,(63,0),
\]
where the order in each even column is \(b=0,\ldots,4\), and in each odd column is \(b=4,\ldots,0\). Since 64 is even, the final vertex \((63,0)\) is adjacent to \((0,0)\) through the cyclic \(C_{64}\) coordinate. Thus this is a simple 320-cycle.

For each fixed pair \((\ell,t)\in\mathbb Z_6^2\), partition the third coordinate into the three adjacent pairs
\[
(c_0,c_1)=(0,1),(2,3),(4,5).
\]
Take one copy of \(H\) in each of the two layers \(c=c_0,c_1\). Delete the same base edge \(h_0h_1\) in both copies and cross-connect the two resulting paths at their endpoints by the two vertical edges
\[
(h_0,\ell,c_0,t)\sim(h_0,\ell,c_1,t),\qquad
(h_1,\ell,c_0,t)\sim(h_1,\ell,c_1,t).
\]
The result is one simple cycle of length \(2\cdot320=640\).

There are \(6\cdot6\cdot3=108\) such cycles. Different choices of \((\ell,t)\) or of the disjoint \(c\)-pair have disjoint vertex sets, and every PRISM vertex belongs to exactly one choice. Every edge used is an edge of the declared Cartesian-product graph. Hence this construction proves the existence of a 108-cycle vertex-disjoint cover of all 69,120 states.

### 3.2 Reproducible certificate and provenance boundary

The implementation is [scripts/audit_prism_108_cycles.py](../../scripts/audit_prism_108_cycles.py), with regression tests in [tests/test_prism_108_cycles.py](../../tests/test_prism_108_cycles.py). Run:
```bash
python scripts/audit_prism_108_cycles.py
python -m pytest tests/test_prism_108_cycles.py -q
```

The audit checks the mixed-radix indexing, simplicity of each cycle, all 640 closing and interior edges per cycle, pairwise vertex-disjointness, and exact coverage of the complete index set \(\{0,\ldots,69\,119\}\). The optional flag `--include-cycles --output reports/prism_108_cycles_certificate.json` writes the full ordered list of 69,120 mixed-radix indices. The deterministic flattened ordering is SHA-256 fingerprinted by the script.

**Important distinction:** this is a new constructive certificate for a valid 108-cycle cover of the specified PRISM graph. It does not establish that these are the same 108 cycles in the earlier historical/Pellis computation, nor does it recover an additional geometric or operator-based selection rule implicit in the word “distinguished”. That historical identification remains open until the original cycle list, generator, or defining rule is supplied.

**Current classification:** existence of a 108-cycle, length-640 vertex-disjoint cover for the specified product graph is **proved constructively and independently audited**; identification with the historical Pellis cycle family and any extra distinguished property remain **open provenance questions**.

## 4. Krist-All: the polynomial identity and the residual

The reported Krist-All claims are:

- 11,725 equivalence classes;
- a finite operator \(K\) satisfying \(K^3=K^2+I\);
- a residual reported at approximately \(5.22\times10^{-16}\).

These three claims require a common, explicit data model. The recovered source-status report records that the available archive does not provide:

1. a formal equivalence relation on the objects being classified;
2. a canonical representative encoding;
3. the complete representative/class table or deterministic enumerator;
4. exact definitions and matrices for \(K\) and \(W_0\);
5. an independent test of the polynomial identity and the reported residual.

Thus 11,725, \(5.22\times10^{-16}\), and \(K^3=K^2+I\) are retained as historical research claims, not certified results. This is a provenance limitation, not evidence that the claims are false.

### 4.1 What follows if the polynomial identity is exact

If a specified finite-dimensional linear operator \(K\) satisfies
\[
K^3-K^2-I=0
\]
as an exact matrix identity, then its minimal polynomial divides
\[
p(x)=x^3-x^2-1.
\]
The unique real root greater than one is
\[
\psi=1.465571231876768\ldots.
\]
This algebraic consequence does not identify \(K\) with a particular \(3\times3\) transfer matrix. Such an identification would require the dimension, coefficient field, invariant factors, and an explicit basis/intertwiner.

The trigram refinement matrix
\[
M_T=\begin{pmatrix}0&0&1\\1&0&0\\0&1&1\end{pmatrix}
\]
and the earlier transfer matrix
\[
A_\psi=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix}
\]
are permutation-similar. This is an exact algebraic change of ordering of three abstract states. It is not yet a geometric derivation from PRISM cycles, Kathara cells, or Krist-All classes.

### 4.2 How the residual must be reported

The number \(5.22\times10^{-16}\) is not auditable without the actual matrix and the normalization convention. A new report must publish:

- the exact matrix \(K\), its dimensions, coefficient type, basis ordering, and SHA-256;
- the raw residual matrix \(R=K^3-K^2-I\);
- at least \(\|R\|_F\), \(\|R\|_2\), and a clearly specified normalized residual;
- the arithmetic used (exact integers/rationals/algebraic field, or floating point);
- if floating point is used, precision, scaling, condition estimates, and tolerance;
- an exact-arithmetic certificate whenever \(K\) has exact entries.

The normalization used in the historical \(5.22\times10^{-16}\) figure has not been recovered and must not be guessed. If \(K\) is supplied only as a floating-point matrix, a small residual is numerical evidence for that supplied matrix, not an exact proof of the polynomial identity.

### 4.3 The missing class enumerator

The class count needs a deterministic pipeline:
\[
\text{raw objects}\longrightarrow\text{declared equivalence relation}
\longrightarrow\text{canonical representative}
\longrightarrow\text{class table}.
\]
The output must include class-size distribution, stabilizers/orbits if a group acts, checksums, and independent re-enumeration. Without these, the number 11,725 is not independently reproducible.

## 5. Kathara: from the planar diagram to cellular algebra

The current Kathara work is more explicit than the PRISM cycle and Krist-All records. It starts from a source-transcribed diagram with 12 centres and 15 primary lines. Expanding the primary polylines gives 21 distinct elementary edges. A reflection
\[
\sigma=(3\ 4)(6\ 7)(9\ 10)
\]
fixes the central chain and exchanges the left and right branches, with a specified induced permutation on the 15 line labels.

The exact geometry is conditional on the adopted source transcription. The square-similarity reconstruction gives
\[
T=\sqrt2R_{-\pi/4}
=\begin{pmatrix}1&1\\-1&1\end{pmatrix},
\quad T^TT=2I,\quad \det T=2.
\]
This establishes the stated \(45^\circ\) rotation and \(\sqrt2\) scale rule, and the constrained centre-6/centre-9/centre-12 relation. The planar stage map has characteristic polynomial \(x^2-2x+2\), not the supergolden cubic. The square-spiral rule alone therefore does not derive \(\psi\).

### 5.1 The filled Kathara complex

With the 10 bounded planar regions declared to be 2-cells, the transcribed complex has
\[
(C_0,C_1,C_2)=(\mathbb Z^{12},\mathbb Z^{21},\mathbb Z^{10}).
\]
Its integer incidence matrices satisfy \(B_1B_2=0\). The reported exact ranks are
\[
\operatorname{rank}B_1=11,\qquad \operatorname{rank}B_2=10,
\]
so
\[
(b_0,b_1,b_2)=(1,0,0).
\]
This is the homology of a disk. The choice to fill the ten bounded regions is an explicit mathematical convention; it is not automatically a physical assertion contained in the source diagram.

### 5.2 Kathara to Q3

The target \(Q_3^{(2)}\) has 8 vertices, 12 edges, and 6 square faces, with
\[
(b_0,b_1,b_2)=(1,0,1).
\]
The existing T060 construction defines a coordinate-based map whose 12 Kathara centres collapse onto four vertices of one square face \(b_2=0\). It is a coarse chain-map candidate, not an injective or canonical identification and not a genuinely three-directional trigram map.

T061 compares the two path conventions (bit-0-first and bit-1-first). Their edge maps differ only on the specified source edge \((5,7)\); the difference is the boundary of the target square, and an explicit chain homotopy is supplied. Thus the two stated constructions induce the same homology map. This does not prove uniqueness among all possible Kathara–Q3 maps.

### 5.3 Kathara to Q6: preserve the existing \(R_0,R_1,R_2\) work

The project has already developed more than one \(R_0,R_1,R_2\) construction. They must be kept distinct rather than recomputed or silently identified:

- **T062 / Gate C:** an explicit integral chain map using root-path differences. It is injective on vertices but collapses all ten 2-cells, so \(R_2=0\). It is a valid algebraic chain map but not a non-degenerate face lift.
- **T116 / Gate D:** a non-degenerate integral chain map using shortest Q6 paths with the declared axis order \((1,2,0,3,4,5)\) and an exact square-swap filling algorithm. It checks
  \[
  B_1^{Q6}R_1=R_0B_1^K,\qquad
  B_2^{Q6}R_2=R_1B_2^K
  \]
  as integer identities and certifies \(\operatorname{rank}_{\mathbb Q}R_2=10\) by a full-rank modular certificate modulo \(1\,000\,003\).

T116 is the stronger current finite chain construction, but its axis order is a declared combinatorial convention, not an RGS-metric canonical choice. It does not yet establish a cellular embedding, equivariance under the recovered symmetry action, a unique lift to the Ellis hypersurface, or an SU(2) edge holonomy. The next geometric gate must derive—not assume—the lift and its transport rule.

## 6. Multidimensional analysis: what has been measured

The existing MQM multidimensional pipeline deliberately separates observational levels:

1. **Vertex block:** 64 Q6 vertices, with fields and local neighbourhood summaries.
2. **Edge block:** 192 Q6 edges, with endpoint means/differences, directions, and metric conductances only when supplied from the archived coframe.
3. **Cell block:** 240 Q6 square faces, to be treated through incidence, curvature/holonomy, and face observables once a geometrically derived connection is available.
4. **Global/operator block:** spectra, singular values, determinants, Hessian eigenvalues, solver residuals, and global parameters. These are not replicated over vertices.

The A13/Q6 exploratory report uses vertex features
\[
(\phi,\tau,d,\overline\phi_{N(g)},\sigma_{\phi,N(g)},
(L_{Q6}\phi)_g,V(\phi_g),\rho_{\mathrm{Dirichlet},g}),
\]
where the metric Dirichlet density is included only when the 192 positive conductances are supplied from the archived coframe. Since Q6 is 6-regular, \(d=6\) is a structural check, not a varying explanatory feature.

For the archived finite field, the report gives:
- \(\operatorname{corr}(\phi,\tau)=0.9269817\);
- standardized SVD-PCA variance ratios approximately
  \[
  (0.8823156,\ 0.1088181,\ 0.0079745,\ 0.0008533,\ 0.0000385);
  \]
- the first two components explain approximately \(99.1134\%\) of the variance in that particular feature table.

These are descriptive finite-model statistics, not independent samples or causal evidence. The 64 vertex rows are spatially coupled. The high \(\phi\)-\(\tau\) association is model-conditioned because \(\tau\) enters the determinant coupling; the quartic-potential feature is also nearly redundant with \(\phi\) on the narrow observed range. No p-values, causal interpretation, physical-unit calibration, predictive validation, or continuum refinement follow from this PCA.

### 6.1 The multidimensional programme for PRISM/Kathara

For Pellis's questions, the analysis should be expanded without treating the 69,120 PRISM states as independent identically distributed observations. The appropriate data model is block-structured:

- five PRISM factor coordinates \((G,L,C,T,B)\);
- vertex, edge, square, and higher-cell incidence blocks;
- the 108 cycle labels, once the cycle cover is recovered;
- Kathara centre, edge, primary-line, and face labels;
- local fields/coframes/connections and global operator data.

The main analyses should be:

1. **Factor-resolved graph Fourier analysis:** use the exact product Laplacian eigenbasis and retain the five factor frequencies separately.
2. **Cycle-resolved observables:** after the 108-cycle generator is recovered, compute per-cycle spectra, winding numbers, field means/variances, inter-cycle correlations, and cross-cycle coupling. Compare these with the full product graph, not only with a selected subset.
3. **Incidence-aware multiblock analysis:** vertex/edge/face variables must be linked by \(B_1,B_2\); do not flatten them into one table without preserving their different units and dependencies.
4. **Symmetry-orbit reduction:** compute orbit averages and irreducible-sector projections only under groups proven to preserve the actual labelled complex and operator.
5. **Operator analysis:** compare singular values, spectral projectors, and residuals of explicitly defined \(R_0,R_1,R_2\), \(K\), and Hodge/Laplacian operators. Basis changes must be handled covariantly.
6. **Robustness:** vary parameters, initial conditions, and admissible cycle/path conventions; report uncertainty and sensitivity. Parameter-sweep configurations, vertices, and cycles are different observational units and must not be pooled as independent samples.

This is the sense in which “multidimensional analysis” should be used here: a joint geometric, combinatorial, spectral, and statistical analysis with explicit incidence structure—not simply a high-dimensional PCA plot.

## 7. Work plan for the next Pellis exchange

The next technical exchange should be staged in this order:

1. **Recover and certify the 108 cycles:** obtain the original generator or complete cycle list, freeze the PRISM indexing and graph version, and run the vertex-cover/edge-adjacency checks.
2. **Recover Krist-All inputs:** obtain the exact \(K\), \(W_0\), class equivalence relation, canonical representative encoding, and original residual normalization. Recompute the residual in exact arithmetic if possible.
3. **Connect the existing \(R_0,R_1,R_2\) maps:** compare T062 and T116 as different chain constructions; do not overwrite earlier results. Test equivariance only after the target group action on Q6 cells is explicitly supplied.
4. **Build the cycle/Kathara bridge:** specify an incidence-preserving map or intertwiner from Kathara cells to the PRISM/Q6 cycle data. The current records do not provide this map.
5. **Run the multidimensional analysis:** preserve the five PRISM factors, the cellular chain levels, the cycle partition, and the global operator block.
6. **Only then test a Krist-All/trigram relation:** derive the three-channel operator from the geometry and compare it with \(M_T\) or \(A_\psi\); do not insert either matrix by hand.

## 8. Evidence ledger

| Object or claim | Current status |
|---|---|
| PRISM product graph, 69,120 vertices, degree 10, 345,600 edges | Exact combinatorial construction |
| Product-graph Laplacian spectrum and gap | Exact formula; gap numerically evaluated |
| PRISM \(B_1B_2=0\) | Exact integer audit |
| Product-torus Betti vector | Standard topological result; higher boundary ranks not all computed by the PRISM script |
| A 108-cycle cover of length 640 | Constructively proved for the specified product graph; independent audit and regression tests added. Historical Pellis cycle-family identity remains unverified |
| 11,725 Krist-All classes | Historical report; equivalence relation and enumerator missing |
| Krist-All \(K^3=K^2+I\), residual \(5.22\times10^{-16}\) | Historical numerical claim; exact \(K\), \(W_0\), and normalization missing |
| Kathara 12-centre/15-line transcription | Source-conditioned finite combinatorics |
| Filled Kathara complex, \(b=(1,0,0)\) | Exact finite result conditional on the declared face filling |
| Kathara–Q3 T060/T061 | Coordinate-defined chain map and explicit chain homotopy; noncanonical |
| Kathara–Q6 T062 | Exact but degenerate chain map |
| Kathara–Q6 T116 | Non-degenerate exact integral chain map for declared path convention; not RGS-canonical |
| A13/Q6 PCA and correlations | Exploratory finite-data analysis; spatial dependence and model conditioning retained |
| PRISM/Kathara/Krist-All unified geometric operator | Open; requires explicit chain/intertwiner construction |

## 9. Repository sources and reproduction entry points

Central repository:
- theorems/T057-kathara-square-similarity-center-overlay.md
- theorems/T058-kathara-15-line-planar-face-audit.md
- theorems/T059-kathara-cellular-chain-hodge-audit.md
- theorems/T060-kathara-q3-chain-map.md
- theorems/T061-kathara-q3-chain-homotopy.md
- theorems/T062-kathara-q6-integral-chain-map.md
- theorems/T116-nondegenerate-kathara-q6-integral-chain-map.md
- theorems/MQM-multidimensional-structure.md
- reports/KRISTALL_RECOVERY_STATUS.md
- reports/prism_69120_audit.json
- scripts/audit_prism_69120.py
- scripts/audit_prism_108_cycles.py
- tests/test_prism_108_cycles.py

Companion bridge repository:
- docs/KATHARA_Q6_NONDEGENERATE_GATE_D.md
- docs/KATHARA_RGS_CANONICAL_SELECTION_AUDIT.md
- docs/TRIGRAM_KRISTALL_SUPERGOLDEN_CROSSWALK.md
- src/kathara_q6_nondegenerate_chain_map.py
- tests/test_kathara_q6_nondegenerate_chain_map.py

PRISM audit:
~~~
python scripts/audit_prism_69120.py --no-save-incidence
~~~

Kathara non-degenerate Q6 chain-map test (run in the companion bridge repository):
~~~
PYTHONPATH=. python -m pytest tests/test_kathara_q6_nondegenerate_chain_map.py -q
~~~

A13 multidimensional archived-data analysis:
~~~
python audits/morphodynamics/mqm_multidimensional_a13.py \
  --bundle A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip \
  --field-report audits/morphodynamics/mqm_a13_local_backreaction.json \
  --output audits/morphodynamics/mqm_multidimensional_a13_summary.json
~~~

**Final scope statement:** this note gives Pellis a coherent route into the PRISM/Kathara/multidimensional programme while preserving the central distinction between exact finite constructions, reported numerical results, and missing source data. The 108-cycle cover is now constructively certified for the declared PRISM graph; its identity with the historical Pellis family remains unverified. The Krist-All class count, operator identity, and residual remain historical claims pending the missing definitions and source data.
