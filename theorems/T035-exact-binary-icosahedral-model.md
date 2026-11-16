# T035 — Exact quaternion realization of the binary icosahedral group

**Status:** exact finite-group construction over \(\mathbb Q(\sqrt5)\), with a concrete two-dimensional unitary representation. This supplies the group/model foundation for the remaining eight irreducible matrix models; it does not claim that those eight have already been split into explicit invariant bases.

## 1. Exact coefficient field

Put \(\phi=(1+\sqrt5)/2\), so \(\phi^2=\phi+1\) and \(\phi^{-1}=\phi-1\). Represent \(a+b\phi\) by \((a,b)\in\mathbb Q^2\). Multiplication is
\[
(a,b)(c,d)=(ac+bd,\ ad+bc+bd).
\]
This gives exact arithmetic in \(\mathbb Q(\sqrt5)\).

## 2. The 120 unit quaternions

The group \(2I\) is realized as the 120 vertices of the 600-cell in the unit quaternions:
- eight coordinate units;
- sixteen points \((\pm\frac12,\pm\frac12,\pm\frac12,\pm\frac12)\);
- the 96 even permutations of \((0,\frac12,\frac\phi2,\frac1{2\phi})\), with independent signs on the three nonzero entries.

The audit checks all \(120^2=14400\) products for closure, all 120 unit norms, and identity/inverse laws. Quaternion conjugation gives the inverse. Associativity is inherited from the quaternion algebra.

## 3. Fixed conjugacy-class convention

The scalar quaternion coordinate \(a\) gives the SU(2) trace \(2a\). In the T021/T034 class order, the scalar values are
\[
1,\ -1,\ -\frac12,\ 0,\ \frac{\phi-1}{2},\
-\frac\phi2,\ \frac12,\ \frac\phi2,\ \frac{1-\phi}{2}.
\]
The class sizes and representative orders are
\[
(1,1,20,30,12,12,20,12,12),\qquad
(1,2,3,4,5,5,6,10,10).
\]
The implementation checks these class counts directly and verifies that twice each scalar reproduces the T034 defining character
\[
(2,-2,-1,0,\phi-1,-\phi,1,\phi,1-\phi).
\]

## 4. The defining representation

For \(q=a+bi+cj+dk\), use
\[
\rho_2(q)=
\begin{pmatrix}
a+bi & c+di\\
-c+di & a-bi
\end{pmatrix}.
\]
The audit constructs this matrix exactly for all 120 elements and verifies
\[
\det\rho_2(q)=1,\qquad \rho_2(q)^*\rho_2(q)=I_2.
\]
It also checks multiplicativity on a deterministic set of products. The quaternion multiplication table is built exhaustively and can be reused for subsequent irreducible models.

## 5. Reproducibility

\`\`\`bash
python -m unittest tests.test_t035_exact_binary_icosahedral_model -v
python -m audits.t035_exact_binary_icosahedral_model
\`\`\`
The audit uses Fraction and SymPy; group construction and closure checks are exact.

## 6. What is closed and what remains open

**Closed by T035:** an exact 120-element quaternion model of \(2I\), its multiplication table and inverse map, exact class sizes/orders in the T034 convention, and the defining two-dimensional SU(2) representation.

**Not closed:** explicit irreducible matrices for \(2',3,3',4,4',5,6\); exact matrix units on Rumin harmonic spaces; and reduced geometric Rumin differential matrices in those bases. The next step is to extract the eight remaining irreducibles as exact invariant subspaces of symmetric powers of the defining representation, using the T034 character table and T033 matrix-unit convention.

No new analytic torsion value, spectral theorem, or continuum-limit claim is made.


## 7. CI verification record (2026-11-16)

The dedicated T035 workflow passed on `main` in [run 43910235426](https://github.com/fabianleonaressi95/theorem/actions/runs/43910235426), commit `ec4cf963b9dce2332e3011bf7bc027847d6bb2f9`.

The run compiled the audit, passed `tests.test_t035_exact_binary_icosahedral_model`, and executed the exact audit successfully. The JSON report records:

- 120 elements constructed over `Q(sqrt(5)));
- all 14,400 ordered products checked for closure;
- all 120 unit norms and 240 identity/inverse equations checked;
- all 120 defining-representation determinants and unitarity equations checked;
- the nine class sizes, nine representative orders, and defining character matched exactly.

The machine-readable report is retained as artifact `t035-exact-audit` (ID `14248755174`, SHA-256 `b7251fede6c4de16984e980c338301487872c9c5133e2ef50bd934958037f12f`, retention through 2027-02-14).

**Scope remains deliberately limited:** the successful audit proves the exact quaternion model, group closure, class data, and defining two-dimensional SU(2) representation. It does not construct the other eight irreducible matrix models. Those remain a separate representation-theoretic task.

The earlier failed run `43907978102` did **not** fail in T035: it stopped in the A1 scalar-spectrum step because SymPy was absent, so all T035 steps were skipped. The dependency was added, and the A1-only workflow subsequently passed in run `43910188230`. The CI split now assigns A1 and T035 to separate workflows to prevent this unrelated failure from masking the T035 result.
