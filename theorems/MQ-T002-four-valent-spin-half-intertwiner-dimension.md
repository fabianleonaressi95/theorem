# MQ-T002 — Dimension of the four-valent spin-1/2 intertwiner space

**Status:** proved analytically.

## Statement

For the fundamental irreducible representation \(V_{1/2}\) of SU(2),
\[
\dim\operatorname{Inv}_{SU(2)}(V_{1/2}^{\otimes4})=2.
\]

## Proof

By Clebsch–Gordan,
\[
V_{1/2}\otimes V_{1/2}=V_0\oplus V_1.
\]
Thus
\[
V_{1/2}^{\otimes4}
\cong(V_0\oplus V_1)\otimes(V_0\oplus V_1).
\]
The trivial representation occurs once in \(V_0\otimes V_0\), once in
\(V_1\otimes V_1\), and not in the two mixed products. Its multiplicity is
therefore exactly two. \(\square\)

## Explicit representatives

With \(|s\rangle=(|01\rangle-|10\rangle)/\sqrt2\) and the standard
triplet basis,
\[
|0_L\rangle=|s\rangle_{12}|s\rangle_{34},
\]
\[
|1_L\rangle=
\bigl(|t_+\rangle_{12}|t_-\rangle_{34}
-|t_0\rangle_{12}|t_0\rangle_{34}
+|t_-\rangle_{12}|t_+\rangle_{34}\bigr)/\sqrt3.
\]
These form an orthonormal basis of the invariant subspace.

## Evidence

The proof is exact and representation-theoretic. The explicit 16-component
basis vectors, total-generator residuals, and pairwise-flux matrices are
independently checked by scripts/audit_mq002_mq003.py.
