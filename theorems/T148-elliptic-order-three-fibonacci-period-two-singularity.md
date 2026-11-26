# T148 — Elliptic order-three tangential spectrum at the singular Fibonacci period-two orbit

**Date:** 25 November 2026  
**Classification:** exact symbolic theorem (finite-dimensional algebra and local spectral continuity).  
**Status:** proved. No numerical fitting or model-dependent assumption is used.

## Abstract

For the Fibonacci trace map
\[
T(x,y,z)=(2xy-z,x,y),\qquad
I(x,y,z)=x^2+y^2+z^2-2xyz-1,
\]
we study the endpoint \(p_0=(0,0,0)\) of the exact period-two branch
\[
p(x)=\left(x,\frac{x}{2x-1},x\right).
\]
The endpoint is a singular point of the Fricke level \(\Sigma_{-1}\). We compute the limiting Fricke normal, the exact monodromy \(DT^2(p_0)\), and its invariant tangent plane. The restricted monodromy is an orthogonal rotation through \(-2\pi/3\), with characteristic polynomial \(\lambda^2+\lambda+1\) and primitive cube roots of unity as eigenvalues. The Fricke level approaches \(-1\) quadratically, with leading coefficient \(3\).

This result is the elliptic counterpart of T147, which treats the distinct endpoint \(p_1=(1,1,1)\) and its golden hyperbolic tangential spectrum.

## 1. Map, invariant, and period-two branch

Let
\[
T(x,y,z)=(2xy-z,x,y),\qquad
I(x,y,z)=x^2+y^2+z^2-2xyz-1.
\]
Direct substitution gives \(I\circ T=I\). A second iteration is
\[
T^2(x,y,z)=(4x^2y-2xz-y,\;2xy-z,\;x).
\]
Solving \(T^2(x,y,z)=(x,y,z)\) gives \(z=x\) and \(y(2x-1)=x\). For \(x\ne\tfrac12\), the first equation is then satisfied identically, so the branch is
\[
p(x)=\left(x,\frac{x}{2x-1},x\right).
\]
Its period is exactly two for \(x\notin\{0,\tfrac12,1\}\); \(p(0)=(0,0,0)\) and \(p(1)=(1,1,1)\) are fixed points. In particular,
\[
p(x)\longrightarrow p_0=(0,0,0)\qquad(x\to0).
\]

## 2. Singular Fricke endpoint and limiting normal

At the endpoint,
\[
I(p_0)=-1,\qquad \nabla I(p_0)=0.
\]
Thus \(p_0\) is a singular point of the level \(\Sigma_{-1}\).

Along the period-two branch, direct substitution gives
\[
\nabla I(p(x))
=\frac{2x(x-1)}{2x-1}\bigl(1,-(2x+1),1\bigr).
\]
Equivalently,
\[
\nabla I(p(x))
=\frac{2x}{2x-1}
\bigl(x-1,-2x^2+x+1,x-1\bigr).
\]
After removing the scalar factor \(2x/(2x-1)\), the vector factor converges to
\[
n_0=(-1,1,-1).
\]
Consequently the limiting tangent plane of the regular Fricke levels along this branch is
\[
\boxed{\Pi_0=\ker(n_0^T)
=\{(u,v,w)\in\mathbb R^3:-u+v-w=0\}.}
\]
The normal is defined up to a nonzero scalar; the displayed choice fixes an orientation convention only.

## 3. Monodromy at \(p_0\)

The derivative is
\[
DT(x,y,z)=
\begin{pmatrix}
2y&2x&-1\\
1&0&0\\
0&1&0
\end{pmatrix}.
\]
At \(p_0\),
\[
J_0=DT(p_0)=
\begin{pmatrix}
0&0&-1\\
1&0&0\\
0&1&0
\end{pmatrix},
\qquad
A_0=DT^2(p_0)=J_0^2=
\begin{pmatrix}
0&-1&0\\
0&0&-1\\
1&0&0
\end{pmatrix}.
\]
The characteristic polynomials are
\[
\chi_{J_0}(\lambda)=\lambda^3+1
=(\lambda+1)(\lambda^2-\lambda+1),
\]
and
\[
\boxed{\chi_{A_0}(\lambda)=\lambda^3-1
=(\lambda-1)(\lambda^2+\lambda+1).}
\]
Thus
\[
\operatorname{spec}(A_0)
=\left\{1,e^{2\pi i/3},e^{-2\pi i/3}\right\}.
\]

## 4. Invariance of the limiting tangent plane

A direct calculation gives
\[
A_0^T n_0=n_0.
\]
For every \(q\in\Pi_0\),
\[
n_0^T(A_0q)=(A_0^Tn_0)^Tq=n_0^Tq=0.
\]
Therefore
\[
\boxed{A_0\Pi_0=\Pi_0.}
\]
Equality follows because \(A_0\) is invertible.

## 5. Exact tangential restriction and order-three rotation

Choose the orthonormal basis of \(\Pi_0\)
\[
u_1=\frac{1}{\sqrt2}(1,1,0)^T,\qquad
u_2=\frac{1}{\sqrt6}(1,-1,-2)^T.
\]
Let \(U=[u_1\ u_2]\). Direct multiplication yields
\[
\boxed{
U^TA_0U=
\begin{pmatrix}
-\tfrac12&\tfrac{\sqrt3}{2}\\
-\tfrac{\sqrt3}{2}&-\tfrac12
\end{pmatrix}.
}
\]
This is the planar rotation through angle \(-2\pi/3\) in the stated oriented orthonormal basis. In particular, the restriction is orthogonal and
\[
(A_0|_{\Pi_0})^3=I_{\Pi_0}.
\]
Its characteristic polynomial and spectrum are
\[
\boxed{\chi_{A_0|_{\Pi_0}}(\lambda)=\lambda^2+\lambda+1,}
\qquad
\boxed{\operatorname{spec}(A_0|_{\Pi_0})
=\{e^{2\pi i/3},e^{-2\pi i/3}\}.}
\]
The restriction has exact order three: it is not the identity, while its cube is the identity.

For completeness, in the non-orthonormal basis
\[
e_1=(1,1,0)^T,\qquad e_2=(1,0,-1)^T
\]
the same restriction is represented by
\[
[A_0|_{\Pi_0}]_{(e_1,e_2)}
=\begin{pmatrix}0&1\\-1&-1\end{pmatrix},
\]
which has the same characteristic polynomial.

## 6. Exact Fricke level and quadratic endpoint scaling

Substitution of \(p(x)\) into \(I\) gives
\[
c(x):=I(p(x))
=\frac{(x-1)^2(4x^2+2x-1)}{(2x-1)^2}.
\]
At \(x=0\), \(c(0)=-1\), and the exact difference is
\[
\boxed{
c(x)+1=\frac{x^2(4x^2-6x+3)}{(2x-1)^2}.
}
\]
Its Taylor expansion is
\[
c(x)+1=3x^2+6x^3+16x^4+O(x^5).
\]
Hence
\[
\boxed{c(x)+1\sim3x^2,\qquad
x=\pm\sqrt{\frac{c+1}{3}}+O(c+1)}
\]
on the two local inverse branches as \(c\downarrow-1\) through values attained by the branch. More precisely, the sign distinguishes the two sides \(x\to0^\pm\).

## 7. Main theorem

**Theorem (elliptic order-three tangential spectrum at the singular period-two endpoint).**  
For the Fibonacci trace map and Fricke invariant defined above, the exact period-two branch
\[
p(x)=\left(x,\frac{x}{2x-1},x\right)
\]
has the singular endpoint \(p_0=(0,0,0)\) as \(x\to0\). The endpoint lies on \(\Sigma_{-1}\) and satisfies \(\nabla I(p_0)=0\). The limiting Fricke normal along the branch is \(n_0=(-1,1,-1)\), and its kernel \(\Pi_0\) is invariant under
\[
A_0=DT^2(p_0)=
\begin{pmatrix}0&-1&0\\0&0&-1\\1&0&0\end{pmatrix}.
\]
The restriction \(A_0|_{\Pi_0}\) is an orthogonal rotation of exact order three, with characteristic polynomial \(\lambda^2+\lambda+1\) and eigenvalues \(e^{\pm2\pi i/3}\). Along the branch the Fricke level satisfies
\[
I(p(x))+1=3x^2+O(x^3).
\]

**Proof.** The branch and its exact period classification follow from the equations for \(T^2(p)=p\). The endpoint, gradient factorization, and level expansion follow by direct substitution. The derivative and its square give \(A_0\). The identity \(A_0^Tn_0=n_0\) proves invariance of the kernel. The displayed orthonormal-basis matrix proves that the restriction is the stated order-three rotation. \(\square\)

## 8. Relation to T147 and scope

T147 concerns the other singular endpoint \(p_1=(1,1,1)\), on \(\Sigma_0\), where the limiting tangential spectrum is the real reciprocal pair \(\{\varphi^4,\varphi^{-4}\}\). T148 concerns \(p_0=(0,0,0)\), on \(\Sigma_{-1}\), where the limiting tangential spectrum is the primitive cube-root pair. These are distinct endpoint limits of the same algebraic period-two branch; neither spectrum is inferred from the other.

All claims here concern exact finite-dimensional algebra and the limiting linearization of the stated trace map. No physical interpretation, continuum limit, or identification with an independent RGS/PSU model is asserted.
