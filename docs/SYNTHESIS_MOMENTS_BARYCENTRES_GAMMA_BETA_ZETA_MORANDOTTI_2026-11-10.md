# Integrated synthesis: moments, barycentres, special functions and Morandotti

**Date:** 10 November 2026  
**Repository:** `fabianleonaressi95/theorem`  
**Purpose:** consolidate the identities, proved lemmas, discrete laws, geometric coincidences, numerical records and open bridges developed across the RGS/Q6, fourth-moment, football-shell and Morandotti work. This document is an index and synthesis, not a claim that every cross-domain interpretation has been proved.

## 1. Epistemic key

Every statement belongs to one of these classes:

- **Exact identity:** follows algebraically or from a standard special-function identity.
- **Proved theorem/lemma:** includes hypotheses and a proof in its own record.
- **Exact finite combinatorics:** exact counts or chain identities on a specified finite complex.
- **Numerically verified:** depends on a specific archived seed, mesh, code or floating-point calculation.
- **Structural coincidence:** two formulas share a form or invariant; the map between their objects must still be specified.
- **Candidate/open bridge:** a proposed connection for which the necessary map, limit theorem or physical interpretation is not established.

A source supports only the statement it actually proves. A numerical equality is not upgraded to an exact identity without a symbolic derivation.

## 2. The moment hierarchy: do not conflate the objects

### 2.1 Triangle-cell first and second moments

For a planar triangle (Fsubset\mathbb R^3), with vertices (v_0,v_1,v_2), area (A_F), and areal centroid
[
c_F=\frac{v_0+v_1+v_2}{3},
]
the normalized covariance is
[
\Sigma_F=\frac1{A_F}\int_F(x-c_F)(x-c_F)^T\,dA
=\frac1{12}\sum_{i=0}^2(v_i-c_F)(v_i-c_F)^T.
]
For (g\in C^3) on a neighbourhood of (F),
[
\int_Fg\,dA=A_Fg(c_F)+\frac{A_F}{2}D^2g(c_F):\Sigma_F+R_F,
\quad |R_F|\leq\frac{A_Fh_F^3}{6}\sup_F\|D^3g\|_{op}.
]
This is **T068**, a proved local Euclidean identity. The companion bridge repository records tests for centroid/covariance, polynomial exactness and the cubic remainder; do not claim a new execution unless the tests are actually run.

### 2.2 Weighted barycentres: Dirichlet/Gamma/Beta

For barycentric coordinates (\lambda_i\) on (F), positive parameters (a_i), (S=a_0+a_1+a_2), and (V) whose rows are the three vertices,
[
Z_F(a)=\int_F\prod_{i=0}^2\lambda_i^{a_i-1}\,dA
=2A_F\frac{\prod_i\Gamma(a_i)}{\Gamma(S)}.
]
The normalized measure has
[
\mathbb E[\lambda_i]=\frac{a_i}{S},\qquad
C_{ij}=\operatorname{Cov}(\lambda_i,\lambda_j)
=\frac{a_i(S\delta_{ij}-a_j)}{S^2(S+1)}.
]
Therefore
[
c_{F,a}=V^T\frac aS,\qquad \Sigma_{F,a}=V^TCV.
]
This is **T070**. Its uniform case (a=(1,1,1)) reduces to T068. The central implementation now includes the corrected Duffy–Gauss–Jacobi rule. Under the map \(\lambda_0=(1-s)(1-t),\lambda_1=s,\lambda_2=(1-s)t\), the Jacobi parameters are \((\alpha_s,\beta_s)=(a_0+a_2-1,a_1-1)\) and \((\alpha_t,\beta_t)=(a_0-1,a_2-1)\); each mapped rule carries its own \(2^{-(\alpha+\beta+1)}\) factor, and the physical triangle integral carries \(2A_F\). The code stores \(M=\mathbb E[\lambda\lambda^T]\) separately from \(C=M-\mathbb E[\lambda]\mathbb E[\lambda]^T\). A1–A3 regression tests are deposited; their execution is not claimed here.

### 2.3 Q6 point-cloud and antipodal covariances

Three different covariance objects must remain distinct:

1. The recovered 64-point RGS cloud has normalized covariance
   [
   \Sigma_X=\frac1{64}\sum_{v=0}^{63}X_vX_v^T=\frac54I_3
   ]
   in the archived seed audit (T069).
2. The six-dimensional cube-vertex measure has barycentre
   (X_B=(1/2,\ldots,1/2)) and covariance (\frac14I_6).
3. A triangle-cell covariance (\Sigma_F\) is a two-dimensional-support ambient tensor attached to one geometric facet.

T069 also proves the finite law of total covariance for any fixed-point-free involution (a):
[
\operatorname{Cov}(X)=\frac1{32}\sum_i d_id_i^T+
\frac1{32}\sum_i(m_i-\bar m)(m_i-\bar m)^T,
\quad m_i=\frac{X_i+X_{a(i)}}2,\quad d_i=\frac{X_i-X_{a(i)}}2.
]
For the recovered label convention, coordinate inversion is XOR 7, whereas the canonical Q6 graph antipode is XOR 63. They are not interchangeable.

The earlier Q6 coordinate-field FEM check reports energy 16 under its declared normalization. It is a separate discrete identity; it is not a triangle covariance theorem and does not prove a surface regularity estimate.

### 2.4 Fourth moments: two separate rank-four tensors

**(A) Fixed 64-site RGS seed (S.4).** Raw sums:
[
M^{(2)}=\sum_nx_nx_n^T=80I_3,\qquad
M^{(4)}_{ijkl}=\sum_nx_{n,i}x_{n,j}x_{n,k}x_{n,l}.
]
The full fourth moment is totally symmetric. Its isotropic projection in three dimensions is
[
M^{(4),iso}_{ijkl}=c(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}),
\quad c=\frac{M^{(4)}_{iikk}}{15}=67.4361954632.
]
The reported seed components are
[
M^{(4)}_{xxxx}=195.9872446501,\quad M^{(4)}_{xxyy}=70.5968663330,
]
[
R_{xxxx}=-6.3213417395,\quad R_{xxyy}=+3.1606708698.
]
The contraction (\mathcal A(Q)_{ij}=R_{ijkl}Q_{kl}) on (\operatorname{Sym}_0(3)) has reported cubic sectors (E_g): (-9.48201261) (multiplicity 2), and (T_{2g}): (+6.32134174) (multiplicity 3). These are **numerical seed records**, not exact symbolic values. (R) is fully symmetric and cannot be torsion, which is antisymmetric in its last two indices. Any constitutive action quadratic in (Q) remains a proposal until independently specified.

**(B) Fourth jump moment of a refinement stencil (S.5).** For
[
\Delta_af(x)=\frac1{a^2m_a(x)}\sum_yw_{xy}[f(x+a\xi_{xy})-f(x)],
]
the normalized jump moments (M_a^{(r)}=m_a^{-1}\sum_yw_{xy}\xi_{xy}^{\otimes r}) give
[
\Delta_af=\frac1aM_a^{(1)}:\nabla f+\frac12M_a^{(2)}:\nabla^2f
+\frac a6M_a^{(3)}:\nabla^3f
+\frac{a^2}{24}M_a^{(4)}:\nabla^4f+O(a^3).
]
With vanishing first and third moments, (\frac12M_a^{(2)}=g^{-1}+O(a^2)), bounded fourth moments and uniform (C^5) control, this yields second-order consistency. The fourth jump moment controls the leading (a^2) truncation term. It is **not** the fixed-cloud fourth moment in S.4.

The earlier continuum-to-discrete metric programme also recorded the conditional requirements: odd-moment cancellation, uniform fourth-moment control, (O(a^2)) metric consistency under H1–H6, and stronger (C^2)-type control before claiming curvature/Einstein convergence. These are hypotheses and proof obligations, not a completed curvature theorem.

### 2.5 Fourth-moment derivative, Maxwell and coframe branches

The fourth-moment work contains three further, distinct mathematical records:

- **S.6 — connection current:** shift the self-adjoint fourth-moment operator to a positive operator (H) on (operatorname{Sym}_0(3)), define (D_iQ=\partial_iQ+[\omega_i,Q]), and vary the positive gradient energy. The exact local current is (J_i=\kappa[H(D_iQ),Q]\in\mathfrak{so}(3)). This is a derived local variational identity; flat-connection constraints and complete TEGR/coframe equations remain open.
- **S.7 — Maxwell obstruction and common subgroup:** the direct contraction (R_{ijkl}F_{ij}F_{kl}) vanishes identically for antisymmetric (F). The viable intermediate is an independent STF tensor (Q), with (A(Q)=R:Q). The proposed electric/magnetic response matrices are candidate constitutive laws. The representation-theoretic bridge is only after restriction to a common tetrahedral (A_4), where the five-dimensional sectors split as (2\oplus3); an actual intertwiner matrix and connection compatibility are still required.
- **S.8 — algebraic coframe variation:** for (\mathcal L=N\sqrt h\,\frac{\lambda}{2}R_{abcd}Q^{ab}Q^{cd}), with (R,Q) held independent of the coframe, the first variations are explicit. Because this action contains no derivatives of the coframe, it does not generate torsion.

These records prevent three common errors: treating a fully symmetric rank-four moment as torsion, inserting it directly into an antisymmetric (RFF) contraction, or treating an algebraic coframe potential as a torsion-generating action.

### 2.6 Q6 cubical 2-skeleton, Anti-Twin and synchronization

The Q6 cubical 2-skeleton has 64 vertices, 192 edges and 240 square faces. With the stated integer orientations, \(B_1B_2=0\). Its graph cycle rank is 129; the square boundaries span that cycle space, so \(b_1=0\). Because this is the **truncated 2-skeleton**, with no 3-cells attached, \(b_2=240-129=111\). Those 111 classes are killed when the 3-cells of the full six-cube are attached. Do not confuse the truncated 2-skeleton with the contractible full cube.

The coordinatewise complement \(v\mapsto\mathbf1-v\), equivalently XOR 63, induces signed involutions \(J_0,J_1,J_2\) on vertices, edges and squares and satisfies the chain-map identities \(J_0B_1=B_1J_1\) and \(J_1B_2=B_2J_2\). This is the Anti-Twin cellular action recorded in T071.

The NL/NLT equations are adapted from Ghorbanchian–Restrepo–Torres–Bianconi (2021), equations (12)–(13) and (16)–(17), by replacing simplicial triangles with Q6 square 2-cells. That replacement is a cubical generalization made by this project, not a result of the cited paper. The numerical synchronization and hysteresis study is exploratory; it is not evidence of constitutive hysteresis in a real material. Preisach, Prandtl–Ishlinskii and Bouc–Wen models are reference constitutive simulators, not industrially identified material models.

### 2.7 Möbius phase action and flat Q6 connection

For \(u=\tan(\phi/2)\), a phase translation by \(\delta\) acts projectively as
\[
u\longmapsto\frac{u+\tan(\delta/2)}{1-u\tan(\delta/2)},
\]
with homogeneous matrix
\[
R(\delta)=
\begin{pmatrix}
\cos(\delta/2)&\sin(\delta/2)\\
-\sin(\delta/2)&\cos(\delta/2)
\end{pmatrix}.
\]
For a vertex phase \(\phi_v\), the edge transport \(U_{vw}=e^{i(\phi_w-\phi_v)}\) is exact and has unit holonomy on every closed cycle. On an equal-proper-time Q6 slice it reduces to \(U_{vw}=1\). Its covariant Laplacian is therefore gauge-conjugate to the ordinary Q6 graph Laplacian, whose Walsh eigenvalues are \(2|S|\) with multiplicity \(\binom6{|S|}\). The canonical graph antipode is XOR 63 and gives the even/odd Walsh sectors of dimensions 32+32 (T072).

This XOR 63 involution is the same bitwise complement used by the Anti-Twin chain map in T071. It is **not** the RGS seed coordinate inversion XOR 7 in T069. The three records describe compatible but different structures: cubical chain action (T071), pure-gauge phase transport and graph spectrum (T072), and the archived 64-point coordinate pairing (T069). None derives a nontrivial physical holonomy without additional vertex proper-time or geometric transport data.

## 3. Gamma, Beta, digamma, zeta and Bernoulli identities

The following chain is exact:

[
B(x,y)=\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)},\qquad
\psi(x)=\frac{d}{dx}\log\Gamma(x).
]
Gamma recurrence gives
[
\psi(x+1)=\psi(x)+\frac1x.
]
Reflection gives
[
\psi(1-x)-\psi(x)=\pi\cot(\pi x),
\quad
\pi\cot(\pi x)=\frac1x-2\sum_{n\ge1}\zeta(2n)x^{2n-1}
\]
in its convergence disk. Equivalently,
[
B(1+x,1-x)=\frac{\pi x}{\sin\pi x},\qquad
\log B(1+x,1-x)=\sum_{n\ge1}\frac{\zeta(2n)}n x^{2n},\quad |x|<1.
]
The even zeta values satisfy
[
\zeta(2n)=(-1)^{n+1}\frac{B_{2n}(2\pi)^{2n}}{2(2n)!}.
]
The digamma asymptotic is
[
\psi(z)\sim\log z-\frac1{2z}
-\sum_{k\ge1}\frac{B_{2k}}{2kz^{2k}}.
]
These are special-function identities/asymptotics, not an automatic Euler–Maclaurin expansion of an irregular mesh.

For the triangular Dirichlet partition function, differentiation with respect to parameters yields
[
\partial_{a_i}\log B_3(a)=\psi(a_i)-\psi(S)
=\mathbb E_a[\log\lambda_i],
]
[
\partial_{a_i}\partial_{a_j}\log B_3(a)
=\delta_{ij}\psi_1(a_i)-\psi_1(S)
=\operatorname{Cov}_a(\log\lambda_i,\log\lambda_j).
]
This is **S.3**. Parameter gradients (\partial_{a_i}) are not spatial gradients (\nabla_S); the distinction is essential when connecting to an energy density.

### Supergolden sampling

Let (s>0) solve (s^3-s^2-1=0). Then (s^3=s^2+1), and the exact digamma shift gives
[
\psi(s^3)-\psi(s^2)=s^{-2}.
]
For (d_n=\psi(s^n)), the asymptotic increment satisfies
[
d_{n+1}-d_n\longrightarrow\log s.
]
Gauss multiplication is valid for integer (m), in particular
[
\sum_{k=0}^{2}\psi\!\left(\frac{s^3+k}{3}\right)
=3\psi(s^2)+3s^{-2}-3\log3.
]
It is invalid to substitute the noninteger (m=s) into the multiplication formula. Nor does (s^{n+3}=s^{n+2}+s^n) imply an additive recurrence for the digamma sequence. See the 10 November special-function dossier.

### Bernoulli/Euler–Maclaurin boundary

Bernoulli coefficients arise in the asymptotic expansion of polygamma/Gamma and in Euler–Maclaurin summation. Applying Euler–Maclaurin to a shell refinement requires an explicit one-dimensional or structured summation rule with the necessary smoothness and boundary terms. An arbitrary irregular triangulation does not acquire Bernoulli coefficients merely because Gamma or zeta appears in a local integral.

## 4. Veneziano: exact Beta-function use, limited geometric claim

The Veneziano-type four-point amplitude is expressed through Euler Beta functions, conventionally
[
A(s,t)\propto B(-\alpha(s),-\alpha(t))
=\frac{\Gamma(-\alpha(s))\Gamma(-\alpha(t))}
{\Gamma(-\alpha(s)-\alpha(t))}.
]
This is an exact mathematical use of the Beta/Gamma relation in a physical amplitude. It motivates studying Beta integrals and their analytic continuation, but does **not** identify a football-shell phase integral with a string scattering amplitude. Such an identification would require an explicit variable map, analytic domain, normalization and a theorem relating the observables.

## 5.1 Right gauge / left fluid Bernoulli-gradient bridge

T077 fixes the sector convention: right = gauge bundle with \(D_A\Psi\); left = fluid with \(B_L=p+\frac12\rho|v|^2+\rho\Phi\). Their common geometric bridge is the cell centroid/Dirichlet barycentre and covariance tensor \(\Sigma_{F,a}\), not an identification of the fields. The directional gradient diagnostics are \((\nabla_SB_L)^T M_{F,a}\nabla_SB_L\) on the fluid side and the corresponding gauge-invariant contraction of \(D_A\Psi\) on the gauge side. T068/T070 give the exact local Taylor/covariance correction for each sector density. Bernoulli numbers in Gamma/polygamma asymptotics remain distinct from Bernoulli's fluid law. The anisotropic kinetic metric and the PRISM-to-fluid/gauge coupling are candidate models, not established physical laws.

## 5. Gradients, barycentres and the Morandotti interface

For a smooth bulk density on a surface,
[
g(X)=W(X,\nabla_Su(X),G(X),\theta(X),\nabla_S\theta(X)),
]
T068/T070 provide cellwise integration formulae when the composed density has the required regularity. Their Hessians contain chain-rule contributions from spatial and field-gradient dependence. They do not themselves prove compactness or homogenisation.

For structured deformations, keep the variables distinct:
[
(g,G)\in SBV\times L^1,\qquad M=\nabla g-G.
]
Here (G) is the matrix field in the structured-deformation pair, not the metric tensor (J^TJ). The curl of (M) has a Burgers/dislocation interpretation in the cited theory, but this does not make the fully symmetric S.4 fourth moment a torsion or dislocation tensor.

The Morandotti programme contains three separate mathematical layers:

1. **Planar incompatible elasticity/Airy:** equilibrium, incompatibility sources, Airy potential and cell problems.
2. **Structured-deformation homogenisation:** bulk and interfacial relaxed densities under periodicity, growth, homogeneity and domain assumptions.
3. **Curved shell application:** a new surface version is needed, with tangent gradients, surface measure, seams/interfaces, constitutive laws and a proof of compactness, liminf and recovery.

A seam in the football mesh is not automatically a jump set (J_g). A quadratic seam law is not automatically covered by a 1-homogeneous interfacial density. A theorem on Euclidean Lipschitz domains is not automatically a theorem on a closed curved shell.

## 6. Football geometry and panel mechanics already recorded

The discrete truncated-icosahedron panel model has
[
(V,F_5,F_6,E)=(60,12,20,90),
]
with 90 physical panel seams, 180 fan-triangulated CST facets, 92 shell nodes including panel centres, and 270 dihedral hinges. These are distinct counts and should not be conflated.

The existing orthotropic-shell model contains CST membrane stiffness, signed-dihedral bending, seam reinforcement and a linearised equilibrium solve. Its parameters are demonstration inputs unless independently measured. The panel-network anisotropy audit proves positive definiteness for positive panel stiffnesses and nonnegative graph coupling; it does not validate a real ball without scan/coupon data.

The cube/sphere radial excess (\chi_{CS}=\|n\|_\infty^{-1}-1), the cubic harmonic (H_4=n_x^4+n_y^4+n_z^4-3/5), and the pentagon/hexagon constitutive contrast are distinct mechanisms. The existing documentation explicitly avoids identifying them.

## 7. Exact geometric coincidences and algebraic constants

Existing records S.1 and S.2 retain the square/diagonal silver-ratio geometry, regular pentagon golden-ratio chords, regular hexagon bronze-ratio metric and supergolden algebraic relation. These are geometric/algebraic identities within their stated constructions. A common circle or a shared polynomial is not by itself a dynamical or physical equivalence.

The supergolden matrix
[
A_s=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix},
\quad \det(\lambda I-A_s)=\lambda^3-\lambda^2-1
]
is an exact combinatorial/algebraic object. The digamma scale sampling does not yet derive this matrix. Midpoint Q6 subdivision T055 restricts to (2I_3), not (A_s).

## 8. Repository cross-index

| Record | Mathematical content | Status |
|---|---|---|
| T055 | Exact Q6 dyadic subdivision chain maps | Proved finite combinatorics |
| T063–T067 | Quaternion/SU(2)/SO(3), gauge holonomy, cubical subdivision/naturality, face conformity and Stokes commuting interpolation | Exact identities under stated conventions |
| T068 | Uniform triangle centroid/covariance quadrature | Proved local theorem |
| T069 | Q6 antipodal pair covariance and Walsh sectors | Exact finite identities + seed numerical audit |
| T070 | Dirichlet weighted barycentres, covariance and phase moments | Proved local theorem |
| T077 | Bernoulli-gradient barycentre bridge: right gauge / left fluid sectors | Exact local moment input + candidate coupled anisotropy |
| T071 | Q6 cubical 2-skeleton, Anti-Twin chain action and NL/NLT benchmark | Exact finite chain identities; exploratory dynamics and hysteresis remain non-physical/unvalidated |
| T072 | Möbius phase translation, exact vertex-phase connection and Q6 spectrum | Exact finite-graph identities; canonical equal-time connection is trivial |
| S.1–S.2 | Silver/bronze/golden/supergolden geometric synthesis | Exact geometry/algebra under stated construction |
| S.3 | Dirichlet log-partition gradients and cumulants | Proved special-function lemma |
| S.4 | 64-site RGS fourth-moment anisotropy | Prior seed numerical record + exact tensor algebra |
| S.5 | Fourth jump moment and graph Laplacian consistency | Proved conditional Taylor lemma |
| S.6 | Fourth-moment SO(3) connection current | Proved local variational identity; complete teleparallel dynamics open |
| S.7 | Fourth-moment Maxwell obstruction and A4 bridge | Exact no-go/representation identities; constitutive and intertwiner applications partly open |
| S.8 | Fourth-moment algebraic coframe variation | Proved for the displayed action; full gravitational equations open |
| T040–T045 | Barnes zeta, twisted Gamma reduction, individual zeta poles | Existing theorem/audit records; do not duplicate |
| T048–T054 | Mosco changing spaces and further geometric/analytic records | Preserve their individual statuses; open convergence obligations remain open |

## 9. Open proof obligations — explicit, not hidden

1. The 64-site seed loader reproduces the archived coordinate-array SHA-256. An independent numerical replay in this synthesis turn recovered M^(2)=80 I_3, the listed M^(4)/R components, the E_g/T_2g eigenvalues and the O_h residual. The imported pytest suite remains unexecuted; retain the distinction between this replay and a test-suite pass.
2. Verify the actual RGS/Q6/PRISM stencil moments (M_a^{(1)},\ldots,M_a^{(4)}) for every refinement level and establish uniform bounds.
3. Define a common map, if any, between the fixed-seed fourth moment S.4 and the refinement jump moment S.5.
4. Derive any Bernoulli/Euler–Maclaurin coefficients from the actual refinement summation rule.
5. Prove a curved-surface structured-deformation result: compactness, lower bound and recovery sequence; specify whether seams are prescribed interfaces or jump sets.
6. Use actual scan and material/coupon data before claiming a physical explanation of football anisotropy.
7. Do not identify the Veneziano amplitude, a phase integral, a Q6 phase, torsion, curvature or a Morandotti defect density without explicit maps and proofs.

### 9.1 Numerical replay record

The independent finite-seed, Dirichlet quadrature, fourth-moment variation and Q6 cubical checks performed during this synthesis are collected in [the 10 November numerical replay report](../reports/2026-11-10_integrated_synthesis_numerical_replay.md). This is explicitly separate from a pytest/CI pass and does not include the real football-shell scan or a continuum/Mosco verification.

## 9.2 Binary-tetrahedral spectrum (Ikeda)

The source-verified spectrum of the binary tetrahedral quotient is now recorded in [S011](../theorems/S011-ikeda-binary-tetrahedral-spectrum.md). The index convention is \(\ell=2k\), giving \(\lambda_k=4k(k+1)\); the Poincaré average is \(F_{T^*}=F_6+\tfrac12F_4-\tfrac12F_2\), and the independently reconstructed Molien series is \(M(t)=(1+t^{12})/((1-t^6)(1-t^8))\). This is the (S^3/T^*) result and is separate from the binary-icosahedral (S^3/2I) programme. Ikeda does not support a Weber/Dedekind-eta connection.

## 9.3 Dedekind eta, Dirichlet eta and the discriminant \(-31\)

The modular and arithmetic eta constructions are now integrated in a separate dependency document:
[Unified Dedekind–Dirichlet eta, Weber–supergolden, barycentric and RGS–Morandotti construction](UNITARY_DEDEKIND_DIRICHLET_ETA_BARYCENTRIC_RGS_MORANDOTTI_2026-11-10.md).

The two new records are:
- [S.9 — Weber–Dedekind eta class invariant and the supergolden root](../theorems/S009-weber-dedekind-eta-supergolden-class-invariant.md): the \(D=-31\) Weber class invariant \(\rho\) satisfies \(\rho^3+\rho-1=0\), hence \(\rho=1/\psi\); the Weber transformations give \(f(i\sqrt{31})=\sqrt2\psi\).
- [S.10 — Dirichlet eta, Dedekind eta Lambert series and quadratic zeta](../theorems/S010-dirichlet-eta-lambert-series-quadratic-zeta.md): exact Dirichlet-series products, \(\zeta_K(s)=\zeta(s)L(s,\chi_{-31})\), the class-number value and Bernoulli/polygamma links.

These records keep the modular eta, alternating Dirichlet eta, Dirichlet \(L\)-function, Dedekind zeta and Dirichlet simplex distribution distinct.

## 9.4 Canonical integrated theory

The canonical dependency map for the entire 10 November programme is now [the unitary theory of the truncated-icosahedral shell, Gamma–Beta–zeta, Morandotti and RGS–PRISM–Q6](UNIFIED_THEORY_FOOTBALL_GAMMA_BETA_ZETA_MORANDOTTI_RGS_PRISM_Q6_2026-11-10.md). It assembles the shell geometry, T068–T072, S.1–S.10, the fourth-moment branch, the Gate D→E transfer programme, and the separate (T^*)/(2I) spectral modules while keeping each proof status intact.

## 9.5 Phase–theta–zeta–barycentric spectral bridge

[T078](../theorems/T078-phase-theta-zeta-barycentric-spectral-bridge.md) adds the exact Dirichlet characteristic function of an affine lifted barycentric phase, its Lauricella-series representation and first two moments. It separates this local transform from the global topological sectors of the shell. For the closed truncated-icosahedral cellulation, (V-E+F=60-90+32=2), hence (H_1(S^2;\mathbb Z)=0): the 31 seam-graph cycles are generated by panel boundaries and do not define independent flat holonomy sectors. The distinct integer sectors are line-bundle Chern classes (c_1\in H^2(S^2;\mathbb Z)\cong\mathbb Z). A quadratic weight over these sectors gives a candidate unary theta series, conditional on deriving the gauge action and normalization. Punctures/defects would change (H_1), but seams alone are not punctures. The Jacobi theta-constant product identity gives the standard Dedekind eta relation. A zeta-regularized determinant still requires a specified elliptic operator, domain, seam conditions and zero-mode prescription; no automatic football-shell eta identity is claimed.

## 10. Bibliography

The special-function and Morandotti sources newly catalogued for this synthesis are in [the special-functions and Morandotti bibliography](../bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md). The wider 55-record Morandotti publication map is in [MATRICE_BIBLIOGRAFICA_MORANDOTTI_RGS_PRISM.md](../manuscripts/MATRICE_BIBLIOGRAFICA_MORANDOTTI_RGS_PRISM.md).

**Editorial rule:** future results in this programme must be deposited first as a theorem/lemma/identity record with assumptions, proof or evidence, scope and bibliography; then indexed here and in the README. Never leave a result only in chat.
