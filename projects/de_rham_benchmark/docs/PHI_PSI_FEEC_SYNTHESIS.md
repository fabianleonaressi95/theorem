# Golden / supergolden synthesis for curvilinear de Rham–FEEC

**Status:** mathematical synthesis and theorem programme. Algebraic identities below are proved under their stated assumptions; the geometric refinement proposal is conditional; Mosco, compactness, norm-resolvent, and harmonic-kernel conclusions are not claimed for the repository benchmark until the listed lemmas are established.

## 1. Governing principle

The curvilinear de Rham benchmark, consistent cubical FEEC masses, and independent audit form one problem: construct uniformly stable finite-dimensional Hilbert complexes on curvilinear meshes, identify their adjoints through metric mass matrices, and prove convergence of the associated closed quadratic forms to the continuum Hodge form.

The golden ratio and supergolden constant do not alter the exterior derivative and are not extra physical axioms. Their legitimate role is to organize candidate mesh families, scale recurrences, and explicit constants. Every claim must be classified as proved identity, conditional theorem, numerical observation, or open conjecture.

The simplification is to factor the programme into (A) geometric scale law, (B) uniformly stable Hilbert-complex approximation, and (C) form convergence. No spectral computation replaces (B) or (C).

## 2. Exact de Rham–FEEC core

On the reference cube [0,1]^d, use the lowest-order tensor-product cubical spaces
\[
\widehat V^k=\bigoplus_{|I|=k}
\left(\bigotimes_{j\notin I}Q_1(\widehat x_j)\right)
\otimes\left(\bigotimes_{i\in I}Q_0(\widehat x_i)\right)d\widehat x^I,
\quad I=(i_1<\cdots<i_k).
\]
For an orientation-preserving cell diffeomorphism F_K, define the physical space by the covariant pullback: F_K^* V_h^k(K)=\widehat V^k. Naturality gives F_K^*(d\omega)=d(F_K^*\omega). This is exact for sufficiently regular maps and explains why incidence matrices are topological. It does not imply projection stability or approximation.

With A=DF_K, ambient metric G, and pullback metric g=A^TGA, the exact local Gram matrix is
\[
(M_K^k)_{ab}=\int_{\widehat K}
\widehat\phi_a^T\Lambda^k(g^{-1})\widehat\phi_b\sqrt{\det g}\,d\widehat x.
\]
For k=0 the exterior-power factor is 1; for k=d it is (det g)^(-1). For unit-integral top-form DoFs and an orientation-preserving affine map, the top mass is 1/vol_g(K). Curved-cell integration retains the pointwise metric density.

For coefficient inner products (u,v)_{h,k}=u^T M_{h,k}v and incidence D_{k-1}:V_h^{k-1}->V_h^k, the Hilbert adjoint is exactly
\[
\delta_h^k=M_{h,k-1}^{-1}D_{k-1}^TM_{h,k},
\]
provided the masses are symmetric positive definite and the domain/codomain convention for D is fixed.

### Orientation prerequisite

The merged independent audit identifies a sign mismatch between the current incidence convention in ddr/mesh.py and the ordered coordinate-wedge convention used for the FEEC basis. Before claiming a commuting diagram, choose one convention globally:
1. standard cubical coefficient (-1)^p(2s-1), with zero-based removed-axis position p; or
2. retain current matrices but change every degree-wise face orientation and basis/DoF sign consistently.

Add a local regression test for d(phi_sigma)=sum_tau D[tau,sigma]phi_tau in every degree. D_{k+1}D_k=0 alone cannot detect a global sign reversal. Spectra may also remain unchanged while the declared differential/basis identification is wrong.

## 3. Legitimate roles of phi and psi

Let phi=(1+sqrt(5))/2, so phi^2=phi+1. Let psi>1 solve psi^3-psi^2-1=0, so psi^3=psi^2+1. These give exact algebraic recurrences, not automatic mesh properties.

### 3.1 Supergolden scale schedule

A candidate isotropic schedule h_n=h_0 psi^(-n) obeys
\[
h_{n-3}=h_{n-2}+h_n.
\]
This is exact scale bookkeeping, not proof that conforming cubical meshes exist at these scales. A mesh construction must specify integer subdivisions, cell maps, interface conformity, and realization of non-integer ratios.

If a concrete refinement operator R on geometric data is constructed and satisfies R^3=R^2+I, then R^(n+3)=R^(n+2)+R^n. This follows by multiplying the operator identity by R^n. It becomes a mesh law only after invariance and conformity of the admissible mesh family are proved.

### 3.2 Golden internal proportions

A candidate cell template may split with t=phi^(-1) and 1-t=phi^(-2), since 1=phi^(-1)+phi^(-2). Repeated golden splits can create nonuniform sizes. Shape regularity therefore requires explicit lower bounds on child aspect ratios and Jacobian singular values; phi alone does not guarantee it.

### 3.3 Route to useful FEEC constants

Assume uniformly over cells and levels
\[
c_A h_K|\xi|\le |DF_K(\hat x)\xi|\le C_A h_K|\xi|,
\quad 0<c_J\le h_K^{-d}|\det DF_K|\le C_J,
\]
with normalized map derivatives bounded to the order required by approximation theory. Then scaled pullback metrics are uniformly elliptic. Mass norm equivalence and approximation constants depend on these geometric bounds, not on the label of the refinement ratio.

Golden/supergolden geometry is useful only if it yields explicit level-independent constants or sharper recurrences for them. Otherwise it is decorative and should not enter the proof.

## 4. Conditional FEEC–Mosco theorem

Let H^k be continuum L2 k-forms on a fixed compact Lipschitz domain/manifold with uniformly elliptic metric. Let V^bullet be the closed de Rham Hilbert complex, with form
\[
q_k(u)=\|d_ku\|^2+\|\delta_ku\|^2
\]
on the joint graph domain. For each n let V_n^bullet be a finite-dimensional subcomplex with discrete differential d_n, positive masses, and reconstruction maps J_n:V_n^k->H^k.

Assume:

**H1 Geometry.** Cell maps are orientation-preserving diffeomorphisms; scaled Jacobians and inverse Jacobians are uniformly bounded; pullback metrics are uniformly elliptic; face maps and traces match across cells.

**H2 Complex and orientation.** d_n^2=0, local basis/DoF orientations agree with incidence matrices, and pullback commutes with d.

**H3 Uniform norm equivalence.** Reconstructed mass inner products are uniformly equivalent to continuum L2 norms.

**H4 Commuting bounded projections.** Projections pi_n^k exist on the relevant graph domains, satisfy d_n pi_n^k=pi_n^{k+1}d, have sup_n ||pi_n^k|| bounded, and converge strongly to identity.

**H5 Joint graph recovery.** For every u in the continuum form domain there are u_n with J_nu_n->u and reconstructed d_nu_n, delta_nu_n converging weakly to du, delta u, with energy limsup no greater than q_k(u).

**H6 Liminf.** If J_nu_n converges weakly to u and discrete energies are bounded, then u is in the continuum form domain and q_k(u)<=liminf q_{n,k}(u_n).

**H7 Compactness.** Bounded discrete graph-energy sequences are precompact after reconstruction on the co-closed subspaces needed for Hodge decomposition.

**H8 Topology and gap.** Discrete cohomology dimensions eventually equal continuum Betti numbers; harmonic projections are controlled and the positive spectrum has a uniform gap away from zero.

Then H5-H6 give generalized Mosco convergence of the reconstructed forms; the associated operators converge in strong resolvent sense. With H7-H8, isolated bounded positive spectral windows converge with multiplicity and harmonic subspaces converge in gap.

This is a conditional theorem programme, not a result already proved for the repository benchmark. Norm-resolvent convergence is not included: it needs additional uniform collective compactness/equicontinuity of reconstructed resolvents, or an appropriate uniform compact embedding.

### Why commutation alone is insufficient

d_n pi_n=pi_n d controls only d. It gives no uniform bound on ||pi_n||, no graph-norm approximation, no control of delta, no convergence of mass inner products, no compactness, and no topology/kernel stability. Since delta_n is defined by M_n and D_n together, convergence of the algebraic differential alone cannot imply convergence of adjoints.

## 5. Keep convergence notions separate

1. Mosco convergence requires a liminf inequality and recovery sequences in a common (possibly generalized) Hilbert-space framework.
2. Discrete compactness requires precompactness of bounded graph-energy sequences, usually after removing exact components or restricting to co-closed spaces.
3. Strong-resolvent convergence follows from suitable closed-form convergence and compatible identification maps.
4. Norm-resolvent convergence is stronger and typically requires collective compactness of resolvents; strong convergence is insufficient.
5. Harmonic-kernel stability requires cohomology control and a uniform positive gap. Mosco convergence alone does not preclude spurious small eigenvalues or changing kernel dimension.

## 6. Candidate laws, explicitly conditional

**Law A — scale cocycle.** If a conforming refinement operator R is actually defined and R^3=R^2+I, then every linear observable s_n=L(R^n x) satisfies s_{n+3}=s_{n+2}+s_n. Proof: apply L to R^(n+3)x=(R^(n+2)+R^n)x. This may simplify cell-count or estimator recurrences, but only after R is constructed.

**Law B — metric mass scaling.** Under a similarity F_h(xhat)=x0+hB xhat, with fixed invertible B, a covariant k-form L2 Gram matrix scales as h^(d-2k): volume contributes h^d and the squared covector norm contributes h^(-2k). This exponent is dimensional, not golden. A phi/psi schedule changes h between levels, not the local exponent.

**Law C — finite-template shape regularity.** If a golden split uses finitely many child templates whose normalized singular values lie in [c,C], and templates are reused by similarities, the shape constants are uniform across levels. This follows from finite template bounds and composition estimates. The bounds must be calculated; phi alone is insufficient.

**Law D — spectral rate conversion.** If a proven eigenvalue estimate is |lambda_{n,j}-lambda_j|<=C h_n^r, then h_n=h0 psi^(-n) gives error <=C h0^r psi^(-rn). The approximation order r comes from polynomial degree, regularity, and spectral theory, not from psi.

## 7. Counterexample logic

- Commuting projections can have diverging operator norms; commutation does not imply uniform stability.
- Varying inner products can change adjoints while leaving the algebraic differential fixed; convergence of d_n does not imply convergence of delta_n.
- Strong-resolvent convergence does not imply norm-resolvent convergence; high-frequency subspaces can obstruct operator-norm convergence.
- Form convergence without topology control does not by itself stabilize kernel dimensions; a uniform gap and cohomology control are needed.
- Global reversal of all D_k preserves D_{k+1}D_k=0 and many quadratic spectra but conflicts with fixed basis orientations unless DoF signs are also reversed.

These are logical obstructions. The repository should record explicit finite-dimensional/operator examples as theorem tests, not misrepresent them as numerical evidence about the current mesh family.

## 8. Lemma programme, in efficient order

1. Orientation lemma: local incidence/exterior-derivative identity in every degree.
2. Pullback lemma: F_K^*d=dF_K^* and trace compatibility.
3. Mass lemma: symmetry/positive definiteness of exact Gram matrices and uniform quadrature perturbation.
4. Metric equivalence lemma: uniform L2 norm equivalence from singular-value/Jacobian bounds.
5. Adjoint lemma: derive the M^(-1)D^TM formula from coefficient inner products and verify matrix ordering.
6. Commuting projection lemma: construct pi_n on the actual curvilinear family.
7. Projection stability lemma: prove sup_n ||pi_n||<infinity.
8. Graph recovery lemma: approximation in the joint graph norm of d and delta.
9. Liminf lemma: weak lower semicontinuity of reconstructed energies.
10. Discrete compactness lemma: precompactness of bounded-energy co-closed sequences.
11. Cohomology lemma: identify discrete and continuum cohomology.
12. Gap lemma: uniform lower bound on the first positive eigenvalue.
13. Mosco theorem: combine liminf and recovery.
14. Resolvent theorem: strong resolvent; add collective compactness for norm resolvent.
15. Optional golden refinement lemma: construct a conforming finite-template operator with exact phi/psi recurrence and prove uniform shape regularity. Pursue only if it improves constants or construction complexity.

## 9. Immediate research actions

1. Treat merged PR #87 and merged independent audit as the baseline.
2. Do not change incidence signs until a local basis-derivative test fixes the convention; then correct all degrees consistently.
3. Keep historical diagonal, top-degree-corrected diagonal, and consistent FEEC masses distinct.
4. State exact Jacobian, derivative, and face-matching assumptions for every mesh family.
5. Do not label finite-level spectral stabilization as Mosco convergence or discrete compactness.
6. Use psi scales only after a conforming refinement construction exists; use phi splits only after child-shape bounds are proved.

## 10. Status table

| Claim | Status |
|---|---|
| Covariant pullback commutes with exterior derivative | Proved identity under smooth diffeomorphism assumptions |
| FEEC Gram formula | Correct under declared metric and basis conventions |
| Discrete codifferential formula | Exact finite-dimensional identity |
| Current incidence orientation | Mismatch reported by independent audit; local regression/correction required |
| phi^2=phi+1 and psi^3=psi^2+1 | Exact algebra |
| Conforming phi/psi cubical refinement family | Open construction |
| Uniform commuting projections on benchmark family | Open |
| Mosco convergence for benchmark family | Open |
| Discrete compactness and harmonic stability | Open |
| Strong-/norm-resolvent convergence | Open; norm resolvent needs extra compactness |
| Golden/supergolden improvement of FEEC constants | Candidate; requires explicit template estimates |

This note supplements, and does not replace, INDEPENDENT_MATHEMATICAL_AUDIT.md and CONSISTENT_FEEC_MASS.md. Golden and supergolden constants are exact algebraic tools for a possible refinement family, not unexplained weights in the metric, mass matrices, or differential.


## 11. The missing geometric bridge: repeated 2D -> 3D promotion

This section is structural. The three-dimensional FEEC complex must not be introduced as a direct algebraic extension of a 2D graph. The geometric passage from planar data to spatial geometry has to be made explicit first, and the same passage must be checked at every refinement level.

The research thread associated in the project notes with **Sergy Gerasmioff** belongs here. The exact bibliographic identity/spelling and the precise source construction still need to be pinned to a primary reference; no formula should be attributed to that name until the source is supplied and checked. The mathematical bridge below records the project construction that must be audited, not a claim about the person's published theorem.

### 11.1 Stage I: planar seed and golden/supergolden deformation

Start with an oriented planar cell or rectangle
\[
X_2=(u,v),\qquad \rho=L/W.
\]
The golden/supergolden transition is encoded in the aspect parameter, with candidate endpoints \(\rho=\varphi\) and \(\rho=\psi\), where
\[
\varphi^2=\varphi+1,\qquad \psi^3=\psi^2+1.
\]
Use an explicit planar deformation \(S_\rho:\widehat\Omega_2\to\Omega_2(\rho)\), and define the induced metric
\[
g^{(2)}_\rho=(DS_\rho)^TDS_\rho.
\]
The determinant and singular values of \(DS_\rho\) must be bounded uniformly over the allowed interval of \(\rho\). The symbols \(\varphi,\psi\) select geometries; they do not themselves establish metric ellipticity.

### 11.2 Stage II: extrinsic lift into three dimensions

A planar deformation is not yet a 3D geometry. Define an immersion
\[
X_3(u,v)=\bigl(X_2(u,v),\,f_\rho(u,v)\bigr)\in\mathbb R^3
\]
or, more generally, a cellwise lift with an explicitly specified normal component. Its first fundamental form is
\[
g^{(3)}_{ab}=\partial_aX_3\cdot\partial_bX_3
=g^{(2)}_{ab}+\partial_af_\rho\,\partial_bf_\rho.
\]
This identity is exact. It shows precisely how a 2D metric is promoted by an extrinsic height field. The induced metric remains positive definite if the planar map is an immersion; quantitative conditioning requires uniform bounds on \(DS_\rho\) and \(\nabla f_\rho\).

For a genuine three-dimensional volume mesh, one further needs a third independent coordinate or a thickening map
\[
\mathcal F_\rho(u,v,w)=X_3(u,v)+w\,n_\rho(u,v),
\]
with a well-defined unit normal \(n_\rho\), nonvanishing Jacobian, and compatible face maps. This is the step that produces a 3D cell map for the cubical FEEC construction. A surface immersion alone only produces a 2D manifold embedded in 3D; it does not produce a 3D volume complex.

### 11.3 Stage III: rank completion and the 2D-to-3D obstruction

For each local triple \(T\), let \(R_T\) encode the planar data and let \(Q\) be the relevant planar quadratic form. Then
\[
\Gamma_T=R_T^T Q R_T
\]
has rank at most two whenever \(R_T\) maps into a two-dimensional plane. Therefore a third spatial direction cannot be obtained by relabelling coordinates: it requires a geometrically defined normal contribution.

A candidate rank-completing lift recorded in the project notes is
\[
V_T=E_pS_\rho R_T+\alpha\,n_p c_T^T,
\qquad
c_T=\bigl(\det(r_y,r_z),\det(r_z,r_x),\det(r_x,r_y)\bigr)^T.
\]
Here \(r_x,r_y,r_z\) are the three planar projected vectors associated with the triple, \(n_p\) is the chosen unit normal, and \(E_p\) embeds the planar frame in the ambient frame. The determinant minors form the cofactor/area-normal data. If the planar part has rank two, \(n_p\) is independent of its image, and \(\alpha\ne0\) with \(c_T\ne0\), the lift can have rank three. This is a conditional linear-algebra statement; the precise dimensions, frame conventions, and geometric meaning of each factor must be fixed in the implementation/proof before it is used as a theorem.

The project notes identify 216 \(W(G_2)\) triplettes as a possible finite family on which to test this rank-completion mechanism. That count and group action must be tied to an explicit enumerated set and verified; it is not a substitute for the rank and orientation proof.

### 11.4 Stage IV: 3D de Rham complex and FEEC

Only after the 3D cell map \(\mathcal F_\rho\) is proved to be orientation-preserving, uniformly nondegenerate, and face-compatible should the 3D reference de Rham spaces be transported by the covariant Piola pullback. The resulting local Gram matrices use the 3D pullback metric and its exterior powers exactly as in Sections 2 and 4.

The crucial commuting diagram is
\[
\begin{array}{ccc}
\widehat V^k & \xrightarrow{d} & \widehat V^{k+1}\\
\downarrow \mathcal F_\rho^{-\,*} && \downarrow \mathcal F_\rho^{-\,*}\\
V_h^k & \xrightarrow{d} & V_h^{k+1}.
\end{array}
\]
It follows from naturality of pullback once the map and orientation conventions are correct. It does not follow from a spectral match between a 2D graph and a 3D polyhedron.

### 11.5 Stage V: repeated promotion across refinement levels

The phrase “2D to 3D repeated” must be interpreted as a level-compatible construction. For every refinement level \(n\), require a commuting family of planar maps \(S_{\rho,n}\), lifts \(\mathcal F_{\rho,n}\), and refinement maps \(R_n\), with:
- uniform lower/upper singular-value bounds for \(DS_{\rho,n}\) and \(D\mathcal F_{\rho,n}\) after scaling;
- nonzero Jacobian with fixed orientation;
- matching traces and normals on shared faces;
- compatibility of refinement with the lift, at least up to a controlled geometric defect tending to zero;
- uniform bounds on derivatives required by the FEEC approximation operators.

The desired diagram is not merely \(d\)-commuting. The geometric refinement and lift should also commute:
\[
\mathcal F_{\rho,n+1}\circ \widehat R_n
\approx R_n^{(3)}\circ\mathcal F_{\rho,n},
\]
with an explicitly estimated defect. If the defect is zero, the construction is exactly compatible; if not, prove it is small in the norm relevant to the metric and mass perturbations.

This is where the \(\psi\)-scale recurrence can be used for the sequence of levels, while \(\varphi\) may determine the internal planar split. Their roles are distinct: \(\varphi\) controls a candidate within-cell proportion; \(\psi\) controls a candidate inter-level scale recurrence.

### 11.6 Consequence for the main theorem

Add the following prerequisite to H1 (geometry): **H0 — repeated 2D-to-3D geometric promotion.** There must exist a level-compatible planar family, an explicit immersion/thickening into 3D, and uniform nondegeneracy, orientation, and face-compatibility estimates. Only then can H1–H8 be applied to the resulting 3D cubical mesh family.

The proof order is therefore revised:
1. identify and reconstruct the Gerasmioff source construction and its exact 2D-to-3D map;
2. prove planar metric bounds for the \(\varphi/\psi\) deformation;
3. prove immersion/thickening and rank-three completion;
4. prove level-to-level compatibility and uniform shape regularity;
5. verify the local incidence/orientation identity;
6. establish FEEC masses, projections, compactness, and Mosco convergence.

Without Steps 1–4, the 3D curvilinear FEEC theorem has no justified geometric input from the proposed 2D construction.


### 11.3.1 The actual \(W(G_2)\) planar-to-spatial construction

The project construction is more specific than a generic graph lift. For each planar triple \(T_p\), use
\[
R_{T_p}=(r_x\ r_y\ r_z)\in\mathbb R^{2\times3},\qquad
c_{T_p}=
\begin{pmatrix}
\det(r_y,r_z)\\
\det(r_z,r_x)\\
\det(r_x,r_y)
\end{pmatrix}.
\]
The cofactor identity is
\[
R_{T_p}c_{T_p}=0.
\]
With the \(G_2\) quadratic form
\[
Q_{G_2}=\begin{pmatrix}2&-3\\-3&6\end{pmatrix},
\qquad
S_\rho=\begin{pmatrix}\sqrt\rho&0\\0&1/\sqrt\rho\end{pmatrix},
\]
the planar Gram datum is
\[
\Gamma_p(\rho)=R_{T_p}^{T}S_\rho^{T}Q_{G_2}S_\rho R_{T_p}.
\]
The candidate family uses the 216 \(W(G_2)\) triples and reports 20 Gram classes. Those counts/classes are finite-computation claims: they must be regenerated from the explicit root/triple enumeration and checked under the declared group action before being treated as verified facts.

Choose an orthonormal planar frame \(E_p\in\mathbb R^{3\times2}\), \(E_p^TE_p=I_2\), and a unit normal \(n_p\) with \(E_p^Tn_p=0\). The rank-completing spatial frame is
\[
V_{T_p}(\rho)=E_pS_\rho R_{T_p}
+\alpha(\rho)n_pc_{T_p}^{T}\in\mathbb R^{3\times3}.
\]
Its Gram matrix is
\[
G_{T_p}^{(3)}(\rho)=V_{T_p}^{T}V_{T_p}
=R_{T_p}^{T}S_\rho^{T}S_\rho R_{T_p}
+\alpha(\rho)^2c_{T_p}c_{T_p}^{T}.
\]
The mixed terms vanish because \(E_p^Tn_p=0\). In the orthonormal frame \((E_p,n_p)\), the determinant lemma gives
\[
\det V_{T_p}(\rho)=\alpha(\rho)\|c_{T_p}\|^2,
\qquad
\boxed{\det G_{T_p}^{(3)}(\rho)=\alpha(\rho)^2\|c_{T_p}\|^4.}
\]
Thus the planar \(2\times3\) data, whose rank is at most two, acquire rank three precisely when \(\alpha(\rho)\ne0\) and \(c_{T_p}\ne0\). Since \(\det S_\rho=1\), the golden/supergolden anisotropic rescaling does not itself change this volume factor. This is an exact algebraic identity under the stated frame assumptions; it is not yet a proof that the resulting cells form a conforming 3D mesh. The function \(\alpha(\rho)\), its normalization, and uniform lower/upper bounds must be specified from the source construction, not fitted after the fact.

### 11.5.1 Möbius seam: boundary identification and the normal coordinate

The second repeated operation is the boundary-to-seam identification. At level \(n\), set \(m=2^n\) and identify the right and left boundary indices by
\[
(i,j)_{\rm right}\sim(0,m-1-j)_{\rm left},
\qquad
\pi_n\!\left(h_n(m-1,j)\right)=h_n(0,m-1-j).
\]
This is a transverse reversal, not ordinary periodic identification. In local coordinates \((s,t)\) on a strip, the continuum model is
\[
(s_{\rm right},t)\sim(s_{\rm left},-t).
\]
For a spatial thickening with normal coordinate \(w\), the compatible Möbius transition is
\[
(s_{\rm right},t,w)\sim(s_{\rm left},-t,-w).
\]
The normal reversal is essential: it is the transition law for the twisted normal coordinate and prevents one from silently treating the Möbius seam as an untwisted product cylinder.

With local frame coordinates ordered as (longitudinal, transverse, normal), one convenient transition matrix is
\[
R_M=\operatorname{diag}(1,-1,-1),\qquad R_M^2=I,\quad\det R_M=+1.
\]
The discrete frame and link data must obey
\[
V_{\pi_n(p)}=V_pR_M,\qquad
U_{\pi_n(p)\pi_n(q)}=R_MU_{pq}R_M^{-1}.
\]
If the implementation stores only the 2D tangent frame, its transition is instead \(\operatorname{diag}(1,-1)\), with determinant \(-1\); do not mix these two representations. Verify the seam identities on every identified boundary cell, edge, and face, including the induced orientation of the 3D volume cells.

The resulting construction has three logically separate maps:
1. \(T_p\mapsto\Gamma_p(\rho)\): planar \(G_2\) metric/Gram data;
2. \(r_i\mapsto v_i\), assembled as \(R_{T_p}\mapsto V_{T_p}(\rho)\): rank-two planar data lifted to rank three;
3. boundary \(\mapsto\) Möbius seam: the index involution and twisted normal/frame transition.

The 3D FEEC domain must be the actual orientable thickened cell complex with these transition rules, not the nonorientable mid-surface regarded as a 3D volume. Prove that the thickened cells have positive Jacobian in compatible local charts and that seam-related face traces agree. A Möbius mid-surface alone is not a 3D volume mesh.

### 11.7. Named source and attribution status

The project associates this repeated 2D-to-3D construction with **Sergy Gerasmioff**. The source identity and spelling are not independently established by the public-source search performed for this revision, and the repository search for Gerasmioff returned no matching file. Therefore:
- retain the name as the user's source attribution and research lead;
- do not claim that the equations above are a published Gerasmioff theorem until a primary source is located;
- compare the original source line-by-line against the three maps and seam law above when it is available;
- preserve any differences rather than silently replacing the historical construction with this algebraic reconstruction.

### 11.8. Revised proof order

The correct order is now:
1. recover and authenticate the Gerasmioff source and its repeated 2D-to-3D construction;
2. enumerate the 216 \(W(G_2)\) triples and verify the 20 Gram classes;
3. prove \(R_Tc_T=0\), the rank-completion determinant identity, and uniform bounds for \(\alpha(\rho)\);
4. implement and verify the Möbius boundary involution, twisted normal transition, and link conjugation;
5. prove that the thickened 3D cells are conforming, orientable, and uniformly nondegenerate;
6. verify local incidence/exterior-derivative orientation;
7. only then establish 3D FEEC mass stability, commuting projections, compactness, and Mosco convergence.
