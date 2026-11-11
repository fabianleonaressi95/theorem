# Morandotti–vorticity bridge: controlled geometric extension

**Status:** research interface / candidate formulation. This note does not modify the published Morandotti model and does not identify FDT vorticity with elastic torsion.

## 1. Scope

Only four FDT motifs are relevant to the two-core Morandotti problem: circulation, transport of a 2-form, Kelvin-type balance, and possible constitutive coupling to stress. The stroke, Born rule, jet wake, and universal-force claims are outside this benchmark.

## 2. Keep the geometric objects distinct

For a material coframe (e^a) and connection (omega^a{}_b), Cartan torsion and curvature are
\[
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]
For a region (S_i) around core (i), defect contents are represented, with fixed orientation and connection conventions, by
\[
b_i^a=\int_{S_i}T^a,\qquad
\Omega_i{}^a{}_b=\int_{S_i}R^a{}_b.
\]
The first encodes Burgers/dislocation content; the second encodes Frank/disclination content.

Separately, a velocity or momentum 1-form (u^\flat) defines kinematic vorticity
\[
\varpi=du^\flat,\qquad d\varpi=0,
\]
and an FDT-like medium 1-form \(\varsigma\) defines
\[
W=d\varsigma,\qquad dW=0.
\]
These closure identities do **not** imply (W=T^a), (W=R^a{}_b), or the full Maxwell system. Torsion is vector-valued, curvature is endomorphism-valued, and (W) is an ordinary 2-form unless additional bundle structure is supplied.

## 3. Interface with the published Morandotti reconstruction

The finite-dimensional reconstruction uses
\[
\Phi_i=(s_i,\ s_i\xi_{i,1}+b_{i,2},\ s_i\xi_{i,2}-b_{i,1}),
\qquad \mathcal M a=\Phi,
\]
and
\[
v_h=-\frac{E}{1-\nu^2}\sum_j a_j\kappa_j^h,
\qquad \sigma_h=\operatorname{cof}(D^2v_h).
\]
The Burgers and Frank data already enter through \(\Phi\). A vorticity variable must therefore remain an independent observable/source until a dimensionally consistent constitutive map is derived. It must not be silently added to or substituted for the Burgers/Frank entries.

Two possible research routes:

1. **Kinematic route:** for a prescribed material velocity, compute
   \[
   \Gamma_i=\int_{S_i}\varpi=\oint_{\partial S_i}u^\flat.
   \]
   Compare \(\Gamma_i\) with independently specified Burgers/Frank data. Correlation is a result to test, not an identity to assume.
2. **Cartan route:** construct \(e^a,\omega^a{}_b\) from displacement/rotation fields and integrate torsion and curvature around each core. Check whether the resulting integrals reproduce the input \(b_i,s_i\) under the selected conventions. This is the geometrically direct route for dislocation/disclination theory.

## 4. Minimal numerical experiment

Use the existing two-core geometry \(\xi^1=(-0.28,0)\), \(\xi^2=(0.28,0)\), identical mesh, core radius, material constants, and four defect cases in the C0-IPDG driver.

First add **no phenomenological coupling**. Export, when defined:

- core-wise circulation \(\Gamma_i\) for a declared test velocity (otherwise mark it unavailable in the static problem);
- integrated torsion and curvature, only if a coframe/connection has actually been constructed;
- existing \(\Phi,a,v_h,\sigma_h\);
- traction residuals and energy on each mesh level.

Test mesh convergence of each quantity separately. Introduce a coupling coefficient only after stating a dimensionally consistent constitutive law and calibrating it independently of the same two-core data.

## 5. Kelvin/baroclinic extension is dynamic, not static

A Kelvin circulation balance requires a specified time-dependent momentum equation. A baroclinic source requires independent thermodynamic fields and a derived term such as \(\nabla T\times\nabla s\). The current Morandotti C0-IPDG computation is static and contains neither velocity evolution nor thermal variables. These effects are therefore not implemented and cannot explain the current static solution.

## 6. Stress and traction acceptance gates

For every mesh level and defect case, report:

1. \(\|\mathcal M a-\Phi\|_2\), symmetry defect, smallest eigenvalue, and condition estimate of \(\mathcal M\);
2. outer-boundary and each-core traction norms separately;
3. interior-facet traction jump using the stated elementwise Hessian convention;
4. stress and energy differences between successive mesh levels;
5. comparison with an independent analytic benchmark using identical geometry, core radius, material parameters, and boundary conditions.

The current driver contains source-level stress/traction diagnostics, but these gates remain **unexecuted** until the DOLFINx run is performed. Algebraic unit tests do not validate these FE quantities.

## 7. Superconducting extension is separate

London response and flux quantization motivate a later materials benchmark, not an automatic identification of a flusson with a dislocation or disclination. Such a test needs an order parameter, electromagnetic potential, penetration depth, coherence length, boundary conditions, and a coupled free-energy functional. Only then can vortex/flux-tube positions be compared with elastic defect cores.

## 8. Epistemic status

- Cartan definitions and Stokes circulation identity: **standard mathematical framework**.
- Morandotti map \(\Phi\mapsto a\mapsto v_h\): **implemented algebraic reconstruction**.
- FDT-medium-form coupling to elastic torsion/stress: **open candidate**, not derived.
- Kelvin/baroclinic dynamics: **not in the static model**.
- Superconducting flux coupling: **separate future application**.
- End-to-end two-core stress validation: **pending DOLFINx execution and independent benchmark**.

**Acceptance rule:** do not add an FDT coupling until the uncoupled Morandotti reconstruction passes its numerical gates.
