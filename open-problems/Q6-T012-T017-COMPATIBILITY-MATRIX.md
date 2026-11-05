# Q6 compatibility matrix — T012–T017

**Purpose.** This note fixes the interfaces between the baryon, gauge-covariance, finite-graph Dirac, Nielsen–Ninomiya, and cubical-refinement results. It prevents the symbol (Q_6) from being silently reused for inequivalent refinement families.

**Repository baseline.** T012, T013, T014, T015, T016, and T017 are separate theorem notes. T017 is merged through PR #13; T016 is merged through PR #12. This matrix does not alter their theorem statements.

## 1. Canonical objects and notation

| Symbol | Definition | Status / role |
|---|---|---|
| (Q_6) | Cayley graph of (mathbb Z_2^6), equivalently the six-dimensional hypercube ((C_2)^{\square 6}) | Base finite graph: 64 vertices, 192 undirected edges, degree 6 |
| (T_i) | Translation (T_i f(x)=f(x+e_i)) on (mathbb Z_2^6) | Involution: (T_i^2=T_i^{-1}=I) |
| (chi_k) | Character (chi_k(x)=(-1)^{k\cdot x}), (k\in\mathbb Z_2^6) | 64-element Fourier basis of the finite group |
| (Q_{6,n}^{\mathrm{cyc}}) | ((C_{2n})^{\square 6}), with (n\geq1) and (Q_{6,1}=Q_6) by the convention in T017 | Six-dimensional periodic cubical refinement; not a 3+1-dimensional model |
| (D_+) | (sum_{i=1}^6\Gamma_i(T_i-I)) on the base graph | Forward graph-Clifford operator of T015/T016 |
| (D_n^{\mathrm{naive}}) | (sum_i\Gamma_i(T_i-T_i^{-1})/(2h_n)) on (Q_{6,n}^{\mathrm{cyc}}), (h_n=1/n) | Centered naive Dirac operator of T017 |
| (D_n^W) | (D_n^{\mathrm{naive}}+W_n I_8), (W_n=(r/h_n)\sum_i(1-\cos p_i)) | Free Wilson symbol of T017 |

**Do not conflate the following.**

1. (Q_6=(C_2)^{\square6}) is the finite six-bit base graph.
2. (Q_{6,n}^{\mathrm{cyc}}=(C_{2n})^{\square6}) is T017's refinement family.
3. ((\mathbb Z/2^{n+1}\mathbb Z)^6), if introduced in a separate project, is a different toroidal family with side length (2^{n+1}). It is not the definition in T017 and must receive a distinct symbol, for example (Q_{6,n}^{\mathrm{pow2}}), together with its own operators and limiting conventions.

No graph isomorphism between the latter two families is asserted. In particular, equal vertex counts at selected parameter values would not establish compatibility of translations, adjacency, cell structure, or refinement maps.

## 2. Theorem interface matrix

| Theorem | Domain / degrees of freedom | Main operator or structure | Exact result | What it does **not** establish |
|---|---|---|---|---|
| **T012** | (V=\mathbb C^3), fundamental flavor representation of (SU(3)_F) | Tensor product (V^{\otimes3}), Young symmetry, spin-flavor selection | (3\otimes3\otimes3=10_S\oplus8_M\oplus8_M\oplus1_A); ground-state (56=(10,4)\oplus(8,2)) under stated (L=0)/Pauli assumptions | No Q6 Dirac operator, color dynamics, confinement, or derivation of baryon masses |
| **T013** | Finite oriented graph (G=(V,E)); quark color vectors (q_f(v)\in\mathbb C^3); links (U_{vw}\in SU(3)_C) | Local gauge action and epsilon contraction (\epsilon_{abc}q^a q^b q^c); Wilson-line dressing for separated fields | Local color-singlet invariance under the stated (SU(3)_C) transformation; graph realization remains a construction proposal | No fermion kinetic operator with controlled continuum limit, no spectrum or QCD mass prediction |
| **T014** | Finite graph with spin-color fields (\psi(v)\in\mathbb C^4\otimes\mathbb C^3) and unitary edge links | Link-covariant graph difference (D_U) | Conditional exact covariance (D_{U^g}(g\psi)=gD_U\psi), assuming the stated link law and gauge-independent spin coefficients | Gauge covariance alone gives neither Hermiticity nor anti-Hermiticity, gamma-five Hermiticity, absence of doublers, or continuum QCD |
| **T015** | Base (Q_6=\mathbb Z_2^6), spin dimension 8; optional independent color multiplicity 3 | (D_+=\sum_i\Gamma_i(T_i-I)) | Exact finite character spectrum (D_+(k)^2=4|k|I_8); only (k=0) is a zero character; centered difference on base (Q_6) is identically zero | No continuous Brillouin zone, continuum chirality count, or physical absence of doublers |
| **T016** | Same base (Q_6), plus the hypotheses of the Nielsen–Ninomiya theorem in its lattice setting | Topological chirality balance; finite (D_+) audit | No-go theorem reconstructed at the stated scope; finite Q6 identities do not constitute an evasion | No proof that the Q6 graph satisfies the continuum/lattice hypotheses; no chiral-regulator construction |
| **T017** | Sequence (Q_{6,n}^{\mathrm{cyc}}=(C_{2n})^{\square6}), spin dimension 8 | Centered naive symbol (D_n^{\mathrm{naive}}(p)), then free Wilson symbol (D_n^W(p)) | 64 naive zero corners; binomial orientation sum zero; fixed-physical-momentum symbol limit with (O(h_n^2\sum_i|k_i|^3)) bound; Wilson term lifts the 63 non-origin corners | No full resolvent/eigenvector convergence, gauge-covariant Wilson coupling, reflection positivity, interacting limit, or 3+1-dimensional derivation |

## 3. Operator conventions: keep separate

### 3.1 Base-graph forward operator (T015/T016)

For (x\in\mathbb Z_2^6),
\[
T_i^2=I,\qquad
\frac{T_i-T_i^{-1}}2=0.
\]
With Hermitian Euclidean Clifford generators satisfying
\[
\{\Gamma_i,\Gamma_j\}=2\delta_{ij}I_8,
\]
T015 defines
\[
D_+=\sum_{i=1}^6\Gamma_i(T_i-I).
\]
On the character indexed by (k\in\mathbb Z_2^6),
\[
D_+(k)=-2\sum_{i:k_i=1}\Gamma_i,
\qquad D_+(k)^2=4|k|I_8.
\]
This is a finite-dimensional forward-difference construction. Its zero-sector count must not be substituted for the corner count of T017.

### 3.2 Centered refinement operator (T017)

For (Q_{6,n}^{\mathrm{cyc}}), (h_n=1/n), and Fourier momentum (p\in(\pi/n)\mathbb Z^6/(2\pi\mathbb Z)^6),
\[
D_n^{\mathrm{naive}}(p)
=\frac{i}{h_n}\sum_{j=1}^6\Gamma_j\sin p_j.
\]
Its zeros satisfy (p_j\in\{0,\pi\}) for every coordinate: 64 corners. Their orientation signs are ((-1)^{|\epsilon|}), hence
\[
\sum_{\epsilon\in\{0,1\}^6}(-1)^{|\epsilon|}
=(1-1)^6=0.
\]
For fixed physical (k\in\pi\mathbb Z^6), the symbol tends to (i\Gamma\cdot k) with the stated sine-remainder estimate. This is a fixed-momentum symbol result, not a theorem of full spectral or resolvent convergence.

### 3.3 Wilson term (T017)

\[
W_n(p)=\frac r{h_n}\sum_j(1-\cos p_j),\qquad r>0.
\]
At a corner labelled by (\epsilon\in\{0,1\}^6),
\[
W_n(p^{(\epsilon)})=\frac{2r}{h_n}|\epsilon|.
\]
Thus the origin remains massless and the other 63 corners receive positive Wilson masses. The scalar term breaks the naive chirality anticommutation away from the origin. This is the conventional Wilson mechanism, not a Nielsen–Ninomiya evasion.

## 4. Compatibility rules for future work

1. **T012 → T013:** use T012 only to specify flavor multiplets and permutation symmetry. Use T013 for color-singlet gauge invariance. Keep (SU(3)_F) and (SU(3)_C) as distinct group actions.
2. **T013 → T014:** the link variables in T013 can be used in a fermion operator only after specifying edge orientation, reverse-link convention, spin matrices, and the Hilbert-space inner product. Gauge covariance is inherited only if every transported term transforms covariantly.
3. **T014 → T015:** T015's free (D_+) is a particular ungauged operator on the base graph. Do not identify it with the schematic (D_U) of T014 without fixing matching spin dimension and coefficient conventions. T014 uses a four-component spin factor in its setup; T015 uses an eight-dimensional irreducible complex spin representation of (Cl_6).
4. **T015 → T016:** T016's (D_+) audit is the same forward operator convention as T015. Its finite spectrum is not a Weyl-node count.
5. **T015/T016 → T017:** T017 changes both the graph family (from the single base graph to a periodic refinement) and the derivative (forward to centered). The operators have different symbols and zero sets. T017's (n=1) centered operator is identically zero; T015/T016's (D_+) has only the trivial character as a zero sector.
6. **T017 → gauge theory:** a gauge-covariant refinement requires link variables on every oriented refined edge, a precise reverse-edge law, a covariant centered difference, a compatible Wilson Laplacian, and proofs of gauge covariance and the relevant adjoint/(\gamma_*)-Hermiticity identities. The free Wilson symbol does not supply these automatically.
7. **Flavor/color baryon spectroscopy:** a later baryon correlator must combine the T012 flavor/spin projectors, T013 color-singlet contractions, and a fully specified gauge-covariant fermion operator. It must then define the action, measure, correlator, and extraction procedure. No mass claim follows from the current graph identities alone.

## 5. Verification and acceptance checklist

- [x] Base (Q_6) identified as (\mathbb Z_2^6) / ((C_2)^{\square6}).
- [x] T017 refinement identified as ((C_{2n})^{\square6}), not a power-of-two torus.
- [x] Forward (D_+) and centered (D_n^{\mathrm{naive}}) kept distinct.
- [x] T016's no-go scope separated from finite graph spectral statements.
- [x] Flavor (SU(3)_F) separated from color (SU(3)_C).
- [ ] Define a single gauge-covariant Dirac/Wilson operator on every (Q_{6,n}^{\mathrm{cyc}}).
- [ ] Prove its adjoint convention and (\gamma_*)-Hermiticity (or state precisely which symmetry is intentionally broken).
- [ ] Establish full low-energy spectral/resolvent convergence, not only pointwise symbol convergence.
- [ ] Construct and test a separate (3+1)-dimensional reduction if that is the intended physical target.
- [ ] Build baryon correlators from the combined flavor, color, and fermion structures; do not infer masses from representation dimensions.

## 6. Evidence labels

- **PROVED:** algebraic statements proved from the definitions in T012–T017, with each theorem's assumptions retained.
- **VERIFIED_NUMERICALLY:** only checks actually executed by the corresponding scripts/tests; a script's existence is not evidence that it has been run.
- **CONDITIONAL:** graph gauge covariance under the link transformation law and coefficient assumptions in T014.
- **OPEN:** gauge-covariant refinement, full spectral convergence, interacting continuum limit, physical (3+1)-dimensional interpretation, and QCD spectroscopy.

## 7. Source theorem notes

- [T012 — SU(3) baryon octet and decuplet](../theorems/T012-su3-baryon-octet-decuplet.md)
- [T013 — Gauge-invariant baryon operators](../theorems/T013-q6-gauge-invariant-baryon-operators.md)
- [T014 — Graph Dirac operator and SU(3) gauge covariance](../theorems/T014-q6-graph-dirac-gauge-covariance.md)
- [T015 — Clifford algebra and exact free spectrum](../theorems/T015-q6-clifford-free-spectrum.md)
- [T016 — Nielsen–Ninomiya and Q6 audit](../theorems/T016-nielsen-ninomiya-q6-audit.md)
- [T017 — Cubical refinement and Dirac doubling audit](../theorems/T017-q6-dirac-refinement.md)
