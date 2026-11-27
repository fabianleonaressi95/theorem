# RGS 4D–6D–3D geometry: recovered embedding, Cartan connection and teleparallel correspondence

**Date:** 27 November 2026  
**Status:** synthesis of prior finite constructions and theorem dependencies; the combined spacetime field theory and its refinement limit remain open.  
**Purpose:** prevent the 4D/6D/3D bridge and the curvature/torsion connection from being split into unrelated programmes.

## 0. Executive correction

## 0.1 Combinatorial origin: six-line I Ching hexagrams and Kirchhoff Q6

The 64-site carrier is not an arbitrary geometric sampling of a 6-cube. It originates in the 64 six-line binary hexagrams:
[
\mathcal H=\{0,1\}^6,\qquad |\mathcal H|=2^6=64.
]
Under the explicitly chosen elementary mutation rule that flips exactly one line, two hexagrams are adjacent precisely when their Hamming distance is one. This defines the six-dimensional hypercube graph (Q_6). The rule must remain explicit: it is a mathematically exact encoding, but should not be conflated without further evidence with every traditional I Ching relation or ordering (e.g. King Wen sequence).

Let (B\in\mathbb R^{64\times192}) be an oriented vertex-edge incidence matrix and (W=I_{192}) for the unweighted graph. The Kirchhoff/combinatorial Laplacian is
[
L=BWB^T=D-A=6I-A.
]
Exact graph identities:
- 64 vertices, degree 6, 192 undirected edges;
- 240 elementary square 2-faces, counted as (inom62 2^4);
- bipartition by parity of the six-bit Hamming weight, 32+32;
- connected graph and graph cycle rank (E-V+1=192-64+1=129);
- Laplacian spectrum (lambda_k=2k), multiplicity (inom6k), (k=0,\ldots,6).

**Topology convention:** (eta_1=129) is the cycle rank/first Betti number of the graph 1-skeleton. If all 240 square faces are attached as 2-cells, the first homology changes; for the full cubical 6-cell the resulting cubical complex is contractible. Never quote (eta_1=129) for the square-filled 2-skeleton or full cube without specifying the chain complex and computing its boundary ranks.

The centred coordinates (v_c=v-\frac12\mathbf1\in\{-\frac12,+\frac12\}^6) used by the golden cut-and-project implementation are therefore the coordinate realization of the six binary line states. The order of construction is: hexagram states → single-line-flip incidence graph and Kirchhoff operator → centred six-coordinate carrier → golden physical/internal projections. The finite 64-state carrier and the infinite (mathbb Z^6) model-set extension are related constructions, not identical objects; the latter requires its own lattice/window and patch-limit statements.

The archived RGS arrays (X_{Oh}\ (64\times3)), (Q_{rebuilt}\ (192\times188)), and (K_{tangent}\ (188\times188)) connect the 64-state/192-edge carrier to the reconstructed spatial and tangent data. Earlier recovery notes explicitly found no stored original 64×64 adjacency or incidence array in that archive; the Gray-code/Hamming-1 adjacency, edge list and Laplacian were separately reconstructed and audited. Preserve this provenance distinction and regenerate/hash the incidence and Laplacian alongside the RGS arrays in the consolidated audit.


The 6D golden physical/internal split is not merely a generic proposal. It is explicitly implemented in the companion repository `fabianleonaressi95/rgs-qlg-quaternion-bridge`, in `src/rgs_psu_cut_project.py`, and is used by theorem card T129. The earlier spherical acceptance window of radius 1.5 was provisional and is superseded by the projected-cube window described below.

The 4D→6D→3D programme must nevertheless keep three different mathematical operations distinct:

1. the archived 188-dimensional RGS tangent embedding into six selected directions;
2. the 6D golden decomposition into physical and internal 3-planes;
3. the spacetime interpretation of one internal direction as a time-like mode, which requires an independently derived torsion observable and remains a candidate, not an established Lorentzian time coordinate.

Likewise, curvature and torsion are not to be forced into a choice between GR/Levi-Civita and TEGR. The common object is the coframe plus a metric-compatible connection; the Levi-Civita, general Riemann–Cartan and teleparallel connections are related but distinct connection choices.

## 1. Recovered 188D-to-6D embedding (21 October 2026)

The archived construction uses an orthonormal six-frame
[
J\in\mathbb R^{188\times6},\qquad J^TJ=I_6,
]
inside the kernel of the rank-64 projector (P_G\) acting on the 188D RGS tangent space:
[
P_GJ=0,\qquad \operatorname{rank}P_G=64,qquad
\dim\ker P_G=124.
]
Write (J=[J_A\;J_B]) for the two three-column blocks. For the golden orthogonal projections (P_\parallel,P_\perp\in\mathbb R^{3\times6}), define
[
J_\parallel=JP_\parallel^T,\qquad
J_\perp=JP_\perp^T.
]
Both are (188\times3), orthonormal, mutually orthogonal and contained in (\ker P_G). The six-dimensional subspace is therefore resolved into two orthogonal three-dimensional sectors inside the 188D tangent carrier. This is the recovered finite embedding, not an identification of the 188D space with spacetime coordinates.

Archived numerical residuals (21 October report):
- \(\|J^TJ-I_6\|=1.686257\times10^{-15}\);
- \(\|J_\parallel^TJ_\parallel-I_3\|=6.145551\times10^{-16}\);
- \(\|J_\perp^TJ_\perp-I_3\|=8.461326\times10^{-16}\);
- \(\|J_\parallel^TJ_\perp\|=3.464881\times10^{-16}\);
- \(\|P_GJ_\parallel\|=8.940595\times10^{-16}\);
- \(\|P_GJ_\perp\|=8.722828\times10^{-16}\);
- reconstruction \(\|X_{\rm full}-X_\parallel-X_\perp\|=5.111437\times10^{-15}\).

The associated archived report also gives projected edge lengths \(\sqrt2\) in both sectors, total length 2, and maximum cross-sector dot product \(7.503\times10^{-16}\). These are finite numerical certificates for the selected embedding and its projection convention; they do not prove a continuum limit.

**Important:** (E_\perp\) is internal space, not automatically physical time. The 3+1 split in T154 is a decomposition of constraint normals (three translations plus one radial-scale normal), not a physical time direction.

## 2. Golden 6D cut-and-project frame and canonical projected-cube window

The companion implementation defines
[
\phi=\frac{1+\sqrt5}{2},\qquad
\phi_* = \frac{1-\sqrt5}{2}=-\phi^{-1},
]
and
[
A(p)=\begin{pmatrix}
0&0&1&-1&p&p\\
1&-1&p&p&0&0\\
p&p&0&0&1&-1
\end{pmatrix},
quad
P_\parallel=\frac{A(\phi)}{\sqrt{2(2+\phi)}},
quad
P_\perp=\frac{A(\phi_*)}{\sqrt{2(2+\phi_*)}}.
]
The implementation `golden_cut_project_frame()` returns the two (3\times6) projections and their stacked (6\times6) orthogonal frame. The exact identities are
[
P_\parallel P_\parallel^T=I_3,\quad
P_\perp P_\perp^T=I_3,\quad
P_\parallel P_\perp^T=0.
]
Consequently the associated 6D projectors are complementary, rank three each.

For the 64 Q6 states, use centred vertices
[
v_c=v-\tfrac12\mathbf1\in\{-\tfrac12,+\tfrac12\}^6,
\quad
x_\parallel=P_\parallel v_c,\quad
x_\perp=P_\perp v_c.
]
The internal acceptance window is not the earlier provisional sphere. It is
[
W=P_\perp([-\tfrac12,\tfrac12]^6),
]
the projected centred 6-cube, a rhombic triacontahedral zonotope with 32 vertices and 30 rhombic facets for this projection convention. The companion audit checks that all 64 projected Q6 internal points lie in this window. A finite-radius model-set patch is enumerated from (\mathbb Z^6) using this window and a certified integer search bound.

Implementation/source: `rgs-qlg-quaternion-bridge/src/rgs_psu_cut_project.py`; theorem dependency: T129. The finite frame/window construction and its numerical checks must be cited separately from the infinite model-set properties and from any physical identification. T113-G proves the relevant abstract rank-two isotropy statement under point-group hypotheses; its original Q6 realization caveat should be updated against this later explicit implementation, while retaining the requirement that the full decorated model's symmetry be checked.

T129's two-angle Purcell map adds a calibration (C\in\mathbb R^{2\times3}), scale and offset. Those are model inputs, not determined by the 6D split. Do not silently identify the 3D internal space with a canonical 2D shape plane.

## 3. Where the 4D layer enters: torsion-coupled internal direction

The companion cut-project module implements `audit_torsion_coupled_internal_time_axis`. It takes:
- the 64×3 internal coordinates (Y_\perp);
- an independently derived 64×m torsion trace (T).

After centring and column normalization it forms
[
C_{\perp T}=Y_{\perp,z}^TT_z/64
]
and selects the leading left singular vector (u_\tau). Its candidate scalar coordinate is
[
\tau_v=(Y_{\perp,v}-\bar Y_\perp)\cdot u_\tau.
]
The implementation also computes a permutation null and a row bootstrap for the axis direction.

This is the actual proposed 6D→4D bridge: the internal 3-space supplies a candidate distinguished direction through coupling to a separately derived torsion observable; the remaining two internal directions form the residual internal plane. The procedure explicitly refuses to substitute the 192×4 edge coframe for a 64×m torsion trace.

**Status:** candidate-selection algorithm only. It does not establish physical time, Lorentzian signature, causal cones, lapse/shift, or a dynamical tetrad. A statistically stable leading singular direction is not by itself a physical time theorem. The 4D coframe must still be constructed and its metric signature and field equations independently checked.

## 4. One coframe, related connections: do not confuse the branches

Let (e^A\) be a nondegenerate Lorentzian coframe and let (\omega^A{}_B\) be a metric-compatible Lorentz connection. Define
[
T^A=de^A+\omega^A{}_B\wedge e^B,\qquad
R^A{}_B=d\omega^A{}_B+\omega^A{}_C\wedge\omega^C{}_B.
]
The Cartan identities are
[
DT^A=R^A{}_B\wedge e^B,\qquad DR^A{}_B=0.
]
They permit (T\ne0) and (R\ne0) simultaneously for a general Riemann–Cartan connection.

For the same coframe, write a metric-compatible connection as
[
\omega=\omega_{\rm LC}+K,
]
where (K) is contorsion. With this convention,
[
T^A=K^A{}_B\wedge e^B,
\qquad
R(\omega)=R(\omega_{\rm LC})+
D_{\rm LC}K+K\wedge K.
]
This is the direct curvature–torsion bridge. It is the general Riemann–Cartan branch.

A teleparallel connection (\omega_{\rm W}) is a special, flat connection:
[
R(\omega_{\rm W})=0,\qquad T(\omega_{\rm W})\ne0
\quad\text{in general}.
]
Then
[
0=R(\omega_{\rm LC})+
D_{\rm LC}K_{\rm W}+K_{\rm W}\wedge K_{\rm W}.
]
Thus Levi–Civita curvature is represented by teleparallel contorsion and its derivative. The two connections are not the same connection: one is torsion-free and generally curved, the other flat and generally torsionful.

**Architecture decision:** the fundamental geometric data for the unified RGS model are ((e,\omega)) with independent metric-compatible connection, allowing both curvature and torsion. The teleparallel branch is a constrained flat-connection representation of the same metric geometry when a suitable inertial spin connection exists. A generic Riemann–Cartan connection with (R\ne0,T\ne0) is not TEGR. If the action is to propagate both curvature and torsion as independent sectors, that is a Poincaré-gauge / quadratic-curvature-and-torsion theory (or another explicitly defined first-order theory), not standard TEGR.

The earlier Levi–Civita numerical kernel is retained only as a torsion-free reference/benchmark and as a way to define (\omega_{\rm LC}) from a differentiable coframe. It is not the fundamental RGS connection.

## 5. Theorem and evidence dependency ledger

| Existing record | What is already established | What it does not establish |
|---|---|---|
| T063 | Proved quaternionic (SU(2)\to SO(3)) double cover, with fixed active-rotation convention | Lorentzian spin bundle or physical QLG identification |
| T115 | Proved pointwise curved Clifford anticommutator for an invertible RGS spatial coframe | A connection, torsion, curvature, or field equations |
| T154 (RGS spatial coframe card; duplicated display ID) | Exact finite constraint-normal split under centred/fixed-scale hypotheses; archived numerical 188D tangent/coframe checks | Physical time or Lorentzian 3+1 spacetime |
| T113-G | Proved abstract rank-two isotropy theorem under stated point-group invariance; Q6-specific realization requires the complete model symmetry | Automatic isotropy of all microscopic or higher-rank tensors |
| T129 | Explicit golden (6D\to3D_\parallel\oplus3D_\perp) frame, calibrated two-angle map conditional on calibration, finite tests | Calibration (C,\sigma,s_0), continuum limit, or physical time |
| S.9 | Exact balanced three-phase/Ferraris rotating-field composition and coframe component transformation laws | A rotating field as a tetrad, torsion source, or gravitational solution |
| Q6 archived carrier coframe dossier | Gauge-covariant 192-edge coframe and 240-square path-sum candidate | Continuum Cartan torsion or torsion Bianchi theorem |
| PR #585 static coframe/LC audit | Reproducible static interpolation and LC-vs-Q6 link comparison; Q6 links differ from that specific LC interpolation | The LC interpolation as the fundamental connection, or a no-go theorem for other connections |

Numbering caution: T154 is reused by an unrelated In2Infinity card; use the full filename/record key, not the display number alone. T141 (antipodal icosahedron lift) and T130 (Q6 gradients/barycentres) remain OPEN in the register and must not be used as proved premises.

## 6. Required next construction (ordered, no rediscovery)

1. **Freeze the recovered 6D data:** import the exact (P_\parallel,P_\perp), centred Q6 cube, projected-cube rhombic-triacontahedral window and the 188×6 (J) embedding. Record hashes and re-run all orthogonality/reconstruction checks in one reproducible audit.
2. **Derive the torsion trace independently:** use the archived 192-edge connection/coframe and 240 oriented square path sums only as candidate raw data. Define a gauge-covariant 64×m vertex observable; do not rename a path sum as Cartan torsion before a discrete Cartan map and convergence statement exist.
3. **Test the internal temporal axis:** run the existing SVD/permutation/bootstrap criterion on that independently derived trace. Report stability and null statistics; if it fails, do not force a time axis.
4. **Build the 4D coframe:** use (e^0=Ndt), (e^a=E^a{}_i(dx^i+N^i dt)), with (N,N^i,E^a{}_i(t,x)) derived or explicitly declared. Check nondegeneracy and Lorentzian signature.
5. **Build the general Cartan connection:** specify the inertial/gauge part and contorsion, compute (T,R), and verify both Bianchi identities and tetrad postulate. Only then derive the teleparallel flat representative and verify its zero curvature and contorsion identity.
6. **Project the geometric fields:** project coframe, connection, torsion and curvature through the declared 6D split, checking gauge covariance and incidence compatibility; do not project coordinates alone.
7. **Couple Anti-Twin, Maxwell and QHD:** keep the U(1), Lorentz-spin, spatial (SU(2)), and sheet-exchange bundles distinct; derive couplings from one declared action. Reuse T063 rather than creating a duplicate quaternion theorem.

## 7. Explicit open gates

- No validated independent 64×m Cartan torsion trace has yet been supplied to the internal-time selector.
- No physical time coordinate, Lorentzian lapse/shift, or dynamical 4D tetrad has been derived from the 188D embedding.
- No single RGS action has yet selected the general Cartan connection and its teleparallel representative.
- No discrete-to-continuum theorem proves convergence of the 192-edge/240-face carrier to Cartan torsion and curvature.
- No Mosco/refinement theorem transfers the cut-and-project fields and their Hodge operators to a continuum model.
- No field-equation derivation establishes a Tesla/MHD/QHD coupling to torsion.

These are the next proof obligations, not reasons to discard the already recovered finite geometry.


## 8. New finite spatial discrete Cartan construction (27 November 2026)

The first executable Cartan layer has now been added in:
- scripts/audit_q6_discrete_cartan.py;
- tests/test_q6_discrete_cartan.py;
- audits/Q6_DISCRETE_CARTAN_AUDIT.json;
- research/Q6_DISCRETE_CARTAN_TORSION_CURVATURE_AUDIT_2026-11-27.md.

It uses the original 64 six-bit I Ching states, the 192 Hamming-1 Q6 edges, and all 240 coordinate-square faces. The archived SPD site coframes define edge increments theta_(g->h)=E_g(X_h-X_g). The existing shortest-radial-rotation links define an SO(3) edge connection. On each face, torsion is the developed boundary closure defect T_p=sum_i P_i^{-1} theta_i; curvature is the ordered face holonomy H_p=U_3 U_2 U_1 U_0.

A deterministic independent local SO(3) gauge at every vertex verifies:
- torsion covariance max residual 5.76e-15;
- curvature conjugation max residual 2.17e-15;
- edge-link orthogonality max residual 2.09e-15;
- edge-link determinant max residual 1.44e-15.

For this specified finite data, 236/240 faces have both nonzero developed torsion and nonzero curvature angle. This is the first explicit finite spatial construction in this programme in which both are present together. It is not yet a Lorentzian 4D Cartan field, a teleparallel flat representative, or a continuum theorem. In particular, the current SO(3) links are not derived from a common variational action, and no non-Abelian cube Bianchi or Mosco limit is claimed.

The static Levi-Civita audit remains a torsion-free benchmark only; the discrete Cartan construction above is the active finite spatial connection layer.


## 9. Flat Q6 branch and exact finite connection-difference identity (27 November 2026)

A second spatial connection has been added on the same Q6 carrier and same reconstructed site coframe:
- \`scripts/audit_q6_teleparallel_branch.py\`;
- \`tests/test_q6_teleparallel_branch.py\`;
- \`research/Q6_TELEPARALLEL_FLAT_BRANCH_AUDIT_2026-11-27.md\`.

In a chosen global trivialization, the flat branch is \(U^{\mathrm W}_{gh}=I_3\) on every edge. Under local vertex-frame changes it transforms as \(G_hU^{\mathrm W}_{gh}G_g^{-1}\), so all 240 square holonomies are identity. The same edge coframe can still have a nonzero developed face closure defect. This is a finite spatial pure-gauge flat representative, not yet a variationally selected TEGR connection.

The curved branch is not relabelled: its nontrivial face holonomy remains a distinct connection choice.

The exact finite comparison is now recorded in:
- \`scripts/audit_q6_connection_difference.py\`;
- \`tests/test_q6_connection_difference.py\`;
- \`research/Q6_DISCRETE_CONTORSION_IDENTITY_2026-11-27.md\`.

For each oriented edge \(g\to h\), define the relative link
\[
V_{gh}=U^{\mathrm C}_{gh}(U^{\mathrm W}_{gh})^{-1}.
\]
It is based at the target frame and transforms by conjugation:
\[
V'_{gh}=G_hV_{gh}G_h^{-1}.
\]
Its principal logarithm \(A_{gh}=\operatorname{Log}(V_{gh})\in\mathfrak{so}(3)\) gives the exact link-group factorization
\[
U^{\mathrm C}_{gh}=\exp(A_{gh})U^{\mathrm W}_{gh}.
\]
The corresponding ordered face-product factorization is checked on the 240 square faces. This is the exact finite lattice connection-difference identity; it is **not** yet the continuum Cartan contorsion 1-form or the differential identity \(R(\omega^{\mathrm C})=R(\omega^{\mathrm W})+D^{\mathrm W}K+K\wedge K\).

**Validation status:** the source, tests and dossiers are committed to the PR branch. No CI workflow run was returned for the latest connection-difference commit when queried; therefore these latest tests are pending and must not be reported as passed.

**Remaining bridge:** define a compatible discrete covariant derivative and coframe difference, establish refinement/convergence, lift to \(SO(1,3)\)/Spin(1,3), and derive an action selecting the flat representative. The internal golden 3-space remains a candidate source for a distinguished direction only after an independent gauge-covariant torsion trace is supplied. No physical time coordinate, Lorentzian tetrad, TEGR field equation or RGS action is claimed.


## Affine SE(3) links and cubical Bianchi identity (27 November 2026)

The Q6 coframe increments and rotational links are now packaged as affine links
\[
\mathsf G_{gh}=(U_{gh},b_{gh}),\qquad b_{gh}=U_{gh}\theta_{gh},
\]
with \(SE(3)\) multiplication \((U,b)(V,c)=(UV,b+Uc)\). This choice makes reverse-edge inversion exact and agrees with the existing source-frame convention:
\[
\mathsf G_{hg}=\mathsf G_{gh}^{-1}=(U_{gh}^{T},-\theta_{gh}),\quad
U_{hg}=U_{gh}^{T},\quad \theta_{hg}=-U_{gh}\theta_{gh}.
\]
The affine face holonomy is \((H_p,t_p)\); its base-frame developed closure is \(H_p^{-1}t_p\), matching the previous discrete face torsion observable.

For each of the 160 Q6 elementary 3-cubes, the non-Abelian Bianchi consistency relation is formed from the six adjacent swaps in the permutation cycle
\(abc\to bac\to bca\to cba\to cab\to acb\to abc\).
Each square holonomy is transported to the cube base before ordered multiplication. The six based loops telescope to the identity in \(SE(3)\), with rotational and translational residuals checked separately. The audit also applies arbitrary local \(SE(3)\) frame changes and checks face-holonomy conjugation and the cube identity.

Implementation:
- scripts/audit_q6_se3_cartan_bianchi.py
- tests/test_q6_se3_cartan_bianchi.py
- research/Q6_SE3_CARTAN_CUBICAL_BIANCHI_AUDIT_2026-11-27.md

This is an exact finite groupoid identity for the present Q6 links, not yet a continuum Cartan theorem. The translational face holonomy is a closure/dislocation observable and candidate torsion diagnostic; identifying it with the continuum Cartan torsion 2-form requires a refinement/consistency result. The current model remains spatial \(SO(3)\ltimes\mathbb R^3\), with no variational action, Lorentzian lift, physical time leg, TEGR equivalence, or polariton/Q-ball identification established.
