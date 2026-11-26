# T147 — Golden tangential spectrum at the conical period-two Fibonacci trace orbit

**Date:** 25 November 2026  
**Classification:** exact symbolic theorem (finite-dimensional algebra and local spectral continuity).  
**Status:** proved. No numerical fitting or model-dependent assumption is used.

## Abstract

For the Fibonacci trace map
\[
T(x,y,z)=(2xy-z,x,y),
\qquad
I(x,y,z)=x^2+y^2+z^2-2xyz-1,
\]
we determine the period-two branch converging to the singular Fricke point \(p_1=(1,1,1)\). We compute the exact monodromy of \(T^2\), identify the limiting tangent plane by the limiting Fricke normal, and prove that this plane is invariant. The restricted monodromy has characteristic polynomial
\[
\lambda^2-7\lambda+1
\]
and eigenvalues \(\varphi^4,\varphi^{-4}\). We also obtain the exact Fricke level along the branch and its quadratic conical asymptotics. Finally, the tangential Floquet multipliers of the regular period-two cycles converge to these two golden eigenvalues.

## 1. Map and invariant

Let
\[
T:\mathbb R^3\longrightarrow\mathbb R^3,
\qquad
T(x,y,z)=(2xy-z,x,y),
\]
and
\[
I(x,y,z)=x^2+y^2+z^2-2xyz-1.
\]
Direct substitution gives
\[
I(T(x,y,z))
=(2xy-z)^2+x^2+y^2-2(2xy-z)xy-1
=I(x,y,z).
\]
Thus \(I\circ T=I\), and every level \(\Sigma_c=I^{-1}(c)\) is invariant.

The point \(p_1=(1,1,1)\) is fixed by \(T\), satisfies \(I(p_1)=0\), and is singular on \(\Sigma_0\), since \(\nabla I(p_1)=0\).

## 2. Exact period-two branch

A direct second iteration gives
\[
T^2(x,y,z)=
(4x^2y-2xz-y,\;2xy-z,\;x).
\]
Solving \(T^2(x,y,z)=(x,y,z)\), the third equation gives \(z=x\), and the second gives
\[
y(2x-1)=x.
\]
For \(x\ne\tfrac12\), the first equation is then satisfied identically. Hence the branch is
\[
\boxed{p(x)=\left(x,\frac{x}{2x-1},x\right),\qquad x\ne\tfrac12.}
\]
The point \(p(x)\) is fixed by \(T\) precisely when
\[
x=\frac{x}{2x-1},
\]
which, on the branch, is equivalent to \(x=0\) or \(x=1\). Consequently the period is exactly two for
\[
x\in\mathbb R\setminus\left\{0,\tfrac12,1\right\}.
\]
In particular,
\[
p(x)\longrightarrow p_1=(1,1,1)\qquad (x\to1).
\]

## 3. Monodromy at the conical point

The derivative of \(T\) is
\[
DT(x,y,z)=
\begin{pmatrix}
2y&2x&-1\\
1&0&0\\
0&1&0
\end{pmatrix}.
\]
At \(p_1\),
\[
J=DT(p_1)=
\begin{pmatrix}
2&2&-1\\
1&0&0\\
0&1&0
\end{pmatrix}.
\]
Since \(p_1\) is fixed,
\[
A:=DT^2(p_1)=J^2
=
\boxed{\begin{pmatrix}
6&\mathbf 3&-2\\
2&2&-1\\
1&0&0
\end{pmatrix}.}
\]
The entry in the first row and second column is \(3\), because
\(\partial_y(4x^2y-2xz-y)=4x^2-1=3\) at \(x=1\).

A determinant calculation yields
\[
\begin{aligned}
\chi_A(\lambda)
&=\det(\lambda I_3-A)\\
&=\lambda^3-8\lambda^2+8\lambda-1\\
&=(\lambda-1)(\lambda^2-7\lambda+1).
\end{aligned}
\]
Writing \(\varphi=(1+\sqrt5)/2\), we have
\[
\frac{7\pm3\sqrt5}{2}=\varphi^{\pm4}.
\]
Therefore
\[
\boxed{\operatorname{spec}(A)=\{1,\varphi^4,\varphi^{-4}\}.}
\]

## 4. Limiting Fricke normal and invariant tangent plane

The gradient is
\[
\nabla I(x,y,z)=
(2x-2yz,\;2y-2xz,\;2z-2xy).
\]
Substitution of \(p(x)\) gives the exact factorization
\[
\boxed{
\nabla I(p(x))
=\frac{2x(x-1)}{2x-1}
\bigl(1,-(2x+1),1\bigr).
}
\]
For \(x\) near \(1\), \(x\ne1\), the scalar factor is nonzero. Thus the regular tangent plane to \(\Sigma_{I(p(x))}\) at \(p(x)\) is
\[
\mathcal T_x=\ker\bigl(1,-(2x+1),1\bigr).
\]
Its limiting normal direction is
\[
n=(1,-3,1),
\]
and the limiting plane is
\[
\boxed{\Pi_{\rm geom}=\ker n^T
=\{(u,v,w):u-3v+w=0\}.}
\]

The invariance of \(I\) under \(T^2\), differentiated at \(p_1\), gives
\[
\nabla I(p_1)^T A=\nabla I(p_1)^T,
\]
which is vacuous because \(\nabla I(p_1)=0\). Instead, the limiting normal must be checked directly. With the correct monodromy matrix,
\[
A^Tn
=
\begin{pmatrix}
6&2&1\\
3&2&0\\
-2&-1&0
\end{pmatrix}
\begin{pmatrix}1\\-3\\1\end{pmatrix}
=
\begin{pmatrix}1\\-3\\1\end{pmatrix}
=n.
\]
Hence
\[
n^TAv=n^Tv
\]
for all \(v\), and in particular \(A(\ker n^T)\subseteq\ker n^T\). The geometric limiting tangent plane is therefore exactly invariant under the limiting monodromy.

## 5. Tangential spectrum

Since \(\Pi_{\rm geom}\) is a two-dimensional invariant subspace, the eigenvalues of \(A|_{\Pi_{\rm geom}}\) are the two eigenvalues of \(A\) other than the simple eigenvalue \(1\). Equivalently, the quotient action on the normal covector has eigenvalue \(1\), so the characteristic polynomial of the restriction is the remaining factor:
\[
\boxed{
\chi_{A|_{\Pi_{\rm geom}}}(\lambda)
=\lambda^2-7\lambda+1.
}
\]
Consequently
\[
\boxed{
\operatorname{spec}(A|_{\Pi_{\rm geom}})
=\{\varphi^4,\varphi^{-4}\}.
}
\]
This identifies the golden pair with the dynamics on the actual geometric tangent plane, not merely with an abstract complementary spectral subspace.

## 6. Exact Fricke level and conical asymptotics

Substitution into the invariant gives
\[
\boxed{
c(x):=I(p(x))
=\frac{(x-1)^2(4x^2+2x-1)}{(2x-1)^2}.
}
\]
For \(x=1+\varepsilon\),
\[
c(1+\varepsilon)
=\frac{\varepsilon^2(5+10\varepsilon+4\varepsilon^2)}
{(1+2\varepsilon)^2}
=5\varepsilon^2-10\varepsilon^3+24\varepsilon^4
+O(\varepsilon^5).
\]
In particular,
\[
\boxed{c(x)=5(x-1)^2+O((x-1)^3),\qquad
c(x)\sim5(x-1)^2.}
\]
The leading order is quadratic, not cubic. On either local branch, inversion gives
\[
\boxed{
x(c)=1\pm\sqrt{\frac c5}+O(c)
}
\]
for \(c\downarrow0\). Thus \(\sqrt c\), rather than \(c\), is the natural local scale for this two-branch parametrization.

## 7. Convergence of the regular tangential Floquet multipliers

For \(x\ne1\) sufficiently close to \(1\), the gradient \(\nabla I(p(x))\) is nonzero, so \(p(x)\) is a regular point of the level \(\Sigma_{c(x)}\). Set
\[
A(x)=DT^2(p(x)),\qquad
\mathcal T_x=\ker\bigl(\nabla I(p(x))^T\bigr).
\]
Differentiating \(I\circ T^2=I\) at \(p(x)\), and using \(T^2(p(x))=p(x)\), yields
\[
A(x)^T\nabla I(p(x))=\nabla I(p(x)).
\]
Therefore \(\mathcal T_x\) is \(A(x)\)-invariant and the tangential restriction
\[
M_{\rm tan}(x)=A(x)|_{\mathcal T_x}
\]
is well-defined. Its two eigenvalues are the tangential Floquet multipliers of the period-two orbit.

The normalized normals converge, up to the harmless common sign, to \(n/\|n\|\). Hence the planes \(\mathcal T_x\) converge to \(\Pi_{\rm geom}\). Also \(A(x)\to A\). Choose a continuous local basis of \(\mathcal T_x\) near \(x=1\); in these bases the \(2\times2\) matrices representing \(M_{\rm tan}(x)\) converge to a matrix representing \(A|_{\Pi_{\rm geom}}\). Continuity of the roots of the characteristic polynomial then gives convergence of the unordered pair of tangential multipliers:
\[
\boxed{
\{\mu_1(x),\mu_2(x)\}
\longrightarrow
\{\varphi^4,\varphi^{-4}\}
\qquad(x\to1,\ x\ne1).
}
\]
After ordering by modulus near the limit, this reads
\[
\mu_u(x)\to\varphi^4,\qquad
\mu_s(x)\to\varphi^{-4}.
\]
The limiting expansion and contraction rates per iterate of \(T^2\) are respectively
\[
\log(\varphi^4)=4\log\varphi,
\qquad
\log(\varphi^{-4})=-4\log\varphi.
\]

## 8. Main theorem

**Theorem (golden tangential spectrum at the conical period-two Fibonacci orbit).**  
For the Fibonacci trace map \(T\) and Fricke invariant \(I\) defined above, the exact period-two branch
\[
p(x)=\left(x,\frac{x}{2x-1},x\right),
\qquad x\notin\{0,\tfrac12,1\},
\]
converges to the singular fixed point \(p_1=(1,1,1)\) as \(x\to1\). The limiting monodromy is
\[
DT^2(p_1)=
\begin{pmatrix}6&3&-2\\2&2&-1\\1&0&0\end{pmatrix},
\]
with characteristic polynomial
\[
(\lambda-1)(\lambda^2-7\lambda+1).
\]
The limiting Fricke normal is \(n=(1,-3,1)\), and its kernel is invariant under this monodromy. The restriction to that geometric tangent plane has eigenvalues \(\varphi^4,\varphi^{-4}\). Along the branch,
\[
I(p(x))=\frac{(x-1)^2(4x^2+2x-1)}{(2x-1)^2}
\sim5(x-1)^2.
\]
Finally, the two tangential Floquet multipliers on the regular levels converge to \(\varphi^4\) and \(\varphi^{-4}\).

**Proof.** Sections 2–7 establish the assertions by direct algebra, differentiation of the invariant, and continuity of the restricted finite-dimensional linear maps. \(\square\)

## 9. Error correction record

The earlier matrix
\[
\begin{pmatrix}6&4&-2\\2&2&-1\\1&0&0\end{pmatrix}
\]
contains a differentiation error: the \((1,2)\) entry is \(4x^2-1=3\) at \(p_1\), not \(4\). The corrected matrix makes the geometric limiting normal \( (1,-3,1)\) a left eigenvector for eigenvalue \(1\). The previously suggested covector \((1,-4,3)\) belongs to the erroneous matrix and must not be retained.

The cubic Fricke-level asymptotic is also excluded by the exact expression in Section 6; the leading term is \(5(x-1)^2\).

## 10. Scope

All statements in this record concern the exact real trace map, its Fricke invariant, its period-two branch, and finite-dimensional linearization. No claim is made here about a further identification with a physical system, a continuum model, or a separate RGS/PSU construction.
