# 64-TG, Vesica geometry, barycentric moments and the Morandotti interface

**Source audited:** 2412.0104v1.pdf, Bruno R. Galeffi, *On the 14-Octahedron Backbone of the Bimetric 64-Tetrahedron Grid Universe* (viXra:2412.0104, 18 December 2024).  
**Purpose:** connect the source's actual geometric claims to the existing Vesica and Morandotti moment/gradient programme without importing its cosmological interpretations as mathematical conclusions.

## 1. Executive result and evidence boundary

The paper proposes a geometric decomposition of a 64-tetrahedron arrangement, including a cuboctahedral reference body, 14 octahedral cavities and 24 square-pyramidal cavities. It also proposes a Jitterbug-type deformation and discusses overlapping circumspheres. These are useful geometric inputs for a moment/phase analysis.

The paper does **not** provide a coordinate list, an oriented incidence complex, a complete tetrahedralization, or a parametrized deformation map. Consequently, the source alone does not determine unique centroids, covariance tensors, interface normals, phase gradients, or a time period. Its bimetric field equations and cosmological interpretations are not derived from the finite geometry.

The bridge below is divided into exact scalar checks, conditional geometric constructions, and open physical interpretations.

## 2. Exact volume audit

Use the paper's reference edge a for the embedded cuboctahedron. For a regular tetrahedron of edge a/2,
\[
V_T=\frac{\sqrt2}{12}\left(\frac a2\right)^3
=\frac{\sqrt2}{96}a^3.
\]
Thus 64 such tetrahedra have total material volume
\[
64V_T=\frac{2\sqrt2}{3}a^3.
\]
This is distinct from the paper's stated **envelope/grid volume**
\[
V_{64\mathrm{TG}}=\frac{5\sqrt2}{4}a^3.
\]
Their ratio is
\[
\frac{64V_T}{V_{64\mathrm{TG}}}=\frac{8}{15}.
\]
Hence the reported packing fraction 8/15 is internally consistent if, and only if, the first quantity denotes tetrahedral material and the second the enclosing grid volume. They must not be conflated.

The cuboctahedron decomposition in the source is arithmetically consistent:
\[
\frac{5\sqrt2}{3}a^3
+8\left(\frac{\sqrt2}{96}a^3\right)
-24\left(\frac{\sqrt2}{48}a^3\right)
=\frac{5\sqrt2}{4}a^3.
\]
Here the square-pyramid volume is \(\sqrt2 a^3/48\), as used in the source's Eq. (2). If its base side is a/2, this volume corresponds to height \(\sqrt2 a/4\); the height must not be silently replaced by a/4. The cavity-volume sum is
\[
14V_{O(a/2)}+24V_{P(a/2)}
=14\frac{\sqrt2}{24}a^3+24\frac{\sqrt2}{48}a^3
=\frac{13\sqrt2}{12}a^3,
\]
which equals \(V_{CO(a)}-56V_T\). Also,
\[
14V_{O(a/2)}=56V_T=\frac{7\sqrt2}{12}a^3.
\]
These are exact consequences of the stated counts and standard regular-solid formulae. They do not independently prove that the pictured cavities form a non-overlapping partition; that requires an incidence/coordinate certificate.

## 3. Surface-area claim: correction required

For a regular tetrahedron with edge a/2, one face has area
\[
A_T=\frac{\sqrt3}{4}\left(\frac a2\right)^2
=\frac{\sqrt3}{16}a^2.
\]
If 144 exposed faces are all faces of these regular tetrahedra, their total planar area is therefore
\[
A_{144}=144A_T=9\sqrt3\,a^2\simeq15.5885a^2,
\]
not 18a² as stated in the paper. This discrepancy is not a rounding effect. Likewise, 16 such faces have total area \(\sqrt3a^2\), not 2a².

The paper's circumsphere radius \(R=a\sqrt{3/2}\) gives
\[
A_{S^2}=4\pi R^2=6\pi a^2\simeq18.8496a^2.
\]
Thus
\[
\frac{A_{S^2}}{A_{144}}=\frac{2\pi}{3\sqrt3}\simeq1.2092.
\]
The claimed comparison 18a² versus 6πa² has a relative deficit \(1-3/\pi\simeq4.51\%\), but the value 18a² does not follow from 144 equilateral faces of edge a/2.

A second logical gap is independent of that arithmetic issue: 144 planar faces do not automatically project to 144 equal-area spherical triangles that tile the circumsphere. The spherical-excess calculation
\[
\Delta=\frac{6\pi a^2}{144},\qquad E=\frac{\Delta}{R^2}=\frac{\pi}{36}
\]
is valid only conditional on an equal-area spherical partition. Equal-area projection, coverage, non-overlap and the face-to-sphere map are not established by the face count alone.

## 4. Golden-ratio comparison: approximate versus imposed equality

For a regular octahedron of edge a, the inradius is \(r_i=a/\sqrt6\), so its insphere volume is
\[
V_{\mathrm{in}}=\frac{4\pi}{3}\left(\frac a{\sqrt6}\right)^3
=\frac{2\pi}{9\sqrt6}a^3.
\]
Dividing by the stated stellated-octahedron volume \(\sqrt2a^3/8\) gives
\[
\frac{V_{\mathrm{in}}}{V_{\mathrm{stell}}}
=\frac{8\pi}{9\sqrt3}\simeq1.6123,
\]
which is close to, but not equal to, \(\varphi\simeq1.6180\). The radius in the paper's subsequent equation is adjusted to force the ratio to equal \(\varphi\); it is not the standard octahedral inradius. These statements must remain separate.

## 5. Where the Vesica enters the source geometry

The paper explicitly describes radial projection of each tetrahedron onto its circumsphere and overlapping spherical analogues. This is the natural, source-faithful entry point for Vesica geometry.

Let tetrahedron i have vertices \(p_{i,0},\ldots,p_{i,3}\in\mathbb R^3\), circumcentre \(q_i\), and circumradius \(\rho_i\). Define
\[
S_i=\{x:\|x-q_i\|=\rho_i\},\qquad
B_i=\{x:\|x-q_i\|\leq\rho_i\}.
\]
For two equal radii \(\rho\), with centre distance \(d<2\rho\), the intersection \(B_i\cap B_j\) is a three-dimensional lens. Its planar section by the plane through the two centres and perpendicular to their joining line is a two-circle Vesica Piscis. In the special case d=ρ, the section has the standard equal-circle Vesica geometry recorded in T137.

For three balls, distinguish the union, the common intersection, the three pairwise lenses, and planar sections of each. Only a specified common intersection (or its specified planar section) is a natural three-body candidate for a triveca. The source does not specify a unique triple of sphere centres/radii or a canonical triveca section. No triveca area/volume formula is asserted until those data are fixed.

For the actual 64-TG, the required data are the 64 tetrahedron vertex quadruples, or equivalently a certified list of \((q_i,\rho_i)\), together with the chosen pair/triple incidence. Without them, the number and shape of distinct Vesica lenses cannot be inferred from the drawings.

## 6. Barycentres, covariance and gradient law

For any measurable region \(F\subset\mathbb R^3\) of positive volume, define
\[
|F|=\int_F1\,dx,\quad
c_F=\frac1{|F|}\int_Fx\,dx,\quad
\Sigma_F=\frac1{|F|}\int_F(x-c_F)(x-c_F)^T\,dx.
\]
For \(g\in C^3\) on a neighbourhood of the convex hull of F, Taylor's theorem gives
\[
\frac1{|F|}\int_Fg(x)\,dx
=g(c_F)+\frac12D^2g(c_F):\Sigma_F+R_F,
\quad
|R_F|\leq\frac{h_F^3}{6}\sup_{\operatorname{conv}(F)}\|D^3g\|_{op},
\]
where \(h_F=\sup_{x\in F}\|x-c_F\|\). The first-order term vanishes exactly because
\[
\int_F(x-c_F)\,dx=0.
\]
This local moment mechanism applies to tetrahedra, octahedra, pyramids, sphere lenses and their specified intersections once their geometric definitions are fixed.

For a finite family \(F_i\) with positive measures, the barycentre of the **sum measure** \(\sum_i\mathbf1_{F_i}dx\) is
\[
c_{\mathrm{sum}}=\frac{\sum_i|F_i|c_{F_i}}{\sum_i|F_i|}.
\]
This is not generally the barycentre of the union: overlaps are counted with multiplicity in the sum measure. For the union, use its indicator \(\mathbf1_{\cup_iF_i}\), or an inclusion-exclusion decomposition with all intersections explicitly included.

For cavity regions \(O_1,\ldots,O_{14}\), the covariance of the normalized sum measure obeys the exact within/between decomposition
\[
\Sigma_{\mathrm{sum}}
=\frac{\sum_i|O_i|\left[\Sigma_{O_i}
+(c_{O_i}-c_{\mathrm{sum}})(c_{O_i}-c_{\mathrm{sum}})^T\right]}
{\sum_i|O_i|}.
\]
The first term measures each cavity's internal spread; the second measures the spatial arrangement of the cavity centres. This is an exact bridge from the 14-octahedron backbone to barycentric moments for the declared sum measure, not a claim about the union or physical mass.

## 7. Phase, gradients and oscillations: a conditional dynamic bridge

Once a Jitterbug path is supplied as an actual differentiable family of configurations \(q(t)\), each vertex and sphere centre becomes time-dependent. A phase field \(\theta(x,t)\) can then be defined on the chosen geometric carrier, with spatial gradient \(k=\nabla_x\theta\). For a fixed region F,
\[
\frac1{|F|}\int_Fe^{i\theta(x,t)}dx
=e^{i\theta(c_F,t)}
\left(1-\frac12 k(c_F,t)^T\Sigma_Fk(c_F,t)+\mathcal R_3\right)
\]
for an affine local phase and small phase variation; the cubic remainder is controlled by the third-order Taylor bound. For a moving region F(t), its derivative includes the boundary-transport term from Reynolds' transport theorem:
\[
\frac d{dt}\int_{F(t)}e^{i\theta}\,dx
=\int_{F(t)}i\,\partial_t\theta\,e^{i\theta}dx
+\int_{\partial F(t)}e^{i\theta}v_n\,dS.
\]
This is a precise route from geometry to phase response and oscillation if the motion and phase are specified. The paper itself says that the Jitterbug details and period remain unknown; it therefore supplies no derived frequency, angular momentum or cosmological oscillation law.

## 8. Bernoulli layer: keep it downstream

Bernoulli numbers/polynomials may enter after a discrete sampling rule has been defined—for example, when sums over a one-parameter family of layers or time steps are compared with an integral by Euler–Maclaurin. The paper's tentative Fibonacci labels do not by themselves define such a sampling rule. No Bernoulli coefficient, period or dynamical recurrence is inferred from the PDF.

## 9. Minimal data needed to close the bridge

A rigorous computational follow-up needs:
1. coordinates for the 64 tetrahedra (four vertices per tetrahedron), with a declared common scale and orientation;
2. tetrahedron-to-tetrahedron face/edge incidence and identification of the 14 octahedra and 24 pyramids;
3. a certificate of non-overlap/coverage for the claimed volume decomposition;
4. circumsphere centres/radii and selected pairwise/triple intersections;
5. a differentiable Jitterbug coordinate path if phase evolution or frequency is to be studied.

From these data one can compute exact or certified volumes, centroids, covariance tensors, interface normals, Vesica/triveca sections, and discrete gradients. The result can then be integrated with T130's Q6 gradient/barycentre/moment framework and the existing Vesica records. Until then, the bridge is a **conditional mathematical programme**, not a proved identification of 64-TG with Q6, RGS, a bimetric spacetime or a cosmological model.

## 10. Status summary

| Claim | Status |
|---|---|
| Regular-solid volume identities in §2 | Exact arithmetic, conditional on stated counts and standard solids |
| 8/15 packing fraction | Exact ratio of material volume to stated envelope volume |
| 144-face area = 18a² | **Incorrect** for 144 regular tetrahedron faces of edge a/2; correct value \(9\sqrt3a^2\) |
| Equal-area spherical partition and E=π/36 | Conditional; partition map not supplied |
| Octahedron insphere ratio equals φ | False for the standard inradius; only approximate |
| Pairwise circumsphere overlap as Vesica lens | Exact definition; actual 64-TG instances await coordinates |
| Triveca | Not uniquely defined by the source; requires a declared triple intersection/section |
| Barycentric Taylor/covariance law | Proved general local identity under stated regularity |
| Jitterbug phase/oscillation law | Open until a path and phase field are specified |
| Cosmological/bimetric interpretation | Not established by this geometric audit |

## References and internal links

- Galeffi, *On the 14-Octahedron Backbone of the Bimetric 64-Tetrahedron Grid Universe*, viXra:2412.0104 (source PDF in repository root: 2412.0104v1.pdf).
- [T130 — Q6 discrete gradients, barycentres, traction moments and resistance assembly](../theorems/T130-q6-discrete-gradients-barycentres-resistance.md).
- [T137 — Exact geometry of the Vesica Piscis and the sqrt(3) hexagonal chord](../theorems/T137-vesica-piscis-two-circle-hexagon-pi-sqrt3.md).
- [Vesica–Needham–Bonilla dossier](VESICA_NEEDHAM_BONILLA_SQRT3_PHI_DOSSIER_2026-11-18.md).
- [Integrated moments/barycentres/Morandotti synthesis](SYNTHESIS_MOMENTS_BARYCENTRES_GAMMA_BETA_ZETA_MORANDOTTI_2026-11-10.md).
