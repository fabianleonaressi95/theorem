# T149 — Exact symmetric period-three and period-six Fibonacci–Fricke orbits

**Date:** 25 November 2026  
**Classification:** exact symbolic theorem; finite-dimensional monodromy.  
**Status:** proved for the stated reversor-symmetric families. The level-\(c=4\) spectra are exact algebraic evaluations.

## Abstract

For the Fibonacci trace map
\[
T(x,y,z)=(2xy-z,x,y),\qquad
I(x,y,z)=x^2+y^2+z^2-2xyz-1,
\]
with reversor \(R(x,y,z)=(z,y,x)\), we determine the nontrivial symmetric period-three orbit and two exact families of symmetric period-six orbits. We compute their Fricke levels and exact monodromy polynomials. On \(c=4\), the period-six families give one orbit of type A and two of type C, with exact tangential traces \(402\) and \(536\pm98\sqrt{89}\).

T149 supplements T147 and T148, which analyze the distinct singular endpoints \(p_1=(1,1,1)\) and \(p_0=(0,0,0)\) of the period-two branch.

## 1. Reversibility

Direct substitution gives \(I\circ T=I\). The map
\[
R(x,y,z)=(z,y,x)
\]
satisfies
\[
R^2=1,\qquad RTR=T^{-1}.
\]
Every \(p=(a,b,a)\) is fixed by \(R\), so a periodic orbit through such a point is reversor-symmetric.

## 2. The nontrivial symmetric period-three orbit

The nontrivial symmetric period-three orbit is
\[
(-1,1,-1)\longmapsto(1,-1,-1)
\longmapsto(-1,-1,1)\longmapsto(-1,1,-1).
\]
Its Fricke value is \(I=0\). At \(p=(-1,1,-1)\),
\[
DT^3(p)=
\begin{pmatrix}
15&-10&-6\\
-6&3&2\\
2&-2&-1
\end{pmatrix},
\]
and
\[
\boxed{\chi_{DT^3(p)}(\lambda)
=(\lambda+1)(\lambda^2-18\lambda+1).}
\]
The full ambient monodromy spectrum is
\[
\boxed{\{-1,\;9+4\sqrt5,\;9-4\sqrt5\}.}
\]
The orbit lies at singular points of \(\Sigma_0\), where \(\nabla I=0\). This is therefore an ambient monodromy result, not a tangential Floquet statement on a regular Fricke surface.

## 3. Two symmetric period-six families

For \(p=(a,b,a)\), two nontrivial period-six families are as follows.

### Type A
\[
\boxed{p_A(b)=(0,b,0),\qquad b\ne0.}
\]
Its orbit is
\[
\begin{aligned}
(0,b,0)&\to(0,0,b)\to(-b,0,0)\\
&\to(0,-b,0)\to(0,0,-b)\to(b,0,0)\to(0,b,0).
\end{aligned}
\]
Its Fricke level is
\[
\boxed{c_A=b^2-1.}
\]

### Type C
\[
\boxed{p_C(a)=\left(a,\frac{a}{2a+1},a\right),}
\]
where \(2a+1\ne0\), \(a\ne0,-1\) for exact period six. Its six points are
\[
\begin{aligned}
p_0&=(a,a/(2a+1),a),\\
p_1&=(-a/(2a+1),a,a/(2a+1)),\\
p_2&=(-a,-a/(2a+1),a),\\
p_3&=(-a/(2a+1),-a,-a/(2a+1)),\\
p_4&=(a,-a/(2a+1),-a),\\
p_5&=(a/(2a+1),a,-a/(2a+1)),
\end{aligned}
\qquad T(p_j)=p_{j+1\pmod6}.
\]
Its Fricke level is
\[
\boxed{
c_C(a)=\frac{(a+1)^2(4a^2-2a-1)}{(2a+1)^2}.
}
\]

The other algebraic component \(b=a/(2a-1)\) of the symmetric \(T^6\)-fixed locus is the period-two branch already treated in T147–T148, not a new period-six family. Lower-period points must be excluded when classifying exact period six.

## 4. Tangential monodromy on regular period-six levels

At an exact period-six point \(p\) on a regular Fricke level, put \(M_6(p)=DT^6(p)\). Differentiating \(I\circ T^6=I\) fixes the normal covector. Since \(\det DT=1\), the ambient characteristic polynomial factors as
\[
\chi_{M_6(p)}(\lambda)
=(\lambda-1)(\lambda^2-\tau\lambda+1),
\qquad
\tau=\operatorname{tr}(M_6(p))-1.
\]
The reciprocal quadratic is the characteristic polynomial of the two-dimensional tangential monodromy.

### Type A at \(c=4\)

The level equation gives \(b=\pm\sqrt5\); these parameter values belong to the same orbit because \(T^3p_A(b)=p_A(-b)\). Exact multiplication gives
\[
\boxed{\chi_{M_6}(\lambda)
=(\lambda-1)(\lambda^2-402\lambda+1).}
\]
The tangential trace is \(402\).

### Type C at \(c=4\)

The level equation is
\[
4a^4+6a^3-17a^2-20a-5=0,
\]
with factorization over \(\mathbb Q(\sqrt{89})\):
\[
4\left(a^2+\frac{3-\sqrt{89}}4a+\frac{3-\sqrt{89}}8\right)
 \left(a^2+\frac{3+\sqrt{89}}4a+\frac{3+\sqrt{89}}8\right)=0.
\]
The four real roots form two period-six cycles, paired by \(T^3\). The two exact tangential traces are
\[
\boxed{\tau_C^\pm=536\pm98\sqrt{89},}
\]
and the corresponding tangential characteristic polynomials are
\[
\boxed{\lambda^2-\bigl(536\pm98\sqrt{89}\bigr)\lambda+1.}
\]
The roots of the quadratic with coefficient \(3+\sqrt{89}\) give the plus trace; those of the quadratic with coefficient \(3-\sqrt{89}\) give the minus trace.

## 5. Periodic-orbit count at \(c=4\)

Within the reversor-symmetric locus \(x=z\), the level \(c=4\) contains one exact period-six Type-A orbit, two exact period-six Type-C orbits, and two period-two orbits on the separate period-two branch. The nontrivial symmetric period-three orbit lies on \(c=0\), not \(c=4\). This is not a classification of all possibly nonsymmetric periodic orbits on the full Fricke surface.

## 6. Theorem statement and proof

**Theorem.** The symmetric period-three orbit and the Type-A and Type-C period-six families above have the stated exact Fricke levels and monodromies. At \(c=4\), the Type-A tangential trace is \(402\), while the two Type-C tangential traces are \(536\pm98\sqrt{89}\).

**Proof.** The orbit formulae follow by direct substitution into \(T\), and the Fricke values by substitution into \(I\). The monodromy matrices are products of
\[
DT(x,y,z)=
\begin{pmatrix}2y&2x&-1\\1&0&0\\0&1&0\end{pmatrix}.
\]
On regular period-six levels, invariance of \(I\) fixes the normal covector and unimodularity gives the reciprocal tangential quadratic. Substitution of \(b^2=5\), and reduction modulo the Type-C quartic, gives the exact traces displayed above. The period-three matrix is obtained by multiplying the three exact Jacobians at its orbit points. \(\square\)

## 7. Scope

- The classification is restricted to the reversor-symmetric locus \(x=z\); nonsymmetric period-six orbits are not classified.
- The period-three orbit is singular on \(\Sigma_0\); its spectrum is ambient, not a regular-surface tangential spectrum.
- The traces \(402\) and \(536\pm98\sqrt{89}\) are exact dynamical monodromy traces. They are not identified here with physical resonance frequencies or Pellis spectral data.
- The relation to the Q6 hexagram involution is treated separately in T150.
