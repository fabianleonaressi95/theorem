# RGS–Q6 Anti-Twin spacetime bridge: 4D first, then 6D and 3D

**Date:** 2026-11-27  
**Classification:** exact finite-chain framework and implementation specification; the dynamical 4D tetrad, TEGR identification and MHD coupling remain open.  
**Required order:** complete the 4D connection layer; return to the 6D physical/internal split; only afterwards perform the 3D cut-and-project realization.

## 0. Essential correction

Q6 is a six-bit combinatorial carrier, not a claim that physical space has six dimensions. Its standard cubical data include 64 vertices, 192 edges and 240 square faces. A physical 3+1 geometry requires a spatial realization/coframe on the 64 labels plus a temporal direction and a compatible transport law.

The companion work associated with PR #234 reconstructs a static RGS spatial coframe and a static lift e_i=diag(1,E_i). This is not a coordinate-dependent spacetime tetrad and does not determine a time coordinate, derivatives, inertial spin connection, TEGR torsion or field equations. The fourth component of the historical QLG edge coframe is a radial increment, not physical time. These distinctions are mandatory.

This document therefore specifies the missing discrete temporal transport layer without claiming that the full continuum 4D tetrad has already been derived.

## 1. Fixed spatial carrier and two sheets

Let K be the chosen oriented cubical carrier on the 64 Q6 labels, with chain groups C_k(K) and integer boundary maps
\[
B_k:C_k(K)\to C_{k-1}(K),\qquad B_{k-1}B_k=0.
\]
For the standard 2-skeleton:
\[
\dim C_0=64,\quad \dim C_1=192,\quad \dim C_2=240,
\]
and B_1 is 64×192, B_2 is 192×240, with B_1B_2=0.
Orient each cell by the increasing order of its free coordinate axes. The 240 faces must retain their orientation signs; unsigned face permutations are insufficient. The full cubical complex also has 160 three-cells; these are required to define the degree-2 Hodge Laplacian through B_3.

The Anti-Twin double is
\[
C_k^{AT}=C_k(K)\oplus C_k(K),\qquad
S_k(c_+,c_-)=(c_-,c_+),\qquad S_k^2=I.
\]
Its spatial boundary is
\[
\mathbb B_k=\begin{pmatrix}B_k&0\\0&B_k\end{pmatrix},
\qquad \mathbb B_{k-1}\mathbb B_k=0,\qquad [\mathbb B_k,S_k]=0.
\]
The even/odd projectors are exactly
\[
P_{e/o}=\tfrac12(I\pm S_k).
\]
Here 1/2 is the normalization of the two-sheet decomposition. It is not, without a separate derivation, a coefficient of a physical action or a consequence of Möbius topology.

## 2. Temporal transport and the 4D chain condition

Choose time slices t_n. For each degree k, temporal transport is a linear map
\[
U_k(n):C_k^{AT}(t_n)\longrightarrow C_k^{AT}(t_{n+1}).
\]
The defining compatibility is
\[
\boxed{\mathbb B_k(n+1)U_k(n)=U_{k-1}(n)\mathbb B_k(n).}\tag{2.1}
\]
Transporting a cell and then taking its boundary must agree with taking its boundary and then transporting. This preserves the chain identities at each time slice.

In the Anti-Twin-symmetric regime impose
\[
[U_k(n),S_k]=0.\tag{2.2}
\]
A block form that satisfies the sheet-exchange commutation condition is
\[
U_k(n)=\begin{pmatrix}A_k(n)&C_k(n)\\C_k(n)&A_k(n)\end{pmatrix}.
\]
Invertibility, unitarity or orthogonality must be selected according to the actual transported field; do not assume unitarity for a generic cochain transport.

A Möbius seam is represented by the transition map S_k: crossing the seam exchanges the sheets. Its square is the identity on the sheet fibre. The global holonomy around a loop is the ordered product of link transports and seam transitions. A nontrivial sheet exchange is not itself a nonzero Cartan torsion tensor.

### 2.1 Canonical chain-compatible time generator

There is a nontrivial finite-dimensional temporal model available without inventing edge weights. Equip the oriented cell bases with the declared Euclidean inner products and define the cubical Hodge Laplacian
\[
L_k=B_k^TB_k+B_{k+1}B_{k+1}^T.
\]
The cubical chain identity implies the exact intertwining relation
\[
B_kL_k=L_{k-1}B_k.
\]
On the doubled complex define
\[
H_k=L_k\otimes I_2+\mu I_{C_k}\otimes(I_2-S),
\qquad \mu\in\mathbb R.
\]
Because the sheet coupling is degree-independent and acts only on the two-sheet factor,
\[
\mathbb B_kH_k=H_{k-1}\mathbb B_k,
\qquad [H_k,S_k]=0.
\]
Consequently both the unitary real-time evolution
\[
U_k(t)=e^{-itH_k}
\]
and the dissipative semigroup \(e^{-tH_k}\) satisfy the temporal chain-map condition (2.1). For real \(\mu\), \(H_k\) is self-adjoint; for \(\mu\geq0\), it is positive semidefinite.

In the even/odd sheet sectors, \(I-S\) has eigenvalues 0 and 2, so
\[
H_{k,e}=L_k,\qquad H_{k,o}=L_k+2\mu I.
\]
This gives an exact, parameter-explicit Anti-Twin splitting. The Möbius seam remains the transition S; the coupling \(\mu\) is a separate dynamical parameter. This construction is a canonical Hodge/chain benchmark, not yet the MHD generator, not a derived Lorentzian tetrad, and not a claim about physical time measured in seconds. A numerical audit should verify the identities using the oriented incidence matrices before any physical interpretation.

## 3. Space-time plaquettes and discrete curvature

Let V_v(n) be the temporal link at vertex v and U_vw(n) the spatial link on an oriented edge v→w. With the convention that the rightmost map acts first, define the temporal-spatial plaquette holonomy
\[
H_{0e}(v,n)=V_w(n)U_{vw}(n)V_v(n)^{-1}U_{vw}(n+1)^{-1}.
\]
Its deviation from identity is the discrete mixed space-time curvature/field-strength diagnostic. Spatial plaquette holonomies H_ij remain associated with the 240 oriented square faces. Both require orientation-aware products and gauge-covariant base-point conventions.

For the double sheet, links are block operators on the sheet index. Insert the seam transition only on links crossing the declared seam; do not apply it to arbitrary edges.

## 4. Continuum 3+1 coframe: required data

A genuine Lorentzian coframe must be a nondegenerate field on a declared four-dimensional base:
\[
e^a=e^a{}_\mu(x,t)dx^\mu,\qquad
g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu,\quad
\eta=\operatorname{diag}(-1,1,1,1).
\]
A useful parametrization, not a fitted solution, is
\[
e^0=N\,dt,\qquad e^a=E^a{}_i(x,t)(dx^i+\beta^i dt),\quad a=1,2,3.
\]
The lapse N, shift β^i and time dependence of E^a_i must be derived from the chosen dynamics/constraints. The static companion lift is only a special time-independent block choice and does not determine these functions.

For covariant teleparallel geometry one must specify the inertial Lorentz spin connection ω^a_bμ, with
\[
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b=0,
\qquad
T^a=de^a+\omega^a{}_b\wedge e^b.
\]
A tetrad array at 64 labels without a base-manifold interpolation and a declared spin connection does not define these derivatives. No TEGR/Einstein-equivalence or nonzero torsion claim is made here.

## 5. Keep vorticity, curvature and torsion distinct

1. MHD vorticity is ζ=∇×u, determined by the fluid velocity and its spatial derivative.
2. Connection curvature is measured by spatial and temporal plaquette holonomies H_ij and H_0i.
3. Cartan torsion is T^a=de^a+ω^a_b∧e^b, determined by a coframe and spin connection.

They are not interchangeable. The MHD induction equation
\[
\partial_t\mathbf B=\nabla\times(\mathbf u\times\mathbf B)+\eta_m\nabla^2\mathbf B,\qquad \nabla\cdot\mathbf B=0
\]
can be discretized on the spatial carrier once metric/Hodge-star data, boundary conditions and compatible incidence operators are fixed. Coupling it to the Anti-Twin connection is a model to test, not an identity implied by the double cover.

## 6. Green and Green–Kubo interfaces already available

The vertex graph Laplacian and the face Hodge Laplacian are different operators and must remain distinct.

For the standard cubical 2-skeleton, the existing face-cochain dossier establishes
\[
Z^2=\ker B_3^T=\operatorname{im}B_2^T,\quad \dim Z^2=129,
\]
and the restricted face Hodge operator A=Δ_2|_{Z²} has exact spectrum
\[
\lambda=4,6,8,10,12,\qquad m_\lambda=15,40,45,24,5.
\]
For the declared reversible OU dynamics
\[
d\Omega=-\gamma A\Omega\,dt+\sqrt{2\gamma\sigma^2A}\,dW,
\]
the exact face Green–Kubo functional is
\[
\mathcal G_{\rm face}(b)=\frac{\sigma^2}{\gamma}
\sum_\lambda\frac{\|\Pi_\lambda b\|^2}{\lambda}.
\]
This is proved for that finite-dimensional stochastic model; physical stress/viscosity interpretation remains open.

For Anti-Twin take b_AT=b_+−b_- only when b_± belong to Z², and evaluate the functional on the appropriate invariant sector. A time-dependent generator requires a separately specified reversible measure and stability analysis. Do not identify the face Hodge operator with the vertex graph Laplacian or reuse a vertex Green value as a face result.

The Q6 cosine face functional
\[
\mathcal F(\Omega)=\sum_{p=1}^{240}(1-\cos\Omega_p)
\]
has the exact local expansion \(\mathcal F(\Omega)=\frac12\|\Omega\|^2+O(\|\Omega\|^4)\). Any connection to the historical Δμ_4 law must preserve the same oriented face variables and normalization.

## 7. Gradients, barycentres and coframe data

The 64-site RGS seed X:Q6→R³ is the spatial carrier. Gradients and barycentres must be computed from this declared embedding and the local metric/weights, not from an invented 6D projection. For each sheet retain separate data X_±, E_±, g_±. Define Anti-Twin differences only after transporting both objects to a common frame:
\[
\delta X_c=X_c^+-X_c^-,
\quad \delta E=E_+-E_-,
\quad \delta\nabla f=\nabla_+f_+-\nabla_-f_-.
\]
A difference of vectors in different local frames is not meaningful until frame transport is applied. The existing discrete coframe/face-torsion tetrahedron note is a candidate construction with covariance checks, not a continuum torsion theorem.

## 8. Required finite audit sequence

1. Reconstruct oriented B_1,B_2 and verify B_1B_2=0 exactly.
2. Build the doubled chain maps and verify B̲_1B̲_2=0, S²=I and [B̲_k,S_k]=0.
3. Construct a nontrivial temporal transport U_k(n) from declared link data and verify (2.1) degree by degree.
4. Verify [U_k,S_k]=0 in the symmetric case; introduce a controlled sheet-asymmetric perturbation and measure the commutator in the broken case.
5. Compute spatial and mixed space-time plaquette holonomies, checking gauge covariance and orientation reversal.
6. Only after a coordinate-dependent coframe and inertial spin connection are supplied, compute T^a, R^a_b, torsion irreducible pieces and the TEGR scalar.
7. Couple the MHD discretization and verify discrete divergence preservation, energy balance and continuum-limit conventions.
8. Recompute the face Green–Kubo functional on Anti-Twin sectors; do not assume the previous OU generator is the MHD generator.

## 9. Ordered continuation: 4D, then 6D, then 3D

### Stage A — finish the 4D layer

Inputs: the hash-checked 64-by-3 spatial seed, oriented cubical incidence, the companion spatial coframe reconstruction and declared temporal link variables. Output: a chain-compatible 3+1 transport complex, space-time plaquette holonomies and a clearly separated coframe/torsion status.

### Stage B — recover the six-dimensional physical/internal split

Only after Stage A is stable, recover a canonical pair of orthogonal three-planes
\[
\mathbb R^6=E_\parallel\oplus E_\perp,\quad
B_\parallel^TB_\parallel=B_\perp^TB_\perp=I_3,\quad
B_\parallel^TB_\perp=0.
\]
The previously discussed golden/icosahedral φ,φ* matrices are a generic template, not an established Q6 embedding. The current theorem T113-G explicitly states that the repository's 64-by-3 seed and abstract Q6 adjacency do not determine the canonical 6D lattice basis, physical/internal split or acceptance window. Do not promote the provisional spherical window to a canonical window.

### Stage C — derive the three-dimensional cut-and-project set

After the 6D data are fixed, declare the lattice L⊂E_parallel⊕E_perp, projections P_parallel,P_perp and a justified acceptance window W⊂E_perp, then form
\[
\Lambda=\{P_\parallel n:n\in L,\ P_\perp n\in W\}.
\]
Derive neighbour stars, phonon/phason coordinates, interactions and symmetry from this actual projected set. Only then compare its induced 3D geometry with the RGS 64-site seed and 188D tangent sector. Do not infer a 6D cut-and-project scheme from the 64-by-3 coordinates alone, and do not impose anisotropy or isotropy before deriving the symmetry of the complete data.

## 10. Integration with QHD, Maxwell and quaternionic transport

The full formal crosswalk is maintained in `research/RGS_Q6_ANTITWIN_QHD_MAXWELL_QUATERNION_FORMALIZATION_2026-11-27.md`. It reuses the established QHD/MHD, Maxwell, quaternionic SU(2), S011 variational and T063 results, while separating exact discrete Bianchi/chain identities from the still-open coupled action and continuum limit. This document remains the 4D geometric/transport specification; the companion formalization is the field-theory interface. Both retain the ordered continuation 4D → 6D → 3D cut-and-project.

## 10. Status ledger

| Item | Status |
|---|---|
| Q6 counts and oriented cubical boundary identity | Exact finite combinatorics |
| Anti-Twin doubled chain complex and even/odd projectors | Exact algebraic construction |
| Temporal chain-map condition (2.1) | Exact criterion; Hodge-generated model supplied in §2.1 |
| Hodge-generated Anti-Twin time generator | Exact finite algebraic model; physical identification open |\n| Möbius sheet-exchange transition | Exact topological model |
| Static RGS spatial coframe reconstruction | Reproducible companion result; not a dynamical tetrad |
| 4D Lorentzian tetrad, lapse/shift and inertial spin connection | Open |
| TEGR torsion/curvature identity for this RGS model | Not certified |
| Face Hodge spectrum and OU Green–Kubo formula | Exact for the stated finite model |
| Physical MHD/viscosity interpretation | Open |
| Canonical Q6 six-dimensional embedding/window | Open (T113-G) |
| Three-dimensional cut-and-project realization from Q6 | Open pending Stage B |

## Repository dependencies

- docs/RGS_QLG_QAT_VIERBEIN_RECOVERY_AUDIT.md — separates archived edge coframe, spatial vertex field and proposed Lorentzian tetrad.
- theorems/Q6_FACE_COCHAINS_HODGE_GREEN_KUBO_2026-11-23.md — exact face-cochain and OU/Green–Kubo result.
- docs/DISCRETE_COFRAME_TORSION_TETRAHEDRON_2026-11-26.md — candidate discrete coframe/face torsion definition and limitations.
- theorems/T113G-cut-project-symmetry-rank-two-isotropy.md — current Q6/RGS cut-and-project data boundary.\n- scripts/audit_q6_antitwin_temporal_chain.py — exact sparse-rational audit of the Hodge-generated temporal chain identities (not yet executed in this PR).
- Companion repository rgs-qlg-quaternion-bridge, PR #234 — deterministic spatial coframe/static-lift reconstruction; not a dynamical spacetime tetrad.
- Teleparallel convention: tetrad/coframe plus inertial flat Lorentz spin connection are the fundamental data; torsion is computed only after both are specified. See EPJC (2021), DOI 10.1140/epjc/s10052-021-09165-x.
