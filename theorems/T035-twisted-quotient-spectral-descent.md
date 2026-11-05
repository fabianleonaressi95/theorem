# T035 — Twisted Rumin spectra as equivariant sectors on the finite quotient

**Purpose.** T033 proves abstract isotypic decomposition and the corresponding additivity on the covering space. T035 identifies, with the deck-action convention fixed in T031, the *individual flat-twisted Rumin complex on the quotient* with a single equivariant multiplicity space upstairs. This removes a frequent ambiguity: the quotient twisted spectrum is not the whole isotypic block multiplied by the dimension of the representation.

**Status.** The finite-covering theorem below is proved under explicit geometric and operator hypotheses. Its application to \(S^3\to S^3/2I\) uses the geometric descent established in T031 and the dimension-three operator identification in T024. No new numerical spectrum or torsion value is claimed.

## 1. Geometric and representation-theoretic setup

Let \(p:X\to M=X/G\) be a regular finite covering of compact manifolds with deck group \(G\), \(|G|=N\). Assume the deck transformations preserve a contact structure, contact form, compatible metric and the induced Hermitian structures. Let
\[
(\mathcal E_X^\bullet,d_R)
\]
be the lifted Rumin complex. Naturality gives
\[
U(g)d_R=d_RU(g),\qquad g\in G,
\]
where \(U(g)\omega=(g^{-1})^*\omega\) is the unitary deck action on scalar-valued forms. Let \(\Delta_{X,k}\) be the associated nonnegative self-adjoint Rumin Laplacians, with compact resolvent, commuting with \(U(G)\).

Let \(\rho:G\to U(V_\rho)\) be a finite-dimensional unitary representation. Fix the associated-bundle convention so that sections of \(E_\rho=(X\times V_\rho)/G\) are represented by coefficient-valued forms \(F\) satisfying
\[
F(gx)=\rho(g)F(x).
\]
This is the equivariance convention used in T031. If the associated-bundle quotient convention is reversed, \(\rho\) must be replaced by \(\rho^*\) throughout.

## 2. Theorem: quotient twisted complex equals an invariant subcomplex upstairs

**Theorem 35.1 (finite-covering descent with unitary twist).** Under the hypotheses above, pullback to the cover gives a unitary isomorphism of Hilbert complexes
\[
L^2\bigl(M;\mathcal E_M^\bullet\otimes E_\rho\bigr)
\;\cong\;
\left(L^2(X;\mathcal E_X^\bullet)\otimes V_\rho\right)^G,
\]
where \(G\) acts diagonally by
\[
W_\rho(g)=U(g)\otimes\rho(g).
\]
Under this isomorphism, the quotient Rumin differentials, including the middle differential, and their self-adjoint Rumin Laplacians correspond to the restrictions of
\[
d_R\otimes I_{V_\rho},\qquad
\Delta_{X,k}\otimes I_{V_\rho}
\]
to the invariant subspace. In particular, the quotient twisted spectrum, including multiplicities and zero modes, is exactly the spectrum of this invariant restriction.

**Proof.** A section of the associated flat bundle is, by the fixed convention, an equivariant coefficient-valued form \(F\) on \(X\). The equivariance relation is equivalent to
\[
(U(g)\otimes\rho(g))F=F
\]
for every \(g\in G\): indeed \(U(g)F(x)=F(g^{-1}x)\), and invariance says \(F(g^{-1}x)=\rho(g)^{-1}F(x)\), equivalently \(F(gx)=\rho(g)F(x)\). The covering pullback identifies smooth quotient sections with these equivariant forms. The \(L^2\) isometry is obtained by multiplying pullback by \(N^{-1/2}\), since integration over \(X\) counts each quotient point \(N\) times. Completion gives the Hilbert-space isomorphism. Naturality of every Rumin differential implies it commutes with deck pullback; the coefficient representation is constant in the lifted flat trivialization, so the diagonal invariant subspace is preserved. The same holds for formal adjoints because the action and coefficient representation are unitary, hence for the Rumin Laplacians and their self-adjoint realizations. The intertwining unitary therefore preserves eigenvalues, eigenspace dimensions and kernels. \(\square\)

## 3. Identification with one multiplicity space

Let \(\mathcal H_k=L^2(X;\mathcal E_X^k)\) and decompose its unitary \(G\)-representation as
\[
\mathcal H_k\cong
\widehat{\bigoplus}_{\sigma\in\widehat G}
V_\sigma\otimes\mathcal M_{\sigma,k},
\]
where \(\mathcal M_{\sigma,k}=\operatorname{Hom}_G(V_\sigma,\mathcal H_k)\) is the multiplicity space. Then
\[
(\mathcal H_k\otimes V_\rho)^G
\cong
\mathcal M_{\rho^*,k}.
\]
Here \(\rho^*\) denotes the contragredient representation. This follows from
\[
(V_\sigma\otimes V_\rho)^G
\cong\operatorname{Hom}_G(V_\sigma^*,V_\rho),
\]
which is zero unless \(\sigma\cong\rho^*\), and one-dimensional in the irreducible matching factor; the remaining factor is \(\mathcal M_{\sigma,k}\).

**Corollary 35.2 (twisted quotient spectral zeta).** If \(\zeta_{M,\rho,k}(s)\) is the spectral zeta function of the quotient Rumin Laplacian with flat coefficient bundle \(E_\rho\), and \(\zeta_{\mathcal M_{\rho^*,k}}(s)\) is the zeta function of the induced operator on the multiplicity space, then
\[
\boxed{\zeta_{M,\rho,k}(s)=
\zeta_{\mathcal M_{\rho^*,k}}(s).}
\]
This identity holds in the common half-plane of absolute convergence and, whenever the zeta functions admit meromorphic continuation, throughout that continuation.

**Proof.** Apply Theorem 35.1 and the invariant-space identification above. The unitary equivalence preserves the complete spectrum with multiplicities, so it preserves the spectral zeta function. Meromorphic continuation is unique. \(\square\)

**Convention warning.** With the equivariance condition \(F(gx)=\rho(g)F(x)\), the multiplicity label upstairs is \(\rho^*\). If one uses the opposite deck action on forms or the inverse associated-bundle convention, the label changes accordingly. For \(2I\), the duality permutation must be checked against the chosen character-table convention; it must not be silently suppressed.

## 4. Reconstruction of the covering spectrum

Let \(\zeta_{X,k}\) denote the scalar-valued Rumin zeta function on \(X\). The central isotypic decomposition of T033 gives
\[
\zeta_{X,k}(s)
=\sum_{\sigma\in\widehat G}
d_\sigma\,\zeta_{\mathcal M_{\sigma,k}}(s).
\]
Since duality permutes \(\widehat G\) and \(d_{\rho^*}=d_\rho\), Corollary 35.2 yields
\[
\boxed{\displaystyle
\zeta_{X,k}(s)=
\sum_{\rho\in\widehat G}
d_\rho\,\zeta_{M,\rho,k}(s).}
\]
Thus there are two distinct, compatible statements:

- A *single quotient twist* \(\rho\) contributes one multiplicity-space spectrum and has no extra factor \(d_\rho\).
- Reconstructing the *full scalar spectrum on the cover* requires summing all quotient twists with weights \(d_\rho\).

If the analytic torsion is defined by the same fixed finite linear combination of zeta derivatives in every sector, and the determinant-line conventions and cohomology bases are compatible, then
\[
\boxed{\displaystyle
\log T_X=\sum_{\rho\in\widehat G}
d_\rho\log T_{M,\rho}.}
\]
For non-acyclic complexes this last formula is an equality of the corresponding determinant-line metrics only after the determinant-line identifications and basis normalizations are specified. It is not a basis-free equality of unnormalized scalar numbers.

## 5. Application to \(S^3\to S^3/2I\)

Take \(X=S^3\simeq SU(2)\), \(G=2I\), and \(M=S^3/2I\). T031 fixes the free left deck action \(q\mapsto gq\), the commuting right Hopf action, the contact data, and the flat-twist convention. Its naturality argument gives the equivariance required in Theorem 35.1. T024 identifies the dimension-three Kitaoka and Rumin–Seshadri Laplacians under the common contact metric and reconciles the torsion conventions for unitary flat coefficients. T021/T022 supply the character-twisted multiplicity and zeta calculations; T032 supplies the exact Molien coefficient implementation; T033 proves the abstract isotypic and torsion-sum statement.

Therefore the precise interpretation of each T021 twist is:
\[
\text{T021 sector for }\rho
\quad\longleftrightarrow\quad
\text{Rumin spectrum on }S^3/2I
\text{ with flat bundle }E_\rho,
\]
with the upstairs multiplicity-space label \(\rho^*\) under T031's displayed convention. The full cover is reconstructed only after summing the nine quotient twists with the dimension weights.

This is the geometric bridge between the character-twisted calculations and the quotient Rumin complex. It does not independently validate the numerical values in T021; those remain subject to the corrected eventual-Hurwitz and Gamma-product audits recorded in T021–T023.

## 6. Synthesis map and proof dependencies

| Existing result | Exact input used by T035 | What T035 derives |
|---|---|---|
| Covering-space theory | Regular finite cover and deck group | Pullback identification with equivariant sections |
| Associated flat bundle theory | Unitary representation and fixed quotient convention | Diagonal invariant-subspace model |
| Naturality of Rumin complex (T031) | Deck-equivariance of every differential | Descent of the full Rumin complex, including middle operator |
| Unitary spectral theory | Self-adjoint Laplacians commuting with deck action | Equality of quotient twisted and invariant-restriction spectra |
| Finite-group representation theory (T033) | Isotypic decomposition and Schur's lemma | Selection of the \(\rho^*\)-multiplicity space |
| Operator/torsion matching (T024) | Dimension-three common metric and flat-unitary hypotheses | Interpretation in the Kitaoka/Rumin–Seshadri convention |
| Molien/zeta calculations (T021/T022/T032) | Character multiplicity series | Identification of the already-computed twists with quotient local systems |

## 7. Scope and open obligations

**PROVED under the stated hypotheses**
1. Quotient flat-twisted Rumin complex is unitarily equivalent to the diagonal invariant subcomplex upstairs.
2. Its complete spectrum and kernel equal those of the invariant restriction.
3. Under the convention \(F(gx)=\rho(g)F(x)\), the quotient \(\rho\)-twist corresponds to the \(\rho^*\)-multiplicity space.
4. The full-cover zeta function is the dimension-weighted sum of the quotient twisted zeta functions.

**INHERITED under the cited theorem hypotheses**
- \(2I\)-equivariance and contact descent: T031.
- Dimension-three operator/torsion convention matching: T024.
- Twisted character/Molien spectral input: T021/T022/T032.
- Abstract isotypic torsion additivity: T033.

**NOT CLAIMED**
- A new numerical evaluation of any of the nine torsions.
- A completed exact character table or explicit nine-irrep matrix catalogue (delegated to T034).
- Any Q6/PRISM operator intertwining, Mosco convergence, or continuum limit.
- Any physical conclusion about QCD, Yang–Mills or microscopic matter.

## References

1. M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), 727–782, DOI: 10.5802/aif.2693.
2. A. Kitaoka, *Analytic Torsions Associated with the Rumin Complex on Contact Spheres*, Int. J. Math. 31 (2020), 2050112, arXiv:1911.03092.
3. Repository T021, T024, T031, T032 and T033, linked above.

## Classification

- **PROVED:** finite-covering twisted descent and invariant-subspace spectral equivalence, with the stated unitary and domain hypotheses.
- **PROVED:** dual-label rule \(\rho\leftrightarrow\rho^*\) for the explicitly fixed equivariance convention.
- **CONDITIONAL APPLICATION:** \(S^3/2I\) Rumin spectra by T031 and T024.
- **OPEN / SEPARATE AUDIT:** exact explicit irreducible models (T034), corrected numerical torsion verification (T021–T023), and all Q6/PRISM continuum comparisons.
