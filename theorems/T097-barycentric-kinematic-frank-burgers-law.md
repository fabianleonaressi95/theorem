# T097 — Barycentric–kinematic reconstruction law for Frank–Burgers defect closure

**Date:** 11 November 2026  
**Status:** exact component identities under the hypotheses below; integrated reconstruction law is a conditional discrete/continuum bridge. Numerical calibration against the two-core Morandotti fields remains to be completed.  
**Dependencies:** T068–T070 (barycentric moments and quadrature), T079 (structured-gradient split), T080 (discrete Stokes complex), T082 (Morandotti second-order variation and anisotropy), T091 (Frank–Burgers tensor composition and sensitivity), T092 (two-circle/SE(2) closure), T093–T095 (Cartan transport and two-core adapter).

## 1. Statement and purpose

The rotation and translation parts of a defect closure are not to be introduced as two unrelated fitted parameters. In the planar Morandotti setting they have different kinematic sources:

- the rotational frame is reconstructed from the already specified deformation-gradient field;
- the translational closure is the circulation of the structured-gradient mismatch;
- barycentric centroids and covariance tensors control the cell sampling of these fields and their anisotropic corrections.

This record packages these ingredients into one reconstruction law. It does not identify a centroid displacement by itself with a Burgers vector, nor does it claim that a barycentric quadrature value is an exact integral for a non-polynomial field.

## 2. Kinematic input and rotation from the gradient

Let (U\subset\mathbb R^2) be a planar region away from defect cores and cuts. Let (g:U\to\mathbb R^2) be the macroscopic deformation and (G:U\to\mathbb R^{2\times2}) the microscopic gradient in the structured-deformation split
\[
\nabla g=G+\mathsf D.
\]
On any region where (\det G>0), define the polar rotation (R_G\in SO(2)) by the right polar decomposition
\[
G=R_G U_G,\qquad U_G=(G^TG)^{1/2}.
\]
Writing
\[
R_G=\begin{pmatrix}\cos\theta_G&-\sin\theta_G\\
\sin\theta_G&\cos\theta_G\end{pmatrix},
\]
the angle is locally determined, modulo (2\pi), by
\[
\boxed{\theta_G=\operatorname{atan2}(G_{21}-G_{12},G_{11}+G_{22}).}
\]
This formula is valid for orientation-preserving nonsingular (G); the branch of the angle must be tracked continuously on each chart. It is the polar rotation of the specified gradient, not an independent microrotation field.

The associated planar connection one-form is
\[
\omega_G=R_G^T dR_G=J\,d\theta_G,
\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
For a loop avoiding cores and cuts, the Frank winding is
\[
\boxed{\Omega_\gamma=\oint_\gamma d\theta_G=2\pi\,\operatorname{wind}(R_G\circ\gamma,SO(2)),}
\]
when the frame map is continuous along the loop. If the frame is represented in multiple charts, include the transition angles at chart crossings. A smooth single-valued frame on a disk has zero winding; nonzero Frank content requires a singularity, a nontrivial frame transition, or a cut/jump contribution. This condition prevents manufacturing disclination charge from a smooth, globally single-valued gradient.

**Important:** the formula reconstructs the rotation from the gradient field. It does not claim that the polar factor of an arbitrary Airy stress tensor is meaningful; the input is the kinematic gradient (G) (or the precise gradient field fixed by the verified kinematic law).

## 3. Translation from structured-gradient incompatibility

With the T079 convention (\mathsf D=\nabla g-G), regard each row of (\mathsf D) as a one-form. For a positively oriented Lipschitz loop (\gamma=\partial V\) on which the traces are defined,
\[
\boxed{b_\gamma=\oint_\gamma\mathsf D\,t\,ds
=\int_V\operatorname{Curl}\mathsf D.}
\tag{97.1}
\]
The equality is row-wise Stokes. For piecewise-smooth fields, the distributional curl includes the interface/jump measure; it must not be replaced by the bulk curl alone. The seam/cut traces are compared in a common frame, as required in T079–T080.

On the finite shell complex of T080, with edge cochain \(\mathsf D_h=\delta_0 y-G_h\), the exact discrete version is
\[
\boxed{b_h(q)= (B_2q)^T\mathsf D_h
=q^T B_2^T\mathsf D_h=-q^TB_2^TG_h.}
\tag{97.2}
\]
This identity is exact because \(B_1B_2=0\). It is the discrete translational closure; it is not inferred from centroid positions alone.

## 4. Barycentric reconstruction and anisotropic correction

For a triangular cell (F=\operatorname{conv}(x_1,x_2,x_3)), choose positive Dirichlet parameters (a_i), let (S=\sum_i a_i), and define
\[
c_{F,a}=\sum_i\frac{a_i}{S}x_i,\qquad
\Sigma_{F,a}=V^T\frac{\operatorname{diag}(a)S-aa^T}{S^2(S+1)}V.
\]
These are the exact weighted barycentre and covariance of T070. For (a=(1,1,1)), they reduce to the areal centroid and covariance of T068.

Let (q_F(x)) be any (C^3) scalar density formed from the kinematic fields, for example a declared rotational density, a component of the incompatibility density after regularisation, or the Morandotti energy density. Then
\[
\boxed{
\mathbb E_{F,a}[q_F]
=q_F(c_{F,a})+\frac12D^2q_F(c_{F,a}):\Sigma_{F,a}+R_{F,a},
\quad
|R_{F,a}|\le\frac{h_F^3}{6}\sup_F\|D^3q_F\|_{op}.
}
\tag{97.3}
\]
Thus the centroid gives the first spatial sample, while the full covariance—not just its trace—gives the leading anisotropic correction. For a quadratic density the formula is exact. For singular core densities, apply it only to cells separated from the core or to a declared regularised density; singular core-loop data are handled by (97.1)–(97.2), not by pretending the density is (C^3) at the core.

For a vector/tensor source (Q), apply (97.3) componentwise. If the source is a measure with an interface part, integrate its bulk and interface contributions separately.

## 5. The combined Frank–Burgers/SE(2) reconstruction law

For each oriented cell/edge transport segment, let (\Delta\theta_e\) be the increment of the gradient-derived polar frame, including chart-transition increments, and let (b_e\) be the corresponding structured-mismatch edge integral in a common transported frame. Define
\[
g_e=\left(R(\Delta\theta_e),b_e\right)\in SE(2).
\]
For an ordered closed path (\gamma=(e_1,\ldots,e_m)\), use the semidirect product in T092:
\[
\boxed{
H_\gamma=g_{e_m}\cdots g_{e_1}
=\left(R(\Omega_\gamma),b_\gamma^{SE(2)}\right),
\qquad
(R_2,b_2)(R_1,b_1)=(R_2R_1,b_2+R_2b_1).
}
\tag{97.4}
\]
The rotational closure is obtained from the gradient-derived frame increments; the translational closure is obtained from the structured-gradient mismatch and must be transported into the common base frame before composition. The barycentric formula (97.3) supplies controlled cellwise sampling/correction for smooth densities entering these increments and for the energy/anisotropy audit. It does not replace path ordering or the semidirect-product transport.

**Law 97 (barycentric–kinematic Frank–Burgers law).** Under: (i) an orientation-preserving kinematic gradient (G) with a consistently tracked polar frame on each cell; (ii) a structured mismatch (\mathsf D=\nabla g-G) with well-defined bulk and interface traces; (iii) a compatible oriented cell complex and common-frame edge transport; and (iv) (C^3) regularity for each density to which (97.3) is applied, the defect closure is reconstructed by (97.1) or (97.2), its rotational component by the winding/transition sum of the polar frame, and its cellwise anisotropic response by (97.3). The resulting (SE(2)) closure is (97.4).

The law is a composition of exact kinematic, Stokes, group-product and moment identities. It is not a new constitutive equation for stress, nor a claim that all its inputs have already been extracted from the current Morandotti Airy-only export.

## 6. Connection to the Morandotti anisotropy results

Once the reconstructed Frank/Burgers sectors are available, T091 supplies the exact tensor decomposition
\[
T=T_F+T_B+T_{FB},
\]
including the signed mixed term. Its parameter-sensitivity identity
\[
x'(p)=M(p)^{-1}(\Phi'(p)-M'(p)x(p))
\]
and the corresponding residual derivative identify how operator variation changes directional response. T082 supplies the conditional first variation of the second-order Morandotti value function and its barycentric score response. T068–T070 supply the geometric covariance correction. These are complementary layers:

- T097 reconstructs kinematic defect closure from gradient and mismatch;
- T091 composes the Frank/Burgers traction tensors and quantifies their mixed anisotropic response;
- T082 differentiates the relaxed second-order energy when its value function is differentiable (or uses a justified subgradient);
- T068–T070 control the barycentric spatial averaging and remainder.

No universal sign is asserted for the mixed Frank–Burgers term. No universal monotonicity in core separation or mesh size is asserted.

## 7. Relation to T096 and correction of scope

T096 remains correct for its stated data: an Airy stress field and a constitutive recovery of symmetric strain do not determine the skew elastic distortion. It must not be read as a non-identifiability theorem for the full RGS–Morandotti kinematic model. When the independently specified gradient law supplies (G), the polar rotation is obtained from (G) as in Section 2. The remaining requirement is to ensure that the model also supplies the mismatch field and its trace/cut convention for the translational closure.

Accordingly, T096 is a restricted Airy-data statement; T097 is the combined kinematic reconstruction law under its additional hypotheses. This resolves the apparent conflict without weakening either result.

## 8. Verification programme and classification

**Exact/proved component identities**
- polar rotation formula for an orientation-preserving planar gradient;
- row-wise Stokes identity (97.1), including distributional interface terms when traces exist;
- finite-complex identity (97.2) from T080;
- Dirichlet centroid/covariance and Taylor remainder (97.3) from T068–T070;
- (SE(2)) semidirect-product composition (97.4).

**Numerically verified elsewhere in the repository**
- T091 five-level Frank/Burgers tensor additivity and nonzero mixed contribution for the reported source configuration;
- T093–T095 manufactured Cartan/SE(2) audit and prescribed two-core source adapter.

**Still to verify on the same computed Morandotti fields**
1. Export the kinematic gradient (G_h) used by the verified gradient law, with element/cell and chart identifiers.
2. Export (\mathsf D_h=\nabla g_h-G_h), or the equivalent edge cochain and seam/cut traces.
3. Compute polar-frame increments and loop winding around each core; report branch and base-frame conventions.
4. Compute Burgers closures from the edge mismatch cochain, compare with the prescribed source charges in T095, and repeat over the five mesh levels.
5. Reconstruct barycentres/covariances from the actual mesh coordinates and compare centroid-only, covariance-corrected and directly integrated cell contributions.
6. Recompute the T091 mixed tensor and residual sensitivity using measured rather than prescribed Frank/Burgers data.

**Classification:** component identities proved; combined law conditional on the stated kinematic and trace inputs; two-core measured-field validation OPEN.  
**FLN**
