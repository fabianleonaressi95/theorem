# In2Infinity — initial technical contact brief

**Prepared:** 2026-11-26  
**Intended recipients:** Colin Power and Dr Heike Bielek  
**Purpose:** request a technical exchange on the Extended Jitterbug and its atomic-radius assignments. This is a draft brief, not a message sent.

## 1. New material available for discussion

We have independently reconstructed unit-edge coordinate models for the five endpoint solids named by In2Infinity:

| Solid | V/E/F | Face types | Face-plane distances | MID | OUT |
|---|---:|---|---|---:|---:|
| Octahedron | 6/12/8 | 8 triangles | 0.408248 | 0.500000 | 0.707107 |
| Icosahedron | 12/30/20 | 20 triangles | 0.755761 | 0.809017 | 0.951057 |
| Cuboctahedron | 12/24/14 | 8 triangles, 6 squares | 0.707107; 0.816497 | 0.866025 | 1.000000 |
| Snub cube | 24/60/38 | 32 triangles, 6 squares | 1.142614; 1.213356 | 1.247223 | 1.343713 |
| Rhombic cuboctahedron | 24/48/26 | 8 triangles, 18 squares | 1.207107; 1.274274 | 1.306563 | 1.398966 |

All radii are normalized to unit edge length. The snub cube is represented using the real Tribonacci root \(t^3-t^2-t-1=0\). The rhombic cuboctahedron is represented by the 24-vertex signed-permutation orbit of \((1,1,1+\sqrt2)\). The combinatorics satisfy Euler's identity in all five cases. The script and tests are in the T154 PR.

A point requiring clarification emerged: for the cuboctahedron, snub cube and rhombic cuboctahedron, the two face families lie at different distances from the centre. Thus the literal definition “IN sphere touches the centre of each face” does not select one common radius. The In2Infinity P-orbital article itself notes two types of cuboctahedral in-sphere. We would like to know which face orbit (or alternative construction) is used for each IN radius in the 81-element mapping.

## 2. Questions for the authors

1. Can you share the exact coordinate construction, vertex correspondence and parameter for each transition in the Extended Jitterbug? In particular, how are the Octahedron–Icosahedron–Cuboctahedron segment and the Snub Cube / Rhombic Cuboctahedron extensions joined continuously?
2. Is the snub-cube chirality fixed by a particular handed vertex ordering?
3. What exact convention defines IN for the solids with multiple face orbits? Are separate IN values used, or is one family selected?
4. Could you share the complete 81-element radius table, including the radius definition, source dataset, uncertainties and any fitted versus predicted values?
5. Does the term “Rhombic Cuboctahedron” refer throughout to the 24-vertex Archimedean solid with 8 triangular and 18 square faces? We want to preserve your nomenclature while ensuring we reconstruct the intended object.
6. Is there a technical manuscript or construction sequence that specifies the claimed 4D/octaplex and higher-dimensional correspondences beyond the web diagrams?

## 3. Relevant independent work from our side

Our RGS–PSU programme contains an exact representation-theoretic and character-audited scalar spectrum for the Poincaré spherical space \(S^3/2I\), with \(2I\subset SU(2)\) the binary icosahedral group. The first positive scalar Laplace eigenvalue on the unit quotient is \(168\), with multiplicity \(13\); the Molien coefficient formula and exact character average agree through degree 120. This is a precise icosahedral spectral result, not a derivation of atomic radii.

Separately, we are in a technical exchange with Stergios Pellis concerning his proposed Golden Spheres Resonance / Pellis Function framework (public preprint DOI 10.13140/RG.2.2.35410.00968). Our comparison programme examines \(S^3/2I\), invariant spectra and geometrically defined self-adjoint operators before testing any proposed connection with golden-sphere hierarchies. We do not assume that Pellis's construction and In2Infinity's Extended Jitterbug are equivalent. A possible common discussion would be limited to explicit icosahedral symmetry, golden-ratio geometry, sphere hierarchies and spectral operators, with each mapping required to be proved.

## 4. Suggested first exchange

The most useful first step would be a short technical exchange focused on the endpoint coordinate conventions, IN/MID/OUT definitions and the 81-element data table. If those are clarified, we can return a reproducible comparison of the authors' radius assignments against the independently reconstructed geometry. The broader RGS–PSU / \(2I\) / Pellis comparison can remain a separate optional second stage.

## 5. Repository record

- T154 theorem and source audit: theorems/T154-in2infinity-extended-jitterbug-audit.md
- Source inventory and validation protocol: audits/in2infinity/T154-source-review-2026-11-26.md
- Coordinate implementation: scripts/audit_t154_in2infinity_geometry.py
- Tests: tests/test_t154_in2infinity_geometry.py
- Open pull request: https://github.com/fabianleonaressi95/theorem/pull/472

**Status:** this brief is prepared for author review; it has not been submitted through the website form.
