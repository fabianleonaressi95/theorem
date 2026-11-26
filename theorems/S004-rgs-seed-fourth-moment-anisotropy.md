# S.4 — Fourth-moment decomposition of the 64-site RGS seed

**Status: NUMERICALLY VERIFIED finite-seed record; algebraic tensor identities proved.** This is the fourth-moment bridge for the recovered 64-point RGS seed in three dimensions. It is not a Haar/600-cell fourth moment and it is not a torsion tensor.

## 1. Seed and raw moments

Let (x_n\in\mathbb R^3), (n=1,\ldots,64), be the recovered, hash-verified RGS seed coordinates used in the 4 November 2026 audit. The reported moments are **raw sums**, not averages:
[
M^{(2)}_{ij}=\sum_{n=1}^{64}x_{n,i}x_{n,j},\qquad
M^{(4)}_{ijkl}=\sum_{n=1}^{64}x_{n,i}x_{n,j}x_{n,k}x_{n,l}.
]
The second moment is
[
\boxed{M^{(2)}=80I_3.}
]
The fourth moment is fully symmetric under all permutations of its four indices. The stored audit reported the independent cubic-symmetry components
[
M^{(4)}_{xxxx}=195.9872446501,\qquad
M^{(4)}_{xxyy}=70.5968663330.
]
These decimal values are numerical outputs for the recovered seed, not exact rational identities.

## 2. Isotropic projection and anisotropic residual

In three dimensions the fully isotropic rank-four tensor with the symmetries of an even fourth moment has the form
[
M^{(4),\mathrm{iso}}_{ijkl}
=c(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
]
Double contraction gives
[
M^{(4),\mathrm{iso}}_{iikk}=15c,
\qquad
\boxed{c=\frac{M^{(4)}_{iikk}}{15}.}
]
For the recovered seed,
[
c=67.4361954632.
]
Define the residual
[
\boxed{R_{ijkl}=M^{(4)}_{ijkl}
-c(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).}
]
The reported components are
[
R_{xxxx}=-6.3213417395,\qquad
R_{xxyy}=+3.1606708698.
]
They obey the cubic-symmetry relation (R_{xxxx}=-2R_{xxyy}) to the displayed precision. The residual is the anisotropic part left after the full rotationally isotropic projection; it is not an arbitrary fitted correction.

## 3. Induced operator on symmetric trace-free tensors

For (Q\in\operatorname{Sym}_0(3)), define
[
(\mathcal A Q)_{ij}=R_{ijkl}Q_{kl}.
]
Because (R) is fully symmetric and has zero isotropic trace component, this contraction preserves the symmetric trace-free sector. Under the cubic symmetry of the seed, that five-dimensional space decomposes into the two-dimensional (E_g) and three-dimensional (T_{2g}) sectors. The recorded numerical eigenvalues are
[
\lambda(E_g)=-9.48201261\quad(\text{multiplicity }2),
\qquad
\lambda(T_{2g})=+6.32134174\quad(\text{multiplicity }3).
]
These are seed-specific numerical spectral values. The representation-theoretic block decomposition follows from cubic symmetry; the displayed decimal eigenvalues require reproduction from the full coordinate tensor.

## 4. What the fourth moment does and does not mean

1. (M^{(2)}=80I_3) records isotropy at second order for this seed and this raw-sum normalization.
2. (R\ne0) records a fourth-order anisotropy invisible to the second moment.
3. (R) is fully symmetric in all four indices. A torsion tensor (T^a{}_{bc}), by contrast, is antisymmetric in its last two indices. Therefore (R) cannot be identified with torsion by index relabelling.
4. A possible constitutive use is the linear map (\mathcal A\) on (\operatorname{Sym}_0(3)). This is a mathematically defined anisotropic operator; interpreting it as a physical stress, curvature, torsion, or gravitational field requires a separately specified constitutive/geometric model and dimensional normalization.

A proposed quadratic coupling
[
S_{\mathrm{aniso}}=\frac{\lambda}{2}\int dt\,d^3x\,N\sqrt h\,
Q^{ab}R_{abcd}Q^{cd}
]
and its formal variation
[
\Pi_{ab}=\lambda R_{abcd}Q^{cd}
]
are therefore **model proposals**, not consequences of the moment calculation and not established field equations.

## 5. Relationship to the other moment results

This fourth moment is distinct from all of the following:

- the triangle-cell covariance (\Sigma_F\) in T068;
- the weighted Dirichlet cell covariance (\Sigma_{F,a}\) in T070;
- the normalized Q6 point-cloud covariance (\Sigma_X=\frac1{64}\sum_vX_vX_v^T=\frac54I_3\) in T069;
- the Q6 vertex-measure covariance (\frac14I_6) recorded in the earlier centroid/FEM work;
- the fourth jump moment of a graph refinement, which controls the leading (O(a^2)) consistency correction in S.5.

They are different measures, dimensions, normalizations and geometric objects. A bridge between them requires an explicit map of observables and a normalization theorem.

## 6. Provenance and reproduction obligations

The central repository now contains a hash-checked reconstruction of the 64-site coordinate seed and the audit implementation/tests:
- `src/rgs_seed_64_reconstruction.py`
- `src/rgs_q6_oh_action.py`
- `src/rgs_fourth_moment_bridge.py`
- `tests/test_rgs_fourth_moment_bridge.py`

The seed provenance is A14_RGS_PSU_QLG_JACOBIAN_BUNDLE.zip (archive SHA-256 `80442238349cd6ddc720dabae93d083075dea88decba8acf0a78c3ec03e0abcc`); the reconstructed float64 coordinate array has SHA-256 `6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf`. The loader verifies the array hash before returning the coordinates.

In this synthesis turn, the coordinate reconstruction and key fourth-moment quantities were independently recomputed from the archived orbit constants: (M^{(2)}=80I_3), the coefficient (c), the displayed (M^{(4)}) and (R) components, the trace-free/orthogonality residuals, the (O_h) invariance residual (approximately (2.8\times10^{-13})), and the (E_g/T_{2g}) eigenvalue split. This is an independent numerical replay of the core formulas, not a claim that the full imported pytest suite has been executed. The repository audit/test now makes that full replay reproducible.

## 7. Evidence classification

- **PROVED algebraically:** full symmetry of (M^{(4)}); isotropic rank-four projector formula; contraction factor 15 in dimension three; definition and tensor symmetries of (R); induced contraction operator.
- **NUMERICALLY VERIFIED in the prior seed audit:** (M^{(2)}=80I_3), the reported fourth-moment components, (c), residual components and (E_g/T_{2g}) eigenvalues.
- **OPEN for this repository:** self-contained replay from the original coordinate artifact; exact symbolic form of the seed moments; physical constitutive interpretation; any identification with torsion or curvature.
