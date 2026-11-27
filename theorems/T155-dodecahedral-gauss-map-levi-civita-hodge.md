# T155 — Dodecahedral Gauss-map connection and covariant Hodge operator

**Date:** 26 November 2026  
**Classification:** explicit geometric discrete connection; finite-volume Hodge construction; numerical and topological certificates.  
**Result:** Levi-Civita transport on the 12 pentagonal face normals is constructed without spectral fitting. Antipodal covariance, the per-triangle Wilson-holonomy/spherical-area identity (maximum residual 2.22×10⁻¹⁶), and the discrete Gauss–Bonnet total pass. Both 12-dimensional spectra reproduce the recorded regular and supergolden controls within 10⁻⁷. The covariant Hodge spectrum is positive and is not the selected Q6 triplet.

## 1. Geometry and frame gauge

The 12 pentagonal faces are indexed by the 12 vertices \(v_i\) of the primal icosahedral hull. Their outward unit normals are the Gauss-map points
\[
n_i=\frac{v_i}{\lVert v_i\rVert}\in S^2.
\]
These are the actual normals of the polar-face planes, not the radial directions of their centroids (which need not agree in the deformed supergolden case).

Let \(c_i\) be the arithmetic centroid and \(A_i\) the planar area of pentagon \(i\). Fix the local oriented tangent frame by projecting the vesica-square axis \(a=(1,0,0)\):
\[
e_{1,i}=\frac{a-(a\cdot n_i)n_i}{\lVert a-(a\cdot n_i)n_i\rVert},
\qquad e_{2,i}=n_i\times e_{1,i}.
\]
This is a gauge choice, not a physical preferred direction. Its projection norm is checked away from zero. Local SO(2) frame changes conjugate link variables and leave the spectrum and Wilson holonomies invariant.

## 2. Levi-Civita link transport

The pentagonal face-adjacency graph has 12 vertices and 30 edges; its triangular 2-cells are the 20 primal icosahedral facets. For an oriented adjacency \(i\to j\), let \(R_{ij}\in SO(3)\) be the unique minimal rotation carrying \(n_i\) to \(n_j\). With \(v=n_i\times n_j\), \(s=\lVert v\rVert\), \(c=n_i\cdot n_j\), and \(K=[v]_\times\),
\[
R_{ij}=I+K+\frac{1-c}{s^2}K^2.
\]
The induced tangent-frame transport is
\[
T_{ij}=F_j^TR_{ij}F_i\in SO(2),\quad F_i=(e_{1,i},e_{2,i}).
\]
Writing
\[
T_{ij}=\begin{pmatrix}\cos\alpha_{ij}&-\sin\alpha_{ij}\\
\sin\alpha_{ij}&\cos\alpha_{ij}\end{pmatrix},
\qquad U_{ij}=e^{i\alpha_{ij}},
\]
defines the discrete Levi-Civita U(1) link. Reversing an edge gives \(U_{ji}=\overline{U_{ij}}\).

## 3. Geometric Hodge star and covariant Laplacian

No weights are fitted. The face mass and edge co-metric are the finite-volume geometric quantities
\[
(M_0)_{ii}=A_i,\qquad W_{ij,ij}=\frac{\ell_{ij}}{d_{ij}},
\]
where \(\ell_{ij}\) is the common dodecahedral-edge length and \(d_{ij}=\lVert c_i-c_j\rVert\) is the distance between adjacent face centroids. Thus \(M_0\) is the face-area Hodge star and \(W\) is the two-point finite-volume co-metric.

The covariant coboundary and Hermitian Hodge operator are
\[
(d_Au)_{ij}=u_j-U_{ij}u_i,\qquad
\boxed{\Delta_A=M_0^{-1}d_A^*Wd_A.}
\]
The generalized spectrum is computed from \(M_0^{-1/2}d_A^*Wd_AM_0^{-1/2}\). Curvature is nonzero, so a constant coefficient vector is not a parallel section and there is no zero mode.

## 4. Antipodal covariance

Let \(\bar i\) denote the antipodal face and
\[
A_i=F_{\bar i}^T(-I)F_i
\]
the induced tangent-frame map. It is a reflection in local coordinates because the antipodal map reverses the orientation of \(S^2\). The audit verifies the full real \(2\times2\) identity
\[
T_{\bar i\bar j}A_i=A_jT_{ij}
\]
with edge orientation handled explicitly.

## 5. Holonomy and Gauss–Bonnet

For each of the 20 outward-oriented primal icosahedral triangles, multiply the three link transports around its boundary. The holonomy angle is the spherical area of that Gauss-map triangle (using the oriented representative in the report). The sum satisfies
\[
\boxed{\sum_{f\in F_{\rm ico}}\operatorname{Hol}(f)=4\pi.}
\]
In the regular \(\varphi\) control all 20 angles are \(0.6283185307=\pi/5\). In the supergolden case the two holonomy values are approximately \(0.60097581\) and \(0.64654701\); their total is \(4\pi\).

## 6. Numerical results

The complete spectra and link data are stored in results/json/t155_dodecahedral_levi_civita_hodge.json.

**Supergolden \(t=\psi_{\rm sg}\):**
\[
\operatorname{spec}(\Delta_A)=
\{2.67266956^{(3)},10.05977279^{(2)},10.66910015^{(3)},
13.89611089,14.09865578^{(3)}\}.
\]

**Regular control \(t=\varphi\):**
\[
\operatorname{spec}(\Delta_A)=
\{0.49643312^{(3)},1.93332265^{(5)},2.59935757^{(4)}\}.
\]
Both operators are Hermitian positive definite. Antipodal frame covariance is at machine precision; the Gauss–Bonnet residual is below numerical tolerance. Neither spectrum equals \((0,4,6)\). No scalar rescaling or edge reweighting has been introduced to force the Q6 values.

## 7. Scope and remaining obstruction

T155 constructs the Levi-Civita connection on the 12 pentagonal face frames and its curvature/holonomy. The subsequent T157 record extends the nodal-normal connection to all 32 centroid-fan nodes and 90 edges, constructs link-transported Whitney masses on the 60 triangles, and verifies the curvature defect \(D_1^A D_0^A\ne0\) by an exact Wilson-loop identity. T157 is a finite curved cochain sequence, not a flat cochain complex.

The present \(\Delta_A\) remains the 12-dimensional face-centred finite-volume Hodge operator, distinct from the 32–90–60 link-covariant Whitney Hodge operators of T157. T158 specifies a piecewise-smooth pullback connection inside each triangle. Mesh-refinement convergence and a continuum curved-FEEC error theory remain open. Neither construction derives \(f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}\); the Q6/RGS interpolation remains the exact result recorded in T144, and its derivation from dodecahedral geometry remains open.

## 8. Reproduction

\`\`\`bash
python scripts/audit_t155_dodecahedral_levi_civita_hodge.py
python -m unittest tests.test_t155_dodecahedral_levi_civita_hodge
\`\`\`

Workflow: .github/workflows/t155-levi-civita-hodge.yml.
