# T034 — Explicit binary icosahedral representations, exact character table, and exact projectors

**Status:** exact finite computation, executed. Every identity below was checked in exact arithmetic over \(K=\mathbb Q(\sqrt5)[i]\) (Python `fractions`, no floating point, no sympy, no dependency on `rgs-qlg-quaternion-bridge`). The test suite `tests/test_t034_binary_icosahedral_representations.py` was run in full (19 tests, OK, ≈200 s). T034 does **not** recompute any torsion and does **not** touch T021–T033.

**Naming note.** `theorems/T034-exact-2i-character-table.md` (already on `main`) reconstructs the character table from the T021 Molien data and states that explicit matrices remain open. This theorem closes that open item and is independent of it: its characters are computed as traces of the explicit matrices below. The two tables were compared entry by entry (all 81 entries agree). The identifier collision is an administrative matter for the maintainer (e.g. renumbering one file); nothing here depends on it.

**Relation to T035/T036 (merged on `main` while this work was in progress).** T035 gives an independent exact 600-cell model of \(2I\) and T036 extracts nine models from symmetric powers by solving for invariant subspaces (SymPy, tests not yet certified there). This theorem was developed independently, in pure `fractions` arithmetic, and was not derived from them. It overlaps with them on the group model and the nine matrix models (same field \(\mathbb Q(\sqrt5,i)\), same class convention), and adds: the Cayley-graph proof of the representation property, the Galois-conjugate analysis (§2.2), exact Schur orthogonality for all matrix coefficients, central projectors and matrix units executed on \(\operatorname{Sym}^m\), and the all-degree Molien identity (§5). The bases differ (here the monomial bases of \(\operatorname{Sym}^k\) directly, there extracted column bases), so matrix units from the two are not entrywise comparable without a change of basis. No entry-by-entry comparison with T036 output was run. Whether to merge, deduplicate or renumber is left to the maintainer.

Conventions are those of T031/T033: scalar-first quaternions, Hamilton product, deck action \(q\mapsto gq\), left representations \(U(gh)=U(g)U(h)\). The class order, class sizes and fundamental character are those fixed in the existing T034 note.

## 1. Exact construction of \(2I\) (Task 1)

Let \(\varphi=\tfrac{1+\sqrt5}{2}\). The set \(G\subset\mathbb H(\mathbb Q(\sqrt5))\) is the union of

- the 8 units \(\pm1,\pm i,\pm j,\pm k\);
- the 16 quaternions \(\tfrac12(\pm1\pm i\pm j\pm k)\);
- the 96 quaternions obtained from \(\tfrac12(0,1,\varphi,\varphi^{-1})\) by even permutations of coordinates and arbitrary signs on the three nonzero entries.

Verified exactly (all in the field \(\mathbb Q(\sqrt5)\), index tables built from exact coordinates):

| Property | Result |
|---|---|
| cardinality | exactly 120, all norms exactly 1 |
| closure | all \(120^2\) Hamilton products lie in \(G\) |
| generation | \(s=\tfrac12(1+i+j+k)\) (order 6) and \(t=\tfrac12(\varphi+i+\varphi^{-1}j)\) (order 10) generate exactly \(G\) |
| identity, inverses | \(g\bar g=1\), inverse \(=\) quaternion conjugate |
| associativity | all \(120^3\) triples |
| centre | exactly \(\{1,-1\}\) |
| classes (by explicit conjugation) | 9 classes, sizes \((1,1,20,30,12,12,20,12,12)\), element orders \((1,2,3,4,5,5,6,10,10)\), \(\sum|C|=120\) |

The nine classes are matched to the fixed order by \(2\operatorname{Re}q=\chi_{\mathbf 2}(C)\), which takes nine distinct values.

## 2. The nine irreducible representations (Task 2)

Let \(M(q)=\begin{pmatrix}w+xi&y+zi\\-y+zi&w-xi\end{pmatrix}\) for \(q=w+xi+yj+zk\); this is a homomorphism (checked on the group, below). Let \(\sigma\) be the field automorphism \(\sqrt5\mapsto-\sqrt5\) (fixing \(i\)), applied entrywise. For \(\operatorname{Sym}^k\) use the monomial basis \(v_1^{k-j}v_2^{j}\) (column convention).

| irrep | construction | spinorial (\(-1\mapsto-I\)) |
|---|---|---|
| \(\mathbf1\) | trivial | no |
| \(\mathbf2\) | \(M(g)\) | yes |
| \(\mathbf2'\) | \(\sigma(M(g))\) | yes |
| \(\mathbf3\) | \(\operatorname{Sym}^2\mathbf2\) | no |
| \(\mathbf3'\) | \(\operatorname{Sym}^2\mathbf2'\) | no |
| \(\mathbf4\) | \(\mathbf2\otimes\mathbf2'\) | no |
| \(\mathbf4'\) | \(\operatorname{Sym}^3\mathbf2\) | yes |
| \(\mathbf5\) | \(\operatorname{Sym}^4\mathbf2\) | no |
| \(\mathbf6\) | \(\operatorname{Sym}^5\mathbf2\) | yes |

**Field of definition.** All matrix entries lie in \(K=\mathbb Q(\sqrt5,i)\subset\mathbb Q(\zeta_{20})\); all characters lie in \(\mathbb Q(\sqrt5)\) and are real. No claim is made that \(K\) is minimal (for the spinorial \(\mathbf2,\mathbf2',\mathbf4',\mathbf6\) the Schur index over \(\mathbb Q(\sqrt5)\) forces a non-real field anyway).

**Generator matrices.** For \(\mathbf2\):
\[
\rho(s)=\tfrac12\begin{pmatrix}1+i&1+i\\-1+i&1-i\end{pmatrix},\qquad
\rho(t)=\tfrac12\begin{pmatrix}\varphi+i&\varphi^{-1}\\-\varphi^{-1}&\varphi-i\end{pmatrix}.
\]
For \(\mathbf2'\) replace \(\varphi\mapsto1-\varphi=-\varphi^{-1}\) and \(\varphi^{-1}\mapsto-\varphi\). The matrices of all nine representations for \(s,t\) (and, by the construction column, for every one of the 120 elements) are exported exactly in `data/t034_2i_character_table.json` (`irreps.*.generator_matrices`, entries encoded as \([a,b,c,d]\) meaning \(a+b\sqrt5+(c+d\sqrt5)i\)).

### 2.1 Representation identity (proved, exact)

**Lemma (Cayley-graph criterion).** Let \(\Phi:G\to GL_n(K)\) satisfy \(\Phi(e)=I\) and \(\Phi(gx)=\Phi(g)\Phi(x)\) for every \(g\in G\) and every \(x\) in a generating set \(S\). Then \(\Phi\) is a homomorphism.
*Proof.* Every \(h\) is a word \(x_1\cdots x_r\) in \(S\) (finite group, so no inverses are needed). Induction on \(r\): \(\Phi(gx_1\cdots x_r)=\Phi(gx_1\cdots x_{r-1})\Phi(x_r)=\Phi(g)\Phi(x_1)\cdots\Phi(x_r)\), and with \(g=e\) this gives \(\Phi(h)=\Phi(x_1)\cdots\Phi(x_r)\). \(\square\)

For each of the nine families \(\Phi(g)\) (defined independently for each of the 120 elements, not through words) the 240 edge identities for \(S=\{s,t\}\) and \(\Phi(e)=I\) were verified exactly; 300 full pair products \(\Phi(gh)=\Phi(g)\Phi(h)\) (deterministic sample) were checked as a redundant test. So all nine are representations. No presentation theorem for \(2I\) is used.

### 2.2 Galois-conjugate representations (proved + verified)

The task asks not to assume that \(\sqrt5\mapsto-\sqrt5\) "preserves the group". Indeed it does not:

- **Not a symmetry of the set.** \(\sigma\) applied coordinatewise to the 120 quaternions sends only **24** of them back into \(G\) (the binary tetrahedral subgroup); \(\sigma(G)\neq G\) (it is the other conjugate icosahedral subgroup; at the level of the generating data, \(\sigma\) exchanges \(\varphi\) and \(-\varphi^{-1}\) and turns even permutations of \((0,1,\varphi,\varphi^{-1})\) into odd ones). Verified exactly.
- **Still a representation of the abstract group.** \(\sigma\) is a ring automorphism of \(K\); entrywise \(\sigma\) is a ring automorphism of \(M_n(K)\), so \(\rho'(g):=\sigma(\rho(g))\) satisfies \(\rho'(gh)=\sigma(\rho(g)\rho(h))=\rho'(g)\rho'(h)\). This is a proof; it was *also* checked via §2.1 and on the generators: \(\rho'(s)^6=I\), \(\rho'(t)^{10}=I\), \((\rho'(s)\rho'(t))^4=I\), \(\rho'(s)^3=\rho'(t)^5=-I\).
- **Inequivalence.** \(\chi_{\mathbf2'}\neq\chi_{\mathbf2}\) (e.g. on the class of order 5), likewise \(\mathbf3'\neq\mathbf3\).

### 2.3 Unitarity — what is and is not claimed

\(\mathbf1,\mathbf2,\mathbf2',\mathbf4\) are exactly unitary in the given bases. For \(\operatorname{Sym}^k\) the monomial basis is orthogonal for the invariant Hermitian form \(D=\operatorname{diag}(1/\binom kj)\), and \(\rho(g)^*D\rho(g)=D\) was verified exactly for all 120 elements. A genuinely unitary basis needs \(\sqrt{\binom kj}\), which are not all in \(K\); such a model is **not** constructed here. Consequently matrix units are written in the basis-independent form (§4); for a unitary model it coincides with the T033 formula \(\tfrac d{120}\sum_g\overline{\rho(g)_{ij}}U(g)\) because then \(\rho(g^{-1})_{ji}=\overline{\rho(g)_{ij}}\).

## 3. Character table (Task 3)

Computed as traces of the explicit matrices on all 120 elements (and checked constant on classes). With \(\varphi=\frac{1+\sqrt5}2\), classes ordered by element order \((1,2,3,4,5,5,6,10,10)\):

| | 1 | −1 | 3 | 4 | 5a | 5b | 6 | 10a | 10b |
|---|---|---|---|---|---|---|---|---|---|
| size | 1 | 1 | 20 | 30 | 12 | 12 | 20 | 12 | 12 |
| \(\mathbf1\) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| \(\mathbf2\) | 2 | −2 | −1 | 0 | \(\varphi-1\) | \(-\varphi\) | 1 | \(\varphi\) | \(1-\varphi\) |
| \(\mathbf2'\) | 2 | −2 | −1 | 0 | \(-\varphi\) | \(\varphi-1\) | 1 | \(1-\varphi\) | \(\varphi\) |
| \(\mathbf3\) | 3 | 3 | 0 | −1 | \(1-\varphi\) | \(\varphi\) | 0 | \(\varphi\) | \(1-\varphi\) |
| \(\mathbf3'\) | 3 | 3 | 0 | −1 | \(\varphi\) | \(1-\varphi\) | 0 | \(1-\varphi\) | \(\varphi\) |
| \(\mathbf4\) | 4 | 4 | 1 | 0 | −1 | −1 | 1 | −1 | −1 |
| \(\mathbf4'\) | 4 | −4 | 1 | 0 | −1 | −1 | −1 | 1 | 1 |
| \(\mathbf5\) | 5 | 5 | −1 | 1 | 0 | 0 | −1 | 0 | 0 |
| \(\mathbf6\) | 6 | −6 | 0 | 0 | 1 | 1 | 0 | −1 | −1 |

Verified exactly: \(\sum_C|C|=120\); \(\sum_\rho d_\rho^2=120\); all 81 row identities \(\frac1{120}\sum_C|C|\overline{\chi_\rho}\chi_\sigma=\delta_{\rho\sigma}\); all 81 column identities \(\sum_\rho\overline{\chi_\rho(C)}\chi_\rho(C')=\frac{120}{|C|}\delta_{CC'}\); and \(\sum_\rho d_\rho\chi_\rho(C)=120\,\delta_{C,1}\) (regular character).

**Irreducibility (proved).** A character with \(\langle\chi,\chi\rangle=1\) is irreducible. The diagonal row identities give \(\langle\chi_\rho,\chi_\rho\rangle=1\) for all nine rows, computed from the actual matrices. The off-diagonal identities show the nine are pairwise inequivalent; with \(\sum d_\rho^2=120\) they exhaust \(\widehat{2I}\).

Export: `data/t034_2i_character_table.json` (class order, sizes, element orders, class representatives as exact quaternions, character values as exact \([a,b,c,d]\) strings plus readable text, generator matrices, and the verification report; field `Q(sqrt5)` for characters and `Q(sqrt5, i)` for matrices).

## 4. Projectors and matrix units (Task 4)

\[
P_\rho=\frac{d_\rho}{120}\sum_{g}\overline{\chi_\rho(g)}\,U(g),\qquad
E^{(\rho)}_{ij}=\frac{d_\rho}{120}\sum_g\rho(g^{-1})_{ji}\,U(g).
\]
**Schur orthogonality (verified exactly, all coefficients).**
\[
\tfrac{d_\rho}{120}\sum_g\rho(g)_{ij}\,\sigma(g^{-1})_{kl}=\delta_{\rho\sigma}\delta_{il}\delta_{jk}
\]
for all \(120\cdot120=14400\) index/representation combinations \((\rho,i,j;\sigma,k,l)\). From this the group-algebra identities follow by the standard computation, giving, for every representation \(U\):
\(E^{(\rho)}_{ij}E^{(\sigma)}_{kl}=\delta_{\rho\sigma}\delta_{jk}E^{(\rho)}_{il}\), \(P_\rho=\sum_iE^{(\rho)}_{ii}\), \(P_\rho^2=P_\rho\), \(P_\rho P_\sigma=0\), \(\sum_\rho P_\rho=I\).

**Central projectors versus matrix units.** \(P_\rho\) is the projector onto the whole isotypic component (rank \(d_\rho m_\rho\)); it depends only on the character. \(E^{(\rho)}_{11}\) projects onto one copy of the \(\mathbf e_1\)-line in each irreducible summand (rank \(m_\rho\), the multiplicity-space dimension) and depends on the chosen basis of \(V_\rho\); \(E^{(\rho)}_{i1}\) transports the multiplicity space to the \(i\)-th basis vector (T033 §3).

**Executed checks on \(U=\operatorname{Sym}^m(\mathbf2)\), \(m=0,\dots,13\)** (matrices \(U(g)\) for all 120 elements, exact): \(P_\rho^2=P_\rho\); \(\sum_\rho P_\rho=I\); \(\operatorname{tr}P_\rho=\operatorname{rank}P_\rho=d_\rho b_{m,\rho}\) with \(b_{m,\rho}\) the T032 coefficient (idempotent \(\Rightarrow\) rank \(=\) trace); pairwise \(P_\rho P_\sigma=0\) (all 36 pairs, both orders) for \(m\le7\); for \(m=8,\dots,13\) orthogonality follows from the verified idempotents summing to \(I\) with ranks summing to \(m+1\) (in characteristic 0, idempotents with \(\sum P_i=I\) are mutually orthogonal). Together \(m=0,\dots,7\) realize every irrep (first occurrences: \(\mathbf1\) at 12, \(\mathbf2\) at 1, \(\mathbf2'\) at 7, \(\mathbf3\) at 2, \(\mathbf3'\) at 6, \(\mathbf4\) at 6, \(\mathbf4'\) at 3, \(\mathbf5\) at 4, \(\mathbf6\) at 5).

**Matrix units, executed.** On \(\operatorname{Sym}^m\), \(m=0,\dots,7\): \(E_{ii}\) idempotent with trace \(=b_{m,\rho}\), \(\operatorname{tr}\sum_iE_{ii}=d_\rho b_{m,\rho}\), the product rule \(E_{ij}E_{kl}=\delta_{jk}E_{il}\) on all quadruples when \(d^4\le60\), otherwise on a deterministic sample of 60 quadruples, and the covariance \(U(g)E_{i1}=\sum_j\rho(g)_{ji}E_{j1}\) for \(g\in\{s,t\}\). Multiplicity \(>1\) is tested on \(\operatorname{Sym}^2\oplus\operatorname{Sym}^{10}\) (contains \(\mathbf3\) twice): \(\operatorname{tr}E_{ii}=2\). (In \(\operatorname{Sym}^m\), \(m\le7\), every multiplicity is 0 or 1, hence the separate multiplicity-two test.) The full product rule in the group algebra is a consequence of the exactly verified Schur relations above, not only of the sampled products.

## 5. Link with T021, T031, T032, T033 (Task 5)

### 5.1 Characters \(\leftrightarrow\) Molien multiplicities: an all-degree exact identity (proved + verified)

For \(g\in SU(2)\), \(\sum_{m\ge0}\chi_{\operatorname{Sym}^m}(g)t^m=1/\det(1-tg)=1/(1-\chi_{\mathbf2}(g)t+t^2)\). Hence
\[
M_\rho(t)=\sum_mb_{m,\rho}t^m=\frac1{120}\sum_C|C|\,\frac{\overline{\chi_\rho(C)}}{q_C(t)},\qquad q_C(t)=1-\chi_{\mathbf2}(C)t+t^2 .
\]
Every \(q_C\) divides \((1-t^{12})(1-t^{20})\) in \(\mathbb Q(\sqrt5)[t]\) (checked by exact polynomial division; the eigenvalues are roots of unity of order dividing 12 or 20). Therefore \((1-t^{12})(1-t^{20})M_\rho(t)\) is an explicit polynomial in \(\mathbb Q(\sqrt5)[t]\). It was computed exactly from the character table of §3 and compared coefficient by coefficient with the T021/T032 numerators \(N_\rho(t)\) (including the coefficient 2 of \(t^{15}\) for \(\mathbf6\)): **equal for all nine \(\rho\)**. This proves \(b_{m,\rho}=\langle\chi_\rho,\chi_{\operatorname{Sym}^m}\rangle\) for **every** \(m\), upgrading the finite regression test of T032 (degrees \(\le240\), also re-run here: 2169 exact averages) to an all-degree statement, and confirms the labels \(\mathbf1,\dots,\mathbf6\) of T021 are those of the explicit models above.

### 5.2 The weighted sum

\[
\sum_\rho d_\rho M_\rho(t)=\frac1{120}\sum_C\frac{|C|}{q_C(t)}\sum_\rho d_\rho\overline{\chi_\rho(C)}
=\frac1{q_{\{1\}}(t)}=\frac1{(1-t)^2},
\]
because \(\sum_\rho d_\rho\chi_\rho=120\,\delta_{\{1\}}\) (regular character; verified exactly in §3). Independently, \(\sum_\rho d_\rho N_\rho(t)=\frac{(1-t^{12})(1-t^{20})}{(1-t)^2}\) was checked as an exact polynomial identity. So \(\sum_\rho d_\rho b_{m,\rho}=m+1\) for all \(m\), the identity used in T033 §4.

### 5.3 Isotypic decomposition, flat twists, torsion additivity (conditional on the cited results)

- **Isotypic decomposition.** §4 shows that the \(P_\rho\) of T031/T033 are exact projectors with \(\operatorname{rank}P_\rho=d_\rho b_{m,\rho}\) on every tested \(\operatorname{Sym}^m\), and \(\sum_\rho\operatorname{rank}P_\rho=m+1\) is exactly the identity of §5.2.
- **Flat twists and descent (T031).** Equivariant sections \(u(gq)=\rho(g)u(q)\) are the \(G\)-invariants of \(V_\rho\otimes C^\infty(S^3)\) under \(g\cdot u=\rho(g)u(g^{-1}\,\cdot)\). By Peter–Weyl, the level-\(m\) part of \(L^2(S^3)\) is \(\operatorname{Sym}^m\otimes\operatorname{Sym}^{m}\) with \(2I\) acting on the first factor, so the level-\(m\) twisted space has dimension \((m+1)\,b_{m,\rho^*}\). **All characters of \(2I\) are real** (§3, exact), so \(\rho^*\cong\rho\), \(b_{m,\rho^*}=b_{m,\rho}\), and the isomorphism class of the flat bundle \(E_\rho\) does not depend on the \(\rho\leftrightarrow\rho^{-1}\)/dual convention flagged in T031 §3. Summing with weights \(d_\rho\) gives \(\sum_\rho d_\rho(m+1)b_{m,\rho}=(m+1)^2=\dim\) of level \(m\) (checked for \(m\le120\), and a consequence of §5.2 for all \(m\)).
- **Additivity (T033 Cor. 3).** The only property of the multiplicities that enters \(\zeta_{X,k}=\sum_\rho d_\rho\zeta_{\rho,k}\) and \(\log T_X=\sum_\rho d_\rho\log T_\rho\) is the weight \(d_\rho\) with \(\sum_\rho d_\rho\cdot(\text{sector multiplicity})=\) cover multiplicity; §5.2 and the Peter–Weyl count above verify exactly that bookkeeping for the \(SU(2)\) tower. The analytic statements themselves (zeta continuation, determinant-line conventions) are inherited from T021–T024/T033 and are **not** re-derived or re-computed here.

## 6. Reproducibility

From the repository root:
```bash
python -m unittest tests.test_t034_binary_icosahedral_representations -v   # ≈ 200 s
python -m src.t034_binary_icosahedral_representations                      # regenerates data/t034_2i_character_table.json (≈ 3 min)
```
Observed in this session: 19 tests OK. Cross-checks run once in this session: `tests.test_t032_2i_molien` (4 OK), `tests.test_t034_exact_2i_character_table` (5 OK, needs sympy), and an entry-by-entry comparison of the 81 character values with that module's output (all equal).

## 7. Classification

**Proved (finite-group theory, plus exact finite checks that are complete for the finite objects involved):**
- \(G\) is a group of order 120 with centre \(\{\pm1\}\) and the stated nine classes; the nine matrix families are representations (Cayley-graph lemma); each is irreducible and they are pairwise inequivalent (character norms); \(\sigma\circ\rho\) is a representation although \(\sigma(G)\ne G\).
- Schur orthogonality for the explicit matrices, hence matrix units, central projectors, \(P_\rho P_\sigma=\delta P_\rho\), \(\sum P_\rho=I\).
- \(b_{m,\rho}=\langle\chi_\rho,\chi_{\operatorname{Sym}^m}\rangle\) for all \(m\) with the T021/T032 numerators; \(\sum_\rho d_\rho M_\rho=(1-t)^{-2}\).

**Verified by exact computation but only on finite samples:**
- Full-pair homomorphism products (300 sampled pairs; the proof uses the edge lemma instead).
- Matrix-unit multiplication on a sample of quadruples when \(d^4>60\) (complete via Schur relations).
- Projector tests on \(\operatorname{Sym}^m\) for \(m\le13\); character averages for \(m\le240\).

**Conditional / inherited, not re-proved here:**
- Geometric equivariance, descent and the dimension-3 operator identification (T031, T024); the Peter–Weyl decomposition of \(L^2(S^3)\) (standard theorem, not machine-checked); additivity of zeta/torsion (T033, under its analytic hypotheses).

**Open / not claimed:**
- A model that is unitary in an orthonormal basis for \(\mathbf3,\mathbf3',\mathbf4',\mathbf5,\mathbf6\) (needs \(\sqrt{\binom kj}\), outside \(K\)); only weighted unitarity is proved.
- Matrix units on the actual Rumin harmonic spaces and the reduced geometric Rumin matrices; any new torsion value; the floating-point `verification/test_t031_quaternion_bridge.py` audit is unchanged and remains a floating-point audit (the exact audit of §1 supersedes it for closure/associativity of \(2I\)).
- Any Q6/PRISM continuum statement.

## Dependencies

T021 (Molien numerators), T024, T031 (conventions), T032 (`src/t032_2i_molien.py`, imported for the numerators and for the cross-check), T033 (matrix-unit formula and torsion additivity), existing T034 character-table note (cross-check only).
