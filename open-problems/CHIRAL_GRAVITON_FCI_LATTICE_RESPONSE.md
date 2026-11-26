# Chiral graviton modes in fractional Chern insulators: RGS research audit

**Record:** RGS-CG-001  
**Status:** OPEN / CANDIDATE — no RGS theorem claimed  
**Date:** 2026-11-26

## Source

Min Long, Zeno Bacciconi, Hongyu Lu, Hernan B. Xavier, Zi Yang Meng and Marcello Dalmonte, *Chiral Graviton Modes in Fermionic Fractional Chern Insulators*, arXiv:2601.05196 (2026), *Reports on Progress in Physics*, DOI https://doi.org/10.1088/1361-6633/ae8369.

The paper studies a charge-neutral spin-2 collective excitation in fractional quantum Hall liquids and its continuation to fractional Chern insulators. It constructs a lattice stress-tensor operator for the fermionic Harper–Hofstadter model in the strong nearest-neighbour-interaction / low-flux regime, and a short-range quadrupolar density operator that generalizes to generic Chern bands. It reports a finite but small intrinsic decay rate in the checkerboard FCI regime, with a thermodynamic estimate of order ΓG/ωG ~ 0.07.

This is a literature audit and proposed RGS research interface. It does **not** claim that RGS/Q6/PRISM operators already realize an FCI Hamiltonian, stress tensor, topological band or graviton.

## Source equations

The generalized short-range density quadrupole is

\[
O_{nn}^{\pm}=\sum_{r_i,\delta}
 e^{\pm 2i\arg(\delta)} f_G(\delta)
 n_{r_i}n_{r_i+\delta}.
\]

The phase selects the two chiral spin-2 channels. The radial weight f_G, cutoff, neighbour shells and sublattice sum are part of the operator definition and must be recorded; they are not free fit parameters after inspecting the spectrum.

For the Harper–Hofstadter construction, the zero-momentum stress components are combined as

\[
O_s^\pm=\sum_r\left(T_r^{xx}-T_r^{yy}\pm2iT_r^{xy}\right).
\]

The source derives this operator under explicit restrictions, including strong nearest-neighbour interactions and a low-flux continuum comparison. It must not be transplanted to an unrelated graph without deriving the relevant current, Hamiltonian commutator and discrete stress balance.

The spectral response is

\[
I_O^\sigma(\omega)=\frac{1}{\mathcal N_-}
 \sum_n |\langle n|O^\sigma|0\rangle|^2
 \delta_\eta(\omega-E_n+E_0).
\]

Here 2η is the FWHM of the Lorentzian broadening in the paper's convention. The paper extracts an intrinsic width by fitting multiple η values and extrapolating

\[
\Gamma_{\mathrm{tot}}(\eta)\simeq \Gamma_G+c\eta,
\qquad c\simeq1.
\]

The extrapolated ΓG, not the raw broadened peak width, is compared across sizes. The paper's chirality-resolved integrated-weight diagnostic is

\[
\mathcal C=
\frac{|\mathcal N_--\mathcal N_+|}
{\mathcal N_-+\mathcal N_+}.
\]

Do not silently replace this with a signed chirality convention.

## Source findings versus RGS open questions

Source-level findings:
- The lattice stress-tensor construction is derived in the specified Harper–Hofstadter setting.
- The quadrupolar density operator is connected to the stress response in the continuum/lowest-Landau-level limit.
- Spectral peaks are tracked along an interpolation from low-flux Harper–Hofstadter to checkerboard FCI.
- The graviton peak remains identifiable despite overlap with a two-magnetoroton continuum.
- The reported FCI intrinsic relative decay rate is finite and small compared with the mode energy.

Not established for RGS:
- An isomorphism between Q6/PRISM and an FCI lattice.
- A Q6-derived Chern band, many-body ground state or fractional filling.
- A RGS stress tensor satisfying the relevant Ward identity.
- Equality of independently defined RGS stress and quadrupolar operators.
- A thermodynamic-limit theorem from finite-size numerical data.

## Candidate questions

### CG-1 — Discrete stress/quadrupole correspondence (OPEN)

Given a specified lattice Hamiltonian H, current jᵃ and derived stress operator Tᵃᵇ, determine whether O_s± and an independently defined O_nn± have the same low-energy spectral support in a stated limit.

Required inputs: Hilbert space and particle-number sector; Hamiltonian and boundary conditions; current convention and continuity equation; derivation of Tᵃᵇ from the Heisenberg commutator; radial kernel f_G and neighbour shells; projection/limit under which the comparison is claimed.

A finite-system diagnostic is the normalized ground-state overlap after subtracting expectation values:

\\[
\\mathcal O_{s,nn}=
\\frac{|\\langle 0|\\widetilde O_s^\\dagger\\widetilde O_{nn}|0\\rangle|^2}
{\\langle 0|\\widetilde O_s^\\dagger\\widetilde O_s|0\\rangle
 \\langle 0|\\widetilde O_{nn}^\\dagger\\widetilde O_{nn}|0\\rangle},
\\quad
\\widetilde O=O-\\langle0|O|0\\rangle.
\\]

This is an operator-state overlap diagnostic, not proof of operator equality. Spectral overlap must also be compared on a declared frequency window.

### CG-2 — Chirality-resolved long-lived mode under lattice deformation (CANDIDATE)

For a fully specified interpolation H(λ), λ∈[0,1], test whether a peak selected by O_nn− remains identifiable and whether its extrapolated intrinsic decay remains small relative to its energy.

Protocol:
- evaluate both chiral channels;
- vary system size and geometry;
- control topological ground-state sectors and boundary twists where applicable;
- vary broadening η and fit windows independently;
- fit Γtot(η)=ΓG+cη, reporting c, intercept and uncertainty;
- compare the peak with the two-magnetoroton threshold and local many-body density of states;
- report sensitivity to the operator kernel and truncation.

A finite ΓG>0 is compatible with a long-lived quasiparticle. Do not require ΓG→0.

### CG-3 — RGS/Q6/PRISM transfer (OPEN, conditional)

Only after an explicit many-body Hamiltonian and Chern-band or equivalent topological input have been constructed may these diagnostics be transferred to an RGS-derived lattice. A graph Laplacian spectrum alone is not a fractional Chern insulator and cannot supply the many-body spectral function.

## Numerical validation gates

| Gate | Required output | Failure condition |
|---|---|---|
| CG-V1 | Hermiticity and particle-number conservation of H | residual above tolerance |
| CG-V2 | Current/continuity and stress-commutator identity | unexplained commutator residual |
| CG-V3 | Independent O_s± and O_nn± constructions | operator definitions conflated |
| CG-V4 | Both chirality-resolved spectral functions | one channel omitted |
| CG-V5 | η-sweep and linear extrapolation | unstable intercept |
| CG-V6 | Size, twist and ground-state-sector sensitivity | uncontrolled finite-size claim |
| CG-V7 | Two-magnetoroton threshold and local DOS | peak called isolated despite continuum overlap |
| CG-V8 | Operator-kernel sensitivity | claimed mode depends on unreported tuning |

No numerical values for CG-V1–V8 are recorded here. Published values are reference targets, not independent RGS reproductions.

## Data schema

Each spectrum record must include model/source commit; N and lattice dimensions; flux/filling/interpolation and interaction parameters; boundary conditions/twist/ground-state sector/solver; operator/chirality/kernel/cutoff; η and frequency grid; raw spectrum; ωG, Γtot, fitted c, extrapolated ΓG and uncertainty; continuum threshold and local density-of-states estimate.

## Bibliography

- Long et al., arXiv:2601.05196 (2026): https://arxiv.org/abs/2601.05196
- Long et al., *Reports on Progress in Physics* (2026), DOI: https://doi.org/10.1088/1361-6633/ae8369

**Evidence status:** source result = published claim; CG-1 and CG-3 = OPEN; CG-2 = CANDIDATE; no RGS theorem or numerical reproduction is claimed.
