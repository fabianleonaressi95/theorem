# Jitterbug kinematics — verified constraint-based audit

**Code:** `audits/jitterbug_gray_kinematics.py` (`python3 audits/jitterbug_gray_kinematics.py` prints the JSON report).
**Reference model:** R. W. Gray, *The Jitterbug Motion* (2002), `rwgrayprojects.com/rbfnotes/polyhed/jitterbug/paper01/jbCurve.pdf`.
**Status:** every quantitative claim below was verified **independently of Gray's formulas** by solving the rigid-bar constraint system numerically, then comparing with Gray's predictions.

## 1. What is being verified

The Jitterbug is the one-parameter flex of the cuboctahedron (Vector Equilibrium) into the octahedron through the icosahedron, driven by 8 rigid equilateral triangular faces. We model it as a bar-and-joint framework:

- 12 spherical joints = cuboctahedron vertices, permutations of `(±1,±1,0)/√2` (edge `L=1`, circumradius `R=1`);
- 24 rigid struts = cuboctahedron edges (each borders exactly one rigid triangle and one flexible square);
- 8 rigid triangular panels indexed by sign triples `ε ∈ {±1}³`, splitting into two chiral tetrahedral groups `T₊`/`T₋`.

The tetrahedral rotation group `T` (order 12) acts transitively on the 12 vertices, so a `T`-symmetric configuration is determined by a single orbit representative `w ∈ R³`. The 24 edge constraints reduce to **two independent quadratic forms**:

```
wᵀ Q₁ w = 1,   wᵀ Q₂ w = 1        (edge orbits of size 12 each)
```

whose intersection is a 1-dimensional algebraic curve — the Jitterbug path. It is traced by pseudo-arclength continuation from the cuboctahedron to the octahedral collapse.

## 2. Verified results

| Check | Result |
|---|---|
| Edge-length rigidity | max residual `2.2e-16` over the whole path |
| Vertex trajectories | all 12 planar to `1e-17`; each an **exact ellipse** with semi-axes `1` and `1/√3` (axis ratio `√3` to `1.9e-14`) — Gray's `3Y² + Z² = L²` |
| Face rotation `γ` | `T₊` and `T₋` rotate oppositely, `γ ∈ [0°, 60°)` |
| Face-centroid law | `V(γ) = √(2/3)·L·cos γ` holds to `3.9e-16` |
| Icosahedron position | 30 unit-distance pairs, `ρ = 0.9510565162951535 = √(10+2√5)/4`; measured `γ_I = 22.238756092964977°` vs predicted `arccos(τ²/2√2) = 22.238756092964977°` — **exact** |
| Octahedron endpoint | vertex pairs collapse, `ρ → 1/√2` |

The `θ ↔ γ` conversion `tan γ = √3 tan θ` and the ellipse parametrization
`Z(θ)=L cos θ/√(3−2cos²θ)`, `Y(θ)=L sin θ/√(3−2cos²θ)` are consistent with the
verified geometry but were not re-derived here; the per-vertex ellipse frames
(6 ellipses in 3 coordinate planes, two per plane) are recovered numerically by
`vertex_ellipses()`.

## 3. Corrections to earlier drafts

- The closed-form trajectory `X₁(θ)` with vertices confined to coordinate planes and `h(θ)=√(2/3)cos θ` imposed by hand is **wrong**: vertices leave those planes; the axial scaling is a *consequence* of the joint constraints, not an assumption.
- A single quaternion `q(θ)` cannot rotate all 8 faces about 8 different axes; the correct object is per-face rigid poses `X = t_ε + R(q_ε) X⁰` subject to joint-closure equations.
- The cuboctahedron's 8 triangular faces do **not** share edges with each other (each triangle edge borders a square face); a triangles-only joint model is incomplete without specifying the struts through the square faces.

## 4. Limits and open items

- This verifies the **standard** Jitterbug (VE → icosahedron → octahedron). Gray's sub-octahedral extensions (scaled faces `SF(γ)=√(3/(1+8cos²γ))`, or interpenetrating triangles to `γ=120°`) are separate models and are **not** covered by the rigid-strut constraint set used here.
- The path is the unique `T`-symmetric flex found; other symmetry branches (e.g. `O_h`-symmetric or chiral `T_d`) were not enumerated.
- Connection to the 64-Tetrahedron Grid of Galeffi (2412.0104v1): the Jitterbug is a kinematic model for a *component*; the 64-TG provides no coordinates, joints, or rigidity data, so no map `E^a_μ(θ)` from this motion to a vierbein field is justified yet.
