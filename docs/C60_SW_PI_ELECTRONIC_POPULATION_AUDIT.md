# C60 pyracylene Stone–Wales: pi tight-binding population and Q6 parity audit

**Classification:** numerical one-orbital Hückel benchmark plus exact finite-graph obstruction. This is not a DFT calculation and does not compute a continuous real-space electron density.

## 1. Why this is the next defensible electronic test

The previous MMFF94s calculation measured the covariance of carbon nuclear coordinates. It did not measure electronic density. Before attempting a costly electronic-structure calculation, this audit isolates the graph-connectivity contribution using a transparent one-orbital pi model on the exact C60 carbon graph.

The same ideal truncated-icosahedron coordinates are used before and after the switch. Thus any difference in the computed site-population tensor comes from the changed adjacency, not from an atomistic relaxation.

## 2. Model definition

Let A be the 60-by-60 adjacency matrix of the carbon graph. The dimensionless nearest-neighbour Hückel Hamiltonian is

\[
H=-tA,\qquad t=1.
\]

There is one pi electron per carbon, hence 60 pi electrons and 30 doubly occupied spatial orbitals. If H=U diag(epsilon_k) U^T, the spin-summed density matrix is

\[
P=2U\operatorname{diag}(f_k)U^T,
\]

where f_k in [0,1] fills the 30 lowest orbitals, with equal occupation within any degenerate shell if a shell is only partially filled. The site populations are n_i=P_ii, with sum_i n_i=60.

For the ideal carbon positions r_i, define the population-weighted covariance

\[
\bar r=\frac1{60}\sum_i n_i r_i,\qquad
Q_\pi=\frac1{60}\sum_i n_i(r_i-\bar r)(r_i-\bar r)^T.
\]

The scalar anisotropy is

\[
\mathcal A_\pi=
\frac{\lambda_{\max}(Q_\pi)-\lambda_{\min}(Q_\pi)}
{\lambda_{\max}(Q_\pi)+\lambda_{\min}(Q_\pi)}.
\]

This is a **site-population covariance** in an orthogonal pi-only model. It is not the covariance of a continuous rho(r).

## 3. Numerical result

The calculation was performed on the ideal truncated icosahedron with unchanged coordinates and uniform hopping.

| Observable | Pristine C60 | Pyracylene SW_5|6 |
|---|---:|---:|
| Pi-electron count tr(P) | 60 | 60 |
| HOMO eigenvalue / t | -0.6180339887 | -0.4773387376 |
| LUMO eigenvalue / t | 0.1385642651 | -0.1589042567 |
| HOMO–LUMO gap / t | 0.7565982539 | 0.3184344809 |
| Site population minimum | 1.0000000000 | 0.9508443551 |
| Site population maximum | 1.0000000000 | 1.0196297095 |
| Site population standard deviation | <4e-16 | 0.0134917469 |
| A_pi | 2.44e-16 | 0.0016099344 |

The Hückel HOMO–LUMO gap narrows by approximately **57.91%** in units of the chosen hopping parameter. The post-switch site populations are no longer uniform, and the population covariance becomes weakly anisotropic.

All **30 labelled** pyracylene moves were evaluated. Their HOMO–LUMO gap spread is below 1e-10 t, and their population-anisotropy spread is below 1e-10. This is consistent with the previously verified single I_h-orbit / single unlabelled postgraph class.

The post-switch carbon graph has automorphism group order 4, with all three nonidentity elements of order 2: it is combinatorially V4. This group-order match with the previously studied Q6 V4 is only an abstract group coincidence at this stage.

## 4. Exact Q6 obstruction: no direct carbon-graph homomorphism

The Q6 1-skeleton is the 6-dimensional hypercube graph, hence bipartite. The C60 carbon graph contains pentagonal 5-cycles and is not bipartite.

A graph homomorphism sends a source cycle to a closed walk of the same length. A bipartite graph has no closed odd walk. Therefore there is **no graph homomorphism**

\[
C60^{(1)}\longrightarrow Q6^{(1)}
\]

that sends every C–C bond to a single Q6 edge.

This does **not** rule out:
- a cellular chain map that sends a C60 edge to a multi-edge Q6 path;
- a map after subdivision or common refinement;
- a face-fibre representation map;
- a chain-level map whose edge images are integer 1-chains rather than single Q6 edges.

It does rule out the simplest vertex-to-state identification that is expected to preserve each carbon bond as one hypercube edge.

## 5. Relation to the existing Q6–C60 representation audits

The repository already records two distinct results for the **pristine** C60 face-tangent bundle:

1. The tested A4 representations have a character mismatch, so no invertible A4 intertwiner exists for that pair.
2. After restriction to a separately specified V4, an abstract 64-dimensional representation intertwiner exists, but it is not a canonical geometric face-to-state map.

Neither result is a Stone–Wales intertwiner. The post-switch graph's V4 automorphism group has not yet been identified with the archived Q6 V4 action on a geometrically realized post-switch face-tangent bundle. No commuting square P' S = A P is claimed.

## 6. What remains necessary for a physical density tensor

A real-space electronic density tensor requires an electronic-structure calculation with:
- identical charge and spin sectors before and after;
- a documented basis and convergence protocol;
- a relaxed geometry for each graph, with convergence diagnostics;
- the same spatial origin, projection plane and integration region;
- density grids or wavefunctions sufficient to evaluate rho(r) and its moments.

The present Hückel model omits sigma electrons, overlap, distance-dependent hopping, electron-electron interactions and self-consistency. It is therefore a controlled graph-spectral diagnostic, not a substitute for DFT.

## 7. Reproduction

~~~bash
python scripts/audit_c60_sw_pi_density.py --out c60_stone_wales_audit/pi_density_q6_parity.json
pytest -q tests/test_c60_sw_pi_density.py
~~~

The JSON report records the full model definition, the 30-move spread, the post-switch automorphism group, and the exact Q6 bipartite obstruction.
