# De Aquino molecular-response programme: H₂ neutral benchmark

**Status:** research programme / open numerical test.  
**Repository classification:** candidate mechanism; no H₂-neutral value of \(\chi_{\rm DA}\) is claimed here.  
**Scope:** transfer the fixed prolate De Aquino region from H₂⁺ to the correlated two-electron ground state of neutral H₂, without refitting the geometric threshold.

## 1. Fixed geometric definition

For nuclei at \(z=\pm R/2\), use prolate spheroidal coordinates

\[
\xi=\frac{r_A+r_B}{R},\qquad
\eta=\frac{r_A-r_B}{R},\qquad
\phi\in[0,2\pi),
\]

with \(1\leq\xi<\infty\), \(-1\leq\eta\leq1\), and volume element

\[
d^3r=\frac{R^3}{8}(\xi^2-\eta^2)\,d\xi\,d\eta\,d\phi.
\]

Keep the threshold fixed:

\[
\xi_\star=\frac{\sqrt5}{2}.
\]

No system-dependent rescaling of \(\xi_\star\), no fitted boundary, and no substitution of ellipsoid surface-area measure for the volume measure are permitted in the primary test.

## 2. Two-electron Born–Oppenheimer Hamiltonian

At fixed internuclear distance \(R\), in atomic units and with a uniform electric field \(F\) along the internuclear axis,

\[
H(F;R)=
-\frac12(\nabla_1^2+\nabla_2^2)
-\sum_{i=1}^2\left(\frac1{r_{iA}}+\frac1{r_{iB}}\right)
+\frac1{r_{12}}+\frac1R
+F(z_1+z_2).
\]

The sign of the field term corresponds to the electronic potential energy for a field directed along +z. Reversing the field convention changes \(F\to-F\), but not the second derivative at zero field.

The target state is the correlated electronic ground state \(X\,{}^1\Sigma_g^+\). The electron-electron repulsion \(1/r_{12}\) must be retained. A product of two one-electron H₂⁺ orbitals is not an acceptable final H₂ model.

## 3. Reduced density and geometric probability

Let the normalized two-electron wavefunction satisfy

\[
\int |\Psi_F(\mathbf r_1,\mathbf r_2;R)|^2\,
d^3r_1d^3r_2=1.
\]

Define the spin-summed one-electron density

\[
\rho_F(\mathbf r;R)=
2\int |\Psi_F(\mathbf r,\mathbf r_2;R)|^2\,d^3r_2,
\qquad
\int\rho_F(\mathbf r;R)d^3r=2.
\]

The De Aquino electron fraction is

\[
P_{\rm DA}^{H_2}(F,R)=
\frac12\int_{\xi(\mathbf r)\leq\xi_\star}
\rho_F(\mathbf r;R)\,d^3r.
\]

Thus \(0\leq P_{\rm DA}^{H_2}\leq1\). The factor \(1/2\) is essential: the reduced density integrates to two electrons. The integral is a volume probability, not a probability on the ellipsoid boundary.

The response observable is

\[
\boxed{
\chi_{\rm DA}^{H_2}(R)=
\left.\frac{\partial^2P_{\rm DA}^{H_2}(F,R)}
{\partial F^2}\right|_{F=0}.
}
\]

For the nondegenerate gerade ground state, inversion symmetry implies
\(P_{\rm DA}^{H_2}(F,R)=P_{\rm DA}^{H_2}(-F,R)\). Therefore the linear term vanishes. A central finite-field estimate is

\[
\chi_{\rm DA}^{H_2}(R;F)=
\frac{P_{\rm DA}^{H_2}(F,R)+P_{\rm DA}^{H_2}(-F,R)
-2P_{\rm DA}^{H_2}(0,R)}{F^2}.
\]

The estimate must be checked at multiple field strengths and extrapolated or shown stable as \(F\to0\). The numerical sign is to be measured, not assumed from the H₂⁺ result.

## 4. Independent polarizability benchmark

Zammit et al., *Physical Review A* **95**, 022707 (2017), DOI:
[10.1103/PhysRevA.95.022707](https://doi.org/10.1103/PhysRevA.95.022707).

Their Table II reports static fixed-nuclei H₂ polarizabilities as functions of internuclear distance. It gives both the authors' values and comparison values from the accurate calculations of Kolos and Wolniewicz. For the primary comparison below, use the **Kolos–Wolniewicz reference columns**, not the less accurate “Present” columns of the scattering model.

All values are in atomic units. The anisotropy is calculated here as
\(\Delta\alpha=\alpha_\parallel-\alpha_\perp\).

| \(R/a_0\) | \(\alpha_\parallel\) (Kolos–Wolniewicz) | \(\alpha_\perp\) (Kolos–Wolniewicz) | \(\Delta\alpha\) |
|---:|---:|---:|---:|
| 0.8 | 3.204 | 2.783 | 0.421 |
| 1.0 | 4.088 | 3.341 | 0.747 |
| 1.2 | 5.147 | 3.944 | 1.203 |
| 1.4 | 6.380 | 4.578 | 1.802 |
| 1.6 | 7.781 | 5.228 | 2.553 |
| 1.8 | 9.320 | 5.878 | 3.442 |
| 2.0 | 10.964 | 6.511 | 4.453 |
| 2.2 | 12.638 | 7.110 | 5.528 |

**Comparison caveat.** The reference values above are the literature comparison column reproduced in Table II, not new calculations performed in this repository. The article notes that its own structure model becomes less accurate as \(R\) increases beyond equilibrium. Do not silently mix the two columns.

## 5. Numerical protocol required for an H₂ result

A valid computation must solve the correlated two-electron fixed-nuclei problem for every \((R,F)\) pair.

Recommended routes:

1. **Primary route:** explicitly correlated Gaussian (ECG) or high-quality Hylleraas-type variational basis, optimized separately or systematically at each \(R\), with singlet spatial symmetry.
2. **Alternative route:** prolate-coordinate configuration interaction with a documented one-electron orbital basis, a converged virtual-orbital space, and explicit treatment of the electron-electron Coulomb matrix elements.
3. For each field, compute the normalized two-electron state and its one-electron reduced density. Integrate the density over the fixed region \(1\leq\xi\leq\sqrt5/2\).
4. Report total BO energy, basis size, energy convergence, density normalization error, quadrature error, and \(P_{\rm DA}(0,R)\).
5. Evaluate symmetric fields \(\pm F\) at at least three decreasing magnitudes. Demonstrate stability of \(\chi_{\rm DA}\) against both field-step and basis refinement. Check that the odd-in-\(F\) component is at numerical noise level.
6. Validate the zero-field energy against high-accuracy H₂ BO benchmarks and validate the static dipole polarizability against the reference values in Section 4 before interpreting the De Aquino response.

A finite-field CI basis can represent the Stark response poorly if the diffuse/continuum sector is truncated. Basis convergence of the energy alone is insufficient: the regional density response itself must converge.

## 6. Falsifiable cross-system test

Only after obtaining converged H₂ values, fit

\[
\Delta\alpha_{H_2}(R)=A_{H_2}
|\chi_{\rm DA}^{H_2}(R)|^{s_{H_2}}.
\]

Report both ordinary and log-space residuals, confidence intervals, and leave-one-out predictions. Because all points lie on one smooth dissociation curve, a high in-sample \(R^2\) is not by itself evidence of a universal law.

The H₂⁺ exploratory relation previously reported in the working discussion,

\[
\Delta\alpha_{H_2^+}\approx
2.02465|\chi_{\rm DA}^{H_2^+}|^{0.84683},
\]

is a **provisional benchmark from that calculation session**, not a result independently reproduced by the files in this repository. It must not be used as a fixed constraint or as a prior imposed on H₂. Recompute and archive the H₂⁺ data and its convergence record before making a quantitative universality claim.

The decisive test is whether the same geometric region and observable definition produce a stable relation across H₂⁺ and H₂, with no system-specific adjustment of \(\xi_\star\). The constants and exponent may be compared, not forced to agree. A subsequent heteronuclear test (e.g. LiH or HeH⁺) must separately document the choice of internuclear axis and account for the loss of inversion symmetry.

## 7. Current evidence classification

| Item | Classification |
|---|---|
| Prolate coordinate map and volume Jacobian | Analytic identity |
| Fixed threshold \(\xi_\star=\sqrt5/2\) | Adopted geometric hypothesis |
| Definition of \(P_{\rm DA}^{H_2}\) | Defined observable |
| Definition and even-field symmetry of \(\chi_{\rm DA}^{H_2}\) | Analytic consequence, subject to the stated ground-state symmetry |
| H₂ polarizability reference data | Published benchmark |
| H₂ correlated field-dependent density | Not yet computed in this repository |
| H₂ value of \(\chi_{\rm DA}\) | Open numerical task |
| H₂ power law and cross-system universality | Open hypothesis |

**No theorem or physical law is claimed.** This file specifies a reproducible and falsifiable research test and records the correct benchmark data. A numerical result may be promoted only after the density-response and convergence requirements above are met.

## References

1. M. C. Zammit, D. V. Fursa, J. S. Savage, I. Bray, L. Chiari, A. Zecca, and M. J. Brunger, “Adiabatic-nuclei calculations of positron scattering from molecular hydrogen,” *Phys. Rev. A* **95**, 022707 (2017). DOI: [10.1103/PhysRevA.95.022707](https://doi.org/10.1103/PhysRevA.95.022707). Table II: static fixed-nuclei polarizabilities and comparison with Kolos–Wolniewicz.
2. W. Kolos and L. Wolniewicz, high-accuracy calculations cited as Ref. [46] in Zammit et al.; the tabulated comparison values are used here as reported in their Table II. The original bibliographic details should be resolved from the reference list before a standalone publication.
