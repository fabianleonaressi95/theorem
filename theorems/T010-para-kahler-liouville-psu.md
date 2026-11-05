# T010 — Para-Kähler geometry and conditional PSU–Liouville bridge

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

Suppose (M,J,g,ω) is para-Kähler and H∈C∞(M). Let X_H be the Hamiltonian vector field defined by
\[
\iota_{X_H}\omega=-dH,
\]
and let Φ_t be its flow wherever defined. Then
\[
\Phi_t^*\omega=\omega,\qquad
\Phi_t^*(\omega^n/n!)=\omega^n/n!.
\]

### Proof

Since dω=0, Cartan's formula gives
\[
\mathcal L_{X_H}\omega
=d(\iota_{X_H}\omega)+\iota_{X_H}d\omega
=d(-dH)+0=0.
\]
Therefore
\[
\frac{d}{dt}\Phi_t^*\omega
=\Phi_t^*(\mathcal L_{X_H}\omega)=0.
\]
At t=0 the pullback is ω, so Φ_t^*ω=ω. Taking the n-fold exterior product and dividing by n! yields preservation of the Liouville volume. □

## 3. Coordinate form and determinant

In local para-canonical coordinates (q¹,…,qⁿ,p₁,…,pₙ), where
\[
\omega=\sum_{j=1}^n dq^j\wedge dp_j,
\]
the Liouville density is, up to orientation,
\[
d\mu_L=d^nq\,d^np.
\]
A Hamiltonian flow preserves this density; its Jacobian relative to the para-canonical volume has absolute determinant 1.

## 4. Conditional application to PSU–Anti-Twin

The implication
\[
\text{para-Kähler data}\Rightarrow\text{Hamiltonian Liouville conservation}
\]
is rigorous. The following are **not** consequences of merely having a PSU involution J²=I:

- integrability of the ± eigendistributions;
- a neutral metric g satisfying g(JX,JY)=−g(X,Y);
- skew-symmetry and non-degeneracy of ω=g(J·,·);
- closure dω=0;
- existence of a Hamiltonian generating the proposed PSU evolution.

These must be constructed and checked in the actual PSU–Anti-Twin geometry. A finite-dimensional involution on a vector space is not, by itself, a para-Kähler manifold.

## 5. Explicit finite-dimensional diagnostic

For a proposed constant-coordinate model, let J and G be matrices representing the para-complex structure and metric. Check:

1. J²−I=0;
2. JᵀGJ+G=0;
3. Gᵀ=G and det(G)≠0, with signature (n,n);
4. Ω=GJ (or the conventionally corresponding matrix) is skew-symmetric and non-degenerate;
5. for variable coefficients, compute dω explicitly and verify it vanishes;
6. if X_H is specified, verify ι_Xω=−dH.

For constant J,G on a coordinate domain, dω=0 follows from constant coefficients, but this does not establish global integrability or a global PSU realization.

## 6. What this does not establish

T010 does not derive:
- the PSU–Anti-Twin involution from Q6;
- a physical time evolution or a quantum Hamiltonian;
- the Bergman density N(z)^−5 on D5;
- a Lorentzian metric or Einstein/TEGR field equations;
- a quark or QCD sector.

The Liouville measure is the para-symplectic volume. Identifying it with a Bergman measure requires an additional explicit map and Jacobian calculation.

## 7. Relation to the Q6 / quark–QCD program

The Q6 Wilson construction is a separate finite gauge-theory layer. T010 supplies a possible mathematical tool for phase-space geometry only if the required para-Kähler structure is established.

The quark sector must independently specify:
- matter fields in the fundamental representation 3 of SU(3), and their conjugates in \bar{3};
- link variables U_e∈SU(3), gauge transformations at vertices, and covariant hopping/Dirac operator;
- fermionic statistics and a defined fermion action (e.g. lattice Wilson or another explicitly stated discretization);
- color-singlet observables and Wilson-loop coupling to the gauge sector;
- a continuum/scaling argument before making claims about physical QCD.

The existing Q6 counts (64 vertices, 192 edges, 240 plaquettes) and a 241-dimensional vacuum-plus-loop truncation do **not** by themselves encode dynamical quarks, the SU(3) representation content, fermion determinants, confinement, or hadron masses. Those remain distinct open constructions.

## 8. Verdict

**Proved:** para-Kähler hypotheses imply symplectic and Liouville preservation for Hamiltonian flow.  
**Conditional:** PSU–Anti-Twin can inherit this result if its actual geometry satisfies the listed hypotheses.  
**Open:** verify the para-Kähler data from PSU, and construct the SU(3) quark/fermion lattice sector independently of the pure-gauge Q6 model.

## References

- V. Cruceanu, P. Fortuny, P. M. Gadea, “A survey on paracomplex geometry,” * Rocky Mountain J. Math.* 26 (1996), 83–115.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989.
- J. M. Souriau, *Structure of Dynamical Systems: A Symplectic View of Physics*, Birkhäuser, 1997.
