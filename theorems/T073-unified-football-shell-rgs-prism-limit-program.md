# T073 — Unified football-shell / RGS–PRISM–Q6 limit programme

**Status: OPEN — conditional research programme; no global Γ-convergence theorem is claimed.**  
**Scope:** organise the local barycentric results, the football-shell discretisation, structured deformations, discrete transfer maps and possible operator limits. The local results T068–T072 and S.1–S.11 retain their own proof classifications. None is promoted here into a global limit theorem.

## 1. Geometry, meshes and distinct complexes

Let \(S\subset\mathbb R^3\) be a compact, orientable, embedded, piecewise-\(C^2\) surface representing the football shell. Its panel complex has 60 vertices, 12 pentagons, 20 hexagons and 90 physical panel seams. The fan triangulation has 180 triangular CST facets; the recorded shell discretisation has 92 nodes when panel centres are included.

Let \(\mathcal T_h\) be a conforming triangular refinement of the shell, with maximum element diameter \(h\to0\). Shape regularity alone is not enough for the conclusions below: the geometric approximation, element maps, metric tensors, normals and seam incidence must also be controlled uniformly.

The comparison cubical complex \(Q_6\) has 64 vertices, 192 edges and 240 square 2-cells. The 92-node shell and \(Q_6\) are different complexes. No bijection or canonical identification is inferred from their node counts. Any comparison must use explicitly defined chain or field maps, with stated domains, codomains and norms.

The orientability of the closed embedded shell supplies a global choice of unit normal away from the panel singularities. If the piecewise-\(C^2\) structure has creases, the two one-sided normals and the convention for traces at each crease must be specified; a global orientation does not make the normal continuous across a crease.

## 2. Intrinsic fibré structured-deformation variables

The shell displacement must be treated as a section of a vector bundle, not globally as a list of unrelated Cartesian components. Let \(S\) be the oriented reference shell, with tangent bundle \(TS\), normal line bundle \(NS\), and displacement bundle
\[
\pi:E=TS\oplus NS\longrightarrow S.
\]
The embedding in \(\mathbb R^3\) gives an ambient trivialization of \(E\), but does not provide a global tangent frame. Tangential and normal components are local bundle components and must transform under changes of panel frame.

A displacement is a section \(u\) of \(E\). When jumps are allowed at panel boundaries, use panelwise sections \(u_p\in SBV(P_p;E|_{P_p})\). The covariant derivative is
\[
\nabla^E u\in L^p(S;T^*S\otimes E),
\]
with the connection induced by the Levi-Civita connection on \(TS\) and the normal connection on \(NS\). If a structured-deformation variable \(G\) is introduced, it must belong to the same bundle as \(\nabla^E u\), so that \(M=\nabla^E u-G\) is intrinsically defined.

For each panel chart, local frames are trivializations only. On a seam overlap, the transition map \(g_{+-}(x):E_x^-\to E_x^+\) identifies fibre coordinates. The intrinsic jump is
\[
[u]_e=u^+-g_{+-}u^-\in E|_{\Gamma_e}.
\]
At multi-panel junctions, the transition maps must satisfy cocycle/holonomy compatibility; force covectors and resultants must be transported to a common fibre before balance is imposed.

A candidate state space is therefore the bundle-valued structured-deformation space
\[
\mathcal{SD}_p(S;E)=
SBV(S;E)\times L^p(S;T^*S\otimes E),
\]
or its panelwise version with prescribed seam traces. Its precise definition on a piecewise-\(C^2\) surface, including traces, jump measures, connection regularity and varying-surface comparison maps, remains a proof obligation. The earlier notation \(SBV(S;\mathbb R^m)\) is recovered only after choosing an ambient trivialization; it is not the intrinsic definition.

The physical seam network \(\Gamma_{\rm phys}\) is prescribed material/geometric data. The mesh skeleton \(\mathcal S_h\) and the variational jump set \(S_u\) are different objects and must remain distinct. A seam energy is a fibrewise density on \(E|_{\Gamma_e}\), with its transition maps and frame covariance explicitly specified.

## 2.1. Triplett anisotropy transferred to the tangent fibre

Two established finite-dimensional structures must be kept distinct and then connected by an explicit map.

**(i) Q6 tangent T2u triplet.** The recorded spectral triplet is
\[
V\in\mathbb R^{188\times3},\qquad V^TV=I_3,\qquad
\lambda_{T_{2u}}=-0.06994933008401777
\]
with multiplicity three. The first triplet has now been reconstructed from the recovered 64-site geometry, the 48-element signed-permutation action of \(O_h\), the \(T_{2u}\) character projector and the constrained Coulomb Hessian. The isotypic projector has rank 30; the lowest restricted eigenvalue is \(-0.069949330084017\) with multiplicity three, separated from the next \(T_{2u}\) eigenvalue by approximately \(0.3193062\). The exported frame \(V\) is a deterministic coordinate-pivoted orthonormal basis of this three-dimensional spectral subspace. Its span/projector is invariant, while the particular basis within the degenerate triplet is a gauge choice. The implementation is reconstruct_rgs_t2u_triplet in models/tangent_triplet_anisotropy.py; the reproducible export is scripts/reconstruct_rgs_t2u_triplet.py. This rank-three spectral subspace is not an invertible tetrad.

**(ii) PRISM/G2 tripletti.** For each triplett \(T=(r_1,r_2,r_3)\), with \(r_i\in\mathbb R^2\), put \(R_T=[r_1\ r_2\ r_3]\) and
\[
Q_{G_2}=\begin{pmatrix}2&-3\\-3&6\end{pmatrix},\qquad
\Gamma_T=R_T^TQ_{G_2}R_T.
\]
The recorded family has 216 tripletti and 20 Gram classes; every \(\Gamma_T\) is positive semidefinite with rank at most two. These Gram classes encode channel anisotropy. They are not automatically the constitutive tensor of the football fabric.

**(iii) Finite-mesh bridge; continuum extension open.** At each of the 92 shell nodes \(x_i\), the implemented transfer is
\[
L_i:\mathbb R^{188}\longrightarrow T_{x_i}S\subset\mathbb R^3,
\qquad L_i=P_iW_iQ.
\]
The transferred T2u channel map is
\[
U_i=L_iV:\mathbb R^3\longrightarrow T_{x_i}S,
\qquad \operatorname{rank}U_i=2.
\]
The implementation checks the rank at every node and raises if it fails; the dedicated all-node regression test is included but its CI execution is still pending. The formula defines a finite-mesh nodal map, not yet a smooth family \(L_x\) at every continuum point. For a selected G2 triplett class, the nodal tangent anisotropy is
\[
A_T(x_i)=U_i\Gamma_TU_i^*
\in\operatorname{Sym}^+(T_{x_i}S).
\]
Equivalently, in a local orthonormal tangent frame \(F_i:\mathbb R^2\to T_{x_i}S\),
\[
[A_T(x_i)]_{F_i}=F_i^TU_i\Gamma_TU_i^TF_i.
\]
Under a frame change \(F_i\mapsto F_iO_i\), this matrix transforms as
\(A_F\mapsto O_i^TA_FO_i\); its eigenvalues and anisotropy ratio are frame-independent. The ambient tensor \(U_i\Gamma_TU_i^T\) is unchanged. A connection-preserving extension along panel interiors and across seam overlaps remains open.

The induced seam constitutive form is then a bundle endomorphism on
\(E|_{\Gamma_e}=TS|_{\Gamma_e}\oplus NS|_{\Gamma_e}\), for example
\[
K_e(x)=
\begin{pmatrix}
k_{0,e}I_{T_xS}+\alpha_e A_T(x)&0\\
0&k_{o,e}
\end{pmatrix}.
\]
This is a model class, not a fitted law: \(\alpha_e,k_{0,e},k_{o,e}\) require material/seam identification. It keeps tangential anisotropy distinct from shell-normal peel/opening.

The code primitive models/tangent_triplet_anisotropy.py implements the Gram construction, the explicitly supplied transfer composition, tangent-fibre push-forward, frame-covariance diagnostics and the block seam-fibre stiffness. Unit tests are in tests/test_tangent_triplet_anisotropy.py.

**Status correction:** the finite-mesh nodal transfer \\(L_i=P_iW_iQ\\) is now explicitly implemented in §2.2, and the T2u triplet can be reconstructed from the original 64-site geometry rather than supplied as an opaque external array. The bridge is therefore computationally specified at the 92 shell nodes. Still open are (a) execution of the repository's complete regression suite, (b) a smooth/connection-preserving extension over the continuum shell, (c) seam transition maps and holonomy, (d) refinement stability/convergence, and (e) physical identification of the PRISM channel gauge and seam coefficients. The 216 tripletti / 20 Gram classes and the T2u eigenspace remain distinct objects connected only by the displayed maps.

### 2.2. Explicit discrete construction of the shell fibre map

The geometry transfer is assembled from the existing direction-grouped affine map \(W\in\mathbb R^{276\times192}\), the exact source constraint tangent basis \(Q\in\mathbb R^{192\times188}\), and the node-wise tangent projector \(P_i=F_iF_i^T\):
\[
CQ=0,\quad Q^TQ=I_{188},\qquad
L_i=P_iW_iQ:\mathbb R^{188}\to T_{x_i}S.
\]
Here \(W_i\in\mathbb R^{3\times192}\) is the three-row block of \(W\) associated with shell node \(x_i\), and \(F_i\in\mathbb R^{3\times2}\) is an orthonormal tangent frame. In local coordinates,
\[
[L_i]_{F_i}=F_i^TW_iQ\in\mathbb R^{2\times188}.
\]
Under \(F_i\mapsto F_iO_i\), the local matrix transforms to \(O_i^T[L_i]_{F_i}\), while the ambient map is unchanged.

The affine \(W\) is the existing 64-point to 92-node direction-grouped transfer: 56 distinct source directions, eight duplicated direction pairs at different radii, with each directional weight split equally among its radial representatives. The source \(Q\) is the null-space basis of the four stated constraints (three translations and the radial/scale constraint). The \(P_i\) are formed from oriented area-weighted node normals of the 180-triangle football shell.

Implementation:
- build_rgs_shell_tangent_fibre_maps in models/tangent_triplet_anisotropy.py returns all 92 ambient maps \(L_i\), local \(2\times188\) matrices, frames, ranks and residual diagnostics.
- reconstruct_rgs_t2u_triplet reconstructs the first T2u eigenspace by the O_h character projector and the constrained Coulomb Hessian; scripts/reconstruct_rgs_t2u_triplet.py exports the 188×3 frame and projector diagnostics.
- push_triplett_to_shell_nodes composes the reconstructed orthonormal Q6 triplet \(V\in\mathbb R^{188\times3}\), forms \(U_i=L_iV\), and evaluates \(A_T(x_i)=U_i\Gamma_TU_i^T\).
- tests/test_rgs_shell_tangent_fibre_transfer.py checks all-node rank two, tangency, source constraints, positive semidefiniteness and local gauge covariance.

An independent numerical replay of the implemented formulas using the reconstructed T2u frame gives rank \(\operatorname{rank}(L_iV)=2\) at all 92 nodes. The maximum normal-component residual \(\max_i\|U_i^Tn_i\|\) is \(3.71\times10^{-17}\). For the algebraic regression triplett \(R=\begin{psmallmatrix}1&0&1\\0&1&1\end{psmallmatrix}\) (a test representative, not a claim that this is one of the archived 216), the pushed tensors are symmetric to \(2.46\times10^{-18}\), have minimum eigenvalue \(-1.60\times10^{-18}\) (roundoff), and maximum normal residual \(7.66\times10^{-18}\). These are independent numerical checks, not yet the repository CI result or validation of all 216 physical tripletti.
- scripts/audit_rgs_shell_tangent_fibre_transfer.py reproduces the nodal-map diagnostics and optionally accepts an audited 188x3 T2u basis plus a 2x3 triplett file to compute the pushed anisotropy.

This upgrades the previous unspecified \(L_x\) to an explicit finite-mesh nodal transfer. It does not yet prove a smooth bundle morphism over every point of \(S\), connection preservation along panels/seams, or convergence under shell refinement. The previously reported principal-angle comparison (three angles near \(2.4^\circ\) at 16 neighbours) concerns the transferred rotational triplet against the three lowest shell tangent modes; it is not a proof about the separate Q6 \(T_{2u}\) eigenspace or the 216 PRISM tripletti.

## Discrete seam connection and gauge compatibility (finite-mesh level)

The implementation in `models/football_bundle_connection.py` now constructs, for each of the 90 physical seam edges, the hinge-wise minimal rotation \(R_{-+}\in SO(3)\) carrying the minus panel normal to the plus panel normal. With fixed panel tangent frames \(F_\pm\in\mathbb R^{3\times2}\), it returns
\[
g^{TS}_{+-}=F_+^T R_{-+}F_-\in O(2).
\]
It also augments the frames by their normals, \(\widehat F_\pm=[F_\pm,n_\pm]\), and returns the full displacement-bundle transition
\[
g^{E}_{+-}=\widehat F_+^T R_{-+}\widehat F_-\in O(3),
\qquad E=TS\oplus NS.
\]
The seam jump is evaluated in the plus chart as \([u]_e=u_+-g^E_{+-}u_-\). Under independent orthogonal chart changes \(O_\pm\), the rules are
\[
u_\pm' = O_\pm^T u_\pm,\qquad
(g^E_{+-})'=O_+^Tg^E_{+-}O_-,\qquad
[u]'_e=O_+^T[u]_e.
\]
Thus a fibrewise quadratic seam energy is chart-independent when its stiffness is transformed by the same conjugation.

The T2u/PRISM channel basis has a separate \(O(3)\) gauge. If \(V\mapsto VO\) and \(R_T\mapsto R_TO\), then \(\Gamma_T\mapsto O^T\Gamma_TO\), \(U_i\mapsto U_iO\), and
\[
(U_iO)(O^T\Gamma_TO)(U_iO)^T=U_i\Gamma_TU_i^T.
\]
The code and tests implement this simultaneous gauge law. This proves gauge covariance of the formula; it does **not** select a physical alignment between the reconstructed T2u basis and the labelled PRISM channels.

**Data-provenance boundary:** the theorem repository currently contains the T2u reconstruction and the PRISM Gram definition \(Q_{G_2}\), but no machine-readable table of the 216 physical \(2\times3\) tripletti with their canonical channel labels and 20 class assignments. The implementation therefore does not fabricate those matrices or claim all-216 validation. Supplying the source table (or its canonical generator) is required to fix the physical channel gauge and run the complete 216-case push-forward audit.

The connection and chart-covariance tests have been added to the football workflow. Their CI result is pending; the finite-mesh construction is not a smooth continuum connection, and its hinge holonomy/refinement limit remains open.

## 3. Local Dirichlet–Gamma/Beta moments and what T068/T070 prove

For a triangle \(F\) of area \(A_F\), let \(a_{F,i}>0\), \(S_F=\sum_{i=1}^3a_{F,i}\), \(\lambda_i\) be barycentric coordinates and \(V_F\) the vertex matrix. Define
\[
B_3(a_F)=\frac{\prod_i\Gamma(a_{F,i})}{\Gamma(S_F)},
\qquad Z_F=2A_FB_3(a_F),
\qquad p_{F,i}=\frac{a_{F,i}}{S_F}.
\]
For the Dirichlet probability measure,
\[
C_{F,ij}
=\operatorname{Cov}(\lambda_i,\lambda_j)
=\frac{p_{F,i}\delta_{ij}-p_{F,i}p_{F,j}}{S_F+1}
=\frac{a_{F,i}(S_F\delta_{ij}-a_{F,j})}
{S_F^2(S_F+1)}.
\]
The barycentre and physical covariance are
\[
c_F=V_F^{\mathsf T}p_F,\qquad
\Sigma_F=V_F^{\mathsf T}C_FV_F.
\]
For a scalar- or vector-valued \(u\in C^3\) on a neighbourhood of \(F\), the local Taylor estimate is
\[
\mathbb E_F[u(X)]
=u(c_F)+\frac12D^2u(c_F):\Sigma_F+R_F,
\qquad
|R_F|\le \frac{h_F^3}{6}
\sup_F\|D^3u\|_{\mathrm{op}},
\]
with the unnormalised integral obtained by multiplying by \(Z_F\).

Consequently,
\[
\sum_{F\in\mathcal T_h}Z_F|R_F|
\le \frac{h^3}{6}
\left(\sup_F\|D^3u\|_{\mathrm{op}}\right)
\sum_{F\in\mathcal T_h}Z_F,
\qquad h=\max_Fh_F,
\]
provided the displayed supremum is uniform. This is a conditional summation of the local estimate, not by itself a global convergence theorem. To conclude that the right-hand side tends to zero one must establish a uniform bound on the total weights \(\sum_F Z_F\), as well as the stated uniform derivative bound and admissible control of the Dirichlet parameters.

T068/T070 establish local moment, covariance and Taylor/quadrature statements under their stated hypotheses. They do not establish uniformity for every football refinement, a global surface quadrature theorem, or a Γ-limit.

The derivatives of \(\log B_3\) are expressed through digamma and trigamma functions and encode cumulants of logarithmic barycentric coordinates. Zeta, Bernoulli and Euler–Maclaurin identities may enter asymptotic expansions, but they do not determine mesh-summation correction terms without an explicit refinement and summation rule.

## 4. Candidate discrete energy — constitutive choices remain open

A schematic family may have the form
\[
\begin{aligned}
\mathcal E_h(u_h,g_h,G_h,\theta_h)
={}&\sum_{F\in\mathcal T_h}\int_F
W_F(X,\nabla_Su_h,G_h,\theta_h,\nabla_S\theta_h)\,dA\\
&+\sum_{e\in\mathcal S_h}\int_e
\psi_e([g_h],\nu_e,\theta_h)\,d\mathcal H^1
+\mathcal E_h^{(4)}.
\end{aligned}
\]
This is only a template. The bulk density \(W_F\), seam density \(\psi_e\), fourth-moment term \(\mathcal E_h^{(4)}\), admissible variables and boundary conditions must be specified before a Γ-convergence statement is even a complete mathematical proposition.

In particular, a physical panel seam \(\Gamma_{\rm phys}\) is prescribed geometric data, whereas the jump set \(S_{g_h}\) is part of the variational state. They must not be identified without an explicit modelling choice. A seam term quadratic in the jump is not automatically covered by a theory requiring a one-homogeneous interfacial density.

## 5. Required hypotheses — obligations, not established assumptions

A proof must verify the following items for the actual mesh family and energy.

- **H1 — Surface approximation and geometry.** Specify \(S_h\), element-to-surface maps and comparison maps to \(S\). Require appropriate uniform bi-Lipschitz bounds, convergence of metrics and surface measures, and convergence/control of one-sided normals. Shape regularity alone does not imply all of these.
- **H2 — Mesh and local moments.** Require uniform shape regularity, admissible Dirichlet parameters, bounds on \(Z_F\), barycentres and covariance tensors, and a uniform Taylor remainder estimate. In particular establish \(\sup_h\sum_F Z_F<\infty\) if using the global estimate in §3.
- **H3 — Field compactness.** State the topology and prove uniform bounds sufficient for compactness of \(g_h\) in \(L^1\), weak compactness of \(G_h\) in \(L^p\), and control of the jump measures. A typical sufficient coercivity assumption is
  \[
  W(X,A,B)\ge c_1(|A|^p+|B|^p)-c_2,\qquad p>1,
  \]
  but it is not necessary in this exact form. Control of \(B\) may instead follow from a bound on \(A-B\) together with control of \(A\). A bound on \(A\) alone does not control \(B\).
- **H4 — Bulk/interface relaxation.** State the precise growth, coercivity, measurability, lower-semicontinuity, quasiconvexity and interfacial subadditivity assumptions needed by the chosen relaxation theorem. The Euclidean periodic theorem of Amar–Matias–Morandotti–Zappale (2022) applies under its own hypotheses; it is not automatically a theorem for a compact curved shell.
- **H5 — Seams and jumps.** Fix one seam model (see §7), define whether physical seams are admissible jump locations, and prevent double counting between a seam energy and the jump part of the bulk/interface functional.
- **H6 — Moment and fourth-order consistency.** Prove the required first-, second-, third- and fourth-moment bounds/cancellations for the actual refinement. S.4 (fixed-cloud fourth moment), S.5 (jump fourth moment/Taylor expansion), S.6 (derivative), S.7 (Maxwell obstruction) and S.8 (coframe variation) are distinct results and must not be conflated.
- **H7 — Discrete transfer.** Define each map between \(Q_6\), Kathara and shell chain/field spaces, including domain, codomain, norms and orientation conventions. Prove the relevant chain identities, uniform boundedness and geometric/metric/measure consistency. The finite Gate D chain identities alone do not imply these analytic properties.
- **H8 — Operator and spectral convergence.** If sought, separately specify varying Hilbert spaces, comparison maps, quadratic forms, Mosco convergence, compactness of resolvents and multiplicity control. A chain map or Γ-limit of a non-quadratic energy is not by itself an operator- or spectral-convergence theorem.

## 6. L1–L6: proof obligations and current status

The following are the logical work packages. Their surface versions remain open unless a separate proof is added.

| Lemma | Required statement and missing proof | Status |
|---|---|---|
| **L1 — Compactness** | Prove compactness of \(g_h\) in the declared \(L^1\) topology and weak compactness of \(G_h\) in \(L^p\). This requires coercive bounds, control of the jump measure (typically a uniform \(\mathcal H^1(S_{g_h})\) bound or the precise substitute supplied by the energy), an \(L^1/L^\infty\) bound or normalization, and uniform surface charts/transfer maps. The Euclidean SBV compactness theorem does not automatically supply the uniform statement on varying \(S_h\). | **OPEN on the shell.** Euclidean compactness is established in the relevant classical theory under its hypotheses. |
| **L2 — Localisation and Radon measure** | Show that the limiting set function on open subsets of \(S\) is finite, increasing and suitably subadditive, and verify the De Giorgi–Letta/Fonseca–Malý hypotheses in the intrinsic surface topology. The local compact-space measure argument is potentially transferable, but the required nested subadditivity and seam conventions must actually be checked. | **OPEN for this functional on \(S\).** General measure-representation machinery is available; its hypotheses have not been verified here. |
| **L3 — Relaxation and cell density** | Define the local blow-up/cell problem, prove existence of the limiting density, and establish independence from charts and local frames. The periodic cell formula in Euclidean space cannot simply be copied to a general compact surface, which has no global translation group. The effective density may depend on position, tangent plane and curvature. | **OPEN.** No intrinsic cell formula or chart-independence proof is supplied. |
| **L4 — Liminf inequality** | For the declared convergence, prove \(\mathcal E(g,G)\le\liminf_h\mathcal E_h(g_h,G_h)\). This requires the appropriate intrinsic lower-semicontinuity/quasiconvexity and control of the limiting interface measure, including discrete seams and one-sided geometry. | **OPEN.** |
| **L5 — Recovery sequence** | For each admissible \((g,G)\), construct a sequence \((g_h,G_h)\) with \(\limsup_h\mathcal E_h(g_h,G_h)\le\mathcal E(g,G)\). The approximation of a general jump set by mesh edges, and the associated seam/jump cost, must be controlled. A jump not aligned with edges cannot be assumed to have a cost-free or uniformly bounded mesh approximation. | **OPEN.** |
| **L6 — Discrete/continuous transfer** | Define explicit maps \(T_h\), prove consistency and stability, and verify the chain/field and metric properties needed by the intended limit. Without a specified \(T_h\), this is not yet a fully testable theorem statement. | **OPEN; not yet an instantiated lemma.** |

Logical dependencies: L1 supports L2, L4 and L5; L2 supplies a measure framework for L3; L3 supplies candidate densities for L4 and L5; L4 and L5 together establish Γ-convergence once compactness/equicoercivity is also available. L6 is a separate prerequisite for conclusions that compare the shell discretisation with \(Q_6\)/Kathara or identify discrete operators with continuum ones.

## 7. Physical seam models — choose one before proving a limit

Let \(\Gamma_{\rm phys}\subset S\) be the prescribed panel-seam network.

- **Model A — kinematic constraint.** Impose a trace constraint such as \([g]=0\), or a prescribed jump, on \(\Gamma_{\rm phys}\). The seam is a constraint, not an additional free jump energy. The admissible class and trace convention must be specified.
- **Model B — cohesive interface.** Assign a separate density \(\psi_\Gamma([g],\nu,\theta)\) to the fixed interface. State its growth, continuity and lower-semicontinuity assumptions and ensure that the same interface is not counted again in a generic jump term.
- **Model C — geometric seam without an energetic jump penalty.** The seam records a change of panel geometry, metric or normal but contributes no independent jump cost. This is mathematically possible only after specifying the admissible traces and the bulk density across the seam; zero penalty can otherwise permit energetically uncontrolled jumps.

These are different models, not interchangeable notational conventions. The energy must say whether \(S_g\) may intersect \(\Gamma_{\rm phys}\), whether it may contain it, and how the seam contribution is counted. In particular, double-counting a seam once as a prescribed interface and again as a free jump is a modelling error unless the two terms represent distinct physical mechanisms.

A useful falsification test is to compare meshes with seams aligned to edges against meshes where the same fixed seam cuts element interiors. Compute the seam and jump contributions separately. A non-vanishing discrepancy under refinement signals that the discrete interface convention is not consistent; it is not, by itself, a proof of a general counterexample.

## 8. Four convergence claims that must remain separate

1. **Γ-convergence** concerns convergence of functionals in a declared topology. It does not by itself imply convergence of minimisers without equicoercivity, nor convergence of operators.
2. **Mosco convergence** is a weak-liminf/strong-recovery convergence for convex functionals (in particular closed quadratic forms) on a fixed Hilbert space, or on varying spaces with explicitly controlled comparison maps. It is not merely another name for Γ-convergence.
3. **Operator/resolvent convergence** requires the relevant closed forms, domains and Hilbert-space identifications, plus the hypotheses of the chosen form-convergence theorem.
4. **Spectral convergence** additionally requires suitable compactness of resolvents (or another precise spectral compactness condition) and control of multiplicities. Compactness of \(S\) alone is not enough if the limiting form domain or coercivity does not give compact embedding.

The \(Q_6\) Walsh spectrum, the \(S^3/T^*\) spectrum and the \(S^3/2I\) spectrum are separate exact benchmarks. None is automatically the limit spectrum of the football shell.

## 9. Separate target statements

The programme has four targets, each requiring its own hypotheses and proof.

**(A) Global barycentric quadrature.** Sum the local T068/T070 expansions and prove an explicit global error bound, including uniform control of the total weights and derivative norms. Derive any Bernoulli/Euler–Maclaurin corrections from the actual mesh summation rule.

**(B) Structured-deformation Γ-limit.** Define the surface functional, topology and seam model; prove compactness/equicoercivity, liminf and recovery. Any use of Amar–Matias–Morandotti–Zappale (2022) must identify the exact Euclidean hypotheses used and prove the additional surface/mesh extension.

**(C) Mosco/operator limit.** Define the discrete and continuum quadratic forms and comparison maps; prove weak-liminf and strong-recovery properties on the declared Hilbert spaces.

**(D) Spectral convergence.** After (C), prove the required compact-resolvent and spectral multiplicity hypotheses. Do not infer it from a finite chain map, a numerical spectral fit or a common algebraic parameter.

## 10. Existing finite inputs and their scope

- **T068/T070:** local triangle barycentre, covariance and Taylor/quadrature identities under their stated hypotheses; not a global shell limit.
- **T069:** exact pair mean/difference covariance identity for a fixed-point-free involution; the recovered RGS seed covariance and XOR 7/XOR 63 distinction are finite records.
- **T071:** exact \(Q_6\) cubical chain identities \(B_1B_2=0\), Anti-Twin chain-map identities and the stated truncated-2-skeleton ranks/Betti numbers; synchronisation/hysteresis remains exploratory.
- **T072:** exact Möbius phase-translation action, pure-gauge vertex-phase connection, \(Q_6\) Walsh Laplacian spectrum and antipodal \(32+32\) decomposition; the canonical equal-time connection is trivial.
- **Gate D / PR #195:** recorded finite Kathara–\(Q_6\) chain-map identities and rank checks; no \(O_h\)-equivariance, canonical metric, shell embedding or spin transport follows.
- **Gate E.1 / T068:** local quadrature law and companion implementation; no global limit theorem.
- **S.4–S.8:** fourth-moment tensor, jump expansion, derivative, Maxwell obstruction and coframe variation, each with its own exact/numerical status.
- **S.9/S.10:** Weber–Dedekind eta, supergolden class invariant, Dirichlet eta/\(L\)-function/quadratic-zeta and Bernoulli/polygamma identities; these special-function identities do not prove the shell limit.
- **S011:** binary-tetrahedral \(S^3/T^*\) spectrum with an independent Molien/Peter–Weyl reconstruction. The binary-icosahedral \(S^3/2I\) spectrum is a separate module.

## 11. Falsification and proof gates

The global programme cannot be promoted if any required item remains absent: a uniformly controlled shell refinement; intrinsic function spaces and traces; uniform local-moment and total-weight bounds; a specified bulk/interface energy; a seam convention without double counting; compactness and relaxation; liminf and recovery; explicit transfer maps with the required consistency; and, for operator/spectral claims, Mosco and compact-resolvent arguments.

A numerical fit, common polynomial, shared phase parameter, visual cell correspondence or finite chain identity cannot replace these proof obligations.

## 12. Status and references

**Status: OPEN.** T073 is a structured research programme and checklist, not a theorem asserting that the global limit exists. The sufficient coercivity and geometric assumptions listed above are candidate hypotheses to be tested against a fully specified energy; they are not claimed to be minimal or already verified.

- [Canonical unitary theory](../docs/UNIFIED_THEORY_FOOTBALL_GAMMA_BETA_ZETA_MORANDOTTI_RGS_PRISM_Q6_2026-11-10.md).
- [Integrated moments/barycentres/Gamma–Beta–zeta/Morandotti synthesis](../docs/SYNTHESIS_MOMENTS_BARYCENTRES_GAMMA_BETA_ZETA_MORANDOTTI_2026-11-10.md).
- [Independent numerical replay report](../reports/2026-11-10_integrated_synthesis_numerical_replay.md).
- [Special-functions and Morandotti bibliography](../bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md).

### References

1. N. Yui and D. Zagier, “On the Singular Values of Weber Modular Functions,” *Mathematics of Computation* 66 (1997), 1645–1662.
2. A. Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Mathematical Journal* 18 (1995), 57–67.
3. Amar–Matias–Morandotti–Zappale (2022), “Periodic Homogenization in the Context of Structured Deformations,” *ZAMP* 73, article 173, DOI 10.1007/s00033-022-01817-6.
4. NIST Digital Library of Mathematical Functions, Chapters 5, 23, 24 and 25.
