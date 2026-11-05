# T037 — Exact isotypic projectors on the Rumin SU(2) spectral blocks

**Status:** exact finite-dimensional representation-theoretic bridge from the T021 Molien multiplicities to the explicit 2I representation models in T034–T036. The result applies to the SU(2)-type blocks used in the T021 spectral decomposition. It does **not** construct geometric eigenforms or reduced Rumin differential matrices.

## 1. Setting and conventions

Let \(G=2I\subset SU(2)\), \(|G|=120\), and let \(W=\mathbb C^2\) be the defining representation fixed in T035. For \(m\geq0\), put
\[
V_m=\operatorname{Sym}^m(W),\qquad \dim V_m=m+1.
\]
Use the pullback action on homogeneous polynomials
\[
(U_m(g)f)(v)=f(\rho_2(g)^{-1}v).
\]
This is a representation of \(G\). Its character is the symmetric-power character \(\chi_m\) used in T021 and T034; the SU(2) characters are real-valued, so the dual/pullback convention does not change the character averages.

For each irreducible \(\rho\in\widehat G\), let \(d_\rho=\dim V_\rho\), and let
\[
b_{m,\rho}=\dim\operatorname{Hom}_G(V_\rho,V_m)
=\frac1{120}\sum_{[g]}|[g]|\,
\overline{\chi_\rho(g)}\chi_m(g),
\]
the coefficient of the exact Molien covariant \(M_\rho(t)\) recorded in T021/T032.

## 2. Theorem: rank of the explicit central projector

Define
\[
P_{m,\rho}=\frac{d_\rho}{120}
\sum_{g\in G}\overline{\chi_\rho(g)}\,U_m(g).
\]

Then, for every \(m\geq0\):

1. \(P_{m,\rho}\) is the orthogonal projection onto the \(\rho\)-isotypic component of \(V_m\).
2. \(P_{m,\rho}^2=P_{m,\rho}\).
3. \(P_{m,\rho}P_{m,\sigma}=0\) for \(\rho\ne\sigma\), and \(\sum_\rho P_{m,\rho}=I_{V_m}\).
4. Its rank is exactly
\[
\boxed{\operatorname{rank}P_{m,\rho}
=\operatorname{tr}P_{m,\rho}
=d_\rho\,b_{m,\rho}.}
\]

**Proof.** Complete reducibility for the finite group gives
\[
V_m\cong\bigoplus_{\rho\in\widehat G}
V_\rho\otimes \mathbb C^{b_{m,\rho}}.
\]
The central character idempotent acts as identity on the \(\rho\)-isotypic summand and zero on every inequivalent summand. This proves the projection, orthogonality and completeness identities. The \(\rho\)-isotypic summand has dimension \(d_\rho b_{m,\rho}\); an idempotent has trace equal to rank. The character formula for \(b_{m,\rho}\) gives the stated exact Molien rank. \(\square\)

This is an all-degree theorem, not a finite numerical extrapolation. The finite exact code checks selected degrees as regression tests of the theorem.

## 3. Application to the T021 Rumin spectral blocks

In the three-dimensional \(n=1\) decomposition used by T021, the relevant \(U(2)\)-type with weights \((q,-p)\), where \(m=p+q\), restricts to \(V_m=\operatorname{Sym}^m(\mathbb C^2)\) on \(SU(2)\). Therefore each fixed weight block carries the same \(2I\)-representation \(V_m\).

Consequently, on each individual T021 block:
\[
\boxed{\operatorname{rank}(P_{m,\rho}|_{\text{one weight block}})
=d_\rho b_{m,\rho}.}
\]

For the \(E^0\) family there are \(m+1\) allowed weights \(p=0,\ldots,m\). Its total blockwise \(\rho\)-isotypic dimension at fixed \(m\) is
\[
(m+1)d_\rho b_{m,\rho}.
\]
For the two conjugate \(E^1\) bidegrees there are \(2(m+1)\) such blocks, giving
\[
2(m+1)d_\rho b_{m,\rho}.
\]

These are blockwise counts. If different weights yield the same numerical eigenvalue, their dimensions must be added to obtain the full eigenspace multiplicity. The eigenvalue formula and boundary conventions remain those of T021/T024.

## 4. What the explicit computation verifies

The implementation src/t037_rumin_isotypic_projectors.py constructs \(U_m(g)\) from the exact quaternion model T035 and the symmetric-power action used by T036. For each selected degree it checks in exact algebraic arithmetic:

- all nine projector idempotence identities;
- all 36 pairwise orthogonality identities;
- completeness \(\sum_\rho P_{m,\rho}=I\);
- centrality against all 120 group matrices;
- \(\operatorname{tr}P_{m,\rho}=d_\rho b_{m,\rho}\), using the exact T032 Molien coefficients.

The test degrees \(m=0,\ldots,7\) include the first multiplicity-one occurrence of each of the nine irreducibles. Degree \(m=12\) checks the first nontrivial invariant level used in the scalar benchmark of T010.

## 5. Boundary of the result

**PROVED:** the all-degree representation-theoretic rank identity and the blockwise projector statement, under the fixed T021 \(SU(2)\)-type identification.

**EXACT COMPUTATIONAL AUDIT SPECIFIED:** the concrete projector matrices, idempotence, centrality, completeness and trace/rank identities at the test degrees. These are not reported as executed until the repository test suite actually runs.

**NOT YET PROVED:** a choice of geometric Rumin eigenform bases on \(S^3\), explicit matrix units acting on those bases, or reduced matrices for the Rumin differential \(d_R\) and middle operator \(D\). T021 supplies spectral multiplicity data, not those geometric bases. T031 supplies equivariance and descent, but does not by itself produce the bases.

**OPEN:** the geometric intertwining maps from the explicit finite-dimensional \(V_m\)-blocks to concrete Rumin eigenspaces, including compatibility with the differentials and domains. This is the next analytic/geometric obligation. No Q6/PRISM Mosco limit follows from T037.

## 6. Dependencies

- T021: \(SU(2)\)-type spectral blocks, \(b_{m,\rho}\), and Rumin eigenvalue labels.
- T032: exact Molien coefficient engine.
- T034: exact nine-row character table over \(\mathbb Q(\sqrt5)\).
- T035: exact quaternion realization and defining \(SU(2)\) matrices.
- T036: explicit irreducible matrix models and invariant Hermitian metrics.
- T031/T024: geometric equivariance and three-dimensional operator conventions.

## 7. Reproducibility

From the repository root:
\`\`\`bash
python -m unittest tests.test_t037_rumin_isotypic_projectors -v
\`\`\`

The tests are intended as exact SymPy checks. No passing result or CI status is claimed before execution.
