# T113-I — EKN isotropic-solid nonlinear tail and packet-mass audit

**Classification:** derivation audit of the published isotropic-solid result in Esposito–Krichevsky–Nicolis (EKN), PRL 122, 084501 (2019), Eqs. (12)–(24). This is a reconstruction of a published result, not a new quasicrystal theorem.

**Primary source:** A. Esposito, R. Krichevsky, A. Nicolis, “Gravitational Mass Carried by Sound Waves,” DOI: [10.1103/PhysRevLett.122.084501](https://doi.org/10.1103/PhysRevLett.122.084501), [arXiv:1807.08771](https://arxiv.org/abs/1807.08771).

## I.1 Why the linearized calculation gives zero

For an isotropic solid the EFT is built from three comoving scalar fields \(\phi^I\), with
\[
B^{IJ}=\partial_\mu\phi^I\partial^\mu\phi^J,\quad
b=\sqrt{\det B},\quad
Y=\frac{\mathrm{tr}B^2}{(\mathrm{tr}B)^2},\quad
Z=\frac{\mathrm{tr}B^3}{(\mathrm{tr}B)^3},
\]
and action
\[
S=-w_0\int d^4x\,f(b,Y,Z).
\]
The homogeneous state is \(\bar\phi^I=b_0^{1/3}x^I\), and the fluctuations are
\[
\phi^I=b_0^{1/3}(x^I+\pi^I).
\]
In the nonrelativistic limit, the leading \(O(c^2)\) contribution to the energy density is
\[
T_{00}\simeq c^2w_0b_0\,\nabla\cdot\boldsymbol\pi.
\]
Thus the transported mass is
\[
M=w_0b_0\left\langle\int d^3x\,\nabla\cdot\boldsymbol\pi\right\rangle.
\]
For a compactly supported linear packet the integral is a boundary term and vanishes. It is not legitimate to stop there.

## I.2 Nonlinear displacement and the finite tail

Expand
\[
\boldsymbol\pi=\boldsymbol\pi_{(1)}+\boldsymbol\pi_{(2)}+\cdots,
\]
where \(\pi_{(1)}\) is a localized solution of the linear elastic wave equation and \(\pi_{(2)}\) is quadratic in its amplitude. EKN's second-order equation has the form
\[
\ddot\pi_i-c_L^2\partial_i(\nabla\cdot\boldsymbol\pi)
-c_T^2(\nabla^2\pi_i-\partial_i\nabla\cdot\boldsymbol\pi)
=\partial_jA_{ij}+\partial_tB_i.
\]
The tensor \(A_{ij}\) is quadratic in the linear solution; \(B_i\) is also quadratic but its detailed form drops out after time averaging and taking the divergence.

Set \(\Psi=\nabla\cdot\boldsymbol\pi_{(2)}\). Taking the divergence and averaging over many wave periods gives
\[
\nabla^2\langle\Psi\rangle
=-\frac{1}{c_L^2}
\left\langle\partial_i\partial_jA_{ij}\right\rangle.
\]
The Green function \(G(\mathbf x)=-1/(4\pi|\mathbf x|)\) produces a \(1/r^2\) displacement tail. Consequently the surface flux of \(\pi_{(2)}\) at large radius need not vanish even though the source \(A_{ij}\) is localized. Using
\[
\partial_i\partial_j\frac1r
=\operatorname{PV}\frac{3\hat r_i\hat r_j-\delta_{ij}}{r^3}
-\frac{4\pi}{3}\delta_{ij}\delta^3(\mathbf x),
\]
the principal-value part integrates to zero on a sphere centered on the source, leaving
\[
\left\langle\int d^3x\,\nabla\cdot\boldsymbol\pi\right\rangle
\simeq-\frac{1}{3c_L^2}
\left\langle\int d^3x\,A_{ii}\right\rangle.
\]
This is the crucial nonzero contribution. The longitudinal speed \(c_L\) appears because the equation for the divergence is governed by the longitudinal Green operator, even when the source packet is transverse.

## I.3 Mode split and the denominator issue

Decompose the linear packet into longitudinal and transverse parts,
\[
\boldsymbol\pi_{(1)}=\boldsymbol\pi_L+\boldsymbol\pi_T,\qquad
\nabla\times\boldsymbol\pi_L=0,\quad
\nabla\cdot\boldsymbol\pi_T=0.
\]
Their quadratic energies are
\[
E_L=\frac{w_0b_0}{2}\int d^3x\,
[\dot{\boldsymbol\pi}_L^2+c_L^2(\nabla\cdot\boldsymbol\pi_L)^2],
\]
\[
E_T=\frac{w_0b_0}{2}\int d^3x\,
[\dot{\boldsymbol\pi}_T^2+c_T^2(\nabla\times\boldsymbol\pi_T)^2].
\]
Combining the Green-function identity with the branch virial identities gives EKN Eq. (23):
\[
M\simeq-\frac{b_0}{c_L^2}
\left[
\frac{c_L'}{c_L}E_L+
\frac{c_T'}{c_T}E_T
\right].
\]
Since \(\rho_m\propto b_0\) under hydrostatic compression,
\[
\frac{d\log c_s}{d\log\rho_m}
=b_0\frac{c_s'}{c_s}.
\]
For a separated packet of either branch, EKN Eq. (24) is therefore
\[
\boxed{M_s=-\frac{d\log c_s}{d\log\rho_m}\frac{E_s}{c_L^2},
\qquad s\in\{L,T\}.}
\]
**Important correction:** the denominator in the isotropic-solid formula is the longitudinal speed squared for both branches. It is not \(c_T^2\) for a transverse packet. The reason is structural: the nonlinear mass correction is extracted from the divergence equation, whose Green operator contains \(c_L\). The branch label \(s\) selects the derivative and packet energy, not the Green-function denominator.

In the perfect-fluid limit \(c_T\to0\), \(c_L\to c_s\), and the expression reduces to the usual fluid result
\[
M=-\frac{d\log c_s}{d\log\rho_m}\frac{E}{c_s^2}.
\]

## I.4 Correction to the repository statement

The former T113-B solid line used \(E_T/c_T^2\) for the transverse contribution. That is not the formula printed in EKN Eq. (24), which uses \(E_s/c_L^2\) for both isolated branches. T113-B is corrected in this branch to match the source. The previous expression should not be used as the isotropic-solid benchmark.

## I.5 What is and is not established

- **Established by the cited EKN calculation:** the nonlinear displacement tail, Green-function identity, and isotropic-solid packet-mass expression above.
- **Checked algebraically in the accompanying regression:** hydrostatic chain rule, branch slopes, common \(c_L^2\) denominator, and perfect-fluid limit.
- **Not independently re-derived here:** the full expansion of every \(g_i\) coefficient from \(f(b,Y,Z)\), and the complete contraction of \(A_{ii}\) term by term. Those steps are reproduced at the level of EKN's displayed equations (15)–(23), not claimed as an independent symbolic derivation.
- **Still open:** replacing isotropic elasticity by icosahedral phonon–phason elasticity, where the divergence Green operator, coupled polarizations, and any relaxational phason sector must be handled from the chosen action.

## I.6 Reproducibility

Run:
\`\`\`bash
python scripts/audit_t113_ekn_solid_mass.py
pytest -q tests/test_t113_ekn_solid_mass.py
\`\`\`

These tests verify the equation-level normalization and limiting case. They do not numerically solve the nonlinear PDE or establish a quasicrystal packet mass.
