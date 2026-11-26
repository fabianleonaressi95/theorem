# Audit protocol: physical origin candidates for the constant 1/2 in f and in K0

**Date:** 2026-11-24
**Status:** protocol defined; M3 resolved negatively; M1, M2, M4 blocked on the K0 generating cell
**Scope:** distinguish genuine physical mechanisms producing 1/2 from spectral relabelings

## 1. Established numerical facts (do not re-derive)

- \(K_0\) on the 188D archived arrays: kernel dimension 64, complement spectrum \(\{(k+5)/10\}_{k=0}^{123}=0.5,0.6,\ldots,12.8\).
- \(N=10K_0-5I\) has spectrum \(\{0,\ldots,123\}\) on the complement; \(K_0=(N+5I)/10\).
- The complement carries the canonical spin-\(j=61.5\) ladder: \(J_z=10K_0-66.5I\) restricted, \(J_\pm\) the standard Condon–Shortley shifts. su(2) brackets and Casimir \(j(j+1)=3843.75\) verified to \(\sim5\times10^{-11}\) (`scripts/audit_k0_su2_ladder_geometric_compatibility.py`).
- With the certified basis map \(W\) (`data/rgs_188d/RGS_PSU_basis_resolution.npz`), exactly two of the 48 \(O_h\) operations commute with \(K_0\): identity and spatial inversion. Cubic symmetry of \(K_0\) is \(\mathbb Z_2\), not \(O_h\) (`audits/K0_SU2_OH_JOINT_COMPATIBILITY_2026-11-24.json`).
- \(f(0)=1/2=\lambda_{\min}^{+}(K_0)\), certified spectral coincidence (`audits/K0_SPECTRAL_LADDER_AND_ZS_SCALE.json`).
- On the 2I counting side, \(1/2\) is neither the quasipolynomial mean \(541/720\) nor the Molien identity weight \(1/120\) (T144 §4, §7).

## 2. The two distinct "one-halves" — keep separate

1. **Spectral-center half:** \(j=(0+123)/2=61.5\) — the midpoint of the integer ladder; a coordinate choice, not a mechanism.
2. **Affine offset half:** \(K_0=\frac{N}{10}+\frac12 I\) — a uniform shift of all 124 positive eigenvalues. This is the quantity whose physical origin is sought.

These are linked by construction but are not the same statement. Neither implies a physical spin.

## 3. Candidate mechanisms and required independent derivations

| Test | Mechanism | Required derivation | Status |
| --- | --- | --- | --- |
| M1 | Bohr–Sommerfeld/Maslov: \(\oint p\,dq=2\pi\hbar(n+\mu/4)\), \(\mu=2\) gives \(n+\tfrac12\) | Maslov index computed from RGS phase-space geometry, not fitted | BLOCKED: no phase-space construction identified for K0 |
| M2 | Canonical quantization: \(H=\hbar\omega(a^\dagger a+\tfrac12)\) | Identify \(q,p\) with \([q,p]=i\hbar\) and derive \(H\) without inserting 1/2 | BLOCKED: K0's generating cell unknown (`docs/K0_ORIGINAL_PRODUCER_RECOVERY_2026-11-21.md`) |
| M3 | Physical spin-1/2 / spinorial holonomy: \(U(2\pi)=(-1)^{2j}\) | Continuous rotation action on the state space, not an equally-spaced spectrum | RESOLVED NEGATIVE: only \(\mathbb Z_2\) (inversion) survives; su(2) ladder is a canonical spectral relabeling, no rotation generators beyond \(J_\pm\) defined from the eigenbasis |
| M4 | APS/Dirac boundary term: \(\operatorname{ind}=\int\mathcal A-\tfrac{\eta+h}{2}\) | Identify Dirac operator, boundary, and \(\eta\)-invariant in the RGS data | OPEN: Q6/QLG Dirac scripts exist (`scripts/q6_qlg_dirac_intertwiner.py`) but no 188D boundary problem identified |

## 4. Admissibility criteria for any claimed origin

A candidate mechanism passes only if it:

1. produces \(1/2\) (or the observed affine offset \(5/10\)) from an independent definition;
2. does not insert the constant into the initial data or fit coefficients a posteriori;
3. survives the basis-certified commutator tests (i.e., respects or explains the \(\mathbb Z_2\) result);
4. is reproducible by a committed script + JSON report.

## 5. Current verdict

- **Proved numerically:** integer spectrum of \(N\), affine form of \(K_0\), 124-level ladder, residual \(\mathbb Z_2\) symmetry, spectral coincidence \(f(0)=\lambda_{\min}^{+}(K_0)=1/2\).
- **Not proved:** any physical origin of the offset \(1/2\).
- **Priority order for future work:** M1 (Maslov) and M2 (canonical quantization) are the most promising *if* the K0 generator is recovered; M4 requires identifying a boundary problem; M3 is closed.
- **Hard blocker:** the exact generating cell of \(K_0\) is absent from all recovered sources. Until it is recovered, M1/M2/M4 cannot be executed non-circularly.
