# T149 — Supergolden dodecahedral Whitney–Hodge construction: executed FEEC audit

**Date:** 26 November 2026  
**Classification:** exact finite incidence construction; numerical Whitney–FEEC mass/Hodge audit; spectral comparison.  
**Result:** the 32–90–60 centroid-fan complex and all three mass matrices have been assembled for the supergolden polar dual and the regular control. Incidence, antipodal equivariance and mass positivity pass. The canonical scalar Hodge operator does not intertwine with the selected Q6 sector.

## 1. Two geometries, kept separate

The main run continues T146 at
\[
t=\psi_{\rm sg}=1.465571231876768,\qquad t^3-t^2-1=0.
\]
This is a deformed icosahedral hull and its polar dual; its pentagons are not regular. T149 preserves the T146 polar normalization (scale 1).

The control run uses
\[
t=\varphi=(1+\sqrt5)/2.
\]
This is the regular icosahedron and regular dodecahedron. Only this control is scaled so that the dodecahedral edge equals the vesica-derived pentagon chord
\[
s_{\rm pent}=CH=2r\sin36^\circ,
\]
with r=1. The resulting edge length is 1.1755705045849463. No T141/Q6 map is transferred to this regular control.

Each dodecahedral pentagon receives its Euclidean centroid and is divided into five triangles. Both runs therefore have
\[
(N_0,N_1,N_2)=(32,90,60),\qquad \chi=2.
\]

## 2. Barycentric gradients and Whitney mass matrices

For an oriented triangle T=(p0,p1,p2), set E=[p1-p0,p2-p0], G=EᵀE. The exact tangential affine gradients are
\[
\nabla\lambda_1=EG^{-1}e_1,\quad
\nabla\lambda_2=EG^{-1}e_2,\quad
\nabla\lambda_0=-\nabla\lambda_1-\nabla\lambda_2.
\]
The assembled mass matrices are
\[
(M_0^T)_{ij}=\int_T\lambda_i\lambda_j\,dA
=\frac{A_T}{12}(1+\delta_{ij}),
\]
\[
(M_1^T)_{ab}=\int_T\langle w_a,w_b\rangle\,dA,
\quad w_{ij}=\lambda_i d\lambda_j-\lambda_jd\lambda_i,
\]
and, for the normalized Whitney 2-form
\[
w_{012}=2(\lambda_0d\lambda_1\wedge d\lambda_2
-\lambda_1d\lambda_0\wedge d\lambda_2
+\lambda_2d\lambda_0\wedge d\lambda_1),
\]
\[
\boxed{M_2^T=\int_T|w_{012}|^2dA=1/A_T.}
\]

**Normalization correction to the original specification:** the earlier value 4/A_T was incorrect for the displayed normalized Whitney 2-form. Since the bracket equals dλ1∧dλ2 and |dλ1∧dλ2|=1/(2A_T), the factor 2 makes w012 have constant norm 1/A_T and integral 1; hence its squared L2 norm is 1/A_T. The script and all results use this corrected normalization. The 1-form mass is integrated by exact degree-two triangular quadrature. No edge weights are fitted.

These matrices are the discrete Hodge-star/mass operators; they are not a claim that the pointwise Hodge star maps each Whitney space exactly into itself. The mass-induced adjoints are
\[
\delta_1=M_0^{-1}D_0^TM_1,\qquad
\delta_2=M_1^{-1}D_1^TM_2,
\]
with
\[
\Delta_0=M_0^{-1}D_0^TM_1D_0,\quad
\Delta_1=D_0\delta_1+\delta_2D_1,\quad
\Delta_2=D_1\delta_2.
\]
All spectra are computed through generalized symmetric eigenproblems.

## 3. Incidence and antipodal certificates

For both geometries:
- D1D0=0 exactly;
- rank(D0)=31 and rank(D1)=59;
- the antipodal signed permutations S0,S1,S2 are involutions;
- d0S0=S1d0 and d1S1=S2d1 have zero residual;
- S_kᵀM_kS_k=M_k to numerical precision.

<badge color="success">Both geometry audits pass</badge>

| Certificate | Supergolden t=ψsg | Regular control t=φ |
|---|---:|---:|
| Incidence residual | 0 | 0 |
| Antipodal mass residual, max over k | 1.38×10⁻¹⁴ | 1.78×10⁻¹⁵ |
| Antipodal involution residual | 0 | 0 |
| Minimum mass eigenvalue, minimum over k | 0.0388530 | 0.2093197 |

The supergolden local pentagon frame is measurably non-regular: maximum residuals in radial equality, side equality and 72° phase spacing are respectively 0.0429963, 0.0925499 and 0.1773773. The regular control gives 2.22×10⁻¹⁶ for all three. This is precisely why the two runs cannot be conflated.

## 4. Supergolden Hodge spectra

For t=ψsg, the scalar generalized spectrum is
\[
\begin{aligned}
\operatorname{spec}(\Delta_0)=\{&
0,\ 4.84767416^{(3)},\ 15.83766753^{(2)},\
&16.67208153^{(3)},\ 35.73536361,\ 35.74756826^{(3)},\
&41.77634179^{(3)},\ 62.63614221,\ 65.95981519^{(3)},\
&74.88135413^{(2)},\ 79.20970731^{(3)},\
&84.92796429^{(3)},\ 115.67871225^{(3)},\ 149.16180286\}.
\end{aligned}
\]
The first twelve degree-one eigenvalues are
\[
4.84767416^{(3)},\ 4.92799199^{(3)},\
14.52457049^{(2)},\ 14.83734328^{(3)},\ 15.83766753^{(2)}.
\]
The first degree-two eigenvalues are
\[
0,\ 4.92799199^{(3)},\ 14.52457049^{(2)},\
14.83734328^{(3)},\ 27.30663695^{(3)},\ldots
\]

The antipodal parity dimensions are (16,16) in degree 0, (45,45) in degree 1, and (30,30) in degree 2. The complete plus/minus spectra are stored in the JSON report.

## 5. Scalar condensation and T146 comparison

Let K0=D0ᵀM1D0 and partition the 32 scalar nodes into 20 original dodecahedral vertices and 12 face centres. Harmonic extension of the retained values is
\[
H=\begin{pmatrix}I_{20}\\-K_{cc}^{-1}K_{cv}\end{pmatrix},
\quad K_{\rm eff}=H^TK_0H,\quad M_{\rm eff}=H^TM_0H.
\]
Thus the reported Schur spectrum is the generalized spectrum of (Keff,Meff), with an explicitly stated mass pullback. It is not the naive Euclidean spectrum of Keff.

For the supergolden run:
\[
\operatorname{spec}(K_{\rm eff},M_{\rm eff})=
\{0,\ 5.13305810^{(3)},\ 17.74566900^{(2)},\
19.06067368^{(3)},\ 35.73536361,\ 35.85934343^{(3)},\
62.67658391,\ 63.99682932^{(3)},\ 65.96898241^{(3)}\}.
\]

The T146 Q6 map is used **only** for this supergolden run. The Q6-pulled and edge-chain energies reproduce the T146 spectra. Their selected-sector intertwiner residuals are
\[
\|\Lambda\Phi-\Phi L_{\rm pull}\|_F=5.7099189664,
\]
\[
\|\Lambda\Phi-\Phi L_{\rm chain}\|_F=2.1936912594,
\]
where Λ=diag(0,4,6). The independent Q6 identity has residual 7.73×10⁻¹⁶. The condensed FEEC spectrum is distinct from both T146 spectra; no Q6 map is invented for the twelve new centre degrees of freedom.

## 6. Regular control

At t=φ with the vesica side-length scale, the scalar spectrum is
\[
\begin{aligned}
0,&\quad0.8998092042^{(3)},\quad3.0254343056^{(5)},\
&6.6334368540^{(4)},\quad7.6755404480^{(3)},\quad12^{(4)},\
&14.2982911162^{(5)},\quad15.6704651320^{(3)},\
&21.3133877741^{(3)},\quad27.5015528100.
\end{aligned}
\]
Its regular pentagon frame residuals are at machine precision. This is a geometry control only; the T141 assignment and Q6 intertwiner are deliberately not applied to it.

## 7. Interpretation

The canonical face-centroid refinement, barycentric gradients, Whitney mass matrices, mass-induced adjoints, antipodal parity blocks and scalar condensation are now numerically assembled. The local face frames are compatible with the regular pentagon only in the φ control. In the supergolden metric, the faces are genuinely deformed even though the same pentagonal combinatorics remains.

The local Hodge mass matrices are invariant under rotations of an individual face frame. Therefore the discrete 72° pentagonal phases do not by themselves define a global connection. A nontrivial inter-face phase transport still requires independently specified transition maps across shared edges and a holonomy calculation. No torsion or spin connection is inferred from the local frames alone.

**Conclusion:** T149's FEEC assembly and antipodal gates pass. The canonical scalar Hodge operator and scalar Schur condensation do not produce the selected Q6 spectrum or an intertwiner. The polynomial
\[
f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}
\]
remains the exact finite Q6–RGS interpolation recorded in T144; its derivation from this Hodge construction remains open.

## 8. Reproduction

\`\`\`bash
python scripts/audit_t149_dodecahedron_feec_hodge.py
python -m unittest tests.test_t149_dodecahedron_feec_hodge
\`\`\`

Machine-readable report: results/json/t149_supergolden_dodecahedron_feec_hodge.json. Workflow: .github/workflows/t149-feec-hodge.yml.


## 9. Follow-up: global face connection constructed in T155

The previously open inter-face connection on the 12 pentagonal frames has now been constructed independently in [T155](T155-dodecahedral-gauss-map-levi-civita-hodge.md). T155 uses the Gauss-map normals, minimal SO(3) rotations, the vesica-axis gauge, geometric face-area masses and shared-edge/centroid-distance conductances. Its antipodal frame covariance and 4π holonomy total pass.

This closes the face-graph connection gap identified in the original T149 conclusion. It does **not** yet produce a covariant Whitney differential on all 32 vertices, 90 edges and 60 triangles. The full 32–90–60 covariant FEEC extension, its Hodge spectrum, and the derivation of the Q6/RGS polynomial f remain open.
