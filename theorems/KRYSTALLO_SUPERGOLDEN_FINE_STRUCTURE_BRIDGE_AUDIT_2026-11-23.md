# Krystallo–supergolden–fine-structure bridge audit

**Date:** 23 November 2026  
**Status:** exact component geometry and algebra; modular identity conditional on the published Weber class-polynomial entry; bridges to a three-state supergolden evolution and to the fine-structure constant remain open.

## 1. Krystallo spiral: exact geometric law

Measure the polar angle in radians. The stated rule, a radial multiplication by \(\sqrt2\) every \(\pi/4\), is equivalent to
\[
K(\theta)=\exp\!\left(\frac{\log 2}{\pi/2}\theta\right)
=2^{2\theta/\pi},\qquad K(0)=1.
\]
Thus
\[
K(\theta+\pi/4)=\sqrt2 K(\theta),\qquad
K(\theta+\pi/2)=2K(\theta).
\]
At quadrant points,
\[
K_n:=K(n\pi/2)=2^n,\qquad n\in\mathbb Z.
\]
This is a logarithmic spiral with constant angular growth rate. Its Cartesian parametrization is
\[
(x(\theta),y(\theta))=
K(\theta)(\cos\theta,\sin\theta).
\]
The sequence \(1,2,4,8,16,\ldots\) is exactly the sequence of radii at successive quadrant points. Intermediate 45-degree radii are \(2^{n+1/2}=2^n\sqrt2\).

## 2. Fibonacci comparison: what is and is not identical

The Fibonacci sequence is
\[
F_0=0,\quad F_1=1,\quad F_{n+2}=F_{n+1}+F_n.
\]
Its positive quadrant samples can be indexed as \(1,1,2,3,5,8,\ldots\), depending on the starting-index convention. The ratio \(F_{n+1}/F_n\) tends to \(\varphi\), but is not constant at finite index. Consequently, Fibonacci samples do not define the same exact logarithmic spiral law as \(K_n=2^n\). A Fibonacci spiral made from quarter-circle arcs is a geometric construction with discrete square sizes; the ideal golden logarithmic spiral has a constant scale factor \(\varphi\) per quarter-turn. These notions should not be conflated.

## 3. Supergolden algebra: exact but independent

Let \(s>1\) be the positive root of
\[
s^3-s^2-1=0.
\]
Then
\[
s^3=s^2+1,\qquad s-1=s^{-2}.
\]
The matrix
\[
M_s=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix}
\]
has characteristic polynomial
\[
\det(xI-M_s)=x^3-x^2-1.
\]
Thus \(s\) is its Perron eigenvalue. This is an exact algebraic fact. It does not follow from the Krystallo radius law: the scalar quadrant sequence obeys
\[
K_{n+1}=2K_n,
\]
whose minimal scalar characteristic polynomial is \(x-2\), not \(x^3-x^2-1\).

A three-component geometric state, transition rule, and observation map must be specified before \(M_s\) can be derived from a spiral construction. Merely sampling a scalar spiral at quadrants does not create three independent state variables.

## 4. Analytic chain T083–T085: audit result

The three records are mutually consistent on the digamma value:
\[
\psi_{\rm dig}(s)
=-\gamma+\sum_{n\ge1}(-1)^{n+1}\zeta(n+1)s^{-2n}
\]
(T083), and the accelerated odd-zeta form in T084.

The positive rational series in T085 is also correct. Put \(r=s-1=s^{-2}\), so \(s=1+r\). NIST DLMF 5.9.16 states
\[
\psi_{\rm dig}(z)+\gamma
=\int_0^1\frac{1-t^{z-1}}{1-t}\,dt,\qquad \Re z>0.
\]
At \(z=s=1+r\), expand \((1-t)^{-1}=\sum_{k\ge0}t^k\) and integrate:
\[
\begin{aligned}
\psi_{\rm dig}(s)+\gamma
&=\sum_{k=0}^\infty\left(\frac1{k+1}-\frac1{k+r+1}\right)\\
&=\sum_{n=1}^\infty\frac{r}{n(n+r)}.
\end{aligned}
\]
There is **no missing factor**. The distinct expansion for \(\psi(1-r)\) concerns a different argument. The distinction between \(r\), \(1-r\), and \(1+r=s\) is now explicit in T085.

## 5. Weber–Dedekind eta normalization: source-level audit

For \(d=-31\), Yui–Zagier's hypotheses in §1 hold: \(d<0\), \(d\equiv1\pmod8\), and \(d\not\equiv0\pmod3\). The principal form is
\[
Q_0=[1,1,8],\qquad \tau_0=\frac{-1+i\sqrt{31}}2.
\]
Their definition (pp. 1647–1648) gives, in the odd-\(a\), even-\(c\) case,
\[
f(Q_0)=\epsilon_{-31}\zeta^{b(a-c+a^2c)}f_2(\tau_0)
=\zeta_{48}f_2(\tau_0),
\]
because \(\epsilon_{-31}=1\) and \(1-8+8=1\). Their Table 1 (p. 1649) lists, for \(|d|=31\), class number 3 and coefficient row \(1,0,1,-1\), i.e.
\[
W_{-31}(X)=X^3+X-1.
\]
The paper explains that its table was obtained by high-precision numerical computation and recognition of integer coefficients (pp. 1649–1650). Accordingly, this record treats the class-polynomial entry as a published computational result, not as a new first-principles derivation in this repository.

Since \(X^3+X-1\) has one positive root and \(s^{-1}\) satisfies it, the principal invariant is identified with \(s^{-1}\), subject to the paper's stated Weber normalization. The eta quotient in T085 follows from the exact eta translation law at \(\tau_{31}=\tau_0+1\):
\[
\eta(\tau_0+1)=e^{\pi i/12}\eta(\tau_0),\qquad
\eta(2\tau_0+2)=e^{\pi i/6}\eta(2\tau_0),
\]
and hence
\[
s=\frac{e^{\pi i/24}\eta(\tau_{31})}
{\sqrt2\,\eta(2\tau_{31})}.
\]
The normalization is algebraically consistent with the paper's definition; the numerical product check is supplementary, not the proof.

**Congruence note.** Yui–Zagier's alternate choice of representative uses \(b\equiv-a\pmod{24}\) (pp. 1648–1649). The Weber multiplier is a 48th root of unity, so phase exponents are tracked modulo 48; that is not a reason to replace the representative congruence by modulo 48. S009 has been corrected accordingly.

## 6. Fine-structure constant: no established bridge

The Wyler expression recorded in F001 is
\[
\alpha_W=\frac{9}{8\pi^4}
\left(\frac{\pi^5}{2^4 5!}\right)^{1/4},
\qquad \alpha_W^{-1}\simeq137.0360824.
\]
This is a dimensionless geometric expression attributed to Wyler. The current T083–T085 chain establishes identities involving the supergolden algebraic number, the digamma function, Hurwitz zeta, and a Weber–Dedekind eta quotient. It does **not** derive \(\alpha_W\), the measured fine-structure constant, or a QED coupling.

A valid bridge would require an independently defined geometric or operator quantity whose normalization is fixed before comparison with \(\alpha\), and a proof that its value equals the proposed expression. Fitting a scale, selecting a normalization after seeing \(\alpha\), or observing numerical proximity is insufficient.

## 7. Classification and next mathematical tasks

| Item | Status |
|---|---|
| \(K(\theta)=2^{2\theta/\pi}\), quadrant radii \(2^n\) | Exact definition/consequence |
| Fibonacci recurrence and limiting ratio \(\varphi\) | Exact standard result |
| \(M_s\) characteristic polynomial | Exact algebra |
| Derivation of \(M_s\) from Krystallo geometry | Open |
| T083–T085 digamma identities | Exact identities; numerical checks recorded |
| Weber–eta identification at \(d=-31\) | Conditional on the published Weber class-polynomial entry and normalization |
| Krystallo/supergolden operator bridge | Open |
| Supergolden/Wyler or supergolden/physical \(\alpha\) bridge | Open; no derivation established |

The next constructive step is to define a three-component state from an explicit geometric refinement of the Krystallo spiral, specify its transition matrix without inserting \(s\), and then calculate its characteristic polynomial. Only if that independently yields \(x^3-x^2-1\) will there be a genuine Krystallo–supergolden theorem candidate.
