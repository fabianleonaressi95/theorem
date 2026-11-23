# 64-TG, Vesica geometry, barycentric moments and the Morandotti interface

**Source audited:** 2412.0104v1.pdf, Bruno R. Galeffi, *On the 14-Octahedron Backbone of the Bimetric 64-Tetrahedron Grid Universe* (viXra:2412.0104, 18 December 2024).  
**Purpose:** connect the source's actual geometric claims to the existing Vesica and Morandotti moment/gradient programme without importing its cosmological interpretations as mathematical conclusions.

## 1. Executive result and evidence boundary

The paper proposes a geometric decomposition of a 64-tetrahedron arrangement, including a cuboctahedral reference body, 14 octahedral cavities and 24 square-pyramidal cavities. It also proposes a Jitterbug-type deformation and discusses overlapping circumspheres. These are useful geometric inputs for a moment/phase analysis.

The paper does **not** provide a coordinate list, an oriented incidence complex, a complete tetrahedralization, or a parametrized deformation map. Consequently, the source alone does not determine unique centroids, covariance tensors, interface normals, phase gradients, or a time period. Its bimetric field equations and cosmological interpretations are not derived from the finite geometry.

The bridge below is divided into exact scalar checks, conditional geometric constructions, and open physical interpretations.

## 2. Exact volume audit
The paper does **not** provide a coordinate list or a complete incidence complex. However, its exact combinatorial counts admit a remarkably economical reconstruction: a finite face-centred-cubic lattice patch (the D3 root lattice) with 63 vertices, 240 nearest-neighbour edges and exactly 64 regular tetrahedra. The same coordinates recover the cuboctahedron, its enclosing cube, all 14 edge-a/2 octahedra and all 24 square-pyramidal cavities. This is an explicit coordinate model, not a claim that Galeffi printed or uniquely specified these coordinates. Its exact agreement with the independent counts and nested-solid descriptions is strong structural evidence for the reconstruction.

The paper still supplies no parametrized Jitterbug deformation map. Thus dynamic frequencies and phase evolution remain open. Its bimetric field equations and cosmological interpretations are not derived from the finite geometry.

The bridge below separates exact coordinate reconstruction, exact scalar checks, and open physical interpretations.

## 2. Explicit coordinates: the 64-TG as a finite FCC/D3 patch

Set
\[
h=\frac{a}{2\sqrt2},\qquad x(n)=h(n_1,n_2,n_3),
\]
with
\[
n\in\mathbb Z^3,\qquad -2\le n_i\le2,\qquad n_1+n_2+n_3\equiv0\pmod2.
\]
This gives the complete coordinate set: all 63 integer triples in the 5-by-5-by-5 box with even coordinate sum. The six vectors
\[
(\pm1,\pm1,0),\quad(\pm1,0,\pm1),\quad(0,\pm1,\pm1)
\]
are the nearest-neighbour differences. Their physical length is \(\sqrt2h=a/2\).

Join two vertices exactly when their integer-coordinate difference has squared norm 2. The resulting graph has **63 vertices and 240 edges**. Its four-cliques are exactly **64 regular tetrahedra**, each with edge \(a/2\). This reconstructs all three headline counts in the source from one coordinate rule, with no fitted parameters.

The 12 points whose absolute coordinate pattern is a permutation of \((2,2,0)\) form the embedded cuboctahedron of edge \(a\). The 8 points \((\pm2,\pm2,\pm2)\) are the vertices of the enclosing cube of edge \(\sqrt2a\). Of the 64 tetrahedra, exactly 56 lie in the cuboctahedron and 8 lie outside it, one at each cube corner.

### The 14 octahedral cavities

For every
\[
c\in\{-1,0,1\}^3,\qquad c_1+c_2+c_3\equiv1\pmod2,
\]
take the six vertices
\[
c\pm e_1,\quad c\pm e_2,\quad c\pm e_3.
\]
There are exactly 14 such centres: six axial centres \((\pm1,0,0)\) and permutations, and eight corner centres \((\pm1,\pm1,\pm1)\). Each six-vertex set is a regular octahedron of edge \(a/2\). The six axial octahedra have opposite vertices at the origin and at the six square-face centres of the cuboctahedron; the eight corner octahedra give the outer group described in the source. Each of the 112 triangular octahedron faces is also a face of one of the 64 tetrahedra.

### The 24 square pyramids

The cuboctahedron has six square faces, given in integer coordinates by \(n_i=\pm2\). On each such face, the lattice points determine exactly four square bases of side \(a/2\). Each base has one inward lattice apex at distance \(a/2\) from all four base vertices. This produces exactly \(6\cdot4=24\) regular square pyramids. Their height is
\[
H=\frac{a}{2\sqrt2}=\frac{\sqrt2a}{4},
\]
and their volume is \(\sqrt2a^3/48\).

### Exact barycentres and covariance tensors

The coordinate construction also closes the static Morandotti moment layer. For uniform volume measure on each cell, the barycentres and covariance tensors are:

- Regular tetrahedron \(T\), vertices \(p_0,\ldots,p_3\):
  \[
  c_T=\frac14\sum_{r=0}^3p_r,\qquad
  \Sigma_T=\frac{a^2}{160}I_3.
  \]
- Edge-\(a/2\) octahedron with centre \(c_O\):
  \[
  c_O=c,\qquad \Sigma_O=\frac{a^2}{80}I_3.
  \]
- Square pyramid with base centroid \(b\), apex \(p\), and face-normal coordinate axis \(j\):
  \[
  c_P=\frac{3b+p}{4},\qquad
  \Sigma_P=\frac{a^2}{80}(I_3-e_je_j^T)
  +\frac{3a^2}{640}e_je_j^T.
  \]

These are exact uniform-volume moments, not point-mass approximations. The tetrahedral centroid coincides with its circumsphere centre. The JSON stores all 102 cell centroids as exact rational lattice coordinates and the covariance diagonal entries as exact rational multiples of \(a^2\). This gives the geometric input for Morandotti's gradient reconstruction without fitting centroids from images.

### Incidence and partition certificate

Use the 56 tetrahedra inside the cuboctahedron, the 14 octahedra and the 24 square pyramids as the cells of its decomposition. The exact face-incidence audit gives:
- 200 distinct internal triangular faces, each incident to exactly two cells;
- 56 boundary facets, each incident to exactly one cell: 32 small triangles and 24 small squares;
- no face with incidence greater than two.

The signed orientation audit verifies that the two induced orientations on each of the 200 internal triangular faces are opposite and cancel. The 32 boundary triangles point outward and subdivide the cuboctahedron's eight triangular faces into four each. The 24 square-pyramid bases lie on the six square cuboctahedron faces, four per face, with each pyramid apex strictly inward. Thus the oriented sum of the 56 tetrahedra, 14 octahedra and 24 pyramids has precisely the cuboctahedron boundary.

The cell volumes also sum exactly to the cuboctahedron volume:
\[
56\frac{\sqrt2a^3}{96}
+14\frac{\sqrt2a^3}{24}
+24\frac{\sqrt2a^3}{48}
=\frac{5\sqrt2}{3}a^3.
\]
Because the cells are positively oriented convex polyhedra contained in the cuboctahedron and their internal oriented faces cancel to its boundary, this is a conforming polyhedral-chain partition, not merely a numerical volume coincidence. The signed incidence checks are implemented in the audit script and unit tests.

The full machine-readable coordinate set, all 102 cell moments, all 64 circumspheres, 360 lens pairs and 648 triple intersections are in [data/64tg_fcc_coordinates.json](../data/64tg_fcc_coordinates.json). Regenerate and audit it with [scripts/audit_64tg_fcc_coordinates.py](../scripts/audit_64tg_fcc_coordinates.py); its checks are in [tests/test_64tg_fcc_coordinates.py](../tests/test_64tg_fcc_coordinates.py).

## 3. Exact volume audit

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
## 4. Surface-area claim: correction required

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
## 5. Golden-ratio comparison: approximate versus imposed equality

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
## 6. Where the Vesica enters the source geometry

The paper explicitly describes radial projection of each tetrahedron onto its circumsphere and overlapping spherical analogues. This is the natural, source-faithful entry point for Vesica geometry.

The reconstructed coordinates now provide these data for all 64 tetrahedra. For tetrahedron \(i\), with vertices \(p_{i,0},\ldots,p_{i,3}\), its circumcentre is its vertex average
\[
q_i=\frac14\sum_{r=0}^3p_{i,r},
\]
and its circumradius is
\[
\rho_i=\frac{\sqrt6}{8}a.
\]
The machine-readable file stores \(q_i\) exactly as a numerator over 4 in the integer \(n\)-coordinates. In units \(h=a/(2\sqrt2)\), the radius is \(\rho_i/h=\sqrt3/2\).

Define the circumsphere and circumball
\[
S_i=\{x:\|x-q_i\|=\rho_i\},\qquad
B_i=\{x:\|x-q_i\|\leq\rho_i\}.
\]
For two equal radii \(\rho\), with centre distance \(d<2\rho\), the intersection \(B_i\cap B_j\) is a three-dimensional lens. Its planar section by the plane through the two centres and perpendicular to their joining line is a two-circle Vesica Piscis. In the special case d=ρ, the section has the standard equal-circle Vesica geometry recorded in T137.

For three balls, distinguish the union, the common intersection, the three pairwise lenses, and planar sections of each. Only a specified common intersection (or its specified planar section) is a natural three-body candidate for a triveca. The source does not specify a unique triple of sphere centres/radii or a canonical triveca section. No triveca area/volume formula is asserted until those data are fixed.

For the actual 64-TG, the required data are the 64 tetrahedron vertex quadruples, or equivalently a certified list of \((q_i,\rho_i)\), together with the chosen pair/triple incidence. Without them, the number and shape of distinct Vesica lenses cannot be inferred from the drawings.

## 6. Barycentres, covariance and gradient law
The exact centre-distance audit gives **360 overlapping pairs**. Their squared centre distances in \(h\)-units are either 1 or 2, both strictly less than \((2\rho_i/h)^2=3\). Each pair therefore defines a nonempty three-dimensional lens \(B_i\cap B_j\). A plane containing the line through \(q_i,q_j\) cuts the two balls in equal disks; their intersection in that plane is the corresponding two-circle Vesica Piscis. (The perpendicular-bisector plane instead cuts the common lens in its central circular section; it is not the Vesica section.)

There are also **648 triples** of circumballs with nonempty common intersection. The exact centre triangles have only two types:
- 432 right-isosceles cases with squared side lengths \((1,1,2)\) in \(h\)-units and minimum enclosing-circle radius squared \(1/2\);
- 216 equilateral cases with squared side lengths \((2,2,2)\) and minimum enclosing-circle radius squared \(2/3\).

Both radii are strictly below the circumball radius squared \(3/4\) in \(h\)-units. Thus every listed triple has a common point and defines a genuine three-ball overlap, a precise three-dimensional triveca candidate. This fixes the combinatorial meaning of biveca/triveca for the reconstructed 64-TG. It does not yet compute their lens volumes, centroids or covariance tensors; those are the next geometric integrals.

The full circumsphere centres, pair list and triple list are included in [the coordinate JSON](../data/64tg_fcc_coordinates.json), and regenerated/audited by the script and tests linked above.

## 7. Barycentres, covariance and gradient law

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
## 8. Phase, gradients and oscillations: a conditional dynamic bridge

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
The static reconstruction now supplies the coordinate list, tetrahedral incidence data, the 14 octahedra, 24 pyramids, and an oriented cell-boundary/volume certificate for the stated cuboctahedral partition. The remaining work is no longer to invent static coordinates, but to test source correspondence and extend the model dynamically: a differentiable Jitterbug path, a declared active-overlap rule, and (if an electromagnetic model is intended) an explicit coil/field coupling. These data can be integrated with T130's Q6 gradient/barycentre/moment framework. The reconstruction is a reproducible realization matching the source counts; it does not prove uniqueness or that Galeffi intended precisely this FCC/D3 realization, and it does not identify 64-TG with Q6, RGS, a bimetric spacetime or a cosmological model.

## 10. Status summary

| Claim | Status |
|---|---|
| Regular-solid volume identities in §2 | Exact arithmetic, conditional on stated counts and standard solids |
## 9. Bernoulli layer: keep it downstream

Bernoulli numbers/polynomials may enter after a discrete sampling rule has been defined—for example, when sums over a one-parameter family of layers or time steps are compared with an integral by Euler–Maclaurin. The paper's tentative Fibonacci labels do not by themselves define such a sampling rule. No Bernoulli coefficient, period or dynamical recurrence is inferred from the PDF.

## 10. Dynamic data still needed

The static coordinate and incidence data are now explicit. The standard 12-vertex Jitterbug path is independently reconstructed in `audits/jitterbug_gray_kinematics.py`, and the conditional one-panel coil attachment is implemented in `audits/jitterbug_coil_coupling.py`. This does not yet define a deformation of the 63-vertex FCC/D3 realization of the 64-TG. The remaining inputs for a genuinely moving 64-TG model are:
1. an explicit embedding of the 64-TG/FCC-D3 cells or selected subframework into the standard Jitterbug mechanism, including which vertices/bars/panels correspond;
2. a differentiable, closure-preserving motion of that embedded structure (the source PDF does not specify one);
3. if a physical/dynamical submodel is intended, a criterion selecting which of the 360 pairwise and 648 triple overlaps are physically active;
4. a phase field or transport law on the moving geometry.

The coordinates include exact tetrahedral, octahedral and pyramidal centroids and covariance tensors, face normals and all circumspheres. They can be integrated with T130's Q6 gradient/barycentre/moment framework and the existing Vesica records. The static reconstruction and the standard Jitterbug model do **not** by themselves identify the 64-TG with a bimetric spacetime or a cosmological model.

## 11. Electromechanical coupling: from Jitterbug motion to coil emf

The geometric parameter \(\gamma(t)\) and the radial face-centre distance
\[
V(t)=\sqrt{\frac{2}{3}}\,EL\cos\gamma(t)
\]
are kinematic quantities. They do not, by themselves, define a magnetic flux or an induced voltage. In particular, Gray's triangle-rotation angle \(\gamma\) is not automatically the angle between a coil normal and an applied magnetic field; the ellipse parameter \(\theta\) is a different angle, related by \(\tan\gamma=\sqrt3\tan\theta\).

For any specified coil surface \(S(t)\), with \(N\) turns and imposed magnetic field \(\mathbf B(\mathbf x,t)\), the flux linkage and transformer/motional emf are determined by
\[
\lambda(t)=N\int_{S(t)}\mathbf B(\mathbf x,t)\cdot d\mathbf S,
\qquad
\mathcal E(t)=-\frac{d\lambda}{dt}.
\]
This is the starting point. The coil mounting, its shape, the field and the mechanical map from the Jitterbug coordinates to the coil must be specified before the emf is determined.

### Model A: explicit coil attachment to one actual rigid Jitterbug panel

We now fix the mechanical map instead of identifying \(\gamma\) with a coil angle by assumption.

1. Choose the rigid triangular face labelled \(\varepsilon=(+1,+1,+1)\) in the standard Jitterbug. Its three labelled vertices in the reference configuration are \(p_0^0,p_1^0,p_2^0\), and their positions along the computed Jitterbug path are \(p_0(t),p_1(t),p_2(t)\).
2. Attach a circular \(N\)-turn coil rigidly and concentrically to that panel: its centre is the panel centroid, its plane is the panel plane, and its normal is the oriented unit panel normal \(n_0\) transported by the panel rotation. The circle is wholly inside the triangular panel when
   \[
   0<r<r_{\rm in}=\frac{a_J}{2\sqrt3},
   \]
   where \(a_J\) is the Jitterbug strut length.
3. Recover the panel's proper rotation \(R(t)\) from the three labelled vertex correspondences by the proper Kabsch fit. This determines the mechanical map without assuming a fixed rotation axis:
   \[
   p_j(t)-c(t)=R(t)(p_j^0-c^0),\qquad j=0,1,2.
   \]
   The coil normal is \(n(t)=R(t)n_0\). The panel-fit residual is also computed; it must be at numerical roundoff for a rigid panel.
4. Declare a uniform static field \(B\), coil area \(A=\pi r^2\), and a time law. The continuation parameter is pseudo-arclength \(s\); the reproducible example sets \(t=s/v_s\) with a declared constant traversal speed \(v_s\). This is an external clock choice, not a frequency predicted by Gray.

For this explicit attachment,
\[
\lambda(t)=NA\,\mathbf B\cdot R(t)n_0,
\qquad
\mathcal E(t)=-NA\,\mathbf B\cdot\bigl(\boldsymbol\omega(t)\times n(t)\bigr),
\]
where \(\boldsymbol\omega\) is the spatial angular velocity obtained from
\(\dot R R^T\). The implementation evaluates the SO(3) logarithm between consecutive panel poses and uses the midpoint angular velocity and normal, so the discrete emf is the Faraday derivative of the flux linkage to the order of the time discretization. The circuit current is obtained by the exact interval update for a piecewise-constant midpoint emf in the series RL equation.

The reproducible implementation is `audits/jitterbug_coil_coupling.py`; run it from the repository root with:

```bash
python3 audits/jitterbug_coil_coupling.py --output jitterbug_coil_report.json
python3 -m unittest discover -s tests -p 'test_jitterbug_coil_coupling.py' -v
```

Default illustrative parameters are \(a_J=0.1\,\mathrm m\), \(v_s=0.01\,\mathrm{m/s}\), \(N=100\), \(r=0.8r_{\rm in}\), \(\mathbf B=(0,0,0.1)\,\mathrm T\), \(R_c=10\,\Omega\), and \(\mathscr L_c=0.01\,\mathrm H\). These are declared example inputs, not measured apparatus parameters. The script records the full time series of flux linkage, emf and current, plus the maximum rigid-panel fit residual. The tests cover rigid-pose recovery, zero emf for a static panel, agreement with the analytic rotating-panel Faraday derivative, and the geometric coil-fit constraint.

The simpler formula \(\mathcal E=NBA\sin\gamma\,\dot\gamma\) remains only a special orientation/convention. It is not used as a substitute for the actual panel-pose reconstruction above.

### Model B: a coil whose radius is mechanically driven by the radial coordinate

As a separate illustrative coupling, suppose a circular coil remains normal to a uniform static field and a linkage imposes \(r(t)=kV(t)\), where \(k\) is a specified dimensionless mechanical scale factor. Then
\[
\lambda(t)=NB\pi k^2V(t)^2,
\qquad
\mathcal E(t)=-2\pi NBk^2V(t)\dot V(t).
\]
Using Gray's kinematic law,
\[
\dot V(t)=-\sqrt{\frac{2}{3}}\,EL\sin\gamma(t)\,\dot\gamma(t),
\]
so
\[
\mathcal E(t)=\frac{4\pi}{3}NBk^2(EL)^2
\sin\gamma(t)\cos\gamma(t)\,\dot\gamma(t).
\]
This formula belongs to the stated radius-linkage model, not to the unmodified Jitterbug mechanism.

For a lumped series circuit with resistance \(R_c\) and inductance \(\mathscr L_c\), the current then satisfies
\[
\mathscr L_c\frac{di}{dt}+R_ci=\mathcal E(t),
\]
with the sign fixed by the chosen loop orientation.

### Status and required inputs

Both models are conditional examples, not predictions of Gray's paper or of the 64-TG source. To turn either into a testable electromechanical model, specify: (i) the coil's attachment points and orientation on the mechanism; (ii) \(N,A\) or the complete moving surface; (iii) the imposed field and its spatial/time dependence; (iv) the map from the Jitterbug configuration to the coil pose/deformation; and (v) circuit resistance, inductance and measurement loading. A rigid translation of a closed coil in a spatially uniform static magnetic field does not, by itself, produce a net loop emf; deformation, rotation, field gradients or time dependence must be included.

**Classification:** the Gray law for \(V(\gamma)\) is a kinematic relation; the coil formulas above are conditional Faraday-law consequences once a mechanical/electromagnetic coupling is declared. No coil voltage is derived from the geometry alone.

## 12. Status summary

| Claim | Status |
|---|---|
| O3 / 64-TG static coordinate realization | Reconstructed as an explicit FCC/D3 model with exact coordinates and incidence certificate; not proved unique or source-authentic |
| FCC/D3 coordinate reconstruction: 63 vertices, 240 edges, 64 tetrahedra | Exact finite computation; matches all source counts |
| 56 tetrahedra + 14 octahedra + 24 pyramids partitioning the cuboctahedron | Exact coordinate/incidence and oriented-boundary/volume certificate |
| Regular-solid volume identities in §3 | Exact arithmetic, conditional on stated counts and standard solids |
| 8/15 packing fraction | Exact ratio of material volume to stated envelope volume |
| 144-face area = 18a² | **Incorrect** for 144 regular tetrahedron faces of edge a/2; correct value \(9\sqrt3a^2\) |
| Equal-area spherical partition and E=π/36 | Conditional; partition map not supplied |
| Octahedron insphere ratio equals φ | False for the standard inradius; only approximate |
| Pairwise circumsphere overlap as Vesica lens | Exact definition; actual 64-TG instances await coordinates |
| Pairwise circumsphere overlap as Vesica lens | Exact definition; 360 instances enumerated in the reconstructed FCC/D3 model |
| Triveca | Not uniquely defined by the source; requires a declared triple intersection/section |
| 360 pairwise circumsphere lenses / Vesica sections | Exact finite enumeration from the reconstructed 64 tetrahedra |
| 648 common triple circumball intersections / triveca candidates | Exact finite enumeration; two certified centre-triangle types |
| Barycentric Taylor/covariance law | Proved general local identity under stated regularity |
| Jitterbug phase/oscillation law | Open until a phase field/transport law is specified |
| One-panel coil coupling | Explicit conditional model; panel pose reconstructed from three vertices, Faraday emf and RL response implemented |
| Cosmological/bimetric interpretation | Not established by this geometric audit |

## References and internal links

- Galeffi, *On the 14-Octahedron Backbone of the Bimetric 64-Tetrahedron Grid Universe*, viXra:2412.0104 (source PDF in repository root: 2412.0104v1.pdf).
- Exact FCC/D3 coordinate dataset and audit script, linked above.
- [T130 — Q6 discrete gradients, barycentres, traction moments and resistance assembly](../theorems/T130-q6-discrete-gradients-barycentres-resistance.md).
- [T137 — Exact geometry of the Vesica Piscis and the sqrt(3) hexagonal chord](../theorems/T137-vesica-piscis-two-circle-hexagon-pi-sqrt3.md).
- [Vesica–Needham–Bonilla dossier](VESICA_NEEDHAM_BONILLA_SQRT3_PHI_DOSSIER_2026-11-18.md).
- [Integrated moments/barycentres/Morandotti synthesis](SYNTHESIS_MOMENTS_BARYCENTRES_GAMMA_BETA_ZETA_MORANDOTTI_2026-11-10.md).
