# Q6 / coordinate O_h / antipodal tangent-fibre equivariance audit

**Status: numerical audit executed; proposed fibre identification fails.**

## Input and numbering
Input archive: `RGS_PSU_all_matrices(3).npz`, recovered from the Library. It contains `X_Oh_reconstructed` (64×3), `Q6_states` (64×6), and `Q6_adjacency` (64×64). The state rows are in canonical binary lexicographic order, beginning `000000` and ending `111111`.

## Results
- The signed coordinate-permutation group acting on the recovered point cloud has order **48** (coordinate action O_h); point-matching residual is below 10⁻⁸.
- Only **16/48** of those coordinate actions preserve the Q6 adjacency exactly. The remaining 32 have a nonzero adjacency-entry residual (maximum 1). Thus the recovered point-cloud O_h action is **not** a full graph automorphism action on Q6.
- Direct antipodal matching of X gives **32 pairs**, involutive and exact: maximum \\|x_i+x_{\\pi(i)}\\| = **0**.
- A proxy fibre construction was tested: for each antipodal pair choose one representative direction \\n_k=x_i/\\|x_i\\|\\ and set \\E_k=\\n_k^\\perp\\subset\\mathbb R^3\\. This yields 32 two-dimensional fibres and total dimension 64. The signed-coordinate action permutes these 32 pair fibres.
- On the tetrahedral subgroup plus inversion \\T_h\\ (order 24), the state and candidate-fibre characters differ. Therefore these two 64-dimensional representations are **not equivalent** under this candidate construction; no intertwiner exists for this pair of representations.

## Interpretation
The dimension count 64 = 32×2 is verified, but it is not an equivariant identification. The candidate fibre construction is not the independently defined \\E_f=n_f^\\perp\\ of 32 geometric faces: no canonical 32-face normal dataset was present in the archive. This audit therefore rejects the current antipodal-direction proxy as the proposed map, and leaves the actual face-fibre hypothesis open pending an explicit face/normal definition.

## Reproduction
Run:

```bash
python scripts/audit_q6_oh_face_fibre_equivariance.py data/RGS_PSU_all_matrices.npz --out audits/Q6_Oh_face_fibre_equivariance.json
```

The script is standalone NumPy. It records coordinate group actions, exact adjacency preservation, antipodal pairs, and the T_h character comparison. It does **not** compare eigenvalues or claim a C60 spectral match.
