# T155 — Rhombic cuboctahedron to snub cube: the 22.5-degree hinge claim

**Status:** exact combinatorial compatibility proved; geometric realization and continuous rigid motion **open**.

## 1. Source statement

In2Infinity's *Brillouin Zones and the Geometry of Ferromagnetic and Electrically Conductive Waves* describes the transition from the rhombic cuboctahedron to the snub cube as a rotation of square faces by (22.5^\circ) about the (x,y,z) axes. It says that a diagonal across twelve square faces collapses into two triangles, while the snub cube is chiral and admits clockwise and anticlockwise versions.

This is recorded as a source claim, not accepted as a proved kinematic construction. The source text available to this audit does not specify the hinge axes, the exact twelve faces, a vertex correspondence, a path parameter, or the rigidity constraints.

## 2. Exact incidence-count test

The audited endpoint combinatorics are:

- rhombic cuboctahedron: (V=24, E=48, F=26), with 8 triangular and 18 square faces;
- snub cube: (V=24, E=60, F=38), with 32 triangular and 6 square faces.

Triangulating twelve distinct quadrilateral faces by adding one diagonal to each gives:

[
F_3'=8+2(12)=32,\
F_4'=18-12=6,\
E'=48+12=60,\
V'=24.
]

Thus the proposed face-splitting operation has exactly the face and edge counts of the snub cube, and preserves the vertex count. Euler's relation is preserved:
[
24-60+38=2.
]

This is an exact combinatorial compatibility certificate. It does **not** prove that the resulting triangulated abstract polyhedron is the snub cube's incidence complex, because the face-adjacency pattern and diagonal choices have not yet been matched. It also does not prove that the new triangles are equilateral or that the motion is isometric.

## 3. Necessary geometric data

A genuine (22.5^\circ) rigid-hinge construction must provide:

1. an explicit list of the twelve square faces that split, and the six that remain square;
2. a vertex/edge/face correspondence between the two endpoint coordinate models;
3. a hinge line and rotation axis for every moving face (or a precisely defined simultaneous group action);
4. a continuous parameter (t\in[0,1]), with endpoint coordinates (X_v(t));
5. proof or certified interval verification that all required edge lengths remain constant, the faces remain planar, and no forbidden self-intersections occur;
6. a chirality convention distinguishing the two snub-cube enantiomorphs.

The angle (22.5^\circ=\pi/8) is a source-reported endpoint rotation. It must not be used as a fitted free parameter. The geometric audit should test the reported value against a construction derived from the incidence and hinge data.

## 4. Relation to T154

T154 reconstructs the five static endpoint solids and identifies multiple face-plane orbits for the IN-sphere convention. T155 isolates one specific transition in that sequence. It does not resolve the other transitions (octahedron/icosahedron/cuboctahedron), nor the atomic-radius mapping.

## 5. Verdict

- **Proved:** the stated twelve-square triangulation has the correct endpoint (V,E,F) and face-size counts.
- **Not proved:** that a choice of twelve diagonals gives the snub-cube incidence complex.
- **Open:** the (22.5^\circ) hinge path, edge-length preservation, planarity, collision-free motion, and chirality correspondence.
- **Not inferred:** any explanation of magnetic order, atomic radii, or electronic structure.

## Source

In2Infinity, “Brillouin Zones and the Geometry of Ferromagnetic and Electrically Conductive Waves,” https://in2infinity.com/brillouin-zones-and-the-geometry-of-ferromagnetic-and-electrically-conductive-waves/
