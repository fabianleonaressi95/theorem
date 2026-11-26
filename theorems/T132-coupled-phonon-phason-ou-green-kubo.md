# T132 — Coupled phonon–phason stress correlations: exact OU benchmark

**Classification:** [P] exact finite-dimensional Gaussian identities under the stated reversible OU hypotheses; [N] deterministic block-sum checks and seeded exact-step Monte Carlo benchmark; [O] material Hamiltonian, Q6 calibration, physical phason kinetics, microscopic stress derivation and material transport.

**Dependencies:** T113-D, T113-G, T131. T132 is a controlled benchmark for T131's sector decomposition and Onsager–Casimir bookkeeping. It does not identify graph-internal variables with physical phasons.

## 1. Purpose and evidence boundary

This record constructs the smallest coupled two-coordinate model in which phonon, phason and interaction stress contributions can be separated and recombined exactly. It tests the algebra of the nine ordered sector-pair correlations and the zero-field reciprocal symmetry. A reversible Ornstein–Uhlenbeck (OU) process supplies a justified relaxation mechanism for this benchmark, so its finite correlation integral exists.

The OU bath is a mathematical benchmark input. It is **not** asserted to represent anharmonic relaxation, phonon scattering, phason flips, or a calibrated material. The resulting integrated response is a model coefficient in the benchmark's chosen units, not a measured or predicted material viscosity.

## 2. Coupled equilibrium model

Let \(q=(u,w)^T\), where \(u\) and \(w\) are independent model coordinates labelled phonon and phason. Set
\[
H(q)=\frac12q^TKq,\qquad
K=\begin{pmatrix}k_u&g\\g&k_w\end{pmatrix}=K^T\succ0.
\]
The nonzero off-diagonal coefficient \(g\) couples the two coordinates. At temperature \(T\), the equilibrium distribution is Gaussian with covariance
\[
\Sigma=k_BT K^{-1}.
\]
The reversible overdamped dynamics is
\[
dq=-\mu Kq\,dt+\sqrt{2\mu k_BT}\,dW_t,\qquad \mu>0.
\]
It has invariant covariance \(\Sigma\), satisfies detailed balance, and has propagator
\[
A(t)=e^{-\mu Kt},\qquad E(t)=\mathbb E[q(t)q(0)^T]=A(t)\Sigma.
\]
Because \(K\) is symmetric positive definite, the eigenvalues of the drift are positive and correlations relax exponentially.

## 3. Sector-resolved stress observables

Choose symmetric matrices \(S_{\rm ph},S_{\rm pha},S_{\rm int}\) and define centered quadratic observables
\[
\Pi_a(q)=\frac12\left(q^TS_aq-\operatorname{tr}(S_a\Sigma)\right),
\qquad a\in\{{\rm ph,pha,int}\}.
\]
They are a declared benchmark decomposition. The interaction matrix \(S_{\rm int}\) is not inferred from the coupling \(g\); in a material model all three matrices must be derived by differentiating one specified strain-dependent Hamiltonian, as required by T131.

For jointly Gaussian \(q(t),q(0)\), Wick's identity gives the exact ordered block
\[
\boxed{
C_{ab}(t)=\langle\Pi_a(t)\Pi_b(0)\rangle
=\frac12\operatorname{tr}\!\left[S_aE(t)S_bE(t)^T\right].
}
\]
Thus the total stress \(\Pi=\sum_a\Pi_a\) obeys
\[
C_{\Pi\Pi}(t)=\sum_{a,b}C_{ab}(t).
\]
There are three diagonal autocorrelations and six ordered cross-correlations. The \(({\rm int,int})\) entry is the interaction-stress autocorrelation, not a cross term.

## 4. Zero-field reciprocity and integrated response

The OU process above is reversible and has no time-reversal-odd external field. Its equilibrium cross-correlation matrix satisfies
\[
C_{ab}(t)=C_{ba}(t)
\]
for the even quadratic stress observables used here. This is the zero-field Onsager reciprocal benchmark. It does not imply that arbitrary non-equilibrium, driven, magnetic, or non-reversible models have the same symmetry; those require the full Onsager–Casimir field reversal and parity bookkeeping in T131.

The finite-window integrated block is
\[
\mathcal L_{ab}(t_{\max})=
\frac{1}{k_BT}\int_0^{t_{\max}}C_{ab}(t)\,dt.
\]
The total response is exactly the sum of all nine integrated blocks. Since the OU drift is stable, the infinite-time integral also exists in this finite model. Numerical output is nevertheless reported at finite \(t_{\max}\), with convergence checked by increasing the cutoff. No volume normalization is inserted: these \(\Pi_a\) are abstract benchmark observables, not extensive material stresses in a physical volume.

## 5. Reproducible implementation and tests

- Implementation: \`audits/phonon_phason/coupled_ou_green_kubo.py\`.
- Tests: \`tests/test_t132_coupled_ou_green_kubo.py\`.
- The exact correlation uses the matrix exponential obtained from the symmetric eigendecomposition of \(K\).
- The stochastic trajectory uses the exact finite-step OU transition and its invariant Gaussian covariance, not an Euler time-step approximation.
- Tests check zero-field reciprocity, exact recombination of all nine blocks into the total-stress correlation, block-sum consistency of the finite Green–Kubo integral, and agreement of the seeded simulation with the analytic lag-zero stress covariance within a declared Monte Carlo tolerance.

The benchmark uses synthetic \(K\) and \(S_a\) matrices. It does not contain Q6-derived force constants, a six-axis material embedding, a microscopic phason transition network, an anharmonic potential, a material strain derivative, or an independently validated bath.

## 6. Classification and next acceptance gates

- **[P]** Gaussian covariance, exact OU propagator, Wick correlation formula and nine-block recombination under the stated hypotheses.
- **[N]** Reproducible finite-dimensional computation and seeded Monte Carlo comparison. These are software/model checks, not experimental validation.
- **[O]** Derive \(K\) and all \(S_a\) from a common strain-dependent Q6/material Hamiltonian; specify physical masses and geometry; derive phason kinetics and anharmonic relaxation rather than inserting a bath by convenience; derive the microscopic momentum flux; test finite-size and long-time convergence; only then interpret an integrated response as a material transport coefficient.

No isotropic average over the six Q6 directions is introduced. A future Q6 realization must retain the six-axis anisotropy and report the full response tensor before any symmetry reduction.
