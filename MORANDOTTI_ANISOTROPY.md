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


## Core-separation sweep

The distance experiment uses a single reference triangulation at separation
\(d_0=0.56\). For each target separation, the same mesh coordinates are
smoothly deformed with compactly supported Wendland-C2 radial weights centred
on the two reference cores. The weights are normalized to one at the core
radius and vanish outside a support radius of 0.32. Core-boundary nodes
therefore follow the prescribed centres, while the outer boundary remains
fixed for the tested separations. Cell connectivity is never regenerated.

The initial sweep uses \(d\in\{0.48,0.56,0.64,0.72\}\), with core radius
\(a=0.12\), material parameters unchanged, and the same laboratory-fixed
Frank/Burgers data. It records the free edge gap \(g=d-2a\), the longitudinal
and transverse entries of the off-diagonal interaction block \(M_{01}\),
\[
A(d)=\frac{M_{\parallel}(d)-M_{\perp}(d)}
{|M_{\parallel}(d)|+|M_{\perp}(d)|},\qquad
C(d)=\frac{\|M_{01}(d)\|_F}{\|M_{00}(d)\|_F},
\]
the mixed longitudinal/transverse entries, and core traction resultants for
each defect case. The report also records the minimum signed area of the
linear corner triangles after coordinate deformation and aborts if an
inversion is detected.

This first distance sweep is a numerical screening study at one mesh size
(default \(h=0.06\)); the existing three-mesh benchmark remains available at
the reference separation. A trend in \(A(d)\) or \(C(d)\) is not yet a
continuum distance law. Before fitting exponential, algebraic or limiting
models, repeat the distance sweep at multiple mesh resolutions and inspect
curved-element Jacobians, not only corner-triangle areas. No decay law is
assumed in advance.


### Reproduction command

Run the reference benchmark and the default distance sweep in the DOLFINx 0.11 environment with:

```bash
python3 scripts/rgs_morandotti_two_core_c0_ipdg.py \
  --mesh-sizes 0.08 0.06 0.045 \
  --orientation-angles-deg 0 30 60 \
  --distance-values 0.48 0.56 0.64 0.72 \
  --distance-mesh-size 0.06 \
  --out artifacts/morandotti_two_core/report.json
```
