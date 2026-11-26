# RGS coframe → spin connection → SU(2) → Q6 bridge: audit specification

**Status:** OPEN / specification only. No continuum-to-graph derivation is claimed.

## 1. Continuum input

Let a non-degenerate coframe \(e^a{}_{\mu}\) on a four-dimensional Lorentzian manifold be given, with inverse \(e_a{}^{\mu}\) and metric
\[
g_{\mu\nu}=\eta_{ab}e^a{}_{\mu}e^b{}_{\nu}.
\]
For the torsion-free Levi-Civita connection, determine \(\omega^{a}{}_{b\mu}\) from Cartan's equation
\[
de^a+\omega^a{}_b\wedge e^b=0,\qquad \omega_{ab}=-\omega_{ba}.
\]
The spinor connection is
\[
\Omega_\mu=\frac14\omega_{ab\mu}\gamma^{ab},\qquad
\gamma^{ab}=\frac12[\gamma^a,\gamma^b].
\]
These definitions require an actual coframe and convention choices (signature, gamma matrices, index placement).

## 2. SU(2) reduction is additional structure

A Lorentzian spin connection has structure group \(Spin(3,1)\), not SU(2). A reduction to SU(2) requires a chosen unit timelike field (or equivalent 3+1 splitting) and spatial frame. The stabilizer of that timelike field is \(Spin(3)\cong SU(2)\).

For a chosen spatial triad, the induced real SU(2) connection may be represented in the usual 3+1 variables by
\[
A^i=\Gamma^i+\beta K^i,
\]
where \(\Gamma^i\) is the triad-compatible spatial spin connection, \(K^i\) is extrinsic-curvature data, and \(\beta\) is a specified convention/parameter. This formula is not available from a coframe alone without the splitting and its associated data. Alternative projections must be stated explicitly.

## 3. Continuum transport

For a path \(\gamma_e\) assigned to an oriented graph edge \(e\), define
\[
U_e=\mathcal P\exp\left(-\int_{\gamma_e}A\right)\in SU(2),
\]
with sign and representation conventions fixed. Under vertex gauge transformations \(g_v\),
\[
U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}
\]
(or the equivalent convention after reversing the transport orientation). A closed-loop Wilson product transforms by conjugation and its trace is gauge invariant.

## 4. Graph/Q6 step

Q6 supplies a finite graph with 64 vertices and 192 oriented-edge pairs (degree 6). Its combinatorial data alone do **not** determine:
- a manifold or embedding;
- edge paths \(\gamma_e\);
- a coframe or spin connection;
- a SU(2) reduction;
- link values \(U_e\).

A graph-to-continuum assignment (or a separately specified discrete connection) is therefore required. If links are assigned, test edge reversal \(U_{\bar e}=U_e^{-1}\), vertex gauge covariance, and loop conjugation invariance before testing any dynamical claim.

## 5. Required audit sequence

| Gate | Test | Status |
|---|---|---|
| C1 | Validate coframe rank and metric/signature | NOT TESTED |
| C2 | Compute torsion-free \(\omega\); verify Cartan residual and antisymmetry | NOT TESTED |
| C3 | Verify spin-connection convention and Clifford compatibility | NOT TESTED |
| C4 | Document timelike field / 3+1 split and SU(2) reduction | NOT PROVIDED |
| C5 | Compute \(\Gamma,K,A\) with stated parameter/conventions | NOT TESTED |
| C6 | Specify graph-edge paths or discrete-link source | NOT PROVIDED |
| C7 | Build links; test reversal, gauge covariance, loop invariance | NOT TESTED |
| C8 | Compare continuum holonomies against graph holonomies under a stated refinement/approximation | NOT PROVIDED |

## 6. What is established versus open

**Established independently:** finite quaternion/SU(2) identities and the Q6 combinatorial Kirchhoff identities are separate algebraic results.

**Open:** the map from the project's RGS coframe to a continuum spin connection, the justified SU(2) reduction, the map to Q6 links, and any convergence/refinement statement.

No physical gauge field, torsion, wormhole, polariton dynamics, or viscosity follows from this specification alone.


## 7. Inspection of the recovered A13 archive (2026-11-19)

The recovered `psu_fibre_connection_matrices.npz` contains:
- `X`: 64×3 point coordinates;
- `Q`: 192×188 tangent/constraint matrix;
- `normals`: 64×3;
- `edges`: 192×3 edge records;
- `R_SO3`: 192 edgewise 3×3 transports;
- `U_SU2`: 192 edgewise 2×2 transports;
- `K0`: 188×188 symmetric operator.

Reproducible checks on this archive give:
| Check | Result | Status |
|---|---:|---|
| Rank of centered 3D point cloud | 3 | PASS |
| Unit-normal max residual | 2.22×10⁻¹⁶ | PASS |
| SO(3) orthogonality max Frobenius residual | 1.18×10⁻¹⁵ | PASS |
| SO(3) determinant max absolute residual from +1 | 8×10⁻¹⁶ | PASS |
| SU(2) unitarity max Frobenius residual | 3.21×10⁻¹⁶ | PASS |
| SU(2) determinant max absolute residual from +1 | 2.29×10⁻¹⁶ | PASS |
| SU(2) adjoint action vs archived SO(3) max entry residual | 4.45×10⁻¹⁶ | PASS |
| K0 symmetry Frobenius residual | 0 | PASS |

**Critical limitation:** the recovered A13 archive does not contain a coordinate-dependent 4×4 coframe, an inverse coframe, a spacetime metric with declared signature, derivatives of a coframe, or a chart/coordinate domain. The other recovered 188-dimensional matrices likewise do not provide these missing geometric data. The named `RGS_PRISM_FINAL_vierbein_E.npy` and `RGS_PRISM_tetrad_4d.npy` inputs were not found in the inspected Library archive or in the A13 bundle.

Consequently:
- the archived `U_SU2` and `R_SO3` are internally compatible **discrete edge transports**;
- their SU(2)↔SO(3) relation is numerically verified;
- their origin as path-ordered exponentials of a continuum Levi-Civita-derived connection is **not established**;
- no Cartan torsion residual or continuum spin connection can be computed from these inputs.

The executable audit is `scripts/audit_rgs_coframe_spin_connection_inputs.py`. It accepts the recovered `psu_fibre_connection_matrices.npz` as input and emits a JSON report. The correct next input is the actual coordinate-dependent coframe (with conventions and derivatives), not another 188×188 operator.

## 8. Updated gate status

| Gate | Status after archive inspection |
|---|---|
| C1: coordinate-dependent coframe rank and metric/signature | NOT POSSIBLE — input absent |
| C2: torsion-free spin connection / Cartan residual | NOT COMPUTABLE — input absent |
| C3: Clifford compatibility | NOT TESTED |
| C4: timelike field / 3+1 split | NOT PROVIDED |
| C5: induced SU(2) continuum connection | NOT COMPUTABLE |
| C6: Q6 edge-path assignment | NOT PROVIDED |
| Discrete archived SU(2)/SO(3) consistency | PASS |
| Continuum-to-discrete holonomy identification | OPEN |
