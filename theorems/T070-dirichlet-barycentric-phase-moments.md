# T070 — Dirichlet barycentres, covariance and phase moments on triangular cells

**Status: PROVED (exact local theorem).** The result extends the uniform barycentric–covariance quadrature law in T068. It is a cellwise integration identity; it is not a homogenisation theorem for the football shell or for the Morandotti structured-deformation functional.

## 1. Geometric setting and normalization

Let (F\subset\mathbb R^3) be a nondegenerate planar triangle with ordered vertices (v_0,v_1,v_2), area (A_F), and diameter (h_F). Write (V\in\mathbb R^{3\times3}) for the matrix whose rows are the vertices. For (x\in F), let (\lambda_0,\lambda_1,\lambda_2\geq0), (\sum_i\lambda_i=1), be its barycentric coordinates, so that
[
x=V^{\mathsf T}\lambda.
]

For parameters (a_i>0), set (S=a_0+a_1+a_2) and define
[
Z_F(a)=\int_F\prod_{i=0}^2\lambda_i^{a_i-1}\,dA.
]
The Dirichlet integral gives the exact partition function
[
\boxed{Z_F(a)=2A_F\,\frac{\Gamma(a_0)\Gamma(a_1)\Gamma(a_2)}{\Gamma(S)}.}
]
Equivalently, the dimensionless factor is the multivariate beta function (B_3(a)=\prod_i\Gamma(a_i)/\Gamma(S)). The normalized measure is
[
d\mu_{F,a}=Z_F(a)^{-1}\prod_i\lambda_i^{a_i-1}\,dA.
]
It is a probability measure because (a_i>0).

## 2. Exact weighted barycentre and covariance

The first and second Dirichlet moments are
[
\mathbb E_a[\lambda_i]=\frac{a_i}{S},\qquad
\operatorname{Cov}_a(\lambda_i,\lambda_j)
=C_{ij}
=\frac{a_i(S\delta_{ij}-a_j)}{S^2(S+1)}.
]
Consequently the physical weighted barycentre and its normalized ambient covariance are
[
\boxed{c_{F,a}=V^{\mathsf T}\frac{a}{S},\qquad
\Sigma_{F,a}=V^{\mathsf T}CV.}
]
In particular, (\Sigma_{F,a}\) is positive semidefinite and has rank at most two.

For (a=(1,1,1)), (Z_F=A_F), (c_{F,a}=(v_0+v_1+v_2)/3), and
[
\Sigma_{F,a}=\frac1{12}\sum_{i=0}^2(v_i-c_{F,a})(v_i-c_{F,a})^{\mathsf T},
]
which is exactly the covariance in T068. Thus T068 is the uniform special case of this weighted moment identity.

## 3. Cell quadrature theorem

Let (g\in C^3(U)), where (U) is an open neighbourhood of (F). Then
[
\int_F g(x)\,d\mu_{F,a}(x)
=g(c_{F,a})+\frac12D^2g(c_{F,a}):\Sigma_{F,a}+R_{F,a},
]
with
[
|R_{F,a}|\leq\frac{h_F^3}{6}\sup_{x\in F}\|D^3g(x)\|_{\mathrm{op}}.
]
Equivalently, for the unnormalized weighted integral,
[
\int_F g(x)\prod_i\lambda_i^{a_i-1}\,dA
=Z_F(a)\left[g(c_{F,a})+\frac12D^2g(c_{F,a}):\Sigma_{F,a}+R_{F,a}\right].
]
The identity is exact for every polynomial of degree at most two.

### Proof

Under (\mu_{F,a}), the barycentric random vector has the Dirichlet distribution with parameter (a). The displayed first and second moments follow from the gamma-ratio identity
[
\mathbb E_a\!\left[\prod_i\lambda_i^{m_i}\right]
=\frac{\Gamma(S)}{\Gamma(S+\sum_i m_i)}
\prod_i\frac{\Gamma(a_i+m_i)}{\Gamma(a_i)}
]
for nonnegative integers (m_i). Applying the affine map (x=V^{\mathsf T}\lambda) gives (c_{F,a}) and (\Sigma_{F,a}).

Taylor-expand (g) at (c_{F,a}). The linear term integrates to zero by the definition of the barycentre; the quadratic term integrates to (D^2g(c_{F,a}):\Sigma_{F,a}/2). Since both (x) and (c_{F,a}) lie in (F), (|x-c_{F,a}|\leq h_F). The third-order Taylor remainder therefore has absolute value at most (h_F^3\sup_F\|D^3g\|_{\rm op}/6), and integration against the probability measure preserves this bound. If (g) is quadratic, the third derivative vanishes. This proves the result.

## 4. Linear phase moment

For a real affine phase (\theta(x)=\theta(c_{F,a})+k\cdot(x-c_{F,a})), with (k\in\mathbb R^3),
[
\int_F e^{i\theta(x)}\,d\mu_{F,a}(x)
=e^{i\theta(c_{F,a})}
\left[1-\frac12k^{\mathsf T}\Sigma_{F,a}k+\rho_{F,a}(k)\right],
]
where
[
|\rho_{F,a}(k)|\leq\frac{|k|^3h_F^3}{6}.
]
This follows by Taylor expansion of (e^{iu}), using (\mathbb E_a[k\cdot(X-c_{F,a})]=0) and (\mathbb E_a[(k\cdot(X-c_{F,a}))^2]=k^{\mathsf T}\Sigma_{F,a}k). The formula is a controlled small-cell phase-moment expansion; it is not a dynamical phase law.

## 5. Relation to gradients and structured-deformation energies

The theorem applies cellwise to any scalar density (g(x)) obtained after evaluating a sufficiently smooth local energy density on fields, for example
[
g(x)=W\bigl(x,\nabla_{\!S}u(x),G(x),\theta(x),\nabla_{\!S}\theta(x)\bigr),
]
provided the resulting composition is (C^3) on the cell and the derivatives are bounded. Its Hessian then contains the spatial, field-gradient and chain-rule contributions of the chosen constitutive density. The theorem supplies a local quadrature correction and a remainder estimate; it does not establish compactness, lower semicontinuity, a recovery sequence, or a surface homogenisation limit.

For a football mesh, the formula can be applied to each of the 180 triangular CST facets once their actual coordinates and connectivity are supplied. The exact 92-node/180-facet shell counts do not determine the coordinates, panel-centre placement, or material frames; no numerical shell centroid or shell-wide energy is asserted here.

## 6. Gamma, Beta, zeta and Bernoulli boundary

The Gamma/Beta connection is exact and is the normalization mechanism for the weighted barycentre:
[
B_3(a)=\frac{\prod_i\Gamma(a_i)}{\Gamma(S)}.
]
Differentiating (log Z_F(a)) with respect to (a_i) generates logarithmic barycentric moments, since
[
\partial_{a_i}\log Z_F(a)=\mathbb E_a[\log\lambda_i]
=\psi(a_i)-\psi(S).
]
Higher derivatives give covariances of (log\lambda_i) and involve polygamma functions. Zeta values and Bernoulli numbers enter through established special-function expansions of polygamma functions (and, in a separate discrete-summation setting, Euler–Maclaurin). They do **not** automatically appear as coefficients of a football-mesh refinement expansion. Such coefficients require a specified refinement family and a proved summation/asymptotic formula.

### Numerical Duffy–Gauss–Jacobi implementation

The central repository also contains a Duffy–Gauss–Jacobi quadrature implementation for the weighted integral. It uses
\[
\lambda_0=(1-s)(1-t),\quad \lambda_1=s,\quad \lambda_2=(1-s)t,
\]
with Jacobi parameters
\[
(\alpha_s,\beta_s)=(a_0+a_2-1,a_1-1),\qquad
(\alpha_t,\beta_t)=(a_0-1,a_2-1),
\]
and the two independent map factors \(2^{-(\alpha+\beta+1)}\). The physical integral includes the factor \(2A_F\).

The routine explicitly returns both the raw second moment
\[
M_{ij}=\mathbb E[\lambda_i\lambda_j]
\]
and the covariance
\[
C=M-\mathbb E[\lambda]\mathbb E[\lambda]^T.
\]
This distinction prevents the raw-moment/covariance error in numerical implementations. Source: src/dirichlet_triangle_quadrature.py; A1–A3 tests: tests/test_dirichlet_triangle_quadrature.py; derivation: docs/DIRICHLET_DUFFY_JACOBI_QUADRATURE.md. The tests are present but are not declared passed until executed.

## 7. Evidence classification and exclusions

- **PROVED:** Dirichlet normalization; weighted barycentre and covariance; cell Taylor identity and cubic remainder; affine-phase expansion and its stated bound.
- **EXACT SPECIAL-FUNCTION IDENTITIES:** Gamma/multivariate-Beta normalization and logarithmic derivatives.
- **OPEN:** application to the actual football mesh; global error accumulation over 180 facets; a compatible refined family (P_N), coherent maps and weak convergence of surface measures; Bernoulli coefficients for that refinement; surface structured-deformation homogenisation; any physical interpretation of the phase.
- This record does not identify a triangle covariance with the Q6 point-cloud covariance or the Q6 vertex-measure covariance. Those are distinct measures and dimensions (see T068 and T069).
- This record does not claim that the Veneziano amplitude is a shell integral. Any such connection requires a separately defined map of variables and a mathematical statement.

## 8. Relation to existing records

- **T068:** uniform triangle barycentric covariance and Taylor quadrature; recovered as (a=(1,1,1)).
- **T069:** Q6 antipodal pairing and total covariance; a distinct finite vertex-pair measure.
- **Morandotti structured deformations:** the present result is a local cell-integration tool for a sufficiently regular bulk density. It is not the periodic homogenisation theorem for structured deformations and does not extend that theorem to a curved closed shell.
