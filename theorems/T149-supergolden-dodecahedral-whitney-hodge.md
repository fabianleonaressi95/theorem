# T149 — Supergolden dodecahedral Whitney–Hodge construction: geometric specification and audit gates

**Date:** 26 November 2026  
**Classification:** proposed finite-element construction; exact combinatorial triangulation and local mass formulas; numerical assembly and Q6 intertwining not yet verified.  
**Scope:** continue T146 at the actual supergolden parameter \(t=\psi_{\rm sg}\). The regular case \(t=\varphi\) is a separate control experiment, not a substitute geometry.

## 1. Geometry and canonical refinement

Use the polar dual returned by the T146 construction at
\[
\psi_{\rm sg}^3-\psi_{\rm sg}^2-1=0.
\]
The twelve pentagonal faces are planar polygons. In each face insert its Euclidean centroid and join it to the five boundary vertices. This gives a triangulated polyhedral surface with

\[
N_0=20+12=32,\qquad N_1=30+60=90,\qquad N_2=60,
\]
and Euler characteristic \(32-90+60=2\). The construction is face-local and introduces no fitted edge weights. The six radial edges in each antipodal face pair are mapped to one another by the antipodal involution; orientations are transported by the induced map, not independently reselected.

The face centroid is the arithmetic mean of its five polar vertices. Every resulting triangle is contained in the supporting plane of its pentagon. Its metric is the Euclidean metric inherited from that plane.

## 2. Whitney finite-element spaces and mass matrices

On each oriented triangle \(T=[v_0,v_1,v_2]\), let \(\lambda_0,\lambda_1,\lambda_2\) be barycentric coordinates. Use the standard Whitney basis:
\[
w_{ij}=\lambda_i\,d\lambda_j-\lambda_j\,d\lambda_i,
\qquad 0\leq i<j\leq2,
\]
and the oriented Whitney 2-form
\[
w_{012}=2(\lambda_0\,d\lambda_1\wedge d\lambda_2
-\lambda_1\,d\lambda_0\wedge d\lambda_2
+\lambda_2\,d\lambda_0\wedge d\lambda_1).
\]
The local mass matrices are the exact geometric integrals
\[
(M_0^T)_{ij}=\int_T\lambda_i\lambda_j\,dA,
\quad
(M_1^T)_{ab}=\int_T\langle w_a,w_b\rangle_T\,dA,
\quad
M_2^T=\int_T |w_{012}|^2\,dA.
\]
For a Euclidean triangle of area \(A_T\),
\[
(M_0^T)_{ij}=\frac{A_T}{12}(1+\delta_{ij}),
\qquad M_2^T=\frac{4}{A_T}.
\]
The 1-form matrix is evaluated by exact degree-two barycentric integration (three-point degree-two quadrature is exact); tangent inner products use the actual planar metric of each triangle. Assemble these local matrices using globally oriented vertices, edges and faces. No rescaling to target eigenvalues is permitted.

The assembled matrices \(M_k\) must be symmetric positive definite on the corresponding cochain spaces. The discrete adjoints are defined by these mass matrices. With cochain differentials \(d_0,d_1\), define
\[
\delta_1=M_0^{-1}d_0^TM_1,\qquad
\delta_2=M_1^{-1}d_1^TM_2,
\]
and
\[
\Delta_0=\delta_1d_0,\qquad
\Delta_1=d_0\delta_1+\delta_2d_1,\qquad
\Delta_2=d_1\delta_2.
\]
These are mass-self-adjoint nonnegative Hodge Laplacians; numerical implementations should solve the corresponding generalized symmetric eigenproblems rather than diagonalize a nonsymmetric matrix naively.

## 3. Antipodal and incidence identities

Let \(S_k\) denote the signed permutation induced by the antipodal involution on refined k-cochains. The assembly must verify exactly at incidence level and to numerical precision at metric level:
\[
d_0S_0=S_1d_0,\qquad d_1S_1=S_2d_1,
\]
\[
S_k^TM_kS_k=M_k,\qquad k=0,1,2.
\]
The chain identities \(d_1d_0=0\) and the Hodge adjoint identities are independent regression gates. A failure of metric invariance means the frame/orientation assembly is wrong; it is not evidence for broken antipodal symmetry in the underlying geometry.

## 4. Interface with T146 and Q6

The refinement adds twelve face-centroid vertices and sixty radial edges. T146's Q6 map is defined on the original 20 dodecahedral vertices and 30 edges only. Therefore **no Q6 images are assigned to the new degrees of freedom by guesswork**.

For the scalar sector, eliminate the twelve face-centroid potentials by the exact Schur complement of the assembled \(\Delta_0\) stiffness form (with the corresponding mass treatment stated explicitly). Compare the resulting 20-vertex operator with the two T146 operators:
\[
L_{\rm pull}=B L_{Q6}B^T,\qquad
L_{\rm chain}=DC^TCD^T.
\]
For the 1- and 2-form sectors, report their spectra and antipodal parity blocks first. A Q6 intertwiner is admissible only after a chain/cochain map for the added radial degrees of freedom is independently constructed and its boundary identities are verified.

The target Q6 sector remains \(\Lambda=\operatorname{diag}(0,4,6)\). The audit must report the full residual
\[
\|\Lambda\Phi-\Phi L_{\rm eff}\|_F
\]
for any explicitly defined comparison map \(\Phi\), and must not infer an intertwiner from a close eigenvalue alone.

## 5. Regular-icosahedron control

Repeat the entire geometric assembly at \(t=\varphi\), using the same polar convention, centroid rule, triangulation, Whitney forms and code. This is a control for the regular dodecahedron and its rotational \(A_5\) symmetry. The supergolden and regular runs must be reported separately:
- \(t=\psi_{\rm sg}\): continuation of T139–T146 and T141's fixed Q6 assignment;
- \(t=\varphi\): regular metric control, with its own symmetry and no automatic inheritance of the T141 Q6 map.

Do not average the two spectra or transfer the regular \(2I\) representation to the supergolden metric without an explicit equivariance proof.

## 6. Required audit output and acceptance gates

The reproducible audit should write a machine-readable report containing:
1. the parameter, coordinates, face areas and triangle areas;
2. dimensions and ranks of all incidence and mass matrices;
3. minimum mass-matrix eigenvalues and condition numbers;
4. incidence residuals and antipodal mass-invariance residuals;
5. the three generalized Hodge spectra, including multiplicities and parity decomposition;
6. scalar Schur-complement spectrum and comparison with T146;
7. any Q6 intertwining residual, with the comparison map and normalization fully specified.

Acceptance requires positive-definite masses, exact incidence identities, antipodal invariance, and reproducibility under vertex/face reordering. Matching \((0,4,6)\) is **not** an acceptance condition for the construction; it is a separate conjectural outcome to be tested.

## 7. Current status

**Established from T146:** the supergolden polar-dual incidence data, 20 vertices, 30 edges, 12 pentagons, antipodal action, Q6 barycentre/edge/face chain maps, and the negative spectral result for the three canonical T146 energies.

**Specified here, not yet numerically executed:** the 32–90–60 centroid-fan refinement, Whitney mass matrices, mass-induced Hodge adjoints, antipodal metric tests, scalar condensation, and regular \(t=\varphi\) control.

**Open:** numerical assembly; Hodge spectra; frame compatibility beyond the canonical planar face triangulation; extension of the T146 Q6 map to radial degrees of freedom; any derivation of \((0,4,6)\) or of \(f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}\).

This record is a construction specification and an audit protocol, not a claim that the Hodge computation or the desired spectral bridge has already succeeded.
