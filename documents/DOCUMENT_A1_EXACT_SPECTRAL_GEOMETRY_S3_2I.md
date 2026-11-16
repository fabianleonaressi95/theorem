# Document A1 — Exact scalar spectrum of the Poincaré spherical space

**Object:** the unit round spherical space form $S^3/2I$, where $2I\subset SU(2)$ is the binary icosahedral group of order $120$, acting by left multiplication.

**Status:** the representation-theoretic formula is proved under the stated action. An exact character-average/Molien comparison is implemented for degrees $0\le k\le120$. CI execution is tracked separately and is not presumed from the presence of the test source.

## A.1 Conventions and the action

Identify the unit sphere $S^3$ with $SU(2)$. The group $2I$ acts by
\[
q\cdot x=qx,\qquad q\in2I,\quad x\in SU(2).
\]
This action is free: if $qx=x$, right multiplication by $x^{-1}$ gives $q=1$. The quotient is therefore a smooth spherical space form.

Let $V_k=\operatorname{Sym}^k(\mathbb C^2)$, the $(k+1)$-dimensional irreducible representation of $SU(2)$. Under $SU(2)_L\times SU(2)_R$, the degree-$k$ scalar spherical harmonics form
\[
\mathcal H_k(S^3)\simeq V_k\otimes V_k^*.
\]
The left $2I$ action is on the first factor only. Consequently
\[
\mathcal H_k(S^3)^{2I}\simeq V_k^{2I}\otimes V_k^*,
\qquad d_k=(k+1)n_k,
\]
where $n_k=\dim V_k^{2I}$.

For the unit-radius metric, the scalar Laplacian eigenvalue is
\[
\lambda_k=k(k+2),\qquad k=0,1,2,\ldots.
\]
Thus the multiplicity on the quotient is exactly $d_k$.

## A.2 Binary Molien coefficient

For the defining two-dimensional complex representation of $2I\subset SU(2)$, Klein's binary-icosahedral invariant Hilbert series is
\[
A_{2I}(t)=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}
=\sum_{k\ge0}c_k t^k.
\]
Equivalently,
\[
c_k=\#\{(a,b,\epsilon)\in\mathbb Z_{\ge0}^2\times\{0,1\}:
12a+20b+30\epsilon=k\}.
\]
Since $V_k=\operatorname{Sym}^k(\mathbb C^2)$, its invariant dimension is $n_k=c_k$. The central element $-1\in2I$ acts on $V_k$ as $(-1)^k$, so $c_k=0$ for odd $k$.

Combining the representation decomposition with the binary Molien coefficient gives
\[
\boxed{
d_k=(k+1)[t^k]\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
}
\]
There is no additional radial subtraction in this formula: $c_k$ is already the invariant dimension of the irreducible harmonic representation $V_k$ on the left factor, multiplied by the untouched right-factor dimension $k+1$. The radial Fischer subtraction belongs to the distinct four-real-variable polynomial Molien series, not to this two-dimensional binary Molien series.

## A.3 Independent character-average derivation

Fix the nine conjugacy classes in the exact quaternion audit convention:
\[
|C_j|=(1,1,20,30,12,12,20,12,12),
\]
and the defining character values
\[
\chi_1=(2,-2,-1,0,\varphi-1,-\varphi,1,\varphi,1-\varphi),
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]
The character of $V_k=\operatorname{Sym}^k(\mathbb C^2)$ obeys the exact recurrence
\[
\chi_0(g)=1,\quad \chi_1(g)\text{ as above},\quad
\chi_k(g)=\chi_1(g)\chi_{k-1}(g)-\chi_{k-2}(g).
\]
The Reynolds projector
\[
P_k=\frac1{120}\sum_{g\in2I}D^k(g)
\]
has image $V_k^{2I}$. Taking its trace and grouping by conjugacy classes yields
\[
\boxed{
n_k=\frac1{120}\sum_{j=1}^{9}|C_j|\chi_k(C_j).
}
\]
The exact audit evaluates this expression in $\mathbb Q(\sqrt5)$ and compares it, degree by degree, with the integer coefficient count $c_k$. The comparison passes for all $121$ degrees $0\le k\le120$. It uses the class sizes and fundamental quaternionic character, not the real four-dimensional Molien determinant expansion.

## A.4 Verified initial spectrum

For $0\le k\le120$, the nonzero degrees and multiplicities are listed below. The eigenvalue is $\lambda_k=k(k+2)$.

| $k$ | $\lambda_k$ | $n_k=c_k$ | $d_k=(k+1)n_k$ |
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
| 62 | 3968 | 1 | 63 |
| 64 | 4224 | 1 | 65 |
| 66 | 4488 | 1 | 67 |
| 68 | 4760 | 1 | 69 |
| 70 | 5040 | 1 | 71 |
| 72 | 5328 | 2 | 146 |
| 74 | 5624 | 1 | 75 |
| 76 | 5928 | 1 | 77 |
| 78 | 6240 | 1 | 79 |
| 80 | 6560 | 2 | 162 |
| 82 | 6888 | 1 | 83 |
| 84 | 7224 | 2 | 170 |
| 86 | 7568 | 1 | 87 |
| 88 | 7920 | 1 | 89 |
| 90 | 8280 | 2 | 182 |
| 92 | 8648 | 2 | 186 |
| 94 | 9024 | 1 | 95 |
| 96 | 9408 | 2 | 194 |
| 98 | 9800 | 1 | 99 |
| 100 | 10200 | 2 | 202 |
| 102 | 10608 | 2 | 206 |
| 104 | 11024 | 2 | 210 |
| 106 | 11448 | 1 | 107 |
| 108 | 11880 | 2 | 218 |
| 110 | 12320 | 2 | 222 |
| 112 | 12768 | 2 | 226 |
| 114 | 13224 | 2 | 230 |
| 116 | 13688 | 2 | 234 |
| 118 | 14160 | 1 | 119 |
| 120 | 14640 | 3 | 363 |

All odd degrees have zero multiplicity. In particular,
\[
\boxed{\lambda_1^+=168,\qquad d(168)=13.}
\]
At degree $120$, $c_{120}=3$ and $d_{120}=121\cdot3=363$.

## A.5 Scope and exclusions

This record proves the scalar multiplicity formula for the specified left action and records an exact finite comparison through degree $120$. It does not infer a new physical mechanism from the eigenvalue sequence.

The following are deliberately not used as steps in this proof: a separate $A_5$-invariant three-dimensional Hilbert series; a variable substitution between that series and the binary series; a proposed $2:3:5$ interpretation; or unverified secondary web references. The quotient $2I/\{\pm1\}\cong A_5$ is a standard group-theoretic fact, but no separate $S^2$ invariant problem is needed for this scalar spectrum on $S^3/2I$.

The radial Fischer decomposition remains relevant only to the real polynomial Molien audit in [the exact real Molien record](../audits/2i_real_molien_exact/README.md). It must not be mixed with the two-dimensional binary Molien calculation above.

## A.6 Reproduction and evidence boundary

From the repository root:
\`\`\`bash
python -m audits.a1_poincare_scalar_spectrum --max-degree 120
python -m unittest tests.test_a1_poincare_scalar_spectrum -v
\`\`\`

The audit uses the nine class sizes and defining character in the T035 convention, constructs symmetric-power characters by recurrence, and compares the Reynolds character average against the binary Molien coefficient count at every degree. The class data are recorded explicitly in the audit so this check does not depend on importing the legacy T035 script. GitHub Actions run [43879748053](https://github.com/fabianleonaressi95/theorem/actions/runs/43879748053) completed successfully: all three tests passed.

**Classification**
- **Proved:** $d_k=(k+1)\dim(V_k^{2I})$, the Reynolds character-average formula, and the binary Molien coefficient formula under the stated action.
- **Exact finite audit passed in CI:** equality of the two calculations for $0\le k\le120$ (121 degrees; three regression tests passed).
- **Open in this record:** vector/tensor spectra, Rumin operators and analytic torsion, and any proposed relation to the Pellis Functions or McKay correspondence beyond established representation-theoretic facts.

## A.7 McKay correspondence: exact citations and evidence map

The McKay correspondence is used here as the representation-theoretic organization of the nine irreducible representations of $2I$ and their tensor products with the defining two-dimensional representation. For $2I$, its McKay graph is the affine Dynkin diagram $\widetilde E_8$.

### A.7.1 Primary project record: GAP session

The archived transcript is [GAP\_sessione\_2A5\_McKay\_2I.pdf](../GAP_sessione_2A5_McKay_2I.pdf) (GAP 4.11.1 session; 24 pages). The exact page references are:

| PDF pages | Exact content | How it is cited here |
|---|---|---|
| **1** | GAP character table for $2.A5$; nine irreducible characters; degrees; orthogonality check; selection of the faithful degree-two character; power-map check distinguishing the $5a,5b,10a,10b$ classes | Computational record for the class/character-table convention and the chosen defining character |
| **1–2** | McKay adjacency matrix obtained from character inner products; symmetry check; dimension vector $d=(1,2,3,4,5,6,4,2,3)$; check $Ad=2d$; eight edges | Computational record of the affine-$E_8$ graph |
| **2–3** | Symmetric-power character recurrence; multiplicity decomposition; invariant coefficient comparison with $(1+t^{30})/((1-t^{12})(1-t^{20}))$; scalar spectrum through degree 60; sum of listed spectral multiplicities $677$ | Computational cross-check of the low-degree scalar spectrum and invariant multiplicities |
| **15–16** | Character-class Molien average for the faithful two-dimensional character; rational function simplified and cross-multiplied against the Klein binary Molien expression; explicit Fischer/radial subtraction in four real variables | Computational record distinguishing the binary invariant series from the four-real-variable polynomial-to-harmonic subtraction |
| **16–18** | Coefficient comparison between the four-variable harmonic dimensions and $(k+1)c_k$ through degree 30 | Finite comparison recorded in the transcript; it is not the all-degree proof |
| **19** | Repeated exact class-character recurrence and coefficient output through degree 30 | Additional transcript evidence for the binary Molien coefficients |
| **20–24** | Quaternion-list construction attempts, matrix-action experiments and group identification as $SL(2,5)$ | Historical working transcript only; several commands fail or return **false**, so these pages are **not cited as a successful certificate** of quaternion closure or of the polynomial matrix action |

**Class-order convention (do not silently mix columns).** The GAP table on PDF p. 1 uses the order
\[
(1a,2a,4a,3a,6a,5a,10a,5b,10b),
\]
whereas A.3 and the T035-based character audit use
\[
(1,2,3,4,5a,5b,6,10a,10b).
\]
The conversion of class labels is therefore
\[
(1,2,3,4,5a,5b,6,10a,10b)_{\rm A.3}
\longleftrightarrow
(1a,2a,3a,4a,5a,5b,6a,10a,10b)_{\rm GAP}.
\]
In particular, the third and fourth columns, and the positions of the order-six and order-ten classes, are not in the same order. The class-size and character tuples must always be permuted together. The GAP PDF is cited for its own displayed ordering; A.3 retains the T035 ordering.

**Important evidence qualification.** The PDF is a raw computational session transcript, not a polished proof. It contains successful outputs as well as syntax errors, failed commands and false tests. In particular, pages 5–11 contain unsuccessful polynomial-action implementations; pages 22–24 contain a failed closure check for one quaternion list, followed by a successful abstract identification of $SL(2,5)$ of order 120 with center of order 2 and nine conjugacy classes. We cite only the successful outputs identified in the table above. We do not cite the failed experiments as evidence.

### A.7.2 Exact theorem and code references in this repository

1. **T026 — [McKay–$E_8$ recurrence for all nine $2I$ multiplicities](../theorems/T026-mckay-e8-2i-multiplicities.md).** The exact node order is $(\mathbf1,2_s,3,4_s,5,6_s,4,2'_s,3')$, with dimension vector $(1,2,3,4,5,6,4,2,3)$ and edges
   $$
   \mathbf1-2_s-3-4_s-5-6_s-4-2'_s,\qquad 6_s-3'.
   $$
   The recurrence is $n(0)=e_{\mathbf1}$, $n(1)=e_{2_s}$, $n(m+1)=An(m)-n(m-1)$. The script is [audits/t026_mckay_e8_multiplicities.py](../audits/t026_mckay_e8_multiplicities.py); its documented reproduction command is: python audits/t026_mckay_e8_multiplicities.py --max-degree 120 --json.

2. **T027 — [Exact McKay–Molien bridge for the nine Rumin twists](../theorems/T027-mckay-molien-rumin-bridge.md).** This fixes the label correspondence from T026 to T021–T023, notably $4_s\leftrightarrow4'$ (not $4$), and checks all nine covariant coefficient sequences against the McKay recurrence. The script is [audits/t027_mckay_molien_bridge.py](../audits/t027_mckay_molien_bridge.py); its documented command is: python audits/t027_mckay_molien_bridge.py --max-degree 240 --json.

3. **Standalone mathematical overview — [McKay correspondence for the binary icosahedral group](../theorems/spectral/mckay_affine_e8_binary_icosahedral.md).** This records the graph, tensor products, recurrence and its precise use in the scalar spectrum. It explicitly distinguishes the all-degree representation-theoretic identities from finite script checks.

### A.7.3 Published references

- J. McKay, “Graphs, singularities, and finite groups,” *Proceedings of Symposia in Pure Mathematics* **37** (1980), 183–186. This is the original source for the McKay graph correspondence.
- P.-P. Dechant, “The birth of $E_8$ out of the spinors of the icosahedron,” *Proceedings of the Royal Society A* **472** (2016), 20150504. DOI: [10.1098/rspa.2015.0504](https://doi.org/10.1098/rspa.2015.0504). See §5 and Figure 1 for the binary-icosahedral spinor construction and the affine-$E_8$ McKay graph.
- F. Klein, *Vorlesungen über das Ikosaeder und die Auflösung der Gleichungen vom fünften Grade*, B. G. Teubner, Leipzig, 1884. Classical source for the icosahedral invariant theory; the binary invariant Hilbert series used in A.2 is the Klein invariant-theory input.
- A. Ikeda, “On the spectrum of a Riemannian manifold of positive constant curvature,” *Osaka Journal of Mathematics* **17** (1980), 75–93. [Original article (Osaka University repository)](https://ir.library.osaka-u.ac.jp/repo/ouka/all/5171/ojm17_01_08.pdf). Reference for spectral analysis of spherical space forms.
- A. Kitaoka, “Analytic torsions associated with the Rumin complex on contact spheres,” *International Journal of Mathematics* **31** (2020), 2050112. [arXiv:1911.03092](https://arxiv.org/abs/1911.03092). Reference for the Rumin spectral blocks used later in the document.
- M. Rumin and N. Seshadri, “Analytic torsions on contact manifolds,” *Annales de l’Institut Fourier* **62** (2012), 727–782. DOI: [10.5802/aif.2693](https://doi.org/10.5802/aif.2693).

### A.7.4 Citation protocol for the joint manuscript

Use the following citation granularity:

- For the **computed McKay adjacency matrix and GAP character-table convention**: cite *GAP session, pp. 1–2*.
- For the **initial symmetric-power decompositions and scalar eigenvalue/multiplicity list through $k=60$**: cite *GAP session, pp. 2–3*.
- For the **binary Molien class average and the radial Fischer distinction**: cite *GAP session, pp. 15–16*.
- For the **finite harmonic-coefficient comparison through degree 30**: cite *GAP session, pp. 16–18*.
- For the **mathematical affine-$E_8$ correspondence and exact all-degree recurrence**: cite McKay (1980), Dechant (2016, §5 and Fig. 1), and repository theorem T026. The GAP transcript is supporting computational evidence, not the source of the general theorem.
- For the **nine Molien covariant sectors and their Rumin multiplicity bridge**: cite T027 and its audit script, together with T021–T025 for the underlying spectral blocks. Do not cite the GAP PDF as proof of the analytic torsion formula.

**Classification.** The affine-$E_8$ correspondence and Clebsch–Gordan recurrence are established representation theory; the repository scripts provide exact finite integer audits at their stated cutoffs; the GAP PDF is a mixed transcript whose successful and failed portions must be distinguished page by page. No new McKay correspondence or completed analytic torsion theorem is claimed here.
