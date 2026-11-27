# T149 — Q6 Clifford graph operator: exact finite spectrum and no low-energy Dirac cone

**Classification:** exact finite-matrix theorem, with numerical audit of gauge covariance and sheet conjugation. This operator is a diagnostic baseline, not the physical continuum Dirac operator.  
**Dependencies:** Q6 six-cube incidence; T147 Cl(6)/Spin(6); T148 PSU–Anti-Twin chiral-fluid decomposition.

## 1. Oriented Q6 partial shifts

For each bit direction \(i=1,\ldots,6\), let \(T_i\) be the partial shift on \(\mathbb C^{64}\):
\[
T_i|b\rangle=
\begin{cases}
|b\oplus e_i\rangle,&b_i=0,\\
0,&b_i=1.
\end{cases}
\]
Set \(K_i=T_i-T_i^\dagger\). Since each coordinate direction partitions Q6 into 32 disjoint edges,
\[
K_i^\dagger=-K_i,\qquad K_i^2=-I_{64},\qquad [K_i,K_j]=0.
\]

Let \(\Gamma_i\) be the Hermitian Cl(6) matrices of T147 and define
\[
D_{Q6}=\frac12\sum_{i=1}^6 K_i\otimes\Gamma_i.
\]
Then \(D_{Q6}^\dagger=-D_{Q6}\). The Clifford relations give
\[
\begin{aligned}
D_{Q6}^2
&=\frac14\sum_i K_i^2\otimes\Gamma_i^2
+\frac14\sum_{i<j}K_iK_j\otimes
(\Gamma_i\Gamma_j+\Gamma_j\Gamma_i)\\
&=-\frac64 I_{512}=-\frac32 I_{512}.
\end{aligned}
\]
Therefore
\[
\boxed{\operatorname{spec}(iD_{Q6})
=\{-\sqrt{3/2},+\sqrt{3/2}\},}
\]
with multiplicity 256 for each sign. There are no zero modes and no low-energy Dirac cone in this bare identity-link operator. Restoring a lattice scale \(a\) multiplies the gap by \(a^{-1}\); it does not create a massless branch.

The 6D chirality matrix \(\Gamma_*\) anticommutes with \(D_{Q6}\). This is an exact finite Clifford property, not evidence for a continuum fermion.

## 2. Gauge-covariant and Anti-Twin extension

For an oriented edge \(g\to h\) in direction \(i\), replace the partial shift by
\[
(T_i[U])_{hg}=U_{hg},\qquad K_i[U]=T_i[U]-T_i[U]^\dagger.
\]
For \(U_{hg}\in U(1)\), \(K_i[U]^\dagger=-K_i[U]\). Under a vertex gauge transformation \(G=\operatorname{diag}(e^{i\chi_b})\),
\[
U_{hg}\mapsto e^{i\chi_h}U_{hg}e^{-i\chi_g},
\quad D_{Q6}[U]\mapsto(G\otimes I_8)D_{Q6}[U](G^{-1}\otimes I_8).
\]
The Anti-Twin link is the conjugate representation \(U^-_{hg}=(U^+_{hg})^*\). The doubled graph operator is block diagonal in sheet space and is exchanged by \(\tau_1\) together with exchange of the two backgrounds. The audit checks anti-Hermiticity, 6D chirality, local gauge covariance and conjugate-sheet exchange.

## 3. Consequence for the spinor programme

This closes a useful diagnostic gap: there is now an explicit Q6 Clifford graph operator, but its bare spectrum proves that it is **not** the desired low-energy Dirac operator. The two-sheet right/left lock of T148 is a representation-level identification; it does not change this flat, gapped identity-link spectrum.

The physical Q6 fermion still requires a different kinetic construction—e.g. a refinement-consistent operator or a domain-wall/overlap mechanism—with its own locality, Hermiticity, spectral-flow and anomaly-cancellation tests. The two sheets retain the mirror partner; no evasion of Nielsen–Ninomiya is claimed.

## 4. Reproduction

~~~bash
python scripts/audit_q6_clifford_graph_dirac.py
python -m unittest discover -s tests -p "test_q6_clifford_graph_dirac.py" -v
~~~

The script writes audits/Q6_CLIFFORD_GRAPH_DIRAC_AUDIT.json.

## Status

| Statement | Status |
|---|---|
| \(K_i^\dagger=-K_i\), \(K_i^2=-I\), \([K_i,K_j]=0\) | Exact operator identities |
| \(D_{Q6}^\dagger=-D_{Q6}\), \(\{\Gamma_*,D_{Q6}\}=0\) | Exact |
| \(D_{Q6}^2=-3I/2\) | Exact |
| Spectrum \(\pm i\sqrt{3/2}\), multiplicity 256 each | Exact consequence; numerically audited |
| Local \(U(1)\) covariance of link-twisted operator | Finite numerical audit |
| Anti-Twin conjugate-sheet exchange | Finite numerical audit |
| Continuum Dirac cone / light fermion | Fails for this bare operator |
| Refined/domain-wall/overlap physical fermion | Open |
