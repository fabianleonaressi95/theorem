# Three defect gases and the QLG–RGS–N=4 SYM–IIB bridge

**Date:** 12 November 2026  
**Status:** research specification; exact lattice identities are separated from RG approximations, finite-size estimators, and open physical identifications.  
**Dependencies:** T102, T104, T107, T110; `docs/KTHNY_N4_SYM_RGS_PRISM.md`; the integrated 27-chapter monograph.

## 0. Scope and non-identification rule

This dossier develops three calculations that must remain distinct:

1. **2D XY/BKT:** integer scalar point-vortex charges and the renormalization of phase stiffness.
2. **3D XY:** divergence-free integer vortex flux on dual links, closed loop networks, and their length statistics.
3. **2D crystal/KTHNY:** vector Burgers charges of dislocations and rotational Frank charges of disclinations, coupled to elastic fields.

They are not interchangeable defect gases. In particular, a 3D XY vortex loop is not a KTHNY dislocation, and neither is automatically a Q6 hexagram charge or a Wilson–'t Hooft charge.

The aim is to define reproducible calculations and interfaces. No critical temperature, exponent, material transition, QLG continuum limit, or QLG-to-string duality is claimed before the corresponding test or derivation is completed.

---

## I. Calculation A — 2D XY/BKT: stiffness flow and vortex fugacity

### A1. Microscopic and topological variables

On a periodic square lattice, let \(\theta_x\in(-\pi,\pi]\) and
\[
H=-J\sum_{x,\mu=1,2}\cos(\theta_{x+\hat\mu}-\theta_x).
\]
For each oriented link define
\[
a_\mu(x)=\operatorname{wrap}_{(-\pi,\pi]}(\theta_{x+\hat\mu}-\theta_x),
\]
and for each plaquette
\[
q_p=\frac1{2\pi}\sum_{\partial p}a\in\mathbb Z.
\]
Periodicity gives the exact neutrality constraint \(\sum_pq_p=0\). This is conservation of total signed charge, not conservation of the number of vortices: local vortex–antivortex pairs can be created and annihilated.

The harmonic winding sector is measured separately on noncontractible cycles. In configurations with vortices, winding on parallel cuts need not agree; report cut-resolved winding rather than one unqualified global integer.

### A2. Coulomb-gas reduction and RG variables

In the dilute-vortex, long-distance regime, the continuum Coulomb-gas description has integer charges \(q_i\), neutrality \(\sum_iq_i=0\), a logarithmic pair interaction, and a core fugacity. Use the dimensionless stiffness
\[
K=\frac{\Upsilon}{k_BT}
\]
and a declared dimensionless unit-vortex fugacity \(y\) (the numerical coefficient in its definition fixes the convention of the RG equations).

In the standard dilute-gas normalization, the leading Kosterlitz recursion relations are
\[
\frac{dK^{-1}}{d\ell}=4\pi^3y^2+O(y^4),
\qquad
\frac{dy}{d\ell}=(2-\pi K)y+O(y^3).
\]
These are asymptotic RG equations near the dilute-vortex regime, not exact finite-lattice identities. The BKT separatrix terminates at
\[
K_R=\frac{2}{\pi},
\qquad
\frac{\Upsilon_R}{k_BT}=\frac2\pi.
\]
The subscript \(R\) is essential: the criterion concerns the long-distance renormalized stiffness, not the bare \(J/(k_BT)\).

### A3. Numerical estimator and finite-size protocol

For each size \(L\), temperature/inverse-temperature point, and independent seed:

1. equilibrate with a declared update protocol and monitor energy, acceptance, vortex density, and winding-sector tunnelling;
2. estimate the directional helicity modulus
\[
\Upsilon_\mu=
\frac{J}{N}\Big\langle\sum_x\cos a_\mu(x)\Big\rangle
-\frac{J^2}{Nk_BT}
\Big\langle\Big(\sum_x\sin a_\mu(x)\Big)^2\Big\rangle;
\]
3. check the exact identity \(\sum_pq_p=0\) at every saved configuration;
4. compare \(\Upsilon_x\) and \(\Upsilon_y\), report autocorrelation-aware uncertainties, and repeat for increasing \(L\);
5. analyse the crossing/drift using the BKT finite-size scaling form, including its logarithmic corrections, rather than declaring a transition from one small lattice.

The leading universal-jump line \(\Upsilon/(k_BT)=2/\pi\) is a diagnostic. A defensible estimate of \(T_{BKT}\) requires a size sequence and uncertainty analysis. The charge correlator \(C_q(r)\) is not itself assumed to be logarithmic. If an effective pair potential is estimated, define a normalized vortex–antivortex pair distribution \(g_{+-}(r)\) and use \(W_{+-}(r)=-k_BT\log g_{+-}(r)+C\), with periodic Green-function corrections stated.

### A4. Deliverables and falsification checks

- data table by \((L,T,\text{seed})\): \(\Upsilon_x,\Upsilon_y\), vortex density, winding histogram, integrated autocorrelation times;
- finite-size plot of \(\Upsilon/(k_BT)\), with the \(2/\pi\) reference and fit uncertainty;
- independent fit of the RG flow only where the dilute-gas assumptions are supported;
- explicit negative result if the simulated sizes do not resolve the universal jump.

**Status:** exact neutrality and winding integrality are lattice identities (T110); BKT RG is established theory in its regime; new transition estimates are pending multi-size simulations.

---

## II. Calculation B — 3D XY: dual vortex loops and length distribution

### B1. Exact dual-flux constraint

For a periodic cubic lattice, the plaquette windings are
\[
q_x=q_{23},\qquad q_y=q_{31},\qquad q_z=q_{12}.
\]
They are integer fluxes on links of the dual lattice. The lattice Bianchi identity gives
\[
\nabla_{\rm dual}\!\cdot q=0,
\quad\text{i.e.}\quad
\Delta_xq_x+\Delta_yq_y+\Delta_zq_z=0,
\]
with the anchoring/orientation convention fixed by T110. This is an exact identity. It implies closed flux networks, including non-contractible winding networks on the three-torus.

At vertices of degree greater than two, the flux support is a network, not a uniquely defined collection of loops. Any loop decomposition must state its local pairing rule. The primary invariant measurements are therefore the dual flux, connected components, winding/homology, and network observables; a loop histogram is secondary and convention-dependent unless the network is resolved unambiguously.

### B2. Dual ensemble and loop observables

Use the Villain representation as the controlled analytic bridge from the phase model to integer conserved dual currents. In a fixed normalization the dual ensemble has the schematic form
\[
Z_{\rm dual}=\sum_{j\in\mathbb Z^{E^*}:\,\nabla\cdot j=0}
\exp\!\left[-2\pi^2K\,(j,Gj)-\mu_c\,\mathcal L(j)\right],
\]
where \(G\) is the appropriate lattice Green operator with zero modes treated according to the torus sector, \(\mathcal L(j)\) is total integer flux length, and \(\mu_c\) records any separately declared core/short-distance convention. The exact coefficient and any local core term must be matched to the chosen Villain action; this schematic expression is not to be used as a fitted identity for the cosine model without that matching.

For each saved configuration record:
- total dual flux length \(\mathcal L=\sum_{e^*}|j_{e^*}|\);
- component/network size distribution;
- winding vector in \(H_1(T^3;\mathbb Z)\);
- largest-component fraction and percolation indicator;
- flux two-point function and the exact maximum divergence residual;
- if a loop-pairing convention is used, loop length \(\ell\), radius of gyration \(R_g\), and winding class.

Define the histogram convention explicitly. For example, \(n(\ell;L,T)\) may mean the number of unrooted loops of length \(\ell\), per lattice volume, per saved configuration. Do not compare it with rooted-loop or total-length-weighted histograms as though they were the same observable.

### B3. Scaling test, not an assumed exponent

A useful finite-size scaling ansatz to test is
\[
n(\ell;L,t)=\ell^{-\tau}\,
\mathcal F\!\left(\ell/L^D,\;\ell/\xi(t)^D\right),
\]
where \(t=(T-T_c)/T_c\), \(\xi\) is a correlation length, and \(D,\tau\) are fitted/derived exponents under a declared loop-count convention. For an ideal scale-invariant ensemble of unrooted loops with the stated counting measure, one sometimes obtains the hyperscaling relation \(\tau=1+d/D\); it is a conditional relation, not a universal number to insert by hand. Check the convention and derivation before using it.

The analysis should compare:
1. subcritical finite loops and the cutoff scale;
2. the critical candidate regime and collapse across \(L\);
3. supercritical proliferation/percolation and non-contractible winding;
4. robustness to the loop-pairing rule at junctions.

Do not infer a critical point from a power-law-looking segment on one lattice. Report fit windows, goodness-of-fit, corrections to scaling, autocorrelation, and seed-to-seed variation. The 3D XY transition is not the 2D BKT jump and is not the KTHNY melting transition.

### B4. Deliverables and falsification checks

- exact divergence residual for every saved configuration;
- flux/network distributions and homology-sector probabilities;
- loop-length distributions under at least one explicitly documented decomposition rule;
- finite-size scaling comparison and sensitivity to junction pairing;
- negative result if no stable scaling collapse is obtained.

**Status:** dual-flux closure is exact (T110); loop decomposition and statistical scaling are analysis choices; critical exponents and transition estimates are pending simulation.

---

## III. Calculation C — 2D KTHNY: vector Coulomb gas of dislocations/disclinations

### C1. Defect species and neutrality

For a two-dimensional crystal, dislocations carry vector Burgers charges
\[
\mathbf b_\alpha\in\Lambda_B,
\]
where \(\Lambda_B\) is the Burgers lattice fixed by the chosen crystal (for a triangular lattice, the minimal Burgers vectors form the corresponding six-direction star). Disclinations carry rotational/Frank charge \(s_\alpha\), defined with the crystal's orientational symmetry and branch convention.

These are different species and different observables:
- Burgers closure measures translational incompatibility;
- Frank holonomy measures rotational incompatibility.

On a periodic defect-free-boundary torus, impose the appropriate global neutrality constraints, including \(\sum_\alpha\mathbf b_\alpha=0\) for the dislocation sector. The exact allowed Frank neutrality depends on the orientational order and global geometry and must be stated for the chosen crystal.

### C2. Elastic Coulomb-gas partition function

Starting from isotropic 2D linear elasticity, integrate out the smooth displacement/phonon field subject to the incompatibility constraints. The resulting defect energy is a nonlocal quadratic form
\[
E_{\rm el}[\rho_B,\rho_F]
=\frac12\sum_{\alpha,\beta}
\mathbf Q_\alpha^{T}\,
\mathsf G_{\alpha\beta}(\mathbf r_\alpha-\mathbf r_\beta;\lambda,\mu)
\mathbf Q_\beta,
\]
where \(\mathbf Q_\alpha\) collects the appropriately normalized translational and/or rotational defect charges, and \(\mathsf G\) is derived from the elastic Green operator with the specified boundary conditions. The matrix kernel is not an arbitrary scalar logarithm: it contains the vector and angular structure of elasticity. The kernel, zero modes, self-energy subtraction, and core cutoff must be derived for the actual lattice and elastic convention.

The grand-canonical defect gas is
\[
Z_{\rm def}=\sum_{\{N_s\}}
\prod_s\frac{y_s^{N_s}}{N_s!}
\sum_{\{\mathbf Q_\alpha\}\,\text{neutral}}
\exp[-\beta E_{\rm el}],
\qquad
y_s=e^{-\beta E_{c,s}},
\]
where species \(s\) labels Burgers direction/type or Frank charge, and \(E_{c,s}\) is its core energy. This expression defines the bookkeeping; the actual \(\mathsf G\), charge lattice, fugacities, and allowed reactions must come from the chosen crystal model, not from Q6 labels by analogy.

### C3. Renormalization and universal condition

The KTHNY RG must retain the vector charge species and their symmetry-related fugacities, together with the elastic moduli. At leading order the fugacity of a species has a scaling equation of the form
\[
\frac{dy_s}{d\ell}=[2-x_s(\mathsf C)]y_s+O(y^2),
\]
where \(x_s\) is the scaling dimension computed from the elastic Green kernel and \(\mathsf C\) denotes the dimensionless elastic-modulus data. The stiffness flow receives defect-pair screening corrections at quadratic order in fugacities. The coefficients must be derived for the chosen lattice, normalization, and allowed defect reactions; do not copy scalar BKT coefficients into the vector theory.

For the standard KTHNY dislocation-unbinding normalization, the renormalized Young modulus obeys
\[
K_R=\frac{Y_Ra^2}{k_BT}=16\pi.
\]
This is a statement about the long-distance renormalized modulus at the dislocation-unbinding transition. It is not a condition on the bare modulus. The subsequent disclination-unbinding sector requires the orientational/Frank theory and its own fugacity and RG flow.

### C4. Numerical/continuum programme

1. Choose one explicit crystal (triangular is the canonical first benchmark), lattice spacing \(a\), Lamé coefficients \((\lambda,\mu)\), boundary conditions, and core regularization.
2. Derive the discrete compatibility operator and its Green kernel; verify symmetry, zero modes, and the continuum limit against isotropic elasticity.
3. Enumerate the minimal Burgers star and the permitted neutral reactions; compute each core energy from the microscopic model or declare it as an independent fitted parameter.
4. Measure Burgers and Frank observables independently. Do not reconstruct one from the other without a proven geometric constraint.
5. Implement the vector Coulomb gas and its RG flow; compare the renormalized Young modulus with \(16\pi\) and track the disclination sector separately.
6. Perform finite-size scaling and uncertainty analysis. Compare the continuum elastic prediction with the Morandotti Airy/KKT or semi-discrete benchmark only after matching geometry, units, core energies, and boundary conditions.

### C5. Deliverables and falsification checks

- exact discrete compatibility and neutrality tests;
- explicit elastic Green kernel and derivation;
- species-resolved core energies/fugacities;
- vector-charge pair distributions and angular dependence;
- renormalized \(Y_R\), disclination observables, and finite-size uncertainty;
- independent reproduction of the \(16\pi\) criterion in the regime where KTHNY assumptions hold.

**Status:** KTHNY framework and universal criterion are established; a Q6/Morandotti-specific vector gas and its numerical verification remain to be implemented.

---

## IV. Bridge matrix: QLG → Q6/RGS → gauge defects → N=4 SYM → IIB strings

This bridge is a separate derivation programme. The three defect calculations above supply candidate observables; they do not, by themselves, establish a gauge/string duality.

| Layer | Object to construct | Required proof/check | Current status |
|---|---|---|---|
| Q6/QLG kinematics | Cell complex, boundary/coboundary, quaternionic/spinor fibres, discrete Dirac operator | Exact chain identities, adjoint/domain control, covariance | Finite Q6 complex and cubical SUSY are available; physical spinor continuum remains open |
| Gauge-covariant geometry | Link connection \(U_{vw}\), parallel transport, face holonomy, Wilson loops | Gauge transformation law and lattice Bianchi identities | Finite gauge/holonomy results exist in the repository; common QLG action not yet derived |
| Defect observables | Scalar XY winding, 3D dual flux, Burgers vector, Frank holonomy | Separate calibrations, charge lattices, conservation/neutrality | T107/T110 provide distinct model observables; cross-identification open |
| Continuum field theory | Refinement family, fields, action, measure, local symmetries | Convergence of operators/actions/correlators; Ward identities | Open |
| \(\mathcal N=4\) SYM | 4D gauge field, six real adjoint scalars, four Weyl fermions, supersymmetry transformations, \(SU(4)_R\) | Closure of 16 Poincaré supercharges (plus conformal enhancement), gauge invariance, conformality | T102 is finite cubical SUSY QM, explicitly not N=4 SYM |
| Line operators and S-duality | Global form of gauge group, electric/magnetic charge lattice, Wilson–'t Hooft lines, complex coupling \(\tau\) | Correct charge quantization, mutual locality, duality action on lines and \(\tau\) | Standard SYM structure; map from Q6/defect charges open |
| IIB/AdS5×S5 | Large-N/strong-coupling regime and geometric/string data | Match symmetries, parameters, spectra/correlators and dictionary | AdS/CFT is established for the standard theory; embedding of this discrete model is unproved |

### IV1. Minimal mathematical interface

The first interface is not “Q6 charge = SYM charge”. It is a commuting map of complexes and representations. One must specify chain/cochain maps
\[
(C_\bullet(Q6),\partial)\longrightarrow
(\mathcal C_\bullet^{\rm target},\partial_{\rm target}),
\qquad
\partial_{\rm target}F_k=F_{k-1}\partial,
\]
together with a representation map for the gauge group and a connection-preserving condition for parallel transport/holonomy. If the continuum limit is claimed, the maps must be compatible with refinement and converge in a stated topology.

### IV2. Requirements for N=4 SYM

The six coordinate directions of Q6 are not automatically the six adjoint scalars of N=4 SYM. A candidate construction must independently produce:
- a four-dimensional gauge connection \(A_\mu\);
- six real scalar fields \(\Phi_I\) in the adjoint;
- four Weyl fermions in the adjoint;
- the interaction terms and supersymmetry transformations of the N=4 action;
- \(SU(4)_R\simeq SO(6)\) representation structure and the conformal theory;
- a regulator/continuum argument showing that unwanted operators or doublers do not spoil the target theory.

T102 proves a finite cubical de Rham/Hodge supersymmetric quantum-mechanics algebra and a McKean–Singer supertrace. It does not prove the field content, interactions, R-symmetry, conformality, or S-duality of N=4 SYM.

### IV3. Requirements for the string bridge

For standard AdS/CFT, the relevant established duality is between four-dimensional N=4 SYM and type-IIB string theory on \(AdS_5\times S^5\), with parameter relations involving \(N\), \(g_{\rm YM}\), the string coupling, and the curvature radius in string units. To connect QLG/RGS to this duality, first derive the N=4 theory or a controlled sector/defect of it. Only then can one ask whether its large-N/strong-coupling limit has a string description. Q6 coordinates must not be identified ad hoc with AdS or sphere coordinates.

### IV4. Charge dictionary: candidate table, not identification

| RGS/QLG observable | Candidate SYM object | Missing step |
|---|---|---|
| Discrete gauge holonomy | Wilson loop/line | Derive representation, continuum connection and path ordering |
| Magnetic flux / dual cocycle | 't Hooft line sector | Establish magnetic charge quantization and global gauge-group data |
| XY vortex number | 2D topological defect/operator | Derive a specified reduction or defect theory; no automatic Wilson/'t Hooft identity |
| Burgers vector | Translational/defect charge in an effective theory | Derive from a symmetry/translation sector; not a gauge weight by naming |
| Frank holonomy | Rotational/twist defect | Identify the relevant spacetime/internal symmetry and its defect operator |
| Q6 six-bit label | No direct SYM field assignment | Construct an equivariant map; cardinality six alone proves nothing |

---

## V. Execution order and acceptance gates

1. **BKT:** extend the T110 runner to a multi-size, multi-temperature ensemble; verify neutrality per configuration; estimate helicity modulus and its finite-size drift.
2. **3D loops:** construct dual flux networks from all three plaquette orientations; measure homology and length statistics; preregister the loop-count convention and test junction sensitivity.
3. **KTHNY:** implement the triangular-lattice elastic Green kernel and vector Burgers gas; only then compute the RG coefficients and compare \(K_R\) with \(16\pi\).
4. **QLG bridge:** formalize the discrete connection/Dirac operator and chain maps; identify what survives refinement.
5. **N=4/SYM:** only after the continuum field content and supersymmetry transformations are derived, test the line-operator charge lattice and S-duality.
6. **IIB strings:** only after the N=4 dictionary is established, assess the large-N/strong-coupling limit and the AdS5×S5 parameter map.

### Acceptance policy

A calculation is accepted only with (i) definitions and normalization, (ii) derivation or stated approximation, (iii) reproducible code/data, (iv) uncertainty and finite-size controls, and (v) explicit failure criteria. A passed unit test verifies code behavior, not a phase transition or physical equivalence.

## References

- J. M. Kosterlitz, D. J. Thouless, “Ordering, metastability and phase transitions in two-dimensional systems,” *J. Phys. C* 6 (1973), 1181.
- J. M. Kosterlitz, “The critical properties of the two-dimensional XY model,” *J. Phys. C* 7 (1974), 1046.
- P. Minnhagen, “The two-dimensional Coulomb gas, vortex unbinding, and superfluid-superconducting films,” *Rev. Mod. Phys.* 59 (1987), 1001. DOI: 10.1103/RevModPhys.59.1001.
- D. R. Nelson, B. I. Halperin, “Dislocation-mediated melting in two dimensions,” *Phys. Rev. B* 19 (1979), 2457. DOI: 10.1103/PhysRevB.19.2457.
- A. P. Young, “Melting and the vector Coulomb gas in two dimensions,” *Phys. Rev. B* 19 (1979), 1855. DOI: 10.1103/PhysRevB.19.1855.
- J. Maldacena, “The Large N Limit of Superconformal Field Theories and Supergravity,” *Adv. Theor. Math. Phys.* 2 (1998), 231–252. DOI: 10.1023/A:1026654312961.
- A. Kapustin, “Wilson–'t Hooft operators in four-dimensional gauge theories and S-duality,” *Phys. Rev. D* 74 (2006), 025005. DOI: 10.1103/PhysRevD.74.025005.


---

## VI. New physical bridge — QHD, quantum vortex flux, classical fluids and MHD

This section makes explicit the physical route suggested by the vortex-flux sector. It distinguishes three meanings that are often all called “quantum hydrodynamics”:

1. **QHD of a neutral condensate/superfluid**, obtained from a complex order parameter (Gross–Pitaevskii/Madelung description);
2. **quantum-corrected charged-fluid/plasma models**, in which Bohm-type terms enter species momentum equations coupled to Maxwell fields and a generalized Ohm law;
3. **MHD**, a classical or extended continuum theory for conducting fluids/plasmas.

They share conservation and transport structures, but they are not the same equations.

### VI1. Neutral quantum fluid: Madelung equations and quantized circulation

For a dilute condensate in the Gross–Pitaevskii regime,
\[
i\hbar\partial_t\psi=
\left[-\frac{\hbar^2}{2m}\nabla^2+V+g|\psi|^2\right]\psi.
\]
Set \(\psi=\sqrt n\,e^{iS/\hbar}\), and define \(\mathbf v=\nabla S/m\). Away from zeros of \(\psi\), the equations are
\[
\partial_t n+\nabla\cdot(n\mathbf v)=0,
\]
\[
m(\partial_t\mathbf v+\mathbf v\cdot\nabla\mathbf v)
=-\nabla(V+gn+Q),\qquad
Q=-\frac{\hbar^2}{2m}\frac{\nabla^2\sqrt n}{\sqrt n}.
\]
The term \(Q\) is the quantum-pressure/Bohm potential. It regularizes vortex cores and participates in nucleation, sound emission and reconnection dynamics.

Because the phase is single-valued modulo \(2\pi\), for a loop avoiding zeros of \(\psi\),
\[
\Gamma=\oint_C\mathbf v\cdot d\boldsymbol\ell
=\frac{h}{m}\,w,\qquad w\in\mathbb Z.
\]
Thus the vorticity vanishes classically in smooth simply connected regions but is distributionally supported on quantized vortex filaments:
\[
\boldsymbol\omega=\nabla\times\mathbf v
=\kappa\sum_a n_a\int
\delta^{(3)}(\mathbf x-\mathbf X_a(s))\,
\mathbf X'_a(s)\,ds,
\qquad \kappa=h/m.
\]
This is the continuum counterpart of the integer dual-flux lines measured by T110 in 3D XY, provided the lattice phase field is interpreted as the phase of an order parameter. T110 alone does not supply the density field, quantum pressure, or GP dynamics; those are the next QHD layer.

### VI2. The exact analogy with Euler and the qualified bridge to MHD

For an inviscid barotropic classical fluid, the vorticity equation has the transport form
\[
\partial_t\boldsymbol\omega
=\nabla\times(\mathbf u\times\boldsymbol\omega)
\]
(with baroclinic and other source terms added when the assumptions fail). For ideal MHD,
\[
\partial_t\mathbf B
=\nabla\times(\mathbf u\times\mathbf B),
\qquad \nabla\cdot\mathbf B=0.
\]
These equations have the same Lie-advection structure: vorticity flux in ideal barotropic flow and magnetic flux in ideal MHD are transported by the fluid velocity. Kelvin's circulation theorem and Alfvén's frozen-in-flux theorem are related geometric conservation statements.

But the transported objects differ:
- \(\boldsymbol\omega\) is curl of velocity;
- \(\mathbf B\) is magnetic induction governed by Maxwell equations and Ohm's law;
- a superfluid vortex is a singular, quantized defect of the phase field.

The ideal-MHD induction equation is only the large-magnetic-Reynolds-number, ideal-Ohm-law limit. Resistivity, Hall terms, electron inertia, pressure anisotropy and kinetic effects can change magnetic topology. Likewise, quantum vortex lines can reconnect because the condensate density vanishes at their cores and the smooth-fluid hypotheses behind Kelvin's theorem fail there. Reconnection is therefore a particularly useful comparison problem, not proof that the two systems are identical.

### VI3. Direct electromagnetic coupling: charged condensates and flux tubes

A direct identification between phase vortices and magnetic flux tubes is available only in a charged condensate/superconductor. For charge \(q\), the gauge-covariant phase gradient is
\[
\mathbf v_s=\frac1m(\hbar\nabla\theta-q\mathbf A).
\]
Single-valuedness gives, around a contour outside the core,
\[
m\oint\mathbf v_s\cdot d\boldsymbol\ell
+q\Phi_B=nh.
\]
In the London limit where the supercurrent circulation term is negligible sufficiently far from an isolated type-II vortex, the flux is quantized:
\[
\Phi_B=n\Phi_0,\qquad \Phi_0=h/|q|.
\]
For Cooper pairs, \(|q|=2e\). Abrikosov vortices are therefore actual magnetic-flux tubes, unlike neutral-superfluid vortices. Their lattice elasticity, pinning, creep and reconnection/entry processes provide a concrete materials bridge to hysteresis and industrially relevant magnetic response.

### VI4. Quantum-hydrodynamic plasmas

For a charged multi-species plasma, the QHD layer must instead start from species continuity and momentum equations, for example
\[
\partial_t n_s+\nabla\cdot(n_s\mathbf u_s)=0,
\]
\[
m_sn_s(\partial_t+\mathbf u_s\cdot\nabla)\mathbf u_s
=q_sn_s(\mathbf E+\mathbf u_s\times\mathbf B)
-\nabla p_s+n_s\mathbf F_{Q,s}+\mathbf R_s,
\]
coupled to Maxwell equations and a derived generalized Ohm law. \(\mathbf F_{Q,s}\) may contain a Bohm quantum force, while \(\mathbf R_s\) contains collisions or interspecies momentum exchange. Hall, electron-inertia, resistive and pressure-tensor terms must be retained or dropped by explicit scale ordering. A neutral GP condensate is not a substitute for this plasma closure.

### VI5. Common geometric language: fluxes, complexes and defects

The common mathematical object is a flux form/current with a conservation law, not a universal “vortex = magnetic line” identity.

- In continuum language: divergence-free fluxes, circulation, helicity, linking and transport by a flow map.
- In discrete language: integer-valued primal/dual cochains, incidence operators, boundary/coboundary identities, and a discrete Bianchi/closure constraint.
- In Q6/QLG: candidate observables are cycle/cocycle classes, holonomies and transported fluxes. A chain map must preserve the boundary operator; a connection map must preserve parallel transport up to gauge transformation.
- In RGS/PRISM: compare the measured dual-flux network with continuum vortex-filament statistics and, separately, with magnetic-flux-tube networks. Do not collapse their charge units or dynamics.

A useful cross-domain observable set is:
\[
\{\text{flux},\ \text{circulation},\ \text{helicity/linking},\
\text{winding/homology},\ \text{reconnection rate},\
\text{energy spectrum},\ \text{transport coefficients}\}.
\]
Each observable needs its own units, normalization, conservation assumptions and measurement map.

### VI6. New computational programme

1. **QHD benchmark:** implement the 2D/3D GP equation with density and phase; verify mass conservation, energy conservation in the Hamiltonian regime, circulation quantization, vortex-core profiles and reconnection events.
2. **T110 bridge:** compare integer plaquette/dual-link fluxes with zeros and phase winding of the GP order parameter under refinement; quantify the error in vortex position, line length and homology.
3. **Euler/MHD comparison:** implement the vorticity and induction equations on the same periodic geometry; verify Kelvin/Alfvén invariants in their ideal regimes and quantify their breakdown under viscosity/resistivity or singular reconnection layers.
4. **Charged-condensate benchmark:** implement the gauge-coupled GL/London model; verify flux quantum, penetration depth, coherence length and Abrikosov lattice response.
5. **Plasma-QHD extension:** add species-resolved Bohm force and generalized Ohm terms; perform a controlled ordering study against ideal/resistive/Hall MHD.
6. **QLG/RGS map:** construct commuting discrete flux and boundary diagrams, then compare continuum limits. Only after this step may a QLG flux class be assigned to a specific hydrodynamic or electromagnetic observable.

### VI7. Acceptance criteria and no-go checks

- GP: conservation residuals converge with spatial/time refinement; circulation is integer-quantized on contours outside cores.
- T110–GP: vortex-line homology and charge agree in the refinement regime; report failures near unresolved cores or reconnection events.
- Ideal MHD: magnetic flux is conserved only under the ideal Ohm/regularity assumptions; resistive and Hall departures are measured, not hidden.
- Charged GL: flux quantum is \(h/|q|\), not the neutral-superfluid circulation quantum \(h/m\).
- QHD plasma: every quantum correction is tied to a specified closure and scale ordering.
- Cross-domain claim: a correspondence is accepted only if the map preserves equations, units, symmetries and observables—not merely visual similarity of filaments.

**Status:** the Madelung, quantized-circulation, Euler-vorticity and ideal-MHD flux-freezing structures are established. The common discrete QLG/RGS implementation, the T110-to-GP refinement test, and the unified multi-physics simulations remain open.

### VI8. References for the QHD–MHD bridge

- A. J. Leggett, “Quantum Liquids,” Oxford University Press (2006).
- C. F. Barenghi, L. Skrbek, K. R. Sreenivasan, “Introduction to quantum turbulence,” *PNAS* 111 (2014), 4647–4652. DOI: 10.1073/pnas.1312541111.
- G. Villois, D. Proment, G. Krstulovic, “Universal and nonuniversal aspects of vortex reconnections in superfluid helium,” *Phys. Rev. Fluids* 2 (2017), 044701.
- A. L. Fetter, “Quantum Theory of Superfluid Vortices. II. Type-II Superconductors,” *Phys. Rev.* 163 (1967), 390. DOI: 10.1103/PhysRev.163.390.
- A. Enciso, D. Peralta-Salas, “Vortex reconnections in classical and quantum fluids,” *J. Math. Fluid Mech.* 24 (2022), 127. DOI: 10.1007/s40324-021-00277-8.
- A. A. Schekochihin et al., “Lessons on collisionless reconnection from quantum fluids,” *Frontiers in Physics* 2 (2014), 76.
- H. K. Moffatt, *Magnetic Field Generation in Electrically Conducting Fluids*, Cambridge University Press (1978).
