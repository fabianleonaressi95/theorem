# T157 — Metric obstruction to a vertex-fixed rhombicuboctahedron split

**Status:** exact Euclidean obstruction for the vertex-fixed diagonal-splitting interpretation; the moving-face/hinged construction described by In2Infinity remains open.

## 1. Statement

Let a regular rhombicuboctahedron have edge length 1. Split each of its twelve lateral square faces along one diagonal, keeping all 24 original vertices fixed. The resulting triangulated surface is **not** metrically a regular snub cube.

## 2. Proof

Every split square has side length 1. By the Euclidean Pythagorean theorem, either diagonal has length
\[
d=\sqrt{1^2+1^2}=\sqrt2.
\]
Each of the two triangles produced by the split therefore has side lengths
\[
(1,1,\sqrt2),
\]
and is a right isosceles triangle, not an equilateral triangle.

A regular snub cube has 32 equilateral triangular faces and 6 square faces; all of its edges have one common length. Thus the split faces cannot be the triangular faces of a regular snub cube under a vertex map that preserves the original rhombicuboctahedron vertices and edge lengths: the new diagonal edges have length \(\sqrt2\), while the original edges have length 1.

This is an exact obstruction, independent of coordinate-rounding or numerical tolerance.

## 3. Scope and interpretation

The obstruction rules out only the **static, vertex-fixed split**. It does not rule out a continuous deformation in which the square panels rotate and their vertices move. Such a construction would need to specify:

1. the hinge axes and which vertices move together;
2. the coordinate path of all 24 vertices;
3. preservation (or an explicitly stated change) of the relevant edge lengths;
4. the planarity of every face throughout the motion;
5. the endpoint map to a unit-edge snub cube;
6. the meaning of the reported \(22.5^\circ=\pi/8\) rotation, including its axis and reference frame.

The source's statement that the square faces rotate by 22.5 degrees is therefore a kinematic hypothesis to reconstruct, not a consequence of the diagonal split. The source also describes a 45-degree rotational freedom of the octagonal midsection; no identity between that 45-degree freedom and the claimed 22.5-degree face rotation is assumed here.

## 4. Consequence for T156

T156 remains a finite incidence result: the two alternating diagonal patterns give the snub-cube incidence type. T157 adds the missing metric distinction. Incidence isomorphism does not imply equality of embedded edge lengths, and the vertex-fixed split cannot be the claimed geometric transition.

The next valid route is to reconstruct the moving-panel mechanism from an explicit hinge/vertex correspondence, rather than trying to infer it from the face-count pattern.

## 5. Sources

- In2Infinity, “Brillouin Zones and the Geometry of Ferromagnetic and Electrically Conductive Waves” (reports the 22.5-degree face rotation): https://in2infinity.com/brillouin-zones-and-the-geometry-of-ferromagnetic-and-electrically-conductive-waves/
- In2Infinity, “Archimedean Solids” (describes snubbing as twisting faces and filling gaps with triangles): https://in2infinity.com/ultimate-guide-to-geometry/regular-and-semi-regular-polyhedra
- In2Infinity, “D-orbital Geometry — Part 1” (describes the rhombicuboctahedron's octagonal midsection and 45-degree rotations): https://in2infinity.com/d-orbital-geometry-part-1/

Reproducibility: `tests/test_t157_vertex_fixed_metric_obstruction.py` checks the exact Pythagorean ratio at the normalized edge-length level.
