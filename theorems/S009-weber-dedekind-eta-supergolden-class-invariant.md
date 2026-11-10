# Lemma S.9 — Dedekind–Weber class invariant and the supergolden root at discriminant -31

**Status:** exact modular/class-field bridge, conditional on the published Weber class equation for discriminant \(-31\). The transformations and reciprocal-cubic reduction are derived below. The source class polynomial is cited explicitly; this record does not claim to re-prove its construction from scratch.

## 1. Arithmetic setting

Let
\[
K=\mathbb Q(\sqrt{-31}),\qquad D_K=-31.
\]
Since \(-31\) is a fundamental discriminant, the maximal order is
\[
\mathcal O_K=\mathbb Z\left[\frac{1+\sqrt{-31}}2\right].
\]
The reduced primitive positive binary quadratic forms of discriminant \(-31\) are
\[
[1,1,8],\qquad [2,1,4],\qquad [2,-1,4].
\]
Hence \(h_K=3\). The principal form is \(Q_0=[1,1,8]\), with CM point
\[
\tau_0=\frac{-1+\sqrt{-31}}2\in\mathbb H.
\]

## 2. Dedekind eta and the Weber functions

For \(\tau\in\mathbb H\), put \(q=e^{2\pi i\tau}\) and
\[
\eta_{\rm Ded}(\tau)
=q^{1/24}\prod_{n\ge1}(1-q^n)
=e^{\pi i\tau/12}\prod_{n\ge1}(1-e^{2\pi i n\tau}).
\]
Use the classical Weber functions
\[
f(\tau)=e^{-\pi i/24}
\frac{\eta_{\rm Ded}((\tau+1)/2)}{\eta_{\rm Ded}(\tau)},
\qquad
f_2(\tau)=\sqrt2\,\frac{\eta_{\rm Ded}(2\tau)}{\eta_{\rm Ded}(\tau)},
\]
and \(\zeta_{48}=e^{2\pi i/48}\).

For \(D=-31\), the Yui–Zagier Weber class-invariant convention gives
\[
\rho=\zeta_{48} f_2(\tau_0).
\]
Their tabulated Weber class polynomial is
\[
W_{-31}(X)=X^3+X-1.
\]
Thus the real positive class invariant \(\rho\) satisfies
\[
\rho^3+\rho-1=0.
\]

## 3. Exact identification with the supergolden number

Let \(\psi>0\) be the unique positive root of
\[
\psi^3-\psi^2-1=0.
\]
Then
\[
\left(\frac1\psi\right)^3+\frac1\psi-1
=\frac{1+\psi^2-\psi^3}{\psi^3}=0.
\]
Since \(X^3+X-1\) has exactly one positive root,
\[
\boxed{\rho=\psi^{-1}.}
\]
Consequently
\[
\boxed{\psi=\frac1{\zeta_{48}f_2(\tau_0)}.}
\]
This is the precise modular/class-invariant bridge: the supergolden algebraic number is the reciprocal of the Weber class invariant attached to the principal class of discriminant \(-31\).

The Grablovitz cubic is not the Weber polynomial itself. Its negative real root is
\[
x_0=-\psi,\qquad x_0^3+x_0^2+1=0.
\]
The two cubic equations are related by reciprocal/sign transformations, not by identifying their polynomials.

## 4. The value at \(\tau=i\sqrt{31}\)

The Weber transformation identity
\[
f_2(\tau)=\zeta_{48}\frac{\sqrt2}{f(2\tau-1)}
\]
and the product definitions give
\[
f(\tau+1)=\zeta_{48}^{-1}f_1(\tau),\qquad
f_1(\tau+1)=\zeta_{48}^{-1}f(\tau),
\]
hence
\[
f(\tau+2)=\zeta_{48}^{-2}f(\tau),\qquad
f(\tau-2)=\zeta_{48}^{2}f(\tau).
\]
For \(\tau=\tau_0=(-1+i\sqrt{31})/2\),
\[
2\tau_0-1=-2+i\sqrt{31}.
\]
Therefore
\[
\begin{aligned}
\rho
&=\zeta_{48}f_2(\tau_0)\\
&=\frac{\zeta_{48}^2\sqrt2}{f(i\sqrt{31}-2)}\\
&=\frac{\sqrt2}{f(i\sqrt{31})}.
\end{aligned}
\]
Combining with \(\rho=1/\psi\) yields
\[
\boxed{f(i\sqrt{31})=\sqrt2\,\psi,}
\qquad
\boxed{f(i\sqrt{31})^2=2\psi^2.}
\]
If \(W=f(i\sqrt{31})^2\), eliminating \(\psi\) gives
\[
\boxed{W^3-2W^2-8W-8=0.}
\]
Indeed, substituting \(W=2\psi^2\) and \(\psi^3=\psi^2+1\) makes the left-hand side identically zero.

**CM-order warning.** The point \(\tau_0=(-1+i\sqrt{31})/2\) has discriminant \(-31\). The point \(i\sqrt{31}\) has quadratic order discriminant \(-124\). They are not the same CM point; the displayed Weber transformations are the exact bridge between the two evaluations. This distinction repairs the imprecise point identification in the input note.


## 4.1 Independent check from the eta quotient and correction of a constant-name mix-up

The eta quotient definition above can be checked directly from the infinite product:
\[
\begin{aligned}
f(\tau)
&=e^{-\pi i/24}\frac{\eta_{\rm Ded}((\tau+1)/2)}{\eta_{\rm Ded}(\tau)}\\
&=q^{-1/48}\prod_{n\ge1}
\frac{1-(-q^{1/2})^n}{1-q^n}\\
&=q^{-1/48}\prod_{n\ge1}(1+q^{n-1/2}).
\end{aligned}
\]
In the last equality, the even-index numerator factors cancel the denominator product, leaving the odd-index factors. This confirms the standard Weber f-product with the stated q convention.

At \(\tau=i\sqrt{31}\),
\[
q=e^{-2\pi\sqrt{31}}=6.4113268701409869\ldots\times10^{-16},
\]
\[
q^{-1/48}=2.0726306602637215\ldots,
\quad
\prod_{n\ge1}(1+q^{n-1/2})=1.0000000253205981\ldots,
\]
and therefore
\[
f(i\sqrt{31})=2.0726307127439694\ldots.
\]
The leading product correction is \(q^{1/2}=2.5320598\ldots\times10^{-8}\), small but not negligible if quoting eight significant digits.

**Terminology correction.** The plastic constant \(p=1.3247179572\ldots\), root of \(p^3-p-1=0\), is not the supergolden number used in this project. Here \(\psi=1.4655712318767680\ldots\) is the positive root of \(\psi^3-\psi^2-1=0\). Thus \(\sqrt2 p=1.87369\ldots\) is not the Weber value, whereas
\[
\boxed{\sqrt2\,\psi=2.0726307127439694\ldots=f(i\sqrt{31}).}
\]
The exact equality in Section 4 is numerically confirmed, not refuted. The degree-six polynomial for \(W=f(i\sqrt{31})^2\) is consistent with \(W=2\psi^2\); it does not imply incompatibility with the cubic equation for \(\psi\).

The document 18_57.pdf is not evidence for this Weber calculation: it concerns spectra of homogeneous spherical spaces. The eta quotient, product expansion and CM class equation must be supported by the Weber/Dedekind-eta sources cited below, independently of that PDF.

## 5. Class-field consequence and the \(j\)-invariant distinction

The Weber class invariant \(\rho\) generates the Hilbert class field over \(K\) under the class-invariant theorem for this discriminant. Since \(\psi=\rho^{-1}\),
\[
K(\psi)=K(\rho)=H_K,\qquad [H_K:K]=h_K=3.
\]
The cubic field \(\mathbb Q(\psi)\) is a non-Galois degree-three subfield; adjoining \(\sqrt{-31}\) gives its splitting field/Hilbert class field.

The singular modulus
\[
j\!\left(\frac{1+\sqrt{-31}}2\right)
\]
is another algebraic generator associated with the same CM class field. It is not the root of \(X^3+X^2+1\), and its Hilbert class polynomial is not that Grablovitz cubic. A relation between two generators of the same field must be given by an explicit algebraic transformation; equality of their minimal polynomials is not implied.

The algebraic integer \(\psi\) is a unit (its monic polynomial has constant term \(-1\) and norm \(1\)). This lemma does **not** assert that it is the fundamental unit of \(\mathbb Q(\psi)\); that requires a separate regulator/minimal-unit argument.

## 6. Evidence and scope

- The class number and the three reduced forms are exact finite arithmetic.
- The Weber class equation \(X^3+X-1\) is the published Yui–Zagier table entry for \(D=-31\).
- The reciprocal relation and the transformations to \(f(i\sqrt{31})\) are exact algebraic consequences of that class equation and the Weber transformation laws.
- A 100-digit numerical cross-check gives
  \[
  \psi=1.465571231876768026656731225219939108\ldots,
  \]
  \[
  \rho=0.682327803828019327369483739711048257\ldots,
  \]
  \[
  f(i\sqrt{31})=2.072630712743969426305340645406994491\ldots.
  \]
  The numerical check supports the normalization; it is not a substitute for the class-invariant theorem.

## References

1. N. Yui and D. Zagier, “On the Singular Values of Weber Modular Functions,” *Mathematics of Computation* **66** (1997), no. 220, 1645–1662, DOI: [10.1090/S0025-5718-97-00854-5](https://doi.org/10.1090/S0025-5718-97-00854-5), especially the Weber functions/class invariants and the \(D=-31\) row of Table 1.
2. NIST Digital Library of Mathematical Functions, §23.15 (Dedekind eta definitions) and §23.18 (modular transformations): https://dlmf.nist.gov/23.15 and https://dlmf.nist.gov/23.18.

3. R. Schertz, “Weber's class invariants revisited,” *Journal de théorie des nombres de Bordeaux* 14 (2002), no. 1, 325–343. DOI: [10.5802/jtnb.361](https://doi.org/10.5802/jtnb.361). This supplies a rigorous account of the singular values of the Weber functions, eta multipliers and Shimura reciprocity.
4. D. A. Cox, *Primes of the Form \\(x^2+ny^2\\): Fermat, Class Field Theory, and Complex Multiplication*, 3rd ed., American Mathematical Society, 2022. Background on quadratic forms, CM and class fields.
5. NIST DLMF, §§23.15, 23.18 and 27.14, for the Dedekind eta definition, product and modular transformation law.
