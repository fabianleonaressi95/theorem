# C60 — Caccioppoli-partition recovery for the variable-field isotropic CF cost

Status: **analytical recovery construction; interior/no-trace formulation**  
Date: 2026-11-21

## 1. Setting and statement

Let \(\Omega\subset\mathbb R^2\) be bounded Lipschitz and \(c\in W^{1,1}(\Omega;\mathbb R^m)\). For finite piecewise-constant maps define
\[
F(v)=\int_{J_v}|[v]|\,d\mathcal H^1.
\]
Then
\[
\boxed{\inf_{v_n\to c\text{ in }L^1}\liminf_n F(v_n)
=\int_\Omega\|\nabla c(x)\|_*\,dx.}
\]
No trace constraint is imposed. This is an interior result; prescribed traces require a boundary-layer analysis.

## 2. Lower bound

For \(Q\in C_c(\Omega;\mathbb R^{m\times2})\), \(\|Q(x)\|_{\rm op}\le1\), rank-one duality gives
\[
Q:([v]\otimes\nu)=[v]\cdot Q\nu\le|[v]|.
\]
If \(v_n\to c\) in \(L^1\) and \(F(v_n)\) is bounded, then \(Dv_n\stackrel{*}{\rightharpoonup}Dc\). Hence
\[
\liminf_nF(v_n)\ge\int_\Omega Q:\nabla c\,dx.
\]
Taking the supremum over continuous operator-unit-ball fields, by duality of nuclear and operator norms,
\[
\liminf_nF(v_n)\ge\int_\Omega\|\nabla c\|_*\,dx.
\]

## 3. Recovery construction for smooth maps

First assume \(c\) is \(C^1\) on a neighborhood of \(\overline\Omega\); use an extension if necessary. Let \(\omega\) be the modulus of continuity of \(\nabla c\).

### 3.1 Macro-partition and frozen SVD

Choose a finite shape-regular polygonal partition \(\{P_j\}\) of an interior polygonal exhaustion, with \(\operatorname{diam}P_j\le\delta\). Choose \(x_j\in P_j\) and put \(M_j=\nabla c(x_j)\). Write
\[
M_j=\sum_{i=1}^2\sigma_i^{(j)}a_i^{(j)}\otimes v_i^{(j)},
\]
where \(v_1^{(j)},v_2^{(j)}\) are orthonormal. In macro-cell \(P_j\), use a square grid of side \(h\) oriented with tangents \(v_1^{(j)},v_2^{(j)}\). The finite partition consists of intersections of grid squares with macro-polygons.

Assign to each intersected square the value \(c(x_C)\) at its grid center \(x_C\), using a smooth extension for centers outside \(\Omega\). This defines a piecewise-constant map \(c_{\delta,h}\).

### 3.2 Cost on grid interfaces

For neighboring squares whose centers differ by \(hv_i^{(j)}\), the jump satisfies
\[
c(x_C+hv_i)-c(x_C)
=hM_jv_i+r_C,\qquad
|r_C|\le h\,\omega(\delta+h).
\]
The shared interface length is at most \(h\). Thus its cost is bounded by
\[
h^2\bigl(|M_jv_i|+\omega(\delta+h)\bigr).
\]
The total length of grid interfaces in \(P_j\), for each orientation, is bounded by
\[
\frac{|P_j|}{h}+C\,\operatorname{Per}(P_j),
\]
where \(C\) is universal for a shape-regular polygonal partition. Summing the costs of the two orientations gives
\[
F_{\rm grid}(P_j)
\le |P_j|\bigl(|M_jv_1|+|M_jv_2|
+2\omega(\delta+h)\bigr)
+C h\,\operatorname{Per}(P_j)\|M_j\|+C h\,\operatorname{Per}(P_j)\omega(\delta+h).
\]
Because \(v_i\) are right singular vectors,
\[
|M_jv_1|+|M_jv_2|=\sigma_1(M_j)+\sigma_2(M_j)=\|M_j\|_*.
\]

### 3.3 Macro-interface cost

At a macro-interface, the two grids have different orientations. The values assigned to cells adjacent to the interface are samples of the same smooth \(c\), at points whose distance is \(O(h)\) from the interface. Therefore the jump is at most \(C h\|\nabla c\|_\infty\). The total macro-interface length is \(\sum_j\operatorname{Per}(P_j)\), so
\[
F_{\rm macro}\le C h\|\nabla c\|_\infty
\sum_j\operatorname{Per}(P_j).
\]
For a shape-regular partition with mesh \(\delta\), the perimeter sum is \(O(|\Omega|/\delta)\). Hence the macro-interface cost is \(O(h|\Omega|/\delta)\), which vanishes when \(h/\delta\to0\).

The boundary of the interior exhaustion is treated similarly; in the no-trace formulation its contribution is removed by exhaustion and diagonalization.

### 3.4 Limit estimates

Combining the estimates,
\[
F(c_{\delta,h})\le
\sum_j|P_j|\|M_j\|_*+
C|\Omega|\omega(\delta+h)+
C h\|\nabla c\|_\infty\sum_j\operatorname{Per}(P_j).
\]
Also, since samples are at distance \(O(h)\) from points in their cells,
\[
\|c_{\delta,h}-c\|_{L^1}\le C h\|\nabla c\|_\infty|\Omega|
\]
up to the vanishing exhaustion remainder.

First let \(h/\delta\to0\), then \(\delta\to0\). The Riemann sums converge:
\[
\sum_j|P_j|\|M_j\|_*\to\int_\Omega\|\nabla c\|_*dx.
\]
Thus for smooth \(c\) the construction gives the recovery upper bound.

## 4. Extension to \(W^{1,1}\)

Choose smooth \(c^\varepsilon\to c\) in \(W^{1,1}\). Since the nuclear norm is equivalent to the Frobenius norm in finite dimensions,
\[
\int_\Omega\|\nabla c^\varepsilon\|_*dx
\to\int_\Omega\|\nabla c\|_*dx.
\]
For each \(\varepsilon\), use the smooth recovery construction and choose grid/macro scales so that both the \(L^1\) error and the excess energy are at most \(\varepsilon\). A diagonal sequence yields \(v_n\to c\) in \(L^1\) and
\[
\limsup_nF(v_n)\le\int_\Omega\|\nabla c\|_*dx.
\]
Combined with the lower bound, this proves the relaxation formula in the stated interior/no-trace setting.

## 5. Exact prescribed-gradient consequence

Set \(u_n(x)=Gx+v_n(x)\). Since each \(v_n\) is piecewise constant,
\[
\nabla u_n=G\quad\text{a.e. exactly}.
\]
The jump cost is \(F(v_n)\); the recovery does not perturb the prescribed bulk gradient.

## 6. Facewise functional and limitations

For polygonal faces \(F_f\), fixed \(\widetilde G_f\), and the interior no-trace formulation, the face contribution is
\[
\int_{F_f}\left[W(\widetilde G_f)+
\|\nabla g_f-\widetilde G_f\|_*\right]\,d\mathcal H^2.
\]
The macro-jump term is separate. Compatibility across C60 edges and prescribed traces are not covered by this interior construction.

## 7. Anisotropic bounds

For \(\psi(a,\nu)=\Phi(a)k(\nu)\), with \(\Phi\) a norm and \(k\) even, the dual lower bound is
\[
\mathcal C_{\Phi,k}(M)\ge
\sup_{Q:\Phi^\circ(Q\nu)\le k(\nu)\ \forall\nu}Q:M.
\]
A two-direction orthogonal laminate gives
\[
\mathcal C_{\Phi,k}(M)\le
\inf_{(v_1,v_2)\ {\rm ONB}}\sum_i k(v_i)\Phi(Mv_i).
\]
Equality for general \(\Phi,k\) is not claimed. For \(\Phi=|\cdot|\) and \(k=1\), both bounds equal \(\|M\|_*\).

## 8. Rank statement

For \(u_h(\xi)=\widetilde G\xi+b+Mq_h(\xi)\), \(\nabla u_h=\widetilde G\) a.e. If \(\widetilde G=cA\), \(c>0\), \(A^TA=I_2\), then \(\operatorname{rank}\nabla u_h=2\) a.e. This does not imply classical immersion across jump interfaces or global embeddedness.
