# Q6 many-body / mean-field and RGS Berry-cycle audits

**Status:** finite-dimensional numerical research benchmarks. Neither script establishes a mean-field limit, a continuum Berry bundle, or a physical calibration of MQM-1.

## 1. Two-boson comparison

`audits/morphodynamics/q6_manybody_meanfield.py` compares:

- exact symmetric two-boson Fock-space dynamics on the 64-vertex Q6 graph (dimension 2,080);
- the Hartree closure for a normalized one-particle orbital `phi`;
- the same 192-edge metric variables `x_e = log(w_e)` in both systems.

The declared Hamiltonian is

```text
H2(x) = dGamma(h(x)) + U * sum_v |2_v><2_v|
h(x)  = t * B * diag(exp(x)) * B^T
```

Here `U` is an explicit on-site Bose-Hubbard interaction. The corresponding Hartree equation is

```text
i hbar d(phi)/dt = [h(x) + U * diag(|phi|^2)] phi
```

The full and Hartree geometric forces use the same unnormalized one-body density matrix `Gamma`, with `trace(Gamma)=2`:

```text
dE/dx_e = kappa * (x_e - x*_e) + t * exp(x_e) * b_e^T Gamma b_e
```

For Hartree, `Gamma = 2 |phi><phi|`. For the exact state, `Gamma[p,q] = <a_p^dagger a_q>` is reconstructed from the Fock amplitudes. Thus the comparison isolates the closure error due to correlations while retaining a common backreaction law.

Reported diagnostics:
- Frobenius norm of the difference between trace-one one-body density matrices;
- Euclidean distance between the two 192-component geometries;
- exact two-body state norm drift.

The noninteracting case `U=0` is the essential regression: a product initial state must remain a product under one-body evolution, and the two closures must agree up to integration error. For `U != 0`, deviations are numerical evidence only. A genuine mean-field limit requires a sequence in particle number `N`, a specified interaction scaling (typically `U/(N-1)`), uniform estimates, and convergence of reduced density matrices. This two-particle benchmark does not prove that limit.

## 2. RGS-derived Berry loop

`audits/morphodynamics/q6_rgs_berry_cycle.py` constructs a closed loop from the archived 64-point RGS seed. It applies two fixed, dimensionless symmetric strain generators:

```text
S1 = diag(1,-1,0)
S2 = [[0,1,0],[1,0,0],[0,0,0]]
F(theta) = exp(amplitude * (cos(theta)*S1 + sin(theta)*S2))
```

The edge lengths are recomputed from the deformed RGS coordinates. Conductances use the existing metric-graph convention:

```text
w_e(theta) = ell_rms(theta) / ell_e(theta)
```

No edge weights are fitted to obtain a target phase. The Hamiltonian is the resulting weighted Q6 Laplacian. For an isolated eigenline `u_j`, the Wilson product is

```text
W = product_j <u(theta_j),u(theta_(j+1))> / abs(<u(theta_j),u(theta_(j+1))>)
gamma_B = -arg(W)
```

The final overlap closes the loop. This is invariant under independent phase choices of the sampled eigenvectors. The script refuses to report a phase if the selected band loses its adjacent spectral gap or if neighboring overlaps vanish.

The Hamiltonian is real symmetric, so a nondegenerate real eigenline can only exhibit a 0 or pi holonomy (a sign change). A nontrivial continuous U(1) Berry curvature would require an appropriate complex Hermitian family, for example a physically specified magnetic/gauge connection; it must not be inferred from this real metric-only cycle. The constant ground state is exactly trivial and is used as a control test. On the hash-checked RGS seed, the declared loop with amplitude 0.04 and 240 samples gives a pi holonomy for band index 8; the minimum adjacent gap is approximately 1.90e-3 and the minimum neighboring overlap approximately 0.965. Bands 1–4 are poorly resolved by this mesh and are rejected by the overlap threshold. This is a finite-seed numerical result, not a continuum invariant. Excited-band holonomy is meaningful only after both spectral-gap and overlap tests pass.

## 3. Reproducibility

Run from the repository root:

```bash
python -m pytest -q tests/test_q6_manybody_meanfield.py tests/test_q6_rgs_berry_cycle.py
```

An interaction sweep (including the exact product-state control at U=0) can be launched with:

```bash
python - <<'PY'
from audits.morphodynamics.q6_manybody_meanfield import interaction_sweep
print(interaction_sweep(final_time=0.25, samples=26))
PY
```

Berry loop:

```bash
python - <<'PY'
from audits.morphodynamics.q6_rgs_berry_cycle import berry_holonomy
print(berry_holonomy(band_index=8, amplitude=0.04, steps=240))
PY
```

The latter may correctly stop if the chosen excited eigenline is not isolated. In that case the output is **no Berry value for that band**, not a zero phase.

## 4. Classification and next proof obligations

| Item | Classification |
|---|---|
| Fock-space construction and on-site interaction matrix | Exact finite-dimensional definition |
| Noninteracting product-state regression | Numerical verification |
| Interacting full-vs-Hartree discrepancy | Numerical verification, parameter-dependent |
| RGS-strain loop and Wilson product | Exact finite-dimensional construction |
| Berry phase for a band | Numerical result only if gap/overlap checks pass |
| Mean-field convergence as N tends to infinity | Open |
| Continuum RGS Berry connection / curvature | Open |
| Physical derivation of U, t, kappa, mu | Open |

Reference interaction sweep for the localized initial state, zero reference geometry, DOP853 (rtol=2e-8, atol=2e-10), and final time 0.25:

| U | max one-body Frobenius error | max geometry L2 error | max norm drift |
|---:|---:|---:|---:|
| 0.0 | 2.92e-8 | 5.43e-10 | 1.96e-8 |
| 0.1 | 1.19e-5 | 4.54e-8 | 1.98e-8 |
| 0.5 | 2.96e-4 | 9.69e-7 | 1.99e-8 |
| 1.0 | 1.18e-3 | 3.06e-6 | 2.03e-8 |

These are reference numerical values from the stated finite model; they are not universal error bounds.

No change is made to T113-D/F, T102, or T048: these benchmarks are companion audits and do not upgrade their theorem status.
