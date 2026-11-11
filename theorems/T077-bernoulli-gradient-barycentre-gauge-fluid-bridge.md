# T077 — Bernoulli–gradient–barycentre bridge between the right gauge and left fluid sectors

**Status:** exact local moment identities inherited from T068–T070; proposed coupled gauge/fluid anisotropy functional; global shell and physical validation OPEN.

## 1. Sector convention

This record fixes the user's sector convention and does not interchange it:

- **Right sector = gauge:** an internal bundle \(E_R\to S\), connection \(A\), section \(\Psi\), and covariant derivative \(D_A\Psi\).
- **Left sector = fluid:** density \(\rho\), velocity \(v\in TS\), pressure \(p\), gravitational potential \(\Phi\), and Bernoulli scalar
  \[
  B_L=p+\tfrac12\rho|v|_g^2+\rho\Phi.
  \]

The two sectors are not identified. Their common geometric interface is the same cell centroid/barycentre, covariance tensor, and tangent anisotropy. The football seams are not the starting point of this bridge; they are a later interface on which the already-defined sector fields may be matched.

## 2. Cell centroid, weighted barycentre and covariance

For a planar triangular cell \(F\), let \(v_0,v_1,v_2\) be its vertices and \(V\) the matrix with these rows. The uniform geometric centroid is
\[
c_F=\frac{v_0+v_1+v_2}{3},\qquad
\Sigma_F=\frac1{12}\sum_{i=0}^2(v_i-c_F)(v_i-c_F)^T.
\]
For Dirichlet weights \(a_i>0\), \(S_a=\sum_i a_i\),
\[
c_{F,a}=V^T\frac a{S_a},\qquad
C_{ij}=\frac{a_i(S_a\delta_{ij}-a_j)}{S_a^2(S_a+1)},\qquad
\Sigma_{F,a}=V^TCV.
\]
The centroid is the uniform special case \(a=(1,1,1)\). These are exact local results (T068, T070). The Q6 vertex covariance and its antipodal pair covariance (T069) are different measures and must not be substituted for \(\Sigma_F\).

Define the dimensionless cell anisotropy
\[
M_{F,a}=\frac{\Sigma_{F,a}}{\operatorname{tr}\Sigma_{F,a}},
\]
when the cell is nondegenerate. It is positive semidefinite, tangent to the cell plane, and has trace one. Its eigenvectors are the principal barycentric spread directions; unequal eigenvalues encode geometric anisotropy.

## 3. Left sector: Bernoulli gradient and anisotropic kinetic structure

For a steady, inviscid, barotropic fluid under the usual Bernoulli hypotheses, the classical scalar is
\[
B_L=p+\tfrac12\rho|v|_g^2+\rho\Phi.
\]
In the incompressible constant-density case, divide by \(\rho\) to obtain the usual head form. The Euler identity gives
\[
\nabla B_L=\rho\bigl(v\times\omega-\partial_t v\bigr)
\]
for constant density (with the stated sign convention for vorticity); in steady flow this reduces to \(\nabla B_L=\rho v\times\omega\). Along a streamline, \(v\cdot\nabla B_L=0\) in the steady ideal case.

The cell anisotropy acts on gradients through
\[
\mathcal Q_{L,F}=\bigl(\nabla_S B_L(c_{F,a})\bigr)^T
M_{F,a}\,\nabla_S B_L(c_{F,a}),
\]
or, when the velocity-gradient rather than the Bernoulli-gradient is the chosen observable,
\[
\mathcal G_{L,F}=\operatorname{tr}\!\left[(\nabla_Sv)^T
M_{F,a}(\nabla_Sv)\right].
\]
These are directional diagnostics, not replacements for the classical Bernoulli theorem. A proposed anisotropic constitutive extension may instead use
\[
B_{L,A}=p+\tfrac12\rho\,g_A(v,v)+\rho\Phi,
\qquad
g_A(v,v)=|v|_g^2+\epsilon\,g(A_Tv,v),
\]
where \(A_T\) is a symmetric tangent-bundle endomorphism and \(\epsilon\) is a calibrated dimensionless coupling. This last expression is a candidate model, not classical Bernoulli.

## 4. Right sector: gauge-covariant gradient

For the right gauge sector, the corresponding cell observable is the covariant-gradient energy
\[
\mathcal E_{R,F}
=\frac12\left\langle D_A\Psi(c_{F,a}),
\,K_R\,D_A\Psi(c_{F,a})\right\rangle,
\]
where \(K_R\) may contain the triplett-induced tangent anisotropy. Under a local gauge transformation \(h\), \(\Psi\mapsto h\Psi\), \(A\mapsto hAh^{-1}-(dh)h^{-1}\), and \(D_A\Psi\mapsto hD_A\Psi\); the scalar energy is gauge invariant when \(K_R\) transforms equivariantly.

The right gauge gradient is therefore not the ordinary spatial gradient of a scalar. It is a section of \(T^*S\otimes E_R\). Its contraction with a tangent anisotropy must preserve both the internal gauge action and the tangent-frame action.

## 5. The common barycentric–gradient bridge

For any \(C^3\) scalar cell density \(g\), T068/T070 give the exact second-order identity with controlled remainder:
\[
\int_F g\,d\mu_{F,a}
=g(c_{F,a})+\frac12D^2g(c_{F,a}):\Sigma_{F,a}+R_{F,a},
\qquad
|R_{F,a}|\leq\frac{h_F^3}{6}\sup_F\|D^3g\|_{op}.
\]
Apply this separately to a gauge density \(g_R=\mathcal E_R\) and a fluid density \(g_L=B_L\) (or a declared fluid energy density). The common anisotropy is the covariance tensor \(\Sigma_{F,a}\), while the two Hessians retain the distinct sector physics:
\[
\mathfrak B_{F,a}
=\underbrace{g_R(c_{F,a})+\tfrac12D^2g_R(c_{F,a}):\Sigma_{F,a}}_{\text{right / gauge}}
+\underbrace{g_L(c_{F,a})+\tfrac12D^2g_L(c_{F,a}):\Sigma_{F,a}}_{\text{left / fluid}}
+R_R+R_L.
\]
This is the precise local bridge: same barycentric geometry and anisotropic second moment, different covariant gradients and constitutive Hessians. The gradients enter through the derivatives of the sector densities; the covariance selects their principal spatial directions.

## 6. The Gamma–Beta–zeta–eta network and the two Bernoulli meanings

These functions form a connected analytic structure, but the distinct meanings of “beta” and “eta” must be labelled.

### 6.1 Euler Gamma and Euler Beta

The Euler beta integral is
\[
B(x,y)=\int_0^1t^{x-1}(1-t)^{y-1}\,dt
=\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}
\qquad(\Re x,\Re y>0).
\]
The Dirichlet barycentric partition function in T070 is precisely a multivariate beta factor:
\[
Z_F(a)=2A_F B_3(a),\qquad
B_3(a)=\frac{\prod_i\Gamma(a_i)}{\Gamma(S_a)}.
\]
Thus the barycentre and covariance are derivatives/moments of a Gamma-normalized partition function, not unrelated geometric formulae.

### 6.2 Logarithmic derivatives: digamma, polygamma and Hurwitz zeta

Differentiating \(\log B_3\) gives
\[
\partial_{a_i}\log B_3=\psi(a_i)-\psi(S_a)
=\mathbb E[\log\lambda_i],
\]
\[
\partial_{a_i}\partial_{a_j}\log B_3
=\delta_{ij}\psi_1(a_i)-\psi_1(S_a)
=\operatorname{Cov}(\log\lambda_i,\log\lambda_j).
\]
For integer \(m\geq1\),
\[
\psi^{(m)}(z)=(-1)^{m+1}m!\,\zeta(m+1,z),
\]
where \(\zeta(s,z)\) is the Hurwitz zeta function. At \(z=1\), this reduces to the Riemann zeta values. Consequently higher derivatives of the barycentric log-partition function are governed by Hurwitz-zeta values and their parameter combinations.

### 6.3 Riemann zeta, Dirichlet eta and Dirichlet beta

The Dirichlet eta function (alternating zeta series) is
\[
\eta_D(s)=\sum_{n\geq1}\frac{(-1)^{n-1}}{n^s}
=(1-2^{1-s})\zeta(s)
\]
in its initial convergence domain, with analytic continuation thereafter. It is not the Dedekind eta function.

The Dirichlet beta function is a different L-function,
\[
\beta_D(s)=\sum_{n\geq0}\frac{(-1)^n}{(2n+1)^s}
=L(s,\chi_{-4}).
\]
It must not be confused with Euler's beta integral \(B(x,y)\). More generally, Dirichlet L-functions encode character-weighted zeta sums; for example the quadratic field with character \(\chi_{-31}\) has \(\zeta_K(s)=\zeta(s)L(s,\chi_{-31})\).

### 6.4 Dedekind eta and modular structure

The Dedekind eta function is
\[
\eta_{\mathrm{Ded}}(\tau)
=q^{1/24}\prod_{n\geq1}(1-q^n),
\qquad q=e^{2\pi i\tau},\quad\Im\tau>0.
\]
It is a modular form of weight \(1/2\) with a multiplier system. Its logarithmic derivatives and modular transformations connect it to Eisenstein series, divisor sums and zeta values. It is not the alternating Dirichlet eta series. A bridge from the barycentric cell partition function to \(\eta_{\mathrm{Ded}}\) requires a specified spectral determinant, lattice/modular parameter or product expansion; it is not obtained merely by renaming the Dirichlet parameter.

### 6.5 Bernoulli numbers and the Bernoulli fluid law

Bernoulli numbers enter the even zeta values,
\[
\zeta(2n)=(-1)^{n+1}
\frac{B_{2n}(2\pi)^{2n}}{2(2n)!},
\]
and the asymptotic expansion
\[
\psi(z)\sim\log z-\frac1{2z}
-\sum_{k\geq1}\frac{B_{2k}}{2kz^{2k}}.
\]
They also occur in Euler–Maclaurin summation when its hypotheses hold. This analytic Bernoulli structure is distinct from **Bernoulli's fluid law** \(B_L=p+\frac12\rho|v|^2+\rho\Phi\). The two may coexist in the same programme, but no identity equates their Bernoulli symbols or coefficients.

The precise programme-level chain is therefore
\[
\boxed{
\text{Gamma}
\xrightarrow{\log\,\partial}
\text{digamma/polygamma}
\xrightarrow{}
\text{Hurwitz/Riemann zeta}
\xleftrightarrow{\text{alternating factor}}
\text{Dirichlet eta};
\quad
\text{Gamma ratios}\leftrightarrow\text{Euler Beta};
\quad
\text{Dedekind eta}\leftrightarrow\text{modular/spectral data}.
}
\]
The common geometric use is through the Dirichlet barycentric measure and its moments; the modular/spectral branch is a further structure requiring its own map.

## 7. Anisotropy induced by the Q6/PRISM triplet

When the reconstructed Q6 \(T_{2u}\) basis \(V\in\mathbb R^{188\times3}\) and a canonical PRISM triplett \(R_T\in\mathbb R^{2\times3}\) are both available, set
\[
\Gamma_T=R_T^TQ_{G_2}R_T,\quad
U_i=L_iV,\quad
A_T(x_i)=U_i\Gamma_TU_i^T.
\]
The cell-level anisotropy may then be composed with the geometric covariance, for example by restricting \(A_T\) to the cell tangent plane and using the dimensionless tensor \(M_{F,a}\) as the spatial averaging weight. This is a candidate coupling; the exact map from the 216 labelled PRISM tripletti and their 20 Gram classes to the left/right sector fields is not yet established. No physical channel alignment is inferred from the gauge-covariance identity alone.

## 8. Evidence and open tasks

**PROVED:** T068 uniform triangle covariance and Taylor quadrature; T070 Dirichlet weighted barycentre/covariance and Taylor remainder; the displayed algebraic contractions once the fields and tensors are given.

**STANDARD FLUID IDENTITY:** Bernoulli/Euler relation under its classical hypotheses. It does not apply to arbitrary unsteady, viscous, compressible flow without the corresponding additional terms and assumptions.

**CANDIDATE:** coupled right-gauge/left-fluid cell functional; anisotropic kinetic metric \(g_A\); composition of PRISM tangent anisotropy with barycentric covariance.

**OPEN:** recover the canonical 216 PRISM matrices and 20 class labels; specify the physical map assigning the right and left fields to the same shell cells; derive the coupled equations/variation; establish regularity and global error accumulation over the 180 triangular facets; define a coherent refinement family and prove convergence; calibrate \(\epsilon\) and fluid material parameters against data. The 90 seams enter only after this cellwise bridge is fixed.

## 9. Linked records

- T068 — uniform triangular centroid and covariance quadrature.
- T069 — Q6 antipodality, Walsh sectors and vertex covariance (distinct from cell covariance).
- T070 — Dirichlet weighted barycentres, covariance, Gamma/Beta and phase moments.
- T073/T076 — football shell, Q6/PRISM tangent anisotropy and seam mechanics.
