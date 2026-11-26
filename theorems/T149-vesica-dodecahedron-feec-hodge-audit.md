# T149 — Vesica-scaled dodecahedral Whitney–FEEC Hodge audit

**Date:** 26 November 2026  
**Classification:** exact regular-polyhedron construction + reproducible finite-element/FEEC numerical audit.  
**Status:** the canonical Whitney–FEEC Hodge matrices are constructed and positive definite; the resulting dodecahedral operator does not intertwine with the selected Q6 sector. This is a negative spectral result, not a derivation of f.

## 1. Geometry and scale: use the regular case

T146 uses the deformed icosahedral parameter t=ψ_sg. Its polar dual is a deformed dodecahedron, not the regular dodecahedron. The regular icosahedron in the T139 coordinate family is obtained at t=φ. T149 therefore rebuilds the polar dual at t=φ, independently of T146's deformed case.

For the vesica construction in docs/VESICA_PENTAGON_FRAME_BRIDGE.md, the regular pentagon side is the chord
\[
s_{\rm pent}=CH=2r\sin36^\circ.
\]
With r=1, scale the polar dodecahedron so that its 30 edges have exactly this length. This is a geometric scale identification, not a fitted spectral normalization. The resulting edge length is 1.1755705045849463.

The 12 pentagonal faces are ordered by the 12 vertices of the icosahedron. In each face, choose a local orthonormal frame (outward normal and a first radial direction); the five vertex phases differ by 2π/5. Across all faces, the maximum residuals in radial equality, edge-length equality, and 72° phase spacing are each 2.22×10⁻¹⁶.

**Important:** these local frames specify the regular pentagons. They do not determine a continuous connection or a global phase-transport law between different faces. The Hodge mass matrices below are intrinsic and therefore independent of the arbitrary choice of the first radial direction in each face.

## 2. Triangulated surface and barycentric gradients

Split each pentagon into five triangles by joining its centre to its five vertices. The closed surface triangulation has
\[
N_0=32,\qquad N_1=90,\qquad N_2=60,\qquad
N_0-N_1+N_2=2.
\]
The 32 vertices comprise the 20 dodecahedral vertices and 12 pentagon centres.

For each oriented triangle T=(p_0,p_1,p_2), set E=[p_1-p_0,p_2-p_0] and G=EᵀE. The exact affine barycentric gradients in the triangle plane are
\[
\nabla\lambda_1=EG^{-1}e_1,\quad
\nabla\lambda_2=EG^{-1}e_2,\quad
\nabla\lambda_0=-\nabla\lambda_1-\nabla\lambda_2.
\]
They are assembled facewise using the actual Euclidean metric of the scaled polar dodecahedron.

## 3. Discrete Hodge stars and codifferentials

Use the standard P1 mass matrix on 0-forms, the Whitney 1-form mass matrix on edges, and the integral-normalized piecewise-constant 2-form mass matrix:
\[
(M_0)_{ij}=\int_\Sigma\lambda_i\lambda_j\,dA,
\]
\[
(M_1)_{ef}=\int_\Sigma\langle w_e,w_f\rangle\,dA,
\qquad w_{ij}=\lambda_i\,d\lambda_j-\lambda_j\,d\lambda_i,
\]
\[
M_2=\operatorname{diag}(A_T^{-1}).
\]
These are the finite-element Hodge-star (mass) matrices for degrees 0, 1, and 2. In particular, M1 is assembled by exact degree-two triangular quadrature; no edge weights are fitted. They are all symmetric positive definite.

Let D0∈R^(90×32) and D1∈R^(60×90) be the incidence/coboundary matrices. The discrete codifferentials are
\[
\delta_1=M_0^{-1}D_0^TM_1,\qquad
\delta_2=M_1^{-1}D_1^TM_2.
\]
The degree-zero Hodge Laplacian is
\[
\Delta_0=M_0^{-1}D_0^TM_1D_0.
\]
The degree-one and degree-two operators are assembled from the same mass matrices and incidence maps. The boundary identity D1D0=0 is exact in the finite incidence representation. Ranks are rank(D0)=31 and rank(D1)=59, giving Betti numbers (1,0,1), as expected for a sphere.

## 4. Spectral result

The generalized eigenproblem is
\[
D_0^TM_1D_0u=\lambda M_0u.
\]
With the vesica-matched scale, the 32 eigenvalues are
\[
\begin{aligned}
0,&\quad 0.8998092042^{(3)},\quad 3.0254343056^{(5)},\\
&6.6334368540^{(4)},\quad 7.6755404480^{(3)},\quad
12^{(4)},\\
&14.2982911162^{(5)},\quad15.6704651320^{(3)},\quad
21.3133877741^{(3)},\quad27.5015528100.
\end{aligned}
\]
They do not give the selected Q6 triple (0,4,6). The result is not repaired by rescaling: the scale has already been fixed by the vesica-derived pentagon chord.

The first twelve degree-one Hodge eigenvalues are
\[
0.8998092042^{(3)},\quad0.9146614831^{(3)},\quad
2.7327541479^{(5)},\quad3.0254343056.
\]
The first degree-two eigenvalues are
\[
0,\quad0.9146614831^{(3)},\quad
2.7327541479^{(5)},\quad5.1758237783^{(3)},\ldots
\]
The zero modes in degrees 0 and 2 are consistent with b0=b2=1; there are no harmonic 1-forms.

## 5. Q6 comparison

Extend the T141 barycentre map from the 20 dodecahedral vertices to the 12 pentagon centres by averaging the five boundary-vertex rows. This gives P∈R^(32×64), rank(P)=12. The Q6-pulled energy P L6 Pᵀ has 20 zero modes and positive eigenvalue groups
\[
0.3593397753^{(3)},\quad2.24^{(5)},\quad
8.7073268913^{(3)},\quad16.
\]
This is not the FEEC operator and does not have the selected spectrum either.

For the FEEC operator L_FE=M0⁻¹D0ᵀM1D0, let Φ=F Pᵀ, where F is the previously archived selected Q6 coisometry and Λ=diag(0,4,6). The direct test gives
\[
\boxed{\|\Lambda\Phi-\Phi L_{FE}\|_F=2.9196339171.}
\]
The independent Q6 identity \|FL6−ΛF\|_F=7.73×10⁻¹⁶ still passes. Thus the failure lies in the dodecahedral-to-Q6 transfer, not in the archived Q6 sector.

## 6. Interpretation and open step

The vesica pentagon fixes the local regular pentagon geometry and the physical edge scale. Barycentric gradients and Whitney forms then determine canonical FEEC mass matrices. This closes the local Hodge construction without arbitrary edge weights.

It does **not** determine the missing inter-face connection. Since the local Hodge mass matrices are invariant under rotations of each face frame, the 72° pentagonal phases alone cannot create a nontrivial global transport operator. To obtain such an operator one must independently define transition maps across shared edges, compute their holonomy, and prove compatibility with the discrete de Rham differential. No torsion, spin connection, or nonzero phase curvature is inferred merely from the pentagonal frames.

**Conclusion:** T149 establishes a reproducible vesica-scaled regular-dodecahedron FEEC Hodge model and falsifies the simplest claim that its canonical scalar Hodge Laplacian already intertwines with the selected Q6 sector. The polynomial
\[
f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}
\]
remains the exact Q6–RGS three-node interpolation from T144; its derivation from this dodecahedral Hodge operator remains open.

## 7. Reproduction

\`\`\`bash
python scripts/audit_t149_dodecahedron_feec_hodge.py
python -m unittest tests.test_t149_dodecahedron_feec_hodge
\`\`\`

Machine-readable output: results/json/dodecahedron_feec_hodge_t149.json.

**Status label:** exact geometry and incidence; numerical FEEC/Hodge audit; spectral intertwining failed; global frame connection and first-principles derivation of f open.
