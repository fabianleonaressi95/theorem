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

## 3.1. Topological phase sectors of the closed truncated-icosahedral shell

Let \(K\) be the cellular decomposition of the closed truncated-icosahedral surface: 60 vertices, 90 physical seams (1-cells), and 32 polygonal panels (12 pentagons and 20 hexagons). It is a connected cellulation of a sphere, not merely the seam graph. Its Euler characteristic is
\[
\chi(K)=V-E+F=60-90+32=2.
\]
Consequently, with integer coefficients,
\[
H_0(K;\mathbb Z)\cong\mathbb Z,\qquad
H_1(K;\mathbb Z)=0,\qquad
H_2(K;\mathbb Z)\cong\mathbb Z.
\]
The seam graph by itself has cycle rank
\[
\operatorname{rank}\ker\partial_1=E-V+1=90-60+1=31.
\]
These 31 graph cycles are not 31 independent topological winding sectors of the closed shell: the 32 oriented panel boundaries span the graph cycle lattice, with one relation (the oriented sum of all panel boundaries is zero). Equivalently, \(\operatorname{rank}\operatorname{im}\partial_2=31\), so \(H_1=\ker\partial_1/\operatorname{im}\partial_2=0\). This is the precise distinction between cycles of the seam graph and homology of the completed shell.

For a flat \(U(1)\) connection on the closed shell, gauge-equivalence classes are classified by
\[
H^1(S^2;U(1))\cong\operatorname{Hom}(H_1(S^2),U(1))=0.
\]
Thus there is no nontrivial flat Wilson-loop winding sector on the unpunctured shell. A seam-graph loop can have nontrivial holonomy only if the connection has curvature through the panel region it bounds, or if a defect/puncture or altered gluing is introduced. It would be incorrect to infer a nonzero \(H^1\) lattice merely from the 31 independent graph cycles.

There is, however, a distinct integer topological sector for complex line bundles:
\[
\operatorname{Pic}_{U(1)}(S^2)\ \text{(topological classes)}
\cong H^2(S^2;\mathbb Z)\cong\mathbb Z,
\qquad
c_1(L)=\frac{1}{2\pi}\int_{S^2}F_A=n\in\mathbb Z,
\]
where \(F_A=dA\) in local unitary trivializations and the sign follows the chosen orientation/connection convention. This integer is magnetic/first-Chern flux, not a flat one-cycle winding. A nonzero \(n\) requires a nontrivial line bundle and cannot be represented by one globally defined smooth potential \(A\) on all of \(S^2\); use local potentials and transition functions on overlaps.

**Candidate topological theta sector.** If the model assigns an action quadratic in the Chern number, with a positive dimensionless coefficient \(g^{-2}\), and a topological angle \(\vartheta_{\rm top}\), then summing over line-bundle sectors gives the schematic factor
\[
Z_{\rm top}(\tau,z)
=\sum_{n\in\mathbb Z}\exp\!\left(\pi i\tau n^2+2\pi i n z\right)
=\vartheta_3(z\mid\tau),
\qquad \operatorname{Im}\tau>0.
\]
For example, a Euclidean weight \(\exp[-c n^2/g^2+i n\vartheta_{\rm top}]\), \(c>0\), is of this form with \(\tau=i c/(\pi g^2)\) and \(z=\vartheta_{\rm top}/(2\pi)\). The coefficient \(c\), the normalization of the flux action, and the existence of a physical sum over line bundles must be derived from the chosen gauge action; they are not fixed by the shell combinatorics. This gives a mathematically valid candidate source of a unary theta function from \(H^2\), rather than inventing \(H^1\) winding cycles.

If \(D\) marked defects/punctures are removed from the shell, the topology changes: for \(D\geq1\), \(H_1(S^2\setminus\{p_1,\ldots,p_D\};\mathbb Z)\cong\mathbb Z^{D-1}\). Such cycles can support independent holonomy data subject to the global relation. A defect-based theta lattice is therefore possible only after the defect set, boundary/meridian conditions and action are specified. The physical seams alone are not punctures.

## 3.2. Discrete Villain gauge action on the 32-panel shell and the induced flux theta series

This subsection derives the quadratic weight of the Chern sectors from a concrete two-dimensional compact \(U(1)\) gauge action. It uses the cellular cochain complex of the *closed panel surface*, not the seam graph alone.

### 3.2.1. Cochain variables and the integer flux class

Let \(K\) be the oriented cellular decomposition with \(C^0(K;\mathbb Z)\cong\mathbb Z^{60}\), \(C^1(K;\mathbb Z)\cong\mathbb Z^{90}\), and \(C^2(K;\mathbb Z)\cong\mathbb Z^{32}\). Choose one orientation for every edge and face, and let
\[
d_0:C^0\to C^1,\qquad d_1:C^1\to C^2
\]
be the cellular coboundary matrices, so \(d_1d_0=0\).

A Villain \(U(1)\) field consists of a real link cochain \(a\in C^1(K;\mathbb R)\) and an integer plaquette cochain \(m\in C^2(K;\mathbb Z)\), with dimensionless integrated face curvature
\[
x=d_1a+2\pi m\in C^2(K;\mathbb R).
\]
Under a large gauge shift \(a\mapsto a+2\pi k\), \(k\in C^1(K;\mathbb Z)\), take \(m\mapsto m-d_1k\); then \(x\) is unchanged. The sign of this simultaneous shift is conventional. Since the oriented sum of all face boundaries vanishes on a closed surface,
\[
\sum_{f=1}^{32}(d_1a)_f=0,
\qquad
\frac{1}{2\pi}\sum_f x_f=\sum_f m_f=:n\in\mathbb Z.
\]
The integer \(n\) is invariant under \(m\mapsto m-d_1k\). On this oriented sphere, the quotient of integer 2-cochains by integer coboundaries is \(H^2(K;\mathbb Z)\cong\mathbb Z\), and the total sum gives its generator coordinate. Thus the Villain flux class is exactly the discrete first-Chern class. The Bianchi condition is automatic in dimension two at the level of 3-cochains because \(C^3(K)=0\); it must not be confused with a three-dimensional monopole constraint.

### 3.2.2. Gauge action and PRISM-compatible face constitutive weight

For each face \(f\), let \(\mathcal A_f>0\) be its physical area. The isotropic two-dimensional Maxwell/Villain action is
\[
S_g[x]=\frac{1}{2g^2}\sum_f\frac{x_f^2}{\mathcal A_f},
\qquad g^2>0.
\]
This is the piecewise-constant discretization of \((2g^2)^{-1}\int_S F\wedge *_gF\), since \(x_f=\int_fF\). It is dimensionless when \(g^2\) has units of inverse area in this two-dimensional normalization (or after choosing a reference area).

To include a positive tangent constitutive anisotropy without inventing the missing 216 PRISM matrices, let \(A_T(x)\) be a symmetric positive-semidefinite tangent endomorphism supplied by the finite-mesh transfer in T073, and define
\[
G_\epsilon(x)=I_{TS_x}+\epsilon A_T(x),\qquad
\epsilon>-\|A_T\|_{\mathrm{op}}^{-1}
\]
(with \(\epsilon\geq0\) a sufficient simple choice). Its induced area density is \(\sqrt{\det G_\epsilon}\). Define the effective face area
\[
\mathcal A_f^{(\epsilon)}
=\int_f\sqrt{\det G_\epsilon(x)}\,dA_g(x)>0.
\]
The corresponding metric-induced two-form action is
\[
S_g^{(\epsilon)}[x]
=\frac{1}{2g^2}\sum_f\frac{x_f^2}{\mathcal A_f^{(\epsilon)}}.
\]
This is the canonical \(F\wedge *_{G_\epsilon}F\) action for a two-form in two dimensions. **Important dimensional restriction:** a 2-form in two dimensions has only one local component. A tangent anisotropy therefore enters this pure gauge kinetic term only through the area density \(\sqrt{\det G_\epsilon}\); it does not create a directional splitting of the scalar face flux. Direction-dependent gauge response would require an additional constitutive tensor/operator on forms or a higher-dimensional extension, and must be separately derived.

The T073 PRISM map currently provides nodal \(A_T(x_i)=U_i\Gamma_TU_i^T\), not a validated smooth field over every face and not the full canonical 216-triplett table. Therefore \(\mathcal A_f^{(\epsilon)}\) is a well-defined continuum/discrete *target definition* when a positive face field is supplied, but its numerical evaluation on the actual shell remains conditional on a connection-compatible interpolation and audited PRISM inputs. No numerical areas or theta modulus are asserted here.

### 3.2.3. Exact minimization in a fixed Chern sector

Write \(A_f^\epsilon=\mathcal A_f^{(\epsilon)}\) and impose the topological constraint
\[
\sum_f x_f=2\pi n.
\]
The constrained minimum of the positive quadratic action is obtained by a Lagrange multiplier:
\[
\min_{\sum_fx_f=2\pi n}
\frac{1}{2g^2}\sum_f\frac{x_f^2}{A_f^\epsilon}.
\]
Stationarity gives \(x_f/A_f^\epsilon=\) constant, hence
\[
x_f^{\star}
=2\pi n\,\frac{A_f^\epsilon}{A_{\rm eff}},
\qquad
A_{\rm eff}:=\sum_fA_f^\epsilon,
\]
and
\[
\boxed{\;
S_{\min}(n)=\frac{2\pi^2}{g^2A_{\rm eff}}\,n^2.
\;}
\]
The same result follows from Cauchy–Schwarz:
\[
(2\pi n)^2
=\left(\sum_f\frac{x_f}{\sqrt{A_f^\epsilon}}\sqrt{A_f^\epsilon}\right)^2
\leq
\left(\sum_f\frac{x_f^2}{A_f^\epsilon}\right)
\left(\sum_fA_f^\epsilon\right).
\]
Equality holds exactly for \(x_f\propto A_f^\epsilon\). This is an exact finite-cell variational identity for the stated quadratic action.

### 3.2.4. The resulting topological theta factor

If the path integral sums over all line-bundle classes \(n\in\mathbb Z\), and if the fluctuation determinant within each class is independent of \(n\) (as for this abelian quadratic Maxwell action with the same linear fluctuation space), the topological part factors as
\[
Z_{\rm flux}(\vartheta_{\rm top})
\propto
\sum_{n\in\mathbb Z}
\exp\!\left[
-\frac{2\pi^2}{g^2A_{\rm eff}}n^2
+i n\vartheta_{\rm top}
\right].
\]
Thus
\[
Z_{\rm flux}\propto
\vartheta_3\!\left(
\frac{\vartheta_{\rm top}}{2\pi}\,\middle|\,
\frac{2\pi i}{g^2A_{\rm eff}}
\right),
\qquad
\operatorname{Im}\tau=\frac{2\pi}{g^2A_{\rm eff}}>0.
\]
This identifies the coefficient \(c=2\pi^2/A_{\rm eff}\) in the normalization of §3.1. The proportionality factor includes the common Gaussian fluctuation/gauge-volume factor and any measure normalization; it is not evaluated here. If determinants or matter couplings depend on \(n\), the simple theta factor is modified and factorization must be rechecked.

The theta modulus is therefore not a fitted parameter: in this specified two-dimensional Maxwell/Villain model it is fixed by \(g^2\) and the effective anisotropic area. The model still has to justify that this is the correct gauge action for the physical Q-ball.

### 3.2.5. Relation to barycentric quadrature

On each triangular subfacet \(T\subset f\), T068–T070 provide the barycentric measure and covariance. For a smooth positive density \(q(x)=\sqrt{\det G_\epsilon(x)}\),
\[
\int_Tq\,dA
=q(c_{T,a})+\frac12D^2q(c_{T,a}):\Sigma_{T,a}+R_T
\]
in the normalized reference-coordinate convention of T068–T070, with the geometric Jacobian included when mapping to the physical face. Summing over the triangulation of a pentagonal/hexagonal panel gives a controlled local approximation to \(A_f^\epsilon=\int_fq\,dA\), provided the map, Jacobian and derivative bounds satisfy the hypotheses of those quadrature results. This is the explicit point where the Gamma–Beta barycentric moments and the PRISM-induced anisotropic area enter the theta modulus.

The approximation error in \(A_{\rm eff}\) propagates to the modulus by
\[
\tau=i\,\frac{2\pi}{g^2A_{\rm eff}},
\qquad
\delta\tau=-i\,\frac{2\pi}{g^2A_{\rm eff}^2}\,\delta A_{\rm eff}
\]
to first order, for fixed \(g^2\). A quantitative global bound still requires summing the panelwise quadrature remainders and controlling the interpolation of \(A_T\).

**Status:** the cochain flux quantization, constrained minimizer and theta-series reduction are exact for the specified finite-cell quadratic model. The physical identification of the Maxwell/Villain action, the connection-compatible PRISM field, numerical \(A_f^\epsilon\), coupling \(g^2\), and refinement limit remain open.

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
