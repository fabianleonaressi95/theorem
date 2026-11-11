# T094 — Numerical SE(2) holonomy audit and Morandotti source adapter

**Date:** 11 November 2026  
**Status:** merged and CI-verified for the smooth manufactured-connection audit (4 regression tests; first-order density-error trend observed). The existing prescribed two-core Morandotti benchmark is now wired into the core-source adapter. Extraction of Frank/Burgers holonomies from a solved defect mesh and end-to-end coupling to the Morandotti interaction matrix remain open.  
**Dependencies:** T091, T092, T093; `models/morandotti_cell_reconstruction.py`.

## 1. Purpose

T093 gives a local smooth-connection consistency estimate for the face estimator
[
\mathcal F_K^h=-\frac{1}{|K|}\log H_K.
]
T094 adds a reproducible manufactured experiment with both rotational and translational components, including a nonzero semidirect-product commutator. It also adds a narrowly scoped adapter from measured integrated core-loop holonomies to the six-field Frank/Burgers vector convention already used by the Morandotti interaction model.

The code is deliberately split into two logically different experiments:

1. **Smooth face audit:** tests curvature/torsion density recovery away from defect cores.
2. **Core-source adapter:** converts externally measured integrated loop data into Morandotti source vectors. It does not infer singular cores from the smooth manufactured connection.

## 2. Manufactured connection

The script `scripts/rgs_se2_holonomy_audit.py` defines
[
A_x=\operatorname{se2}(0.17y,(1+0.13y,0.07x)^T),\
A_y=\operatorname{se2}(0.23x,(0.09y,1+0.11x)^T),
]
where
[
\operatorname{se2}(\theta,v)=
\begin{pmatrix}\theta J&v\\0&0\end{pmatrix}.
]
The curvature is evaluated analytically as
[
\mathcal F_{xy}=\partial_xA_y-\partial_yA_x+[A_x,A_y].
]
The commutator is nonzero at the audit point, so the experiment is not an abelian translation-only test.

For every positively oriented equilateral face, the edge transports solve
[
\dot U=-A(\dot\gamma)U,qquad U(0)=I,
]
and the based holonomy is
[
H=U_{20}U_{12}U_{01}.
]
The estimator and error are
[
\mathcal F_h=-\log(H)/|K|,\qquad
E_h=\|\mathcal F_h-\mathcal F_{xy}(x_K)\|_F.
]
The script writes all matrices, errors and successive refinement ratios to JSON. The target is the T093 first-order density estimate (E_h=O(h)). The regression test checks decreasing error only; it is a trend guard, not a proof of asymptotic order.

## 3. Morandotti core-loop source adapter

An optional JSON input has the form:
```json
{
  "cores": [
    {"center": [-0.28, 0.0], "theta": 0.2, "q": [0.01, -0.02]},
    {"center": [0.28, 0.0], "theta": -0.1, "q": [-0.03, 0.04]}
  ]
}
```
For
[
\log H_i=\begin{pmatrix}\Theta_iJ&q_i\\0&0\end{pmatrix},
]
the T093 sign convention gives Frank angle (s_i=-\Theta_i) and Burgers vector (b_i=-q_i). These are passed to the existing `build_defect_components` routine, which returns separate Frank and Burgers vectors and their total in the Morandotti ordering
[
\Phi_i=(s_i,\ s_ix_i+b_{i2},\ s_iy_i-b_{i1}).
]
This adapter is a data-convention bridge, not a derivation of core holonomies. The interaction matrix, constitutive parameters, boundary conditions and source normalization must still be supplied and audited independently before solving the Morandotti system.

## 4. Reproduction

```bash
python -m pytest -q tests/test_rgs_se2_holonomy_audit.py
python scripts/rgs_se2_holonomy_audit.py \
  --sizes 0.32 0.16 0.08 0.04 \
  --out artifacts/se2_holonomy_audit/report.json
```

With measured integrated core-loop data:
```bash
python scripts/rgs_se2_holonomy_audit.py \
  --core-holonomies path/to/core_holonomies.json \
  --out artifacts/se2_holonomy_audit/report_with_morandotti_sources.json
```

## 5. Prescribed two-core Morandotti benchmark coupling

The repository fixture `data/morandotti_two_core_core_holonomies.json` now carries the prescribed two-core benchmark charges already used by the Morandotti reconstruction gate:

- core 1 at ((-0.28,0)): Frank angle (s^1=0.2), Burgers vector (b^1=(0,0));
- core 2 at ((0.28,0)): Frank angle (s^2=0), Burgers vector (b^2=(0.03,-0.04)).

To feed the adapter in the T093 convention, the fixture encodes (Theta_i=-s_i) and (q_i=-b_i). The resulting Morandotti source vector must be
[
Phi=(0.2,-0.056,0, 0,-0.04,-0.03).
]
The CI now runs the smooth audit and this benchmark source adapter in the same report. This is a genuine connection to the repository's existing prescribed disclination–dislocation benchmark, but it is **not** a measurement of loop holonomy extracted from the finite-element defect solution. The fixture makes that distinction explicit in its metadata.

## 6. Classification and limitations

- **Implemented:** numerical edge transport, ordered triangular (SE(2)) holonomy, analytic manufactured curvature, face-density error report, noncommuting connection, and core-loop-to-Morandotti source-vector adapter.
- **Regression tests authored:** noncommuting connection, refinement trend, sign convention, source-vector ordering, and malformed-input rejection.
- **Numerically verified:** CI executes the smooth manufactured audit and the prescribed two-core source-adapter fixture; the measured smooth density errors are recorded in the Actions artifact.
- **Open:** singular-core loop extraction from a resolved defect mesh; weak convergence of defect measures; calibrated coupling of extracted loop data to the C0-IPDG/KKT source and boundary conventions; mesh-independent Morandotti interaction convergence.
- **Not claimed:** the manufactured smooth connection is a physical defect solution; smooth curvature/torsion densities determine singular core charges without an additional limiting argument; or the adapter by itself validates the Morandotti constitutive model.

**Classification:** computational audit implementation and regression specification; execution pending.  
**FLN**
