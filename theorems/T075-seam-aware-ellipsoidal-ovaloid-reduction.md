# T075 — Seam-aware ellipsoidal reduction and ovaloid realization for the football shell

**Status: FORMULATION ESTABLISHED; numerical fit and continuum realization OPEN.**  
**Relation:** T073 (football-shell programme), T074 (icosahedral/Hopf–Seifert bridge), the repository's `models/football_shell.py` and `docs/FOOTBALL_ORTHOTROPIC_DISCRETE_SHELL.md`, and the Caccioppoli ovaloid discussion reproduced in the user's Nardelli/Lange reference PDF.

## 1. Purpose and modelling principle

The football is not a smooth ellipsoid. It is a closed assembly of pentagonal and hexagonal panels joined along physical seams. The ellipsoid is introduced as a **global reference shape and low-dimensional geometric reduction**, while panel boundaries, seam constitutive laws, orthotropy and hinge bending remain explicit in the mechanical model.

The reduction must therefore not replace the sewn shell by a featureless ellipsoid. It separates:
1. global smooth geometry (ellipsoid/ovaloid);
2. discrete panel partition and seam network;
3. panel material frames and orthotropic constitutive response;
4. seam/interface mechanics and bending hinges;
5. residual shape modes not represented by the ellipsoid.

The repository reference mesh has 60 truncated-icosahedron vertices, 12 pentagonal and 20 hexagonal panels, 90 physical panel-boundary seams, 92 mechanical nodes after adding panel centres, 180 fan triangles and 270 triangular hinges. The 270 hinges include internal fan edges; they are not 270 physical seams.

## 2. Ellipsoid as the first reference surface

Let (Qinmathrm{Sym}^+(3)) and (A=Q^{1/2}). The centred ellipsoid is
[
mathcal E_Q={xinmathbb R^3:x^TQ^{-1}x=1},
qquad X_Q(n)=An,quad nin S^2.
]
Its radial function in direction (n) is
[
r_Q(n)=rac{1}{sqrt{n^TQ^{-1}n}}.
]
For tangent vectors (v,win T_nS^2), its first fundamental form is
[
g_Q(v,w)=langle Av,Awangle=v^TQw.
]
The ellipsoid's Gaussian curvature at (X_Q(n)) is
[
K_Q(n)=rac{1}{det(Q),lVert A^{-T}nVert^4}>0.
]
For (Q=a^2I), this reduces to the round sphere of radius (a), with (K=a^{-2}).

The six independent entries of (Q) describe the global ellipsoidal degrees of freedom. Translation and rotation are treated separately as rigid registration variables; they must not be mistaken for shape parameters.

## 3. Fitting the global ellipsoid to the shell

For the generated mesh, denote the 60 physical panel vertices by (X_i), and let (n_i=X_i/lVert X_iVert) after choosing a centre and radial frame. A first radial fit is
[
mathcal J_{m vert}(Q,c)=
sum_{i=1}^{60}w_ileft[
lVert X_i-cVert-
rac{1}{sqrt{n_i^TQ^{-1}n_i}}
ight]^2,
quad Q>0.
]
This is only a vertex-shape fit. It does not encode seams or panel mechanics and must not be reported as a seam-aware shell fit.

A stronger surface fit samples the actual triangular surface, with area weights, and estimates the centre/orientation jointly. For a measured scan, use symmetric scan-to-model and model-to-scan distances after rigid registration; do not allow unconstrained scale to hide a shape mismatch.

The residual field is
[
u(n)=r_{m mesh}(n)-r_Q(n).
]
Project (u) onto a declared basis (for example spherical harmonics or the already implemented cube/sphere and (H_4) fields). Report coefficients and residual norm separately. Do not label a coefficient as golden-ratio-related unless it is identified by a preregistered constraint or independently measured ratio.

## 4. The seam network is retained explicitly

Let (mathcal P={P_1,ldots,P_{32}}) be the polygonal panels and
[
Gamma=igcup_{ein E_{m seam}}Gamma_e,qquad |E_{m seam}|=90
]
the physical seam network. The seam curves are embedded in, or mapped onto, the ellipsoidal reference surface. Their positions are inherited from panel incidence; they are not replaced by the 270 triangulation hinges.

A schematic seam-aware energy is
[
mathcal E_Q(u,artheta)=
sum_{pinmathcal P}int_{P_p}
W_pigl(x,arepsilon_{g_Q}(u),arthetaigr),dA_{g_Q}
+sum_{ein E_{m seam}}int_{Gamma_e}
left[
rac{k_{t,e}}2lVert [u]_tVert^2+
rac{k_{n,e}}2 [u]_n^2+
rac{k_{	heta,e}}2[artheta]^2
ight]ds_{g_Q}
+mathcal E_{m bend}(u,artheta).
]
Here (W_p) is the panel constitutive density (possibly orthotropic, with its own material frame); ([u]) and ([artheta]) denote the appropriate displacement/rotation mismatch across an interface. The precise trace variables and admissible spaces depend on the physical seam construction. For a perfectly bonded seam, displacement continuity is imposed as a constraint or as the limit (k_{t,e},k_{n,e}	oinfty), not assumed for every textile seam. The seam rotational stiffness (k_{	heta,e}) is distinct from internal triangulation hinges.

This expression is a **modelling template**, not a claim that the current linear CST/dihedral implementation already solves this continuum interface functional. The current code has an optional axial line spring on each physical seam and a separate seam bending multiplier; it does not yet implement general opening/slip/cohesive damage or independent rotational jump fields.

## 5. Discrete-to-ellipsoid correspondence

For each panel (P_p), define a reference map (Phi_p:P_p	omathcal E_Q) and a panel deformation (y_p). On each triangle, the current code computes a discrete deformation gradient (F_T), metric (C_T=F_T^TF_T), and Green–Lagrange strain
[
E_T=	frac12(C_T-I).
]
A continuum limit must compare these element metrics with the pullback metric of (Phi_p) and retain seam traces. In particular, the limit cannot be derived from vertex convergence alone: it requires control of element Jacobians, panel normals, edge traces, seam measures and material-frame transport.

The finite-dimensional ellipsoid fit is therefore a first reduction, not a proof of convergence. The natural next level is a piecewise smooth ovaloid whose metric is allowed to vary beyond the six ellipsoid parameters.

## 6. Extension from ellipsoid to ovaloid with prescribed metric

Let ((S^2,g)) be a smooth reference surface and let (h) be a positive-definite metric with positive Gauss curvature. The realization problem seeks an embedding
[
X:(S^2,h)longrightarrowmathbb R^3,
qquad X^*langlecdot,cdotangle_{mathbb R^3}=h,
]
with strict convexity. The ellipsoid family is a six-parameter subfamily of such metrics/embeddings.

The Nardelli/Lange PDF's chapter 3 reproduces the classical ovaloid-of-prescribed-metric framework attributed there to Caccioppoli (1940): the first fundamental form, second fundamental form, Mainardi–Codazzi compatibility, and a linear elliptic equation for the infinitesimal realization problem on a positively curved ovaloid. It also identifies the three-dimensional rigid-motion kernel and corresponding compatibility conditions. This historical source is a secondary reproduction and must be checked against the primary Caccioppoli publication before theorem-level attribution or transcription of its displayed formulas.

For the football problem, the intended route is:
- fit (Q) and quantify the residual;
- test whether residual modes can be represented by a smooth positive-curvature metric perturbation;
- impose Gauss–Codazzi compatibility and convexity;
- solve the prescribed-metric realization problem modulo rigid motions;
- pull the 90-seam network and panel constitutive fields onto the realized ovaloid;
- only then formulate a curved-shell variational limit with explicit interface terms.

A positive-curvature metric is a necessary geometric input for the classical strictly convex realization setting; it does not follow from arbitrary noisy mesh data. Convexity and regularity must be verified.

## 7. Icosahedral symmetry and the ellipsoid obstruction

If the centred ellipsoid is invariant under the full rotational icosahedral group (A_5), then
[
R^TQR=Qqquadorall Rin A_5.
]
The standard three-dimensional representation of (A_5) is irreducible, so its commuting symmetric matrices are scalar:
[
Q=a^2I.
]
Thus the only exactly (A_5)-invariant ellipsoid is a sphere. A non-spherical ellipsoid is a symmetry-breaking global deformation. The combinatorial football can still have (A_5)-symmetric panel/seam incidence, while its fitted shape or material response breaks that symmetry.

The panel/seam constitutive model must therefore be tested separately. A uniform seam law on the (A_5)-orbit of physical seams may preserve the group; panel orthotropy preserves it only if material frames are transported equivariantly. A measured ellipsoidal distortion generally lowers the geometric symmetry subgroup.

## 8. Golden-ratio constraints: hypothesis, not axiom

A condition such as
[
a/b=arphi,qquad arphi=(1+sqrt5)/2
]
may be tested as a constrained subfamily of ellipsoids, but it is not implied by convexity, positive Gaussian curvature, the truncated-icosahedron topology, or the definition of a general ovaloid. Compare:
- unconstrained (Qinmathrm{Sym}^+(3));
- a preregistered golden-ratio constraint on selected principal semiaxes;
- a general positive-curvature ovaloid.

Use held-out geometric data or an information criterion/regularised fit to determine whether the extra constraint is supported. Do not tune the golden constraint and all mechanical parameters against the same observations without independent validation.

## 9. Relation to T074, T073 and the spherical quotient

The ellipsoid/ovaloid is a two-dimensional shell reference surface. (S^3/2I) is a three-dimensional spherical space form. The Hopf–Seifert map in T074 supplies a group-theoretic relation between the binary icosahedral quotient and the orbifold (S^2/A_5), but it does not identify the physical football shell with either round quotient.

The appropriate comparison is representation-theoretic and operator-specific:
- identify which (A_5) sectors survive in the panel/seam complex;
- determine the symmetry subgroup of the fitted metric and constitutive operator;
- define the relevant scalar/vector/tensor shell operator on the ovaloid;
- compare invariant sectors only after specifying the operator, measure, boundary/interface conditions and fibre-mode decomposition.

No direct eigenvalue transfer from the round (S^2/A_5) value 42 or the (S^3/2I) value 168 is asserted.

## 10. Verification plan and status

| Item | Status |
|---|---|
| Ellipsoid parametrisation, radial function and induced metric | Exact |
| Positive Gaussian curvature formula for (Q>0) | Exact |
| Full (A_5)-invariant ellipsoid must be spherical | Proved |
| 60/32/90 vertex-panel-seam incidence of repository model | Implemented in source; existing audit |
| Seam-aware continuum energy | Formulated; constitutive trace spaces need specification |
| Current discrete seam axial spring and seam hinge multiplier | Implemented; not a general cohesive seam law |
| Ellipsoid fit to the 60 mesh vertices/surface | Not yet run |
| Ellipsoid fit with explicit seam and panel weighting | Not yet implemented |
| General ovaloid metric reconstruction | Open |
| Caccioppoli primary-source formula audit | Open |
| Golden-ratio semiaxis relation | Testable hypothesis only |
| Curved-shell Γ/Mosco/spectral limit with seams | Open |

### Required numerical outputs

A reproducible follow-up should report:
1. fitted centre and (Q), principal semiaxes and orientation;
2. vertex and area-weighted surface residuals, including held-out residuals;
3. seam lengths, panel areas, and residuals stratified by pentagon/hexagon and seam orbit;
4. orthotropic frame transport and seam stiffness values independently of the geometric fit;
5. (A_5)-commutators for mass/stiffness in the spherical reference case and measured symmetry-breaking residuals for fitted (Q);
6. principal curvatures and (K_G>0) checks for any reconstructed ovaloid;
7. sensitivity to seam stiffness and mesh refinement.


## 11. Physical status of seams: literature-based correction

A seam is not merely a curve in a drawing. In a textile/membrane structure it is a **joint between material panels**, and its load-transfer and failure behaviour must be characterised independently of the parent fabric. The JRC report *Prospect for European Guidance for the Structural Design of Tensile Membrane Structures* (Stranghöner et al., 2023, JRC 132615, DOI 10.2760/24763) explicitly states that membrane joints are carried out by seams; uncoated fabrics are sewn, while coated fabrics commonly use welded or clamped joints. It requires seam resistance to be established by tensile tests and distinguishes seam strength from bulk tensile strength, tear strength and adhesion. See the dedicated literature audit at `audits/2026-11-10_physical_seams_interfaces_literature_audit.md`.

This is consistent with experimental work on welded PVDF membranes (Liu et al., 2026, DOI 10.1016/j.tws.2026.114501) and off-axis welded-fabric seam testing (Yu et al., 2025, DOI 10.1177/15589250251342853). The seam may fail by tensile rupture or peeling; it can be the limiting structural component even when the base membrane remains intact.

### 11.1 The physics connection, stated precisely

Physics contains several related but non-identical interface objects:
- grain boundaries and disconnections in polycrystalline solids (Han, Thomas & Srolovitz, 2018);
- dislocations and disclinations as line defects (Kleman & Friedel, 2008);
- ferroic domain walls and lower-dimensional defects hosted by them (Nataf et al., 2020);
- cohesive, adhesive and frictional interfaces in continuum mechanics.

These are not literally sewn textile seams. The common mathematical structure is that an interface can carry its own energy, internal variables, defects, transport law and failure/kinetic response. Therefore the football seam network can be treated using interface mechanics, while analogies to grain boundaries or domain walls must remain structural analogies unless a specific physical identification is proved.

### 11.2 Corrected interface functional

Let (P_p) be the material panel regions on the reference ovaloid and (Gamma_e) the physical seam curves. The general energy is
[
mathcal E[y,z]=
sum_{p=1}^{32}int_{P_p}W_p(x,
abla_Sy),dA_g
+sum_{e=1}^{90}int_{Gamma_e}
psi_e(x,[y],[
abla_Sy],z_e),ds_g
+mathcal E_{m bend}[y].
]
The seam state (z_e) may encode damage, slip, thread pull-out, frictional state or hysteresis, but only if the actual joining process supports those variables. A cohesive law has traction (t_e=partial_deltapsi_e) with (delta=[y]); a frictional/clamped interface requires contact and tangential-slip laws; a sewn textile seam may require an effective law calibrated against stitch/thread and fabric tests. A welded seam needs tensile/peel and process-dependent parameters. These classes must not be collapsed into one universal spring.

The current code's axial line spring on physical seam edges and separate seam bending multiplier are only a rudimentary discrete special case. They do not implement cohesive damage, peel, thread pull-out, frictional slip, fatigue or hysteresis. The 270 triangulation hinges remain distinct from the 90 physical seams.

### 11.3 Consequence for the ellipsoid/ovaloid reduction

The seam network is now treated as a metric-measure graph embedded in the global ellipsoid/ovaloid:
[
(Gamma,ds_g,{psi_e}_{e=1}^{90}).
]
The global ellipsoid captures the low-dimensional shape; panel fields describe bulk material response; seam fields encode the joining physics. At seam crossings or multi-panel junctions, separate junction balance/compatibility conditions may be required. Any homogenised seam law must be derived in a stated scale regime and validated against seam-specific experiments.

**Revised status:** existence and mechanical relevance of seams are established by the engineering literature; the actual seam law for this football, its parameters, fatigue/hysteresis response and the seam-aware ovaloid limit remain open pending construction data and experiments.

## References and provenance

- Repository `models/football_shell.py`: generated truncated-icosahedral shell, 90 physical seams, orthotropic CST membrane, dihedral hinges, optional physical seam line reinforcement.
- Repository `docs/FOOTBALL_ORTHOTROPIC_DISCRETE_SHELL.md`: model scope, discrete metric diagnostics and experimental scan interface.
- User-provided PDF, *Serie di Fibonacci, rapporto aureo e ovaloidi a sezione aurea*, chapter 3, pp. 29–35: secondary reproduction of the prescribed-metric ovaloid framework attributed to Caccioppoli (1940). Primary-source verification remains required.
- T073 and T074.


## 12. Constitutive continuation

The construction-specific constitutive, damage, contact/friction, fatigue and hysteresis framework for the 90 physical seams is developed separately in [T076](T076-constitutive-mechanics-fatigue-hysteresis-football-seams.md). T075 supplies the geometric and panel/interface setting; T076 supplies candidate interface-law classes and the experimental identification gates. Neither record assigns unmeasured parameters to the football.
