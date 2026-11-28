# RGS–Q6–Anti-Twin: vierbein, tetrad, spin connection, Tesla rotating fields and coupled field sectors

**Date:** 27 November 2026  
**Status:** formal integration dossier; established geometry, archived finite constructions, standard field equations and RGS hypotheses are explicitly separated.  
**Order:** spatial RGS coframe → genuine 4D coframe and connection → Maxwell/QHD/Tesla dynamics → quaternionic spin lift and Anti-Twin bundle → 6D physical/internal split → 3D cut-and-project.

## 0. Objective and evidence separation

## 0.1 Recovered 4D–6D–3D and Cartan/teleparallel synthesis

The consolidated dependency map, including the 21 October 188D→6D embedding, the golden (3+3) split, the projected-cube rhombic-triacontahedral window, the torsion-coupled internal-time candidate, and the general Cartan/teleparallel connection distinction, is recorded in [RGS 4D–6D–3D geometry: recovered embedding, Cartan connection and teleparallel correspondence](RGS_4D6D3D_RC_TELEPARALLEL_CUT_PROJECT_SYNTHESIS_2026-11-27.md). This synthesis reuses T063, T115, T154, T113-G, T129 and S.9; it does not promote the internal temporal axis to physical time or claim a completed continuum theory.



The tetrad is not an accessory to the Anti-Twin connection. It is the soldering field identifying the internal Lorentz frame with spacetime tangent directions. The programme must start from a 4D coframe and connection, then express electromagnetic fields, fluid currents and spinorial transport in that local frame.

The repository already contains distinct objects:
1. 64 site-dependent spatial covariance frames \(E_v\in GL^+(3,\mathbb R)\);
2. the static lift \(e^A{}_\mu(v)=\mathrm{diag}(1,E_v)\), signature \((-+++)\);
3. an analytic Ellis four-dimensional coframe and first jet;
4. archived Q6 edge transports and an edge-coframe/face-path-sum construction;
5. the 188-dimensional constraint tangent space, which is not a spacetime coordinate chart.

The static lift and analytic Ellis chart are benchmarks, not yet a time-dependent spacetime tetrad derived from the Q6 seed.

## 1. Four-dimensional coframe and tetrad postulate

Let \(M\) be an oriented, time-oriented four-manifold with coordinates \(x^\mu=(t,x^1,x^2,x^3)\). A coframe is a nondegenerate matrix field
\[
e^A=e^A{}_\mu dx^\mu,\qquad \det(e^A{}_\mu)\ne0,
\]
with inverse frame \(e_A=e_A{}^\mu\partial_\mu\). Capital Latin indices are orthonormal-frame indices and Greek indices are coordinate indices. Fix
\[
\eta_{AB}=\operatorname{diag}(-1,1,1,1),\qquad
g_{\mu\nu}=\eta_{AB}e^A{}_\mu e^B{}_\nu.
\]
Then \(e_A{}^\mu e^A{}_\nu=\delta^\mu_\nu\), \(e_A{}^\mu e^B{}_\mu=\delta_A^B\), and \(|e|=\sqrt{-g}\).

The Lorentz connection is an independent \(\mathfrak{so}(1,3)\)-valued one-form
\[
\omega^A{}_B=\omega^A{}_{B\mu}dx^\mu,\qquad \omega_{AB}=-\omega_{BA}.
\]
The tetrad postulate reads
\[
\partial_\mu e^A{}_\nu+\omega^A{}_{B\mu}e^B{}_\nu
-\Gamma^\rho{}_{\mu\nu}e^A{}_\rho=0.
\]
It relates the coordinate affine connection and frame connection; it is not itself a field equation.

Cartan's structure equations define
\[
\boxed{T^A=De^A=de^A+\omega^A{}_B\wedge e^B,}
\qquad
\boxed{R^A{}_B=d\omega^A{}_B+\omega^A{}_C\wedge\omega^C{}_B.}
\]
The Bianchi identities are
\[
DT^A=R^A{}_B\wedge e^B,\qquad DR^A{}_B=0.
\]
These are geometric identities for the selected connection. They do not imply that torsion is nonzero.

### 1.1 Three connection choices — do not mix them

**Levi–Civita / GR:** for a given coframe and metric, the metric-compatible torsion-free connection is fixed by \(T^A=0\); curvature is generally nonzero.

**Einstein–Cartan–Sciama–Kibble (ECSK):** coframe and Lorentz connection are varied independently in a first-order action. In minimal ECSK, torsion is sourced algebraically by spin density. It is not inferred from nonorientability or a rotating magnetic field.

**Teleparallel equivalent GR (TEGR):** the teleparallel connection is constrained to be flat, \(R^A{}_B(\omega)=0\), while torsion is generally nonzero. The TEGR torsion scalar and Levi–Civita Ricci scalar differ by a total divergence (sign depends on convention). A covariant tetrad formulation requires the inertial spin connection.

Metric-affine extensions add nonmetricity \(Q_{AB}=-D\eta_{AB}\); it vanishes in the metric-compatible Lorentz sector assumed here. ECSK and TEGR are alternative connection branches, not ingredients to blend without defining a new theory.

## 2. Genuine 3+1 tetrad extension of the RGS spatial coframe

Let \(E^a{}_i(t,x)\) be a spatial triad, \(N(t,x)>0\) the lapse and \(N^i(t,x)\) the shift. In time gauge choose
\[
\boxed{e^0=N\,dt,\qquad e^a=E^a{}_i(dx^i+N^i dt).}
\]
Then
\[
ds^2=-N^2dt^2+h_{ij}(dx^i+N^i dt)(dx^j+N^jdt),
\quad h_{ij}=\delta_{ab}E^a{}_iE^b{}_j.
\]
This is the extension template for the archived spatial coframe. The fields \(N,N^i,E^a{}_i\) must be functions on a declared chart or mesh/refinement family. Setting \(N=1,N^i=0\) and taking \(E_i\) static recovers only the existing static lift; it does not solve dynamical field equations.

The spatial spin connection \(\omega^{ab}\) and boost components \(\omega^{0a}\) are fixed by the selected gravity theory and constraints. In time gauge the residual local frame rotations are \(SO(3)\), whose spin lift is \(SU(2)\). A full Lorentzian spin connection uses \(\mathrm{Spin}(1,3)\simeq SL(2,\mathbb C)\), not merely unit quaternions.

## 3. Exact repository evidence and the missing operation

Reuse:
- *research/COMPANION_RGS_GEC6_VIERBEIN_CROSSWALK_2026-11-27.md*: companion PR #234, deterministic 64-site spatial coframe reconstruction and static 3+1 lift.
- *docs/RGS_COFRAME_SPIN_CONNECTION_RECOVERED_IMPLEMENTATIONS_2026-11-27.md*: distinction among 64 covariance frames, static lift and analytic Ellis chart; general coframe-first-jet Levi–Civita kernel and analytic Ellis implementation, with machine-precision residuals on that analytic chart.
- *theorems/T115-rgs-curved-clifford-coframe-identity.md*: pointwise curved Clifford anticommutator for an invertible static tetrad.
- *theorems/T154-rgs-spatial-coframe-constraint-splitting.md*: exact \(3+1\) split of the constraint-normal space. Its fourth direction is a radial scalar constraint, **not physical time**.
- *docs/Q6_ARCHIVED_CARRIER_COFRAME_2026-11-27.md*: spatial edge coframe on 192 archived links and transported path sums on 240 squares; continuum Cartan interpretation remains open.

The missing operation is a reproducible map
\[
(X_v,E_v,U_{vw})\longrightarrow
(N,N^i,E^a{}_i)(t,x),\ \omega^{AB}{}_\mu(t,x)
\]
with: (i) a declared atlas/mesh; (ii) gauge-fixed interpolation of spatial triads; (iii) time coordinate and temporal transport; (iv) a first jet or convergent discrete substitute; (v) connection from the tetrad postulate or variational principle; (vi) gauge-covariant comparison with archived \(SO(3)\)/\(SU(2)\) links. Until then, the Ellis chart is an analytic benchmark and Q6 links are discrete connection data; equality of their holonomies is not established.

## 4. Maxwell field in the tetrad frame

Let \(A\) be a \(U(1)\) connection and \(F=dA=\frac12F_{\mu\nu}dx^\mu\wedge dx^\nu\). The homogeneous equation \(dF=0\) and sourced equation \(d\star F=\star J\) (unit conventions suppressed) are independent of whether the gravitational connection has torsion, when electromagnetism is minimally coupled through \(F=dA\).

Local components are
\[
F_{AB}=e_A{}^\mu e_B{}^\nu F_{\mu\nu},\quad
E_a=F_{a0},\quad B_a=\tfrac12\epsilon_a{}^{bc}F_{bc}
\]
(up to sign/orientation convention). The Hodge star is built from \(g\) and orientation, hence from the tetrad. In SI-like normalization,
\[
T^{EM}_{\mu\nu}=\frac1{\mu_0}
\left(F_{\mu\alpha}F_\nu{}^\alpha-\tfrac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right),
\quad T^{EM}_{AB}=e_A{}^\mu e_B{}^\nu T_{\mu\nu}.
\]
The potential \(A\), Lorentz spin connection \(\omega\), and Anti-Twin connection are different bundles. Maxwell theory does not acquire a torsion term merely by replacing \(dA\) with an affine covariant derivative.

## 5. Tesla rotating fields in a moving tetrad

Tesla's 1888 polyphase patents describe phase-displaced alternating currents and progressive rotation of magnetic poles/resultant field. The geometric object to import is the time-dependent spatial field vector, not a new gravity law.

In a local orthonormal spatial frame \((e_1,e_2,e_3)\), the ideal circular rotating-field benchmark is
\[
\boxed{\mathbf B_{\rm rot}(t)=B_0(\cos\omega t\,e_1+\sin\omega t\,e_2).}
\]
Its magnitude is constant and angular velocity is \(\omega e_3\). Reversing phase sequence reverses rotation. If amplitudes or phase quadrature are unbalanced, the field tip generally traces an ellipse.

For three stator axes \(n_k=(\cos\alpha_k,\sin\alpha_k)\), \(\alpha_k=2\pi k/3\), and currents \(i_k=I\cos(\omega t-\alpha_k)\), equal winding coefficients give
\[
\mathbf H(t)=\frac{3cI}{2}(\cos\omega t\,e_1+\sin\omega t\,e_2).
\]
This balanced idealization is already recorded in S009; actual machines also depend on winding distribution, geometry, material response and boundary conditions.

### 5.1 Covariant angular velocity

When the tetrad rotates, the derivative of frame components is not the physical derivative. For a spatial vector \(B^a\),
\[
(D_tB)^a=\partial_tB^a+\omega^a{}_{bt}B^b.
\]
Thus a rotating magnetic field can be described by time-varying components in a fixed inertial frame or constant components in a co-rotating frame with nonzero connection. The two descriptions are related by a local \(SO(3)\) gauge transformation. This is the precise Tesla–tetrad bridge.

Fortescue's positive/negative/zero sequence decomposition supplies the circuit-side modal split. Positive and negative sequences reverse the direction of the rotating resultant in the balanced idealization. A phase-sequence label is **not** automatically the Anti-Twin sheet label: an explicit intertwiner between the \(C_3\) sequence action and sheet exchange is required before identifying them.

## 6. Quantum hydrodynamics in the tetrad frame

For a charged scalar \(\psi=\sqrt n\,e^{iS/\hbar}\), define
\[
D_\mu\psi=(\partial_\mu-iqA_\mu/\hbar)\psi,\qquad
u_\mu=\frac1m(\partial_\mu S-qA_\mu).
\]
The nonrelativistic Madelung equations follow from minimally coupled Schrödinger dynamics away from nodes:
\[
\partial_t n+\nabla\cdot(n\mathbf u)=0,
\]
\[
m(\partial_t+\mathbf u\cdot\nabla)\mathbf u
=q(\mathbf E+\mathbf u\times\mathbf B)-\nabla V-\nabla Q,\quad
Q=-\frac{\hbar^2}{2m}\frac{\nabla^2\sqrt n}{\sqrt n}.
\]
In curved spacetime/non-inertial tetrads, derivatives and volume measure must be adapted to the declared metric and observer frame, and additional terms must be derived from the chosen action. A Pauli/Takabayasi spin fluid has additional spin density, magnetization and spin-gradient terms; it is not scalar Madelung theory.

The tetrad converts current \(J^\mu\) to \(J^A=e^A{}_\mu J^\mu\). Maxwell is sourced by this current; the Lorentz force acts back on matter. The two-sheet state \(\Psi=(\psi_+,\psi_-)^T\) decomposes into exchange-even/odd components only when the full matter/gauge action commutes with Anti-Twin exchange \(S\).

## 7. Quaternionic lift and Anti-Twin connection

In time gauge the spatial rotational spin connection is \(\mathfrak{su}(2)\)-valued and can be represented by imaginary quaternions. For unit \(q\), \(v\mapsto qvq^{-1}\) gives \(SU(2)\to SO(3)\) with kernel \(\{\pm1\}\), reusing T063.

The full Lorentz spin connection acts in \(\mathrm{Spin}(1,3)\simeq SL(2,\mathbb C)\). Quaternionic \(SU(2)\) is a spatial/time-gauge reduction, not a complete Lorentzian spin representation.

For a matter doublet a factorized covariant derivative is
\[
\mathscr D_\mu=
\partial_\mu+\tfrac14\omega_{\mu AB}\gamma^{AB}
-\frac{iq}{\hbar}A_\mu I+\mathcal A^{AT}_\mu,
\qquad \mathcal A^{AT}_\mu=a_\mu I+b_\mu S.
\]
An additional internal \(SU(2)\) acting on another factor must be added separately. Representations and tensor factors must be declared before multiplying matrices. Exchange symmetry is exact when \([\mathscr D_\mu,S]=0\); otherwise the commutator measures sheet mixing.

## 8. Variational architecture

A candidate unified action is
\[
S[e,\omega,A,\Psi_+,\Psi_-,\ldots]
=S_{\rm grav}[e,\omega]+S_{\rm EM}[e,A]
+S_{\rm QHD/Dirac}[e,\omega,A,\Psi]
+S_{\rm AT}[e,\omega,A,\Psi_+,\Psi_-]+S_{\rm medium}.
\]
The choice of \(S_{\rm grav}\) selects GR/Palatini, ECSK or TEGR (or a precisely specified extension). Variation with respect to \(A\) yields Maxwell's sourced equation/current; \(\Psi_\pm\) yields matter equations; \(e^A\) yields energy-momentum response; \(\omega^{AB}\) yields spin-current/connection equations in ECSK or constrained equations in TEGR; Anti-Twin fields yield sheet-exchange equations.

A coupling among torsion, vorticity, magnetic field, density gradient and sheet exchange is allowed only if it follows from the action, symmetries and dimensions, or is explicitly phenomenological and tested. Vorticity, electromagnetic \(F\), Cartan torsion \(T^A\) and curvature \(R^A{}_B\) remain different tensors.

## 9. Formal statements and proof status

**Lemma 1 — Metric reconstruction.** Every invertible coframe defines \(g_{\mu\nu}=\eta_{AB}e^A{}_\mu e^B{}_\nu\) and its inverse.  
**Status:** exact algebra; RGS static Clifford consequence is T115.

**Lemma 2 — Cartan identities.** For any Lorentz connection, (T^A=de^A+\omega^A{}_B\wedge e^B), (R^A{}_B=d\omega^A{}_B+\omega^A{}_C\wedge\omega^C{}_B), and the Bianchi identities are (DT^A=R^A{}_B\wedge e^B), (DR^A{}_B=0).  
**Status:** standard differential-geometric identities; not yet audited on Q6 mesh.

**Proposition 3 — Maxwell Bianchi preservation.** If discrete potential is a 1-cochain \(a\), \(f=\delta a\), and temporal cochain transport commutes with \(\delta\), then \(\delta f=0\) is preserved.  
**Status:** exact cochain identity; metric-dependent discrete Hodge star and sourced equation remain implementation tasks.

**Proposition 4 — Tesla field covariance.** Under local spatial frame rotation \(R(t)\), vector components transform as \(B'=RB\) and spin connection transforms so \(D_tB\) is covariant.  
**Status:** standard gauge-covariance identity. Balanced three-phase field formula is already in S009; machine-specific constitutive response remains conditional.

**Main candidate — RGS spacetime tetrad compatibility.** Given a nondegenerate 4D coframe, declared Lorentz connection, compatible Q6 refinement/transport family, U(1) links and Anti-Twin matter representation, if discrete transports intertwine cellular boundary, commute with sheet exchange and transform covariantly under local frame/gauge transformations, then induced cochain constraints and homogeneous Maxwell identity are preserved. If a consistent stable refinement limit is additionally proved, discrete fields may converge to the declared continuum variational equations.

**Status:** finite chain/Hodge/Anti-Twin algebra is audited in PR #585; T063 and T115 are proved within their hypotheses; S009 supplies exact rotating-field identities. The actual RGS dynamical 4D coframe, Q6 first jet, continuum holonomy comparison, common coupled action and convergence remain **open**.

## 10. Literature map — core authors and contributions

This is a working core bibliography, not a claim to enumerate every publication.

**Frames, coframes, tetrads and spin geometry:** Ricci & Levi-Civita (absolute differential calculus and parallel transport); Élie Cartan (moving frames, exterior forms, torsion and curvature); Einstein (1928) and Hermann Weyl (1929) (tetrad/vierbein and spinorial local-frame formulations); Sciama, Kibble, Hehl, Obukhov and Trautman (gauge gravity, ECSK, spin sources and conservation); Dirac and Weyl (spinors and Clifford representations).

**Teleparallel branch:** Weitzenböck, Møller, Hayashi & Shirafuji, Maluf, Aldrovandi & Pereira, Krššák & Pereira (tetrad/flat-spin-connection formulation, inertial spin connection, torsion scalar and TEGR equivalence).

**Maxwell and discrete geometry:** Faraday, Maxwell and Minkowski (electromagnetic field equations and 4D formulation); Hehl & Obukhov (premetric Maxwell and constitutive tensor); Bossavit, Desbrun, Hirani, Marsden and Stern (discrete differential forms, incidence and metric-dependent Hodge operators).

**Quantum hydrodynamics and spin fluids:** Madelung (Schrödinger hydrodynamic rewriting); Bohm (quantum potential); Takabayasi (spin-fluid representation); Gross & Pitaevskii (condensate mean-field hydrodynamics, distinct from single-particle Madelung).

**Rotating fields and polyphase systems:** Ferraris (rotating-field induction-motor principle); Nikola Tesla (US patents 381,968 and 382,281, 1888; 433,700, 1890; 455,067, 1891); C. L. Fortescue (1918 symmetrical components); Clarke and Park (reference-frame transforms for machine/control dynamics, distinct from Fortescue sequence decomposition).

### Core sources
1. Tecchiolli, *On the Mathematics of Coframe Formalism and Einstein–Cartan Theory*, Universe 5 (2019), 206, DOI 10.3390/universe5100206.
2. Hehl & Obukhov, *Élie Cartan's torsion in geometry and in field theory* (2007); Trautman, *Recent Advances in the Einstein–Cartan Theory of Gravity*.
3. Maluf, *The teleparallel equivalent of general relativity*, Annalen der Physik 525 (2013), DOI 10.1002/andp.201200272.
4. Krššák & Pereira, *Spin connection and renormalization of teleparallel action*, EPJC 75 (2015), 519; Aldrovandi & Pereira, *Teleparallel Gravity: An Introduction* (2013).
5. Hehl & Obukhov, *Foundations of Classical Electrodynamics* and premetric Maxwell work.
6. Takabayasi, *The Vector Representation of Spinning Particle in the Quantum Theory*, Prog. Theor. Phys. 14 (1955), 283–302, DOI 10.1143/PTP.14.283.
7. Tesla, US Patents 381,968 and 382,281 (1888), 433,700 (1890), 455,067 (1891).
8. Fortescue, *Method of Symmetrical Co-Ordinates Applied to the Solution of Polyphase Networks* (1918), DOI 10.1109/T-AIEE.1918.4765570.
9. *Differential Forms in Lattice Field Theories: An Overview* (2013), DOI 10.1155/2013/487270.

## 11. Executed coframe/connection audit (27 November 2026)

The follow-up implementation and measured result are recorded in [RGS–Q6 static coframe and Levi-Civita link audit](RGS_Q6_STATIC_COFRAME_LC_LINK_AUDIT_2026-11-27.md), with machine-readable report [RGS_Q6_STATIC_COFRAME_LC_LINK_AUDIT.json](../audits/RGS_Q6_STATIC_COFRAME_LC_LINK_AUDIT.json). CI run #25 succeeded. It reconstructs the 64 spatial coframes, builds an SPD-preserving log-Gaussian interpolation, computes its Levi-Civita connection and compares all 192 edge transports and 240 face holonomies with the Q6 minimal-radial-rotation links. The mismatch is measured, not fitted away. It also checks a time-dependent co-rotating tetrad gauge, the Tesla positive/negative sequence rates, temporal Cartan torsion cancellation and the quaternionic SU(2) double-cover behaviour. This closes the **static interpolation/connection audit gate only**; the dynamical 4D tetrad and common field action remain open.

## 12. Repository dependencies and next construction

Preserve and reuse:
- docs/RGS_COFRAME_SPIN_CONNECTION_RECOVERED_IMPLEMENTATIONS_2026-11-27.md
- docs/Q6_ARCHIVED_CARRIER_COFRAME_2026-11-27.md
- research/COMPANION_RGS_GEC6_VIERBEIN_CROSSWALK_2026-11-27.md
- theorems/T115-rgs-curved-clifford-coframe-identity.md
- theorems/T154-rgs-spatial-coframe-constraint-splitting.md
- theorems/S009-three-phase-ferraris-coframe-tetrad-bridge.md
- theorems/S011-fdt-density-cone-riemann-cartan-kathara-maxwell.md
- theorems/T063-quaternion-su2-so3-double-cover.md
- research/RGS_Q6_ANTITWIN_QHD_MAXWELL_QUATERNION_FORMALIZATION_2026-11-27.md

Immediate implementation gates:
1. Recover exact 64 spatial \(E_v\), frame gauge and analytic Ellis first-jet benchmark.
2. Define mesh/atlas interpolation \(E^a{}_i(t,x)\), lapse \(N\) and shift \(N^i\); do not infer physical time from T154's radial scalar.
3. Compute \(\omega^{AB}{}_\mu\) from the tetrad postulate for the Levi–Civita benchmark; implement ECSK or TEGR only after choosing the branch.
4. Compare continuum edge holonomies against archived Q6 \(SO(3)\)/\(SU(2)\) links with path and gauge conventions fixed.
5. Express Tesla positive/negative rotating fields in the local triad and verify the covariant derivative under a co-rotating frame transformation.
6. Express Maxwell \(F_{AB}\), QHD \(J^A\), spin current and Anti-Twin doublet in the same frame; derive common action variations.
7. Only when 4D geometry and field couplings are fixed, return to canonical 6D split and 3D cut-and-project.

**No new theorem number is assigned here.** T115, T154, S009, S011 and T063 remain canonical for their own claims; global spacetime tetrad compatibility remains a candidate/open theorem.


## Discrete Cartan layer from the I Ching/Kirchhoff carrier

The executable finite spatial construction is documented in [Q6 discrete Cartan torsion and curvature audit](Q6_DISCRETE_CARTAN_TORSION_CURVATURE_AUDIT_2026-11-27.md). It starts from the 64 six-bit hexagrams, 192 single-line-flip edges and 240 square faces. Edge coframe increments and SO(3) link transports define a gauge-covariant developed torsion on each face and an ordered curvature holonomy. Both are simultaneously nonzero on 236 of 240 faces for the declared finite data. This is a spatial discrete candidate, not yet the 4D Lorentzian or teleparallel field solution.
