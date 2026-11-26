# TSMR-F — Morphological recursion and multifractal spectrum

**Record type:** proposed synthesis / exact special-case identities  
**Status:** definitions exact; Cantor–Bernoulli formulas exact under the stated separation model; anisotropic pressure implemented as a finite-level diagnostic. This record does **not** claim a new general dimension theorem or a physical law.

## 1. Recursive geometry

Let \(X=\mathbb R^d\), and let
\[
w_i(x)=A_i x+b_i,\qquad i=1,\ldots,m,
\]
be affine contractions. For a nonempty compact set \(K_0\), define
\[
\mathcal T(K)=\bigcup_{i=1}^m w_i(K),\qquad
K_{n+1}=\mathcal T(K_n).
\]
Under the usual Hutchinson hypotheses (a finite family of contractions on a complete metric space), there is a unique nonempty compact invariant attractor \(K\) satisfying \(K=\mathcal T(K)\). The set recursion describes geometry; it does not by itself imply a non-integer dimension or multifractality.

## 2. Invariant probability measure

For probabilities \(p_i\geq0\), \(\sum_i p_i=1\), the associated self-similar measure satisfies
\[
\mu=\sum_{i=1}^m p_i(w_i)_\#\mu.
\]
Here \((w_i)_\#\mu(E)=\mu(w_i^{-1}(E))\) is the push-forward. The geometry is determined by the maps; the statistical weighting is additionally determined by the \(p_i\). A geometrically fractal support can carry a monofractal measure, and a nonuniform measure is not automatically multifractal without scale-dependent moment evidence.

## 3. Partition sums and generalized dimensions

For a mesh or covering at scale \(\varepsilon\), let \(\mu_j(\varepsilon)\) be the mass in cell \(j\), omitting zero-mass cells. Define
\[
Z(q,\varepsilon)=\sum_j\mu_j(\varepsilon)^q.
\]
When the limit exists,
\[
\tau(q)=\lim_{\varepsilon\downarrow0}
\frac{\log Z(q,\varepsilon)}{\log\varepsilon}.
\]
For \(q\ne1\), \(D_q=\tau(q)/(q-1)\). At \(q=1\), the information dimension is
\[
D_1=\tau'(1)
\]
when \(\tau\) is differentiable there; equivalently it is obtained from the Shannon entropy scaling. The formal \(q=0\) case counts occupied cells and gives the box-counting dimension when that limit exists. Negative \(q\) requires care with arbitrarily small cell masses and is not included in the reference implementation.

If \(\tau\) is differentiable and the multifractal formalism applies, set
\[
\alpha=\tau'(q),\qquad f(\alpha)=q\alpha-\tau(q).
\]
More generally the Legendre-Fenchel candidate spectrum is
\[
f_{\mathrm{LF}}(\alpha)=\inf_q\{q\alpha-\tau(q)\}.
\]
Equality between this transform and the true Hausdorff spectrum requires additional hypotheses; it is not automatic for arbitrary measures.

## 4. Exact separated Cantor–Bernoulli model

For the two-map Cantor IFS with common contraction ratio \(r\in(0,1)\), disjoint images, and weights \(p,1-p\), the level-\(n\) cylinder masses are \(p_w\), and
\[
Z_n(q)=\bigl(p^q+(1-p)^q\bigr)^n,\qquad
\varepsilon_n=r^n.
\]
Consequently, for \(q\ne1\),
\[
\tau(q)=\frac{\log(p^q+(1-p)^q)}{\log r},\qquad
D_q=\frac{\log(p^q+(1-p)^q)}{(q-1)\log r}.
\]
At \(q=1\),
\[
D_1=-\frac{p\log p+(1-p)\log(1-p)}{\log(1/r)}.
\]
For \(p=1/2\), all \(D_q=\log2/\log(1/r)\): the measure is monofractal in this model. For \(p\ne1/2\), the generalized dimensions depend on \(q\), giving a multifractal Bernoulli measure on the separated Cantor support. These are exact model identities, not empirical claims about a physical vesica.

## 5. Anisotropic self-affine pressure

For a \(2\times2\) matrix \(A\), let \(\sigma_1(A)\geq\sigma_2(A)>0\) be its singular values and define the singular-value function
\[
\phi^s(A)=
\begin{cases}
\sigma_1(A)^s,&0\leq s\leq1,\\
\sigma_1(A)\sigma_2(A)^{s-1},&1\leq s\leq2.
\end{cases}
\]
For a word \(u=(i_1,\ldots,i_n)\), set \(A_u=A_{i_1}\cdots A_{i_n}\) and \(p_u=\prod_k p_{i_k}\). The finite-level quantity implemented in the audit is
\[
P_n(q,s)=\frac1n\log\sum_{|u|=n}p_u^q\phi^s(A_u)^{1-q}.
\]
A limiting pressure may be studied as \(n\to\infty\). Roots or zeros of this pressure are not automatically the generalized dimensions of the invariant measure: overlap, separation, dominated-splitting and other hypotheses matter. The code reports \(P_n\) only and labels it a finite-level diagnostic.

## 6. Unified TSMR-F system

The compact synthesis is
\[
\boxed{
\begin{aligned}
K_{n+1}&=\bigcup_i(A_iK_n+b_i),\\
\mu_{n+1}&=\sum_i p_i(w_i)_\#\mu_n,\\
Z(q,\varepsilon)&=\sum_j\mu_j(\varepsilon)^q,\\
\tau(q)&=\lim_{\varepsilon\downarrow0}
\frac{\log Z(q,\varepsilon)}{\log\varepsilon},\\
f_{\mathrm{LF}}(\alpha)&=\inf_q(q\alpha-\tau(q)).
\end{aligned}}
\tag{TSMR-F}
\]
The first two lines specify recursive morphology and its probability measure. The last three extract scale exponents and a candidate spectrum. The existence of the limits and the validity of the multifractal formalism are separate mathematical questions.

## 7. Verification plan and scope

The companion audit and tests cover:
- exact generalized dimensions for separated two-branch Cantor–Bernoulli measures;
- the uniform-weight monofractal identity and nonuniform-weight \(q\)-dependence;
- the information-dimension limit;
- finite-level anisotropic singular-value pressure, including a scalar/isotropic special case.

The earlier TSMR-03 vesica code samples and deforms a lens and constructs finite recursive generations. A single ellipse or vesica is not thereby a fractal. A finite box-count slope is not a proof of an asymptotic dimension. Connecting the measure above to a vesica requires an explicit IFS, weights, scale convention, and validation of separation/overlap assumptions.

**Classification:** TSMR-F is a proposed organizing framework. The Hutchinson attractor theorem and the separated Cantor–Bernoulli formulas are established mathematics. Numerical outputs from finite-depth pressure or finite-scale box counts are diagnostics, not proofs. No Gödelian, physical, or quantum-gravity conclusion is asserted.


## 8. Arithmetic overlaps and external thresholds

The complementary audit [TSMR-F_DEAQUINO_GOLDEN_BERNOULLI_BRIDGE.md](../audits/TSMR-F_DEAQUINO_GOLDEN_BERNOULLI_BRIDGE.md) records three distinct appearances of (1/2): the De Aquino golden identity (arphi=1/2+sqrt5/2) after imposing the model's zero threshold; the squared projection norm (\|Pq\|^2=1/2) for the regular pentagonal frame; and, separately, Bernoulli probability (p=1/2) or contraction ratio (\lambda=1/2). They are not interchangeable. The audit also corrects the raw finite-level golden-coding distinct-sum counts and distinguishes them from the Fibonacci overlap graph in the literature.
