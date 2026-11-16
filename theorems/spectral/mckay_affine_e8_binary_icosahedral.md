# McKay correspondence for the binary icosahedral group

**Status:** classical representation-theoretic structure, stated separately from the scalar spectral calculation. The accompanying program is a finite consistency check, not a proof of McKay's correspondence or Molien's theorem.

## 1. The affine E8 McKay graph

Let (G=2I\subset SU(2)) be the binary icosahedral group, of order 120, and let (U\cong\mathbb C^2) be its defining representation. The McKay graph has one vertex for each irreducible complex representation \(\rho_i\) of \(G\); the multiplicity of \(\rho_j\) in \(U\otimes\rho_i\) is the adjacency multiplicity.

For \(2I\), this graph is the affine Dynkin diagram \(\widetilde E_8\). The following labels fix the convention used here:

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

The dimension vector in this vertex order is
\[
\delta=(1,2,3,4,5,6,4,2,3),\qquad A\delta=2\delta,
\]
where \(A\) is the adjacency matrix. Moreover,
\[
\sum_i(\dim\rho_i)^2=120=|2I|.
\]
The affine graph is a representation-theoretic object attached to \(2I\). Removing the affine vertex gives the finite Dynkin diagram \(E_8\).

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
The labels \(\rho_i\) are bookkeeping labels for this chosen graph ordering; only the trivial representation and the defining representation are singled out canonically in the notation.

## 2. Precisely defined McKay recurrence

For each integer \(r\geq0\), let
\[
W_r=\operatorname{Sym}^r(U),
\]
and define the nine-component column vector \(m_r\) by
\[
W_r\big|_{2I}\cong\bigoplus_{i=0}^{8}(m_r)_i\rho_i.
\]
Thus \((m_r)_i\) is the multiplicity of \(\rho_i\) in the restriction of \(\operatorname{Sym}^r(U)\) to \(2I\); in particular, \((m_r)_0\) is the multiplicity of the trivial representation.

Let \(e_i\) denote the standard basis vector for vertex \(i\). The initial conditions are
\[
m_0=e_0,\qquad m_1=e_1.
\]
The SU(2) Clebsch–Gordan identity
\[
U\otimes W_r\cong W_{r+1}\oplus W_{r-1}\qquad(r\geq1)
\]
restricts to \(2I\). By the definition of the McKay adjacency matrix,
\[
U\otimes\rho_i\cong\bigoplus_j A_{ij}\rho_j.
\]
Consequently, with the above column-vector convention and symmetric adjacency matrix,
\[
\boxed{m_{r+1}=A m_r-m_{r-1}\quad(r\geq1).}
\]
Set
\[
a_r=(m_r)_0=\dim\bigl(\operatorname{Sym}^r(U)^{2I}\bigr).
\]
This defines the index unambiguously: \(r\) is polynomial degree, and \(a_r\) is the coefficient of \(t^r\) in the Molien series.

## 3. Molien–Klein series and the finite check

For the binary icosahedral action on \(\mathbb C^2\), the Molien–Klein series is
\[
M_{2I}(t)=\sum_{r\geq0}a_rt^r
=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]
Equivalently,
\[
a_r=\#\{(p,q,\epsilon)\in\mathbb Z_{\geq0}^2\times\{0,1\}:
12p+20q+30\epsilon=r\}.
\]
This theorem gives the invariant multiplicities in every degree. The script only checks agreement of two computational routes over a finite range; it does not establish the all-degree identity.

For the run through polynomial degrees \(0\leq r\leq120\), there are 121 coefficient comparisons: 61 even degrees and 60 odd degrees. The odd-degree coefficients vanish because the central element \(-I\in2I\) acts on \(\operatorname{Sym}^r(U)\) as \((-1)^r\). The report therefore separates the 61 even-degree recurrence/Molien comparisons from the 60 odd-degree parity checks; the total 121 must not be interpreted as 121 nontrivial even-degree tests.

## 4. Scalar spectrum on the unit round \(S^3/2I\)

Let \(k\) denote the spherical-harmonic degree on the unit-radius round 3-sphere. The scalar harmonic space satisfies
\[
\mathcal H_k\cong V_{k/2}\otimes V_{k/2}^{*},
\qquad
\lambda_k=k(k+2),
\qquad
\dim\mathcal H_k=(k+1)^2,
\]
where \(V_j\) is the irreducible SU(2) representation of spin \(j\), so \(V_{k/2}=\operatorname{Sym}^{k}(U)\) has dimension \(k+1\). The eigenvalue is for the positive scalar Laplace–Beltrami operator on the round sphere of radius 1; for radius \(R\), it is \(k(k+2)/R^2\).

For the quotient by the left action of \(2I\), define the spin-indexed invariant multiplicity
\[
n_j:=\dim(V_j^{2I})=a_{2j}.
\]
Then, for even spherical degree \(k=2j\),
\[
\boxed{d_k=\dim(\mathcal H_k^{2I})=(k+1)n_{k/2}
=(k+1)a_k.}
\]
For odd \(k\), \(-I\in2I\) acts on the left factor \(V_{k/2}\) as \((-1)^k=-1\), so there are no invariant vectors and \(d_k=0\). This is a representation-theoretic parity argument, not merely a numerical observation.

The first positive Molien degree is \(k=12\), equivalently spin \(j=6\), with \(a_{12}=n_6=1\). Therefore
\[
\lambda_{12}=12(12+2)=168,\qquad d_{12}=13.
\]

The following table gives the even spherical degrees through \(k=60\). Here \(a_k=[t^k]M_{2I}(t)\), \(n_{k/2}=a_k\), and \(d_k=(k+1)a_k\).

| Spherical degree \(k\) | Spin \(j=k/2\) | Molien coefficient \(a_k=n_j\) | Eigenvalue \(k(k+2)\) | Quotient multiplicity \(d_k\) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 | 1 |
| 2 | 1 | 0 | 8 | 0 |
| 4 | 2 | 0 | 24 | 0 |
| 6 | 3 | 0 | 48 | 0 |
| 8 | 4 | 0 | 80 | 0 |
| 10 | 5 | 0 | 120 | 0 |
| 12 | 6 | 1 | 168 | 13 |
| 14 | 7 | 0 | 224 | 0 |
| 16 | 8 | 0 | 288 | 0 |
| 18 | 9 | 0 | 360 | 0 |
| 20 | 10 | 1 | 440 | 21 |
| 22 | 11 | 0 | 528 | 0 |
| 24 | 12 | 1 | 624 | 25 |
| 26 | 13 | 0 | 728 | 0 |
| 28 | 14 | 0 | 840 | 0 |
| 30 | 15 | 1 | 960 | 31 |
| 32 | 16 | 1 | 1088 | 33 |
| 34 | 17 | 0 | 1224 | 0 |
| 36 | 18 | 1 | 1368 | 37 |
| 38 | 19 | 0 | 1520 | 0 |
| 40 | 20 | 1 | 1680 | 41 |
| 42 | 21 | 1 | 1848 | 43 |
| 44 | 22 | 1 | 2024 | 45 |
| 46 | 23 | 0 | 2208 | 0 |
| 48 | 24 | 1 | 2400 | 49 |
| 50 | 25 | 1 | 2600 | 51 |
| 52 | 26 | 1 | 2808 | 53 |
| 54 | 27 | 1 | 3024 | 55 |
| 56 | 28 | 1 | 3248 | 57 |
| 58 | 29 | 0 | 3480 | 0 |
| 60 | 30 | 2 | 3720 | 122 |

For clarity, the next requested check is
\[
a_{60}=[t^{60}]M_{2I}(t)=2
\quad\Longrightarrow\quad d_{60}=61\cdot2=122.
\]
At degree 120, \(a_{120}=3\), hence \(d_{120}=121\cdot3=363\). In the Molien coefficient at degree 60, the two solutions are \((p,q,\epsilon)=(5,0,0)\) and \((0,3,0)\); there is no contribution from the numerator term \(t^{30}\), since 30 is not representable as \(12p+20q\). At degree 120 the three solutions are \((10,0,0),(5,3,0),(0,6,0)\); again the \(\epsilon=1\) term contributes zero because 90 is not representable as \(12p+20q\).

## 5. Scope and exclusions

- The affine \(\widetilde E_8\) graph and the nine irreducible representations of dimensions \(1,2,2',3,3',4,4',5,6\) are representation-theoretic data of \(2I\). They are not derived from the scalar spectrum.
- The spectrum follows by taking invariants in the scalar harmonic representation \(V_{k/2}\otimes V_{k/2}^{*}\); McKay is a separate representation-theoretic organization of tensoring with the defining two-dimensional representation.
- The radius-one normalization is essential for the displayed numerical eigenvalues.
- No numerical or physical relation to \(\varphi\), the supergolden constant, PSU scales, or Pellis coefficients is asserted here.
- The finite script check is a computational consistency check only; the all-degree invariant formula is supplied by Molien–Klein.
