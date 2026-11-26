# T124 — Frank–Read source: line-tension threshold, pinned-curve evolution and atomistic core input

**Classification:** PROVED within the stated constant-line-tension circular-arc model; MODEL-DEPENDENT for the critical stress of a material; OPEN for an RGS–PRISM derivation and for quantum-tunnelling rates.

**Purpose:** record the classical force balance, identify a common factor-of-two ambiguity in the quoted threshold, and specify where atomistic/quantum calculations enter. This record is a bridge to the dislocation and structured-deformation programme; it is not a claim that Frank–Read multiplication has already been derived from Q6.

## 1. Geometry and Peach–Koehler force

A dislocation segment of Burgers vector \(\mathbf b\), pinned at two endpoints separated by distance \(L\), lies in a slip plane. Under an applied stress tensor \(\boldsymbol\sigma\), the Peach–Koehler force per unit length is

\[
\mathbf f_{PK}=(\boldsymbol\sigma\cdot\mathbf b)\times\boldsymbol\xi,
\]

where \(\boldsymbol\xi\) is the unit tangent to the dislocation line (the sign depends on the chosen orientation convention). For resolved shear stress \(\tau\) in the active slip system, its glide component has magnitude

\[
f_{glide}=|\tau|\,|\mathbf b|.
\]

The scalar expression \(\tau b\) is therefore the resolved glide-force magnitude, not the full vector Peach–Koehler law in arbitrary stress geometry.

## 2. Constant line-tension approximation and critical arc

Assume a constant isotropic line tension \(T>0\), with units of force, and a circular bowed segment of radius \(R\). The restoring force per unit length due to line tension is \(T/R\). A stationary circular arc satisfies

\[
|\tau|b=\frac{T}{R}.
\]

At the semicircular configuration, the chord between the pinning points is the diameter, so \(R=L/2\). Hence the critical stress in this model is

\[
\boxed{\tau_c=\frac{2T}{bL}.}
\]

This identity is exact under the circular-arc and constant-line-tension assumptions.

A frequently used isotropic estimate is

\[
T\simeq \frac12 G b^2,
\]

where \(G\) is the shear modulus. Substitution gives

\[
\boxed{\tau_c\simeq \frac{Gb}{L}.}
\]

**Factor-of-two audit.** The often-quoted expression \(2Gb/L\) follows instead if one adopts \(T\simeq Gb^2\). It does not follow from the pair of assumptions \(T=Gb^2/2\) and \(R=L/2\). Any numerical comparison must state the line-tension convention, character (edge/screw/mixed), logarithmic cutoff and core correction. The line tension is generally not a universal constant: elastic line energy depends on character and length scale.

## 3. Frank–Read multiplication: what the force balance does and does not prove

For stress above the instability threshold, the pinned line bows out. In the idealized Frank–Read mechanism, the evolving line forms a loop; the two approaching portions reconnect/annihilate in the slip-plane construction, leaving an emitted closed dislocation loop and restoring a pinned source segment.

The force balance in §2 establishes a threshold for loss of the circular-arc equilibrium in the reduced model. It does **not**, by itself, prove the full nonlinear evolution, reconnection, topological cutting, or source regeneration. Those require a curve-evolution law and a rule for the topology change. In particular, the modern pinned-mean-curvature-flow model treats line tension, a slip-plane flow rule, pinning, remeshing and topological cutting as separate modelling ingredients.

## 4. Atomistic and quantum input

The continuum elastic field of an ideal dislocation is singular at the core. A core radius/cutoff and a core energy are therefore required to regularize continuum formulas. Atomistic calculations, including density-functional theory (DFT), can supply material-specific information about relaxed core structures, bonding, generalized stacking-fault energies and Peierls barriers. Such inputs can then inform a continuum or discrete-dislocation model.

The following distinctions are mandatory:

- DFT is a quantum-mechanical electronic-structure method; a DFT-derived parameter does not make the subsequent Frank–Read curve evolution quantum coherent.
- The Peierls barrier is a lattice-periodic resistance to dislocation glide. Its magnitude depends on crystal structure, dislocation character and core reconstruction.
- Thermally activated kink-pair nucleation and quantum tunnelling are distinct mechanisms. A nonzero tunnelling rate at very low temperature requires a specified effective action/mass, barrier profile, dissipation and coupling to phonons/electrons. It cannot be inferred merely from the existence of a Peierls barrier.
- Quantum tunnelling of an entire dislocation segment is not established by the classical Frank–Read force balance. It remains a separate low-temperature microscopic problem.

Thus the robust multiscale chain is

\[
\text{electronic/atomistic core data}
\longrightarrow
\text{core energy and Peierls landscape}
\longrightarrow
\text{effective line tension and mobility}
\longrightarrow
\text{pinned dislocation evolution}.
\]

Every arrow needs a declared coarse-graining or parameter-identification procedure.

## 5. RGS–PRISM / structured-deformation interface

The natural mathematical interface is the Burgers content of a line defect and its representation as a measure/current supported on a one-dimensional set. In a continuum description, dislocation density is encoded by the curl of the plastic distortion (up to the adopted sign and index convention). In structured deformations, the distinction between macroscopic deformation and the limiting microscopic deformation/disarrangement must be preserved.

A candidate discrete programme is:

1. represent oriented dislocation segments as 1-chains on a mesh, with Burgers labels in the lattice;
2. encode pinning points and slip-plane constraints as boundary/constraint data;
3. define a discrete line energy and Peach–Koehler work functional;
4. derive the discrete force as the first variation of that energy plus external work;
5. prove convergence of the energies and evolutions under a stated refinement regime;
6. only then compare the limiting evolution with pinned mean-curvature flow or a Frank–Read source.

The chain boundary records endpoint balance, but a closed emitted loop and reconnection require an explicit topological update. No such update is implied by \(\partial_1\partial_2=0\) alone.

**No current theorem is claimed** that derives Frank–Read multiplication, a material-specific Peierls stress, or a quantum tunnelling rate from Q6/RGS/PRISM. This is the open bridge to be developed.

## 6. References

1. T. Hudson, F. Rindler and J. Rydell, “A quantitative model for the Frank–Read dislocation source based on pinned mean curvature flow,” *Proceedings of the Royal Society A* **481** (2025), 20240740. DOI: [10.1098/rspa.2024.0740](https://doi.org/10.1098/rspa.2024.0740); [open Warwick repository record](https://wrap.warwick.ac.uk/191270/); [arXiv:2409.20294](https://arxiv.org/abs/2409.20294).
2. P. Cesana, L. De Luca and M. Morandotti, “Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method,” *SIAM Journal on Mathematical Analysis* **56** (2024), 79–136. DOI: [10.1137/22M1523443](https://doi.org/10.1137/22M1523443); [arXiv:2207.02511](https://arxiv.org/abs/2207.02511).
3. P. Cesana, E. Fabbrini and M. Morandotti, “Variational formulation of planar linearized elasticity with incompatible kinematics,” *Journal of Elasticity* **157** (2025), article 71. DOI: [10.1007/s10659-025-10161-5](https://doi.org/10.1007/s10659-025-10161-5); [arXiv:2503.18053](https://arxiv.org/abs/2503.18053).
4. T. Hudson and F. Rindler, “Elasto-plastic evolution of single crystals driven by dislocation flow,” *Mathematical Models and Methods in Applied Sciences* **32** (2022), 851–910. DOI: [10.1142/S0218202522500191](https://doi.org/10.1142/S0218202522500191).

## 7. Status and proof obligations

- **PROVED:** \(\tau_c=2T/(bL)\) for a constant-tension circular arc at the semicircle.
- **PROVED:** with the specific estimate \(T=Gb^2/2\), the preceding formula yields \(\tau_c=Gb/L\), not \(2Gb/L\).
- **MODEL-DEPENDENT:** quantitative threshold for a real crystal; requires character-dependent elastic line energy, core and pinning data.
- **REFERENCE MODEL:** pinned mean-curvature-flow dynamics and its numerical discretization, as in Hudson–Rindler–Rydell (2025).
- **OPEN:** discrete-chain/energy derivation on RGS–PRISM, convergence of the evolution, and coupling to the atomistic core.
- **OPEN:** any quantum-tunnelling contribution to source activation.
