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
- Three sphere levels attached to each form: **IN, MID, OUT**.
- A proposed mapping of these sphere radii to atomic radii for 81 stable elements.
- A second operation, **truncation**, and a nested Cube/Octahedron blueprint, with stated mid-sphere scales of 50 pm and 100 pm.
- **Geo-Molecular Chemistry:** an extension of molecular/lattice geometry to four dimensions, with proposed explanations for conductivity, resistance, thermal properties, nitrogen fixation and biogeochemical cycles.
- **Atomic Geometry / D-orbital Geometry:** polyhedral interpretations of orbital shapes and proposed links between the Extended Jitterbug, transition-metal radii and electronic configurations.

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

The source's five-solid sequence is a proposed continuous transformation chain. The pages inspected do not provide, in the accessible text, a common vertex labelling, explicit coordinate paths, a parameter interval, or a proof that all five stages belong to one continuous family with specified rigidity constraints. Therefore this record does **not** claim such a family has been reconstructed.

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

**Access note:** web indexing exposed substantial page text, while direct page retrieval returned HTTP 403 during this audit. The source register is therefore not a claim of exhaustive archival capture. Original figures, animations, tables and downloadable material must still be preserved and transcribed.
