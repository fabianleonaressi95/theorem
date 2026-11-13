# T134 — Conditional coercivity of the curved-P3 C0-IPDG Airy cell form

**Classification:** [P] coercivity is proved conditionally on a mesh-uniform mapped-element trace-inverse estimate and explicit geometric comparability assumptions. The 12-case finite-mesh audit found \(C_{\rm tr,h}\in[9.1545,15.8152]\): \(\alpha=10\) fails the sufficient condition \(\alpha>2C_{\rm tr,h}\) in every case. The two-core solver default is therefore provisionally raised to \(\alpha=40\), which clears the largest observed finite-mesh threshold by about \(8.37\). **This is numerical tuning only:** neither \(\alpha=40\) nor a mesh-uniform trace bound is certified by the finite sweep.

**Implementation audited:** 'scripts/rgs_morandotti_c0_ipdg.py' (P3 Lagrange space on Gmsh order-3 annulus meshes; Hessian volume form; symmetric interior and boundary consistency terms; normal-gradient penalties). The theorem below is stated with the actual code's penalty length scales.

## 1. Discrete space, boundary conditions, and geometric weights

Let \(\Omega\subset\mathbb R^2\) be the annular computational domain and \(\mathcal T_h\) a conforming triangulation by straight or curved triangular cells. Let \(V_h\) be the globally continuous, elementwise mapped P3 Lagrange space. For the homogeneous variation space use
\[
V_h^0=\{v_h\in V_h:\ v_h=0\text{ on both boundary components}\}.
\]
The code prescribes the value trace strongly on both the outer and core boundaries; the normal derivative is imposed weakly. Thus the coercivity estimate is for homogeneous variations, not for the nonhomogeneous lifted cell solutions themselves.

For each cell let \(h_K=\operatorname{diam}(K)\), as represented by the DG0 coefficient 'cell_h' in the implementation. Define the penalty length on an interior facet and on a boundary facet by
\[
\ell_F=
\begin{cases}
\tfrac12(h_{K^+}+h_{K^-}),&F=K^+\cap K^-\text{ interior},\\
h_K,&F\subset\partial K\text{ boundary}.
\end{cases}
\]
These are precisely the scales represented by 'avg(cell_h)' on 'dS' and 'cell_h('+')' on 'ds' in the code. Assume uniform comparability
\[
c_g h_F\le \ell_F\le C_g h_F
\]
with constants independent of the mesh level. Here \(h_F\) is the facet diameter. For curved cells this comparability is an additional geometric condition; it must not be inferred from the target mesh size alone.

Let \(n_F\) be a consistently oriented unit normal on an interior facet. The scalar gradient jump used by UFL 'jump(grad(v), n)' is the sum of the two outward normal derivatives. Set
\[
j_F(v)=
\begin{cases}
\nabla v^+\cdot n^++\nabla v^-\cdot n^-,&F\text{ interior},\\
\nabla v\cdot n,&F\text{ boundary},
\end{cases}
\quad
q_F(v)=
\begin{cases}
\{n_F^TD^2v\,n_F\},&F\text{ interior},\\
n^TD^2v\,n,&F\text{ boundary}.
\end{cases}
\]
The average in \(q_F\) is the arithmetic average of the two normal-normal Hessian traces. Define
\[
D_h(v)^2=\sum_{K\in\mathcal T_h}\|D^2v\|_{L^2(K)}^2,
\quad
J_{h,\ell}(v)^2=\sum_{F\in\mathcal F_h^i\cup\mathcal F_h^b}
\ell_F^{-1}\|j_F(v)\|_{L^2(F)}^2,
\]
and
\[
H_{h,\ell}(v)^2=\sum_{F\in\mathcal F_h^i\cup\mathcal F_h^b}
\ell_F\|q_F(v)\|_{L^2(F)}^2.
\]
Here \(\mathcal F_h^b\) includes both the outer and core boundary facets.

## 2. Uniform mapped-P3 trace-inverse hypothesis

Assume there is a constant \(C_{\rm tr}\), independent of the mesh level, such that
\[
\boxed{H_{h,\ell}(v)^2\le C_{\rm tr}D_h(v)^2
\qquad\forall v\in V_h^0.}\tag{T134.1}
\]
This is the precise trace estimate needed by the coercivity proof, and it includes both interior and boundary facets. Its constant depends on the polynomial degree, the shape-regularity bounds, the mapped-element regularity bounds, and the uniform facet-weight comparability constants. For a fixed-degree family (here P3), these dependencies are fixed and the required assertion is that the resulting constant is independent of the mesh level h. For a variable-degree method, the degree dependence must be tracked explicitly and the penalty must satisfy \(\alpha(p)>2C_{\rm tr}(p)\); no universal p-scaling is asserted here. For straight affine triangles and fixed polynomial degree it follows from the polynomial inverse-trace inequality and shape regularity, after scaling. For curved P3 cells the physical Hessian of a mapped polynomial is generally not a polynomial in physical coordinates. Therefore one must additionally assume a uniformly regular family of element maps: uniformly bounded scaled derivatives of the maps through the order entering the physical Hessian, uniformly bounded inverse Jacobians after scaling, and uniform nondegeneracy of the Jacobian determinant. Together with the weight comparability above, these conditions give a uniformly bounded family of pullback trace operators on the finite-dimensional mapped P3 reference space and hence (T134.1).

The trace quantity here is the normal-normal Hessian trace \(n^TD^2v,n\), not the distinct quantity \(\partial_n\Delta v\). This paragraph explains a sufficient route to (T134.1); it does **not** claim that the current Gmsh meshes have already been shown to satisfy those uniform map bounds. An alternative direct proof or verified bound of (T134.1) for the generated mesh family is acceptable.
This is the precise trace estimate needed by the coercivity proof. For straight affine triangles and fixed polynomial degree it follows from the polynomial inverse-trace inequality and shape regularity, after scaling. For curved P3 cells the physical Hessian of a mapped polynomial is generally not a polynomial in physical coordinates. Therefore one must additionally assume a uniformly regular family of element maps: uniformly bounded scaled derivatives of the maps through the order entering the physical Hessian, uniformly bounded inverse Jacobians after scaling, and uniform nondegeneracy of the Jacobian determinant. Together with the weight comparability above, these conditions give a uniformly bounded family of pullback trace operators on the finite-dimensional mapped P3 reference space and hence (T134.1).

This paragraph explains a sufficient route to (T134.1); it does **not** claim that the current Gmsh meshes have already been shown to satisfy those uniform map bounds. An alternative direct proof or verified bound of (T134.1) for the generated mesh family is acceptable.

## 3. Bilinear form and theorem

The homogeneous bilinear form assembled by the code is
\[
\begin{aligned}
a_{h,\ell}(u,v)={}&
\sum_K\int_K D^2u:D^2v\\
&-\sum_{F\in\mathcal F_h^i}
\left(\int_F q_F(u)j_F(v)+\int_F q_F(v)j_F(u)\right)\\
&-\sum_{F\in\mathcal F_h^b}
\left(\int_F q_F(u)j_F(v)+\int_F q_F(v)j_F(u)\right)\\
&+\alpha\sum_{F\in\mathcal F_h^i\cup\mathcal F_h^b}
\ell_F^{-1}\int_F j_F(u)j_F(v).
\end{aligned}
\]
On boundary facets this is exactly the 'ds' consistency and penalty structure; on interior facets it is the 'dS' structure. The code's 'alpha/avg(cell_h)' and 'alpha/cell_h('+')' are represented by \(\alpha/\ell_F\).

**Theorem.** If (T134.1) holds with a mesh-independent constant \(C_{\rm tr}>0\), then for
**Theorem.** If (T134.1) holds with a mesh-independent constant \(C_{\rm tr}\), then for
\[
\boxed{\alpha>2C_{\rm tr}}
\]
one has
\[
\boxed{
a_{h,\ell}(v,v)\ge
\frac12D_h(v)^2+(\alpha-2C_{\rm tr})J_{h,\ell}(v)^2
\qquad\forall v\in V_h^0.}
\]
Consequently,
\[
a_{h,\ell}(v,v)\ge c_{\rm coer}\,
\|v\|_{2,h,\ell}^2,
\qquad
c_{\rm coer}=\min\left\{\frac12,\alpha-2C_{\rm tr}\right\}>0,
\]
where \(\|v\|_{2,h,\ell}^2=D_h(v)^2+J_{h,\ell}(v)^2\). This is coercivity in the stated mesh-dependent seminorm. If the homogeneous value boundary conditions eliminate the affine kernel, the corresponding discrete Poincare/Friedrichs inequality upgrades this seminorm to control the full discrete \(H^2\)-type norm.
Thus the form is coercive in the mesh-dependent seminorm
\[
\|v\|_{2,h,\ell}^2=D_h(v)^2+J_{h,\ell}(v)^2.
\]
If the homogeneous value boundary conditions eliminate the affine kernel, the corresponding discrete Poincare/Friedrichs inequality upgrades this seminorm to control the full discrete \(H^2\)-type norm.

## 4. Proof

For each facet, use the weighted Cauchy-Schwarz inequality and then sum over all interior and boundary facets:
\[
\begin{aligned}
\left|\sum_F\int_Fq_F(v)j_F(v)\right|
&\le
\left(\sum_F\ell_F\|q_F(v)\|_{L^2(F)}^2\right)^{1/2}
\left(\sum_F\ell_F^{-1}\|j_F(v)\|_{L^2(F)}^2\right)^{1/2}\\
&=H_{h,\ell}(v)J_{h,\ell}(v).
\end{aligned}
\]
The two symmetric consistency contributions in \(a_{h,\ell}(v,v)\) therefore have absolute value at most \(2H_{h,\ell}(v)J_{h,\ell}(v)\). By (T134.1) and Young's inequality,
\[
2H_{h,\ell}(v)J_{h,\ell}(v)
\le \eta H_{h,\ell}(v)^2+\eta^{-1}J_{h,\ell}(v)^2
\le \eta C_{\rm tr}D_h(v)^2+\eta^{-1}J_{h,\ell}(v)^2.
\]
Choose \(\eta=(2C_{\rm tr})^{-1}\). Then
\[
2H_{h,\ell}(v)J_{h,\ell}(v)
\le2\sqrt{C_{\rm tr}}D_h(v)J_{h,\ell}(v)
\le\frac12D_h(v)^2+2C_{\rm tr}J_{h,\ell}(v)^2.
\]
Since
\[
a_{h,\ell}(v,v)=D_h(v)^2
-2\sum_F\int_Fq_F(v)j_F(v)
+\alpha J_{h,\ell}(v)^2,
\]
we obtain
\[
a_{h,\ell}(v,v)\ge
\frac12D_h(v)^2+(\alpha-2C_{\rm tr})J_{h,\ell}(v)^2.
\]
The condition \(\alpha>2C_{\rm tr}\) makes both coefficients positive. This proves the theorem. \(\square\)

## 5. What is verified against the implementation — and what is not

The source-level comparison establishes the following algebraic correspondence:
- 'V=fem.functionspace(mesh,("Lagrange",3))' gives the globally continuous P3 space;
- 'Hu=grad(grad(u))' and 'Hun=dot(dot(Hu,n),n)' give the Hessian and normal-normal Hessian;
- 'jump(grad(u),n)' gives the sum of outward normal derivatives on an interior facet;
- 'avg(Hun)' supplies the arithmetic average in the interior consistency term;
- the 'dS' and 'ds' terms are symmetric in trial and test functions;
- the penalty weights are \(\alpha/\operatorname{avg}(h_K)\) internally and \(\alpha/h_K\) on the boundary;
- both boundary components receive strong value constraints, while the normal derivative is weakly imposed.

This is a source inspection, not an executed assembly-equivalence test. In particular, it does not establish a uniform trace constant or prove coercivity of every assembled matrix.

The following remain open:
1. establish (T134.1) uniformly for the actual Gmsh curved P3 mesh family, including bounds on scaled element-map derivatives and inverse Jacobians;
2. verify the geometric comparability constants between \(\ell_F\) and facet diameters;
3. prove the boundary constraints eliminate the affine kernel on the annulus in the exact discrete space;
4. establish a mesh-uniform upper bound for \(C_{\rm tr}\); the finite sweep rejects \(\alpha=10\), while the provisional two-core value \(\alpha=40\) has not been proved to exceed \(2C_{\rm tr}\) uniformly;
5. add an assembly-level regression comparing the UFL form with the displayed bilinear form, including facet orientation and boundary contributions.

The finite audit comprises 12 generated meshes (two core separations, two target sizes, three seeds). Its largest observed value is \(C_{\rm tr,h}=15.8151566\), so the sufficient finite-mesh threshold is \(2C_{\rm tr,h}=31.6303132\) for that case. Thus \(\alpha=10\) fails on the entire tested set, while \(\alpha=40\) exceeds every observed finite-mesh threshold. The two-core solver default was changed to 40 as a provisional numerical safeguard. This does not bound \(\sup_h C_{\rm tr,h}\), certify the curved-map hypotheses, or prove coercivity uniformly; \(\alpha=40\) remains uncertified at theorem level. Nor does T134 prove consistency error estimates, approximation estimates, convergence of cell solutions, convergence of the multi-core interaction matrix, or a continuum distance law. Those require separate analysis.

## 6. Relation to T133

T133 concerns the finite-dimensional constrained quadratic minimization problem and applies only after the assembled energy matrix is SPD and the constraint matrix has full row rank. T134 is a separate coercivity argument for the biharmonic C0-IPDG cell form. Neither theorem supplies the hypotheses of the other automatically.


## 7. Extended refinement audit (2026-11-13)

A follow-up finite-mesh study is configured in
`.github/workflows/morandotti-trace-constant.yml`. In addition to the
previous target sizes (h=0.08,0.045), it now includes (h=0.03,0.025),
with the same two core separations and three independent mesh seeds. The
curved-map Jacobian diagnostic samples a 16-subdivision triangular reference
grid (153 points per cell), rather than the previous 8-subdivision grid.

This extension is a **diagnostic refinement**, not an all-points geometry
certificate. Positivity at finitely many reference points does not prove
(det J_K>0) throughout each curved cell, and a finite sequence of
generalized eigenvalues does not prove
(sup_h C_{\rm tr,h}<\infty). The new run must complete before its
numerical values are recorded here. The analytical mapped-element derivative,
inverse-Jacobian, nondegeneracy, and facet-weight comparability bounds remain
open obligations.

**Current status:** conditional coercivity proof; initial 12-case finite-mesh
audit completed; extended 24-case refinement audit configured and pending.
No uniform trace constant or unconditional coercivity claim is made.


## 8. Statistical diagnostics added to the refinement workflow

The extended audit now records exploratory Gaussian least-squares model
comparisons using AIC, AICc, and BIC for three candidate trends in the
seed-level estimates: a constant, a power law (a h^p), and an asymptotic
finite-limit model (C_\infty+a h^p). It also performs a 2,000-replicate
seed-stratified nonparametric bootstrap, resampling the independent mesh-seed
realizations within each target mesh size and reporting a percentile interval
for the fitted (C_\infty).

These are model-selection and sampling-uncertainty diagnostics only. AIC/BIC
rank the specified candidate models conditional on the observed data; they do
not establish that the candidate family is correct. With three seeds per
mesh level, bootstrap intervals are necessarily coarse and conditional on
the mesh generator. Neither a preferred finite-limit model nor a bounded
bootstrap interval proves a uniform trace inequality. The analytic
mesh-uniform mapped-element estimate remains open.


## 9. Statistical audit corrections and grouped validation (2026-11-13)

The Gaussian information-criterion calculation counts the residual-variance
parameter in addition to the mean-model parameters. The report now includes
AIC, AICc, BIC, and HQIC. AICc is undefined (reported as infinity) when
\(n \leq k+1\), where \(k\) includes the estimated variance parameter.

The resampling unit is the **mesh-seed trajectory**, not an individual
seed-by-resolution observation. The paired cluster bootstrap resamples whole
seed trajectories across all target mesh sizes, preserving dependence induced
by reusing a seed across resolutions. The validation diagnostic is
leave-one-seed-block-out cross-validation; the jackknife deletes one complete
seed block at a time. Both are reported as exploratory because the current
configuration has only three independent seed blocks.

DIC, WAIC, Bayes factors, and INLA are not included: the current audit is a
frequentist nonlinear least-squares analysis, with no posterior samples,
pointwise posterior log-likelihood, explicit prior model, or latent-Gaussian
Bayesian hierarchy. Mallows' \(C_p\) is not suitable for the current nonlinear
scaling fits without a justified linear-regression formulation and common
variance estimate. LASSO, Ridge, and Elastic Net are regularizers, not
standalone model-comparison criteria, and there is no justified predictor
matrix requiring them here.

**Interpretation limits:** AIC-family scores compare only the specified
candidate trends under the Gaussian residual model. Grouped cross-validation,
jackknife, and bootstrap quantify sensitivity to the available seed
realizations; with three seed blocks their uncertainty assessment is coarse.
None of these statistical procedures proves
\(\sup_h C_{\rm tr,h}<\infty\), certifies curved-cell Jacobian positivity at
every point, or replaces the analytical mapped-element trace estimate.


## 10. Analytical mapped-element trace lemma (proof; geometric hypothesis isolated)

This section supplies the analytical argument behind (T134.1), rather than
inferring it from the generalized-eigenvalue experiments.

### 10.1 Uniform class of cubic element maps

For every cell \(K\), let
\[
F_K:\widehat K\longrightarrow K,\qquad
x=x_K+h_K\widehat F_K(\widehat x),
\]
where \(\widehat K\) is the fixed reference triangle and \(h_K=\operatorname{diam}K\).
The isoparametric Gmsh P3 geometry makes \(\widehat F_K\) a polynomial map of
degree at most three. Assume the normalized maps belong to one fixed compact
admissible class \(\mathfrak F\) of cubic maps, with
\[
\sup_{\widehat K}\|D\widehat F\|\le M_1,\qquad
\sup_{\widehat K}\|(D\widehat F)^{-1}\|\le M_{-1},\qquad
\sup_{\widehat K}\|D^2\widehat F\|\le M_2,
\]
and
\[
0<j_0\le |\det D\widehat F(\widehat x)|
\le j_1<\infty
\quad(\widehat x\in\widehat K).
\tag{10.1}
\]
Compactness here is in the finite-dimensional coefficient space of cubic
maps; the lower determinant bound excludes degenerate maps. These constants
must be independent of \(K\), \(h\), and the seed. Assume also the usual
uniform shape-regularity/facet comparability: for every facet \(F\subset
\partial K\), \(c_f h_K\le h_F\le C_f h_K\), and neighboring cell diameters
are comparable by constants independent of the mesh.

### 10.2 Local mapped-P3 trace inequality

**Lemma.** Under (10.1), there is a constant \(C_{\rm loc}\), depending only
on \(\widehat K\), the degree \(3\), and \(M_1,M_{-1},M_2,j_0,j_1\), such that
for every mapped P3 function \(v=\widehat v\circ F_K^{-1}\),
\[
h_K\|D_x^2v\|_{L^2(\partial K)}^2
\le C_{\rm loc}\|D_x^2v\|_{L^2(K)}^2.
\tag{10.2}
\]
In particular the same estimate holds with \(D_x^2v\) replaced on each
facet by its scalar normal-normal component.

**Proof.** Write \(J=D F_K=h_KD\widehat F_K\). The chain rule gives
\[
\nabla_xv=J^{-T}\nabla_{\widehat x}\widehat v,
\]
and, componentwise,
\[
D_x^2v
=J^{-T}D_{\widehat x}^2\widehat v\,J^{-1}
+\sum_{a=1}^2
(\partial_{\widehat x_a}\widehat v)\,
D_x^2(F_K^{-1})_a.
\tag{10.3}
\]
The inverse-function identity yields
\[
D_x^2(F_K^{-1})_a
=-J^{-T}\left(\sum_{b=1}^2
(\partial_{x_b}F_{K,a})\,D_{\widehat x}^2F_{K,b}\right)J^{-1},
\]
equivalently the standard second-derivative formula for the inverse map.
The scaled bounds in (10.1) therefore bound the coefficients in (10.3)
uniformly after extracting the expected factor \(h_K^{-2}\).
The volume Jacobian is bounded above and below by fixed multiples of
\(h_K^2\); the surface Jacobian is bounded above and below by fixed multiples
of \(h_K\). Thus the left and right sides of (10.2), after pullback and
cancellation of their common scaling, are quadratic forms on the fixed
finite-dimensional space \(\mathbb P_3(\widehat K)\).

The kernel of the volume quadratic form is exactly
\[
\mathcal N_F=\{\widehat v:\widehat v\circ F_K^{-1}
\text{ is affine in }x\}
=\operatorname{span}\{1,F_{K,1},F_{K,2}\}.
\]
The boundary Hessian quadratic form has the same kernel: an affine physical
function has zero Hessian everywhere. On the quotient
\(\mathbb P_3(\widehat K)/\mathcal N_F\), the volume form is positive
definite. Its smallest eigenvalue is bounded away from zero uniformly over
the compact admissible map class: otherwise a convergent sequence of
normalized maps and unit quotient vectors would produce a nonzero quotient
vector with zero volume Hessian, contradicting the stated kernel. The
boundary quadratic form has uniformly bounded largest eigenvalue by the
same compactness and the surface-Jacobian bounds. Their quotient is
therefore uniformly bounded. This proves (10.2). Finally,
\(|n^TD_x^2v\,n|\le |D_x^2v|\), so the normal-normal version follows.
\(\square\)

### 10.3 Assembly over facets

For an interior facet \(F=K^+\cap K^-\),
\[
|\{n^TD^2v\,n\}|^2
\le \tfrac12\bigl(|D^2v^+|^2+|D^2v^-|^2\bigr).
\]
For a boundary facet the same estimate holds with its sole adjacent cell.
Using \(\ell_F\simeq h_F\simeq h_K\), applying (10.2) cell by cell, and
noting that a triangle has three edges (uniformly bounded facet incidence),
gives
\[
\begin{aligned}
H_{h,\ell}(v)^2
&=\sum_{F\in\mathcal F_h^i}\ell_F
 \|\{n^TD^2v\,n\}\|_{L^2(F)}^2
 +\sum_{F\in\mathcal F_h^b}\ell_F
 \|n^TD^2v\,n\|_{L^2(F)}^2\\
&\le C_{\rm tr}\sum_{K\in\mathcal T_h}
 \|D^2v\|_{L^2(K)}^2
=C_{\rm tr}D_h(v)^2,
\end{aligned}
\]
where \(C_{\rm tr}\) depends only on the uniform map-class and mesh
comparability constants, not on \(h\), the cell, or the seed. This is
(T134.1).

### 10.4 Coercivity consequence

For the implemented symmetric form,
\[
a_{h,\ell}(v,v)=D_h(v)^2
-2\sum_F(q_F(v),j_F(v))_F
+\alpha J_{h,\ell}(v)^2.
\]
Weighted Cauchy--Schwarz and the just-proved trace estimate imply
\[
2\left|\sum_F(q_F(v),j_F(v))_F\right|
\le 2H_{h,\ell}(v)J_{h,\ell}(v)
\le 2\sqrt{C_{\rm tr}}D_h(v)J_{h,\ell}(v).
\]
The scalar inequality \(2\sqrt{C_{\rm tr}}\,D J
\le \tfrac12D^2+2C_{\rm tr}J^2\) then gives
\[
\boxed{a_{h,\ell}(v,v)\ge
\tfrac12D_h(v)^2+(\alpha-2C_{\rm tr})J_{h,\ell}(v)^2.}
\]
Hence \(\alpha>2C_{\rm tr}\) proves coercivity in
\(D_h^2+J_{h,\ell}^2\), uniformly in \(h\), provided the uniform geometry
hypotheses above hold.

### 10.5 Exact logical status for the present Gmsh generator

The local lemma and its assembly are analytical proofs. They do **not** by
themselves prove that the current generator satisfies (10.1) uniformly.
The generator constructs OCC disks, asks Gmsh for cubic high-order optimized
meshes, inserts six seed-dependent interior points, and then moves geometry
nodes by the sampled Wendland displacement. The source currently checks
positive signed corner areas and samples \(\det J\) on a finite barycentric
grid. Neither check establishes a lower bound for \(\det D\widehat F_K\) at
every reference point, nor uniform bounds on \(D\widehat F_K\),
\((D\widehat F_K)^{-1}\), and \(D^2\widehat F_K\) over all refinement levels
and seeds.

Accordingly, the result now proved is:

* **Analytically proved:** the mesh-uniform mapped-P3 trace inequality and
  T134 coercivity for every family in the explicitly defined compact
  admissible geometry class (10.1), with uniform facet comparability.
* **Not yet proved for the actual generated family:** that all Gmsh meshes
  produced by the current algorithm, for every refinement level and allowed
  seed, lie in one such class with explicit constants.
* **Not certified:** that the numerical choice \(\alpha=40\) exceeds
  \(2C_{\rm tr}\) for that entire generated family.

To upgrade the second bullet, the generator needs a deterministic geometric
regularity condition (or a certified rejection rule with fixed uniform
bounds) on every normalized cubic map, including a global polynomial
certificate for \(\det D\widehat F_K>0\). Sampling, AIC, bootstrap, and
cross-validation cannot replace that condition.
