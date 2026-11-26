# T082 — First variation of the Morandotti second-order density and barycentric anisotropy

**Date:** 10 November 2026  
**Status:** exact variational representation under the hypotheses of the cited second-order structured-deformation theorem; differentiability and the curved Q-ball transfer are conditional/open.  
**Dependencies:** T068, T070, T077, T079, T081.

## 1. Purpose and notation

This record sharpens T081. It identifies the correct variational meaning of the second-order field and derives its coupling to the Dirichlet barycentric measure without postulating a quadratic constitutive law.

Write the second-order field as \(\Gamma_{\mathrm{Mor}}\) to distinguish it from Euler's scalar Gamma function \(\Gamma_E\). In the Euclidean theory of Barroso–Matias–Morandotti–Owen, the bulk relaxed density is a value function
\[
W_2(x_0,A,B,D)
=\inf\left\{
\int_Q W(x_0,A,\nabla u(y))\,dy+
\int_{S_u\cap Q}\Psi(x_0,[u],\nu_u)\,d\mathcal H^{N-1}:
\begin{array}{l}
u|_{\partial Q}=B\,y,\\[1mm]
\displaystyle\int_Q\nabla u(y)\,dy=D
\end{array}
\right\}.
\]
Here \(D\) is the second-order datum (the tensor represented by \(\Gamma_{\mathrm{Mor}}\)); the admissible maps are \(SBV\)-valued matrix fields with the boundary and mean-gradient constraints displayed above. This is the cell formula, not an assumed quadratic function of \(D\).

The relaxed functional also has a separate interfacial term
\[
\int_{\Omega\cap S_G}\gamma_2(x,[G],\nu_G)\,d\mathcal H^{N-1}.
\]
The surface density in this representation depends on the jump of \(G\) and the normal; it must not be silently identified with a football-panel seam law.

## 2. First variation with respect to the second-order field

Fix \(x_0,A,B\), and abbreviate the cell admissible class with prescribed mean gradient \(D\) by \(\mathcal A_D\). Define
\[
\mathcal F(u)=\int_Q W(x_0,A,\nabla u)\,dy+
\int_{S_u\cap Q}\Psi(x_0,[u],\nu_u)\,d\mathcal H^{N-1},
\qquad
W_2(D)=\inf_{u\in\mathcal A_D}\mathcal F(u).
\]

The exact statement is that \(W_2\) is a constrained minimum/value function. No differentiability in \(D\) follows merely from the integral representation.

If \(W_2\) is differentiable at \(D\), then for a perturbation \(H\)
\[
W_2(D+\varepsilon H)
=W_2(D)+\varepsilon\,\partial_DW_2(D):H+o(\varepsilon).
\]
If it is only convex/locally Lipschitz in the relevant regime, use its convex/Clarke subdifferential as appropriate; existence and the correct subdifferential notion must be established from the constitutive assumptions, not presumed.

### Multiplier interpretation (conditional)

Use the Lagrangian convention
\[
\mathscr L(u,\Lambda;D)
=\mathcal F(u)+\Lambda:\left(\int_Q\nabla u\,dy-D\right).
\]
Whenever a suitable constrained minimizer, multiplier and envelope theorem exist, the multiplier relation is
\[
\partial_D W_2(D)=-\Lambda.
\]
The minus sign is fixed by this displayed convention. Reversing the sign of the constraint in the Lagrangian reverses the multiplier sign. Thus the energetic conjugate to \(\Gamma_{\mathrm{Mor}}\) is the multiplier enforcing the microscopic mean-gradient constraint. This is not an independent postulated stress law.

## 3. Dirichlet barycentric averaging

Let \(F\) be a triangle with vertices \(x_1,x_2,x_3\), barycentric coordinates \(\lambda\in\Delta_2\), positive parameters \(a_i\), and \(S=a_1+a_2+a_3\). Let \(X(\lambda)=\sum_i\lambda_i x_i\). For a cellwise second-order field \(D(\lambda)=\Gamma_{\mathrm{Mor}}(X(\lambda))\), define
\[
\mathcal E_F(a)=
\mathbb E_{\operatorname{Dir}(a)}
\left[
W_2\bigl(X(\lambda),A(\lambda),B(\lambda),D(\lambda)\bigr)
\right],
\]
whenever the integrand is measurable and integrable. The normalized density is
\[
p_a(\lambda)=\frac{\Gamma_E(S)}{\prod_i\Gamma_E(a_i)}
\prod_i\lambda_i^{a_i-1}.
\]

Assume first that \(W_2\) is differentiable in \(D\) along the field under consideration and that differentiation may be passed through the integral. For a perturbation \(H(\lambda)\),
\[
\delta_D\mathcal E_F(a)[H]
=\mathbb E_a\left[
\partial_DW_2(X,A,B,D):H
\right].
\]
If differentiability fails, replace \(\partial_DW_2\) by an admissible measurable selection of the relevant subgradient only after the required measurable-selection and integral-subdifferential hypotheses have been proved.

Combining with the multiplier formula gives, conditionally,
\[
\delta_D\mathcal E_F(a)[H]
=-\mathbb E_a[\Lambda(\lambda):H(\lambda)].
\]
This is the sought field-side variational response averaged with the barycentric measure.

## 4. Parameter variation and the mixed derivative

For a parameter direction \(h=(h_1,h_2,h_3)\), differentiating the normalized Dirichlet density gives its score
\[
s_h(\lambda)
=\Big(\sum_i h_i\Big)\psi_{\mathrm{dig}}(S)
-\sum_i h_i\psi_{\mathrm{dig}}(a_i)
+\sum_i h_i\log\lambda_i,
\qquad \psi_{\mathrm{dig}}=\Gamma_E'/\Gamma_E.
\]
For any integrable \(f\) with the required domination,
\[
D_a\mathbb E_a[f][h]=\mathbb E_a[f\,s_h].
\]
In particular,
\[
D_a\mathcal E_F(a)[h]
=\mathbb E_a[\mathcal W(\lambda)s_h(\lambda)],
\quad
\mathcal W(\lambda)=W_2(X,A,B,D).
\]

If the field derivative exists and the mixed differentiations commute under a joint domination hypothesis, then
\[
D_a\bigl(\delta_D\mathcal E_F(a)[H]\bigr)[h]
=\mathbb E_a\left[
\bigl(\partial_DW_2:H\bigr)s_h
+\partial_DW_2:D_aH[h]
+D_a(\partial_DW_2)[h]:H
\right].
\]
For a fixed perturbation field \(H\) and no explicit \(a\)-dependence in \(X,A,B,D,H\) except through the sampling law, this reduces to
\[
D_a\bigl(\delta_D\mathcal E_F(a)[H]\bigr)[h]
=\mathbb E_a\left[
(\partial_DW_2:H)s_h
\right]
\]
provided the spatial/field arguments are held fixed as functions of \(\lambda\). If those arguments themselves depend on \(a\), their chain-rule terms must be retained.

This mixed response is the precise mathematical object linking:
- the Morandotti second-order field response \(\partial_DW_2\);
- the barycentric anisotropy encoded by \(a\) and \(\operatorname{Cov}_a(\lambda)\);
- the special-function score involving the digamma function \(\psi_{\mathrm{dig}}\).

The anisotropy is not simply the Dirichlet score: its geometric directional effect is carried by the map \(X(\lambda)\), the tangent metric/covariance, and the dependence of \(A,B,D\) on position.

## 5. Tangent anisotropy and the Q-ball shell

On a panel chart, let \(P_T\) denote the tangent projection and let \(M_{F,a}\) be a specified positive tangent metric or covariance-derived tensor. A directional diagnostic can be formed from the conjugate field
\[
\mathcal Q_{\Gamma,F}
=\mathbb E_a\!\left[
(P_T\partial_DW_2)^T M_{F,a}(P_T\partial_DW_2)
\right],
\]
with tensor contractions adjusted to the actual tensor type of \(D\). This is a diagnostic/candidate functional, not a theorem that the physical shell energy has this form.

At panel transitions, \(D\), \(H\), and the conjugate multiplier must be transported by the appropriate bundle/frame transition before comparing traces. Raw componentwise subtraction across differently oriented panel frames is not invariant.

For the 90 physical seams, distinguish:
1. the bulk cell relaxation defining \(W_2\);
2. the continuum jump term on \(S_G\);
3. any independently calibrated panel-seam constitutive energy.

The three can be coupled only after specifying trace spaces, transition maps and a common variational domain. A seam is not automatically a jump set.

## 6. Relation to Euler Gamma, Beta, eta and zeta

The Euler Gamma function enters only through the Dirichlet normalization:
\[
p_a(\lambda)=
\frac{\Gamma_E(S)}{\prod_i\Gamma_E(a_i)}
\prod_i\lambda_i^{a_i-1}.
\]
Its logarithmic derivative creates the digamma score \(\psi_{\mathrm{dig}}\) \(\psi_{\mathrm{dig}}\); higher parameter derivatives produce polygamma functions. For \(m\geq1\),
\[
\psi_{\mathrm{dig}}^{(m)}(z)=(-1)^{m+1}m!\,\zeta(m+1,z),
\]
where the zeta function is the Hurwitz zeta. Beta functions appear in lower-dimensional edge/simplex integrations and through Gamma ratios.

Neither Dirichlet eta nor Dedekind eta follows from this local first variation. A Dedekind eta factor requires modular/lattice structure; a Dirichlet eta factor requires an alternating Dirichlet series. A spectral zeta determinant requires a separately specified elliptic operator, domain, seam conditions and zero-mode prescription.

## 7. What is proved, conditional, and open

**Exact under the cited Euclidean relaxed-density hypotheses**
- The bulk density is the constrained \(SBV\) cell value function displayed in Section 1.
- The second-order datum is imposed as the mean microscopic gradient.
- The Dirichlet score identity follows by differentiating the normalized density, under integrability/differentiation hypotheses.

**Conditional variational result**
- \(\partial_DW_2=-\Lambda\) requires a suitable minimizer, multiplier and envelope theorem.
- The integrated field variation and mixed parameter/field derivative require differentiability, measurable selection where needed, and domination sufficient to exchange derivatives and integrals.

**Open for the Q-ball/RGS–PRISM transfer**
- Identify the exact tensor bundle and transformation law of \(D=\Gamma_{\mathrm{Mor}}\) on the curved shell.
- Establish existence/regularity and differentiability or a usable subdifferential theory for the relevant cell value function.
- Specify the constitutive bulk density \(W\), interfacial density \(\Psi\), and independent panel-seam law.
- Prove frame-compatible assembly, compactness, liminf and recovery for the curved, seam-bearing refinement.
- Only after these steps derive a physical anisotropic constitutive law or spectral determinant.

## 8. References

1. A. C. Barroso, J. Matias, M. Morandotti and D. R. Owen, “Second-Order Structured Deformations: Relaxation, Integral Representation and Applications,” *Archive for Rational Mechanics and Analysis* 225 (2017), 1025–1072, DOI: [10.1007/s00205-017-1120-5](https://doi.org/10.1007/s00205-017-1120-5), arXiv: [1607.02311](https://arxiv.org/abs/1607.02311). The cell formula and integral representation are in the cited paper; this record's multiplier/envelope statements are conditional deductions, not quoted theorems from that paper.
2. T068, T070, T077, T079 and T081 in this repository.

**Editorial rule:** do not replace the cell formula by a quadratic ansatz, and do not identify the tensor field \(\Gamma_{\mathrm{Mor}}\) with Euler's scalar function \(\Gamma_E\).
