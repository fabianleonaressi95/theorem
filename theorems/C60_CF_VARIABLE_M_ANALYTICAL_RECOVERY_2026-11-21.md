# C60 — analytical closure of the variable-field isotropic CF cell cost

Status: **theorem (under the stated BV admissibility and boundary conventions)**  
Date: 2026-11-21

This note closes the variable-field recovery argument for the isotropic jump density
\(\psi(a,\nu)=|a|\). It does not claim the general separable anisotropic cell formula.

## 1. Setting

Let \(F\subset\mathbb R^2\) be a bounded Lipschitz polygon, let
\(c\in W^{1,1}(F;\mathbb R^3)\), and let \(G\in\mathbb R^{3\times2}\) be fixed.
Set \(M=\nabla c\). We consider maps
\[
u_h(x)=Gx+c_h(x),\qquad c_h\in SBV(F;\mathbb R^3),
\]
with \(\nabla c_h=0\) a.e., so that \(\nabla u_h=G\) a.e. exactly.
The jump cost is \(\int_{J_{c_h}}|[c_h]|\,d\mathcal H^1\).
Boundary effects are either excluded by local formulation or treated with the corresponding trace constraint; no boundary cost is included in the interior formula.

## 2. Theorem (variable-field nuclear-norm relaxation)

For every \(c\in W^{1,1}(F;\mathbb R^3)\),
\[
\boxed{
\inf_{c_h\to c\;\mathrm{in}\;L^1}
\liminf_{h\to0}
\int_{J_{c_h}}|[c_h]|\,d\mathcal H^1
=
\int_F\|\nabla c(x)\|_*\,dx,
}
\]
where the infimum is over piecewise-constant (hence SBV) approximants \(c_h\) and the right-hand side uses the nuclear norm of the \(3\times2\) derivative matrix. Equivalently, the relaxed singular cost of the prescribed defect field \(M(x)\) is \(\int_F\|M(x)\|_*dx\).

### 2.1 Lower bound

Let \(c_h\to c\) in \(L^1\) and assume \(\sup_h|Dc_h|(F)<\infty\). Then, after a subsequence,
\(Dc_h\stackrel{*}{\rightharpoonup}Dc\) as matrix-valued Radon measures.

For every \(Q\in C_c(F;\mathbb R^{3\times2})\) satisfying
\(\|Q(x)\|_{op}\le1\),
\[
\begin{aligned}
\int_F Q:Dc_h
&=\int_{J_{c_h}}[c_h]\cdot Q\nu_{c_h}\,d\mathcal H^1\\
&\le\int_{J_{c_h}}|[c_h]|\,d\mathcal H^1.
\end{aligned}
\]
Passing to the weak-* limit gives
\[
\int_F Q:\nabla c\,dx
\le\liminf_h\int_{J_{c_h}}|[c_h]|\,d\mathcal H^1.
\]
The pointwise duality \(\|M\|_* = \sup_{\|Q\|_{op}\le1}Q:M\), together with density of continuous compactly supported test fields in the dual representation of the absolutely continuous measure \(\nabla c\,dx\), yields
\[
\int_F\|\nabla c\|_*dx
\le\liminf_h\int_{J_{c_h}}|[c_h]|\,d\mathcal H^1.
\]

## 3. Recovery sequence (strict BV approximation)

The recovery is obtained from the strict-density theorem for piecewise-constant functions in BV, applied to the convex, positively 1-homogeneous matrix norm \(N(M)=\|M\_*\) (nuclear norm).

### Lemma

For \(c\in W^{1,1}(F;\mathbb R^3)\), there exists a sequence of finite piecewise-constant functions \(c_n\) such that
\[
c_n\to c\quad\text{in }L^1(F),\qquad
\int_{J_{c_n}}\|[c_n]\otimes\nu_{c_n}\|_*\,d\mathcal H^1
\to\int_F\|\nabla c\|_*dx.
\]
Since \([c_n]\otimes\nu\) is rank one, its nuclear norm equals its Frobenius norm and hence \(\|[c_n]\otimes\nu\|_*=|[c_n]|\).

### Proof outline of the lemma

1. Extend \(c\) locally across the polygonal boundary (or use an interior exhaustion when boundary traces are not prescribed), and mollify: \(c^\varepsilon=c*\rho_\varepsilon\). Then \(c^\varepsilon\to c\) in \(W^{1,1}\), so by continuity of the norm,
   \(\int N(\nabla c^\varepsilon)\to\int N(\nabla c)\).
2. For each fixed smooth \(c^\varepsilon\), approximate by values on a finite polyhedral partition with mesh \(\delta\). The jump across each facet is the difference of neighboring sampled values. Taylor expansion gives the facet difference as \(\delta\nabla c^\varepsilon\nu+o(\delta)\); summing facet costs and using the Riemann-sum convergence gives the total variation integral of \(N(\nabla c^\varepsilon)\). The partition can be chosen with boundary remainder tending to zero.
3. Choose \(\delta=\delta(\varepsilon)\) sufficiently small, then diagonalize \(\varepsilon\downarrow0\). This gives the stated L1 convergence and strict convergence of the N-variation.

The density lemma is the standard strict BV density construction for a convex 1-homogeneous variation; the above describes the smoothing, polyhedral discretization, and diagonal steps. If a boundary trace is prescribed, the approximation must be chosen trace-compatible; the theorem as stated is interior/local and makes no unsupported claim about an added boundary layer cost.

### Applying the lemma

Take \(u_n(x)=Gx+c_n(x)\). Since \(c_n\) is piecewise constant,
\[
\nabla u_n=G\quad\text{a.e.}
\]
and the jump cost equals \(\int_{J_{c_n}}|[c_n]|\). The lemma gives the matching upper bound. Together with Section 2.1, this proves the formula.

## 4. Consequence for the facewise C60 functional

For a finite collection of polygonal faces \(F_f\), with \(c_f\in W^{1,1}(F_f;\mathbb R^3)\) and fixed facewise \(\widetilde G_f\), the interior relaxation is
\[
\boxed{
I_{rel}=\sum_f\int_{F_f}
W(\widetilde G_f)+
\|\nabla g_f-\widetilde G_f\|_*\,d\mathcal H^2
+\sum_f\int_{J_{g_f}}|[g_f]|\,d\mathcal H^1,
}
\]
provided the macro-jump term is kept separate and the facewise recovery sequences are compatible with whatever edge/boundary conditions are imposed. The formula is an interior face result; edge compatibility is not silently absorbed.

## 5. Anisotropic case: what is proved analytically

Let \(\Phi\) be a norm and let \(k:S^1\to[0,\infty)\) be even. For
\(\psi(a,\nu)=\Phi(a)k(\nu)\), the rank-one dual constraint is
\[
\Phi^\circ(Q\nu)\le k(\nu)\quad\forall\nu\in S^1.
\]
Thus the lower bound
\[
\mathcal C_{\Phi,k}(M)\ge
\sup_{Q:\,\Phi^\circ(Q\nu)\le k(\nu)}Q:M
\]
is rigorous. An orthogonal two-direction laminate gives the upper bound
\[
\mathcal C_{\Phi,k}(M)\le
\inf_{(v_1,v_2)\,ONB}\sum_{j=1}^2k(v_j)\Phi(Mv_j).
\]
The equality of these expressions is **not asserted** for general \(\Phi,k\): it requires an additional argument identifying the relaxed rank-one convex envelope/cell formula. For \(\Phi(a)=|a|\) and \(k\equiv1\), both bounds equal \(\|M\|_*\), which is the isotropic theorem.

## 6. Rank statement

For the constant-face staircase \(u_h(\xi)=\widetilde G\xi+b+Mq_h(\xi)\), one has \(\nabla u_h=\widetilde G\) a.e. If \(A^TA=I_2\) and \(\widetilde G=cA\), \(c>0\), then
\[
\operatorname{rank}\nabla u_h=2\quad\text{a.e.}
\]
This is a rank-a.e. statement for a discontinuous SBV map, not classical immersion across jump interfaces or global embeddedness.

## 7. Status

- Variable-field isotropic nuclear-norm relaxation: **proved under the BV strict-density theorem and the stated interior/boundary convention**.
- Exact prescribed-gradient recovery: **proved**, because the recovery correction is piecewise constant.
- General separable anisotropic equality: **open**.
- Global embeddedness: **open**.
