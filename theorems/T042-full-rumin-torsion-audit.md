# T042 — Complete alternating Rumin torsion on S^3/2I

## 1. Scope

T040–T041 isolated the exceptional degree-one boundary sectors. They are not the full torsion: the scalar degree-zero boundary at p=0 contributes with coefficient -2 and cancels the common interior spectral weights. T042 performs this cancellation before regularization. It computes the combined function kappa=-2 zeta_0+zeta_1, not separate continuations of zeta_0 and zeta_1.

The calculation uses the trivial coefficient system on the standard CR quotient S^3/2I, with |2I|=120.

## 2. Exact invariant multiplicity and spectral labels

The trivial 2I-multiplicity in Sym^m(C^2) is
\[
a_m=[t^m]\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]
For contact dimension three (n=1), put q=m-p. Kitaoka's eigenvalue formula becomes
\[
\Lambda_m(p)=\frac{(p(q+1)+q(p+1))^2}{4}
=\frac{(m+2p(m-p))^2}{4}.
\]

The scalar sector has p=0,...,m, with the constant zero mode separated according to Kitaoka's convention 0^s=1:
\[
\zeta_0(s)=1+\sum_{m\ge1}a_m\sum_{p=0}^{m}\Lambda_m(p)^{-s}.
\]
The middle Rumin degree is the sum of the conjugate bidegrees (1,0) and (0,1), each with p=1,...,m+1:
\[
\zeta_1(s)=2\sum_{m\ge0}a_m\sum_{p=1}^{m+1}\Lambda_m(p)^{-s}.
\]
These positive Dirichlet series converge absolutely for Re(s)>1.

## 3. Exact cancellation of all interior weights

For every m>=1, the terms p=1,...,m in zeta_1 agree exactly with the interior terms in zeta_0, including the factor two in -2 zeta_0+zeta_1. They cancel. The m=0 constant mode contributes -2, while the two degree-one boundary modes contribute +2, so they cancel as well.

Only the two ends remain:
\[
\boxed{
\kappa(s)=2\sum_{m\ge1}a_m
\left[\left(\frac{(m+2)^2}{4}\right)^{-s}
-\left(\frac{m^2}{4}\right)^{-s}\right].
}
\]
This is an identity in the common half-plane Re(s)>1. The positive exceptional boundary contribution isolated in T041 is paired with the scalar boundary contribution; it is not the complete torsion by itself.

## 4. Period-60 difference sequence

Let d_n=a_{n-2}-a_n, n>=3. Then
\[
\kappa(s)=2\,4^s\sum_{n\ge3}d_n n^{-2s}.
\]
The generating function is
\[
D(t)=\sum_{n\ge3}d_nt^n
=(t^2-1)\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}+1-t^2.
\]
Exact polynomial simplification gives
\[
(1-t^{60})D(t)=P(t),
\]
where
\[
\begin{aligned}
P(t)={}&-t^{12}+t^{14}-t^{20}+t^{22}-t^{24}+t^{26}-t^{30}
+t^{34}\\
&-t^{36}+t^{38}-t^{40}+t^{46}-t^{48}+t^{58}-2t^{60}+t^{62}.
\end{aligned}
\]
Hence d_(n+60)=d_n for n>=3. The nonzero representatives in the first admissible period are
\[
\begin{array}{c|rrrrrrrr}
n&12&14&20&22&24&26&30&34\\
d_n&-1&1&-1&1&-1&1&-1&1\\
n&36&38&40&46&48&58&60&62\\
d_n&-1&1&-1&1&-1&1&-2&1.
\end{array}
\]
The two finite identities needed at s=0 are
\[
\sum_n d_n=-1,\qquad
\sum_n d_n\left(\frac12-\frac n{60}\right)=0.
\]

## 5. Hurwitz continuation and exact derivative

Grouping the periodic series by residue classes yields
\[
\boxed{
\kappa(s)=2\,4^s60^{-2s}
\sum_n d_n\,\zeta_H\left(2s,\frac n{60}\right).
}
\]
The right-hand side is a finite sum of Hurwitz zeta functions, so it supplies a meromorphic continuation of the combined torsion function, regular at zero. No separate continuation of zeta_0 or zeta_1 is claimed.

Using
\[
\zeta_H(0,x)=\frac12-x,\qquad
\zeta_H'(0,x)=\log\Gamma(x)-\frac12\log(2\pi),
\]
the prefactor derivative cancels and
\[
\kappa'(0)=4\sum_n d_n
\left[\log\Gamma\left(\frac n{60}\right)-\frac12\log(2\pi)\right].
\]
With Kitaoka's normalization 2 log T_E=kappa'(0),
\[
\boxed{
T_E=2\pi\prod_n\Gamma\left(\frac n{60}\right)^{2d_n}.
}
\]
Numerically,
\[
\log T_E=0.2745567511565355917080822540155806471969978481\ldots
\]
and
\[
T_E=1.3159472534785811491779321333168201513751599209\ldots.
\]

## 6. Comparison with quotient volume

The finite Gamma product reduces using Gamma(1+x)=x Gamma(x) and the reflection identity Gamma(x)Gamma(1-x)=pi/sin(pi x). The remaining sine quotient is
\[
\frac{\sin(\pi/5)\sin(\pi/3)\sin(2\pi/5)}
{\sin(\pi/30)\sin(7\pi/30)\sin(11\pi/30)\sin(13\pi/30)}
=\sqrt{60}.
\]
Consequently,
\[
\boxed{T_E=\frac{2\pi^2}{15}.}
\]
In Kitaoka's spherical normalization g_(theta,J)=4g_std, so Vol(S^3,g_(theta,J))=16 pi^2. Division by |2I|=120 gives
\[
\operatorname{Vol}(S^3/2I,g_(theta,J))=\frac{16\pi^2}{120}
=\frac{2\pi^2}{15}.
\]
The volume agreement is a consistency check with the CR-Seifert/Rumin-Seshadri comparison and the non-acyclic determinant-line convention.

## 7. Reproducibility

- src/t042_full_rumin_torsion_audit.py: Molien coefficients, finite spectral zeta sums, cancellation, period-60 generating function, Hurwitz representation and Gamma product.
- tests/test_t042_full_rumin_torsion_audit.py: symbolic generating-function identity, period checks through n=600, finite spectral cancellation, exact coefficient moments and high-precision Gamma/volume comparison.
- data/t042_full_rumin_torsion_audit.json: machine-readable audit.

Commands:
\`\`\`bash
python -m pytest tests/test_t042_full_rumin_torsion_audit.py -q
python -m src.t042_full_rumin_torsion_audit --max-degree 180 --dps 50
\`\`\`

## 8. Status ledger

| Claim | Status |
|---|---|
| a_m from the trivial 2I-Molien series | Exact |
| Kitaoka eigenvalue specialization for n=1 | Exact source-derived formula |
| Cancellation of all interior p-weights | Exact algebraic cancellation |
| Period-60 identity for d_n | Exact generating-function identity |
| Finite Hurwitz continuation of kappa(s) | Exact |
| Gamma product for T_E | Exact consequence of Hurwitz derivative |
| Equality to 2 pi^2/15 | Exact reflection/recurrence reduction; high-precision numerical regression |
| Separate zeta'_0(0), zeta'_1(0) | Not computed |
| Nontrivial flat bundles / twisted sectors | Open |

## References

1. A. Kitaoka, Analytic Torsions Associated with the Rumin Complex on Contact Spheres, arXiv:1911.03092, Theorem 0.1, Theorem 0.2, §§1–3.
2. A. Kitaoka, Ray–Singer Torsion and the Rumin Laplacian on Lens Spaces, SIGMA 18 (2022), 091, used for source conventions and comparison, not as a cyclic quotient formula for 2I.
3. KITAOKA_RUMIN_FORMULA_AUDIT.md, §§10.0–10.4, independently audited here.
4. T032 Molien coefficients and T039 boundary identification; T040–T041 record the isolated boundary term and its Barnes representation.

## Classification

T042 closes the combined trivial-coefficient Rumin torsion calculation on S^3/2I at the level of the explicit Hurwitz/Gamma formula. It does not compute the individual degree zeta derivatives or twisted torsions.
