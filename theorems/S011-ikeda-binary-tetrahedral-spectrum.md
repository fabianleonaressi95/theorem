# S011 — Spectrum of the binary tetrahedral spherical space form

**Classification:** SOURCE-VERIFIED FORMULA (Ikeda, Theorem 4.4(1)); independent Molien reconstruction and index/eigenvalue bookkeeping are recorded separately.  
**Primary source:** Akira Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Mathematical Journal* 18 (1995), 57–67, especially Proposition 3.1(2), the Poincaré-series calculation on p. 63, and Theorem 4.4(1)–(2).  
**Repository PDF:** `18_57.pdf`  
**Publisher copy:** https://www.jstage.jst.go.jp/article/kodaimath1978/18/1/18_1_57/_pdf/-char/en

## 1. Index convention and eigenvalues

For the unit three-sphere, scalar spherical harmonics of degree \(\ell\geq0\) have Laplace eigenvalue
\[
\lambda_\ell=\ell(\ell+2).
\]
In the binary-tetrahedral quotient formula, Ikeda's index is \(\ell=2k\). Thus
\[
\boxed{\lambda_k=2k(2k+2)=4k(k+1),\qquad k=0,1,2,\ldots.}
\]
This follows from the standard unit-sphere eigenvalue \(\lambda_\ell=\ell(\ell+2)\) after setting \(\ell=2k\). It must **not** be described as a specialization of Ikeda's Theorem 4.4(2): that part is explicitly stated only for \(n>1\). The 3-dimensional quotient is covered by Theorem 4.4(1), while the eigenvalue conversion is an independent reconstruction.

## 2. Poincaré-series average: inclusion–exclusion

Ikeda's Proposition 3.1(2) describes \(T^*\) as the union of four cyclic subgroups of order 6 and three cyclic subgroups of order 4, with every pairwise intersection equal to the common center \(C_2\). The noncentral elements of these seven cyclic subgroups are disjoint. The order count is therefore
\[
4(6-2)+3(4-2)+2=16+6+2=24=|T^*|.
\]
If \(F_q\) denotes the normalized cyclic-subgroup contribution used by Ikeda, the four order-6 subgroups contribute \(4\cdot6F_6=24F_6\), and the three order-4 subgroups contribute \(3\cdot4F_4=12F_4\). The common center has been counted seven times and must occur once, so six excess copies of its order-2 contribution are subtracted: \(6\cdot2F_2=12F_2\). Dividing by 24 gives
\[
\boxed{F_{T^*}=\frac{24F_6+12F_4-12F_2}{24}
=F_6+\frac12F_4-\frac12F_2.}
\]
The printed p. 63 coefficient combination agrees with this reconstruction. The simplified expression is \\(F_6+\\frac12F_4-\\frac12F_2\\). The interpretation of the symbols as cyclic-subgroup series is stated as a reconstruction, not as a verbatim definition supplied by the quoted coefficient line.

## 3. Independent Molien check

For the binary tetrahedral group in its defining two-dimensional representation in \(SU(2)\), the conjugacy-class contributions give
\[
M(t)=\frac1{24}\left[
\frac1{(1-t)^2}+\frac1{(1+t)^2}
+\frac6{1+t^2}
+\frac8{1-t+t^2}+\frac8{1+t+t^2}
\right].
\]
Simplifying,
\[
\boxed{M(t)=
\frac{1-t^{24}}{(1-t^6)(1-t^8)(1-t^{12})}
=\frac{1+t^{12}}{(1-t^6)(1-t^8)}.}
\]
The first expression is the Molien average over the identity, central element, six elements with eigenvalues \(\pm i\), and the two classes of eight elements with eigenvalues \(e^{\pm i\pi/3}\) and \(e^{\pm2i\pi/3}\), respectively. The second expression is the Hilbert-series form for the binary-tetrahedral invariant ring.

The central element \(-I\) forces odd-degree invariant polynomials to vanish. Writing \(m_{2k}=[t^{2k}]M(t)\), coefficient extraction yields
\[
m_{2k}=1+2\left\lfloor\frac{k}{3}\right\rfloor
+\left\lfloor\frac{k}{2}\right\rfloor-k.
\]
Equivalently,
\[
m_{2k}=\#\{(a,b)\in\mathbb Z_{\ge0}^2:3a+4b=k\}
+\#\{(a,b)\in\mathbb Z_{\ge0}^2:3a+4b=k-6\}.
\]
The degree-\(2k\) spherical harmonic representation on \(S^3\) is
\(\operatorname{Sym}^{2k}(\mathbb C^2)\otimes
\operatorname{Sym}^{2k}(\mathbb C^2)^*\). Taking invariants under the left \(T^*\)-action therefore multiplies the invariant dimension \(m_{2k}\) by the dimension \(2k+1\) of the other factor. Hence
\[
\boxed{a_k=(2k+1)\left(
1+2\left\lfloor\frac{k}{3}\right\rfloor
+\left\lfloor\frac{k}{2}\right\rfloor-k
\right).}
\]
This is Ikeda's Theorem 4.4(1). The theorem lists \(k\ne1,2,5\); these are precisely the zero-multiplicity indices, so the formula may be used for all \(k\ge0\) if zero multiplicities are retained.

## 4. Initial values

| \(k\) | Eigenvalue \(4k(k+1)\) | \(m_{2k}\) | Multiplicity \(a_k=(2k+1)m_{2k}\) |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 |
| 1 | 8 | 0 | 0 |
| 2 | 24 | 0 | 0 |
| 3 | 48 | 1 | 7 |
| 4 | 80 | 1 | 9 |
| 5 | 120 | 0 | 0 |
| 6 | 168 | 2 | 26 |
| 7 | 224 | 1 | 15 |
| 8 | 288 | 1 | 17 |

In particular, \(m_6=1\), \(a_3=7\), and \(m_{12}=2\), \(a_6=26\).

## 5. Scope and exclusions

- **Directly reported by the source:** Proposition 3.1(2) subgroup decomposition; p. 63 Poincaré-series coefficient combination; Theorem 4.4(1) multiplicity formula and its excluded indices. The PDF is the repository file `18_57.pdf`.
- **Independent reconstruction:** the order count from the subgroup decomposition; the simplified Poincaré average and cyclic-series interpretation; the eigenvalue \\(4k(k+1)\\) from \\(\\ell=2k\\) and the unit-sphere spectrum; the Molien series and its coefficient check.
- **Not established by this paper:** any connection to Weber functions, Dedekind's modular eta, Dirichlet eta, \(\mathbb Q(\sqrt{-31})\), Gamma/Beta integrals, or barycentric covariance. Those are separate research strands and must not be attributed to Ikeda.
- **No broader geometric or physical interpretation is inferred** from this spectral calculation alone.
