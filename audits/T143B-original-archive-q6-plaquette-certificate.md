# T143-B — original archive formula, plaquette and Anti-Twin quotient audit

**Classification:** numerical certificate for the original floating-point archive, plus exact finite combinatorics.  
**Source:** \`psu_fibre_connection_matrices.npz\` and \`RGS_PSU_all_matrices.npz\`.  
**Involution:** \(p(g)=g\oplus7\).

## 1. Result

The original fibre archive is consistent, to machine precision, with the normal-based minimal SO(3) connection and its canonical SU(2) lift. The direct archived-link comparison and all 240 coordinate-square holonomies are Anti-Twin invariant.

The quotient graph has 32 vertex orbits, 96 edge orbits, and is 6-regular.

This is a numerical certificate for the stored arrays. The exact theorem is T143-A; numerical agreement does not replace generator provenance.

## 2. Geometry and formula reconstruction

The 64 archived normals agree exactly with normalized embedding vectors:
\[
\max_g\left\|n_g-\frac{X_g}{\|X_g\|}\right\|=0,
\qquad
\max_g\|n_{g\oplus7}+n_g\|=0.
\]

For every one of the 192 stored directed edges, the archived matrices were compared directly with
\[
R_{gh}=I+[v_{gh}]_\times+\frac{[v_{gh}]_\times^2}{1+c_{gh}},
\qquad
U_{gh}=\sqrt{\frac{1+c_{gh}}2}I_2
-\frac{i}{\sqrt{2(1+c_{gh})}}(v_{gh}\cdot\sigma),
\]
where \(c_{gh}=n_g\cdot n_h\) and \(v_{gh}=n_g\times n_h\).

| Formula fit | Maximum Frobenius residual | RMS residual |
|---|---:|---:|
| SO(3) | \(3.7683\times10^{-15}\) | \(9.5064\times10^{-16}\) |
| SU(2), direct sign | \(1.4066\times10^{-15}\) | \(3.5735\times10^{-16}\) |

The minimum \(1+c_{gh}\) over stored edges is \(0.2274948516\), so the formula denominator is nonsingular.

Archived matrix integrity:
- SO(3) orthogonality residual: \(1.1716\times10^{-15}\);
- SO(3) determinant residual: \(7.7716\times10^{-16}\);
- SU(2) unitarity residual: \(3.2096\times10^{-16}\);
- SU(2) determinant residual: \(2.2888\times10^{-16}\).

## 3. Direct archived-link Anti-Twin replay

All 192 stored links have an antipodal image. Exactly 96 image links are stored with reversed orientation; those were compared using transpose and Hermitian adjoint, respectively.

| Check | Maximum residual |
|---|---:|
| SO(3), direct | \(0\) |
| SU(2), direct lift (not only projective) | \(0\) |
| SU(2), projective | \(0\) |

All 192 direct SU(2) lift signs are \(+1\). Thus the archive does not merely satisfy projective Spin(3) equivariance: with the recorded edge orientation convention, its stored lifts agree directly.

## 4. All 240 Q6 coordinate-square holonomies

The square list is generated from the Q6 bit labels themselves: choose two of the six coordinate directions and fix the other four bits. This gives
\[
\binom62\,2^4=15\cdot16=240
\]
distinct ordered four-edge boundary cycles. Each boundary edge is checked against the archived edge list before multiplying matrices.

Using the column-vector convention \(H=U_3U_2U_1U_0\), the antipodal image of every square has the same archived holonomy:

| Holonomy comparison | Maximum residual |
|---|---:|
| SO(3), all 240 squares | \(0\) |
| SU(2), direct lift, all 240 squares | \(0\) |
| SU(2), projective, all 240 squares | \(0\) |

This closes the earlier gap where the fibre NPZ contained no \`squares\` array. The square boundaries are now reconstructed canonically from the documented Q6 bit-coordinate structure and validated edge-by-edge.

## 5. Anti-Twin quotient graph

Taking the 32 orbits of \(g\sim g\oplus7\) gives:
- 32 quotient vertices;
- 96 quotient edge orbits;
- no quotient loops or duplicate edge orbits;
- degree exactly 6 at every quotient vertex.

This is a finite graph quotient. No manifold or continuum claim is made.

## 6. Operator-level check: \(K_{\rm fibre}\)

The fibre matrix has shape \(128\times128\), with the natural interleaved vertex-spin indexing \(2g+s\). Its \(2\times2\) block pattern confirms this ordering: all nonadjacent Q6 vertex blocks vanish, while every adjacent block has Frobenius norm \(\sqrt2\).

Define the deck action
\[
P_{\rm fibre}e_{g,s}=e_{g\oplus7,s}.
\]
The archived operator satisfies
\[
\|K_{\rm fibre}P_{\rm fibre}-P_{\rm fibre}K_{\rm fibre}\|_F
=6.0354\times10^{-15},
\]
with relative residual \(8.2314\times10^{-17}\). Also,
\[
\|D_{\rm fibre}^{\dagger}D_{\rm fibre}-K_{\rm fibre}\|_F
=3.4857\times10^{-17}.
\]

Consequently the archived \(K_{\rm fibre}\) decouples into the two 64-dimensional eigenspaces of \(P_{\rm fibre}\). The off-diagonal parity block has Frobenius norm \(2.8139\times10^{-15}\).

### Hidden three-generator Clifford symmetry

The exact algebraic implication is isolated in [T143-C — Clifford symmetry and even spectral multiplicity](../theorems/T143C-clifford-symmetry-fibre-operator.md).

The archive exhibits three further commuting symmetries on \(\mathbb C^{64}\otimes\mathbb C^2\):
\[
G_1=T_{\oplus1}\otimes\sigma_3,\qquad
G_2=T_{\oplus2}\otimes\sigma_2,\qquad
G_3=T_{\oplus4}\otimes\sigma_1,
\]
where \(T_{\oplus a}|g\rangle=|g\oplus a\rangle\). Numerically, each \(G_j\) commutes with \(K_{\rm fibre}\) to Frobenius residuals
\[
(6.7704,\ 5.4892,\ 6.5383)\times10^{-15}.
\]
Their squares and Hermiticity residuals are zero, their pairwise anticommutator residuals are zero, and
\[
G_1G_2G_3=-iP_{\rm fibre}
\]
has zero matrix residual.

This gives an algebraic explanation for the Anti-Twin commutation: \(P_{\rm fibre}=iG_1G_2G_3\), so commutation with all three generators implies commutation with \(P_{\rm fibre}\).

It also yields a conditional degeneracy theorem. On either \(P_{\rm fibre}=\pm1\) sector, the three generators give one of the two irreducible two-dimensional complex representations of the three-generator Clifford algebra. Since \(K_{\rm fibre}\) commutes with this algebra, each eigenspace in either parity sector has even complex dimension. The archived spectrum confirms 32 distinct eigenvalues, each of multiplicity two, in each 64-dimensional sector.

**Additional numerical observation:** the sorted spectra of the \(P=+1\) and \(P=-1\) blocks agree to maximum difference \(1.2435\times10^{-14}\). This equality between the two sectors is stronger than the Clifford degeneracy theorem and is not explained by it; it remains a separate structural question.

This operator-level statement is specific to \(K_{\rm fibre}\) and the stated deck action. It is not automatically transferable to \(K_{\rm fibre,biverso}\), \(K_0\), or the tangent operators.

## 7. Reproduction

Run from a checkout with the two original NPZ archives available:

\`\`\`bash
python scripts/audit_t143b_original_archive_q6_plaquettes.py \\
  --fibre data/psu_fibre_connection_matrices.npz \\
  --embedding data/RGS_PSU_all_matrices.npz \\
  --out T143B_original_archive_q6_plaquette_audit.json
\`\`\`

The script independently regenerates the 240 coordinate squares, checks all their boundary edges, compares the archived links with the formulae, replays direct SU(2) signs, computes the quotient graph, and tests the \(K_{\rm fibre}\) commutator and parity blocks.

## 8. Remaining limitation

The numerical results identify the archived arrays with the stated normal-based construction to machine precision. A source-level generator specification is still needed to establish historical provenance—that the matrices were originally produced by these formulae—rather than merely agreeing with them numerically.
