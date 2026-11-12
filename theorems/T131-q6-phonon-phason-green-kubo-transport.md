# T131 — Q6 phonon–phason normal modes and Green–Kubo transport

**Classification:** [P] finite-dimensional generalized-eigenproblem and Green–Kubo identities under stated hypotheses; [N] numerical implementation tests; [O] Q6 material calibration, phason kinetics, thermodynamic-limit transport and acoustic-geometric application.

**Dependencies:** T113, T113-A, T113-D, T113-G, T128–T130. This record extends the existing Q6 phonon/internal-mode framework; it does not replace it or identify the RGS internal sector with physical phasons.

## 1. Scope and separation of physical inputs

The bare Q6 graph has 64 vertices, 192 edges, six coordinate-flip directions and Laplacian spectrum
\[
\operatorname{spec}(L_{Q6})=0^1,2^6,4^{15},6^{20},8^{15},10^6,12^1.
\]
This finite graph spectrum is not, by itself, a Bloch phonon dispersion. A physical vibrational model additionally requires:
- a declared embedding or material geometry;
- atomic/site masses and a positive mass matrix;
- a Hessian or force-constant matrix derived from a specified potential, electronic-structure calculation, or independently calibrated data;
- boundary conditions or a periodic/quasiperiodic family if a wavevector \(\mathbf q\) and dispersion are claimed.

For a finite Q6 motif, use a finite generalized normal-mode problem. For an extended material, use a wavevector-dependent family only after its translation/quasiperiodic construction is specified.

## 2. Finite generalized normal modes

Let \(K=K^T\in\mathbb R^{n\times n}\) be the Hessian of the declared potential at the reference configuration and \(M=M^T\succ0\) the mass matrix. The linearized equations are
\[
M\ddot u+Ku=0,
\qquad
K e_\alpha=\omega_\alpha^2 M e_\alpha.
\]
With a Cholesky factorization \(M=LL^T\), the symmetric standard problem is
\[
L^{-1}KL^{-T}z_\alpha=\omega_\alpha^2z_\alpha,
\qquad e_\alpha=L^{-T}z_\alpha.
\]
The eigenvectors can be normalized by \(e_\alpha^TMe_\beta=\delta_{\alpha\beta}\).

Negative eigenvalues of the mass-weighted Hessian are unstable directions, not real-frequency phonons. Zero eigenvalues may represent rigid translations or other exact symmetries and must be identified from the model, not silently discarded. The finite implementation reports \(\omega^2\) and stability flags; it does not turn negative eigenvalues into real frequencies.

For a periodic or quasiperiodic family the corresponding problem is
\[
K(\mathbf q)e_s(\mathbf q)
=\omega_s^2(\mathbf q)M(\mathbf q)e_s(\mathbf q).
\]
A group velocity \(\nabla_{\mathbf q}\omega_s\) is defined only where the wavevector family and a differentiable branch are defined. Degenerate branches require subspace/degenerate perturbation analysis.

## 3. Polarization labels are diagnostics, not assumed identities

For a mode represented by site displacement vectors \(e_{a}\in\mathbb C^d\) and a nonzero propagation direction \(\hat q\), define
\[
P_L=\frac{\sum_a|e_a\cdot\hat q|^2}{\sum_a\|e_a\|^2},
\qquad P_T=1-P_L.
\]
For layered systems, an out-of-plane projector is evaluated separately. These projections diagnose longitudinal/transverse/out-of-plane character. Acoustic/optical character is a different classification: it depends on relative motion of the basis atoms and the acoustic sum rule at \(\mathbf q=0\). Mixed modes remain mixed; no hard label is imposed by frequency ordering alone.

The labels LA/TA/LO/TO/ZA/ZO are therefore used only when the geometry, basis, and polarization justify them. A finite Q6 graph without a material basis does not automatically possess these six branch labels.

## 4. Phonon and phason sectors

A conservative coupled quadratic model may be written
\[
H_2=\frac12\dot q^T\mathsf M\dot q+
\frac12q^T
\begin{pmatrix}K_{pp}&K_{p\varphi}\\
K_{\varphi p}&K_{\varphi\varphi}\end{pmatrix}q,
\qquad q=(u,w).
\]
Here \(u\) denotes physical displacement variables and \(w\) an independently defined internal/phason variable. The blocks are model inputs until derived from the same microscopic energy or measured.

A phason flip is instead a transition between alternative quasiperiodic configurations. Its state space, allowed transitions, energy differences and rates must be specified. If modeled as an equilibrium continuous-time Markov chain with rates \(r_{ab}\), detailed balance requires
\[
\pi_a r_{ab}=\pi_b r_{ba},
\qquad
\pi_a\propto e^{-\beta E_a},
\]
for the declared equilibrium energies \(E_a\). This condition is not a claim that all real phason dynamics is Markovian. A propagating phason normal mode, a relaxational phason field and a discrete flip process are distinct models.

In particular, the RGS \(T_{2u}\) sector or any internal graph representation is not identified with a physical phason without a derived microscopic map and dynamical law. This preserves the data boundary recorded in T113-D and T113-G.

## 5. Green–Kubo law for the stress response

Let \(\Pi_{ij}\) be the **total extensive microscopic stress** in volume \(V\), with equilibrium fluctuation \(\delta\Pi_{ij}=\Pi_{ij}-\langle\Pi_{ij}\rangle_{eq}\). In classical equilibrium linear response, the viscosity tensor is
\[
\boxed{
\eta_{ij,kl}=\frac{1}{k_BT V}
\int_0^\infty
\left\langle
\delta\Pi_{ij}(t)\delta\Pi_{kl}(0)
\right\rangle_{eq}\,dt
}
\]
when the correlation integral exists and the thermodynamic/long-time limits are justified. For a stress density \(P_{ij}=\Pi_{ij}/V\), the equivalent prefactor is \(V/(k_BT)\).

The complete stress of a coupled model includes phonon, phason and mixed contributions, and its autocorrelation includes cross-correlations. These pieces are not assumed statistically independent. The scalar shear viscosity is a symmetry-reduced component only when the material symmetry and constitutive setting justify that reduction; the six Q6 directions are not averaged away by assumption.

For sampled trajectories, the finite-window estimator is
\[
\widehat C_{ij,kl}(m\Delta t)=
\frac{1}{N-m}\sum_{n=0}^{N-m-1}
\delta\Pi_{ij}(t_{n+m})\delta\Pi_{kl}(t_n),
\]
\[
\widehat\eta_{ij,kl}(t_{\max})=
\frac{\Delta t}{k_BT V}
\operatorname{Trapz}_{m=0}^{m_{\max}}
\widehat C_{ij,kl}(m\Delta t).
\]
This is a finite-window estimate, not a certified infinite-time integral. Report the window, sampling interval, uncertainty, stationarity checks, and convergence against increasing record length and integration cutoff. Do not infer convergence from a visually decaying plot alone.

A quantum calculation requires the appropriate quantum Kubo-transformed/imaginary-time correlation, not the classical trajectory formula copied unchanged.

## 6. Why a harmonic spectrum alone does not determine viscosity

The harmonic Hessian determines normal-mode frequencies and eigenvectors. It does not, by itself, provide a finite dissipative viscosity. In a finite purely harmonic system, the dynamics is non-decaying and correlations generally oscillate or fail to be integrable in the required sense. A transport coefficient requires a physically specified relaxation mechanism, such as anharmonic interactions, coupling to a validated bath, or an appropriate kinetic collision operator.

Thus the following are separate inputs and audits:
1. harmonic force constants and normal modes;
2. anharmonic force constants or a justified stochastic/open-system dynamics;
3. the microscopic stress observable consistent with that Hamiltonian;
4. equilibrium sampling and correlation convergence;
5. finite-size and thermodynamic-limit control.

A fitted damping constant inserted solely to make the Green–Kubo integral finite is not a derivation of material viscosity.

## 7. Thermodynamics and acoustic propagation

For a specified equilibrium free energy \(F(T,V)\),
\[
p=-\left(\frac{\partial F}{\partial V}\right)_T,
\qquad
c_s^2=\left(\frac{\partial p}{\partial\rho}\right)_s.
\]
A harmonic phonon contribution can be included in \(F\) only after the frequencies and their volume dependence are defined; anharmonic and configurational/phason contributions may also be essential. The equation of state is not determined by the Q6 graph spectrum alone.

For a barotropic, inviscid, irrotational fluid background, the acoustic perturbation equation can be represented by an effective Lorentzian acoustic metric. The sonic horizon condition is \(|\mathbf v|=c_s\). This is an effective propagation geometry, not a derivation of quantum gravity. In anisotropic or strongly dispersive media, different branches may have different characteristic surfaces; a single acoustic metric must not be assumed before testing the dispersion and hydrodynamic limit. See T113-B and the metric/phonon–phason limits in T113/T113-A.

## 8. Reproducible finite audit

Implementation: `audits/phonon_phason/normal_modes_kubo.py`.  
Tests: `tests/test_t131_phonon_phason_kubo.py`.

The implementation provides:
- a mass-weighted symmetric generalized eigensolver with stability flags;
- longitudinal/transverse polarization weights for supplied site displacement vectors and a supplied propagation direction;
- a finite-window Green–Kubo estimator for sampled extensive stress components.

It does **not** generate a material Hessian, a six-dimensional cut-and-project acceptance window, physical phason flip rates, an anharmonic Hamiltonian, a thermodynamic-limit viscosity, or an acoustic black-hole analogue.

## 9. Status and acceptance gates

- **[P] Mathematical identities:** generalized normal-mode reduction for symmetric \(K\) and positive-definite \(M\); polarization projectors; Green–Kubo expression under equilibrium linear-response and convergence hypotheses.
- **[N] Numerical tests:** synthetic finite matrices, mass normalization, instability flagging, polarization normalization, and a finite-window stress-correlation calculation.
- **[O] Physical construction:** calibrated Q6/material geometry, masses and Hessian; actual phonon branches; microscopic phason variables and rates; anharmonic stress dynamics; converged Green–Kubo tensor; equation of state; anisotropic acoustic characteristics.
- **Not claimed:** that the bare Q6 Laplacian is a phonon dispersion; that RGS internal modes are already physical phasons; that harmonic frequencies alone determine viscosity; that a sonic horizon demonstrates quantum gravity.

## References within the repository

- T113: gravitational response of phonon–phason modes; ordinary-fluid/solid control and open quasicrystal extension.
- T113-A: metric-coupled material-frame action and generalized eigenvalue sensitivity.
- T113-B: acoustic gravitational-mass control.
- T113-D: Q6/RGS phonon–internal-mode model and exact graph/symmetry obstructions.
- T113-G: cut-and-project symmetry, anisotropy and missing canonical Q6 acceptance-window data.
- T112: golden geometry and KTHNY defect controls.
