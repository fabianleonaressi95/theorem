# RGS–Q6–Anti-Twin: formal compatibility with QHD, Maxwell and quaternionic transport

**Status:** integration dossier; standard continuum identities and exact finite-complex identities are separated from proposed RGS couplings. The complete coupled field theory and its Q6 continuum limit remain open.  
**Dependency order:** 4D connection/transport → QHD and Maxwell → quaternionic/spin lift → 6D internal/physical split → 3D cut-and-project.

## 0. Purpose

This record formalizes one architecture joining:
1. the oriented cubical Q6 complex and Anti-Twin double;
2. spacetime connection and compatible temporal transport;
3. gauge-covariant quantum hydrodynamics (QHD/Madelung);
4. Maxwell electrodynamics and its discrete Bianchi identity;
5. quaternionic SU(2) transport and spin representations;
6. Green–Kubo response as a later statistical layer.

These are not interchangeable descriptions of one field. The bridge consists of explicit maps, common representations, variational couplings and identities that must survive each passage.

## 1. Geometric carrier and Anti-Twin bundle

For the cubical 6-cube, the cell counts through degree three are
\[
(\dim C_0,\dim C_1,\dim C_2,\dim C_3)=(64,192,240,160).
\]
Let \(\partial_k:C_k\to C_{k-1}\) be the oriented boundary and \(\delta_k=\partial_{k+1}^{T}\) the coboundary:
\[
\partial_{k-1}\partial_k=0,\qquad \delta_{k+1}\delta_k=0.
\]
The dual cochain differential is the discrete exterior derivative. It is not the metric-dependent Hodge star.

The Anti-Twin double is
\[
C_k^{AT}=C_k\otimes\mathbb R^2,\quad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad S^2=I,
\]
with \(\mathbb\partial_k=\partial_k\otimes I_2\). Hence
\[
[\mathbb\partial_k,I\otimes S]=0,\qquad
P_\pm=\tfrac12(I\pm I\otimes S).
\]
A Möbius seam is a sheet-exchange transition. It is not, by itself, Cartan torsion, electromagnetic curvature or a magnetic monopole.

The 64×3 RGS seed is a spatial realization. It does not alone supply a canonical 6D physical/internal split, a continuum 3-manifold, or a Lorentzian metric.

## 2. Spacetime connection and chain-compatible temporal transport

At time slices \(t_n\), let
\[
U_k(n):C_k^{AT}(t_n)\to C_k^{AT}(t_{n+1})
\]
be the transport on k-cells. The compatibility axiom is
\[
\boxed{\mathbb\partial_k(t_{n+1})U_k(n)
=U_{k-1}(n)\mathbb\partial_k(t_n).}\tag{2.1}
\]
It makes transport commute with taking boundaries and induces maps on homology/cohomology. Anti-Twin symmetry is the additional condition
\[
[U_k(n),I\otimes S]=0.
\]
If this fails, the even and odd sectors mix; this is a measurable symmetry-breaking defect, not automatically a failure of the chain complex.

For Euclidean cell inner products define
\[
\Delta_k=\partial_k^T\partial_k+
\partial_{k+1}\partial_{k+1}^T,\quad
H_k=\Delta_k\otimes I_2+\mu I\otimes(I-S).
\]
The chain-Hodge identity gives
\[
\partial_k\Delta_k=\Delta_{k-1}\partial_k,\quad
\mathbb\partial_kH_k=H_{k-1}\mathbb\partial_k.
\]
Therefore \(U_k(t)=e^{-itH_k}\) is an exact chain map and commutes with sheet exchange. In the sheet-even/odd sectors,
\[
H_{k,+}=\Delta_k,\qquad H_{k,-}=\Delta_k+2\mu I.
\]
This is an exact finite Hodge-evolution benchmark. The parameter \(\mu\) is not yet a measured physical coupling, and this generator is not automatically the MHD or Schrödinger Hamiltonian.

A continuum Lorentzian realization additionally needs a nondegenerate coframe \(e^a{}_\mu(x)\), a specified spin connection \(\omega^{ab}{}_\mu\), and a declared signature:
\[
g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu,\quad
T^a=de^a+\omega^a{}_b\wedge e^b,\quad
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]
The static spatial RGS coframe alone does not determine lapse, shift, time dependence or inertial spin connection.

## 3. Maxwell sector

### 3.1 Continuum

Let \(A\) be a U(1) potential, \(F=dA\), and \(J\) the electric current. With metric and orientation fixing the Hodge star,
\[
dF=0,\qquad d\star F=\star J
\]
up to unit conventions. The first equation is the homogeneous Maxwell/Bianchi identity; the second is the sourced equation. Gauge transformations \(A\mapsto A+d\chi\) leave F invariant.

The electromagnetic U(1) connection is not the quaternionic SU(2) spin/rotation connection. A U(1) subgroup can be embedded in unit quaternions only after choosing a fixed imaginary unit and a compatible representation.

### 3.2 Discrete Maxwell complex

For a discrete 1-cochain \(a\in C^1(K)\), define \(f=\delta_1a\in C^2(K)\). Exactly,
\[
\boxed{\delta_2 f=\delta_2\delta_1a=0.}\tag{3.1}
\]
This is the discrete homogeneous Maxwell identity. With a metric/Hodge operator \(\star_h\), the sourced equation has schematic form
\[
\delta_1\star_h f=j,
\]
where degree, dual-cell complex, boundary conditions and unit factors must be fixed in the implementation. The Hodge star is metric-dependent; incidence alone does not determine it.

If induced temporal cochain transport commutes with \(\delta\), the discrete Bianchi identity is preserved in time. This is the exact bridge between (2.1) and homogeneous Maxwell. Numerical tests must use oriented incidences, not unsigned face adjacency.

## 4. Quantum hydrodynamics: gauge-covariant Madelung map

For a charged scalar wavefunction
\[
\psi=\sqrt n\,e^{iS/\hbar},\qquad D_\mu=\partial_\mu-\frac{iq}{\hbar}A_\mu,
\]
the gauge-invariant phase gradient defines the nonrelativistic mechanical velocity
\[
\mathbf v=\frac{\nabla S-q\mathbf A}{m}.
\]
The minimally coupled Schrödinger equation with scalar potential \(\varphi\) and external potential V yields, away from zeros of \(\psi\),
\[
\partial_t n+\nabla\cdot(n\mathbf v)=0,
\]
\[
m(\partial_t+\mathbf v\cdot\nabla)\mathbf v
=q(\mathbf E+\mathbf v\times\mathbf B)-\nabla V-\nabla Q,
\quad
Q=-\frac{\hbar^2}{2m}\frac{\nabla^2\sqrt n}{\sqrt n}.
\]
These are standard Madelung equations where \(n>0\) and the phase is locally regular. At nodes, phase singularities and quantized circulation require separate treatment. A Pauli/spinor fluid adds spin density, magnetization and spin-gradient terms; these are not part of scalar Madelung theory.

For two Anti-Twin components \(\Psi=(\psi_+,\psi_-)^T\), let S exchange the components. The sheet-even/odd combinations
\[
\psi_e=\frac{\psi_++\psi_-}{\sqrt2},\qquad
\psi_o=\frac{\psi_+-\psi_-}{\sqrt2}
\]
diagonalize S. A common electromagnetic U(1) action and sheet-symmetric interaction preserve exchange symmetry. Different sheet potentials, masses, gauge couplings or boundary conditions mix the sectors.

A discrete QHD model must specify vertex density \(n_v\), compact phase \(\theta_v\), edge gauge integral \(a_e\), metric/Hodge inner product and discrete current. Its continuity equation must follow from a gauge-invariant discrete action or be verified as an exact balance law. A graph gradient alone is not a quantum velocity.

## 5. Maxwell–QHD coupling and MHD limit

For a nonrelativistic charged fluid, the minimal matter sources are
\[
\rho_q=qn,\qquad \mathbf j=qn\mathbf v,
\]
with magnetization/spin contributions only in a specified spin-fluid model. Maxwell's equations are sourced by this current; the fluid momentum equation contains \(q(\mathbf E+\mathbf v\times\mathbf B)\) and the quantum-potential force \(-\nabla Q\).

The conducting-fluid MHD closure is an additional approximation, not an identity:
\[
\mathbf E+\mathbf u\times\mathbf B=\eta_{\rm el}\mathbf J
\]
in a simple resistive Ohm law (unit convention to be declared). Ideal flux freezing requires the ideal limit and suitable regularity; resistivity permits reconnection. Quantum pressure, Hall response, spin magnetization and electron inertia may require additional terms.

The bridge is therefore
\[
\text{QHD matter current}\to\text{Maxwell source}
\to\text{Lorentz force}\to\text{MHD/QHD transport}.
\]
It does not identify vorticity with magnetic field, nor electromagnetic curvature with Cartan torsion.

## 6. Quaternionic and spinorial layer

In scalar-first convention,
\[
q=w+x\mathbf i+y\mathbf j+z\mathbf k,\quad
\mathbf i^2=\mathbf j^2=\mathbf k^2=\mathbf i\mathbf j\mathbf k=-1.
\]
Unit quaternions form \(S^3\simeq SU(2)\). Their action on a pure imaginary quaternion is
\[
v\mapsto qvq^{-1},
\]
giving the double cover \(SU(2)\to SO(3)\) with kernel \(\{\pm1\}\). This is the already-proved theorem T063; reuse it rather than relabel it as a new physical law.

For a spatial orthonormal frame (or declared time gauge), the rotational part of the spin connection can be represented by an \(\mathfrak{su}(2)\)-valued connection \(\mathcal A\), with
\[
\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A.
\]
A full Lorentzian spin connection instead uses \(\mathrm{Spin}(1,3)\simeq SL(2,\mathbb C)\); SU(2) is only the spatial rotation subgroup/time-gauge reduction.

The existing QAT quaternionic four-current convention is
\[
\mathcal J=c\rho+j_x\mathbf i+j_y\mathbf j+j_z\mathbf k.
\]
Conjugation by a unit quaternion preserves its scalar component and rotates its spatial current. This is a covariance identity, not a Maxwell equation or proof that the current is a connection.

A candidate covariant derivative on a combined matter doublet is
\[
\mathscr D_\mu=
\partial_\mu+\frac14\omega_{\mu ab}\gamma^{ab}
-\frac{iq}{\hbar}A_\mu I
+\mathcal A_\mu^{SU(2)}
+\mathcal A_\mu^{AT}.
\]
Each summand must act on a declared tensor factor. U(1), Lorentz-spin, optional SU(2) internal and Anti-Twin sheet connections are distinct representations. Terms on different factors commute; terms on the same factor require a common gauge convention. This is a definition template until the fibre representation and couplings are fixed.

## 7. Variational coupling: minimum requirements

A unified continuum model must be derived from an action of the schematic form
\[
S=S_{\rm geom}[e,\omega]+S_{\rm EM}[A,g]
+S_{\rm matter}[\Psi,A,e,\omega]
+S_{\rm AT}[\psi_+,\psi_-,e,\omega].
\]
The minimal electromagnetic term is \(-\frac14\int F\wedge\star F\). The matter term must yield the chosen Schrödinger/Pauli or relativistic Dirac equation in the declared limit. The Anti-Twin term must be exchange-invariant if exact Anti-Twin symmetry is claimed.

Variation must separately produce the matter equation, U(1) current and Maxwell source, stress-energy response to the coframe, spin current sourcing the Lorentz connection where the selected gravity theory permits it, and sheet-exchange selection/conservation rules.

No coupling constant between torsion, vorticity, magnetic field, density gradient or sheet exchange is assigned by analogy. It must follow from the action, symmetry and dimensions, or be labelled phenomenological and constrained by data.

## 8. Green–Kubo response

The existing Q6 face-cochain Green–Kubo result applies to its declared finite reversible OU generator and face Hodge operator. It is not automatically a QHD current correlator or MHD viscosity/resistivity. For a new model choose observable J, stationary/equilibrium measure and generator \(\mathcal L\), then derive
\[
\int_0^\infty\langle J(t)J(0)\rangle\,dt
=\langle J,(-\mathcal L)^{-1}J\rangle
\]
on the mean-zero subspace, only when reversibility/ergodicity and existence of the integral and inverse hold. The observable and normalization determine whether the coefficient is viscosity, conductivity, diffusion or another response.

## 9. Formal propositions and main candidate

**Proposition A — Anti-Twin cochain compatibility.** If the temporal transports satisfy (2.1), they induce maps on homology and cohomology. If they also commute with S, the induced maps preserve even and odd sectors.  
**Status:** exact algebraic consequence of the hypotheses.

**Proposition B — discrete Maxwell Bianchi preservation.** If \(f_n=\delta_1a_n\) and the induced cochain transports commute with the coboundary, then \(\delta_2f_n=0\) at every time slice.  
**Status:** exact finite-complex identity.

**Proposition C — quaternionic rotation covariance.** Unit-quaternion conjugation gives the SU(2) double cover of SO(3).  
**Status:** proved standard theorem T063, reused here.

**Proposition D — gauge-covariant Madelung equations.** On a region where \(\psi\ne0\), the minimally coupled Schrödinger equation is equivalent to continuity and quantum Hamilton–Jacobi/Madelung equations, subject to phase-branch and regularity conditions.  
**Status:** standard continuum result; Q6 discretization and Anti-Twin extension remain open.

**Main candidate — RGS–Q6–Anti-Twin spacetime compatibility theorem.** Given (i) an oriented Q6 chain complex; (ii) a nondegenerate Lorentzian coframe and declared spin connection on a continuum realization or controlled mesh family; (iii) chain-compatible temporal transports; (iv) gauge-covariant U(1) links; (v) a specified matter representation and gauge-invariant QHD/Dirac action; and (vi) sheet-symmetric Anti-Twin couplings, the induced discrete evolution preserves chain constraints, the homogeneous Maxwell identity and the even/odd Anti-Twin decomposition. In a consistent continuum limit, matter and Maxwell equations converge to the Euler–Lagrange system of the declared action.

**Proof status:** finite algebraic implications (i), (iii) and sheet-exchange commutation are conditionally proved; the Maxwell Bianchi implication is exact; quaternionic rotation is T063. The convergence assertion, action-derived RGS coupling, physical identification of the temporal generator and complete coupled field theory are open. This candidate must not be labelled proved before consistency, stability and convergence are established.

## 10. Repository dependencies and execution order

Reuse rather than duplicate:
- research/RGS_Q6_ANTITWIN_SPACETIME_BRIDGE_2026-11-27.md — finite Anti-Twin time transport and 4D-first sequencing.
- research/GRAVITOMAGNETISM_MHD_QHD_FLUXON_BRIDGE.md — standard MHD/QHD equations and physical distinctions.
- docs/RUBINO_QAT_QUATERNIONIC_SU2_BRIDGE.md — quaternionic current and SU(2) transport boundary.
- theorems/T063-quaternion-su2-so3-double-cover.md — proved quaternion/SU(2)/SO(3) theorem.
- theorems/S011-fdt-density-cone-riemann-cartan-kathara-maxwell.md — conditional Riemann–Cartan/Maxwell action and variational identities.
- src/rgs_fourth_moment_maxwell_bridge.py — fourth-moment-to-STF constitutive candidate; do not contract a fully symmetric rank-four tensor directly with two antisymmetric field strengths.
- tests/test_qat_quaternion_current_identities.py — existing quaternionic current covariance regression tests.
- theorems/Q6_FACE_COCHAINS_HODGE_GREEN_KUBO_2026-11-23.md — finite face Hodge/OU Green–Kubo result.

Implementation order:
1. Run the exact Anti-Twin temporal-chain audit and correct any failures.
2. Build the discrete U(1) potential/field-strength cochain pair and test \(\delta^2=0\), gauge covariance and discrete Gauss law.
3. Build the two-sheet QHD state, gauge-covariant current and exact total continuity balance.
4. Add quaternionic/SU(2) parallel transport using T063/T118 conventions; keep U(1) and SU(2) fibres distinct.
5. Specify continuum coframe/spin connection and derive the coupled action variations.
6. Only after the 4D layer is stable, resume the canonical 6D split and 3D cut-and-project derivation.

## 11. Status ledger

| Component | Status |
|---|---|
| Q6 oriented incidence and cochain Bianchi identity | Exact finite-complex identity |
| Anti-Twin sheet double and even/odd projectors | Exact algebra |
| Hodge-generated chain-compatible time evolution | Exact finite algebraic model; physical calibration open |
| Maxwell continuum equations and U(1) gauge invariance | Standard established theory |
| Discrete Maxwell \(f=\delta a,\ \delta f=0\) | Exact finite identity |
| Scalar Madelung equations | Standard continuum theory under stated regularity |
| Quaternionic SU(2) double cover | Proved T063 |
| QAT quaternionic current rotation | Existing algebraic identity/test |
| RGS-derived Maxwell constitutive anisotropy | Candidate with existing numerical audit, not fundamental Maxwell law |
| Coupled QHD–Maxwell–Anti-Twin action on RGS | Open |
| Quaternionic Lorentzian spin lift on actual RGS coframe | Open |
| TEGR/Einstein–Cartan field equations for this model | Open |
| Continuum/Mosco convergence from Q6 | Open |
| Canonical Q6 6D split and 3D cut-and-project | Open; retain T113-G boundary |
