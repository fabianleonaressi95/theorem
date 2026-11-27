# RGS–PSU / QLG vierbein and QAT recovery audit

**Status:** source reconstruction and archived numerical audit report recovered. The values below are historical outputs recorded in `RGS_QLG_QAT_generalization_audit.json`; the raw NPZ bundles are not currently present in the accessible repository, so this pass verifies report/source consistency rather than rerunning the binary computation.
**Scope:** distinguish the archived link coframe, the spatial vertex field called `E`, the proposed Lorentzian tetrad, and the operators grouped in the historical QAT audit. This note does not identify them by notation alone.

## 1. Recovered source chain

The archive contains the following executable source records:

- `A13_RGS_PSU_QLG_TWINE_ANTITWIN.py`: integrated QLG audit. It loads `RGS_PSU_all_matrices.npz`, the fibre-connection archive, `sea_operators.npz`, and the Giacosa twin/anti-twin bridge.
- `A14_RGS_PSU_QLG_JACOBIAN.py`: independently reconstructs the labelled (4\times192) constraint Jacobian from the (64\times3) embedding and compares its tangent projector with the archived (Q).
- `RGS_QLG_QAT_generalization_audit.py`: historical QAT generalization audit, which combines A13/A14 archives with `Q6_exact_incidence_and_H241.npz`.
- `RGS_PSU_construct_geometric_intertwiner.py`: tests a proposed geometry-to-kernel map, while explicitly warning that a projected-polar extension commuting with (K_0) is not evidence of geometric alignment.

The original binary arrays and full ZIP bundles are not currently present in the accessible `fabianleonaressi95/theorem` branch. However, the complete A13/A14 source scripts and the machine-readable QAT result `RGS_QLG_QAT_generalization_audit.json` are in the user's Library. The quantitative results below are transcribed from that archived report and cross-checked against the source definitions. They are not represented as a fresh rerun of the unavailable NPZ files.

## 2. Four distinct geometric objects

### 2.1 Archived QLG link coframe

For an oriented Q6 edge (g\to h), with (X_g\in\mathbb R^3), the recovered A13 definition is

\[
\widetilde e_{gh}
=\bigl(X_h-X_g,\;\|X_h\|-\|X_g\|\bigr)\in\mathbb R^4,
\qquad
 e_{gh}=\frac{\widetilde e_{gh}}{\|\widetilde e_{gh}\|}.
\]

It is an edge-indexed (192\times4) normalized coframe. Its fourth component is a radial increment, not a physical time coordinate. The A13 script checks its reconstruction from (X) and the edge list, its unit norm, and consistency of the archived tangent frames.

The A13 archive records (Q\in\mathbb R^{192\times188}), (K_0\in\mathbb R^{188\times188}), (R_{gh}\in SO(3)), and (U_{gh}\in SU(2)). The two biverse spin-fibre sheets are (U) and its complex conjugate. No map from the Bell-tetrahedron labels to the 64 Q6 states is silently imposed.

### 2.2 Labelled (3+1) constraint Jacobian

A14 reconstructs the constraint map
\[
F(X)=\left(
\sum_i x_i,\sum_i y_i,\sum_i z_i,
\frac12\left(\sum_i\|X_i\|^2-R_0^2\right)
\right)
\]
and its Jacobian (J\in\mathbb R^{4\times192}). The first three rows generate uniform translations; the fourth is the fixed-scale/radial covector (X_{\rm flat}^{T}). The tangent space is (\ker J), of expected dimension 188.

A14 validates the archived (Q) by (JQ\simeq0), (Q^TQ\simeq I), and equality of the projectors (QQ^T) and (Q_{\rm SVD}Q_{\rm SVD}^T). The normal complement is four-dimensional. A basis obtained by SVD is not itself a canonical physical labelling; the labels belong to the four rows of (J).

### 2.3 Spatial vertex field (E)

A recovered execution transcript records the construction
\[
 E_i=\operatorname{principal\_sqrt}(C_i/c_0),\qquad
 c_0=43.96495130838031,\qquad
 \ell^2=7.035514834154695,
\]
with a reported array shape (64\times3\times3). It also records (\|Q^TQ-I\|_F=1.3121453838922012\times10^{-14}), (\operatorname{rank}J=192), and (\operatorname{rank}(JQ)=188) for the separate response Jacobian (J\) of shape (576\times192).

These are historical transcript values, not independently recomputed values in this repository. The original (C_i) matrices and `RGS_PRISM_FINAL_vierbein_E.npy` were not recovered as accessible repository files. The reported determinant/conditioning interval for (E_i) must therefore remain a historical, unverified report until the array and its inputs are restored.

### 2.4 Proposed Lorentzian tetrad

The archived `RGS_PRISM_tetrad_4d.npy` was described as (64\times4\times4). A previous completion (e_i=\operatorname{diag}(1,E_i)), with (\eta=\operatorname{diag}(-1,1,1,1)), was explicitly only an ansatz for the temporal block. It is not derived by the link coframe or A14 constraints.

Consequently, no TEGR torsion tensor, Weitzenböck connection, Levi-Civita curvature identity, or Einstein-equivalent field equation may be claimed from that static completion alone. Those require a specified tetrad field on a base manifold, its inverse, a declared inertial spin connection (or a justified gauge choice), and derivatives/finite differences consistent with that geometry.

## 3. What the QAT generalization audit actually compares

The recovered script named `RGS_QLG_QAT_generalization_audit.py` constructs a report from the A13, A14, SEA, fibre-connection, and Q6 incidence archives. Its checks are:

1. (JQ\), (Q^TQ-I), normal orthogonality, tangent-normal orthogonality, and projector complement.
2. Agreement of the A13, SEA, and A14 tangent projectors and identity of edge lists.
3. (SU(2)) unitarity, (SO(3)) orthogonality/determinant, and quaternion-to-(SO(3)) convention (the transcript fixes the active-rotation convention; the transpose convention fails).
4. The exact Gram identity
   \[
   K_{\rm geometry,tangent}=D_{\rm tangent}^{\dagger}D_{\rm tangent}.
   \]
   This is a covariant-derivative Gram operator, not (K_0) and not the missing constrained energy Hessian.
5. The fibre operator (K_{\rm fibre}=D_{\rm fibre}^{\dagger}D_{\rm fibre}), acting on 64 two-component vertex spinors (128 complex dimensions). It is dimensionally distinct from the 192-dimensional edge-coordinate space; (Q^TK_{\rm fibre}Q) is not a defined projection.
6. Reconstruction and unit norm of the four-component edge coframe; the fourth component is radial, while (\tau) is a vertex scalar. Neither is automatically physical time or a Cartan torsion scalar.
7. Q6 incidence-chain checks (B_1B_2=0), ranks, edge and plaquette counts, plus conjugation of the two sheets' holonomies.

The source script uses the acronym **QAT** in its filename/title but the recovered code does not define an expanded name or a single standalone operator called “QAT”. This audit therefore preserves the historical label and records the explicit operators above; it does not invent an expansion.

## 4. Important non-identifications

- (e_{gh}\in\mathbb R^4) is an edge coframe, not a (4\times4) tetrad (e^a{}_{\mu}(x)).
- (E_i\in\mathbb R^{3\times3}) is a vertex-indexed spatial matrix field, not by itself a spacetime metric.
- (K_{\rm geometry,tangent}=D^\dagger D\) is not (K_0). The recovered QAT script explicitly reports their relative Frobenius and spectral differences.
- (K_{\rm fibre}\) acts on vertex spinors, not on tangent edge coordinates.
- A radial edge component or vertex scalar (\tau) is not a time coordinate or a torsion scalar without a further geometric derivation.
- A tiny commutator for an operator extended by a projected polar factor on \(\ker K_0\) is structural and does not prove that the proposed geometric feature map equals the kernel.

## 4A. Archived quantitative results recovered

The archived QAT JSON records the following values:

| Check | Archived value | Interpretation |
|---|---:|---|
| (\operatorname{rank}J) | 4 | Four independent constraints |
| (\|JQ\|_F) | (1.23855\times10^{-14}) | Archived tangent frame lies in the constraint kernel |
| (\|Q^TQ-I\|_F) | (1.31455\times10^{-14}) | Tangent frame is orthonormal |
| (\|N^TN-I\|_F) | (2.45327\times10^{-18}) | Labelled normal frame is orthonormal |
| (\|Q^TN\|_F) | (1.05471\times10^{-15}) | Tangent and normal spaces are orthogonal |
| (\|QQ^T+NN^T-I\|_F) | (8.97758\times10^{-15}) | Tangent/normal projectors resolve the identity |
| A13/A14 tangent projector difference | 0 | Exact agreement in the archived arrays |
| SEA/A14 tangent projector difference | 0 | Exact agreement in the archived arrays |
| (SU(2)) unitarity max residual | (3.20960\times10^{-16}) | Archived link matrices are unitary |
| (SO(3)) orthogonality max residual | (1.17162\times10^{-15}) | Archived rotations are orthogonal |
| (SO(3)) determinant max residual | (7.77156\times10^{-16}) | Archived rotations have determinant +1 |
| Coframe reconstruction Frobenius residual | 0 | Archived coframe matches its formula exactly at stored precision |
| Coframe unit-norm max residual | (1.11022\times10^{-16}) | Normalization verified |
| (\|K_{geometry}-D^TD\|_F) | 0 | Exact Gram construction |
| (\lambda(K_{geometry})) range | [1.00898634, 12] | Positive definite on archived tangent coordinates |
| (\lambda(K_0)) range | [(9.94038\times10^{-13}), 12.8] | (K_0) is near-semidefinite |
| Relative (\|K_{geometry}-K_0\|_F/\|K_0\|_F) | 0.844971 | They are materially different operators |
| Sorted spectral difference (L^2) | 38.08997 | Their spectra are not interchangeable |
| (K_{fibre}) Hermiticity residual | 0 | Archived spinor-fibre operator is Hermitian |
| (\lambda(K_{fibre})) range | [0.58610364, 11.41389636] | Positive fibre spectrum |
| (B_1B_2) Frobenius residual | 0 | Q6 incidence chain identity |
| (\operatorname{rank}B_1,\operatorname{rank}B_2) | 63, 129 | Consistent with the 64-vertex/192-edge/240-plaquette chain |
| Holonomy sheets | 240 each | Both conjugate sheets cover the 240 plaquettes |
| Sheet conjugation residual | 0 | Second holonomy sheet is the complex conjugate of the first |

Additional radial-channel diagnostics: RMS fourth coframe component (0.27599575), maximum absolute value (0.68186731); (\tau\) lies in ([0.07834387,0.45027537]) and its correlation with vertex radius is (-0.89115925). This is evidence for a nontrivial radial geometric channel, not for physical time.

The key correction to the earlier handoff is that the A14 rank and residuals are already available in the archived JSON. They should not be described as awaiting discovery. What remains unavailable is the raw-array rerun and hash-level provenance of those arrays.

## 5. Epistemic classification

| Statement | Classification | Reason |
|---|---|---|
| A13 link coframe formula and its dimensions | Definition recovered; archived numerical checks pass | A13 source and QAT JSON give exact reconstruction residual 0 and unit-norm residual (1.11\times10^{-16}) |
| A14 translation + scale constraint Jacobian | Analytically reconstructed; archived numerical checks pass | rank 4; (\|JQ\|_F=1.24\times10^{-14}); projector complement (8.98\times10^{-15}) |
| (\dim\ker J=188) | Conditional on rank (J=4) | A14 checks rank from the original (X) |
| (E_i=\operatorname{principal\_sqrt}(C_i/c_0)) | Historical construction record | Transcript recovered; (C_i) and binary (E) unavailable |
| (64\times4\times4) Lorentzian tetrad | Candidate/ansatz only | Temporal block was not derived |
| TEGR/Cartan torsion from that tetrad | Open | No fully specified tetrad field and spin connection |
| QAT acronym expansion | Open | No expansion in the recovered source |
| (D^\dagger D\) identities and dimensional distinctions | Exact algebraic definitions | Directly specified by the recovered audit script |
| Physical interpretation as spacetime dynamics | Open | No continuum limit, units, action, or calibrated couplings established here |

## 6. Reproduction and closure checklist

To upgrade the archived result to a fully reproducible raw-data rerun, restore the exact bundle inputs:

- `RGS_PSU_all_matrices.npz` (or the archived `RGS_PSU_all_matrices (1).npz`);
- `psu_fibre_connection_matrices.npz`;
- `sea_operators.npz`;
- `A14_jacobian_matrices.npz`;
- `Q6_exact_incidence_and_H241.npz`;
- original (C_i), (E_i), and tetrad arrays, with hashes and provenance.

Then run A13, A14, and QAT in that order, preserving the original arrays. Report both absolute and relative residuals, numerical ranks with thresholds, eigenvalue spectra, array hashes, and the exact source file for each input. Only after that should one attempt a tetrad-level audit. The tetrad audit must define the base coordinates, coframe/tetrad conventions, metric signature, spin connection, and discrete derivative before evaluating torsion or curvature.

**No physical TEGR, QAT unification, or 3+1 spacetime theorem is asserted by this recovery note.**
