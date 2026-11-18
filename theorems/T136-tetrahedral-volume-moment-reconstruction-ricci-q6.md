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
