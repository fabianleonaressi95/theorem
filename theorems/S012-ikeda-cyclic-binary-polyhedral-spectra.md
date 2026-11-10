# S012 — Ikeda (1995): cyclic and binary-polyhedral scalar spectra

**Classification:** independent derivation, checked against Ikeda's printed theorem statements and subgroup decompositions.  
**Primary source:** Akira Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Mathematical Journal* 18 (1995), 57–67. Repository source: [18_57.pdf](../18_57.pdf). Publisher PDF: https://www.jstage.jst.go.jp/article/kodaimath1978/18/1/18_1_57/_pdf/-char/en.

## 1. Notation: keep the two indices separate

For the unit sphere \(S^{2n-1}\), a spherical harmonic of degree \(r\) has eigenvalue
\[
\lambda_r=r(r+2n-2).
\]
For a binary subgroup \(G\subset SU(2)\) acting on \(S^3\), the central element \(-I\) kills odd harmonic degrees. Write the surviving degree as \(r=2k\). Then
\[
\lambda_k=(2k)(2k+2)=4k(k+1),
\]
and the multiplicity is indexed by \(k\), not by the full harmonic degree \(r\).

This index conversion is essential when comparing Theorems 4.2–4.6 and 5.1. The general binary-group parts (2) of Ikeda's Theorems 4.3–4.6 concern \(S^{4n-1}\) with Ikeda's quaternionic dimension \(n>1\). The three-dimensional parts (1) concern \(S^3\), corresponding to the boundary case \(n=1\); Lemma 2.6 is not available in that boundary case.

## 2. Theorem 4.2 — homogeneous lens spaces

Let \(q\ge2\), \(n\ge2\), and let \(\mathbb Z_q\) act on \(\mathbb C^n\) by scalar multiplication. The eigenvalues are
\[
\lambda_r=r(r+2n-2),\qquad r\ge0,
\]
with \(a_0=1\), \(a_1=0\), and, for \(r\ge2\),
\[
a_r(n,q)=\frac{n-1+r}{n-1}
\sum_{\substack{0\le l\le r\\r\equiv2l\pmod q}}
\binom{n-2+r-l}{n-2}
\binom{n-2+l}{n-2}.
\]

### Proof

Let \(H_r\) be the degree-\(r\) spherical harmonics on \(S^{2n-1}\). The harmonic decomposition and the standard sphere spectrum give
\[
L^2(S^{2n-1})=\widehat{\bigoplus}_{r\ge0}H_r,\qquad
-\Delta|_{H_r}=r(r+2n-2).
\]
For \(\zeta=e^{2\pi i/q}\), the generator \(\zeta I\) has complex eigenvalues \(\zeta,\bar\zeta\), each with multiplicity \(n\), on the complexification of the real representation. The harmonic Poincaré series is therefore
\[
F_q(n,z)=\frac1q\sum_{t=1}^q
\frac{1-z^2}{(1-\zeta^t z)^n(1-\zeta^{-t}z)^n}.
\]
Expanding both factors by the negative-binomial series gives the coefficient before multiplication by \(1-z^2\):
\[
b_r=\sum_{l=0}^r
\binom{n-1+r-l}{n-1}
\binom{n-1+l}{n-1}
\left(\frac1q\sum_{t=1}^q\zeta^{t(r-2l)}\right).
\]
The roots-of-unity filter makes the parenthesis equal to \(1\) exactly when \(r\equiv2l\pmod q\), and zero otherwise. Since \(a_r=b_r-b_{r-2}\), reindexing the second sum by \(l\mapsto l-1\) gives, term by term,
\[
\begin{aligned}
&\binom{n-1+r-l}{n-1}\binom{n-1+l}{n-1}\\
&\quad-\binom{n-2+r-l}{n-1}\binom{n-2+l}{n-1}\\
&=\frac{n-1+r}{n-1}
\binom{n-2+r-l}{n-2}\binom{n-2+l}{n-2}.
\end{aligned}
\]
At the endpoints \(l=0,r\), the out-of-range term in \(b_{r-2}\) is interpreted as zero; the displayed identity still holds. This proves the multiplicity formula.

Every summand in the final formula is positive. Thus \(a_r>0\) precisely when the congruence \(r\equiv2l\pmod q\), \(0\le l\le r\), has a solution:
- if \(q\) is even, this is equivalent to \(r\) being even;
- if \(q\) is odd, it is equivalent to \(r\) being even, or \(r\) being odd with \(r\ge q\).

This is Ikeda's Theorem 4.2 (pp. 61–62); the proof above is the independent coefficient derivation from the preliminary propositions.

## 3. Binary dihedral group — Theorem 4.3(1)

Use Ikeda's notation \(D_m^*\), of order \(4m\), \(m>1\). Proposition 3.1(1) decomposes it into one cyclic subgroup of order \(2m\) and \(m\) cyclic subgroups of order \(4\), with common intersection the central \(C_2\). Inclusion–exclusion in the normalized cyclic Poincaré series gives
\[
F_{D_m^*}(z)
=\frac12F_{2m}(2,z)+F_4(2,z)-\frac12F_2(2,z)
=\frac12F_{2m}(2,z)+\frac12\frac{1-z^2}{(1+z^2)^2}.
\]
The last identity follows directly from the cyclic averages for orders \(2\) and \(4\).

Only even full harmonic degrees \(r=2k\) occur. In degree \(2k\), the cyclic \(2m\)-average counts the integers \(l\in[0,2k]\) with \(l\equiv k\pmod m\); there are \(2\lfloor k/m\rfloor+1\). The coefficient of \(z^{2k}\) in \((1-z^2)/(1+z^2)^2\) is \((-1)^k(2k+1)\). Combining the two terms yields
\[
a_k(D_m^*)=
\begin{cases}
(2k+1)\bigl(\lfloor k/m\rfloor+1\bigr),& k\ \text{even},\\[2mm]
(2k+1)\lfloor k/m\rfloor,& k\ \text{odd and }k\ge m,\\[1mm]
0,& k\ \text{odd and }k\le m.
\end{cases}
\]
The eigenvalue is \(4k(k+1)\). The odd branch begins at \(k\ge m\), not strictly \(k>m\): at the endpoint \(k=m\) (when (m) is odd), the coefficient count gives multiplicity \(2m+1\). The scan/OCR glyph at this threshold is ambiguous, so the endpoint is fixed by the exact coefficient calculation. This is the piecewise structure in Ikeda's Theorem 4.3(1), p. 62. Positivity is manifest in this formula; no appeal to Lemma 2.6 is needed for the three-dimensional case.

## 4. Binary tetrahedral group — Theorem 4.4(1)

This case is recorded in detail in [S011](S011-ikeda-binary-tetrahedral-spectrum.md). The normalized subgroup inclusion–exclusion identity is
\[
F_{T^*}=F_6+\frac12F_4-\frac12F_2.
\]
The independent Molien series is
\[
M_{T^*}(z)=\frac{1+z^{12}}{(1-z^6)(1-z^8)}.
\]
Writing \(r=2k\), the multiplicity is
\[
a_k(T^*)=(2k+1)
\left(1+2\left\lfloor\frac{k}{3}\right\rfloor
+\left\lfloor\frac{k}{2}\right\rfloor-k\right).
\]
It vanishes exactly at \(k=1,2,5\). The first positive eigenvalue is \(48\), with multiplicity \(7\).

**Dimensional correction:** Theorem 4.4(1) is the three-dimensional \(S^3/T^*\) case. Theorem 4.4(2) is separately stated for \(S^{4n-1}/T^*\), \(n>1\). The latter must not be specialized to \(n=1\) and then cited as the proof of part (1).

## 5. Binary octahedral group — Theorem 4.5(1)

Proposition 3.1(3) decomposes \(O^*\) into three cyclic subgroups of order \(8\), four of order \(6\), and six of order \(4\), all sharing the central \(C_2\). The subgroup sum counts the central subgroup thirteen times, so twelve excess copies are removed. Since \(|O^*|=48\),
\[
F_{O^*}(z)=\frac12\bigl(F_8(2,z)+F_6(2,z)+F_4(2,z)-F_2(2,z)\bigr).
\]
The corresponding Molien series simplifies to
\[
M_{O^*}(z)=\frac{1+z^{18}}{(1-z^8)(1-z^{12})}.
\]
With \(x=z^2\), its coefficient at \(x^k\) is
\[
c_k(O^*)=
1+\left\lfloor\frac{k}{4}\right\rfloor
+\left\lfloor\frac{k}{3}\right\rfloor
+\left\lfloor\frac{k}{2}\right\rfloor-k.
\]
Consequently
\[
a_k(O^*)=(2k+1)c_k(O^*),
\qquad \lambda_k=4k(k+1).
\]
The zero indices are \(k=1,2,3,5,7,11\), as in Ikeda's Theorem 4.5(1), pp. 64–65. The first positive index is \(k=4\), giving eigenvalue \(80\), multiplicity \(9\).

## 6. Binary icosahedral group — Theorem 4.6(1)

Proposition 3.1(4) decomposes \(I^*\) into six cyclic subgroups of order \(10\), ten of order \(6\), and fifteen of order \(4\), all sharing the central \(C_2\). There are thirty excess copies of the center in the subgroup sum. Since \(|I^*|=120\),
\[
F_{I^*}(z)=\frac12\bigl(F_{10}(2,z)+F_6(2,z)+F_4(2,z)-F_2(2,z)\bigr).
\]
The Molien series is
\[
M_{I^*}(z)=\frac{1+z^{30}}{(1-z^{12})(1-z^{20})}.
\]
Writing \(x=z^2\), the coefficient at \(x^k\) is
\[
c_k(I^*)=
1+\left\lfloor\frac{k}{5}\right\rfloor
+\left\lfloor\frac{k}{3}\right\rfloor
+\left\lfloor\frac{k}{2}\right\rfloor-k.
\]
Thus
\[
a_k(I^*)=(2k+1)c_k(I^*),
\qquad \lambda_k=4k(k+1).
\]
The zero indices are
\[
1,2,3,4,5,7,8,9,11,13,14,17,19,23,29,
\]
as in Ikeda's Theorem 4.6(1), p. 65. The first positive index is \(k=6\), giving eigenvalue \(168\), multiplicity \(13\).

## 7. Theorem 5.1(1) — first nonzero eigenvalues in dimension three

The first positive indices follow directly from the formulas above.

| Quotient | First positive index | First positive eigenvalue | Multiplicity |
|---|---:|---:|---:|
| \(S^3/\mathbb Z_2\) | full degree \(r=2\) | 8 | 9 |
| \(S^3/\mathbb Z_q,\ q>2\) | full degree \(r=2\) | 8 | 3 |
| \(S^3/D_2^*\) | \(k=2\) | 24 | 10 |
| \(S^3/D_m^*,\ m>2\) | \(k=2\) | 24 | 5 |
| \(S^3/T^*\) | \(k=3\) | 48 | 7 |
| \(S^3/O^*\) | \(k=4\) | 80 | 9 |
| \(S^3/I^*\) | \(k=6\) | 168 | 13 |

For the two lens rows, the index \(r\) is the full spherical-harmonic degree and the eigenvalue is \(r(r+2)\). For the binary rows, \(k\) is half the full degree and the eigenvalue is \(4k(k+1)\). This distinction prevents an apparent index mismatch in the table.

The first-eigenvalue sequence agrees with the three-dimensional list in Ikeda's Theorem 5.1 (pp. 66–67). The multiplicities in this table are independently recovered from Theorems 4.2–4.6 above; in particular, the (m=2) versus (m>2) dihedral multiplicity distinction is read from the explicit formula in Theorem 4.3(1), not inferred from the OCR layout of the summary table.

## 8. Correct use and non-use of Lemma 2.6

Lemma 2.6 is stated for Ikeda's higher-dimensional binary-group calculation with \(n>1\), where the binomial parameter \(N=2n-2\) is positive. It can be used to compare the paired binomial terms in the general \(S^{4n-1}/P^*\) formulas (parts (2) of Theorems 4.3–4.6).

It **cannot** be invoked to prove positivity in the three-dimensional cases (parts (1)): there \(S^3=S^{4\cdot1-1}\), so Ikeda's quaternionic parameter is \(n=1\) and \(N=0\). The three-dimensional positivity statements are instead established directly by the explicit floor-function formulas above. In particular, the phrase “the central binomial term dominates” is not a substitute for the coefficient calculation and is removed from the proof record.

## 9. Status register

| Result | Status |
|---|---|
| Lemmas 2.1–2.3 and Propositions 2.4–2.5 | Independent coefficient derivations |
| Lemma 2.6 | Strict monotonicity proved for its stated \(N>0\) range |
| Proposition 4.1 | Reynolds averaging formula proved |
| Theorem 4.2 | Full coefficient derivation; source statement checked |
| Theorem 4.3(1), \(S^3/D_m^*\) | Explicit formula reconstructed and checked against source |
| Theorem 4.4(1), \(S^3/T^*\) | Source formula and independent Molien reconstruction; see S011 |
| Theorem 4.5(1), \(S^3/O^*\) | Explicit formula reconstructed and checked against source |
| Theorem 4.6(1), \(S^3/I^*\) | Explicit formula reconstructed and checked against source |
| Theorem 5.1(1), dimension three | First eigenvalues and multiplicities recovered |
| Theorems 4.3(2), 4.4(2), 4.5(2), 4.6(2), \(S^{4n-1}\), \(n>1\) | **Not yet closed here**; require separate transcription and term-by-term verification of the higher-dimensional binomial formulas |

**Scope:** this record closes the three-dimensional parts (1) of Theorems 4.3–4.6 and Theorem 5.1(1), plus the general cyclic Theorem 4.2. It does not claim that the higher-dimensional parts (2) have been proved.
