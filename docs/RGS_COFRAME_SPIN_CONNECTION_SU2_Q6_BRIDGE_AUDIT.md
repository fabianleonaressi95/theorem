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
