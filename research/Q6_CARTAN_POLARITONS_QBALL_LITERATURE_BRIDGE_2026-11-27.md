# Q6 discrete Cartan geometry, polaritons and Q-balls: literature comparison and research bridge

**Date:** 27 November 2026  
**Classification:** literature-grounded research synthesis; proposed discrete construction; no new physical theorem claimed.

## Executive conclusion

Three literatures meet here, but they must not be conflated:

1. **Discrete Riemann–Cartan geometry:** a mathematically direct route to coframes, connections, torsion and curvature on a cell complex. The most directly relevant recent reference is Christiansen–Hu–Lin (2026), *Extended Regge Complex for Linearized Riemann-Cartan Geometry and Cohomology*, DOI 10.1007/s10208-026-09746-w. It builds a discrete twisted/Regge complex in which coframes and connection 1-forms occur at degree one and torsion and curvature at degree two. It is linearized and triangulation-based; adapting it to the Q6 cubical complex and nonlinear link variables is a research task, not a result already contained in that paper.
2. **Polaritons:** a physical platform for coherent bosonic fields, nonlinear waves, spinor order parameters, vortices, solitons, Berry curvature and synthetic Abelian/non-Abelian gauge fields. It is especially relevant as a possible *analogue simulator* of internal phase and link transport. Ordinary exciton-polariton condensates are driven and dissipative; their particle number is not generally an exactly conserved Q-ball charge.
3. **Q-balls:** non-topological, charge-stabilized localized field configurations. The strongest condensed-matter realization located is not an exciton-polariton experiment but a magnon BEC in superfluid \(^{3}\mathrm{He}\)-B, where the magnon number plays the role of \(Q\), and a neutral orbital mode helps generate the self-consistent confining potential.

The strongest physical bridge is therefore **Q6 geometry ↔ synthetic-gauge spinor polariton lattice** for controllable link/holonomy experiments, and **Q6 internal phase/charge sector ↔ magnon-Q-ball mechanism** for conserved-charge localization. A direct claim that Q6 already predicts polariton Q-balls would be unsupported.

## 1. The Q6 cell carrier and the missing 3-cells

The carrier remains the six-bit hexagram space
\[
\mathcal H=\{0,1\}^{6},
\]
with Hamming-one adjacency. Its cubical cell counts are
\[
N_k=\binom{6}{k}2^{6-k}.
\]
Thus
\[
N_0=64,\quad N_1=192,\quad N_2=240,\quad N_3=160,
\]
and, for completeness, \(N_4=60,N_5=12,N_6=1\).

The 160 elementary 3-cubes are essential for the next stage. Curvature is a face (2-cell) holonomy; its covariant Bianchi identity is tested on 3-cells. A face-only audit cannot establish the Bianchi identity. The graph cycle rank \(E-V+1=129\) is the first Betti number of the 1-skeleton only; after attaching all cubical faces and higher cells, the full 6-cube is contractible.

## 2. A more intrinsic discrete Cartan variable: affine/Poincaré link

The previous code separately stores an \(SO(3)\) edge transporter \(U_{gh}\) and a vector increment \(\theta_{gh}\). A more intrinsic finite Cartan object is the semidirect-product link
\[
\mathsf G_{gh}=(U_{gh},\theta_{gh})\in SE(3)=SO(3)\ltimes\mathbb R^3,
\]
with multiplication
\[
(U,t)(V,s)=(UV,t+Us).
\]
For an oriented face \(p=(v_0,\ldots,v_{m}=v_0)\), its ordered affine holonomy is
\[
\mathsf H_p=\mathsf G_{v_{m-1}v_m}\cdots\mathsf G_{v_0v_1}
=(H_p,\tau_p).
\]
The rotational part \(H_p\) is the discrete curvature holonomy; the translational part \(\tau_p\) is the developed closure defect, i.e. the natural discrete torsion/dislocation observable in this affine model.

Under a local affine frame change \(g_v=(G_v,a_v)\in SE(3)\), links transform by
\[
\mathsf G'_{gh}=g_h\,\mathsf G_{gh}\,g_g^{-1},
\]
and face holonomies by conjugation at the base vertex:
\[
\mathsf H'_p=g_{v_0}\mathsf H_p g_{v_0}^{-1}.
\]
This is stronger and conceptually cleaner than treating a raw vector closure and a rotational Wilson loop as unrelated quantities. The precise choice of whether \(\theta_{gh}=E_g(X_h-X_g)\) or a symmetrized/parallel-transported edge coframe is used must be fixed so reverse-edge inversion holds exactly:
\[
\mathsf G_{hg}=\mathsf G_{gh}^{-1}
=(U_{gh}^{-1},-U_{gh}^{-1}\theta_{gh}).
\]
In particular, setting \(\theta_{hg}=-\theta_{gh}\) independently is generally incompatible with this inverse law when \(U\ne I\). This orientation issue must be corrected before interpreting the earlier closure observable as a fully intrinsic Cartan torsion.

For the flat branch \(U^{\mathrm W}=I\), nonzero translational face holonomy is possible. For the curved branch, both rotational and translational components may be nonzero. The two branches remain distinct.

## 3. Discrete Bianchi identities: what must be checked

For each elementary 3-cube \(c\), the six boundary face holonomies must be transported to a common base frame and multiplied in the order induced by the oriented boundary. Because every edge link is shared with opposite orientation, the complete boundary word is a group identity when built consistently from the same edge variables. This is the finite non-Abelian lattice Bianchi consistency relation.

For the affine holonomy \((H,\tau)\), the rotational and translational parts give coupled identities. In the continuum these tend to
\[
D T^A=R^A{}_B\wedge e^B,\qquad D R^A{}_B=0.
\]
A numerical test on all 160 cubes is a necessary algebraic audit, but not a proof of convergence to the differential Cartan identities. The implementation must:
1. enumerate all 160 3-cubes with a fixed orientation;
2. enumerate their six square faces with induced orientations;
3. transport every face holonomy to a common cube base point;
4. multiply in the correct boundary order in \(SE(3)\);
5. check rotational and translational residuals independently;
6. repeat after arbitrary local \(SE(3)\) frame transformations.

This is the next exact finite-combinatorial milestone. Do not infer it from the 240-face test alone.

## 4. Literature: discrete Riemann–Cartan geometry

### 4.1 Christiansen, Hu and Lin (2026) — closest mathematical match

S. H. Christiansen, K. Hu and T. Lin, “Extended Regge Complex for Linearized Riemann-Cartan Geometry and Cohomology,” *Foundations of Computational Mathematics* (published 17 February 2026), DOI: 10.1007/s10208-026-09746-w.

The authors extend the Regge sequence using twisted de Rham/elasticity complexes. Their abstract explicitly places coframes and connection 1-forms at degree one, torsion and curvature at degree two, and establishes the cohomology of the resulting linearized complex. They explain that the BGG construction can eliminate rotational degrees of freedom to recover a Riemannian complex.

**Relevance:** this supplies the right mathematical architecture for a structure-preserving Q6 discretization: a complex with incidence maps and a cohomology theorem, rather than a collection of face diagnostics.

**Difference:** their construction is linearized and based on triangulations. Q6 is naturally cubical and the current links are nonlinear group-valued. The research task is a cubical, nonlinear \(SE(3)\)/Cartan analogue, or a justified cubical-to-simplicial subdivision with commuting cochain maps.

### 4.2 Schmidt and Kohler (2001) — torsion as dislocation

J. Schmidt and C. Kohler, “Torsion Degrees of Freedom in the Regge Calculus as Dislocations on the Simplicial Lattice,” *General Relativity and Gravitation* 33 (2001), 1799–1807, DOI: 10.1023/A:1013031402382.

They add dislocations to the usual conical/disclination defects of Regge calculus and formulate a discrete Einstein–Cartan action with field equations.

**Relevance:** supports interpreting the translational part of an affine holonomy as a dislocation/torsion defect, distinct from rotational curvature.

### 4.3 Hamber and Kagel (2004) — exact lattice Bianchi identity

H. W. Hamber and G. Kagel, “Exact Bianchi identity in Regge gravity,” *Classical and Quantum Gravity* 21 (2004), 5915–5947, DOI: 10.1088/0264-9381/21/24/013.

They derive exact discrete Bianchi identities from products of rotation matrices around null-homotopic paths, valid beyond the weak-curvature limit.

**Relevance:** the correct precedent for testing the 160 Q6 cubes through ordered products and parallel transports, rather than imposing a continuum differential identity numerically.

### 4.4 Teleparallel geometry

The 2025 philosophy/mathematics analysis “Equivalence, reduction, and sophistication in teleparallel gravity” describes teleparallel geometry through a flat principal connection plus a coframe, and explains how they combine into a Cartan connection for the Poincaré group.

**Relevance:** reinforces the separation already made in the Q6 project: a flat \(U^{\mathrm W}\) branch with torsion is distinct from a curved Riemann–Cartan branch. The finite flat branch is not yet a variationally selected TEGR solution.

## 5. Literature: polaritons and synthetic gauge fields

### 5.1 Ma et al. (2026) — vortices and solitons in polariton condensates

X. Ma et al., “Vortices and solitons in polariton superfluids and condensates,” *Nature Reviews Physics* 8, 437–451 (published 14 May 2026), DOI: 10.1038/s42254-026-00943-8.

This review covers optically driven polariton vortices and solitons, phase jumps, stationary nonlinear structures and spinor half-vortices.

**Relevance:** experimentally controllable phase winding, localized nonlinear states and half-quantized defects are natural observables to compare with Q6 plaquette phases and internal two-sheet sectors.

**Caution:** polariton condensates are typically driven-dissipative. Their steady-state equations are not automatically conservative relativistic scalar field equations.

### 5.2 Biegańska et al. (2021) — spinor polaritons in synthetic gauge fields

D. Biegańska et al., “Collective Excitations of Exciton-Polariton Condensates in a Synthetic Gauge Field,” *Physical Review Letters* 127, 185301 (2021), DOI: 10.1103/PhysRevLett.127.185301.

They measure anisotropic collective excitations and spin textures in a high-density trapped spinor polariton condensate, linking the anisotropy to TE–TM splitting and a synthetic magnetic gauge field.

**Relevance:** a two-component polariton order parameter and its pseudospin texture provide a possible analogue of an internal doublet carried over the Q6 links. The effective gauge connection and its plaquette holonomy can be experimentally reconstructed.

### 5.3 Artificial gauge fields in photonics (2025)

“Artificial gauge fields in photonics,” *Nature Reviews Physics* 7, 606–620 (2025), DOI: 10.1038/s42254-025-00869-7.

The review classifies photonic gauge fields as scalar/vectorial, Abelian/non-Abelian, real/complex, and discusses synthetic dimensions.

**Relevance:** supports the idea that an internal Q6 index or two-sheet/pseudospin label could be treated as a synthetic dimension, with engineered link phases. It does not imply that the Q6 6D cut-and-project space is already realized in a polariton device.

### 5.4 Exciton-polariton condensates and topological defects (2015)

The 2015 *Annual Review of Condensed Matter Physics* review “Exciton-Polariton Bose-Einstein Condensates,” 6, 155, surveys quantized vortices, half-vortices and hyperbolic spin vortices, including the role of dissipation and disorder.

**Relevance:** provides baseline experimental phenomenology for phase winding and spinor defects.

### 5.5 Annular polariton condensate as a controllable two-state system (2024)

“Qubit analog with polariton superfluid in an annular trap,” *Science Advances* 10, eado4042 (23 October 2024), DOI: 10.1126/sciadv.ado4042.

The experiment coherently couples counter-circulating vortex modes \(l=+1\) and \(l=-1\), realizes their two-state superpositions, and tracks Rabi-like oscillations.

**Relevance:** a useful minimal laboratory analogue for the two orientations/sheets of an Anti-Twin pair and for controlled transitions between counter-propagating phase windings. It is not evidence that the Anti-Twin topology itself is realized.

## 6. Literature: Q-balls and condensed-matter analogues

### 6.1 Coleman Q-balls and the conserved charge

For a complex scalar field with global \(U(1)\),
\[
\mathcal L=|\partial_\mu\Phi|^2-U(|\Phi|),
\qquad \Phi(\mathbf x,t)=f(r)e^{i\omega t},
\]
the conserved Noether charge is
\[
Q=\int d^3x\,j^0,\qquad
j^\mu=i(\Phi^*\partial^\mu\Phi-\Phi\partial^\mu\Phi^*),
\]
up to the convention-dependent overall sign. A Q-ball is a localized finite-energy stationary configuration stabilized at fixed \(Q\), provided the potential satisfies the relevant existence condition (in the standard normalization, \(\min_{\phi>0}2U(\phi)/\phi^2 < m_\phi^2\)).

Nugaev and Shkerin (2019), “Review of non-topological solitons in theories with \(U(1)\)-symmetry,” arXiv:1905.05146 / *JETP* 130 (2020), 301, reviews Q-balls, charged condensates, Q-holes, Q-bulges, gauged Q-balls and boson stars.

### 6.2 Direct condensed-matter Q-ball: magnon BEC in superfluid \(^{3}\)He-B

S. Autti et al., “Propagation of self-localized Q-ball solitons in the \(^{3}\)He universe,” *Physical Review B* 97, 014518 (2018), DOI: 10.1103/PhysRevB.97.014518.

The experiment realizes long-lived self-localized Q-ball solitons as magnon Bose–Einstein condensates. The magnon number \(N_M\) plays the role of conserved charge \(Q\), the precession frequency corresponds to the internal phase frequency, and a neutral orbital Nambu–Goldstone mode provides a self-consistent confining potential. Propagation and collisions of multiple Q-balls are observed.

A related earlier result is Bunkov and Volovik, “Magnon Condensation into a Q Ball in \(^{3}\)He-B,” *Physical Review Letters* 98, 265302 (2007).

**Relevance to RGS/PSU:** this is a concrete example of a charged coherent bosonic mode coupled to a neutral geometric/order-parameter mode that creates its own trap. It suggests a disciplined two-sector ansatz: a complex charged field \(\Phi\) plus a neutral geometric/internal field \(\zeta\). It does not identify \(\zeta\) with the Q6 perpendicular 3-space or Anti-Twin sector; that would require deriving the coupling and conserved charge from the RGS action.

### 6.3 Why ordinary polaritons are not automatically Q-balls

Exciton-polaritons have a finite lifetime and require pumping; the driven-dissipative Gross–Pitaevskii description includes gain and loss. A strict Q-ball analogy requires an approximately or exactly conserved \(U(1)\) charge over the relevant timescale and a stationary localized solution minimizing energy at fixed charge. The existence of polariton vortices or bright/dark solitons alone does not establish this criterion.

The polariton literature is therefore most useful for **synthetic gauge fields, spinor order, phase winding and controlled nonlinear wave packets**. The magnon \(^{3}\)He-B literature is the stronger precedent for **charge-stabilized Q-ball dynamics**.

## 7. A testable Q6-to-platform dictionary (proposal, not identification)

| Q6/RGS object | Candidate laboratory analogue | Required test |
|---|---|---|
| 64 hexagram vertices | 64-site micropillar/polariton array | Implement adjacency graph and measure couplings |
| 192 Q6 edges | engineered tunnelling links | Reconstruct complex hopping amplitudes |
| 240 square faces | plaquettes | Measure Wilson phases/holonomies |
| two spinor components / Anti-Twin sheets | polariton circular pseudospin \(\sigma^\pm\) | Measure Stokes vector and inter-sheet coupling |
| \(U_{gh}\) | link transport / hopping phase | Verify local-frame covariance and plaquette flux |
| internal phase frequency \(\omega\) | condensate precession/oscillation frequency | Spectroscopy and phase-resolved interferometry |
| conserved \(Q\) | magnon number or approximate polariton occupation | Quantify loss and charge conservation timescale |
| neutral \(\zeta\) field | reservoir/order-parameter deformation | Demonstrate self-consistent trapping feedback |
| torsion/translation holonomy | affine coframe defect | Must be separately engineered/measured; not the same as Berry curvature |

A practical first experiment/simulation is not a full 64-site six-dimensional quasicrystal. Begin with a small Q6 subgraph or a two-sheet annular polariton device. Reconstruct the link matrices and plaquette Wilson loops from interferometry; compare the measured pseudospin texture to the graph gauge-covariant model. Only after this is validated should the golden cut-and-project window be encoded in site positions or couplings.

## 8. Proposed next computational milestones

### M1 — Cubical topology and 3-cell Bianchi audit
Generate the full oriented Q6 cubical chain complex through dimension 3. Verify
\[
\partial_1\partial_2=0,\qquad \partial_2\partial_3=0,
\]
with dimensions \(64,192,240,160\). Then implement the non-Abelian \(SE(3)\) boundary-holonomy identity on every 3-cube.

### M2 — Affine Cartan links
Replace the current pair \((U,\theta)\) with a single \(SE(3)\) link and enforce reverse-edge inversion exactly. Compare the resulting translational face holonomy with the previous developed closure observable. This will reveal whether the earlier edge convention was already consistent or requires correction.

### M3 — Polariton lattice forward model
Use a driven-dissipative spinor discrete Gross–Pitaevskii model,
\[
i\partial_t\Psi_g=
\sum_{h\sim g}J_{gh}\Psi_h+
\bigl[\Delta_g+\alpha_1|\psi_{g,+}|^2+\alpha_2|\psi_{g,-}|^2\bigr]\Psi_g
+\frac{i}{2}(P_g-\gamma_g)\Psi_g
+\mathsf H_{\mathrm{TE-TM}}\Psi,
\]
with \(\Psi_g=(\psi_{g,+},\psi_{g,-})^T\). The hopping \(J_{gh}\) can carry engineered link matrices. Compare gauge-invariant plaquette observables and vortex/spinor textures to Q6 predictions. The exact model must specify whether the pump is resonant or incoherent and include the appropriate reservoir dynamics.

### M4 — Q-ball charge and neutral geometric mode
Introduce a complex field \(\Phi\) and neutral field \(\zeta\) with a \(U(1)\)-invariant action and derive the Noether current. A minimal FLS-type ansatz is
\[
\mathcal L=|\partial\Phi|^2+\tfrac12(\partial\zeta)^2-U(|\Phi|,\zeta),
\]
with a coupling that allows \(\zeta\) to generate a self-consistent localized trap. Determine whether the Q6/PSU internal variables can supply \(\zeta\) and whether the resulting charge is conserved. Do not assume the coupling or potential from geometry alone.

### M5 — Relate, do not conflate, Berry curvature and Cartan curvature
The polariton pseudospin Berry connection is a connection on the eigenstate bundle; its curvature is Berry curvature. The RGS Cartan connection acts on local frames and has both rotational curvature and translational torsion. They can be compared through a specified representation/bundle map, but are not the same tensor by definition. A measured polariton Berry phase is not a measurement of spacetime torsion.

## 9. References

1. Christiansen, S. H., Hu, K., Lin, T. (2026), *Extended Regge Complex for Linearized Riemann-Cartan Geometry and Cohomology*, DOI: 10.1007/s10208-026-09746-w.
2. Schmidt, J., Kohler, C. (2001), *Torsion Degrees of Freedom in the Regge Calculus as Dislocations on the Simplicial Lattice*, DOI: 10.1023/A:1013031402382.
3. Hamber, H. W., Kagel, G. (2004), *Exact Bianchi identity in Regge gravity*, DOI: 10.1088/0264-9381/21/24/013.
4. Ma, X. et al. (2026), *Vortices and solitons in polariton superfluids and condensates*, DOI: 10.1038/s42254-026-00943-8.
5. Biegańska, D. et al. (2021), *Collective Excitations of Exciton-Polariton Condensates in a Synthetic Gauge Field*, DOI: 10.1103/PhysRevLett.127.185301.
6. *Artificial gauge fields in photonics* (2025), DOI: 10.1038/s42254-025-00869-7.
7. *Exciton-Polariton Bose-Einstein Condensates* (2015), DOI: 10.1146/annurev-conmatphys-031214-014542.
8. *Qubit analog with polariton superfluid in an annular trap* (2024), DOI: 10.1126/sciadv.ado4042.
9. Nugaev, E., Shkerin, A. (2019), *Review of non-topological solitons in theories with U(1)-symmetry*, arXiv:1905.05146.
10. Autti, S. et al. (2018), *Propagation of self-localized Q-ball solitons in the \(^{3}\)He universe*, DOI: 10.1103/PhysRevB.97.014518.
11. Bunkov, Yu. M., Volovik, G. E. (2007), *Magnon Condensation into a Q Ball in \(^{3}\)He-B*, DOI: 10.1103/PhysRevLett.98.265302.

