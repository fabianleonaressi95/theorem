# T119 — Binary icosahedral group and selected representations

**Classification:** standard algebraic group/representation statements, accompanied by floating-point exhaustive repository audits (not a formal proof-assistant certificate).

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

**Source:** `src/binary_icosahedral.py`, `src/representations_2i.py`. **Tests:** `tests/test_binary_icosahedral.py`, `tests/test_representations_2i.py`. The audit checks all 14,400 quaternion products numerically, inverses, norms, the 60-element SO(3) quotient, representation homomorphisms/unitarity, central action and selected intertwiner dimensions. The implementation uses floating-point coordinates and tolerances, so these checks are numerical certificates rather than exact-arithmetic formal verification.

**Boundary:** \(\rho_2\) does not automatically identify the Möbius orientation cocycle with \(-1\in2I\), construct a Pin structure, or show that a Q6 connection has holonomy group \(2I\).