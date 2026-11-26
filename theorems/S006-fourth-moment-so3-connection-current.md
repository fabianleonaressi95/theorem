# S.6 — Fourth-moment constitutive operator and SO(3) connection current

**Status: PROVED local finite-dimensional variational identity.** The positivity and current formula are exact under the hypotheses below. The finite-difference implementation is evidence only after its tests are executed. This is not a complete teleparallel or Einstein–Cartan theory.

## 1. Fourth-moment operator and positive shift

Let \(R_{abcd}\) be the fully symmetric, pair-trace-free cubic residual defined in S.4. It induces a self-adjoint map on \(\operatorname{Sym}_0(3)\):
\[
(AQ)_{ab}=R_{abcd}Q_{cd}.
\]
For a real parameter \(\beta\), set
\[
\mu=\max\{0,-\lambda_{\min}(\beta A)\}+\varepsilon,\qquad
\varepsilon>0,\qquad H=\mu I+\beta A.
\]
Then \(H\) is strictly positive on \(\operatorname{Sym}_0(3)\), with
\[
\lambda_{\min}(H)\geq\varepsilon.
\]
The shift is a stability regularization, not a measured coupling or a new fundamental constant.

## 2. Covariant derivative and gradient energy

Let \(Q(x)\in\operatorname{Sym}_0(3)\) be an independent order parameter and let \(\omega_i(x)\in\mathfrak{so}(3)\) be a spatial connection. Define
\[
D_iQ=\partial_iQ+[\omega_i,Q],
\qquad
\mathcal L_{\mathrm{grad}}=
\frac{\kappa}{2}\sum_i\langle D_iQ,H(D_iQ)\rangle_F,
\quad \kappa\geq0.
\]
Because \(\omega_i\) is antisymmetric and \(Q\) symmetric, \([\omega_i,Q]\) is symmetric; its trace vanishes. Thus \(D_iQ\in\operatorname{Sym}_0(3)\), and positivity of \(H\) gives \(\mathcal L_{\mathrm{grad}}\geq0\).

Under a local frame transformation \(U(x)\in SO(3)\),
\[
Q'=UQU^T,\quad R'=U^{\otimes4}R,\quad
\omega_i'=U\omega_iU^T-(\partial_iU)U^T,
\]
the derivative and \(H\) transform covariantly, and the Frobenius energy is invariant. If the material components of \(R\) are held fixed rather than transformed, the symmetry is reduced to the stabilizer of the cubic material tensor. This is a local tensorial covariance statement, not by itself a global bundle construction.

## 3. Connection variation and current

For a variation \(\delta\omega_i\in\mathfrak{so}(3)\),
\[
\delta(D_iQ)=[\delta\omega_i,Q].
\]
With the Frobenius pairing \(\langle X,Y\rangle_F=\operatorname{tr}(X^TY)\),
\[
\delta\mathcal L_{\mathrm{grad}}
=\sum_i\langle J_i,\delta\omega_i\rangle_F,
\qquad
\boxed{J_i=\kappa[H(D_iQ),Q]\in\mathfrak{so}(3).}
\]
The commutator of two symmetric matrices is antisymmetric, so the current has the required Lie-algebra symmetry.

## 4. Proof

The map \(A\) is self-adjoint because \(R_{abcd}=R_{cdab}\). The definition of \(\mu\) gives
\[
\lambda_{\min}(H)=\mu+\lambda_{\min}(\beta A)\geq\varepsilon,
\]
hence strict positivity. Also
\[
[\omega_i,Q]^T
=(\omega_iQ-Q\omega_i)^T
=Q(-\omega_i)-(-\omega_i)Q
=\omega_iQ-Q\omega_i,
\]
and \(\operatorname{tr}[\omega_i,Q]=0\) by cyclicity.

Put \(S_i=H(D_iQ)\), which is symmetric. Then
\[
\begin{aligned}
\delta\mathcal L_i
&=\kappa\operatorname{tr}(S_i[\delta\omega_i,Q])\\
&=\kappa\operatorname{tr}((QS_i-S_iQ)\delta\omega_i).
\end{aligned}
\]
Since \(J_i=\kappa(S_iQ-QS_i)\) is antisymmetric, \(J_i^T=\kappa(QS_i-S_iQ)\). Therefore the last expression is exactly \(\langle J_i,\delta\omega_i\rangle_F\), proving the current formula.

## 5. Boundary of the claim

This is a derivative coupling to an \(\mathfrak{so}(3)\)-valued connection. It is not yet a complete teleparallel theory. Imposing flatness \(R(\omega)=0\) requires constrained variation or an inertial spin-connection parametrization. The coframe equation, lapse/shift constraints, TEGR sector, matter terms and boundary terms have not been combined. A local connection current has been derived; a solved torsion field equation has not.

## 6. Evidence classification

- **PROVED:** positivity of the shifted operator; preservation of \(\operatorname{Sym}_0(3)\); local frame covariance under simultaneous tensor transformations; connection-current variation.
- **IMPLEMENTED, NOT EXECUTION-CERTIFIED HERE:** positive shifted metric, nonnegative gradient energy, antisymmetric current and finite-difference variation checks are supplied by the companion source/tests.
- **OPEN:** constrained flat-connection variation; full TEGR/coframe equations; Q6/Yang–Mills/fermion coupling; continuum or Mosco limit.

Companion source and test files are imported into this repository as src/rgs_fourth_moment_connection.py and tests/test_rgs_fourth_moment_connection.py.
