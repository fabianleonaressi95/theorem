# T032 — Fixed harmonic-basis matrix for the Rumin middle differential

**Status:** the generic Case V multiplicity-space matrix is reconstructed from the exact coefficient data recorded in T025. Its Gram matrix is proved algebraically below. The repository audit script is supplied but has **not yet been executed in this session**. The result is not a new global nine-irrep spectral theorem.

## 1. Purpose and relation to earlier results

T025 determines the generic middle-degree block of the Rumin operator through Kitaoka's Case V coefficients. T029 records its Gram matrix, and the separate polar-factorization contribution T030 constructs a positive square root of that Gram matrix. A positive square root is an endomorphism of the source multiplicity space; it is not, by itself, the geometric differential into the target multiplicity space.

Here the source and target multiplicity spaces are fixed explicitly. The target is the one-dimensional positive-output line in the generic block. This fixes the geometric matrix up to the unavoidable phase of the target basis.

## 2. Exact coefficients

Let (p,q\geq1), and put
[
L=2pq+p+q,qquad
A^2=\frac{p(q+1)}2,qquad
B^2=\frac{q(p+1)}2,qquad
S=A^2+B^2=\frac L2.
]
Take (A,B>0). In Kitaoka's Case V coefficient convention, let
[
C=\frac{p-q}{2},qquad
A'=C-2A^2,qquad B'=C+2B^2.
]
Direct simplification gives
[
A'=-\frac L2,qquad B'=\frac L2.
]

Choose the orthonormal source multiplicity basis ((e_1,e_2)) in the order used by the two coefficients (A'B) and (B'A), and choose the target unit vector (f) by the real-positive output convention. The middle differential on this multiplicity block is the row matrix
[
\boxed{
[D_{p,q}]_{f\leftarrow(e_1,e_2)}
=\frac1{\sqrt S}(A'B,\ B'A)
=\frac{L}{2\sqrt S}(-B,\ A).
}
]
Since (S=L/2), this can also be written
[
D_{p,q}=\sqrt{\frac L2}\,(-B,\ A).
]
The last expression is a (1\times2) matrix. Its target is a line, not a second copy of the source plane.

The full generic block carries the common (SU(2))-type (V_{p+q}\cong\operatorname{Sym}^{p+q}(\mathbb C^2)), so the corresponding map is
[
D_{p,q}\otimes I_{V_{p+q}}:
\mathbb C^2\otimes V_{p+q}
\longrightarrow
\mathbb C\otimes V_{p+q}.
]
This is the multiplicity-space realization; it does not assert that the full global harmonic decomposition has only one such block.

## 3. Gram identity

Taking the Hermitian adjoint,
[
D_{p,q}^*D_{p,q}
=\frac{L^2}{4S}
\begin{pmatrix}
B^2&-AB\\
-AB&A^2
\end{pmatrix}
=\frac L2
\begin{pmatrix}
B^2&-AB\\
-AB&A^2
\end{pmatrix}.
]
This is exactly the T029 Gram matrix. Its eigenvalues are (0) and (L^2/4), because
[
\begin{pmatrix}B^2&-AB\\-AB&A^2\end{pmatrix}
\begin{pmatrix}A\\B\end{pmatrix}=0,
quad
\begin{pmatrix}B^2&-AB\\-AB&A^2\end{pmatrix}
\begin{pmatrix}-B\\A\end{pmatrix}
=S\begin{pmatrix}-B\\A\end{pmatrix}.
]
Thus
[
\ker D_{p,q}=\mathbb C(A,B),qquad
\operatorname{im}D_{p,q}=\mathbb C f,
qquad
\|D_{p,q}\|=L/2.
]
The positive singular value is (L/2), with the (V_{p+q}) multiplicity carried unchanged.

## 4. What the target phase means

Replacing (f) by (e^{i\vartheta}f) changes the row to (e^{-i\vartheta}D_{p,q}), depending on the coordinate convention for target components. It leaves (D^*D) unchanged. This is the ordinary (U(1)) freedom of a unit vector in a one-dimensional target. There is no independent (U(2)) target rotation in this fixed multiplicity model.

The positive square root (G^{1/2}=(L/2)P_+) from the polar-factorization note is a canonical positive operator on the two-dimensional source space. It is not the (1\times2) Rumin differential above. Both have the same nonzero singular value and encode the same Gram operator, but they have different source/target types.

## 5. (2I)-equivariance

The binary icosahedral group acts on the common (V_{p+q}) factor. The multiplicity row (D_{p,q}) acts trivially on that factor. Consequently, for every representation matrix (pi_{p+q}(g)),
[
(D_{p,q}\otimes I) (I_2\otimes\pi_{p+q}(g))
=(1\otimes\pi_{p+q}(g))(D_{p,q}\otimes I).
]
For any central isotypic projector (P_\rho) on (V_{p+q}), the same identity holds with (P_\rho) in place of (pi_{p+q}(g)). This is the explicit multiplicity-space form of the abstract equivariance already established in T031.

This argument does not provide all nine irreducible matrix models or their character table; those remain a separate finite-representation task.

## 6. Scope and status ledger

**Established algebraically from the T025 Case V coefficients**
- (A'=-L/2), (B'=L/2), and (S=L/2).
- The fixed-basis row (D_{p,q}=L(-B,A)/(2\sqrt S)).
- The identity (D_{p,q}^*D_{p,q}=G_{p,q}) with the T029 Gram matrix.
- The one-dimensional target phase freedom and the common (V_{p+q}) factor.
- Equivariance of this multiplicity row on the common representation factor.

**Not claimed**
- An independent derivation of Kitaoka's Case V coefficients from scratch; T025 is the cited source reduction.
- A new computation of the full Rumin spectrum on (S^3/2I).
- Explicit matrices for all nine irreducible representations of (2I).
- Any Q6/PRISM continuum limit or physical consequence.

**Validation status:** `audits/t032_rumin_fixed_harmonic_matrix.py` is an exact SymPy audit intended to check the identities over a configurable rectangle. It has been added but was not run in this session.

## References

1. A. Kitaoka, *Analytic torsions associated with the Rumin complex on contact spheres*, arXiv:1911.03092, §1.1 and §2.3, Case V.
2. Repository T025, *Exact Rumin middle-degree blocks on (S^3/2I)*.
3. Repository T029, *Rumin Gram matrices for the binary icosahedral twists*.
4. Repository T030, *Polar factorization and target-gauge ambiguity of the Rumin middle block* (work branch).
5. Repository T031, *Equivariance of the 3D Rumin complex under the binary icosahedral action*.
