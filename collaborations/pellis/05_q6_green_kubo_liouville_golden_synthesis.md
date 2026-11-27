# Pellis collaboration — Q6 foundations, Green–Kubo transport, Liouville–Bergman geometry, and golden hierarchies

**Date:** 2026-11-27  
**Purpose:** integrative technical note for the proposed collaboration with Stergios Pellis.  
**Status:** synthesis of existing theorem records and explicit open bridges. This document does not promote model identities to physical laws and does not claim a derivation of the fine-structure constant.

## 1. Why begin with the 64 hexagrams?

The combinatorial starting point is the set of all 64 six-line binary patterns conventionally called the hexagrams. Encode each line by a bit:
\[
x=(x_1,\ldots,x_6)\in\{0,1\}^6.
\]
The six bits can be grouped into a lower trigram and an upper trigram:
\[
x=(\ell,u),\qquad \ell,u\in\{0,1\}^3.
\]
Thus the state set is the six-dimensional Boolean cube
\[
V(Q_6)=(\mathbb Z_2)^6,\qquad |V(Q_6)|=2^6=64.
\]

For the mathematical model used here, two states are adjacent when exactly one line changes:
\[
x\sim y\iff d_H(x,y)=1.
\]
This is a declared mutation rule. It should not be confused with a claim that every traditional ordering or interpretive system of the I Ching uses this adjacency.

The resulting graph has degree six and
\[
|E(Q_6)|=\frac{64\cdot6}{2}=192.
\]
Its elementary cubical square faces number
\[
|F_2(Q_6)|=\binom62 2^{6-2}=240.
\]

The distinction between the graph and its cubical filling matters. As a one-dimensional graph, its cycle-space dimension is
\[
\beta_1^{\rm graph}=192-64+1=129.
\]
After the 240 square 2-cells and their boundary relations are included, one is studying a different chain complex. In particular, the graph cycle rank must not be reported as the first Betti number of the filled cubical complex.

### 1.1 Exact spectrum

Let \(L_{Q_6}\) be the unweighted combinatorial Laplacian. Walsh characters diagonalize it:
\[
\operatorname{spec}(L_{Q_6})
=\{(2k)^{\binom6k}:k=0,\ldots,6\}.
\]
Explicitly,
\[
0^{(1)},\ 2^{(6)},\ 4^{(15)},\ 6^{(20)},\
8^{(15)},\ 10^{(6)},\ 12^{(1)}.
\]
This is an exact theorem about the Boolean hypercube. The eigenspaces are the Walsh-degree sectors, not empirical frequency bands.

The two trigram factors are also explicit:
\[
Q_6=Q_3^{\rm lower}\square Q_3^{\rm upper},\qquad
L_{Q_6}=L_-\otimes I+I\otimes L_+,
\]
up to the declared tensor-index ordering. There are 96 edges changing a lower-trigram line and 96 changing an upper-trigram line.

**Interpretive boundary.** The 64 states and their adjacency form a finite combinatorial model. A physical interpretation as microscopic configurations, charges, atoms, or spacetime points requires additional observables, units, dynamics and calibration. None is assigned by the hexagram label alone.

**Primary records:** theorems/T099-shao-yong-q6-kirchhoff-network.md, theorems/T108-boolean-influences-q6-laplacian-cohomology.md, theorems/T114-q6-gauge-covariant-cubical-dirac-kaehler.md, theorems/T117-six-square-mobius-subcomplex-of-q6.md, theorems/T143b-original-archive-q6-plaquettes.md.

## 2. Discrete gradients, barycentres, moments and resistance

There are several distinct gradient and barycentric results in the repository. They should be kept separate rather than compressed into one purported universal law.

### 2.1 Graph gradient and Poisson/Green operator

For an oriented Q6 edge \(e=(v,w)\), define
\[
(d_0 f)(e)=f(w)-f(v).
\]
With the counting inner products, the graph Laplacian is
\[
L_0=d_0^*d_0.
\]
For a mean-zero source \(b\), the equation
\[
L_0u=b,\qquad \mathbf1^Tb=0
\]
has the unique mean-zero solution \(u=L_0^\dagger b\), where \(L_0^\dagger\) is the Moore–Penrose inverse. The effective resistance between vertices is
\[
R_{\rm eff}(v,w)
=(e_v-e_w)^TL_0^\dagger(e_v-e_w).
\]
These are standard finite graph identities; their use in a physical circuit requires a declared conductance and capacitance model.

### 2.2 Embedded least-squares shape gradient and local resistance

T130 treats a different construction. Given a declared planar shape coordinate \(x_v=\Phi(v)\in\mathbb R^2\), a scalar vertex field \(f_v\), and positive edge weights \(\omega_{vw}\), set
\[
G_v=\sum_{w\sim v}\omega_{vw}(x_w-x_v)(x_w-x_v)^T,
\quad
b_v=\sum_{w\sim v}\omega_{vw}(x_w-x_v)(f_w-f_v).
\]
When \(G_v\) is positive definite, define
\[
\nabla_{Q6}f(v)=G_v^{-1}b_v.
\]
For an affine field \(f(x)=a\cdot x+c\), this reconstructs \(a\) exactly whenever the projected local star spans \(\mathbb R^2\).

For positive quadrature weights \(w_i\), the barycentre is
\[
x_c=\frac{\sum_iw_ix_i}{\sum_iw_i}.
\]
For local tractions \(t_i\), the resultant and moments satisfy
\[
F_h=\sum_iw_it_i,\quad
M_o=\sum_iw_i(x_i-o)\times t_i,\quad
M_c=M_o-(x_c-o)\times F_h.
\]
This is an exact change-of-origin identity. The geometric barycentre is not automatically a centre of mass or centre of hydrodynamic resistance.

For local kinematic Jacobians \(J_i\) and symmetric positive-definite drag tensors \(D_i\), the declared local-drag model has
\[
R_h=\sum_iw_iJ_i^TD_iJ_i,\qquad
qdot^TR_hqdot\ge0.
\]
Its Schur complement gives the force-free body response under the stated hypotheses. This proves positive dissipation for that local model; it is not a nonlocal Stokes/BEM theorem.

### 2.3 Barycentric quadrature on a triangle

T068 is a separate local Euclidean theorem. For a nondegenerate planar triangle \(F\), areal barycentre \(c_F\), and normalized covariance
\[
\Sigma_F=\frac1{A_F}\int_F(x-c_F)(x-c_F)^T\,dA,
\]
one has
\[
\Sigma_F=\frac1{12}\sum_{i=0}^2(v_i-c_F)(v_i-c_F)^T.
\]
For \(g\in C^3\) on a neighbourhood of \(F\),
\[
\int_Fg\,dA
=A_Fg(c_F)+\frac{A_F}{2}D^2g(c_F):\Sigma_F+R_F,
\]
with
\[
|R_F|\le \frac{A_Fh_F^3}{6}\sup_F\|D^3g\|.
\]
For quadratic \(g\), the formula is exact. This is a local cell quadrature theorem; it does not by itself prove a global surface-refinement or continuum convergence result.

### 2.4 Gradient–barycentre kinematics for defects

T097 packages a conditional reconstruction law for planar Frank–Burgers defect closure. The rotation is recovered from the orientation-preserving microscopic gradient \(G\) through its polar factor:
\[
G=R_GU_G,\qquad
\theta_G=\operatorname{atan2}(G_{21}-G_{12},G_{11}+G_{22}).
\]
The Frank winding is the circulation of the frame angle around a loop, provided the frame and chart transitions are handled correctly. The translational closure is associated with the circulation of the structured-gradient mismatch. Barycentric centroids and covariance tensors control cell sampling and anisotropic corrections.

This is not the assertion that a centroid displacement alone is a Burgers vector. The integrated discrete/continuum bridge retains its stated calibration and convergence obligations.

**Primary records:** theorems/T068-barycentric-covariance-quadrature-law.md, theorems/T079-morandotti-surface-gradient-barycentre-bridge.md, theorems/T097-barycentric-kinematic-frank-burgers-law.md, theorems/T098-two-circle-positive-gradient-negative-barycentre-duality.md, theorems/T130-q6-discrete-gradients-barycentres-resistance.md.

## 3. Green–Kubo: what is proved and what is not

Green–Kubo is not a single graph identity. It is an equilibrium linear-response formula whose observable, dynamics, normalization and limiting procedure must be specified.

### 3.1 Exact hypercube OU benchmark

For a mean-zero vector process on Q6, consider the reversible Ornstein–Uhlenbeck model
\[
dX_t=-\gamma L_0X_t\,dt+
\sqrt{2\gamma\sigma^2L_0}\,dW_t,
\qquad \gamma>0,
\]
restricted to the mean-zero subspace. Its stationary covariance is \(\sigma^2I\). For \(J_t=b^TX_t\), with \(\mathbf1^Tb=0\),
\[
C_J(t)=\sigma^2b^Te^{-\gamma L_0t}b.
\]
Let \(P_k\) be the orthogonal projector onto the eigenvalue-\(2k\) Walsh sector. Then
\[
C_J(t)=\sigma^2\sum_{k=1}^6e^{-2\gamma kt}\|P_kb\|^2
\]
and
\[
\boxed{
\int_0^\infty C_J(t)\,dt
=\frac{\sigma^2}{2\gamma}
\sum_{k=1}^6\frac{\|P_kb\|^2}{k}.
}
\]
This is an exact Green–Kubo-type integral for the declared reversible OU model. It is not automatically a material viscosity: \(b\) has to be derived from a microscopic stress or flux, and the physical volume, units and normalization must be supplied.

### 3.2 Phonon–phason stress response

T131 defines the finite generalized normal-mode problem
\[
Ke_\alpha=\omega_\alpha^2Me_\alpha,\qquad
K=K^T,\quad M=M^T\succ0,
\]
and specifies what is needed before a Q6 motif can be interpreted as a material vibrational model: a physical embedding, mass matrix, force-constant Hessian, and (for dispersion) a periodic or quasiperiodic wavevector family.

For total extensive stress \(\Pi_{ij}\), the classical equilibrium formula is
\[
\eta_{ij,kl}
=\frac1{k_BT V}\int_0^\infty
\langle\delta\Pi_{ij}(t)\delta\Pi_{kl}(0)\rangle_{\rm eq}\,dt,
\]
provided the correlation integral and relevant limits exist. Phonon, phason and mixed stress terms must be derived from a common Hamiltonian; they are not presumed independent. The phonon-only symmetric-stress sector has 18 channels when three sectors and six Voigt components are used. Phason strain can have a different number of independent components and must not be forced into the phonon Voigt convention.

T132 supplies an exact two-coordinate reversible OU benchmark. With \(H(q)=\frac12q^TKq\), \(K\succ0\), and centered quadratic observables
\[
\Pi_a(q)=\frac12(q^TS_aq-\operatorname{tr}(S_a\Sigma)),
\quad \Sigma=k_BT K^{-1},
\]
Wick's identity gives
\[
C_{ab}(t)=\frac12\operatorname{tr}[S_aE(t)S_bE(t)^T],
\quad E(t)=e^{-\mu Kt}\Sigma.
\]
All nine ordered phonon/phason/interaction sector-pair correlations recombine exactly into the total-stress correlation. This is an exact Gaussian benchmark, not a calibrated material.

The hierarchy of claims is therefore:
- **proved under the model hypotheses:** finite OU covariance, correlations and integrated response;
- **not yet established:** that the Q6 variables are calibrated microscopic material degrees of freedom;
- **open:** derive the Hessian, phason kinetics and stress observables from one physical Hamiltonian, then prove finite-size and long-time convergence and identify the continuum transport coefficient.

T100 and the Q6–Green–Kubo scale note give additional graph/charge and scale analyses. In particular, the graph Green operator and a Green–Kubo time integral are not interchangeable without a dynamical model and a specified observable.

**Primary records:** theorems/T100-hypercube-moire-green-kubo-defects.md, theorems/T131-q6-phonon-phason-green-kubo-transport.md, theorems/T132-coupled-phonon-phason-ou-green-kubo.md, theorems/Q6_GREEN_KUBO_KRYSTALLO_SCALE_BRIDGE_2026-11-23.md, projects/Q6-HYPERCUBE-STORA-ZUMINO-GREEN-KUBO.md.

## 4. PRISM cycle cover and the Krist-All boundary

The ambient PRISM graph is
\[
G_{\rm PRISM}=C_{64}\square C_6\square C_6\square C_6\square C_5,
\]
with
\[
|V|=64\cdot6^3\cdot5=69\,120,\qquad
\deg=10,\qquad |E|=345\,600.
\]
Its product-graph Laplacian has the separated spectrum
\[
\lambda(k_1,\ldots,k_5)
=4\sum_{r=1}^5\sin^2(\pi k_r/n_r),
\quad(n_1,\ldots,n_5)=(64,6,6,6,5),
\]
and spectral gap \(4\sin^2(\pi/64)\).

A deterministic 108-cycle cover of length 640 is already constructed and audited in scripts/audit_prism_108_cycles.py. The construction starts with a Hamiltonian 320-cycle in \(C_{64}\square C_5\), takes pairs of adjacent \(C_6\)-layers, deletes the same base edge in both copies, and cross-connects the two paths. The three disjoint coordinate pairs in one \(C_6\) factor and the \(6\times6\) choices of the other two \(C_6\) coordinates give
\[
3\cdot6\cdot6=108
\]
cycles. The script checks simplicity, every closing/interior graph edge, pairwise vertex-disjointness and complete coverage:
\[
108\cdot640=69\,120.
\]
Reproduce with:
~~~bash
python scripts/audit_prism_108_cycles.py
python -m pytest tests/test_prism_108_cycles.py -q
~~~

**Proved scope:** existence of a deterministic vertex-disjoint 108-cycle cover of the declared Cartesian-product graph.

**Open provenance question:** whether this is the same distinguished 108-cycle family in the historical Pellis/PRISM computation. The construction is a valid explicit cycle cover; the original historical generator or ordered cycle list is needed to establish identity with that earlier family.

The Krist-All record must remain separate. The exact \(3\times3\) Phase-21 and trigram matrices are permutation-conjugate (T056), both with characteristic polynomial
\[
x^3-x^2-1.
\]
This proves equivalence of those two abstract three-state linear systems after a cyclic change of ordering. It does not derive the matrix from Kathara/Krist-All cell subdivision.

The reported 11,725 Krist-All classes and residual \(5.22\times10^{-16}\) remain historical claims until the class equivalence relation, canonical representative encoding, enumerator, exact operator and residual normalization are supplied. A small companion matrix satisfying the same polynomial cannot substitute for the missing geometric operator.

**Primary records:** collaborations/pellis/02_prism_kathara_kristall_multidimensional.md, theorems/T056-phase21-trigram-supergolden-permutation-conjugacy.md, scripts/audit_prism_108_cycles.py, tests/test_prism_108_cycles.py, reports/KRISTALL_RECOVERY_STATUS.md.

## 5. Liouville–Bergman geometry and the Q6–D5 bridge

The phase-space starting point is \(T^*\mathbb R^5\) with canonical symplectic form
\[
\omega=\sum_{j=1}^5dp_j\wedge dq_j,
\qquad d\mu_L=\frac{\omega^5}{5!}.
\]
For the isotropic five-mode Hamiltonian in the Q6–D5 construction, the normalized complex coordinates are
\[
z_j=\frac{\sqrt{\beta_{\rm eff}\Omega}\,q_j+
i\pi_j/\sqrt{\beta_{\rm eff}\Omega}}{\sqrt{20}},
\qquad j=1,\ldots,5,
\]
so that
\[
d\mu_L=20^5\,d^{10}z.
\]

On the type-IV bounded symmetric domain
\[
D_5=\{z:N(z)>0,\ |z^Tz|<1\},\qquad
N(z)=1-2z^\dagger z+|z^Tz|^2,
\]
the Bergman density in this chart is
\[
\boxed{dV_B=N(z)^{-5}\,d\mu_L.}
\]
The exponent five is the genus of the type-IV domain in this realization. The symplectic Liouville measure and the Bergman density have distinct roles: the first is canonical phase-space volume; the second is the invariant complex-geometric density.

The repository proves a conditional invariance lemma: a specified real orthogonal five-dimensional action preserving the isotropic chart preserves both \(\omega\) and \(N(z)\), hence preserves the displayed Liouville–Bergman density.

There is also a crucial obstruction. The natural D4 action induced by the original Q6 labels does not preserve the old five-dimensional Q6 edge sector as an invariant subspace; the character comparison rules out an invertible intertwiner to the specified M3 orbit-graph five-sector. Thus the D4 invariance of the abstract five-dimensional chart cannot simply be transferred to the original Q6 D5 sector. A new full orbit-edge complex, a different Q6 sector, or a nontrivial quotient/bundle map would be needed.

**Established:** the canonical symplectic volume, the chart Jacobian, the type-IV generic norm, the Bergman density and the conditional orthogonal invariance lemma.

**Open:** the canonical Q6-induced representation/intertwiner and any Wilson-to-Bergman limit. The finite-coupling Wilson marginal is not identified with the Bergman measure.

**Primary records:** docs/Q6_D5_D4_LIOUVILLE_BRIDGE.md, theorems/T001-liouville-theorem.md, theorems/T010-para-kahler-liouville-psu.md, theorems/T011-para-kahler-liouville-psu.md.

## 6. Golden and supergolden hierarchies

The golden ratio and the supergolden constant arise from different exact recurrence operators.

The Fibonacci transfer matrix is
\[
M_\varphi=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\qquad
\chi_{M_\varphi}(x)=x^2-x-1,
\]
with Perron root
\[
\varphi=\frac{1+\sqrt5}{2}.
\]
Its scalar recurrence is \(F_{n+2}=F_{n+1}+F_n\).

The supergolden three-channel transfer is
\[
M_\psi=\begin{pmatrix}0&0&1\\1&0&0\\0&1&1\end{pmatrix},
\qquad
\chi_{M_\psi}(x)=x^3-x^2-1,
\]
with positive Perron root
\[
\psi=1.465571231876768\ldots.
\]
Its recurrence is \(a_{n+3}=a_{n+2}+a_n\). T056 proves that this matrix is permutation-conjugate to the Phase-21 matrix \(A_\psi\). It does not prove a geometric Kathara/Krist-All parent-to-child subdivision rule.

The fields have degrees two and three over \(\mathbb Q\). Since the degrees are coprime,
\[
\mathbb Q(\varphi)\cap\mathbb Q(\psi)=\mathbb Q,\qquad
[\mathbb Q(\varphi,\psi):\mathbb Q]=6.
\]
In particular, \(\log\varphi/\log\psi\notin\mathbb Q\): otherwise positive powers of \(\varphi\) and \(\psi\) would agree, giving a common rational algebraic unit greater than one, which is impossible.

One can therefore define an abstract rank-two scale semigroup
\[
\ell_{m,n}=\ell_0\varphi^{-m}\psi^{-n},
\qquad m,n\in\mathbb Z_{\ge0}.
\]
Distinct pairs give distinct scales. This is an exact algebraic construction, not yet a physical refinement law selected by Q6 or PRISM.

The binary icosahedral invariant degrees are \(12,20,30\), whose prime factorizations are
\[
12=2^2\cdot3,\quad20=2^2\cdot5,\quad30=2\cdot3\cdot5.
\]
Their prime-divisor set is \(\{2,3,5\}\). This is an exact arithmetic observation. It does **not** by itself derive Pellis's exponents or coefficients from icosahedral representation theory.

The geometric controls are also distinct:
- the regular pentagon gives \(D/s=\varphi\);
- the supergolden rectangle is defined by \(\psi^3-\psi^2-1=0\);
- the square/pentagon/hexagon common-circle synthesis records separate silver, golden and bronze ratios;
- the supergolden dodecahedral Whitney–Hodge construction (T149 and follow-ups) is a finite numerical/geometric FEEC study, not a proof that the supergolden ratio is a universal physical eigenvalue.

T112 keeps the golden-ratio/KTHNY physical scaling question falsifiable: a golden exponent must emerge under size refinement and null controls, not be inserted by the coordinate transform.

The Pellis core expression, as audited in document 04, is
\[
P_{\rm core}(x)=360x^{-2}-2x^{-3}+(3x)^{-5}.
\]
At \(x=\varphi\), its exact algebraic value is
\[
P_{\rm core}(\varphi)=\frac{264373-88447\sqrt5}{486}.
\]
This exact evaluation does not establish that it equals the QED inverse fine-structure constant by a physical derivation. The coefficients, exponent selection and normalization need an independent geometric/operator principle before the expression can be treated as a prediction.

**Primary records:** theorems/T056-phase21-trigram-supergolden-permutation-conjugacy.md, theorems/T112-golden-ratio-kthny-defect-geometry.md, theorems/S002-square-pentagon-supergolden-synthesis.md, theorems/T149-supergolden-dodecahedral-whitney-hodge.md, theorems/KRYSTALLO_SUPERGOLDEN_FINE_STRUCTURE_BRIDGE_AUDIT_2026-11-23.md, collaborations/pellis/04_pellis_functions_golden_spheres_resonance.md.

## 7. Self-adjoint operators and spectral-state selection

For a non-negative self-adjoint operator \(A\) with spectral resolution \(E_A\), a normalized state \(\xi\) defines the probability measure
\[
\mu_\xi(B)=\langle\xi,E_A(B)\xi\rangle.
\]
For discrete eigenspaces with projections \(P_n\), the weights are
\[
w_n=\|P_n\xi\|^2,\qquad w_n\ge0,\qquad\sum_nw_n=1.
\]
An expectation value alone does not determine the weights. T151 and the PEL-05 work distinguish the attainable barycentres from their closed convex hull and state a conditional uniqueness criterion: an isolated simple ground eigenvalue selects a unique state ray; degeneracy obstructs uniqueness unless an additional selection rule is supplied.

For the Poincaré scalar operator \(A=-\Delta_{S^3/2I}\), the Poisson-type semigroup
\[
R_s=e^{-s\sqrt A}
\]
is well-defined. On degree \(k\), its multiplier is \(e^{-s\sqrt{k(k+2)}}\). Choosing \(s=2\log\varphi\) gives \(\varphi^{-2\sqrt{k(k+2)}}\). This is a well-defined spectral filter, but the choice of \(s\) and a state \(\xi\) must be derived independently if the resulting weights are to be claimed as a physical resonance distribution.

The first collaboration paper can therefore be sharply framed around the scalar Poincaré spectrum, the self-adjoint operator, the semigroup and a non-circular state-selection criterion. It should not assume the Pellis resonance weights as input.

**Primary records:** collaborations/pellis/01_exact_scalar_spectrum_poincare_sphere.md, collaborations/pellis/03_geometric_self_adjoint_operators.md, docs/PELLIS_GSR_REGISTER_AUDIT_2026-11-27.md, open-problems/PELLIS_GSR_OPEN_PROBLEMS.md.

## 8. Research significance and staged collaboration

The programme connects several subjects that are often treated separately:

1. **Finite combinatorial geometry:** Q6 provides a completely explicit state space, adjacency, cubical faces, Walsh decomposition and Laplacian.
2. **Discrete differential geometry:** incidence, gradients, Green operators, barycentres, quadrature and resistance provide exact finite constructions.
3. **Statistical mechanics and transport:** reversible OU benchmarks and Green–Kubo identities connect the spectrum to integrated equilibrium response under explicit dynamics.
4. **Defect mechanics and hydrodynamics:** gradient-derived frame rotation, Burgers closure, barycentric moments and resistance assembly give a conditional bridge to continuum mechanics.
5. **Symplectic and complex geometry:** Liouville volume and the D5 Bergman density provide a structured phase-space setting.
6. **Arithmetic spectral geometry:** the Poincaré quotient, the binary icosahedral invariant ring, Fibonacci and supergolden recurrences, and modular/eta analyses offer testable arithmetic structures.

If the open bridges can be proved, the implications could extend well beyond one numerical constant: they could affect how discrete geometric models are related to continuum operators, how transport coefficients are derived from microscopic dynamics, and how spectral selection is connected to symmetry and arithmetic. These are research possibilities, not conclusions already established by the current finite results.

### Proposed work packages

**WP1 — Q6 foundation and exact finite operators.** Freeze conventions for the hexagram encoding, graph/cell distinction, incidence matrices, Walsh sectors and observables.

**WP2 — Green–Kubo and transport.** Derive a common microscopic Hamiltonian, stress/flux observables and dynamics; preserve anisotropy; prove the required finite-size and long-time convergence before claiming a material coefficient.

**WP3 — Liouville–Bergman and Q6 representation.** Resolve the Q6/D4 intertwining obstruction or construct a different equivariant complex. Do not identify the finite Wilson marginal with Bergman measure without a limit theorem.

**WP4 — Golden/supergolden geometric selection.** Derive the transfer operators from explicit refinement maps; test the Pellis exponents and coefficients without target-dependent fitting; keep the arithmetic relation \(2,3,5\) distinct from a physical derivation.

**WP5 — Poincaré spectrum and Pellis Functions.** Establish the scalar spectral/operator layer, then independently define the state-selection functional and compare its output with the Pellis expression.

### Evidence classification

| Component | Current classification |
|---|---|
| Q6 vertex/edge/face counts and graph spectrum | Exact theorem |
| Q6 graph Green operator and effective resistance identities | Exact finite graph identities |
| T068 barycentric covariance/quadrature | Proved local Euclidean theorem |
| T130 gradient, barycentre, local resistance assembly | Exact identities under stated hypotheses; finite tests |
| T097 Frank–Burgers reconstruction | Exact component identities; integrated bridge conditional |
| Q6 OU Green–Kubo formula | Exact for the specified reversible OU model |
| T131 phonon–phason transport framework | Conditional linear-response framework; physical calibration open |
| T132 coupled OU stress benchmark | Exact Gaussian benchmark under its hypotheses |
| PRISM 108-cycle cover | Constructively proved and audited; historical family identity open |
| T056 golden/supergolden matrix conjugacy | Exact finite-dimensional algebra |
| 11,725 Krist-All classes and reported residual | Historical claims; source definitions missing |
| D5 Liouville–Bergman density | Exact in the declared chart; Q6-induced D4 bridge obstructed/open |
| Pellis core expression at \(\varphi\) | Exact algebraic evaluation; physical derivation open |
| Q6/PRISM-to-continuum transport or gauge theory | Open convergence/calibration problem |
| Pellis resonance weights from a unique geometric operator | Open state-selection problem |

## 9. Reproduction entry points

~~~bash
python scripts/audit_prism_108_cycles.py
python -m pytest tests/test_prism_108_cycles.py -q
python -m pytest tests/test_q6_face_cochain_green_kubo.py -q
python -m pytest tests/test_t132_coupled_ou_green_kubo.py -q
python -m pytest tests/test_t097_barycentric_kinematic_law.py -q
~~~

The commands are entry points for the existing repository records; this documentation-only PR does not claim that they were executed in the present authoring session. CI results should be checked after opening the PR.

## 10. Central methodological principle

The collaboration should proceed from independently defined objects to operators, then to theorems, and only afterwards to physical interpretation:
\[
\text{definitions}
\longrightarrow
\text{incidence/geometry}
\longrightarrow
\text{operators}
\longrightarrow
\text{spectral or dynamical theorem}
\longrightarrow
\text{continuum/physical identification}.
\]

Numerical proximity, a shared polynomial, a suggestive geometric ratio or a matching dimension is not a substitute for a map, an intertwiner, a convergence theorem or a derivation from a common physical model. This principle makes the programme stronger and gives a collaborator a concrete way to contribute.
