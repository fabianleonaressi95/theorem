# RGS–football quaternionic triplet comparison

## The dimensional mismatch is real

The existing RGS tangent construction has 188 reduced coordinates embedded
in 192 ambient coordinates (64 sites × 3). The football shell has 92 nodes,
276 ambient coordinates and 184 node-wise tangent coordinates. There is no
canonical identification between 188 and 184. In particular, matching the
numbers of components of a triplet is not a geometric map.

## Required transfer

Given an RGS ambient triplet \(A\in\mathbb R^{192\times3}\), a shell
triplet \(B\in\mathbb R^{276\times3}\), and a geometrically justified
transfer \(W\in\mathbb R^{276\times192}\), compare
\(\operatorname{col}(WA)\) with \(\operatorname{col}(B)\). Principal
angles are computed from singular values of \(Q_A^TQ_B\), where columns
of \(Q_A,Q_B\) are orthonormal bases. The transfer must preserve the
intended site/panel correspondence; it is not guessed from array sizes.

## Quaternionic intertwiner

A unit quaternion \(q\) acts on pure imaginary quaternions by
\(p\mapsto qpq^{-1}\), inducing \(R(q)\in SO(3)\). For paired group
generators, seek a nonzero matrix \(X\) such that
\[
S_gX=XR_g.
\]
The code solves the stacked linear system using
\[
\operatorname{vec}(S_gX-XR_g)=
(I\otimes S_g-R_g^T\otimes I)\operatorname{vec}(X).
\]
It reports a normalized residual and quaternion lifts of the supplied
rotations. A small residual is only a candidate: verify group relations,
generator correspondence, commutators with the stiffness operators,
projectors/characters and stability under perturbations.

## What this does and does not establish

- Principal angles quantify alignment of two three-dimensional subspaces
  after an explicit transfer.
- The intertwiner tests equivalence of two supplied three-dimensional
  rotation representations.
- Neither result establishes that a numerically clustered eigenspace is a
  symmetry-protected triplet.
- No RGS-to-football transfer matrix or experimentally identified material
  generators are currently supplied; therefore no physical RGS/football
  matching number is reported.
- The comparison is ready to run once the actual 192-to-276 geometric
  transfer and the corresponding symmetry actions are provided.

Run: `python -m pytest -q tests/test_football_quaternion_bridge.py`.
