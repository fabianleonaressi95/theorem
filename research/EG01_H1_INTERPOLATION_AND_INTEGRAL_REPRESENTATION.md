# EG-01B: H1 interpolation, fundamental estimate, and subsequential integral representation

**Status:** conditional theorem package built on the local nonlocal-energy domination in `EG01_LOCAL_POINCARE_PROOF.md`. The interpolation and cutoff estimates below are derived directly. The integral-representation conclusion is stated for subsequential Gamma-limits, using the standard local integral-representation theorem. No full-sequence homogenization is claimed.

## 1. Standing assumptions

Let \(\Omega\subset\mathbb R^d\) be bounded, connected, and Lipschitz. Let \(G_\varepsilon=(V_\varepsilon,E_\varepsilon)\) satisfy:

- separation \(|x-y|\ge c_s\varepsilon\);
- boundary-complete fill \(\sup_{z\in\overline\Omega}\operatorname{dist}(z,V_\varepsilon)\le C_f\varepsilon\);
- edge length \(|p-q|\le C_e\varepsilon\);
- the path-tube property (G5), with tube radius \(C_p\varepsilon\);
- conductances \(0<a_-\le a_e^\varepsilon\le a_+<\infty\).

The energy and Voronoi embedding are
\[
E_\varepsilon(v)=\frac12\sum_{\{p,q\}\in E_\varepsilon}
\varepsilon^{d-2}a_{pq}^\varepsilon|v(p)-v(q)|^2,
\qquad u_\varepsilon=P_\varepsilon v.
\]
Let \(r\in(0,1]\) be the fixed radius used in the nonlocal estimate already proved:
\[
N_{\varepsilon,r}(u)=\varepsilon^{-d-2}
\int_\Omega\int_{\Omega\cap B(x,r\varepsilon)}
|u(x)-u(y)|^2\,dy\,dx
\le C E_\varepsilon(v). \tag{1.1}
\]

All constants below depend only on the displayed geometric constants, \(d\), and the Lipschitz character of \(\Omega\), not on \(\varepsilon\).

## 2. A boundary-adapted H1 interpolation operator

A global extension of \(u_\varepsilon\) is not needed. Use a normalized local average entirely inside \(\Omega\).

Choose a nonnegative radial \(\rho\in C_c^\infty(B_1)\) with \(\int\rho=1\), and choose \(0<\delta<r/2\). Put
\[
\rho_{\delta\varepsilon}(z)=(\delta\varepsilon)^{-d}
\rho\!\left(\frac z{\delta\varepsilon}\right),
\quad
D_\varepsilon(x)=\int_\Omega\rho_{\delta\varepsilon}(x-y)\,dy,
\]
and define
\[
I_\varepsilon u(x)=
\frac{\int_\Omega\rho_{\delta\varepsilon}(x-y)u(y)\,dy}
{D_\varepsilon(x)},\qquad x\in\Omega. \tag{2.1}
\]

The uniform interior-cone property of a bounded Lipschitz domain gives
\[
0<c_\Omega\le D_\varepsilon(x)\le 1
\quad (x\in\Omega,\ 0<\varepsilon<\varepsilon_0). \tag{2.2}
\]
Thus \(I_\varepsilon\) is a well-defined linear map \(L^2(\Omega)\to H^1(\Omega)\).

### Lemma 2.1 (consistency and gradient estimate)

For every \(u\in L^2(\Omega)\),
\[
\|I_\varepsilon u-u\|_{L^2(\Omega)}^2
\le C\varepsilon^2N_{\varepsilon,r}(u), \tag{2.3}
\]
and
\[
\|\nabla I_\varepsilon u\|_{L^2(\Omega)}^2
\le C N_{\varepsilon,r}(u). \tag{2.4}
\]

**Proof.** Write \(K_x(y)=\rho_{\delta\varepsilon}(x-y)\) and \(D(x)=\int_\Omega K_x\). By Jensen's inequality,
\[
|I_\varepsilon u(x)-u(x)|^2
\le D(x)^{-1}\int_\Omega K_x(y)|u(y)-u(x)|^2\,dy.
\]
Integrating in \(x\), using (2.2), the kernel bound \(K_x(y)\le C\varepsilon^{-d}\), and \(|x-y|\le\delta\varepsilon<r\varepsilon\), gives (2.3).

Differentiating (2.1) and using the quotient rule gives the cancellation identity
\[
\nabla I_\varepsilon u(x)
=D(x)^{-1}\int_\Omega\nabla_xK_x(y)
\bigl(u(y)-I_\varepsilon u(x)\bigr)\,dy.
\]
Apply weighted Cauchy-Schwarz, then Jensen to
\[
|u(y)-I_\varepsilon u(x)|^2
\le D(x)^{-1}\int_\Omega K_x(z)|u(y)-u(z)|^2\,dz.
\]
The kernel bounds
\[
\|\nabla\rho_{\delta\varepsilon}\|_{L^1}\le C\varepsilon^{-1},
\quad
\|\nabla\rho_{\delta\varepsilon}\|_\infty\le C\varepsilon^{-d-1},
\quad
\|\rho_{\delta\varepsilon}\|_\infty\le C\varepsilon^{-d}
\]
give
\[
|\nabla I_\varepsilon u(x)|^2
\le C\varepsilon^{-2d-2}
\int_{\Omega\cap B(x,\delta\varepsilon)}
\int_{\Omega\cap B(x,\delta\varepsilon)}
|u(y)-u(z)|^2\,dz\,dy.
\]
Integrate in \(x\) and use Fubini. For fixed \(y,z\), the set of \(x\) contributing has measure at most \(C\varepsilon^d\), and \(|y-z|\le2\delta\varepsilon<r\varepsilon\). This yields (2.4). \(\square\)

Combining (1.1), (2.3), and (2.4) gives the graph-to-Sobolev interpolation estimate
\[
\boxed{
\|I_\varepsilon P_\varepsilon v-P_\varepsilon v\|_2^2
\le C\varepsilon^2E_\varepsilon(v),\qquad
\|\nabla I_\varepsilon P_\varepsilon v\|_2^2
\le CE_\varepsilon(v).
} \tag{2.5}
\]
This is the required \(H^1\) interpolation estimate. It is boundary-adapted and does not assume a triangulation or a global extension operator.

## 3. Uniform upper growth and recovery sequences

Separation and the edge-length bound imply a uniform degree bound: every neighbor of \(p\) lies in \(B(p,C_e\varepsilon)\), which contains only a uniformly bounded number of separated vertices.

For \(u\in H^1(\Omega)\), define the discrete recovery values by cell averages
\[
v_\varepsilon(p)=\dashint_{V_\varepsilon(p)}u(x)\,dx.
\]
The Voronoi cell-volume bounds and the uniform local Poincare inequality on Lipschitz patches imply, for every edge \(\{p,q\}\),
\[
|v_\varepsilon(p)-v_\varepsilon(q)|^2
\le C\varepsilon^{2-d}
\int_{\Omega\cap B(p,C\varepsilon)}|\nabla u|^2\,dx.
\]
The balls on the right have uniformly bounded overlap, by vertex separation and the degree bound. Summing over edges and using \(a_e^\varepsilon\le a_+\) yields
\[
E_\varepsilon(v_\varepsilon)\le C\int_\Omega|\nabla u|^2\,dx. \tag{3.1}
\]
The fill-distance and cell-diameter bounds also give
\[
P_\varepsilon v_\varepsilon\longrightarrow u
\quad\text{strongly in }L^2(\Omega). \tag{3.2}
\]
For general \(H^1\) functions, (3.2) follows first for smooth functions and then by density and the uniform cell-average stability estimate.

Thus the family has a uniform \(H^1\)-type upper-growth/recovery bound. This is not an identification of the exact limiting density.

## 4. Discrete fundamental estimate

For an open set \(U\subset\Omega\), localize the energy by assigning an edge to \(U\) when its midpoint lies in \(U\). Write \(U^{s}=\{x:\operatorname{dist}(x,U)<s\}\).

Let \(\eta:\Omega\to[0,1]\) be Lipschitz and define
\[
z(p)=\eta(p)v(p)+(1-\eta(p))w(p).
\]
For an edge \(e=\{p,q\}\),
\[
D_ez=\eta(p)D_ev+(1-\eta(p))D_ew
+(\eta(p)-\eta(q))(w(q)-v(q)).
\]
Young's inequality and \(|\eta(p)-\eta(q)|\le C_e\varepsilon\|\nabla\eta\|_\infty\) give, for every \(\tau>0\),
\[
\begin{aligned}
E_\varepsilon(z,U)
\le &(1+\tau)\bigl(E_\varepsilon(v,U^{C\varepsilon})
+E_\varepsilon(w,U^{C\varepsilon})\bigr)\\
&+C(1+\tau^{-1})\|\nabla\eta\|_\infty^2
\|P_\varepsilon(v-w)\|_{L^2(U^{C\varepsilon}\cap T_\eta)}^2,
\end{aligned} \tag{4.1}
\]
where \(T_\eta\) is the transition region \(0<\eta<1\), enlarged by \(C\varepsilon\). In the last step one uses the uniform degree bound and the lower Voronoi cell-volume bound to compare
\(\varepsilon^d\sum |v(p)-w(p)|^2\) with the \(L^2\) norm of the Voronoi embedding.

Equation (4.1) is the discrete fundamental estimate: the error is confined to the cutoff layer and is controlled by the \(L^2\) discrepancy there. It is valid for arbitrary bounded Lipschitz cutoffs; no periodicity is used.

## 5. Consequences for subsequential Gamma-limits

Define \(F_\varepsilon:L^2(\Omega)\to[0,\infty]\) by
\[
F_\varepsilon(P_\varepsilon v)=E_\varepsilon(v),
\qquad F_\varepsilon(u)=+\infty
\text{ if }u\notin P_\varepsilon(\mathbb R^{V_\varepsilon}).
\]

The estimates above provide the standard ingredients:

1. **Equicoercivity:** bounded \(L^2\) norm and bounded energy imply boundedness of \(I_\varepsilon P_\varepsilon v\) in \(H^1\), while (2.5) makes the interpolation error vanish. Rellich compactness gives strong \(L^2\) precompactness.
2. **Coercive lower growth:** (1.1) and the nonlocal-to-local liminf theorem imply \(F(u)\ge c\int_\Omega|\nabla u|^2dx\) for any subsequential limit \(F\).
3. **Upper growth:** (3.1) supplies recovery sequences and \(F(u)\le C\int_\Omega|\nabla u|^2dx\).
4. **Locality and fundamental estimate:** interactions have range at most \(C_e\varepsilon\), and (4.1) permits gluing across cutoff layers. The associated edge-energy measures are supported at edge midpoints and have uniformly bounded mass on bounded-energy sequences.

### Measure-property check (De Giorgi-Letta criterion)

Fix a subsequence along which the localized functionals converge on a countable basis of open subsets, and define \(F(u,U)\) by the corresponding localized Gamma-limit.

- Monotonicity follows from \(E_\varepsilon(v,U)\le E_\varepsilon(v,V)\) for \(U\subset V\).
- Superadditivity on disjoint open sets follows from additivity of the midpoint-localized edge sum: for disjoint \(U,V\), an edge midpoint is counted in at most one of them.
- Subadditivity for a finite open cover follows by choosing local recovery sequences, taking a Lipschitz partition of unity subordinate to the cover, and gluing them with (4.1). For a fixed cutoff layer, all local recovery sequences converge strongly to the same target \(u\), so the \(L^2\) discrepancy term in (4.1) vanishes as \(\varepsilon\to0\). Exhaustion by relatively compact subsets gives inner regularity.
- The uniform energy bound gives local boundedness of the resulting set function.

The De Giorgi-Letta criterion therefore identifies \(U\mapsto F(u,U)\) with a Radon measure. This is the measure property required by the local integral-representation theorem. The argument depends on using the same midpoint convention for every localized energy; changing that convention only changes an \(O(\varepsilon)\) boundary layer.

Consequently, every sequence \(\varepsilon_n\downarrow0\) has a subsequence along which \(F_{\varepsilon_n}\) Gamma-converges in strong \(L^2\). For each such subsequential limit, the standard integral-representation theorem for local quadratic energies on \(H^1\), together with the quadratic-form/Mosco structure, yields
\[
F(u)=
\begin{cases}
\displaystyle\int_\Omega \nabla u(x)^{T}A(x)\nabla u(x)\,dx,
&u\in H^1(\Omega),\\[1mm]
+\infty,&u\notin H^1(\Omega),
\end{cases} \tag{5.1}
\]
with a measurable symmetric matrix field \(A(x)\) satisfying
\[
0<\lambda I\le A(x)\le\Lambda I<\infty
\quad\text{for a.e. }x\in\Omega. \tag{5.2}
\]

The lower ellipticity follows from the nonlocal coercivity/BBM liminf; the upper bound follows from (3.1). The quadratic character follows because each \(F_\varepsilon\) is a nonnegative quadratic form and energy-bounded sequences are strongly precompact, so subsequential strong Gamma convergence upgrades to Mosco convergence on the effective domain.

**Scope:** (5.1) is a subsequential representation theorem. It does not assert that \(A(x)\) is independent of the selected subsequence.

## 6. Cell formula and full-sequence convergence

Once a subsequential limit \(F\) is fixed, its density is recovered almost everywhere by the usual blow-up/local Dirichlet formula on cubes:
\[
\xi^TA(x)\xi
=\lim_{\rho\downarrow0}\frac{1}{|Q_\rho(x)|}
\inf\left\{
F(w,Q_\rho(x)):
w=\ell_\xi\text{ on a boundary collar}
\right\}, \tag{6.1}
\]
where \(\ell_\xi(y)=\xi\cdot y\), and the localized limit energy is understood through the same subsequence. Equivalently, one can use the discrete cell problems before passing to the subsequential limit, with a boundary collar thicker than the interaction range \(C_e\varepsilon\). The order of limits is essential: first take the discrete limit along the selected subsequence at fixed cube, then let \(\rho\downarrow0\).

The geometric assumptions do **not** imply full-sequence convergence. A simple obstruction is to take square-grid graphs and alternate, with the sequence index, between conductance patterns
\[
(a_{\rm horizontal},a_{\rm vertical})=(1,2)
\quad\text{and}\quad(2,1).
\]
Both patterns satisfy the same separation, fill, edge-length, path-tube, and ellipticity constants, but their continuum matrices are respectively
\(\operatorname{diag}(1,2)\) and \(\operatorname{diag}(2,1)\). The full sequence therefore has two different subsequential Gamma-limits. Full-sequence convergence requires an additional uniqueness mechanism, such as convergence of the local cell energies, periodicity with a fixed cell, or a suitable stationary ergodic hypothesis.

## 7. Classification and open items

- Boundary-adapted \(H^1\) interpolation (2.5): **proved conditionally** under the standing geometric assumptions.
- Uniform upper growth and \(H^1\) recovery (3.1)-(3.2): **proved conditionally** with \(a_e^\varepsilon\le a_+\).
- Discrete fundamental estimate (4.1): **proved conditionally**.
- Subsequential integral representation (5.1): **follows conditionally** from the standard local integral-representation theorem for quadratic energies; the graph-specific estimates needed to invoke it are supplied above.
- Local cell formula: **available for each fixed subsequential limit** by blow-up; a direct full-sequence discrete cell limit is not established.
- Full-sequence Gamma convergence: **false without an additional uniqueness/homogenization hypothesis**, as shown by the alternating-conductance example.

## 8. References and precise relation to the literature

1. R. Alicandro, M. Cicalese, A. Gloria, “Integral representation results for energies defined on stochastic lattices and application to nonlinear elasticity,” *Archive for Rational Mechanics and Analysis* 200 (2011), 881–943, DOI [10.1007/s00205-010-0378-7](https://doi.org/10.1007/s00205-010-0378-7). This is a stochastic-lattice theorem; its hypotheses are not silently identified with the arbitrary embedded-graph assumptions here.
2. R. Alicandro, M. Cicalese, “A general integral representation result for the continuum limits of discrete energies with superlinear growth,” *SIAM Journal on Mathematical Analysis* 36 (2004), 1–37.
3. A. Braides, L. Kreutz, “An integral-representation result for continuum limits of discrete energies with multi-body interactions,” *SIAM Journal on Mathematical Analysis* 50 (2018), 1485–1520, DOI [10.1137/17M1121433](https://doi.org/10.1137/17M1121433). This is a lattice result and is used as a methodological comparison, not as a theorem directly covering arbitrary graphs.
4. A. C. Ponce, “A new approach to Sobolev spaces and connections to Gamma-convergence,” *Calculus of Variations and Partial Differential Equations* 19 (2004), 229–255, DOI [10.1007/s00526-003-0195-z](https://doi.org/10.1007/s00526-003-0195-z), for the nonlocal-to-local compactness/liminf step.
5. G. Dal Maso, *An Introduction to Γ-convergence*, Birkhäuser, 1993, for the general localization and integral-representation framework.
