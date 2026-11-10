# T078 — Phase–Theta–Zeta–Barycentric Spectral Bridge

**Status:** exact Dirichlet characteristic-function identity and standard theta/modular identities; proposed phase-bundle coupling; spectral determinant and football-shell realization OPEN.

## 1. Purpose and sector convention

T078 extends T070 and T077 by adding circle-valued phase data without identifying the two physical sectors:

- **Right sector = gauge:** a Hermitian bundle \(E_R\to S\), connection \(A\), section \(\Psi\), and covariant derivative \(D_A\Psi\).
- **Left sector = fluid:** \((\rho,v,p,\Phi)\), with Bernoulli scalar \(B_L=p+\frac12\rho |v|_g^2+\rho\Phi\) under the hypotheses stated in T077.
- **Shared cell geometry:** barycentre \(c_{F,a}\), covariance \(\Sigma_{F,a}\), and tangent anisotropy \(M_{F,a}\).
- **Phase data:** a circle-valued field \(u=e^{i\theta}\), treated as a section of a unitary line bundle when global topology requires it.

The right/gauge and left/fluid assignment is fixed. A phase variable does not by itself create a physical coupling between them.

## 2. Dirichlet barycentric phase characteristic function

Let \(F\) be a triangle with barycentric coordinates \(\lambda_i\geq0\), \(\sum_{i=0}^2\lambda_i=1\), and positive parameters \(a_i\), \(S=\sum_i a_i\). The normalized Dirichlet measure is
\[
d\mu_a(\lambda)=\frac{\Gamma(S)}{\prod_i\Gamma(a_i)}
\prod_{i=0}^2\lambda_i^{a_i-1}\,d\lambda_0d\lambda_1
\]
on the simplex, with \(\lambda_2=1-\lambda_0-\lambda_1\).

Choose real lifts \(\vartheta_i\) of three vertex phases and define the affine lifted phase
\[
\Theta_F(\lambda)=\sum_{i=0}^2\lambda_i\vartheta_i.
\]
Its Fourier/characteristic transform is
\[
\Phi_F(t;a,\vartheta)
=\mathbb E_a[e^{it\Theta_F}]
=\int_{\Delta_2}e^{it\sum_i\lambda_i\vartheta_i}\,d\mu_a(\lambda).
\]
This is an exact, well-defined local construction for fixed real lifts. It is not yet an intrinsic interpolation of three arbitrary points on \(U(1)\): changing a lift by \(2\pi k_i\) can change the interior interpolation. A global construction must specify a branch, a connection and/or winding data.

Expanding the exponential and using Dirichlet moments gives
\[
\Phi_F(t;a,\vartheta)
=\sum_{k_0,k_1,k_2\geq0}
\frac{(it)^{|k|}\prod_i(a_i)_{k_i}\vartheta_i^{k_i}}
{(S)_{|k|}\prod_i k_i!},
\]
where \((x)_k=\Gamma(x+k)/\Gamma(x)\). Equivalently this is the confluent Lauricella function
\[
\Phi_F(t;a,\vartheta)
=\Phi_2^{(3)}(a_0,a_1,a_2;S;
it\vartheta_0,it\vartheta_1,it\vartheta_2).
\]
The series is entire in \(t\) for fixed finite \(\vartheta_i\). In particular,
\[
\Phi_F(0)=1,\quad
\Phi_F'(0)=i\,\mathbb E_a[\Theta_F],\quad
-\Phi_F''(0)=\mathbb E_a[\Theta_F^2].
\]
The mean and variance are
\[
\mathbb E_a[\Theta_F]=\sum_i\frac{a_i}{S}\vartheta_i,
\qquad
\operatorname{Var}_a(\Theta_F)
=\frac{1}{S+1}\left[
\sum_i\frac{a_i}{S}\vartheta_i^2
-\left(\sum_i\frac{a_i}{S}\vartheta_i\right)^2
\right].
\]
Thus the first two phase moments are controlled by the same Dirichlet barycentric measure as T070.

The unnormalized transform is
\[
\mathcal Z_F(a,t,\vartheta)
=2A_F\frac{\prod_i\Gamma(a_i)}{\Gamma(S)}
\Phi_F(t;a,\vartheta).
\]
At \(t=0\), it reduces exactly to the T070 partition function \(Z_F(a)\). Differentiating \(\log \mathcal Z_F\) in \(a_i\) at \(t=0\) recovers the digamma/polygamma identities in T070. At nonzero \(t\), mixed derivatives generate mixed log-barycentric/phase cumulants, wherever the logarithm is defined locally (zeros of \(\Phi_F\) must be excluded).

## 3. Phase as a gauge-bundle object

For a unitary line bundle with local connection convention \(D_A=d+iA\), write locally \(u=e^{i\theta}\). Then
\[
D_Au=i(d\theta+A)u.
\]
Under \(u\mapsto e^{-i\chi}u\), \(A\mapsto A+d\chi\), the one-form
\[
\alpha=d\theta+A
\]
is invariant. Its holonomy data are encoded by \(\exp(i\oint_C A)\), with the usual care that a nontrivial bundle may require several charts and transition functions.

For a cellwise phase model, the vertex values must therefore be understood as local lifts compatible with a chosen trivialization. Across a seam or chart overlap, the phase lifts and connection transition must transform together. The affine interpolation in §2 is a local coordinate formula, not a substitute for bundle gluing.

A gauge-covariant phase energy can be written
\[
\mathcal E_{\theta,F}
=\frac{\kappa_\theta}{2}\int_F
|d\theta+A|_{g_A}^2\,d\mu_{F,a},
\]
where \(\kappa_\theta\) carries the units required by the chosen action and \(g_A\) is a positive tangent metric. This expression is gauge invariant under the convention above. Its relation to the full right-sector field \(\Psi\) must be derived from the representation and decomposition of \(\Psi\); it is not automatically an independent extra energy.

## 4. From periodic phases to Jacobi theta: the missing winding sum

A single characteristic function \(\Phi_F(t)\) is not generally a Jacobi theta function. A theta function appears when periodicity is combined with a quadratic weight on an integer winding/charge lattice.

Let \(\Lambda\cong\mathbb Z^r\) be a specified winding or charge lattice, \(Q\) a positive-definite integral quadratic form (or a positive-definite real form with an explicitly stated lattice), and \(\tau\) lie in the Siegel upper half-space (for \(r=1\), \(\operatorname{Im}\tau>0\)). Define
\[
\Theta_{\Lambda,Q}(z\mid\tau)
=\sum_{m\in\Lambda}
\exp\!\left(\pi i\tau Q(m)+2\pi i\,\langle m,z\rangle\right).
\]
Positive definiteness and \(\operatorname{Im}\tau>0\) ensure absolute, locally uniform convergence. For \(r=1\), \(Q(m)=m^2\), this is a standard Jacobi theta series, up to the chosen characteristic and normalization.

The proposed bridge is therefore two-stage:
1. the Dirichlet characteristic function supplies local barycentric phase moments;
2. a separately specified global winding/charge lattice and quadratic action periodizes those data into a theta series.

The lattice, quadratic form, characteristics, and gluing law are not determined by the three barycentric parameters \(a_i\). They must come from the topology and dynamics of the phase bundle (or from an explicitly declared discrete model). No theta identity is claimed until those data are fixed.

## 5. Theta constants and Dedekind eta

For the standard Jacobi theta constants, with consistent nome conventions,
\[
\vartheta_2(0\mid\tau)\,
\vartheta_3(0\mid\tau)\,
\vartheta_4(0\mid\tau)=2\eta_{\rm Ded}(\tau)^3,
\]
where
\[
\eta_{\rm Ded}(\tau)
=e^{\pi i\tau/12}\prod_{n=1}^\infty(1-e^{2\pi i n\tau}).
\]
The eta function transforms with weight \(1/2\) and a multiplier system. These identities give a precise modular bridge once a genuine theta series and modular parameter \(\tau\) have been constructed.

The implication is not “phase implies Dedekind eta.” It is:
\[
\text{periodic phase + quadratic lattice sum}
\longrightarrow \text{theta series}
\longrightarrow \text{theta-product identities involving }\eta_{\rm Ded}.
\]
A particular eta factor, power, multiplier and modular subgroup depend on the lattice and normalization.

## 6. Spectral zeta and determinant: a separate operator is required

Let \(L\) be a positive self-adjoint elliptic operator with discrete positive spectrum \(\{\lambda_j\}\), after removing or separately treating zero modes. Its spectral zeta function is initially
\[
\zeta_L(s)=\sum_j\lambda_j^{-s}
\]
in a right half-plane and is continued meromorphically when the operator class permits. The zeta-regularized determinant is
\[
\det{}'_\zeta L=\exp[-\zeta_L'(0)].
\]
This gives a rigorous route from a specified spectrum to a regularized product. To obtain a Dedekind eta factor, one must calculate \(\zeta_L'(0)\) for the actual operator and show that the resulting product equals the required eta expression, including zero-mode and normalization factors.

For a one-dimensional periodic operator, a lattice spectrum can produce Hurwitz/Riemann zeta factors; for two-dimensional flat tori, theta transformations and modular forms naturally enter heat-kernel and determinant formulae. But the exact determinant depends on the operator, geometry, boundary conditions, bundle holonomy and scale. T078 does not assert a universal determinant-to-eta identity for the football shell.

## 7. Gamma–Beta–polygamma–zeta and Bernoulli network

The local barycentric branch remains the one established in T070:
\[
B_3(a)=\frac{\prod_i\Gamma(a_i)}{\Gamma(S)},\qquad
\partial_{a_i}\log B_3=\psi(a_i)-\psi(S),
\]
\[
\partial_{a_i}\partial_{a_j}\log B_3
=\delta_{ij}\psi_1(a_i)-\psi_1(S),
\qquad
\psi^{(m)}(z)=(-1)^{m+1}m!\zeta(m+1,z),\quad m\geq1.
\]
Bernoulli polynomials also encode the Fourier coefficients of periodic functions and the special values
\[
\zeta(1-n,x)=-\frac{B_n(x)}{n},\quad n\geq1.
\]
The Euler–Maclaurin expansion of Hurwitz zeta introduces Bernoulli numbers under its standard remainder hypotheses. This is analytically related to the phase-periodic branch, but it is distinct from the fluid Bernoulli scalar/law in T077.

Keep the notational distinctions:
- Euler beta integral \(B(x,y)\) versus Dirichlet beta \(L(s,\chi_{-4})\);
- Dirichlet eta \((1-2^{1-s})\zeta(s)\) versus Dedekind eta \(\eta_{\rm Ded}(\tau)\);
- Hurwitz zeta \(\zeta(s,a)\) versus Riemann zeta \(\zeta(s)\).

## 8. Coupling to the right gauge and left fluid sectors

The cellwise second-moment expansion from T068–T070 applies separately to smooth scalar densities in the two sectors:
\[
\int_F g_R\,d\mu_{F,a}
=g_R(c_{F,a})+\tfrac12D^2g_R(c_{F,a}):\Sigma_{F,a}+R_R,
\]
\[
\int_F g_L\,d\mu_{F,a}
=g_L(c_{F,a})+\tfrac12D^2g_L(c_{F,a}):\Sigma_{F,a}+R_L.
\]
Here \(g_R\) is built from gauge-covariant derivatives and \(g_L\) from a declared fluid energy or Bernoulli-derived observable. The same barycentric covariance samples both, but their derivatives and transformation laws remain distinct.

A formal generating functional may be introduced only after the densities are made dimensionless:
\[
\mathscr Z_F
=\int_F
\exp[-\beta_R\widehat g_R(x)-\beta_L\widehat g_L(x)]
\,d\mu_{F,a}(x),
\]
where \(\widehat g_R,\widehat g_L\) are dimensionless and \(\beta_R,\beta_L\) are dimensionless source parameters (or are defined with explicit reference scales). Then
\[
-\partial_{\beta_R}\log\mathscr Z_F=\langle\widehat g_R\rangle,\qquad
-\partial_{\beta_L}\log\mathscr Z_F=\langle\widehat g_L\rangle,
\]
and
\[
\partial_{\beta_R}\partial_{\beta_L}\log\mathscr Z_F
=\operatorname{Cov}(\widehat g_R,\widehat g_L).
\]
This mixed covariance is a diagnostic of statistical dependence under the chosen common measure. It is not, by itself, a dynamical interaction term or a derivation of coupled Euler–Yang–Mills equations. Any actual cross-sector interaction must be specified by a gauge-invariant, dimensionally consistent local density and derived from a variational principle.

The phase factor may be inserted as a source,
\[
\mathscr Z_F(t)=\int_F
e^{it\Theta_F(x)}
e^{-\beta_R\widehat g_R(x)-\beta_L\widehat g_L(x)}
\,d\mu_{F,a}(x),
\]
but a global gauge-invariant version must replace the local lifted \(\Theta_F\) by a bundle-compatible holonomy/parallel-transport construction. This distinction is essential.

## 9. Anisotropy and the football/PRISM programme

The covariance \(M_{F,a}=\Sigma_{F,a}/\operatorname{tr}\Sigma_{F,a}\) is the geometric sampling anisotropy. A PRISM-induced tangent endomorphism \(A_T\) may be composed with it only after the canonical triplett and tangent representation are fixed (T077). A positive anisotropic metric can be written, for sufficiently small \(\epsilon\) relative to the spectrum of the symmetric part,
\[
g_\epsilon(\xi,\xi)=g(\xi,\xi)+\epsilon\,g(A_T\xi,\xi)>0.
\]
The phase kinetic term, right gauge energy and left fluid diagnostics can then be evaluated with the same tangent metric while retaining their separate bundle/field structures.

The shell realization still requires: (i) canonical PRISM triplett matrices and class labels; (ii) a bundle-compatible phase assignment on each facet; (iii) transition/holonomy data across seams; (iv) a specified global winding lattice and quadratic form; and (v) an operator whose spectral determinant is actually computed. The 90 seams are gluing interfaces, not a substitute for these definitions.

## 10. Status and verification programme

**EXACT / STANDARD**
- Dirichlet characteristic-function series and its first two moments in §2.
- Gamma-normalized Dirichlet partition function at \(t=0\).
- Gauge invariance of \(d\theta+A\) under the declared convention.
- Theta-series convergence for positive-definite lattice form and \(\operatorname{Im}\tau>0\).
- Jacobi theta-constant/Dedekind eta identity with consistent conventions.
- Definition of zeta-regularized determinant for a specified admissible operator.

**CANDIDATE**
- Phase-resolved barycentric generating functional.
- Joint right-gauge/left-fluid statistical generator with separate sources.
- Composition of the PRISM tangent anisotropy and the barycentric covariance.

**OPEN**
1. Choose and justify the phase bundle and its topology on the shell.
2. Fix the local lift/transition/holonomy prescription so the phase interpolation is intrinsic.
3. Recover the canonical 216 PRISM triplett matrices and 20 Gram classes and define their action on the phase bundle.
4. Derive the winding lattice \(\Lambda\), quadratic form \(Q\), theta characteristics and modular parameter \(\tau\) from the model rather than fitting them post hoc.
5. Specify the elliptic operator, domain, boundary/seam conditions and zero-mode treatment; compute \(\zeta_L'(0)\) and test whether \(\det'_\zeta L\) contains a Dedekind eta factor.
6. Derive any right/left interaction from a gauge-invariant variational density; do not infer it from a mixed statistical covariance alone.
7. Prove refinement stability and global error bounds across the shell; numerical agreement alone is not a proof.

## 11. Linked records

- T068 — uniform triangular centroid, covariance and local quadrature.
- T069 — Q6 antipodality and vertex covariance (not the cell covariance).
- T070 — Dirichlet barycentres, Gamma/Beta normalization and logarithmic moments.
- T073/T076 — football shell, tangent anisotropy and seam mechanics.
- T077 — Bernoulli-gradient-barycentre bridge between right gauge and left fluid sectors.
