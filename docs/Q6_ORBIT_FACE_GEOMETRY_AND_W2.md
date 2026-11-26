# Q6 D4-orbit face geometry: exact classification before W2

**Status:** exact geometric classification algorithm added; the audit and tests have not yet been executed in this session. No face mass matrix is claimed.

## Purpose

The D4 orbit-edge complex has 64 vertices, 256 unoriented edges, and 384 distinct cyclic square 2-cells. A cyclic 2-cell is combinatorial data; its four six-bit vertices need not bound a planar Euclidean square in the canonical embedding \(x(v)=v\in[0,1]^6\subset\mathbb R^6\).

This audit classifies every distinct cyclic face in that fixed embedding using exact integer arithmetic. It does not silently replace a nonplanar cycle by a chosen triangulated surface.

## Exact tests

For a cyclic face \(F=(v_0,v_1,v_2,v_3)\), form

\[
A_F=[x(v_1)-x(v_0)\; x(v_2)-x(v_0)\; x(v_3)-x(v_0)].
\]

Its affine rank is the exact rank of this \(6\times3\) integer matrix.

- rank 2: the four vertices are coplanar;
- rank 3: the cycle is nonplanar in the chosen embedding.

The parallelogram condition is tested coordinatewise:

\[
x(v_0)+x(v_2)=x(v_1)+x(v_3).
\]

For a planar cycle, the audit also computes the squared norm of its oriented area bivector:

\[
\mathcal A_F=\frac12\sum_{i=0}^{3}x(v_i)\wedge x(v_{i+1}),\qquad
A_F^2=\lVert\mathcal A_F\rVert^2,\quad v_4=v_0.
\]

All these calculations are exact. A nonzero oriented area is a useful nondegeneracy certificate, but it does not by itself certify that the ordered quadrilateral is a simple polygon.

## Classification

The output partitions all 384 cyclic faces into three classes: planar with nonzero oriented area, planar degenerate, and nonplanar. It separately counts parallelograms. The per-face records retain the canonical cyclic vertex order, affine rank, parallelogram flag, and exact area-squared value where defined.

## Why this audit does not yet assign W2

A face mass depends on more than four vertices and a positive area. We must also specify:

- whether the ordered planar polygon is simple and which filling it bounds;
- the face finite-element space/basis (e.g. constant integrated 2-form or a specified Whitney construction);
- orientation and normalization conventions;
- how the local face inner products assemble and transform under D4.

For a planar simple face with a constant integrated 2-form coefficient, the local scalar mass is \(1/\operatorname{Area}(F)\). This formula is conditional on that explicit choice; it is not assigned to every combinatorial cycle. Nonplanar faces require a separately specified spanning surface or a triangulation with embedded triangles. Such a choice changes the geometric model and must be recorded rather than inferred.

## Reproduction

    python audits/audit_q6_orbit_face_geometry.py
    pytest -q tests/test_q6_orbit_face_geometry.py

The audit uses the existing Q6 complex builder and the exact D4 action used by the orbit-edge Hodge construction.

## Next theorem

Only after the geometric face model is fixed can we construct W2, verify positive definiteness, and form the weighted Hodge Laplacian. The chain identity B1 B2 = 0 remains combinatorial and is unaffected by the choice of positive face metric. A Bernoulli correction to W2 must then be derived from the actual face moments and a declared quadrature, not assigned by analogy with the one-dimensional edge cumulants.
