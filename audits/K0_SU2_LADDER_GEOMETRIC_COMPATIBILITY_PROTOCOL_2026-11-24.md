# K0 spin-61.5 reconstruction and geometric ladder compatibility

**Date:** 24 November 2026  
**Classification:** spectral reconstruction reported from local artifacts; geometric compatibility is an open test  
**Status:** reconstruction results recorded as externally reported; test protocol specified, not yet executed in this repository

## 1. Reported spectral reconstruction

A local audit performed outside this repository reports the following files:

- \`K0_INTRINSIC_SU2_REPORT.json\`
- \`K0_INTEGER_OPERATOR_CERTIFICATION.json\`
- \`K0_LADDER_ALGEBRA_REPORT.json\`

The reported conclusions are:

1. \`intrinsic_su2_verified: true\`, with \(j=61.5=123/2\) and \(j(j+1)=3843.75\).
2. On the 124-dimensional complement of the kernel, \(N=10K_0-5\) has integer eigenvalues \(0,\ldots,123\); moments 1 through 6 are reported exact and \`all_pass: true\`.
3. Ladder operators are reported to satisfy \([N,S]=S\), with residuals of order \(10^{-13}\).

The user's independent reconstruction from local \`K0.npy\` reports
\[
K_0|_{\mathcal H_{124}}=\frac{J_z+66.5I}{10},
\qquad
\operatorname{spec}(J_z)=
\{-61.5,-60.5,\ldots,61.5\}.
\]
Equivalently,
\[
N=10K_0-5I=J_z+61.5I,
\qquad
\operatorname{spec}(N)=\{0,1,\ldots,123\}.
\]
The kernel has dimension 64 and \(K_0=0\) there.

**Provenance qualification.** The three JSON reports and \`K0.npy\` were found in the user's local \`~/Scaricati\` directory; they have not yet been committed or attached to this repository. The statements above are therefore recorded as reported local results, not as results independently rerun by this repository audit. The spectral arithmetic is internally consistent:
\[
\frac{123}{2}\left(\frac{123}{2}+1\right)
=\frac{123\cdot125}{4}=3843.75.
\]
The value \(j=61.5=(124-1)/2\) is fixed by the dimension once an irreducible spin representation on the 124D sector is assumed; the affine reconstruction of \(J_z\) from an equally spaced spectrum alone does not establish a geometric \(SU(2)\) action.

## 2. Scope: what is and is not established

The reported spectrum supports a canonical *spectral model* for \(J_z\) on the 124D complement. It does not by itself establish:

- that the ladder generators coincide with geometric operators;
- that the kernel carries a spin-\(31.5\) representation;
- that the reconstructed \(SU(2)\) is selected by the Q6/RGS geometry;
- that the exact generating source of \(K_0\) has been recovered.

In particular, \(K_0=0\) on the 64D kernel contains no information that selects a \(J_z\) action on that kernel. A spin-\(31.5\) extension would require independent operators and independent commutator/Casimir checks.

## 3. Test 2 — compatibility with \(Z_S,Z_A,T_{\mathrm{transport}}\)

### 3.1 Required input arrays — AVAILABLE on `main`

All required arrays are committed on `main` (verified 2026-11-24, `git ls-files`):

| Array | Repository path | SHA-256 |
| --- | --- | --- |
| \(K_0\) | `artifacts/K0.npy` (188×188 float64) | `1aa4a6c0e237f5fb43d1d05e2de5a073087f3a2c1d1d200946fd693f1476aaa1` |
| \(Z_S\) | `artifacts/Z_S.npy` (188×188 float64) | `a37b6d13a7c97122d6adaf015764c992ca6380cca023f43dce2b01fecf350d16` |
| \(Z_A\) | `artifacts/Z_A.npy` (188×188 float64) | `e526e9ae82a2a71e1f636ba6c19c9bf3a755768093f9a234cd3d7bc88427412f` |
| \(P_G\) | `artifacts/P_G.npy` (188×188 float64) | `2eb41891a2b545499f80078eafb504e01c3f26f583310e49a60d3bf5be787493` |
| full bundle | `data/RGS_PSU_all_matrices.npz` | `29b758d56c20ba9eb488d1846d1439c0fc145973762421d03083239ee832bba1` |

The NPZ additionally contains `T_transport`, `R_geo_tangent`, `Pi_AT`, `B_PG_A`, `U_polar`, `A_geometry_orthonormal`, `A_raw`, `Q_tangent`, `X_Oh_reconstructed`, `Q6_states`, `Q6_adjacency`, `Q6_laplacian`, `Q6_antipodal`, each in the same 188D (or stated) coordinate basis. Loading example:

```python
import numpy as np
d = np.load("data/RGS_PSU_all_matrices.npz")
K0, ZS, ZA, PG, T = d["K0"], np.load("artifacts/Z_S.npy"), np.load("artifacts/Z_A.npy"), d["P_G"], d["T_transport"]
```

Coordinate-basis provenance: all arrays share the archived 188D tangent coordinate system documented in `docs/RGS_188D_OPERATOR_PROVENANCE.md`; the basis-identification certificate itself remains an open item (see §6 of that document). A filename alone is insufficient — the SHA-256 values above are the content certificate.

### 3.2 Construct the standard ladder on the 124D sector

Let \(P_\perp=I-P_G\). Diagonalize the Hermitian restriction of \(N=10K_0-5I\) to \(\operatorname{Im}P_\perp\), ordering the eigenvectors by eigenvalue \(n=0,\ldots,123\). In that ordered basis define
\[
J_z=\operatorname{diag}(-j,-j+1,\ldots,j),\qquad j=123/2,
\]
and
\[
(J_+)_{n+1,n}=\sqrt{(j-m_n)(j+m_n+1)},
\quad m_n=-j+n,
\]
with all other entries zero; set \(J_-=J_+^\dagger\). Check
\[
[J_z,J_\pm]=\pm J_\pm,\qquad
[J_+,J_-]=2J_z,
\]
and
\[
J_x=\tfrac12(J_++J_-),\quad
J_y=\tfrac1{2i}(J_+-J_-),\quad
J_x^2+J_y^2+J_z^2=j(j+1)I_{124}.
\]

The test must report residuals for all three Lie brackets and the Casimir, not merely the spectrum of \(J_z\).

### 3.3 Phase-gauge issue

The ordered eigenvectors of a simple-spectrum Hermitian matrix are defined only up to independent phases. Consequently, the matrix entries of \(J_\pm\) in the original 188D coordinates depend on a phase convention.

The implementation must state and freeze a deterministic convention (for real data, for example, choose the sign so the largest-magnitude component of each eigenvector is positive). In addition, report gauge-invariant quantities and, where an alignment is claimed, test whether a diagonal unitary phase change can account for the difference. Do not interpret a mismatch under one arbitrary eigenvector phase convention as a geometric obstruction.

### 3.4 Compare against the archived operators

Embed the candidate \(J_z,J_\pm,J_x,J_y\) into the 188D space by zero extension on \(\operatorname{Im}P_G\), unless an independently justified kernel action is supplied. For each \(B\in\{Z_S,Z_A,T_{\mathrm{transport}}\}\), report:

- \(\|[J_z,B]\|_F\), \(\|[J_+,B]\|_F\), and \(\|[J_-,B]\|_F\);
- the same commutators for \(P_\perp B P_\perp\), \(P_GBP_\perp\), \(P_\perp BP_G\), and \(P_GBP_G\), so kernel/complement couplings are not hidden;
- normalized residuals \(\|[J,B]\|_F/(\|J\|_F\|B\|_F)\), with zero-denominator cases explicitly handled;
- covariance/intertwining residuals in the actual common basis, if the basis certificate is available.

For \(T_{\mathrm{transport}}\), the already archived provenance record identifies it as a rank-64 polar partial isometry with range in \(\operatorname{Im}P_G\). This makes the kernel/complement block analysis essential; do not assume it is a generic 188D operator or an independent connection.

### 3.5 Nontriviality controls

A small commutator is not automatically evidence of a geometric \(SU(2)\). Compare the observed residuals against:

1. phase-gauge variants of the same ladder construction;
2. random unitary conjugates preserving the \(J_z\) spectrum;
3. a null model in which the same spectral ladder is placed in a random 124D subspace;
4. the exact algebraic identities forced by the construction.

A geometric compatibility claim requires a residual materially smaller than the null controls and a basis-independent explanation of the alignment.

## 4. Kernel spin-31.5 question

The 64D kernel has the right dimension for \(j=31.5\), but dimension alone is not evidence of that representation. A separate candidate triple \((J_x^{(0)},J_y^{(0)},J_z^{(0)})\) must be obtained from operators independent of \(K_0\), restricted to \(\operatorname{Im}P_G\), and tested against
\[
[J_x^{(0)},J_y^{(0)}]=iJ_z^{(0)}
\quad\text{and cyclic permutations},\qquad
\sum_a(J_a^{(0)})^2=31.5(32.5)I_{64}.
\]
The construction must not infer these operators from the desired spectrum or fit them to the Casimir after the fact.

## 5. Required verdict categories

- **PASS — spectral reconstruction:** affine \(J_z\) and integer \(N\) identities reproduce from the archived arrays.
- **PASS — ladder algebra:** all Lie brackets and Casimir reproduce in a frozen basis convention.
- **PASS — geometric compatibility:** \(J_\pm\) have independently justified, gauge-robust relations to \(Z_S,Z_A,T_{\mathrm{transport}}\), beating the null controls.
- **OPEN — kernel representation:** no independent spin-\(31.5\) generators are available.
- **BLOCKED — provenance:** exact \(K_0\) generating source and basis certificate remain unavailable.

These verdicts must be kept separate. A PASS in the first two categories does not imply a PASS in geometric compatibility.

## 6. Current repository state and immediate next action

The three JSON reports and `q6-d5-integer-fiber.yml` are now present on `main`. The workflow is an exact-arithmetic Q6-D5 audit; its declared path filters and commands do not run the geometric ladder-compatibility test in this document.

**Input status corrected (2026-11-24):** the required arrays are in fact already on `main` — see §3.1 for exact paths and SHA-256 hashes. The earlier statement that they were missing was incorrect: `K0.npy`, `Z_S.npy`, `Z_A.npy`, `P_G.npy` are tracked under `artifacts/` (moved from repository root in the 2026-11-26 repository reorganization) and `data/RGS_PSU_all_matrices.npz` contains `T_transport` and the remaining operators in the same coordinate basis.

**Test 2 executed (2026-11-24) — cubic-sector variant:** the joint \(SU(2)\times O_h\) audit was run via `scripts/audit_k0_su2_oh_joint_compatibility.py` (report `audits/K0_SU2_OH_JOINT_COMPATIBILITY_2026-11-24.json`). The \(O_h\) character projectors were reconstructed in the same 188D tangent basis as `models/tangent_triplet_anisotropy.py`): \(P_{T_{1u}}\) has rank 39 and \(P_{T_{2u}}\) rank 30, reproducing the reported 13 and 10 triplets. Results:

- \([K_0,R_g]\) has Frobenius norm up to \(83.9\) over the 48 cubic operations; restricted to the \(P_\perp\) block the maximum is \(46.4\), while the \(P_G\) block is \(\sim4\times10^{-14}\) (trivially, since \(K_0=0\) on the kernel). \(K_0\) therefore does **not** commute with the cubic action on the 124D complement.
- \(K_0\) has large off-diagonal blocks between all cubic sectors (e.g. \(\|P_{T_{1u}}K_0P_{T_{2u}}\|=10.4\), \(\|P_{T_{1u}}K_0P_{\rm rest}\|=21.4\)).
- The ladder generators \(J_z,J_\pm,J_x,J_y\) have Frobenius norm \(O(50\!-\!360)\) in **every** \(T_{1u}/T_{2u}/{\rm rest}\) block pair: they mix the cubic sectors completely.
- \(Z_S,Z_A\) have all cubic-sector blocks \(\le0.8\) (they are supported on the 6D carrier \(\mathcal W\) only); \(T_{\rm transport}\) blocks are \(1.3\!-\!5.3\).

**Verdict for the cubic-sector variant of geometric compatibility: FAIL** — the spin-61.5 ladder and \(K_0\) do not respect the \(O_h\) \(T_{1u}/T_{2u}\) decomposition in the archived basis. Caveat: the 188D basis-identification certificate remains open (`docs/RGS_188D_OPERATOR_PROVENANCE.md`); however the same \(O_h\) action is the one verified against the Coulomb Hessian in `models/tangent_triplet_anisotropy.py`, so the negative result is meaningful within the archived data. The commutator suite of §3.4 against \(Z_S,Z_A,T_{\rm transport}\) with frozen phase convention and §3.5 null controls remains implemented in `scripts/audit_k0_su2_ladder_geometric_compatibility.py` (report `audits/K0_SU2_LADDER_GEOMETRIC_COMPATIBILITY_2026-11-24.json`); preliminary commutators are large and show no covariance, but the formal verdict categories of §5 are unchanged pending review of that report.
