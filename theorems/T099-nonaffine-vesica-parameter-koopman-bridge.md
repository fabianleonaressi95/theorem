# T099 — Non-affine vesica observables and the parameter-Koopman bridge

**Date:** 11 November 2026  
**Status:** exact geometric definitions and shape-derivative identities under the stated transversality hypotheses; exact RGS finite-dimensional parameter sensitivity inherited from T091; parameter-Koopman construction conditional on a differentiable continuation family. A physical-time Koopman flow and an EDMD spectrum are **not** claimed.  
**Dependencies:** T091 (interaction-matrix variation/residual sensitivity), T097 (gradient/mismatch kinematics), T098 (two-circle geometric generator), MORANDOTTI_ANISOTROPY.md and the existing two-core separation sweep.

## 1. Terminology and affine classification

Let
\[
E_i(p)=\{x\in\mathbb R^2:(x-c_i(p))^T\Sigma_i(p)^{-1}(x-c_i(p))\leq1\},
\qquad \Sigma_i(p)\in\operatorname{Sym}^+(2).
\]
Define the common region
\[
V(p)=E_1(p)\cap E_2(p).
\]
In this record, **two-ellipse lens** or **generalized vesica** means precisely this intersection. “Non-affine pair” is reserved for a pair that cannot be mapped simultaneously to two circular disks by one common affine map.

A common affine map \(x=Ly+a\) makes both ellipses circular (possibly with different radii) if and only if
\[
\Sigma_2=\lambda\Sigma_1\quad\text{for some }\lambda>0.
\]
Indeed, the transformed shape matrices are \(L^{-1}\Sigma_iL^{-T}\); both can be scalar multiples of the identity exactly when the original matrices are proportional. The classical equal-radius vesica is the stricter case \(\Sigma_1=\Sigma_2\), with the appropriate centre separation. Thus \(\Sigma_1\ne\Sigma_2\) alone does not prove non-affinity: proportional but unequal matrices are still a common-shape affine pair. The genuinely non-affine regime is that \(\Sigma_1,\Sigma_2\) are not proportional.

For every invertible affine map \(T(x)=Lx+a\),
\[
T(E_1\cap E_2)=T(E_1)\cap T(E_2),\qquad
|T(V)|=|\det L|\,|V|.
\]
Incidence and tangency are preserved; Euclidean distances, angles and curvature are not.

## 2. Geometric observables

For the lens \(V(p)\), define its area, first raw moment and second raw moment:
\[
A(p)=\int_{V(p)}1\,dx,\qquad
m(p)=\int_{V(p)}x\,dx,\qquad
S(p)=\int_{V(p)}xx^T\,dx.
\]
When \(A(p)>0\), define
\[
\bar x(p)=\frac{m(p)}{A(p)},\qquad
C_V(p)=\frac{S(p)}{A(p)}-\bar x(p)\bar x(p)^T.
\]
The full symmetric tensor \(C_V\), not only its trace or eigenvalue contrast, is retained as the geometric anisotropy observable.

Under \(T(x)=Lx+a\), these moments transform exactly as
\[
A_T=|\det L|A,\quad
\bar x_T=L\bar x+a,\quad
C_T=LC_VL^T.
\]
These formulas distinguish affine covariance from Euclidean metric invariance.

## 3. Exact shape derivatives for a differentiable two-ellipse family

Assume \(c_i,\Sigma_i\) are \(C^1\) in a scalar continuation parameter \(p\), the two ellipse boundaries intersect transversely, and the intersection topology is locally constant. Let
\[
\Gamma_i(p)=\partial E_i(p)\cap\operatorname{int}E_{3-i}(p)
\]
be the active boundary arcs of the lens. Let \(v_i(x,p)\) be the boundary velocity of \(\partial E_i(p)\), and \(n_i\) its outward unit normal. The Reynolds transport theorem gives
\[
\boxed{A'(p)=\sum_{i=1}^2\int_{\Gamma_i(p)}v_i\cdot n_i\,ds.}
\tag{99.1}
\]
\[
\boxed{m'(p)=\sum_{i=1}^2\int_{\Gamma_i(p)}x\,(v_i\cdot n_i)\,ds.}
\tag{99.2}
\]
\[
\boxed{S'(p)=\sum_{i=1}^2\int_{\Gamma_i(p)}xx^T\,(v_i\cdot n_i)\,ds.}
\tag{99.3}
\]
Consequently,
\[
\bar x'=\frac{m'-A'\bar x}{A},\qquad
C_V'=\frac{S'}A-\frac{A'}A\frac SA-\bar x'\bar x^T-\bar x(\bar x')^T.
\tag{99.4}
\]
These identities are exact while the transversality and fixed-topology hypotheses hold. At tangency, birth/death of intersection arcs, or a topology change, differentiability may fail; one-sided derivatives or a separate local analysis are then required.

For example, write a boundary parametrization as
\[
X_i(\theta,p)=c_i(p)+\Sigma_i(p)^{1/2}
\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix}.
\]
Its boundary velocity is \(\partial_pX_i\); only its normal component enters (99.1)–(99.3). This gives a direct numerical route to the geometric derivative without replacing one ellipse by an ad hoc effective circle.

## 4. The existing RGS parameter dynamics

The repository already contains a finite-dimensional **parameter-sensitivity law**, not an autonomous physical-time evolution. In T091 the reconstructed coefficient vector satisfies
\[
M(p)a(p)=\Phi(p),\qquad
a'(p)=M(p)^{-1}\bigl(\Phi'(p)-M'(p)a(p)\bigr).
\tag{99.5}
\]
For a residual \(r(p)=C(p)a(p)-g(p)\),
\[
r'=C'a+C M^{-1}(\Phi'-M'a)-g'.
\tag{99.6}
\]
When \(\Phi,C,g\) are fixed, this reduces to \(r'=-CM^{-1}M'a\). These are exact finite-dimensional identities under differentiability and invertibility of \(M(p)\), inherited from T091; they are not a new constitutive law.

The existing Morandotti separation experiment supplies a natural continuation coordinate \(p=d\), the distance between the two core centres. It reuses a fixed reference mesh and deforms its coordinates as the target separation changes. Its currently documented values \(d\in\{0.48,0.56,0.64,0.72\}\) are a one-mesh screening sweep. They do not establish a continuum distance law or a physical clock.

For the two-ellipse extension, the state may be augmented to
\[
Z(p)=\big(c_1,c_2,\Sigma_1,\Sigma_2,a,r,A,m,S\big)(p).
\]
Its derivative is assembled from (99.1)–(99.6), once the ellipse path and the corresponding RGS matrix/source/trace data have been supplied. In particular, the shape path \(\Sigma_i(p),c_i(p)\) must be specified; the existing circular-core separation sweep does not by itself supply arbitrary evolving ellipse matrices.

## 5. Parameter-Koopman operator

Let \(Z:I\to\mathcal X\) be a \(C^1\) continuation curve on the augmented state space, with tangent \(F_p(Z(p))=Z'(p)\). For an observable \(f:\mathcal X\to\mathbb R\) differentiable along the curve, define the **parameter-Koopman pullback**
\[
(U_{p,s}f)(Z(p))=f(Z(p+s)),
\]
whenever \(p,p+s\in I\). Its infinitesimal generator along the continuation is
\[
\boxed{(\mathcal L_{K,p}f)(Z(p))
=\frac{d}{dp}f(Z(p))
=Df(Z(p))[Z'(p)].}
\tag{99.7}
\]
For the geometric observables \(A,m,S,\bar x,C_V\), the derivatives are given by (99.1)–(99.4); for the RGS coefficient and residual observables they are given by (99.5)–(99.6). Thus the Koopman action on these observables is determined by the existing parameter-sensitivity law plus the exact shape derivatives, rather than by fitting an unrelated vector field.

**Scope warning.** Equation (99.7) is a Koopman-type evolution in the continuation parameter \(p\), not a physical-time Koopman semigroup. A physical-time flow requires an independently specified law \(\dot p\) and evolution equations for all state variables. No such autonomous time law is asserted in T091, T097 or the current Morandotti separation benchmark.

## 6. EDMD protocol and evidence gate

An EDMD approximation may be built from snapshots \(Z(p_k)\) and a declared dictionary \(\{\psi_j\}_{j=1}^N\), using paired data
\[
\Psi_X=[\psi_j(Z(p_k))]_{j,k},\qquad
\Psi_Y=[\psi_j(Z(p_k+\Delta p))]_{j,k},
\]
and the least-squares matrix
\[
K_{\rm EDMD}=\Psi_Y\Psi_X^\dagger.
\]
For this application the dictionary must include, at minimum, the area, centred first moment, all independent entries of \(C_V\), the longitudinal/transverse RGS residuals, and the signed Frank–Burgers mixed-tensor components. The dictionary and scaling must be fixed across mesh levels; otherwise apparent spectral changes may be dictionary/normalization artefacts.

The currently documented four-separation sweep at one mesh size is insufficient to claim a stable EDMD spectrum. Before reporting eigenvalues, collect a denser continuation path, repeat it on multiple mesh sizes, verify the shape-derivative identities against finite differences, and report singular values/conditioning of \(\Psi_X\), held-out prediction error, and spectral stability under dictionary and sampling changes. No Koopman eigenvalue, mode, or EDMD convergence result is claimed here.

## 7. Exact triangular benchmark used in the preceding geometric exploration

Let
\[
\Delta_h=\{(x,y):|x|\leq1,\ 0\leq y\leq h(1-|x|)\},\qquad
D=\{x^2+y^2\leq1\}.
\]
For \(0<h\leq1\), convexity of \(D\) and the fact that all three triangle vertices lie in \(D\) imply \(\Delta_h\subset D\), so
\[
A_\triangle(h)=h.
\]
For \(h>1\), put \(q=h(h-1)/(h^2+1)\). On the right half-plane the upper boundary of the intersection is \(\min(\sqrt{1-x^2},h(1-x))\), with the two functions crossing at \(x=q\). Hence
\[
\boxed{
A_\triangle(h)=q\sqrt{1-q^2}+\arcsin q+h(1-q)^2,\quad h>1.
}
\tag{99.8}
\]
In particular \(A_\triangle(1)=1\), \(A_\triangle(\sqrt3)\simeq1.4312041746394546\), and
\[
\lim_{h\to\infty}A_\triangle(h)=\frac\pi2.
\]
This is an exact benchmark for a triangle–disk overlap. It is **not** the area formula for a two-ellipse lens and is not used as a substitute for (99.1)–(99.3).

## 8. Classification

- **PROVED:** common-affine classification by proportional shape matrices; affine transformation laws for area, centroid and covariance; shape-derivative identities under transversality/fixed topology; triangular benchmark (99.8).
- **INHERITED, EXACT UNDER HYPOTHESES:** RGS coefficient and residual parameter sensitivities (99.5)–(99.6), from T091.
- **DEFINED, CONDITIONAL ON A CONTINUATION PATH:** parameter-Koopman pullback and generator (99.7).
- **OPEN:** extraction of an anisotropic ellipse path and its \(M,\Phi,C,g\) from the same RGS two-core computation; multi-mesh EDMD data and spectral stability; any physical-time Koopman dynamics; constitutive energy of the non-affine lens; continuum convergence.

**Editorial rule:** do not call the parameter \(d\) time, do not identify the Airy stress with the kinematic gradient, and do not infer a physical fusion/interaction energy from lens area alone.

**FLN**
