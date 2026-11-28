# T165 — Quaternionic rotations and biquaternionic Lorentzian spin lift

**Status:** exact finite-dimensional representation theorem; global lattice connection and field equations remain OPEN.

## 1. Hermitian quaternion/Pauli representation of Minkowski vectors

Represent (x=(t,x_1,x_2,x_3)) by the Hermitian matrix
[
X(x)=tI_2+x_1\sigma_1+x_2\sigma_2+x_3\sigma_3
=\begin{pmatrix}
t+x_3&x_1-i x_2\\
x_1+i x_2&t-x_3
\end{pmatrix}.
]
Then
[
\det X(x)=t^2-x_1^2-x_2^2-x_3^2=x^T\eta x,
\quad \eta=\operatorname{diag}(1,-1,-1,-1).
]

## 2. Spin action

For (A\in SL(2,\mathbb C)), define
[
X\longmapsto X'=AXA^\dagger.
]
The result remains Hermitian and
[
\det X'=\det(A)\det(X)\det(A^\dagger)=\det X.
]
Thus the induced real-linear map (\Lambda(A)) satisfies
[
\Lambda(A)^T\eta\Lambda(A)=\eta.
]
The identity component is obtained for the connected (SL(2,\mathbb C)) action, giving the standard double cover
[
Spin^+(1,3)\simeq SL(2,\mathbb C)\to SO^+(1,3).
]
Since (A) and (-A) induce the same (\Lambda), the kernel is ({\pm I_2}).

## 3. Quaternionic rotation sector

A unit Hamilton quaternion (q=(w,x,y,z)) is represented by
[
U(q)=\begin{pmatrix}
w-iz&-y-ix\\
y-ix&w+iz
\end{pmatrix}\in SU(2).
]
It is a subgroup of (SL(2,\mathbb C)) and induces a purely spatial rotation. For the T164 junction element
[
q_*=(1+i+j+k)/2,
]
the vector rotation is (120^\circ), cyclically permuting the three imaginary quaternion axes. The spin lift has (U(q_*)^3=-I_2), as recorded in T164.

## 4. Boost sector

For a unit spatial direction (n\in\mathbb R^3) and rapidity (\chi\), let
[
A_B(n,\chi)=\exp\left(\frac\chi2 n\cdot\sigma\right)
=\cosh(\chi/2)I_2+\sinh(\chi/2)n\cdot\sigma.
]
Since ((n\cdot\sigma)^2=I_2), this matrix is Hermitian, has determinant one, and induces a Lorentz boost of rapidity (\chi). A combined rotation and boost is
[
A=A_B(n,\chi)U(q_*)\in SL(2,\mathbb C).
]
This gives an explicit Lorentzian extension of the compact quaternionic junction transport. In biquaternion language, the boost coefficients are complexified relative to the real quaternionic rotation subgroup.

## 5. Numerical audit

The companion implementation is:
- `src/lorentzian_biquaternion_lift.py`
- `tests/test_lorentzian_biquaternion_lift.py`

For the manufactured test (\chi=0.73), (n=(1,-2,0.5)/\| (1,-2,0.5)\|), the independent calculation gives:
- (SL(2,\mathbb C)) determinant error below (3\times10^{-16});
- Lorentz metric residual below (9\times10^{-16});
- Lorentz determinant equal to one to floating-point precision;
- Minkowski norm residual below (3\times10^{-15});
- (A) and (-A) induce identical Lorentz transformations.

These are representation checks, not a physical fit or continuum convergence result.

## 6. Interface to Cartan geometry

The result supplies the correct group-valued carrier for Lorentzian spin transport. On each oriented Q6 interface one may now seek (A_{vw}\in SL(2,\mathbb C)), with vector transport (\Lambda(A_{vw})\in SO^+(1,3)), and enforce
[
A_{wv}=A_{vw}^{-1},\qquad
A_{vw}\mapsto S_vA_{vw}S_w^{-1}.
]
The associated Lorentzian coframe remains independent. Discrete torsion and curvature must still be computed from the coframe and the (SL(2,\mathbb C)) holonomies; they are not determined by the spin lift alone.

The quaternionic junction is therefore the compact rotational part; the (SL(2,\mathbb C)) extension adds boosts. The PSU–Anti-Twin sheet exchange remains a separate tensor factor.

## 7. Evidence classification

- **PROVED EXACTLY:** determinant/Minkowski norm identity; (SL(2,\mathbb C)) action preserves the Lorentz metric; kernel ({\pm I}); unit quaternions embed as spatial rotations; Hermitian exponentials generate boosts.
- **NUMERICALLY AUDITED:** implemented rotation, boost and combined lifts for manufactured data.
- **OPEN:** global (SL(2,\mathbb C)) link assignment on the resolved Q6 complex; compatibility with the independent Cartan coframe; global spin structure; PSU–Anti-Twin throat matching; field equations, refinement and Sakharov limit.
