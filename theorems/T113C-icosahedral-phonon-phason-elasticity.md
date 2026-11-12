# T113-C — Icosahedral phonon–phason elasticity by finite-group projection

**Classification:** exact symmetry construction and variational reduction; constitutive coefficients and gravitational packet mass remain open.

## 1. Representations and fields

Let \(I\cong A_5\) be the proper rotational icosahedral group, with \(|I|=60\). Let
\[
R:I\to SO(3),\qquad S:I\to SO(3)
\]
be, respectively, the physical-space and perpendicular-space three-dimensional representations of the chosen icosahedral cut-and-project model. The representation \(S\) must be fixed by the actual six-dimensional embedding; it is not a freely adjustable second copy of \(R\).

The long-wavelength displacement fields are
\[
u_i(x,t)\in V_{\parallel},\qquad
w_A(x,t)\in V_{\perp}.
\]
Under \(g\in I\), use
\[
u\mapsto R_g u,\qquad w\mapsto S_g w,\qquad
\partial_i\mapsto (R_g)_{ji}\partial_j.
\]
Define the phonon strain and phason gradient
\[
\varepsilon_{ij}=\tfrac12(\partial_i u_j+\partial_j u_i),
\qquad
\chi_{Ai}=\partial_i w_A.
\]
The phason gradient is not symmetrized: its two indices belong to inequivalent representation spaces.

## 2. Most general quadratic local elastic density

At leading order in gradients, the harmonic energy density has the block form
\[
W=\tfrac12 C_{ij kl}\varepsilon_{ij}\varepsilon_{kl}
+R_{ij,A k}\varepsilon_{ij}\chi_{Ak}
+\tfrac12 K_{Ai,Bj}\chi_{Ai}\chi_{Bj}.
\]
The minor and major symmetries required by the quadratic form are
\[
C_{ij kl}=C_{ji kl}=C_{ij lk}=C_{kl ij},
\qquad K_{Ai,Bj}=K_{Bj,Ai}.
\]
The mixed tensor obeys \(R_{ij,A k}=R_{ji,A k}\). No additional symmetry is imposed unless it follows from the selected point group or microscopic model.

The coefficients are invariant under the icosahedral action:
\[
C_{ij kl}=R_{ia}R_{jb}R_{kc}R_{ld}C_{ab cd},
\]
\[
R_{ij,A k}=R_{ia}R_{jb}S_{AC}R_{kd}R_{ab,Cd},
\]
\[
K_{Ai,Bj}=S_{AC}R_{ik}S_{BD}R_{jl}K_{Ck,Dl},
\]
for every \(g\in I\). Repeated indices are summed. These equations are the defining symmetry constraints; they do not by themselves determine numerical elastic constants.

## 3. Exact Reynolds construction

For any seed tensors \(C^{(0)},R^{(0)},K^{(0)}\) with the stated index symmetries, define
\[
C=\mathcal P_I C^{(0)},\quad
R=\mathcal P_I R^{(0)},\quad
K=\mathcal P_I K^{(0)},
\]
where the Reynolds projector is the finite average over the 60 proper rotations:
\[
(\mathcal P_I C^{(0)})_{ij kl}
=\frac1{60}\sum_{g\in I}
(R_g)_{ia}(R_g)_{jb}(R_g)_{kc}(R_g)_{ld}
C^{(0)}_{ab cd},
\]
\[
(\mathcal P_I R^{(0)})_{ij,A k}
=\frac1{60}\sum_{g\in I}
(R_g)_{ia}(R_g)_{jb}(S_g)_{AC}(R_g)_{kd}
R^{(0)}_{ab,Cd},
\]
\[
(\mathcal P_I K^{(0)})_{Ai,Bj}
=\frac1{60}\sum_{g\in I}
(S_g)_{AC}(R_g)_{ik}(S_g)_{BD}(R_g)_{jl}
K^{(0)}_{Ck,Dl}.
\]
Because the group average is idempotent and invariant under left multiplication by any group element, the projected tensors satisfy the three invariance equations exactly. Projection preserves the tensor symmetries when the seed is first restricted to the corresponding symmetry class.

This is a constructive parameterization of invariant tensors, not a claim that a particular seed spans the full invariant space. A complete independent-constant count requires an explicit matrix realization of \(R,S\) and a rank computation for the Reynolds projector on each tensor space.

## 4. Stability and coupled acoustic modes

A sufficient harmonic stability condition is strict positivity of the block quadratic form on nonzero admissible strain pairs:
\[
\begin{pmatrix}\varepsilon&\chi\end{pmatrix}
\begin{pmatrix}C&R\\R^T&K\end{pmatrix}
\begin{pmatrix}\varepsilon\\\chi\end{pmatrix}>0.
\]
Translations remain zero modes; stability is imposed on strains, not on constant displacements. If \(C\) is positive definite on symmetric strains, the Schur-complement condition is
\[
K-R^T C^{-1}R>0
\]
on the phason-gradient sector (with the inverse understood on the admissible phonon-strain space). This condition is sufficient for the displayed block form and makes explicit why an arbitrary mixed coupling cannot be inserted without checking stability.

For a plane wave with direction \(n\in S^2\), amplitudes \((U_i,W_A)\), and wave number \(k\), set
\[
\varepsilon_{ij}=\tfrac{ik}{2}(n_iU_j+n_jU_i),
\qquad \chi_{Ai}=ik W_A n_i.
\]
Substitution into \(W\) defines the direction-dependent acoustic stiffness matrix \(\mathcal K(n)\) on the six amplitudes. With a positive inertia matrix \(\mathcal M\), the conservative acoustic branches satisfy
\[
\mathcal K(n)q_\alpha=c_\alpha(n)^2\mathcal M q_\alpha,
\qquad q_\alpha=(U,W).
\]
The six branches can mix phonon and phason polarizations when \(R\ne0\). At \(R=0\), the two sectors decouple only if the inertia matrix is block diagonal as well.

For a simple eigenvalue and a smooth material-density path \(\lambda=\log\rho_m\), the generalized Hellmann–Feynman identity gives
\[
\frac{d c_\alpha^2}{d\lambda}
=\frac{q_\alpha^\dagger
(\partial_\lambda\mathcal K-c_\alpha^2\partial_\lambda\mathcal M)
q_\alpha}
{q_\alpha^\dagger\mathcal M q_\alpha}.
\]
At eigenvalue crossings or degeneracies, one must diagonalize the perturbation within the degenerate eigenspace; differentiating a sorted eigenvalue list is not valid.

## 5. Connection to metric response: what is still missing

The tensors above specify the spatial harmonic energy. They do **not** yet specify the full covariant material action. To compute gravitational mass, one must supply:
1. the material four-velocity and the spacetime/spatial projectors;
2. the covariant extension of \(C,R,K\), including their density and metric dependence;
3. the inertia matrix and its metric dependence;
4. the nonlinear constitutive terms that determine the medium's second-order response to a localized wave;
5. boundary conditions and a background-subtracted, time-averaged integral of the full \(T_{00}\).

Only after these inputs are fixed can
\[
T_{\mu\nu}=-\frac2{\sqrt{-g}}\frac{\delta S}{\delta g^{\mu\nu}}
\]
be evaluated and the packet's gravitational mass extracted. The diagnostic
\[
-\frac{d\log c_\alpha}{d\log\rho_m}\frac{E_\alpha}{c_\alpha^2}
\]
remains a candidate comparison quantity, not a theorem for the coupled icosahedral system.

## 6. Defects and golden geometry

A specified dislocation/disclination configuration may change the local coefficients and mode problem:
\[
(B,\Omega)\longrightarrow(C,R,K,\mathcal M)_{\rm local}
\longrightarrow(c_\alpha,q_\alpha)
\longrightarrow T_{\mu\nu}^{(\alpha)}.
\]
Burgers translation holonomy and Frank rotational holonomy remain distinct. Their effect on the elastic tensors must be derived from a defect-core or coarse-grained constitutive model; it is not encoded by assigning them arbitrary tensor weights.

The icosahedral symmetry is compatible with the golden geometry of the icosahedron, but the invariant-tensor projection uses the group representations, not an automatic factor of \(\varphi\). A golden-ratio dependence in elastic coefficients or acoustic speeds requires a specified microscopic cut-and-project model and an explicit derivation. No De Aquino threshold is inserted without its exact source definition.

## 7. Falsifiable next calculations and status

The next reproducible calculation must:
- instantiate exact generators for the physical and perpendicular representations from one stated six-dimensional embedding;
- enumerate the 60 group elements and verify closure and orthogonality;
- construct the Reynolds projectors on the phonon, phason, and mixed tensor spaces;
- compute their ranks and bases of invariant tensors;
- parameterize the positive cone of \((C,R,K)\);
- calculate \(c_\alpha(n,\rho_m)\) on a direction grid, track polarization mixing, and check the uncoupled limit;
- only then add a covariant metric completion and nonlinear packet calculation.

**Established in this record:** the exact finite-group Reynolds construction, the invariant constraints, the harmonic block form, and the generalized eigenvalue sensitivity under the stated hypotheses.

**Not established:** independent elastic-constant counts for a specified icosahedral embedding, numerical material coefficients, a golden-ratio scaling law, a quasicrystal phonon–phason gravitational mass, or a universal sign.
