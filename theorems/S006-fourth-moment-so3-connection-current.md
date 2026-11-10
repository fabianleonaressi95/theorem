# S.6 — Fourth-moment constitutive operator and SO(3) connection current

**Status: PROVED local finite-dimensional variational identity; numerical variation checks are in the companion implementation.** This record extends S.4. It does not constitute a complete teleparallel or Einstein–Cartan theory.

## 1. Fourth-moment operator and positive shift

Let (R_{abcd}) be the fully symmetric, trace-free, cubic-invariant residual from S.4. It induces a self-adjoint linear map on (operatorname{Sym}_0(3)):
[
(AQ)_{ab}=R_{abcd}Q_{cd}.
]
The recorded seed spectrum has a negative (E_g) eigenvalue, so (A) itself is not a positive kinetic metric. For (etainmathbb R), define
[
mu=max{0,-lambda_{min}(eta A)}+arepsilon,qquad arepsilon>0,
quad H=mu I+eta A.
]
Then (H) is strictly positive on (operatorname{Sym}_0(3)). The shift is a stability regularization, not a measured coupling or a new fundamental constant.

## 2. Covariant derivative and gradient energy

Let (Q(x)inoperatorname{Sym}_0(3)) be an independent order parameter and let (omega_i(x)inmathfrak{so}(3)) be a spatial connection. Define
[
D_iQ=partial_iQ+[omega_i,Q],
qquad
mathcal L_{mathrm{grad}}=rac{kappa}{2}sum_i
langle D_iQ,H(D_iQ)angle_F,quad kappageq0.
]
Because (omega_i) is antisymmetric and (Q) symmetric, ([omega_i,Q]) is symmetric; its trace vanishes. Thus (D_iQinoperatorname{Sym}_0(3)), and positivity of (H) gives (mathcal L_{mathrm{grad}}geq0).

Under a local frame transformation (U(x)in SO(3)),
[
Q'=UQU^T,quad R'=U^{otimes4}R,quad
omega_i'=Uomega_iU^T-(partial_iU)U^T,
]
the derivative and (H) transform covariantly, and the Frobenius energy is invariant. If the material components of (R) are held fixed rather than transformed, the symmetry is reduced to the stabilizer of the cubic material tensor. This is a pointwise tensorial covariance statement; it is not by itself a global bundle construction.

## 3. Connection variation

For a variation (deltaomega_iinmathfrak{so}(3)),
[
delta(D_iQ)=[deltaomega_i,Q].
]
Using the Frobenius pairing and the symmetry of (H(D_iQ)) and (Q),
[
deltamathcal L_{mathrm{grad}}
=sum_ilangle J_i,deltaomega_iangle_F,
qquad
oxed{J_i=kappa[H(D_iQ),Q]inmathfrak{so}(3).}
]
The commutator of two symmetric matrices is antisymmetric, so the current has the required Lie-algebra symmetry.

## 4. Proof

The map (A) is self-adjoint because (R_{abcd}=R_{cdab}). By the spectral theorem, (lambda_{min}(H)=mu+lambda_{min}(eta A)geqarepsilon), hence strict positivity. The commutator ([omega_i,Q]) is symmetric since
[
(omega_iQ-Qomega_i)^T=Q(-omega_i)-(-omega_i)Q
=omega_iQ-Qomega_i,
]
and is trace-free by cyclicity of trace.

For the variation, write (S_i=H(D_iQ)), which is symmetric. Then
[
deltamathcal L_i=kappaoperatorname{tr}(S_i[deltaomega_i,Q])
=kappaoperatorname{tr}((QS_i-S_iQ)deltaomega_i).
]
Since (J_i=kappa(S_iQ-QS_i)) is antisymmetric, (J_i^T=-J_i), and the last expression equals (langle J_i,deltaomega_iangle_F). This proves the formula.

## 5. Boundary of the claim

This is a derivative coupling to an (mathfrak{so}(3))-valued connection. It is not yet a complete teleparallel theory. Imposing flatness (R(omega)=0) requires constrained variation or an inertial spin-connection parametrization. The coframe equation, lapse/shift constraints, TEGR sector, matter terms and boundary terms have not been combined. A current has been derived; a solved torsion field equation has not.

## 6. Evidence

- **PROVED:** positivity of the shifted operator; preservation of (operatorname{Sym}_0(3)); local frame covariance under simultaneous tensor transformations; connection-current variation.
- **NUMERICALLY VERIFIED in companion code/tests:** positive shifted metric, nonnegative gradient energy, antisymmetric current and finite-difference variation.
- **OPEN:** constrained flat-connection variation; full TEGR/coframe equations; Q6/Yang–Mills/fermion coupling; continuum or Mosco limit.

Implementation and tests are in the bridge repository at src/rgs_fourth_moment_connection.py and tests/test_rgs_fourth_moment_connection.py. The theorem statement is self-contained; the finite-difference test evidence remains implementation evidence.
