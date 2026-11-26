# A16 — RGS/Q6 spatial bundle and SO(2) reduction

**Classification:** exact finite-graph construction, with numerical archive checks.  
**Not claimed:** a 4D Lorentzian spacetime, a continuum Levi-Civita spin connection, or a continuum limit.

## 1. Three-dimensional base geometry

The archived vertex map is (X:Q_6\to\mathbb R^3), with 64 vertices and centered affine rank 3. The 192 edge displacements span the same three-dimensional spatial vector space. This is a genuine embedded discrete spatial geometry.

The QLG augmented edge coframe is
\[
e_{gh}=\frac{(X_h-X_g,\ |X_h|-|X_g|)}
{\sqrt{\|X_h-X_g\|^2+(|X_h|-|X_g|)^2}}\in\mathbb R^4.
\]
Its fourth component is not an independent coordinate: it is the finite increment of the scalar function (r(X)=\|X\|).

Indeed, the map
\[
F:\mathbb R^3\setminus\{0\}\to\mathbb R^4,
\qquad F(X)=(X,\|X\|)
\]
has differential
\[
DF_X(v)=(v,n\cdot v),\qquad n=X/\|X\|,
\]
and induced metric
\[
DF_X^TDF_X=I_3+n n^T.
\]
Its eigenvalues are (1,1,2), so (DF_X) has rank exactly 3. Thus the augmented 4-component coframe describes a 3D graph hypersurface in (\mathbb R^4), not a four-dimensional spacetime coframe. Its natural spatial projection is simply (X_h-X_g\in\mathbb R^3).

## 2. The archived SO(3) links define a radial-preserving discrete connection

The recovered link construction uses
\[
n_g=\frac{X_g}{\|X_g\|},
\qquad R_{gh}\in SO(3),
\qquad R_{gh}n_g=n_h.
\]
The last identity is the defining transport law of the minimal rotation used in the archive. Consequently
\[
P_g=I_3-n_gn_g^T,
\qquad
R_{gh}P_gR_{gh}^T=P_h.
\]
The rank-2 planes (n_g^\perp\) are therefore transported into one another. The fibre splits orthogonally:
\[
\mathbb R^3=\operatorname{span}(n_g)\oplus n_g^\perp.
\]
The selected unit radial section is parallel, and the structure group reduces from (SO(3)) to the stabilizer (SO(2)) acting on the transverse planes.

For every closed plaquette based at (g), its holonomy (H_p\) fixes (n_g). Hence (H_p\in SO(2)_g\). This is a real, finite-graph reduction to a rank-2 transverse bundle plus a parallel radial line.

## 3. SU(2) lift

The archived (U_{gh}\in SU(2)) is the spin lift of (R_{gh}\). With
\[
\sigma(n_g)=n_g^i\sigma_i,
\]
the adjoint compatibility gives
\[
U_{gh}\sigma(n_g)U_{gh}^\dagger=\sigma(n_h).
\]
Therefore every closed-loop spin holonomy (W_p\) commutes with (\sigma(n_g)\):
\[
[W_p,\sigma(n_g)]=0.
\]
Its plaquette stabilizer is the corresponding (U(1)\subset SU(2)\). This is the spin lift of the (SO(2)\) reduction, not evidence for a spacetime (Spin(3,1)\) connection.

## 4. Critical distinction from the A14 constraint-sphere normal

A14 defines a normal vector in the 192-dimensional configuration space:
\[
N_r=\frac{\operatorname{vec}(X)}{\|\operatorname{vec}(X)\|}.
\]
The link construction instead uses 64 separately normalized vectors (n_g=X_g/\|X_g\|). They are not the same field unless all 64 radii are equal. The archived radii are not constant. The SO(3) links transport (n_g\), not the 192-dimensional A14 radial normal (N_r\).

Likewise, the 188D A14 tangent projector and the edgewise rank-3 vector-bundle connection act on different spaces. The graph connection cannot be called the Levi-Civita connection of (S^{188}(\sqrt{240})\) merely because both originate from the same (X\) data.

## 5. Reproducible audit

Run:
\`\`\`bash
python scripts/audit_rgs_q6_spatial_so2_reduction.py \
  path/to/psu_fibre_connection_matrices.npz \
  --output reports/RGS_A16_SPATIAL_SO2_REDUCTION_2026-11-19.json
\`\`\`

The script checks:
- rank-3 spatial embedding and edge displacements;
- (SO(3)) orthogonality, determinant and (R_{gh}n_g=n_h);
- transport of the transverse projectors;
- (SU(2)\to SO(3)) adjoint compatibility;
- all 240 plaquette holonomies fixing the radial direction;
- commutation of spin holonomies with (\sigma(n_g)\);
- the distinction between vertexwise unit radial vectors and the A14 fixed-radius normal.

## 6. Status

**PASS by construction, subject to numerical audit:** a rank-3 Euclidean discrete spatial bundle with (SO(3)\to SO(2)) and (SU(2)\to U(1)) plaquette stabilizers.

**NOT ESTABLISHED:** identification with the A14 (188\)-dimensional induced Levi-Civita connection, a continuum triad/spin connection, a Lorentzian time direction, or a continuum/refinement limit.

The geometrically justified conclusion is therefore: **the archive supports a 3D discrete spatial embedding and a radial/transverse reduction of its internal transport bundle. It does not yet provide a 3D continuum manifold with a derived spin connection.**
