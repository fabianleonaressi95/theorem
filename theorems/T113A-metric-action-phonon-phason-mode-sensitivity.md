# T113-A — Metric-coupled phonon–phason action and mode sensitivity

**Status:** explicit minimal effective-action ansatz and exact spectral sensitivity identity. This is a derivation framework, not a computed quasicrystal gravitational mass. Constitutive tensors must be supplied for a chosen symmetry class.

## A.1 Covariant material-frame action

Use signature \((-+++ )\), a unit material four-velocity \(U^\mu\) with \(g_{\mu\nu}U^\mu U^\nu=-1\), and spatial projector
\[
h^{\mu\nu}=g^{\mu\nu}+U^\mu U^\nu.
\]
Collect physical phonons and perpendicular-space phasons as \(q^I=(u_i,w_A)\), keeping their point-group representations distinct. Define
\[
Dq^I=U^\mu\nabla_\mu q^I,\qquad
D_\mu q^I=h_\mu{}^\nu\nabla_\nu q^I.
\]
A minimal conservative quadratic action is
\[
S_2=\frac12\int d^4x\sqrt{-g}\left[
\mathsf M_{IJ}(q_0,U,g)(Dq^I)(Dq^J)
-\mathsf C^{\mu\nu}_{IJ}(q_0,U,g)
(D_\mu q^I)(D_\nu q^J)
\right].
\]
The symmetric inertia matrix \(\mathsf M_{IJ}\) and spatial elastic tensor \(\mathsf C^{\mu\nu}_{IJ}\) contain phonon, phason, and mixed blocks corresponding to \(C,R,K\); spatial projection requires \(U_\mu\mathsf C^{\mu\nu}_{IJ}=U_\nu\mathsf C^{\mu\nu}_{IJ}=0\). Their allowed components depend on the quasicrystal point group. This is a preferred-material-frame medium, not a Lorentz-invariant vacuum theory. Relaxational/diffusive phasons require an open-system or dissipative extension and cannot simply be treated as real-frequency normal modes.

## A.2 Metric variation and gravitational source

Adopt
\[
T_{\mu\nu}=-\frac{2}{\sqrt{-g}}\frac{\delta S}{\delta g^{\mu\nu}}.
\]
The variation must include the metric dependence of \(\sqrt{-g}\), \(h^{\mu\nu}\), the normalization of \(U^\mu\), and any metric dependence of \(\mathsf M\) and \(\mathsf C\). Holding all material-frame structures fixed while varying only explicit contractions is generally incomplete. For the stated ansatz the safe exact definition is
\[
T_{\mu\nu}^{(2)}
=-\frac{2}{\sqrt{-g}}\frac{\delta S_2}{\delta g^{\mu\nu}},
\]
with the material-coordinate and constitutive variation prescription specified by the chosen model.

For a weak static field take \(g_{00}=-(1+2\Phi/c^2)+O(\Phi^2/c^4)\). The packet's source is the coefficient of \(\Phi\) in the on-shell, background-subtracted action, equivalently the corresponding background-subtracted stress-energy including the induced second-order response of the medium and boundary/long-range terms. The naive integral of the quadratic wave energy alone need not reproduce the sound-wave mass formula.

## A.3 Exact mode-sensitivity identity

In a homogeneous reference state the conservative Fourier kernel is
\[
\mathcal D(\omega,\mathbf k;\lambda)
=\mathcal K(\mathbf k;\lambda)-\omega^2\mathcal M(\mathbf k;\lambda),
\]
and a mode obeys
\[
\mathcal Kq_\alpha=\omega_\alpha^2\mathcal Mq_\alpha.
\]
For a simple non-degenerate eigenvalue, Hermitian \(\mathcal K,\mathcal M\), and positive \(q_\alpha^\dagger\mathcal Mq_\alpha\), differentiation yields
\[
\boxed{
\frac{d\omega_\alpha^2}{d\lambda}
=
\frac{q_\alpha^\dagger
(\partial_\lambda\mathcal K-\omega_\alpha^2\partial_\lambda\mathcal M)
q_\alpha}
{q_\alpha^\dagger\mathcal Mq_\alpha}.}
\]
The parameter \(\lambda\) may be the background mass density along a specified compression path; all density-dependent elastic, coupling, inertia, and background parameters must be differentiated. In a degenerate eigenspace, diagonalize the perturbation matrix within that subspace first.

For an acoustic branch \(\omega_\alpha(k\hat n)=c_\alpha(\hat n)k+o(k)\),
\[
\frac{d\log c_\alpha}{d\log\rho_m}
=\frac12\frac{d\log\omega_\alpha^2}{d\log\rho_m}
\]
at fixed direction and in the acoustic limit. This gives an exact spectral sensitivity, not the gravitational mass itself.

The scalar expression
\[
M_{g,\alpha}^{\rm candidate}
=-\frac{d\log c_\alpha}{d\log\rho_m}
\frac{E_\alpha}{c_\alpha^2}
\]
is only a candidate diagnostic for coupled quasicrystals. It becomes a mass formula only if the full metric variation of the medium-plus-wave system reduces to it. Anisotropic stress, mode mixing, phason dynamics, and nonlinear medium response may contribute additional terms. The Esposito–Krichevsky–Nicolis fluid result and isotropic-solid longitudinal/transverse results are mandatory controls.

## A.4 Falsifiable sequence

1. Choose a quasicrystal point group and list its invariant phonon, phason, and mixed constitutive tensors.
2. Specify the material-frame metric-variation prescription and a density/compression path.
3. Reproduce the scalar-fluid result, including induced medium response and boundary terms.
4. Reproduce isotropic-solid longitudinal and transverse branches.
5. Set the phonon–phason block \(R=0\), verify sector separation, then turn on symmetry-allowed \(R\) and track eigenvectors as well as eigenvalues.
6. Evaluate the full metric-derived packet mass and compare it with the candidate speed-derivative diagnostic.
7. Only then add specified Burgers/Frank defects and compare their changes to the local elastic operator, modes, and packet stress-energy.
8. Treat dissipative phasons using an open-system energy balance, not the conservative normal-mode formula.

A sign change is accepted only if it occurs in the full metric-derived packet mass and survives normalization, boundary, and constitutive-path checks. A sign change in \(d c_\alpha/d\rho_m\) alone is insufficient.

## A.5 Defects and circulation

The proposed chain is
\[
(B,\Omega)\to(\mathsf C,\mathsf M)_{\rm local}
\to(\omega_\alpha,q_\alpha)
\to T_{\mu\nu}^{(\alpha)}
\to M_{g,\alpha}.
\]
Burgers and Frank data can modify the local elastic operator only after a concrete defect geometry and constitutive response are specified. Vorticity and circulation remain distinct fluid/phase observables; neither is identified by definition with Cartan curvature, torsion, Burgers charge, or Frank charge.

## A.6 Classification

- **Derived here:** covariant material-frame quadratic action ansatz; variational definition of its stress-energy; generalized Hellmann–Feynman sensitivity identity for simple conservative modes.
- **Open:** explicit stress-energy components for a chosen icosahedral/quasiperiodic constitutive tensor; full packet gravitational mass for coupled phonon–phason modes; any universal sign.
- **Required input:** concrete point group, invariant tensors, density path, material-frame variation prescription, and phason dynamical law.
