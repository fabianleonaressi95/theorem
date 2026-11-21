# C60: reconstructed face connection and I_h spectral audit

## Scope

This audit reconstructs the truncated-icosahedron face structure from the
icosahedron coordinates already defined in
`scripts/audit_c60_mmff94s_relaxed_coulomb.py`. It does not rely on a
hand-entered list of the 32 faces.

The ideal geometry is the symmetry reference. The MMFF94s geometry uses the
same atom indexing and inherits the face cycles from the ideal cage; face
normals are recomputed by a best-fit plane. The relaxed geometry is **not**
assumed to retain exact I_h symmetry.

## Reconstructed combinatorics

The convex hull of the 60 directed-edge points is triangulated by Qhull.
Coplanar triangular facets are merged into polygonal faces. The audit checks:

- 60 vertices;
- 90 edges, each incident to exactly two faces;
- 12 pentagons and 20 hexagons;
- 32 faces and Euler characteristic 2.

The dual graph has one vertex per face and one edge per shared cage edge.

## Rank-two connection

For each face f, the fibre is the two-dimensional plane perpendicular to its
outward normal n_f. A deterministic orthonormal frame B_f identifies it with
R^2. For adjacent faces f,g sharing an edge with unit tangent t, set

```math
m_f=n_f\times t, \qquad m_g=n_g\times t,
\qquad T_{fg}=tt^T+m_gm_f^T.
```

The 2 by 2 transport matrix is A_fg=B_g^T T_fg B_f. The script checks the
ambient partial-isometry identities and A_fg^T A_fg=I_2.

The connection energy and matrix are

```math
E(u)=\frac12\sum_{\{f,g\}}\|A_{fg}u_f-u_g\|^2,
\qquad E(u)=\frac12 u^T L_T u.
```

The scalar dual graph Laplacian is assembled from the same face-edge
incidence, allowing a direct spectral comparison.

## I_h action and irreducible decomposition

The 120 orthogonal symmetries are reconstructed from the icosahedron vertex
Gram geometry. Each operation induces a permutation of the 32 face centroids
and an orthogonal 2 by 2 change of fibre frame. The induced 64 by 64 action U(g)
is checked for orthogonality and for

```math
\|L_T U(g)-U(g)L_T\|_F.
```

The irreducible representations of I_h=A_5 x C_2 are built from the five
real A_5 character rows (dimensions 1,3,3,4,5) and the two inversion parities.
For each irrep rho, the central isotypic projector is

```math
P_\rho=\frac{d_\rho}{120}\sum_{g\in I_h}
\chi_\rho(g^{-1})U(g).
```

The report includes projector ranks, multiplicities, idempotence residuals,
pairwise orthogonality, completeness, and the spectrum of L_T restricted to
each isotypic subspace.

## Relaxed geometry

When `--mmff-npz` is supplied, the face cycles are inherited by atom index
from the ideal cage and the connection Laplacian and its spectrum are
recomputed using relaxed coordinates. The ideal I_h representation is not
imposed on this geometry: a generic relaxed point cloud need not be invariant
under the ideal orthogonal group. The ideal run is the symmetry decomposition;
the relaxed run is a geometric perturbation/spectral comparison.

## Reproduction

```bash
python scripts/audit_c60_icosahedral_connection.py \
  --out-dir c60_icosahedral_ideal

python scripts/audit_c60_mmff94s_relaxed_coulomb.py \
  --out-dir c60_mmff94s_start

python scripts/audit_c60_icosahedral_connection.py \
  --mmff-npz c60_mmff94s_start/C60_MMFF94s_relaxed_coulomb.npz \
  --out-dir c60_icosahedral_mmff94s
```

The GitHub Actions workflow runs all three stages and uploads the JSON and NPZ
artifacts. No numerical spectrum, multiplicity, or successful test is claimed
until the workflow artifacts have been inspected.

## Classification

- Geometry reconstruction and operator definitions: implemented, awaiting run.
- I_h commutator and character-projector tests: implemented, awaiting run.
- Ideal-vs-MMFF94s spectral comparison: implemented, awaiting run.
- Any interpretation of spectral multiplicities as physical modes: open; it
  requires independent mathematical and physical justification.
