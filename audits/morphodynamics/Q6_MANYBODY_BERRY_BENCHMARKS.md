# Q6 many-body / mean-field and RGS Berry-cycle audits

**Status:** finite-dimensional numerical research benchmarks. Neither script establishes a mean-field limit, a continuum Berry bundle, or a physical calibration of MQM-1.

## 1. Two-boson comparison

`audits/morphodynamics/q6_manybody_meanfield.py` compares:

- the exact symmetric two-boson Fock-space dynamics on the 64-vertex Q6 graph (dimension `binom(65,2)=2080`);
- the Hartree closure for a normalized one-particle orbital `phi`;
- the same 192-edge metric variables `x_e=log(w_e)` in both systems.

The declared Hamiltonian is

[
H_2(x)=dGamma(h(x))+
Usum_{v=0}^{63}|2_vanglelangle2_v|,
qquad
h(x)=t B,mathrm{diag}(e^x)B^T.
]

Here `U` is an explicit on-site Bose-Hubbard interaction. The corresponding Hartree equation is

[
ihbardotphi=
left[h(x)+U,mathrm{diag}(|phi|^2)ight]phi.
]

The full and Hartree geometric forces are computed from the same unnormalized one-body density matrix (Gamma), with (mathrm{Tr}Gamma=2):

[
partial_{x_e}E=
kappa(x_e-x_e^*)+
t e^{x_e}b_e^TGamma b_e.
]

For Hartree, (Gamma=2|phianglelanglephi|). For the exact state, (Gamma_{pq}=langle a_p^dagger a_qangle) is reconstructed from the Fock amplitudes. Thus the comparison isolates the closure error due to correlations, while retaining a common backreaction law.

Reported diagnostics:
- Frobenius norm of the difference between trace-one one-body density matrices;
- Euclidean distance between the two 192-component geometries;
- exact two-body state norm drift.

The noninteracting case (U=0) is the essential regression: a product initial state must remain a product under one-body evolution, and the two closures must agree up to integration error. For (U
e0), deviations are numerical evidence only. A genuine mean-field limit requires a sequence in particle number (N), a specified interaction scaling (typically (U/(N-1))), uniform estimates, and convergence of reduced density matrices; this two-particle benchmark does not prove that limit.

## 2. RGS-derived Berry loop

`audits/morphodynamics/q6_rgs_berry_cycle.py` constructs a closed loop from the archived 64-point RGS seed. It applies the two fixed symmetric strain generators

[
S_1=mathrm{diag}(1,-1,0),qquad
S_2=egin{pmatrix}0&1&0\1&0&0\0&0&0end{pmatrix},
]

through (F(	heta)=exp[epsilon(cos	heta S_1+sin	heta S_2)]). The edge lengths are recomputed from the deformed RGS coordinates and the conductances use the existing metric-graph convention

[
w_e(	heta)=ell_{m rms}(	heta)/ell_e(	heta).
]

No edge weights are fitted to obtain a target phase. The Hamiltonian is the resulting weighted Q6 Laplacian. For an isolated eigenline (u_j), the Wilson product is

[
W=prod_{j=0}^{M-1}
rac{langle u(	heta_j),u(	heta_{j+1})angle}
{|langle u(	heta_j),u(	heta_{j+1})angle|},
qquad
gamma_B=-arg W,
]

with the last overlap closing the loop. This is invariant under independent phase choices of the sampled eigenvectors. The script refuses to report a phase if the selected band loses its adjacent spectral gap or if neighboring overlaps vanish.

The Hamiltonian is real symmetric, so a nondegenerate real eigenline can only exhibit a (0) or (pi) holonomy (a sign change). A nontrivial continuous (U(1)) Berry curvature would require an appropriate complex Hermitian family, for example a physically specified magnetic/gauge connection; it must not be inferred from this real metric-only cycle. The constant ground state is exactly trivial and is used as a control test. Excited-band holonomy is meaningful only after the spectral-gap test passes.

## 3. Reproducibility

Run from the repository root:

```bash
python -m pytest -q tests/test_q6_manybody_meanfield.py tests/test_q6_rgs_berry_cycle.py
```

A short numerical comparison can be launched with:

```bash
python - <<'PY'
from audits.morphodynamics.q6_manybody_meanfield import run_comparison
print(run_comparison(final_time=0.25, samples=26))
PY
```

Berry loop:

```bash
python - <<'PY'
from audits.morphodynamics.q6_rgs_berry_cycle import berry_holonomy
print(berry_holonomy(band_index=1, amplitude=0.04, steps=240))
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
| Mean-field convergence as (N\to\infty) | Open |
| Continuum RGS Berry connection / curvature | Open |
| Physical derivation of (U,t,kappa,mu) | Open |

No change is made to T113-D/F, T102, or T048: these benchmarks are companion audits and do not upgrade their theorem status.
