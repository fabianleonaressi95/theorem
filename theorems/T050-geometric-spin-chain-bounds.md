# T050 — Geometric spin-chain profile: summability and operator bound

**Status:** proved.  
**Scope:** an explicitly defined inhomogeneous finite spin chain. No renormalization or physical interpretation is asserted.

## 1. Definitions

Let \(\varphi=(1+\sqrt5)/2\), \(\alpha,g\in\mathbb R\), and
\[
q=\varphi^{-1}e^{-\varphi^{-2}}.
\]
Since \(\varphi>1\), one has \(0<q<1\). For \(n\geq0\), define
\[
J_n=\alpha q^n.
\]
For an open chain of \(N\geq2\) spin-\(\tfrac12\) sites, set
\[
H_N=-\sum_{n=0}^{N-2}J_n
(\sigma_n^x\sigma_{n+1}^x+\sigma_n^z\sigma_{n+1}^z)
-g\sum_{n=0}^{N-1}\sigma_n^x.
\]

## 2. Theorem

The coupling profile is absolutely summable and satisfies
\[
\sum_{n=0}^{\infty}|J_n|=\frac{|\alpha|}{1-q},
\qquad
J_{n+1}=qJ_n.
\]
Moreover,
\[
\boxed{\ \|H_N\|\leq\frac{2|\alpha|}{1-q}+N|g|\ }.
\]
In particular, the exchange contribution has operator norm bounded uniformly in chain length \(N\), for fixed \(\alpha\).

## 3. Proof

The first identity is the geometric-series formula. For each bond, the two Pauli products commute, are self-adjoint, and have joint eigenvalues whose sums are in \(\{-2,0,2\}\). Hence
\[
\|\sigma_n^x\sigma_{n+1}^x+\sigma_n^z\sigma_{n+1}^z\|=2.
\]
Also \(\|\sigma_n^x\|=1\). By the triangle inequality,
\[
\begin{aligned}
\|H_N\|
&\leq 2\sum_{n=0}^{N-2}|J_n|+N|g|\\
&=2|\alpha|\sum_{n=0}^{N-2}q^n+N|g|\\
&\leq\frac{2|\alpha|}{1-q}+N|g|.
\end{aligned}
\]
This proves the result. \(\square\)

## 4. Exact ratio and numerical value

The identity \(J_{n+1}/J_n=q\) holds when \(J_n\neq0\). Numerically,
\[
q=0.4218194769076527\ldots
\]
The ratio is a consequence of the chosen ansatz, not an independently established physical law.

## 5. Non-conclusions

This theorem does not establish a renormalization-group flow, a momentum-space or ultraviolet cutoff, localization, a Yang–Mills mass gap, or any universal scaling law. The Hamiltonian has both \(XX\) and \(ZZ\) exchange channels and an \(X\)-field; it is not the canonical transverse-field Ising Hamiltonian.

**Source:** [cleaned inhomogeneous spin-chain note](../manuscripts/INHOMOGENEOUS_SPIN_CHAIN.md).
