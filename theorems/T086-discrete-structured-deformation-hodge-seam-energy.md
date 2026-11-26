# T086 — Discrete structured-deformation energy, Hodge projection and seam-trace separation

**Date:** 11 November 2026  
**Status:** finite-complex theorem, proved below. The construction is a discrete first-order structured-deformation model. It is not a discretization theorem for the full Morandotti relaxed density, and it does not establish a continuum limit.

**Dependencies:** T079, T080, T068–T070.

## 1. Purpose: close the missing finite-dimensional variational link

T079 identifies the structured mismatch
\[
\mathsf D=\nabla g-G.
\]
T080 proves the exact shell identity \(d_1\mathsf D_h=-d_1G_h\), but does not yet give the variational problem that selects the best macroscopic deformation for a prescribed microscopic edge field.

This record supplies that missing finite-dimensional problem. It makes three objects distinct:

1. the macroscopic nodal deformation \(y_h\);
2. the microscopic edge 1-cochain \(G_h\);
3. the mismatch \(D_h=d_0y_h-G_h\).

The construction is an exact graph/cochain analogue of the first-order split. It does not replace the SBV cell formula or the second-order \(W_2\) density in Morandotti's continuum theory.

## 2. Oriented surface complex and cochains

Let \(K=(V,E,F)\) be a finite, connected, coherently oriented triangulation of a closed connected surface. Let
\[
B_1\in\mathbb Z^{|V|\times|E|},\qquad
B_2\in\mathbb Z^{|E|\times|F|}
\]
be its vertex-edge and edge-face incidence matrices, with
\[
B_1B_2=0.
\]
For ambient three-component fields, define
\[
C^0(K;\mathbb R^3)=\mathbb R^{|V|\times3},\qquad
C^1(K;\mathbb R^3)=\mathbb R^{|E|\times3},\qquad
C^2(K;\mathbb R^3)=\mathbb R^{|F|\times3}.
\]
The coboundary maps are
\[
d_0y=B_1^Ty,\qquad d_1G=B_2^TG.
\]
The chain identity gives the cochain identity \(d_1d_0=0\).

An edge cochain is understood as an oriented ambient increment, or as an increment already transported to a common ambient frame. If panel-local coordinates are used, the transition maps must be applied before assembling the global cochain.

## 3. Discrete structured-deformation functional

Let \(M:C^1\to C^1\) be a symmetric positive-definite edge mass/operator. It may be block diagonal by edge, with a positive-definite \(3\times3\) block per edge, or include a declared local coupling. Define
\[
D_h(y,G):=d_0y-G
\]
and
\[
\boxed{
E_h(y;G)=\frac12\langle d_0y-G,M(d_0y-G)\rangle.
}
\]
For fixed microscopic field \(G\), the relaxed discrete bulk energy is
\[
\boxed{
\mathcal W_h(G)=\min_{y\in C^0(K;\mathbb R^3)/\mathbb R^3}
E_h(y;G).
}
\]
The quotient removes the three rigid translations. Since the graph is connected and \(M\) is positive definite, the minimizer exists and is unique modulo translations.

This is a finite-dimensional quadratic model. It is a legitimate test energy for the structured mismatch, but it is not asserted to equal Morandotti's continuum cell value \(W_2\).

## 4. Euler equation and Hodge projection theorem

Differentiating with respect to \(y\) gives the normal equation
\[
\boxed{
B_1M(B_1^Ty-G)=0.
}
\]
Equivalently,
\[
(B_1MB_1^T)y=B_1MG.
\]
The weighted graph Laplacian \(L_M=B_1MB_1^T\) is positive semidefinite with kernel exactly the constant vertex fields. Therefore the equation has a solution, unique modulo translations.

Let \(y_*\) be this solution and \(D_*=d_0y_*-G\). Then
\[
\boxed{
\langle d_0v,MD_*\rangle=0
\quad\text{for every }v\in C^0(K;\mathbb R^3).
}
\]
Thus \(D_*\) is the \(M\)-orthogonal residual after projecting \(G\) onto the space of exact edge cochains \(\operatorname{im}d_0\). In particular,
\[
\mathcal W_h(G)=\frac12\|D_*\|_M^2
=\frac12\operatorname{dist}_M
\bigl(G,\operatorname{im}d_0\bigr)^2.
\]

**Proof.** The first variation in direction \(v\) is
\[
\delta E_h(y;G)[v]
=\langle d_0v,M(d_0y-G)\rangle
=\langle v,B_1M(B_1^Ty-G)\rangle.
\]
The Hessian is \(B_1MB_1^T\). For any vertex field \(v\),
\[
v^TB_1MB_1^Tv=\|B_1^Tv\|_M^2.
\]
It vanishes precisely when \(v\) is constant on the connected graph. Coercivity on the quotient gives existence and uniqueness. The normal equation is exactly the orthogonality condition, which characterizes the weighted orthogonal projection. \(\square\)


## 5A. Explicit Schur-complement formula

The minimizer and the relaxed energy can be written without solving for the displacement component-by-component. On the quotient by translations, let
\[
L_M=B_1MB_1^T,\qquad
y_*=L_M^\dagger B_1MG,
\]
where \(L_M^\dagger\) is the Moore–Penrose inverse (acting independently on the three ambient components). Then
\[
D_*=(B_1^TL_M^\dagger B_1M-I)G.
\]
Substitution gives
\[
\boxed{
\mathcal W_h(G)
=\frac12\langle G,
\bigl[M-MB_1^TL_M^\dagger B_1M\bigr]G\rangle.
}
\]
Define
\[
P_M:=I-B_1^TL_M^\dagger B_1M.
\]
Then \(P_M^2=P_M\) and \(P_M^TM=MP_M\): this is the \(M\)-orthogonal projector onto the complement of \(\operatorname{im}d_0\). The bracketed operator in the energy formula is \(MP_M\), which is symmetric positive semidefinite but is not, in general, itself an idempotent projector. Its kernel is exactly \(\operatorname{im}d_0\).

This formula is useful computationally: it provides an independent energy evaluation from the assembled graph Laplacian and exposes the relaxed energy as a quadratic form in the prescribed microscopic cochain. For large meshes one should not form the dense pseudoinverse; solve the gauge-fixed sparse Laplacian system and evaluate the residual energy instead.

## 5. Exact incompatibility and the zero-energy criterion

Because \(d_1d_0=0\),
\[
\boxed{
d_1D_*= -d_1G.
}
\]
The right-hand side is the discrete Burgers/incompatibility 2-cochain in this convention.

For any connected closed triangulated surface,
\[
\mathcal W_h(G)=0
\quad\Longleftrightarrow\quad
G\in\operatorname{im}d_0.
\]
If, in addition, \(H^1(K;\mathbb R)=0\) (in particular for the sphere topology of the finite Q-ball shell), then
\[
\ker d_1=\operatorname{im}d_0,
\]
and hence
\[
\boxed{
\mathcal W_h(G)=0
\quad\Longleftrightarrow\quad
d_1G=0.
}
\]
Thus on the simply connected shell, vanishing face incompatibility is both necessary and sufficient for zero relaxed mismatch energy. On a surface with nontrivial first cohomology, curl-free but non-exact harmonic edge fields may carry positive energy; the correct criterion remains exactness, not merely zero curl.

This is a useful distinction for non-spherical quotients and periodic cells: local Burgers curl does not detect global cohomology classes.

## 6. Separate panel-seam traces and frame transitions

To model independent panel traces, replace the globally identified seam edge by two panel-side copies. Choose a common orientation for the physical seam and let
\[
G_e^+,G_e^-\in\mathbb R^3
\]
be the two edge increments after expressing them in a common ambient frame. If panel coordinates are used, let \(R_e^{-+}\) be the declared transition/transport from the minus frame to the plus frame. Define the covariant trace jump
\[
J_e:=G_e^+-R_e^{-+}G_e^-.
\]
For nonnegative seam weights \(\eta_e\), the separate interface contribution is
\[
E_{\rm seam}(G)
=\frac12\sum_{e\in\mathcal S}
\eta_e\,|J_e|^2.
\]
A combined test functional is
\[
\boxed{
E_h^{\rm bulk+seam}(y;G^+,G^-)
=\frac12\|d_0y-G\|_M^2
+\frac12\sum_{e\in\mathcal S}\eta_e|J_e|^2.
}
\]
Here \(G\) in the bulk term is assembled using a declared single-valued representative or a panelwise broken complex; the seam term is evaluated on the two traces. The two contributions must not be collapsed into one another.

Consequences:
- a physical seam is only an interface label;
- it contributes no seam energy when the transported traces match;
- bulk face curl and interface trace jump are different observables;
- a nonzero seam penalty is a constitutive choice, not a consequence of the incidence identity;
- the \(\eta_e\) must be calibrated or derived from a separate material/interface model.

This separation is compatible with the conceptual distinction in second-order structured-deformation theory between bulk relaxation and the interfacial density on the jump set. It does not identify the finite seam term above with the continuum \(\gamma_2\).

## 7. Relation to T079–T080 and the next continuum obligation

T079 supplies the continuum split and the surface circulation formula. T080 supplies the exact finite shell incidence complex and discrete Stokes identity. T086 adds the variational projection and the exact finite-dimensional Hodge interpretation.

The resulting finite chain is
\[
G_h
\xrightarrow{\;\text{projection modulo }\operatorname{im}d_0\;}
D_{h,*}
\xrightarrow{\;d_1\;}
-d_1G_h.
\]
This closes the finite-dimensional first-order variational layer. It does **not** yet establish:
- convergence of \(M_h\) to a surface metric or constitutive tensor;
- compactness of interpolants \(y_h,G_h\);
- a liminf inequality or recovery sequence;
- convergence of the seam trace measures;
- the second-order \(\Gamma_{\rm Mor}\) cell relaxation;
- a Mosco/\(\Gamma\)-limit on the curved Q-ball.

For such a limit, the edge mass must be scaled consistently with edge length and surface measure; the reconstruction of \(G_h\) must be uniformly stable; and the panel transitions and seam traces must form a compatible bundle/discrete-complex family under refinement.

## 8. Concrete numerical consequences and falsifiable tests

The theorem suggests the next benchmark, rather than another generic comparison:

1. **Exactness test:** on the 92-vertex/270-edge/180-face shell of T080, generate an exact field \(G=d_0z\). The minimizer must recover \(y_*=z\) modulo translation and the minimum energy must be at solver tolerance.
2. **Single-face source test:** prescribe an edge cochain with one nonzero face curl, solve the weighted graph Laplacian, and verify \(d_1D_*=-d_1G\) exactly at the cochain level.
3. **Hodge orthogonality:** verify \(B_1MD_*=0\) and \(\langle d_0v,MD_*\rangle=0\) for random vertex fields.
4. **Topology test:** compare the sphere shell with a periodic/torus complex. On the torus, construct a non-exact harmonic 1-cochain with zero curl and verify positive relaxed energy. This tests the distinction between local incompatibility and global cohomology.
5. **Seam test:** duplicate the 90 physical seam traces, apply nontrivial panel-frame transitions, and verify that matching transported traces have zero interface energy while a prescribed jump produces exactly the declared quadratic cost.

These tests are finite-dimensional algebraic/variational audits. They do not claim a continuum convergence rate.


## 8A. Executed Q-ball shell audit (11 November 2026)

The finite-mesh numerical gate has now been executed on the canonical T080 shell, reconstructed from `models/football_shell.py`. The incidence matrices use the T080 orientation convention. The edge metric is the declared positive diagonal choice
\[
M=\operatorname{diag}(\ell_e^{-1}),
\]
where \(\ell_e\) is the Euclidean length of edge \(e\). This is a graph-energy metric for this audit, not a calibrated material tensor.

The observed combinatorial counts are \((|V|,|E|,|F|,|\mathcal S|)=(92,270,180,90)\), and \(\max|B_1B_2|=0\) exactly.

| Test | Numerical result |
|---|---:|
| Exact cochain energy, \(G=B_1^Tz\) | \(1.3343\times10^{-27}\) |
| Recovery error modulo translation | \(3.0665\times10^{-14}\) |
| Exact-case Hodge residual | \(1.6375\times10^{-13}\) |
| Non-exact impulse curl norm | \(1.4142135624\) |
| Curl identity residual, \(\|d_1D_*+d_1G\|\) | \(8.6897\times10^{-18}\) |
| Non-exact Hodge residual, \(\|B_1MD_*\|\) | \(3.0954\times10^{-15}\) |
| Direct minimum energy | \(0.8277381346948023\) |
| Schur-formula energy | \(0.8277381346948021\) |
| Energy discrepancy | \(2.2204\times10^{-16}\) |
| Projector idempotence residual, \(\|P_M^2-P_M\|\) | \(2.6094\times10^{-14}\) |
| \(M\)-self-adjointness residual | \(8.2459\times10^{-14}\) |

The exact case confirms recovery modulo the translational gauge. The impulse case confirms that nonzero local curl survives as an incompatibility while the minimizing residual is Hodge-orthogonal. The Schur energy and the residual energy agree to floating-point precision.

**Reproduction:** run `python scripts/audit_t086_hodge_projection.py` from the repository root. The script prints the full JSON audit. The random seed is fixed at `20261111`.

These are finite-mesh numerical verification results. They do not test the torus harmonic case, the panel-frame seam transition law, or any continuum refinement limit; those remain separate gates.

## 9. Classification

| Statement | Classification |
|---|---|
| Weighted graph minimizer exists and is unique modulo translations | Proved for connected finite graph and SPD \(M\) |
| Normal equation and weighted Hodge projection | Proved |
| \(d_1D_*=-d_1G\) | Exact cochain identity |
| Zero energy iff \(G\) is exact | Proved |
| Zero energy iff curl vanishes when \(H^1=0\) | Proved under the stated topology |
| Independent seam-trace energy | Explicit model ansatz, not a derived material law |
| Continuum curved-shell relaxation / Mosco / Gamma limit | Open |

## References

- T079, “Morandotti structured gradients, surface incompatibility and barycentric RGS–PRISM bridge.”
- T080, “Exact discrete Stokes complex and structured-gradient incompatibility on the Q-ball shell.”
- Barroso, Matias, Morandotti & Owen, “Second-Order Structured Deformations: Relaxation, Integral Representation and Applications,” *Arch. Rational Mech. Anal.* 225 (2017), 1025–1072, DOI: 10.1007/s00205-017-1120-5.
- Barroso, Matias, Morandotti & Owen, “Explicit Formulas for Relaxed Disarrangement Densities Arising from Structured Deformations,” *Math. Mech. Complex Syst.* 5 (2017), 163–189, DOI: 10.2140/memocs.2017.5.163.

**Editorial rule:** this is a finite graph/cochain variational theorem. Do not describe it as the continuum Morandotti relaxation theorem, as a proof of Mosco convergence, or as a calibrated seam constitutive law.
