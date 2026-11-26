# T154 — In2Infinity Extended Jitterbug: source reconstruction and geometric audit

**Status:** source-derived claims catalogued; elementary coordinate identities proved; Extended-Jitterbug interpolation and physical predictions remain **open / unverified**.

**Scope.** This record preserves the terminology and sequence used by In2Infinity while separating (i) exact polyhedral geometry, (ii) source assertions, and (iii) physical claims requiring independent data and derivations. It does not identify a geometric correspondence with a quantum-mechanical explanation.

## 1. Source model recorded

The In2Infinity pages reviewed describe:

- **Geo-Quantum Mechanics (GQM):** an “Extended Jitterbug” sequence of five forms, ordered
  \[
  O \longrightarrow I \longrightarrow C \longrightarrow S \longrightarrow RC,
  \]
  where \(O\) is the octahedron, \(I\) the icosahedron, \(C\) the cuboctahedron, \(S\) the snub cube and \(RC\) the rhombic cuboctahedron.
- Three concentric sphere levels attached to each form: **IN** (tangent to face centres), **MID** (tangent to edge centres) and **OUT** (through the vertices), as explicitly defined in the GQM FAQ.
- A proposed mapping of these sphere radii to atomic radii for 81 stable elements.
- A second operation, **truncation**, and a nested Cube/Octahedron blueprint, with stated mid-sphere scales of 50 pm and 100 pm.
- **Geo-Molecular Chemistry:** an extension of molecular/lattice geometry to four dimensions, with proposed explanations for conductivity, resistance, thermal properties, nitrogen fixation and biogeochemical cycles.
- **Atomic Geometry:** maps S/P/D/F orbital families to nested polyhedral forms; the indexed pages describe P-orbitals through an octahedral arrangement, D-orbital families through cube / rhombic-cuboctahedral geometry, and F-orbital structures through cuboctahedral and star-tetrahedral constructions.
- **Geo-Nuclear Physics:** proposes polyhedral arrangements for nucleon counts, isotope stability and a toroidal 4D connection between nuclear and electron-cloud structure.
- **D-orbital Geometry:** proposes links between the Extended Jitterbug, transition-metal radii and electronic configurations.

These are statements of the source's model, not results established by this repository.

## 2. Exact coordinate certificate: cuboctahedron

Use the vertex set
\[
V_C=\{(\pm1,\pm1,0),(\pm1,0,\pm1),(0,\pm1,\pm1)\}.
\]
Join two vertices when their Euclidean distance is \(\sqrt2\). Direct enumeration gives
\[
|V_C|=12,\quad |E_C|=24,\quad |F_C|=14,
\]
with 8 triangular and 6 square faces. Its edge length is \(\sqrt2\).

The origin-to-face pyramids give an exact volume decomposition:

- each of the 8 triangular faces, joined to the origin, forms a regular tetrahedron of edge \(\sqrt2\), volume \(1/3\);
- each of the 6 square faces, joined to the origin, forms a square pyramid of base side \(\sqrt2\), height \(1\), volume \(2/3\).

Thus
\[
\operatorname{Vol}(C)=8(1/3)+6(2/3)=20/3.
\]
Each square pyramid is exactly one half of a regular octahedron: reflect it across its square base to obtain the other half. Its square base diagonal divides it into two tetrahedra of equal volume \(1/3\). Consequently the cuboctahedron is partitioned into 8 regular tetrahedra and 12 further tetrahedra, with total volume \(20/3\). The latter 12 are not asserted to be regular.

This is a static decomposition, not by itself a Jitterbug motion.

## 2A. Five-solid coordinate audit (unit edge)

A standard-coordinate reconstruction was added for all five solids. The snub cube uses the real Tribonacci root \(t^3-t^2-t-1=0\) in its chiral signed-permutation orbit; the rhombic cuboctahedron uses the 24 vertices given by permutations and sign changes of \((1,1,1+\sqrt2)\). The hull audit enumerates supporting planes and edge midpoints, without an external geometry package.

| Solid | V | E | F | Face sizes | IN candidates (face-plane distances) | MID | OUT |
|---|---:|---:|---:|---|---|---:|---:|
| Octahedron | 6 | 12 | 8 | 8 triangles | 0.408248 | 0.500000 | 0.707107 |
| Icosahedron | 12 | 30 | 20 | 20 triangles | 0.755761 | 0.809017 | 0.951057 |
| Cuboctahedron | 12 | 24 | 14 | 8 triangles, 6 squares | 0.707107 (square), 0.816497 (triangle) | 0.866025 | 1.000000 |
| Snub cube | 24 | 60 | 38 | 32 triangles, 6 squares | 1.142614, 1.213356 | 1.247223 | 1.343713 |
| Rhombic cuboctahedron | 24 | 48 | 26 | 8 triangles, 18 squares | 1.207107, 1.274274 | 1.306563 | 1.398966 |

All radii are normalized to edge length 1. Euler's identity \(V-E+F=2\) holds in every row. The listed IN candidates are distances from the centre to distinct face-plane orbits, not a single common inradius where the face types have different distances. This matters: the cuboctahedron has two face orbits, as In2Infinity itself notes in its P-orbital discussion; the same issue occurs for the snub cube and rhombic cuboctahedron in this coordinate reconstruction. A unique IN sphere tangent to every face centre therefore cannot be assumed for these three solids. The source needs to specify which face family or construction defines the IN value used in each atomic-radius assignment.

The script `scripts/audit_t154_in2infinity_geometry.py` and tests `tests/test_t154_in2infinity_geometry.py` reproduce the combinatorics and numerical sphere radii. These are a coordinate-level numerical certificate; exact algebraic simplification of every snub-cube radius and reconstruction of the source's animation/vertex correspondence remain open.

## 3. Exact polar dual: rhombic dodecahedron

With the polar convention \(P^\circ=\{x:x\cdot v\leq1\ \forall v\in P\}\), the polar of the above cuboctahedron is
\[
C^\circ=\{x: |x_1|+|x_2|\leq1,\ |x_1|+|x_3|\leq1,\
|x_2|+|x_3|\leq1\}.
\]
Its 14 vertices are
\[
(\pm1,0,0),(0,\pm1,0),(0,0,\pm1),
\quad (\pm\tfrac12,\pm\tfrac12,\pm\tfrac12).
\]
It is the rhombic dodecahedron, with 12 rhombic faces. This establishes the polar-duality statement with an explicit normalization; it does not identify the source's “rhombic cuboctahedron” with the rhombic dodecahedron. Those are distinct named solids in the source.

## 4. What is not yet a theorem

The source distinguishes the classical Fuller Jitterbug (cuboctahedron collapsing through icosahedral configurations to the octahedron) from its Extended Jitterbug, whose five-form order is octahedron → icosahedron → cuboctahedron → snub cube → rhombic cuboctahedron. The indexed pages describe the five forms as continuously related and the latter three as progressive opening of triangular faces. However, they do not expose a common vertex labelling, explicit coordinate paths, a parameter interval, or a proof of the rigidity constraints in the accessible text. The coordinate audit above reconstructs the five static endpoint solids only; it does **not** prove the continuous five-stage motion.

Likewise, the source's IN/MID/OUT sphere definitions and the 81-element radius table need to be transcribed with their exact radius convention, element-by-element values, uncertainty, source provenance and fitting/prediction split before any accuracy claim can be checked. The stated superiority over Bohr or van der Waals radii is not accepted without a like-for-like benchmark.

The claims about four-dimensional lattice mechanisms, conductivity, magnetism, Aufbau anomalies, nitrogen fixation, haemoglobin, chlorophyll and biogeochemical cycles are recorded as research hypotheses. Each requires a defined state space, equations of motion or energy, observables, data and comparison against established models.

## 5. RGS–PSU interface: permitted and forbidden identifications

Permitted next steps:

1. Build explicit coordinate/incidence models for the five named solids, preserving source nomenclature.
2. Define candidate maps between successive vertex/edge/face sets and test lengths, angles, symmetry groups and rank.
3. Reconstruct IN/MID/OUT radii from source figures/tables and compare against a declared experimental radius dataset.
4. Only after these steps, test whether any map is equivariant with a specific RGS carrier representation.

Not permitted at this stage:

- identifying the Extended Jitterbug parameter with RGS torsion or with the inter-sheet complex structure \(J\);
- treating the static tetrahedron/half-octahedron decomposition as a continuous Jitterbug path;
- treating a geometric match to an atomic radius as a derivation of an orbital, electronic configuration or chemical property;
- treating the source's four-dimensional language as a constructed 4-polytope or a validated physical fourth spatial dimension.

The existing T145 conclusion remains unchanged: the audited \(J\) is a complex structure on the two-sheet carrier, not a torsion tensor.

## 6. Source register

1. In2Infinity, “Geo-Quantum Mechanics,” https://www.in2infinity.com/theory/geo-quantum-mechanics
2. In2Infinity, “Geo-Molecular Chemistry,” https://www.in2infinity.com/theory/geo-molecular-chemistry
3. In2Infinity, “D-orbital Geometry — Part 1,” https://www.in2infinity.com/d-orbital-geometry-part-1/
4. In2Infinity, “D-orbital Geometry — Part 2,” https://www.in2infinity.com/d-orbital-geometry-part-2/
5. In2Infinity, “4D Thinking,” https://www.in2infinity.com/theory/geometric-thinking/4d-thinking/
6. In2Infinity, “Atomic Geometry,” https://www.in2infinity.com/theory/atomic-geometry/
7. In2Infinity, “P-orbital Geometry,” https://www.in2infinity.com/p-orbital-geometry/
8. In2Infinity, “Geo-Nuclear Physics,” https://www.in2infinity.com/theory/geo-nuclear-physics/

**Access note:** web indexing exposed substantial page text, while direct page retrieval returned HTTP 403 during this audit. The source register is therefore not a claim of exhaustive archival capture. Original figures, animations, tables and downloadable material must still be preserved and transcribed.
