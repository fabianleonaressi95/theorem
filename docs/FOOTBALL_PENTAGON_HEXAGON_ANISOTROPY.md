# Pentagon–hexagon anisotropy in a pressurised football

**Research strand:** RGS–PRISM / Morandotti  
**Implementation:** \`models/football_anisotropy.py\`  
**Runner:** \`scripts/run_football_anisotropy_audit.py\`  
**Status:** finite geometry exact; linear panel-network model numerically verified; constitutive and experimental validation open.

## 1. Geometric object

The ideal 32-panel football is the truncated icosahedron. Its combinatorics are

\[
(V,F_5,F_6,E)=(60,12,20,90).
\]

Its panel-adjacency graph has 90 links: 60 pentagon–hexagon and 30 hexagon–hexagon; no two pentagons share an edge. The script constructs the geometry from the icosahedron by directed-edge truncation, rather than hard-coding a drawing.

The construction and incidence counts are exact finite combinatorial checks (up to floating-point coordinate construction). The familiar count follows from the truncation: each of the 30 icosahedral edges yields two directed truncated vertices, each original vertex yields one pentagon, and each original triangular face yields one hexagon.

## 2. Coarse-grained mechanical model

A scalar \(q_i\) is assigned to each panel and represents the normal displacement of its representative patch centre. Let \(A_i\) be the panel area, \(C_i=C_5\) on pentagons and \(C_i=C_6\) on hexagons, and let \(\ell_{ij}\) be the length of a shared panel edge. The implemented energy is

\[
E(q)=\frac12\sum_i C_i A_iq_i^2
+\frac{\gamma}{2}\sum_{(i,j)\in\mathcal E_P}
\ell_{ij}(q_i-q_j)^2
-p\sum_i A_iq_i .
\]

Here \(p\) is a uniform pressure-like load and \(\gamma\geq0\) couples neighbouring patch displacements. The equilibrium is the unique solution of

\[
Kq=f,\qquad
K=\operatorname{diag}(C_iA_i)+\gamma L_{\ell},
\qquad f_i=pA_i,
\]

where \(L_\ell\) is the weighted graph Laplacian of the panel-adjacency graph. Since \(C_iA_i>0\) and \(L_\ell\) is positive semidefinite, \(K\) is positive definite. Thus the linear system has a unique minimizer.

The parameters \(C_5,C_6,\gamma\) are effective model parameters. They are not measured material constants and must not be interpreted as measured differences between real pentagonal and hexagonal panels.

## 3. What the audit measures

The representative panel centre \(c_i\) and outward normal \(n_i\) are moved to

\[
c_i'=c_i+q_i n_i.
\]

The report computes the radial increment

\[
\Delta r_i=\|c_i'\|-\|c_i\|
\]

and its panel-area-weighted RMS variation

\[
A_{\rm patch}=
\left[
\frac{\sum_i A_i(\Delta r_i-\overline{\Delta r})^2}
{\sum_i A_i}
\right]^{1/2}.
\]

This is a **patch-sampled anisotropy diagnostic**, not a certified continuum sphericity measure. It deliberately subtracts the undeformed panel-centre radii, so the isotropic control \(C_5=C_6=C\) gives \(q_i=p/C\) and zero incremental anisotropy to numerical precision.

## 4. Geometric transformations and continuum extension

For a smooth radial interpolation \(u(\theta,\phi)\) on a reference sphere of radius \(R\), the radial-graph transformation is

\[
X(\theta,\phi)=(R+u(\theta,\phi))\,n(\theta,\phi).
\]

The induced metric is

\[
g'_{ab}=(R+u)^2\gamma_{ab}
+\partial_a u\,\partial_b u,
\]

where \(\gamma\) is the unit-sphere metric. This gives the exact geometric route from a scalar radial deformation to a changed metric. In the present implementation only the patch-centre values \(q_i\) are solved; no smooth interpolant, metric tensor, Gaussian curvature field, or continuum shell equation is claimed to have been computed. A subsequent model must add compatible panel-corner or shell finite-element degrees of freedom before reporting those quantities.

The panel network is equivariant under automorphisms preserving panel type and edge weights. A perfectly symmetric input and equal constitutive parameters preserve the corresponding symmetry in the solution. A pentagon/hexagon material contrast changes the two panel-orbit responses while retaining the ideal combinatorial pattern. Manufacturing asymmetry, seams, textile anisotropy, local reinforcement, and nonuniform pressure can break further symmetries and require measured inputs.

## 5. Reproducible baseline

Run from the repository root:

\`\`\`bash
python scripts/run_football_anisotropy_audit.py \\
  --pressure 0.01 --C5 1.25 --C6 1.0 --coupling 0.15 \\
  --json reports/football_anisotropy_audit.json \\
  --svg reports/football_anisotropy_displacement.svg
python -m pytest -q tests/test_football_anisotropy.py
\`\`\`

The runner records a five-point \(C_5/C_6\) sensitivity sweep, linear-system residuals, the isotropic control, package version, command line, and a vector SVG of panel displacements.

The baseline is dimensionless/model-unit data. It is a demonstration that a declared constitutive contrast produces different pentagonal and hexagonal patch responses in this chosen coarse model. It is **not** evidence that a real football has \(C_5/C_6=1.25\), nor that the measured ball shape is explained quantitatively.

## 6. Evidence status and next obligations

| Claim | Status |
|---|---|
| Truncated-icosahedron panel counts and adjacency counts | Exact finite combinatorics; tested |
| Positive definiteness and unique linear minimizer for \(C_5,C_6>0\), \(\gamma\geq0\) | Follows from the displayed energy |
| Numerical solution and residual for the baseline | Numerically verified by tests and JSON report |
| Pentagon-to-hexagon stress transfer in an actual ball | Not yet experimentally validated |
| Nonlinear membrane/shell mechanics, seams, textile orthotropy, contact and large inflation | Not implemented |
| Induced continuum metric and curvature of the deformed ball | Formula specified; not computed by this coarse model |
| Quantitative prediction of real-ball non-sphericity | Open; requires geometry scans and material/seam data |

Next research step: replace patch-centre scalar variables with a conforming shell or finite-element discretisation, identify material and seam constitutive laws, calibrate them on coupons, then compare predicted shape and strain fields with 3D scans and pressure-controlled experiments. This is the point at which the Morandotti collaboration can test whether the pentagonal constraints explain the observed departure from spherical shape.

## 7. Bibliographic positioning

This implementation is a new coarse-grained audit, not a claim of priority for modelling soccer-ball mechanics. The literature already contains finite-element treatments of pressurised football structures and material/seam effects. The prospective contribution here is the explicit separation of panel topology, panel-orbit constitutive contrast, graph coupling, and the induced radial-geometry diagnostic in the RGS–PRISM research programme. Bibliographic records should be added only after exact source metadata and the specific comparison being made have been independently checked.
