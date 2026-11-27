# QAT / Q6 gauge–spinor sector: recovered result hierarchy

**Purpose.** Consolidate the existing QAT scripts and archived numerical audits into one dependency-ordered record. This is not a new physical theory claim. Numerical statements below are sourced from archived JSON outputs in the Library; scripts are cited as reproducibility sources. Raw NPZ/ZIP inputs are not all available in the repository branch, so this is a source-and-report audit, not a fresh raw-data rerun.

## 1. Discrete Q6 chain complex

The base complex has 64 vertices, 192 oriented links and 240 plaquettes, with incidence matrices
\[
B_1\in\mathbb R^{64\times192},\qquad
B_2\in\mathbb R^{192\times240},\qquad B_1B_2=0.
\]
Archived ranks are \(\operatorname{rank}B_1=63\) and \(\operatorname{rank}B_2=129\). Hence the link gauge-generator space \(\operatorname{im}B_1^T\) has dimension 63, and the plaquette-curvature map has rank 129. These are finite-complex statements.

## 2. Embedded U(1) Wilson sector

Selecting \(T_3=\sigma_3/2\) inside the archived SU(2) fibre gives the abelian quadratic link operator
\[
H_{U(1)}=\frac14 B_2B_2^T\in\mathbb R^{192\times192}.
\]
The archived audit reports:
- rank 129, nullity 63, with 129 positive modes;
- \(B_2^TB_1^T=0\) and \(B_1B_2=0\), both with residual 0;
- rounded eigenvalue multiplicities \(0:63, 1:15, 1.5:40, 2:45, 2.5:24, 3:5\).

Thus the Hessian kernel is exactly the 63-dimensional vertex-gauge image for this connected Q6 complex. The Q6 vertex Laplacian has eigenvalues \(0,2,4,6,8,10,12\) with multiplicities \(1,6,15,20,15,6,1\).

**Status:** exact algebraic finite-graph result, conditional only on the stated incidence convention. It is an embedded Cartan U(1), not a derived electromagnetic sector or a spontaneous symmetry-breaking mechanism.

## 3. Joint spinor–gauge quadratic model

The archived script `derive_QAT_joint_U1_spinor_gauge.py` expands a *chosen* spatial action around \(\psi_0=(1,0)\) and \(U_e=I\):
\[
S=\frac12\|D_U\psi\|^2+\frac12\|B_2^Ta/2\|^2.
\]
Its reported model has 448 real variables, Hessian rank 381 and nullity 67. The linearized gauge generator has rank 64 and annihilates the real residual operator; three further constant-spinor flat directions are recorded. The link-link Hessian block satisfies
\[
H_{aa}=\frac14B_2B_2^T+\frac14I_{192}.
\]
The extra \(I/4\) is the spinor-link contribution at the selected background; it is not part of the pure Wilson photon Hessian.

This is a finite-dimensional quadratic expansion around a selected background. It does not derive the background dynamically, a physical photon, a massless transverse continuum mode, or a time kinetic term.

## 4. Gauge-covariant quaternionic spinor transfer

The recovered transfer script defines the edge covariant difference
\[
(D_U\psi)_{gh}=\psi_h-U_{gh}\psi_g,
\qquad K_U=D_U^\dagger D_U,
\qquad T_U(s)=\exp[-is\sqrt{K_U}].
\]
For vertex gauge matrices \(g_v\), the link transformation is
\[
U_{gh}\mapsto g_hU_{gh}g_g^\dagger,
\]
and the vertex/edge block actions give covariance of \(D_U\), \(K_U\) and \(T_U(s)\). The script tests a deterministic local gauge transformation in the selected \(T_3\) subgroup, checks reconstruction against archived \(D_{fibre}\) and \(K_{fibre}\), and checks transfer unitarity.

**Status:** the source defines a rigorous, falsifiable covariance test. The result JSON is not present in the recovered set, so this audit does not invent numerical residuals or mark the run as independently passed. The script explicitly says \(s\) is external and the photon Wilson sector remains separate: no photon–spinor interaction or backreaction is derived.

## 5. AntiTwin two-sheet photon lift: negative/limiting result

The archived finite-graph lift uses
\[
H_{two}=H_0\otimes I_2+\delta A\otimes\sigma_z-t_{throat}I_{192}\otimes\sigma_x,
\quad H_0=\frac14B_2B_2^T,
\]
where \(A\) is a sampled fourth-order angular anisotropy. This is explicitly a test Hamiltonian, not a derived throat coupling.

The recorded commutator is nonzero (Frobenius 6.02459; relative 0.0244557). More decisively, the trace-free ratio of \(A^2\) on the physical \(H_0\) subspace is 0.69091365, so the second-order sheet-odd correction is not scalar. Residual mode-dependent corrections survive. The archived parameter sweep therefore does **not** establish a universal scalar photon renormalization.

This is a useful obstruction: the simple AntiTwin lift does not collapse to a mode-independent correction for the tested geometry and parameter range.

## 6. Temporal-closure obstruction

The recovered temporal-closure script identifies the A14 fourth constraint as the fixed-radius/fixed-scale covector \(X_{flat}^T\). The fourth coframe component is the endpoint increment of \(\|X\|\), not a time coordinate. The quaternionic fibre supplies internal complex structures, but the spatial incidence and link data select no canonical imaginary unit or evolution direction.

The conditional extension
\[
\partial_s^2 A+c_*^2H_{U(1)}A=0,
\qquad \omega_j=c_*\sqrt{\lambda_j},
\]
introduces both \(s\) and \(c_*\) externally. It is a parametrized wave ansatz, not a derivation of physical time or light speed.

## 7. Physical conclusions that remain unavailable

The finite Q6 graph is the binary hypercube \(\mathbb Z_2^6\): its characters have only binary momenta. The continuous covering-lattice symbol
\[
\lambda(k)=4\sum_{a=1}^6\sin^2(k_a/2)
\]
has an isotropic six-dimensional small-(k\) limit, but that does not supply a 3+1-dimensional continuum. The existing propagation verification explicitly finds anisotropy in the attempted 3D embedding and lacks a time-evolution operator/refinement family.

Therefore the following remain open:
1. a derived, equivariant map from six bit directions to three physical spatial directions;
2. a coupled action with dynamical spinor and gauge backreaction;
3. a preferred evolution generator and a causal/positive transfer construction;
4. a refinement/continuum limit with an isotropic principal symbol;
5. a derived Lorentzian signature and a calibrated limiting speed.

## 8. Source inventory

- `derive_QAT_U1_light_sector.py` + `QAT_U1_light_sector_audit.json`: embedded U(1) Wilson sector and exact finite-complex ranks.
- `derive_QAT_joint_U1_spinor_gauge.py`: joint quadratic spinor/gauge expansion and 67-dimensional kernel analysis.
- `derive_QAT_joint_gauge_covariant_transfer.py`: local gauge covariance of spinor transport and spectral transfer.
- `RGS_PSU_AntiTwin_photon_lift_audit.json`: two-sheet photon lift and non-scalar second-order obstruction.
- `derive_QAT_quaternionic_temporal_closure.py`: radial-normal and temporal-closure audit.
- `verify_QAT_light_propagation.py`: finite-graph propagation anisotropy and absence of a derived light cone.
- `RGS_QLG_QAT_generalization_audit.json`: integrated dimensions, residuals, operator spectra, coframe and holonomy cross-checks.

**Classification:** finite Q6 chain and embedded U(1) Hessian — exact algebraic/numerical; joint spinor/gauge and two-sheet lifts — chosen finite models; gauge-covariant transfer — explicit construction with rerun still required; physical photon, time, Lorentzian continuum and TEGR dynamics — open.
