# C60 intrinsic angular defects and discrete Gauss–Bonnet

## Scope

This audit uses the intrinsic polygonal geometry of the ideal truncated icosahedron, replacing the tree-dependent facewise candidate M_f = B_f(I-D_f) as the preferred intrinsic geometric quantity.

At each vertex v, the angular defect is delta_v = 2*pi - sum of incident face angles. Each C60 vertex is incident to one pentagon and two hexagons: 108°, 120°, 120°, giving 12° = pi/15.

## Checks

- 60 vertices, 90 edges, 32 faces;
- 12 pentagons and 20 hexagons;
- exactly three incident faces at every vertex;
- every vertex defect equals 12°;
- total defect is 720° = 4*pi = 2*pi*chi(S2).

## Distinct defect notions

The intrinsic vertex angle defect is 12° at each of 60 vertices. A crystallographic pentagonal disclination charge relative to a planar hexagonal lattice is conventionally 60° per pentagon; twelve such charges total 720°. These related descriptions are not interchangeable local quantities.

## Frank vector caveat

The scalar defect is intrinsic and gauge/tree independent. A vector omega_v = delta_v n_v is not assigned: a polyhedral vertex has no unique normal. Vectorization requires a declared convention, documented and tested separately.

## Connection comparison

The independent face-connection audit reports 12° vertex-cycle holonomy and total 720° curvature. This script does not rederive transport holonomy; equality is a consistency comparison, not an independent proof of Gauss–Bonnet.

## Classification

- Intrinsic angle defects and total curvature: verified by reconstruction and numerical checks.
- Connection/holonomy agreement: cross-audit consistency check.
- Frank-vector convention: undefined/open.
- Kröner–de Wit or structured-deformation interpretation: research question, not claimed.
- Tree-dependent M_f norms: heuristic archive only, not intrinsic.

## Reproduction

Run: `python scripts/audit_c60_local_angular_defects.py --out-dir c60_local_angular_defects`
