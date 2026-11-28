# Unified PSU–RGS–Anti-Twin wormhole construction

**Date:** 2026-11-28  
**Programme status:** integrated construction specification; several interfaces remain open. This document is the common physical/geometric target for T161–T165 and the earlier PSU double-toroid / Einstein–Rosen work. It does not claim that a Q6-derived wormhole solution has already been constructed.

## 0. Unification rule

The Q6 Lorentzian complex, PSU two-sheet geometry, wormhole throat, independent Cartan connection, discrete action, spin lift and Schwarzschild–Kruskal limit are not separate models. They are structures and limits of one candidate geometric system.

The common object is a family
\[
(\mathcal K_h,\pi_h,e_h,\omega_h,\Psi_h;\lambda),
\]
where \(\mathcal K_h\) is an oriented four-dimensional cellular refinement (to be constructed from Q6 data), \(\pi_h\) carries the two PSU–Anti-Twin sheets and throat interface, \(e_h\) is a nondegenerate Lorentzian coframe, \(\omega_h\) is an independent metric-compatible Lorentz connection, and \(\Psi_h\) is a spinor field. The parameter \(\lambda\) controls the inter-sheet/throat sector; its physical normalization remains open.

The continuum target is one Cartan geometry
\[
(\mathcal M=\mathcal M_+\cup\mathcal W\cup\mathcal M_-,e,\omega,\Psi),
\quad T^a=de^a+\omega^a{}_b\wedge e^b,
\quad R^{ab}=d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb}.
\]
Generic Riemann–Cartan geometry permits both \(R\ne0\) and \(T\ne0\). The teleparallel subfamily \(R=0\) is a separate constraint, not the default. Sheet exchange is not torsion.

## 1. Historical geometric seed: retain the toroidal PSU ansatz

The earlier PSU–Anti-Twin work used a toroidal throat, not merely a spherical Morris–Thorne throat. Its reference metric was originally written in signature \((-+++ )\). For consistency with T161 and the Cartan/spin sections, this document uses \((+---)\), i.e. the overall-sign-equivalent form
\[
ds^2=+N(l)^2c^2dt^2-dl^2-r(l)^2d\theta^2-
[R(l)+r(l)\cos\theta]^2d\varphi^2.
\]
with PSU on one side, Anti-Twin on the other, and \(l=0\) the throat. The associated sheet variables were written
\[
g^\pm=g^c\pm g^r,\qquad h^\pm=h^c\pm h^r.
\]
The earlier model also proposed a one-way flux and an external Vesica-Piscis anisotropy triplet. Those are physical hypotheses, not consequences of the metric or of sheet exchange. Flux orientation and its field equation must be derived.

For this toroidal spatial geometry, regularity conditions include
\[
N(l)>0,\quad r(l)>0,\quad R(l)-r(l)>0
\]
on the coordinate patch, together with sufficient smoothness and finite curvature invariants. A reflection-symmetric throat may impose \(r'(0)=R'(0)=N'(0)=0\), with the appropriate flare-out condition determined from the chosen embedding/areal geometry. These conditions must be checked for an actual solution, not imposed as proof of one.

### Explicit toroidal coframe and independent connection

Set \(A(l,\theta)=R(l)+r(l)\cos\theta\). On a regular toroidal chart a concrete orthonormal coframe for signature \((+---)\) is
\[
e^0=N(l)c\,dt,\quad e^1=dl,\quad
e^2=r(l)d\theta,\quad e^3=A(l,\theta)d\varphi.
\]
Its oriented volume density is
\[
e^0\wedge e^1\wedge e^2\wedge e^3
=NcrA\,dt\wedge dl\wedge d\theta\wedge d\varphi.
\]
Thus the coframe is nondegenerate on this chart precisely when \(N>0\), \(r>0\), and \(A>0\); the sufficient toroidal condition \(R-r>0\) guarantees the last inequality for every \(\theta\). At a smooth reflection-symmetric throat \(l=0\), with \(N,r,R\) even and positive, the determinant remains finite and nonzero. This is a local chart statement; the periodic angular coordinates require the usual overlapping charts and are not a physical singularity.

For reference, the torsion-free metric-compatible connection of this coframe has the nonzero mixed components
\[
\omega_{\rm LC}{}^0{}_1=\frac{N'}{N}e^0,\quad
\omega_{\rm LC}{}^2{}_1=\frac{r'}{r}e^2,\quad
\omega_{\rm LC}{}^3{}_1=\frac{\partial_l A}{A}e^3,\quad
\omega_{\rm LC}{}^3{}_2=\frac{\partial_\theta A}{rA}e^3
=-\frac{\sin\theta}{A}e^3,
\]
with the remaining components fixed by metric compatibility. This gives a concrete regular reference connection at the throat: the first three displayed coefficients vanish there for even profiles, while the angular connection is finite wherever \(A>0\).

The independent Cartan connection is then parameterized as
\[
\omega=\omega_{\rm LC}+K,\qquad K_{ab}=-K_{ba},
\]
where \(K\) is an independently varied contortion 1-form. Consequently
\[
T^a=K^a{}_b\wedge e^b,\qquad
R(\omega)=R(\omega_{\rm LC})+D_{\rm LC}K+K\wedge K.
\]
This is the explicit bridge between the toroidal throat coframe and the independent Cartan sector. The Levi-Civita connection here is only a reference decomposition, not the fundamental connection and not a restriction \(K=0\).

### Explicit throat-localized transport candidate

A minimal independent contortion component that produces both a radial throat transport and nonzero torsion is
\[
K^{02}=\kappa(l)e^1=\kappa(l)\,dl,\qquad K^{20}=-K^{02},
\]
with all other independent components set to zero for this test ansatz. With \(\eta=(+---)\),
\[
T^0=-\kappa(l)e^1\wedge e^2,\qquad
T^2=-\kappa(l)e^1\wedge e^0,
\]
up to the fixed orientation convention for the internal generators. Hence a smooth bounded \(\kappa\) gives finite torsion at \(l=0\), while \(\kappa\not\equiv0\) gives a nonzero torsion sector.

Along a radial path \(\gamma:l_-\to l_+\), the displayed diagonal reference coframe has no Levi-Civita connection component proportional to \(dl\). For this one-generator test ansatz the radial transport is therefore
\[
\mathcal P_\gamma=
\exp\!\left[-J_{02}\int_{l_-}^{l_+}\kappa(l)\,dl\right],
\]
where \(J_{02}\) is the Lorentz boost generator in the \(0\)-\(2\) plane. This is an explicit finite throat-transport candidate, not yet a solution of the field equations. Its curvature must be computed from \(R_{\rm LC}+D_{\rm LC}K+K\wedge K\), and its profile must be matched across the PSU/Anti-Twin interface by the actual transition map. A compactly supported smooth \(\kappa\) localizes the relative transport near the throat; the integral controls the net boost. Setting \(\kappa=0\) removes this torsional transport but does not by itself decouple the full two-sheet geometry.

For the two-sheet interface, use this same boost as the candidate transition:
\[
g_{+-}=\exp(-\chi_\Sigma J_{02}),\qquad
g_{-+}=g_{+-}^{-1},\qquad
\chi_\Sigma=\int_{\gamma_\Sigma}\kappa(l)\,dl.
\]
The Anti-Twin operation exchanges the sheet labels; \(g_{+-}\) is the independent Lorentz-frame transport between their fibres. They must not be identified. The coframe and connection traces on the interface are matched by this transition, and the reverse path uses its inverse. This gives a concrete candidate throat gluing map whose parameter is computed from the connection profile rather than chosen independently. The field equations must still determine whether such a profile exists and whether it is compatible with the global two-sheet topology.

The earlier spherical two-ended comparison ansatz
\[
ds^2=+N(u)^2dt^2-du^2-(u^2+r_0^2)d\Omega^2
\]
is a distinct comparison geometry. It has \(R(0)=r_0>0\), \(R'(0)=0\), and a regular local coframe when \(N(0)>0\). It must not silently replace the historically used toroidal throat. Spherical and toroidal branches are separate symmetry sectors of the unified programme.

## 2. Q6 carrier and the genuine 4D-complex gate (T162)

Start with the full six-cube cellular complex, not just its graph:
\[
N_k=\binom 6k2^{6-k},\qquad
(N_0,\ldots,N_6)=(64,192,240,160,60,12,1).
\]
The 64 vertices, 192 edges and 240 square faces are the familiar Q6 data; 160 three-cells and 60 four-cells are the canonical higher incidences. The 4-skeleton is an exact finite cubical subcomplex, but it is not automatically a 4-manifold: a 3-face of the six-cube is incident to three 4-faces, whereas a manifold-like 4-complex requires two local sides at an interior codimension-one face.

Therefore T162 must construct and audit a specific 4D manifold-like refinement/resolution from these incidences, rather than relabel the 4-skeleton as spacetime. It must specify selected 4-cells and attaching maps, local incidence numbers and links, orientation/time-orientation, the two-sheet lift and involution, throat subcomplex and gluing, and a shape-regular refinement family.

The golden cut-and-project data from T129/T161 are retained:
\[
P_\parallel P_\parallel^T=P_\perp P_\perp^T=I_3,\qquad
P_\parallel P_\perp^T=0.
\]
The 3D golden internal window and rhombic triacontahedron remain spatial geometric data. They do not select Lorentzian time. The IVM/FCC six-axis frame and its \(O_h\) symmetry remain distinct from the golden \(I_h\) frame until an explicit decorated equivariant map is supplied.

A Lorentzian coframe is a rank-four map on each 4-cell,
\[
e_h:C_1(\mathcal K_h)\longrightarrow\mathbb R^{1,3},
\qquad g_h=e_h^T\eta e_h,\quad \eta=\operatorname{diag}(1,-1,-1,-1).
\]
It must be assembled from the PSU–Anti-Twin temporal/relative sector and an independently constructed spatial triad. A candidate temporal leg may use the already-recorded conditional identity for future unit timelike sheet vectors \(u_\pm\):
\[
v_0=(u_++u_-)/2,\quad s_{AT}=(u_+-u_-)/2,\quad v_0\cdot s_{AT}=0,
\]
\[
v_0^2=\cosh^2(\chi/2),\quad s_{AT}^2=-\sinh^2(\chi/2).
\]
This identity is exact if the unit-timelike hypothesis holds; deriving that hypothesis from PSU fields is open. At \(\chi=0\), the relative leg vanishes and cannot be normalized. The spatial triad must be constructed in \(e_0^\perp\); it cannot be inferred from the 6D Euclidean split alone.

**T162 status:** higher cubical incidences are exact; a manifold-like Lorentzian refinement, physical time selector, throat gluing and nondegenerate coframe are open.

## 3. One two-sheet Cartan geometry and throat transport

On each sheet use coframes and independent connections \((e_+,\omega_+)\) and \((e_-,\omega_-)\). The Anti-Twin involution \(J_{AT}=\tau_x\) exchanges sheets. Common and relative fields are
\[
e_c=(e_++e_-)/2,\quad e_r=(e_+-e_-)/2.
\]
The relative coframe is not Cartan torsion.

The throat is a shared interface subcomplex \(\Sigma_h\). Its gluing data consist of an invertible transition map \(g_{+-}:\Sigma_h\to SO^+(1,3)\) (or its spin lift), and compatible coframe/connection pullbacks. With a fixed left/right convention, the continuum matching is the usual gauge transformation of the coframe and connection. A nontrivial throat transport is
\[
\mathcal P_\gamma=\mathcal P\exp(-\int_\gamma\omega),
\]
and on the finite complex the ordered product of Lorentz links. The affine edge pair \((L,E)\) uses
\[
(L,E)(K,S)=(LK,E+LS).
\]
The already-proved finite tetrahedral boundary identity and local smooth-sampling Cartan consistency theorem apply to this transport formalism; neither constructs the Q6 throat or proves convergence of its solutions.

The throat regularity audit must check coframe rank in regular charts; bounded components of \(R^{ab}\), \(T^a\), and scalar invariants; invertibility of sheet transition; and finite, well-defined transport across the interface. Coordinate degeneracies (for example spherical polar axes) must be separated from genuine frame degeneracy by using multiple regular charts.

## 4. Independent Cartan action (T163)

Use a first-order Palatini–Cartan action with independent coframe and Lorentz connection:
\[
S[e,\omega,\Psi]=
\frac{1}{4\kappa}\int_{\mathcal M}\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}(\omega)
-\frac{\Lambda}{24\kappa}\int_{\mathcal M}\epsilon_{abcd}e^a\wedge e^b\wedge e^c\wedge e^d
+S_m[e,\omega,\Psi]+S_\Sigma.
\]
The interface term \(S_\Sigma\) must be derived from the chosen variational boundary data; it is not optional when the two sheets are glued and variations are independent on either side.

A discrete candidate on oriented triangular faces is
\[
S_h[e,L]=\frac{1}{4\kappa}\sum_f
\epsilon_{abcd}B_f^{ab}X_f^{cd}
+S_{\Lambda,h}+S_{m,h}+S_{\Sigma,h},
\]
where \(B_f^{ab}\) is the transported coframe area bivector and \(X_f=\log H_f\) is the Lie-algebra curvature coordinate for face holonomy \(H_f\). This is a local small-h branch of the logarithm; branch choices and large holonomies must be handled explicitly. The exact discretization of cosmological, matter and interface terms remains to be fixed.

Variations are independent:
\[
\delta_eS_h=0,\qquad \delta_LS_h=0.
\]
The connection variation must use the Fréchet derivative of the matrix logarithm (or an equivalent group-valued variational formula); replacing \(\delta\log H\) by \(H^{-1}\delta H\) is not valid in general for noncommuting matrices. The variation has the exact structural form
\[
\delta_eS_h=\frac{1}{4\kappa}\sum_f
\epsilon_{abcd}\,(\delta_e B_f^{ab})X_f^{cd}
+\delta_e(S_{\Lambda,h}+S_{m,h}+S_{\Sigma,h}),
\]
\[
\delta_LS_h=\frac{1}{4\kappa}\sum_f\epsilon_{abcd}
\left[(\delta_LB_f^{ab})X_f^{cd}
+B_f^{ab}\,\mathrm D(\log)_{H_f}[\delta H_f]^{cd}\right]
+\delta_L(S_{m,h}+S_{\Sigma,h}).
\]
Here \(\mathrm D(\log)_{H_f}\) is the Fréchet derivative of the matrix logarithm on the selected local branch. If \(H_f=L_1\cdots L_m\), then
\[
\delta H_f=\sum_{j=1}^m
L_1\cdots L_{j-1}(\delta L_j)L_{j+1}\cdots L_m.
\]
These expressions make the two independent variations explicit; the discrete Euler–Lagrange residuals are obtained by collecting the coefficients of each independent \(\delta e\) and each Lie-algebra variation \(\delta L\,L^{-1}\). The face transports entering \(B_f\) must also be varied in the connection equation.

For comparison, the continuum Palatini–Cartan variation (before adding matter and boundary terms) is
\[
\delta_eS_{\rm PC}=\frac{1}{2\kappa}\int
\epsilon_{abcd}\,\delta e^a\wedge e^b\wedge R^{cd},
\]
\[
\delta_\omega S_{\rm PC}=
-\frac{1}{2\kappa}\int
\epsilon_{abcd}\,T^a\wedge e^b\wedge\delta\omega^{cd}
+\text{boundary term},
\]
using \(D(e^a\wedge e^b)=T^a\wedge e^b-e^a\wedge T^b\). This verifies why the connection variation imposes the torsion equation in vacuum and why a spin-current source changes it. It also identifies the interface contribution that must be cancelled or retained by the chosen throat boundary action.

The resulting discrete Euler–Lagrange equations, gauge identities, constraints and boundary matching equations must be derived from the same action.

In the smooth limit the vacuum equations target
\[
\epsilon_{abcd}e^b\wedge R^{cd}=0,\qquad
\epsilon_{abcd}T^a\wedge e^b=0
\]
for nondegenerate coframe and no spin source. With spin matter, the connection equation has a spin-current source and torsion need not vanish. This is the Einstein–Cartan/Palatini branch; imposing \(R=0\) gives a separate teleparallel branch.

**T163 status:** continuum action is standard; the discrete action is a candidate. Its full independent variations, interface term, constraints and discrete equations remain to be derived and tested.

## 5. Traversability and energy conditions (part of T164)

For a static candidate metric, traversability requires more than a nonzero throat radius. Audit no horizon on the traversed branch (positive lapse in a regular static chart); a positive, nondegenerate spatial throat cross-section; finite proper travel time and tidal components for admissible observers; regular curvature and torsion in a freely falling frame; and a causal, globally specified throat gluing without closed timelike curves.

For a toroidal throat, verify that \(R(l)+r(l)\cos\theta\) stays positive and use the toroidal symmetry/embedding data rather than importing spherical flare-out formulas unchanged.

Energy conditions must be evaluated from the stress tensor obtained by varying the same action. In Einstein–Cartan theory distinguish material stress tensor, spin current, torsion-induced effective terms and the effective source in the metric equation. The earlier candidate expression
\[
\rho+p_l=-\frac{\ell^2}{4\pi G(\ell^2+l^2)^2}
\]
was recorded for a particular prior wormhole ansatz; it is not a theorem for the present toroidal model and must be re-derived with its own conventions before use. A claim that PSU–Anti-Twin removes the null-energy-condition obstruction requires an explicit solution and an independently defined effective stress tensor.

The proposed one-way PSU-to-Anti-Twin flux is likewise a hypothesis. A conserved current obeys a balance law on the two-sheet complex; asymmetric flux requires a source, boundary condition, non-time-reversal-invariant dynamics or another derived mechanism. It does not follow from \(J_{AT}\) alone.

## 6. Schwarzschild–Kruskal / Einstein–Rosen limit (part of T164)

The same solution family must include a controlled decoupling limit of the throat/inter-sheet coupling. Denote its parameter by \(\lambda\), but do not assume that setting \(\lambda=0\) automatically gives Schwarzschild: prove the limiting field equations and convergence.

The target vacuum exterior is
\[
ds^2=\left(1-\frac{2GM}{rc^2}\right)c^2dt^2
-\left(1-\frac{2GM}{rc^2}\right)^{-1}dr^2-r^2d\Omega^2
\]
for signature \((+---)\), with
\[
R_{\mu\nu}=0,\qquad
K=R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=\frac{48G^2M^2}{c^4r^6}.
\]
The static tetrad is not regular at the horizon. The limit must be expressed in a regular Kruskal chart (or another horizon-regular chart) and a regular tetrad. The maximally extended Schwarzschild geometry contains two exterior regions and an Einstein–Rosen bridge on the time-symmetric slice, but that bridge is not traversable. The programme must not identify this limit with the traversable PSU throat.

The limiting audit includes metric convergence away from the horizon, regular-chart convergence across the horizon, curvature invariants, causal structure and limiting inter-sheet transport. The result may be a degeneration to a non-traversable Einstein–Rosen bridge or to disconnected exteriors; which occurs is determined by the actual family and must not be stipulated.

## 7. Spinorial lift and Dirac limit (T165)

After T162 supplies an oriented, time-oriented Lorentzian four-complex and a nondegenerate coframe, lift its frame transitions:
\[
SO^+(1,3)\leftarrow Spin^+(1,3)\simeq SL(2,\mathbb C).
\]
The local spinor bundle has rank four complex, with
\[
\{\gamma^a,\gamma^b\}=2\eta^{ab}I_4,\quad
\mathcal D_\mu=\partial_\mu+\frac14\omega_{\mu ab}\gamma^{ab},\quad
\slashed D=i\gamma^ae_a{}^\mu\mathcal D_\mu.
\]
The two-sheet field is \(\Psi=(\Psi_+,\Psi_-)\), with T148 sheet/chiral locking imposed only as a separately specified representation constraint. Spin transport through the throat is the spin lift of the same Lorentz holonomy used for vector transport; it is not an independent fitted link.

The bare Q6 Clifford operator from T149 has the exact obstruction \(D_{Q6}^2=-3I/2\); it is not a massless continuum Dirac operator. A new refinement-dependent operator is required. Its audit includes locality, consistency with coframe and connection, spectral/resolvent convergence on a specified Hilbert embedding, fermion doubling, chirality and anomalies, and the throat matching condition for spinors.

**T165 status:** the target Spin+(1,3) operator is fixed; the Q6 spin structure, discrete operator and continuum limit remain open.

## 8. Convergence of solutions (T164, not merely local consistency)

The previously proved Cartan refinement theorem establishes local smooth-sampling consistency:
\[
\log H_f=\tfrac12h^2R_p(u,v)+O(h^3),\qquad
\tau_f=\tfrac12h^2T_p(u,v)+O(h^3).
\]
The manufactured RK4 audit is numerical evidence for one smooth noncommuting connection with nonzero curvature and torsion. Neither result proves convergence of discrete critical points.

Solution convergence needs a shape-regular Q6-derived four-dimensional refinement family; gauge fixing and uniform bounds for coframes, connections and matter fields; coercivity/energy estimates or an appropriate hyperbolic stability estimate; compactness modulo gauge and preservation of nondegeneracy/causality; consistency of the complete discrete action including the throat term; identification of subsequential limits as weak solutions; and uniqueness or a selection principle if full-sequence convergence is claimed.

Mosco convergence for positive elliptic/Hodge sectors is reusable for those sectors only; it does not by itself establish convergence of an indefinite Lorentzian gravitational action or its hyperbolic critical points.

## 9. One construction's theorem/dependency map

\[
\text{Q6 incidences + two-sheet lift}
\to \text{4D refinement and throat}
\to (e_h,\omega_h)
\to S_h[e_h,\omega_h,\Psi_h]
\to \text{discrete field equations}
\to \text{solution convergence}
\to \text{Spin}^+(1,3)\text{ Dirac limit}.
\]
Wormhole regularity, traversability, energy conditions and Schwarzschild–Kruskal degeneration are not side projects: they are geometric and physical tests on the same family between the coframe/connection construction and its continuum limit.

Reuse without changing their status: T129/T146/T147/T148/T149/T161; the exact affine tetrahedral boundary identity; the local Cartan smooth-sampling consistency theorem; companion finite affine Cartan tests; earlier PSU double-toroid and ER/Kruskal comparison records. Do not silently promote a candidate, numerical audit or physical hypothesis to a theorem.

## 10. Immediate falsifiable milestones

- **M1 — incidence:** export complete Q6 cubical boundary maps and construct the proposed 4D resolution; publish all local links and incidence histograms.
- **M2 — throat:** define the two-sheet gluing map and a nondegenerate coframe on every throat-adjacent 4-cell; report minimum singular value and signature counts.
- **M3 — Cartan:** implement independent Lorentz links and coframe variables; verify local gauge covariance and independent curvature/torsion observables.
- **M4 — variation:** derive analytic gradients of the same discrete action with respect to coframe and links; compare with finite differences on small complexes.
- **M5 — physical limits:** solve a manufactured traversable-throat case and a Schwarzschild/Kruskal limiting case; check invariants and freely falling regularity.
- **M6 — spin:** construct the spin lift of exact vector links and test spinor throat matching and spectral scaling.
- **M7 — convergence:** establish uniform estimates and a solution-convergence theorem only after M1–M6 provide the required hypotheses.

**No physical wormhole solution, Q6-derived Lorentzian manifold, complete discrete action variation, discrete-solution convergence theorem or massless spinorial limit is claimed by this specification.**
