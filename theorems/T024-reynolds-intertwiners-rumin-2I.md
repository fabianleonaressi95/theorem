# T024 — Reynolds projectors and equivariance of the Rumin differential on S³/2I

**Status:** the operator-level equivariance statement is proved abstractly from naturality of the Rumin complex under contact transformations. The resulting isotypic block decomposition is exact. Explicit matrices for the Rumin differential in Kitaoka's harmonic bases, and a numerical comparison of each block's (D^\dagger D) spectrum, remain open.

**Base:** T023, branch `t023-symbolic-gamma-2i`.  
**Group:** the binary icosahedral group (2I\subset SU(2)), of order 120.  
**Geometric input:** the standard CR/contact structure on (S^3\subset\mathbb C^2), preserved by the (SU(2)) action.

## 1. Setup and conventions

Let (G=2I), and let (widehat G) be its set of nine irreducible complex representations. Write (d_\rho=\dim V_\rho) and (chi_\rho) for the character of (\rho).

For a finite-dimensional (G)-module (W), denote its representation by (U_W(g)). The central Reynolds projector onto the full (\rho)-isotypic component is

\[
\boxed{
P_{\rho,W}=\frac{d_\rho}{|G|}
\sum_{g\in G}\overline{\chi_\rho(g)}\,U_W(g).
}
\tag{1}
\]

The character factor is (\overline{\chi_\rho(g)}=\chi_\rho(g^{-1})). The operator (1) is the *isotypic* projector; it is not a rank-one or matrix-unit projector onto a single copy of (V_\rho).

For the (SU(2)) harmonic module
\[
V_m=\operatorname{Sym}^m(\mathbb C^2),
\qquad \dim V_m=m+1,
\]
we write (U_m=\operatorname{Sym}^m|_G) and (P_{\rho,m}=P_{\rho,V_m}).

## 2. Exact projector identities

Character orthogonality for finite groups gives
\[
P_{\rho,W}^2=P_{\rho,W},\qquad
P_{\rho,W}^*=P_{\rho,W},
\]
\[
P_{\rho,W}P_{\sigma,W}=0\quad(\rho\ne\sigma),
\qquad
\sum_{\rho\in\widehat G}P_{\rho,W}=I_W.
\tag{2}
\]

Moreover, (P_{\rho,W}) is central in the image of the group algebra:
\[
P_{\rho,W}U_W(h)=U_W(h)P_{\rho,W}
\quad(h\in G).
\tag{3}
\]

Its rank is determined by the character inner product:
\[
\operatorname{rank}P_{\rho,W}
=d_\rho\,\dim\operatorname{Hom}_G(V_\rho,W)
=\frac{d_\rho}{|G|}
\sum_{g\in G}\overline{\chi_\rho(g)}\chi_W(g).
\tag{4}
\]

For (W=V_m), (\chi_W=\chi_m), where
\[
\chi_0(g)=1,\quad \chi_1(g)=\chi_{\mathbb C^2}(g),\quad
\chi_m=\chi_1\chi_{m-1}-\chi_{m-2}.
\tag{5}
\]
The trivial-isotypic multiplicity used in T021–T023 is the special case
\[
a_m=\dim(V_m^G)=\frac1{120}\sum_{[g]}|[g]|\chi_m(g).
\tag{6}
\]
Notice the distinction between (a_m), the multiplicity of the trivial representation, and the rank of a general (P_{\rho,m}), which includes the factor (d_\rho).

## 3. Naturality of the Rumin differential

Let ((M,H,J,\theta)) be the standard contact/CR three-sphere and let (D_R) denote any of the natural Rumin differentials in its complex, with the relevant source and target bundles denoted (E^j) and (E^{j+1}).

A contact transformation (h) preserving the CR structure acts by pullback on the Rumin bundles. Naturality of the construction means
\[
D_R\,U_j(h)=U_{j+1}(h)\,D_R.
\tag{7}
\]
The standard (SU(2)) action on (S^3\subset\mathbb C^2) preserves the contact form up to the chosen invariant normalization and preserves the standard CR structure. In particular, every (h\in2I\subset SU(2)) satisfies the hypotheses of (7).

Define (P^j_\rho) by (1) on (E^j). Multiplying (7) by the character weight and summing over the finite group gives
\[
\begin{aligned}
D_RP^j_\rho
&=\frac{d_\rho}{120}\sum_{g\in G}
\overline{\chi_\rho(g)}D_RU_j(g)\\
&=\frac{d_\rho}{120}\sum_{g\in G}
\overline{\chi_\rho(g)}U_{j+1}(g)D_R\\
&=P^{j+1}_\rho D_R.
\end{aligned}
\]
Therefore
\[
\boxed{D_RP^j_\rho=P^{j+1}_\rho D_R.}
\tag{8}
\]

This is an exact intertwining identity. It is not a numerical observation and does not depend on a choice of harmonic basis.

## 4. Isotypic subcomplexes and quotient interpretation

Equation (8) implies
\[
D_R\bigl(\operatorname{im}P^j_\rho\bigr)
\subseteq\operatorname{im}P^{j+1}_\rho.
\]
Thus the Rumin complex decomposes into (G)-isotypic subcomplexes:
\[
(E^\bullet,D_R)
\cong
\bigoplus_{\rho\in\widehat G}
(\operatorname{im}P^\bullet_\rho,
D_R|_{\operatorname{im}P^\bullet_\rho}).
\tag{9}
\]

The trivial representation gives the (G)-invariant complex, which is the scalar quotient sector on (S^3/G). Nontrivial isotypic sectors should be interpreted as the corresponding equivariant/associated-bundle sectors on the quotient; they are not scalar functions or scalar forms on the quotient. This distinction matters when comparing twisted analytic torsions.

If the chosen Laplacian is built functorially from the differential and its adjoint using a (G)-invariant Hermitian metric, then the projectors also commute with it:
\[
\Delta_RP^j_\rho=P^j_\rho\Delta_R.
\tag{10}
\]
Indeed, (8), its adjoint, and unitarity of the (G)-action imply commutation with each constituent (D_R,D_R^*\).

## 5. What follows for the Kitaoka calculation

The (SU(2))-types (V_m=\operatorname{Sym}^m(\mathbb C^2)) used in the (n=1) spectral decomposition are stable under (2I). Their (2I)-isotypic components can therefore be selected by the projectors (1). This justifies organizing equivariant spectral multiplicities by irreducible (2I)-type.

It does **not**, by itself, identify a concrete matrix for (D_R) in the ((q,p)) basis, nor does it prove that a proposed finite matrix has Kitaoka's eigenvalues. To make that stronger claim, the actual Rumin operator and the inner products defining its adjoint must be represented in the same basis.

In particular, the scalar character average (a_m) in (6) is sufficient for the untwisted invariant sector, but not for the full nine-twist audit. For a general twist the correct multiplicity is the character inner product (4), with the actual irreducible character (\chi_\rho).

## 6. Explicit finite-dimensional verification still required

The next computational stage must construct, from the geometric differential and not from a freely chosen intertwiner:

1. matrices (U^j_m(g)) on the source and target harmonic-form spaces;
2. the matrix (D_{R,m}) in the same bases;
3. the nine central projectors (P^j_{\rho,m});
4. residuals for
   \[
   \|D_{R,m}P^j_{\rho,m}-P^{j+1}_{\rho,m}D_{R,m}\|;
   \]
5. block spectra of (D_{R,m}^*D_{R,m}), compared with the corresponding Kitaoka eigenvalue and multiplicity lists.

For exact arithmetic, the representation matrices and character values should be expressed in the appropriate algebraic number field (at least (\mathbb Q(\sqrt5)), with any additional roots of unity required by the chosen realization). Floating-point residuals are supplementary checks, not substitutes for the exact identities.

## 7. Acceptance criteria and status ledger

| Claim | Status |
|---|---|
| Central Reynolds formula (1) | Exact finite-group identity |
| Projector orthogonality/completeness (2) | Exact consequence of character orthogonality |
| Rumin naturality (7) under (2I) | Geometric theorem, given the standard invariant CR/contact structure |
| Differential intertwining (8) | Exact consequence of naturality |
| Isotypic subcomplex decomposition (9) | Exact consequence of (8) |
| Laplacian block decomposition (10) | Exact when the metric and adjoint are (G)-invariant |
| Explicit harmonic-basis matrices for (D_R) | Open |
| Numerical/exact block-spectrum comparison with Kitaoka | Open |
| Full convention match with Rumin–Seshadri torsion | Open; see T021–T023 |

## References

1. A. Kitaoka, *Analytic torsions associated with the Rumin complex on contact spheres*, Int. J. Math. 31 (2020), 2050112, [arXiv:1911.03092](https://arxiv.org/abs/1911.03092).
2. M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), 727–782, [DOI: 10.5802/aif.2693](https://doi.org/10.5802/aif.2693).
3. A. Kitaoka, *Ray–Singer Torsion and the Rumin Laplacian on Lens Spaces*, SIGMA 18 (2022), 091, [arXiv:2009.03276](https://arxiv.org/abs/2009.03276).

## Classification

- **Proved:** finite-group projector identities and their intertwining with any (2I)-equivariant Rumin differential.
- **Geometric input:** naturality of the Rumin complex under the (2I) contact/CR action.
- **Not yet computed:** explicit differential matrices and blockwise (D_R^*D_R) spectra.
- **Not claimed:** a new spectral formula, a completed Kitaoka/Rumin–Seshadri convention match, or a physical interpretation beyond this geometric representation-theoretic result.
