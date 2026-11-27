# MQM-2 — Dynamical RGS–Q6 symmetry of the coupled finite flow

**Classification:** [P] equivariance identities follow exactly from the MQM-1 definitions and graph automorphism action; [N] finite numerical regression tests; [M] MQM-1's gradient/Schrödinger closure remains a declared model; [O] physical calibration and continuum limit remain open.

## 1. Question and inherited structure

EQC–RGS–Q6 identifies a 16-element subgroup
[
G_{mathrm{RGS,Q6}}cong C_2	imes D_8
]
inside (operatorname{Aut}(Q_6)), represented by the existing EQC qutrit gates. MQM-1 evolves a real edge field (xinmathbb R^{192}) and a normalized state (psiinmathbb C^{64}):
[
H(x)=gamma Boperatorname{diag}(e^x)B^T,qquad
E(x,psi;x_*)=rac{kappa}{2}|x-x_*|^2+psi^dagger H(x)psi,
]
[
dot x=-mu
abla_xE,qquad
dotpsi=-rac{i}{hbar}H(x)psi.
]

For (gin G_{mathrm{RGS,Q6}}), let (P_g) be its vertex permutation and (ho_g) its induced permutation of the 192 unoriented edges. Define
[
(P_gpsi)_{g(v)}=psi_v,qquad
(ho_gx)_{ho_g(e)}=x_e.
]

## 2. Exact covariance identities

Because (g) is a Q6 graph automorphism, it maps each edge to an edge. The chosen orientation of an image edge may agree or disagree with the canonical orientation; this changes an incidence column by a sign only. Therefore, for a signed edge permutation matrix (S_g),
[
P_gB=B S_g,qquad
S_goperatorname{diag}(e^x)S_g^T
=operatorname{diag}(e^{ho_gx}).
]
Consequently,
[
oxed{H(ho_gx)=P_gH(x)P_g^T.}
]

The quantum energy term is invariant under the simultaneous action:
[
(P_gpsi)^dagger H(ho_gx)(P_gpsi)=psi^dagger H(x)psi.
]
The complete energy is invariant precisely when the reference field is fixed:
[
ho_gx_*=x_*.
]
For such (g), differentiation of the energy identity gives gradient covariance
[

abla_xE(ho_gx,P_gpsi;x_*)
=ho_g
abla_xE(x,psi;x_*),
]
and hence the full coupled vector field is equivariant:
[
F(ho_gx,P_gpsi;x_*)=
(ho_gdot x,P_gdotpsi).
]

Thus the symmetry group of the fixed-parameter MQM-1 dynamics is exactly the reference stabilizer
[
oxed{G_{mathrm{dyn}}(x_*)=
operatorname{Stab}_{G_{mathrm{RGS,Q6}}}(x_*).}
]
The Hamiltonian covariance holds for all graph automorphisms; the restoring term centered at (x_*) is what can break the symmetry of the coupled dynamics.

## 3. Exact cases within the 16-element geometric subgroup

The inherited finite audit gives the following cases:

| Reference edge field (x_*) | (|G_{mathrm{dyn}}(x_*)|) | Interpretation |
|---|---:|---|
| Uniform on all 192 edges | 16 | Full RGS–Q6 subgroup survives |
| Six distinct direction-dependent values | 8 | Three bit translations survive; paired coordinate swap is broken |
| 192 pairwise distinct values | 1 | Only identity survives |

These are exact finite stabilizer counts for the stated reference patterns. They are not a physical calibration of (x_*).

## 4. Dynamical verification

The audit compares, for transformed initial data and reference fields:

1. Hamiltonian covariance (H(ho_gx)=P_gH(x)P_g^T);
2. energy invariance;
3. gradient covariance;
4. equivariance of both (dot x) and (dotpsi);
5. commutation of a deterministic RK4 time stepper with the group action.

The tests cover all 16 elements for the uniform reference, all 8 surviving elements for the directional reference, and the identity for a generic edgewise-distinct reference. They also exhibit a non-stabilizing element for which the reference and energy covariance fail.

Run:
```bash
python -m pytest -q tests/test_mqm_dynamical_rgs_q6_symmetry.py
```

The RK4 checks are numerical consistency tests of the finite ODE, not proofs of global existence, long-time stability, or a continuum limit.

## 5. Scope and next obligations

This result connects the EQC gate subgroup to the actual coupled MQM-1 equations, rather than only to the static Q6 graph. It establishes a conditional symmetry statement: the dynamics inherits exactly the subgroup preserving the fixed reference conductances.

It does **not** show that all solutions are symmetric. A symmetry-equivariant flow maps symmetry-related initial conditions to symmetry-related trajectories; an individual trajectory need not be fixed by the group unless its initial condition is also fixed.

Open work:
- determine the stabilizer for a reference (x_*) derived from an RGS/PSU action rather than a test pattern;
- extend the result to an MQM model with dynamical reference data or conjugate geometric momenta;
- establish a compatible refinement/continuum limit;
- calibrate parameters and observables before assigning physical meaning.
