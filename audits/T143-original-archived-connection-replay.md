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
