# T087 — Covariant discrete Hodge projection, curvature defect and seam-frame covariance

**Date:** 11 November 2026  
**Status:** finite-dimensional theorem, proved below. It extends T086 from globally identified ambient cochains to fields represented in local orthonormal frames. No continuum convergence claim is made.

**Dependencies:** T079, T080, T086.

## 1. Why the ordinary cochain identity must be qualified

T080 and T086 use ambient vector increments, for which all fibres are identified with \(\mathbb R^3\) and the transport is the identity. This is a flat coefficient system. For panel-local tangent frames, edge values live in different fibres. They must be transported before addition.

If the connection has curvature, the covariant vertex-to-edge map followed by the face circulation is not zero. The failure is precisely the discrete holonomy defect. Requiring it to vanish on a curved shell would erase the geometric curvature we intend to retain.

This record gives the exact finite-complex formula.

## 2. Discrete orthogonal bundle data

Let \(K\) be an oriented triangulated surface. Assign a Euclidean vector space \(E_v\simeq\mathbb R^r\) to each vertex. For every oriented edge \(i\to j\), let
\[
U_{ij}:E_i\longrightarrow E_j
\]
be an orthogonal isomorphism, with
\[
U_{ji}=U_{ij}^{-1}.
\]
The matrices are expressed in the chosen local orthonormal frames. For a vertex field \(y=(y_i)\), define the covariant edge difference, stored in the target fibre \(E_j\), by
\[
(A_Uy)_{ij}:=y_j-U_{ij}y_i.
\]
Reversing the orientation gives
\[
(A_Uy)_{ji}=-U_{ji}(A_Uy)_{ij}.
\]
Thus the edge field is an oriented bundle-valued 1-cochain with the expected transport rule.

For an oriented face \(f=(i,j,k)\), define its transported circulation in \(E_k\) by
\[
(C_Uq)_{ijk}:=
U_{jk}q_{ij}+q_{jk}+U_{ik}q_{ki},
\]
where each edge component is stored in its target fibre. The three terms now lie in \(E_k\).

## 3. Curvature-defect identity

Define the triangular holonomy defect, represented in \(E_k\), by
\[
\mathcal F_{ijk}:=U_{ik}-U_{jk}U_{ij}:E_i\to E_k.
\]
Then, for every vertex field \(y\),
\[
\boxed{
(C_UA_Uy)_{ijk}=\mathcal F_{ijk}y_i.
}
\]

**Proof.** Expand the three transported edge differences:
\[
\begin{aligned}
(C_UA_Uy)_{ijk}
={}&U_{jk}(y_j-U_{ij}y_i)
 +(y_k-U_{jk}y_j)\\
&+U_{ik}(y_i-U_{ki}y_k).
\end{aligned}
\]
The \(y_j\) terms cancel. Since \(U_{ik}U_{ki}=I_{E_k}\), the \(y_k\) terms cancel. What remains is
\[
(U_{ik}-U_{jk}U_{ij})y_i.
\]
\(\square\)

Consequently,
\[
C_UA_U=0
\quad\text{if and only if}\quad
U_{ik}=U_{jk}U_{ij}
\]
on every face (as an operator identity). This is the local flatness condition. In a non-flat connection, \(C_UA_Uy\) is the curvature/holonomy source, not zero.

For a prescribed microscopic edge field \(G\), the mismatch \(D=A_Uy-G\) therefore satisfies the exact identity
\[
\boxed{
C_UD=\mathcal F y-C_UG.
}
\]
This replaces the flat formula \(d_1D=-d_1G\). The old formula is recovered when all \(U_{ij}=I\).

## 4. Covariant Hodge minimization still works

Let \(M\) be symmetric positive definite on the direct sum of edge fibres, and define
\[
E_U(y;G)=\frac12\langle A_Uy-G,M(A_Uy-G)\rangle.
\]
Let \(A_U^*\) denote the Euclidean adjoint in the chosen orthonormal frames. Then
\[
\boxed{
A_U^*M(A_Uy_*-G)=0.
}
\]
The minimizer exists and is unique modulo \(\ker A_U\). Indeed, the Hessian is \(A_U^*MA_U\), which is positive semidefinite and has kernel exactly \(\ker A_U\); it is coercive on the orthogonal complement of that kernel.

Set \(D_*=A_Uy_*-G\). Then
\[
\langle A_Uv,MD_*\rangle=0
\quad\text{for every vertex field }v.
\]
Thus the weighted Hodge projection survives unchanged as a least-squares theorem, even though the covariant face complex is no longer a complex when curvature is present.

The kernel has a geometric meaning:
\[
\ker A_U=\{y:\ y_j=U_{ij}y_i\text{ on every edge}\},
\]
the space of discrete parallel sections. For a flat, globally trivial connection on a connected graph it consists of constant sections. For nontrivial holonomy it may be smaller or zero. Therefore the gauge quotient in the covariant problem is by \(\ker A_U\), not automatically by global translations.

The minimum is
\[
\mathcal W_U(G)=\frac12\operatorname{dist}_M
\bigl(G,\operatorname{im}A_U\bigr)^2.
\]
With
\[
L_U=A_U^*MA_U,
\]
the Moore–Penrose representation is
\[
y_*=L_U^\dagger A_U^*MG,\qquad
P_U=I-A_UL_U^\dagger A_U^*M,
\]
\[
D_*=-P_UG,\qquad
\mathcal W_U(G)=\frac12\langle G,MP_UG\rangle.
\]
Here \(P_U^2=P_U\), \(P_U^*M=MP_U\), while \(MP_U\) is the symmetric positive-semidefinite energy operator, not generally an idempotent projector.

## 5. Seam transitions are coordinate-covariant

Let a physical seam have minus and plus panel frames \(E^-\) and \(E^+\). Let
\[
R^{-+}:E^-\to E^+
\]
be the orthogonal transition map, and let \(G^-,G^+\) be the two seam traces expressed in their respective frames. Define
\[
J:=G^+-R^{-+}G^-.
\]
Under independent orthogonal changes of panel frames \(S^-\) and \(S^+\),
\[
G'^\pm=S^\pm G^\pm,\qquad
R'^{-+}=S^+R^{-+}(S^-)^{-1}.
\]
It follows exactly that
\[
J'=S^+J,\qquad |J'|^2=|J|^2.
\]
Therefore
\[
E_{\rm seam}=\frac12\sum_{e\in\mathcal S}\eta_e|J_e|^2
\]
is invariant under panel-frame changes, provided \(\eta_e\) is a scalar seam weight (or is transformed as a quadratic form if anisotropic).

This proves coordinate covariance of the proposed seam observable. It does **not** derive the weights \(\eta_e\), nor does it identify this quadratic penalty with Morandotti's continuum interfacial density.

## 6. Three distinct sources in the shell balance

The covariant mismatch identity
\[
C_UD=\mathcal F y-C_UG
\]
and the seam jump \(J\) separate three mathematically different quantities:

1. **Geometric curvature:** \(\mathcal F y\), determined by edge parallel transport/holonomy and the vertex field.
2. **Microscopic incompatibility:** \(C_UG\), determined by the prescribed microscopic edge field.
3. **Interfacial disarrangement:** \(J\), determined by the two panel traces after transition to a common frame.

They must not be added as if they were the same defect, nor should one be used as a proxy for another. A constitutive energy coupling them requires an independently specified model.

For the Q-ball, the globally ambient \(\mathbb R^3\) formulation of T086 remains a valid flat reference model. A tangent-bundle formulation instead requires local frames and transport matrices. If the tangent connection is Levi-Civita, its nonzero curvature must appear in \(\mathcal F\); it cannot be removed by an arbitrary choice of panel coordinates.

## 7. What this does and does not establish

**Proved:** the face holonomy-defect identity; the covariant least-squares normal equation and Hodge orthogonality; uniqueness modulo parallel sections; invariance of the seam jump norm under independent orthogonal frame changes.

**Not proved:** a particular discrete Levi-Civita transport calibrated to the Q-ball geometry; convergence of the holonomy defect to smooth Gaussian curvature; a surface SBV relaxation theorem; a \(\Gamma\)- or Mosco-limit; a constitutive law for seam fatigue, opening, sliding or hysteresis; a coupling to the left Bernoulli sector and right gauge sector.

A future refinement theorem must specify the bundle, connection, edge transport, reconstruction operators, scaling of \(M_h\), compactness, and seam trace convergence. In particular, the curvature source must converge with the correct area scaling rather than being treated as a vanishing consistency error.

## 8. Classification

| Statement | Classification |
|---|---|
| \(C_UA_Uy=\mathcal F y\) on each oriented triangle | Exact finite-dimensional identity, proved |
| \(C_UA_U=0\) for face-flat transport | Proved |
| Covariant Hodge minimizer modulo \(\ker A_U\) | Proved for finite complex and SPD \(M\) |
| Seam jump norm invariant under orthogonal frame changes | Proved |
| Q-ball Levi-Civita transport and curvature calibration | To construct and test |
| Discrete-to-continuum curvature and seam convergence | Open |
| Morandotti surface relaxation / \(\Gamma\)-Mosco limit | Open |

**Editorial rule:** do not call \(C_UA_U=0\) in a curved tangent bundle. The exact identity is the curvature-defect formula in Section 3.
