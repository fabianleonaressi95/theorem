# McKay correspondence for the binary icosahedral group

**Status:** exact representation-theoretic result; the accompanying finite computation is a consistency check, not the proof of the McKay correspondence.

## 1. The affine E8 McKay graph

Let (G=2I\subset SU(2)) be the binary icosahedral group, of order 120, and let (U\cong\mathbb C^2) be the defining representation. The McKay graph has one vertex for each irreducible complex representation \(\rho_i\) of (G\); the multiplicity of \(\rho_j\) in \(U\otimes\rho_i\) is the number of edges from (i) to (j\).

For (2I\), this graph is the affine Dynkin diagram \(\widetilde E_8\). The following labeling fixes the convention used here:

| Vertex | Dimension | Adjacent vertices |
|---|---:|---|
| \(\rho_0\) (trivial) | 1 | \(\rho_1\) |
| \(\rho_1\) (defining \(U\)) | 2 | \(\rho_0,\rho_2\) |
| \(\rho_2\) | 3 | \(\rho_1,\rho_3\) |
| \(\rho_3\) | 4 | \(\rho_2,\rho_4\) |
| \(\rho_4\) | 5 | \(\rho_3,\rho_5\) |
| \(\rho_5\) | 6 | \(\rho_4,\rho_6,\rho_8\) |
| \(\rho_6\) | 4 | \(\rho_5,\rho_7\) |
| \(\rho_7\) | 2 | \(\rho_6\) |
| \(\rho_8\) | 3 | \(\rho_5\) |

Thus the dimension vector in this vertex order is
\[
\delta=(1,2,3,4,5,6,4,2,3).
\]
It obeys \(A\delta=2\delta\), where \(A\) is the adjacency matrix. Also
\[
\sum_i(\dim\rho_i)^2=120=|2I|,
\]
as required by the regular representation dimension identity.

Equivalently, the tensor products with the defining representation are
\[
\begin{aligned}
U\otimes\rho_0&=\rho_1, &
U\otimes\rho_1&=\rho_0\oplus\rho_2,\\
U\otimes\rho_2&=\rho_1\oplus\rho_3, &
U\otimes\rho_3&=\rho_2\oplus\rho_4,\\
U\otimes\rho_4&=\rho_3\oplus\rho_5, &
U\otimes\rho_5&=\rho_4\oplus\rho_6\oplus\rho_8,\\
U\otimes\rho_6&=\rho_5\oplus\rho_7, &
U\otimes\rho_7&=\rho_6,\\
U\otimes\rho_8&=\rho_5.
\end{aligned}
\]

The vertex labels \(\rho_i\) are local bookkeeping labels; only \(\rho_0\) and \(\rho_1=U\) are singled out canonically here.

## 2. Recurrence for restricted SU(2) representations

Write \(V_n=\operatorname{Sym}^n(U)\), the irreducible \(SU(2)\)-representation of dimension \(n+1\). The Clebsch–Gordan identity
\[
U\otimes V_n\cong V_{n+1}\oplus V_{n-1}\qquad(n\geq1)
\]
gives, after restriction to \(2I\), a recurrence for the multiplicity vector \(m_n\) of the nine irreducibles:
\[
m_0=e_0,\qquad m_1=e_1,\qquad
m_{n+1}=A m_n-m_{n-1}.
\]
In particular, the trivial-representation multiplicity is
\[
a_n=\dim(V_n^{2I})=(m_n)_0.
\]

This is an independent exact-integer route to the invariant dimensions. It uses the McKay graph and the SU(2) tensor-product recurrence, rather than evaluating conjugacy-class characters degree by degree.

## 3. Molien comparison

For the binary icosahedral action on \(\mathbb C^2\), the Molien series is
\[
M_{2I}(t)=\sum_{n\geq0}a_nt^n
=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]
The coefficient can be computed without symbolic algebra:
\[
a_n=\#\{(r,s,\epsilon)\in\mathbb Z_{\geq0}^2\times\{0,1\}:
12r+20s+30\epsilon=n\}.
\]
The accompanying script compares the McKay recurrence with this coefficient formula for every degree \(0\leq n\leq120\). This finite check validates the implementation and the chosen graph convention over that range; the general equality follows from the representation-theoretic McKay correspondence and Molien's theorem, not from a finite-range test alone.

## 4. Scalar spectrum on \(S^3/2I\)

For the round unit 3-sphere, scalar harmonics of degree \(n\) have
\[
\mathcal H_n\cong V_n\otimes V_n^*,\qquad
\lambda_n=n(n+2),\qquad
\dim\mathcal H_n=(n+1)^2.
\]
For the quotient by the left action of \(2I\), the invariant subspace has dimension
\[
d_n=\dim(\mathcal H_n^{2I})=(n+1)a_n.
\]
Since the central element \(-1\in2I\) acts on \(V_n\) by \((-1)^n\), one has \(a_n=d_n=0\) for odd \(n\).

The first positive invariant degree is \(n=12\), hence
\[
\lambda_1^{\mathrm{quot}}=12(12+2)=168,\qquad d_{12}=13.
\]
This is a statement about scalar Laplace eigenvalues for the unit-radius round spherical quotient. It does not by itself imply a physical frequency, a PSU scale identification, or a Pellis-exponent correspondence.

## 5. Scope and exclusions

- The affine \(\widetilde E_8\) graph is a representation-theoretic structure of \(2I\); it is not an additional geometric cell complex on the quotient.
- The recurrence computes invariant dimensions. It does not replace the geometric definition of the Laplacian or establish spectra for other operators.
- No numerical relation to \(\varphi\), the supergolden constant, or Pellis coefficients is asserted here.
- The finite script check is labeled a computational verification, not a proof of a new theorem.
