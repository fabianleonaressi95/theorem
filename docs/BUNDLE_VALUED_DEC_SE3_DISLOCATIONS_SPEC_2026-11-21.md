# Bundle-Valued DEC, discrete defects, Bianchi identities, and dislocation cohomology

**Status:** mathematical specification / research programme. No theorem claim is made until the hypotheses and proofs below are discharged.

**Scope:** oriented finite 3-dimensional cell complexes with an (SE(3))-valued discrete connection. The C60 surface audit is a 2-dimensional test case for rotational holonomy; it cannot by itself test 3-cell Bianchi identities.

## 1. Conventions and cellular data

Let (K) be a finite oriented regular cell complex of dimension at most three. Write (K_p) for its oriented (p)-cells and (C_p(K;mathbb Z)) for cellular chains. Reversing a cell orientation changes its chain sign.

At each vertex (v), choose a copy (F_v\cong\mathbb R^3) of Euclidean affine space. For each oriented edge (e=(v,w)), assign
[
G_{vw}=(R_{vw},t_{vw})\in SE(3),\qquad
G_{wv}=G_{vw}^{-1}=(R_{vw}^{T},-R_{vw}^{T}t_{vw}).
]
The multiplication convention is
[
(R_2,t_2)(R_1,t_1)=(R_2R_1,t_2+R_2t_1).
]
Thus (G_{vw}) maps coordinates in the fibre at (v) to coordinates in the fibre at (w). All products below are ordered by path traversal: the first traversed edge acts first and appears rightmost.

A change of local frames (h_v\in SE(3)) acts by
[
G_{vw}\longmapsto G'_{vw}=h_wG_{vw}h_v^{-1}.
]
This is the required discrete gauge covariance. Any proposed observable must be invariant or transform in a declared representation under this action.

## 2. Bundle-valued cochains and covariant coboundary

Let (V) be a representation space of (SE(3)), with representation \(\rho\). A vertex 0-cochain is (u=(u_v)), (u_v\in V_v). Define
[
(d_Au)_{vw}=\rho(G_{vw})u_v-u_w.
]
This convention compares the transported value at (w) with the value already expressed at (w). It is covariant under simultaneous transformation of (G) and the local components of (u).

For higher-degree cochains, choose for each cell \(\sigma\) a reference fibre and transport each oriented boundary contribution to that fibre along declared paths. Then define
[
(d_A c)(\sigma)=\sum_{\tau\prec\sigma}[\sigma:\tau]\,
P_{\sigma\leftarrow\tau}c(\tau),
]
where \([\sigma:\tau]\) is the incidence number and \(P_{\sigma\leftarrow\tau}\) is the ordered edge transport along the chosen comparison path. The paths and reference fibres are part of the data; different choices are related by holonomy and must not be silently identified.

**Important qualification.** For a non-flat connection, this operator is generally not a differential: \(d_A^2\ne0\). Ordinary twisted cellular cohomology \(H^p(K;\mathcal V_A)\) is defined in this form only when the coefficient system is flat (or when a separately specified chain/cochain complex with square-zero differential is supplied). For a curved connection use the term *curved covariant cochain operator* and do not write its kernel/image quotient as cohomology without proving it is well-defined.

## 3. Face holonomy: rotational and translational defects

For an oriented face \(f\) with boundary path \(e_1,\ldots,e_m\), define
[
H_f=G_{e_m}\cdots G_{e_1}=(R_f,b_f)\in SE(3).
]
The pair is the face holonomy based at the chosen initial vertex. Under a change of frame at that base vertex, \(H_f\mapsto h_vH_fh_v^{-1}\). Its components therefore have different transformation laws; \(b_f\) is not a gauge-invariant vector by itself.

Define the rotational defect by
[
\Omega_f=\operatorname{Log}(R_f)\in\mathfrak{so}(3),
]
on a declared logarithm branch (or use the conjugacy class / rotation angle when the logarithm is ambiguous). Define the translational closure defect by
[
\alpha_f=b_f\in\mathbb R^3
]
in the face-base frame. It transforms under the rotational and translational part of the base-frame change according to the adjoint action. A Burgers vector interpretation requires a material frame and a kinematic convention identifying this affine closure failure with a lattice circuit closure failure.

For an (SE(3)) product, the translation is not a plain sum:
[
(R_m,t_m)\cdots(R_1,t_1)
=\left(R_m\cdots R_1,
 t_m+R_m t_{m-1}+\cdots+R_m\cdots R_2t_1\right).
]
This ordered expression is mandatory in implementation.

## 4. Relation to Cartan torsion and deWit/Nye dislocation density

In the continuum Cartan description, let \(e\) be a coframe and \(\omega\) an \(SO(3)\) connection. With the stated convention,
[
T=D_\omega e=de+\omega\wedge e,\qquad
R=d\omega+\omega\wedge\omega.
]
The Cartan–Bianchi identities are
[
D_\omega R=0,\qquad D_\omega T=R\wedge e.
]

In continuum dislocation theory, a common convention defines the Nye/dislocation density tensor from the curl of plastic distortion,
[
\alpha=\operatorname{Curl}\beta^p,
\]
with index placement and sign depending on the adopted Curl convention. A relation between this tensor and Cartan torsion is not automatic: it requires a declared identification of the plastic distortion/coframe, the material frame, and the index/dualization conventions. This document treats that identification as a derivation target, not an established identity.

A discrete coframe may be represented by edge data \(E_{vw}\in\mathbb R^3\) in a chosen endpoint frame. One possible covariant face closure is
[
\mathcal T_f=\sum_{e\subset\partial f}[f:e]\,
P_{f\leftarrow e}E_e.
]
This is a candidate discrete torsion/closure 2-cochain. The edge-frame convention and transports must be specified so that \(\mathcal T_f\) transforms covariantly. It must not be identified with \(b_f\) unless the edge transports and coframe are constructed from the same discrete Cartan data and the equivalence is proved.

## 5. Discrete Bianchi identities: two distinct levels

### 5.1 Exact lattice-gauge identity for curvature

For a 3-cell \(c\), the face holonomies on \(\partial c\) cannot in general be multiplied as raw matrices: each face holonomy has its own base point and orientation. Choose a common base point, paths transporting each face holonomy to it, and an ordering induced by a shelling of the boundary. The resulting conjugated, ordered product obeys the discrete non-Abelian Bianchi relation (boundary-of-boundary cancellation with parallel transports). The precise formula depends on the chosen shelling and paths; different choices give conjugate/equivalent identities, not an unqualified commutative sum.

**Required proof obligation:** specify this transport/shelling convention and prove the identity by cancellation of each oriented boundary edge, retaining the conjugations. A test that merely sums rotation angles is insufficient.

### 5.2 Torsion Bianchi identity

The continuum identity \(D_\omega T=R\wedge e\) suggests a discrete identity of the form
[
D_A\mathcal T=\mathcal R\smile_A E,
]
where \(\mathcal R\) is a discrete curvature 2-cochain, \(E\) a discrete coframe 1-cochain, and \(\smile_A\) is a specified covariant cup/wedge product with the required transports and ordering. This is a *target equation*, not yet a theorem. Its definition must be derived from a discrete Cartan structure equation or a consistent finite-element/DEC discretization; an arbitrary cup product will not suffice.

In particular, \(D_A\mathcal T=0\) is expected only in a flat/zero-curvature regime under the relevant assumptions. Do not impose closure in a curved configuration.

## 6. 2-chains, Burgers flux, and cohomology

Let \(C=\sum_f n_f f\in C_2(K;\mathbb Z)\). After transporting each \(\alpha_f\) to a common reference fibre, define the chain evaluation
[
B_A(C)=\sum_f n_f P_{C\leftarrow f}\alpha_f.
]
This is a covariant, frame-dependent vector (or a vector in the selected common fibre), not automatically a topological invariant. For non-Abelian transport, the linear sum is a first-order/additive flux construction; the exact finite-defect composition is the ordered (SE(3)) product of holonomies. The two agree only in a suitable linearized/abelian regime.

If the coefficient system is flat and \(\alpha\in C^2(K;\mathcal V_A)\) is a genuine cocycle, it defines a class \([\alpha]\in H^2(K;\mathcal V_A)\). Its pairing with a homology class is well-defined under the standard chain/cochain pairing (with dual local systems where needed). If \(\alpha=d_A\eta\) is exact, its pairing with closed 2-cycles vanishes. A nonzero cohomology class is an obstruction to removing the defect globally by an admissible potential.

For a curved connection, the preceding cohomology statement does **not** follow: \(d_A^2\ne0\), and chain evaluation can depend on the chosen comparison paths and on curvature in the swept 3-chain. The appropriate replacement may be a curved-cochain, cellular sheaf, relative-homology, or higher-gauge formulation; the correct choice is an open mathematical question.

### 6.1 Local density versus integrated flux

If \(|f^*|\) is the volume of the dual 3-cell associated with a primal face in a 3D dual mesh, a candidate local density is
[
\rho_f=\frac{P_f\alpha_f}{|f^*|}.
]
The integrated flux through a primal 2-chain is \(B_A(C)\). These are different objects and have different units. The normalization and primal/dual assignment must be fixed by the chosen DEC Hodge star and mesh geometry. On a 2D surface complex such as C60, there is no 3D dual volume \(|f^*|\); a surface density requires a different normalization.

## 7. Minimal theorem programme and status

| ID | Statement to establish | Necessary hypotheses | Current status |
|---|---|---|---|
| BDEC-01 | Gauge covariance of edge transports and covariant coboundary | Explicit representation and frame action | Direct algebraic proof required |
| BDEC-02 | Face holonomy transforms by base-point conjugation | Ordered path convention | Direct algebraic proof required |
| BDEC-03 | Discrete Cartan structure equation and torsion closure | Cochain coframe and compatible transports | Candidate definition |
| BDEC-04 | Discrete curvature Bianchi identity on each 3-cell | Shelling, paths, ordered conjugations | Derivation open |
| BDEC-05 | Discrete torsion Bianchi identity | Defined covariant cup product and discrete Cartan equation | Derivation open |
| BDEC-06 | deWit/Nye density is a continuum limit of the discrete torsion/closure | Kinematic identification and convergence assumptions | Derivation open |
| BDEC-07 | 2-cycle flux depends only on homology class | Flat local system and cocycle condition | Standard cohomological consequence once hypotheses hold |
| BDEC-08 | Curved correction to flux balance across a 3-chain | Curved transport and discrete Bianchi data | Open |

No item in this table is classified as proved by the present specification. BDEC-01, 02 and 07 are expected to admit short proofs once all conventions are fixed; BDEC-04 through 06 require substantive derivation.

## 8. Verification plan

1. **Algebraic unit tests:** verify \(G_{wv}=G_{vw}^{-1}\), composition, gauge covariance, and face-base conjugation on random (SE(3)) data.
2. **Flat test:** set all face holonomies to identity (pure-gauge edge data); verify zero rotational and translational closure defects and path independence.
3. **Controlled dislocation test:** prescribe a known Burgers circuit in a flat rotational background; compare the exact ordered holonomy with the additive small-defect approximation.
4. **Curved test:** prescribe noncommuting rotations and translations on a tetrahedral 3-complex; verify the transported non-Abelian curvature Bianchi product, not a scalar-angle surrogate.
5. **Cartan test:** construct a discrete coframe and connection from one common generating model; test the discrete torsion equation and the curvature-coupled Bianchi residual under mesh refinement.
6. **Cohomology test:** use a complex with known \(H_2\) and a flat local system; compare flux on homologous cycles and verify vanishing for exact cocycles.
7. **Convergence test:** compare the discrete fields with smooth continuum \((e,\omega,T,R)\) under refinement, reporting norms, rates, and gauge covariance.

## 9. Relation to the C60 audits

The merged C60 work establishes a surface-level geometric connection/holonomy crosscheck and intrinsic angular defects. The Devin/GH cross-audit independently reproduces the connection and full vertex holonomy matrices in a fixed common frame/tree convention. It also establishes that the reported \(\|M_f\|\) changes with tree/frame and is not an invariant.

Those results are useful test fixtures for the rotational, 2D part of this programme. They do **not** establish an \(SE(3)\) translational defect, a deWit/Nye identification, a 3D Bianchi identity, a global deformation \(g\), or a dislocation-density theorem. In particular, a 2D C60 surface has no 3-cells and cannot certify the 3D Bianchi statements.

## 10. References and convention control

The implementation should record the precise convention used for:
- left/right group action and path-product order;
- orientation and incidence signs;
- face base points and comparison paths;
- representation and associated local system;
- Cartan torsion sign and curvature sign;
- continuum Curl/index convention in the Nye tensor;
- primal/dual Hodge star and density units.

Relevant foundational references to anchor the later bibliography include:
- É. Cartan, *La théorie des groupes finis et continus et l'Analysis Situs* (Cartan structure equations and moving frames).
- J. F. Nye, “Some geometrical relations in dislocated crystals,” *Acta Metallurgica* 1 (1953), 153–162.
- R. deWit, “Theory of disclinations,” *Journal of Research of the National Bureau of Standards A* 77A (1973), 607–658; and “Theory of dislocations: II. Continuous distributions of dislocations,” *Journal of Research of the National Bureau of Standards A* 77A (1973), 49–100.
- M. Desbrun, A. N. Hirani, M. Leok, J. E. Marsden, “Discrete Exterior Calculus,” arXiv:math/050834 ಡ (preprint; verify final bibliographic form before formal citation).
- M. G. Eastwood? **Do not cite without verification.** The discrete non-Abelian Bianchi and higher-gauge references must be added only after checking the exact theorem/convention used.

The reference list is intentionally provisional. In particular, verify the exact deWit article title/pages and replace the DEC preprint placeholder with the authoritative publication record before treating this document as a finished bibliography.
