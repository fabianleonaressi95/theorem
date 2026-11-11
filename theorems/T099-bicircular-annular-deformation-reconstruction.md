# T099 — Bicircular-annular deformation measurements

**Date:** 11 November 2026  
**Status:** exact lens geometry and affine reconstruction are proved by formula; the manufactured convergence and loop-closure checks are numerical verification. General recovery from finite annular samples is conditional on sampling geometry, regularity and identifiability. No physical constitutive law is claimed.  
**Dependencies:** T092 (local two-circle/Frank–Burgers bridge), T097 (barycentric–kinematic reconstruction), T098 (two-circle gradient/barycentre duality), T068–T070 (centroid and covariance identities).

## 1. Purpose and relation to the existing two-circle results

T098 already proves the equal-radius, centre-separation-equals-radius construction and its paired gradient/barycentre identities. T092 already supplies the local two-circle cell and the conditional (SE(2))/Cartan interpretation. T097 already defines a downstream barycentric–kinematic Frank–Burgers reconstruction.

T099 does not duplicate those results. It adds a measurement layer: unequal-radius lens geometry, annular sampling around both centres, least-squares recovery of a local deformation gradient, directional strain, and controlled loop-closure diagnostics.

The term *bicircular-annular* refers to the measurement geometry, not to a new physical substance or a universal constitutive equation.

## 2. Exact geometry of a general lens

Let (D_1,D_2subsetmathbb R^2) be disks of radii (R_1,R_2>0), with centres (O_1=(0,0)), (O_2=(d,0)). A proper lens exists exactly when
[
|R_1-R_2|<d<R_1+R_2.
]
The common-chord coordinate and half-length are
[
x_*={d^2+R_1^2-R_2^2over 2d},qquad
h=sqrt{R_1^2-x_*^2},qquad L=2h.
]
The lens area is
[
egin{aligned}
A={}&R_1^2arccos {d^2+R_1^2-R_2^2over2dR_1}
+R_2^2arccos {d^2+R_2^2-R_1^2over2dR_2}\
&-rac12sqrt{(-d+R_1+R_2)(d+R_1-R_2)
(d-R_1+R_2)(d+R_1+R_2)}.
end{aligned}
]
These are classical circle-intersection identities. The centroid lies on the line of centres by reflection symmetry. Its first coordinate is obtained from the one-dimensional cap integral
[
ar x={2over A}int_{d-R_2}^{R_1}
xmin{sqrt{R_1^2-x^2},sqrt{R_2^2-(x-d)^2}},dx,
]
with the integrand split at (x_*) and the integration limits intersected with the actual lens interval. The implementation uses Gauss–Legendre quadrature and checks the area against the closed formula.

For (R_1=R_2=d=R), (L=sqrt3R) and
[
A={R^2over6}(4pi-3sqrt3),qquad ar x=d/2.
]

## 3. Annular sampling and deformation recovery

For a sampling centre (c), radii (0le r_-<r_+), and angular/radial sample counts (N_	heta,N_r), define midpoint samples
[
x_{jk}=c+r_j(cos	heta_k,sin	heta_k),quad
r_j=r_-+(j+	frac12){r_+-r_-over N_r},quad
	heta_k={2pi kover N_	heta}.
]
Samples may be taken around both circle centres. For measured displacement values (u_i), fit
[
u_i=A_h(x_i-ar x)+ar u+	ext{residual}_i
]
by least squares. If the sample points span (mathbb R^2), the affine coefficient is uniquely determined by this least-squares problem. Set
[
F_h=I+A_h,qquad E_h={1over2}(F_h^TF_h-I).
]
The two eigenvalues of (E_h) are the principal Green–Lagrange strains. A convenient nonnegative planar anisotropy magnitude is
[
mathcal A_h=
sqrt{left({(E_h)_{11}-(E_h)_{22}over2}ight)^2+(E_h)_{12}^2}.
]
This is half the absolute difference of the two principal strains. It is not a material anisotropy coefficient.

**Identifiability boundary.** An arbitrary deformation field cannot be reconstructed from the two radii, centre separation, lens area and centroid alone. The reconstruction requires spatially distributed displacement or feature correspondences, a full-rank sample geometry, and a declared approximation class. A finite affine fit returns the best-fit affine component, not the exact pointwise gradient of a general nonlinear field.

## 4. Five reproducible checks

The audit runner implements:

- **E001 — classical vesica baseline:** verifies the common chord, closed-form area and symmetry centroid for (R_1=R_2=d=1).
- **E002 — asymmetric lens:** compares quadrature area and centroid computation for unequal radii with the exact lens-area formula.
- **E003 — affine anisotropy:** samples annuli around both centres and recovers a known nonsingular affine deformation and its Green strain.
- **E004 — annular gradient convergence:** uses a smooth manufactured cubic displacement field and checks that the annular least-squares gradient error decreases as the sampling radii shrink.
- **E005 — Frank/Burgers loop witness:** samples a prescribed (1/r) circulation field and checks polygonal loop-integral convergence to prescribed Frank and Burgers values.

E005 is a manufactured kinematic witness. It is not a dislocation solution of elasticity and does not establish a physical defect in a measured material.

## 5. Relation to dislocations, disclinations and Möbius geometry

The loop witness tests numerical circulation and rotational closure with explicit base-frame conventions. A physical Burgers vector or Frank angle requires a displacement/elastic-distortion field or a connection/coframe supplied by the model, plus the appropriate transport and cut conventions. It cannot be inferred from a scalar area residual or centroid displacement alone.

On a non-orientable surface, the construction must be expressed in local charts with transition maps; no global choice of (u^perp), signed area, or orientation is assumed. T098's planar reflection is a local Euclidean map and is not, by itself, a proof of a global Möbius transport law. A future extension must implement chart transitions and verify frame covariance around orientation-reversing loops.

## 6. Reproduction

From the repository root:
```bash
python scripts/run_bicircular_annular_audit.py --out artifacts/bicircular_annular_audit.json
python -m pytest -q tests/test_bicircular_annular_geometry.py
```

The script is NumPy-only beyond the Python standard library. Its output labels all results as a manufactured numerical audit.

## 7. Evidence classification

- **CLASSICAL / EXACT:** proper-lens condition, common-chord geometry, exact lens area, symmetry of the centroid.
- **PROVED FINITE-DIMENSIONAL:** uniqueness of the least-squares affine coefficient when the centred sample matrix has rank two.
- **NUMERICALLY VERIFIED:** the five manufactured checks, once the recorded script and tests pass.
- **CONDITIONAL:** recovery of a continuum deformation gradient from annular data under sampling-density, regularity and identifiability assumptions.
- **OPEN:** convergence for the actual RGS/Morandotti fields; anisotropic mesh refinement; non-orientable chart transport; physical constitutive interpretation.

**Classification:** measurement framework and candidate reconstruction law; not a universal physical law.  
**FLN**
