# T156 — Whitney–FEEC Hodge data on the dodecahedral polar surface

**Date:** 27 November 2026  
**Classification:** finite geometric construction + numerical FEEC audit.  
**Status:** verified finite-element identities and antipodal equivariance; target Q6 spectral intertwining remains open.

## 1. Canonical surface triangulation

Start from the polar dual of the T139 icosahedral hull at
\[
t=\psi_{\rm sg},\qquad \psi_{\rm sg}^3-\psi_{\rm sg}^2-1=0.
\]
The dodecahedral surface has 20 vertices, 30 edges and 12 planar pentagonal faces. For each pentagon, add its Euclidean centroid and join it to the five boundary vertices. This gives a closed triangular surface with
\[
(V,E,F)=(32,90,60),\qquad V-E+F=2.
\]
The face centroid and fan triangulation are fixed by Euclidean geometry; no edge weights are fitted.

Each pentagon is equipped with an orthonormal frame: the first boundary edge fixes the first tangent vector, the oriented polygon normal fixes the normal, and their cross product fixes the second tangent vector. The audit checks orthonormality and pentagon planarity.

## 2. Whitney/FEEC mass matrices

Let \(d_0:C^0\to C^1\) and \(d_1:C^1\to C^2\) be the simplicial coboundary matrices of the 60-triangle mesh. The audit assembles:

- \(M_0\): consistent P1 scalar mass matrix, with local entries \(A_T(1+\delta_{ij})/12\);
- \(M_1\): consistent Whitney 1-form Gram matrix, integrated by exact degree-two barycentric quadrature;
- \(M_2\): top-form Gram matrix, diagonal with entries \(1/A_T\), since a 2-cochain stores the integral over triangle \(T\).

The scalar stiffness matrix is
\[
K_0=d_0^T M_1d_0.
\]
The discrete 1-form Hodge stiffness is
\[
K_1=M_1d_0M_0^{-1}d_0^TM_1+d_1^TM_2d_1.
\]
The generalized Hodge spectra are computed from \(K_0u=\lambda M_0u\) and \(K_1v=\lambda M_1v\). These are consistent finite-element Gram matrices, not diagonal circumcentric DEC weights.

## 3. Numerical results

The audit gives the scalar generalized spectrum:
\[
\begin{aligned}
\operatorname{spec}(K_0,M_0)=\{&
0,\ 4.8476741595^{(3)},\ 15.8376675338^{(2)},\\
&16.6720815293^{(3)},\ 35.7353636125,\\
&35.74756826^{(3)},\ 41.77634179^{(3)},\\
&62.63614221,\ 65.95981519^{(3)},\\
&74.88135413^{(2)},\ 79.20970731^{(3)},\\
&84.92796429^{(3)},\ 115.67871225^{(3)},\\
&149.16180286\}.
\end{aligned}
\]
This canonical FEEC operator does not have the selected Q6 eigenvalue triple \((0,4,6)\). Its first positive eigenvalue is approximately 4.84767416 with multiplicity three. It is not rescaled to 4.

For the selected Q6 map, extend the T146 barycentre rows from the 20 dodecahedral vertices to the 12 pentagon centres by the arithmetic mean of the five incident vertex rows. With \(\Phi=FB_{32}^T\) and \(\Lambda=\operatorname{diag}(0,4,6)\), the generalized operator \(A_0=M_0^{-1}K_0\) gives
\[
\|\Lambda\Phi-\Phi A_0\|_F=13.0217866959959.
\]
The map has rank three, but it is not an intertwiner.

## 4. Structural certificates

The reproducible audit checks \(d_1d_0=0\), \(K_0=d_0^TM_1d_0\), positive definiteness of \(M_0,M_1,M_2\), antipodal equivariance of all three mass matrices and \(K_0\), orthonormality of all 12 local pentagon frames, planarity of all 12 pentagons, non-negativity of the generalized Hodge-0 and Hodge-1 spectra, and Euler characteristic 2.

Representative residuals:
\[
\begin{array}{ll}
\|d_1d_0\|_F &=0,\\
\|K_0-d_0^TM_1d_0\|_F &=0,\\
\|S_0^TM_0S_0-M_0\|_F &<3.0\times10^{-17},\\
\|S_1^TM_1S_1-M_1\|_F &<8.2\times10^{-16},\\
\|S_2^TM_2S_2-M_2\|_F &<7.2\times10^{-15}.
\end{array}
\]

## 5. Interpretation and open gate

This establishes a canonical, antipodally equivariant Whitney/FEEC Hodge construction on a triangulated dodecahedral polar surface. It supplies explicit scalar, 1-form and top-form inner products and a reproducible spectral obstruction for the centroid-fan construction.

It does **not** derive \((0,4,6)\), does not establish an intertwiner with the selected Q6 sector, and does not derive
\[
f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}.
\]
The next legitimate step is to test a different independently justified geometric discretization, such as a compatible primal/dual FEEC pair. Any change must preserve antipodal equivariance and must not fit weights to the target spectrum.

## 6. Reproduction

~~~bash
python scripts/audit_t156_dodecahedral_feec_hodge.py
python -m unittest tests.test_t156_dodecahedral_feec_hodge
~~~

The workflow runs the deterministic audit and both regression tests. The JSON report is written to results/json/t156_dodecahedral_feec_hodge_audit.json.
