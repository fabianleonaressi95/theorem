# Sakharov induced gravity, heat supertraces and the PSU–RGS–Anti-Twin Cartan wormhole

**Date:** 2026-11-28  
**Status:** integrated research specification. Historical finite-dimensional audits are recorded as numerical/algebraic results; induced gravitational dynamics, physical supersymmetry and the Q6 continuum limit remain open.

## 1. Role in the unified programme

Sakharov induced gravity belongs to the same PSU–RGS–Anti-Twin construction as the toroidal wormhole. The intended chain is
\[
\text{Q6/two-sheet microscopic carrier}
\to (e,\omega,T,R)\text{ Cartan geometry}
\to \text{matter and gauge fluctuation operators}
\to \Gamma_{\rm 1-loop}[e,\omega]
\to \text{induced gravitational action}.
\]
The coframe \(e\) and metric-compatible Lorentz connection \(\omega\) remain independent. The background is Riemann–Cartan: both curvature and torsion are allowed. The teleparallel subfamily \(R(\omega)=0\) is a separate restriction.

The historical PSU toroidal-throat interpretation and the mini-black-hole-scale proposal are retained as model motivation, not established physical facts. The Sakharov calculation must stand on its own spectral and field-theoretic assumptions.

## 2. Three operators that must not be conflated

### 2.1 Q6 graph / arithmetic operator

Q6 has 64 vertices, 192 edges and degree six. Earlier audits reported two distinct operator constructions:
- one Q6 spectral audit: minimum about \(0.02829\), maximum about \(11.97044\), gap about \(1.51364\), with a torsional U(1) link ansatz whose plaquette-holonomy RMS was about \(0.2415\);
- a separate positive-semidefinite operator audit: \(\lambda_{\min}\simeq-9.11\times10^{-15}\) (numerical zero), \(\lambda_{\max}\simeq36.97\), and \(K(0.001)=\operatorname{Tr}(e^{-0.001L})\simeq186.77\).

These are different operators and their spectra must not be merged. The heat trace \(K_L(s)=\operatorname{Tr}(e^{-sL})\) is a finite spectral diagnostic, not yet a physical Sakharov coefficient. A finite graph alone establishes neither a four-dimensional continuum nor a Newton constant.

### 2.2 Geometric 188-dimensional operator \(K_0\)

For the particular 188D RGS/PRISM operator audited previously:
\[
\lambda_{\min}=-2.7768623,\quad \lambda_{\max}=15.575302,
\]
with 29 negative, 3 quasi-zero and 156 positive eigenvalues. The grading had block sizes 64 and 124, but
\[
\|[K_0,P_G]\|_F\simeq35.1466582,\quad
\|[K_0,J_G]\|_F\simeq70.2933164,
\]
and relative cross-block coupling about 0.4822653. The recorded geometric heat supertrace values for \(s=(.001,.01,.05,.1,.5,1)\) were approximately
\[
(-59.789,-57.958,-51.154,-45.006,-32.206,-46.829).
\]
This does not show boson–fermion cancellation and does not establish that \(K_0\) is a physical fluctuation operator. Its negative spectrum also prevents inserting it unmodified as a positive elliptic heat-kernel operator without a justified spectral prescription.

### 2.3 Algebraic SUSY candidate \(H_{\rm SUSY}=Q^2\)

A separate finite-dimensional construction used
\[
Q=\begin{pmatrix}0&B^\dagger\\B&0\end{pmatrix},\quad
\dim=64+124=188,\quad
\Gamma=\operatorname{diag}(I_{64},-I_{124}).
\]
The recorded numerical audit gave \(\operatorname{rank}B=64\), singular values about 0.983568–6.080289, 64 paired nonzero modes, 60 unpaired negative-sector zero modes, and index \(-60\). It verified numerically
\[
Q^\dagger=Q,\quad \{\Gamma,Q\}=0,\quad
H_{\rm SUSY}=Q^2,\quad [H_{\rm SUSY},\Gamma]=0.
\]
Thus
\[
\operatorname{Str}_{\Gamma}(e^{-sH_{\rm SUSY}})=-60,\qquad
\operatorname{Str}_{\Gamma}(H_{\rm SUSY}^{k})=0\quad(k\geq1),
\]
to the precision of the stored audit. This is an algebraic finite-dimensional SUSY-like pairing candidate, not a physical supersymmetric field theory. It is not the spectrum of geometric \(K_0\).

Historical artifacts were recorded under /kaggle/working/RGS_PRISM_188_192_HEAT_AUDIT, including B_supercharge_used.npy, Q_supercharge_188.npy, H_susy_Q_squared_188.npy, Gamma_susy_188.npy, susy_heat_audit.json and sector_moments_audit.json. These are provenance paths, not files verified in this repository at the date of this document.

## 3. Two inequivalent meanings of supertrace

The Sakharov/one-loop field supertrace is
\[
\operatorname{Str}_{\rm fields}(\cdots)
=\sum_{\rm bosons}w_b\operatorname{Tr}(\cdots)
-\sum_{\rm fermions}w_f\operatorname{Tr}(\cdots),
\]
where weights depend on real/complex field normalization, statistics, gauge fixing and ghosts. This definition does not require supersymmetry.

The finite matrix supertrace is
\[
\operatorname{Str}_{\Gamma}(A)=\operatorname{Tr}(\Gamma A),
\]
where \(\Gamma\) grades the 64/124 algebraic candidate. It becomes a physical boson-minus-fermion trace only if a field construction proves that the graded sectors are precisely the physical bosonic and fermionic fluctuation spaces, with correct statistics, multiplicities, gauge constraints and ghosts. The Anti-Twin sheet exchange \(J_{AT}=\tau_x\) is neither grading: it exchanges PSU and Anti-Twin sheets and is not \((-1)^F\).

## 4. Sakharov proper-time effective action

For specified covariant, gauge-fixed fluctuation operators \(\mathcal O_i[e,\omega]\), the one-loop effective action has schematic proper-time form
\[
\Gamma_1[e,\omega]=-\frac12\int_\epsilon^\infty\frac{ds}{s}
\operatorname{Str}_{\rm fields}\left(e^{-s\mathcal O[e,\omega]}\right).
\]
The overall sign and multiplicity factors must be fixed separately for each real/complex boson, fermion, ghost and Euclidean-continuation convention. This is schematic until field content, domains, zero modes, regularization and subtractions are fixed.

In four dimensions,
\[
\operatorname{Tr}(e^{-s\mathcal O})\sim(4\pi s)^{-2}
\int d^4x\sqrt g\,[a_0+s a_2+s^2a_4+\cdots],
\]
with boundary/interface contributions at the throat. After proper-time integration:
- \(a_0\) contributes to the induced cosmological term;
- \(a_2\) contributes to the Einstein–Hilbert / Einstein–Cartan term and induced inverse Newton coupling;
- \(a_4\) and higher terms contribute curvature-squared, torsion-dependent, gauge and anomaly terms.

The target effective action on the two-sheet Riemann–Cartan background is schematically
\[
\Gamma_{\rm eff}[e,\omega]=\int d^4x\,e\left[
-\Lambda_{\rm ind}+\frac{M_{\rm ind}^2}{2}\mathcal R(\omega,e)
+c_T\mathcal I_T(T)+c_1\mathcal R^2+c_2R_{\mu\nu}R^{\mu\nu}+\cdots
\right]+\Gamma_\Sigma.
\]
Here \(\mathcal I_T\) denotes the allowed quadratic torsion invariants, whose contractions and parity properties must be enumerated; \(\Gamma_\Sigma\) contains throat/interface and boundary terms. Coefficients must be calculated from actual field operators and their Seeley–DeWitt coefficients. No numerical \(G_{\rm ind}\) or \(\Lambda_{\rm ind}\) is claimed from the existing finite heat traces.

The calculation is naturally defined after Euclidean continuation, where fluctuation operators can be elliptic, followed by controlled analytic continuation to the Lorentzian wormhole. The continuation, spin structure, zero modes and boundary conditions at both asymptotic ends and at the throat must be stated. A Lorentzian hyperbolic operator cannot simply be treated as a positive elliptic heat operator.

## 5. Matter, spinors and torsion on the wormhole

After the Q6-to-4D manifold-like refinement and Lorentzian spin lift, a local spinor has four complex components. On two sheets \(\Psi=(\Psi_+,\Psi_-)\). The finite carrier may be written schematically as \(\mathbb C^{64}\otimes\mathbb C^4\otimes\mathbb C^2\) only once the site/spin/sheet interpretation is justified.

The fermionic operator must use the same independent Cartan connection:
\[
\mathcal D_\mu=\partial_\mu+\frac14\omega_{\mu ab}\gamma^{ab},
\qquad \slashed D=i\gamma^ae_a{}^\mu\mathcal D_\mu.
\]
Bosonic, fermionic and ghost fluctuation operators must be derived from one gauge-fixed action on the same \((e,\omega)\) background. This turns the abstract field supertrace into a defined object.

For the existing toroidal throat coframe
\[
e^0=N(l)c\,dt,\quad e^1=dl,\quad e^2=r(l)d\theta,\quad
e^3=[R(l)+r(l)\cos\theta]d\varphi,
\]
use \(\omega=\omega_{\rm LC}+K\), with \(K\) independently varied. The Sakharov calculation must retain torsion dependence and calculate whether the induced action generates or renormalizes torsion terms. It must not assume \(K=0\), nor infer torsion merely from sheet exchange.

## 6. PSU–Anti-Twin two-sheet sector

The sheet involution \(J_{AT}=\tau_x\) exchanges \(\Psi_+\oplus\Psi_-\) and the corresponding geometric fields. The effective action may be decomposed into sheet-even and sheet-odd sectors only after the inter-sheet coupling and throat boundary conditions are specified. The two-sheet operator has block form
\[
\mathcal O_{\rm 2sh}=
\begin{pmatrix}\mathcal O_+&\mathcal V_{+-}\\
\mathcal V_{-+}&\mathcal O_-\end{pmatrix},
\]
where \(\mathcal V_{+-}\) must be derived from throat gluing/transport, not inserted as an arbitrary weight. Symmetric and antisymmetric sheet combinations are not automatically boson/fermion pairs. Any cancellation in \(\operatorname{Str}_{\rm fields}\) must follow from physical field content and an actual symmetry of the action.

## 7. Physical SUSY: remaining construction

The 188D \(Q\) supplies an algebraic pairing pattern and nonzero index, but physical SUSY additionally requires:
1. fields with assigned spin/statistics and a local action;
2. transformations of coframe, connection, matter and partner fields;
3. closure (on/off shell, with stated auxiliary fields);
4. invariance of bulk plus throat/interface action;
5. compatible gauge fixing and ghosts;
6. anomaly and boundary/index analysis;
7. a continuum/refinement limit preserving the supercharge and its domain.

Only then may \(\Gamma\) be identified with physical fermion parity and the finite \(-60\) index compared with a continuum index. The current algebraic audit is not proof of SUSY, supergravity or a vanishing Sakharov cosmological term.

## 8. New coupled workstreams

- **WQ6-09 — Q6 spectral-to-continuum bridge:** identify the exact Q6 operator, zero modes, positivity/self-adjoint domain, spectral dimension \(d_s(s)=-2\,d\log K/d\log s\), large-\(s\) limit and convergence under 4D refinement.
- **WQ6-10 — Sakharov heat-kernel coefficients:** define physical multiplets, Euclidean operators, gauge fixing and ghosts; compute \(a_0,a_2,a_4\) on a Riemann–Cartan background with toroidal throat interface; derive \(\Lambda_{\rm ind},G_{\rm ind}\), torsion and higher-curvature coefficients, including regulator dependence.
- **WQ6-11 — two-sheet spectral matching:** construct the PSU/Anti-Twin block operator from derived throat transport; prove self-adjointness/ellipticity and compatible boundary conditions; determine sheet-even/odd spectra without equating sheet parity to statistics.
- **WQ6-12 — physical SUSY realization:** construct or rule out a local supersymmetric action whose finite discretization yields the 188D supercharge; prove closure, action invariance, field statistics, anomaly control and convergence.
- **WQ6-13 — torsionful induced Cartan gravity:** calculate independent torsion invariants and induced coefficients; derive coframe/connection equations; test whether the throat contortion is dynamically supported and preserves regularity/traversability.
- **WQ6-14 — wormhole semiclassical backreaction:** solve \(S_{\rm PC}+\Gamma_1+S_\Sigma\); test regularity, traversability, energy conditions and Schwarzschild–Kruskal decoupling with the same renormalized action.

Dependencies: WQ6-01 (4D Q6 resolution) precedes WQ6-09; WQ6-02 (two-sheet gluing), WQ6-03 (Lorentzian coframe) and WQ6-04 (independent Cartan transport) precede WQ6-10/11/13; WQ6-05 (discrete Palatini–Cartan action) and WQ6-07 (spinorial transport) supply field operators; WQ6-08 (convergence) is required before interpreting finite spectra as continuum gravitational coefficients. These are programme dependencies, not proofs.

## 9. Evidence classification

| Statement | Status |
|---|---|
| Q6 has 64 vertices and 192 edges | Exact combinatorial fact |
| Historical Q6 heat-trace values above | Numerical audit, operator-specific; recover arrays for reproducibility |
| 188D geometric \(K_0\) spectrum and heat supertrace | Numerical audit; not physical field supertrace |
| 188D algebraic \(Q\), grading identities and index \(-60\) | Finite-dimensional algebraic/numerical result; not physical SUSY |
| Proper-time/Seeley–DeWitt mechanism | Established general framework |
| Sakharov coefficients for this PSU–RGS–Anti-Twin wormhole | Open; no \(G_{\rm ind}\) or \(\Lambda_{\rm ind}\) computed |
| Induced torsion dynamics and throat support | Open |
| Physical SUSY and boson–fermion cancellation | Open |
| Q6 continuum limit and convergence of induced coefficients | Open |

## 10. Immediate computations

1. Recover/version the original Q6 and 188D arrays/JSON; rerun each audit from committed scripts with checksums.
2. Select a positive self-adjoint Euclidean Q6 operator and state its Hilbert space, domain and zero-mode sector; compute \(K(s)\), \(d_s(s)\) and refinement scaling.
3. Derive continuum boson, Dirac, gauge and ghost operators from one gauge-fixed matter-plus-Cartan action on the toroidal two-sheet background.
4. Compute torsionful Seeley–DeWitt coefficients including throat interface/boundary terms; compare torsion-free and teleparallel branches.
5. Only then identify induced Newton, cosmological, torsion and higher-curvature couplings and solve semiclassical throat equations.
6. Keep the 188D algebraic SUSY candidate separate until a physical local supersymmetry construction is supplied.

**Conclusion:** Sakharov induced gravity is now a defined branch of the unified programme: Q6 heat trace is its microscopic spectral-input candidate; the independent Cartan wormhole is its background; the field supertrace is its one-loop mechanism; and the 188D SUSY construction remains a separate algebraic candidate.
