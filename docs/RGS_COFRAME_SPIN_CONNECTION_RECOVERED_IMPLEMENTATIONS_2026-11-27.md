# RGS coframe and spin-connection follow-up (2026-11-27)

**Purpose:** reconcile the 2026-11-19 coframe-input audit with the reconstruction and analytic-connection implementations now present in the companion repository `fabianleonaressi95/rgs-qlg-quaternion-bridge`.

**Scope rule:** three geometrical objects must remain distinct:
1. the 64 site-dependent spatial covariance frames;
2. their static block-diagonal 3+1 lift;
3. the analytic Ellis coordinate coframe on a smooth four-dimensional chart.

A result for (3) is not automatically a derivative, connection, or continuum limit for (1).

## 1. Recovered implementation map

The companion repository contains the following source-level implementation:

| Component | Source | What it supplies | Status |
|---|---|---|---|
| Deterministic 64-site seed and coframe reconstruction | `examples/reconstruct_rgs_vierbein_tetrads.py`, `src/rgs_ellis_refinement.py` | Reconstructs the 64x3 seed from the checked-in provenance routine; forms local Gaussian covariance matrices and their principal SPD square roots | IMPLEMENTED; regenerate and run its tests in the companion checkout |
| Static 3+1 lift | same reconstruction example | `e^A_mu=diag(1,E_i)`, with `eta=(-,+,+,+)` | IMPLEMENTED as a static lift; not a time-dependent field-equation solution |
| General local Levi-Civita kernel | `src/rgs_spin_connection.py` | Computes Christoffel and Lorentz spin connection from an invertible coframe and its first jet; reports antisymmetry, tetrad-postulate and torsion residuals | IMPLEMENTED |
| Analytic Ellis coframe jet | `src/rgs_ellis_spin_connection.py` | Supplies exact first derivatives for the smooth Ellis chart and calls the general kernel | IMPLEMENTED |
| Intrinsic Ellis edge transport | `src/ellis_spin_connection.py` | Parallel transport along the embedded Ellis hypersurface, with SO(3) frame transport and SU(2) lift | IMPLEMENTED as a discrete/geometric edge transport; do not identify it with a sampled continuum LC holonomy without a comparison theorem |

The companion documentation and tests are:
- `docs/VIERBEIN_RECONSTRUCTION_STATUS.md`
- `docs/LEVI_CIVITA_SPIN_CONNECTION_CORE.md`
- `docs/RGS_ELLIS_ANALYTIC_SPIN_CONNECTION.md`
- `tests/test_rgs_spin_connection.py`
- `tests/test_rgs_ellis_spin_connection.py`
- `tests/test_rgs_vierbein_reconstruction.py`

These paths are the source of truth for implementation details. The original historical binary payloads are not claimed to have been recovered byte-for-byte; the checked-in deterministic reconstruction is the reproducible route.

## 2. Analytic Ellis continuum chart

Use coordinates `(t,u,theta,phi)`, signature `(-,+,+,+)`, and
`R(u)=sqrt(u^2+r0^2)`. The reference metric and diagonal coframe are

[
ds^2=-dt^2+du^2+R(u)^2(d\theta^2+\sin^2\theta\,d\phi^2),
\qquad
e^a{}_{\mu}=\operatorname{diag}(1,1,R,R\sin\theta).
]

The nonzero first-jet entries, in the companion implementation's convention
`de[a, nu, mu] = partial_mu e[a, nu]`, are

[
\partial_u e^2{}_{\theta}=u/R,\qquad
\partial_u e^3{}_{\phi}=(u/R)\sin\theta,\qquad
\partial_\theta e^3{}_{\phi}=R\cos\theta.
]

The general kernel solves the tetrad postulate
[
\partial_\mu e^a{}_{\nu}
+\omega^a{}_{b\mu}e^b{}_{\nu}
-\Gamma^\rho{}_{\mu\nu}e^a{}_{\rho}=0
]
and audits Lorentz antisymmetry and vanishing torsion. The companion tests explicitly check metric reconstruction, the analytic jet, antisymmetry, tetrad-postulate residual and torsion-free residual.

An independent numerical spot-check of the analytic chart at
`r0=0.8292, u=0.37, theta=0.91` gave residuals of order
`1e-16` for all three checks (maximum approximately `3.64e-16`).
Additional sample points also remained below `4.1e-16`. These are numerical
checks of the analytic Ellis chart, not of derivatives of the 64 site frames.
The reproducible regression tests live in the companion repository; this
follow-up does not claim that its full test suite was rerun during this update.

## 3. Corrected gate register

| Gate | Evidence now located | Classification |
|---|---|---|
| Deterministic 64-site seed/coframe reconstruction | Checked-in reconstruction code, provenance routine and reconstruction tests | IMPLEMENTED; test execution status NOT RE-RUN HERE |
| Static 3+1 block lift | Explicit constructor and metric-reconstruction tests | IMPLEMENTED; static benchmark only |
| Analytic Ellis coframe and first jet | Exact source implementation and dedicated tests | IMPLEMENTED |
| Local torsion-free LC spin connection on the analytic Ellis chart | General coframe-jet kernel; analytic Ellis wrapper; residual checks in tests and numerical spot-check above | NUMERICALLY VERIFIED on the analytic chart |
| Clifford/spinor coupling | Spinor connection and Dirac covariant-derivative utilities plus regression tests | IMPLEMENTED; convention compatibility remains subject to the stated gamma/signature contract |
| Intrinsic Ellis edge transport and SU(2) lift | Companion edge-transport implementation | IMPLEMENTED; do not infer continuum LC origin solely from the lift |
| Derivatives/interpolation of the 64 site-dependent covariance coframes | No unique differentiable interpolation or first-jet construction identified | OPEN |
| LC spin connection derived from those 64 RGS coframes | Requires the preceding interpolation/derivative data and frame-gauge control | OPEN |
| Continuum LC holonomy = archived Q6/SU(2) edge transport | Requires specified paths, link construction and a refinement/convergence comparison | OPEN |
| SU(2) reduction of a Lorentzian LC connection | Requires a declared unit timelike field or 3+1 splitting and spatial triad | OPEN unless separately supplied |
| Teleparallel inertial spin connection and TEGR identity | Requires tetrad-gauge-compatible inertial connection, torsion scalar, boundary term and convention-fixed identity audit | OPEN |

## 4. Mathematical guardrails

- The 188-dimensional tangent/constraint space is not a four-dimensional spacetime coordinate chart.
- A Lorentzian Levi-Civita spin connection is a `Spin(3,1)` connection. An `SU(2)` connection requires an explicit reduction, for example by a unit timelike field and its spatial stabilizer.
- The Ellis diagonal coframe is a smooth continuum reference geometry. Its derivatives are not finite differences of the 64 covariance frames.
- The static block lift is a constructed static extension; it does not derive lapse, shift, time dependence, or dynamics from the RGS–PSU/QAT action.
- Intrinsic edge parallel transport on the Ellis embedding is meaningful as its own construction. It is not, without a proven identification, the path-ordered exponential of the continuum LC connection above.
- No torsion, Pin structure, TEGR identity, Einstein–Cartan solution, or physical wormhole dynamics follows merely from the existence of these coframes.

## 5. Reproduction commands

From a checkout of `rgs-qlg-quaternion-bridge`:

```bash
PYTHONPATH=. python examples/reconstruct_rgs_vierbein_tetrads.py
PYTHONPATH=. python -m pytest tests/test_rgs_vierbein_reconstruction.py tests/test_rgs_spin_connection.py tests/test_rgs_ellis_spin_connection.py -q
```

The generator writes reconstructed arrays and a JSON residual report under
`results/vierbein_reconstruction` by default. Keep generated binaries and
historical binary payloads distinct unless their hashes and provenance match.

## 6. Relationship to the earlier theorem-repository audit

This note supplements, rather than replaces,
`docs/RGS_COFRAME_SPIN_CONNECTION_SU2_Q6_BRIDGE_AUDIT.md` and the merged
PR #321. The earlier audit remains correct about the A13 fibre-connection
archive: its archived edge transports do not by themselves establish a
continuum Levi-Civita origin. The new source map adds independently
implemented reconstruction and analytic Ellis-chart branches; it does not
close the discrete RGS coframe-to-continuum connection gap.
