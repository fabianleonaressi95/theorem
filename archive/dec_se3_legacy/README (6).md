# Discrete \(SE(3)\) Defect Program

This directory contains four independent mathematical specifications.

| Specification | Status | Purpose |
|---|---|---|
| `T-DEC-SE3.md` | Foundational | Discrete \(SE(3)\) bundle, connection, holonomy, covariant coboundary |
| `T-DEWIT.md` | Derivation needed | Torsion, plastic distortion, dislocation density |
| `T-BIANCHI.md` | Derivation needed | Discrete curvature and torsion Bianchi identities on 3-cells |
| `T-H2-DISLOC.md` | Open problem | Burgers flux, twisted cohomology, curvature correction |

## Non-negotiable rules

1. Do not identify the affine face defect \(b_f\) with a physical Burgers density without deriving the relation.
2. Do not assume \(d_A^2=0\) unless the connection is flat.
3. Do not validate a 3D Bianchi identity using C60 alone.
4. Do not claim cohomological invariance without flatness and cocyclicity.
5. Do not merge a theorem before its definitions, proof, and failing tests are complete.
6. Do not present the global deformation \(g\) as solved until an explicit construction or impossibility result is available.

## Implementation order

1. Implement and test T-DEC-SE3.
2. Define the discrete co-frame and derive T-DEWIT.
3. Construct a volumetric complex and derive T-BIANCHI.
4. State and test the conditional homological theorem in T-H2-DISLOC.
5. Only then investigate the existence or obstruction of a global deformation \(g\).
