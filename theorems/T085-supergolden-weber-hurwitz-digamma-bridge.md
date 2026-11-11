# T085 — Supergolden Weber–Dedekind–Hurwitz–digamma bridge

**Date:** 10 November 2026  
**Status:** exact identity; proof assembled from the Weber class invariant at discriminant \(-31\) and standard digamma/Hurwitz identities.  
**Classification:** proved special-function identity, conditional only on the stated normalization of the principal Weber invariant; no finite elementary evaluation is claimed.  
**Depends on:** S009, T083, T084.

## 1. Notation and algebraic number

Let \(s\) denote the supergolden constant, not the digamma function:
\[
s>0,\qquad s^3-s^2-1=0.
\]
Set
\[
r=s-1=s^{-2},\qquad 0<r<1,
\]
and write
\[
\psi_{\rm dig}(z)=\frac{\Gamma_E'(z)}{\Gamma_E(z)}.
\]
Let \(\eta(\tau)\) be the Dedekind eta function and
\[
\tau_{31}=\frac{1+i\sqrt{31}}2,\qquad
q_{31}:=\frac{e^{\pi i/24}\eta(\tau_{31})}
{\sqrt2\,\eta(2\tau_{31})}.
\]

## 2. Modular identification of the supergolden number

**Lemma 2.1 (Weber–eta identification).** With the principal binary quadratic form
\[
Q_0=[1,1,8],\qquad
\tau_0=\frac{-1+i\sqrt{31}}2,
\]
the principal Weber class invariant is
\[
f(Q_0)=\zeta_{48}f_2(\tau_0),\qquad
\zeta_{48}=e^{\pi i/24},\qquad
f_2(\tau)=\sqrt2\frac{\eta(2\tau)}{\eta(\tau)}.
\]
Since \(\tau_{31}=\tau_0+1\), the eta transformation law gives
\[
\eta(\tau_0+1)=e^{\pi i/12}\eta(\tau_0),\qquad
\eta(2\tau_0+2)=e^{\pi i/6}\eta(2\tau_0).
\]
Consequently,
\[
q_{31}=\frac1{f(Q_0)}.
\]

**Proof.** The definition of the Weber class invariant in Yui–Zagier, applied to \(Q_0=[1,1,8]\), has \(a=1,b=1,c=8\), \(\epsilon_{-31}=1\), and phase exponent
\(b(a-c+a^2c)=1\). Hence \(f(Q_0)=\zeta_{48}f_2(\tau_0)\). Taking the reciprocal and using the two eta translation laws above gives exactly the displayed expression for \(q_{31}\). \(\square\)

Yui–Zagier's Weber class-polynomial table gives
\[
W_{-31}(X)=X^3+X-1.
\]
Thus \(f(Q_0)\) is the positive real root of this polynomial, and its reciprocal satisfies
\[
q_{31}^3-q_{31}^2-1=0.
\]
The positive root is unique, so
\[
\boxed{q_{31}=s.}
\]
In particular,
\[
\boxed{
s=\frac{e^{\pi i/24}\eta(\tau_{31})}
{\sqrt2\,\eta(2\tau_{31})}.
}
\]

The modular input used here is the principal Weber invariant and its tabulated class polynomial. The conjectural assertion in Yui–Zagier that all signed Weber invariants are conjugate is **not** needed for this principal-class identification.

## 3. Hurwitz-zeta characterization

For \(a>0\), the Laurent expansion at \(u=1\) is
\[
\zeta_H(u,a)=\frac1{u-1}-\psi_{\rm dig}(a)+O(u-1).
\]
Therefore
\[
\boxed{
\psi_{\rm dig}(s)
=-\operatorname{FP}_{u=1}\zeta_H(u,s).
}
\]
Here \(\operatorname{FP}\) denotes the constant Laurent coefficient after subtracting the pole.

The Hurwitz–Lerch relation at zero gives
\[
\zeta_H'(0,a)=\log\Gamma_E(a)-\frac12\log(2\pi).
\]
Differentiating with respect to the second argument (permitted for \(a>0\)) yields a second exact representation:
\[
\boxed{
\psi_{\rm dig}(s)
=\left.\frac{\partial}{\partial a}\zeta_H'(0,a)\right|_{a=s}.
}
\]

## 4. Exact modular integral and positive series

The NIST DLMF integral representation, valid for \(\Re z>0\), is
\[
\psi_{\rm dig}(z)+\gamma
=\int_0^1\frac{1-t^{z-1}}{1-t}\,dt.
\]
Substitute the modular identity \(z=s=q_{31}\):
\[
\boxed{
\psi_{\rm dig}\!\left(
\frac{e^{\pi i/24}\eta(\tau_{31})}
{\sqrt2\eta(2\tau_{31})}
\right)
=-\gamma+
\int_0^1
\frac{
1-t^{
\frac{e^{\pi i/24}\eta(\tau_{31})}
{\sqrt2\eta(2\tau_{31})}-1}
}{1-t}\,dt.
}
\]
This is an exact integral representation whose argument is specified by a singular modular value of discriminant \(-31\).

Because \(s=1+r\), expanding \((1-t^r)/(1-t)\) as a nonnegative geometric series and applying monotone convergence gives
\[
\boxed{
\psi_{\rm dig}(s)
=-\gamma+\sum_{n=1}^{\infty}
\left(\frac1n-\frac1{n+r}\right)
=-\gamma+\sum_{n=1}^{\infty}
\frac{r}{n(n+r)},\qquad r=s^{-2}.
}
\]
All summands are positive and the series converges absolutely, since its terms are \(O(n^{-2})\).

## 5. Relation to T083 and T084

T083 gives the Euler-zeta expansion
\[
\psi_{\rm dig}(s)
=-\gamma+\sum_{n=1}^{\infty}
(-1)^{n+1}\zeta(n+1)s^{-2n}.
\]
T084 gives the accelerated odd-zeta and rational-series forms. T085 adds the exact modular identification of the argument and two Hurwitz/integral representations. These are complementary exact identities, not competing evaluations.

## 6. Epistemic status and non-claims

- **Proved exact identity:** the principal Weber invariant at discriminant \(-31\) is the reciprocal of the supergolden root, with the eta normalization displayed above.
- **Proved exact identity:** the digamma value is the finite part of the Hurwitz-zeta pole and the derivative with respect to the Hurwitz parameter of \(\zeta_H'(0,a)\).
- **Proved exact representation:** the modular integral and positive rational series.
- **Not proved / not claimed:** a finite expression for \(\psi_{\rm dig}(s)\) in terms of a finite set of algebraic numbers, logarithms, Dedekind eta values, or Dirichlet \(L\)-values.
- **Not implied:** CM algebraicity of the eta quotient does not by itself imply a closed-form evaluation of the digamma at that algebraic argument.
- **Numerics:** no new numerical digits are needed for this theorem; the independent high-precision decimal check remains the T083/T084 record.

## 7. References

1. N. Yui and D. Zagier, “On the singular values of Weber modular functions,” *Mathematics of Computation* 66 (1997), 1645–1662, especially the Weber invariant definition and the \(|d|=31\) row of Table 1. DOI: 10.1090/S0025-5718-97-00854-5.
2. NIST Digital Library of Mathematical Functions, §5.9(ii), equation 5.9.16 (digamma integral representation): https://dlmf.nist.gov/5.9.E16.
3. NIST Digital Library of Mathematical Functions, §25.11, equation 25.11.18 (Hurwitz zeta derivative at zero): https://dlmf.nist.gov/25.11.E18.
4. NIST Digital Library of Mathematical Functions, §5.2, equation 5.2.2 (definition of the digamma function): https://dlmf.nist.gov/5.2.E2.
