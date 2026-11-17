# T134 — Exact integration and finite-mesh trace certification

**Status: exact curved-P3 interval assembly is implemented; end-to-end finite-mesh certification is not yet demonstrated. The mesh-uniform trace bound remains open.**

This record separates three claims:

1. exact-rational enclosure of each local curved-cell/facet integral;
2. a finite-mesh rational certificate of \(C_\star D_h-H_{h,\ell}\succeq0\);
3. a mesh-uniform estimate over every refinement and every admissible mesh in the Gmsh family.

The local integral enclosures, global interval assembly, and interval-PSD machinery are implemented at source level. The second claim still requires a successful end-to-end execution on a specified mesh and a stored certificate. The third requires an independent analytic proof of the all-level geometric hypotheses.

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

**Kernel correction (2026-11-17).** The cellwise kernel of the physical Hessian on a mapped P3 cell is \(\operatorname{span}\{1,F_{K,1},F_{K,2}\}\), i.e. physical-affine functions on that cell. This does **not** imply that the kernel of the assembled \(D_h\) consists only of global physical affine functions. Globally, \(\ker D_h\) consists of C0 functions that are physical-affine cell by cell and whose traces agree across shared facets. On straight-sided facets, nonzero piecewise-affine hat functions can satisfy homogeneous boundary values, so \(D_h\) and \(H_{h,\ell}\) both have a common nontrivial kernel. Boundary P3 degrees of freedom are constrained to impose the stated homogeneous trace; interior vertex degrees of freedom remain free. The old statement that boundary conditions remove the global kernel of \(D_h\) was incorrect and is withdrawn. No C0-P1 quotient or interior-vertex elimination is used. The combined quantity \(D_h^2+J_{h,\ell}^2\), not \(D_h^2\) alone, has trivial kernel on a connected conforming mesh with the stated nondegenerate homogeneous boundary: zero normal-gradient jumps plus C0 continuity force matching full gradients, hence one global affine function, then zero.

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

## 5A. Preferred alternative: direct finite-mesh certificate for the IPDG form

For a fixed mesh, avoid the singular trace matrix and certify the assembled bilinear form itself. Let the global homogeneous-Dirichlet P3 basis be \(\{\phi_i\}_{i=1}^N\), after eliminating only boundary trace degrees of freedom. Assemble rational interval enclosures for three global blocks (two symmetric and one generally nonsymmetric):

- \(D_{ij}=\sum_K\int_K D^2\phi_i:D^2\phi_j\,dx\) (already implemented);
- \(P_{ij}=\sum_F\ell_F^{-1}\int_F j_F(\phi_i)j_F(\phi_j)\,ds\) (normal-gradient penalty block; to implement);
- \(C_{ij}=\sum_F\int_F q_F(\phi_i)j_F(\phi_j)\,ds\) (consistency coupling block; to implement, with the same arithmetic average and orientation conventions as the UFL form).

The boundary and interior contributions are assembled separately. On an interior facet, \(q_F\) is the arithmetic average of the two normal-normal Hessian traces and \(j_F\) is the sum of outward normal derivatives. On a boundary facet, use the one-sided traces. The global symmetric matrix of the stated form is
\[
A_{h,\ell}=D-C-C^T+\alpha P.
\]
All local entries must be enclosed rigorously; use exact rational Bernstein integration when the metric factors cancel to rational functions and the certified square-root segment integrator otherwise. Shared curved-facet traces, endpoint ordering, outward normals, and the exact \(\ell_F\) weights must be checked before accumulation.

For a stronger and scale-aware certificate, also assemble
\[
W_{h,\ell}=D+P,
\]
and seek a positive rational \(\kappa\) such that
\[
A_{h,\ell}-\kappa W_{h,\ell}\succ0.
\]
A successful interval certificate with a strict positive LDL factor after subtracting the full interval perturbation bound proves
\[
a_{h,\ell}(v,v)\ge\kappa\bigl(D_h(v)^2+J_{h,\ell}(v)^2\bigr)
\quad\forall v\in V_h^0
\]
on that **one fixed mesh**. It simultaneously avoids quotienting the common kernel of \(D_h\) and \(H_{h,\ell}\), and directly certifies coercivity in the natural mesh-dependent norm. A weaker alternative is strict positive definiteness of \(A_{h,\ell}\) in the chosen coefficient basis, but that only gives a basis- and mesh-dependent finite-dimensional lower bound.

The implementation should not reuse the current semidefinite LDL acceptance rule unchanged: require strictly positive pivots for the shifted matrix, and store \(\kappa\), the basis/DOF ordering, mesh and coordinate hashes, all interval radii, the perturbation bound, and the exact pivot diagnostics. A failed \(\kappa\) trial is inconclusive; decrease \(\kappa\) or tighten integration intervals. This finite-mesh result does not imply an all-level lower bound or prove that the T093 midpoint-refined family satisfies the curved-P3 Gmsh hypotheses.

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

## 6A. Interior-facet scaling correction (2026-11-17)

A source audit found that the first implementation of
`assemble_interior_facet_interval` formed the two-sided blocks from
\(q_A q_A\), \(q_A q_B\), and \(q_B q_B\), but omitted both the
penalty length \(h_F\) and the factor \(1/4\) coming from the arithmetic
average \(\{q\}=(q_A+q_B)/2\). Consequently, the assembled interior-facet
matrix was not the stated \(H_{h,\ell}\), and a PSD result from that version
would not certify the T134 trace inequality.

The implementation is corrected on branch
`t134-interior-facet-weight-fix`: all three blocks now include
\(h_F/4\), with \(h_F=(h_{K_A}+h_{K_B})/2\). A regression test compares
AA, AB, and BB against the corresponding single-side boundary Gram matrix
on an identical affine trace and checks the exact scaling. This is a
**source correction awaiting CI execution**, not a completed certificate.
Any prior finite-mesh PSD artifact produced by the uncorrected interior
facet assembly must be treated as invalid for T134 and must not be cited as
evidence for \(C_\star D_h-H_{h,\ell}\succeq0\).

## 7. Explicit theorem status

| Claim | Status |
|---|---|
| Exact P3 map reconstruction and Jacobian positivity for archived finite cells | Certified for the archived meshes |
| Rational interval integration of curved-P3 volume entries | Implemented; unit tests exist; end-to-end execution pending |
| Rational interval integration of curved boundary/interior facet entries | Implemented; unit tests exist; end-to-end execution pending |
| Sparse global interval assembly of \(D_h,H_{h,\ell}\) | Implemented at source level; end-to-end execution pending |
| Direct interval assembly of \\(A_{h,\\ell}=D-C-C^T+\\alpha P\\) and \\(W=D+P\\) | Proposed in §5A; not implemented |
| Fixed-mesh direct coercivity certificate \\(A_{h,\\ell}-\\kappa W\\succ0\\) | Proposed in §5A; not implemented |
| Exact interval PSD certificate for \\(C_\\star D_h-H_{h,\\ell}\\) on the full space | Obstructed when the common piecewise-affine kernel is present; an exact kernel complement is not implemented |
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
