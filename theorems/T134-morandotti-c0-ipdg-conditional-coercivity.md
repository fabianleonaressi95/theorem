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
