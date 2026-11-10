# Unitary theory of the truncated-icosahedral shell: barycentric statistics, special functions, phases, structured deformations and RGS–PRISM–Q6

**Date:** 10 November 2026  
**Repository:** `fabianleonaressi95/theorem`  
**Role:** canonical integration document for the mathematical work assembled on 10 November 2026. The theorem files cited below retain their individual proofs and assumptions; this document specifies how they fit together, what the connecting maps are, and which global statements remain open.

## Abstract

The programme has one geometric carrier and several mathematically distinct but compatible descriptions. The carrier is a truncated-icosahedral shell, decomposed into pentagonal and hexagonal panels and then into triangular cells. On each triangle, a Dirichlet/Gamma–Beta measure defines weighted barycentres, covariance tensors and controlled phase moments. Digamma and polygamma derivatives are the parameter-response calculus of this measure; zeta and Bernoulli values enter through exact special-function identities and asymptotic expansions. The same local cell moments provide a quadrature interface for bulk energy densities of structured-deformation type. Morandotti's theory supplies the bulk/interfacial variational framework under its own Euclidean hypotheses, while the curved closed-shell extension remains a separate homogenisation problem.

The RGS–PRISM–Q6 programme supplies finite geometric, topological and spectral comparison structures: Q6 point-cloud moments, cubical chain maps, Anti-Twin involution, Möbius phase action and Walsh spectrum. These structures are not automatically the same measure or mesh as the football shell. The required bridge is an explicit, geometry- and measure-compatible transfer map. The modular/arithmetic strand is connected exactly through Dedekind eta, Weber class invariants, the discriminant (-31), Dirichlet (L)-functions, Dirichlet eta and the supergolden algebraic number. The spherical-spectrum strand, including Ikeda's binary-tetrahedral quotient and the separate binary-icosahedral (2I) programme, supplies finite-group spectral benchmarks, not a hidden derivation of the modular identities.

The resulting theory is **unitary as an organized mathematical architecture**, not as a claim that every object is one and the same operator or that every proposed bridge has already been proved.

## 1. Epistemic and notational rules

Every result is assigned one of five statuses:

1. **PROVED / EXACT:** an identity or theorem under explicitly stated assumptions.
2. **FINITE EXACT COMBINATORICS:** exact incidence, rank, chain-map or representation identities on a specified finite object.
3. **NUMERICALLY VERIFIED:** a reproducible finite computation with stated data, normalization and precision.
4. **CONDITIONAL INTERFACE:** a valid local formula or variational identity whose global application requires additional compactness, convergence or geometric hypotheses.
5. **OPEN / CANDIDATE:** a proposed map, physical interpretation or continuum theorem not yet established.

Do not identify the following different objects merely because they share notation or tensor rank:

- triangle-cell covariance \(\Sigma_{F,a}\), Q6 point-cloud covariance \(\Sigma_X\), and six-cube vertex covariance;
- the fixed 64-site fourth moment S.4 and the refinement-stencil fourth jump moment S.5;
- the Dirichlet parameter gradient \(\nabla_a\), the surface spatial gradient \(\nabla_S\), and the modular derivative \(q\,d/dq\);
- Dedekind's modular eta, Dirichlet's alternating eta, a Dirichlet (L)-function, Dedekind zeta, and a Dirichlet probability distribution;
- the structured-deformation field (G), the shell metric, and the fourth-moment tensor;
- the canonical Q6 antipode XOR 63 and the RGS seed coordinate inversion XOR 7;
- the binary tetrahedral group (T^*) and the binary icosahedral group (2I).

## 2. Geometric carrier: truncated icosahedron and triangular shell

### 2.1 Panel complex

The truncated icosahedron has the combinatorial data
\[
(V,F_5,F_6,E)=(60,12,20,90),
\]
namely 60 panel vertices, 12 pentagons, 20 hexagons and 90 physical panel seams. Fan-triangulating each panel gives
\[
12\cdot5+20\cdot6=180
\]
triangular CST facets. With one centre node per panel, the shell model has 92 nodes (60 shared vertices plus 32 panel centres). The recorded discrete shell model also has 270 dihedral hinges. These counts refer to different entities: panel seams, CST edges/facets, shell nodes and bending hinges must not be conflated.

The panel network carries pentagon/hexagon constitutive contrast, orthotropic membrane stiffness, signed-dihedral bending and seam reinforcement. Positive panel stiffnesses and nonnegative graph coupling give the recorded positive-definiteness result for the panel-network quadratic form. The model's parameters remain demonstration inputs until scan geometry and material/coupon measurements are supplied.

### 2.2 Geometric constants

The square-corner tangency lemma S.1 gives, for \(\delta_S=1+\sqrt2\),
\[
R:d:r=1:\delta_S^{-1}:\delta_S^{-2},\qquad r=d^2/R.
\]
The S.2 construction places square/silver, pentagonal/golden, hexagonal/bronze and supergolden algebraic identities in a common geometric discussion. The component identities are exact in their own configurations; a common circle, shared polynomial or visual arrangement does not by itself prove a common incidence law, a refinement operator or a physical dynamics. The labelled incidence construction that would derive the supergolden scale from the panel geometry remains open. The related T056 record proves permutation similarity of the Phase-21 and trigram three-state transfer matrices, hence equality of their characteristic polynomial and Perron root; it does not provide a geometric cell intertwiner between the two constructions.

The cube/sphere radial excess, cubic harmonic anisotropy and pentagon/hexagon constitutive contrast are also distinct mechanisms. They are not identified without an explicit map.

## 3. The local probabilistic geometry: Gamma, Beta and barycentric moments

Let \(F\) be a nondegenerate planar triangle with ordered vertices (v_0,v_1,v_2), area (A_F), diameter (h_F), vertex matrix (V) (rows are the vertices), and barycentric coordinate vector \(\lambda=(\lambda_0,\lambda_1,\lambda_2)\). For parameters (a_i>0), put (S=a_0+a_1+a_2). The weighted partition function is
\[
Z_F(a)=\int_F\prod_{i=0}^2\lambda_i^{a_i-1}\,dA
=2A_F B_3(a)
=2A_F\frac{\prod_i\Gamma(a_i)}{\Gamma(S)}.
\]
After normalization, \(\lambda\) has the Dirichlet distribution with parameter (a). Its mean and covariance are
\[
m_i=\mathbb E[\lambda_i]=\frac{a_i}{S},\qquad
C_{ij}=\frac{a_i(S\delta_{ij}-a_j)}{S^2(S+1)}.
\]
The physical barycentre and covariance are therefore
\[
c_{F,a}=V^{\mathsf T}m,\qquad
\Sigma_{F,a}=V^{\mathsf T}CV.
\]

For (a=(1,1,1)), (Z_F=A_F), the barycentre is the ordinary triangle centroid and T070 reduces to T068. For every (g\in C^3) on a neighbourhood of \(F\),
\[
\int_F g\,d\mu_{F,a}
=g(c_{F,a})+\frac12D^2g(c_{F,a}):\Sigma_{F,a}+R_{F,a},
\qquad
|R_{F,a}|\leq\frac{h_F^3}{6}\sup_F\|D^3g\|_{op}.
\]
The identity is exact for polynomials of degree at most two. This is the local mathematical core of the shell quadrature construction.

**Established:** T068 (uniform covariance quadrature) and T070 (weighted Dirichlet barycentre/covariance/phase moments) are proved local triangle theorems. They do not yet imply a global error bound over the 180 facets of an actual measured shell, nor convergence of a refining shell family.

## 4. Digamma, trigamma, zeta, Bernoulli and gradients

### 4.1 Parameter gradients and cumulants

Since
\[
\log B_3(a)=\sum_i\log\Gamma(a_i)-\log\Gamma(S),
\]
the parameter derivatives are
\[
\partial_{a_i}\log B_3(a)=\psi(a_i)-\psi(S)
=\mathbb E_a[\log\lambda_i],
\]
\[
\partial_{a_i}\partial_{a_j}\log B_3(a)
=\delta_{ij}\psi_1(a_i)-\psi_1(S)
=\operatorname{Cov}_a(\log\lambda_i,\log\lambda_j).
\]
Thus the digamma is the first parameter-response function and the trigamma is the Hessian/cumulant response. This logarithmic covariance is different from the ordinary barycentric covariance (C=\operatorname{Cov}(\lambda)) used to construct (\Sigma_{F,a}).

The spatial derivative of a shell energy density is a separate derivative. If
\[
g(X)=W(X,\nabla_Su(X),G(X),\theta(X),\nabla_S\theta(X)),
\]
then (D^2g) contains the chain-rule contributions from the spatial variable and the fields/field gradients. T068/T070 apply once this composite (g) has the required (C^3) regularity and bounded derivatives. No identification \(\partial_{a_i}=\nabla_S\) is made.

### 4.2 Exact special-function chain

The Euler Beta/Gamma identities and the alternating Dirichlet eta function give
\[
B(x,y)=\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)},\qquad
\eta_D(s)=(1-2^{1-s})\zeta(s),
\]
and, for (\Re s>0),
\[
\Gamma(s)\eta_D(s)
=\int_0^\infty\frac{x^{s-1}}{e^x+1}\,dx.
\]
The even zeta values satisfy
\[
\zeta(2n)=(-1)^{n+1}\frac{B_{2n}(2\pi)^{2n}}{2(2n)!},
\]
so Dirichlet eta values at positive even integers are explicit Bernoulli multiples. The digamma/polygamma asymptotics also contain Bernoulli coefficients, for example
\[
\psi(z)\sim\log z-\frac1{2z}
-\sum_{k\ge1}\frac{B_{2k}}{2kz^{2k}}.
\]
These are exact special-function identities and asymptotic expansions. They do not automatically become coefficients of an irregular football-mesh refinement: that requires an explicit summation rule, a refinement family and a separate Euler–Maclaurin argument including boundary terms.

### 4.3 Digamma sampled on the supergolden scale

Let (\psi_*>0) denote the supergolden algebraic number (to avoid confusing it with the digamma function):
\[
\psi_*^3-\psi_*^2-1=0,\qquad \psi_*^3=\psi_*^2+1.
\]
The Gamma recurrence gives the exact identity
\[
\psi_{dig}(\psi_*^3)-\psi_{dig}(\psi_*^2)=\psi_*^{-2}.
\]
For (d_n=\psi_{dig}(\psi_*^n)), the digamma asymptotic gives
\[
d_{n+1}-d_n\longrightarrow\log\psi_*.
\]
Gauss multiplication is valid for integer (m), including (m=3); it cannot be used with the noninteger (m=\psi_*). The algebraic relation for (\psi_*) does not imply an additive recurrence for (d_n). A digamma-derived Q6 refinement operator with characteristic polynomial (x^3-x^2-1) remains a candidate, not a theorem.

## 5. Modular eta, Weber invariants and the arithmetic field of discriminant (-31)

Dedekind's modular eta is
\[
\eta_{Ded}(\tau)=q^{1/24}\prod_{n\ge1}(1-q^n),\qquad q=e^{2\pi i\tau}.
\]
It is not the Dirichlet eta \(\eta_D(s)\). Its logarithmic q-expansion is
\[
\log\eta_{Ded}(\tau)=\frac{\pi i\tau}{12}
-\sum_{n\ge1}\sigma_{-1}(n)q^n,
\]
with Dirichlet generating series \(\sum_n\sigma_{-1}(n)n^{-s}=\zeta(s)\zeta(s+1)\). Differentiation yields (q(d/dq)\log\eta_{Ded}=E_2/24), with coefficients \(\sigma_1(n)\) and Dirichlet series \(\zeta(s)\zeta(s-1)\).

For (K=\mathbb Q(\sqrt{-31})), the reduced forms give (h_K=3), and
\[
\zeta_K(s)=\zeta(s)L(s,\chi_{-31}),\qquad
\eta_D(s)L(s,\chi_{-31})=(1-2^{1-s})\zeta_K(s).
\]
The quadratic residues modulo 31 sum to 186 and the nonresidues sum to 279, hence
\[
\sum_{a=1}^{30}a\chi_{-31}(a)=-93,qquad
L(1,\chi_{-31})=\frac{3\pi}{\sqrt{31}}.
\]
Since (\eta_D(1)=\log2), the regularized product value is
\[
\eta_D(1)L(1,\chi_{-31})=\frac{3\pi\log2}{\sqrt{31}}.
\]

For the principal Weber class invariant, the user's reported full-text check of Yui–Zagier's (D=-31) table (p. 1649) records
\[
\rho^3+\rho-1=0,\qquad \rho=\psi_*^{-1}.
\]
The reciprocal identification \\(\\rho=\\psi_*^{-1}\\) is an algebraic reconstruction from the tabulated polynomial, not terminology used by Yui–Zagier. The exact Weber transformations then give
\[
f(i\sqrt{31})=\sqrt2\,\psi_*,\qquad
f(i\sqrt{31})^2=2\psi_*^2.
\]
The CM point \((-1+i\sqrt{31})/2\) has discriminant (-31), whereas (i\sqrt{31}) has order discriminant (-124); the Weber transformation, not equality of CM points, is the bridge. The published class-polynomial entry supports the principal-invariant statement; Yui–Zagier's stronger all-classes conjugacy assertion is explicitly conjectural. The plastic constant is not \(\psi_*\), and fundamental-unit status is not claimed.

This arithmetic branch is genuinely connected to the Gamma/Beta/zeta branch through Dirichlet series, (L)-functions and the same discriminant field. It is not a statement that the modular eta function equals the probability normalizer or the Dirichlet eta function.

## 6. Veneziano Beta function: exact identity, limited interpretation

The Veneziano-type amplitude uses
\[
A(s,t)\propto B(-\alpha(s),-\alpha(t))
=\frac{\Gamma(-\alpha(s))\Gamma(-\alpha(t))}
{\Gamma(-\alpha(s)-\alpha(t))}.
\]
This is an exact Beta/Gamma application and a useful analytic example. It does not identify a football-shell phase integral with a string scattering amplitude. Such an identification would require an explicit variable map, analytic domain, normalization and an observable-level theorem.

## 7. Phase field and Möbius action

For a real affine phase on one triangle,
\[
\theta(x)=\theta(c_{F,a})+k\cdot(x-c_{F,a}),
\]
T070 gives
\[
\mathbb E_a[e^{i\theta(X)}]
=e^{i\theta(c_{F,a})}
\left(1-\frac12k^{\mathsf T}\Sigma_{F,a}k+\rho(k)\right),
\quad |\rho(k)|\leq\frac{|k|^3h_F^3}{6}.
\]
This is a controlled small-cell phase moment, not a dynamical law.

On Q6, the half-angle coordinate (u=\tan(\phi/2)) makes phase translation a Möbius map:
\[
u\mapsto\frac{u+\tan(\delta/2)}{1-u\tan(\delta/2)}.
\]
A vertex phase field induces (U_{vw}=e^{i(\phi_w-\phi_v)}), an exact pure-gauge connection with unit holonomy on every cycle. On an equal-proper-time slice (U_{vw}=1). Its graph Laplacian has Walsh spectrum
\[
0^{(1)},2^{(6)},4^{(15)},6^{(20)},8^{(15)},10^{(6)},12^{(1)},
\]
and the canonical graph antipode XOR 63 splits the vertex space into even/odd sectors of dimension 32+32. No nontrivial physical holonomy or (\varphi)-/(\psi_*)-dependent spectrum follows from this canonical flat connection.

## 8. Q6/RGS finite geometry and the transfer-map problem

### 8.1 Three different covariance structures

The archived RGS 64-point seed has numerical normalized covariance \(\Sigma_X=5I_3/4\). Its coordinate inversion is XOR 7. The canonical graph antipode of Q6 is XOR 63. T069 proves the pair mean/difference law of total covariance for any fixed-point-free involution:
\[
\operatorname{Cov}(X)=\frac1{32}\sum_i d_id_i^{\mathsf T}
+\frac1{32}\sum_i(m_i-\bar m)(m_i-\bar m)^{\mathsf T}.
\]
The six-cube vertex measure has covariance \(I_6/4\). Neither is the triangle-cell covariance (\Sigma_{F,a}). Their relation needs an explicit push-forward or transfer map.

### 8.2 Cubical topology and Anti-Twin

Q6 has 64 vertices, 192 edges and 240 square 2-cells. For the truncated cubical 2-skeleton, \(B_1B_2=0\), \(\operatorname{rank}B_1=63\), \(\operatorname{rank}B_2=129\), \(b_1=0\), and \(b_2=111\). The 111 two-cycles are killed by the omitted 3-cells in the full six-cube. Bitwise complement induces signed involutions on vertices, edges and squares and satisfies the exact chain-map identities in T071. The NL/NLT synchronization dynamics are an exploratory cubical adaptation of a simplicial source model; hysteresis in that simulation is not industrial constitutive hysteresis.

### 8.3 Earlier Q6 subdivision and the supergolden operator

T055 proves the specified dyadic midpoint subdivision chain maps. Its restriction to the three selected directions is \(2I_3\), not the supergolden companion matrix
\[
A_* = \begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix},\qquad \det(xI-A_*)=x^3-x^2-1.
\]
The same cubic appears in the T056 transfer-matrix conjugacy and in the Weber/supergolden arithmetic, but no derivation of \(A_*\) from T055 or from a digamma-generated refinement operator is claimed. The latter is an explicit open construction problem.


### 8.4 Gate D to Gate E and the football transfer

The shell has 92 nodes and 180 triangular facets; Q6 has 64 vertices and 240 square faces. There is no canonical bijection from these counts. The bridge must be a pair of explicit maps on the relevant chain/field spaces, with orientation, incidence, geometry, metric and measure compatibility stated.

- **Gate D / Kathara–Q6:** the recorded PR #195 identities \(B_1R_1=R_0B_1^K\) and \(B_2R_2=R_1B_2^K\), the 10/10 face correspondence and the \(240\times10\) map \(R_2\) of rank 10 modulo 1,000,003 establish the stated finite chain-map result. They do not establish \(O_h\)-equivariance, canonical RGS metric, a shell embedding or spin transport.
- **Gate E.1 / barycentric quadrature:** T068 (THEOREM PR #127) and T070 provide the local triangle moment and quadrature laws. The companion RGS–QLG implementation was integrated through PR #196 (`src/barycentric_triangle_quadrature.py`, `tests/test_barycentric_triangle_quadrature.py`, and `docs/GATE_E1_BARYCENTRIC_COVARIANCE_QUADRATURE.md`). These are local mathematical/software results; Gate E.1 does not by itself prove global embedding or continuum convergence.
- **Football transfer robustness:** PR #124 and its merged audit compare the football triplet transfer under the declared finite model. This is a finite robustness result, not a proof that the 92-node shell and 64-state Q6 are spectrally identical.

The correct Gate D→E statement is therefore a **composition programme**: first a finite chain/field transfer with declared conventions; then local geometric quadrature on actual shell facets; then uniform refinement estimates and a continuum limit. Each arrow has its own proof obligations.

### 8.5 RGS 188D and PRISM comparison modules

The RGS 188-dimensional operator audit and the PRISM/Krist-All graph records are retained as separate finite-dimensional comparison modules. The 188D audit records the \(O_h\)-commutation and tangent/bulk decomposition under its archived matrix conventions; its negative and quasi-zero eigenvalue sectors are spectral properties of that operator, not a proof of a shell continuum limit. The PRISM graph record \(C_{64}\square C_6^3\square C_5\) has \(N=69120\), degree 10, 1,920 active vertices, 108 length-640 cycles, \(b_1=5\), \(b_2=10\), spectral gap \(0.009630546656\), and the recorded Krist-All residual \(5.22\times10^{-16}\). The supergolden relation \(K^3=K^2+I\) is an exact algebraic identity for the specified matrix. These values belong to the PRISM graph/operator data; they are not invariants of the 92-node football shell or the 64-vertex Q6 cube unless an explicit transfer theorem is supplied.


## 9. Fourth moments and constitutive branches

Keep the fourth-moment objects separate.

1. **S.4 fixed-seed fourth moment:** the fully symmetric rank-four moment of the 64-site RGS cloud. The recorded seed has \(M^{(2)}=80I_3\), isotropic fourth-moment coefficient \(c=67.4361954632\), and residual components \(R_{xxxx}=-6.3213417395\), \(R_{xxyy}=3.1606708698\). Its \(E_g\) and \(T_{2g}\) eigenvalues are numerical seed values, not exact symbolic constants. A fully symmetric rank-four tensor is not torsion.
2. **S.5 refinement jump moment:** for the graph stencil, the fourth jump moment enters the \(a^2\) term of the Taylor expansion. Under vanishing first/third moments, second-moment metric consistency, bounded fourth moments and uniform \(C^5\) control, it gives a conditional second-order consistency result. It is not the S.4 fixed-cloud tensor.
3. **S.6 connection current:** varying the positive fourth-moment gradient energy gives the local \(SO(3)\) current \(J_i=\kappa[H(D_iQ),Q]\). Complete TEGR/coframe equations and flat-connection constraints remain open.
4. **S.7 Maxwell obstruction:** the direct contraction \(R_{ijkl}F_{ij}F_{kl}\) vanishes for antisymmetric \(F\). The independent STF order parameter \(Q\) is the viable intermediate; the constitutive matrices and the \(A_4\) intertwiner application remain partly open.
5. **S.8 coframe variation:** the displayed algebraic coframe action has the recorded variation but contains no coframe derivatives and therefore does not generate torsion.

The fourth-moment branch is an independent constitutive/variational module of the unified shell programme; it is not an identification with the Dirichlet covariance, Morandotti disarrangement tensor or a modular function.

## 10. Spherical spectra and finite-group benchmarks

### 10.1 Binary tetrahedral quotient (S^3/T^*): Ikeda

For the unit three-sphere, degree-(\ell) scalar harmonics have eigenvalue (\ell(\ell+2)). In Ikeda's binary-tetrahedral formula the index is (\ell=2k), hence
\[
\lambda_k=4k(k+1).
\]
Proposition 3.1(2) gives four cyclic subgroups of order 6 and three of order 4, all sharing the central (C_2). Inclusion–exclusion gives
\[
|T^*|=4(6-2)+3(4-2)+2=24,
\]
and the normalized Poincaré average is
\[
F_{T^*}=F_6+\frac12F_4-\frac12F_2.
\]
The independent Molien series is
\[
M(t)=\frac1{24}\left[
\frac1{(1-t)^2}+\frac1{(1+t)^2}+\frac6{1+t^2}
+\frac8{1-t+t^2}+\frac8{1+t+t^2}
\right]
=\frac{1+t^{12}}{(1-t^6)(1-t^8)}.
\]
It gives
\[
m_{2k}=1+2\lfloor k/3\rfloor+\lfloor k/2\rfloor-k,
\qquad a_k=(2k+1)m_{2k}.
\]
For example (a_3=7) and (a_6=26). This is S011: the quoted multiplicity formula and subgroup/Poincaré statements are source-recorded from Ikeda (1995); the eigenvalue indexing and Molien series are independent reconstructions/checks. It concerns (S^3/T^*), not (S^3/2I).

### 10.2 Binary icosahedral quotient (S^3/2I)

The separate (2I) strand uses the binary icosahedral group of order 120, Peter–Weyl decomposition and its own Molien/Hilbert-series calculation. The recorded first nonzero scalar eigenvalue is (168) with multiplicity (13), under the unit-sphere and quotient conventions in the corresponding theorem record. It must not be conflated with the binary-tetrahedral (T^*) calculation above. Neither finite-group spectrum, by itself, proves a map from the football shell or Q6 to a spherical space form.

## 11. Integrated variational architecture

The preceding modules can be assembled into a *candidate shell functional* without pretending that its global limit is already proved. For a triangulated shell \(\mathcal T_h\), let (u_h,\theta_h) be fields and ((g_h,G_h)) a structured-deformation pair. A representative discrete energy is
\[
\mathcal E_h(u_h,\theta_h,g_h,G_h)
=\sum_{F\in\mathcal T_h}
\int_F W_F(X,\nabla_Su_h,G_h,\theta_h,\nabla_S\theta_h)\,dA
+\sum_{e\in\mathcal S_h}
\int_e\varphi_e([g_h],\nu_e,\theta_h)\,d\mathcal H^1
+\mathcal E_h^{(4)}.
\]
Here \(\mathcal S_h\) is the set of physical panel seams, \(\varphi_e\) is a separately specified interface density, and \(\mathcal E_h^{(4)}\) is included only when a fourth-moment constitutive law has been independently defined. No particular constitutive formula is asserted by this schematic expression.

On each facet, T068/T070 give a controlled quadrature for the bulk integral:
\[
\int_F W_F\,dA
=Z_F(a_F)\left[
W_F(c_{F,a_F})+
\frac12D^2W_F(c_{F,a_F}):\Sigma_{F,a_F}
+R_{F,a_F}
\right],
\]
after fixing the reference weight and regularity. The seam term is not absorbed into the cell covariance. A Morandotti-type relaxation would then require a proof for the chosen bulk and interface densities, the correct growth/homogeneity assumptions, compactness, a liminf inequality and a recovery sequence. The existing Euclidean periodic theorem cannot simply be relabelled as a theorem on a closed curved shell.

## 12. The actual unifying theorem programme

The rigorous target is a *conditional convergence theorem*, not the assertion that all modules are already one theorem.

**Target theorem (open):** Let \(\mathcal T_h\) be a shape-regular family of triangulations of a fixed closed shell, with coherent transfer maps from the discrete Q6/Kathara data, uniformly controlled Dirichlet parameters and phase fields, and bulk/interface densities satisfying suitable coercivity, growth, periodicity or ergodicity and surface-compatibility assumptions. Prove:

1. uniform cell-moment and quadrature bounds, including summable Taylor remainders;
2. compactness of the interpolated fields and structured-deformation variables;
3. a liminf inequality for the bulk and seam/interface energies;
4. a recovery sequence;
5. compatibility of the finite chain maps and discrete operators with the limiting surface differential structure;
6. convergence of the relevant fourth-moment/stencil operators under separately stated moment assumptions;
7. spectral convergence only after specifying the operator, measure, metric, quotient and transfer-map hypotheses.

**Status: OPEN.** Shape regularity, the actual refinement family, the shell-to-Q6 transfer, surface structured-deformation compactness, seam/jump-set treatment, and Mosco/spectral convergence have not all been established. The theorem is the unifying research target; it is not a result claimed today. The formal hypothesis list and separate target conclusions (global quadrature, structured-deformation Gamma limit, Mosco limit and spectral convergence) are registered as [T073 — Unified football-shell / RGS–PRISM–Q6 limit programme](../theorems/T073-unified-football-shell-rgs-prism-limit-program.md).

## 13. Repository map: source records to preserve

| Module | Record | Status |
|---|---|---|
| Silver/golden/bronze/supergolden geometry | S.1, S.2 | Exact component geometry; common incidence/refinement derivation open |
| Barycentric covariance quadrature | T068 | Proved local Euclidean theorem |
| Q6 point cloud, antipodes and Walsh sectors | T069 | Exact finite identities + numerical seed audit |
| Dirichlet barycentres, covariance and phase moments | T070 | Proved local triangle theorem |
| Q6 cubical topology and Anti-Twin | T071 | Exact finite chain identities; dynamics exploratory |
| Möbius phase and flat Q6 connection | T072 | Exact finite graph theorem; nontrivial transport open |
| Weber–Dedekind eta / supergolden class invariant | S.9 | Exact transformations plus published class-polynomial input; scope caveat retained |
| Dirichlet eta, (L)-function, quadratic zeta and Bernoulli | S.10 | Exact analytic identities; character sum (-93) |
| Binary tetrahedral spherical spectrum | S011 | Source-verified Ikeda formula + independent Molien check |
| RGS fourth moments | S.4–S.8 | Mix of exact tensor/variation identities and numerical seed data; physical constitutive closure open |
| Binary icosahedral (2I) spectra | T010 and associated records | Separate finite-group spectral programme |
| Morandotti structured deformations | bibliography and synthesis records | Euclidean source theorem; curved-shell extension open |

## 14. Open obligations and non-claims

1. Supply actual scan coordinates, panel-centre placement, material frames and coupon data for the 92-node/180-facet shell.
2. Prove a global error estimate over all facets and a compatible shape-regular refinement family.
3. Derive Bernoulli/Euler–Maclaurin coefficients from the actual shell refinement summation rule; do not infer them from the appearance of Gamma or zeta.
4. Specify a non-circular transfer from 92 shell nodes/180 facets to 64 Q6 states/240 squares, including chain, metric, measure and field compatibility.
5. Complete the curved-surface Morandotti/structured-deformation compactness, liminf and recovery proof, and distinguish physical seams from jump sets.
6. Verify the actual RGS/PRISM stencil moments at every refinement level; relate S.4 to S.5 only through an explicit map.
7. Derive any nontrivial phase holonomy from supplied geometric transport or vertex proper-time data; the canonical equal-time Q6 connection is flat and trivial.
8. Keep the (T^*) and (2I) quotient spectra separate and state all sphere/metric/volume conventions.
9. Independently derive the (D=-31) Weber class polynomial if a proof independent of the published Yui–Zagier table is required.
10. Do not claim a Veneziano-shell identity, a physical supergolden constant, a torsion interpretation of the symmetric fourth moment, or an industrial hysteresis law without the missing derivation/data.

### Companion records and evidence

- [Integrated moments/barycentres/Gamma–Beta–zeta/Morandotti synthesis](SYNTHESIS_MOMENTS_BARYCENTRES_GAMMA_BETA_ZETA_MORANDOTTI_2026-11-10.md).
- [Dedekind–Dirichlet eta and Weber–supergolden construction](UNITARY_DEDEKIND_DIRICHLET_ETA_BARYCENTRIC_RGS_MORANDOTTI_2026-11-10.md).
- [Digamma–supergolden–Q6 analytic dossier](DIGAMMA_SUPERGOLDEN_Q6_PROGRAM_2026-11-10.md).
- [Independent numerical replay report](../reports/2026-11-10_integrated_synthesis_numerical_replay.md); numerical replay is not a pytest/CI pass.
- [PDF source inventory and audit](../audits/2026-11-10_pdf_repository_audit.md).
- [Special-functions and Morandotti bibliography](../bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md).

## 15. Primary references and repository sources

- A. Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Mathematical Journal* 18 (1995), 57–67, especially Proposition 3.1(2), p. 63 Poincaré series, Theorem 4.4. Publisher PDF: https://www.jstage.jst.go.jp/article/kodaimath1978/18/1/18_1_57/_pdf/-char/en.
- N. Yui and D. Zagier, “On the Singular Values of Weber Modular Functions,” *Mathematics of Computation* 66 (1997), 1645–1662, DOI 10.1090/S0025-5718-97-00854-5.
- R. Schertz, “Weber's class invariants revisited,” *Journal de théorie des nombres de Bordeaux* 14 (2002), 325–343, DOI 10.5802/jtnb.361.
- NIST Digital Library of Mathematical Functions, §§5.11, 5.12, 5.15, 23.15, 23.18, 24.2, 25.2 and 25.15.
- A. V. Sutherland, MIT 18.785 Lecture 19, “The Analytic Class Number Formula” (2021).
- T. P. Minka, “Estimating a Dirichlet Distribution” (2000; revisions through 2012).
- Amar–Matias–Morandotti–Zappale (2022), “Periodic Homogenization in the Context of Structured Deformations,” *Zeitschrift für angewandte Mathematik und Physik* 73, article 173, DOI 10.1007/s00033-022-01817-6. Apply only under the paper's stated Euclidean periodic hypotheses.
- Barroso–Matias–Morandotti–Owen (2017), relaxed disarrangement densities; preserve the distinction (M=\nabla g-G).
- Ghorbanchian–Restrepo–Torres–Bianconi (2021), “Higher-order simplicial synchronization of coupled topological signals,” *Communications Physics* 4, 120, DOI 10.1038/s42005-021-00605-4; Q6 square-cell dynamics are this project's cubical adaptation.
- The repository records T068–T072, S.1–S.10 and S011, plus the 10 November numerical replay and PDF-source audit.

**Editorial rule:** every new identity, law, theorem or numerical coincidence must be placed in its own record with assumptions, proof/evidence, status and source; this document is the canonical dependency map. A chat-level observation is not a theorem until it is recorded and audited.
