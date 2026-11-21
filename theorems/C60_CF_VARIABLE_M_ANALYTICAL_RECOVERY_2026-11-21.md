# C60 — Caccioppoli-partition recovery for the variable-field isotropic CF cost

Status: **analytical recovery construction, interior formulation**  
Date: 2026-11-21

## 1. Setting and statement

Let \(\Omega\subset\mathbb R^2\) be bounded Lipschitz and \(c\in W^{1,1}(\Omega;\mathbb R^m)\). Define
\[
F(v)=\int_{J_v}|[v]|\,d\mathcal H^1
\]
for finite piecewise-constant maps \(v\). Then
\[
\boxed{\inf_{v_n\to c\text{ in }L^1}\liminf_n F(v_n)
=\int_\Omega\|\nabla c(x)\|_*\,dx.}
\]
No trace constraint is imposed. The result is interior; prescribed traces require a separate boundary-layer construction.

## 2. Lower bound

For \(Q\in C_c(\Omega;\mathbb R^{m\times2})\), \(\|Q(x)\|_{\rm op}\le1\), rank-one duality gives
\[
Q:([v]\otimes\nu)=[v]\cdot Q\nu\le|[v]|.
\]
If \(v_n\to c\) in \(L^1\) and \(F(v_n)\) is bounded, then \(Dv_n\stackrel{*}{\rightharpoonup}Dc\) as measures. Thus
\[
\liminf_nF(v_n)\ge\int_\Omega Q:\nabla c\,dx.
\]
Taking the supremum over continuous operator-unit-ball fields, using the duality of nuclear and operator norms and approximation of the measurable polar field, yields
\[
\liminf_nF(v_n)\ge\int_\Omega\|\nabla c\|_*\,dx.
\]

## 3. Recovery by locally SVD-oriented Caccioppoli partitions

The construction below supplies the upper bound; it does not infer recovery from the SVD alone.

### Step 1 — smooth and freeze the gradient

Choose \(c^\varepsilon\in C^\infty\) with \(c^\varepsilon\to c\) in \(W^{1,1}\). Since the nuclear norm is continuous in finite dimensions,
\[
\int_\Omega\|\nabla c^\varepsilon\|_*\,dx
\to\int_\Omega\|\nabla c\|_*\,dx.
\]
Fix \(\varepsilon\). Partition an interior polygonal exhaustion into macro-polygons \(P_j\) of diameter at most \(\delta\). Let \(M_j=\nabla c^\varepsilon(x_j)\) for \(x_j\in P_j\). Uniform continuity gives
\[
\sup_{x\in P_j}\|\nabla c^\varepsilon(x)-M_j\|_F
\le\omega_\varepsilon(\delta).
\]

### Step 2 — local grid oriented by the right singular vectors

For each macro-polygon, choose an SVD
\[
M_j=\sum_{i=1}^{2}\sigma_i^{(j)}a_i^{(j)}\otimes v_i^{(j)},
\]
where \(v_1^{(j)},v_2^{(j)}\) are orthonormal. Tile the plane by squares of side \(h\) with sides parallel to these vectors, and intersect the grid with \(P_j\). This produces a finite Caccioppoli partition. On each full grid square \(C\), set the approximant equal to \(c^\varepsilon(x_C)\), where \(x_C\) is its center. Boundary cells are assigned values from points in the same macro-polygon at distance \(O(h)\).

For the frozen affine map \(x\mapsto M_jx+b\), neighboring values across a side with normal \(v_i^{(j)}\) differ by exactly \(hM_jv_i^{(j)}\). The side has length \(h\). Per unit area, the two families of sides therefore cost
\[
|M_jv_1^{(j)}|+|M_jv_2^{(j)}|
=\sigma_1^{(j)}+\sigma_2^{(j)}
=\|M_j\|_*.
\]
This is the exact local cell cost for this oriented grid, not merely an algebraic SVD identity.

### Step 3 — perturbation and macro-interface estimates

For \(c^\varepsilon\) on a grid cell, the difference between the neighboring sampled values and the frozen-affine values is bounded by
\(O(h\,\omega_\varepsilon(\delta))\). Summing over grid sides gives an interior cost error bounded by
\(C|\Omega|\omega_\varepsilon(\delta)\), with \(C\) depending only on dimension and the norm equivalence constants.

At macro-polygon interfaces, grid cells from the two orientations need not match. Assign boundary-cell values by sampling \(c^\varepsilon\) within distance \(O(h)\) of the interface. Because \(c^\varepsilon\) is Lipschitz, the mismatch across the macro-interface is \(O(h\|\nabla c^\varepsilon\|_\infty)\). The total interface length of a shape-regular macro-partition is \(O(|\Omega|/\delta)\); hence the added cost is
\[
O\!\left(h\,\|\nabla c^\varepsilon\|_\infty\,|\Omega|/\delta\right).
\]
Choose \(h/\delta\to0\). The outer-boundary cells are handled by an interior exhaustion; their contribution vanishes in the no-trace formulation.

Consequently, for fixed \(\varepsilon,\delta\), sending \(h/\delta\to0\), then \(\delta\to0\), gives
\[
\limsup F(v_{\varepsilon,\delta,h})
\le\int_\Omega\|\nabla c^\varepsilon\|_*\,dx
+C|\Omega|\omega_\varepsilon(\delta).
\]
The local grid values converge to \(c^\varepsilon\) in \(L^1\), with error \(O(h\|\nabla c^\varepsilon\|_\infty)\). Choose \(\delta\downarrow0\), then \(h/\delta\downarrow0\), and finally diagonalize \(\varepsilon\downarrow0\). This yields \(v_n\to c\) in \(L^1\) and
\[
\limsup_nF(v_n)\le\int_\Omega\|\nabla c\|_*\,dx.
\]
Together with the lower bound, this proves the formula.

**Geometric scope:** the argument uses shape-regular macro-polygons and a finite Caccioppoli partition at each stage. The boundary and macro-interface estimates are essential; the SVD alone would not establish recovery.

## 4. Exact prescribed-gradient consequence

Set \(u_n(x)=Gx+v_n(x)\). Since each \(v_n\) is piecewise constant,
\[
\nabla u_n=G\quad\text{a.e. exactly}.
\]
The jump cost of \(u_n\) is \(F(v_n)\). Hence the variable-field isotropic correction is recovered without perturbing the prescribed bulk gradient.

## 5. Facewise functional and limitations

For polygonal faces \(F_f\), fixed \(\widetilde G_f\), and an interior no-trace formulation, the face contribution relaxes to
\[
\int_{F_f}\left[W(\widetilde G_f)+
\|\nabla g_f-\widetilde G_f\|_*\right]\,d\mathcal H^2.
\]
The macro-jump term is separate. Compatibility across C60 edges and prescribed traces are not covered by this interior construction.

## 6. Anisotropic bounds

For \(\psi(a,\nu)=\Phi(a)k(\nu)\), with \(\Phi\) a norm and \(k\) even, the dual lower bound is
\[
\mathcal C_{\Phi,k}(M)\ge
\sup_{Q:\Phi^\circ(Q\nu)\le k(\nu)\ \forall\nu}Q:M.
\]
A two-direction orthogonal laminate gives the upper bound
\[
\mathcal C_{\Phi,k}(M)\le
\inf_{(v_1,v_2)\ {\rm ONB}}\sum_i k(v_i)\Phi(Mv_i).
\]
Equality for general \(\Phi,k\) is not claimed. For \(\Phi=|\cdot|\) and \(k=1\), both bounds equal \(\|M\|_*\).

## 7. Rank statement

For \(u_h(\xi)=\widetilde G\xi+b+Mq_h(\xi)\), \(\nabla u_h=\widetilde G\) a.e. If \(\widetilde G=cA\), \(c>0\), \(A^TA=I_2\), then \(\operatorname{rank}\nabla u_h=2\) a.e. This does not imply classical immersion across jump interfaces or global embeddedness.
