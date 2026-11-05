# T011 — Para-Kähler geometry and conditional PSU–Liouville bridge

**Status:** theorem proved under standard para-Kähler hypotheses; verification of these hypotheses for the PSU–Anti-Twin construction is open.  
**Scope:** establishes a valid symplectic/Liouville structure from para-Kähler data. It does not assert that a given PSU matrix or lattice model automatically defines such data.

## 1. Definitions

Let M be a smooth manifold of dimension 2n. A para-complex structure is a smooth endomorphism J:TM→TM such that J²=Id and the ±1 eigendistributions have equal rank n and are integrable (equivalently, the para-complex Nijenhuis tensor vanishes).

Let g be a pseudo-Riemannian metric of neutral signature (n,n), compatible with J:
\[
g(JX,JY)=-g(X,Y).
\]
Define the fundamental 2-form
\[
\omega(X,Y)=g(JX,Y).
\]
Compatibility implies that ω is skew-symmetric. If dω=0, then (M,J,g,ω) is para-Kähler.

## 2. Theorem (para-Kähler implies Liouville volume preservation)

Suppose (M,J,g,ω) is para-Kähler and H∈C∞(M). Let X_H be defined by ι_{X_H}ω=−dH, with flow Φ_t wherever defined. Then
\[
\Phi_t^*\omega=\omega,\qquad \Phi_t^*(\omega^n/n!)=\omega^n/n!.
\]

**Proof.** Cartan's formula and dω=0 give
\[
\mathcal L_{X_H}\omega=d(\iota_{X_H}\omega)+\iota_{X_H}d\omega
=d(-dH)=0.
\]
Hence d/dt Φ_t^*ω=Φ_t^*(L_{X_H}ω)=0. At t=0 the pullback is ω, so Φ_t^*ω=ω. Taking the n-fold exterior product proves preservation of ω^n/n!. □

## 3. Conditional PSU–Anti-Twin application

The implication para-Kähler data ⇒ Hamiltonian Liouville conservation is rigorous. Merely having a PSU involution J²=I does **not** imply:
- integrability of the ± eigendistributions;
- a neutral metric g with g(JX,JY)=−g(X,Y);
- a closed, non-degenerate fundamental form ω;
- Hamiltonian evolution of the proposed PSU dynamics.

These must be constructed and checked for the actual PSU–Anti-Twin model. A finite-dimensional involution alone is not a para-Kähler manifold.

For constant coordinate matrices J,G, check J²=I, JᵀGJ+G=0, G symmetric and non-degenerate of signature (n,n), and Ω=GJ skew/non-degenerate. Constant coefficients imply dω=0 locally; global integrability and a PSU realization remain separate.

## 4. Limits

T011 does not derive the PSU involution from Q6, a physical time evolution, a Bergman density N(z)^−5, Lorentzian Einstein/TEGR equations, or the quark/QCD sector. Liouville volume is not automatically Bergman volume; an explicit map and Jacobian are required.

## 5. Connection to quark/QCD work

The Q6 Wilson construction is a finite pure-gauge layer. T011 could provide phase-space geometry only after its para-Kähler hypotheses are verified.

A dynamical quark sector must independently specify:
- quark fields in the fundamental 3 of SU(3) and conjugate fields in \bar{3};
- link variables U_e∈SU(3), vertex gauge transformations, and a covariant hopping/Dirac operator;
- fermionic statistics and an explicit fermion action (e.g. lattice Wilson fermions or another stated discretization);
- color-singlet observables and coupling to the Wilson gauge action;
- a continuum/scaling argument before claims about physical QCD.

The Q6 counts (64 vertices, 192 edges, 240 plaquettes) and a 241-dimensional vacuum-plus-loop truncation do **not** by themselves provide dynamical quarks, fermion determinants, confinement, or hadron masses. These are separate open constructions.

## Verdict

- **Proved:** para-Kähler hypotheses imply symplectic and Liouville preservation for Hamiltonian flow.
- **Conditional:** PSU–Anti-Twin inherits this only if its geometry satisfies the hypotheses.
- **Open:** derive/check para-Kähler data from PSU; construct the SU(3) fermion lattice sector separately from pure-gauge Q6.

## References

- V. Cruceanu, P. Fortuny, P. M. Gadea, “A survey on paracomplex geometry,” *Rocky Mountain J. Math.* 26 (1996), 83–115.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989.
- J.-M. Souriau, *Structure of Dynamical Systems: A Symplectic View of Physics*, Birkhäuser, 1997.
