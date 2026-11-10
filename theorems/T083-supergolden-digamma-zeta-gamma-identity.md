# T083 — Supergolden constant, digamma and the zeta expansion

**Date:** 10 November 2026  
**Status:** proved exact special-function identity; numerical value independently checked.  
**Scope:** relation between the supergolden algebraic number and Euler's Gamma/digamma/Riemann zeta. This is an analytic identity, not a new physical law.

## 1. Notation

Let \(s=\psi_{\mathrm{sg}}\) be the unique positive root of
\[
s^3-s^2-1=0,\qquad s=1.4655712318767680266567\ldots
\]
Write \(\Gamma_E\) for Euler's Gamma function and
\[
\psi_{\mathrm{dig}}(z)=\frac{d}{dz}\log\Gamma_E(z).
\]
The symbols \(s\) and \(\psi_{\mathrm{dig}}\) are different objects.

## 2. Algebraic reduction

The defining polynomial gives
\[
s^2(s-1)=1,\qquad r:=s-1=s^{-2},\qquad 0<r<1.
\]
Thus the supergolden number is exactly \(s=1+r\), with the digamma Taylor argument \(r\) lying strictly inside the unit disk of convergence.

## 3. Main theorem: zeta expansion at the supergolden argument

Euler's Taylor expansion, valid absolutely for \(|z|<1\), is
\[
\psi_{\mathrm{dig}}(1+z)
=-\gamma+\sum_{n=1}^{\infty}(-1)^{n+1}\zeta(n+1)z^n.
\]
Substituting \(z=r=s^{-2}\) proves the exact identity
\[
\boxed{
\psi_{\mathrm{dig}}(s)
=-\gamma+\sum_{n=1}^{\infty}
(-1)^{n+1}\frac{\zeta(n+1)}{s^{2n}}
}.
\]
This is the direct bridge: the digamma value at the supergolden constant is an absolutely convergent zeta-value series whose argument is fixed by the supergolden cubic. The series converges geometrically because \(s^{-2}=r<1\).

Equivalently, using \(\eta_D(q)=(1-2^{1-q})\zeta(q)\) for \(q>1\),
\[
\psi_{\mathrm{dig}}(s)
=-\gamma+\sum_{n=1}^{\infty}
(-1)^{n+1}\frac{\eta_D(n+1)}
{(1-2^{-n})s^{2n}}.
\]
Here \(\eta_D\) is the **Dirichlet eta function**, not Dedekind's modular eta function.

## 4. Recurrence and reflection companions

The digamma recurrence gives
\[
\psi_{\mathrm{dig}}(s)
=\psi_{\mathrm{dig}}(s^{-2})+s^2.
\]
The reflection identity gives
\[
\psi_{\mathrm{dig}}(2-s)
-\psi_{\mathrm{dig}}(s-1)
=\pi\cot(\pi s^{-2}).
\]
These are exact consequences of standard digamma identities and \(s-1=s^{-2}\).

## 5. Gamma-function form

Integrating the same Taylor series from 0 to \(r\), or using the classical expansion of \(\log\Gamma_E(1+z)\), gives
\[
\boxed{
\log\Gamma_E(s)
=-\gamma r+
\sum_{n=2}^{\infty}\frac{(-1)^n\zeta(n)}{n s^{2n}}
}.
\]
This supplies a direct relation to Euler's Gamma function itself, not only its logarithmic derivative.

## 6. Dedekind eta / discriminant -31 bridge

A separate, stronger modular identity already recorded in S009 states that for
\[
\tau=\frac{1+i\sqrt{31}}2,
\]
the supergolden constant is represented by a Weber/Dedekind-eta class invariant:
\[
s=\frac{e^{\pi i/24}\eta_{\mathrm{Ded}}(\tau)}
{\sqrt2\,\eta_{\mathrm{Ded}}(2\tau)}.
\]
This is not the Dirichlet eta function. Combined with Sections 3 and 5, it places the same algebraic number in both a modular eta quotient and an absolutely convergent zeta expansion for \(\psi_{\mathrm{dig}}(s)\). It does **not** by itself yield a closed elementary value for the digamma constant.

## 7. Numerical check

High-precision evaluation gives
\[
s=1.4655712318767680266567312252\ldots,
\]
\[
r=s^{-2}=0.4655712318767680266567312252\ldots,
\]
\[
\psi_{\mathrm{dig}}(s)
=0.00380489074098203186438725795\ldots.
\]
The numerical value is a check of the exact series/identities, not their proof.

## 8. Proof status and limits

- **Proved:** algebraic reduction \(s-1=s^{-2}\); zeta Taylor expansion substitution; Gamma logarithm expansion; recurrence and reflection consequences.
- **Established modular identity (cross-reference S009):** Dedekind eta/Weber class-invariant representation at discriminant \(-31\).
- **Not claimed:** an elementary closed form for \(\psi_{\mathrm{dig}}(s)\); an identity equating the supergolden constant with the digamma function; a physical interpretation without an independently specified model.
- **Useful next step:** exploit the Pisot conjugates and the recurrence of the Narayana sequence to seek accelerated algebraic approximants for the zeta series, and compare its modular parametrization with the Weber class invariant.

## References

1. J. C. Lagarias, *Euler's constant: Euler's work and modern developments*, Theorem 3.1.2 (Euler's Taylor expansion of the digamma function).
2. Wolfram MathWorld, “Supergolden Ratio” (minimal polynomial, value, and Dedekind eta special value at discriminant \(-31\)).
3. Repository record S009, *Weber–Dedekind eta class invariant and the supergolden root*.
