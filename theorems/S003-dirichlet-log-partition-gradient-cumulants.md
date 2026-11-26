# S.3 — Gradient and Hessian of the Dirichlet log-partition function

**Status: PROVED (exact special-function identity).** This lemma supplies the exact parameter-gradient link between the Gamma/Beta normalization, logarithmic barycentric observables, and their fluctuations.

## Statement

For (a=(a_0,a_1,a_2)\in(0,\infty)^3), let
[
B_3(a)=\frac{\Gamma(a_0)\Gamma(a_1)\Gamma(a_2)}{\Gamma(S)},
\qquad S=a_0+a_1+a_2,
]
and let (\lambda\) have the Dirichlet distribution with parameter (a). Write (\psi=\Gamma'/\Gamma) and (\psi_1=\psi') for the digamma and trigamma functions. Then
[
\boxed{\frac{\partial}{\partial a_i}\log B_3(a)
=\psi(a_i)-\psi(S)
=\mathbb E_a[\log\lambda_i].}
]
The Hessian is
[
\boxed{\frac{\partial^2}{\partial a_i\partial a_j}\log B_3(a)
=\delta_{ij}\psi_1(a_i)-\psi_1(S)
=\operatorname{Cov}_a(\log\lambda_i,\log\lambda_j).}
]
Thus the gradient of the log-partition function gives the mean logarithmic barycentric coordinates, while its Hessian gives their covariance matrix.

## Proof

The Dirichlet density on the reference simplex is (B_3(a)^{-1}\prod_i\lambda_i^{a_i-1}). Differentiation under the integral sign is justified locally uniformly for (a_i>0), since logarithmic factors are integrable against the corresponding positive-power boundary weights. Differentiating (B_3) once inserts (\log\lambda_i) into the normalized integral, hence
[
\partial_{a_i}\log B_3(a)=\mathbb E_a[\log\lambda_i].
]
Differentiating a second time gives the covariance of the two sufficient statistics (\log\lambda_i) and (\log\lambda_j). Direct differentiation of the Gamma quotient gives the displayed digamma and trigamma expressions.

## Bernoulli and zeta connection

The connection to Bernoulli numbers is through the standard large-argument asymptotic expansions
[
\psi(z)\sim\log z-\frac1{2z}
-\sum_{k\geq1}\frac{B_{2k}}{2k\,z^{2k}},
]
[
\psi_1(z)\sim\frac1z+\frac1{2z^2}
+\sum_{k\geq1}\frac{B_{2k}}{z^{2k+1}}.
]
The even zeta values satisfy
[
\zeta(2k)=(-1)^{k+1}\frac{B_{2k}(2\pi)^{2k}}{2(2k)!}.
]
These identities explain how Bernoulli and zeta constants can enter a large-parameter asymptotic analysis of the Dirichlet log-partition function. They do not, by themselves, prove a Bernoulli expansion for a sequence of football meshes: that requires a specified refinement and a separate summation theorem.

## Relation to T068, T070 and Morandotti

- T070 gives the physical weighted barycentre (c_{F,a}), covariance (\Sigma_{F,a}), and local phase moments on a triangle.
- This lemma gives derivatives with respect to the **Dirichlet parameters** (a_i). These parameter derivatives must not be confused with the spatial gradient (\nabla_S u) appearing in a structured-deformation energy.
- If a smooth cell energy density depends on spatial fields and their gradients, T070 controls its local spatial quadrature once the composed density is (C^3). This lemma separately controls sensitivity to the barycentric weighting parameters.
- Together they provide exact local ingredients for a future surface energy analysis. Neither result proves the compactness, lower-semicontinuity, recovery-sequence or homogenisation statements required for a Morandotti-type limit on a curved shell.

## Evidence classification

- **PROVED:** log-partition gradient and Hessian identities.
- **STANDARD ASYMPTOTICS:** digamma/trigamma Bernoulli expansions and the even-zeta/Bernoulli identity.
- **OPEN:** a mesh-refinement theorem deriving explicit Bernoulli/zeta coefficients for the football shell or for the RGS–PRISM family.
