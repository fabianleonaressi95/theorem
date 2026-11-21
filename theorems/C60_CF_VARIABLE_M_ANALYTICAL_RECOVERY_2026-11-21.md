# C60 — analytical closure of the variable-field isotropic CF cell cost

Status: **theorem, using the strict polyhedral BV-density lemma stated below**  
Date: 2026-11-21

This note closes the variable-field recovery argument for the isotropic jump density
\(\psi(a,\nu)=|a|\). It does not claim the general separable anisotropic cell formula.

## 1. Setting

Let \(F\subset\mathbb R^2\) be a bounded Lipschitz polygon, \(c\in W^{1,1}(F;\mathbb R^3)\), and \(G\in\mathbb R^{3\times2}\) fixed. Set \(M=\nabla c\). Consider
\[
u_n(x)=Gx+c_n(x),\qquad c_n\in SBV(F;\mathbb R^3),
\]
with \(\nabla c_n=0\) a.e. Thus \(\nabla u_n=G\) a.e. exactly. The jump cost is
\(\int_{J_{c_n}}|[c_n]|\,d\mathcal H^1\).
The statement is interior/local; trace constraints and boundary-layer costs are not included.

## 2. Theorem — variable-field nuclear-norm relaxation

For every \(c\in W^{1,1}(F;\mathbb R^3)\),
\[
\boxed{
\inf_{c_n\to c\text{ in }L^1}
\liminf_{n\to\infty}\int_{J_{c_n}}|[c_n]|\,d\mathcal H^1
=\int_F\|\nabla c(x)\|_*\,dx,
}
\]
where the admissible recovery functions are finite piecewise-constant functions. The norm on \(3\times2\) matrices is the nuclear norm.

### 2.1 Lower bound

If \(c_n\to c\) in \(L^1\) and the jump costs are bounded, then \(Dc_n\stackrel{*}{\rightharpoonup}Dc\), after subselection. For every \(Q\in C_c(F;\mathbb R^{3\times2})\) with \(\|Q(x)\|_{\rm op}\le1\),
\[
\begin{aligned}
\int_F Q:Dc_n
&=\int_{J_{c_n}}[c_n]\cdot Q\nu_{c_n}\,d\mathcal H^1\\
&\le\int_{J_{c_n}}|[c_n]|\,d\mathcal H^1.
\end{aligned}
\]
Passing to the weak-* limit and using the duality
\(\|M\|_*=\sup_{\|Q\|_{\rm op}\le1}Q:M\), with continuous test-field approximation, yields
\[
\int_F\|\nabla c\|_*\,dx
\le\liminf_n\int_{J_{c_n}}|[c_n]|\,d\mathcal H^1.
\]

## 3. Recovery — analytic construction

The upper bound is the strict polyhedral approximation property for the convex, positively 1-homogeneous variation \(N(Dc)=\int\|\frac{dDc}{d|Dc|}\|_*\,d|Dc|\).

### Lemma (strict polyhedral approximation)

For \(c\in W^{1,1}(F;\mathbb R^3)\), there exist finite piecewise-constant \(c_n\) such that
\[
c_n\to c\text{ in }L^1(F),\qquad
\int_{J_{c_n}}|[c_n]|\,d\mathcal H^1
\to\int_F\|\nabla c\|_*\,dx.
\]

### Construction / proof

1. **Smooth approximation.** By extension and mollification (or interior exhaustion), choose \(c^\varepsilon\in C^\infty\) with \(c^\varepsilon\to c\) in \(W^{1,1}\). Since the nuclear norm is continuous and bounded by a constant times the Frobenius norm,
   \[
   \int_F\|\nabla c^\varepsilon\|_*\,dx\to\int_F\|\nabla c\|_*\,dx.
   \]
2. **Local SVD laminate.** On a small cell \(P\) where \(\nabla c^\varepsilon\) varies by at most \(\omega(\operatorname{diam}P)\), freeze \(M_P=\nabla c^\varepsilon(x_P)\). Write
   \(M_P=\sum_{i=1}^2\sigma_i a_i\otimes v_i\), with \(a_i,v_i\) unit and \(v_i\) orthonormal. A two-scale staircase with interfaces normal to \(v_i\) and jumps parallel to \(a_i\) realizes the affine correction \(M_P(x-x_P)\); its limiting cost per area is \(\sum_i\sigma_i=\|M_P\|_*\). The laminate is cut off in a boundary strip of \(P\); choose the oscillation scale much smaller than the strip width, then the strip width much smaller than \(\operatorname{diam}P\), so its added cost is \(o(|P|)\).
3. **Partition and diagonalization.** Choose a polyhedral partition with mesh tending to zero. On each cell use the frozen-gradient laminate. The oscillation error is bounded by the modulus of continuity of \(\nabla c^\varepsilon\) times the cell area; boundary-strip errors are summable and tend to zero. First send laminate scale to zero for the fixed partition, then mesh to zero, then \(\varepsilon\to0\), and take a diagonal sequence. This gives \(L^1\) convergence and the upper bound by \(\int\|\nabla c\|_*\).

The local laminate step is the essential ingredient: a generic Cartesian staircase only yields \(|Me_1|+|Me_2|\), which need not equal \(\|M\|_*\). The SVD-oriented construction is required for the nuclear-norm value.

### Applying the lemma

Set \(u_n(x)=Gx+c_n(x)\). Since \(c_n\) is piecewise constant,
\[
\nabla u_n=G\quad\text{a.e.}
\]
and its jump cost is exactly the recovery cost in the lemma. This gives the matching upper bound and closes the interior relaxation.

## 4. Facewise functional

For polygonal faces \(F_f\), fixed \(\widetilde G_f\), and \(g_f-\widetilde G_fx\in W^{1,1}(F_f;\mathbb R^3)\), the interior face relaxation is
\[
I_{\rm rel}^{\rm face}
=\sum_f\int_{F_f}\left[
W(\widetilde G_f)+
\|\nabla g_f-\widetilde G_f\|_*
\right]\,d\mathcal H^2
+\sum_f\int_{J_{g_f}}|[g_f]|\,d\mathcal H^1.
\]
This is a face-interior formula. Compatibility of recovery sequences along C60 edges and any prescribed traces must be separately imposed; no edge cost is silently included.

## 5. Separable anisotropy — rigorous bounds

Let \(\Phi\) be a norm and \(k:S^1\to[0,\infty)\) even. For
\(\psi(a,\nu)=\Phi(a)k(\nu)\), the dual lower bound is
\[
\mathcal C_{\Phi,k}(M)\ge
\sup_{Q:\,\Phi^\circ(Q\nu)\le k(\nu)\ \forall\nu}Q:M.
\]
An orthogonal two-direction laminate gives
\[
\mathcal C_{\Phi,k}(M)\le
\inf_{(v_1,v_2)\ {\rm ONB}}\sum_{j=1}^2k(v_j)\Phi(Mv_j).
\]
Equality is not asserted for general \(\Phi,k\). For \(\Phi(a)=|a|\), \(k\equiv1\), the two bounds coincide with \(\|M\|_*\).

## 6. Rank statement

For the constant-face staircase \(u_h(\xi)=\widetilde G\xi+b+Mq_h(\xi)\), one has \(\nabla u_h=\widetilde G\) a.e. If \(A^TA=I_2\) and \(\widetilde G=cA\), \(c>0\), then
\[
\operatorname{rank}\nabla u_h=2\quad\text{a.e.}
\]
This is a rank-a.e. statement for a discontinuous SBV map, not classical immersion through jump interfaces or global embeddedness.

## 7. Status

- Variable-field isotropic nuclear-norm relaxation: **closed by the SVD-oriented strict polyhedral recovery construction, under the interior convention**.
- Prescribed-gradient recovery: **exact**, because the correction is piecewise constant.
- General separable anisotropic equality: **open**.
- Global embeddedness and edge compatibility: **open**.
