# T033 — Equivariant isotypic decomposition of the 3D Rumin complex and torsion

**Status:** abstract finite-group decomposition theorem proved below. Its application to the binary icosahedral action on \(S^3\) follows from the equivariance/descent hypotheses recorded in T031. The identification of the dimension-three Rumin operators and torsion conventions is supplied by T024. T021 and T032 provide the representation multiplicities and their exact Molien generating functions. This theorem synthesizes those results; it does **not** introduce new torsion values or a Q6/PRISM continuum limit.

## 1. Hypotheses and conventions

Let \(X\) be a compact manifold and \(G\) a finite group of order \(N\) acting on \(X\) by diffeomorphisms preserving the contact data and the Hermitian structures of a finite-rank graded complex bundle \(\mathcal E^\bullet\). Let
\[
(\mathcal E^\bullet,d_R),\qquad
\mathcal E^0\xrightarrow{d_R^0}\cdots\xrightarrow{d_R^{n-1}}
\mathcal E^n\xrightarrow{D}\mathcal E^{n+1}\to\cdots
\]
be a \(G\)-equivariant Rumin complex. Equivariance means that the induced unitary action \(U(g)\) on each \(L^2\)-completion satisfies
\[
U(g)d_R^k=d_R^kU(g),\qquad U(g)D=DU(g)
\quad(g\in G).
\]
Assume the associated nonnegative self-adjoint Rumin Laplacians \(\Delta_k\) have discrete spectrum with finite-dimensional eigenspaces, commute with \(U(G)\), and have zeta functions admitting the regularity at \(s=0\) required by the chosen analytic-torsion convention.

For each irreducible unitary representation \(\rho\in\widehat G\), write \(d_\rho=\dim V_\rho\) and \(\chi_\rho\) for its character. Use the character-projector convention
\[
P_\rho=\frac{d_\rho}{N}\sum_{g\in G}
\overline{\chi_\rho(g)}\,U(g).
\]
The associated flat bundle on \(X/G\) is understood with the equivariance convention fixed in T031; changing that convention can replace \(\rho\) by its dual and must be done consistently.

## 2. Theorem: decomposition of the complex and Laplacians

**Theorem 33.1 (finite-group isotypic decomposition).** Under the hypotheses above:

1. Each \(P_\rho\) is an orthogonal projection, \(P_\rho P_\sigma=0\) for inequivalent irreducibles, and
   \[
   \sum_{\rho\in\widehat G}P_\rho=I.
   \]
2. Every differential and every Rumin Laplacian preserves each isotypic subspace:
   \[
   P_\rho d_R^k=d_R^kP_\rho,\qquad
   P_\rho D=DP_\rho,\qquad
   P_\rho\Delta_k=\Delta_kP_\rho.
   \]
   Thus the full Rumin complex is the finite orthogonal direct sum of its \(\rho\)-isotypic subcomplexes.
3. There are Hilbert multiplicity spaces \(\mathcal M_{\rho,k}\) and unitary identifications
   \[
   P_\rho L^2(\mathcal E^k)\cong V_\rho\otimes\mathcal M_{\rho,k}
   \]
   under which every \(G\)-equivariant differential or Laplacian has the form
   \[
   I_{V_\rho}\otimes A_{\rho,k}.
   \]
   In particular, each eigenvalue in the multiplicity-space operator \(A_{\rho,k}\) occurs in the full \(\rho\)-isotypic space with multiplicity multiplied by \(d_\rho\).

**Proof.** The first assertion is the finite-group character orthogonality theorem: the displayed character sums are the central primitive idempotents of the unitary representation algebra. Their sum is the identity because the regular character decomposition contains every irreducible. Since the differentials and Laplacians commute with every \(U(g)\), they commute with every linear combination \(P_\rho\), proving the second assertion. For the third, the isotypic component of any unitary \(G\)-representation is a Hilbert direct sum of copies of \(V_\rho\), hence is \(V_\rho\otimes\mathcal M_{\rho,k}\). A bounded intertwiner between such components is \(I_{V_\rho}\otimes A\) by Schur's lemma; the same statement for the closed differentials and self-adjoint Laplacians follows on their invariant domains. The spectral multiplicity statement follows because the identity acts on the \(d_\rho\)-dimensional factor. \(\square\)

## 3. Corollary: zeta functions and analytic torsion add by sectors

Let \(\zeta_{\rho,k}(s)\) denote the spectral zeta function of \(A_{\rho,k}\), with zero-mode convention fixed consistently, and let \(\zeta_{X,k}(s)\) denote that of the full Laplacian on \(X\). In every common half-plane of absolute convergence,
\[
\boxed{\displaystyle
\zeta_{X,k}(s)=\sum_{\rho\in\widehat G}d_\rho\,\zeta_{\rho,k}(s).}
\]
If the meromorphic continuations are regular at zero, the identity continues meromorphically and differentiates at zero. For any analytic-torsion functional that is a fixed finite linear combination of these zeta derivatives,
\[
\boxed{\displaystyle
\log T_X=\sum_{\rho\in\widehat G}d_\rho\log T_\rho,}
\]
provided the same metric, zero-mode convention, determinant-line convention, and coefficient normalizations are used on both sides.

**Proof.** The spectral decomposition in Theorem 33.1 is an orthogonal finite direct sum. Eigenvalue multiplicities therefore add, with the factor \(d_\rho\) from the irreducible factor. This proves the zeta identity in the convergence half-plane. Uniqueness of meromorphic continuation proves the continued identity. Differentiation and the linearity of the logarithmic torsion functional give the formula. In the non-acyclic case, the corresponding determinant-line metrics are multiplicative under orthogonal direct sums when the cohomology bases and their induced determinant-line bases are combined; no unrecorded change of basis is permitted. \(\square\)

**Important distinction.** The zeta function \(\zeta_{\rho,k}\) is the multiplicity-space/twisted-sector contribution. The full-cover spectrum contains it \(d_\rho\) times. A quotient local system associated with \(\rho\) is not to be multiplied by \(d_\rho\) when reporting its own twisted torsion. The factor appears only when reconstructing the full \(G\)-equivariant cover from all isotypic sectors.

## 4. Corollary: exact multiplicity conservation in the \(SU(2)\) tower

Take \(G=2I\subset SU(2)\), \(|G|=120\), and the defining \(SU(2)\)-representation \(W=\mathbb C^2\). The restriction of \(\operatorname{Sym}^m(W)\) to \(2I\) decomposes as
\[
\operatorname{Sym}^m(W)\big|_{2I}
\cong\bigoplus_{\rho\in\widehat{2I}}V_\rho^{\oplus b_{m,\rho}},
\qquad
b_{m,\rho}=\dim\operatorname{Hom}_{2I}
(V_\rho,\operatorname{Sym}^m W).
\]
Consequently
\[
\boxed{\displaystyle
\sum_{\rho\in\widehat{2I}}d_\rho b_{m,\rho}=m+1.}
\]
If \(M_\rho(t)=\sum_{m\ge0}b_{m,\rho}t^m\), then as a formal power-series identity
\[
\boxed{\displaystyle
\sum_{\rho\in\widehat{2I}}d_\rho M_\rho(t)=
\sum_{m\ge0}(m+1)t^m=\frac1{(1-t)^2}.}
\]
Using the nine Molien covariants recorded in T021 and encoded with exact integer coefficients in T032, this is an exact identity of rational formal series, not merely a finite numerical fit. The coefficient checks through degree 240 in T032 are regression tests of this identity; the proof for every \(m\) is the representation-theoretic dimension formula above, once the nine \(M_\rho\) are established as the actual multiplicity series.

**Proof.** Complete reducibility holds because \(2I\) is finite and the representation is unitary. Taking dimensions of the decomposition gives the first identity, since \(\dim\operatorname{Sym}^m(\mathbb C^2)=m+1\). Multiplying by \(t^m\) and summing gives the generating-function identity. \(\square\)

## 5. Application to \(S^3/2I\): synthesis of T021, T024, T031 and T032

Set \(X=S^3\) and \(G=2I\), acting freely by left multiplication. The right Hopf action commutes with the deck action. T031 establishes preservation of the chosen contact/CR data, naturality of the Rumin differentials, and descent of the equivariant complexes. Hence the hypotheses concerning group equivariance in Theorem 33.1 hold for the lifted Rumin complex.

T024 establishes, in contact dimension three and under its common contact-metric and flat-unitary hypotheses, equality of the Kitaoka and Rumin–Seshadri Laplacians degree by degree and the corresponding torsion-convention conversion. Thus the sector operators appearing in T021 can be interpreted in the same three-dimensional Rumin/Ray–Singer convention after the determinant-line normalization specified there.

T021 supplies the character-twisted multiplicities \(b_{m,\rho}\), their nine Molien covariants, and the corrected eventual-Hurwitz framework. T032 supplies exact coefficient-generation code and tests for the dimension-conservation identity. The theorem above supplies the missing organizational statement: these are not nine unrelated spectral calculations but the nine orthogonal isotypic sectors of one \(2I\)-equivariant Rumin complex.

The resulting rigorous synthesis is:
\[
\boxed{\displaystyle
\log T_{S^3,\mathrm{Rumin}}
=\sum_{\rho\in\widehat{2I}}d_\rho
\log T_{\rho,\mathrm{Rumin}},}
\]
with the same metric, spectral zero-mode convention, and determinant-line normalization on both sides. This identity is a decomposition theorem; it does not assert that any particular numerical torsion table is correct unless the corrected sector zeta calculations and their conventions have independently passed their audits.

## 6. What follows — and what does not

**PROVED from finite-group representation theory plus the stated analytic hypotheses**
- Orthogonal isotypic decomposition of the equivariant Rumin complex and its Laplacians.
- Preservation of sectors by the Rumin differentials and Laplacians.
- Additivity of spectral zeta functions and logarithmic analytic torsion across sectors, with the irreducible-dimension factor.
- The all-degree dimension-conservation identity for the decomposition of \(\operatorname{Sym}^m(\mathbb C^2)\).

**INHERITED from the cited repository theorems, under their hypotheses**
- Geometric \(2I\)-equivariance and descent: T031.
- Dimension-three operator and torsion-convention identification: T024.
- Character-twisted spectral/Molien formulas: T021.
- Exact-integer Molien coefficient implementation and finite-range regression tests: T032.

**NOT ESTABLISHED BY T033**
- A new evaluation of the nine analytic torsions or acceptance of the corrected Gamma-product identities; those require the separate T021–T023 audits.
- Explicit matrices for all nine irreducibles or a new exact character-table export.
- Any Q6/PRISM-to-Rumin operator intertwining, Mosco convergence, or continuum limit.
- Any physical conclusion about QCD, Yang–Mills, or subatomic matter.

## 7. Proof dependencies and acceptance checklist

| Input | Exact role in this theorem | Acceptance condition |
|---|---|---|
| Finite-group character orthogonality / Schur lemma | Projectors and isotypic factorization | Algebraic theorem |
| T031 | \(2I\)-equivariance of the lifted Rumin complex | Fixed left deck/right Hopf convention |
| T024 | Equality of 3D Rumin operators and torsion conventions | Same contact metric and flat-unitary coefficients |
| T021 | Nine twisted spectral multiplicity series | Corrected preperiod/tail formulas; no use of superseded formula |
| T032 | Exact coefficient implementation | Tests run in repository CI; not inferred from code existence |

The main formula is valid only after all rows' hypotheses are met. In particular, the torsion additivity is not a substitute for the analytic continuation and determinant-line calculations in T021–T024.

## References within this repository

- [T021 — Character-twisted Rumin analytic torsion on the Poincaré sphere](T021-rumin-analytic-torsion-2I.md).
- [T024 — Operator and torsion-convention matching for the 3D Rumin complex](T024-rumin-kitaoka-operator-matching-3d.md).
- [T031 — Equivariance of the 3D Rumin complex under the binary icosahedral action](T031-rumin-2i-equivariance.md).
- [T032 — Exact Molien covariants and the 2I isotypic-projector interface](T032-2i-irrep-molien-projectors.md).

## Classification

- **PROVED:** The abstract finite-group isotypic decomposition and its zeta/torsion additivity, under the stated operator and regularity hypotheses.
- **PROVED:** The dimension identity \(\sum_\rho d_\rho b_{m,\rho}=m+1\) for the actual irreducible decomposition of \(\operatorname{Sym}^m(\mathbb C^2)\).
- **APPLICATION ESTABLISHED UNDER T031/T024 HYPOTHESES:** The synthesis for the \(2I\)-equivariant 3D Rumin complex on \(S^3\) and its flat twists on \(S^3/2I\).
- **OPEN / SEPARATE AUDIT:** Acceptance of all corrected sector torsion values, explicit nine-irrep matrices, and any Q6/PRISM continuum theorem.
