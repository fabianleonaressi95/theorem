# T015 — Clifford algebra and exact free spectrum on Q6

**Status:** Exact finite-dimensional spectral result for a specified graph operator. It is not a continuum Dirac operator and does not establish a QCD fermion discretization.

## 1. Q6 translations and characters

Identify the six-cube graph with the group \(\mathbb Z_2^6\). For \(x=(x_1,\ldots,x_6)\), let \(T_i f(x)=f(x+e_i)\). Then
\[
T_i^2=I,\qquad T_i^{-1}=T_i.
\]
The 64 characters
\[
\chi_k(x)=(-1)^{k\cdot x},\quad k\in\mathbb Z_2^6
\]
form an orthogonal basis and satisfy \(T_i\chi_k=(-1)^{k_i}\chi_k\).

**Immediate obstruction.** The usual centered first difference vanishes identically:
\[
\frac{T_i-T_i^{-1}}2=0.
\]
Thus Q6, viewed literally as a \(\mathbb Z_2^6\) Cayley graph, has no nonzero centered derivative. A continuum-like momentum derivative cannot be imported without changing the graph or adding extra structure.

## 2. Six Euclidean Clifford matrices

Let \(X,Y,Z\) be the Pauli matrices. On \((\mathbb C^2)^{\otimes3}\cong\mathbb C^8\), define
\[
\begin{aligned}
\Gamma_1&=X\otimes I\otimes I,&
\Gamma_2&=Y\otimes I\otimes I,\\
\Gamma_3&=Z\otimes X\otimes I,&
\Gamma_4&=Z\otimes Y\otimes I,\\
\Gamma_5&=Z\otimes Z\otimes X,&
\Gamma_6&=Z\otimes Z\otimes Y.
\end{aligned}
\]
They are Hermitian and satisfy
\[
\Gamma_i\Gamma_j+\Gamma_j\Gamma_i=2\delta_{ij}I_8.
\]
This is an explicit irreducible complex spin representation in six Euclidean dimensions.

## 3. A precisely defined forward graph-Clifford operator

Define, on vertex-spinors \(\psi:Q_6\to\mathbb C^8\),
\[
D_+=\sum_{i=1}^6\Gamma_i(T_i-I).
\]
This is a well-defined Hermitian operator on the finite graph Hilbert space with counting measure. It is a forward-difference Clifford operator, not the conventional anti-Hermitian continuum Dirac operator.

On character sector \(k\), put \(m=|k|\). Then
\[
D_+(k)=\sum_i\Gamma_i\big((-1)^{k_i}-1\big)
=-2\sum_{i:k_i=1}\Gamma_i.
\]
By the Clifford relations,
\[
D_+(k)^2=4m I_8.
\]
For \(m>0\), the trace is zero, so the eigenvalues are \(+2\sqrt m\) and \(-2\sqrt m\), each with multiplicity four. For \(m=0\), all eight eigenvalues are zero.

## 4. Exact spectrum and multiplicities

There are \(\binom6m\) characters of Hamming weight \(m\). Therefore:

| Hamming weight m | Character count | Eigenvalues in spin sector | Multiplicity of each sign, including color |
|---:|---:|---:|---:|
| 0 | 1 | 0 (×8) | zero multiplicity 24 after color |
| 1 | 6 | ±2 | 72 each |
| 2 | 15 | ±2√2 | 180 each |
| 3 | 20 | ±2√3 | 240 each |
| 4 | 15 | ±4 | 180 each |
| 5 | 6 | ±2√5 | 72 each |
| 6 | 1 | ±2√6 | 12 each |

The last column uses three independent color components. The full Hilbert space has dimension \(64\cdot8\cdot3=1536\); the zero eigenspace has dimension 24 and the nonzero eigenspaces together have dimension 1512.

**Proof.** For fixed k, set \(A_k=\sum_{i:k_i=1}\Gamma_i\). Anticommutation gives \(A_k^2=mI_8\), hence eigenvalues have absolute value \(\sqrt m\). For m>0, conjugation by any \(\Gamma_j\) with \(k_j=0\) anticommutes with \(A_k\), so the spectrum is symmetric about zero. Such a j exists for m<6. For m=6, the product/chirality operator \(\Gamma_*=i^3\Gamma_1\cdots\Gamma_6\) anticommutes with every \(\Gamma_i\), hence with A_k, giving the same symmetry. Since the spin dimension is eight and no zero eigenvalue occurs when m>0, each sign has multiplicity four. Multiplying by \(\binom6m\) characters and three colors gives the table. □

## 5. Gauge covariance

Replace each edge translation by a color-parallel transport:
\[
(D_U\psi)(x)=\sum_i\Gamma_i\big(U_i(x)\psi(x+e_i)-\psi(x)\big),
\]
where \(U_i(x)\in SU(3)_C\) and
\[
U_i(x)\mapsto g(x)U_i(x)g(x+e_i)^{-1},\quad
\psi(x)\mapsto g(x)\psi(x).
\]
The edge-by-edge calculation in T014 gives \(D_{U^g}(g\psi)=gD_U\psi\). T015's free spectrum is the special case \(U_i(x)=I_3\).

## 6. What this audit tells us about doublers

The centered derivative on Q6 is identically zero, so the conventional naive-fermion doubling analysis is not even defined for that choice. The forward operator \(D_+\) has exactly one zero character sector (k=0), but this fact alone does **not** prove absence of physical doublers: the graph has no continuum momentum torus, no scaling parameter, and no established Dirac symbol near a continuum limit.

A Wilson term cannot be declared successful by inspection. It must be defined with a consistent adjoint convention, and its full spectrum and target low-energy sector must be checked. In particular, adding a scalar graph Laplacian changes eigenvalues and may create accidental zero crossings for particular parameters.

## 7. Reproducible finite audit recipe

The result can be reproduced without numerical diagonalization:
1. enumerate the 64 binary vectors k;
2. group them by Hamming weight m;
3. use \(D_+(k)^2=4mI_8\);
4. use Clifford anticommutation to pair positive and negative eigenvalues;
5. multiply degeneracies by \(\binom6m\) and color multiplicity three.

A numerical implementation should additionally construct the 8×8 matrices above and verify maximum residuals for \(\Gamma_i^\dagger-\Gamma_i\), \(\{\Gamma_i,\Gamma_j\}-2\delta_{ij}I\), and the predicted eigenvalue multiset.

## 8. Classification and next step

- **Exact:** Clifford relations, character decomposition, centered-difference obstruction, and the spectrum/multiplicities of the explicitly defined \(D_+\).
- **Conditional:** gauge covariance of the link-coupled version, under the transformation law in §5.
- **Open:** a physically suitable Q6 Dirac operator, chirality, fermion doubling in a continuum sense, anomaly matching, fermion determinant, and continuum/QCD limit.

The next mathematically meaningful step is to compare alternative graph discretizations (forward, Wilson-like, staggered/Kähler-Dirac) against explicit criteria, rather than calling this finite spectrum a QCD spectrum.
