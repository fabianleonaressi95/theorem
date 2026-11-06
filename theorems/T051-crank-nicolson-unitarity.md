# T051 — Unitarity of Crank–Nicolson evolution for a fixed Hermitian Hamiltonian

**Status:** proved.  
**Scope:** finite-dimensional, time-independent Hermitian Hamiltonian. A nonlinear or state-dependent feedback problem is not covered.

## 1. Setting

Let \(\mathcal H\) be a finite-dimensional complex Hilbert space, let \(H=H^\dagger\), and let \(\Delta t\in\mathbb R\). Define \(\psi_{n+1}\) from \(\psi_n\) by
\[
\left(I+\frac{i\Delta t}{2}H\right)\psi_{n+1}
=\left(I-\frac{i\Delta t}{2}H\right)\psi_n.
\]
The inverse on the left exists because every eigenvalue of \(I+i\Delta t H/2\) has modulus at least one.

## 2. Theorem

The Crank–Nicolson update is unitary:
\[
\psi_{n+1}=U_{\Delta t}\psi_n,\qquad
U_{\Delta t}=
\left(I+\frac{i\Delta t}{2}H\right)^{-1}
\left(I-\frac{i\Delta t}{2}H\right),
\]
and
\[
U_{\Delta t}^\dagger U_{\Delta t}=I.
\]
Consequently,
\[
\|\psi_{n+1}\|=\|\psi_n\|
\]
at every step, in exact arithmetic.

## 3. Proof

Since \(H=H^\dagger\), the two operators
\[
A=I+\frac{i\Delta t}{2}H,\qquad
B=I-\frac{i\Delta t}{2}H
\]
are adjoints: \(A^\dagger=B\). Both are polynomials in \(H\), so they commute. The update is \(U=A^{-1}B\), and
\[
U^\dagger U
=B^\dagger(A^{-1})^\dagger A^{-1}B
=A\,B^{-1}A^{-1}B=I,
\]
using commutativity and invertibility. Thus \(U\) is unitary and preserves the Hilbert norm. \(\square\)

## 4. What the theorem does not imply

It does not imply conservation of an arbitrary proposed energy functional for a state-dependent Hamiltonian \(H[\psi]\), nor does it establish a coupled field–spinor Noether law. It also does not prove the existence of a breather, a localized periodic solution, particle–hole symmetry, Majorana structure, or a Bogoliubov–de Gennes interpretation.

For a time-dependent but externally prescribed Hermitian \(H_n\), each frozen Crank–Nicolson step is unitary. If \(H_n\) depends self-consistently on the evolving state, norm preservation may still hold for a suitably defined step, but conservation of the coupled energy requires a separate derivation.

**Source:** [consolidated audit of the exploratory Dirac PDF](../manuscripts/FOUR_PDF_CONSOLIDATED_AUDIT.md).
