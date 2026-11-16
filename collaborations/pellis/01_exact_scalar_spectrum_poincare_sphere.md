# Document 1 — Exact scalar spectral geometry of the Poincaré sphere

**Prepared as a mathematical foundation for discussion with Stergios Pellis**  
**Scope:** the scalar Laplace spectrum of the unit round quotient \(S^3/2I\).  
**Status:** established representation-theoretic identities plus an exact finite computational audit. No physical interpretation or connection to Pellis's resonance model is assumed in this document.

---

## 1. Purpose and logical order

This note fixes the geometric object, conventions, and verified spectral data before any new conjecture or proposed correspondence is introduced.

The order is deliberate:

1. define the group action and quotient;
2. identify the scalar eigenspaces on the covering sphere;
3. determine the invariant multiplicities from the binary icosahedral invariant ring;
4. independently check the multiplicities by exact character averaging;
5. list the resulting initial spectrum and state precisely what has, and has not, been established.

The note does **not** attempt to derive the fine-structure constant, interpret a spectral ratio as a golden-ratio law, or identify the Poincaré quotient with a Pellis resonance construction. Those questions require separate definitions and proofs.

## 2. Geometric object and group action

Let
\[
2I\subset SU(2)
\]
be the binary icosahedral group, of order \(120\). Identify \(SU(2)\) with the unit sphere \(S^3\) by the standard unit-quaternion realization. The group acts on \(S^3\) by **left multiplication**:
\[
q\cdot x=qx,\qquad q\in2I,\quad x\in S^3.
\]
Throughout this note, \(S^3/2I\) means the orbit space for this left action. The induced action on scalar harmonics is on the left Peter–Weyl factor. The right-action convention gives an isometric quotient and the same scalar spectrum, but it is not the convention used below.

This action is free. Indeed, if \(qx=x\), then multiplication on the right by \(x^{-1}\) gives \(q=1\). Thus
\[
M:=S^3/2I
\]
is a smooth compact spherical space form. We equip it with the quotient of the unit round metric on \(S^3\), so its sectional curvature is \(1\).

The project contains an exact quaternion model of the 120 elements over \(\mathbb Q(\sqrt5)\), recorded in T035. On this collaboration branch the duplicated legacy implementation has been removed: the audit module now has one top-level `from __future__ import annotations`, and the regression test targets its current API. The branch workflow compiles the module, runs the A1 and T035 tests, and executes the T035 audit. A successful run must be reported only after the Actions result for the resulting branch commit is observed; see §8.
The project contains an exact quaternion model of the 120 elements over \(\mathbb Q(\sqrt5)\). Its source record is T035. The legacy audit file is retained as a project record, but it currently contains a duplicated `from __future__ import annotations` block and is not an executable reproduction command; see §8.

## 3. Scalar eigenvalues on the covering sphere

For the unit round three-sphere, use the **positive Laplacian convention**
\[
\Delta=-\operatorname{div}\nabla,
\]
so scalar spherical harmonics of degree \(k\geq0\) have eigenvalue
\[
\lambda_k=k(k+2).
\]

Let \(U=\mathbb C^2\) be the defining representation of \(SU(2)\), and set
\[
W_r:=\operatorname{Sym}^{r}(U),\qquad \dim_{\mathbb C}W_r=r+1.
\]
Here \(r\) is always the **polynomial degree**. Under the standard left-right action of \(SU(2)_L\times SU(2)_R\), the degree-\(k\) scalar harmonic space is
\[
\mathcal H_k(S^3)\cong W_k\otimes W_k^*.
\]
Fix the induced action on functions by \( (L_qf)(x)=f(q^{-1}x) \). With the Peter–Weyl identification chosen so that this left-regular action is on the first factor, the quotient group \(2I\) acts through that factor only. Therefore
The quotient group \(2I\) acts through the left factor only. Therefore
\[
\mathcal H_k(S^3)^{2I}
\cong W_k^{2I}\otimes W_k^*.
\]
Define
\[
a_k:=\dim W_k^{2I}.
\]
For even degree \(k=2j\), one may also write \(W_{2j}=V_j\), where \(V_j\) denotes the spin-\(j\) irreducible representation and has dimension \(2j+1\). Define separately
\[
n_j:=a_{2j}=\dim V_j^{2I}.
\]
Thus the invariant-series coefficient is indexed by polynomial degree \(k\), whereas \(n_j\) is indexed by spin \(j\). The multiplicity of \(\lambda_k\) on \(M=S^3/2I\) is
\[
\boxed{d_k=(k+1)a_k,\qquad d_{2j}=(2j+1)n_j.}
\]

This is the key representation-theoretic reduction: the invariant dimension \(a_k\) is computed on the left \(SU(2)\) representation, while the right factor contributes the independent dimension \(k+1\).

The general spherical-space-form framework behind the invariant-eigenspace identification is treated by Ikeda [1]. The exact proposition and page locator should be checked directly against the version of record before external submission.

## 4. Binary icosahedral invariant series

Consider the action of \(2I\) on \(\mathbb C^2\), its defining two-dimensional representation. The classical binary icosahedral invariant ring has homogeneous generators of degrees \(12,20,30\), with one relation of degree \(60\). In a standard normalization the generators \(f,H,T\) satisfy
\[
H^3+T^2=1728f^5.
\]
Consequently its Hilbert–Molien series is
\[
\begin{aligned}
A_{2I}(t)
&=\frac{1-t^{60}}{(1-t^{12})(1-t^{20})(1-t^{30})}\\
&=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}\\
&=\sum_{k\geq0}c_k t^k,
\end{aligned}
\]
where
\[
c_k=\dim\bigl(W_k^{2I}\bigr).
\]
Thus \(a_k=c_k\), and the scalar multiplicity formula becomes
\[
\boxed{
d_k=(k+1)[t^k]\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
}
\]

Equivalently, the coefficient has the exact integer description
\[
c_k=
\#\left\{(a,b,\epsilon)\in\mathbb Z_{\geq0}^2\times\{0,1\}:
12a+20b+30\epsilon=k\right\}.
\]
This form is useful because it computes every coefficient by finite integer counting, without floating-point arithmetic.

The invariant-ring presentation and the degree-12, degree-20, degree-30 generators are treated in Klein's classical work and in Nash's modern exposition [2, 3]. The precise equation locators in Nash are left for direct page-level verification before external submission. The Hilbert series above follows from the graded complete-intersection presentation: three generators in degrees \(12,20,30\), one relation in degree \(60\).

### 4.1 Why there is no extra radial subtraction in this coefficient formula

The series \(A_{2I}(t)\) is the invariant series for the defining **complex two-dimensional** representation of \(2I\). Its coefficient \(c_k=a_k\) is already \(\dim W_k^{2I}\). The full scalar harmonic multiplicity on \(S^3/2I\) is then \((k+1)a_k=(k+1)c_k\), because of the untouched right \(SU(2)\) factor.

This must not be confused with the distinct real four-variable polynomial calculation. For a finite group acting linearly on \(\mathbb R^4\), the Fischer decomposition separates homogeneous polynomials into harmonic polynomials and multiples of \(r^2\). Ikeda writes this as
\[
P^k=H^k\oplus r^2P^{k-2}
\]
in its discussion of Fischer decomposition and the spherical-space-form generating function [1]. The precise equation, theorem, and page locators are intentionally not asserted here pending a direct page-level check:
\[
F_G(t)=\frac1{|G|}\sum_{g\in G}
\frac{1-t^2}{\det(I_4-tg)}.
\]
That real four-dimensional Molien/Fischer expression is a valid independent route to the same scalar spectrum. It is not the same Hilbert series as \(A_{2I}(t)\).

The two generating functions are related by the coefficient identity
\[
F_{2I}(t)=\sum_{k\geq0}(k+1)a_k t^k
=A_{2I}(t)+tA_{2I}'(t).
\]
This relation follows by differentiating the power series term by term. It is a useful consistency check and prevents the two Molien calculations from being mixed.

## 5. Exact character calculation and Reynolds cross-check
## 5. Independent exact character calculation

The invariant dimension can also be computed by the Reynolds projector:
\[
a_k=\frac1{120}\sum_{g\in2I}\chi_k(g),
\]
where \(\chi_k\) is the character of \(W_k=\operatorname{Sym}^k(\mathbb C^2)\).

For the exact conjugacy-class convention fixed in T035, the class sizes are
\[
(1,1,20,30,12,12,20,12,12),
\]
and the character of the defining two-dimensional representation is
\[
\chi_1=
(2,-2,-1,0,\varphi-1,-\varphi,1,\varphi,1-\varphi),
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]
The class sizes sum to \(120\). The characters of the polynomial-degree representations \(W_k\) are generated exactly by
\[
\chi_0(g)=1,\qquad
\chi_1(g)\text{ as above},\qquad
\chi_k(g)=\chi_1(g)\chi_{k-1}(g)-\chi_{k-2}(g).
\]
Hence
\[
a_k=\frac1{120}\sum_{j=1}^{9}|C_j|\chi_k(C_j).
\]
All character values lie in \(\mathbb Q(\sqrt5)\); the average is evaluated exactly, not numerically.

The central element \(-I\in2I\) acts on \(W_k\) by \((-1)^k\). Since an invariant vector must be fixed by every group element, it follows immediately that
\[
a_k=0\quad\text{for odd }k.
\]

The A1 audit compares this character average with the integer coefficient count in §4 for every degree \(0\leq k\leq120\). The arithmetic routes are distinct (Reynolds recurrence versus integer coefficient counting), but the class sizes and fundamental character are transcribed from T035. This is an independent spectral calculation conditional on shared group data, not an independent reconstruction of the group. The two calculations agree exactly at all 121 degrees.


### 5.1 Representation-theoretic cross-checks: McKay and covariant Molien series

The scalar invariant multiplicity is the trivial-isotypic coefficient in the decomposition of each \(W_k\). The repository contains two separate representation-theoretic records that extend this calculation beyond the trivial representation:

- **T026 (affine \(\widetilde E_8\) McKay recurrence):** tensoring an irreducible \(2I\)-module with the defining two-dimensional module gives the adjacency recurrence on the nine irreducibles. The graph dimensions satisfy \(\sum_i d_i^2=120\), \(\sum_i d_i=30\), and \(Ad=2d\). The weighted dimension identity \(\sum_i d_i n_i(k)=k+1\) and the central parity rule provide internal checks on the recurrence. The recurrence is an algebraic consequence of the Clebsch–Gordan rule once the McKay graph and its irreducible labels are established; the graph's identification from the exact quaternion model is a separate representation-theory input.
- **T027 (nine covariant Molien series):** its nine coefficient sequences are compared with the T026 recurrence, with the two four-dimensional irreducibles kept distinct. The comparison is a coefficient-consistency check for the supplied Molien numerators; it does not independently derive the covariant modules or prove their module presentations.

The current recorded mapping is \(1\leftrightarrow1\), \(2_s\leftrightarrow2\), \(3\leftrightarrow3\), \(4_s\leftrightarrow4'\), \(5\leftrightarrow5\), \(6_s\leftrightarrow6\), \(4\leftrightarrow4\), \(2'_s\leftrightarrow2'\), and \(3'\leftrightarrow3'\). The distinction \(4_s\ne4\) is essential: their first occurrences are at degrees 3 and 6, respectively.

**Evidence status:** the recurrence identities and the displayed low-degree decompositions have been independently reproduced from the recorded data; this is not a claim that the repository T026/T027 scripts were directly executed in the present audit. T027's nine Molien numerator sequences remain input data pending derivation from explicit covariant-module constructions. These extensions are supplementary and are not needed for the scalar spectrum formula in §§3–6.
The project audit compares this character average with the integer coefficient count in §4 for every degree \(0\leq k\leq120\). The two calculations agree exactly at all 121 degrees.

## 6. Verified initial scalar spectrum

For every degree \(k\), the eigenvalue is \(\lambda_k=k(k+2)\) and its multiplicity is \(d_k=(k+1)a_k\). The first nonzero entries are:

| \(k\) | \(\lambda_k\) | \(a_k=c_k\) | \(d_k\) |
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

All odd degrees vanish. Therefore the first positive scalar eigenvalue is
\[
\boxed{\lambda_{\min}^{+}=168,\qquad \operatorname{mult}(168)=13.}
\]
In particular, the value \(35=5(5+2)\) is not in this scalar spectrum: it corresponds to odd degree \(k=5\), for which the central element \(-I\) forces the invariant multiplicity to vanish.

The complete nonzero list through degree \(120\), including the exact multiplicity at each degree, is maintained in the repository's A1 audit output and source document. This note displays the initial values needed to identify the spectral gap; the full finite record is reproducible from the command in §8.

## 7. What is established — and what is not

### Established mathematical statements

1. The left multiplication action of \(2I\) on \(S^3\) is free, so the quotient is a smooth spherical space form.
2. The scalar eigenvalues on the unit-radius quotient are \(k(k+2)\), with multiplicity \((k+1)a_k\); equivalently, for even \(k=2j\), this is \((2j+1)n_j\).
3. The binary invariant Hilbert series is \((1+t^{30})/((1-t^{12})(1-t^{20}))\).
4. The exact scalar multiplicity formula is therefore the coefficient formula in §4.
5. Odd degrees vanish because the central element \(-I\) acts by \((-1)^k\).

### Exact computational verification

The A1 source evaluates the Reynolds character average and the binary Molien coefficient count in exact arithmetic for \(0\leq k\leq120\), using the T035 class data as fixed input. The historical GitHub Actions run 43879748053 is evidence for the A1 source/test versions whose blob identities were checked against the then-current main branch; it is not evidence that T035 ran in that workflow. The updated collaboration-branch workflow now explicitly compiles and runs T035. The successful run [43891483378](https://github.com/fabianleonaressi95/theorem/actions/runs/43891483378), on commit `006516d32d534a000ee66c302eb53a3586a2ce2a`, completed `py_compile`, all three A1 regression tests, the T035 regression test, and the direct T035 audit.
The repository audit independently evaluates the Reynolds character average and the binary Molien coefficient count in exact arithmetic for \(0\leq k\leq120\). The corresponding GitHub Actions run completed successfully with all three tests passing.

### Explicitly outside the scope of this note

- vector, tensor, spinor, or Rumin spectra;
- analytic torsion and determinant calculations;
- any identification of the Pellis Functions with the binary invariant generators;
- any derivation of the fine-structure constant;
- any claim that a near-golden numerical ratio is an exact spectral identity;
- any physical interpretation of the scalar spectrum.

These questions belong to later documents and require their own definitions, evidence, and proofs.

The PRISM cycle cover, Krist-All operator, Kathara chain maps, and multidimensional finite-data analysis requested for the broader collaboration are treated separately in [Document 2 — PRISM cycles, Krist-All, Kathara, and multidimensional analysis](02_prism_kathara_kristall_multidimensional.md). They are not premises of the scalar spectral theorem.

## 8. Reproducibility and project records

Repository: [fabianleonaressi95/theorem](https://github.com/fabianleonaressi95/theorem)

- **Exact group model:** [T035 — Exact quaternion realization of the binary icosahedral group](../../theorems/T035-exact-binary-icosahedral-model.md).
- **Exact T035 audit source:** [audits/t035_exact_binary_icosahedral_model.py](../../audits/t035_exact_binary_icosahedral_model.py). The branch source is aligned byte-for-byte with the repaired implementation from commit `9a60d887e434ef3b0c4a954942e228587fdc4052`; its blob SHA is `20968cf5426de6a579d2eec7755469c69b080a74`.
- **Scalar spectral formula and complete table:** [Document A1 — Exact scalar spectrum](../../documents/DOCUMENT_A1_EXACT_SPECTRAL_GEOMETRY_S3_2I.md).
- **Independent scalar spectral audit:** [audits/a1_poincare_scalar_spectrum.py](../../audits/a1_poincare_scalar_spectrum.py).
- **Regression tests:** [tests/test_a1_poincare_scalar_spectrum.py](../../tests/test_a1_poincare_scalar_spectrum.py).
- **Historical A1 CI evidence:** [GitHub Actions run 43879748053](https://github.com/fabianleonaressi95/theorem/actions/runs/43879748053). It must not be cited as a T035 run. **Combined A1/T035 verification:** [GitHub Actions run 43891483378](https://github.com/fabianleonaressi95/theorem/actions/runs/43891483378), commit `006516d32d534a000ee66c302eb53a3586a2ce2a`.
- **Legacy T035 audit source (not currently executable):** [audits/t035_exact_binary_icosahedral_model.py](../../audits/t035_exact_binary_icosahedral_model.py).
- **Scalar spectral formula and complete table:** [Document A1 — Exact scalar spectrum](../../documents/DOCUMENT_A1_EXACT_SPECTRAL_GEOMETRY_S3_2I.md).
- **Independent scalar spectral audit:** [audits/a1_poincare_scalar_spectrum.py](../../audits/a1_poincare_scalar_spectrum.py).
- **Regression tests:** [tests/test_a1_poincare_scalar_spectrum.py](../../tests/test_a1_poincare_scalar_spectrum.py).
- **Recorded CI run:** [GitHub Actions run 43879748053](https://github.com/fabianleonaressi95/theorem/actions/runs/43879748053).

Reproduce from the repository root:
```bash
python -m audits.a1_poincare_scalar_spectrum --max-degree 120
python -m unittest tests.test_a1_poincare_scalar_spectrum -v
python -m py_compile audits/t035_exact_binary_icosahedral_model.py
python -m unittest tests.test_t035_exact_binary_icosahedral_model -v
python audits/t035_exact_binary_icosahedral_model.py
```

The first two commands reproduce the scalar-spectrum audit and its regression tests. The third and fourth commands compile and execute the exact T035 group model and its regression test. A1 keeps its class-size and character input local so that its calculation is reproducible without importing T035; the two audits therefore share group-theoretic input but exercise different exact constructions. The successful combined run above is recorded for commit `006516d32d534a000ee66c302eb53a3586a2ce2a`; later documentation-only commits do not alter the audited T035 source or test.
```

The two commands below reproduce the scalar-spectrum audit and its regression tests. They do **not** execute the legacy T035 script or independently rebuild the quaternion group. The A1 audit keeps the exact class-size and character input local, avoiding import of the currently broken legacy T035 module. The recorded GitHub Actions run is separate evidence: it completed with three tests passing and 121 exact degree comparisons. No new test execution is claimed by this document update.

## 9. References

**[1]** A. Ikeda, “On the spectrum of a Riemannian manifold of positive constant curvature,” *Osaka Journal of Mathematics* **17** (1980), no. 1, 75–93. DOI: [10.18910/5171](https://doi.org/10.18910/5171). Open version of record: [Osaka University Institutional Knowledge Archive](https://ir.library.osaka-u.ac.jp/repo/ouka/all/5171/ojm17_01_08.pdf). Used as the general spherical-space-form spectral reference. Pinpoint page, proposition, theorem, and equation locators are withheld until rechecked directly against the PDF.

**[2]** F. Klein, *Vorlesungen über das Ikosaeder und die Auflösung der Gleichungen vom fünften Grade*. Leipzig: B. G. Teubner, 1884. Classical source for the icosahedral invariant forms and their syzygy.

**[3]** O. Nash, “On Klein’s Icosahedral Solution of the Quintic,” *Expositiones Mathematicae* **32** (2014), no. 2, 99–120. DOI: [10.1016/j.exmath.2013.09.003](https://doi.org/10.1016/j.exmath.2013.09.003). Preprint: [arXiv:1308.0955](https://arxiv.org/abs/1308.0955). Used for the modern discussion of the icosahedral invariant forms and syzygy; pinpoint equation locators are pending direct recheck.

**[4]** A. Ikeda and Y. Yamamoto, “On the spectra of 3-dimensional lens spaces,” *Osaka Journal of Mathematics* **16** (1979), no. 2, 447–469. DOI: [10.18910/4811](https://doi.org/10.18910/4811). Background reference only; no specific proposition, page, or equation from this paper is used as a premise here.

---

**Document status:** foundational note assembled from established spectral geometry, classical invariant theory, the exact T035 group model, and the existing finite A1 audit. No new physical correspondence is asserted.
