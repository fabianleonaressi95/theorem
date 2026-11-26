# T119 — Binary icosahedral group and selected representations

**Classification:** standard algebraic group/representation statements, with an exact-arithmetic finite audit of the quaternionic left action and separate numerical source audits for the selected representation code.

Let \(\varphi=(1+\sqrt5)/2\). The standard 600-cell vertex set in \(\mathbb R^4\) consists of the 8 coordinate units, 16 points \((\pm1/2,\pm1/2,\pm1/2,\pm1/2)\), and 96 even permutations of \((0,1/2,\varphi/2,1/(2\varphi))\) with independent signs on the nonzero coordinates. All are unit quaternions since \((1+\varphi^2+\varphi^{-2})/4=1\). Under Hamilton multiplication this is the binary icosahedral group \(2I\) of order 120, with central quotient \(2I/\{\pm1\}\cong A_5\).

Using scalar-first \(q=(w,x,y,z)\), the defining complex representation is
\[
\rho_2(q)=\begin{pmatrix}w-iz&-y-ix\\y-ix&w+iz\end{pmatrix}\in SU(2).
\]
The vector representation \(\rho_3:2I\to SO(3)\) is the usual quaternion rotation action; the third selected representation is trivial. Their central actions are
\[
\rho_2(-1)=-I_2,\quad \rho_3(-1)=I_3,\quad \rho_0(-1)=1.
\]
Thus the fundamental representation does not factor through \(A_5\), while the vector and trivial representations do.

The three selected representations are irreducible and pairwise inequivalent over \(\mathbb C\). Schur's lemma gives \(\dim_\mathbb C\mathrm{Hom}_{2I}(V,W)=1\) for equal selected irreducibles and 0 for distinct ones. This is not a complete irreducible catalogue or character table.

**Source:** `src/binary_icosahedral.py`, `src/representations_2i.py`. **Tests:** `tests/test_binary_icosahedral.py`, `tests/test_representations_2i.py`. The earlier source audit checked quaternion products, inverses, norms, the 60-element SO(3) quotient, representation homomorphisms/unitarity, central action and selected intertwiner dimensions using floating-point coordinates and tolerances. Those checks remain numerical. The quaternionic group closure and real four-dimensional Molien computation are now separately covered by the exact-arithmetic audit in §12 below.

**Boundary:** \(\rho_2\) does not automatically identify the Möbius orientation cocycle with \(-1\in2I\), construct a Pin structure, or show that a Q6 connection has holonomy group \(2I\).


## Exact quaternionic closure and real Molien audit (16 November 2026)

The earlier floating-point product audit cited above is superseded for the quaternionic vertex set by the exact-arithmetic audit in [\`audits/2i_real_molien_exact/README.md\`](../audits/2i_real_molien_exact/README.md). The corrected 96-point construction applies independent signs to the three nonzero coordinates **after** each even permutation, wherever those coordinates occur. Applying signs only to fixed coordinate positions 2–4 is incorrect when the zero coordinate moves.

The new implementation represents each coordinate as \(r+s\sqrt5\), with \(r,s\in\mathbb Q\). It checks:
- 120 distinct elements and unit norm for every quaternion;
- all 14,400 Hamilton products for exact closure;
- all 120 quaternionic inverses;
- all 120 real left-multiplication matrices \(L_q\);
- the exact determinant identity
  \[
  \det(I-tL_q)=(1-2\operatorname{Re}(q)t+t^2)^2
  \]
  by a \(4\times4\) Leibniz determinant expansion over \(\mathbb Q(\sqrt5)\).

The direct real Molien sum is
\[
M_{\mathbb R^4}(t)=\frac1{120}\sum_{q\in2I}
\frac1{(1-2\operatorname{Re}(q)t+t^2)^2}.
\]
Its coefficients through degree 60 are computed from the exact reciprocal-determinant recurrences. They agree degree by degree with the independently specified Klein coefficient count and the harmonic/Fischer formula recorded in S013. The complete rational-function simplification is also available as an optional exact SymPy check.

**Status update:** the 120-element quaternionic group and its real \(4\)-dimensional left-action Molien computation now have an exact-arithmetic reproducibility path. This upgrades the former floating-point closure check; it does not change the boundary on physical interpretation or Q6 coupling.


## Extended exact Molien verification (16 November 2026)

The exact quaternionic real-Molien audit has been extended from degree 60 to degree 240. The direct finite sum is evaluated with rational arithmetic in \(\mathbb Q(\sqrt5)\); group closure, determinant expansion, and reciprocal-series coefficient averaging remain exact. All coefficients \(m_n\) for \(0\le n\le240\) agree with the Peter–Weyl/Fischer expression in S013.

Selected real-polynomial Molien coefficients are
\[
m_{60}=677,\quad m_{120}=5073,\quad m_{144}=8708,
\quad m_{180}=16789,\quad m_{200}=22943,
\quad m_{216}=28829,\quad m_{240}=39425.
\]
These are not the spherical multiplicities themselves: those are \(d_n=(n+1)c_n\). The command-line audit and regression test now use degree 240. See [the audit record](../audits/2i_real_molien_exact/README.md).
