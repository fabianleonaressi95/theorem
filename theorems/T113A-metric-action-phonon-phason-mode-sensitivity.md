# T113-A — Metric-coupled phonon–phason action and mode sensitivity

**Status:** explicit minimal effective-action ansatz and exact spectral sensitivity identity. This is a derivation framework, not yet a computed quasicrystal gravitational mass. The constitutive tensors must be supplied for a chosen symmetry class.

## A.1 Kinematics and background structure

Work in a four-dimensional background with signature \((-+++ )\). Let \(U^\mu\) be the unit timelike velocity field of the material, \(g_{\mu\nu}U^\mu U^\nu=-1\), and define the spatial projector

\[
h^{\mu\nu}=g^{\mu\nu}+U^\mu U^\nu.
\]

Collect the physical phonon and perpendicular-space phason fields into \(q^I=(u_i,w_A)\). The index \(I\) labels both sectors; it is not a claim that physical and perpendicular indices transform under the same point-group representation.

Define convective and spatial derivatives

\[
Dq^I=U^\mu\nabla_\mu q^I,\qquad
D_\mu q^I=h_\mu{}^\nu\nabla_\nu q^I.
\]

A minimal nondissipative quadratic action is

\[
S_2=\frac12\int d^4x\sqrt{-g}\left[
\mathsf M_{IJ}(q_0,U,g)(Dq^I)(Dq^J)
-\mathsf C^{\mu\nu}_{IJ}(q_0,U,g)
(D_\mu q^I)(D_\nu q^J)
\right].
\]

Here \(q_0\) denotes the material reference state. The inertia matrix \(\mathsf M_{IJ}\) and spatial elastic tensor \(\mathsf C^{\mu\nu}_{IJ}\) are symmetric in the appropriate paired indices; spatial projection requires \(U_\mu\mathsf C^{\mu\nu}_{IJ}=U_\nu\mathsf C^{\mu\nu}_{IJ}=0\). Their phonon, phason, and mixed blocks encode the continuum elastic tensors \(C,R,K\). This action is the conservative propagating-mode sector only. Diffusive/relaxational phasons require dissipative or open-system variables and cannot be represented by simply declaring their frequency real.

The action is generally covariant as a background-field expression, but the material state \(U^\mu,q_0\) selects a preferred rest frame. General covariance therefore does not imply Lorentz invariance of the medium.

## A.2 Stress-energy tensor: what must be varied

With the convention
\[
T_{\mu\nu}=-\frac{2}{\sqrt{-g}}\frac{\delta S}{\delta g^{\mu\nu}},
\]
the stress-energy tensor is obtained by varying the *entire* action, including the metric dependence of \(h^{\mu\nu}\), the normalization of \(U^\mu\), the material measure, and any metric dependence of \(\mathsf M\) and \(\mathsf C\). It is not generally correct to vary only the explicit metric contractions while holding all background structures fixed.

For the quadratic action above the unexpanded but exact variational definition is

\[
T_{\mu\nu}^{(2)}
=-\frac{2}{\sqrt{-g}}\frac{\delta S_2}{\delta g^{\mu\nu}}.
\]

This equation is the safe starting point for a specified constitutive model. An explicit component formula is model-dependent because the material tensors and the prescription for holding the material coordinates fixed under metric variation must be stated.

In a weak, static field choose
\[
g_{00}=-(1+2\Phi/c^2)+O(\Phi^2/c^4),
\]
with \(\Phi\) the Newtonian potential per unit mass. The packet's gravitational coupling is the term linear in \(\Phi\) in the *on-shell, background-subtracted effective action*. Equivalently, its source is the corresponding background-subtracted \(T_{00}\), including the second-order change of the equilibrium medium and the nonlinear wave response. A spatial integral of the naive quadratic wave energy alone need not reproduce the sound-wave mass formula: the medium's induced response and boundary terms are essential.

## A.3 Plane-wave operator and exact eigenvalue sensitivity

In a homogeneous reference state, Fourier transformation gives the quadratic action kernel
\[
\mathcal D(\omega,\mathbf k;\lambda)
=\mathcal K(\mathbf k;\lambda)
-\omega^2\mathcal M(\mathbf k;\lambda),
\]
where \(\lambda\) is a control parameter such as the background mass density along a specified thermodynamic/compression path. A conservative normal mode satisfies
\[
\mathcal K q_\alpha=\omega_\alpha^2\mathcal M q_\alpha.
\]

For a simple (non-degenerate) eigenvalue, with Hermitian \(\mathcal K,\mathcal M\) and positive \(q_\alpha^\dagger\mathcal M q_\alpha\), differentiation gives the generalized Hellmann–Feynman identity

\[
\boxed{
\frac{d\omega_\alpha^2}{d\lambda}
=
\frac{
q_\alpha^\dagger
\left(\partial_\lambda\mathcal K
-\omega_\alpha^2\partial_\lambda\mathcal M\right)
q_\alpha
}{
q_\alpha^\dagger\mathcal M q_\alpha
}.}
\]

The derivative includes the density dependence of all elastic, phonon–phason coupling, inertia, and background parameters along the declared path. For a degenerate branch one must first diagonalize the perturbation matrix inside the degenerate eigenspace. This identity quantifies how hybridization and polarization affect the mode frequency; it does **not**, by itself, equal the gravitational mass.

In an acoustic branch, if \(\omega_\alpha(k\hat n;\lambda)=c_\alpha(\hat n;\lambda)k+o(k)\), it yields the branch- and direction-dependent logarithmic sensitivity
\[
\frac{d\log c_\alpha}{d\log\rho_m}
=\frac12\frac{d\log\omega_\alpha^2}{d\log\rho_m}
\quad (k,\hat n\text{ fixed in the acoustic limit}).
\]

The scalar expression
\[
M_{g,\alpha}^{\rm candidate}
=-\frac{d\log c_\alpha}{d\log\rho_m}
\frac{E_\alpha}{c_\alpha^2}
\]
is therefore a sharply defined **candidate diagnostic**, not a theorem for coupled quasicrystals. It becomes a physical mass formula only after the metric variation of the complete medium-plus-wave system is evaluated and shown to reduce to this expression. In particular, anisotropic stress, mode mixing, phason inertia/relaxation, and the nonlinear equilibrium response can add terms.

## A.4 Required control and falsification sequence

1. **Scalar fluid:** choose an equation of state and reproduce the Esposito–Krichevsky–Nicolis expression, including the induced medium response and boundary contribution.
2. **Isotropic elastic solid:** recover the longitudinal and transverse control branches.
3. **Uncoupled quasicrystal:** set the phonon–phason block \(R=0\); verify that the mode calculation separates into the expected sectors.
4. **Coupled quasicrystal:** turn on symmetry-allowed \(R\), track eigenvectors as well as eigenvalues, and compare the metric-variation result against the candidate diagnostic.
5. **Defect-free versus defective samples:** only after the preceding controls, introduce specified Burgers/Frank sectors and compute their changes to the local constitutive operator and packet stress-energy.

A sign change is accepted only if it appears in the full metric-derived packet mass, is stable under normalization and boundary checks, and is not merely a sign change in a frequency derivative.

## A.5 Relation to Cartan defects and circulation

For a specified discrete/continuum Cartan model, dislocation and disclination data may alter the background elastic tensors and therefore \(\mathcal K,\mathcal M\). The test chain is
\[
(B,\Omega)\to(\mathsf C,\mathsf M)_{\rm local}
\to(\omega_\alpha,q_\alpha)
\to T_{\mu\nu}^{(\alpha)}
\to M_{g,\alpha}.
\]

Vorticity and circulation remain separate fluid/phase observables. They may couple to the elastic modes in a specified superfluid or active-medium model, but neither is identified with Cartan curvature, torsion, Burgers charge, or Frank charge by definition.

## A.6 Status

- **Derived:** the covariant quadratic action ansatz; the variational definition of its stress-energy tensor; the generalized eigenvalue sensitivity identity for simple conservative modes.
- **Not derived:** a closed explicit \(T_{00}\) for a particular icosahedral/quasiperiodic constitutive tensor; the full packet gravitational mass of a coupled phonon–phason branch; any universal sign.
- **Next required input:** a concrete point group, its invariant phonon/phason tensors, a density/compression path, and the material-frame variation prescription.
