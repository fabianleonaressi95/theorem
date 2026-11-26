# In2Infinity source review — T154

Date: 2026-11-26

## Purpose

This file is a source-faithful index for the In2Infinity material used in T154. It keeps the site's claims visible while marking what is and is not independently established.

## Pages and extracted claims

| Source | Claims visible in indexed page text | Audit status |
|---|---|---|
| Geo-Quantum Mechanics | Classical Jitterbug described as Cuboctahedron → Icosahedron → Octahedron; Extended Jitterbug uses Octahedron → Icosahedron → Cuboctahedron → Snub Cube → Rhombic-Cuboctahedron; IN/MID/OUT spheres; 81 stable-element radii; truncation and nested Cube/Octahedron scales | Endpoint coordinates independently reconstructed; continuous paths and radius table reproduction open |
| D-orbital Geometry, Part 1 | Defines the Rhombic Cuboctahedron as an Archimedean solid with 24 vertices, 8 triangular and 18 square faces; describes it as an exploded Cube/Octahedron, with a central octagonal prism and nested cube of side √2 | Endpoint coordinates reconstructed (24,48,26); source's exact face/vertex correspondence and motion still open |
| D-orbital Geometry, Part 2 | Lists ratios including \(1:\sqrt2\), \(\Phi\), Tribonacci constant and silver-ratio expressions; describes progressive opening of octahedral triangular faces | Source claim catalogued; exact definitions/normalizations open |
| Atomic Geometry | Maps S/P/D/F orbital families to nested polyhedra; P-orbital lobes to octahedral directions; D families to cube and rhombic-cuboctahedral forms; F constructions to cuboctahedron / star-tetrahedron | Source claims catalogued; not an identification with quantum-mechanical orbital wavefunctions |
| P-orbital Geometry | Defines IN/MID/OUT spheres as face-tangent / edge-tangent / vertex-passing spheres; gives cuboctahedron MID/OUT ratios 0.866 and 1.154; maps nested polyhedral radii to P-block elements | Geometric ratios can be checked; atomic-radius comparison requires uniform radius convention and raw table |
| Geo-Nuclear Physics | Applies polyhedra to nucleon counts and isotope stability; proposes toroidal 4D nuclear/electron-cloud connection and quark-spin account | Speculative physical hypotheses; no nuclear Hamiltonian or quantitative validation supplied in this audit |
| Geo-Molecular Chemistry | Four-dimensional lattice interpretation; conductivity/resistance/thermal properties; tetrahedral cycle molecules; nitrogen fixation as a linear-to-tetrahedral transformation | Research hypotheses; no physical derivation validated here |
| 4D Thinking | Claims 4D morphing transfers information between shells and excludes intermediate stable states | Speculative physical interpretation; not adopted as theorem |

| 4D Thinking | Claims 4D morphing transfers information between shells and excludes intermediate stable states | Speculative physical interpretation; not adopted as theorem |

## Independent five-solid endpoint audit

The unit-edge coordinate audit in `scripts/audit_t154_in2infinity_geometry.py` returns:

| Solid | V/E/F | Face types | Face-plane distances | MID radius | OUT radius |
|---|---:|---|---|---:|---:|
| Octahedron | 6/12/8 | 8 triangles | 0.408248 | 0.500000 | 0.707107 |
| Icosahedron | 12/30/20 | 20 triangles | 0.755761 | 0.809017 | 0.951057 |
| Cuboctahedron | 12/24/14 | 8 triangles, 6 squares | 0.707107; 0.816497 | 0.866025 | 1.000000 |
| Snub cube | 24/60/38 | 32 triangles, 6 squares | 1.142614; 1.213356 | 1.247223 | 1.343713 |
| Rhombic cuboctahedron | 24/48/26 | 8 triangles, 18 squares | 1.207107; 1.274274 | 1.306563 | 1.398966 |

All lengths are in edge-length units. Euler's identity holds for all five. The three multi-face-orbit solids (cuboctahedron, snub cube, rhombic cuboctahedron) have two distinct face-plane distances. Consequently a single IN-sphere touching every face centre does not exist for these coordinate models. In2Infinity explicitly notes two in-sphere types for the cuboctahedron in its P-orbital page; the authors should clarify which face orbit defines each IN value in the radius map.

## Required source-data capture

- Download or manually archive all original diagrams, animations, captions and tables.
- Capture the complete element-by-element 81-row radius mapping, including radius type (covalent, metallic, empirical, van der Waals or other), units and source.
- Record all IN/MID/OUT sphere definitions, including whether each is inscribed, midscribed, circumscribed or defined by another construction.
- Record the coordinate normalization and edge length for each of the five solids.
- Recover the exact transformation parameter and vertex correspondence at each transition.
- Separate values used to calibrate the model from values claimed as predictions.

## Quantitative audit protocol

1. Reconstruct each solid independently from exact coordinates or algebraic coordinates.
   For every solid, implement the source's IN/MID/OUT definitions literally: face-tangent inradius, edge-tangent midradius and vertex circumradius. Do not silently substitute another convention.
2. Compute vertex/edge/face counts, face types, edge lengths, dihedral angles, symmetry group and all three sphere radii.
3. Verify each claimed transition using a single explicit parameterized coordinate family. If combinatorics change, state the singular/degenerate parameter values and the allowed identifications.
4. Compare predicted and measured radii using one predeclared experimental convention. Report MAE, RMSE, maximum absolute error, uncertainty-weighted residuals and baseline results on the same elements.
5. Use held-out elements or a genuinely independent dataset; do not score fitted radii as predictions.
6. For chemical/biological claims, specify the Hamiltonian or free-energy functional, state variables, boundary conditions, observables and falsifiable numerical predictions.

## Additional source-level issue to clarify

The site states that the Geo-Quantum table covers 81 stable elements, while the P-orbital discussion calls bismuth (Z=83) the final stable atom and names thallium (81), lead (82), and bismuth (83). The standard count of 81 elements with at least one stable isotope excludes technetium (43) and promethium (61); bismuth-209 is now known to be radioactive with an extremely long half-life. The radius table should state whether “stable” means stable element, naturally occurring element, or the authors' adopted historical convention, and should identify the isotopes/radius data used.

## Access and provenance

The indexed text was available through search results on 2026-11-26. Direct retrieval of the canonical pages returned HTTP 403. The summaries above therefore do not replace a full source archive, and no inaccessible figure/table has been reconstructed by guesswork.
