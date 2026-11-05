# Phenomenological dust-like torsion contribution to FLRW

**Status: MODEL CONSISTENCY RESULT. Not a derivation of Einstein--Cartan cosmology.**

## 1. Definition

Use dimensionless densities normalized to the present critical density and set
\(a_0=1\). The proposed background ansatz is

\[
E(a)^2=\Omega_{r0}a^{-4}
      +\Omega_{m0}(1+\beta)a^{-3}+\lambda,
\qquad E(a)=H(a)/H_0.
\]

It is useful to split the effective matter term as

\[
\rho_m(a)=\Omega_{m0}a^{-3},\qquad
\rho_T(a)=\beta\Omega_{m0}a^{-3}.
\]

Here \(\rho_T\) is a phenomenological bookkeeping sector. It is not, by
definition, the algebraic Einstein--Cartan spin-torsion correction.

## 2. Conservation fixes the pressure

For a separately conserved homogeneous component,

\[
\frac{d\rho_T}{d\ln a}+3(\rho_T+p_T)=0.
\]

Since \(d\rho_T/d\ln a=-3\rho_T\), the equation gives

\[
\boxed{p_T=0.}
\]

Therefore the assignment \(p_T=\rho_T/3\) is incompatible with the assumed
\(a^{-3}\) scaling unless an interaction term is added to the continuity
equation or the background scaling is changed. Neither modification is part
of this baseline model.

The effective pressure and density are

\[
\rho_{\rm eff}=\Omega_{r0}a^{-4}
+\Omega_{m0}(1+\beta)a^{-3}+\lambda,
\qquad
p_{\rm eff}=\frac{\Omega_{r0}}{3}a^{-4}-\lambda.
\]

## 3. Flat closure and limiting cases

The normalization \(E(1)^2=1\) requires

\[
\boxed{\Omega_{r0}+\Omega_{m0}(1+\beta)+\lambda=1.}
\]

Thus

\[
\lambda=1-\Omega_{r0}-\Omega_{m0}(1+\beta).
\]

On the \(\lambda=0\) boundary,

\[
\boxed{\Omega_{m0}=\frac{1-\Omega_{r0}}{1+\beta}},
\qquad \beta>-1.
\]

The GR/LCDM background is recovered at \(\beta=0\). The no-matter limit
\(\Omega_{m0}=0\) removes the torsion bookkeeping sector as well.

## 4. Einstein--Cartan interpretation boundary

In Einstein--Cartan theory, torsion is algebraically related to the spin
current; it is not generically an independent propagating dust fluid. Its
effective contribution after eliminating torsion depends on the matter
spin-density and averaging assumptions. Consequently, the scaling
\(\rho_T\propto a^{-3}\) and \(p_T=0\) must be treated as a phenomenological
closure until derived from a specified spin-fluid action or microscopic
averaging procedure.

This note does not identify \(\beta\) with a universal Einstein--Cartan
coupling, does not add a propagating torsion degree of freedom, and does not
claim observational viability.

## 5. Reproducible implementation

The dimensionless background and its consistency residuals are implemented in
`scripts/torsion_lambda_dust_closure.py`. Regression tests are in
`tests/test_torsion_lambda_dust_closure.py`.

The exact analytic conservation residual is zero by construction. The tests
check the flat normalization, the corrected \(\lambda=0\) boundary, the
\(\beta=0\) GR limit, the effective pressure, and invalid parameter inputs.

## 6. Evidence classification

- **Algebraically established:** \(p_T=0\) follows from separate conservation
  and the assumed \(a^{-3}\) law.
- **Algebraically established:** the flat closure and \(\lambda=0\) boundary
  above follow from the chosen Friedmann ansatz.
- **Implemented, pending CI:** the Python reference model and regression tests.
- **Open:** derivation of this closure from an Einstein--Cartan spin-fluid
  action; perturbation equations and growth observables; observational
  constraints; alternatives with interaction \(Q\) or radiation-like scaling.
