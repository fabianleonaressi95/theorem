# Unified construction: Dedekind eta, Dirichlet eta, Weber–supergolden arithmetic, barycentres and RGS–Morandotti geometry

**Date:** 10 November 2026  
**Scope:** audit and synthesis of the 10 November work recorded in THEOREM and the companion RGS–QLG repository, with the earlier Dedekind-eta/Weber material recovered from the supplied Nardelli note. This is a structured mathematical programme, not a claim that every strand has already been reduced to one theorem.

## 1. The four meanings that must remain distinct

This construction uses four different objects:

1. **Dedekind modular eta**
   \[
   \eta_{\rm Ded}(\tau)=q^{1/24}\prod_{n\ge1}(1-q^n),\qquad q=e^{2\pi i\tau},\quad \Im\tau>0.
   \]
2. **Dirichlet eta**
   \[
   \eta_D(s)=\sum_{n\ge1}(-1)^{n-1}n^{-s}
   =(1-2^{1-s})\zeta(s).
   \]
3. **Dirichlet \(L\)-function** \(L(s,\chi)\), including the quadratic character \(\chi_{-31}\).
4. **Dirichlet distribution on a simplex**, whose normalizer is the multivariate Beta function \(B_3(a)\).

There is also a fifth, related object: the **Dedekind zeta function** \(\zeta_K(s)\) of a number field. It is not the Dedekind eta function.

The construction is unitary because these objects are connected by exact transformations and moment-generating identities, not because they are the same function.

## 2. The central arithmetic–modular bridge: \(-31\) and the supergolden number

Let
\[
K=\mathbb Q(\sqrt{-31}),\qquad D_K=-31.
\]
Its reduced positive primitive forms are
\[
[1,1,8],\quad [2,1,4],\quad [2,-1,4],
\]
so \(h_K=3\). The principal CM point is
\[
\tau_0=\frac{-1+i\sqrt{31}}2.
\]

The Weber function is built from Dedekind eta:
\[
f(\tau)=e^{-\pi i/24}
\frac{\eta_{\rm Ded}((\tau+1)/2)}{\eta_{\rm Ded}(\tau)},\qquad
f_2(\tau)=\sqrt2\,\frac{\eta_{\rm Ded}(2\tau)}{\eta_{\rm Ded}(\tau)}.
\]
With \(\zeta_{48}=e^{2\pi i/48}\), the principal Weber class invariant for \(D=-31\) is
\[
\rho=\zeta_{48}f_2(\tau_0).
\]
Yui–Zagier's Weber class equation for this discriminant is
\[
\rho^3+\rho-1=0.
\]
The positive supergolden number \(\psi\), defined by
\[
\psi^3-\psi^2-1=0,
\]
therefore satisfies
\[
\boxed{\rho=\psi^{-1}.}
\]

The Weber transformations further give
\[
f_2(\tau)=\zeta_{48}\frac{\sqrt2}{f(2\tau-1)},\qquad
f(\tau-2)=\zeta_{48}^2f(\tau).
\]
At \(\tau_0=(-1+i\sqrt{31})/2\), this yields
\[
\boxed{f(i\sqrt{31})=\sqrt2\,\psi,\qquad
f(i\sqrt{31})^2=2\psi^2.}
\]
Thus the supplied note's \(W=f(i\sqrt{31})^2\) obeys the exact cubic
\[
\boxed{W^3-2W^2-8W-8=0.}
\]
The derivation is in [S.9](../theorems/S009-weber-dedekind-eta-supergolden-class-invariant.md).

**CM-point correction.** \((-1+i\sqrt{31})/2\) has order discriminant \(-31\), while \(i\sqrt{31}\) has order discriminant \(-124\). They are not the same point. The Weber transformation is the explicit bridge. Also, \(j((1+i\sqrt{31})/2)\) is a singular modulus in the same class field, not the Grablovitz root and not a root of \(X^3+X^2+1\).

The negative Grablovitz root is simply
\[
x_0=-\psi,\qquad x_0^3+x_0^2+1=0.
\]
The Weber invariant \(\rho=1/\psi\) generates the Hilbert class field over \(K\) under the cited class-invariant theorem. The statement that \(\psi\) is a unit follows from its monic polynomial and norm \(1\); calling it the *fundamental* unit requires a separate regulator/minimality proof and is not assumed here.

## 3. Dirichlet eta and the arithmetic of the same field

For the quadratic character
\[
\chi_{-31}(n)=\left(\frac{-31}{n}\right),
\]
the Dedekind zeta factorization is
\[
\zeta_K(s)=\zeta(s)L(s,\chi_{-31}),\qquad \Re s>1.
\]
Multiplication by the Dirichlet-eta factor gives
\[
\boxed{\eta_D(s)L(s,\chi_{-31})
=(1-2^{1-s})\zeta_K(s).}
\]
The right side is regular at \(s=1\), because the zero of \(1-2^{1-s}\) cancels the simple pole of \(\zeta_K\).

Since \(h_K=3\), \(w_K=2\), and \(D_K=-31\), the imaginary-quadratic class-number formula gives
\[
L(1,\chi_{-31})=\frac{3\pi}{\sqrt{31}}.
\]
Using \(\eta_D(1)=\log2\),
\[
\boxed{\eta_D(1)L(1,\chi_{-31})
=\frac{3\pi\log2}{\sqrt{31}}.}
\]
This is the arithmetic companion to the Weber identity: both eta constructions meet the same quadratic field \(K\), but through different functions.

## 4. Dedekind's \(q\)-product produces Dirichlet series

The logarithm of the modular product is the Lambert series
\[
\log\eta_{\rm Ded}(\tau)
=\frac{\pi i\tau}{12}
-\sum_{n\ge1}\sigma_{-1}(n)q^n,
\qquad
\sigma_{-1}(n)=\sum_{d\mid n}d^{-1}.
\]
The coefficients have Dirichlet generating function
\[
\sum_{n\ge1}\frac{\sigma_{-1}(n)}{n^s}
=\zeta(s)\zeta(s+1)
=\frac{\eta_D(s)\zeta(s+1)}{1-2^{1-s}},
\quad \Re s>1.
\]
Likewise,
\[
q\frac{d}{dq}\log\eta_{\rm Ded}(\tau)
=\frac{E_2(\tau)}{24}
=\frac1{24}-\sum_{n\ge1}\sigma_1(n)q^n,
\]
and
\[
\sum_{n\ge1}\frac{\sigma_1(n)}{n^s}
=\zeta(s)\zeta(s-1)
=\frac{\eta_D(s)\zeta(s-1)}{1-2^{1-s}},
\quad \Re s>2.
\]
These identities provide a second, coefficient-wise bridge between Dedekind eta and Dirichlet eta. The Euler pentagonal expansion
\[
\prod_{n\ge1}(1-q^n)
=\sum_{k\in\mathbb Z}(-1)^kq^{k(3k-1)/2}
\]
is the companion sparse expansion.

## 5. Gamma–Beta–zeta–Bernoulli and Dirichlet cumulants

The Mellin transform
\[
\Gamma(s)\eta_D(s)
=\int_0^\infty\frac{x^{s-1}}{e^x+1}\,dx,\qquad \Re s>0,
\]
puts the Dirichlet eta function directly beside Gamma.

At even integers,
\[
\eta_D(2n)
=(1-2^{1-2n})(-1)^{n+1}
\frac{B_{2n}(2\pi)^{2n}}{2(2n)!}.
\]
The same Bernoulli coefficients occur in the asymptotic expansions of the digamma and trigamma. In particular, the exact Dirichlet cumulant lemma S.3 is
\[
\partial_{a_i}\log B_3(a)=\psi(a_i)-\psi(S),
\]
\[
\partial_{a_i}\partial_{a_j}\log B_3(a)
=\delta_{ij}\psi_1(a_i)-\psi_1(S)
=\operatorname{Cov}(\log\lambda_i,\log\lambda_j).
\]
Thus the eta/zeta/Bernoulli chain supplies the asymptotic coefficient system for the parameter-cumulant geometry. This is an exact special-function bridge, not a claim that the finite triangle partition function equals \(\eta_D(s)\).

## 6. Dirichlet barycentres and local geometric moments

For a triangle \(F\) with area \(A_F\), vertices stored as rows of \(V\), positive parameters \(a_i\), and \(S=\sum_i a_i\),
\[
Z_F(a)=2A_F\frac{\prod_i\Gamma(a_i)}{\Gamma(S)}.
\]
Writing \(m=a/S\),
\[
c_{F,a}=V^Tm,\qquad
C=\frac{\operatorname{diag}(m)-mm^T}{S+1},\qquad
\Sigma_{F,a}=V^TCV.
\]
The uniform case \(a=(1,1,1)\) reduces to T068. T070 extends it to weighted barycentres and phase moments. The Duffy–Gauss–Jacobi implementation now distinguishes the raw second moment from the covariance and includes A1–A3 regression tests; those tests are deposited but not claimed passed until executed.

For \(g\in C^3\),
\[
\int_Fg(x)\prod_i\lambda_i^{a_i-1}\,dA
=Z_F(a)\left[g(c_{F,a})
+\frac12D^2g(c_{F,a}):\Sigma_{F,a}
+R_{F,a}\right],
\]
with
\[
|R_{F,a}|\le\frac{h_F^3}{6}\sup_F\|D^3g\|_{\rm op}.
\]
This is the precise handoff to a smooth local energy density.

## 7. Discrete RGS/Q6 layer: what is connected and what is not

The Q6 2-skeleton has 64 vertices, 192 edges and 240 square faces. The exact chain identities, ranks and Anti-Twin action are recorded in T071; the exact Möbius phase action, pure-gauge connection and Walsh spectrum are recorded in T072. Its graph Laplacian has eigenvalues \(2k\) with multiplicities \(\binom6k\), \(k=0,\ldots,6\). Its finite spectral zeta is
\[
Z_{Q6}(s)=\sum_{k=1}^6\binom6k(2k)^{-s},
\]
with heat trace
\[
K_{Q6}(t)=(1+e^{-2t})^6.
\]
This has the same *Mellin-transform architecture* as the integral representation of \(\eta_D\), but it is a finite graph spectral function, not the Dirichlet eta function.

The RGS fourth-moment records remain separate:
- S.4: fixed 64-site seed fourth tensor and its cubic anisotropic decomposition;
- S.5: fourth jump moment of a refinement stencil and conditional \(O(a^2)\) consistency;
- S.6: local SO(3) connection current;
- S.7: antisymmetric Maxwell contraction obstruction and candidate STF response;
- S.8: conditional algebraic coframe variation.

The fully symmetric S.4 tensor is not torsion; the S.5 stencil moment is not the S.4 seed moment. No eta function has been identified with either tensor.

## 8. Morandotti interface: local quadrature, not yet surface homogenisation

For the surface density
\[
g(X)=W(X,\nabla_Su,G,\theta,\nabla_S\theta),
\]
T068/T070 provide local cell integration formulae when the composed density has the required \(C^3\) regularity. They do not prove compactness, a liminf inequality or a recovery sequence on a curved shell.

Keep
\[
(g,G)\in SBV\times L^1,\qquad M=\nabla g-G
\]
distinct from the metric \(J^TJ\). A physical seam is not automatically a jump set; a quadratic seam law is not automatically covered by a 1-homogeneous interfacial density. The football shell has exact combinatorial counts and a linearized orthotropic model, but material constants remain uncalibrated without scan/coupon data.

## 9. Audit of the work committed on 10 November 2026

The repository history records **80 commits in THEOREM** and **10 commits in the companion RGS–QLG repository** on this date. The audited work falls into the following blocks:

| Work block | Deposited result | Evidence boundary |
|---|---|---|
| Defect elasticity / Airy / Torino | Initial 2D benchmark, cochain/Airy comparisons, C0-IPDG reproduction plan | Reproducible numerical work; not a curved-surface homogenisation theorem |
| Football geometry | Orthotropic CST shell, panel anisotropy, triplet transfer and seam model | Exact panel combinatorics; demonstration material parameters; no scan validation |
| FEEC | Relative boundary complex, injectivity and codifferential convergence audit | Hypotheses and finite-mesh checks remain distinct from Mosco convergence |
| Digamma / supergolden | Shift and multiplication identities, asymptotic count filter | Exact analytic identities; Q6/PSU derivation of \(\psi\) remains open |
| Kathara–Q6 Gate D | Integral non-degenerate face lift \(R_0,R_1,R_2\), rank \(R_2=10\) | Exact chain map for the declared vertex chart and fixed axis order \((1,2,0,3,4,5)\); not RGS-canonical |
| Triangle barycentres | T068 / Gate E.1, T070, S.3 and Duffy–Jacobi implementation | Local Euclidean identities; regression tests deposited, full execution not claimed |
| Fourth moments | S.4–S.8, hash-checked seed reconstruction, \(O_h\) action, connection/Maxwell/coframe branches | Seed values are numerical; S.6–S.8 are conditional local variational records |
| Q6 topology and phase | T071 cubical chain complex/Anti-Twin/synchronization, T072 Möbius phase/flat connection | Exact finite identities; synchronization physics and nontrivial transport remain open |
| Bibliography and synthesis | Special-functions/Morandotti sources, numerical replay, central theorem index | Provenance and epistemic status separated |

The T068 collision was corrected: T068 is the barycentric theorem, T069 the antipodal/Walsh record, T070 the weighted Dirichlet theorem, T071 the cubical synchronization audit, and T072 the Möbius/flat-connection record. The README now has a unique index for these IDs and S.1–S.8.

## 10. What is now genuinely unified

The exact bridges form a connected chain:
\[
\boxed{
\eta_{\rm Ded}
\longrightarrow \text{Weber class invariant}
\longrightarrow \rho=\psi^{-1}
\longrightarrow K=\mathbb Q(\sqrt{-31})
\longrightarrow L(s,\chi_{-31}),\ \zeta_K(s)
}
\]
and, independently but compatibly,
\[
\boxed{
\eta_{\rm Ded}\ q\text{-coefficients}
\longrightarrow \zeta(s)\zeta(s+1),\ \zeta(s)\zeta(s-1)
\longrightarrow \eta_D(s)
\longrightarrow \Gamma,\ B_{2n},\ \psi,\psi_1
\longrightarrow \nabla_a^2\log B_3(a)
\longrightarrow (c_{F,a},\Sigma_{F,a}).
}
\]
The local moment expansion then connects \((c_{F,a},\Sigma_{F,a})\) to the Morandotti bulk density on a cell. The RGS fourth-moment tensors and Q6 chain/spectral structures provide discrete geometric inputs and comparison operators. Their coupling to a global curved-shell limit is the next proof programme, not a completed theorem.

## 11. Open obligations

1. Independently derive or machine-check the \(D=-31\) Weber class polynomial and its normalization, rather than relying only on the published table.
2. Run the new Duffy–Jacobi A1–A3 tests and record actual output.
3. Run the full relevant theorem/FEEC/football test suites and attach the exact CI run identifiers.
4. Verify the real 180-facet football mesh against scan and material/coupon data.
5. Prove the curved-surface compactness, liminf and recovery sequence for the Morandotti structured-deformation functional.
6. Establish an explicit, non-circular map from Q6/PSU refinement data to the supergolden/Weber invariant if such a map exists.
7. Keep the Dirichlet parameter gradient \(\partial_{a_i}\), the spatial gradient \(\nabla_S\), the fourth jump moment, the seed fourth moment, and the modular derivative \(q\,d/dq\) as distinct operators.

## 12. Primary references

- N. Yui and D. Zagier, “On the Singular Values of Weber Modular Functions,” *Math. Comp.* 66 (1997), 1645–1662, DOI 10.1090/S0025-5718-97-00854-5.
- NIST DLMF §§20.10, 23.15, 23.18, 25.15, 27.14.
- A. V. Sutherland, MIT 18.785, Lecture 19, *The Analytic Class Number Formula* (2021).
- Amar–Matias–Morandotti–Zappale (2022), periodic homogenization in structured deformations; retain the Euclidean-domain and density hypotheses of the source paper.
- Barroso–Matias–Morandotti–Owen (2017), relaxed disarrangement densities; retain the distinction \(M=\nabla g-G\).
