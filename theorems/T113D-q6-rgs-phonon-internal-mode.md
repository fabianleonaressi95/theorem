# T113-D — Q6/RGS phonon–internal-mode model: induced symmetry and the exact graph obstruction

**Classification:** exact finite Q6 identities; numerically audited induced \(O_h\) action on the recovered RGS seed; proposed discrete variational model. No phonon–phason gravitational mass is claimed.

**Correction to the generic icosahedral construction:** this programme must start from the user's actual 64-state Q6 and its hash-checked RGS embedding. A generic six-dimensional cut-and-project quasicrystal with a freely selected \(A_5\) physical/perpendicular representation is not a substitute for Q6. The icosahedral group is not imposed on the Q6 graph without checking the induced action.

## 1. The actual Q6 object

Use the six-bit label
\[
v=(b_0,b_1,b_2,b_3,b_4,b_5)\in\{0,1\}^6,
\qquad v=\sum_{j=0}^{5}2^{5-j}b_j
\]
with the repository's stated big-endian convention. The graph is the six-cube:
\[
V=64,\quad |E|=192,\quad \deg(v)=6,
\qquad A_{v,w}=1\iff d_H(v,w)=1,
\]
\[
L_{Q6}=6I_{64}-A,
\qquad
\operatorname{spec}(L_{Q6})=
0^1,2^6,4^{15},6^{20},8^{15},10^6,12^1.
\]
The cubical completion has 240 square faces. The 64 hexagrams remain 64 distinct sites; the graph is also \(Q_3^-\square Q_3^+\), with the lower- and upper-trigram three-bit factors kept distinct.

## 2. The recovered RGS geometric embedding

The repository's canonical 64-point coordinate seed is not a generic icosahedral cut-and-project construction. It is the hash-checked map
\[
X:V(Q6)\longrightarrow\mathbb R^3
\]
defined in `src/rgs_seed_64_reconstruction.py`, with eight orbit representatives and three independent coordinate signs. Its canonical SHA-256 is
`6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e7f286126e419cf`
(the audit imports the authoritative constant and checks the bytes).

The induced point-cloud symmetry is the signed-coordinate-permutation group
\[
O_h=\{G\in\mathrm{Mat}_{3\times3}(\mathbb Z):
G\text{ has one }\pm1\text{ in each row and column}\},
\qquad |O_h|=48.
\]
For each \(G\), the seed determines a unique permutation \(\pi_G\) of the 64 labels by
\[
X_{\pi_G(v)}=G X_v.
\]
This is the actual induced action used here. It is not replaced by an assumed action on a hypothetical perpendicular six-dimensional space.

## 3. Crucial exact obstruction: the full \(O_h\) action does not preserve Q6 adjacency

For each induced permutation, let \(P_G\) be its 64-by-64 permutation matrix. The graph is an automorphism precisely when
\[
P_G A_{Q6}P_G^T=A_{Q6}.
\]
The companion audit constructs all 48 permutations from the hash-checked coordinates and computes this residual. Its finite result is:
- 48 induced signed-permutation actions on the 64-point seed;
- exactly 16 preserve the canonical six-cube adjacency;
- 32 do not;
- the nonzero Frobenius residual is 16 for each of those 32 elements.

Therefore **the full geometric \(O_h\) symmetry of the embedded point cloud is not a symmetry of the unweighted 192-edge Q6 graph**. One cannot simultaneously claim that the bare Q6 Laplacian is \(O_h\)-invariant. The 16-element adjacency-preserving subgroup and the full 48-element point-cloud group must be kept distinct.

This is why a generic Reynolds average over \(A_5\), or an assertion that Q6 itself is an icosahedral six-dimensional cut-and-project lattice, would be the wrong starting point.

## 4. Two legitimate operators — do not conflate them

### 4.1 Bare Q6 operator

Keep the exact 192 edges and use \(L_{Q6}\). Under the full induced point-cloud group, record the symmetry-breaking residual
\[
\Delta_G=P_G L_{Q6}P_G^T-L_{Q6}.
\]
This preserves the original graph, its 240 cubical plaquettes, the 129-dimensional graph cycle space, and all Q6 Walsh/Laplacian identities. It does **not** have full \(O_h\) symmetry.

### 4.2 Full-\(O_h\) Reynolds operator

Alternatively define
\[
\overline L_{O_h}=\frac1{48}\sum_{G\in O_h}
P_G L_{Q6}P_G^T.
\]
As an average of positive-semidefinite symmetric graph Laplacians, \(\overline L_{O_h}\) is symmetric, positive semidefinite, annihilates constants, and commutes with the induced \(O_h\) action. For this recovered seed its off-diagonal conductances form three nonzero classes:
\[
1,\qquad\frac23,\qquad\frac13,
\]
with 96 unordered pairs in each class, hence 288 weighted edges. This is an **O_h-invariant weighted comparison operator**, not the original 192-edge Q6 graph. It must not inherit Q6's 240 square plaquettes or Q6's cubical cohomology claims without a new cell-complex construction.

The two operators provide a controlled comparison: the bare Q6 model retains the exact hypercube topology; the Reynolds model restores the full point-cloud symmetry at the price of changing the interaction graph.

## 5. Q6 discrete phonon/internal-mode action

Let \(D_0\in\mathbb R^{192\times64}\) be the oriented Q6 vertex-to-edge incidence matrix. Let \(u\in\mathbb R^{64}\otimes V_{\rm phys}\) be a physical displacement field, with \(V_{\rm phys}\cong\mathbb R^3\) carrying the polar-vector representation induced by \(O_h\). Let \(w\in\mathbb R^{64}\otimes W_{\rm int}\) be an internal field.

The Q6 edge gradients are
\[
e_u=(D_0\otimes I_{V_{\rm phys}})u,
\qquad
e_w=(D_0\otimes I_{W_{\rm int}})w.
\]
A finite conservative quadratic action is
\[
S_{Q6}^{(2)}=\frac12\int dt\left[
\begin{pmatrix}\dot u\\\dot w\end{pmatrix}^{T}
\mathsf M
\begin{pmatrix}\dot u\\\dot w\end{pmatrix}
-
\begin{pmatrix}e_u\\e_w\end{pmatrix}^{T}
\begin{pmatrix}\mathsf C&\mathsf R\\
\mathsf R^T&\mathsf K\end{pmatrix}
\begin{pmatrix}e_u\\e_w\end{pmatrix}
\right].
\]
Here \(\mathsf M\) is positive definite on the nonzero dynamical sector and the elastic block is positive semidefinite (strictly positive after removing translational zero modes). This is a well-defined discrete Q6 model once the internal representation, matrices, and coefficients are specified.

**Important:** Q6 alone supplies the 64 sites, 192 edges, six bit directions, and cubical incidence maps. It does not by itself supply a perpendicular-space coordinate, a phason representation, a phason kinetic law, or numerical elastic constants. Therefore \(W_{\rm int}\) is deliberately left as explicit model input. The existing RGS \(T_{2u}\) sector may be tested as a candidate internal representation, but it is not identified with a physical phason until the intertwiner and microscopic meaning are derived.

For the bare graph, the generalized normal modes solve
\[
\mathcal K_{Q6}q_\alpha=\omega_\alpha^2\mathcal M q_\alpha.
\]
The graph Fourier basis is the 64 Walsh characters, with bare Q6 eigenvalues \(2|S|\). The mode degeneracies are thus known exactly before constitutive weights are added. Density-dependent coefficients can be varied along a declared material path and treated with the generalized Hellmann–Feynman identity for simple eigenvalues.

## 6. Gravitational response: the correct next calculation

Couple the complete finite action, including the material frame and density-dependent coefficients, to a weak metric. Define
\[
T_{\mu\nu}=-\frac2{\sqrt{-g}}\frac{\delta S}{\delta g^{\mu\nu}},
\qquad
M_{g,\alpha}=\frac1{c^2}\int d^3x\,
\langle\delta T_{00}^{(\alpha)}\rangle.
\]
For a finite Q6 model this requires a specified spatial reconstruction/quadrature map from the 64 site degrees of freedom to a material volume. Without that map the finite graph has a mode energy, but no uniquely defined continuum energy density or gravitational mass.

The diagnostic
\[
-\frac{d\log c_\alpha}{d\log\rho_m}
\frac{E_\alpha}{c_\alpha^2}
\]
is to be compared with the full metric-derived mass, not substituted for it. The EKN fluid and isotropic-solid limits remain mandatory controls.

## 7. Involutions: preserve the established Q6/RGS distinction

The canonical Q6 graph antipode is
\[
a_6(v)=v\mathbin{\mathrm{XOR}}63.
\]
The coordinate inversion of the recovered RGS point seed is
\[
a_{\rm RGS}(v)=v\mathbin{\mathrm{XOR}}7.
\]
They are different maps. The audit retains both and verifies that the RGS coordinate inversion, not the canonical graph antipode, sends \(X_v\) to \(-X_v\). No antipodal or Walsh-sector argument may silently exchange these involutions.

## 8. Reproducibility and status

Run:
```bash
python scripts/audit_t113d_q6_rgs_oh.py
pytest -q tests/test_t113d_q6_rgs_oh.py
```

**Exact/proved inputs:** Q6 graph counts and spectrum; the hash-checked 64-by-3 RGS seed; the signed-permutation group of order 48; induced point-cloud permutations.

**Numerically audited finite result:** 16 of the 48 induced \(O_h\) permutations preserve Q6 adjacency; the other 32 do not. The Reynolds-averaged operator has the stated three conductance classes and is distinct from the bare Q6 Laplacian.

**Open:** explicit microscopic interpretation and coefficients of \(\mathsf C,\mathsf R,\mathsf K,\mathsf M\); identification of a genuine Q6 internal/phason representation; a site-to-continuum reconstruction; metric variation and packet gravitational mass; any \(\varphi\)- or De Aquino-dependent law.

## References within this repository

- T099: exact Q6 product graph and Kirchhoff network.
- T104: Q6 cycles, cocycles, holonomy and cubical cohomology.
- T069: distinct Q6 graph antipode and RGS coordinate inversion.
- `src/rgs_seed_64_reconstruction.py`: canonical hash-checked 64-point embedding.
- T113/T113-A/T113-B: EKN control and metric-coupled variational programme.
