# T143 — direct replay of the archived fibre connection

**Status: implementation added; numerical replay not yet executed.** This is deliberately separate from the earlier reconstructed-connection audit.

## Purpose

Compare the original arrays `edges`, `R_SO3`, and `U_SU2` in
`psu_fibre_connection_matrices.npz` under the geometric involution
\[
p(g)=g\oplus7.
\]
No link is reconstructed from the embedding.

## Orientation rule

For a stored oriented edge \(g\to h\), find the stored edge representing
\(p(g)\to p(h)\). If its stored orientation is reversed, compare using
\[
R_{p(g)p(h)}=R_{\rm stored}^{T},\qquad
U_{p(g)p(h)}=U_{\rm stored}^{\dagger}.
\]
The SO(3) residual is the Frobenius norm of the matrix difference. The SU(2)
residual is projective:
\[
\min\{\|U'-U\|_F,\|U'+U\|_F\}.
\]
The edgewise signs are reported separately; sign variation alone is not a
failure of SO(3) equivariance.

## Run

```bash
python scripts/audit_t143_original_archived_connection.py \
  --fibre psu_fibre_connection_matrices.npz \
  --embedding RGS_PSU_all_matrices.npz \
  --out T143_original_connection_antipodal_replay.json
```

For plaquettes, supply a separate NPZ whose `squares` array consists of
ordered four-vertex boundary cycles:

```bash
python scripts/audit_t143_original_archived_connection.py \
  --fibre psu_fibre_connection_matrices.npz \
  --embedding RGS_PSU_all_matrices.npz \
  --squares Q6_exact_incidence_and_H241.npz
```

The square-cycle input must genuinely be an ordered vertex-cycle array of
shape \((240,4)\); an incidence matrix or unordered face record is not a
substitute.

## Evidence boundary

The script and this specification are committed, but no numerical result is
claimed until the script is run against the original binary arrays. The
plaquette test remains conditional on verifying the source format and order
of the square cycles. The earlier T143 reconstructed-connection results are
not promoted to results about the archived links.
# T143 — direct replay of the original archived fibre connection

**Status: numerical replay completed.**

The original NPZ arrays have now been checked directly. The full certificate,
including formula fit, all 192 links, all 240 coordinate-square holonomies,
the quotient graph, and the (K_{\rm fibre}) operator checks, is in
[T143-B — original archive and Q6 plaquette certificate](T143B-original-archive-q6-plaquette-certificate.md).

## Original archived links

For each stored oriented edge (g\to h), the replay locates the stored
representative of (p(g)\to p(h)), where (p(g)=g\oplus7). Reversed
storage orientation is handled with
[
R_{hg}=R_{gh}^{T},qquad U_{hg}=U_{gh}^{\dagger}.
]

Observed result on all 192 links:
- 96 antipodal image links are stored with reversed orientation;
- SO(3) direct maximum residual: 0;
- SU(2) direct-lift maximum residual: 0;
- all 192 SU(2) edge signs are (+1).

## Canonical formula fit

The stored matrices agree with the normal-based minimal-rotation SO(3)
formula and the fixed canonical SU(2) lift to machine precision. Maximum
Frobenius residuals:
[
3.7683\times10^{-15}quad(SO(3)),qquad
1.4066\times10^{-15}quad(SU(2),\text{ direct sign}).
]

## Plaquette replay

The 240 ordered Q6 coordinate-square boundaries are generated from the
six bit directions and checked edge-by-edge against the archive. For all
240 squares, the archived SO(3) and direct SU(2) holonomies equal those
of their antipodal image with maximum residual 0.

This closes the former missing-`squares`-array gap: the cycles are
constructed canonically from the Q6 bit-coordinate definition, not
guessed from an unordered incidence matrix.

## Reproduction

```bash
python scripts/audit_t143b_original_archive_q6_plaquettes.py \\
  --fibre data/psu_fibre_connection_matrices.npz \\
  --embedding data/RGS_PSU_all_matrices.npz \\
  --out T143B_original_archive_q6_plaquette_audit.json
```

The earlier `audit_t143_original_archived_connection.py` remains the
link-only replay utility. The T143-B script is the complete formula,
plaquette, quotient, and fibre-operator audit.

## Remaining limitation

The original archive matches the declared construction to machine
precision. Historical generator provenance—documentation that the
original matrices were produced by those formulae—remains to be recovered
or written from the source construction.
