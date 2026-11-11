# Morandotti two-core anisotropy: operational definition

## Geometric frame

For core centres \(c_0,c_1\), define the preferred axis
\[
e_\parallel=\frac{c_1-c_0}{\lVert c_1-c_0\rVert},\qquad
e_\perp=(-e_{\parallel,y},e_{\parallel,x}),\qquad
Q=(e_\parallel,e_\perp).
\]
The present benchmark has two equal circular holes in a circular outer domain, but the pair selects a longitudinal direction. This is a geometric anisotropy of the two-core configuration, not an anisotropic constitutive material law.

## Interaction-matrix anisotropy

The six cell modes are ordered as \((c_0:0,x,y;c_1:0,x,y)\). For each 2-by-2 translational block \(B_{ij}\) of the Laplacian interaction matrix, resolve
\[
\widetilde B_{ij}=Q^T B_{ij}Q.
\]
The signed longitudinal/transverse contrast is
\[
A_{ij}=\frac{\widetilde B_{ij,\parallel\parallel}
-\widetilde B_{ij,\perp\perp}}
{|\widetilde B_{ij,\parallel\parallel}|
+|\widetilde B_{ij,\perp\perp}|},
\]
when the denominator is nonzero. Both mixed components are retained; they must not be silently discarded.

## Residual anisotropy

For each active core and each boundary component, let \(r_\parallel\) and \(r_\perp\) be the normal-derivative residuals for the translational modes resolved in the preferred frame. The implementation records these as longitudinal/transverse modes in the co-rotating frame, including for rotated configurations. Report
\[
A_r=\frac{r_\parallel^2-r_\perp^2}
{r_\parallel^2+r_\perp^2},
\]
and the ratio \(r_\parallel/r_\perp\) when defined. Scalar mode residuals remain separate.

## Core traction anisotropy

For each integrated core force \(F_k\), report its longitudinal and transverse projections and the signed contrast
\[
A_{F,k}=\frac{F_{k,\parallel}^2-F_{k,\perp}^2}
{F_{k,\parallel}^2+F_{k,\perp}^2}.
\]
The normal convention remains the outward normal of the material domain, pointing into the hole.

## Interpretation and falsifiability

These quantities make the proposed chain testable:
\[
\text{two-core geometry}\to\text{directional operator response}
\to\text{directional residuals and traction resultants}.
\]
They quantify correlation and directional structure; they do **not** prove that anisotropy is the unique cause of residuals. The implemented orientation audit performs two distinct sweeps at fixed mesh size: (A) rotate the core centres and Burgers vectors together; (B) rotate the core centres while keeping Burgers vectors fixed in laboratory coordinates. In each run, the translational cell modes, Frank–Burgers source components, and reported force components are expressed in the co-rotating longitudinal/transverse frame before solving or comparing. It compares the local interaction matrix, directional boundary residuals and core traction components. For an isotropic continuum model, sweep A should be covariant up to floating-point and finite-element geometry effects; angle-dependent remeshing noise is removed. Sweep B isolates the relative orientation of the dislocation source and the two-core axis; its traction response can therefore change even though the cell operator and its boundary residuals do not depend on the defect source. The sweep is a first controlled test, not a full causal proof: mesh refinement at every angle, residual normalization by boundary measure/field scale, and separation-parameter variation remain required.

The default orientation sweep uses 0°, 30° and 60° at a common mesh size, alongside the existing three-grid benchmark. The in-place rotation removes angle-dependent Gmsh remeshing differences, but finite-element discretization and curved-boundary geometry errors remain; a mesh/orientation convergence study is still required. The numerical audit is not a proof of asymptotic convergence, force equilibrium, or a material law. The report retains both laboratory-frame and local-frame defect vectors so the basis transformation is auditable. The Airy stress potential does not define a velocity field, so Kelvin circulation is not inferred from these diagnostics.
