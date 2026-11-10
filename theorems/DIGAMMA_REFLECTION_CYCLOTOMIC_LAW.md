# Theorem — Digamma reflection and the rational/irrational angle dichotomy

**Status:** proved (analytic and transcendence-theoretic statement).  
**Scope:** exact identities for the digamma function. This theorem does **not** assert a geometric realization in Q6/PSU; that remains a separate open problem.

## 1. Statement

Let
\[
\psi(z)=\frac{\Gamma'(z)}{\Gamma(z)}
\]
be the digamma function.

### Theorem 1 (reflection law)

For every \(x\in\mathbb C\setminus\mathbb Z\) at which the terms are defined,
\[
\boxed{\psi(1-x)-\psi(x)=\pi\cot(\pi x).}
\]

In particular, for real \(x\notin\mathbb Z\), the difference of the two digamma values is exactly the cotangent coefficient multiplied by \(\pi\).

### Theorem 2 (algebraic-parameter dichotomy)

Let \(x\) be a real algebraic number with \(x\notin\mathbb Z\).

1. If \(x\in\mathbb Q\), then \(\cot(\pi x)\) is algebraic.
2. If \(x\notin\mathbb Q\), then \(\cot(\pi x)\) is transcendental.

Consequently, the reflection difference
\[
D(x):=\psi(1-x)-\psi(x)
\]
has the exact form
\[
D(x)=\pi a_x,
\]
where \(a_x\) is algebraic for rational \(x\), and transcendental for algebraic irrational \(x\).

The theorem distinguishes the arithmetic nature of the angle parameter; it does not claim that \(D(x)\) itself is algebraic or transcendental.

## 2. Proof

**Reflection.** The identity is the standard logarithmic derivative of Euler's Gamma reflection formula
\[
\Gamma(x)\Gamma(1-x)=\frac{\pi}{\sin(\pi x)}.
\]
Taking the logarithmic derivative gives
\[
\psi(x)-\psi(1-x)=-\pi\cot(\pi x),
\]
which is the stated formula.

**Rational case.** If \(x=p/q\) with integers \(p,q\), \(q>0\), and \(p/q\notin\mathbb Z\), then
\[
\zeta=e^{2\pi i p/q}
\]
is a root of unity. Since
\[
\cot(\pi p/q)=i\,\frac{\zeta+1}{\zeta-1},
\]
the cotangent is algebraic.

**Algebraic irrational case.** Suppose \(x\) is algebraic irrational. By the Gelfond–Schneider theorem, every value of \((-1)^x\) is transcendental. In particular, using the principal logarithm,
\[
e^{i\pi x}=\exp(x\,i\pi)
\]
is transcendental. Hence \(e^{2\pi i x}\) is transcendental as well: if its square-root \(e^{i\pi x}\) were algebraic, its square would be algebraic, and conversely if the square were algebraic then \(e^{i\pi x}\) would satisfy a quadratic equation over the algebraic numbers.

For real noninteger \(x\), put \(u=e^{2\pi i x}\). Then
\[
\cot(\pi x)=i\,\frac{u+1}{u-1}.
\]
If \(\cot(\pi x)\) were algebraic, solving this fractional-linear equation for \(u\) would make \(u\) algebraic, a contradiction. Therefore \(\cot(\pi x)\) is transcendental.

This proves both cases. \(\square\)

## 3. Exact corollaries for the three constants

### 3.1 Silver ratio

Let
\[
\delta=1+\sqrt2=\cot(\pi/8).
\]
Then
\[
\boxed{\psi(7/8)-\psi(1/8)=\pi\delta.}
\]
Moreover, the quadratic equation
\[
\delta^2-2\delta-1=0
\]
is exactly compatible with cotangent doubling:
\[
\cot(\pi/4)=\frac{\delta^2-1}{2\delta}=1.
\]

### 3.2 Golden ratio and pentagonal angle

Let
\[
\varphi=\frac{1+\sqrt5}{2}=2\cos(\pi/5).
\]
Since
\[
\cot(\pi/5)=\sqrt{1+\frac{2}{\sqrt5}},
\]
the reflection law gives
\[
\boxed{
\psi(4/5)-\psi(1/5)
=\pi\sqrt{1+\frac{2}{\sqrt5}}.
}
\]
The coefficient is algebraic and belongs to a real cyclotomic field. It is **not** equal to \(\varphi\); the connection is through the pentagonal angle.

### 3.3 Supergolden parameter

Let \(s\) be the real root of
\[
s^3-s^2-1=0.
\]
The polynomial has no rational root, so \(s\) is irrational; it is real algebraic. Theorem 2 therefore gives
\[
\boxed{\cot(\pi s)\ \text{is transcendental}.}
\]
Applying reflection at \(s-1\in(0,1)\) and using digamma recurrence:
\[
\boxed{
\psi(2-s)-\psi(s)+\frac{1}{s-1}
=\pi\cot(\pi s).
}
\]
In particular, \(\cot(\pi s)\) cannot equal the silver ratio, the golden ratio, or any other algebraic number.

## 4. What is unified, and what is not

The three cases are unified by one exact analytic law: the Gamma reflection formula.

- Rational angles select algebraic cotangent values; the silver and pentagonal examples are cyclotomic.
- An algebraic irrational angle parameter selects a transcendental cotangent value; the supergolden parameter is in this second class.

This is a genuine theorem, not a numerical pattern. It supplies an arithmetic classification of the digamma reflection coefficient.

It does **not** yet prove that the silver, golden, and supergolden constants are eigenvalues of one common Q6/PSU refinement operator. In particular, the theorem does not derive the matrix
\[
A_s=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix}
\]
from the digamma, nor does it identify a quaternionic transport law producing that matrix.

## 5. Geometric law still to be proved

A possible next theorem must start with independently defined geometric data:

1. an oriented three-channel space \(V\) extracted from Q6;
2. a refinement or transfer operator \(R:V\to V\) defined from incidence/geometry, not from a target polynomial;
3. an explicitly defined quaternionic frame transport \(U(q)\);
4. a proof of closure (zero leakage from \(V\)) and equivariance under the relevant Anti-Twin action.

Only after these definitions may one compute the characteristic polynomial of \(R\). To obtain the supergolden polynomial, one must prove
\[
\det(\lambda I-R)=\lambda^3-\lambda^2-1
\]
without inserting \(A_s\) into the construction. Analogous constructions for the golden and silver cases must specify their own geometric operators or show that they arise as exact restrictions/iterates of one operator.

Until that construction exists, the analytic theorem above is **proved**, while the proposed common geometric refinement law is **open**.

## 6. Classification

| Claim | Status |
|---|---|
| Digamma reflection identity | **Proved** |
| Rational algebraic parameter gives algebraic cotangent | **Proved** |
| Algebraic irrational parameter gives transcendental cotangent | **Proved** (Gelfond–Schneider) |
| Silver digamma identity and angle doubling | **Proved** |
| Pentagonal-angle digamma identity | **Proved** |
| Supergolden digamma reflection identity | **Proved** |
| Common Q6/PSU operator generating all three cases | **Open** |
| Quaternionic derivation of the supergolden transfer matrix | **Open** |
