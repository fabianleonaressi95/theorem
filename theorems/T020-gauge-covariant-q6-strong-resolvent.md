# T020 — Gauge-covariant strong-resolvent convergence of the Q6 Wilson refinement

**Status: PROVED for each fixed smooth SU(3) connection on the periodic six-torus, with the cell-average discretization and parallel-transport links specified below.** The first-order consistency estimate (C) is proved in Section 4, and the generalized strong-resolvent conclusion follows in Section 5. This does not claim norm-resolvent convergence or an interacting gauge-field continuum limit.

## 1. Continuum data

Let \(\mathbb T^6_2=(\mathbb R/2\mathbb Z)^6\), \(h_n=1/n\), and \(\Lambda_n=(\mathbb Z/2n\mathbb Z)^6\). The cell centre is \(x_j=h_n(j+\frac12\mathbf1)\), and \(Q_{n,j}=x_j+[-h_n/2,h_n/2)^6\), interpreted periodically. Equip \(\mathcal H_n=\ell^2(\Lambda_n;\mathbb C^{24})\) with \(\langle u,v\rangle_n=h_n^6\sum_j\langle u(j),v(j)\rangle\). Define cell averaging and piecewise-constant embedding by \((P_nf)(j)=h_n^{-6}\int_{Q_{n,j}}f(y)\,dy\) and \((J_nu)|_{Q_{n,j}}=u(j)\). Then \(J_n\) is isometric, \(P_n=J_n^*\), and \(J_nP_n=\Pi_n\) is the orthogonal projection onto cellwise constants. Let \(\mathcal A_i\in C^\infty(\mathbb T^6_2;\mathfrak{su}(3))\), with anti-Hermitian convention, and set
\[
\mathcal H=L^2(\mathbb T^6_2;\mathbb C^8\otimes\mathbb C^3),\qquad
A_{\mathcal A}=m_0I+\sum_{i=1}^6(\Gamma_i\otimes I_3)(\partial_i+\mathcal A_i).
\]
The domain is \(H^1(\mathbb T^6_2;\mathbb C^{24})\). The \(\Gamma_i\) are Hermitian Clifford matrices. Since the free Dirac operator \(\sum_i\Gamma_i\partial_i\) is skew-adjoint on \(H^1\), and \(\sum_i\Gamma_i\mathcal A_i\) is a bounded skew-adjoint multiplication operator, \(A_{\mathcal A}-m_0\) is skew-adjoint on \(H^1\).

## 2. Link fields and lattice operator

For each oriented positive edge \((x_j,x_j+he_i)\), let \(U_{n,i}(j)\in SU(3)\) be the inverse-oriented parallel transporter (from the endpoint fibre back to the base-point fibre), with the convention
\[
U_{n,i}(j)=U_i(x_j;h),\qquad \frac{d}{dt}U_i(x_j;t)=U_i(x_j;t)\mathcal A_i(x_j+te_i),\quad U_i(x_j;0)=I,\quad 0\le t\le h.
\]
Define the unitary covariant shift
\[
(S_{n,i}\psi)(j)=(I_8\otimes U_{n,i}(j))\psi(j+e_i).
\]
For fixed \(r>0\), define
\[
A_n^{\mathcal A}=m_0I+
\frac1{2h}\sum_i(\Gamma_i\otimes I_3)(S_{n,i}-S_{n,i}^*)
+\frac r{2h}\sum_i(2I-S_{n,i}-S_{n,i}^*).
\]
The centered term is anti-Hermitian. Moreover,
\[
\langle\psi,(2I-S_{n,i}-S_{n,i}^*)\psi\rangle_n
=\|(I-S_{n,i})\psi\|_n^2\geq0.
\]
Thus for every \(z\) with \(\Re z<m_0\),
\[
\|(A_n^{\mathcal A}-z)^{-1}\|\leq(m_0-\Re z)^{-1}.
\]
This estimate is exact and independent of the link field and lattice spacing.

## 3. Gauge covariance

For a smooth continuum gauge transformation \(g:\mathbb T^6_2\to SU(3)\), use \(\mathcal A_i^g=g\mathcal A_i g^{-1}-(\partial_i g)g^{-1}\). The right-ordered link ODE in Section 2 then gives \(U_{n,i}^g(j)=g(x_j)U_{n,i}(j)g(x_j+he_i)^{-1}\). More generally, for any sitewise gauge transformation \(g_n(j)\in SU(3)\), let
\[
U^g_{n,i}(j)=g_n(j)U_{n,i}(j)g_n(j+e_i)^{-1},
\qquad (G_n\psi)(j)=(I_8\otimes g_n(j))\psi(j).
\]
Then \(S^g_{n,i}=G_nS_{n,i}G_n^{-1}\), and consequently
\[
A_n^{\mathcal A^g}=G_nA_n^{\mathcal A}G_n^{-1}.
\]
This is an exact finite-dimensional identity, not an asymptotic statement.

## 4. Cell-average consistency: proof of (C)

Write \(D_i=\partial_i+\mathcal A_i\), \(p_n=P_n\phi\), and let \(M_k(\mathcal A)\) and \(M_k(\phi)\) denote the maximum operator/vector sup norms of all derivatives of order at most \(k\), over the finitely many components and directions. These quantities are finite for the fixed smooth fields considered here.

**Lemma (forward/backward cell expansion).** For every \(\phi\in C^\infty(\mathbb T^6_2;\mathbb C^{24})\), there is a constant \(C_0=C_0(M_1(\mathcal A),M_0(\mathcal A),M_2(\phi),M_1(\phi))\), independent of \(n\), \(j\), and \(i\), such that, for \(h=h_n\le1\),
\[
\begin{aligned}
(S_{n,i}p_n)(j)&=p_n(j)+h(P_nD_i\phi)(j)+R^+_{n,i}(j),\\
(S_{n,i}^*p_n)(j)&=p_n(j)-h(P_nD_i\phi)(j)+R^-_{n,i}(j),\\
\max_j\bigl(\|R^+_{n,i}(j)\|+\|R^-_{n,i}(j)\|\bigr)&\le C_0h^2.
\end{aligned}
\]

**Proof.** By the definition of cell averages and translation of the cell,
\[
(P_n\phi)(j+e_i)=h^{-6}\int_{Q_{n,j}}\phi(y+he_i)\,dy
=(P_n\phi)(j)+h(P_n\partial_i\phi)(j)+O(h^2M_2(\phi)).
\]
The transport ODE and one integration of its integral equation give the uniform expansion
\[
U_{n,i}(j)=I+h\mathcal A_i(x_j)+O\!\left(h^2\,[M_1(\mathcal A)+M_0(\mathcal A)^2e^{M_0(\mathcal A)}]\right).
\]
Moreover, by the mean-value estimate on each cell,
\[
\|\mathcal A_i(x_j)(P_n\phi)(j)-(P_n(\mathcal A_i\phi))(j)\|
\le C h\,[M_1(\mathcal A)M_0(\phi)+M_0(\mathcal A)M_1(\phi)].
\]
Multiplying the two expansions proves the forward formula. For the backward shift, use
\[
(P_n\phi)(j-e_i)=(P_n\phi)(j)-h(P_n\partial_i\phi)(j)+O(h^2M_2(\phi))
\]
and, since \(\mathcal A_i^*=-\mathcal A_i\),
\[
U_{n,i}(j-e_i)^*=I-h\mathcal A_i(x_j)+O(h^2 C_{\mathcal A}).
\]
The same cellwise mean-value estimate gives the backward formula. All constants are uniform because the torus is compact and the connection and section are fixed and smooth. \(\square\)

Subtracting and adding the two expansions yields
\[
\left\|\frac{S_{n,i}-S_{n,i}^*}{2h}P_n\phi-P_nD_i\phi\right\|_n
\le C_1h,
\qquad
\left\|(2I-S_{n,i}-S_{n,i}^*)P_n\phi\right\|_n
\le C_1h^2.
\]
Consequently, for fixed \(r>0\),
\[
\|A_n^{\mathcal A}P_n\phi-P_nA_{\mathcal A}\phi\|_n
\le C_2(\mathcal A,\phi,r,m_0)h.
\]
Finally, the standard cellwise Poincaré estimate gives
\[
\|J_nP_n\phi-\phi\|_{\mathcal H}
\le C_6h\|\nabla\phi\|_{L^2},\qquad
\|J_nP_n(A_{\mathcal A}\phi)-A_{\mathcal A}\phi\|_{\mathcal H}
\le C_6h\|\nabla(A_{\mathcal A}\phi)\|_{L^2}.
\]
Using that \(J_n\) is an isometry, we obtain the explicit order statement
\[
\boxed{\;
\|J_nA_n^{\mathcal A}P_n\phi-A_{\mathcal A}\phi\|_{\mathcal H}
\le C(\mathcal A,\phi,r,m_0)h_n,\qquad
\|J_nP_n\phi-\phi\|_{\mathcal H}\le C_6h_n\|\nabla\phi\|_{L^2}.
\;}
\tag{C}
\]
Thus (C) is proved for every fixed smooth periodic connection and smooth periodic section. The estimate is first order and is uniform in the lattice cell and direction; its constant depends on finitely many sup norms of the fixed smooth data. No uniformity over unbounded families of connections is asserted.

## 5. Strong-resolvent theorem

**Theorem.** For every fixed \(\mathcal A_i\in C^\infty(\mathbb T^6_2;\mathfrak{su}(3))\), every \(r>0\), every \(z\in\mathbb C\) with \(\Re z<m_0\), and every \(f\in\mathcal H\),
\[
J_n(A_n^{\mathcal A}-z)^{-1}J_n^*f
\longrightarrow
(A_{\mathcal A}-z)^{-1}f
\quad\text{strongly in }\mathcal H.
\]

**Proof.** The free operator \(\sum_i\Gamma_i\partial_i\) is skew-adjoint on \(H^1\). The multiplication operator \(\sum_i\Gamma_i\mathcal A_i\) is bounded and skew-adjoint, since each \(\mathcal A_i\) is anti-Hermitian and commutes with the spin matrices. Hence \(A_{\mathcal A}-m_0\) is skew-adjoint on \(H^1\), and \(A_{\mathcal A}-z\) is onto with inverse norm at most \((m_0-\Re z)^{-1}\). The finite-lattice accretivity estimate in Section 2 gives the same uniform bound for \((A_n^{\mathcal A}-z)^{-1}\).

First take \(f=(A_{\mathcal A}-z)\phi\) with \(\phi\in C^\infty\). The identity
\[
\begin{aligned}
J_n(A_n^{\mathcal A}-z)^{-1}J_n^*f-J_nP_n\phi
=J_n(A_n^{\mathcal A}-z)^{-1}
\bigl[J_n^*f-(A_n^{\mathcal A}-z)P_n\phi\bigr]
\end{aligned}
\]
and the uniform resolvent bound show that the right-hand side tends to zero: after applying the isometry \(J_n\), the bracket is
\[
\Pi_nf-J_n(A_n^{\mathcal A}-z)P_n\phi\longrightarrow
f-(A_{\mathcal A}-z)\phi=0
\]
by (C) and \(\Pi_n f\to f\). Also \(J_nP_n\phi\to\phi=(A_{\mathcal A}-z)^{-1}f\). Such \(f\) form a dense subset of \(\mathcal H\), because \(C^\infty\) is a core and \(A_{\mathcal A}-z\) is onto. The operators \(J_n(A_n^{\mathcal A}-z)^{-1}J_n^*\) are uniformly bounded, so convergence extends to every \(f\in\mathcal H\). \(\square\)

The result is generalized strong-resolvent convergence between the varying lattice spaces and \(\mathcal H\). It is not norm-resolvent convergence.

## 6. Controlled numerical audit

The companion script scripts/t020_gauge_covariant_q6_audit.py tests a genuinely non-Abelian smooth \(SU(3)\) connection. In direction \(i\), the Hermitian coefficient is
\[
H_i(x)=\alpha\left[\sin(\pi x_{i+1})+0.31\cos(\pi x_{i+2})\right]\lambda_{a_i},
\qquad \mathcal A_i(x)=iH_i(x),
\]
with indices read modulo six and
\[
(a_1,\ldots,a_6)=(1,4,6,2,5,7).
\]
The \(\lambda_a\) are the corresponding Hermitian Gell-Mann generators. Distinct directions therefore use noncommuting generators. Since each coefficient is independent of \(x_i\), the link
\[
U_i(x)=\exp\!\left(ihH_i(x+\tfrac h2e_i)\right)
\]
is the exact parallel transporter along that edge for this selected field.

The gauge test uses a site-dependent product of rotations generated by \(\lambda_2,\lambda_5,\lambda_7\), and applies the full matrix law
\[
U_i^g(x)=g(x)U_i(x)g(x+he_i)^\dagger,\qquad
\psi^g(x)=g(x)\psi(x).
\]
The audit records link unitarity and determinant-one residuals, the non-Abelian generator commutator, exact covariance residual, the Wilson quadratic-form identity and imaginary part, Clifford residual, and a two-level nodal consistency diagnostic. This legacy diagnostic evaluates the test spinor at cell centres rather than applying the exact cell-average map (P_n); it is therefore not the numerical verification of (C). The proof of (C) is the analytic cellwise estimate in Section 4.

**Local nodal numerical diagnostic (not the cell-average proof of (C)), \(\alpha=0.35,r=1,m_0=0.2\):**

| Diagnostic | \(n=2\) | \(n=3\) |
|---|---:|---:|
| Consistency error | 1.60064035 | 1.18427676 |
| Gauge-covariance residual | \(2.20\times10^{-16}\) | \(6.98\times10^{-16}\) |
| Link unitarity residual | \(7.11\times10^{-16}\) | \(7.86\times10^{-16}\) |
| Link determinant-one residual | \(5.55\times10^{-16}\) | \(5.55\times10^{-16}\) |
| Wilson identity residual | \(3.70\times10^{-15}\) | \(2.54\times10^{-14}\) |
| Wilson imaginary-form residual | \(4.76\times10^{-18}\) | \(1.14\times10^{-16}\) |
| Clifford residual | 0 | 0 |

The generator commutator norm is \(\sqrt2\), and the actual link commutator at the origin has norms 0.03708029 and 0.01135974 at the two levels. The sitewise gauge matrices also pass unitarity and determinant-one checks at roundoff scale. The test is therefore not confined to a common Cartan subgroup. The JSON report is stored at evidence/T020-gauge-covariant-audit-local.json.

**Evidence label:** the analytic cell-average estimate (C) is proved in Section 4. The finite-dimensional non-Abelian link/Wilson checks passed GitHub Actions run #7; the plaquette-curvature refinement and its assertions passed run #9 (PR #73). These numerical tests are independent corroboration, not the proof of (C).


## 7. Non-Abelian plaquette curvature audit

The link commutator alone is not a curvature test. The audit evaluates, for every coordinate pair i<j, the based plaquette

```
P_ij(x) = U_i(x) U_j(x+h e_i) U_i(x+h e_j)^dagger U_j(x)^dagger
```

and the continuum curvature in the anti-Hermitian convention

```
F_ij = partial_i A_j - partial_j A_i + [A_i,A_j].
```

Since P_ij is based at x, the curvature at the plaquette centre x_c=x+h(e_i+e_j)/2 is transported back to that base point. The audit uses the two half-edge transporters W from x to x_c and compares

```
(P_ij(x)-I)/h^2  with  W F_ij(x_c) W^dagger.
```

This frame transport is essential: direct comparison with an untransported curvature matrix at the plaquette centre is not gauge-covariant.

For alpha=0.35, 128 deterministic sampled base points and all 15 coordinate planes per point, the relative RMS residuals are:

| n | h | Relative RMS residual | Observed order |
|---:|---:|---:|---:|
| 2 | 0.5 | 0.152670666 | — |
| 3 | 0.3333 | 0.066368709 | 2.055 |
| 4 | 0.25 | 0.038092113 | 1.930 |
| 6 | 0.1667 | 0.017102969 | 1.975 |
| 8 | 0.125 | 0.009675618 | 1.980 |
| 12 | 0.0833 | 0.004303979 | 1.998 |

The sampled residual exhibits second-order scaling over these six finite refinements. This is numerical evidence for the selected smooth connection and link convention, not a proof of a uniform estimate over all plaquettes, all smooth connections, or the continuum limit. The script and CI workflow compute and assert this refinement trend.

## 8. Scope


**Proved:** first-order cell-average consistency (C) for fixed smooth connections; finite-lattice gauge covariance; Wilson positivity; uniform left-half-plane resolvent bound; generalized strong-resolvent convergence for every fixed smooth background connection.

**Not established:** norm-resolvent convergence, gauge-field integration, reflection positivity of a full interacting theory, fermion determinant control, interacting continuum QCD, confinement, baryon masses, or a derivation of a physical \(3+1\)-dimensional theory.
