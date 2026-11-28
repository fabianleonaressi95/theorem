# Explicit Seeley–DeWitt baseline on the toroidal PSU–Anti-Twin Cartan background

**Date:** 2026-11-28  
**Status:** exact universal Laplace-type formulas plus a declared minimal matter baseline. This is not yet the full model: field multiplicities, gauge/gravitational ghosts, interface conditions and the actual contortion profile remain to be fixed.

## 1. Euclidean toroidal background

Use the Euclidean continuation of the previously defined coframe:
\[
e^0=N(l)c\,d\tau,\quad e^1=dl,\quad
e^2=r(l)d\theta,\quad e^3=A(l,\theta)d\varphi,\qquad
A(l,\theta)=R(l)+r(l)\cos\theta.
\]
The metric is
\[
ds_E^2=N^2c^2d\tau^2+dl^2+r^2d\theta^2+A^2d\varphi^2,
\quad
\sqrt g=NcrA.
\]
The coframe is nondegenerate where \(N>0,\ r>0,\ A>0\); a sufficient global condition is \(R(l)>r(l)>0\). The independent metric-compatible connection is
\[
\omega^{ab}=\omega_{\rm LC}^{ab}(e)+K^{ab},\qquad K^{ab}=-K^{ba},
\]
with
\[
T^a=K^a{}_b\wedge e^b,\qquad
R^{ab}(\omega)=R^{ab}(\omega_{\rm LC})+D_{\rm LC}K^{ab}
+K^a{}_c\wedge K^{cb}.
\]
In the heat-kernel formulas below, \(R_{\rm LC}\), \(R_{\mu\nu}^{\rm LC}\), \(R_{\mu\nu\rho\sigma}^{\rm LC}\) denote the metric curvature used by the underlying Laplace-type operator. Torsion enters through the operator endomorphism \(E\) and bundle curvature \(\Omega\). One must **not** replace every Levi-Civita curvature in the universal formula by \(R(\omega)\) by fiat. If the chosen operator is built from a torsionful affine Laplacian, first complete its square and identify its effective bundle connection and \(E\).

## 2. Universal coefficients

For a positive Euclidean Laplace-type operator written in the convention
\[
P=-(g^{\mu\nu}\mathcal D_\mu\mathcal D_\nu+E),
\qquad \Omega_{\mu\nu}=[\mathcal D_\mu,\mathcal D_\nu],
\]
the diagonal coefficients in four dimensions are
\[
a_0(x,P)=(4\pi)^{-2}\operatorname{tr}I,
\]
\[
a_2(x,P)=(4\pi)^{-2}\operatorname{tr}\left(E+\frac16R_{\rm LC}I\right),
\]
\[
\begin{aligned}
a_4(x,P)=(4\pi)^{-2}\operatorname{tr}\bigg[&
\frac12E^2+\frac16R_{\rm LC}E+\frac16\mathcal D^2E
+\frac1{30}\Box R_{\rm LC}\\
&+\frac1{72}R_{\rm LC}^2-\frac1{180}R_{\mu\nu}^{\rm LC}R_{\rm LC}^{\mu\nu}
+\frac1{180}R_{\mu\nu\rho\sigma}^{\rm LC}R_{\rm LC}^{\mu\nu\rho\sigma}
+\frac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu}
\bigg].
\end{aligned}
\]
Equivalently, the \(a_4\) bracket is
\[
\frac1{360}\left[
(5R^2-2R_{\mu\nu}R^{\mu\nu}+2R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma})I
+60RE+180E^2+60\mathcal D^2E+12\Box R+30\Omega^2
\right].
\]
This is the universal local formula for the specified Laplace-type operator. For a smooth compact manifold without boundary, integrated total derivatives vanish. If the throat is treated as an actual interface/shell rather than a smooth internal gluing, additional interface/boundary coefficients depend on the matching conditions and cannot be omitted.

## 3. Explicit scalar baseline

Take \(N_s\) real scalar fields with
\[
P_s=-\nabla_{\rm LC}^2+m_s^2+\xi_sR_{\rm LC}.
\]
Then \(E_s=-(m_s^2+\xi_sR_{\rm LC})\), \(\Omega_s=0\), and
\[
a_0^{(s)}=(4\pi)^{-2},
\qquad
a_2^{(s)}=(4\pi)^{-2}\left[\left(\frac16-\xi_s\right)R_{\rm LC}-m_s^2\right].
\]
For a single scalar,
\[
\begin{aligned}
(4\pi)^2a_4^{(s)}={}&\frac12m_s^4
+m_s^2\left(\xi_s-\frac16\right)R_{\rm LC}
+\frac12\left(\xi_s-\frac16\right)^2R_{\rm LC}^2\\
&+\frac1{180}\left(R_{\mu\nu\rho\sigma}^2-R_{\mu\nu}^2\right)
+\left(\frac1{30}-\frac{\xi_s}{6}\right)\Box R_{\rm LC}.
\end{aligned}
\]
For several species, sum these expressions with their actual multiplicities. A complex scalar counts as two real scalar degrees of freedom in this determinant convention.

## 4. Explicit Dirac baseline and torsion insertion

For a Euclidean Dirac field, define the first-order operator using the independent spin connection:
\[
\slashed D_\omega=\gamma^ae_a{}^\mu
\left(\partial_\mu+\frac14\omega_{\mu bc}\gamma^{bc}\right),
\qquad
P_D=\slashed D_\omega^\dagger\slashed D_\omega.
\]
This is positive by construction on a specified self-adjoint domain. Put \(P_D\) into Laplace form \(P_D=-(\mathcal D_D^2+E_D)\) by completing the square. The resulting \(\mathcal D_D\), \(E_D\) and \(\Omega_D=[\mathcal D_D,\mathcal D_D]\) are the exact inputs to section 2. This completion must be performed for the chosen contortion \(K\); it is not legitimate to insert a torsion-free Lichnerowicz endomorphism and then append a guessed \(T^2\) term.

As a check, in the torsion-free limit with the standard Euclidean convention, \(E_D=-R_{\rm LC}I_4/4\), so
\[
\operatorname{tr}_{4}\left(E_D+\frac16R_{\rm LC}I_4\right)
=-\frac13R_{\rm LC}.
\]
For nonzero \(K\), the additional terms are determined by \(E_D(K)\) and \(\Omega_D(K)\). The full \(a_4\) expression then generates the allowed quadratic torsion, derivative-of-torsion and curvature–torsion invariants after gamma traces and integration by parts. Their coefficients are not universal numbers independent of the chosen Dirac operator and torsion convention.

## 5. Minimal field supertrace and induced Einstein term

For a deliberately minimal baseline consisting of \(N_s\) real scalars and \(N_D\) four-component Dirac fermions, with no gauge vectors or ghosts yet included, define
\[
\operatorname{Str}_{\rm fields}=\sum_{\rm bosons}\operatorname{Tr}
-\sum_{\rm fermions}\operatorname{Tr}.
\]
For massless scalars and the torsion-free Dirac check above, the coefficient multiplying \(R_{\rm LC}\) in the field-supertraced \(a_2\) is
\[
C_R=\sum_{s=1}^{N_s}\left(\frac16-\xi_s\right)+\frac{N_D}{3}.
\]
The \(N_D/3\) term includes the four spinor components and the fermionic minus sign in the field supertrace. The leading \(a_0\) supertrace multiplicity is \(C_0=N_s-4N_D\). These expressions are only the declared scalar+Dirac baseline; vectors, gauge fixing, Faddeev–Popov ghosts, gravitino/other fields and any physical SUSY multiplets alter them.

With a proper-time UV cutoff \(\epsilon=\Lambda_{\rm UV}^{-2}\) and convention
\[
\Gamma_1=-\frac12\int_\epsilon^\infty\frac{ds}{s}
\operatorname{Str}_{\rm fields}\operatorname{Tr}(e^{-sP}),
\]
the local UV terms are
\[
\Gamma_{\rm UV}\supset
-\frac{1}{4(4\pi)^2\epsilon^2}\int d^4x\sqrt g\,C_0
-\frac{1}{2(4\pi)^2\epsilon}\int d^4x\sqrt g\,C_RR_{\rm LC}
-\frac{\log(1/\epsilon\mu^2)}{2(4\pi)^2}
\int d^4x\sqrt g\,\operatorname{Str}_{\rm fields}a_4^{\rm bracket}
+\cdots.
\]
Here \(a_4^{\rm bracket}\) means the dimension-four bracket before the common \((4\pi)^{-2}\) factor; finite terms and mass-dependent threshold functions have not been included. If the Euclidean Einstein term is written as \(-M_{\rm ind}^2\int\sqrt g\,R/2\), this minimal hard-cutoff baseline gives
\[
M_{\rm ind}^2=\frac{C_R}{(4\pi)^2}\Lambda_{\rm UV}^2,
\qquad
G_{\rm ind}=\frac{1}{8\pi M_{\rm ind}^2}
=\frac{2\pi}{C_R\Lambda_{\rm UV}^2},
\]
provided \(C_R>0\). This is a regulator- and field-content-dependent induced coefficient, not a prediction for the PSU model until its physical multiplets and cutoff are fixed. If \(C_R\leq0\), this baseline does not yield a positive Einstein kinetic coefficient with the stated convention.

## 6. What is and is not computed for the PSU throat

Computed exactly at the operator-formula level:
- the universal \(a_0,a_2,a_4\) expressions for any specified Laplace-type fluctuation operator;
- the scalar \(a_0,a_2,a_4\) for arbitrary \(m_s,\xi_s\);
- the torsion-free Dirac \(a_2\) trace check;
- the scalar+Dirac baseline coefficient \(C_R\) and its hard-cutoff mapping to \(M_{\rm ind}^2\), under the declared sign convention.

Not yet computed:
- the explicit \(E_D(K)\) and \(\Omega_D(K)\) for the actual throat contortion profile;
- the full \(\theta,l\)-dependent Levi-Civita curvature invariants of the toroidal metric in terms of \(N,r,R\);
- vector/graviton/ghost operators and their gauge fixing;
- interface heat-kernel coefficients for the PSU/Anti-Twin throat matching;
- the physical field multiplicities, masses, cutoff and renormalization conditions;
- the resulting numerical \(G_{\rm ind}\), \(\Lambda_{\rm ind}\), torsion couplings or semiclassical throat solution.

## 7. Immediate exact next step

Fix the contortion profile \(K^{ab}(l,\theta)\), field multiplets and throat matching/domain. Then construct \(P_i[e,\omega]\), complete each to Laplace type, compute \(E_i,\Omega_i\), insert them into section 2, and only then sum with physical statistics and ghosts. This gives a reproducible torsionful \(a_2/a_4\) calculation and a well-defined induced Einstein–Cartan action. Until these inputs are fixed, reporting numerical \(G_{\rm ind}\) would be fabricated.
