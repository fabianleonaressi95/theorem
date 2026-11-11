# Morandotti–vorticity bridge: a controlled geometric extension

**Status:** research interface / candidate formulation. This document does not modify the published Morandotti model and makes no claim that FDT vorticity is identical to elastic torsion.

## 1. Scope

The useful FDT material for the two-core Morandotti problem is restricted to:

- circulation and transport of a 2-form;
- Kelvin-type balance and possible baroclinic production;
- constitutive coupling to stress and, only as a later application, superconducting flux.

The FDT claims about the universal stroke, Born rule, jet wake, and the numerical value of the maximum force are outside this benchmark.

## 2. Keep the geometric objects distinct

For a 2D material body, let (e^a) be a coframe and (omega^a{}_b) a connection. Define Cartan torsion and curvature by
\[
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]
For a region (S_i) surrounding core (i), the corresponding defect contents are represented (with the chosen connection and orientation conventions) by
\[
b_i^a=\int_{S_i}T^a,\qquad
\Omega_i{}^a{}_b=\int_{S_i}R^a{}_b.
\]
Here (b_i^a) is the Burgers vector and the curvature integral encodes Frank/disclination content. In a distributional idealization these are concentrated at the cores; in a regularized computation they are integrated over finite core neighborhoods.

Separately, for a velocity or momentum 1-form (u^\flat), define its kinematic vorticity by
\[
\varpi=du^\flat,\qquad d\varpi=0.
\]
An FDT-like medium 1-form \(\varsigma\) similarly gives
\[
W=d\varsigma,\qquad dW=0.
\]
The closure identities are mathematical identities. They do **not** imply
\(W=T^a\), (W=R^a{}_b\), or Maxwell's full equations. Torsion is vector-valued, curvature is endomorphism-valued, while (W) is an ordinary 2-form unless extra bundle structure is supplied.

## 3. Candidate bridge to the Morandotti data vector

The published finite-dimensional reconstruction uses
\[
\Phi_i=(s_i,\ s_i\xi_{i,1}+b_{i,2},\ s_i\xi_{i,2}-b_{i,1}),
\qquad \mathcal M a=\Phi,
\]
followed by
\[
v_h=-\frac{E}{1-\nu^2}\sum_j a_j\kappa_j^h,
\qquad \sigma_h=\operatorname{cof}(D^2v_h).
\]

A controlled extension is to test whether a separately computed circulation/transport field contributes a *new, explicitly parameterized source* to the defect data or to the constitutive law. It must not be silently folded into the Burgers or Frank entries.

Two admissible research routes are:

1. **Kinematic route:** compute \(\varpi=du^\flat\) from a prescribed material velocity and test its circulation around each core,
   \[
   \Gamma_i=\int_{S_i}\varpi=\oint_{\partial S_i}u^\flat.
   \]
   Compare \(\Gamma_i\) with the independently specified Burgers/Frank data. A correlation is a result to report, not an identification to assume.

2. **Cartan route:** construct \(e^a,\omega^a{}_b\) from the displacement/rotation fields and evaluate the integrated torsion and curvature. Check whether their core integrals reproduce the input \(b_i,s_i\) under the selected conventions.

The second route is the geometrically direct one for Morandotti. The first is an optional dynamical extension and requires a specified velocity field and evolution law.

## 4. Minimal numerical experiment

Use the existing two-core geometry \(\xi^1=(-0.28,0)\), \(\xi^2=(0.28,0)\), with the same mesh, core radius, material constants, and four defect cases already implemented in the C0-IPDG driver.

Add no phenomenological coupling initially. First compute and export:

- core-wise circulation \(\Gamma_i\) for a declared test velocity field (or mark it unavailable for the static problem);
- integrated torsion and curvature, if a coframe/connection has actually been constructed;
- the existing \(\Phi, a, v_h, \sigma_h\);
- stress/traction residuals and energy on each mesh level.

Then test mesh convergence of each quantity separately. A coupling coefficient may be introduced only after a dimensionally consistent constitutive law is stated and independently calibrated. Do not fit it to force agreement with the same two-core data used to define it.

## 5. Kelvin/baroclinic extension: only for a dynamic model

For a time-dependent medium, a Kelvin-type circulation balance requires a specified momentum equation and constitutive variables. A baroclinic source requires independent fields (for example density and temperature/entropy) and a derived term of the form \(\nabla T\times\nabla s\). The current Morandotti C0-IPDG calculation is static; it contains neither a velocity evolution nor thermal variables. Therefore these terms are **not implemented** and cannot explain changes in the current static solution.

## 6. Stress and traction acceptance gates

For every mesh level and defect case, report:

1. \(\|\mathcal M a-\Phi\|_2\), symmetry defect, smallest eigenvalue and condition estimate of \(\mathcal M\);
2. outer-boundary and each-core traction norms separately;
3. interior-facet traction jump using the stated elementwise Hessian convention;
4. stress and energy differences between successive mesh levels;
5. comparison against an independent analytic benchmark with identical geometry, core radius, material parameters, and boundary conditions.

The current driver contains source-level stress/traction diagnostics, but these gates remain **unexecuted** until the DOLFINx run is performed. The algebraic unit tests do not validate these FE quantities.

## 7. Superconducting extension is a separate benchmark

The London relation and flux quantum may motivate a later material application, but they are not part of the present elastic reconstruction. A superconducting test would need a specified order parameter, electromagnetic potential, penetration depth, coherence length, boundary conditions, and a coupled free-energy functional. Only then could vortex/flux-tube positions be compared with elastic defect cores. No universal identification of a flusson with a dislocation or disclination is assumed here.

## 8. Epistemic status

- Cartan definitions and Stokes circulation identity: **standard mathematical framework**.
- Morandotti map \(\Phi\mapsto a\mapsto v_h\): **implemented algebraic reconstruction** in this branch.
- FDT-medium-form coupling to elastic torsion/stress: **open candidate**, not derived.
- Kelvin/baroclinic dynamics: **not in the static model**.
- Superconducting flux coupling: **separate future application**.
- End-to-end two-core stress validation: **pending DOLFINx execution and independent benchmark**.

The acceptance principle is simple: add no FDT coupling until the uncoupled Morandotti reconstruction passes its numerical gates.
