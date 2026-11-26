# QAT–RGS–Q6: Kirchhoff, fluid/gauge sectors and compatibility audit

**Status:** integration specification and read-only audit harness. This does not assert that the full physical model has passed.

## 1. Reuse the existing sector decomposition

This audit reuses existing records; it does not recreate the cube, QAT construction, RGS coframe or quaternionic representation.

### Q6 and Kirchhoff network (T099)

A hexagram is the ordered pair of lower and upper trigrams
\[
H=(\ell,u),\qquad \ell,u\in\{0,1\}^3,
\]
with the established index
\[
\iota(\ell,u)=\sum_{r=0}^2 2^r\ell_r+
8\sum_{r=0}^2 2^r u_r.
\]
The 64 vertices form \(Q_6=Q_3^-\square Q_3^+\), with 192 edges and 240 square faces. The 192 edges split into 96 lower-trigram flips (bits 0–2) and 96 upper-trigram flips (bits 3–5). The weighted Kirchhoff model in T099 is
\[
L(g_-,g_+)=g_-(I_8\otimes L_3)+g_+(L_3\otimes I_8),
\qquad LV=J,\quad \mathbf1^TJ=0.
\]
The trigram labels remain:
000 Kun, 001 Gen, 010 Kan, 011 Xun,
100 Zhen, 101 Li, 110 Dui, 111 Qian.
These are cube labels, not assignments of vertices to physical fluid or gauge sectors.

### Left fluid / right gauge (T077, T089, T090)

Keep the established convention:
- **Left sector: fluid**, with density \(\rho\), velocity \(v\), pressure \(p\), and Bernoulli scalar \(B_L\).
- **Right sector: gauge**, with internal bundle \(E_R\), connection \(A\), section \(\Psi\), and covariant derivative \(D_A\Psi\).

The sectors share geometric cell/barycentre data and tangent anisotropy, but their fields and constitutive equations remain distinct. T089 supplies the common variational model; T090 supplies a Whitney/cochain discretization and exact cochain gauge identities. Neither sector is automatically the polariton momentum current.

The Kirchhoff conductances \(g_-,g_+\) are network parameters. They are not silently identified with the continuum gauge coupling \(g\), fluid viscosity, or polariton inter-sheet energy \(J\).

## 2. Quaternionic transport and fixed convention

Reuse T063, T064 and T118. A unit quaternion
\[
q=w+x\mathbf i+y\mathbf j+z\mathbf k,\qquad
w^2+x^2+y^2+z^2=1
\]
maps to
\[
U(q)=\begin{pmatrix}
w-iz&-y-ix\\ y-ix&w+iz
\end{pmatrix}\in SU(2).
\]
The four real quaternion coordinates are not the four geometric coframe axes. Conjugation \(q\mathbf vq^{-1}\) rotates the three-dimensional imaginary subspace and realizes \(SU(2)\to SO(3)\).

The existing QAT four-current notation is
\[
\mathcal J=c\rho+j_x\mathbf i+j_y\mathbf j+j_z\mathbf k.
\]
Quaternionic conjugation leaves the scalar component invariant and rotates the spatial current. This is a transformation law for the QAT current, not an identification of that current with the gauge connection. The SU(2) link variables separately encode internal parallel transport.

For graph links this audit follows T118:
\[
U_{gh}\in SU(2),\quad U_{hg}=U_{gh}^{\dagger},\quad
U^G_{gh}=G_hU_{gh}G_g^\dagger,
\]
\[
(D_U\Psi)_{gh}=\Psi_h-U_{gh}\Psi_g.
\]
Then
\[
(D_{U^G}\Psi^G)_{gh}=G_h(D_U\Psi)_{gh}.
\]
This convention is internally consistent for column spinors and left multiplication. Do not mix it with a reversed-link convention without changing both the covariant difference and transporter ordering. For a path \(p=(v_0,\ldots,v_n)\), T118 uses
\[
P_U(p)=U_{v_{n-1}v_n}\cdots U_{v_0v_1},\quad
P_{U^G}(p)=G_{v_n}P_U(p)G_{v_0}^{\dagger}.
\]

## 3. Geometry: no dimension inference from array shape

The tracked RGS coordinate source X_Oh_reconstructed.csv contains 64 points in \(\mathbb R^3\). The recovered RGS tetrad record has a four-slot internal coframe convention, but this does not prove four physical coordinate directions. The fourth slot is treated as radial/auxiliary unless an explicit coordinate map, metric and geometric interpretation are supplied.

The audit records exact shape, dtype and SHA-256 for each available source array and for the NPZ container. It does not convert an internal array index into a coordinate index. Measure and edge weights must be supplied explicitly and checked for positivity/nonnegativity.

## 4. Read-only NPZ input contract

The script scripts/audit_qat_rgs_kirchhoff_fluid_gauge.py accepts --bundle PATH. It opens the archive with allow_pickle=False and never modifies it. Recognized keys:

| Key | Expected shape | Meaning |
|---|---:|---|
| edges | (192,3) | oriented endpoints plus flipped bit index |
| B1 | (64,192) | vertex-edge incidence |
| B2 | (192,240) | edge-face incidence |
| U_SU2 or U_plus | (192,2,2) | SU(2) links |
| U_minus | (192,2,2) | second-sheet links, if separately stored |
| tetrad / vierbein | source-dependent | stored coframe; shape only is reported |
| plaquette_vertices | (240,4) | ordered vertices of square boundaries, if archived |
| L_RGS | (64,64) | independently stored scalar RGS graph Laplacian, if archived |
| K_QAT / K_tau / qat_kernel | square | archived QAT kernel/operator; checked for Hermiticity and positivity |
| M / measure / site_measure | source-dependent | positive site measure |
| edge_weights | (192,) | nonnegative edge weights |
| inter_sheet_J | (2N,2N) | explicit inter-sheet coupling block |
| H_two_sheet | (4N,4N) | assembled two-sheet operator |
| H_plus_block, H_minus_block | (2N,2N) | diagonal sheet operators |
| H_plus_chirality, H_minus_chirality | (2N,2N) | independently assembled operators |
| mirror_site_perm | (N,) | explicit mirror site permutation |
| mirror_spin_matrix | (2,2) | explicit unitary spin lift of the mirror, if present |
| mirror_spin_identity | scalar bool | explicit declaration that the mirror acts trivially on spin |
| mirror_antiunitary | scalar bool | explicit conjugation flag; never inferred |

The recovered Library archive `RGS_PSU_all_matrices(1).npz` was located and independently audited on 2026-11-19. It contains Q6 states, adjacency and Laplacian, but no SU(2) link arrays or full two-sheet polariton blocks. The exact Kirchhoff/incidence results are recorded in `reports/Q6_KIRCHHOFF_RECOVERED_SOURCE_AUDIT_2026-11-19.md`. The script can derive the combinatorial edge/face incidence from those archived states and adjacency without reconstructing the RGS geometry. The A13/A14 archives remain only partially recovered for this audit; missing physical-sector arrays stay NOT TESTED.
The source inventory says original A13/A14 and Q6 NPZ bundles were recovered in the user's source archive but are not all present as tracked binary files in this repository snapshot. Therefore the default run reports bundle-dependent checks as NOT TESTED; it does not fabricate replacement arrays.

## 5. Audit logic

The script reports PASS, FAIL or NOT TESTED for:
1. provenance/hash and dimensions of tracked coordinate input;
2. Q6 edge and incidence dimensions, plus exact \(B_1B_2=0\);
3. 96+96 lower/upper Kirchhoff edge split under T099 bit ordering;
4. QAT kernel Hermiticity/positivity when the archived kernel is supplied;
5. coframe shape without interpreting four internal slots as four coordinates;
5. positivity of supplied site measure and nonnegative edge weights;
6. SU(2) unitarity and determinant;
7. random local gauge covariance of the covariant Laplacian;
8. Hermiticity and nonnegative spectrum of \(D_U^\dagger W D_U\);
9. plaquette holonomy conjugation and Wilson-trace invariance;
10. the \(U=I\) comparison with a separately supplied RGS Laplacian;
11. conjugate two-sheet link relation, only if both sheet arrays are present;
12. exact (J=0) block-diagonal limit, only with all two-sheet blocks supplied;
13. specular intertwining with an explicit site permutation, distinguishing unitary from antiunitary maps.

For the gauge-covariant Laplacian, the implementation forms \(D_U\) from supplied edges and links and tests
\[
H_U=D_U^\dagger W D_U,\qquad
H_{U^G}=G_{\rm site}H_UG_{\rm site}^\dagger.
\]
This tests finite-dimensional algebra with T118 conventions. The separate limit \(U=I\) can be compared with a supplied RGS graph Laplacian only when that source matrix is present; the script does not assert that the covariant Laplacian is automatically the RGS Laplacian.

A unitary mirror relation is
\[
H_{-\chi}=P H_{+\chi}P^\dagger.
\]
An explicitly antiunitary relation is tested as
\[
H_{-\chi}=P\overline{H_{+\chi}}P^\dagger.
\]
The site permutation, spin action (or explicit identity declaration) and antiunitary flag must be source data. If absent, the result is NOT TESTED, not a guessed parity. The inter-sheet zero-coupling check is reported as NOT TESTED until the full two-sheet operator, both diagonal blocks and the coupling block are supplied; the mere presence of a coupling matrix is not a successful decoupling test.

## 6. Run

From the repository root:

    python scripts/audit_qat_rgs_kirchhoff_fluid_gauge.py

With an original recovered archive:

    python scripts/audit_qat_rgs_kirchhoff_fluid_gauge.py --bundle /path/to/original_RGS_Q6_bundle.npz

Optional JSON output:

    python scripts/audit_qat_rgs_kirchhoff_fluid_gauge.py --bundle /path/to/original_RGS_Q6_bundle.npz --output reports/qat_rgs_kirchhoff_fluid_gauge_audit.json

The script returns a nonzero exit code only for FAIL. Missing source objects remain NOT TESTED. A small synthetic unit test checks the T118 algebra and positivity independently of the recovered data: run pytest -q tests/test_qat_rgs_kirchhoff_fluid_gauge.py. The synthetic fixture does not stand in for the archived Q6/RGS arrays. The JSON report is a diagnostic, not a theorem certificate.

## 7. Scope and exclusions

This audit does not calculate polariton spectra, viscosity, Green–Kubo coefficients or a Keldysh response. It does not infer a physical microcavity, Lorentzian time axis, Pin structure or continuum limit. It checks only whether archived geometry, Q6/Kirchhoff incidence, two-sheet structure and SU(2) transport can be used consistently in one finite operator.

### Existing records reused
- T063: quaternionic realization of SU(2) and the double cover of SO(3).
- T064 and T118: finite-graph gauge covariance and Wilson holonomy (T118 conventions used here).
- T077: left-fluid/right-gauge sector convention and common barycentric bridge.
- T089–T090: gauge–fluid variational coupling and Whitney discretization.
- T099: Shao–Yong Q6 Kirchhoff network and trigram bit convention.
- docs/RUBINO_QAT_QUATERNIONIC_SU2_BRIDGE.md: QAT current and quaternionic/spin-connection bridge.
- data/rgs_188d/RECOVERED_SOURCE_ARTIFACTS.md: provenance and availability limits of original NPZ arrays.
