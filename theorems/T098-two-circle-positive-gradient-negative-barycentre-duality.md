# T098 — Universal two-circle duality: positive gradient triangle and negative barycentre triangle

**Date:** 11 November 2026  
**Status:** the Euclidean two-circle geometry, the paired-centroid identities and the affine gradient transformation are proved below. The identification of this geometric duality with a particular physical field or constitutive law requires the model-specific hypotheses stated in Section 6.  
**Role:** foundational geometric law. T097 is a downstream Frank–Burgers/Morandotti application, not the generator of this construction.

## 1. Two-circle generator

Let \(C_1,C_2\in\mathbb R^2\), let \(r>0\), and impose
\[
|C_2-C_1|=r.
\]
Let \(u=(C_2-C_1)/r\), choose the positive quarter-turn \(u^\perp=Ju\), and put
\[
M=\frac{C_1+C_2}{2},\qquad
P_\pm=M\pm\frac{\sqrt3\,r}{2}u^\perp.
\]
Then \(P_+\) and \(P_-\) are exactly the two intersections of the circles
\[
\mathcal C_i=\{x:|x-C_i|=r\},\qquad i=1,2.
\]
The two triangles
\[
\Delta_+=\operatorname{conv}(C_1,C_2,P_+),\qquad
\Delta_-=\operatorname{conv}(C_1,C_2,P_-)
\]
are equilateral, have the same side length \(r\), and have opposite orientations. With the orientation induced by \((u,u^\perp)\),
\[
A_\pm^{\rm or}=\pm\frac{\sqrt3}{4}r^2,\qquad
|\Delta_\pm|=\frac{\sqrt3}{4}r^2.
\]
The reflection
\[
\mathcal R(x)=M+\bigl(2uu^T-I\bigr)(x-M)
\]
fixes the line of centres, exchanges \(P_+\leftrightarrow P_-\), and maps \(\Delta_+\) onto \(\Delta_-\). It is an orientation-reversing isometry.

## 2. The negative triangle and its barycentre

Define the areal barycentres
\[
B_\pm=\frac{1}{|\Delta_\pm|}\int_{\Delta_\pm}x\,dA
=\frac{C_1+C_2+P_\pm}{3}.
\]
Substitution of the two-circle coordinates gives the exact identities
\[
\boxed{B_\pm=M\pm\frac{r}{2\sqrt3}u^\perp,}
\qquad
\boxed{B_+-B_-=\frac{r}{\sqrt3}u^\perp,}
\qquad
\boxed{\frac{B_++B_-}{2}=M.}
\]
In particular, the negative-triangle barycentre is not an independent fitted point: it is fixed by the same two-circle geometry. The barycentre branch is the \(\Delta_-\) branch; its orientation is negative, while its positive area measure in the barycentre integral is \(|\Delta_-|\,dA\).

## 3. The positive triangle and the gradient

Let \(f\in C^1(\overline{\Delta_+})\). Define the positive-triangle mean-gradient operator
\[
\mathcal G_+[f]
:=\frac{1}{|\Delta_+|}\int_{\Delta_+}\nabla f(x)\,dA.
\]
By the planar divergence theorem, componentwise,
\[
\boxed{
\mathcal G_+[f]
=\frac{1}{|\Delta_+|}\int_{\partial\Delta_+}f\,n_+\,ds,
}
\]
where \(n_+\) is the outward unit normal to the positively oriented boundary of \(\Delta_+\). This is the exact gradient quantity assigned to the positive triangle. If \(f\) is affine, \(\mathcal G_+[f]=\nabla f\) everywhere, so the construction reproduces its gradient exactly; for non-affine \(f\), it is the cell-average gradient, not an unsupported pointwise identity.

Reflection transports the positive-triangle gradient to the negative triangle. For \(f_-=f\circ\mathcal R^{-1}\),
\[
\boxed{
\mathcal G_-[f_-]
=\frac{1}{|\Delta_-|}\int_{\Delta_-}\nabla f_-(x)\,dA
=Q\,\mathcal G_+[f],
\qquad Q=2uu^T-I.
}
\]
Since \(Q^TQ=I\) and \(\det Q=-1\), the gradient transforms as a covector under the orientation-reversing reflection. The sign change of oriented area is not an extra sign in the positive area average; it is carried by the boundary orientation and the reflection map.

## 4. Universal paired-triangle law

**Theorem 98.1 (two-circle positive-gradient / negative-barycentre duality).**  
For every \(C_1,C_2\in\mathbb R^2\) with \(|C_2-C_1|=r>0\), the two equal-radius circles determine a unique pair \((\Delta_+,\Delta_-)\) of equilateral triangles with common base \(C_1C_2\), equal area and opposite orientation. Their barycentres are the reflected pair in Section 2. For every \(C^1\) scalar field on \(\Delta_+\), its mean gradient is given exactly by the boundary formula in Section 3 and transforms under the same reflection by \(Q\). Thus the positive gradient branch and negative barycentre branch are not independent geometric inputs: both are functorial constructions of the same two-circle pair, with scale \(r\), centre \(M\), and axis \(u\).

**Proof.** The distance identities
\[
|P_\pm-C_1|^2=|P_\pm-C_2|^2
=\frac{r^2}{4}+\frac{3r^2}{4}=r^2
\]
establish the two circle intersections and equilateral triangles. The signed areas follow from the base \(r u\) and the signed heights \(\pm\sqrt3r/2\). The barycentre formula follows from the centroid formula for a triangle. The reflection formula is immediate from its action on the orthonormal basis \((u,u^\perp)\). The gradient identity is the divergence theorem. Finally, the chain rule gives
\(\nabla(f\circ\mathcal R^{-1})(x)=Q\nabla f(\mathcal R^{-1}x)\); changing variables by the isometry \(\mathcal R\) proves the transformation law. \(\square\)

## 5. Scale covariance and anisotropic information

Under a similarity \(x\mapsto a+\lambda Sx\), where \(\lambda>0\) and \(S\in O(2)\), the paired triangles map to the corresponding two-circle pair. Their areas scale by \(\lambda^2\), barycentres by \(a+\lambda S(\cdot)\), and mean gradients of a transported scalar field by the chain rule. The normalized barycentre and mean-gradient constructions therefore commute with similarities, with the expected tensorial scaling. This is the precise Euclidean scale-covariance meant by “universal”.

The negative-triangle covariance is
\[
\Sigma_-=\frac{1}{|\Delta_-|}
\int_{\Delta_-}(x-B_-)(x-B_-)^T\,dA.
\]
It is the second central moment of the negative branch and transforms as
\[
\Sigma_-=Q\Sigma_+Q^T
\]
under the reflection. T068 supplies the exact covariance formula and the quadratic Taylor correction on each triangle. Consequently, anisotropy is retained as a tensor, not collapsed to a scalar residual or discarded as noise.

## 6. Scope: geometry versus physical law

Theorem 98.1 is universal as a Euclidean geometric and differential identity. It does **not**, by itself, prove that an arbitrary physical gradient field equals a particular barycentre, nor does it derive a constitutive stress law. To use the pair for a physical system one must specify:
1. which scalar/vector/tensor field is sampled on \(\Delta_+\);
2. which measure or weighting defines the negative-branch barycentre;
3. the transport or reflection convention identifying the two local frames;
4. how the resulting gradient and barycentric moments enter the model's energy, incompatibility, or balance equation.

For the Morandotti/RGS application, these choices must be made from the already verified gradient law and the existing barycentric moment identities, not fitted after the fact. Dislocations and disclinations enter only after the resulting kinematic data are converted into the appropriate incompatibility/holonomy variables. T091–T097 then provide downstream interaction, anisotropy, and Frank–Burgers machinery.

## 7. Evidence classification

- **PROVED:** two-circle intersection coordinates; equilateral geometry; opposite signed areas; exact negative-branch barycentre; reflection relation; mean-gradient boundary identity; reflected gradient transformation; similarity covariance.
- **PROVED in T068:** triangle covariance identity and second-order barycentric quadrature with its stated remainder.
- **APPLICATION, conditional:** coupling the paired geometric quantities to Morandotti defect sources, Frank–Burgers holonomy and anisotropic energy.
- **OPEN:** derive and validate the model-specific field/measure identification on the actual two-core FEM data. This is a physical/model validation task, not a gap in the Euclidean two-circle theorem.

**Classification:** foundational Euclidean duality theorem proved; physical universal-law interpretation conditional on the model's field and measure assignments.  
**FLN**
