# T084 — Supergolden digamma formula via odd zeta values

**Date:** 10 November 2026  
**Status:** exact identity from the NIST DLMF digamma expansion; numerical check performed.  
**Scope:** an accelerated exact representation of the digamma at the supergolden constant.

## 1. Definitions

Let \(s>1\) be the positive root of
\[
s^3-s^2-1=0.
\]
Then
\[
r=s-1=s^{-2},\qquad 0<r<1.
\]
Write \(\psi_{\mathrm{dig}}(z)=\Gamma_E'(z)/\Gamma_E(z)\), and let \(\gamma\) be Euler's constant.

## 2. Exact formula

The NIST DLMF expansion (5.7.5), valid for \(|z|<2\), \(z\ne0,\pm1\), is
\[
\psi_{\mathrm{dig}}(1+z)
=\frac1{2z}-\frac\pi2\cot(\pi z)
+\frac1{z^2-1}+1-\gamma
-\sum_{k=1}^{\infty}(\zeta(2k+1)-1)z^{2k}.
\]
Set \(z=r=s^{-2}\). Since \(1+r=s\), this gives
\[
\boxed{
\begin{aligned}
\psi_{\mathrm{dig}}(s)
={}&\frac{s^2}{2}
-\frac\pi2\cot\!\left(\frac\pi{s^2}\right)
+\frac1{s^{-4}-1}+1-\gamma\\
&-\sum_{k=1}^{\infty}
(\zeta(2k+1)-1)s^{-4k}.
\end{aligned}}
\]
Equivalently, the rational term is \(-s^4/(s^4-1)\).

This is an exact rapidly convergent formula involving the supergolden algebraic number, one elementary cotangent term, Euler's constant and only odd zeta values with the trivial limiting contribution \(1\) subtracted.

## 3. Why the convergence is fast

For \(k\ge1\),
\[
\zeta(2k+1)-1=\sum_{n=2}^{\infty}n^{-(2k+1)}.
\]
Thus the summand is positive before the overall minus sign and decays at least geometrically in \(r^2=s^{-4}\), with additional decay from the subtraction of the zeta limit 1. Since
\[
s^{-4}=0.216756\ldots,
\]
the series is substantially faster than the direct Euler expansion in powers of \(s^{-2}=0.465571\ldots\).

A useful exact double-series rearrangement (all terms nonnegative, so Tonelli applies) is
\[
\sum_{k=1}^{\infty}(\zeta(2k+1)-1)r^{2k}
=\sum_{n=2}^{\infty}\frac{r^2}{n(n^2-r^2)}.
\]
Indeed, interchange the sums and evaluate
\(\sum_{k\ge1}r^{2k}n^{-(2k+1)}
=r^2/[n(n^2-r^2)]\).
Therefore an equivalent compact formula is
\[
\boxed{
\psi_{\mathrm{dig}}(s)
=\frac1{2r}-\frac\pi2\cot(\pi r)
+\frac1{r^2-1}+1-\gamma
-r^2\sum_{n=2}^{\infty}\frac1{n(n^2-r^2)},
\quad r=s^{-2}.
}
\]
This last series is an elementary positive Lambert-type sum and is another exact form.

## 4. Numerical verification

Using the algebraic root and evaluating the series at high precision:
\[
s=1.465571231876768026656731225219939108\ldots,
\]
\[
r=0.465571231876768026656731225219939108\ldots,
\]
\[
\psi_{\mathrm{dig}}(s)
=0.00380489074098203186438725795184465739\ldots.
\]
The value agrees with direct high-precision evaluation of \(\Gamma_E'/\Gamma_E\). This is a numerical check; the proof is the substitution into the DLMF identity and the justified series rearrangement.

## 5. Relation to T083 and modular eta

T083 gives the complementary Euler expansion
\[
\psi_{\mathrm{dig}}(s)
=-\gamma+\sum_{n=1}^{\infty}
(-1)^{n+1}\zeta(n+1)s^{-2n}.
\]
T084 is a faster alternative, not a conflicting formula. S009 separately represents \(s\) through a Weber/Dedekind-eta class invariant at discriminant \(-31\). Combining S009 with T084 gives an exact modular specification of the algebraic argument in the odd-zeta digamma formula; it does not imply that the digamma value itself is an elementary modular unit or has a finite closed form.

## 6. Proof status and limits

- **Proved:** exact identity by DLMF substitution; double-series rearrangement by absolute/nonnegative convergence.
- **Numerically checked:** displayed decimal values.
- **Not claimed:** finite expression using only algebraic numbers, logarithms and elementary constants; such a reduction is not established here.
- **Reference:** NIST Digital Library of Mathematical Functions, §5.7, equation 5.7.5, https://dlmf.nist.gov/5.7.E5.
