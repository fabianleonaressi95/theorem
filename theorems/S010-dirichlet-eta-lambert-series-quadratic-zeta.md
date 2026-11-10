# Lemma S.10 — Dirichlet eta, Dedekind eta coefficients and the quadratic field of discriminant -31

**Status:** exact analytic identities. The lemma separates four distinct objects: Dedekind's modular eta function, Dirichlet's alternating eta function, Dirichlet \(L\)-functions, and the Euler/Dirichlet simplex distribution. The links below are identities, not notational identifications.

## 1. Dirichlet eta and its Mellin transform

Define the Dirichlet eta function
\[
\eta_D(s)=\sum_{n\ge1}\frac{(-1)^{n-1}}{n^s}
=(1-2^{1-s})\zeta(s).
\]
The alternating series converges for \(\Re s>0\), and the right-hand side gives its entire continuation, with the removable value \(\eta_D(1)=\log2\).

For \(\Re s>0\),
\[
\boxed{\Gamma(s)\eta_D(s)
=\int_0^\infty\frac{x^{s-1}}{e^x+1}\,dx.}
\]
This is the Mellin transform of the Fermi–Dirac kernel. It is a direct Gamma–Dirichlet-eta bridge.

## 2. Dedekind eta and divisor-sum Dirichlet series

For \(\tau\in\mathbb H\), \(q=e^{2\pi i\tau}\), and
\[
\eta_{\rm Ded}(\tau)=q^{1/24}\prod_{n\ge1}(1-q^n),
\]
take the logarithm of the convergent product:
\[
\begin{aligned}
\log\eta_{\rm Ded}(\tau)
&=\frac{\pi i\tau}{12}
+\sum_{n\ge1}\log(1-q^n)\\
&=\frac{\pi i\tau}{12}
-\sum_{m\ge1}\sigma_{-1}(m)q^m,
\end{aligned}
\]
where
\[
\sigma_{-1}(m)=\sum_{d\mid m}\frac1d.
\]
The Dirichlet generating function of these coefficients is
\[
\boxed{\sum_{m\ge1}\frac{\sigma_{-1}(m)}{m^s}
=\zeta(s)\zeta(s+1),\qquad \Re s>1.}
\]
Consequently, in the same half-plane,
\[
\boxed{\sum_{m\ge1}\frac{\sigma_{-1}(m)}{m^s}
=\frac{\eta_D(s)\zeta(s+1)}{1-2^{1-s}}.}
\]
This is an exact bridge from the logarithmic \(q\)-coefficients of Dedekind eta to Dirichlet eta and zeta. It is not an equality between the two eta functions.

Differentiating the product gives a second Lambert-series identity:
\[
q\frac{d}{dq}\log\eta_{\rm Ded}(\tau)
=\frac1{24}-\sum_{m\ge1}\sigma_1(m)q^m
=\frac{E_2(\tau)}{24},
\]
where \(E_2\) is the weight-two quasimodular Eisenstein series. Since
\[
\sum_{m\ge1}\frac{\sigma_1(m)}{m^s}
=\zeta(s)\zeta(s-1),\qquad \Re s>2,
\]
the coefficient Dirichlet series is also
\[
\frac{\eta_D(s)\zeta(s-1)}{1-2^{1-s}}.
\]

## 3. The same quadratic field: Dirichlet \(L\) and Dedekind zeta

For \(K=\mathbb Q(\sqrt{-31})\), the fundamental discriminant is \(D=-31\), and
\[
\chi_{-31}(n)=\left(\frac{-31}{n}\right)
\]
is the primitive quadratic Kronecker character. The quadratic factorization is
\[
\boxed{\zeta_K(s)=\zeta(s)L(s,\chi_{-31}),\qquad \Re s>1.}
\]
Multiplying by \(1-2^{1-s}\) gives the exact relation
\[
\boxed{\eta_D(s)L(s,\chi_{-31})
=(1-2^{1-s})\zeta_K(s).}
\]
The right side is regular at \(s=1\): the zero of \(1-2^{1-s}\) cancels the simple pole of \(\zeta_K\).

The three reduced forms of discriminant \(-31\) give \(h_K=3\). Since \(K\) is imaginary quadratic with \(w_K=2\), the analytic class-number formula yields
\[
L(1,\chi_{-31})=\frac{\pi h_K}{\sqrt{31}}
=\frac{3\pi}{\sqrt{31}}.
\] For the odd primitive character of conductor \(31\), the finite character-sum formula gives the independent exact check
\[
\sum_{a=1}^{30}a\,\chi_{-31}(a)=-93,\qquad
L(1,\chi_{-31})=-\frac{\pi}{31^{3/2}}
\sum_{a=1}^{30}a\,\chi_{-31}(a)
=\frac{3\pi}{\sqrt{31}}.
\]
Thus
\[
\boxed{\eta_D(1)L(1,\chi_{-31})
=\frac{3\pi\log2}{\sqrt{31}}.}
\]
This is the arithmetic companion to S.9: the same field whose Weber class invariant generates the supergolden reciprocal also has its Dedekind zeta factored by the quadratic Dirichlet \(L\)-function.

For completeness, the finite Hurwitz-zeta expression is
\[
L(s,\chi_{-31})
=31^{-s}\sum_{a=1}^{30}\chi_{-31}(a)\,
\zeta\!\left(s,\frac a{31}\right).
\]

## 4. Bernoulli values and the Dirichlet eta constants

For \(n\ge1\),
\[
\zeta(2n)=(-1)^{n+1}
\frac{B_{2n}(2\pi)^{2n}}{2(2n)!}.
\]
Therefore
\[
\boxed{\eta_D(2n)
=(1-2^{1-2n})(-1)^{n+1}
\frac{B_{2n}(2\pi)^{2n}}{2(2n)!}.}
\]
The Bernoulli coefficients in the large-argument polygamma expansions are consequently tied to special values of the Dirichlet eta function. In particular,
\[
\psi(z)\sim\log z-\frac1{2z}
-\sum_{k\ge1}\frac{B_{2k}}{2k\,z^{2k}},
\]
\[
\psi_1(z)\sim\frac1z+\frac1{2z^2}
+\sum_{k\ge1}\frac{B_{2k}}{z^{2k+1}}.
\]
These are asymptotic expansions; they are not exact finite series.

## 5. The Euler Beta/Dirichlet simplex and barycentric cumulants

Do not confuse \(\eta_D\) with the Dirichlet probability distribution. For \(a_i>0\), \(S=a_0+a_1+a_2\), and barycentric coordinates on the reference 2-simplex,
\[
B_3(a)=\int_{\lambda_i\ge0,\,\sum\lambda_i=1}
\prod_{i=0}^2\lambda_i^{a_i-1}\,d\lambda_1d\lambda_2
=\frac{\prod_i\Gamma(a_i)}{\Gamma(S)}.
\]
For a physical triangle of area \(A_F\),
\[
Z_F(a)=2A_F B_3(a).
\]
Writing \(m=a/S\), the barycentric mean and covariance are
\[
\mathbb E[\lambda]=m,\qquad
C=\frac{\operatorname{diag}(m)-mm^T}{S+1}.
\]
If \(V\) has the physical vertices as rows, then
\[
c_{F,a}=V^Tm,\qquad \Sigma_{F,a}=V^TCV.
\]

The parameter derivatives of the same log-partition function are
\[
\partial_{a_i}\log B_3(a)=\psi(a_i)-\psi(S)
=\mathbb E[\log\lambda_i],
\]
\[
\partial_{a_i}\partial_{a_j}\log B_3(a)
=\delta_{ij}\psi_1(a_i)-\psi_1(S)
=\operatorname{Cov}(\log\lambda_i,\log\lambda_j).
\]
The \(\lambda\)-covariance \(C\) and the log-coordinate covariance (the Hessian above) are different tensors. S.3 records the latter; T070 records the former and the physical barycentre.

The chain
\[
\eta_D(2n)\longleftrightarrow \zeta(2n)
\longleftrightarrow B_{2n}
\longleftrightarrow \psi,\psi_1
\longleftrightarrow \nabla_a^2\log B_3(a)
\]
is exact at the level of special values and asymptotic coefficients. It does not say that a finite Dirichlet triangle integral equals a Dirichlet eta value.

## 6. Interface to Morandotti and the RGS fourth moments

For a cell density \(g\in C^3\) on a planar triangle,
\[
\int_F g(x)\prod_i\lambda_i^{a_i-1}\,dA
=Z_F(a)\left[g(c_{F,a})
+\frac12D^2g(c_{F,a}):\Sigma_{F,a}+R_{F,a}\right],
\]
with
\[
|R_{F,a}|\le \frac{h_F^3}{6}\sup_F\|D^3g\|_{\rm op}.
\]
For
\[
g(X)=W(X,\nabla_Su,G,\theta,\nabla_S\theta),
\]
this gives a local cell-integration tool when the composition has the stated regularity. It is not a surface homogenisation theorem: a curved-surface version still needs compactness, a liminf inequality, a recovery sequence, and a precise treatment of seams versus jump sets.

Keep the fourth-moment records separate:
- S.4 is the fully symmetric fourth moment of the fixed 64-site RGS seed;
- S.5 is the fourth jump moment of a refinement stencil;
- S.6–S.8 are local constitutive/variational developments using the S.4 tensor.

None of these rank-four objects is identified with the modular eta function, the Dirichlet eta function, torsion, or the Morandotti disarrangement tensor without an explicit map.

## References

1. NIST DLMF, §27.14 (Dedekind eta product and transformations): https://dlmf.nist.gov/27.14.
2. NIST DLMF, §20.10 (Mellin transforms of theta kernels and the factor \(1-2^{1-s}\)): https://dlmf.nist.gov/20.10.
3. NIST DLMF, §25.15 (Dirichlet \(L\)-functions and Hurwitz-zeta representation): https://dlmf.nist.gov/25.15.
4. A. V. Sutherland, MIT 18.785, Lecture 19, *The Analytic Class Number Formula* (2021): https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec19.pdf.
5. N. Yui and D. Zagier, “On the Singular Values of Weber Modular Functions,” *Mathematics of Computation* 66 (1997), 1645–1662, DOI: 10.1090/S0025-5718-97-00854-5.
