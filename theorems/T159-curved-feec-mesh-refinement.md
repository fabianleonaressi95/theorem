# T159 — Mesh-refinement audit of the curved dodecahedral FEEC operator

**Date:** 27 November 2026  
**Classification:** finite numerical refinement study of the T158 interior-transport Whitney model.  
**Status:** structural, antipodal and quadrature checks pass on four meshes; observed spectral stabilization is not a proof of convergence.

## 1. What is refined

T149 supplies the 32–90–60 centroid-fan triangulation; T155 supplies the vesica-axis face-frame gauge and Gauss-map Levi-Civita transport; T157 extends the link connection to all nodes and records its curvature defect; T158 defines the piecewise-smooth normal map and path-transported Whitney masses inside each triangle.

T159 refines this same surface conformingly by a barycentric lattice of factor \(m\). On a parent triangle \(T=(v_0,v_1,v_2)\), refined vertices have coordinates
\[
x_{ijk}=\frac{k v_0+i v_1+j v_2}{m},\qquad i+j+k=m.
\]
The normal field is not re-fitted on each mesh. It is the restriction of the fixed T158 parent field
\[
n_T(\lambda)=
\frac{\lambda_0n_{v_0}+\lambda_1n_{v_1}+\lambda_2n_{v_2}}
{\|\lambda_0n_{v_0}+\lambda_1n_{v_1}+\lambda_2n_{v_2}\|},
\]
evaluated at each refined vertex and at the parent-barycentric coordinates of each quadrature point. Thus the geometry and connection being approximated are held fixed while the finite-element spaces are enriched.

The vesica axis \(a=(1,0,0)\) remains the preferred tangent-frame gauge. Where its tangent projection has norm below 0.5, the implementation switches to the Cartesian axis with smallest absolute dot product with the normal. This is a local gauge-chart switch, not a new connection; edge transports carry the transition. A single global smooth tangent frame on \(S^2\) is not assumed.

## 2. Refined cell counts

For each factor \(m\), every original triangle is divided into \(m^2\) triangles. The conforming global counts are:

| Factor \(m\) | Vertices | Edges | Triangles |
|---:|---:|---:|---:|
| 1 | 32 | 90 | 60 |
| 2 | 122 | 360 | 240 |
| 3 | 272 | 810 | 540 |
| 4 | 482 | 1,440 | 960 |

All four meshes have Euler characteristic 2. Shared-edge nodes are identified by their exact integer barycentric support keys. The parent normal map agrees from both sides of every shared coarse edge.

## 3. Refined covariant Whitney operator

The edge links are the minimal \(SO(3)\) rotations between refined nodal normals, projected into the local \(SO(2)\) frames. Inside each refined triangle, the path transport follows the T158 prescription: vertex-to-quadrature-point and quadrature-point-to-base-vertex along minor great-circle arcs, with the normal at the quadrature point evaluated from the fixed parent triangle.

The path-transported masses \(M_0^A,M_1^A,M_2^A\) use the T158 barycentric Whitney bases and Duffy-transformed tensor Gauss–Legendre quadrature. The scalar Hodge problem is
\[
K_0^A u=\lambda M_0^A u,\qquad
K_0^A=(D_0^A)^*M_1^A D_0^A.
\]
The covariant sequence remains curved:
\[
D_1^A D_0^A\ne0.
\]
The audit checks the exact T157 curvature-defect identity on every refined triangle. It does not impose a flat cochain-complex relation.

## 4. Spectral refinement results

The lowest generalized Hodge-0 eigenvalue is a triplet on all four meshes:

| \(m\) | Lowest eigenvalue, multiplicity 3 | Next triplet |
|---:|---:|---:|
| 1 | 2.2889673702 | 13.0228860324 |
| 2 | 2.3579348334 | 12.1475792989 |
| 3 | 2.3683065648 | 11.9630442067 |
| 4 | 2.3715586988 | 11.8957625698 |

The absolute increments of the first eigenvalue are
\[
6.8967463\times10^{-2},\quad
1.0371731\times10^{-2},\quad
3.2521341\times10^{-3}.
\]
The decreasing increments show numerical stabilization on these four meshes. They do **not** establish monotone convergence beyond the tested levels, identify a continuum limit, or prove an FEEC error estimate.

The factor-2 mass quadrature comparison (orders 8 and 12) gives relative Frobenius residuals
\[
\|M_0^{(12)}-M_0^{(8)}\|_F/\|M_0^{(12)}\|_F
=1.62\times10^{-15},
\]
\[
\|M_1^{(12)}-M_1^{(8)}\|_F/\|M_1^{(12)}\|_F
=5.89\times10^{-16}.
\]

The first refined Hodge eigenvalue remains approximately 2.372, not 4 or 6. This refinement therefore does not produce the Q6 selected spectrum \((0,4,6)\), and does not derive
\[
f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}.
\]
No Q6 intertwiner is asserted for the newly introduced refined nodes.

## 5. Structural and geometric checks

Across all four meshes:
- the normal field is continuous across shared coarse edges;
- the refined antipodal node map is an involution;
- antipodal normal residuals are below \(2.3\times10^{-16}\);
- antipodal link-covariance residuals are below \(9.1\times10^{-16}\);
- the curvature-defect identity residual is below \(1.1\times10^{-14}\);
- the holonomy sum is \(4\pi\), with residual below \(1.8\times10^{-15}\);
- each triangle holonomy agrees with its oriented spherical Gauss-map area to below \(3.3\times10^{-16}\);
- \(M_0^A\) and \(M_1^A\) pass Cholesky positive-definiteness checks, and \(M_2^A\) has positive diagonal entries.

The vesica-axis chart fallback is used at 4, 14, 28 and 62 nodes for \(m=1,2,3,4\), respectively. The minimum tangent-frame projection after chart selection is at least 0.5067.

## 6. Scientific status and remaining gates

**Numerically verified:** conforming mesh counts, parent-map consistency, positive Whitney masses, quadrature agreement, antipodal covariance, Gauss-map holonomy, curvature identity, and stabilization of the lowest Hodge-0 eigenvalue over four refinement levels.

**Still open:** the local covariant Whitney consistency/commuting defect \(\mathfrak C_{h,T}=\nabla^A I_{h,T}^0-I_{h,T}^1D_0^A\), including derivatives of the path-transport factors; a rigorous spectral-convergence theorem for this piecewise-smooth connection; a curved-FEEC approximation/error estimate; convergence of the complete Hodge spectra and eigenspaces; a compatible refined Q6/RGS chain map; and any first-principles derivation of \(f\).

The current four-level stabilization study does not estimate the covariant Whitney consistency defect. The correct conclusion is a finite refinement study, not a continuum theorem. The observed eigenvalue sequence is a useful target for a future convergence proof, while the mismatch with \((0,4,6)\) remains explicit.

## 7. Reproduction

~~~bash
python scripts/audit_t159_curved_feec_refinement.py
python -m unittest tests.test_t159_curved_feec_refinement
~~~

The JSON report is written to results/json/t159_curved_feec_refinement.json.
