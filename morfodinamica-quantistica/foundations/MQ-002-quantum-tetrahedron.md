# MQ-002 — Four-valent spin-1/2 quantum tetrahedron

## Scope

Let each of four legs carry the fundamental irreducible representation
\(V_{1/2}\cong\mathbb C^2\) of \(SU(2)\). The quantum-tetrahedron
intertwiner space is
\[
\mathcal I_{1/2}^{(4)}
=\operatorname{Inv}_{SU(2)}(V_{1/2}^{\otimes4}).
\]

This note establishes its exact dimension, gives an orthonormal basis, and records the pairwise-flux operators used to probe its shape degrees of freedom.

## Exact decomposition

The Clebsch–Gordan rule gives
\[
V_{1/2}\otimes V_{1/2}=V_0\oplus V_1.
\]
Regrouping the four factors into pairs,
\[
V_{1/2}^{\otimes4}
\cong (V_0\oplus V_1)\otimes(V_0\oplus V_1).
\]
A total-spin-zero representation occurs once in \(V_0\otimes V_0\), and once
in \(V_1\otimes V_1\). It does not occur in \(V_0\otimes V_1\) or
\(V_1\otimes V_0\). Therefore
\[
\boxed{\dim\mathcal I_{1/2}^{(4)}=2.}
\]

This is an exact representation-theoretic result, not a numerical estimate.

## Explicit orthonormal basis

Use the computational ordering \(|0000\rangle,\ldots,|1111\rangle\).
For a pair of qubits define
\[
|s\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2},\quad
|t_+\rangle=|00\rangle,\quad
|t_0\rangle=\frac{|01\rangle+|10\rangle}{\sqrt2},\quad
|t_-\rangle=|11\rangle.
\]
An orthonormal invariant basis is
\[
|0_L\rangle=|s\rangle_{12}|s\rangle_{34},
\]
\[
|1_L\rangle=
\frac{|t_+\rangle_{12}|t_-\rangle_{34}
-|t_0\rangle_{12}|t_0\rangle_{34}
+|t_-\rangle_{12}|t_+\rangle_{34}}{\sqrt3}.
\]
Each basis vector is annihilated by the total generators
\[
\mathbf J_{\rm tot}=\sum_{k=1}^4\mathbf J^{(k)}.
\]

## Pairwise flux operators

With \(\mathbf J^{(k)}=\boldsymbol\sigma^{(k)}/2\), define
\[
Q_{km}=\mathbf J^{(k)}\cdot\mathbf J^{(m)}.
\]
In the ordered basis \((|0_L\rangle,|1_L\rangle)\), the exact matrices are
\[
Q_{12}=Q_{34}=
\begin{pmatrix}-3/4&0\\0&1/4\end{pmatrix},
\]
\[
Q_{13}=Q_{24}=
\begin{pmatrix}0&-\sqrt3/4\\-\sqrt3/4&-1/2\end{pmatrix},
\quad
Q_{14}=Q_{23}=
\begin{pmatrix}0&\sqrt3/4\\\sqrt3/4&-1/2\end{pmatrix}.
\]
They satisfy
\[
\sum_{m\ne k}Q_{km}=-\frac34 I_2,
\]
which is the pairwise form of closure on the invariant subspace. The different
shape operators do not all commute; a quantum tetrahedron therefore does
not have a simultaneously sharp assignment of all dihedral angles.

For equal spins \(j=1/2\), a normalized angle-cosine operator can be written
\[
\widehat{\cos\theta_{km}}
=\frac{\mathbf J^{(k)}\cdot\mathbf J^{(m)}}
{\sqrt{j(j+1)j(j+1)}}=\frac43Q_{km},
\]
subject to the operator-ordering and angle-convention choices of the model.

## Geometric interpretation and limits

The invariant condition
\[
\left(\sum_{k=1}^4\mathbf J^{(k)}\right)|\iota\rangle=0
\]
is the quantum closure condition. In the classical flux interpretation, four
oriented face-area vectors close to form a tetrahedron. For non-degenerate
classical data, the closure vectors determine a convex tetrahedron up to
translation under the usual reconstruction hypotheses.

At \(j=1/2\), quantum fluctuations are large. The two-dimensional intertwiner
space is a minimal quantum shape space; it should not be described as a
classical tetrahedron with four simultaneously definite face normals.

## Reproducibility

Run the script at scripts/audit_mq002_mq003.py. The audit checks basis
orthonormality, total-spin annihilation, the exact pair-operator matrices,
and the closure identities. Regression tests are in tests/test_mq002_mq003.py.

## Source

K. Li et al., “Quantum spacetime on a quantum simulator,” *Communications
Physics* 2, 122 (2019), DOI:
[10.1038/s42005-019-0218-5](https://doi.org/10.1038/s42005-019-0218-5).
The paper experimentally prepares four-qubit SU(2)-invariant tensors with
reported fidelities above 95% and measures geometric observables. That
experimental result is a benchmark, not a proof of the present RGS–QLG bridge.
