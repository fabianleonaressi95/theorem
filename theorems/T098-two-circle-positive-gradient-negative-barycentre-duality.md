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

## 7. Unification: what the reflection identifies, and what it does not

The two-circle construction gives a canonical geometric correspondence between the positive and negative branches. It transports every field once its tensor type and transformation rule have been specified. This is the rigorous content of the unification principle: the two branches are two realizations of one geometric generator, rather than independently fitted geometries.

For the reflection matrix \(Q=2uu^T-I\), the planar rotation generator satisfies
\[
QJQ^T=-J.
\]
Consequently, if a local rotational connection is \(\omega J\), its reflected connection is \(-\omega J\) (with the reflected path and chart convention understood). A translational vector \(b\), by contrast, is transported as \(Qb\). These are different representation laws.

In Cartan language, curvature and torsion are respectively an \(\mathfrak{so}(2)\)-valued two-form and a vector-valued two-form. Under an orientation-reversing reflection their components acquire the induced representation and the two-form orientation sign. The reflection transports each object according to its own tensor character; it does **not** canonically turn an \(\mathfrak{so}(2)\)-valued curvature into a translational torsion, or a Frank charge into a Burgers vector. Likewise, Frank and Burgers data have different types (scalar angle versus vector translation in the planar setting) and cannot be identified merely by reflecting the triangles.

Thus the unifying correspondence is:
\[
\begin{array}{c}
\text{positive branch: gradient / boundary flux}\\
\downarrow\quad \mathcal R_* \text{ (tensorial push-forward)}\\
\text{negative branch: reflected gradient data / barycentric moments}
\end{array}
\]
and, once a physical Cartan/defect model has been specified, the rotational and translational sectors are both transported consistently through that same geometric correspondence. A stronger **exchange**
\[
(\text{rotation},\text{Frank},\text{curvature})
\longleftrightarrow
(\text{translation},\text{Burgers},\text{torsion})
\]
would require an additional, explicitly defined bundle isomorphism or constitutive map between the rotational and translational representation spaces, with compatible units, equivariance and balance laws. The two-circle reflection alone does not supply such a map.

**Two-core implication.** If the two centres are interpreted as defect-core locations, the reflection gives an exact geometric pairing of their sampling domains and transforms their gradient, centroid and covariance data. Whether the *measured* core fields, anisotropic energy contributions and residuals obey the corresponding reflected identities is a testable model statement. It must be checked on the actual FEM fields, with the core labels, material axes, boundary conditions and frame transports reflected consistently. A nonzero residual is not automatically a physical dual contribution: it is evidence of anisotropy or unresolved modelling only after the predicted reflected quantity and its error bound have been specified.

## 8. Evidence classification

- **PROVED:** two-circle intersection coordinates; equilateral geometry; opposite signed areas; exact negative-branch barycentre; reflection relation; mean-gradient boundary identity; reflected gradient transformation; similarity covariance.
- **PROVED in T068:** triangle covariance identity and second-order barycentric quadrature with its stated remainder.
- **APPLICATION, conditional:** coupling the paired geometric quantities to Morandotti defect sources, Frank–Burgers holonomy and anisotropic energy.
- **OPEN:** derive and validate the model-specific field/measure identification on the actual two-core FEM data. This is a physical/model validation task, not a gap in the Euclidean two-circle theorem.

**Classification:** foundational Euclidean duality theorem proved; physical universal-law interpretation conditional on the model's field and measure assignments.  
**FLN**

## 9. Derivation from the established RGS–Morandotti laws

This section fixes the logical direction of the physical application. The two-circle construction is the geometric generator; the kinematic, incompatibility, moment, Cartan and interaction identities already established in the repository supply the downstream laws. No new Frank-to-Burgers constitutive map is introduced.

### 9.1 Kinematic split: the common source of the two defect sectors

For a planar structured deformation, take the fields and conventions of T079 and T097:
\[
\nabla g=G+\mathsf D,\qquad \mathsf D:=\nabla g-G.
\tag{98.2}
\]
Here \(G\) is the specified microscopic/structured gradient and \(\mathsf D\) is its mismatch with the macroscopic gradient. They are not independent fitted fields.

On every region where \(\det G>0\), the polar decomposition fixed in T097 gives
\[
G=R_GU_G,\qquad
R_G\in SO(2),\qquad
\theta_G=\operatorname{atan2}(G_{21}-G_{12},G_{11}+G_{22}),
\]
and the associated rotational connection is
\[
\omega_G=R_G^T dR_G=J\,d\theta_G.
\tag{98.3}
\]
The Frank winding around a loop is the winding of this gradient-derived frame, with chart transitions included as specified in T097. It is not an independently postulated microrotation.

The translational sector is fixed by the same kinematics:
\[
\boxed{
b_\gamma
=\oint_\gamma\mathsf D\,t\,ds
=\int_V\operatorname{Curl}\mathsf D,
\qquad \gamma=\partial V.
}
\tag{98.4}
\]
This is row-wise Stokes with the T079 convention. Interface/jump measures must be included when the field is piecewise smooth. Thus the rotational and translational data are both derived from the single split (98.2), by the already established polar-frame and Stokes identities. No centroid displacement is substituted for Burgers closure.

### 9.2 Exact discrete inheritance

On the finite oriented complex of T080, let \(\delta_0y\) be the nodal coboundary, \(G_h\) the declared microscopic edge cochain, and
\[
\mathsf D_h=\delta_0y-G_h.
\]
The chain-complex identity \(B_1B_2=0\) gives
\[
\boxed{
B_2^T\mathsf D_h
=B_2^T\delta_0y-B_2^TG_h
=-B_2^TG_h.
}
\tag{98.5}
\]
For every face 2-chain \(q\),
\[
(B_2q)^T\mathsf D_h=q^T B_2^T\mathsf D_h.
\tag{98.6}
\]
These are exact finite-mesh identities. They provide the discrete translational incompatibility and Stokes closure; they do not by themselves select the constitutive reconstruction of \(G_h\), nor prove a continuum shell homogenisation theorem.

### 9.3 Cartan and ordered \(SE(2)\) composition

Once the gradient-derived frame increments and the mismatch circulations have been computed in a common transported frame, T092–T094 prescribe their joint closure. For each oriented transport segment,
\[
g_e=(R(\Delta\theta_e),b_e)\in SE(2),
\]
and for an ordered loop \(\gamma=(e_1,\ldots,e_m)\),
\[
\boxed{
H_\gamma=g_{e_m}\cdots g_{e_1},\qquad
(R_2,b_2)(R_1,b_1)=(R_2R_1,b_2+R_2b_1).
}
\tag{98.7}
\]
The semidirect-product term is essential: translations are transported into the common base frame before they are added. T093 supplies the stated smooth-connection consistency result under its regularity and mesh hypotheses; T094 supplies a manufactured noncommuting numerical audit and a prescribed-source adapter. Neither is represented as extraction of singular core charges from the solved Morandotti FEM fields.

In the continuum Cartan description of T092, for a specified coframe and metric-compatible connection,
\[
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\tag{98.8}
\]
These are the torsion and curvature of that specified Cartan structure. The two-circle reflection transports them in their respective representations; it does not identify the two forms or replace the coframe/connection data.

### 9.4 Moment and anisotropy inheritance

The negative branch retains its full covariance tensor. For a cell density \(q\) with the regularity required in T068–T070, the barycentric expansion is
\[
\mathbb E[q]
=q(c)+\frac12D^2q(c):\Sigma+R,
\tag{98.9}
\]
with the theorem's stated remainder bound (and exactness for quadratic densities). This is the controlled route by which the geometry's anisotropic second moment enters cellwise sampling; it is not an arbitrary scalar correction.

For the Morandotti interaction, T091 proves on its fixed discrete mesh and source convention
\[
\boxed{T=T_F+T_B+T_{FB},}
\tag{98.10}
\]
where the mixed tensor is signed and cannot in general be discarded. T082 supplies the conditional first variation of the second-order Morandotti value function under its differentiability/subgradient hypotheses. These results preserve anisotropy as a tensorial response and distinguish exact algebraic identities from the continuum constitutive interpretation.

### 9.5 Reflection-equivariance: the precise residual statement

Let \(\mathcal R(x)=M+Q(x-M)\). For a vector field, its reflected push-forward is
\[
(\mathcal R_*h)(x)=Qh(\mathcal R^{-1}x);
\]
for a two-point tensor such as a displacement gradient, both the value and spatial indices must be transported. The corresponding residual is the difference between the second-core field and the correctly typed push-forward of the first-core field.

If the kinematic data, microscopic cochains, constitutive tensors, sources, boundary/interface traces and frame transitions are all transported by this same action, then the identities (98.2)–(98.10) are preserved by change of variables and by the chain-complex maps. In particular, the reflected mismatch circulation is the push-forward of the original circulation, and the ordered \(SE(2)\) product is conjugated by the change of base frame. This is the derived equivariance statement.

A zero two-core residual follows when the actual data are related by that reflected action. It is not implied merely by the Euclidean shape of the two triangles. If the material axes or sources are not reflected, their difference remains a genuine anisotropic/source residual and must be evaluated using the T082/T091 tensorial energy and interaction quantities. No conditions such as \(\operatorname{div}R=0\), \(\operatorname{curl}R=0\), or vanishing on the centre axis are added as universal laws; they require separate consequences of the particular governing equations and data.

### 9.6 Dependency theorem and evidence boundary

**Theorem 98.2 (RGS–Morandotti inheritance of the two-circle duality).**  
Take the two-circle pair of Theorem 98.1. On each branch, use the same reflected geometric identification and the kinematic fields of T079/T097. Assume the hypotheses already stated in those records: an orientation-preserving structured gradient wherever the polar frame is used; well-defined bulk and interface traces for the mismatch; compatible orientation and common-frame transport for loop data; and the regularity assumptions of T068–T070 for every barycentric Taylor expansion invoked. On a finite mesh, additionally use the oriented chain complex and cochains of T080.

Then:

1. the positive-branch gradient data are determined by the structured gradient and its polar frame, with rotational closure given by the frame winding and chart transitions;
2. the translational closure is determined by the circulation of \(\mathsf D=\nabla g-G\), equivalently by its bulk-plus-interface curl, and on the T080 complex by (98.5)–(98.6);
3. their joint discrete closure is the ordered \(SE(2)\) product (98.7), with the Cartan interpretation (98.8) only when the coframe and connection are specified;
4. the negative-branch barycentric covariance enters through the exact moment identities and controlled expansion (98.9);
5. the Frank–Burgers interaction and its anisotropy are composed by (98.10), retaining the signed mixed term.

All five conclusions are inherited from the cited component laws and the two-circle change of variables; no additional Frank-to-Burgers map, residual PDE constraint, or penalty energy is assumed.

**Proof.** The geometric pairing and reflection are Theorem 98.1. The structured-gradient split, polar reconstruction and row-wise Stokes identity are those of T079/T097. The finite-complex statements follow from \(B_1B_2=0\) and the discrete Stokes identity in T080. Ordered transport and the semidirect-product law are the exact group law used in T092–T094. The barycentric expansion follows from T068–T070, while the tensor decomposition follows by expansion of \(j=j_F+j_B\) in T091. Each identity is preserved under the reflected change of variables when all its inputs and frame conventions are transported consistently. The stated hypotheses are exactly those needed by the component results; no stronger continuum or physical conclusion is used. \(\square\)

**Evidence boundary.** Theorem 98.2 is a dependency/transfer theorem: its component identities are proved under the cited hypotheses. It does not claim that the current two-core Morandotti FEM export already contains the required \(G_h\), \(\mathsf D_h\), chart transitions and measured loop holonomies. T093–T095 and T094's prescribed-source fixture are not substitutes for that extraction. End-to-end measured-field validation, singular-core convergence and the surface extension identified in T079 remain open.

## 10. Corrected classification

- **PROVED geometrically:** the two-circle pair, reflection, centroids, mean-gradient boundary identity and covariance transport.
- **INHERITED EXACTLY under cited hypotheses:** structured-gradient split; polar-frame reconstruction; row-wise Stokes closure; finite-complex discrete Stokes; ordered \(SE(2)\) composition; barycentric moment expansion; Frank–Burgers tensor additivity.
- **NUMERICALLY VERIFIED within stated scope:** the manufactured noncommuting Cartan/\(SE(2)\) audit and prescribed two-core source adapter of T094, together with the specific mesh/energy audits recorded in T091.
- **OPEN:** extraction of \(G_h\), \(\mathsf D_h\), frame transitions and measured loop holonomies from the same solved two-core FEM fields; validation of reflected core fields with material anisotropy and boundary data transported consistently; singular-core and curved-surface convergence.
- **NOT CLAIMED:** a universal constitutive identity \(b=(r/\sqrt3)f u^\perp\); automatic vanishing of the two-core residual; universal harmonicity of that residual; or a proved continuum physical equivalence between curvature and torsion.

**Classification:** foundational two-circle geometric law plus a proved conditional inheritance theorem from the repository's established RGS–Morandotti identities. Physical validation on measured two-core fields remains open.  
**FLN**
