# T113 — Gravitational mass of phonon–phason modes in quasiperiodic media

**Classification:** established parent result for ordinary fluids/solids; exact isotropic-limit regression; proposed variational extension to coupled quasiperiodic elasticity; no quasicrystal gravitational mass sign or measurement claimed.

**Dependencies:** T110 (vortex/phase-winding distinctions), T112 (triangular KTHNY control versus quasiperiodic phonon–phason sector), the three-defect-gas dossier, and the quasicrystal phonon–phason elasticity literature.

## 1. Research question

Can the gravitational mass carried by an acoustic wave packet be derived for coupled phonon–phason modes of a quasiperiodic solid, and can its sign depend on polarization, propagation direction, and phonon–phason hybridization?

This is a well-posed extension of a published result, not an established result for quasicrystals. The calculation must start from a generally covariant (or weak-field metric-coupled) effective action and define gravitational mass by variation with respect to the background metric. Refraction in a gravitationally stratified medium is an observable propagation effect, but by itself it is not a complete derivation of the source mass carried by the wave.

## 2. Established acoustic result: control limit

Esposito, Krichevsky and Nicolis, *Phys. Rev. Lett.* **122**, 084501 (2019), DOI: 10.1103/PhysRevLett.122.084501, derive for a sound packet in a nonrelativistic ordinary fluid

\[
M_g=-\frac{d\log c_s}{d\log\rho_m}\frac{E}{c_s^2},
\]

where the derivative is the appropriate adiabatic derivative along hydrostatic compression, \(E\) is packet energy, and \(\rho_m\) is the medium mass density. For ordinary solids the longitudinal and transverse branches have the corresponding elastic generalization, with their own speeds and energies.

If \(d c_s/d\rho_m>0\), this contribution is negative. The paper explains that in an external gravitational field the corresponding ray bends upward, while the wave packet also sources a tiny gravitational field. This is a nonlinear wave effect and survives the nonrelativistic limit. It is not a negative rest mass of the constituent atoms, nor a Lorentz-invariant particle mass in a boost-breaking medium.

The sign is not universal: it depends on the equation of state or elastic constitutive law through the derivative of the mode speed.

## 3. Quasiperiodic elastic variables

For a quasicrystal introduce physical phonon displacement \(u_i(x,t)\) and perpendicular-space phason displacement \(w_A(x,t)\). Their gradients are

\[
\varepsilon_{ij}=\tfrac12(\partial_i u_j+\partial_j u_i),
\qquad
\chi_{iA}=\partial_i w_A.
\]

A minimal quadratic elastic energy has block form

\[
F=\frac12
\begin{pmatrix}\varepsilon\\\chi\end{pmatrix}^{T}
\begin{pmatrix}C&R\\R^{T}&K\end{pmatrix}
\begin{pmatrix}\varepsilon\\\chi\end{pmatrix}.
\]

Here \(C\) is phonon elasticity, \(K\) phason elasticity, and \(R\) phonon–phason coupling. This is a constitutive template; tensor symmetries and allowed couplings depend on the quasicrystal point group.

The dynamical problem additionally requires inertia and, where appropriate, phason relaxation/dissipation. One must not assume that every phason branch is propagating: in many quasicrystal models phason dynamics is relaxational or diffusive. The acoustic mass formula applies only to well-defined propagating wave packets for which the relevant conserved energy and mode normalization are specified.

## 4. Definition by metric variation

Let the low-energy action be \(S[u,w;g_{\mu\nu}]\), including the background medium and its constitutive response. Define

\[
T^{\mu\nu}=\frac{2}{\sqrt{-g}}\frac{\delta S}{\delta g_{\mu\nu}}
\]

(up to the chosen stress-energy sign convention, which must be stated consistently). In a weak, static gravitational field, define the packet's excess gravitational mass by the appropriately background-subtracted, time-averaged energy density:

\[
M_{g,\alpha}=\frac1{c^2}
\int_{\mathcal V}\!d^3x\,
\left\langle\delta T_{00}^{(\alpha)}\right\rangle,
\]

where \(\mathcal V\) encloses the localized packet and the subtraction removes the unperturbed medium. The nonlinear correction to the wave and boundary/long-range contributions must be retained, as in the parent PRL calculation.

An equivalent weak-field definition may be obtained from the coefficient of the packet energy in the effective action's coupling to the Newtonian potential \(\Phi\), but the sign convention for \(g_{00}\) and \(\Phi\) must be fixed before comparing formulas.

## 5. Mode-resolved research target

For a conservative, nondissipative coupled model, Fourier transformation gives a generalized eigenproblem

\[
\mathcal K(\mathbf k;\rho_m)\,q_\alpha
=\omega_\alpha^2(\mathbf k;\rho_m)
\mathcal M(\mathbf k;\rho_m)\,q_\alpha,
\qquad q_\alpha=(u_\alpha,w_\alpha).
\]

The mode speed in the acoustic regime is direction- and branch-dependent:
\[
c_\alpha(\hat k;\rho_m)
=\lim_{k\to0}\frac{\omega_\alpha(k\hat k;\rho_m)}{k},
\]
provided this limit exists and is real and positive.

A tempting scalar generalization is
\[
M_{g,\alpha}\stackrel{?}{=}
-\frac{d\log c_\alpha}{d\log\rho_m}
\frac{E_\alpha}{c_\alpha^2}.
\]
This is **not asserted as a theorem** for a coupled quasicrystal. It is a testable candidate only if the metric variation, mode normalization, density path, and all phonon/phason constitutive parameters are varied consistently. In general, the metric-variation calculation may produce additional terms from density-dependent eigenvectors, phason relaxation, anisotropic stress, and mode mixing. The PRL isotropic-fluid/solid limits are mandatory regression cases.

## 6. Defects and geometric couplings

The quasicrystal defect sector is tracked independently:
- phonon/phason dislocation charge \(B=(b_{\parallel},b_{\perp})\);
- disclination/Frank holonomy;
- local curvature/torsion variables only after a discrete Cartan connection and coframe have been specified.

A defect can change the local elastic operator and hence the spectrum and packet energy. The proposed chain to test is

\[
(B,\Omega)\longrightarrow
(C,R,K,\mathcal M)_{\rm local}
\longrightarrow
(\omega_\alpha,q_\alpha)
\longrightarrow M_{g,\alpha}.
\]

This does not identify vorticity with Cartan curvature, or a superfluid vortex with a crystal dislocation. Circulation remains a separate phase/winding observable. Any cross-identification requires a derived map between the relevant complexes and conserved charges.

## 7. Falsifiable programme

1. Specify a quasicrystal symmetry class and the complete phonon–phason constitutive tensors.
2. Specify conservative phason inertia or a dissipative phason law; identify which modes are propagating.
3. Derive the weak-field action and stress-energy tensor by metric variation.
4. Compute the background-subtracted packet mass to quadratic order in amplitude, including nonlinear corrections and boundary terms.
5. Resolve the result by branch, wavevector direction, polarization, and phonon/phason content.
6. Recover the Esposito–Krichevsky–Nicolis fluid limit and the longitudinal/transverse isotropic-solid limits.
7. Add defects only after obtaining defect-free controls; compare spectra and packet masses for neutral pairs and isolated admissible defects.
8. Test sign and scaling across constitutive parameter families. Do not assume all branches have negative mass.
9. For dissipative phasons, formulate an open-system energy balance and do not apply a conservative normal-mode formula without modification.

## 8. Acceptance criteria and status

- **Established:** ordinary-fluid sound packets carry gravitational mass with the equation-of-state-dependent expression above; the published solid calculation includes longitudinal and transverse modes.
- **Established background:** phonon–phason coupling is part of quasicrystal elasticity and can alter acoustic anisotropy and attenuation.
- **Open target:** derive the gravitational mass of propagating coupled phonon–phason packets from metric variation.
- **Open target:** determine whether defect-induced changes in the elastic spectrum alter the sign or magnitude of the packet's gravitational mass.
- **Not claimed:** negative rest mass of matter; universal negative mass of all phonons/fasons; direct experimental detection in quasicrystals; a derived De Aquino threshold; a proven \(\varphi\)-dependence of gravitational mass.

## References

1. A. Esposito, R. Krichevsky, A. Nicolis, “Gravitational Mass Carried by Sound Waves,” *Physical Review Letters* **122**, 084501 (2019), DOI: 10.1103/PhysRevLett.122.084501.
2. S. B. Rochal, V. L. Lorman, “Anisotropy of acoustic-phonon properties of an icosahedral quasicrystal at high temperature due to phonon-phason coupling,” *Physical Review B* **62**, 874 (2000), DOI: 10.1103/PhysRevB.62.874.
3. S. B. Rochal, V. L. Lorman, “Minimal model of the phonon-phason dynamics in icosahedral quasicrystals and its application to the problem of internal friction in the i-AlPdMn alloy,” *Physical Review B* **66**, 144204 (2002), DOI: 10.1103/PhysRevB.66.144204.


## 9. Metric-action derivation appendix

The explicit covariant material-frame action, metric-variation prescription, generalized eigenvalue sensitivity identity, and falsifiable control sequence are developed in [T113-A](T113A-metric-action-phonon-phason-mode-sensitivity.md). The spectral sensitivity is not identified with gravitational mass until the full medium-plus-wave metric variation has been evaluated.
