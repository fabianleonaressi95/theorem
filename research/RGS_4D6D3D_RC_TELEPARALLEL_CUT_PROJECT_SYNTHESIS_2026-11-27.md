# RGS 4D–6D–3D geometry: recovered embedding, Cartan connection and teleparallel correspondence

**Date:** 27 November 2026  
**Status:** synthesis of prior finite constructions and theorem dependencies; the combined spacetime field theory and its refinement limit remain open.  
**Purpose:** prevent the 4D/6D/3D bridge and the curvature/torsion connection from being split into unrelated programmes.

## 0. Executive correction

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
