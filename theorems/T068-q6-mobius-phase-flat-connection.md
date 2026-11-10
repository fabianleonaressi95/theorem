# T068 — Möbius phase action and the canonical flat connection on Q6

**Status:** exact finite-graph theorem and reproducible audit. The canonical equal-proper-time-slice connection is flat and gauge-trivial. A nontrivial physical connection is **not** derived: it requires vertex proper-time/phase data or an independently specified geometric transport law.

## 1. Scope and conventions

Let \(Q_6\) be the six-dimensional hypercube graph with vertex set
\[
V=(\mathbb Z_2)^6,
\]
and edges \(v\leftrightarrow v\oplus e_k\), \(k=0,\ldots,5\). There are \(64\) vertices, \(192\) unoriented edges, and \(240\) elementary square 2-cells. For an oriented edge write \(U_{vw}\in U(1)\), with \(U_{wv}=U_{vw}^{-1}\).

This record separates (i) the exact projective action of phase translations, (ii) the connection obtained from a vertex phase field, and (iii) the spectrum of the canonical equal-time baseline. It does not identify phase rotations with Lorentz boosts.

## 2. Möbius representation of a phase translation

For \(u=\tan(\phi/2)\) and \(\delta\in\mathbb R\), set
\[
a=\tan(\delta/2).
\]
Whenever the affine chart is finite,
\[
u'=\tan((\phi+\delta)/2)=\frac{u+a}{1-au}.
\]
In homogeneous projective coordinates this is represented without a singular parameter by
\[
R(\delta)=
\begin{pmatrix}
\cos(\delta/2)&\sin(\delta/2)\\
-\sin(\delta/2)&\cos(\delta/2)
\end{pmatrix},
\qquad
[u:1]\mapsto
[\cos(\delta/2)u+\sin(\delta/2):-\sin(\delta/2)u+\cos(\delta/2)].
\]
The determinant is \(1\). The projective action is defined for every \(\delta\), including \(\delta=\pi\), where the coordinate \(a\) is infinite. Also \(R(\delta_1)R(\delta_2)=R(\delta_1+\delta_2)\); the matrices are understood projectively, so \(R(\delta+2\pi)=-R(\delta)\) represents the same Möbius map.

## 3. Connection induced by a vertex phase

Given an actual phase field \(\phi:V\to\mathbb R/(2\pi\mathbb Z)\), define
\[
U_{vw}=\exp\!\big(i(\phi_w-\phi_v)\big).
\]
Then for every oriented closed cycle \(C=(v_0,v_1,\ldots,v_r=v_0)\),
\[
\operatorname{Hol}_U(C)=\prod_{j=0}^{r-1}U_{v_jv_{j+1}}
=\exp\!\left(i\sum_j(\phi_{v_{j+1}}-\phi_{v_j})\right)=1.
\]
Thus this construction is a pure-gauge (exact) connection. Under a global phase translation \(\phi_v\mapsto\phi_v+\delta\), every edge variable is unchanged. Under a local change of phase representative \(\phi_v\mapsto\phi_v+\chi_v\), the edge variables change by the usual endpoint gauge transformation; cycle holonomy remains unchanged.

For a free massive particle, the phase is \(\phi=mc^2\tau/\hbar+\phi_0\). On a single equal-proper-time slice, all Q6 vertices have the same \(\tau\), hence the induced canonical connection is
\[
\boxed{U_{vw}=1\quad\text{for every oriented edge}.}
\]
This is the only phase connection fixed by the supplied equal-time Q6 data. Assigning different \(\tau_v\), or a nonzero edge transport, would require additional geometric/physical data not contained in the abstract Q6 incidence structure. No prime weights, \(\varphi\)-weights, \(\psi\)-weights, or fitted phases are introduced here.

A useful converse is also exact for this cubical 2-complex: if every elementary square has unit \(U(1)\) holonomy, then the edge connection is gauge-equivalent to \(U=1\). Indeed the square boundaries generate the cycle space of the hypercube graph (equivalently, its cubical 2-skeleton is simply connected), so all cycle holonomies are one and path transport from a fixed base vertex defines a global gauge.

## 4. Covariant Laplacian and exact spectrum

For an oriented edge \(v\to w\), use
\[
(D_U f)_{vw}=f(w)-U_{vw}f(v),\qquad L_U=D_U^*D_U.
\]
For the canonical connection \(U=1\), this is the ordinary graph Laplacian
\[
(Lf)(v)=6f(v)-\sum_{k=0}^5 f(v\oplus e_k).
\]
The Walsh characters
\[
\chi_S(v)=(-1)^{\sum_{k\in S}v_k},\qquad S\subseteq\{0,\ldots,5\},
\]
form an orthogonal eigenbasis and satisfy \(L\chi_S=2|S|\chi_S\). Therefore
\[
\operatorname{Spec}(L)=
\{0^{(1)},2^{(6)},4^{(15)},6^{(20)},8^{(15)},10^{(6)},12^{(1)}\}.
\]
The same spectrum holds for any exact vertex-phase connection above, because its covariant Laplacian is unitarily conjugate to \(L\).

## 5. Antipodal involution and the two 32-dimensional sectors

Define the antipodal map \(A(v)=v\oplus(1,1,1,1,1,1)\), and its action on functions by \((\mathcal Af)(v)=f(A(v))\). Then \(\mathcal A^2=I\) and \([\mathcal A,L]=0\). On Walsh characters,
\[
\mathcal A\chi_S=(-1)^{|S|}\chi_S.
\]
Consequently the \(+1\) and \(-1\) eigenspaces of the antipodal involution both have dimension \(32\), with spectral multiplicities
\[
\begin{array}{c|rrrr}
\lambda&0&4&8&12\\\hline
\mathcal A=+1&1&15&15&1
\end{array}
\qquad
\begin{array}{c|rrr}
\lambda&2&6&10\\\hline
\mathcal A=-1&6&20&6.
\end{array}
\]
This is an antipodal-even/odd decomposition. It is not the bipartition of \(Q_6\): because the dimension is even, the bit-parity colouring is preserved by the antipodal map.

## 6. What is and is not established

**Proved:** the phase-translation Möbius formula; exactness and unit cycle holonomy of a connection induced by a vertex phase; the canonical equal-proper-time connection \(U=1\); the Q6 covariant-Laplacian spectrum; and the antipodal \(32+32\) spectral decomposition.

**Not established:** a nontrivial RGS–PSU transport law on Q6; nonzero plaquette flux; an identification of phase translation with a Lorentz boost; or the emergence of \(\varphi\) or the supergolden root \(\psi\). Since the canonical connection is pure gauge, its spectrum cannot produce new \(\varphi\)- or \(\psi\)-dependent eigenvalues. To obtain nontrivial holonomy one must supply a geometric connection (for example, a derived spin/Clifford transport or a specified nonuniform proper-time embedding), not arbitrary edge weights.

## 7. Reproducibility

Run:
\`\`\`bash
python scripts/audit_q6_mobius_phase.py
pytest -q tests/test_q6_mobius_phase.py
\`\`\`
The script reports the exact cell counts, plaquette holonomies, Laplacian multiplicities, and antipodal sector dimensions. It uses only the canonical bit-flip incidence structure.
