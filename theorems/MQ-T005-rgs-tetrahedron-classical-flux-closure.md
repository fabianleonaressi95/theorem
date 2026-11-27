# MQ-T005 — Classical flux closure of an RGS carrier tetrahedron

**Classification:** [P] general Euclidean tetrahedral area-vector closure is exact; [N] one hash-checked RGS-seed instance is numerically audited; [O] Q6 cellular identification and \(SU(2)\) quantization are open.

## Statement

Let \(p_0,p_1,p_2,p_3\in\mathbb R^3\) be affinely independent. For each of the four triangular faces \(f\), let \(\mathbf A_f=A_f\mathbf n_f\) be its outward-oriented area vector. Then

\[
\sum_{f=1}^4\mathbf A_f=0.
\]

This is the classical closure condition for the tetrahedral face fluxes.

## Proof

For every constant \(c\in\mathbb R^3\), the divergence theorem gives
\[
c\cdot\sum_f\mathbf A_f
=\int_{\partial T}c\cdot n\,dA
=\int_T\nabla\cdot c\,dV=0.
\]
Hence the vector sum is zero. \(\square\)

## RGS-seed instance

The selected carrier indices are \((0,8,32,56)\) from the 64-site seed reconstructed by **src/rgs_seed_64_reconstruction.py**, whose expected coordinate SHA-256 is

**6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf**.

The tetrahedron has oriented volume \(0.11513116875074175\). Its four face areas are approximately

\[
0.7311849740919621,\quad
0.3435980118580774,\quad
0.4756732132860049,\quad
0.4720653654111676.
\]

The computed closure residual is \(6.36\times10^{-17}\). The independent script and regression test are **scripts/audit_mq005_rgs_tetrahedron_flux.py** and **tests/test_mq005_rgs_tetrahedron_flux.py**; the machine-readable output is **results/mq005_rgs_tetrahedron_flux.json**.

## Incidence obstruction

The pairwise Hamming distances between the four Q6 labels are \(1,1,3,2,2,2\). Thus only two of the six pairs are Q6 edges. The selected geometric tetrahedron is not a Q6 \(K_4\) and is not identified with a Q6 tetrahedral cell. Its geometric faces must not be relabelled as Q6 2-cells.

## Quantum boundary

No spins \(j_f\), Immirzi/area scale, or exact coherent intertwiner are assigned. In particular, the four unequal face areas do not justify reusing the equal-spin-\(\tfrac12\) intertwiner from MQ-T002. The map from these classical fluxes to admissible \(SU(2)\) representation data remains open.

## References and relation to existing records

- MQ-002 / MQ-T002: exact dimension-two four-valent \(j=\tfrac12\) intertwiner.
- MQ-003 / MQ-T003: invariant one-link gluing and the distinction between area and shape matching.
- **docs/RGS_CARRIER_DERIVED_COFRAME_TETRAHEDRON_2026-11-26.md**: source construction and explicit warning that the selected tetrahedron is not asserted to be a Q6 subcomplex.
- **theorems/T154-rgs-spatial-coframe-constraint-splitting.md**: spatial coframe and constraint splitting; not a spacetime tetrad.

**No claim** is made about a global Regge geometry, Q6–RGS continuum correspondence, spin-foam dynamics, or physical validation.
