# T135 — Bernstein–Neumann certified rational integration on triangles

**Classification:** **[P] Proved under explicit hypotheses** for the local inclusion, geometric order bound, global inclusion, and finite-order termination on an already certified finite partition. The rational Bernstein quotient enclosure is a pre-existing lemma (Theorem 4.1, equation (11), p. 5, in the cited 2022 paper); the Neumann-polynomial/residual construction and the quantitative bound below are the proposed method's results. Computational validation is recorded separately. This theorem does **not** claim that the complete Morandotti 55-entry IPDG assembly or the downstream LDL certificate has been proved by this result.

## 1. Bernstein quotient enclosure (pre-existing lemma)

Let \(T\subset\mathbb R^2\) be a nondegenerate closed triangle. Let \(a,g\in\mathbb R[\xi,\eta]\), and represent both in the same Bernstein basis of degree \(D\), with
\[
D\geq\max\{\deg a,\deg g\},
\]
as
\[
a(x)=\sum_{|\alpha|=D}a_\alpha B_\alpha^D(x),
\qquad
g(x)=\sum_{|\alpha|=D}g_\alpha B_\alpha^D(x).
\]
Assume \(g_\alpha>0\) for every index. Define
\[
\ell=\min_{|\alpha|=D}\frac{a_\alpha}{g_\alpha},
\qquad
u=\max_{|\alpha|=D}\frac{a_\alpha}{g_\alpha}.
\]
Then
\[
\boxed{\ell\leq \frac{a(x)}{g(x)}\leq u\quad(x\in T).}
\]

**Proof.** Bernstein basis functions are nonnegative on \(T\) and sum to one. In particular,
\[
g(x)\geq\min_\alpha g_\alpha>0.
\]
Set
\[
w_\alpha(x)=\frac{g_\alpha B_\alpha^D(x)}{g(x)}.
\]
Then \(w_\alpha(x)\geq0\), \(\sum_\alpha w_\alpha(x)=1\), and
\[
\frac{a(x)}{g(x)}
=\sum_\alpha w_\alpha(x)\frac{a_\alpha}{g_\alpha}.
\]
The quotient is a convex combination of the coefficient ratios, proving the enclosure, including on the boundary of \(T\). No sign assumption on \(a\) is required. \(\square\)

The lemma is used as an external ingredient; it is not claimed as a new result of T135.

## 2. Setting and Neumann-residual construction

Let \(p,g\in\mathbb R[\xi,\eta]\), and suppose \(g\) has a Bernstein representation of degree \(d_g\geq\deg g\) on \(T\) whose coefficients satisfy
\[
0<\gamma_T:=\min_{|\alpha|=d_g}b_\alpha(g,d_g,T)
\leq
\max_{|\alpha|=d_g}b_\alpha(g,d_g,T)=:G_T.
\]
Define
\[
m_T=\frac{\gamma_T+G_T}{2},
\qquad
z_T=1-\frac{g}{m_T},
\qquad
\rho_T=\frac{G_T-\gamma_T}{G_T+\gamma_T}\in[0,1).
\]
Choose \(d_p\geq\deg p\), and define
\[
A_T=\max_{|\alpha|=d_p}|b_\alpha(p,d_p,T)|.
\]

For an integer \(N\geq0\), set
\[
s_{T,N}=\frac{p}{m_T}\sum_{k=0}^{N}z_T^k,
\qquad
a_{T,N}=p\,z_T^{N+1}.
\]
The finite geometric-series identity gives the exact polynomial/rational decomposition
\[
\boxed{\frac pg=s_{T,N}+\frac{a_{T,N}}g.}
\tag{2.1}
\]

Choose a common Bernstein degree
\[
D_N\geq\max\{\deg a_{T,N},\deg g\}.
\]
Write
\[
a_{\alpha,N}=b_\alpha(a_{T,N},D_N,T),
\qquad
g_{\alpha,N}=b_\alpha(g,D_N,T),
\]
and define
\[
\ell_{T,N}=\min_{|\alpha|=D_N}\frac{a_{\alpha,N}}{g_{\alpha,N}},
\qquad
u_{T,N}=\max_{|\alpha|=D_N}\frac{a_{\alpha,N}}{g_{\alpha,N}}.
\]
The denominator coefficients remain strictly positive under degree elevation, so these ratios are well-defined.

## 3. Theorem — local certified inclusion and geometric order bound

**Theorem 3.1.** Under the hypotheses of §2, define
\[
\mathbf I_{T,N}
=
\int_Ts_{T,N}(x)\,dx
+
|T|[\ell_{T,N},u_{T,N}],
\]
where the polynomial integral is exact. Then:

1. (**Local inclusion**)
   \[
   \boxed{\int_T\frac{p(x)}{g(x)}\,dx\in\mathbf I_{T,N}.}
   \tag{3.1}
   \]

2. (**Geometric width estimate**)
   \[
   \boxed{
   \operatorname{wid}(\mathbf I_{T,N})
   \leq
   \frac{2|T|A_T}{\gamma_T}\rho_T^{N+1}.
   }
   \tag{3.2}
   \]

3. In particular,
   \[
   \lim_{N\to\infty}\operatorname{wid}(\mathbf I_{T,N})=0.
   \]

**Proof.**

For (3.1), apply the Bernstein quotient enclosure of §1 to \(a_{T,N}/g\). It gives
\[
\ell_{T,N}\leq a_{T,N}(x)/g(x)\leq u_{T,N}
\quad(x\in T).
\]
Integrate this inequality and use the exact identity (2.1).

For (3.2), first observe that the degree-\(d_g\) Bernstein coefficients of \(z_T\) are
\[
1-\frac{b_\alpha(g,d_g,T)}{m_T}.
\]
Since \(b_\alpha(g,d_g,T)\in[\gamma_T,G_T]\), each such coefficient has absolute value at most \(\rho_T\).

For Bernstein polynomials of degrees \(d,e\), the coefficient of their product at multi-index \(\gamma\) is
\[
b_\gamma(fh,d+e,T)
=
\sum_{\alpha+\beta=\gamma}
\frac{\binom d\alpha\binom e\beta}
     {\binom{d+e}\gamma}
b_\alpha(f,d,T)b_\beta(h,e,T).
\]
The weights are nonnegative and sum to one by the multivariate Vandermonde identity. Thus every product coefficient is a convex combination of products of factor coefficients. Repeated application gives
\[
\max_\alpha
|b_\alpha(pz_T^{N+1},d_p+(N+1)d_g,T)|
\leq A_T\rho_T^{N+1}.
\tag{3.3}
\]

**Degree convention.** If a product or common representation uses a degree larger than \(d_p\), first elevate \(p\) to the required degree. Degree elevation expresses each new Bernstein coefficient as a convex combination of old coefficients; hence its maximum absolute coefficient cannot exceed \(A_T\). Likewise, degree elevation of \(g\) preserves the lower bound \(\gamma_T\), because each elevated coefficient is a convex combination of old coefficients. Therefore (3.3) and
\[
g_{\alpha,N}\geq\gamma_T
\]
hold at the common degree \(D_N\).

Consequently,
\[
\left|\frac{a_{\alpha,N}}{g_{\alpha,N}}\right|
\leq\frac{A_T}{\gamma_T}\rho_T^{N+1}.
\]
The difference between the largest and smallest such ratios is at most twice this bound:
\[
u_{T,N}-\ell_{T,N}
\leq\frac{2A_T}{\gamma_T}\rho_T^{N+1}.
\]
The polynomial integral is an exact translation of the interval, so
\[
\operatorname{wid}(\mathbf I_{T,N})
=|T|(u_{T,N}-\ell_{T,N}),
\]
which proves (3.2). Since \(0\leq\rho_T<1\), the width tends to zero. \(\square\)

## 4. Theorem — global inclusion and exact width additivity

Let \(\widehat K\) be a reference triangle and let
\[
\mathcal L=\{T_1,\ldots,T_M\}
\]
be a finite partition of \(\widehat K\), with pairwise disjoint interiors and union \(\widehat K\). Suppose the hypotheses of Theorem 3.1 hold on every leaf \(T_j\), possibly with leaf-dependent quantities \(\gamma_{T_j},G_{T_j},A_{T_j},\rho_{T_j}\) and orders \(N_j\).

Set
\[
\mathbf I_{\mathcal L}
=\sum_{j=1}^{M}\mathbf I_{T_j,N_j}.
\]
Then
\[
\boxed{
\int_{\widehat K}\frac pg\in\mathbf I_{\mathcal L}.
}
\tag{4.1}
\]
Moreover, for the usual interval sum in exact arithmetic,
\[
\boxed{
\operatorname{wid}(\mathbf I_{\mathcal L})
=
\sum_{j=1}^{M}|T_j|
(u_{T_j,N_j}-\ell_{T_j,N_j})
\leq
\sum_{j=1}^{M}
\frac{2|T_j|A_{T_j}}{\gamma_{T_j}}
\rho_{T_j}^{N_j+1}.
}
\tag{4.2}
\]

**Proof.** The local inclusions and additivity of the integral over a finite partition give (4.1). Write each interval as \(\mathbf I_{T_j,N_j}=[L_j,U_j]\). The usual interval sum is exactly
\[
\sum_j[L_j,U_j]=[\sum_jL_j,\sum_jU_j].
\]
Therefore its width is
\[
\sum_jU_j-\sum_jL_j
=\sum_j(U_j-L_j),
\]
which proves the equality in (4.2). The inequality follows by summing (3.2). \(\square\)

The equality is an exact-arithmetic statement for ordinary interval addition. A floating-point interval implementation must additionally ensure outward rounding in every local operation and in the global endpoint sums.

## 5. Corollary — finite-order termination on a certified partition

For any fixed finite partition \(\mathcal L\) satisfying the hypotheses of §4 and any \(\varepsilon>0\), there exist finite orders \(N_1,\ldots,N_M\) such that
\[
\operatorname{wid}(\mathbf I_{\mathcal L})\leq\varepsilon.
\]

**Proof.** For each fixed leaf, the right-hand side of (3.2) tends to zero geometrically as its order tends to infinity. Since there are finitely many leaves, choose a finite order on each leaf so that the sum of the local upper bounds is at most \(\varepsilon\). Then (4.2) gives the result. \(\square\)

This is a termination result for order escalation on a partition whose denominator coefficients are already certified positive. It does not prove termination of an arbitrary adaptive procedure that must discover a valid partition, nor does it give a complexity bound.

## 6. Application target: curved-P3 Morandotti IPDG volume entries

For the mapped cubic geometry used in the Morandotti volume Hessian form, the target rational integrands have the structure
\[
\frac{p_{ij}(\xi,\eta)}{g(\xi,\eta)},
\qquad
g=(\det J)^5,
\qquad 1\leq i\leq j\leq10,
\]
giving 55 symmetric entries.

On each leaf \(T\), the method can use a common denominator certificate \((\gamma_T,G_T,m_T,\rho_T)\), while the numerator bounds \(A_{ij,T}\) and orders \(N_{ij,T}\) may differ. A common geometric tree is an implementation strategy, not a consequence required by the theorem. The theorem remains valid with separate leaf partitions and orders for different entries.

The theorem certifies rational integrals only when the stated Bernstein denominator condition is verified on every leaf. It does not by itself certify the derivation of the \(p_{ij}\), the geometry-to-reference transformation, finite-precision implementation, assembly of the complete IPDG operator, or the subsequent LDL coercivity inequality.

## 7. Evidence and scientific-status boundary

- **Proved:** local inclusion, geometric order-width estimate, global inclusion, exact interval-width additivity, and finite-order termination on an already certified finite partition.
- **Pre-existing ingredient:** rational Bernstein coefficient-ratio enclosure (§1), attributed to Theorem 4.1, equation (11), p. 5, of the 2022 paper supplied with this project.
- **Prototype/computational evidence:** exact-rational polynomial and Bernstein operations, local enclosure tests, and an initial adaptive subdivision experiment are documented separately in the development record and the Bernstein-residual prototype PR.
- **Not implied by T135:** termination of every adaptive tree-search strategy; a universal complexity estimate; superiority over the existing Neumann remainder integrator; validation of all 55 actual curved-P3 integrands; end-to-end interval assembly; or propagation to a successful LDL certificate.
- **Novelty:** T135 records the specific Neumann-polynomial plus Bernstein-residual construction and its quantitative bound. It does not claim priority for the underlying Bernstein enclosure or for the elementary finite geometric-series identity. A novelty claim requires a separate targeted literature comparison.

## 8. Reference and implementation record

- 2022 source paper supplied in the project discussion: Theorem 4.1, equation (11), p. 5 (rational Bernstein coefficient-ratio enclosure).
- Prototype implementation and tests: [PR #288 — Bernstein-residual integration prototype](https://github.com/fabianleonaressi95/theorem/pull/288).
- Related predecessor record: [T134 — exact integration and finite-mesh trace certification](T134-exact-integration-certification-gap.md).

