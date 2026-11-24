# Q6/Walsh finite filtration audit

**Date:** 2026-11-24
**Status:** finite numerical audit. No fractal scaling, spectral
dimension, multifractal exponent, or physical interpretation is
established or claimed.
**Scope:** research note
`research/QUANTUM_FRACTAL_PRISM_Q6_INTERFACE_2026-11-24.md`, §6D and §8
items 1–5 only.

## 1. Operator provenance (requirement 1)

All vertex-space operators tested are taken from the canonical recovered
artifact `data/RGS_PSU_all_matrices.npz` (SHA-256 recorded in the JSON
report):

| operator | provenance | role |
|---|---|---|
| `Q6_laplacian` | stored array; verified `= 6I − Q6_adjacency` exactly | zero-commutator control |
| `Q6_adjacency` | stored array; verified 0/1 cube adjacency | control (`L = 6I − A`) |
| `Q6_antipodal` | stored array; symmetric involution, bitwise-complement permutation | stored involution |
| `Pi_AT` | stored array; Anti-Twin involution (`R_geo_tangent A = A Pi_AT`, see `scripts/audit_188d_antitwin.py`) | stored involution |
| `P_antipodal_±`, `P_AT_±` | derived `(I ± involution)/2` | derived sector projectors |
| `synthetic_GOE_control` | fixed-seed (20261124) GOE random symmetric matrix | discrimination control only — **not** a stored operator |

**Ambiguity reported (requirement 7):** no weighted or coupled
64×64 vertex-space Q6/PRISM operator could be identified unambiguously
in the canonical NPZ or in the audited scripts. The stored
`Q6_laplacian` is *exactly* the standard unweighted hypercube
Laplacian, so it can only serve as the zero-commutator control
predicted by research-note §10. A genuine coupled-operator test
remains **open** until such an operator is supplied with provenance.

## 2. Filtration definition

For `j = 0,…,6`, `E_j` is the orthogonal projection onto functions of
the first `j` columns of `Q6_states` (columns `0..j−1`), averaging over
the suffix columns `j..5`. Verified identities (all exact to <1e-12):
`E_j² = E_j = E_j*`, `rank E_j = 2^j`, `E_j E_k = E_min(j,k)`.

## 3. Results

Machine-readable report:
`results/quantum_fractal_q6/walsh_filtration_audit.json`.

- **Stored operators:** every commutator `[O, E_j]` and every Walsh
  block coupling `W_keep^T O W_~keep` vanishes *exactly* (Frobenius and
  spectral norms = 0) for all `j`, for all four stored/derived
  operators. Reason: each stored operator acts by coordinate
  permutations or bit flips, which preserve every suffix-fiber
  sigma-algebra; none mixes kept and averaged coordinates.
- **Synthetic GOE control:** commutator Frobenius norms range
  9.4–32.2 across `j = 0..5` and Walsh block norms 6.7–22.8 — the
  machinery has discriminating power; the zeros above are structural,
  not a bug.
- **Spectrum check:** numerical eigenvalues of `Q6_laplacian` match the
  Walsh formula `2|S|` (multiplicities `C(6,j)`) to <1e-14.
- **Compressions:** eigenvalues of `E_j O E_j` on `range(E_j)` are
  recorded per level in the JSON for every operator.

## 4. Negative results and non-conclusions

- Exact zero commutators for stored operators are a **structural
  property of fiber-preserving maps**, not evidence of a nontrivial
  renormalization law, scale invariance, or fractal behaviour.
- Six-bit Q6 is a single finite graph; no scaling limit, spectral
  dimension, or multifractal exponent can be extracted.
- The Walsh filtration commutes with the standard Laplacian, as proved
  in research-note §10; this audit recomputes it numerically and extends
  the check to the stored involutions.
- No statement is made about PRISM/Kathara–Q6 dynamics, quantum
  emergence, or any physical observable.

## 5. Reproduction

```bash
python experiments/quantum_fractal_q6/walsh_filtration.py   # writes JSON
python -m pytest tests/test_quantum_fractal_q6.py -v      # 7 tests
```
