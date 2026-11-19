# A15 — Exact RGS constraint-manifold geometry from A13/A14

**Classification:** numerical verification of an exact finite-dimensional geometric identification.  
**Scope:** intrinsic Riemannian geometry of the archived constraint manifold. This is **not** a spacetime tetrad or a spacetime spin connection.

## 1. Source data

The A13 archive `RGS_PSU_all_matrices.npz` contains

- `X_Oh_reconstructed` with shape (64\times3);
- `Q_tangent` with shape (192\times188).

The A14 Jacobian construction defines four constraints on (X\in\mathbb R^{64\times3}):

\[
F(X)=\begin{pmatrix}
\sum_i x_i\\
\sum_i y_i\\
\sum_i z_i\\
\frac12(\sum_i\|X_i\|^2-240)
\end{pmatrix}=0.
\]

The Jacobian with respect to (x=\operatorname{vec}(X)\in\mathbb R^{192}) is

\[
J(X)=\begin{pmatrix}
1&0&0&1&0&0&\cdots\\
0&1&0&0&1&0&\cdots\\
0&0&1&0&0&1&\cdots\\
x_1&y_1&z_1&\cdots&x_{64}&y_{64}&z_{64}
\end{pmatrix}.
\]

The first three constraints define the 189-dimensional linear subspace of zero-centroid configurations. The last constraint fixes the radius. Since the archived configuration has \(\|x\|^2=240\), the full constraint set is

\[
\boxed{\mathcal M=\{x:\sum_i X_i=0,\ \|x\|^2=240\}
\cong S^{188}(\sqrt{240}).}
\]

This is an exact identification, not a claim that the 188 tangent directions are four spacetime coordinates.

## 2. Canonical normal frame and tangent projector

Let (t_1,t_2,t_3\in\mathbb R^{192}) be the three normalized translation vectors. Each has value (1/8) in its corresponding Cartesian coordinate at all 64 sites and zero elsewhere. Let

\[
n(x)=\frac{x}{\sqrt{240}}.
\]

The four vectors (t_1,t_2,t_3,n(x)) form an orthonormal normal frame along the sphere. Hence

\[
P_x=I_{192}-\sum_{a=1}^3t_at_a^T-n(x)n(x)^T.
\]

The archived (Q\) is an orthonormal basis of the tangent space, so numerically

\[
QQ^T=P_x,\qquad JQ=0.
\]

The A15 audit independently checks these identities and the associated projector residuals.

## 3. The induced Levi-Civita connection

For tangent vector fields (V,W\) on \(\mathcal M\), the Levi-Civita connection of the induced Euclidean metric is

\[
\boxed{\nabla_VW=P_x(D_VW).}
\]

With the outward radial normal (n=x/r), (r=\sqrt{240}), the second fundamental form is

\[
\mathrm{II}(V,W)=-\frac{\langle V,W\rangle}{r}\,n.
\]

Equivalently, with (S_n(V)=-D_Vn), the radial shape operator is

\[
S_n=-\frac1r I.
\]

The three translation normals are constant. Also (D_Vn=V/r) is tangent, so the normal connection coefficients in the global frame ((t_1,t_2,t_3,n)) vanish. This is the normal connection of the embedded constraint sphere; it is not a Lorentzian spin connection.

## 4. Curvature

For the 188-dimensional sphere of radius squared 240, the induced Riemannian metric has constant sectional curvature

\[
K=\frac1{240}.
\]

Its Ricci tensor and scalar curvature are

\[
\operatorname{Ric}=\frac{187}{240}g,
\qquad
\operatorname{Scal}=\frac{188\cdot187}{240}
=146.4833333333333.
\]

These are intrinsic curvature invariants of the finite-dimensional constraint manifold.

## 5. Numerical verification

Run:

```bash
python scripts/audit_rgs_constraint_sphere_geometry.py \
  path/to/RGS_PSU_all_matrices.npz \
  --output reports/RGS_A15_CONSTRAINT_SPHERE_GEOMETRY_2026-11-19.json
```

The audit checks:

- centering and fixed radius;
- rank (J=4);
- (JQ=0);
- (Q^TQ=I_{188});
- symmetry and idempotence of (QQ^T);
- orthonormality of the canonical normal frame;
- equality of (QQ^T) and (P_x).

All tests use a (10^{-10}) tolerance, except the centering/radius checks as specified in the JSON report.

## 6. Boundary of the result

**PASS:** the A13/A14 data determine the exact Riemannian constraint manifold and its induced Levi-Civita connection in projection form.

**NOT ESTABLISHED:** a coordinate-dependent invertible (4\times4) coframe, a Lorentzian metric, a (Spin(3,1)) connection, a timelike field/3+1 reduction, or an identification of the archived (SU(2)) links with holonomies of this induced connection.

Therefore A15 advances the genuine geometry available in the archives without manufacturing a four-dimensional spacetime tetrad.
