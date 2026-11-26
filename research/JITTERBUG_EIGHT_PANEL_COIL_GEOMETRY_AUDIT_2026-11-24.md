# Jitterbug eight-panel coil geometry: exact incidence audit and implementation boundary

**Date:** 2026-11-24  
**Status:** [P] exact finite combinatorics of the eight panel labels and their shared-vertex graph; [N] source-level audit of the existing one-panel implementation; [C] eight-coil frame/flux construction; [O] mutual-inductance matrix, coupled circuit solution, and full mechanical-electromagnetic energy closure.

## 1. Scope and reuse

This note advances issue [#409](https://github.com/fabianleonaressi95/theorem/issues/409) without duplicating the merged one-panel implementation. It audits:

- `audits/jitterbug_coil_coupling.py` (main-branch blob `0348b6d6e3eab590413175714c4816a6e5e674a1`);
- `audits/jitterbug_gray_kinematics.py` (main-branch blob `6d50c1ef0a94bda372a3aa1c3a17afd636a71468`).

The current coil script fits only face `(1,1,1)`, assumes a spatially uniform static magnetic field, and solves one scalar series-RL circuit. It is a valid one-panel baseline, not an eight-panel mutually coupled model. Its scalar RL solver must not be applied independently to eight coils when mutual inductances are nonzero.

## 2. Exact sign-triple panel incidence

Let the eight panels be indexed by
[
\varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{\pm1\}^3.
]
In the unit-edge cuboctahedral reference configuration, their ordered vertices are
[
p_{\varepsilon,0}=\frac1{\sqrt2}(\varepsilon_1,\varepsilon_2,0),\quad
p_{\varepsilon,1}=\frac1{\sqrt2}(\varepsilon_1,0,\varepsilon_3),\quad
p_{\varepsilon,2}=\frac1{\sqrt2}(0,\varepsilon_2,\varepsilon_3).
]
Each panel is an equilateral triangle. For two distinct labels \(\varepsilon,\delta\):

- if their Hamming distance is one, they share exactly one vertex;
- if their Hamming distance is two or three, they share no vertex.

For example, if only the first sign changes, the common vertex is
\(2^{-1/2}(0,\varepsilon_2,\varepsilon_3)\); the other two cases follow cyclically. Thus the panel shared-vertex graph is exactly
[
G_{\rm panel}\cong Q_3,
\qquad |V|=8,\quad |E|=12,\quad \deg(v)=3.
]
This is an exact incidence statement. **It is not a claim that two triangular panels share a full hinge edge**: in this sign-triple realization adjacent panels share one vertex. Rod/hinge constraints must be represented by the actual Jitterbug linkage incidence, not inferred from a panel graph edge alone.

## 3. Eight rigid panel frames

For each \(\varepsilon\), let \(P_\varepsilon^0\in\mathbb R^{3\times3}\) contain the three ordered reference vertices as rows, and let \(P_\varepsilon(t)\) contain the corresponding vertices in a Jitterbug configuration. Define the reference centroid
\[
c_\varepsilon^0=\frac13\sum_{k=0}^2p_{\varepsilon,k},
\]
and the ordered local frame
\[
e_{1,\varepsilon}^0=
\frac{p_{\varepsilon,1}-p_{\varepsilon,0}}
{\|p_{\varepsilon,1}-p_{\varepsilon,0}\|},\quad
n_\varepsilon^0=
\frac{(p_{\varepsilon,1}-p_{\varepsilon,0})\times
(p_{\varepsilon,2}-p_{\varepsilon,0})}
{\|(p_{\varepsilon,1}-p_{\varepsilon,0})\times
(p_{\varepsilon,2}-p_{\varepsilon,0})\|},\quad
e_{2,\varepsilon}^0=n_\varepsilon^0\times e_{1,\varepsilon}^0.
\]
The ordered triple \((e_1,e_2,n)\) fixes the winding orientation; changing the vertex order reverses \(n\) and must be accompanied by a winding-sign change if the physical coil is unchanged.

For each time sample, fit a proper rotation \(R_\varepsilon(t)\in SO(3)\) and translation \(c_\varepsilon(t)\) by the same Kabsch procedure as the one-panel script, using all three ordered panel vertices. The fit must enforce
\(\det R_\varepsilon(t)=+1\). Then
\[
n_\varepsilon(t)=R_\varepsilon(t)n_\varepsilon^0,
\qquad
e_{a,\varepsilon}(t)=R_\varepsilon(t)e_{a,\varepsilon}^0.
\]
The eight fits are independent frame reconstructions of the same linkage configuration; their residuals and relative orientation continuity are acceptance data, not assumed to vanish.

A circular coil may be placed at the panel centroid with local radius \(r_\varepsilon\), turn count \(N_\varepsilon\), and winding sign \(s_\varepsilon\in\{\pm1\}\). The geometric clearance condition inherited from the triangular inradius is
\[
0<r_\varepsilon<\frac{a_J}{2\sqrt3},
\]
where \(a_J\) is the instantaneous/reference panel edge length according to the declared length convention. This condition alone does not check clearance from other panels, rods, or neighbouring coils.

## 4. Flux and circuit equations to implement

For a prescribed uniform static field \(B\), the external flux linkage of coil \(i\) is
\[
\lambda_i^{\rm ext}(t)=s_iN_i\pi r_i^2\,B\cdot n_i(t),
\qquad
\mathcal E_i^{\rm ext}(t)=-\frac{d}{dt}\lambda_i^{\rm ext}(t).
\]
This is the same restricted field model used by the existing one-panel baseline. A spatially varying or time-dependent field requires a surface integral and must not be silently approximated by this expression.

For eight circuits, define the full inductance matrix
\[
L(q)=\begin{pmatrix}
L_{11}(q)&\cdots&L_{18}(q)\\
\vdots&\ddots&\vdots\\
L_{81}(q)&\cdots&L_{88}(q)
\end{pmatrix},
\qquad L_{ij}=L_{ji}.
\]
The diagonal terms require a declared finite-wire/cross-section model or calibrated self-inductance input; the singular filament self-integral is not admissible. Off-diagonal terms may be computed from the Neumann mutual-inductance integral with declared discretization, regularization and convergence study. Reciprocity and positive semidefiniteness of the complete matrix are mandatory numerical checks.

For a resistance matrix \(R\), current vector \(i\), and flux vector
\(\lambda=L(q)i+\lambda^{\rm ext}(q,t)\), the coupled circuit system is
\[
\frac{d}{dt}\big[L(q)i+\lambda^{\rm ext}(q,t)\big]+Ri=0,
\]
or
\[
L\dot i+\dot L\,i=\mathcal E^{\rm ext}-Ri.
\]
The sign convention must be tested against the one-coil baseline. Series/parallel wiring and winding polarity are separate circuit topologies; eight identical panel coils do not imply eight additive outputs.

## 5. Exact and unresolved claims

| Claim | Classification |
|---|---|
| Eight sign-triple triangular panels | [P] exact combinatorial indexing |
| Shared-vertex graph is \(Q_3\), with 12 contacts | [P] exact |
| Shared-vertex contact is a full hinge edge | [O] not implied; do not assume |
| Proper Kabsch frame for each panel at sampled poses | [N] numerical procedure; eight-panel replay required |
| Eight external flux linkages in a uniform static field | [C] direct extension of the existing frame model |
| Full mutual-inductance matrix and coupled RL response | [O] not implemented by the one-coil scalar solver |
| Energy closure including mechanical work from \(L(q)\) | [O] |
| Generator power, gain, self-sustaining operation | [O] no such claim follows |

## 6. Implementation sequence for issue #409

1. Preserve and replay the current one-panel report and regression tests.
2. Add a deterministic sign-triple panel registry and exact tests for eight panels, 12 shared-vertex contacts, and the \(Q_3\) adjacency relation.
3. Fit all eight ordered panel frames along the full existing Gray branch; record per-panel maximum residual, determinant, normal continuity and endpoint values.
4. Add eight external-flux channels and verify that selecting only \((1,1,1)\) reproduces the one-panel result.
5. Add a two-coil mutual-inductance benchmark before the eight-coil matrix; test reciprocity, positive semidefiniteness, winding reversal and zero-coupling limits.
6. Implement the coupled eight-current ODE with \(\dot L(q)\), then perform time-step/quadrature convergence and a complete electrical/magnetic/mechanical energy audit.
7. Compare open circuit, independent coils, series/parallel wiring and polarity patterns only after the mutual matrix is validated.

The present note supplies the exact panel-label/contact combinatorics and a non-ambiguous frame/circuit specification. It does not claim that the eight-coil numerical implementation or its energy audit has already been performed.
