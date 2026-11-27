# Vesica–Moiré TM_z Maxwell polarization audit

**Research extension — 2026-11-27**  
**Status:** a 2-D polarization-reduced Maxwell eigenproblem is specified and implemented; full 3-D vector Maxwell and the physical origin of the constitutive modulation remain open.  
**Classification:** numerical model with an explicit constitutive ansatz, not a new law.

## 1. Why this is the next step

The earlier Vesica–Moiré experiment used a scalar weighted graph Laplacian. That operator is mathematically useful but is not, by itself, an electromagnetic model. This extension makes a controlled step toward Maxwell by using the exact two-dimensional TM_z polarization reduction.

Assume fields independent of z:
\[
\mathbf E=(0,0,E_z(x,y,t)),\qquad
\mathbf H=(H_x(x,y,t),H_y(x,y,t),0).
\]
For an isotropic, lossless medium with scalar relative permittivity \(\varepsilon_r(x,y)>0\) and constant relative permeability \(\mu_r=1\), source-free Maxwell gives
\[
\varepsilon_r\,\partial_t E_z
 = \partial_x H_y-\partial_y H_x,
\]
\[
\partial_t H_x=-\partial_y E_z,\qquad
\partial_t H_y=\partial_x E_z.
\]
In normalized units with \(c=1\), eliminating \(H_x,H_y\) yields
\[
\varepsilon_r\,\partial_t^2 E_z=\Delta E_z.
\]
Restoring physical units gives \(\varepsilon_r\,\partial_t^2 E_z=c^2\Delta E_z\).
For harmonic fields \(E_z=e(x,y)e^{-i\omega t}\),
\[
-\Delta e=(\omega/c)^2\varepsilon_r e
\]
when lengths are expressed in consistent units and c is restored. Equivalently:
\[
K e=(\omega/c)^2 M_\varepsilon e.
\]
This is the TM_z (out-of-plane electric field) scalar polarization of vector Maxwell, not the full 3-D vector system. It is exact for the stated 2-D isotropic setting.

## 2. Vesica–Moiré constitutive ansatz

Keep the two radial phases:
\[
\rho_1=\sqrt{(x+a)^2+y^2},\quad
\rho_2=\sqrt{(x-a)^2+y^2},\quad
\Delta\phi=k_g(\rho_1-\rho_2).
\]
For this experiment only, posit
\[
\boxed{\varepsilon_r(x,y)=1+\eta\cos\Delta\phi(x,y)},\qquad |\eta|<1,
\]
with \(\mu_r=1\).

This is an assumed spatially modulated dielectric. The geometry does not derive this constitutive law. The modulation parameter \(\eta\) is dimensionless and is not fitted to the optical spectrum. Since \(1-|\eta|\le\varepsilon_r\le1+|\eta|\), the dielectric mass is strictly positive for \(|\eta|<1\).

The ansatz is a physically interpretable test medium, not a claim that vacuum permittivity varies with Vesica geometry. A later model could instead vary \(\mu_r\), use anisotropic tensors, or derive constitutive tensors from a separate microstructure homogenization.

## 3. Discrete problem

Use an N-by-N interior Cartesian grid with spacing \(h=L/(N+1)\), and PEC boundary condition \(E_z=0\) on the box boundary. The five-point Dirichlet stiffness is
\[
K=\frac{1}{h^2}(T\otimes I+I\otimes T),
\quad T=\operatorname{tridiag}(-1,2,-1).
\]
The diagonal dielectric mass is
\[
M_\varepsilon=\operatorname{diag}\{\varepsilon_r(x_i,y_j)\}.
\]
The discrete generalized eigenproblem is
\[
K e_j=\lambda_j M_\varepsilon e_j,\qquad
\lambda_j=(\omega_j/c)^2.
\]
Because K is symmetric positive definite under the PEC Dirichlet condition and M is symmetric positive definite for |eta|<1, all generalized eigenvalues are real and strictly positive.

For the uniform control eta=0, the exact discrete eigenvalues are
\[
\lambda_{pq}^{(0)}=\frac{4}{h^2}\left[
\sin^2\frac{p\pi}{2(N+1)}+
\sin^2\frac{q\pi}{2(N+1)}
\right],\quad 1\le p,q\le N.
\]
The implementation compares the numerical uniform spectrum with this formula before interpreting any Moiré shifts.

## 4. Reproducible numerical example

Default parameters: N=24, L=8, a=1, k_g=pi/2 in normalized inverse-length units, eta=0.10, PEC boundary, mu_r=1.

The computed relative permittivity lies between approximately 0.9000005 and 1.0991340. For the first nine modes, the normalized frequency shifts sqrt(lambda_M/lambda_0)-1 are:

| Mode | Shift (%) |
|---:|---:|
| 1 | +0.669 |
| 2 | -0.780 |
| 3 | +3.581 |
| 4 | +2.104 |
| 5 | -0.557 |
| 6 | +2.133 |
| 7 | +1.292 |
| 8 | +2.166 |
| 9 | -0.803 |

These are outputs of the declared dimensionless model, not optical frequencies or predictions for the measured electromagnetic spectrum. They depend on the chosen domain, boundary condition, grid, grating scale and dielectric ansatz. Degeneracy splitting in this finite box is not, by itself, evidence of a universal spectral law.

## 5. Energy and stability

The semidiscrete time-domain equation is
\[
M_\varepsilon\ddot e+c^2Ke=0.
\]
Its conserved energy is
\[
\mathcal H=\frac12\dot e^\top M_\varepsilon\dot e
+\frac{c^2}{2}e^\top K e.
\]
Positivity of M and K makes this energy positive definite. A time integrator must preserve or control this energy according to its stability properties; the current implementation solves the generalized eigenproblem and does not claim a time-domain energy-conservation experiment.

## 6. What this does establish — and what remains open

Established for this discrete model:
- the TM_z polarization reduction follows from the stated Maxwell assumptions;
- the Moiré dielectric ansatz is positive for |eta|<1;
- the PEC stiffness and dielectric mass define a symmetric positive generalized eigenproblem;
- the uniform discrete spectrum has a closed-form benchmark;
- the modulation changes the normalized modal spectrum for the declared finite example.

Not established:
- a derivation of epsilon_r from circle geometry, Q6, or RGS;
- full 3-D vector Maxwell, general TE/TM coupling, anisotropic media or sources;
- topological defects or quantized dislocations;
- a mechanism for generating light;
- a mapping from dimensionless eigenvalues to visible-light frequencies;
- a match to the measured electromagnetic spectrum.

## 7. Next validation gates

1. Grid refinement at fixed physical domain and fixed k_g; compare eigenfrequencies and mode shapes.
2. Vary eta and verify convergence to the uniform result as eta tends to zero.
3. Compare finite-difference results with a compatible FEEC/edge-element or Yee discretization.
4. Implement the time-domain first-order TM_z Maxwell system and monitor discrete energy and Gauss constraints.
5. Only after numerical convergence, investigate whether a constitutive tensor can be derived independently from an RGS microstructure.

## Files

- audits/vesica_moire_tmz_maxwell.py — reproducible generalized eigenproblem, JSON/CSV output and optional coefficient plot.
- tests/test_vesica_moire_tmz_maxwell.py — uniform analytic spectrum, positivity, symmetry and zero-modulation controls.
