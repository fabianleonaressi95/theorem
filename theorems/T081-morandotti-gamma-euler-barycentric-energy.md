# T081 — Morandotti second-order field and Euler Gamma through barycentric energy integration

**Status:** the second-order structured-deformation density and the Dirichlet/Gamma normalization are established mathematical ingredients. Their composition below is an exact finite-cell identity when the density is integrable. Any physical constitutive identification and any continuum limit on the Q-ball remain open.

## 1. Two different Gamma objects

Write \(\Gamma_{\mathrm{Mor}}(x)\) for the second-order structured-deformation field and \(\Gamma_E(s)\) for Euler's Gamma function:
\[
\Gamma_E(s)=\int_0^\infty t^{s-1}e^{-t}\,dt,\qquad \Re s>0.
\]
They are categorically different objects. \(\Gamma_{\mathrm{Mor}}\) is a field (with tensorial type fixed by the second-order kinematics); \(\Gamma_E\) is a scalar meromorphic function.

In the second-order theory of Barroso–Matias–Morandotti–Owen, the relaxed bulk density depends on \(x,G,\nabla G,\Gamma_{\mathrm{Mor}}\), with a separate interfacial contribution. In particular, the integral representation has the form
\[
I_2(G,\Gamma_{\mathrm{Mor}})
=\int_\Omega W_2(x,G,\nabla G,\Gamma_{\mathrm{Mor}})\,dx
+\int_{S_G\cap\Omega}\gamma_2(x,G,[G],\nu_G)\,d\mathcal H^{N-1},
\]
under the paper's hypotheses. This Euclidean theorem is not itself a theorem on the curved Q-ball shell.

## 2. Exact Dirichlet/Gamma bridge on a triangular cell

Let \(F=\operatorname{conv}(x_1,x_2,x_3)\) and let \(\lambda=(\lambda_1,\lambda_2,\lambda_3)\) have the Dirichlet distribution with parameters \(a_i>0\), \(S=a_1+a_2+a_3\). Set
\[
x(\lambda)=\sum_{i=1}^3\lambda_i x_i,
\quad
\mathcal W_F(\lambda)=
W_2\!\left(x(\lambda),G(x(\lambda)),
\nabla G(x(\lambda)),\Gamma_{\mathrm{Mor}}(x(\lambda))\right).
\]
The normalized density is
\[
p_a(\lambda)=
\frac{\Gamma_E(S)}{\prod_i\Gamma_E(a_i)}
\prod_i\lambda_i^{a_i-1}.
\]
Therefore, whenever the integral is finite,
\[
\boxed{
\mathcal E_F(a)=
\frac{\Gamma_E(S)}{\prod_i\Gamma_E(a_i)}
\int_{\Delta_2}\mathcal W_F(\lambda)
\prod_i\lambda_i^{a_i-1}\,d\lambda_1d\lambda_2.
}
\]
This is the direct bridge: the Morandotti field is an argument of the local energy density, while Euler's Gamma function normalizes the barycentric measure used to average that energy. It is not an identification \(\Gamma_{\mathrm{Mor}}=\Gamma_E\).

For constant \(\mathcal W_F=W_0\), \(\mathcal E_F(a)=W_0\), since the Dirichlet density integrates to one. This is a useful normalization check.

## 3. Parameter derivatives: digamma and polygamma

For a parameter \(a_i\), differentiation under the integral is justified, for example, when the density and its logarithmic moments admit a common integrable majorant in a neighbourhood of \(a\). Then
\[
\partial_{a_i}\log p_a(\lambda)
=\psi(S)-\psi(a_i)+\log\lambda_i,
\]
where \(\psi=\Gamma_E'/\Gamma_E\) is the digamma function. Consequently
\[
\boxed{
\partial_{a_i}\mathcal E_F(a)
=\mathbb E_a\!\left[
\mathcal W_F(\lambda)
\{\psi(S)-\psi(a_i)+\log\lambda_i\}
\right].
}
\]
The score has zero mean, so a constant cell density has zero parameter derivative, as required.

The second derivatives involve
\[
\partial_{a_j}\partial_{a_i}\log p_a
=\psi_1(S)-\delta_{ij}\psi_1(a_i),
\]
and products of score functions. Thus trigamma/polygamma functions arise as exact sensitivities of the barycentric averaging measure. These derivatives quantify how the averaged second-order energy responds to changes in barycentric concentration; they do not by themselves constitute a physical evolution law for \(\Gamma_{\mathrm{Mor}}\).

## 4. Polynomial energy densities: exact finite Gamma ratios

If the cell energy density is a polynomial in barycentric coordinates,
\[
\mathcal W_F(\lambda)=\sum_{k\in\mathbb N^3}c_k\lambda_1^{k_1}\lambda_2^{k_2}\lambda_3^{k_3}
\]
with finitely many nonzero coefficients, then
\[
\boxed{
\mathcal E_F(a)=
\sum_k c_k
\frac{\prod_{i=1}^3(a_i)_{k_i}}{(S)_{|k|}},
}
\]
where \((z)_m=\Gamma_E(z+m)/\Gamma_E(z)\). This follows from the Dirichlet moments and gives an exact route for affine/quadratic finite-element ansatzes for \(G,\nabla G,\Gamma_{\mathrm{Mor}}\), provided the resulting energy density is polynomial in \(\lambda\).

For non-polynomial constitutive densities, use the T068–T070 Taylor/quadrature estimates with explicit remainder bounds; do not replace an exact integral by a moment truncation without recording its error.

## 5. How Beta, zeta and eta enter — and where they do not

- Euler Beta is the two-parameter simplex normalization \(B(x,y)=\Gamma_E(x)\Gamma_E(y)/\Gamma_E(x+y)\); it appears on edges and in iterated simplex integrations.
- Digamma/polygamma appear when differentiating the Dirichlet normalization or logarithmic moments.
- Hurwitz zeta is related to polygamma at positive integer order:
  \[
  \psi^{(m)}(z)=(-1)^{m+1}m!\,\zeta(m+1,z),\qquad m\ge1.
  \]
- Dirichlet eta \(\eta_D(s)=(1-2^{1-s})\zeta(s)\) is distinct from Dedekind eta \(\eta_{\mathrm{Ded}}(\tau)\). Neither follows automatically from the local Morandotti field. They can enter only after a specified series/spectral or modular structure has been derived.
- A zeta-regularized determinant requires a specified elliptic operator, domain, boundary conditions and zero-mode prescription. It is not supplied merely by writing \(\Gamma_{\mathrm{Mor}}\) in an energy density.

## 6. Candidate second-order cell functional for the Q-ball

A controlled finite-cell model is
\[
E_F^{(2)}(a)=|F|\,\mathbb E_a\!\left[
W_2(x(\lambda),G,\nabla G,\Gamma_{\mathrm{Mor}})
\right]
+\int_{\partial F\cap\Gamma_{\mathrm{seam}}}
\gamma_{\mathrm{seam}}(G^+,G^-,\nu)\,d\mathcal H^1.
\]
The first term is bulk sampling of the second-order density; the second is an explicitly separate interface energy. The latter must use covariantly compared panel traces when panel frames/bundles differ. It is not fixed by the Dirichlet normalization.

The cell covariance from T068–T070 gives the second-order spatial correction for a smooth scalar energy density \(q\):
\[
\mathbb E_a[q(x(\lambda))]
=q(c_a)+\frac12D^2q(c_a):\Sigma_{F,a}+R_F.
\]
Here \(q=W_2(x,G,\nabla G,\Gamma_{\mathrm{Mor}})\). This is the exact point at which the barycentric covariance probes the spatial variation of the Morandotti second-order energy.

## 7. Research consequences and proof obligations

1. Fix the precise tensor type, transformation law and regularity of \(\Gamma_{\mathrm{Mor}}\) on each shell chart.
2. Specify \(W_2\) and the interface density \(\gamma_{\mathrm{seam}}\), including frame covariance and coercivity/growth.
3. Define how \(G,\nabla G,\Gamma_{\mathrm{Mor}}\) are reconstructed on each triangle and transported across panel transitions.
4. Prove integrability and uniform bounds that justify differentiating the Dirichlet expectation with respect to \(a\).
5. Prove consistency of the barycentric quadrature for the second-order density.
6. For a continuum theorem, establish equicoercivity, liminf and recovery sequence on a shape-regular refinement family of the curved shell.
7. Only after deriving the Hessian/linearized operator of the relaxed energy should one investigate spectral zeta functions or determinants.

## 8. References and classification

- Barroso, Matias, Morandotti & Owen, *Second-Order Structured Deformations: Relaxation, Integral Representation and Applications*, Arch. Rational Mech. Anal. 225 (2017), 1025–1072, DOI 10.1007/s00205-017-1120-5; arXiv:1607.02311.
- T068–T070: exact triangle covariance, Dirichlet barycentres, Gamma/Beta normalization, moments and quadrature.
- T079–T080: surface structured-gradient bridge and finite discrete Stokes complex.

| Statement | Status |
|---|---|
| Morandotti second-order relaxed density depends on \(G,\nabla G,\Gamma_{\mathrm{Mor}}\) | Established in cited Euclidean setting |
| Dirichlet normalization by Euler Gamma | Established identity |
| Dirichlet average of the Morandotti density | Exact definition/identity when integrable |
| Parameter derivatives via digamma/polygamma | Exact under differentiation-under-integral hypotheses |
| Polynomial cell energy Gamma-ratio formula | Exact |
| Q-ball constitutive law for \(\Gamma_{\mathrm{Mor}}\) | Open |
| Curved-shell relaxation/homogenization | Open |
| Spectral zeta/determinant of the relaxed Hessian | Not yet defined; open |
