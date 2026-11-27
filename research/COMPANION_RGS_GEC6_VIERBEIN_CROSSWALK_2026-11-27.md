# Companion-repository crosswalk: GEC-6 and RGS vierbein evidence

**Date:** 27 November 2026  
**Primary repository:** `fabianleonaressi95/theorem`  
**Companion repository:** `fabianleonaressi95/rgs-qlg-quaternion-bridge`  
**Purpose:** connect merged companion work PRs #233–#235 to the existing theorem architecture without copying or renumbering canonical proofs.

This is an evidence-routing document, not a new theorem and not a claim that the companion models are physically identified.

## 1. GEC-6 lower/upper trigram decomposition — companion PR #233

Canonical mathematical dossier and implementation:

- [GEC-6 trigram block decomposition](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/research/GEC6_TRIGRAM_BLOCK_DECOMPOSITION.md)
- [Exact bookkeeping implementation](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/src/gec6_trigram_decomposition.py)
- [Focused tests](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/tests/test_gec6_trigram_decomposition.py)
- [Q6 graph-cycle to A5 quotient dossier](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/research/GEC6_SIXFOLD_PAIR_GEOMETRY_A5_QUOTIENT.md)

The exact finite algebra is:

\[
\Lambda^2(\mathbb Z^6)
=\Lambda^2L\oplus(L\otimes U)\oplus\Lambda^2U,
\qquad 3+9+3=15,
\]
where (L=\langle e_0,e_1,e_2\rangle) and (U=\langle e_3,e_4,e_5\rangle). The block-preserving wreath group ((S_3\times S_3)\rtimes C_2) has order 72. Under the contraction
\[
c(e_i\wedge e_j)=e_j-e_i,
\]
the mixed block alone surjects onto the rank-five root lattice (A_5), with rank-four kernel. The source of the composite map is the **graph-cycle lattice** of (Q_6^{(1)}), of rank 129; it is not (H_1) of the filled cubical six-cube, which is zero.

### Orientation correction required by review

With graph edges globally oriented from bit 0 to bit 1, translation by (t\in(\mathbb Z/2)^6) acts on the oriented (ij)-square generator by
\[
\epsilon_{ij}(t)=(-1)^{t_i+t_j}.
\]
Thus a general bit translation is not the identity on the exterior-square module and need not preserve (\ker c); it does not generally descend to (A_5). For the global antipode (t=(1,1,1,1,1,1)), every pair receives sign (+1), so the antipodal action on the GEC-6 quotient is indeed trivial. The companion dossier/test correction is tracked in [the follow-up audit PR](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/236) once opened; until merged, use the explicit qualification above.

### Existing theorem links — related, not interchangeable

- [T055 — Q6 dyadic subdivision chain map](../theorems/T055-q6-dyadic-subdivision-chain-map.md) and [T062 — Kathara–Q6 integral chain map](../theorems/T062-kathara-q6-integral-chain-map.md) concern cellular subdivision/chain maps, not the GEC-6 contraction itself.
- [T069 — Q6 antipodal Walsh covariance](../theorems/T069-q6-antipodal-walsh-covariance.md) distinguishes the graph antipode (v\mapsto v\oplus63) from the RGS coordinate inversion (v\mapsto v\oplus7). Its covariance statements are not a substitute for the oriented-square quotient argument above.
- [T053 — exterior-square projector lemma](../theorems/T053-exterior-square-projector-lemma.md) concerns the exterior-square action induced by the icosahedral (6\times6) matrix. It is **not** the GEC-6 contraction (\Lambda^2\mathbb Z^6\to A_5).

No new theorem number is assigned here: the companion dossier remains the canonical detailed source for this GEC-6 decomposition, and the theorem repository already has later T157–T158 records.

## 2. RGS–PSU vierbein/tetrad reconstruction — companion PR #234

Canonical companion records:

- [Reconstruction status and recovery map](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/VIERBEIN_RECONSTRUCTION_STATUS.md)
- [Deterministic generator](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/examples/reconstruct_rgs_vierbein_tetrads.py)
- [Numerical report](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/results/vierbein_reconstruction/vierbein_reconstruction_report.json)
- [SHA-256 manifest](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/results/vierbein_reconstruction/SHA256SUMS.txt)
- [Reconstruction tests](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/tests/test_rgs_vierbein_reconstruction.py)

The reconstructed spatial coframes are computed from the checked 64-site seed using the archived local covariance and principal positive square root. The (64\times4\times4) RGS–PRISM array is the static lift (e=\operatorname{diag}(1,E_i)), with (eta=(-,+,+,+)). It is a deterministic reconstruction, not byte-for-byte recovery of the historical binary payload and not a coordinate-dependent spacetime coframe. The Ellis and Kerr–Schild coframes are separate analytic benchmark geometries; they are not derived RGS solutions.

The report's maximum condition number for (E_i) is approximately 1.733712; its square, approximately 3.00576, is the corresponding condition number for (C_i/c_0). This reconciles the two matrix conventions in the historical reconstruction notes.

**TEGR/torsion remains NOT CERTIFIED.** A tetrad array alone is insufficient: a base manifold and coordinate-dependent coframe, an inertial spin connection with fixed conventions, and the torsion/curvature identity audit are still required.

### Existing theorem link

[T154 — RGS spatial coframe and labelled constraint splitting](../theorems/T154-rgs-spatial-coframe-constraint-splitting.md) proves the exact finite (3+1) split of the constraint-normal space and records the radial edge feature as a scalar singlet, not Lorentz time. PR #234 adds reproducible spatial coframe and static-lift arrays; it does not extend T154 into a dynamical tetrad or TEGR theorem. See also [the QLG/QAT recovery audit](../docs/RGS_QLG_QAT_VIERBEIN_RECOVERY_AUDIT.md), which keeps edge coframes, vertex spatial matrices and spacetime tetrads distinct.

## 3. Evidence matrix — companion PR #235

The [51-step evidence matrix](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/51_STEP_EVIDENCE_MATRIX_2026-11-26.md) is the companion repository's traceability index. Its 2026-11-26 snapshot predates the #233/#234 merges; the companion follow-up adds them as supplements to S35 (GEC-6) and S11 (RGS seed/coframe provenance), without creating duplicate theorem records or renumbering S01–S51.

No pull-request-triggered workflow runs were returned for the three merge commits in the audit. This means **no CI run evidence was retrieved**, not that tests failed or passed. Reproduction commands remain in the companion dossiers.

## 4. Dependency and interpretation rules

1. (Q_6) graph cycles, the filled cubical six-cube, the (A_5) root lattice, and the Cartesian PRISM product are distinct objects. An abstract rank-five lattice isomorphism does not identify their graph actions, metrics, spectra or dynamics.
2. The antipodal result is specific to the global bit complement; do not extend it to all (C_2^6) translations.
3. The RGS static lift is not the historical edge coframe and does not provide derivatives or an inertial spin connection.
4. Passing implementation tests is software evidence only. Exact algebraic proofs, finite audits, floating-point reconstruction and physical hypotheses must remain separately labelled.
