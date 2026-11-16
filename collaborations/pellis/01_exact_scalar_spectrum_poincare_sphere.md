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
be the binary icosahedral group, of order \(120\). Identify \(SU(2)\) with the unit sphere \(S^3\) by the standard unit-quaternion realization. The group acts on \(S^3\) by left multiplication:
\[
q\cdot x=qx,\qquad q\in2I,\quad x\in S^3.
\]

This action is free. Indeed, if \(qx=x\), then multiplication on the right by \(x^{-1}\) gives \(q=1\). Thus
\[
M:=S^3/2I
\]
is a smooth compact spherical space form. We equip it with the quotient of the unit round metric on \(S^3\), so its sectional curvature is \(1\).

The group model used in the project is exact: the 120 elements are represented as unit quaternions with coordinates in \(\mathbb Q(\sqrt5)\), and the multiplication table, unit norms, inverses, and defining two-dimensional representation are checked using exact arithmetic. See project record **T035**, §2–§5, and the corresponding audit script cited in §8 below.

## 3. Scalar eigenvalues on the covering sphere

For the unit round three-sphere, scalar spherical harmonics of degree \(k\geq0\) have Laplace eigenvalue
\[
\lambda_k=k(k+2).
\]

Let
\[
V_k=\operatorname{Sym}^k(\mathbb C^2),
\qquad \dim_{\mathbb C}V_k=k+1,
\]
be the irreducible \(SU(2)\)-representation of highest weight \(k\). Under the standard left-right action of \(SU(2)_L\times SU(2)_R\), the degree-\(k\) scalar harmonic space is
\[
\mathcal H_k(S^3)\cong V_k\otimes V_k^*.
\]
The quotient group \(2I\) acts through the left factor only. Therefore
\[
\mathcal H_k(S^3)^{2I}
\cong V_k^{2I}\otimes V_k^*.
\]
Writing
\[
n_k:=\dim V_k^{2I},
\]
the multiplicity of \(\lambda_k\) on \(M=S^3/2I\) is
\[
\boxed{d_k=(k+1)n_k.}
\]

This is the key representation-theoretic reduction: the invariant multiplicity \(n_k\) is computed on the left \(SU(2)\) representation, while the right factor contributes the independent dimension \(k+1\).

The general spherical-space-form framework behind the invariant-eigenspace identification is given by Ikeda, Proposition 1.5, pp. 79–80. In particular, the eigenspaces downstairs are exactly the invariant parts of the spherical eigenspaces upstairs.

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
c_k=\dim\bigl(\operatorname{Sym}^k(\mathbb C^2)^{2I}\bigr).
\]
Thus \(n_k=c_k\), and the scalar multiplicity formula becomes
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

The invariant-ring presentation and the degree-12, degree-20, degree-30 generators are treated explicitly in Klein's classical work and in Nash's modern exposition, §2, especially equations (2.8)–(2.11). The Hilbert series above follows from the graded complete-intersection presentation: three generators in degrees \(12,20,30\), one relation in degree \(60\).

### 4.1 Why there is no extra radial subtraction in this coefficient formula

The series \(A_{2I}(t)\) is the invariant series for the defining **complex two-dimensional** representation of \(2I\). Its coefficient \(c_k\) is already \(\dim V_k^{2I}\). The full scalar harmonic multiplicity on \(S^3/2I\) is then \((k+1)c_k\), because of the untouched right \(SU(2)\) factor.

This must not be confused with the distinct real four-variable polynomial calculation. For a finite group acting linearly on \(\mathbb R^4\), the Fischer decomposition separates homogeneous polynomials into harmonic polynomials and multiples of \(r^2\). Ikeda writes this as
\[
P^k=H^k\oplus r^2P^{k-2}
\]
in equation (1.1), p. 78, and derives the spherical-space-form generating function in Theorem 2.2, pp. 80–81:
\[
F_G(t)=\frac1{|G|}\sum_{g\in G}
\frac{1-t^2}{\det(I_4-tg)}.
\]
That real four-dimensional Molien/Fischer expression is a valid independent route to the same scalar spectrum. It is not the same Hilbert series as \(A_{2I}(t)\).

The two generating functions are related by the coefficient identity
\[
F_{2I}(t)=\sum_{k\geq0}(k+1)c_k t^k
=A_{2I}(t)+tA_{2I}'(t).
\]
This relation follows by differentiating the power series term by term. It is a useful consistency check and prevents the two Molien calculations from being mixed.

## 5. Independent exact character calculation

The invariant dimension can also be computed by the Reynolds projector:
\[
n_k=\frac1{120}\sum_{g\in2I}\chi_k(g),
\]
where \(\chi_k\) is the character of \(V_k=\operatorname{Sym}^k(\mathbb C^2)\).

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
The class sizes sum to \(120\). The symmetric-power characters are generated exactly by
\[
\chi_0(g)=1,\qquad
\chi_1(g)\text{ as above},\qquad
\chi_k(g)=\chi_1(g)\chi_{k-1}(g)-\chi_{k-2}(g).
\]
Hence
\[
n_k=\frac1{120}\sum_{j=1}^{9}|C_j|\chi_k(C_j).
\]
All character values lie in \(\mathbb Q(\sqrt5)\); the average is evaluated exactly, not numerically.

The central element \(-I\in2I\) acts on \(V_k\) by \((-1)^k\). Since an invariant vector must be fixed by every group element, it follows immediately that
\[
n_k=0\quad\text{for odd }k.
\]

The project audit compares this character average with the integer coefficient count in §4 for every degree \(0\leq k\leq120\). The two calculations agree exactly at all 121 degrees.

## 6. Verified initial scalar spectrum

For every degree \(k\), the eigenvalue is \(\lambda_k=k(k+2)\) and its multiplicity is \(d_k=(k+1)c_k\). The first nonzero entries are:

| \(k\) | \(\lambda_k\) | \(c_k=n_k\) | \(d_k\) |
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
2. The scalar eigenvalues on the unit-radius quotient are among \(k(k+2)\), with multiplicity \((k+1)\dim V_k^{2I}\).
3. The binary invariant Hilbert series is \((1+t^{30})/((1-t^{12})(1-t^{20}))\).
4. The exact scalar multiplicity formula is therefore the coefficient formula in §4.
5. Odd degrees vanish because the central element \(-I\) acts by \((-1)^k\).

### Exact computational verification

The repository audit independently evaluates the Reynolds character average and the binary Molien coefficient count in exact arithmetic for \(0\leq k\leq120\). The corresponding GitHub Actions run completed successfully with all three tests passing.

### Explicitly outside the scope of this note

- vector, tensor, spinor, or Rumin spectra;
- analytic torsion and determinant calculations;
- any identification of the Pellis Functions with the binary invariant generators;
- any derivation of the fine-structure constant;
- any claim that a near-golden numerical ratio is an exact spectral identity;
- any physical interpretation of the scalar spectrum.

These questions belong to later documents and require their own definitions, evidence, and proofs.

## 8. Reproducibility and project records

Repository: [fabianleonaressi95/theorem](https://github.com/fabianleonaressi95/theorem)

- **Exact group model:** [T035 — Exact quaternion realization of the binary icosahedral group](../../theorems/T035-exact-binary-icosahedral-model.md).
- **Exact group construction and audit:** [audits/t035_exact_binary_icosahedral_model.py](../../audits/t035_exact_binary_icosahedral_model.py).
- **Scalar spectral formula and complete table:** [Document A1 — Exact scalar spectrum](../../documents/DOCUMENT_A1_EXACT_SPECTRAL_GEOMETRY_S3_2I.md).
- **Independent scalar spectral audit:** [audits/a1_poincare_scalar_spectrum.py](../../audits/a1_poincare_scalar_spectrum.py).
- **Regression tests:** [tests/test_a1_poincare_scalar_spectrum.py](../../tests/test_a1_poincare_scalar_spectrum.py).
- **Recorded CI run:** [GitHub Actions run 43879748053](https://github.com/fabianleonaressi95/theorem/actions/runs/43879748053).

Reproduce from the repository root:
\`\`\`bash
python -m audits.t035_exact_binary_icosahedral_model
python -m audits.a1_poincare_scalar_spectrum --max-degree 120
python -m unittest tests.test_a1_poincare_scalar_spectrum -v
\`\`\`

The first command checks the exact 120-element quaternion model and defining representation. The second compares the exact character average with the binary Molien coefficient count through degree 120. The third runs the three regression tests. These commands are the reproducibility protocol; a reader should run them locally rather than infer a new test result from the text of this note.

## 9. References

**[1]** A. Ikeda, “On the spectrum of a Riemannian manifold of positive constant curvature,” *Osaka Journal of Mathematics* **17** (1980), no. 1, 75–93. DOI: [10.18910/5171](https://doi.org/10.18910/5171). Open version of record: [Osaka University Institutional Knowledge Archive](https://ir.library.osaka-u.ac.jp/repo/ouka/all/5171/ojm17_01_08.pdf). Relevant locations: Lemma 1.3 and Lemma 1.4, pp. 78–79; Proposition 1.5, p. 79; Theorem 2.2 and equations (2.1)–(2.2), pp. 80–81.

**[2]** F. Klein, *Vorlesungen über das Ikosaeder und die Auflösung der Gleichungen vom fünften Grade*. Leipzig: B. G. Teubner, 1884. Classical source for the icosahedral invariant forms and their syzygy.

**[3]** O. Nash, “On Klein’s Icosahedral Solution of the Quintic,” *Expositiones Mathematicae* **32** (2014), no. 2, 99–120. DOI: [10.1016/j.exmath.2013.09.003](https://doi.org/10.1016/j.exmath.2013.09.003). Preprint: [arXiv:1308.0955](https://arxiv.org/abs/1308.0955). Relevant location: §2, especially the invariant forms (2.8)–(2.9), the degree-60 syzygy (2.11), and the invariant-ring argument immediately following it.

**[4]** A. Ikeda and Y. Yamamoto, “On the spectra of 3-dimensional lens spaces,” *Osaka Journal of Mathematics* **16** (1979), no. 2, 447–469. DOI: [10.18910/4811](https://doi.org/10.18910/4811). This is background for the spherical-space-form spectral method; the specific general spherical-space-form statements used above are cited to Ikeda [1].

---

**Document status:** foundational note assembled from established spectral geometry, classical invariant theory, the exact T035 group model, and the existing finite A1 audit. No new physical correspondence is asserted.
