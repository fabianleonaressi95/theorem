# T063 — Quaternionic realization of SU(2) and the double cover of SO(3)

**Status:** proved standard finite-dimensional Lie-group theorem, with the matrix and rotation conventions fixed below.  
**Scope:** unit Hamilton quaternions, their defining (2\times2) complex representation, and the active action on column vectors in \(\mathbb R^3\). This theorem formalizes the conventions implemented in the RGS–QLG Quaternion Bridge; it makes no additional physical claim.

## 1. Conventions

Write a quaternion in scalar-first order
\[
q=w+x\mathbf i+y\mathbf j+z\mathbf k,
\qquad
q^*=w-x\mathbf i-y\mathbf j-z\mathbf k.
\]
Let \(\mathbb H_1=\{q\in\mathbb H:|q|=1\}\). For \(q\in\mathbb H_1\), define
\[
U(q)=
\begin{pmatrix}
w-iz&-y-ix\\
y-ix&w+iz
\end{pmatrix}.
\]
Identify \(\operatorname{Im}\mathbb H\) with \(\mathbb R^3\) by
\((x,y,z)\leftrightarrow x\mathbf i+y\mathbf j+z\mathbf k\). The active rotation is
\[
\pi(q)v=qvq^{-1},\qquad v\in\operatorname{Im}\mathbb H.
\]

## 2. Theorem

The map
\[
U:\mathbb H_1\longrightarrow SU(2)
\]
is a group isomorphism. The conjugation action
\[
\pi:\mathbb H_1\longrightarrow SO(3)
\]
is a surjective group homomorphism with kernel \(\{1,-1\}\). Hence
\[
1\longrightarrow\{\pm1\}\longrightarrow SU(2)
\xrightarrow{\;\pi\;}SO(3)\longrightarrow1
\]
is exact and \(SU(2)\) is the two-sheeted universal cover of \(SO(3)\). In particular,
\[
\pi(q)=\pi(-q),\qquad
\pi(q_1q_2)=\pi(q_1)\pi(q_2).
\]

For \(q=(w,x,y,z)\in\mathbb H_1\), the rotation matrix in the stated active, column-vector convention is
\[
R(q)=
\begin{pmatrix}
1-2(y^2+z^2)&2(xy-wz)&2(xz+wy)\\
2(xy+wz)&1-2(x^2+z^2)&2(yz-wx)\\
2(xz-wy)&2(yz+wx)&1-2(x^2+y^2)
\end{pmatrix}\in SO(3).
\]
The composition is compatible with the matrix representation:
\[
U(q_1q_2)=U(q_1)U(q_2),\qquad
\pi(q)=R(q).
\]

## 3. Proof

### 3.1 The quaternion-to-SU(2) isomorphism

Since \(|q|^2=w^2+x^2+y^2+z^2=1\), direct multiplication gives
\[
U(q)^*U(q)=I_2,\qquad
\det U(q)=w^2+x^2+y^2+z^2=1.
\]
Thus \(U(q)\in SU(2)\).

The Hamilton product, using \(\mathbf i\mathbf j=\mathbf k\), \(\mathbf j\mathbf k=\mathbf i\), \(\mathbf k\mathbf i=\mathbf j\) and anticommutation of distinct imaginary units, gives
\[
U(q_1q_2)=U(q_1)U(q_2).
\]
Every matrix in \(SU(2)\) has the form
\[
\begin{pmatrix}a&b\\-\overline b&\overline a\end{pmatrix},
\qquad |a|^2+|b|^2=1.
\]
Writing \(a=w-iz\) and \(b=-y-ix\) uniquely recovers four real numbers with
\(w^2+x^2+y^2+z^2=1\). Therefore \(U\) is bijective as well as a homomorphism.

### 3.2 The conjugation action

For a unit quaternion, \(q^{-1}=q^*\). Conjugation preserves the pure-imaginary subspace and the quaternion norm. Its restriction to that three-dimensional real subspace is therefore orthogonal. The determinant is continuously equal to \(+1\), since \(\mathbb H_1\cong S^3\) is connected and the identity quaternion acts as the identity. Hence \(\pi(q)\in SO(3)\).

Expanding \(q(0,v)q^*\) with the Hamilton product yields the displayed matrix \(R(q)\). Associativity gives
\[
(q_1q_2)v(q_1q_2)^{-1}
=q_1(q_2vq_2^{-1})q_1^{-1},
\]
so \(\pi\) is a homomorphism.

If \(q\) lies in the kernel, it commutes with every pure imaginary quaternion. The center of \(\mathbb H\) is \(\mathbb R\), so \(q\) is real; unit norm then forces \(q=\pm1\). Conversely, both \(1\) and \(-1\) act trivially. Thus
\[
\ker\pi=\{\pm1\}.
\]

### 3.3 Surjectivity and the two lifts

Every element of \(SO(3)\) is a rotation about some unit axis \(n\in\mathbb R^3\) through an angle \(\theta\). Set
\[
q=\cos(\theta/2)+
(n_1\mathbf i+n_2\mathbf j+n_3\mathbf k)\sin(\theta/2).
\]
Direct substitution into the conjugation action gives that rotation. Thus \(\pi\) is surjective. Since its kernel has exactly two elements, every rotation has exactly the two lifts \(q\) and \(-q\).

Finally, \(S^3\) is simply connected, so this surjective local Lie-group homomorphism with discrete kernel is the universal double cover of \(SO(3)\). \(\square\)

## 4. Computational correspondence and verification boundary

The implementation correspondence is:
- `src/quaternions.py`: scalar-first Hamilton algebra, conjugation, norm and inverse;
- `src/rotations.py`: active \(SO(3)\) matrix and vector action;
- `src/su2_lifts.py`: \(U(q)\), inverse extraction, projection and lift diagnostics;
- `tests/test_quaternion_algebra.py`;
- `tests/test_su2_so3.py`.

These tests check finite numerical instances of the identities above. They do not replace the algebraic proof. The CI job named “Quaternion / SU2 / SO3 / QLG tests” first runs `compileall`; if compilation fails in any test module, the subsequent quaternion, SU(2)/SO(3), holonomy and full-suite steps have not run and must not be reported as failed mathematical tests.

## 5. Non-conclusions

This theorem establishes the standard quaternionic double cover and the stated implementation conventions. It does not prove a new physical spin law, identify a QLG fibre with a Lorentzian spinor bundle, select a chirality, or establish any RGS–PSU continuum limit. Those require additional hypotheses and separate theorems.
