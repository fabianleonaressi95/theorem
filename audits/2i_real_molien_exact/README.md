# Exact quaternionic \(2I\) real Molien audit

**Date:** 16 November 2026  
**Status:** exact finite computation in \(\mathbb Q(\sqrt5)\); the general Fischer/Peter–Weyl identity is proved independently in [S013, §§2.1 and 4](../../theorems/S013-general-spherical-space-form-molien-diagonal-actions.md).

## Construction

Write \(q=(a,b,c,d)=a+bi+cj+dk\), with coordinates in \(\mathbb Q(\sqrt5)\), and
\[
\varphi=\frac{1+\sqrt5}{2},\qquad \varphi^{-1}=\frac{\sqrt5-1}{2}.
\]
The vertex set used is the standard 600-cell set:
- the eight coordinate units \((\pm1,0,0,0)\) and their coordinate permutations;
- the sixteen points \((\pm\frac12,\pm\frac12,\pm\frac12,\pm\frac12)\);
- the 96 points obtained from the twelve even coordinate permutations of
  \((0,1,\varphi^{-1},\varphi)/2\), with independent signs on **all three nonzero coordinates wherever they occur**.

The last qualification matters: signs must not be applied only to coordinates 2–4 after permutation, because the zero coordinate moves under the permutation. The construction produces 120 distinct unit quaternions.

All arithmetic in the audit uses pairs of rational numbers \(r+s\sqrt5\), not floating-point rounding. The script checks all \(120^2=14{,}400\) Hamilton products for closure and checks all 120 quaternionic inverses.

## Real four-dimensional action and determinant

For scalar-first coordinates, left multiplication \(L_q:x\mapsto qx\) has matrix
\[
L_q=
\begin{pmatrix}
a&-b&-c&-d\\
b&a&-d&c\\
c&d&a&-b\\
d&-c&b&a
\end{pmatrix}.
\]
For \(a^2+b^2+c^2+d^2=1\), direct determinant expansion gives
\[
\boxed{\det(I-tL_q)=(1-2at+t^2)^2.}
\]
The script computes each \(4\times4\) determinant by the 24-term Leibniz formula over \(\mathbb Q(\sqrt5)\), then checks this identity for all 120 group elements. It expands the reciprocal determinant series by exact coefficient recurrence and averages the 120 series.

Thus the computed real Molien function is the exact finite sum
\[
M_{\mathbb R^4}(t)=\frac1{120}
\sum_{q\in2I}\frac1{(1-2\,\operatorname{Re}(q)t+t^2)^2}.
\]

## Result and independent comparison

Let
\[
A(t)=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}
=\sum_{\ell\ge0}c_\ell t^\ell,
\]
so, explicitly,
\[
c_\ell=\#\{(p,q,\epsilon)\in\mathbb Z_{\ge0}^2\times\{0,1\}:
12p+20q+30\epsilon=\ell\}.
\]
For the left action of \(2I\subset SU(2)\) on \(S^3\simeq SU(2)\), Peter–Weyl gives
\[
\dim\mathcal H_\ell(S^3)^{2I}=(\ell+1)c_\ell.
\]
The orthogonal Fischer decomposition
\(P_\ell(\mathbb R^4)=\mathcal H_\ell(\mathbb R^4)\oplus
r^2P_{\ell-2}(\mathbb R^4)\) then gives
\[
\boxed{
M_{\mathbb R^4}(t)=
\frac{A(t)+tA'(t)}{1-t^2}.
}
\]
This is a theorem under the specified orthogonal left action, not an empirical assumption. The direct 4D Molien computation is an independent finite-group check of the formula.

The exact coefficient comparison passes at every degree \(0\le n\le60\). The coefficients of the real Molien series in degrees 0–60 are:
\[
\begin{aligned}
(&1,0,1,0,1,0,1,0,1,0,1,0,14,0,14,0,14,0,14,0,35,0,35,0,60,0,60,0,60,0,91,0,124,0,124,0,161,0,161,0,202,0,245,0,290,0,290,0,339,0,390,0,443,0,498,0,555,0,555,0,677).
\end{aligned}
\]

The optional SymPy check simplifies the complete finite sum exactly and verifies the rational-function identity above, not merely a truncated series. The script remains runnable without SymPy; its core construction, closure, determinant and coefficient audit use only the Python standard library.

## Reproduction

From the repository root:

\`\`\`bash
python scripts/audit_2i_real_molien_exact.py
pytest -q tests/test_2i_real_molien_exact.py
\`\`\`

Files:
- [exact audit script](../../scripts/audit_2i_real_molien_exact.py)
- [regression tests](../../tests/test_2i_real_molien_exact.py)
- [T119 group record](../../theorems/T119-binary-icosahedral-group-and-selected-representations.md)
- [S013 general Molien framework](../../theorems/S013-general-spherical-space-form-molien-diagonal-actions.md)

**Evidence boundary:** this certifies the specified finite quaternionic group, its left real four-dimensional representation, and the stated Molien coefficients/rational identity. It does not by itself establish any additional physical interpretation or a new Q6 coupling.


## Extended exact range: degrees 61–240

The same exact-arithmetic audit has been extended to degree 240. No floating-point arithmetic is introduced: the group elements, Hamilton products, determinant polynomials, reciprocal-series recurrences, and the 120-term Molien average remain in \(\mathbb Q(\sqrt5)\) using rational pairs.

The implementation now compares all 241 coefficients, from degree 0 through degree 240 inclusive, against
\[
[t^n]\frac{A(t)+tA'(t)}{1-t^2}
=\sum_{j=0}^{\lfloor n/2\rfloor}(n-2j+1)c_{n-2j}.
\]
Selected exact integer coefficients are
\[
m_{60}=677,\quad m_{120}=5073,\quad m_{144}=8708,
\]
\[
m_{180}=16789,\quad m_{200}=22943,\quad
m_{216}=28829,\quad m_{240}=39425.
\]
These are coefficients of the **real four-variable polynomial Molien series**, not spherical-harmonic multiplicities. The latter are \(d_n=(n+1)c_n\); for example \(d_{60}=122\), whereas \(m_{60}=677\).

The regression test now executes the exact audit through degree 240 and checks the listed checkpoints. The command-line script also defaults to degree 240. The optional SymPy calculation still checks the complete rational-function identity, not just the truncation.
