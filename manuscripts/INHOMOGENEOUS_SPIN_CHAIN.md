# A geometrically decaying inhomogeneous spin chain

## Status and scope

**Status: mathematical model note; no physical claim is made.** This note extracts the part of the Naressi-law manuscript that is precisely specified and elementary to verify. It does not claim a new renormalization law, a UV regulator, a Yang–Mills mass gap, quasicrystalline localization, or an engineering result.

## 1. Coupling profile

Let \(\varphi=(1+\sqrt5)/2\) and fix a real amplitude \(\alpha\). Define, for integer bond indices \(n\geq0\),
\[
J_n=\alpha\,\varphi^{-n}\exp(-n/\varphi^2)
=\alpha q^n,
\qquad
q=\varphi^{-1}\exp(-\varphi^{-2}).
\]
Since \(0<q<1\),
\[
q=0.4218194769076527\ldots,
\qquad
\frac{J_{n+1}}{J_n}=q
\]
whenever \(J_n\ne0\). The ratio is an identity following from the definition; it is not an independently derived physical law.

The profile is absolutely summable:
\[
\sum_{n=0}^{\infty}|J_n|
=\frac{|\alpha|}{1-q}.
\]
It is a one-sided, spatially inhomogeneous bond profile. It is not translation invariant and does not define a momentum-space cutoff.

## 2. Finite-chain Hamiltonian

For an open chain with \(N\geq2\) sites, define
\[
H_N(\alpha,g)=
-\sum_{n=0}^{N-2}J_n
\left(\sigma_n^x\sigma_{n+1}^x+
      \sigma_n^z\sigma_{n+1}^z\right)
-g\sum_{n=0}^{N-1}\sigma_n^x.
\]
Here \(\sigma_n^a\) are Pauli matrices and \(g\in\mathbb R\). The Hamiltonian has two exchange channels, \(XX\) and \(ZZ\), and an \(X\)-directed field. It is not the canonical transverse-field Ising Hamiltonian.

This definition fixes the bond indexing: bond \(n\) joins sites \(n\) and \(n+1\). Any numerical study must publish \(N,\alpha,g\), boundary conditions, matrix convention, solver, tolerance and raw output.

## 3. Elementary operator bound

For each bond, the commuting operators \(\sigma^x\otimes\sigma^x\) and \(\sigma^z\otimes\sigma^z\) have joint eigenvalues whose sum is in \(\{-2,0,2\}\). Hence
\[
\left\|\sigma_n^x\sigma_{n+1}^x+
\sigma_n^z\sigma_{n+1}^z\right\|=2.
\]
Also \(\|\sigma_n^x\|=1\). The triangle inequality therefore gives
\[
\|H_N(\alpha,g)\|
\leq 2|\alpha|\sum_{n=0}^{N-2}q^n+N|g|
\leq \frac{2|\alpha|}{1-q}+N|g|.
\]
In particular, for fixed \(\alpha\), the total norm contribution of the exchange part is uniformly bounded in \(N\), while the field contribution can be extensive. This is a direct consequence of the one-sided summable profile.

## 4. Central-cut consistency check

For even \(N=64\), the central bipartition separates sites \(0,\ldots,31\) from \(32,\ldots,63\); the crossing bond is \(n=31\). At \(\alpha=\varphi\),
\[
J_{31}=\varphi q^{31}\simeq 3.87\times10^{-12}.
\]
Any reported entanglement entropy across this cut must be recomputed from the stated Hamiltonian and indexing. The very weak crossing bond is a stringent consistency check; it does not by itself prove a particular entropy value impossible, because the field and the state preparation/ground-state calculation must also be specified.

## 5. Numerical evidence required

No numerical energy or entropy value is promoted to a result by this note. To report one, archive:
- the exact parameter values and Hamiltonian convention;
- code and version, raw eigenvalues/state or MPS checkpoint;
- eigensolver residuals and convergence/tolerance data;
- the precise entropy definition and bipartition;
- finite-size data with uncertainty and controls.

At minimum, compare the profile with uniform, generic exponential, pure \(\varphi^{-n}\), reflected, and randomized profiles. A finite-size peak near a chosen parameter is not evidence of universality without such controls and a justified scaling analysis.

## 6. What this note does not establish

The coupling profile does not, on its own, establish renormalization-group flow, UV regularization, quasicrystalline transport/localization, a Yang–Mills mass gap, particle physics, or high-voltage pulse optimization. Those are distinct research questions requiring distinct models and evidence.

## References and provenance

This note is a cleaned mathematical extraction of the coupling ansatz in the internal document *Computational Analysis of the Naressi Law* (Library upload dated 28 September 2026). The original manuscript is retained as historical provenance and its unsupported extensions are assessed in [the critical audit](naressi-law/README.md).
