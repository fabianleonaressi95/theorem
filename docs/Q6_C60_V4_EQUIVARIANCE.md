# Q6–C60 restriction to the Klein four subgroup V4

**Date:** 2026-11-26  
**Classification:** subgroup-restriction theorem from the archived character data, plus a new numerical audit whose execution is delegated to GitHub Actions.

## 1. Why V4 is the next test

The full tested \(A_4\) representations are inequivalent: their characters differ on the eight order-three elements. However, the normal Klein-four subgroup
\[
V_4=\{e,a,b,c\}\cong C_2\times C_2
\]
contains only the identity and the three order-two elements.

The archived \(A_4\) character data give:
\[
\begin{array}{c|rrrr}
 &e&a&b&c\\ \hline
Q6&64&0&0&0\\
\bigoplus_f E_f&64&0&0&0
\end{array}
\]
where \(E_f=n_f^\perp\) is the tangent plane of an actual C60 face.

Thus the restrictions have equal characters on \(V_4\). Since every irreducible real representation of \(V_4\) is one-dimensional, the multiplicity of each of its four real characters is
\[
m_\chi=\frac14\sum_{g\in V_4}\chi_{\rm rep}(g)\chi(g)=16.
\]
Consequently the two 64-dimensional real representations are isomorphic after restriction to \(V_4\).

This is a genuine positive representation-theoretic result, but it does **not** reverse the obstruction on \(A_4\) or \(T_h\).

## 2. What the numerical audit must establish

The script **scripts/audit_q6_c60_v4_equivariance.py** performs the following independent checks against **data/RGS_PSU_all_matrices.npz**:

1. Reconstruct the coordinate \(A_4\) action on the 64 Q6 points and extract its \(V_4\).
2. Reconstruct an \(A_4\subset I\) from the icosahedral rotation group and extract its \(V_4\) acting on the 32 actual C60 faces and their tangent planes.
3. Fix an explicit abstract \(V_4\)-isomorphism: identity to identity and the three nonidentity elements paired in lexicographic rounded-matrix order in the respective Cartesian frames. Every bijection of the three nonidentity elements is a group isomorphism; this convention is deterministic, not geometrically canonical.
4. Test whether all four Q6 transformations preserve **Q6_adjacency** exactly.
5. Construct the four character projectors on both 64-dimensional spaces, compare their multiplicities, and assemble an explicit orthogonal \(64\times64\) intertwiner.
6. Independently restrict the reconstructed 188D tangent action and test covariance of **K0**, **R_geo_tangent**, **P_G**, and **T_transport** on this \(V_4\).

The script writes a JSON report and an NPZ containing the explicit intertwiner and representation matrices. GitHub Actions uploads these as a run artifact.

## 3. Interpretation rules

The outcomes must be kept separate:

- **Representation equivalence:** an orthogonal intertwiner exists for the two 64D \(V_4\)-representations.
- **Q6 graph symmetry:** all three nonidentity Q6 transformations must preserve adjacency. If this fails, the equivalence concerns the coordinate-induced point action, not an action by graph automorphisms.
- **188D operator covariance:** each archived operator must be tested separately. The existence of the 64D intertwiner says nothing by itself about covariance of a 188D operator.
- **Geometric canonicity:** the deterministic abstract group isomorphism and the projector-built intertwiner are not a canonical assignment of Q6 states to named C60 faces.
- **Spectral comparison:** remains unauthorized unless an operator map is independently defined and verified.

## 4. Reproduction

    python scripts/audit_q6_c60_v4_equivariance.py data/RGS_PSU_all_matrices.npz --out audits/Q6_C60_V4_equivariance.json --matrices artifacts/Q6_C60_V4_intertwiner.npz

The workflow **.github/workflows/q6-c60-v4-equivariance.yml** runs this command and uploads both outputs.

## 5. Numerical results (GitHub Actions run 5)

The workflow completed successfully on 2026-11-26. The generated JSON and NPZ matrix bundle were uploaded as the artifact **q6-c60-v4-equivariance**.

- Q6 and C60 V4 characters: \((64,0,0,0)\) on both sides.
- Each of the four real V4 irreducibles occurs with multiplicity 16 on both sides.
- All four Q6 V4 transformations preserve Q6 adjacency exactly; all four adjacency residuals are zero.
- The explicit orthogonal intertwiner is \(64\times64\). Its orthogonality residual is \(8.04\times10^{-15}\), and its maximum per-element intertwining residual is \(6.63\times10^{-15}\).
- The reconstructed 188D tangent subspace is invariant under all four elements; maximum projector residual \(1.19\times10^{-14}\), maximum induced-orthogonality residual \(3.50\times10^{-14}\).

Operator covariance on the 188D space is selective:

| Operator | Elements preserved (of 4) | Maximum relative covariance residual |
|---|---:|---:|
| \(K_0\) | 1 | 0.9897387721 |
| \(R_{\rm geo,tangent}\) | 4 | \(2.64\times10^{-15}\) |
| \(P_G\) | 1 | 1.1530236121 |
| \(T_{\rm transport}\) | 1 | 1.3618898128 |

Therefore the \(V_4\) equivalence is a verified representation-level result and all three nonidentity elements are genuine Q6 graph symmetries. However, among the archived 188D operators, only \(R_{\rm geo,tangent}\) is \(V_4\)-covariant. The \(K_0\), \(P_G\), and \(T_{\rm transport}\) spectra cannot be interpreted as \(V_4\)-symmetry-resolved using this action.

Workflow run: https://github.com/fabianleonaressi95/theorem/actions/runs/45868725620

## 6. Scientific status

The equality of the four \(V_4\) characters and the multiplicities \(16,16,16,16\) follow from the previously archived \(A_4\) character data. The graph-automorphism, explicit-matrix, and 188D operator checks are now numerically verified. No C60 spectrum is asserted or compared.

The equality of the four \(V_4\) characters and the multiplicities \(16,16,16,16\) follow from the previously archived \(A_4\) character data. The graph-automorphism, explicit-matrix, and 188D operator checks are new numerical tests and must be read from the generated workflow report. No C60 spectrum is asserted or compared here.
