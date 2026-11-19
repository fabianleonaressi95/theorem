# T142 — Antipodal six-state model of the Vesica hexagon and geometric mixing

**Record type:** exact finite-dimensional operator theorem.  
**Status:** the six-point geometry, antipodal decomposition, operator identities, and block ranks are proved exactly. The Q6 transfer and any physical PSU–Anti-Twin interpretation remain open.

## 1. Scope and relation to the Vesica theorem

This record does **not** re-prove the Vesica chord theorem and does not introduce a new value of its constant. The exact equal-circle Vesica result is recorded in [T137](T137-vesica-piscis-two-circle-hexagon-pi-sqrt3.md): for circle radius \(R\), the common chord has length \(\sqrt3R\).

Here we study a finite six-point configuration that packages a third-roots triangle and its antipodal image. The ratio \(\sqrt3\) below is stated precisely as the ratio between a side of the triangle \(T\) and a side of the regular hexagon \(\mathcal H\). This is a geometric correspondence, not a second proof of the Vesica theorem.

## 2. Six-point configuration

Let
\[
\omega=e^{2\pi i/3},\qquad \omega^3=1,\qquad
1+\omega+\omega^2=0,
\]
and define
\[
T=\{1,\omega,\omega^2\},\qquad
\mathcal H=T\cup(-T)
=\{\pm1,\pm\omega,\pm\omega^2\}.
\]
The six elements of \(\mathcal H\) are the vertices of the regular unit hexagon. Its side length is
\[
|1-e^{i\pi/3}|=1.
\]
The three points of \(T\) form an equilateral triangle, since
\[
|1-\omega|=|\omega-\omega^2|=|\omega^2-1|=\sqrt3.
\]
Thus
\[
\boxed{\frac{\text{side length of }T}
{\text{side length of }\mathcal H}=\sqrt3.}
\]
The antipodal map \(z\mapsto-z\) exchanges \(T\) and \(-T\).

## 3. Hilbert space and antipodal sectors

Let
\[
\mathscr H=\ell^2(\mathcal H)
\]
with orthonormal point basis \(\{\delta_z:z\in\mathcal H\}\). Define
\[
(Jf)(z)=f(-z).
\]
Then
\[
J^\dagger=J,\qquad J^2=I.
\]
The orthogonal projections onto the even and odd antipodal sectors are
\[
P_\pm=\frac{I\pm J}{2},\qquad
\mathscr H=\mathscr H_+\oplus\mathscr H_-,
\qquad \dim\mathscr H_+=\dim\mathscr H_-=3.
\]

For \(k=0,1,2\), choose the representatives
\[
z_0=1,\qquad z_1=\omega,\qquad z_2=\omega^2
\]
of the three antipodal pairs, and set
\[
e_k^+=\frac{\delta_{z_k}+\delta_{-z_k}}{\sqrt2},
\qquad
e_k^-=\frac{\delta_{z_k}-\delta_{-z_k}}{\sqrt2}.
\]
These are orthonormal bases of \(\mathscr H_+\) and \(\mathscr H_-\), respectively.

## 4. Geometric coordinate operators

Define the multiplication operators
\[
(Xf)(z)=\operatorname{Re}(z)f(z),\qquad
(Yf)(z)=\operatorname{Im}(z)f(z).
\]
Since their multipliers are real,
\[
X^\dagger=X,\qquad Y^\dagger=Y.
\]
Since \(|z|=1\) for every \(z\in\mathcal H\),
\[
\boxed{X^2+Y^2=I.}
\]
Moreover, \(\operatorname{Re}(-z)=-\operatorname{Re}(z)\) and
\(\operatorname{Im}(-z)=-\operatorname{Im}(z)\), so
\[
JXJ=-X,\qquad JYJ=-Y,
\]
or equivalently
\[
\boxed{\{J,X\}=0,\qquad \{J,Y\}=0.}
\]
Consequently both operators exchange the even and odd sectors:
\[
P_\pm XP_\pm=0,\qquad P_\pm YP_\pm=0.
\]

## 5. Exact off-diagonal blocks and their ranks

For every representative \(z_k\),
\[
Xe_k^+=\operatorname{Re}(z_k)e_k^-,
\qquad
Ye_k^+=\operatorname{Im}(z_k)e_k^-.
\]
Therefore, in the ordered bases \((e_0^+,e_1^+,e_2^+)\) and
\((e_0^-,e_1^-,e_2^-)\), the two off-diagonal blocks are
\[
[P_-XP_+]_{-+}
=\operatorname{diag}\left(1,-\frac12,-\frac12\right),
\]
and
\[
[P_-YP_+]_{-+}
=\operatorname{diag}\left(0,\frac{\sqrt3}{2},-\frac{\sqrt3}{2}\right).
\]
It follows directly, without inferring a block rank from invertibility on the full space, that
\[
\boxed{\operatorname{rank}(P_-XP_+)=3,\qquad
\operatorname{rank}(P_-YP_+)=2.}
\]
The singular values of the first block are \(1,\frac12,\frac12\); those of the second are \(\frac{\sqrt3}{2},\frac{\sqrt3}{2},0\).

The ranks are exact consequences of the displayed diagonal matrices. In particular, \(X\) is invertible on \(\mathscr H\), but the rank-three conclusion is established here by the explicit block calculation, not by invertibility alone.

## 6. What is and is not identified

The construction gives an exact finite-dimensional model with:
- a three-dimensional even sector and a three-dimensional odd sector;
- two Hermitian coordinate operators odd under the antipodal involution;
- an \(X\)-block of full rank and a \(Y\)-block of rank two;
- the exact identity \(X^2+Y^2=I\).

It does **not** by itself establish:
- a physical identification of \(\mathscr H_+\) with PSU and \(\mathscr H_-\) with Anti-Twin;
- a physical current or dynamical transfer law between those sectors;
- a canonical operator on all of \(\mathbb C^{64}\).

These are separate derivation problems.

## 7. Q6 transfer: precise open problem

Let \(J_{Q6}\) be the antipodal involution on \(\mathbb C^{64}\), induced by bitwise complementation \(x\mapsto x\oplus63\). A transfer must first specify an isometry
\[
\iota:\mathscr H\longrightarrow\mathbb C^{64},
\qquad \iota^\dagger\iota=I_6,
\qquad \iota J=J_{Q6}\iota.
\]
Then \(\iota\mathscr H\) is a six-dimensional \(J_{Q6}\)-invariant subspace, and
\[
\widetilde X_{\rm im}=\iota X\iota^\dagger,\qquad
\widetilde Y_{\rm im}=\iota Y\iota^\dagger
\]
are well-defined operators on \(\mathbb C^{64}\) whose restrictions to \(\iota\mathscr H\) are isometrically equivalent to \(X,Y\). They vanish on \((\iota\mathscr H)^\perp\). Thus these formulas define a zero extension, not a canonical extension to the whole Q6 space.

The intertwining relation implies
\[
J_{Q6}\widetilde X_{\rm im}J_{Q6}=-\widetilde X_{\rm im},
\qquad
J_{Q6}\widetilde Y_{\rm im}J_{Q6}=-\widetilde Y_{\rm im}.
\]
The next audit must verify the proposed \(\iota\), its isometry, antipodal intertwining, the image-subspace block ranks, and the action on the orthogonal complement. Any nonzero or otherwise structured extension on that complement must be specified separately and justified.

The previously proposed icosahedron-to-Q6 map is a distinct construction; it is not silently identified with this six-state map.

## 8. Reproducibility and evidence classification

Run:
\`\`\`bash
python scripts/audit_t142_vesica_antipodal_six_state.py
python -m unittest tests.test_t142_vesica_antipodal_six_state
\`\`\`

The audit uses floating-point matrix arithmetic to check the finite identities and ranks numerically. The proof of the block ranks and operator identities is the exact calculation in Sections 4–5; a script pass is not a substitute for that proof.

**Evidence labels**
- **Proved exactly:** hexagon/triangle distances; antipodal sector dimensions; Hermiticity; \(X^2+Y^2=I\); anticommutation with \(J\); explicit block matrices and ranks 3 and 2.
- **Numerically audited by the accompanying script:** finite matrix identities and numerical block ranks.
- **Open:** construction and audit of an isometric antipodal intertwiner into Q6; choice of extension on the Q6 orthogonal complement; physical PSU–Anti-Twin interpretation.
