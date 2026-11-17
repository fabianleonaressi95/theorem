# Rubino–QAT–quaternionic geometry–RGS: tensor transport and discrete SU(2) holonomy

**Date:** 17 November 2026  
**Purpose:** connect the coordinate/tensor discussion in Leonardo Rubino's *Spherical and Cylindrical Coordinates from the Tensors of the Relativity* (June 2026; viXra:2608.0051v1) to the programme's existing QAT, quaternionic, SU(2), and Q6 records. This note is an integration and source audit; it does not claim that Rubino develops QAT or quaternionic gauge theory.

## 1. Source boundary

Rubino's paper treats Cartesian, spherical and cylindrical coordinates; tensor component transformations; affine connections and Christoffel symbols; geodesic equations; parallel transport; the Riemann–Christoffel tensor; and classical vector-calculus formulae.

The relevant discussion is the section **“Parallel Transport and Riemann Tensor”** (PDF pp. 29–32). It introduces parallel transport by the condition that the covariant derivative of a vector along the path vanishes, then considers transport around a small closed coordinate loop and relates the resulting change to curvature.

The paper does **not** provide a quaternionic formulation, an SU(2) link model, a QAT derivation, or a Q6 discretization. Those parts of the bridge below come from the existing THEOREM programme and standard geometry, not from Rubino.

## 2. Mathematical audit of the parallel-transport argument

For a curve \(\gamma(\lambda)\), parallel transport of a vector field \(V\) is defined by
\[
\nabla_{\dot\gamma}V=0,
\qquad
\frac{dV^\mu}{d\lambda}
+\Gamma^\mu{}_{\nu\rho}\dot\gamma^\nu V^\rho=0.
\]

This definition is coordinate invariant. The Christoffel symbols themselves are not tensor components and need not vanish in flat space. In particular, Euclidean space in spherical coordinates has nonzero Christoffel symbols while its Riemann tensor is zero. Thus curvilinear coordinates must not be identified with intrinsic curvature.

With the convention
\[
[\nabla_\mu,\nabla_\nu]V^\rho
=R^\rho{}_{\sigma\mu\nu}V^\sigma
\]
for a torsion-free coordinate connection, the leading change after parallel transport around an infinitesimal loop is proportional to
\[
\delta V^\rho
=\pm R^\rho{}_{\sigma\mu\nu}V^\sigma
\,\Delta S^{\mu\nu}
+o(\operatorname{area}),
\]
where the sign depends on loop orientation and curvature convention, and the area bivector convention may include a factor of one half. This commutator identity is the clean derivation; it avoids treating coordinate components at different points as if they belonged to one fixed basis.

**Audit qualification.** Rubino's geometric idea is appropriate, but the component-by-component rectangular-loop derivation on pp. 30–32 should not be imported as a proof without rechecking its index placement, path ordering, Taylor expansion, and sign convention. The rigorous statement is the curvature/commutator identity above.

If the Riemann tensor vanishes, infinitesimal contractible-loop holonomy is trivial. This does not by itself rule out global holonomy on a non-simply-connected flat manifold. Likewise, a geodesic is locally extremal for the relevant geometric functional; it is not universally the globally shortest path (and Lorentzian timelike geodesics extremize proper time rather than minimize a Riemannian distance).

## 3. Quaternionic rotation and the QAT current

Write a quaternion as
\[
q=q_0+q_1i+q_2j+q_3k,
\quad i^2=j^2=k^2=ijk=-1,
\quad |q|=1.
\]
The unit quaternions form \(S^3\cong SU(2)\). A spatial vector is represented by a pure imaginary quaternion
\[
\mathbf v=v_xi+v_yj+v_zk.
\]
Its rotation is
\[
\mathbf v' = q\mathbf v q^{-1}.
\]
The map \(SU(2)\to SO(3)\) is a double cover with kernel \(\{\pm1\}\).

In the existing QAT notation, the quaternionic four-current is
\[
\mathcal J=c\rho+j_xi+j_yj+j_zk
=c\rho+\mathbf j.
\]
Under a spatial rotation represented by a unit quaternion,
\[
\mathcal J'=q\mathcal Jq^{-1}
=c\rho+q\mathbf j q^{-1}.
\]
The scalar component is invariant and the spatial current rotates. This is an algebraic covariance statement. It does not, by itself, derive a field equation, identify the current with a gauge connection, or establish a gravitational interpretation.

For a full Lorentzian four-dimensional spin geometry, the spin group is \(\mathrm{Spin}(1,3)\cong SL(2,\mathbb C)\). SU(2) is the appropriate group for spatial rotations (or a specified time-gauge/reduced setting); it must not be silently substituted for the full Lorentz spin group.

## 4. The correct geometric bridge: coframe and spin connection

The Christoffel connection in a coordinate basis is not automatically an SU(2) gauge connection. The intervening structure is an orthonormal coframe
\[
e^a=e^a{}_{\mu}\,dx^\mu
\]
and its spin connection \(\omega^a{}_b\). Its curvature is
\[
R^a{}_b=d\omega^a{}_b+
\omega^a{}_c\wedge\omega^c{}_b.
\]

After choosing a spatial orthonormal frame (or an explicit time gauge), the rotational part of the spin connection can be represented in \(\mathfrak{su}(2)\). Denote that connection by \(A\); then
\[
F=dA+A\wedge A.
\]
This is the legitimate continuum route from tensorial parallel transport to SU(2) transport. A derivation must specify the coframe, signature, frame convention, reduction to the rotational subgroup, and normalization of generators.

## 5. Existing finite-graph result: reuse T118, do not duplicate it

The finite Q6/graph link construction is already recorded in **[T118 — Gauge covariance of path transport and Wilson holonomy on a finite graph](../theorems/T118-su2-path-transport-wilson-holonomy.md)**.

For an oriented edge \(u\to v\), T118 uses \(U_{uv}\in SU(2)\), with
\[
U_{vu}=U_{uv}^{\dagger},
\qquad
U^G_{uv}=G_vU_{uv}G_u^{\dagger}.
\]
For a path \(p=(v_0,\ldots,v_n)\), its ordered transporter obeys
\[
P_{U^G}(p)=G_{v_n}P_U(p)G_{v_0}^{\dagger}.
\]
For a closed path, the holonomy is conjugated at the base vertex and its trace is gauge invariant. This is an exact finite-graph algebraic theorem; it is not a continuum-limit theorem.

The programme's related records have distinct roles:

- **[T114](../theorems/T114-q6-gauge-covariant-cubical-dirac-kaehler.md):** gauge-covariant cubical Dirac–Kähler differential.
- **[T118](../theorems/T118-su2-path-transport-wilson-holonomy.md):** open-path covariance and closed-loop Wilson holonomy.
- **[T119](../theorems/T119-binary-icosahedral-group-and-selected-representations.md):** quaternionic binary icosahedral group and selected representations.
- **[T120](../theorems/T120-mobius-orientation-cocycle-and-independent-su2-fibre.md):** separation of base-orientation cocycle from the independent internal SU(2) fibre.

These records must not be collapsed into a claim that Möbius non-orientability creates SU(2) curvature, torsion, or a Pin structure. T120 explicitly keeps those structures separate.

## 6. Discrete covariant derivative and continuum target

For a vertex field \(\Psi\) in the appropriate representation, the existing link-covariant edge difference is
\[
(D_U\Psi)_e=\Psi_h-U_e\Psi_g,
\qquad e=(g,h),
\]
with the corresponding positive operator
\[
K_U=D_U^{\dagger}D_U.
\]
For a closed oriented edge cycle \(C\), the ordered product of link variables gives its holonomy. These are the discrete counterparts of covariant differentiation and parallel transport.

A continuum-consistency claim requires more than gauge covariance. At minimum it must specify:

1. a family of meshes/complexes and geometric realizations;
2. a smooth target coframe and connection;
3. link variables obtained by path-ordered integration of that connection (or a precisely defined approximation);
4. compatible fibre and cochain inner products;
5. consistency and stability estimates;
6. a stated convergence mode for transport/operators (for example, a suitable resolvent or Mosco convergence statement).

Until these are supplied and proved, the Q6-to-continuum SU(2) bridge remains open. Existing Q6 data and prior R0/R1/R2 results are inputs to reuse, not reasons to reconstruct the model from scratch.

## 7. Theorem/status register

| Item | Statement | Status |
|---|---|---|
| Quaternion rotation | Unit quaternions act on imaginary quaternions by conjugation and give the double cover \(SU(2)\to SO(3)\). | Classical exact result; reuse existing quaternion/2I records. |
| Tensor parallel transport | \(\nabla_{\dot\gamma}V=0\) defines parallel transport; curvature is the commutator of covariant derivatives. | Classical exact result. |
| Finite graph holonomy | Path covariance, loop conjugation and Wilson-trace invariance. | Proved in T118. |
| QAT current covariance | Scalar density is invariant and spatial current rotates under quaternionic conjugation. | Algebraic identity; physical dynamics not implied. |
| Spin-connection reduction | Derive the spatial \(\mathfrak{su}(2)\) connection from the chosen coframe/spin connection. | Requires explicit convention and derivation for the selected RGS/QAT geometry. |
| Q6 continuum limit | Prove that the chosen discrete links/operators converge to the target continuum connection/operator. | Open. |
| Unified QAT–RGS field equations | Derive the common action, variations, constraints and observables. | Open; not established by Rubino or T118. |

## 8. Conclusion and attribution

Rubino is a useful introductory source for coordinate transformations, tensor components and the geometric idea of parallel transport. The rigorous bridge to the programme is supplied by standard curvature theory, the quaternionic double cover, the chosen coframe/spin connection, and the already-proved finite-graph covariance theorem T118.

The contribution of this integration is organizational and mathematical: it places the existing QAT quaternionic current, the spin-connection reduction, and the Q6 link-holonomy theorem in one dependency chain while preserving the open continuum and physical steps. It is not an independent validation of QAT, RGS, or Rubino's full derivation.

## References

- L. Rubino, *Spherical and Cylindrical Coordinates from the Tensors of the Relativity*, June 2026, viXra:2608.0051v1, especially the section “Parallel Transport and Riemann Tensor”, pp. 29–32.
- T118, T114, T119 and T120, as linked above.
- Standard differential-geometric identity: curvature as the commutator of covariant derivatives; standard quaternionic double covering \(SU(2)\to SO(3)\).
