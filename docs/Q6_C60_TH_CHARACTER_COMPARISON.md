# Q6 versus actual C60 face-tangent representation: T_h character test

**Classification:** numerical/geometric representation audit. The proposed equivalence is rejected for the coordinate-induced Q6 action tested.

## Construction
C60 is generated as the truncated regular icosahedron. Its 32 polygonal faces are recovered from the convex hull and supporting planes: 12 pentagons and 20 hexagons. Each face with outward unit normal n_f carries E_f=n_f-perp in R^3, so the direct sum has dimension 64.

The proper icosahedral rotation group I (order 60) is generated from the golden-ratio icosahedron. An A4 subgroup (order 12) is selected; adjoining inversion gives T_h=A4 x C2 (order 24).

On Q6, the tested T_h action is induced by signed-coordinate transformations preserving the reconstructed X_Oh point cloud. The action on the 64 labels is obtained by point matching.

## Character calculation
A C60 face contributes to the trace only when its outward normal is fixed. For a proper orthogonal transformation R:
\[
\chi_f(R)=\operatorname{tr}(R|_{n_f^\perp})
=\operatorname{tr}(R)-n_f^T R n_f.
\]
The total character sums over fixed faces. The inversion coset is evaluated using -R.

Expected character multisets from the calculation:
- Q6 states on A4: identity 64; eight order-three elements 4; three order-two elements 0.
- C60 face-tangent bundle on A4: identity 64; eight order-three elements -2; three order-two elements 0.
- Both inversion cosets: character 0 on all 12 elements.

The order-three characters differ, so the representations are inequivalent. This mismatch is invariant under any abstract A4 isomorphism because all eight order-three elements have the same character in each representation. No invertible intertwiner exists for this pair.

## Additional obstruction
Only a proper subset of the coordinate-induced Q6 T_h transformations preserves Q6 adjacency. Therefore this is not a symmetry representation of the Q6 graph Laplacian. Spectral comparison with K0 or a C60 vibrational operator is not authorized.

## Reproduction
python scripts/compare_q6_c60_th_characters.py data/RGS_PSU_all_matrices.npz --out audits/Q6_C60_T_h_character_comparison.json
