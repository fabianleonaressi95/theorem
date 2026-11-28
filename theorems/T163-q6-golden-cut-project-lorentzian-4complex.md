# T163 — Explicit 6D-to-Lorentzian-4D Q6 cut-and-project complex

**Status:** exact finite-dimensional frame construction and combinatorial incidence audit; affine gradient patch numerically verified by an independent calculation. The resulting object is a **branched Lorentzian 4-complex, not a 4-manifold**. Its role as a continuum spacetime remains OPEN.

## 1. Golden 6D frame

Use the T161 golden orthogonal decomposition
[
P_parallel P_parallel^T=I_3,quad
P_perp P_perp^T=I_3,quad
P_parallel P_perp^T=0.
]
To obtain four coordinates, select a unit internal direction by a reproducible nondegeneracy rule. Among primitive positive integer triples (c=(c_1,c_2,c_3)), ordered by increasing (c_1+c_2+c_3) and then lexicographically, choose the first for which every (4	imes4) coordinate minor below is nonzero. The selected vector is
[
c=(1,1,2),qquad widehat c=c/sqrt6.
]
Define
[
Pi_4=
egin{pmatrix}
widehat c^{,T}P_perp\
P_parallel
end{pmatrix}inmathbb R^{4	imes6},
qquad
Pi_4Pi_4^T=I_4.
]
For (qin{0,1}^6), the projected coordinates are
[
X_4(q)=Pi_4(q-	frac12mathbf1).
]
The first coordinate is selected from the internal space and is declared the time coordinate; the other three are the T161 physical coordinates. Assign
[
eta=operatorname{diag}(1,-1,-1,-1).
]
This is an explicit signature choice. The internal time direction is not claimed to be uniquely selected by the Q6 graph or by the field equations; it breaks the residual internal rotational symmetry.

All fifteen (4	imes4) minors of (Pi_4) are nonzero. The minimum absolute minor is
[
min_{|I|=4}|det(Pi_4[:,I])|
=0.021549959396876144.
]
Thus every coordinate 4-face has a nondegenerate affine image in (mathbb R^{1,3}).

## 2. The 4-dimensional cubical skeleton

The 4-faces of the six-cube are indexed by four free bit axes and two fixed bits. Their number is
[
inom64,2^2=60.
]
The 3-faces number
[
inom63,2^3=160.
]
Every 3-face is contained in exactly three coordinate 4-faces: there are three remaining axes that can be released to form a 4-face. Hence the facet-incidence multiset is exactly ({3}), not ({2}).

**Conclusion:** the projected 4-skeleton is a branched 4-complex. It is not a 4-manifold and cannot yet be used as a smooth Lorentzian spacetime without a further resolution, quotient, or gluing rule. This is a precise obstruction, not a defect to be hidden by assigning arbitrary weights.

## 3. Conforming simplicial refinement

Each coordinate 4-cube is split by the Freudenthal construction, using the global order of its four free axes. This gives (4!=24) 4-simplices per cell:
[
N_{	ext{4-simplices}}=60cdot24=1440.
]
The global axis ordering makes the induced triangulation agree on common coordinate faces. Every projected 4-simplex is nondegenerate. For the selected frame, the numerical 4-simplex volume range is
[
8.979149748698394	imes10^{-4}
leq V_sigmaleq
1.84632023843412	imes10^{-2}.
]
The Lorentzian Gram determinant of every 4-simplex is nonzero, since for its edge matrix (J_sigma),
[
det(J_sigma^Teta J_sigma)
=det(eta)det(J_sigma)^2
=-det(J_sigma)^2
e0.
]

## 4. Four-dimensional gradient and barycentric covariance

For each Q6 vertex, use all six projected edge vectors (d_{vw}=X_4(w)-X_4(v)) and the positive auxiliary Euclidean chart norm to define
[
G_v^{(4)}=sum_{wsim v}rac{d_{vw}d_{vw}^T}{d_{vw}^Td_{vw}},
qquad
b_v^{(4)}=sum_{wsim v}
rac{d_{vw}(f_w-f_v)}{d_{vw}^Td_{vw}},
qquad

abla_{Q6}^{(4)}f(v)=(G_v^{(4)})^{-1}b_v^{(4)}.
]
All six-star Gram matrices have rank four. The maximum condition number for this frame is (1.6535736014956326).

On each nondegenerate 4-simplex (sigma=(v_0,ldots,v_4)), the affine P1 gradient is the unique solution
[
J_sigma^T
abla_sigma^{P1}f
=(f_{v_1}-f_{v_0},ldots,f_{v_4}-f_{v_0})^T,
quad
J_sigma=[X_4(v_1)-X_4(v_0) cdots X_4(v_4)-X_4(v_0)].
]
Project these cell gradients to vertices by 4-volume-weighted averaging. For every affine field (f(X)=a_mu X^mu+c), both operators reproduce (a) exactly in exact arithmetic. The independent numerical reconstruction gives maximum operator residual (1.07	imes10^{-14}).

For a uniform 4-simplex, the normalized barycentric covariance is
[
Sigma_sigma=rac1{30}
sum_{i=0}^4(X_i-c_sigma)(X_i-c_sigma)^T,
qquad c_sigma=rac15sum_iX_i.
]
This is the four-dimensional T068 moment identity; it is not the 2D triangle covariance.

For a declared non-affine parity field (f_v=(-1)^{|v|_1}(1+v/64)), the maximum difference between the six-neighbour Q6 gradient and the volume-averaged P1 gradient is (8.656580124566762). This is a finite operator mismatch diagnostic, not a convergence error bound.

## 5. Relation to Cartan and Sakharov

This construction supplies a concrete 4D affine cell carrier on which one can now place:
- vertex coframes (e^a{}_mu) and independent edge transports (L_{vw}in SO^+(1,3));
- discrete torsion and curvature using the already established Cartan edge/face transport conventions;
- a cellwise Palatini–Cartan action with contributions from all incident branches;
- a Dirac-type operator and its heat trace only after a spin lift and consistent treatment of the branched links are specified.

It does **not** yet supply the branch matching conditions, discrete Palatini variations, a 4D spin structure, a self-adjoint Dirac operator, heat-kernel coefficients, or a continuum limit. In particular, no new (G_{m ind}) or Sakharov coefficient is claimed.

## 6. Reproduction

- `audits/q6_lorentzian_4d_cut_project.py`
- `tests/test_q6_lorentzian_4d_cut_project.py`

The audit reports frame orthogonality, all 4-face minors, 4-cell/3-face counts, Freudenthal simplex volumes, facet incidence, 4D star conditioning, affine patch residual, and non-affine operator mismatch.

## 7. Evidence classification

- **PROVED by finite algebra:** row orthogonality of the selected frame; 60/160 cell counts; incidence three for every 3-face; 24-simplex Freudenthal count per 4-cell; conditional affine patch identity.
- **NUMERICALLY AUDITED:** nonzero minors, simplex volumes, Lorentzian Gram determinants, local gradient conditioning and the stated residuals. CI remains a separate status.
- **OPEN:** physical derivation of the internal time direction; resolution of the three-way branch incidence into a Lorentzian 4-manifold (if a manifold is required); PSU–Anti-Twin throat gluing on this complex; discrete Cartan field equations; spinorial transport; spectral convergence and Sakharov induced gravity.


**Additional geometric limitation.** The nonzero (4\times4) minors prove that each individual coordinate 4-face has a nondegenerate affine image. They do not prove that distinct projected 4-cells intersect only along their prescribed common faces, nor that the global projection is injective. Pairwise projected-cell intersection and overlap audits are still required before treating the image as a geometric CW embedding.
