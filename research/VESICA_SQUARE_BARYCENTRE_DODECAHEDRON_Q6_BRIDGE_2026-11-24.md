# Vesica–square–barycentre–dodecahedron–Q6 bridge: exact local geometry and open operator lift

**Date:** 24 November 2026  
**Classification:** exact Euclidean construction for the local vesica/square/triangle data; exact affine-gradient and barycentre formulas; proposed global dodecahedral/Q6 assembly, with the operator intertwining still open.

## 1. Vesica and its two equilateral triangles

Take two circles of radius \(R>0\) with centres
\[
O_-=(-R/2,0),\qquad O_+=(R/2,0).
\]
Their common chord endpoints are
\[
P=(0,\sqrt3R/2),\qquad Q=(0,-\sqrt3R/2).
\]
Then \(O_-O_+P\) and \(O_-O_+Q\) are equilateral triangles of side \(R\). Their union is the rhombus with angles \(60^\circ\) and \(120^\circ\), not a square. This is the exact starting geometry recorded in T137.

## 2. A canonical square inside the vesica

Let
\[
M_+=(0,R/2),\qquad M_-=(0,-R/2).
\]
These points lie on the common chord segment because \(R/2<\sqrt3R/2\). The four points, in cyclic order,
\[
O_-,\ M_+,\ O_+,\ M_-,
\]
form a square: its two diagonals are \(O_-O_+\) and \(M_+M_-\), both of length \(R\), and they are perpendicular and bisect one another. Hence
\[
\boxed{\ell_{\square}=R/\sqrt2,\qquad
d_{\square}=R,\qquad
A_{\square}=R^2/2.}
\]
Moreover, \(M_\pm\) lie in both disks since
\[
|M_\pm-O_\pm|=|M_\pm-O_\mp|=R/\sqrt2<R.
\]
The whole square lies in the vesica because the lens is convex. This is a precise square construction using the circle centres and the central subsegment of the common chord of length \(R\). It is a declared canonical choice relative to the centre axis; it is not the union of the two equilateral triangles and is not the only square that could be inscribed in the lens.

The square's diagonal reflection is an involution exchanging two congruent right triangles. Its parity projections are \((I\pm S_\square)/2\). This realizes the abstract \(\mathbb Z_2\) projector algebra geometrically, but an intertwiner to the RGS carrier is not inferred from the picture alone.

## 3. Triangle barycentres and exact gradients

The two triangle centroids are
\[
G_+=\frac{O_-+O_++P}{3}
=\left(0,\frac{\sqrt3R}{6}\right),\qquad
G_-=\frac{O_-+O_++Q}{3}
=\left(0,-\frac{\sqrt3R}{6}\right).
\]
Thus
\[
|G_+-G_-|=R/\sqrt3.
\]
These are geometric barycentres of the two equilateral cells, not the centre of the vesica or a dodecahedral vertex.

On the upper triangle \(T_+=\operatorname{conv}(O_-,O_+,P)\), define the affine barycentric coordinate functions \(\lambda_-,\lambda_+,\lambda_P\), with \(\lambda_i(v_j)=\delta_{ij}\). Since the altitude is \(h=\sqrt3R/2\),
\[
\lambda_P(x,y)=\frac{2y}{\sqrt3R},
\]
\[
\lambda_-(x,y)=\frac12-\frac{x}{R}-\frac{y}{\sqrt3R},\qquad
\lambda_+(x,y)=\frac12+\frac{x}{R}-\frac{y}{\sqrt3R}.
\]
Their gradients are constant:
\[
\nabla\lambda_P=\left(0,\frac{2}{\sqrt3R}\right),\quad
\nabla\lambda_-=\left(-\frac1R,-\frac1{\sqrt3R}\right),\quad
\nabla\lambda_+=\left(\frac1R,-\frac1{\sqrt3R}\right),
\]
and
\[
\boxed{|\nabla\lambda_i|=\frac{2}{\sqrt3R}\quad(i=-,+,P).}
\]
The lower-triangle formulas follow by \(y\mapsto-y\). This supplies a fully specified local gradient/barycentre package. It does not yet define a global field on the dodecahedron; that requires a rule for transporting the local vertex labels and matching gradients across adjacent faces.

## 4. From the vesica pentagon to the dodecahedral incidence structure

The existing repository already contains two relevant exact/numerical ingredients:

- The Vesica–pentagon construction records an exact construction of a regular pentagon from the vesica, including the golden-ratio length \(r/\varphi\) and the \(72^\circ\) phases. Its chosen linear frame map is explicitly convention-dependent; it does not derive a spatially varying transport or torsion.
- T139 constructs and audits the icosahedral hull, with the regular icosahedron at \(t=\varphi\). The regular dodecahedron is the polar dual of the regular icosahedron after fixing a centre and scale. Its 12 pentagonal faces correspond to the 12 icosahedral vertices, and its 20 vertices correspond to the 20 icosahedral faces.

This gives a canonical global combinatorial target: use the icosahedron/dodecahedron dual incidence, and use the vesica-derived pentagon as a local face frame. But the local pentagon construction alone does not choose the 12 face-frame rotations or prove their compatibility around edges and vertices. Those transition maps must be fixed and checked.

## 5. Interface with Q6, discrete gradients and the function \(f\)

The repository already has a finite Q6–RGS interpolation bridge. On the selected three-dimensional Q6 invariant sector, the reduced graph Laplacian has eigenvalues
\[
0,\ 4,\ 6,
\]
and the selected lower RGS triplet has eigenvalues
\[
0.5,\ 0.6,\ 0.7.
\]
The unique polynomial of degree at most two mapping the first triple to the second is
\[
\boxed{f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}.}
\]
This interpolation and its finite-dimensional map are recorded in T144 §7 and the Q6–Vesica–RGS spectral-intertwiner research note. It is an exact three-node interpolation identity on the selected sector, not yet a theorem that the dodecahedron generates the Q6 operator.

T130 gives a specified least-squares discrete gradient on Q6 and a weighted barycentre/moment construction. Those formulas can be used only after a map from the dodecahedral vertices/faces/edges to Q6 states/links has been fixed, including weights, orientations and incidence. T141 supplies an antipodally equivariant path-valued lift of the icosahedral 1-skeleton into Q6, but it does not preserve edge lengths as single Q6 edges, does not provide a 2-chain lift, and does not yet intertwine the dodecahedral/icosahedral metric Laplacian with the selected Q6 Laplacian.

Therefore the missing theorem is sharply identifiable. Use the verified chain map through degree two to construct a metric/cochain or Hodge map such that:
1. it respects the antipodal involutions;
2. it transports the face-frame barycentric gradients and their adjoints;
3. its induced quadratic form is the Q6 Dirichlet form on the selected three-dimensional sector;
4. the induced operator has selected spectrum \(0,4,6\);
5. the resulting map intertwines the operator with the archived RGS lower triplet.

If these identities hold, the polynomial \(f\) follows by uniqueness of quadratic interpolation. Until then, the existing \(f\) is recovered from the Q6/RGS spectral correspondence, while the proposed vesica–dodecahedron derivation remains open.

## 6. Status table

| Claim | Status |
|---|---|
| Two equilateral triangles in the standard vesica | Exact |
| Their union is a \(60^\circ/120^\circ\) rhombus, not a square | Exact |
| The specified square \(O_-,M_+,O_+,M_-\) lies in the vesica | Exact |
| Triangle centroids and affine barycentric gradients above | Exact |
| Vesica-to-regular-pentagon construction | Exact, separately documented |
| Regular dodecahedron as polar dual of regular icosahedron | Classical exact geometry |
| Compatible 12-face pentagon-frame transport | Open |
| Equal-face-barycentre lift into Q6 | Constructed; antipodal-equivariant (T146) |
| Dodecahedral 1-chain map into Q6 | Constructed; boundary and antipodal identities certified; induced energy misses target spectrum (T146) |
| Dodecahedral chain map through degree two into Q6 | Constructed; minimum-norm antipodal-equivariant pentagon fillings certified (T146) |
| Compatible metric/cochain/Hodge intertwiner yielding (0,4,6) | Open |
| Derivation of Q6 eigenvalues \(0,4,6\) from that dodecahedral map | Open |
| Recovery of \(f\) from dodecahedral geometry alone | Open |
| Existing Q6-to-RGS three-node interpolation formula \(f\) | Exact interpolation identity on the selected finite sector |


## 7. T149 executed FEEC/Hodge audit (26 November 2026)

The supergolden polar-dual geometry (t=ψsg) and the regular icosahedral control (t=φ) have now been triangulated independently by the 32–90–60 face-centroid fan. The Whitney 0-, 1- and 2-form mass matrices, mass-induced adjoints, antipodal signed permutations and parity spectra are computed in T149. The supergolden Q6 comparison is made only with the T141 assignment; no Q6 map is imposed on the regular control.

The normalized Whitney 2-form displayed in T149 has squared L2 norm 1/A_T, not 4/A_T. The original specification's 4/A_T value was corrected before the reported audit. Both cases satisfy the incidence and antipodal metric tests, and all mass matrices are positive definite. The supergolden scalar Schur spectrum and T146 Q6 pull/chain spectra remain distinct; the Q6-sector intertwining residuals are 5.7099189664 and 2.1936912594. The regular control has regular pentagonal frames to machine precision; the supergolden pentagons are measurably deformed.

This completes the canonical FEEC assembly, but not the missing connection: local pentagonal frames do not determine transition maps or holonomy across faces. The derivation of the Q6/RGS polynomial f from a global dodecahedral Hodge operator remains open. See [T149](../theorems/T149-supergolden-dodecahedral-whitney-hodge.md), its [audit script](../scripts/audit_t149_dodecahedron_feec_hodge.py), and the [machine-readable summary](../results/json/t149_supergolden_dodecahedron_feec_hodge_summary.json).
