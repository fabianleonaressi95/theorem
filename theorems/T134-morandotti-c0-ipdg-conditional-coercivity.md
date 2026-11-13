# T134 — Conditional coercivity of the curved-P3 C0-IPDG Airy cell form

**Classification:** [P] coercivity is proved conditionally: the mesh-uniform mapped-P3 trace estimate is derived from an explicit compact coefficient class of admissible element maps and quantified facet/element comparability. The actual Gmsh family has not yet been proved to satisfy those all-level hypotheses. The 12-case finite-mesh audit found \(C_{\rm tr,h}\in[9.1545,15.8152]\): \(\alpha=10\) fails the sufficient condition \(\alpha>2C_{\rm tr,h}\) in every case. The two-core solver default is therefore provisionally raised to \(\alpha=40\), which clears the largest observed finite-mesh threshold by about \(8.37\). **This is numerical tuning only:** neither \(\alpha=40\) nor a mesh-uniform trace bound is certified by the finite sweep.

**Implementation audited:** 'scripts/rgs_morandotti_c0_ipdg.py' (P3 Lagrange space on Gmsh order-3 annulus meshes; Hessian volume form; symmetric interior and boundary consistency terms; normal-gradient penalties). The theorem below is stated with the actual code's penalty length scales.

## 1. Discrete space, boundary conditions, and geometric weights

Let \(\Omega\subset\mathbb R^2\) be the two-core annular computational domain and \(\mathcal T_h\) a conforming triangulation by straight or curved triangular cells. Its boundary consists of the outer component \(\Gamma_{\rm out}\) and the two core components \(\Gamma_{c,1},\Gamma_{c,2}\). Let \(V_h\) be the globally continuous, elementwise mapped P3 Lagrange space, and set
\[
V_h^0=\{v_h\in V_h: v_h|_{\Gamma_{\rm out}}=v_h|_{\Gamma_{c,1}}=v_h|_{\Gamma_{c,2}}=0\}.
\]
These homogeneous Dirichlet traces are imposed strongly by zero boundary trace degrees of freedom on all three components. The normal derivative is imposed weakly through symmetric consistency and penalty terms on every boundary facet. The estimate is for homogeneous variations, not the nonhomogeneous lifted cell solutions.

For each cell let \(h_K=\operatorname{diam}(K)\), as represented by the DG0 coefficient 'cell_h' in the implementation. Define the penalty length on an interior facet and on a boundary facet by
\[
\ell_F=
\begin{cases}
\tfrac12(h_{K^+}+h_{K^-}),&F=K^+\cap K^-\text{ interior},\\
h_K,&F\subset\partial K\text{ boundary}.
\end{cases}
\]
These are precisely the scales represented by 'avg(cell_h)' on 'dS' and 'cell_h('+')' on 'ds' in the code. Assume there are constants \(c_0,c_1>0\), independent of cell, level, and seed, such that
\[
c_0h_K\le\ell_F\le c_1h_K
\qquad(F\subset\partial K).
\tag{1.1}
\]
For an interior facet this is required with respect to both incident cells; it therefore implies a uniform neighboring-cell size ratio. This is the explicit facet/element comparability used below, not an inference from nominal target mesh size.

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

## 2. Uniform mapped-P3 trace lemma

Let \(\widehat K\) be the fixed reference triangle. Fix a vertex \(\hat x_0\), and write each normalized cubic map in the ten-monomial basis of \(\mathbb P_3(\widehat K)\):
\[
\widehat F_a(\hat x)=
\left(\sum_{|\beta|\le3}a_{1,\beta}\hat x^\beta,
      \sum_{|\beta|\le3}a_{2,\beta}\hat x^\beta\right),
\qquad \widehat F_a(\hat x_0)=0.
\]
The coefficient vector belongs to \(\mathbb R^{20}\) and satisfies the two normalization constraints. Assume that all normalized maps from every cell, level, and allowed seed belong to one fixed compact coefficient set \(K_0\subset\mathbb R^{20}\), and that every map in this class is one-to-one on the reference triangle and
\[
\inf_{a\in K_0}\inf_{\hat x\in\widehat K}
\det D\widehat F_a(\hat x)\ge j_0>0.
\tag{2.1}
\]
Compactness and (2.1) imply uniform finite bounds \(M_1,M_{-1},M_2,j_1\) for the scaled Jacobian, its inverse, second derivatives, and determinant upper bound. These are consequences of the single compact-class hypothesis, not separate independent assumptions.

**Lemma (uniform mapped-P3 trace estimate).** Under (2.1), the quantified scale condition (1.1), and the fixed P3 reference-element structure, there is
\[
C_{\rm tr}=C_{\rm tr}(K_0,c_0,c_1,\widehat K)
\]
independent of level and seed such that
\[
\boxed{H_{h,\ell}(v_h)^2\le C_{\rm tr}D_h(v_h)^2
\qquad\forall v_h\in V_h^0.}\tag{T134.1}
\]
The estimate includes every interior facet and every boundary facet (outer and both cores).

**Proof.** On each cell the inverse-map chain rule in §10.2 bounds the physical Hessian pullback by a uniform multiple of
\(h_K^{-2}(|D_{\hat x}^2\hat v|+|\nabla_{\hat x}\hat v|)\).
The volume and boundary Jacobians scale as \(h_K^2\) and \(h_K\). The volume Hessian form has kernel exactly the pullbacks of physical affine functions,
\[
N_{\widehat F}=\operatorname{span}\{1,\widehat F_1,\widehat F_2\},
\]
and is positive definite on \(\mathbb P_3(\widehat K)/N_{\widehat F}\). Compactness of \(K_0\) gives a uniform positive lower quotient eigenvalue; the boundary Hessian form is uniformly bounded above on coefficient-unit vectors. This yields the local estimate (10.6). Summing it over the three facets of each triangle, using (1.1) and the arithmetic-average bound on interior facets, proves (T134.1). The full quotient compactness argument and derivative calculation are in §10.2–§10.3. \(\square\)

For affine triangles this is the usual fixed-degree polynomial inverse-trace estimate. For curved P3 cells, (2.1) is an additional all-level geometric hypothesis; finite sampling and high-order optimization do not establish it.

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

**Theorem (conditional C⁰-IPDG coercivity).** Suppose the mesh family satisfies the compact normalized-map condition (2.1) and the quantified scale condition (1.1). Impose homogeneous value traces strongly on \(\Gamma_{\rm out},\Gamma_{c,1},\Gamma_{c,2}\), and include the symmetric consistency and \(\alpha/\ell_F\) penalty terms on every interior and boundary facet as displayed above. Then the lemma yields \(C_{\rm tr}=C_{\rm tr}(K_0,c_0,c_1,\widehat K)\), independent of mesh level and seed. For every
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
where \(\|v\|_{2,h,\ell}^2=D_h(v)^2+J_{h,\ell}(v)^2\). This is coercivity in the stated mesh-dependent seminorm. The homogeneous trace on the outer boundary eliminates the physical affine kernel, since an affine function vanishing at three non-collinear points is zero; the corresponding discrete Poincare/Friedrichs inequality therefore upgrades the seminorm to control the full discrete \(H^2\)-type norm.
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
The two symmetric consistency contributions in \(a_{h,\ell}(v,v)\) therefore have absolute value at most \(2H_{h,\ell}(v)J_{h,\ell}(v)\). By the lemma (T134.1) and Young's inequality,
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


## 10. Conditional analytical mapped-element trace lemma

This section proves the local trace estimate **under a fixed compact geometric
admissibility hypothesis**. It does not prove that the present Gmsh generator
produces a family satisfying that hypothesis. In particular, finite-dimensional
norm equivalence is used only after uniformity of the normalized element-map
family has been explicitly assumed.

### 10.1 Fixed admissible class of normalized maps

For each cell write
\[
F_K(\hat x)=x_K+h_K\widehat F_K(\hat x),\qquad h_K=\operatorname{diam}(K),
\]
and normalize \(\widehat F_K(\hat x_0)=0\). In the ten-monomial basis, the two components of each cubic map have a coefficient vector in \(\mathbb R^{20}\), subject to the two normalization constraints. The all-level geometric hypothesis is that every such vector, over all cells, levels, and allowed seeds, lies in one fixed compact set \(K_0\), every corresponding map is one-to-one on \(\widehat K\), and
\[
\inf_{a\in K_0}\inf_{\hat x\in\widehat K}
\det D\widehat F_a(\hat x)\ge j_0>0.
\tag{10.1}
\]
Compactness and strict determinant positivity imply the finite uniform bounds \(M_1,M_{-1},M_2,j_1\); these are consequences, not independent hypotheses. In principle, the condition is certifiable by coefficient bounds and a global polynomial positivity certificate.

The independent mesh-family condition is the quantified scale bound
\[
c_0h_K\le\ell_F\le c_1h_K
\qquad(F\subset\partial K),
\tag{10.2}
\]
with fixed constants for both incident cells of an interior facet. It implies neighboring-cell size comparability. Neither condition follows merely from Gmsh high-order optimization or finitely many sampled Jacobian values.

### 10.2 Local trace estimate, including the inverse-map term

Let \(v=\hat v\circ F_K^{-1}\), with \(\hat v\in\mathbb P_3(\widehat K)\), and
put \(J=DF_K=h_KD\widehat F_K\). The chain rule is
\[
\nabla_xv=J^{-T}\nabla_{\hat x}\hat v,
\]
\[
D_x^2v
=J^{-T}D_{\hat x}^2\hat v\,J^{-1}
+\sum_{a=1}^2(\partial_{\hat x_a}\hat v)
                 D_x^2(F_K^{-1})_a.
\tag{10.2}
\]
Differentiating \(F_K\circ F_K^{-1}=I\) twice gives
\[
D^2(F_K^{-1})[\xi,\eta]
=-J^{-1}D^2F_K[J^{-1}\xi,J^{-1}\eta],
\]
and hence
\[
\|D^2(F_K^{-1})\|
\le C\|J^{-1}\|^3\|D^2F_K\|
\le C h_K^{-2}M_{-1}^3M_2.
\tag{10.3}
\]
Thus the gradient-dependent term in (10.2) is controlled explicitly:
\[
|D_x^2v(F_K(\hat x))|
\le C h_K^{-2}
\bigl(|D_{\hat x}^2\hat v(\hat x)|
      +|\nabla_{\hat x}\hat v(\hat x)|\bigr),
\tag{10.4}
\]
where \(C\) depends only on the uniform bounds in (2.2) and the dimension.
In particular, that term is not discarded or assumed to vanish.

The volume and boundary Jacobians satisfy
\[
c h_K^2\le |\det DF_K|\le C h_K^2,\qquad
c h_K\le J_{\partial K}\le C h_K,
\tag{10.5}
\]
with constants uniform over the compact coefficient class \(K_0\). Equations (10.4)--(10.5)
show that both quadratic forms
\[
Q_{\widehat F}^{\rm vol}(\hat v)
=\int_{\widehat K}|D_x^2(\hat v\circ F^{-1})|^2
                         |\det DF|\,d\hat x
\]
and
\[
Q_{\widehat F}^{\rm bdry}(\hat v)
=h_K\int_{\partial\widehat K}
 |D_x^2(\hat v\circ F^{-1})|^2J_{\partial K}\,d\hat s
\]
are continuous in the map coefficients and in \(\hat v\), uniformly
bounded on bounded subsets of \(\mathbb P_3(\widehat K)\), and have the
same physical scaling. Here \(F=x_K+h_K\widehat F\); translation \(x_K\)
does not affect either Hessian.

The kernel of the volume form is exactly
\[
N_{\widehat F}
=\{\hat v:\hat v\circ F^{-1}\text{ is affine in physical }x\}
=\operatorname{span}\{1,\widehat F_1,\widehat F_2\}.
\]
The volume form is positive definite on the quotient
\(\mathbb P_3(\widehat K)/N_{\widehat F}\). Its smallest quotient
eigenvalue has a positive lower bound uniform over \(K_0\).
To see this rigorously, suppose otherwise. Choose a sequence
\(\widehat F_m\inK_0\) and representatives \(\hat v_m\)
orthogonal, in one fixed coefficient-space inner product, to
\(N_{\widehat F_m}\), with coefficient norm one and
\(Q_{\widehat F_m}^{\rm vol}(\hat v_m)\to0\).
Compactness gives convergent subsequences
\(\widehat F_m\to\widehat F\) and \(\hat v_m\to\hat v\).
The subspaces \(N_{\widehat F_m}\) converge to \(N_{\widehat F}\);
therefore \(\hat v\) has norm one and is orthogonal to
\(N_{\widehat F}\). Continuity gives
\(Q_{\widehat F}^{\rm vol}(\hat v)=0\), so
\(\hat v\in N_{\widehat F}\), a contradiction.
The boundary form is uniformly bounded above on coefficient-unit
vectors by (10.4)--(10.5) and compactness. It need not have the same
kernel as the volume form; no equality of those kernels is used.

It follows that
\[
h_K\|D_x^2v\|_{L^2(\partial K)}^2
\le C_{\rm loc}\|D_x^2v\|_{L^2(K)}^2,
\tag{10.6}
\]
where \(C_{\rm loc}\) depends only on the fixed class \(K_0\),
the reference cell, and the stated uniform geometric constants, and is
independent of \(K,h\), and the seed. Since
\(|n^TD_x^2v\,n|\le |D_x^2v|\), (10.6) also holds for the
normal-normal Hessian component. This proves the local estimate for
families contained in the fixed compact admissible class; it does not
establish that the actual generated family is contained in such a class.

### 10.3 Assembly and penalty scaling

For an interior facet,
\[
|\{n^TD^2v\,n\}|^2
\le\tfrac12\bigl(|D^2v^+|^2+|D^2v^-|^2\bigr);
\]
on a boundary facet there is only the adjacent-cell term. By (10.2), (10.6), the resulting neighboring-cell comparability, and the fact that each triangle has three facets,
\[
H_{h,\ell}(v)^2
\le C_{\rm tr}\sum_K\|D^2v\|_{L^2(K)}^2
=C_{\rm tr}D_h(v)^2.
\]
The constant depends only on \(K_0,c_0,c_1\), the reference triangle, and the fixed P3 degree; it is independent of level, cell, and seed. Thus (T134.1) follows
**conditionally** for every mesh family satisfying all the hypotheses
of §10.1.

For the penalty scaling in this theorem, the source code uses
\(\alpha/\operatorname{avg}(h_K)\) on interior facets and
\(\alpha/h_K\) on boundary facets. With the definitions in §1 this is
exactly \(\alpha/\ell_F\), so the jump term is
\[
J_{h,\ell}^2=\sum_F\ell_F^{-1}\|j_F\|_{L^2(F)}^2.
\]
In two dimensions, if \(v\) has physical units \(U\) and length has
units \(L\), then
\[
[D_h^2]=U^2L^{-2},\qquad
[H_{h,\ell}^2]=U^2L^{-2},\qquad
[J_{h,\ell}^2]=U^2L^{-2}.
\]
Consequently \(\alpha\) and \(C_{\rm tr}\) are dimensionless and
\(\alpha>2C_{\rm tr}\) is dimensionally consistent for this exact
weighted form. If the penalty were instead unweighted, or used a
different power of \(h_F\), this comparison and the coercivity
condition would have to be re-derived; it cannot be transferred
unchanged.

### 10.4 Coercivity and exact scope

For the form in §3, weighted Cauchy--Schwarz gives
\[
2\left|\sum_F(q_F(v),j_F(v))_F\right|
\le2H_{h,\ell}(v)J_{h,\ell}(v)
\le2\sqrt{C_{\rm tr}}D_h(v)J_{h,\ell}(v).
\]
Young's inequality yields
\[
2\sqrt{C_{\rm tr}}D_hJ_{h,\ell}
\le\tfrac12D_h^2+2C_{\rm tr}J_{h,\ell}^2,
\]
and therefore
\[
a_{h,\ell}(v,v)\ge
\tfrac12D_h(v)^2+(\alpha-2C_{\rm tr})J_{h,\ell}(v)^2.
\]
Thus \(\alpha>2C_{\rm tr}\) proves coercivity in the stated weighted
mesh-dependent seminorm, uniformly over mesh families satisfying the fixed compact map-class and quantified facet/element comparability hypotheses above. This is a sufficient condition; no necessity statement is claimed, and arbitrary curved P3 mesh families are not covered.

### 10.5 What remains open for the actual Gmsh generator

The current generator requests Gmsh cubic high-order optimized meshes.
The source-level inspection and finite diagnostics do not establish that
all normalized maps produced for every refinement level and allowed seed
belong to one fixed compact coefficient class \(K_0\). In particular:

1. finite sampling of \(\det D\widehat F_K\) does not certify its strict
   positivity on the whole reference cell;
2. no common, refinement-independent bounds \(M_1,M_{-1},M_2,j_0,j_1\)
   have been proved for all generated cells;
3. no all-level proof of facet and neighboring-cell comparability has
   been supplied;
4. the observed finite-mesh values of \(C_{\rm tr,h}\) do not bound
   \(\sup_h C_{\rm tr,h}\), and do not certify that \(\alpha=40\)
   exceeds \(2C_{\rm tr}\) for the whole generated family.

Accordingly, the valid result is a conditional analytical theorem for
families in the fixed compact admissible geometry class. The corresponding
unconditional statement for the present Gmsh generator remains open.
A deterministic generator-level construction or rejection rule with
fixed, certified bounds is needed to close that gap; finite sampling,
AIC, bootstrap, and cross-validation cannot do so.
