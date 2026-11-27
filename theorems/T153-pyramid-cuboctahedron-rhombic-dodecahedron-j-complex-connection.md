# T153 — Pyramid bisection, cuboctahedral–rhombic-dodecahedral duality, and the geometric status of the inter-sheet complex structure

**Classification:** exact elementary geometry for §§1–4; source-critical literature synthesis for §5; conditional geometric programme / open problem for §§6–8.  
**No claim:** this record does not derive a physical torsion field, identify a molecular orbital with a polyhedron, or validate the proposed 4D/ether explanations discussed in some of the sources.

## 1. A square pyramid is the union of two tetrahedra

Let \(P\subset\mathbb R^3\) be a square pyramid with square base \(ABCD\) (cyclically ordered) and apex \(S\notin\operatorname{aff}(ABCD)\). The plane
\[
\Pi=\operatorname{aff}(S,A,C)
\]
contains the apex and one diagonal of the square. It divides \(P\) into the two tetrahedra
\[
P_1=\operatorname{conv}\{S,A,B,C\},\qquad
P_2=\operatorname{conv}\{S,A,C,D\}.
\]
Their intersection is the triangular section \(\operatorname{conv}\{S,A,C\}\), and
\[
P=P_1\cup P_2,\qquad
\operatorname{int}(P_1)\cap\operatorname{int}(P_2)=\varnothing.
\]
Because the two base triangles \(ABC\) and \(ACD\) have equal area, both tetrahedra have the same altitude from \(S\) to the base plane, hence
\[
\operatorname{Vol}(P_1)=\operatorname{Vol}(P_2)
=\frac12\operatorname{Vol}(P).
\]
This holds for every square pyramid, not only a regular one. For a non-square quadrilateral base, a diagonal still splits the pyramid into two tetrahedra, but their volumes are equal only when the two base triangles have equal area.

**Terminology safeguard.** “A tetrahedron is half a pyramid” is therefore correct only with the pyramid and bisection specified: here it means one of the two tetrahedra obtained by cutting a square pyramid through its apex and a base diagonal. It is not a universal identity for an arbitrary pyramid.

## 2. Cuboctahedron: exact tetrahedron / half-octahedron decomposition

For a cuboctahedron of edge length \(a\), the standard face count is 8 equilateral triangles and 6 squares, with \(V=12\), \(E=24\), \(F=14\). Its volume is
\[
V_{\rm cuboct}=\frac{5\sqrt2}{3}a^3.
\]
The central decomposition described in the Cosmic Core source consists of eight congruent regular tetrahedra and six square-based pyramidal cavities, each a half of a regular octahedron. Equivalently, the six half-octahedra pair into three full octahedra. The volume check is exact:
\[
8\left(\frac{\sqrt2}{12}a^3\right)
+6\left(\frac{\sqrt2}{6}a^3\right)
=\frac{2\sqrt2}{3}a^3+\sqrt2a^3
=\frac{5\sqrt2}{3}a^3.
\]
Each half-octahedron is a square pyramid and therefore splits along a base diagonal into two tetrahedra by §1. This gives a further tetrahedral subdivision, but the resulting tetrahedra need not all be regular or congruent; the decomposition must retain its actual coordinates and incidence data.

The source's phrase “8 tetrahedra and 3 octahedra” is consistent with the equivalent “8 tetrahedra and 6 half-octahedra” description. This is a geometric decomposition, not evidence that the cuboctahedron is a physical energy ground state.

## 3. Cuboctahedron and rhombic dodecahedron

The rhombic dodecahedron is the polar dual of the cuboctahedron. Its combinatorial data are
\[
(V,E,F)=(14,24,12),\qquad V-E+F=14-24+12=2.
\]
Its twelve faces are rhombi; it is a space-filling parallelohedron (its translates tile Euclidean three-space). Duality exchanges the cuboctahedron's 12 vertices with the rhombic dodecahedron's 12 faces, and its 14 faces with the dual's 14 vertices; the 24 edges correspond.

A useful independent construction is the cube-plus-pyramids description: a cube decomposes into six square pyramids with common apex at its centre and bases on the six cube faces. Reattaching/assembling such pyramidal pieces on the faces of a second cube produces the rhombic-dodecahedral arrangement described by the source. The precise gluing map and scale must be specified before treating this as a cell complex or a metric construction.

**Euler / curvature extension.** For a connected closed orientable surface of genus \(g\),
\[
V-E+F=\chi=2-2g.
\]
For a polyhedral metric, the angle defect at a vertex \(v\) is
\[
K(v)=2\pi-\sum_{f\ni v}\theta_{f,v},
\]
and the discrete Gauss–Bonnet identity is
\[
\sum_v K(v)=2\pi\chi.
\]
Thus the sphere case gives \(4\pi\), while handles change the Euler characteristic and total defect. The Portuguese source's Cauchy proof establishes the sphere formula by deleting a face, triangulating the planar map, and successively removing boundary triangles; its examples correctly warn that \(V-E+F=2\) is not valid for arbitrary surfaces with handles.

## 4. Jitterbug and the extended polyhedral family

The cuboctahedron is the rectification of the cube and octahedron. The classical Jitterbug is a continuous articulated deformation of the cuboctahedral framework through special configurations, including icosahedral and octahedral symmetry limits. The Cosmic Core page describes this as a hierarchy of nested Platonic/Archimedean forms and also associates it with toroidal flow, ether, consciousness, and universal energy. Only the kinematic/geometric part is suitable for mathematical formalization without additional evidence.

The In2Infinity pages propose an “Extended Jitterbug” involving the octahedron, icosahedron, cuboctahedron, snub cube and rhombicuboctahedron. This should be treated as a proposed parametrized polyhedral sequence, not as a theorem about atomic structure. To become a mathematical result it needs:
1. explicit vertex coordinates \(X_i(t)\);
2. a declared parameter interval and endpoint identifications;
3. a list of preserved constraints (edge lengths, incidence, convexity, symmetry);
4. proof of continuity and of the claimed limiting polyhedra;
5. a distinction between an actual rigid-bar linkage path and a sequence of independently rescaled solids.

## 5. Source audit: what is usable and what is not established

### 5.1 Cosmic Core, cuboctahedron and rhombic dodecahedron

Usable geometric claims include the cuboctahedron's face/edge/vertex counts, its duality with the rhombic dodecahedron, the rhombic dodecahedron's 14,24,12 counts, its space tiling, and the cube/square-pyramid construction. These are standard polyhedral facts and are recorded here with independent mathematical statements.

The article also contains claims about aether ground states, toroidal photon flow, consciousness, noble-gas “vortices”, and cosmic cells. Those claims are not consequences of the polyhedral identities and are not adopted. The article's stated “2160°” sum for the twelve rhombic faces is not the sum of all planar face-interior angles: twelve rhombi contribute \(12\cdot360^\circ=4320^\circ\). Its earlier statement that all cuboctahedron face-interior angles are 60° is also false if read literally: triangular faces have 60° angles, while square faces have 90° angles. Any alternative angle convention would need to be explicitly defined. Symbolic numerical coincidences (for example 10,080) are not mathematical evidence.

### 5.2 In2Infinity: atomic, orbital, molecular and geo-quantum proposals

The pages make testable-sounding claims: six \(p\)-orbital lobes form an octahedral arrangement; polyhedral ratios predict atomic radii for 81 stable elements; the Extended Jitterbug explains conductivity and thermal behaviour; tetrahedral geometry unifies selected molecules in the five biogeochemical cycles; and a 4D geometric cavity explains biological nitrogen fixation.

The first item is a legitimate visualization of the three Cartesian \(p\)-orbital orientations (two lobes per orbital), but a lobe diagram is not a polyhedral model of the electron's probability density or a derivation of atomic radii. Standard quantum chemistry describes orbitals through wavefunctions and angular functions; the geometric picture must be shown to reproduce those quantitative objects, not replace them by a six-point shell.

Tetrahedral coordination is indeed relevant to methane, ammonia's electron-domain geometry, sulfate and phosphate; water has tetrahedral electron-domain geometry but a bent molecular geometry. These distinct notions must not be collapsed into the statement that all five molecules have the same tetrahedral molecular shape.

The nitrogen-fixation explanation is not supported by the cited mainstream mechanism literature. Nitrogenase catalysis requires coupled electron/proton transfer, metal clusters, and ATP hydrolysis; the FeMo cofactor and the protein components are structurally and chemically characterized. The In2Infinity 4D-cavity explanation is therefore a hypothesis requiring an explicit Hamiltonian/energy pathway and predictions against biochemical data, not an accepted resolution of nitrogen fixation.

The claimed 81-element radius superiority is not accepted as validated here: the overview page does not provide, in the material inspected, a reproducible data table, a uniform radius definition, uncertainty treatment, fitting/holdout protocol, or a statistical comparison sufficient to establish predictive superiority. No numerical performance claim is imported into this repository.

### 5.3 Frei Otto / soap films and ResearchGate figure

The supplied ResearchGate page identifies a Frei Otto image of experimental form-finding with catenaries and soap bubbles, credited to *Casabella* no. 301 (1966), and places it in Annarita Zarrillo's 2020 publication. The figure is relevant as an experimental methodology, not as evidence for a specific polyhedral or quantum model.

Soap films under fixed boundary conditions realize stationary/minimal-area surfaces (subject to stability and topology); hanging chains under gravity realize catenaries. These are distinct variational systems. The physical experiment can be used to discover candidate geometries and compare them with numerical minimizers, but its output depends on boundary conditions, surface tension, gravity, film topology and stability. It does not by itself generate a torsion tensor.

### 5.4 GeoGebra and Pinterest

The GeoGebra resource is titled “Dualidad Icosaedro-Dodecaedro” and describes an icosahedron, its dual dodecahedron, and their intersection/envelope when nested. It is a useful interactive visualization of polar duality, but its page metadata alone does not provide a proof or coordinate convention. The Pinterest URL could not be inspected in the available page response; no mathematical claim is extracted from it.

## 6. Can the certified inter-sheet \(J\) be part of a discrete connection?

On the archived six-dimensional carrier \(\mathcal W\), the prior audit certifies
\[
S^2=I,\qquad J^2=-I,\qquad SJ+JS=0.
\]
Thus \(J\) is an orthogonal-compatible candidate complex structure on the carrier and is odd with respect to the two-sheet grading. This is an exact algebraic structure on the selected carrier, but the underlying archive verification remains numerical to its stated floating-point tolerance.

A discrete connection on a graph requires fibre spaces \(\mathcal W_v\) and invertible link transports \(U_{vw}:\mathcal W_w\to\mathcal W_v\). Compatibility with a site-dependent complex structure means
\[
U_{vw}J_w=J_vU_{vw},
\qquad\text{equivalently}\qquad \nabla^U J=0.
\]
This condition makes \(J\) parallel; it does not make \(J\) torsion.

For a continuum geometric interpretation, one additionally needs a coframe \(e^a\) identifying the internal fibre with tangent directions and a connection \(\omega^a{}_b\). Only then is torsion defined by
\[
T^a=de^a+\omega^a{}_b\wedge e^b.
\]
A nonzero \(J\), or a nontrivial inter-sheet exchange, does not imply \(T^a\ne0\). The coframe, link transports, discrete torsion/defect operator, scaling, and convergence theorem must all be supplied independently.

### 6.1 Representation-theoretic obstruction that must be checked first

The existing icosahedral \(A_5\) action on the six signed axes decomposes as
\[
\mathbb R^6=V_3\oplus V_{3'},
\]
where \(V_3\) and \(V_{3'}\) are inequivalent irreducible three-dimensional representations. By Schur's lemma, an operator commuting with the same \(A_5\) action cannot be an invertible map exchanging \(V_3\) and \(V_{3'}\). Consequently, if the carrier's two sheets carry precisely these two inequivalent \(A_5\) modules, an inter-sheet \(J\) cannot be \(A_5\)-equivariant in the ordinary commuting sense.

A possible alternative is covariance under the nontrivial outer automorphism of \(A_5\), which exchanges the two 3-dimensional character types. That is a different condition:
\[
J\rho(g)J^{-1}=\rho(\alpha(g)),
\]
for a specified automorphism \(\alpha\), and must be checked on explicit generators. It must not be assumed from the existence of \(J\).

The six-axis \(A_5\) representation in T121 and the archived RGS carrier \(\mathcal W\) must not be silently identified. First construct the actual group action on \(\mathcal W\), then compute the intertwining/outer-twisted residuals. The existing T138 record also explicitly leaves the six-index \(2I^*\) action and its compatibility with the two-sheet matrix open.

## 7. A minimal, falsifiable programme

The next stage is not to label \(J\) “torsion”, but to test the following gates in order:

1. **Carrier representation:** provide explicit matrices \(\rho_{\mathcal W}(g)\) for generators of \(A_5\) or \(2I\); verify group relations and identify the two sheet characters.
2. **Equivariance:** compute \(\|[J,\rho(g)]\|\) and, separately, \(\|J\rho(g)J^{-1}-\rho(\alpha(g))\|\) for a declared outer automorphism. Do not select whichever convention gives the smaller residual after seeing the result.
3. **Discrete connection:** construct link maps \(U_{vw}\) from geometric data, not by fitting them to \(J\); test \(U_{vw}J_w-J_vU_{vw}=0\), inverse-link consistency and cycle holonomy.
4. **Coframe:** define a geometrically meaningful \(e_v\) or edge coframe and its transformation law. State how six internal carrier directions map to the tangent dimension used in the continuum model.
5. **Torsion:** define a discrete \(T_h\) from the coframe and connection (or a finite-element/DEC equivalent), and show it is nonzero for the proposed configuration.
6. **Refinement:** specify a mesh family, scaling, norms and convergence target; prove or numerically test convergence of \(T_h\) to a nonzero continuum \(T\).
7. **Variational test:** if the Jitterbug or soap-film configuration is proposed as selected by an action, write that action and derive its Euler–Lagrange/stationarity conditions. A visual resemblance is not a variational derivation.

**Current answer to the central question:** \(J\) can be used as an internal complex structure that a discrete connection is required to preserve. The available results do not show that it is part of a geometrically derived connection, and they do not show that torsion survives a continuum limit. The ordinary \(A_5\)-equivariance route may be obstructed if \(J\) exchanges the inequivalent \(3\) and \(3'\) modules; an outer-twisted covariance is a precise alternative to test. Therefore the correct status is **candidate structure / open geometric problem**, not established torsion.

## 8. Prior work retained without duplication

- T121: exact \(A_5\) signed-axis representation and \(3\oplus3'\) decomposition; it explicitly does not construct torsion or a Pin lift.
- T138: exact six-dimensional two-sheet matrix decomposition; the six-index \(2I^*\) generator action remains open.
- T143-A: conditional antipodal-equivariant \(SO(3)/SU(2)\) link connection; it does not imply a continuum limit or torsion.
- T145: numerical RGS carrier grading and off-diagonal \(Z_A\); \(K_0\) mixes the grading sectors.
- T146: dodecahedron–Q6 chain map and spectral obstruction; no dodecahedral Hodge operator producing the selected \(0,4,6\) spectrum is established.
- T152: binary McKay–ADE and crepant-resolution results; no RGS/Q6 operator identification is claimed.

## References

1. Cosmic Core, “Geometry — Platonic Solids — Part 10: Cuboctahedron & Rhombic Dodecahedron”, https://www.cosmic-core.org/free/article-49-geometry-platonic-solids-part-10-cuboctahedron-rhombic-dodecahedron/
2. João Nuno Tavares, “A Fórmula de Euler”, https://cmup.fc.up.pt/cmup/pick/Manhas/Modulo3PolidrosEuler.html
3. In2Infinity, “Geo-Molecular Chemistry”, https://in2infinity.com/theory/geo-molecular-chemistry/
4. In2Infinity, “Geo-Quantum Mechanics”, https://in2infinity.com/theory/geo-quantum-mechanics/
5. In2Infinity, “P-Orbital Geometry”, https://in2infinity.com/p-orbital-geometry/
6. In2Infinity, “Atomic Geometry”, https://in2infinity.com/theory/atomic-geometry/
7. Annarita Zarrillo, “Adaptive Dimension in Architecture: Modular and Transformable Structures as an Alternative to Traditional Building Systems” (2020), figure credited to *Casabella* no. 301 (1966), https://www.researchgate.net/figure/Frei-Otto-Experimental-models-of-research-of-the-shape-with-catenaries-and-soap_fig8_339948319
8. GeoGebra, José Manuel Arranz, “Dualidad Icosaedro-Dodecaedro”, https://www.geogebra.org/m/E8ugkfT8
9. Seefeldt, Hoffman & Dean, “Mechanism of Mo-dependent nitrogenase”, *Annual Review of Biochemistry* 78 (2009), DOI: 10.1146/annurev.biochem.78.070907.103812.
10. “Structural Enzymology of Nitrogenase Enzymes”, *Chemical Reviews* (2020), DOI: 10.1021/acs.chemrev.0c00067.
11. Colding & Minicozzi, “A Course in Minimal Surfaces”, Notices of the AMS (2019), https://math.mit.edu/documents/uploads/papers/Notices2019-41.pdf.
