# Scalar spectrum of the Poincaré spherical space \(S^3/2I\)

**Status:** exact representation-theoretic derivation; computational cross-check supplied.  
**Scope:** scalar Laplacian, unit round metric on \(S^3\), quotient by the left action of the binary icosahedral group \(2I\) of order 120.

## 1. Group and Molien series

Let \(2I\subset SU(2)\) be the binary icosahedral group. Its invariant ring on the defining representation \(\mathbb C^2\) has Molien series
\[
M_{2I}(t)=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]
Write
\[
M_{2I}(t)=\sum_{k\geq 0} a_k t^k.
\]
Since \(\operatorname{Sym}^k(\mathbb C^2)\cong V_{k/2}\), the coefficient \(a_k\) is exactly
\[
a_k=\dim V_{k/2}^{2I}.
\]
No invariant series for \(I\subset SO(3)\) is used in this argument.

## 2. Harmonics on \(S^3\) and quotient multiplicities

Identify \(S^3\cong SU(2)\). Under \(SU(2)_L\times SU(2)_R\), the degree-\(k\) scalar spherical harmonics form
\[
\mathcal H_k\cong V_{k/2}\otimes V_{k/2},
\qquad \dim\mathcal H_k=(k+1)^2.
\]
For the left action of \(2I\), the invariant subspace is
\[
\mathcal H_k^{2I}\cong V_{k/2}^{2I}\otimes V_{k/2}.
\]
Consequently the multiplicity of the scalar Laplacian eigenvalue
\[
\lambda_k=k(k+2)
\]
on \(S^3/2I\) is
\[
\boxed{d_k=(k+1)a_k=(k+1)[t^k]M_{2I}(t).}
\]
This formula holds for every integer \(k\geq0\). In particular, it already gives zero for odd \(k\), because the central element \(-1\in2I\) acts as \((-1)^k\) on \(V_{k/2}\), so \(V_{k/2}^{2I}=0\) when \(k\) is odd.

The radial/harmonic decomposition is not an additional correction to this quotient formula: the representation \(\mathcal H_k\) is already the degree-\(k\) harmonic space.

## 3. Independent character formula

For an element of \(SU(2)\) with eigenvalues \(e^{\pm i\alpha}\), the spin-\(j\) character is
\[
\chi_j(\alpha)=\frac{\sin((2j+1)\alpha)}{\sin\alpha},
\]
with limiting values at \(\alpha=0,\pi\). Therefore
\[
\boxed{
a_k=\frac1{120}\sum_{[g]\subset2I}|[g]|\,
\chi_{k/2}(g).
}
\]
The reproducibility script records the nine conjugacy classes by their exact angles \(\alpha=\pi p/q\) and class sizes. It evaluates the character averages with exact SymPy algebraic expressions, then checks equality with the Molien coefficients degree by degree through \(k=120\).

## 4. Initial spectrum

The first nonzero terms are:

| \(k\) | \(\lambda_k=k(k+2)\) | \(a_k\) | \(d_k=(k+1)a_k\) |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 |
| 12 | 168 | 1 | 13 |
| 20 | 440 | 1 | 21 |
| 24 | 624 | 1 | 25 |
| 30 | 960 | 1 | 31 |
| 32 | 1088 | 1 | 33 |
| 36 | 1368 | 1 | 37 |
| 40 | 1680 | 1 | 41 |
| 42 | 1848 | 1 | 43 |
| 44 | 2024 | 1 | 45 |
| 48 | 2400 | 1 | 49 |
| 50 | 2600 | 1 | 51 |
| 52 | 2808 | 1 | 53 |
| 54 | 3024 | 1 | 55 |
| 56 | 3248 | 1 | 57 |
| 60 | 3720 | 2 | 122 |

Thus the first positive eigenvalue is
\[
\boxed{\lambda_1^+=168,\qquad d_1^+=13.}
\]
Here \(\lambda_1^+\) denotes the first positive eigenvalue, not the eigenvalue with index \(k=1\).

## 5. Corrections and exclusions

- The series \((1+t^{15})/((1-t^6)(1-t^{10}))\) is **not** used for the quotient \(S^3/2I\); it concerns a different icosahedral invariant problem.
- No substitution \(t\mapsto t^2\) is needed.
- The numerical identity \(6=2\cdot3\), \(10=2\cdot5\), \(15=3\cdot5\) is not asserted to establish a structural correspondence with Pellis Functions.
- This document establishes a scalar spectral multiplicity formula. It does not establish a physical interpretation or a connection to the fine-structure constant.

## 6. Reproduction

From the repository root, install SymPy and run:

    python -m pip install sympy
    python scripts/verify_2i_spectral_multiplicities.py

The script must print a PASS line confirming exact agreement of character averages and Molien coefficients through degree 120. The code is an independent finite-range check; the formula for all degrees follows from the representation-theoretic argument in Sections 1–3.
