# T158 — Standard snub-cube twist angle versus the In2Infinity 22.5° claim

**Status:** exact numerical comparison of two stated angle conventions; whether the source uses the same reference frame remains unresolved.

## 1. Standard snub-cube construction

The standard snub-cube construction from a rhombicuboctahedral/cubic framework rotates the six square panels associated with the three coordinate axes, with opposite panels sharing an axis direction. The twelve remaining square regions are the ones that resolve into pairs of equilateral triangles. This matches the standard topological description of 6 squares plus 32 triangles, but it does not identify every informal "face rotation" angle with one another.

For the standard uniform snub cube, the twist angle is
\[
\theta_{\rm snub}
=\arctan\!\left(\frac{t-1}{t+1}\right),
\qquad t^3-t^2-t-1=0,\quad t>1.
\]
Using the unique real Tribonacci root gives
\[
\theta_{\rm snub}=0.2874131487577776\ldots\;\mathrm{rad}
=16.46756040038636\ldots^\circ.
\]
This value is independently reported in the NASA polyhedron data and in the published construction algorithm of Sandoval-Salazar et al.; the latter explicitly says its twist parameter was determined numerically and uses 16.47 degrees.

## 2. Comparison with 22.5 degrees

The In2Infinity page reports a 22.5-degree rotation of square faces in its rhombicuboctahedron-to-snub-cube transition. If this is intended to be the same local face-twist angle as the standard snubification parameter above, then the two values do not agree:
\[
22.5^\circ-\theta_{\rm snub}
=6.03243959961364\ldots^\circ.
\]
Therefore 22.5 degrees is **not** the standard uniform snub-cube twist angle under that convention.

This is not yet a contradiction in the source's full geometric model: 22.5 degrees might refer to a different reference frame, a half-step of the octagonal midsection's 45-degree rotational symmetry, or a different staged transformation. The source must specify the rotation axis, the moving panel set, the fixed reference frame, and whether the angle is local or relative between two configurations.

## 3. What is established and what remains open

- **Established:** the standard uniform snub-cube twist angle from the Tribonacci constant is approximately 16.4675604 degrees.
- **Established:** this differs from 22.5 degrees by approximately 6.0324396 degrees.
- **Open:** whether In2Infinity's 22.5 degrees denotes the same parameter, a different frame angle, a symmetry half-step, or a non-uniform/intermediate configuration.
- **Not claimed:** that the source's proposed moving-panel construction is impossible. A coordinate path and its angle convention are still needed.

## 4. Required clarification for the kinematic reconstruction

The next model should distinguish:
1. the six square panels rotated in the standard snubification construction;
2. the twelve lateral square regions that become 24 triangles;
3. the six square faces retained at the snub-cube endpoint;
4. the local twist angle of each moving panel versus any global/octagonal-frame rotation.

Only after these are labelled can the 22.5-degree statement be tested without mixing angle conventions.

## 5. Sources

- Wolfram MathWorld, “Snub Cube”: https://mathworld.wolfram.com/SnubCube.html
- NASA technical polyhedron data, report 19960054372 (reports 16.4675604°): https://ntrs.nasa.gov/api/citations/19960054372/downloads/19960054372.pdf
- Sandoval-Salazar et al., “Modeling 13 Archimedean solids by an object-oriented language,” *Mundo Nano* 15(29), 2022, DOI: 10.22201/ceijch.24485691e.2022.29.69694: https://doi.org/10.22201/ceijch.24485691e.2022.29.69694
- In2Infinity, “Brillouin Zones and the Geometry of Ferromagnetic and Electrically Conductive Waves”: https://in2infinity.com/brillouin-zones-and-the-geometry-of-ferromagnetic-and-electrically-conductive-waves/
- In2Infinity, “D-orbital Geometry — Part 1”: https://in2infinity.com/d-orbital-geometry-part-1/

Reproducibility: `tests/test_t158_snub_twist_angle.py`.
