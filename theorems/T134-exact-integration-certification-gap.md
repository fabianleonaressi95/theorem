# T134 — Exact integration and finite-mesh trace certification

**Status: exact curved-P3 interval assembly is implemented; end-to-end finite-mesh certification is not yet demonstrated. The mesh-uniform trace bound remains open.**

This record separates three claims:

1. exact-rational enclosure of each local curved-cell/facet integral;
2. a finite-mesh rational certificate of \(C_\star D_h-H_{h,\ell}\succeq0\);
3. a mesh-uniform estimate over every refinement and every admissible mesh in the Gmsh family.

Only the first is currently implemented at source level. The second still requires a successful end-to-end execution on a specified mesh and a stored certificate. The third requires an independent analytic proof of the all-level geometric hypotheses.

## 1. Target inequality and admissible space

For the globally continuous mapped-P3 space with homogeneous physical Dirichlet trace on every boundary component, define
\[
D_h(v)^2=\sum_K\int_K |D_x^2v|^2\,dx,
\qquad
H_{h,\ell}(v)^2=\sum_{F\in\mathcal F_h^i}\ell_F
\int_F\left|\{n_F^TD_x^2v\,n_F\}\right|^2ds
+\sum_{F\in\mathcal F_h^b}\ell_F
\int_F|n^TD_x^2v\,n|^2ds.
\]
The finite-mesh objective is to certify, for a rational \(C_\star<20\),
\[
C_\star D_h-H_{h,\ell}\succeq0
\]
on the full homogeneous-Dirichlet P3 space. Such a certificate implies \(C_{\mathrm{tr},h}\le C_\star<20\), and hence the sufficient C⁰-IPDG condition \(\alpha=40>2C_\star\) for that mesh.

**Kernel correction (2026-11-13).** On a curved isoparametric mesh, reference C⁰-P1 functions are not generally affine in physical coordinates and are not the kernel of the physical Hessian. The common zero-Hessian modes are global physical affine functions. Homogeneous trace on the full nondegenerate boundary eliminates those modes. Therefore the admissible matrix space constrains boundary P3 degrees of freedom only; interior vertex degrees of freedom must remain free. Both the exact assembler and the floating-point diagnostic have been corrected accordingly. No C⁰-P1 quotient or interior-vertex elimination is used.

## 2. Exact local volume integration

For a cubic map \(F_K:\widehat K\to K\), the physical Hessian of a mapped basis function is represented as
\[
D_x^2\phi_i=\frac{P_i}{(\det J_K)^3},
\]
where \(P_i\) is a matrix of rational-coefficient polynomials when the stored binary64 geometry coordinates are interpreted as exact dyadic rationals. Since \(dx=(\det J_K)d\hat x\), the volume Gram entry is
\[
(D_K)_{ij}=\int_{\widehat K}
\frac{P_i:P_j}{(\det J_K)^5}\,d\hat x.
\]
The module models/morandotti_certified_curved_p3_forms.py reconstructs the P3 map and basis over Fraction, differentiates the polynomials exactly, and calls integrate_rational_triangle for every symmetric local matrix entry.

The rational triangle integrator:
- composes numerator and denominator onto rational subtriangles;
- obtains exact Bernstein coefficient bounds;
- certifies strict denominator positivity before division;
- uses exact polynomial moments in a rational Neumann expansion when the numerator has a certified sign;
- bounds the geometric-series remainder rationally, subdividing when needed;
- returns rational lower/upper endpoints or raises if positivity or the requested width is not certified.

No floating-point quadrature value is used as an integration certificate.

## 3. Exact curved-facet integration

For a reference edge parameter \(t\), let
\[
s(t)=|F'_K(t)|^2.
\]
The unnormalised physical normal is polynomial and the unit normal introduces \(s^{-1/2}\). Combining two normal-normal Hessian traces with the arclength element \(ds=\sqrt{s(t)}dt\) yields an integrand of the form
\[
\frac{p(t)}{q(t)\,s(t)^{3/2}},
\]
with rational polynomial \(p,q,s\). The implementation integrate_rational_sqrt_segment encloses this expression by exact-rational Bernstein bounds and a certified positive arclength radicand.

For interior facets, the two adjacent cubic maps must have exactly matching physical edge traces. The assembler checks this coefficient-by-coefficient, uses the common edge metric, and forms the two-sided average blocks \(AA,AB,BB\) with the factor \(1/4\) from the arithmetic average. Boundary and interior facet blocks are then accumulated into sparse global interval matrices.

## 4. Interval propagation to a matrix certificate

The global assembler produces symmetric rational intervals for every nonzero entry of \(D_h\) and \(H_{h,\ell}\). For a proposed rational \(C_\star\), it forms entrywise intervals for \(M=C_\star D_h-H_{h,\ell}\).

certify_interval_psd computes the exact rational midpoint matrix and an upper bound on the spectral norm of the symmetric interval perturbation using the maximum row sum of entry radii. It subtracts this perturbation bound from the midpoint diagonal and applies sparse exact-rational Schur/LDL elimination. Successful nonnegative pivots certify that every symmetric matrix in the input interval enclosure is positive semidefinite.

This is a sufficient certificate and may fail when the integration intervals are too wide or the chosen \(C_\star\) is too small. Such a failure is not evidence that the target inequality is false; it means this enclosure did not prove it.

## 5. DOLFINx adapter and remaining execution gate

assemble_dolfinx_mesh_interval_forms extracts the serial planar triangular P3 geometry, solution dofs, cell diameters, boundary facets, and paired interior facets. It checks the equispaced coordinate map, the scalar P3 solution family/degree, nodal interpolation identity, and correspondence of reference nodes. It then invokes the exact local/global assemblers.

The DOLFINx adapter has recently been corrected to use the public CoordinateElement.variant property rather than a nonexistent cmap.basix_element, and to inspect the solution element's interpolation matrix rather than a nonexistent FiniteElement.variant. These API corrections have **not** yet been validated by a successful end-to-end CI run. Do not mark the finite-mesh certificate complete until the adapter executes on the supported DOLFINx/Basix versions and writes a reproducible certificate.

The next execution gate is:
1. run the focused exact-integration and curved-form unit tests;
2. run scripts/certify_morandotti_curved_p3_mesh.py on one small, fixed curved-P3 mesh;
3. require all cell Jacobians to be certified positive;
4. certify \(C_\star D_h-H_{h,\ell}\succeq0\) for a stated rational \(C_\star<20\);
5. store the mesh identity, coordinate hash, integration tolerance, subdivision limits, interval/LDL diagnostics, and final certificate in the report.

A failed or inconclusive run must be reported as such; it must not be replaced by the floating-point generalized eigenvalue estimate.

## 6. What the existing finite-mesh audit establishes

The 24-mesh diagnostic reported generalized-eigenvalue estimates in the range 9.1545269506–15.8151565222, with the largest observed sufficient threshold \(2C_{\mathrm{tr},h}=31.6303130444\). Thus \(\alpha=40\) cleared the observed floating-point thresholds in those 24 cases. Exact-rational Bernstein subdivision also certified positive Jacobians for all 145,256 archived cell maps.

The quadrature-degree 32/40 agreement (relative difference at most \(1.71\times10^{-13}\)) is a numerical stability diagnostic only. It is not an interval integration certificate and does not establish the matrix inequality.

## 7. Explicit theorem status

| Claim | Status |
|---|---|
| Exact P3 map reconstruction and Jacobian positivity for archived finite cells | Certified for the archived meshes |
| Rational interval integration of curved-P3 volume entries | Implemented; unit tests exist; end-to-end execution pending |
| Rational interval integration of curved boundary/interior facet entries | Implemented; unit tests exist; end-to-end execution pending |
| Sparse global interval assembly of \(D_h,H_{h,\ell}\) | Implemented at source level; end-to-end execution pending |
| Exact interval PSD certificate for \(C_\star D_h-H_{h,\ell}\) | Primitive implemented; no successful mesh certificate yet |
| Finite-mesh \(C_{\mathrm{tr},h}<20\) | Not established |
| Uniform \(C_{\mathrm{tr}}<20\) over all Gmsh refinements/seeds | Open |
| Uniform coercivity with \(\alpha=40\) for the actual Gmsh family | Not established |

A finite-mesh certificate, once obtained, is specific to that mesh. A mesh-uniform theorem additionally requires a single compact admissible class of normalized element maps, uniform positive Jacobian and derivative/inverse-derivative bounds, and uniform facet/neighboring-cell comparability for every refinement and allowed seed. The finite archive cannot prove those all-level hypotheses.

## 8. Scope discipline

Do not:
- call quadrature convergence exact integration;
- infer a rigorous upper bound from a floating-point generalized eigenvalue;
- constrain interior vertices as a proxy for quotienting by physical affine functions;
- infer a mesh-uniform estimate from finitely many mesh certificates;
- promote \(\alpha=40\) to a theorem-level threshold before the required rational matrix certificate and all-level geometric hypotheses are proved.

**Classification:** T134 remains a conditional coercivity theorem. Exact-rational local form certification is an implemented verification method, not yet a completed finite-mesh certificate. The unconditional statement for the actual Gmsh family remains open.
