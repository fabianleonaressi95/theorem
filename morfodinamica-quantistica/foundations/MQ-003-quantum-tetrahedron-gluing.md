# MQ-003 — Invariant one-link gluing of two quantum tetrahedra

## Setup

Let \(\iota_A\) and \(\iota_B\) be four-valent SU(2)-invariant tensors.
Choose one leg of each tensor, carrying the same representation label
\(j=1/2\), to be glued. The remaining six legs are boundary legs.

For the fundamental representation, the normalized invariant two-leg tensor is
\[
|\epsilon\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}.
\]
Contracting the two selected legs with this invariant tensor defines the
six-leg boundary tensor
\[
\Psi_{a b c d e f}
=\sum_{x,y=0}^1
(\iota_A)_{a b c x}\,\epsilon_{xy}\,
(\iota_B)_{y d e f},
\]
with the ordering/orientation convention fixed by the displayed epsilon
pairing. Equivalent dual-representation conventions may move a transpose or
complex conjugation onto one endpoint; the invariant content is unchanged.

## Theorem — invariant gluing

If \(\iota_A\) and \(\iota_B\) are SU(2)-invariant and the two glued legs
carry dual-equivalent representations, then their contraction with the
invariant pairing is SU(2)-invariant on the six uncontracted legs.

### Proof

For every \(g\in SU(2)\), invariance of each intertwiner means that the
tensor product action on all four of its legs leaves it fixed. The two
actions on the contracted legs cancel against the invariance of the
bilinear pairing \(\epsilon\) (equivalently, the singlet is invariant under
\(g\otimes g\)). The remaining six legs therefore transform trivially as a
collective tensor. Hence \(\Psi\) is an invariant six-valent tensor. \(\square\)

## What is matched?

The common representation label \(j\) gives the same area eigenvalue on
the two sides of the glued link. In the convention used by Li et al.,
\[
\hat A=8\pi\ell_P^2\sqrt{\hat{\mathbf J}\cdot\hat{\mathbf J}},
\qquad
A_j=8\pi\ell_P^2\sqrt{j(j+1)}.
\]
Other LQG conventions may include the Barbero–Immirzi parameter and differ
by the normalization convention for the flux/area operator.

For \(j=1/2\), both sides have the same eigenvalue proportional to
\(\sqrt3/2\). This is **area matching**.

It is not, by itself, **shape matching**. The intertwiner at each node contains
shape information, and two tetrahedra can induce different quantum shapes on
the face even when the shared spin/area agrees. Li et al. explicitly note that
their quantum gluing requires matching the quantum area but does not require
matching the face shape because of quantum fluctuations.

## Normalization in the four-qubit case

For normalized four-valent invariant tensors with one fundamental leg exposed,
SU(2) invariance and irreducibility imply that the reduced density matrix of
that leg is \(I_2/2\). Contracting two such legs with the normalized singlet
therefore gives an unnormalized six-leg tensor of norm \(1/2\). Multiplying
the contraction by 2 yields a normalized boundary state.

This normalization statement assumes both input intertwiners are normalized
and the epsilon tensor has norm one.

## Scope limits

- This is a local spin-network contraction, not a proof of a globally
  shape-matched Regge geometry.
- A collection of such contractions needs consistent edge labels,
  orientations, and node intertwiners.
- Classical shape matching requires additional constraints or a suitable
  coherent-state/large-spin regime.
- The result does not yet identify any RGS cell with a tetrahedral face or
  Q6 edge. That is a separate MQ-005 construction and audit.

## Source

K. Li et al., “Quantum spacetime on a quantum simulator,” *Communications
Physics* 2, 122 (2019), DOI:
[10.1038/s42005-019-0218-5](https://doi.org/10.1038/s42005-019-0218-5).
