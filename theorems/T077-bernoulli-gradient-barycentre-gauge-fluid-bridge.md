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

## 6. Bernoulli numbers versus Bernoulli's fluid law

Two notions must remain distinct:
1. **Bernoulli fluid law:** the pressure–kinetic–potential balance in Section 3.
2. **Bernoulli numbers:** coefficients in special-function asymptotics (for example digamma/polygamma) and in applicable Euler–Maclaurin summation formulas.

T070 establishes the Gamma/Beta and digamma identities for Dirichlet barycentric moments. Bernoulli numbers can occur in the asymptotics of those special functions, but they are not automatically coefficients of the fluid Bernoulli scalar or of a football refinement expansion. To obtain mesh-asymptotic Bernoulli coefficients one must specify a refinement family, summation rule, and prove the relevant Euler–Maclaurin hypotheses.

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
