# T121 — Icosahedral A5 action on Q6 and its exterior Clifford module

**Classification:** exact finite-group representation result. The six-axis action and the decomposition (6=3\oplus3') are constructed and checked exactly over \(\mathbb Q(\sqrt5)\) by `audits/t121_q6_a5_three_plus_three_prime.py`. This does not by itself establish a Pin lift, a Dirac operator, or physical dynamics.

## Geometric signed-axis action

Let \(\varphi=(1+\sqrt5)/2\). Use the twelve vertices
\[
\mathcal V=\{(0,\pm1,\pm\varphi),\ (\pm1,\pm\varphi,0),\ (\pm\varphi,0,\pm1)\}
\]
of a regular icosahedron, and choose the following six representatives of its antipodal axes:
\[
\begin{aligned}
a_1&=(0,1,\varphi),&a_2&=(1,\varphi,0),&a_3&=(\varphi,0,1),\\
a_4&=(0,1,-\varphi),&a_5&=(1,-\varphi,0),&a_6&=(\varphi,0,-1).
\end{aligned}
\]
The proper rotational symmetry group has order 60 and is isomorphic to \(A_5\). For each rotation \(R\), there are unique \(\sigma\in S_6\) and signs \(\epsilon_j\in\{\pm1\}\) such that
\[
Ra_j=\epsilon_j a_{\sigma(j)}.
\]
Define the signed-permutation representation by
\[
\rho_6(R)_{\sigma(j),j}=\epsilon_j.
\]
Thus \(\rho_6(R)\in O(6)\), and its action on Q6 bit strings copies a bit for a positive sign and complements it for a negative sign. The construction is a declared identification of the six axes with the six Q6 coordinates.

The exact audit reconstructs all 60 rotations from the icosahedral vertex Gram matrix, induces the 60 signed actions, and checks orthogonality and closure. The conjugacy-class sizes are \((1,15,20,12,12)\), and the six-dimensional character is
\[
\chi_6=(6,-2,0,1,1).
\]

## Exact decomposition into the two geometric tripletts

The two three-dimensional irreducible characters of \(A_5\), in the class order above, are
\[
\chi_3=(3,-1,0,\varphi,\varphi'),\qquad
\chi_{3'}=(3,-1,0,\varphi',\varphi),
\quad \varphi'=\frac{1-\sqrt5}{2}.
\]
Their central idempotents in this six-dimensional representation are
\[
P_3=\frac3{60}\sum_{g\in A_5}\chi_3(g^{-1})\rho_6(g),\qquad
P_{3'}=\frac3{60}\sum_{g\in A_5}\chi_{3'}(g^{-1})\rho_6(g).
\]
The exact sums simplify to
\[
P_3=\frac12I_6+\frac{\sqrt5}{10}B,\qquad
P_{3'}=\frac12I_6-\frac{\sqrt5}{10}B,
\]
where
\[
B=\begin{pmatrix}
0&1&1&-1&-1&-1\\
1&0&1&1&-1&1\\
1&1&0&-1&1&1\\
-1&1&-1&0&-1&1\\
-1&-1&1&-1&0&1\\
-1&1&1&1&1&0
\end{pmatrix},\qquad B^2=5I_6.
\]
Consequently, exactly,
\[
P_3^2=P_3,\quad P_{3'}^2=P_{3'},\quad
P_3P_{3'}=0,\quad P_3+P_{3'}=I_6,
\]
and
\[
\operatorname{rank}P_3=\operatorname{rank}P_{3'}=3.
\]
Both projectors commute with all 60 signed actions. The restricted characters are respectively \((3,-1,0,\varphi,\varphi')\) and \((3,-1,0,\varphi',\varphi)\). Hence
\[
\boxed{\mathbb R^6\cong V_3\oplus V_{3'},\qquad
V_3=\operatorname{im}P_3,\quad V_{3'}=\operatorname{im}P_{3'}.}
\]

**Reproducibility:** run `python audits/t121_q6_a5_three_plus_three_prime.py`. It uses SymPy exact algebraic arithmetic only (no floating-point rank or tolerance tests), reconstructs the icosahedral rotations and signed-axis action, computes the character projectors, and raises an exception if any check fails. The output includes the exact projector matrices, class sizes, restricted characters, and Boolean checks. The audit checks 60 distinct actions, orthogonality, closure, class sizes, both idempotents, mutual orthogonality, completeness, ranks, commutation, the closed form \(B^2=5I\), and the two restricted characters.

## Exterior Clifford module

Let \(V=\mathbb R^6\), \(\mathcal S=\Lambda^*V_\mathbb C\), so \(\dim_\mathbb C\mathcal S=64\). Define \(c(v)=\varepsilon(v)+\iota(v)\), with exterior multiplication and contraction. Their standard identities imply
\[
c(v)c(w)+c(w)c(v)=2\langle v,w\rangle I,
\]
so \(\mathcal S\) is a complex Euclidean Clifford module.

For any \(S\in O(6)\), the induced map \(\Lambda S=\bigoplus_k\Lambda^kS\) obeys
\[
(\Lambda S)c(v)(\Lambda S)^{-1}=c(Sv).
\]
This follows from naturality of exterior multiplication and the isometry covariance of contraction. Therefore each signed-axis transformation induces a Clifford-module automorphism, and these maps form a representation. The decomposition also induces the graded vector-space factorization
\[
\Lambda^*(V_3\oplus V_{3'})\cong
\Lambda^*V_3\otimes\Lambda^*V_{3'},
\qquad 64=8\cdot8.
\]
This factorization is not, by itself, a decomposition into two independent physical spin systems.

## Central distinction and scope

The Q6 signed-axis action is an \(A_5\) representation. Viewed as a representation of \(2I\), it factors through \(2I/\{\pm1\}\), so the central element \(-1\) acts trivially on Q6 and on the induced exterior module. In contrast, the defining two-dimensional representation in T119 sends \(-1\) to \(-I_2\). These are different central characters; an intertwiner between these spaces cannot be presumed. The decomposition \(3\oplus3'\) does not remove the central-character obstruction established separately in T123.

**Boundary:** this result does not construct a Pin lift of the Möbius transitions, a connection-compatible Dirac operator, torsion, a continuum limit, or physical QLG dynamics.
