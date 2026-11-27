# T157 — Full 32–90–60 link-covariant Whitney model with curvature defect

**Date:** 27 November 2026  
**Classification:** explicit discrete geometric connection; exact algebraic curvature identity; numerical covariant Whitney mass/Hodge audit.  
**Status:** the T155 connection is extended to all 32 centroid-fan nodes and 90 edges. The 60 face holonomies reproduce the spherical Gauss-map areas and sum to (4\pi). The covariant derivative sequence is deliberately **not** a cochain complex: its composition is the nonzero curvature defect. This is a finite link-based model, not yet a theorem identifying it with a smooth continuum connection.

## 1. Scope and geometric choice

T149 supplies the oriented centroid-fan triangulation
\[
(N_0,N_1,N_2)=(32,90,60),\qquad \chi=32-90+60=2.
\]
The 20 original dodecahedral vertices and 12 pentagon centroids are retained. The 12 centroid nodes are the same Gauss-map fibres used by T155.

The extension needs a normal at each of the 20 original vertices. We choose the area-weighted discrete normal
\[
\boxed{
n_v=\frac{\sum_{T\ni v}|T|\,n_T}
{\left\|\sum_{T\ni v}|T|\,n_T\right\|},
}
\]
where (n_T) is the outward unit normal of triangle (T). This is an explicit, antipodally symmetric geometric choice; it is not asserted to be the unique possible nodal-normal convention. At a face-centroid node the five incident triangles are coplanar, so this formula returns exactly the polar-face normal (v_i/\|v_i\|) of T155.

At all 32 nodes choose the same vesica-axis gauge:
\[
e_{1,v}=\frac{a-(a\cdot n_v)n_v}{\|a-(a\cdot n_v)n_v\|},
\qquad e_{2,v}=n_v\times e_{1,v},\qquad a=(1,0,0).
\]
The projection norm is checked to stay away from zero in both geometries. This is a gauge convention, not a physical preferred direction.

## 2. Connection on all 90 edges

For every oriented edge (i\to j), let (R_{ij}\in SO(3)) be the minimal rotation carrying (n_i) to (n_j). With (v=n_i\times n_j), (s=\|v\|), (c=n_i\cdot n_j), and (K=[v]_\times),
\[
R_{ij}=I+K+\frac{1-c}{s^2}K^2.
\]
For (F_i=(e_{1,i},e_{2,i})), define
\[
T_{ij}=F_j^T R_{ij}F_i\in SO(2),\qquad
U_{ij}=(T_{ij})_{11}+i(T_{ij})_{21}.
\]
Then (U_{ji}=\overline{U_{ij}}). The 90 links are built from the geometry, without fitted phases or spectral weights.

**Compatibility with T155.** On the 12 centroid fibres, the nodal normals equal the T155 Gauss-map normals. Recomputing all 30 T155 face-graph transports from these same frames gives the same links to numerical precision. Those 30 face-graph links are an additional adjacency set on the 12-centre subset; they are not falsely identified with centroid-centroid edges of the 32–90–60 triangulation.

## 3. Curvature-aware covariant differences

A vertex cochain (u_i) takes values in the complex line at node (i). For an oriented edge, the covariant difference is stored in the fibre at its endpoint:
\[
(D_0^A u)_{ij}=u_j-U_{ij}u_i.
\]
For an oriented triangle ((i,j,k)), edge values are transported to the base fibre at (i):
\[
(D_1^A c)_{ijk}
=U_{ji}c_{ij}+U_{ki}c_{jk}+c_{ki}.
\]
Orientation reversal is fixed by (c_{ji}=-U_{ji}c_{ij}).

This is not a flat cochain complex. Direct substitution gives the exact identity
\[
\boxed{
(D_1^A D_0^A u)_{ijk}
=(U_{ji}-U_{ki}U_{jk})u_j
=(1-H_{ijk})U_{ji}u_j,
\qquad H_{ijk}=U_{ij}U_{jk}U_{ki}.
}
\]
Thus (D_1^A D_0^A=0) holds only when the triangular Wilson holonomy is trivial. Here the curvature is nonzero, and the nonzero composition is required rather than treated as a failed incidence test. The script compares the computed matrix (D_1^AD_0^A) against the displayed curvature formula.

## 4. Link-transported Whitney masses

For each triangle (T=(i,j,k)), choose (i) as local base fibre. Let (B_{0,T}) transport its three vertex values to that fibre, and (B_{1,T}) transport its three oriented edge values to the same fibre. With the standard local Whitney mass blocks (M_{0,T}) and (M_{1,T}), assemble
\[
M_0^A=\sum_T B_{0,T}^*M_{0,T}B_{0,T},\qquad
M_1^A=\sum_T B_{1,T}^*M_{1,T}B_{1,T},
\]
and
\[
(M_2^A)_{TT}=\frac1{|T|}.
\]
The local (M_{0,T}) and (M_{1,T}) use the same exact barycentric/degree-two quadrature construction as T149. The endpoint transports make these finite matrices gauge-covariant. They define a link-based discrete covariant Whitney model; they are not claimed to be the exact mass matrices of a separately specified smooth connection inside each triangle.

The generalized Hodge operators are assembled from the mass adjoints:
\[
\begin{aligned}
K_0^A&=(D_0^A)^*M_1^AD_0^A,\\
K_1^A&=M_1^AD_0^A(M_0^A)^{-1}(D_0^A)^*M_1^A
 +(D_1^A)^*M_2^AD_1^A,\\
K_2^A&=M_2^AD_1^A(M_1^A)^{-1}(D_1^A)^*M_2^A.
\end{aligned}
\]
Spectra are computed as generalized Hermitian eigenproblems ((K_k^A,M_k^A)). Positivity follows at the matrix level from the sum-of-squares construction; the audit also checks the assembled mass eigenvalues and Hermiticity numerically.

## 5. Numerical certificates

The script runs the supergolden geometry (t=\psi_{\rm sg}=1.465571231876768) and the regular control (t=\varphi), with the T149 scale convention.

| Certificate | Supergolden | Regular \(\varphi\) |
|---|---:|---:|
| Cells ((N_0,N_1,N_2)) | (32, 90, 60) | (32, 90, 60) |
| Antipodal link covariance residual | (4.71\times10^{-16}) | (5.55\times10^{-16}) |
| (D_1^AD_0^A) norm | 1.6271950 | 1.6193480 |
| Curvature identity residual | (2.31\times10^{-15}) | (2.31\times10^{-15}) |
| Holonomy sum | 12.56637061435918 | 12.56637061435916 |
| Gauss–Bonnet residual from (4\pi) | (1.78\times10^{-15}) | 0.0 |
| Holonomy / spherical-area residual | (2.22\times10^{-16}) | (2.50\times10^{-16}) |
| Gauge-covariance residual | (7.92\times10^{-15}) | (1.82\times10^{-15}) |

All three covariant mass matrices are positive definite in both runs. Their minimum eigenvalues are:

| Mass | Supergolden | Regular \(\varphi\) |
|---|---:|---:|
| (M_0^A) | 0.04228686 | 0.22790227 |
| (M_1^A) | 0.32308898 | 0.32237353 |
| (M_2^A) | 10.61778063 | 2.10292445 |

The lowest generalized Hodge eigenvalues are:

| Degree | Supergolden | Regular \(\varphi\) |
|---|---|---|
| 0 | (2.25166977^{(3)},\ 13.01097505^{(3)},\ 13.32496312,\ldots) | (0.41688880^{(3)},\ 2.43462642^{(5)},\ 5.98965596^{(3)},\ldots) |
| 1 | (0,\ 4.71440480^{(3)},\ 10.18110888^{(3)},\ldots) | (0,\ 0.87479509^{(3)},\ 1.92215779^{(5)},\ldots) |
| 2 | (2.55046809^{(3)},\ 12.20994575,\ 12.22295989,\ldots) | (0.47282401^{(3)},\ 2.28843800^{(5)},\ 4.87106792^{(3)},\ldots) |

The degree-one zero mode is a kernel of this curved discrete Hodge operator; because (D_1^AD_0^A\ne0), it must not be interpreted as the cohomology of a flat cochain complex. No rescaling or fitted weights are introduced to match the Q6 values (0,4,6).

## 6. What is established, and what remains open

**Established by construction / exact algebra**
- The chosen nodal-normal rule extends the T155 face-centre normals to all 32 nodes.
- Every one of the 90 edges receives an SO(2) link transport.
- The curvature-defect identity for (D_1^AD_0^A) follows exactly from the link definitions.
- The link-transported mass assembly is gauge-covariant by construction.

**Numerically verified for the two specified geometries**
- Antipodal link covariance on all 90 edges.
- T155 compatibility on all 30 links of the 12-centre Gauss-map graph.
- Each triangle holonomy agrees with its oriented spherical Gauss-map area; the total is (4\pi).
- Positive assembled masses, Hermiticity, gauge covariance, and the reported spectra.

**Still open**
1. Prove a uniqueness or optimality principle for the area-weighted nodal-normal extension; the present choice is explicit and symmetry-compatible, not unique by fiat.
2. Replace the endpoint-link mass approximation by a continuum connection (A) specified inside each triangle, with path-independent gauge-covariant quadrature data where possible.
3. Establish convergence under mesh refinement and a compatible curved-connection FEEC error theory.
4. Derive, rather than fit, any map from this 32–90–60 operator to the selected Q6/RGS sector.
5. Derive the T144 polynomial (f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}) from geometry, if such a derivation exists.

**Conclusion:** T157 closes the finite 32–90–60 *link-connection and covariant Whitney mass* construction. It does not claim a flat FEEC complex or a continuum convergence theorem. Nonzero curvature is retained explicitly in (D_1^AD_0^A), as required.

## 7. Reproduction

```bash
python scripts/audit_t157_full_covariant_whitney_curvature.py
python -m unittest tests.test_t157_full_covariant_whitney_curvature
```

Machine-readable report: `results/json/t157_full_covariant_whitney_curvature.json`. Workflow: `.github/workflows/t157-covariant-whitney.yml`.
