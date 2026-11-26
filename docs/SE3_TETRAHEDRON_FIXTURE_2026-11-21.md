# SE(3) tetrahedral fixture — 2026-11-21

## Purpose

This is the first executable fixture following the Bundle-Valued DEC specification. It uses the boundary of one oriented tetrahedron (4 vertices, 6 edges, 4 triangular faces) and deterministic edge transports in SE(3).

It is deliberately a **local algebraic validation**, not a theorem about discrete dislocation cohomology.

## Executable checks

Run:

```bash
python scripts/audit_se3_tetrahedron_fixture.py
```

Dependency: NumPy.

The script checks:

1. **SE(3) inverse/composition:** each stored edge transport composed with its inverse gives the identity.
2. **Vertex-gauge covariance:** for (G_{ij}\mapsto h_jG_{ij}h_i^{-1}), the based face holonomy transforms by conjugation at its base vertex.
3. **Flat pure-gauge connection:** (G_{ij}=h_jh_i^{-1}) gives identity holonomy on every triangular face.
4. **Controlled translational defect:** a fixed translation is inserted on one oriented edge; the script records the resulting translational components of all incident face holonomies.
5. **Gauge-invariant defect magnitude:** the Euclidean norm of the translational component is unchanged under the vertex-gauge transformation used here.

The generated JSON is deterministic for the fixed seeds and records residuals and status labels.

## Conventions and limitations

An element ((R,t)\in SE(3)) acts as (x\mapsto Rx+t). Composition is “A after B”:
[
(R_A,t_A)(R_B,t_B)=(R_AR_B,R_At_B+t_A).
]
The oriented face loop is (i\to j\to k\to i).

The translational component of affine face holonomy is reported as a **closure defect** only. It is not called a Burgers vector: that interpretation requires an explicit material frame/coframe and a kinematic convention. Nor is it identified automatically with Cartan torsion or deWit/Nye dislocation density.

## Explicitly not established

- No 3-cell Bianchi identity is tested or proved.
- No discrete torsion Bianchi identity is derived.
- No continuum Cartan torsion identification is asserted.
- No cohomology class or global 2-cycle flux is computed.
- No mesh-refinement or convergence result is claimed.

A single tetrahedron is sufficient for the group/gauge/face-holonomy fixture, but a genuine 3-cell Bianchi test needs a separately specified, ordered and transported boundary-face product. That derivation must precede any numerical claim.

## Status

| Item | Status |
|---|---|
| SE(3) group operations | Numerical verification |
| Face-holonomy gauge covariance | Numerical verification |
| Pure-gauge flatness | Numerical verification |
| Controlled translational face closure | Numerical verification |
| 3-cell Bianchi identity | Open / not tested |
| Cartan torsion identification | Open |
| Burgers-vector interpretation | Not assigned |
