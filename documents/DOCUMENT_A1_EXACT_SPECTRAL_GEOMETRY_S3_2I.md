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

The audit imports the exact class convention and $\mathbb Q(\sqrt5)$ quaternionic data from T035, constructs symmetric-power characters by recurrence, and compares the Reynolds character average against the binary Molien coefficient count at every degree. The test source is included; a GitHub Actions pass is not claimed until a corresponding run is observed.

**Classification**
- **Proved:** $d_k=(k+1)\dim(V_k^{2I})$, the Reynolds character-average formula, and the binary Molien coefficient formula under the stated action.
- **Exact finite audit specified:** equality of the two calculations for $0\le k\le120$.
- **Open in this record:** vector/tensor spectra, Rumin operators and analytic torsion, and any proposed relation to the Pellis Functions or McKay correspondence beyond established representation-theoretic facts.
