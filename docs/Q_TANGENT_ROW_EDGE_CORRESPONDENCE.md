# Superseded: Q_tangent row interpretation

This earlier note incorrectly treated the 192 rows of `Q_tangent` as
unlabelled graph-edge coordinates. That interpretation is false.

The 192 rows are the 64 vertex displacement triples
((\delta x_i,\delta y_i,\delta z_i)), in vertex-major order. This is fixed
by the A14 constraint Jacobian: its first three rows are uniform Cartesian
translations and its fourth row is (X_{flat}^T).

The correct reconstruction is documented in
[Q6_TANGENT_188D_RECONSTRUCTION.md](Q6_TANGENT_188D_RECONSTRUCTION.md) and
implemented by `scripts/reconstruct_q6_tangent_188d_action.py`.

Do not use a row-to-edge map or an edge permutation matrix to act on
`Q_tangent`.
