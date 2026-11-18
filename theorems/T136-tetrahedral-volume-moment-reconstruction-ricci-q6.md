# T136 — Tetrahedral volume moments, local Ricci reconstruction, and the Q6 curvature gate

**Date:** 18 November 2026  
**Status:** Established local expansion; conditional finite-dimensional identifiability; RGS–Q6 continuum correspondence open.  
**Scope:** Riemannian geometry in dimension three, tetrahedral volume measurements, Regge curvature, and the proposed Q6 plaquette functional.

## 1. Geometric setup

Let $(M,g)$ be a three-dimensional Riemannian manifold, let $p\in M$, and identify $T_pM$ with $\mathbb R^3$ using an orthonormal frame. Let $T\subset T_pM$ be a fixed nondegenerate Euclidean tetrahedron. Its position relative to the origin matters: translating $T$ changes its second-moment tensor.

For sufficiently small $r>0$, define the geodesic tetrahedral region
\[
T_r:=\exp_p(rT).
\]
Assume the exponential map is injective on a neighbourhood containing $rT$ and that the metric has sufficient regularity for the normal-coordinate volume-density expansion with a cubic remainder.

Define
\[
|T|=\int_T d^3y,\qquad
M^{ij}(T)=\int_T y^iy^j\,d^3y.
\]
The tensor $M(T)$ is symmetric and positive definite for a nondegenerate tetrahedron with nonempty interior.

## 2. Local volume expansion

In Riemannian normal coordinates centred at $p$, with the curvature-sign convention for which positively curved spheres have smaller small-ball volume than Euclidean balls,
\[
\sqrt{\det g(x)}
=1-\frac16\operatorname{Ric}_{ij}(p)x^ix^j+O(|x|^3).
\]
Changing variables $x=ry$ and integrating over $T$ gives
\[
\boxed{
V_g(T_r)
=r^3|T|-\frac{r^5}{6}\operatorname{Ric}_{ij}(p)M^{ij}(T)+O(r^6).
}
\]
The $O(r^6)$ remainder is valid for this fixed-domain rescaling under the stated regularity. The expansion is a standard consequence of the normal-coordinate volume density; it is not claimed as a new curvature law.

Equivalently, define the normalized measurement
\[
b_T(r):=-\frac{6}{r^2}
\left(\frac{V_g(T_r)}{r^3|T|}-1\right).
\]
Then
\[
b_T(r)=\frac{\operatorname{Ric}_{ij}(p)M^{ij}(T)}{|T|}+O(r).
\]
Thus a single tetrahedral volume measurement gives one linear functional of the Ricci tensor to leading order, not the full tensor.

## 3. Conditional reconstruction of the Ricci tensor

Choose tetrahedra $T_1,\ldots,T_m$ in the same orthonormal tangent frame, and write
\[
b_a(r)=b_{T_a}(r),\qquad
A_{a,ij}=\frac{M^{ij}(T_a)}{|T_a|}.
\]
The leading-order inverse problem is
\[
b_a(r)=A_{a,ij}\operatorname{Ric}^{ij}(p)+O(r).
\]

The space $\operatorname{Sym}^2(T_p^*M)$ has dimension six. Therefore:

1. At least six scalar measurements are necessary to recover a general symmetric Ricci tensor in dimension three.
2. Six measurements are sufficient for leading-order identifiability only if the six moment tensors $M(T_a)$ are linearly independent in $\operatorname{Sym}^2(\mathbb R^3)$.
3. For $m\geq6$, recovery is an overdetermined linear inverse problem. Its stability depends on the smallest singular value and condition number of the measurement matrix, as well as on volume-measurement and truncation errors.

If $A$ has full column rank, the leading-order least-squares estimator is
\[
\widehat{\operatorname{Ric}}(r)
=(A^TA)^{-1}A^T b(r),
\]
with the usual weighted/pseudoinverse variant when the noise covariance is known. This is a conditional identifiability statement, not a claim that arbitrary six tetrahedra suffice.

The origin and orientation of each tetrahedron must be fixed relative to the same frame. In particular, translations are not innocuous: they alter $M(T)$ and hence the measurement functional.

## 4. Continuous spherical-volume control

For comparison, the small geodesic-ball expansion in the same sign convention is
\[
V_g(B_r(p))=\frac{4\pi}{3}r^3
\left(1-\frac{\operatorname{Scal}(p)}{30}r^2+O(r^4)\right).
\]
This isotropic measurement recovers scalar curvature:
\[
\operatorname{Scal}(p)
=\lim_{r\to0}\frac{30}{r^2}
\left(1-\frac{V_g(B_r(p))}{\frac{4\pi}{3}r^3}\right).
\]
It does not, by itself, recover the six independent components of $\operatorname{Ric}$.

## 5. Regge curvature and the Q6 functional: separate objects

For a three-dimensional Regge triangulation, the deficit angle at an edge $e$ is
\[
\varepsilon_e=2\pi-\sum_{\sigma\supset e}\theta_{\sigma,e},
\]
and the Regge action (up to the conventional gravitational prefactor and boundary terms) is
\[
S_{\rm Regge}=\sum_e l_e\varepsilon_e.
\]
The deficit is attached to an edge and measures the rotational holonomy around its dual loop.

The Q6 plaquette functional under consideration is
\[
\mathcal F_{Q6}=\sum_{p=1}^{240}(1-\cos\Omega_p).
\]
For small plaquette angles,
\[
\mathcal F_{Q6}
=\frac12\sum_p\Omega_p^2+O\!\left(\sum_p\Omega_p^4\right).
\]
This establishes quadratic sensitivity to small holonomies only. It does **not** identify $\mathcal F_{Q6}$ with scalar curvature, the Regge action, or a continuum curvature norm.

Such an identification would require, at minimum:
- a specified family of geometric triangulations and a refinement parameter;
- a map from Q6 plaquettes to geometric loops/domains;
- the loop areas, orientations, and parallel-transport representation defining each $\Omega_p$;
- geometric weights and a dimensionally consistent normalization;
- control of anisotropy, multiplicities, and the scaling of $\Omega_p$ under refinement;
- a convergence theorem or a reproducible numerical convergence study.

In three dimensions, loop holonomies sample curvature in loop-dependent tangent two-planes. An unweighted sum of their squared angles is not automatically a norm of the full curvature tensor.

## 6. Verification programme

The numerical programme is deliberately staged:

**A. Manufactured smooth metrics.** Use metrics with analytically known Ricci tensors (including constant-curvature and anisotropic examples). Generate $T_r=\exp_p(rT)$ and compare measured volumes with the expansion. Verify the predicted $O(r^6)$ absolute remainder, equivalently the $O(r)$ error in $b_T(r)$.

**B. Moment design and conditioning.** Construct a family of tetrahedra whose normalized moment tensors span $\operatorname{Sym}^2(\mathbb R^3)$. Report singular values, condition number, reconstruction error, and sensitivity to perturbations in measured volumes. Do not accept the count $m=6$ as a substitute for a rank check.

**C. Noise and scale study.** Add controlled volume-measurement noise and vary $r$. Separate truncation error, floating-point error, and measurement noise; identify the scale range in which the inverse problem is stable.

**D. Regge refinement.** Only after A–C, define triangulation families, dual loops, deficits, volumes, and convergence norms. Compare discrete curvature with the known smooth metric.

**E. Q6 correspondence.** As a separate stage, define the plaquette-to-geometric-loop map and all weights before testing convergence of a normalized Q6 functional. No such canonical map or convergence result is asserted here.

## 7. Relation to Florenskij and RGS

Florenskij's discussion of geometry, measurement, and curvature is retained as historical and conceptual motivation. The tetrahedral moment calculation above is formulated independently in standard Riemannian geometry. It does not validate every geometric or physical interpretation in Florenskij's text.

For RGS, the concrete interface is a proposed measurement protocol: oriented tetrahedral volumes provide linear probes of the local Ricci tensor. An RGS–Q6 realization would require an explicit discrete-to-continuum map and the convergence obligations in Sections 5–6. Until then, the correspondence remains an open research programme.

## 8. Epistemic classification

| Statement | Classification |
|---|---|
| Normal-coordinate expansion of tetrahedral volume | Established differential-geometric consequence under stated regularity |
| At least six scalar probes are needed for a general 3D Ricci tensor | Exact dimension count |
| Full-rank moment design gives leading-order identifiability | Conditional finite-dimensional linear algebra |
| Stable reconstruction under noise | Numerical question, dependent on conditioning and noise |
| Regge refinement converges for a specified mesh family | Not established by this record; requires a separate theorem/proof |
| Q6 plaquette functional converges to a curvature invariant | Conjectural/open |
| Florenskij's geometric interpretation is physically validated by this construction | Not claimed |

## References

- T. Regge, “General Relativity Without Coordinates,” *Il Nuovo Cimento* **19** (1961), 558–571.
- A. Gray, “The volume of a small geodesic ball of a Riemannian manifold,” *Michigan Mathematical Journal* **20** (1973), 329–344.
- A. Gray, *Tubes*, 2nd ed., Birkhäuser, 2004.

**Repository rule:** this record is a mathematical specification and verification plan. No numerical audit, code implementation, continuum convergence, or physical validation is claimed until separately supplied and checked.


## 9. First manufactured numerical audit (T136-A/B)

A deterministic NumPy audit is provided in [audits/t136_tetrahedral_ricci.py](../audits/t136_tetrahedral_ricci.py), with regression tests in [tests/test_t136_tetrahedral_ricci.py](../tests/test_t136_tetrahedral_ricci.py). It uses a three-dimensional constant-sectional-curvature space form with $K=0.4$, for which $\operatorname{Ric}=2K I=0.8I$, and integrates the exact normal-coordinate density $(\sin(\sqrt K\,|x|)/(\sqrt K\,|x|))^2$ over six fixed tetrahedra by Duffy-transformed Gauss–Legendre quadrature.

The deterministic six-tetrahedron moment matrix has rank 6, singular values approximately
\[
(1.68989446,1.33500349,0.82677003,0.57782569,0.11501344,0.09043041),
\]
and condition number $18.6872362$. The reconstructed Ricci errors at scales $r=(0.16,0.12,0.09,0.0675)$ are approximately
\[
(1.2489\times10^{-2},7.0358\times10^{-3},3.9610\times10^{-3},2.2291\times10^{-3}).
\]
The error decreases at every refinement step. In this constant-curvature space-form control the radial density is even, so the normalized remainder exhibits the special $O(r^2)$ behaviour (successive error ratios approximately $0.563$, $0.563$, $0.563$), stronger than the generic $O(r)$ estimate. A deterministic observation perturbation of amplitude $10^{-7}$ gives Ricci reconstruction error approximately $2.23\times10^{-6}$.

**Evidence boundary:** this is a finite manufactured benchmark and a deterministic conditioning/noise check. It is not a general-metric convergence theorem, a Regge refinement result, a Q6 correspondence, or a physical validation. The regression tests are committed but have not been run in GitHub Actions in this PR.


## 10. Anisotropic manufactured control with nonzero off-diagonal Ricci

The audit now includes a second, independent manufactured local metric. Prescribe at the origin
\[
\operatorname{Ric}(0)=
\begin{pmatrix}
0.80&0.12&-0.08\\
0.12&0.50&0.09\\
-0.08&0.09&0.30
\end{pmatrix}.
\]
In three dimensions the algebraic Riemann tensor is determined by Ricci. The code constructs that tensor and the quadratic normal-coordinate metric
\[
g_{ij}(x)=\delta_{ij}-\frac13R_{ikjl}(0)x^kx^l.
\]
It integrates $\sqrt{\det g}$ over the same six fixed tetrahedra. This is a local manufactured normal-coordinate model, not a global spacetime or material model.

The moment matrix again has rank 6 and condition number $18.6872362$. The six-component reconstruction errors for $r=(0.16,0.12,0.09,0.0675)$ are
\[
(5.11596\times10^{-3},\;2.86315\times10^{-3},\;
1.60595\times10^{-3},\;9.01910\times10^{-4}).
\]
At the smallest scale the recovered components $(xx,yy,zz,xy,xz,yz)$ are approximately
\[
(0.79986219,\;0.50064474,\;0.29960334,\;
0.11990109,\;-0.08030948,\;0.09034038).
\]
All three off-diagonal entries are nonzero and are recovered with decreasing error. The normalized errors exhibit the expected special quadratic scaling for this even quadratic local metric. This closes the finite manufactured anisotropic check, but does not prove stability for arbitrary metrics, arbitrary tetrahedral families, or noisy nonlinear measurements.


## 11. Non-quadratic smooth-metric audit through the exponential map

A third audit removes the special quadratic-density simplification. The physical-coordinate metric is the smooth conformal metric
\[
g=e^{2f(x)}\delta,\qquad
f(x)=\frac12x^THx+\frac16C_{ijk}x^ix^jx^k,
\]
where $C$ is a nonzero fully symmetric cubic tensor. At the origin $df(0)=0$, and in dimension three
\[
\operatorname{Ric}(0)=-H-(\operatorname{tr}H)I.
\]
The Hessian $H$ is chosen so that the exact Ricci tensor is the same non-diagonal tensor used in Section 10. Since the cubic jet is nonzero, $\nabla\operatorname{Ric}(0)$ is generically nonzero.

Unlike the previous local quadratic model, the tetrahedra are mapped by the numerical Riemannian exponential map of this smooth metric. The code integrates the geodesic equation together with its variational equation for $D\exp_p$, then integrates the pulled-back density
\[
e^{3f(\exp_p(v))}\det(D\exp_p(v)).
\]
Thus the test includes the actual exponential-map Jacobian, rather than assuming the quadratic normal-coordinate density.

For the same six-tetrahedron design (moment rank 6, condition number $18.6872362$), the reconstruction errors at $r=(0.06,0.045,0.03375,0.0253125)$ are approximately
\[
(1.14047\times10^{-1},\;8.56246\times10^{-2},\;
6.42684\times10^{-2},\;4.82292\times10^{-2}).
\]
Successive ratios are approximately $(0.7508,0.7506,0.7504)$, consistent with the generic first-order $O(r)$ normalized truncation error. At the smallest scale the recovered components $(xx,yy,zz,xy,xz,yz)$ are approximately
\[
(0.791948,\;0.529949,\;0.270948,\;0.102696,\;-0.092190,\;0.098500).
\]
The error is larger than in the quadratic tests because the cubic jet contributes at first order to the normalized measurement; this is expected and is not evidence of a failed expansion.

**Noise/scale trade-off.** A fixed deterministic relative perturbation of $10^{-9}$ in each of the six volume measurements changes the reconstructed Ricci tensor by approximately
\[
(2.7251\times10^{-5},\;4.8452\times10^{-5},\;
8.6142\times10^{-5},\;1.5315\times10^{-4})
\]
over the same decreasing scales. The successive amplification factors are approximately $1.778$, consistent with the $r^{-2}$ factor in the normalized observable. This exposes the expected bias/noise trade-off: reducing $r$ decreases truncation bias but amplifies fixed relative volume noise.

A quadrature/integrator cross-check at $r=0.06$ changes the reconstructed six-vector by less than $2.1\times10^{-11}$ when increasing the Duffy quadrature order from 7 to 9 and the RK4 geodesic integration from 80 to 120 steps, respectively. This is a numerical resolution check for this example, not a rigorous error bound.

**Classification:** finite manufactured smooth-metric numerical verification, including nonzero cubic jet, off-diagonal Ricci, exponential-map Jacobian, and deterministic noise propagation. It is not a general stability theorem, an optimal scale-selection rule, a Regge convergence result, or a Q6 continuum limit.


## 12. D-optimal design of the tetrahedral probes

The noise study makes the conditioning of the moment matrix an operational issue, not merely a formal rank condition. A deterministic sequential D-optimal search was therefore added. It generates 4,000 candidate tetrahedra (fixed seed 1362026) and selects 12 probes by maximizing the incremental information determinant using the matrix determinant lemma.

For the selected 12-probe design:
- rank is 6;
- singular values are approximately
\[
(8.77639,7.64796,6.41882,6.15753,4.75081,4.03306);
\]
- the 2-norm condition number is approximately $2.17611$.

The original six-probe design used in Sections 9–11 has condition number $18.68724$. The selected overdetermined design therefore reduces the condition number by a factor of approximately $8.59$ in this deterministic candidate pool.

This is a design-of-experiments result for one fixed candidate distribution and seed. It does not prove global optimality over all tetrahedra, and it does not eliminate the $r^{-2}$ amplification of fixed relative volume noise in the normalized observable. It does improve the linear inverse problem's conditioning and supplies redundancy for residual diagnostics.

**Next mathematical gate:** test the optimized 12-probe family on the non-quadratic conformal metric, comparing six-probe and twelve-probe reconstructions under identical volume perturbations. Only after that comparison should a scale-selection rule be proposed.


## 13. Six-probe versus twelve-probe reconstruction on the non-quadratic metric

The D-optimal design was tested on the same smooth non-quadratic conformal metric of Section 11, using the same geodesic-volume integration and the same scale sequence. The comparison uses the original six tetrahedra and the selected 12-probe family. Both designs have rank 6; their condition numbers are $18.68724$ and $2.17611$, respectively.

At $r=(0.06,0.045,0.03375,0.0253125)$, the six-probe versus twelve-probe truncation errors are approximately
\[
\begin{array}{c|cc}
r&6\text{ probes}&12\text{ probes}\\
0.06&0.114047&0.017525\\
0.045&0.085625&0.013100\\
0.03375&0.064268&0.009802\\
0.0253125&0.048229&0.007339
\end{array}
\]
The 12-probe design reduces the reconstruction bias by factors between $6.51$ and $6.57$ in this test.

With deterministic relative volume perturbations of amplitude $10^{-9}$, the change in the reconstructed Ricci tensor is:
\[
\begin{array}{c|cc}
r&6\text{ probes}&12\text{ probes}\\
0.06&2.7251\times10^{-5}&5.2502\times10^{-7}\\
0.045&4.8452\times10^{-5}&9.3390\times10^{-7}\\
0.03375&8.6142\times10^{-5}&1.6608\times10^{-6}\\
0.0253125&1.5315\times10^{-4}&2.9531\times10^{-6}
\end{array}
\]
The noise-induced change is smaller by a factor of approximately $51.9$ for the 12-probe design. The first six noise variates are held fixed between designs; the overdetermined design has six additional independent perturbations.

This finite test shows that an overdetermined, well-conditioned moment design can substantially reduce both reconstruction bias and sensitivity to this particular noise realization. It does not remove the scale-dependent $r^{-2}$ amplification, establish a uniform statistical bound, or prove that this D-optimal design is optimal for other metrics or measurement distributions.


## 14. Covariance-based scale selection

The bias/noise trade-off in Sections 11–13 can be made quantitative for a specified measurement-noise model. Let $A\in\mathbb R^{m\times6}$ be the moment matrix, let
\[
q_i(r)=\frac{V_i(r)}{r^3|T_i|},\qquad
b_i(r)=-\frac6{r^2}(q_i(r)-1),
\]
and let $P=A^+$ be the Moore–Penrose inverse. Assume independent, zero-mean relative volume errors
\[
V_i^{\rm obs}=V_i(1+\epsilon_i),\qquad
\mathbb E[\epsilon_i]=0,\quad
\mathbb E[\epsilon_i\epsilon_j]=\sigma_{\rm rel}^2\delta_{ij}.
\]
The noisy normalized observation is
\[
b_i^{\rm obs}=b_i-\frac6{r^2}q_i(r)\epsilon_i.
\]
Consequently, for the linear least-squares estimator $\widehat R=P b^{\rm obs}$, the covariance is
\[
\operatorname{Cov}(\widehat R)
=P\,\operatorname{diag}\!\left(
\frac{36\sigma_{\rm rel}^2q_i(r)^2}{r^4}
\right)P^T.
\]
This expression retains the measured volume ratios $q_i(r)$; replacing them by 1 is only a small-scale approximation. The six-component coordinate vector is ordered as $(xx,yy,zz,xy,xz,yz)$. To measure the error as a symmetric tensor rather than as an unweighted coordinate vector, use the Frobenius metric
\[
W=\operatorname{diag}(1,1,1,2,2,2).
\]
For zero-mean noise, the expected squared Frobenius reconstruction error is exactly
\[
\mathbb E\|\widehat R-R(0)\|_F^2
=\|P b(r)-R(0)\|_W^2
+\operatorname{tr}\!\left(W\operatorname{Cov}(\widehat R)\right),
\qquad \|v\|_W^2=v^TWv.
\]
The finite-grid scale selector therefore minimizes the squared clean tensor bias plus the Frobenius-weighted covariance trace. This choice weights off-diagonal components twice in the squared tensor norm; it is not the same as an unweighted Euclidean norm on the six listed coordinates. The selected scale still depends on the metric, probe family, noise amplitude, and noise covariance.

If the asymptotic laws are $\|P b(r)-R(0)\|_F\sim a r$ and
$\sqrt{\operatorname{tr}(W\operatorname{Cov})}\sim b\sigma_{\rm rel}r^{-2}$, minimizing the leading squared error gives
\[
r_{\rm asym}=
\left(\frac{\sqrt2\,b\sigma_{\rm rel}}{a}\right)^{1/3}.
\]
The coefficients $a$ and $b$ are design- and metric-dependent. This cube-root estimate is an asymptotic guide, not a universal scale law.

The implementation is [audits/t136_scale_selection.py](../audits/t136_scale_selection.py), with regression checks in [tests/test_t136_scale_selection.py](../tests/test_t136_scale_selection.py). It compares the original six-probe design with the 12-probe D-optimal design, computes geodesic volumes on the same smooth non-quadratic conformal metric, propagates the independent relative-volume-noise covariance, uses the Frobenius norm of the symmetric Ricci tensor (including the factor 2 on off-diagonal components), and reports both a grid minimizer and the asymptotic estimate.

**Classification and evidence boundary:** the covariance identity is an exact finite-dimensional consequence of the stated linear estimator and independent relative-noise model. The numerical scale minimizing the resulting risk is model-, design-, grid-, and noise-specific. It is not a universal optimal scale, a general stability theorem, a Regge convergence result, or a Q6 continuum limit. The new audit and tests are committed for execution; no test or CI pass is claimed here.


### 14.1. Numerical scale-selection result for the manufactured metric

The scale audit was executed on the smooth non-quadratic conformal metric of Section 11, with independent relative-volume noise variance $\sigma_{\rm rel}^2$ and $\sigma_{\rm rel}=10^{-9}$. The risk uses the Frobenius norm of the symmetric Ricci tensor. On the declared geometric grid
\[
r\in(0.012,0.009,0.00675,0.005,0.00375,0.0028,
0.0021,0.0016,0.0012,0.0009),
\]
the finite-grid minimizers are:

\[
\begin{array}{c|ccccc}
\text{design}&r_{\rm grid}&\|\text{bias}\|_F&
\text{noise RMS}_F&\text{total RMSE}_F&r_{\rm asym}\
\hline
6\text{ probes}&0.00375&7.9168\times10^{-3}&
7.4690\times10^{-3}&1.0884\times10^{-2}&0.0041281\\
12\text{ probes}&0.00210&8.1326\times10^{-4}&
6.8942\times10^{-4}&1.0662\times10^{-3}&0.0022310
\end{array}
\]
Here $r_{\rm asym}$ is obtained by estimating $a$ and $b$ from the four finest grid points, not by fitting the entire risk curve. The corresponding coefficients are approximately $(a,b)=(2.1115,105.0324)$ for six probes and $(0.38718,3.04033)$ for twelve probes. The asymptotic estimate is close to, but distinct from, the finite-grid minimizer, as expected.

At their respective grid minimizers, the twelve-probe design has a total Frobenius RMSE approximately $10.2$ times smaller than the six-probe design. This comparison is specific to this manufactured metric, the fixed D-optimal candidate pool, the relative-noise level, and the tested scale grid; it is not a uniform improvement theorem.

A resolution cross-check at the two selected scales changed both the Duffy quadrature order from 7 to 9 and the geodesic RK4 step count from 80 to 120. The reconstructed Ricci vector changed by Frobenius norm approximately $1.01\times10^{-9}$ for the six-probe case and $2.44\times10^{-10}$ for the twelve-probe case. These are observed discretization changes under this cross-check, not rigorous integration-error bounds.

**Evidence status:** the numerical audit has been executed independently using the committed algorithm and matching deterministic seeds. The repository regression tests remain a separate check; no GitHub Actions pass is claimed unless a workflow run reports it.


## 15. Matched-budget exact design comparison protocol

The next audit fixes the observation model and the reconstruction map before comparing design criteria. For a physical tetrahedral probe (T_j), define
[
q_j(r)=\frac{V_g((T_j)_r)}{r^3|T_j|},\qquad
y_j(r)=-\frac{6}{r^2}(q_j(r)-1).
]
For a design (D=(T_1,\ldots,T_m)), let (A_D\in\mathbb R^{m\times6}) be the matrix whose rows are the normalized second-moment vectors in the component order ((xx,yy,zz,xy,xz,yz)), with doubled off-diagonal moments as in Section 4. The declared reconstruction is ordinary least squares:
[
\widehat R_D(r)=L_Dy_D(r),\qquad L_D=A_D^+.
]
The relative-volume observation model is
[
V_{j,\mathrm{obs}}=V_j(1+\epsilon_j),\qquad
\mathbb E\epsilon_j=0,\quad
\operatorname{Cov}(\epsilon)=\sigma_{\rm rel}^2I.
]
It follows that
[
\operatorname{Cov}(y_D(r))=
\operatorname{diag}\left(
\frac{36\sigma_{\rm rel}^2q_j(r)^2}{r^4}
\right),\qquad
\operatorname{Cov}(\widehat R_D)=
L_D\operatorname{Cov}(y_D)L_D^T.
]
Thus the A-criterion is applied to the covariance of the reconstructed estimator, not to an intermediate information matrix:
[
\Phi_A(D)=\frac1{|\mathcal G_{\rm sel}|}
\sum_{r\in\mathcal G_{\rm sel}}
\operatorname{tr}\left(W\operatorname{Cov}(\widehat R_D(r))\right).
]
The risk criterion uses the same fixed selection grid and equal scale weights:
[
\Phi_{\rm risk}(D)=\frac1{|\mathcal G_{\rm sel}|}
\sum_{r\in\mathcal G_{\rm sel}}
\left[
B_D(r)^TWB_D(r)+
\operatorname{tr}\left(W\operatorname{Cov}(\widehat R_D(r))\right)
\right].
]
The D-criterion remains the determinant criterion on (A_D^TA_D). These objectives are not interchangeable.

### Exact designs and validation

The A- and risk-based procedures select **exact subsets of 12 physical probes** from one shared finite candidate pool. They are not approximate designs with fractional weights. The implementation uses greedy augmentation from a common full-rank six-probe D-optimal seed; it therefore produces deterministic feasible exact designs, not globally optimal combinatorial subsets. The D-optimal 12-probe design is selected from the same pool and budget.

The selection grid is fixed in advance. Final risks and scale minimizers are recomputed on a separate, finer validation grid, with a higher quadrature/integration resolution than the lower-fidelity values used during subset selection. The six-probe legacy design is retained only as a separate benchmark because its budget differs.

### Monte Carlo coupling

For each candidate-probe index and replica, one relative-volume noise variate is generated and reused whenever that candidate appears in multiple designs. This common-random-number coupling makes paired comparisons reproducible even when two designs contain different probes. The same candidate-indexed variates are also reused across scales; this is an explicit coupling convention for the simulation, not a claim that measurements at different scales are physically identical random events.

The audit reports the analytic covariance propagated through (L_D), Monte Carlo covariance estimates, entrywise standard errors for those covariance estimates, and the Monte Carlo standard error of the squared Frobenius error. The number of replicas and all random seeds are fixed in the script.

### Implementation and epistemic status

Implementation: [audits/t136_exact_design_comparison.py](../audits/t136_exact_design_comparison.py); regression checks: [tests/test_t136_exact_design_comparison.py](../tests/test_t136_exact_design_comparison.py).

**No numerical winner is asserted by this protocol.** A- and risk-optimal designs are optimized for different declared objectives, and neither is presumed to dominate the other. A winner can be named only relative to a primary objective specified before inspecting the validation results. The exact subsets are greedy, the candidate pool is finite, and design selection uses lower numerical resolution than final evaluation. Global optimality, continuous-design optimality, and general geometric convergence are not claimed. Test execution and numerical audit output must be recorded separately from code being committed.


### 15.1. First executed matched-budget results

The focused GitHub Actions run completed successfully (4 focused tests passed; 2,000 Monte Carlo replicas; JSON artifact generated; run [44328318376](https://github.com/fabianleonaressi95/theorem/actions/runs/44328318376)). The comparison used a shared candidate pool of 128 tetrahedra, 12 probes per exact design, \(\sigma_{\rm rel}=10^{-9}\), a ten-scale equal-weight selection grid, and an independent 18-scale validation grid. Selection used Duffy order 3 / RK4 20 steps; validation used order 5 / RK4 40 steps.

All three exact 12-probe designs attained their validation-grid minimum at (r=0.0028664703):

| Exact 12-probe design | Moment condition number | Bias squared | Weighted covariance trace | Total risk squared | (ho=|B|_W/|N|_{L^2(W)}) | RMSE |
|---|---:|---:|---:|---:|---:|---:|
| D-optimal | 2.8854 | (1.37998\times10^{-6}) | (4.09511\times10^{-7}) | (1.78949\times10^{-6}) | 1.8357 | (1.33772\times10^{-3}) |
| A-optimal | 2.9804 | (1.28852\times10^{-6}) | (4.01871\times10^{-7}) | (1.69040\times10^{-6}) | 1.7906 | (1.30015\times10^{-3}) |
| Risk-optimal | 2.8267 | (9.13509\times10^{-7}) | (4.36029\times10^{-7}) | (1.34954\times10^{-6}) | 1.4474 | (1.16170\times10^{-3}) |

On this validation grid and manufactured metric, the greedy risk-selected design reduced total squared risk by about 24.59% relative to D-optimal and 20.16% relative to A-optimal. A-optimal reduced it by about 5.54% relative to D-optimal. These are empirical results for three finite subsets, not global optimality statements. The common grid minimizer does not establish that the continuous minimizers coincide.

At the common grid minimizer, Monte Carlo mean squared errors were (1.77658\times10^{-6}), (1.67950\times10^{-6}), and (1.34863\times10^{-6}), respectively, with estimated standard errors (1.61\times10^{-8}), (1.45\times10^{-8}), and (1.24\times10^{-8}). The Monte Carlo Frobenius-weighted covariance traces differed from the analytic traces by approximately 4.8–5.3%. The JSON artifact contains full covariance estimates and entrywise standard errors.

The legacy six-probe reference had condition number 18.6872 and validation-grid minimum RMSE (1.06774\times10^{-2}) at (r=0.00407765). It has a different budget and is not part of the matched 12-probe ranking.

**Resolution cross-check:** at each design's validation-grid minimizer, the audit was repeated with Duffy order 7 / RK4-80 (run [44329248687](https://github.com/fabianleonaressi95/theorem/actions/runs/44329248687); all four tests and the full audit passed). The relative changes in total squared risk from order-5 / RK4-40 to order-7 / RK4-80 were:
- D-optimal: (+3.06\times10^{-8}) relative;
- A-optimal: (+2.85\times10^{-8}) relative;
- risk-optimal: (+2.43\times10^{-8}) relative.

The weighted covariance traces are unchanged to the reported floating-point precision; the tiny changes arise in the clean volume-derived bias. This is a strong numerical resolution-sensitivity check at the selected scales, but it is not a rigorous integration-error bound and does not establish convergence of the estimator as the tetrahedral scale tends to zero.


## 16. Candidate-pool and seed robustness audit

The matched-budget comparison was repeated over five deterministic candidate-pool configurations while holding fixed the nonquadratic conformal metric, exact Ricci target, observation model, relative-noise level \(10^{-9}\), exact probe budget 12, selection grid, validation grid, and numerical integration resolutions. Three independent pool-generation seeds were tested at pool size 128; two of those seeds were also tested at size 256. For each repeated seed, the 128-candidate pool is a prefix of the 256-candidate pool, so the size comparison isolates the effect of adding candidates while preserving the original pool.

For each pool, the D-optimal exact 12-subset was rebuilt; the A- and risk-selected exact 12-subsets were then greedily augmented from that pool's common D-optimal six-probe seed. All designs were reevaluated on the same independent 18-scale validation grid. Monte Carlo checks used 2,000 candidate-indexed Gaussian-noise replicas per design and common random numbers among the three designs within each trial.

| Pool configuration | Pool size | D risk squared (×10⁻⁶) | A risk squared (×10⁻⁶) | Risk-selected (×10⁻⁶) | Risk scale | Reduction vs D | Reduction vs A |
|---|---:|---:|---:|---:|---:|---:|---:|
| Seed A | 128 | 1.7895 | 1.6904 | **1.3495** | 0.002866 | 24.59% | 20.16% |
| Seed B | 128 | 2.3996 | 2.3793 | **1.4251** | 0.002866 | 40.61% | 40.11% |
| Seed C | 128 | 1.4374 | 1.7506 | **1.0216** | 0.003419 | 28.93% | 41.65% |
| Seed A | 256 | 1.5068 | 1.3893 | **0.9922** | 0.002866 | 34.15% | 28.59% |
| Seed B | 256 | 1.5411 | 1.4222 | **1.0516** | 0.002866 | 31.76% | 26.06% |

The risk-selected exact design had lower validation-grid risk than both D- and A-selected designs in **all five configurations**. Across the five trials, its mean relative risk reduction was 32.01% versus D-optimal (descriptive across-trial standard deviation 5.98 percentage points; range 24.59–40.61%) and 31.31% versus A-optimal (standard deviation 9.27 percentage points; range 20.16–41.65%). These standard deviations describe only these five deterministic trials; they are not confidence intervals for the population of all candidate pools.

All selected designs had moment rank 6. Risk-selected condition numbers ranged from approximately 2.50 to 3.15. The risk-selected design did not always have the best condition number, and its weighted covariance trace was sometimes higher than those of D- or A-optimal designs. Its lower total risk is therefore driven by a reduction in squared tensor bias that compensates for the variance trade-off, not by a uniform improvement in conditioning or variance alone.

The Monte Carlo mean squared errors at the respective grid minima tracked the analytic risk values: over the 15 design/trial cases, the relative discrepancy was at most about 1.8%, with Monte Carlo standard errors approximately 0.9–1.2% of the analytic risk. This supports the covariance propagation under the declared noise model at the tested scales; it does not establish a general probabilistic theorem.

### Interpretation and limits

This is **positive finite-sample robustness evidence** for the risk-based selection rule across the five tested pools and two pool sizes. Increasing the pool from 128 to 256 lowered the absolute minimum risk for all three criteria in both nested-seed comparisons, but the relative advantage of risk-selection did not increase monotonically. The selected minimizing scale also changed in one of the five trials, so a single universal optimal scale is not supported.

The A- and risk-selected subsets remain greedy augmentations from a D-optimal six-probe seed, not globally optimal combinatorial designs. The test covers five deterministic candidate pools, one manufactured metric, one noise level, and one finite validation grid. It does not establish robustness over arbitrary metrics, noise laws, tetrahedral distributions, or continuous design spaces.

Implementation: [audits/t136_pool_seed_robustness.py](../audits/t136_pool_seed_robustness.py); tests: [tests/test_t136_pool_seed_robustness.py](../tests/test_t136_pool_seed_robustness.py). The focused workflow completed successfully: [run 44330581457](https://github.com/fabianleonaressi95/theorem/actions/runs/44330581457). Its JSON artifact is [t136-pool-seed-robustness](https://github.com/fabianleonaressi95/theorem/actions/runs/44330581457).


### 17.1. Executed initial-seed sensitivity results

The focused workflow completed successfully: [run 44334797224](https://github.com/fabianleonaressi95/theorem/actions/runs/44334797224). Both focused regression tests passed, the full numerical audit completed, and the JSON artifact `t136-initial-seed-robustness` was uploaded (artifact ID 14442120122). The experiment evaluated 30 completed designs: three pools, five initializations per pool (one D-optimal and four random), and two augmentation criteria (A and tensor-risk), with 2,000 Monte Carlo replicas per design.

The following values are validation-grid total squared Frobenius risks, in units of (10^{-6}). “Random min / median / max” summarizes the four random starts, not the D-optimal start.

| Candidate pool (128) | Criterion | D-seed risk | Random min | Random median | Random max | Random starts beating D |
|---|---|---:|---:|---:|---:|---:|
| A | A | 1.6904 | 3.5863 | 4.1093 | 6.4861 | 0/4 |
| A | Risk | 1.3495 | 2.6147 | 2.6880 | 2.8920 | 0/4 |
| B | A | 2.3793 | 2.8422 | 4.3320 | 5.5390 | 0/4 |
| B | Risk | 1.4251 | 1.3585 | 1.7297 | 2.7170 | 1/4 |
| C | A | 1.7506 | 1.5089 | 2.4385 | 2.8772 | 1/4 |
| C | Risk | 1.0216 | 1.4578 | 2.3543 | 3.5279 | 0/4 |

Across all 12 random starts per criterion, one random initialization beat the D-seed result for A-augmentation (1/12) and one for risk-augmentation (1/12). For A, the random/D-seed risk ratio ranged from 0.862 to 3.837 (median 1.821); for risk, it ranged from 0.953 to 3.453 (median 1.922). Thus the D-optimal seed was usually advantageous in this finite experiment, but it was not uniformly best. In particular, pool B contains a random risk-start with a slightly lower validation risk than the D-seed (1.3585 versus 1.4251, in units of (10^{-6})); pool C contains a random A-start with lower risk than the D-seed (1.5089 versus 1.7506).

All 30 completed designs had moment rank 6. The selected validation-grid minimizing scale varied among the tested grid values (0.002403, 0.002866, 0.003419, and 0.004078); this reinforces that the minimizing scale is design-dependent in this manufactured example. The Monte Carlo mean squared errors tracked the analytic risk: the absolute relative discrepancy was at most 2.65% across the 30 cases (mean absolute discrepancy 0.81%). This is a consistency check for the declared Gaussian relative-volume noise model, not a general probabilistic guarantee.

### Interpretation and limits

The initial-seed experiment qualifies, rather than overturns, Section 16. Section 16 supports the risk-selected design's advantage across five candidate-pool configurations **when A/risk greedy augmentation starts from the D-optimal six-probe seed**. Section 17 shows that this advantage is sensitive to initialization: random full-rank seeds usually produced higher validation risk, but occasional random starts performed better. The evidence therefore supports the D-optimal seed as a useful and generally strong initialization in the tested setting, not as a theorem of optimal initialization or as a guarantee that greedy completion reaches the best 12-probe subset.

The random starts are uniform random full-rank six-subsets, not A-optimal six-probe seeds. The experiment does not compare against an independently optimized A-optimal six-probe initialization, does not exhaust all rank-six starts, and does not establish global combinatorial optimality. Its conclusions remain restricted to three fixed pools of 128 candidates, one smooth nonquadratic manufactured metric, one relative-noise level, one finite validation grid, and the stated greedy augmentation procedures.

Implementation: [audits/t136_initial_seed_robustness.py](../audits/t136_initial_seed_robustness.py); tests: [tests/test_t136_initial_seed_robustness.py](../tests/test_t136_initial_seed_robustness.py); workflow: [.github/workflows/t136-initial-seed-robustness.yml](../.github/workflows/t136-initial-seed-robustness.yml). The successful workflow and numerical artifact are linked above.


### 17.2. A-optimal six-probe seed versus D-optimal and random initializations

The follow-up audit adds an independently optimized A-optimal six-probe initialization to the comparison in Section 17.1. It uses the same three fixed candidate pools (128 probes each), smooth nonquadratic manufactured metric, exact Ricci target, relative-volume noise level \\(\\sigma_{\\rm rel}=10^{-9}\\), 12-probe budget, selection and validation grids, and numerical resolutions. For each pool, the A seed is obtained by multi-start best-improvement one-exchange local search minimizing the mean selection-grid objective
\\[
\\Phi_A(S)=\\frac{1}{|\\mathcal G_{\\rm sel}|}\\sum_{r\\in\\mathcal G_{\\rm sel}}
\\operatorname{tr}\\left(W\\operatorname{Cov}(\\widehat R_S(r))\\right).
\\]
The search uses nine starts: the D-optimal six-probe seed and eight objective-blind random full-rank seeds. The resulting seed is a one-swap local optimum among the tested endpoints, not a global optimum over all six-subsets. Four independent objective-blind random full-rank seeds are also retained as controls. Each of the six initializations per pool is independently augmented to 12 probes under both the A and tensor-risk greedy criteria. All 36 completed designs are evaluated on the same independent 18-scale validation grid; Monte Carlo checks use 2,000 replicas per design.

The table reports validation-grid total squared Frobenius risk in units of \\(10^{-6}\\). Random min/median/max refer to the four independent random starts.

| Pool | Augmentation | D-seed | A-local seed | Random min | Random median | Random max | Random starts beating D |
|---|---|---:|---:|---:|---:|---:|---:|
| A | A | 1.6904 | 1.6904 | 3.5863 | 4.1093 | 6.4861 | 0/4 |
| A | Risk | 1.3495 | 1.3791 | 2.6147 | 2.6880 | 2.8920 | 0/4 |
| B | A | 2.3793 | 2.6380 | 2.8422 | 4.3320 | 5.5390 | 0/4 |
| B | Risk | 1.4251 | 1.1714 | 1.3585 | 1.7297 | 2.7170 | 1/4 |
| C | A | 1.7506 | 1.6077 | 1.5089 | 2.4385 | 2.8772 | 1/4 |
| C | Risk | 1.0216 | 0.7858 | 1.4578 | 2.3543 | 3.5279 | 0/4 |

The A-seed search reduced the declared selection-grid A objective relative to the D seed by approximately 0.14%, 18.65%, and 40.00% in pools A, B, and C, respectively. This optimization of the selection objective does not guarantee a lower independent validation risk. Under A-criterion augmentation, the A-local seed produced essentially the same risk as the D seed in pool A, a 10.87% higher risk in pool B, and an 8.16% lower risk in pool C. Under tensor-risk augmentation, it produced a 2.19% higher risk in pool A, a 17.80% lower risk in pool B, and a 23.08% lower risk in pool C.

Across the 12 random starts per augmentation criterion, one random start beat the D-seed result for A augmentation (1/12) and one did so for tensor-risk augmentation (1/12). In pool C, one random A-augmentation start also beat the A-local-seed result (risk 1.5089 versus 1.6077, in units of \\(10^{-6}\\)). Thus neither the D seed nor the A-local seed is uniformly best on the independent validation grid. The A-local seed is particularly helpful for risk augmentation in two of the three tested pools, but the result depends on the candidate pool and the augmentation objective.

Across all 36 completed designs, the largest absolute relative discrepancy between Monte Carlo mean squared error and analytic risk was approximately 1.64%; the mean absolute relative discrepancy was approximately 0.67%. This is a numerical consistency check for the declared independent Gaussian relative-volume-noise model, not a general probabilistic guarantee.

### Interpretation and limits

The follow-up refines Section 17.1. The D-optimal six-probe seed remains a strong baseline: random starts beat it only twice among the 24 random-start/criterion comparisons (one per criterion). However, an independently A-optimized local seed can improve the final tensor-risk design materially for some pools. The evidence does not support a universal preference for D or A initialization. A practical finite-pool procedure should compare both seeds under the predeclared validation objective rather than assume either seed is optimal.

The experiment covers three fixed pools, one manufactured metric, one relative-noise level, four random control starts per pool, and a finite validation grid. The A-seed search is multi-start one-exchange local search; greedy completion is not globally optimal; validation-grid minima are not continuous-scale minima. No global six-subset or 12-subset optimality, probability guarantee, or general geometric stability theorem is established.

Implementation: [audits/t136_initial_seed_robustness.py](../audits/t136_initial_seed_robustness.py); regression tests: [tests/test_t136_initial_seed_robustness.py](../tests/test_t136_initial_seed_robustness.py); workflow: [.github/workflows/t136-pool-seed-robustness.yml](../.github/workflows/t136-pool-seed-robustness.yml). The combined workflow completed successfully: [run 44340176100](https://github.com/fabianleonaressi95/theorem/actions/runs/44340176100). The uploaded artifact is `t136-pool-and-initial-seed-robustness` (artifact ID 14443148778).
