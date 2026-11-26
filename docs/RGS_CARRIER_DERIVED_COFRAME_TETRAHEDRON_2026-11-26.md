# Carrier-derived coframe and torsion on an RGS tetrahedron — 2026-11-26

## Result and classification

This note constructs edge coframe data from the hash-checked 64-site RGS/O_h coordinate seed, rather than assigning independent edge vectors. It tests a four-vertex tetrahedral cell selected from that carrier.

**Classification:** explicit finite geometric construction; numerical verification of frame covariance and Euclidean rotation invariance. The tetrahedron is a selected geometric fixture, **not asserted to be a Q6 subcomplex**. No continuum Cartan limit or torsion Bianchi identity is claimed.

## 1. Source carrier

The source is \`src/rgs_seed_64_reconstruction.py\`, which reconstructs the 64 coordinates and checks the canonical float64 SHA-256:

\`6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf\`.

The selected carrier indices are \`(0, 8, 32, 56)\`. Their coordinates, radii and oriented volume are recorded by the audit JSON. The tetrahedron has nonzero volume, so it is not a degenerate four-point sample.

The origin is geometrically fixed by the RGS zero-centroid constraint. The radial directions are
\[
n_i=X_i/\|X_i\|.
\]

## 2. Radial frames and edge transport

At each selected vertex choose a deterministic oriented frame
\[
F_i=(u_i,v_i,n_i)\in SO(3),
\]
where \(u_i\) is obtained by projecting a fixed reference axis orthogonally to \(n_i\), and \(v_i=n_i\times u_i\). This is only a local frame choice; the audit separately tests arbitrary changes of these frames.

Let \(R^g_{ij}\in SO(3)\) be the shortest ambient rotation carrying \(n_i\) to \(n_j\). The selected edges have no antipodal radial pair, so this minimal rotation is unique. Its local-frame representation is
\[
R_{ij}=F_j^T R^g_{ij}F_i.
\]

## 3. Symmetric coframe derived from the carrier chord

Write \(\Delta X_{ij}=X_j-X_i\). Its source- and target-frame components are \(F_i^T\Delta X_{ij}\) and \(F_j^T\Delta X_{ij}\). Pull the target component back to the source fibre with \(R_{ij}^{-1}\), then average:
\[
\boxed{
E_{ij}=\frac12\left(F_i^T\Delta X_{ij}
+R_{ij}^{-1}F_j^T\Delta X_{ij}\right).
}
\]
This construction is symmetric under reversal of the oriented edge. Direct substitution gives
\[
E_{ji}=-R_{ij}E_{ij}.
\]
It is also gauge covariant under independent changes of the local frames:
\[
R'_{ij}=S_jR_{ij}S_i^{-1},\qquad E'_{ij}=S_iE_{ij}.
\]

Because this is an average of two vectors of equal norm, it obeys
\[
\|E_{ij}\|\leq\|\Delta X_{ij}\|.
\]
The ratio \(\|E_{ij}\|/\|\Delta X_{ij}\|\) records the alignment of the source and transported target chord components. It is not required to equal one.

The radial increment
\[
\rho_{ij}=\|X_j\|-\|X_i\|
\]
is also recorded as a scalar diagnostic. It is **not appended as a fourth component** to the spatial coframe: the three components of \(E_{ij}\) already describe the spatial chord in a local orthonormal frame. The older augmented object \((X_j-X_i,\rho_{ij})\in\mathbb R^4\) is a separate feature/cochain and is not, without further structure, an invertible spacetime tetrad.

## 4. Face torsion

For an oriented face \((i,j,k)\), define
\[
\boxed{
\mathcal T_{ijk}
=E_{ij}+R_{ij}^{-1}E_{jk}
 +(R_{jk}R_{ij})^{-1}E_{ki}.
}
\]
Every term is transported into the fibre at \(i\). Under independent local frame rotations \(S_i\in SO(3)\),
\[
\mathcal T'_{ijk}=S_i\mathcal T_{ijk}.
\]
The audit tests this covariance on 1,000 seeded independent frame changes, as well as invariance under common ambient \(SO(3)\) rotations and direct edge-reversal consistency.

## 5. Numerical result

Run from the repository root:
\`\`\`bash
python scripts/audit_rgs_carrier_coframe_tetrahedron.py
\`\`\`

The script writes \`audits/RGS_CARRIER_DERIVED_COFRAME_TETRAHEDRON_2026-11-26.json\`.

The four face-torsion norms for the selected tetrahedron are approximately:
- \((0,1,2)\): \(0.3899601615\)
- \((0,1,3)\): \(0.1603420467\)
- \((0,2,3)\): \(0.2466332511\)
- \((1,2,3)\): \(0.1191567159\)

The independently seeded 1,000-sample checks give maximum residuals:
- frame-gauge covariance: \(2.47\times10^{-15}\);
- common ambient \(SO(3)\) invariance: \(3.38\times10^{-15}\);
- direct reverse-edge consistency: \(7.04\times10^{-16}\);
- coframe norm upper-bound excess: zero to working precision.

These are implementation checks of a finite construction, not a proof of a continuum limit. The numerical loop was independently reproduced locally against the exact hash-checked coordinates; the checked-in script was inspected but was not run from a Git checkout in this session.

## 6. Relation to archived PSU transports and open work

This fixture uses the radial shortest-rotation connection defined explicitly above. It does **not** silently substitute the archived \`R_SO3\` / \`U_SU2\` arrays from the A13 bundle: their edge ordering and vertex-frame convention must first be aligned with the selected carrier indices. The archived transport audit remains a separate validated result.

Next gates:
1. align the complete Q6 edge list and archived \(SO(3)/SU(2)\) links with the hash-checked RGS coordinate ordering;
2. compare the radial shortest-rotation connection with the archived PSU connection, including edge reversal and gauge conversion;
3. establish whether the selected tetrahedral cell is present in the recovered 3-complex, rather than treating a geometric tetrahedron as an incidence cell;
4. define a consistent simplicial cochain differential and test refinement;
5. prove convergence to \(D_\omega e\) before identifying the face quantity with continuum Cartan torsion;
6. only then investigate a deWit–Nye or Burgers interpretation.

**Not claimed:** Q6 subcomplex membership, continuum Cartan torsion, a discrete torsion Bianchi identity, deWit/Nye dislocation density, Burgers vector, or a spacetime tetrad.
