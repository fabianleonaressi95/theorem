# T113-B — Explicit acoustic gravitational-mass control: fluid and isotropic solid

**Classification:** reproduction/derivation of the published Esposito–Krichevsky–Nicolis (EKN) control result. This is not a new result and is not yet the quasicrystal extension.

**Primary reference:** A. Esposito, R. Krichevsky, A. Nicolis, “Gravitational Mass Carried by Sound Waves,” *Physical Review Letters* 122, 084501 (2019), DOI: 10.1103/PhysRevLett.122.084501; arXiv:1807.08771.

## 1. Physical quantity and sign

For a localized, time-averaged acoustic packet of energy \(E\), the nonrelativistic gravitational mass in an ordinary fluid is

\[
\boxed{M_g=-\frac{d\log c_s}{d\log\rho_m}\frac{E}{c_s^2}.}
\]

The derivative is the adiabatic derivative along hydrostatic compression. The sign is material-dependent:
- if \(dc_s/d\rho_m>0\), then \(M_g<0\);
- if \(dc_s/d\rho_m<0\), then \(M_g>0\);
- if the derivative vanishes, this leading contribution vanishes.

This is the gravitational mass carried by a wave packet in a medium, not a negative rest mass of the atoms or molecules. It is a nonlinear effect: a linearized calculation alone gives zero net transported mass.

## 2. Fluid EFT and metric variation

Use the relativistic fluid EFT
\[
S=\int d^4x\sqrt{-g}\,P(X),\qquad
X=-c^2g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi.
\]
With the convention
\[
T_{\mu\nu}=-\frac{2}{\sqrt{-g}}\frac{\delta S}{\delta g^{\mu\nu}},
\]
the stress-energy tensor is
\[
T_{\mu\nu}=P(X)g_{\mu\nu}
+2c^2P'(X)\partial_\mu\phi\partial_\nu\phi.
\]
The background chemical potential and number density obey
\[
n=\frac{dP}{d\mu},\qquad
\rho+P=\mu n,\qquad dP=n\,d\mu.
\]

Expand the phase field around a homogeneous state, \(\phi=\bar\phi+\pi\). The quadratic phonon action gives the sound speed \(c_s\). To compute the packet's mass, the stress-energy must be expanded through quadratic order in the wave and the nonlinear correction to the wave solution must be retained. The latter is sourced by quadratic combinations of the linear wave. Omitting it is not a valid calculation of the net packet mass.

After spatial integration and time averaging over many oscillations, the linear total-derivative terms vanish. The quadratic terms are related to the packet energy by the virial identity for a localized acoustic solution. EKN obtain
\[
\left\langle\int d^3x\,T_{00}\right\rangle
=\left(1-\mu c_s\frac{dc_s}{d\mu}\right)E
=\left(1-\frac{\rho+P}{c_s}\frac{dc_s}{dP}\right)E.
\]
Taking the nonrelativistic limit, with \(\rho=\rho_m c^2+o(c^2)\), and using the adiabatic thermodynamic relations gives
\[
M_g=\frac1{c^2}\left\langle\int d^3x\,T_{00}\right\rangle
\simeq
-\frac{\rho_m}{c_s}\frac{dc_s}{d\rho_m}\frac{E}{c_s^2}
=-\frac{d\log c_s}{d\log\rho_m}\frac{E}{c_s^2}.
\]

The cancellation of the leading rest-energy contribution and the surviving term depend on the nonlinear medium response. The formula is not obtained by treating the sound packet as a point particle with an assumed inertial mass.

## 3. Isotropic solid control

For an isotropic elastic solid, longitudinal and transverse branches have different speeds and energies. EKN derive the mode-resolved nonrelativistic result
\[
\boxed{
M_g=-\frac{d\log c_L}{d\log\rho_m}\frac{E_L}{c_L^2}
-\frac{d\log c_T}{d\log\rho_m}\frac{E_T}{c_T^2},
}
\]
when both components are included in a packet; after the branches spatially separate, each packet obeys its own term. The derivatives are taken under hydrostatic compression, with no pure shear. This is the relevant solid control for any anisotropic extension.

## 4. Exact power-law regression

For
\[
c_s(\rho_m)=c_0(\rho_m/\rho_0)^\alpha,
\]
one has
\[
\frac{d\log c_s}{d\log\rho_m}=\alpha,
\qquad
M_g=-\alpha\frac{E}{c_s^2}.
\]
Thus the sign is controlled by \(\alpha\), not fixed universally. The regression in `scripts/audit_t113_quasicrystal_phonon_gravity.py` checks this logarithmic derivative and its mass consequence.

## 5. What this does and does not say about quasicrystals

For a quasicrystal, the propagating modes are eigenvectors of a coupled phonon–phason dynamical matrix. A branch may depend on propagation direction, polarization, density, and phonon–phason mixing. Replacing \(c_s\) by a branch speed \(c_\alpha(\hat k)\) in the fluid formula is a **candidate**, not an established theorem.

The proper extension must:
1. specify the icosahedral (or other) point group and its invariant phonon, phason, and mixed elastic tensors;
2. specify whether the phason mode is propagating or relaxational;
3. couple the complete material-frame action to the metric;
4. vary the metric, including the material frame and constitutive tensors;
5. solve the nonlinear packet response and compute the background-subtracted integrated \(T_{00}\);
6. recover the fluid and isotropic-solid limits above.

Defects enter only after the defect-free control is passed. Burgers and Frank charges may alter local constitutive coefficients and mode spectra; circulation and vorticity remain distinct hydrodynamic observables unless a concrete coupled action derives their relation.

## 6. Reproducibility and status

- **Established parent result:** EKN 2019 fluid and isotropic-solid acoustic packet mass.
- **Reproduced algebraic regression:** power-law speed dependence and sign.
- **Open:** full metric-derived packet mass of coupled phonon–phason modes in an icosahedral quasicrystal.
- **Not claimed:** universal negative phonon/fason mass, an experimental quasicrystal measurement, or a derived \(\varphi\)- or De Aquino-dependent gravitational threshold.
