# T079 — Morandotti structured gradients, surface incompatibility and barycentric RGS–PRISM bridge

**Status:** the structured-deformation split and its Euclidean relaxation results are established in the cited literature; the cellwise barycentric identities are established in T068–T070; the surface-shell transfer below is a precisely formulated candidate and is NOT claimed as a proved surface homogenization theorem.

## 1. The point of contact: gradients, not theta or total area

The relevant Morandotti framework is structured deformations. For a macroscopic deformation \(g\) and a microscopic/without-disarrangements gradient \(G\), it separates
\[
\nabla g=G+\mathsf D,\qquad \mathsf D:=\nabla g-G.
\]
The tensor \(\mathsf D\) records the part of the macroscopic gradient not represented by the limiting microscopic gradient. It is not automatically a crack, a seam, or a defect: its interpretation is energetic and depends on the approximation and relaxation framework. In the first-order theory, \(\mathsf D\) and its curl encode disarrangement and dislocation information.

For the Q-ball/RGS shell the natural geometric analogue is a surface deformation
\[
y:S\longrightarrow\mathbb R^3,\qquad
\nabla_S y=G+\mathsf D,
\]
where \(G\) is the limiting microscopic tangential distortion and \(\mathsf D\) is the structured-gradient mismatch. Here \(\nabla_S y\) is a \(3\times2\) tangential derivative. This is the central bridge to investigate. It is distinct from the previously developed theta/area calculation.

## 2. Surface incompatibility and Burgers circulation

Let \(S\) be an oriented smooth surface and suppose first that each row of \(\mathsf D\) is a smooth tangential one-form \(d^\alpha\), \(\alpha=1,2,3\). Define the row-wise surface incompatibility by
\[
\operatorname{Curl}_S\mathsf D
:=
\bigl(d_Sd^1,d_Sd^2,d_Sd^3\bigr),
\]
a triple of surface 2-forms. For any oriented surface patch \(U\subset S\) with positively oriented boundary \(C=\partial U\), Stokes' theorem gives
\[
\boxed{
\oint_C\mathsf D\,t\,ds
=\int_U\operatorname{Curl}_S\mathsf D.
}
\]
This is the surface version of the circulation/Burgers relation. It is a local differential identity, not yet a statement that the football seams carry nonzero dislocation.

For piecewise-smooth fields separated by seam curves \(\Gamma\), the distributional derivative has both bulk and interface contributions. In local oriented coordinates, if \(d^\alpha\) has traces \(d^\alpha_\pm\), its distributional exterior derivative contains the measure
\[
[d^\alpha]\wedge n^\flat\,\mathcal H^1\!\llcorner\Gamma
\]
(up to the fixed choice of normal/orientation convention), in addition to the piecewise classical \(d d^\alpha\). Thus a seam contributes only when the relevant trace mismatch is nonzero. A geometrical seam with matching traces is not, by itself, a dislocation.

## 3. What the Morandotti results actually supply

The first-order structured-deformation literature identifies \(\mathsf D=\nabla g-G\) as the disarrangement part and relates \(\mathsf D\) and its curl to Burgers vectors and dislocation density. The second-order theory introduces a further field \(\Gamma\) to capture submacroscopic bending/curving; its higher-order split includes
\[
\nabla^2g=\nabla\mathsf D+(\nabla G-\Gamma)+\Gamma.
\]
The term \(\nabla G-\Gamma\) describes gradient disarrangements at the next scale. This is relevant to a sewn shell because panel bending and seam-scale changes cannot in general be represented by a first-order displacement jump alone.

The cited relaxation and integral-representation theorems are formulated in Euclidean domains under their own SBV/SBV\(^2\), coercivity, growth and boundary hypotheses. They do **not** already prove the corresponding theorem on a closed curved football shell with 90 physical seams. The shell result requires a surface adaptation, charts/transition maps, interface bookkeeping and a refinement theorem.

## 4. Exact finite-cell gradient bridge

Let \(F\) be a nondegenerate triangular facet with vertices \(x_i\), and let \(y_h\) be affine on \(F\). Its tangential gradient \(\nabla_F y_h\) is constant on that facet. Given a constant or cellwise projected microscopic gradient \(G_F\), define
\[
\mathsf D_F:=\nabla_Fy_h-G_F.
\]
For a quadratic structured-gradient density
\[
W_F(\mathsf D_F)=\tfrac12
\langle\mathsf D_F,\mathbb C_F\mathsf D_F\rangle,
\qquad \mathbb C_F\succeq0,
\]
the cell energy is exactly
\[
E_F^{\rm str}=|F|\,W_F(\mathsf D_F).
\]
If \(G_F\) varies within the cell, the exact cell energy is instead
\[
E_F^{\rm str}=\frac12\int_F
\langle\nabla_Fy_h-G(x),\mathbb C(x)(\nabla_Fy_h-G(x))\rangle\,dA;
\]
the constant-cell expression is then a quadrature/model reduction, not an identity.

The same facet carries the exact barycentric covariance
\[
\Sigma_{F,a}=X^T
\frac{\operatorname{diag}(a)S-aa^T}{S^2(S+1)}X
\]
for Dirichlet weights \(a_i>0\), \(S=\sum_i a_i\), with \(X\) the vertex-coordinate matrix. For a \(C^3\) scalar cell density \(q\),
\[
\int_Fq\,d\mu_{F,a}
=q(c_{F,a})+\tfrac12D^2q(c_{F,a}):\Sigma_{F,a}+R_F,
\]
with the T068/T070 remainder bound. Apply this to \(q=W(\mathsf D(\cdot))\), not to \(\mathsf D\) itself unless the required regularity is available. This gives a controlled bridge from Morandotti-type gradient mismatch to centroid/covariance quadrature.

**Notation warning:** \(\mathsf D\) is the structured-gradient mismatch. \(\Sigma_{F,a}\) is a covariance tensor. They are different objects and must never share the same symbol in subsequent records.

## 5. The two RGS sectors remain distinct

The Morandotti mismatch is a mechanical deformation-gradient object. It must not be identified with either a Bernoulli gradient or a gauge-covariant derivative.

- **Left / fluid:** the observable is \(\nabla_SB_L\), or \(\nabla_Sv\), with the classical Bernoulli/Euler hypotheses stated separately. A cell diagnostic is
  \[
  Q_{L,F}=(\nabla_SB_L)^T\widehat\Sigma_{F,a}\nabla_SB_L,
  \quad
  \widehat\Sigma_{F,a}=\Sigma_{F,a}/\operatorname{tr}\Sigma_{F,a}.
  \]
- **Right / gauge:** the observable is \(D_A\Psi\in T^*S\otimes E_R\), and a gauge-invariant anisotropic contraction has the form
  \[
  Q_{R,F}=\langle D_A\Psi,
  (\widehat\Sigma_{F,a}\otimes K_R)D_A\Psi\rangle,
  \]
  with \(K_R\) positive and equivariant under the internal gauge action.
- **Structured shell mechanics:** \(\mathsf D=\nabla_Sy-G\) is the mismatch field. Its energy and incompatibility are additional observables, not a replacement for the left/right fields.

The common object is the cell's tangent geometry and its covariance-weighted sampling. The physical coupling among these three fields must come from a specified constitutive energy or variational principle; it cannot be inferred merely because all contain gradients.

## 6. A candidate three-channel cell functional

A useful test functional, explicitly labelled as a model ansatz, is
\[
\begin{aligned}
E_F={}&\frac{|F|}{2}
\langle\mathsf D_F,\mathbb C_F\mathsf D_F\rangle\\
&+\frac{|F|}{2}\,\beta_L
(\nabla_SB_L)^T\widehat\Sigma_{F,a}\nabla_SB_L\\
&+\frac{|F|}{2}\,\beta_R
\langle D_A\Psi,
(\widehat\Sigma_{F,a}\otimes K_R)D_A\Psi\rangle
+E_{\Gamma,F}.
\end{aligned}
\]
Here \(\beta_L,\beta_R\geq0\) are calibration parameters and \(E_{\Gamma,F}\) is reserved for second-order structured-gradient/bending effects (for example a term depending on \(\nabla G-\Gamma\)). This functional is not claimed to be Morandotti's relaxed energy, nor a derived Q-ball law. Its purpose is to expose exactly which gradients and constitutive coefficients need to be identified.

A more faithful Morandotti programme should first identify the bulk and interface densities separately and only then perform relaxation. The 90 seams should enter through trace/jump variables and an interface density, not by inserting an arbitrary seam penalty into the bulk tensor.

## 7. Discrete-to-continuum obligations for the football shell

A valid shell theorem would need, at minimum:

1. A sequence of shape-regular surface triangulations \(\mathcal T_h\) of the same closed surface, with compatible panel charts and seam traces.
2. Discrete macroscopic deformations \(y_h\), microscopic gradients \(G_h\), and mismatches \(\mathsf D_h=\nabla_{\mathcal T_h}y_h-G_h\).
3. A discrete row-wise surface curl/edge-circulation operator satisfying a Stokes commuting identity.
4. Bulk and seam energy densities with coercivity, growth and frame/gauge invariance assumptions.
5. Equicoercivity and a liminf inequality, followed by a recovery sequence, for the proposed surface structured-deformation energy.
6. If second-order effects are retained, a compatible discrete field for \(\Gamma_h\) and control of \(\nabla G_h-\Gamma_h\).
7. Separate convergence/consistency estimates for the fluid Bernoulli gradient and the gauge covariant gradient.

The existing 60-vertex/90-seam/32-panel shell generator is one finite geometry. It does not by itself provide a refinement family or establish \(\Gamma\)- or Mosco-convergence.

## 8. Research alignment and references

- Barroso, Matias, Morandotti & Owen, “Explicit Formulas for Relaxed Disarrangement Densities Arising from Structured Deformations,” *Math. Mech. Complex Syst.* 5 (2017), 163–189, DOI: 10.2140/memocs.2017.5.163; arXiv:1508.06908.
- Barroso, Matias, Morandotti & Owen, “Second-Order Structured Deformations: Relaxation, Integral Representation and Applications,” *Arch. Rational Mech. Anal.* 225 (2017), 1025–1072, DOI: 10.1007/s00205-017-1120-5; arXiv:1607.02311.
- Barroso, Matias, Morandotti, Owen & Zappale, “The Variational Modeling of Hierarchical Structured Deformations,” *J. Elasticity* 155 (2024), 371–392, DOI: 10.1007/s10659-022-09961-w; arXiv:2208.11785.
- T068–T070: local triangle centroid, covariance, Dirichlet barycentre and Taylor quadrature.
- T077: left Bernoulli-gradient and right gauge-covariant-gradient cell observables.

## 9. Status

| Claim | Status |
|---|---|
| \(\nabla g=G+\mathsf D\) structured-gradient split | Established framework |
| \(\mathsf D\) and curl/Burgers interpretation | Established in cited Euclidean structured-deformation setting |
| Second-order field \(\Gamma\) and gradient-disarrangement term \(\nabla G-\Gamma\) | Established in cited second-order setting |
| Surface Stokes identity for smooth row-wise \(\mathsf D\) | Exact differential identity |
| Finite-facet affine gradient and constant-cell energy | Exact finite-element identity |
| Barycentric covariance/Taylor quadrature | T068–T070 established |
| Curved football-shell relaxation/homogenization | OPEN |
| Coupling Morandotti mismatch to fluid/gauge channels | Candidate variational model; OPEN |
| Physical Q-ball interpretation and calibration | OPEN |
