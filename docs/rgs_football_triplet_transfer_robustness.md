# RGS–football rotational-triplet transfer: robustness audit

## Purpose

This note formalises the numerical comparison between the 188-dimensional RGS
constraint tangent space and the 184-dimensional tangent space of the current
92-node football shell. It adds a controlled sensitivity study for the
geometric transfer and algebraic checks of the quaternion lift.

The comparison is **geometric and numerical**. It is not a proof that the two
discretisations describe the same microscopic physics, and it does not identify
the rotational triplet with the separate (T_{2u}) mode.

## Source tangent space and rotational triplet

The source configuration is (X=(x_1,\ldots,x_{64})\in\mathbb R^{64\times3}).
The four linear constraints are the three zero-translation constraints and the
fixed radial/scale constraint represented by the flattened vector (X).
Writing their matrix as (C\in\mathbb R^{4\times192}), the exact tangent
space is

\[
  \mathcal T_{\rm RGS}=\ker C,\qquad
  \dim\mathcal T_{\rm RGS}=192-\operatorname{rank}C=188.
\]

For the three Cartesian angular-velocity generators (e_a), define

\[
  G_a=(e_a\times x_i)_{i=1}^{64},\qquad
  G_{\rm tan}=Q Q^T G,
\]

where the columns of (Q\) are an orthonormal basis of \(\ker C\).
The three-dimensional rotational space is obtained by rank-revealing SVD of
(G_{\rm tan}). This construction is kinematic: it does not select modes
from the unavailable original RGS Hessian.

## Directional degeneracy and transfer construction

The source has 64 points but only 56 distinct unit directions. Eight directions
(the body-diagonal directions) occur twice at different radii. A nearest-neighbor
query on all 64 points can therefore choose an arbitrary representative when
distances tie. This is a data-structure ambiguity, not a physical degeneracy
that should be silently discarded.

The revised transfer groups source points whose unit directions differ by at
most (10^{-10}). Local affine weights are computed on the unique directions,
then the weight of each direction is split equally among its radial
representatives. Thus the transfer still acts on all 64 source sites, while
its directional interpolation is independent of KD-tree tie-breaking.

For each target unit direction (n_j\), and a selected set (I_j\) of (k\)
distinct source directions (u_i\), the local minimum-norm weights solve

\[
 \min_w\|w\|_2^2,\qquad
 \sum_{i\in I_j}w_i=1,\qquad
 \sum_{i\in I_j}w_i u_i=n_j.
\]

The 92 scalar weights are lifted identically over the three Cartesian
components, giving (W\in\mathbb R^{276\times192}). The shell-node tangent
projection is then applied before computing principal angles.

## Robustness grid

The executable audit evaluates

\[
  k\in\{8,12,16,24,32\}
\]

distinct source directions. For every (k\), it records:

- number and sizes of coincident-direction groups and radial spreads;
- minimum separation among unique directions;
- maximum local constraint condition number;
- affine reproduction and row-sum residuals;
- rank and singular values of the transferred triplet;
- three principal angles against the three lowest shell tangent eigenmodes.

The spread of each principal angle across the grid is a sensitivity diagnostic.
It is **not** a convergence theorem. A stable result across this finite grid
would strengthen numerical robustness, but further tests under mesh refinement,
alternative transfer families, and material calibration remain necessary.

## Quaternionic formulation and what the audit proves

At each shell node, an oriented orthonormal frame is encoded by a scalar-first
unit quaternion (q=[w,x,y,z]). A tangent vector is represented by a pure
imaginary quaternion (p=[0,v]) and transported by

\[
  p\longmapsto q p q^{-1}.
\]

The audit checks the rotation action, composition, and double-cover identity
(q\) and (-q\) inducing the same (SO(3)) action. It also computes an
identity-intertwiner calibration on the abstract three-dimensional vector
representation.

That calibration is deliberately **not** described as a physical intertwiner
between the RGS point set and the football mesh. Such a claim requires
independently defined group actions on both discrete spaces, verification of
their group relations and commutators, and stability under the transfer and
mesh-refinement studies. The current football mesh has icosahedral construction
while the RGS source has octahedral structure; a shared full symmetry group
must not be assumed.

## Reproducibility

Run from the repository root:

```bash
python scripts/audit_rgs_football_transfer_robustness.py
python -m pytest -q tests/test_rgs_football_triplet_spectral_comparison.py
```

The audit writes:

- `reports/rgs_football_transfer_robustness.json`
- `reports/rgs_football_transfer_robustness.npz`

The JSON contains all per-(k) diagnostics and quaternion residuals; the NPZ
contains the grid, principal-angle matrix, shell eigenvalues, source tangent
basis, and source rotational triplet. The test suite executes the complete
five-point grid, so a successful CI run verifies the calculation rather than
only checking that the modules import.

## Evidence classification

| Statement | Status |
|---|---|
| (\dim\ker C=188) and the source rotational generators have rank 3 | Numerically verified by the audit |
| 64 source points reduce to 56 distinct directions, with eight duplicated direction pairs | Explicitly verified from the source coordinates |
| Direction-grouped affine transfer reproduces constants and directions to numerical tolerance | Numerically verified per neighbor count |
| Principal-angle alignment is stable across (k=8,12,16,24,32) | To be filled from the executed CI report; not assumed here |
| Quaternion double-cover and composition identities | Algebraic numerical checks |
| A physical symmetry-protected common eigenspace or shared microscopic dynamics | Open; not established |
| Experimental validation of shell material parameters | Open; requires scans and coupon/constitutive data |
