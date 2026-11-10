# Volterra dipole-to-edge audit: corrected kinematic comparison

This audit separates a source-identity test from an elasticity/energy comparison.

## Kinematic identity

Use the two-dimensional incompatibility convention
\[
\operatorname{inc}\varepsilon^p
=\partial_{yy}\varepsilon^p_{xx}
 +\partial_{xx}\varepsilon^p_{yy}
 -\partial_{xy}\gamma^p_{xy}.
\]

Let \(x_0\) be the cut tip, \(H\) the Heaviside function, and
\(f_\sigma(y)=\sigma^{-1}f(y/\sigma)\) a normalized smooth core profile.

An opposite wedge-disclination pair with Frank strengths \(+\Omega\) and
\(-\Omega\), separated by \(d\), is represented by
\[
\varepsilon^p_{yy}
=\Omega (x-x_0)H(x-x_0)
 [f_\sigma(y-d/2)-f_\sigma(y+d/2)].
\]
Its incompatibility is
\[
\operatorname{inc}\varepsilon^p
=\Omega\delta(x-x_0)
 [f_\sigma(y-d/2)-f_\sigma(y+d/2)].
\]

The edge-dislocation slip-cut representation is
\[
\gamma^p_{xy}=bH(x-x_0)f_\sigma(y),
\]
and therefore
\[
\operatorname{inc}\varepsilon^p
=-b\delta(x-x_0)f_\sigma'(y).
\]

Setting \(b=\Omega d\), the dipole incompatibility profile divided by
\(\Omega d\) is
\[
\frac{f_\sigma(y-d/2)-f_\sigma(y+d/2)}{d}
\longrightarrow -f_\sigma'(y)
\quad(d/\sigma\to0).
\]
Thus the dipole converges kinematically to the edge-dislocation source with
Burgers magnitude \(b=\Omega d\), with the sign fixed by the ordering above.

## What is corrected

- Compare at the level of the incompatibility source, not by comparing raw eigenstrain components \(\varepsilon^p_{yy}\) and \(\gamma^p_{xy}\), which are different components.
- The relevant continuum parameter is \(d/\sigma\). A sweep in \(d/h\) and \(\sigma/h\) is useful for grid studies, but profile-level error depends on their ratio.
- \(d=2h\) is not a distinguished continuum value. It can align a pair with a centred grid stencil, but it does not make a finite dipole equal to the derivative of the core profile.
- Gaussian and normalized sech-squared profiles are both included to test profile dependence.

## Reproducible test

Run `python scripts/rgs_volterra_dipole_audit.py --out artifacts/volterra_dipole_audit`.

The script writes JSON and CSV sweeps for \(d/h\in\{1,1.5,2,2.5,3,4,8\}\) and \(\sigma/h\in\{1,2,3.2,6.4\}\), for both profiles. It also checks the small-\(d/\sigma\) regime. The pytest regression is `tests/test_rgs_volterra_dipole_audit.py`.

## Explicit limitation

This is a source-profile/incompatibility audit. It does not solve the elasticity equations and does not establish equality or convergence of displacement, stress, or elastic energy. Those require solving both representations with the same domain, core geometry, constitutive tensor, boundary conditions, quadrature, and mesh sequence. The published Morandotti C0-IPDG method remains a separate reference implementation; this test does not claim to reproduce its multi-core reconstruction algorithm.
