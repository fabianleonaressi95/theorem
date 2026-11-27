# EG-03: H1 reconstruction and the graph fundamental estimate

**Status:** conditional analytic result proved from the EG-01 nonlocal coercivity estimate, boundary-complete Voronoi geometry, and the stated conductance bounds. This note does not claim a complete Gamma-convergence theorem.

## 1. Setting and notation

Let \(\Omega\subset\mathbb R^d\) be bounded, connected, and Lipschitz. Let \(G_\varepsilon=(V_\varepsilon,E_\varepsilon)\) satisfy:

- separation \(|x-y|\ge c_s\varepsilon\) for distinct vertices;
- boundary-complete fill distance \(\sup_{z\in\overline\Omega}\operatorname{dist}(z,V_\varepsilon)\le C_f\varepsilon\);
- edge lengths at most \(C_e\varepsilon\);
- the path-tube condition (G5);
- conductances \(0<a_-\le a_e^\varepsilon\le a_+\).

Use the energy
\[
E_\varepsilon(v)=\frac12\sum_{e=\{p,q\}\in E_\varepsilon}
\varepsilon^{d-2}a_e^\varepsilon|v(p)-v(q)|^2
\]
and the Voronoi embedding \(P_\varepsilon v\in L^2(\Omega)\).

The EG-01 estimate already established is
\[
N_\varepsilon(P_\varepsilon v)
:=\varepsilon^{-d-2}
\int_\Omega\int_{\Omega\cap B_{r\varepsilon}(x)}
|P_\varepsilon v(x)-P_\varepsilon v(y)|^2\,dy\,dx
\le C E_\varepsilon(v), \tag{1.1}
\]
for one fixed \(r>0\). The uniform Poincare inequality also gives
\[
\|P_\varepsilon v-m_\varepsilon(v)\|_{L^2(\Omega)}^2
\le C E_\varepsilon(v),\qquad
m_\varepsilon(v):=\fint_\Omega P_\varepsilon v. \tag{1.2}
\]

## 2. Uniform nonlocal extension and smoothing

We use the nonlocal extension theorem of Alicandro–Ansini–Braides–Piatnitski–Tribuzio, *A Variational Theory of Convolution-Type Functionals* (Springer, 2023), Theorem 4.1. For a bounded Lipschitz domain and fixed interaction radius, it gives a linear extension operator
\[
\mathsf E:L^2(\Omega)\longrightarrow L^2(\widetilde\Omega),
\qquad \mathsf E u=u\text{ on }\Omega,
\]
and constants independent of sufficiently small \(\varepsilon\), such that
\[
\|\mathsf E u\|_{L^2(\widetilde\Omega)}^2+
N_\varepsilon^{r_1}(\mathsf E u;\widetilde\Omega)
\le C\bigl(\|u\|_{L^2(\Omega)}^2+
N_\varepsilon^r(u;\Omega)\bigr). \tag{2.1}
\]
Here \(N_\varepsilon^r\) denotes the same scaled difference quotient with interaction radius \(r\varepsilon\). The extension theorem is used only for this nonlocal estimate; it does not assert that the Voronoi embedding itself belongs to \(H^1\).

Let \(\eta\in C_c^\infty(B_{r_1})\) be nonnegative with integral one and set \(\eta_\varepsilon(x)=\varepsilon^{-d}\eta(x/\varepsilon)\). Define the regularized reconstruction
\[
I_\varepsilon v
=m_\varepsilon(v)+
\left.\eta_\varepsilon*
\mathsf E\bigl(P_\varepsilon v-m_\varepsilon(v)\bigr)
\right|_\Omega. \tag{2.2}
\]
This is a smooth function on \(\Omega\), and the map \(v\mapsto I_\varepsilon v\) is linear.

For any \(U\in L^2(\widetilde\Omega)\), the zero-mean identity \(\int\nabla\eta_\varepsilon=0\), Jensen's inequality, and the support and scaling of \(\eta_\varepsilon\) give
\[
\|\nabla(\eta_\varepsilon*U)\|_{L^2(\Omega)}^2
\le C N_\varepsilon^{r_1}(U;\widetilde\Omega), \tag{2.3}
\]
and
\[
\|\eta_\varepsilon*U-U\|_{L^2(\Omega)}^2
\le C\varepsilon^2N_\varepsilon^{r_1}(U;\widetilde\Omega). \tag{2.4}
\]
For (2.3), write
\[
\nabla(\eta_\varepsilon*U)(x)
=\int \nabla\eta_\varepsilon(h)[U(x-h)-U(x)]\,dh
\]
and apply weighted Cauchy–Schwarz. For (2.4), write the convolution difference as an average of translations and apply Jensen. Both estimates involve only pairs at distance at most \(r_1\varepsilon\).

Apply (2.1) to \(U=\mathsf E(P_\varepsilon v-m_\varepsilon(v))\). By (1.1)–(1.2), the right-hand side of (2.1) is bounded by \(C E_\varepsilon(v)\). Combining (2.2)–(2.4) yields
\[
\boxed{
\|\nabla I_\varepsilon v\|_{L^2(\Omega)}^2
\le C E_\varepsilon(v),\qquad
\|I_\varepsilon v-P_\varepsilon v\|_{L^2(\Omega)}^2
\le C\varepsilon^2 E_\varepsilon(v).
} \tag{2.5}
\]

The constants depend only on the domain, the fixed geometric constants, the lower conductance bound, and the chosen mollifier; they do not depend on \(v\) or \(\varepsilon\).

**Theorem EG-03A (uniform H1 reconstruction).** Under the hypotheses above, the maps (2.2) satisfy (2.5). In particular, bounded graph energy and bounded Voronoi \(L^2\)-norm imply boundedness of the reconstructed functions in \(H^1(\Omega)\). By Rellich compactness and the second estimate in (2.5), the Voronoi embeddings are strongly precompact in \(L^2(\Omega)\).

This is a regularized reconstruction, not a nodal finite-element interpolant: in general \(I_\varepsilon v(p)\ne v(p)\).

## 3. Localized graph energy and a fundamental estimate

For an open set \(U\subset\Omega\), let \(m_e\) be the Euclidean midpoint of edge \(e\) and define
\[
E_\varepsilon(v;U)
=\frac12\sum_{e:\,m_e\in U}
\varepsilon^{d-2}a_e^\varepsilon|D_ev|^2. \tag{3.1}
\]
Changing the midpoint convention to an edge-intersection convention changes only an \(O(\varepsilon)\) boundary layer; all statements below use (3.1) consistently.

Let \(A,B\subset\Omega\) be open and let \(A'\Subset A\), \(B'\Subset B\). Choose a Lipschitz cutoff \(\varphi:\overline\Omega\to[0,1]\) such that \(\varphi=1\) on a neighbourhood of \(A'\setminus B\), \(\varphi=0\) on a neighbourhood of \(B'\setminus A\), and
\[
\|\nabla\varphi\|_\infty\le C/\ell,
\]
where \(\ell>0\) is the width of the transition region. Set
\[
w_\varepsilon(p)=\varphi(p)v(p)+(1-\varphi(p))z(p).
\]

For an edge \(e=\{p,q\}\), the exact difference identity is
\[
D_ew_\varepsilon
=\varphi(p)D_ev+(1-\varphi(p))D_ez
+\bigl(\varphi(p)-\varphi(q)\bigr)(z(q)-v(q)).
\]
Using \(|a+b+c|^2\le(1+\delta)(|a|+|b|)^2+C\delta^{-1}|c|^2\), the convexity of the first two terms, and
\[
|\varphi(p)-\varphi(q)|
\le \|\nabla\varphi\|_\infty |p-q|
\le C\varepsilon/\ell,
\]
we obtain, after summing edges and using the uniform degree bound,
\[
\begin{aligned}
E_\varepsilon(w_\varepsilon;A'\cup B')
\le{}&(1+\delta)
\bigl(E_\varepsilon(v;A)+E_\varepsilon(z;B)\bigr)\\
&+\frac{C}{\delta\ell^2}
\int_{S_{C\varepsilon}}
|P_\varepsilon v-P_\varepsilon z|^2\,dx. 
\end{aligned} \tag{3.2}
\]
Here \(S\) is the transition region of \(\varphi\), and \(S_{C\varepsilon}\) is its fixed-multiple-\(\varepsilon\) enlargement. The conversion of the discrete error sum to the integral uses the lower Voronoi-cell volume bound \(|V_\varepsilon(p)|\ge c\varepsilon^d\) and the uniform degree bound.

Equation (3.2) is the graph fundamental estimate with an explicit boundary-layer enlargement. It is the key gluing estimate needed in a De Giorgi localization argument.

## 4. What this does and does not establish for integral representation

The graph energy has an exact continuum-kernel representation on Voronoi cells. If \(C_p\) denotes the cell of vertex \(p\), define the symmetric measurable kernel
\[
K_\varepsilon(x,y)=
\begin{cases}
\displaystyle
\frac{\varepsilon^{d-2}a_{\{p,q\}}^\varepsilon}
{2|C_p||C_q|},
&x\in C_p,\ y\in C_q,\ \{p,q\}\in E_\varepsilon,\\[2mm]
0,&\text{otherwise}.
\end{cases}
\]
Then
\[
E_\varepsilon(v)
=\frac12\int_\Omega\int_\Omega
K_\varepsilon(x,y)
|P_\varepsilon v(x)-P_\varepsilon v(y)|^2\,dy\,dx. \tag{4.1}
\]
The kernel is supported where \(|x-y|\le(C_e+2C_f)\varepsilon\), and the cell-volume bounds give \(K_\varepsilon\le C\varepsilon^{-d-2}\). It is sparse: it vanishes on most pairs of nearby Voronoi cells.

The lower comparison (1.1), the upper comparison from edge locality and the lower cell-volume bound, and (3.2) give the coercivity, upper growth, and gluing ingredients for a discrete localization proof.

**Important distinction from the convolution theorem.** The hypotheses of Alicandro–Ansini–Braides–Piatnitski–Tribuzio, Theorem 5.1, are stated for convolution-type continuum functionals with pointwise kernel growth and locality assumptions. The sparse kernel (4.1) does not satisfy their pointwise lower kernel bound merely because its *total energy* dominates a nonlocal difference quotient. Therefore Theorem 5.1 cannot be cited as a black-box proof for this graph class. Likewise, Alicandro–Cicalese–Gloria (2011) treats stochastic lattices, not arbitrary embedded graphs.

To complete the integral representation for this graph class, the remaining proof must establish, for the localized functionals (3.1):

1. the De Giorgi–Letta measure property for every fixed continuum limit function;
2. locality of every subsequential Gamma-limit under the Voronoi identification;
3. a uniform upper-growth/recovery construction for every \(u\in H^1(\Omega)\), not just smooth functions;
4. preservation of the quadratic form structure under the chosen convergence of the discrete quadratic forms.

The fundamental estimate (3.2) supplies the central gluing inequality, but items 1–4 are not silently inferred from it.

## 5. Status and next proof obligations

- EG-01 local path length and congestion: **proved conditionally** under separation and (G5).
- EG-02 nonlocal coercivity, uniform Poincare, and strong \(L^2\) compactness: **proved conditionally** with boundary-complete fill.
- EG-03A regularized \(H^1\) reconstruction (2.5): **proved conditionally**, using the cited nonlocal extension theorem.
- EG-03B localized graph fundamental estimate (3.2): **proved conditionally**, for the midpoint localization and the stated cutoff geometry.
- EG-04 integral representation for arbitrary embedded graphs: **open**.
- EG-05 quadraticity of the subsequential density: **open until the quadratic-form convergence step is written out**.
- EG-06 cell formula and full-sequence convergence: **open**.

## 6. References

1. R. Alicandro, N. Ansini, A. Braides, A. Piatnitski, A. Tribuzio, *A Variational Theory of Convolution-Type Functionals*, SpringerBriefs on PDEs and Data Science, Springer, 2023. DOI: [10.1007/978-981-99-0685-7](https://doi.org/10.1007/978-981-99-0685-7). In particular, Theorem 4.1 (nonlocal extension) and Theorem 4.2 (compactness and Sobolev regularity).
2. A. C. Ponce, “A new approach to Sobolev spaces and connections to Γ-convergence,” *Calculus of Variations and Partial Differential Equations* 19 (2004), 229–255. DOI: [10.1007/s00526-003-0195-z](https://doi.org/10.1007/s00526-003-0195-z).
3. R. Alicandro, M. Cicalese, A. Gloria, “Integral Representation Results for Energies Defined on Stochastic Lattices and Application to Nonlinear Elasticity,” *Archive for Rational Mechanics and Analysis* 200 (2011), 881–943. DOI: [10.1007/s00205-010-0378-7](https://doi.org/10.1007/s00205-010-0378-7). Its stochastic-lattice hypotheses are not identified with (G1)–(G6).
