# T113-H — Metric-variation and spectral control suite

**Classification:** numerical verification of finite-dimensional spectral identities and a lapse-variation identity; **not** a derivation or numerical estimate of quasicrystal packet gravitational mass.

**Dependencies:** [T113](T113-quasicrystal-phonon-phason-gravitational-mass.md), [T113-A](T113A-metric-action-phonon-phason-mode-sensitivity.md).

## B.1 Purpose

T113-A gives the generalized Hellmann–Feynman identity and requires four controls before any coupled quasiperiodic claim: a fluid, isotropic longitudinal/transverse solid branches, zero phonon–phason coupling, and nonzero coupling. This record supplies reproducible finite-dimensional controls for those spectral steps and makes explicit what the quadratic action's lapse variation does—and does not—compute.

## B.2 Model and exact sensitivities

For each scalar acoustic sector choose
[
mathcal M(ho)=ho^m,qquad
mathcal K(ho)=ho^{m+2a}.
]
At unit wave number, (omega^2=mathcal K/mathcal M=ho^{2a}), hence
[
rac{dlog c}{dlogho}=a.
]
The three scalar controls use (a=0.25) (fluid), (a_L=0.20) (longitudinal solid), and (a_T=-0.10) (transverse solid). These are manufactured constitutive laws for regression, not empirical material parameters.

For the two-sector toy model,
[
mathcal M=ho I,qquad
mathcal K=
egin{pmatrix}
ho^{1+2a_p}&rho^{1+a_p+a_s}\
rho^{1+a_p+a_s}&ho^{1+2a_s}
end{pmatrix},
]
with (a_p=0.20), (a_s=-0.10). At (r=0) the sectors decouple exactly. At (r=0.20), the off-diagonal block mixes eigenvectors while the kernel remains positive definite. The code compares centered finite differences of (logomega_j^2) against
[
rac{domega_j^2}{dlogho}=
rac{q_j^dagger[(dmathcal K/dlogho)
-omega_j^2(dmathcal M/dlogho)]q_j}
{q_j^daggermathcal Mq_j}.
]
All modes in this toy model are simple near the reference density (ho=1).

## B.3 Lapse variation: exact scope

For a fixed quadratic oscillator sector in a homogeneous lapse (N),
[
L_N=rac{1}{2N}dot q^Tmathcal Mdot q
-rac{N}{2}q^Tmathcal Kq.
]
At (N=1), (-partial L_N/partial N) equals the canonical quadratic Hamiltonian
[
H_2=	frac12(dot q^Tmathcal Mdot q+q^Tmathcal Kq).
]
The test checks this identity by finite difference. It does **not** reproduce the negative or equation-of-state-dependent EKN sound-packet contribution: that requires the coupled medium's induced response, constitutive metric dependence, nonlinear terms, background subtraction, and boundary/long-range contributions. In particular, (H_2/c^2) must not be relabelled as the EKN packet mass.

## B.4 Reproducibility

Run:
```bash
python scripts/audit_t113_metric_variation.py --pretty
pytest -q tests/test_t113_metric_variation.py
```

The acceptance conditions are:
- finite-difference and Hellmann–Feynman logarithmic sensitivities agree to (10^{-7});
- (r=0) gives the union of independent phonon and phason spectra;
- (r=0.20) keeps positive eigenvalues and verifies the same sensitivity identity for mixed modes;
- lapse variation agrees with the quadratic Hamiltonian to (10^{-9}).

## B.5 Status and next mathematical obligation

- **Numerically verifiable in this suite:** generalized spectral sensitivity for the manufactured fluid/solid/decoupled/coupled controls; quadratic lapse-variation identity.
- **Not established:** full metric stress-energy for a specified icosahedral constitutive tensor; the EKN medium-backreaction calculation in the solid controls; equality of the speed-derivative candidate and metric-derived packet mass; any quasicrystal packet mass or sign.
- **Next required derivation:** choose a concrete constitutive action for the medium and perturbation, vary the *combined* action with respect to the weak-field lapse/metric while allowing the background medium to respond, solve the second-order field/material equations, and retain boundary terms. Only after recovering the EKN fluid and isotropic-solid expressions should the (R\ne0) quasicrystal case be evaluated.

The suite is a control and falsification scaffold, not evidence that the open T113 target has been solved.
