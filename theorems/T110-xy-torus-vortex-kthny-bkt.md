# T110 — XY vortices on 2D and 3D tori: topology, loop closure, and KTHNY comparison

**Classification:** exact lattice identities for plaquette winding and 3D dual-flux closure; specified classical XY Monte Carlo protocol; finite-size numerical tests pending; KTHNY material identification open.

**Dependencies:** T099 (Gray-torus/Q6 geometry), T100 (charge correlations and Green–Kubo distinctions), T104 (cycle–cocycle–holonomy), T105 (hexagram-resolved measurements), T107 (the 2D Gray quotient and 3D (C_4^3) realization).

## 1. Scope and geometric realizations

There are two distinct finite geometries in the current program:

1. The full graph-preserving Gray realization (Q_6\cong C_4\square C_4\square C_4), which has 64 vertices and is a three-dimensional discrete torus graph.
2. The 16-vertex quotient (C_4\square C_4) used in T107 as a two-dimensional base with a four-state internal fibre.

They must not be conflated. The XY benchmark is run on periodic lattices (mathbb Z_L^d), (d=2,3). The case (L=4,d=3) reproduces the full (C_4^3) combinatorial graph; (L=4,d=2) is a 2D torus control. Larger (L) are finite-size extensions of the XY model, not larger Q6 graphs.

## 2. XY model and principal-link phases

Let (	heta_x\in(-\pi,\pi]) at each site of (mathbb Z_L^d), with periodic boundary conditions. For nearest-neighbour coupling (J>0),
\[
H_{XY}(\theta)=-J\sum_{x}\sum_{\mu=1}^{d}
\cos(\theta_{x+\hat\mu}-\theta_x).
\]
Define the principal link increment
\[
a_\mu(x)=\operatorname{wrap}_{(-\pi,\pi]}
(\theta_{x+\hat\mu}-\theta_x).
\]
For an oriented plaquette in the ((\mu,\nu)) plane,
\[
q_{\mu\nu}(x)=\frac{1}{2\pi}\left[
a_\mu(x)+a_\nu(x+\hat\mu)
-a_\mu(x+\hat\nu)-a_\nu(x)\right]\in\mathbb Z.
\]
The integer property follows because the unwrapped phase differences telescope around the plaquette and the remaining sum is an integer multiple of (2\pi).

### 2.1 Two dimensions: point vortices and torus winding

For (d=2), write (q_p=q_{12}(p)). On a periodic torus,
\[
\boxed{\sum_{p}q_p=0.}
\]
This is an exact global neutrality identity for the lattice plaquette vorticity. It does not mean that individual vortex charges cannot be created locally: local updates can create or annihilate vortex–antivortex pairs. The total signed charge is constrained, while the number of vortices is not conserved.

The two noncontractible torus cycles also carry winding data. For a chosen periodic row/column,
\[
W_\mu=\frac{1}{2\pi}\sum_{x\in\gamma_\mu}a_\mu(x)\in\mathbb Z.
\]
In a vortex-free smooth sector these encode the two harmonic winding numbers, corresponding to (H^1(T^2;\mathbb Z)\cong\mathbb Z^2). In a configuration containing vortices, winding measured on parallel cuts can differ by the total vorticity enclosed between the cuts. The code therefore records winding on every coordinate line rather than silently assigning one cut-independent integer to a configuration with defects.

The global neutrality identity is not a statement that all winding numbers vanish. Vortex charge on contractible plaquettes and harmonic winding around noncontractible cycles are different pieces of data.

### 2.2 Three dimensions: dual vortex flux and closed loops

For (d=3), the three plaquette fields are
\[
q_x=q_{23},\qquad q_y=q_{31},\qquad q_z=q_{12}.
\]
Under lattice duality they live on links of the dual cubic lattice. They are not point charges on primal plaquettes. The oriented sum around every elementary cube gives the exact discrete Bianchi identity
\[
\boxed{
\Delta_x q_x+\Delta_y q_y+\Delta_z q_z=0,
}
\]
where the forward difference is defined consistently with the plaquette anchoring convention in the audit script. Thus the dual vortex flux is divergence-free. Its support forms closed loop networks, including loops that can wind around periodic directions. At junctions, decomposing a network into individually labelled loops may require an explicit pairing convention; the divergence identity itself is unambiguous.

This is the correct 3D counterpart of 2D point-vortex vorticity. A 3D (C_4^3) test must therefore report dual-link flux and loop/network observables, not a 3D array of independent point-vortex charges.

## 3. Coulomb-gas reference in two dimensions

In the dilute continuum vortex-gas approximation, a neutral configuration with charges (q_i\in\mathbb Z), positions (r_i), and core energy (E_c) has
\[
H_{v}=
-2\pi J\sum_{i<j}q_iq_j
\log\frac{|r_i-r_j|}{a}
+E_c\sum_i q_i^2,
\qquad \sum_iq_i=0,
\]
up to boundary-condition-dependent constants and finite-torus Green-function corrections. Equivalently, the pair sum can be written with an ordered (i\ne j) sum and coefficient (-\pi J). This is a long-distance effective description; the lattice XY Hamiltonian remains the simulation's microscopic energy.

For a unit vortex–antivortex pair, the interaction cost grows logarithmically with separation. The logarithm belongs to the effective pair potential, not generically to the signed charge correlator (C_q(r)=\langle q(0)q(r)\rangle). To estimate an effective potential, measure a pair distribution (g_{+-}(r)) with a declared normalization and form the potential of mean force
\[
W_{+-}(r)=-k_BT\log g_{+-}(r)+\text{constant}.
\]
On a finite torus, use the periodic lattice Green function or explicitly report the distance range where the infinite-plane logarithm is a controlled approximation.

## 4. BKT and KTHNY are different benchmarks

For the 2D XY model with unit vortices, the BKT universal-jump criterion is
\[
\boxed{\frac{\Upsilon_R(T_{BKT})}{k_BT_{BKT}}=\frac{2}{\pi},}
\]
where \(\Upsilon_R\) is the long-distance renormalized helicity modulus (superfluid stiffness). It is not the bare coupling (J). In finite-size Monte Carlo, estimate the directional helicity modulus
\[
\Upsilon_\mu=
\frac{J}{N}\left\langle\sum_x\cos a_\mu(x)\right\rangle
-\frac{J^2}{Nk_BT}
\left\langle\left(\sum_x\sin a_\mu(x)\right)^2\right\rangle,
\]
and perform finite-size analysis; a single (L=4) crossing or a single bare \,\(\beta J\) value is not a transition determination.

KTHNY is instead a theory of 2D crystalline melting mediated first by dislocation unbinding and, at a higher temperature in the two-stage scenario, by disclination unbinding. Its dislocation-unbinding condition is conventionally written
\[
K_R=\frac{Y_Ra^2}{k_BT}=16\pi,
\]
where (Y_R) is the renormalized 2D Young modulus and (a) is the lattice spacing. The KTHNY gas is vector-valued in Burgers charge and includes elastic/angular structure. XY vortices are a useful scalar Coulomb-gas control, not a substitute for Burgers/Frank defects. A KTHNY test requires an independently specified 2D crystal, displacement/orientation fields, elastic constants, core energies, and calibrated Burgers and Frank observables.

The 3D XY model has vortex-loop proliferation and belongs to a different critical problem. KTHNY's 2D point-dislocation criterion cannot be applied to the 3D (C_4^3) realization.

## 5. Monte Carlo protocol and preregistered observables

The reproducible implementation is `scripts/audit_xy_torus_kthny_bkt.py`; its tests are in `tests/test_xy_torus_kthny_bkt.py`.

The script implements:
- nearest-neighbour XY energy and random-site Metropolis updates in (d=2,3);
- all oriented plaquette windings in 2D and all three plaquette orientations in 3D;
- total signed vorticity in 2D and the dual-flux divergence identity in 3D;
- winding numbers along every periodic coordinate line;
- directional helicity modulus;
- periodic radial-bin (C_q(r)) in 2D and vector-flux correlator in 3D.

Suggested protocol:
1. Validate exact identities on random phase configurations before thermal sampling.
2. Run (L=4) to reproduce the finite (C_4^2) and (C_4^3) controls, but do not use these sizes to claim scaling.
3. For the 2D XY/BKT study, run a size sequence such as (L=8,12,16,24,32), with independent seeds, burn-in checks, autocorrelation-aware errors, and temperature scans.
4. Locate BKT behaviour from helicity-modulus finite-size scaling and vortex-pair statistics. Do not fit (C_q(r)) directly to a logarithm as if it were the potential.
5. For 3D, measure dual vortex-loop/network length distributions, winding-loop statistics, and finite-size thermodynamic observables. Do not report BKT or KTHNY thresholds for this system.
6. For a separate KTHNY comparison, simulate or measure a 2D elastic crystal and calculate Burgers/Frank defects, renormalized elastic moduli, and defect fugacities.
7. Only after these controls, test any calibrated map from the Q6 two-field/circuit observables to the XY phase or elastic fields.

The implementation is an auditable baseline, not an optimized production Monte Carlo package. It does not yet trace individual loop identities through junctions, fit a periodic Coulomb potential, estimate critical exponents, or simulate the vector KTHNY Coulomb gas.

## 6. Exact identities and open claims

**Exact for the stated lattice definitions**
- 2D periodic plaquette vorticity is integer-valued and globally neutral.
- 3D plaquette vorticity maps to divergence-free dual-link flux.
- Winding along a specified periodic coordinate line is integer-valued.
- The Metropolis transition rule samples the stated nearest-neighbour XY Gibbs distribution in equilibrium, subject to adequate equilibration.

**Numerical tasks, not yet established**
- BKT finite-size scaling and the universal helicity-modulus jump.
- 3D vortex-loop distribution and critical scaling.
- Any relation between XY vortex observables and the Q6 circuit's 64 individual hexagram charges.

**Open physical bridge**
- KTHNY requires an independent 2D elastic model and calibrated Burgers/Frank observables.
- No identification of XY vortex charge with electric charge, Burgers vector, Frank angle, or the T104 \(\mathbb F_2\) plaquette flux is made here.

## References

1. J. M. Kosterlitz and D. J. Thouless, “Ordering, metastability and phase transitions in two-dimensional systems,” *J. Phys. C* 6 (1973), 1181. DOI: 10.1088/0022-3719/6/7/010.
2. D. R. Nelson and B. I. Halperin, “Dislocation-mediated melting in two dimensions,” *Phys. Rev. B* 19 (1979), 2457. DOI: 10.1103/PhysRevB.19.2457.
3. A. P. Young, “Melting and the vector Coulomb gas in two dimensions,” *Phys. Rev. B* 19 (1979), 1855. DOI: 10.1103/PhysRevB.19.1855.
4. P. Minnhagen, “The two-dimensional Coulomb gas, vortex unbinding, and superfluid-superconducting films,” *Rev. Mod. Phys.* 59 (1987), 1001. DOI: 10.1103/RevModPhys.59.1001.
5. P. Olsson, “Effective vortex interaction in the two-dimensional XY model,” *Phys. Rev. B* 46 (1992), 14598. DOI: 10.1103/PhysRevB.46.14598.
6. F. James, *Complex Langevin dynamics as a cure for the sign problem*, PhD thesis, Swansea University (2012), Chapter 4.4, “Vortex loops” (dual-lattice loop tracing; the thesis also studies the 3D XY model).
