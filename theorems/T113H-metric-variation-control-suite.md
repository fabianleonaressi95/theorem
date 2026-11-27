# T113-H — Metric-variation and spectral control suite

**Classification:** numerical verification of finite-dimensional spectral identities and a lapse-variation identity; not a derivation or numerical estimate of quasicrystal packet gravitational mass.

**Dependencies:** [T113](T113-quasicrystal-phonon-phason-gravitational-mass.md), [T113-A](T113A-metric-action-phonon-phason-mode-sensitivity.md).

## H.1 Purpose

This record supplies manufactured finite-dimensional controls for scalar fluid/solid branches, decoupled and coupled phonon–phason sectors, and the lapse variation of a quadratic wave action. It checks the generalized Hellmann–Feynman identity against centered finite differences.

## H.2 Manufactured models

For a scalar sector, choose
\[
\mathcal M(\rho)=\rho^m,\qquad
\mathcal K(\rho)=\rho^{m+2a}.
\]
Then \(\omega^2=\rho^{2a}\) and \(d\log c/d\log\rho=a\). The selected slopes \(a=0.25,0.20,-0.10\) are regression inputs, not measured material parameters.

For the coupled toy model, the inertia is \(\mathcal M=\rho I\); the stiffness is a positive two-sector matrix with distinct reference eigenvalues and a tunable off-diagonal coupling \(R\). At \(R=0\) the spectrum separates into independent sectors. At \(R\ne0\) the eigenvectors mix. The implementation uses manufactured coefficients only.

## H.3 Lapse variation

For
\[
L_N=\frac{\dot q^T\mathcal M\dot q}{2N}
-\frac{N}{2}q^T\mathcal Kq,
\]
the identity \(-\partial L_N/\partial N|_{N=1}=H_2\) gives the canonical quadratic Hamiltonian. This is not the EKN packet mass: it omits the nonlinear medium response and the long-range correction.

## H.4 Status

The tests verify finite-dimensional spectral identities and the lapse/Hamiltonian identity only. They do not compute the metric-derived mass of a packet in a fluid, solid, or quasicrystal. The EKN solid calculation requires the nonlinear displacement correction and its \(1/r^2\) tail; see [T113-I](T113I-ekn-solid-nonlinear-tail-and-mass.md).
