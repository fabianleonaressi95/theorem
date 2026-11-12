# Notation policy: supergolden constant and special functions

**Canonical convention for THEOREM**

The supergolden (superaurate) constant is
\[
\psi_{\rm SA}=s>0,\qquad s^3-s^2-1=0,
\qquad s=1.465571231876768\ldots.
\]

The Gross–Pitaevskii complex order parameter is always
\[
\Psi_{\rm GP}(\mathbf x,t),
\]
never \(\psi\) or \(\psi_{\rm SA}\).

The digamma and trigamma are written
\[
\digamma(x)=\frac{d}{dx}\log\Gamma(x),\qquad
\digamma_1(x)=\digamma'(x).
\]
This is a project notation choice; standard references often write these as \(\psi(x)\) and \(\psi_1(x)\).

Other overloaded conventional uses must be qualified:
- Chebyshev second function: \(\vartheta(x)\) or \(\psi_C(x)\).
- Dedekind psi/totient: \(\psi_D(n)\).
- Reciprocal-Fibonacci constant: \(\psi_F\).
- Dedekind modular eta: \(\eta_{\rm Ded}(\tau)\).
- Dirichlet eta: \(\eta_D(s)\).
- Dedekind zeta: \(\zeta_K(s)\).

## Mathematical relationship, not symbol identity

The project does **not** treat the supergolden constant, digamma, GP field, or eta functions as the same object. It records proved bridges among selected objects:

1. The Weber class invariant at the quadratic discriminant \(-31\) satisfies \(\rho^3+\rho-1=0\), with \(\rho=\psi_{\rm SA}^{-1}\), and the corresponding Weber–Dedekind eta quotient yields \(f(i\sqrt{31})=\sqrt2\,\psi_{\rm SA}\).
2. The field \(K=\mathbb Q(\sqrt{-31})\) supplies the quadratic Dirichlet character and its class-number value \(L(1,\chi_{-31})=3\pi/\sqrt{31}\).
3. Gamma/digamma identities evaluated at powers and integer partitions generated from \(\psi_{\rm SA}\) are exact analytic relations; the asymptotic increment tends to \(\log\psi_{\rm SA}\).
4. Dirichlet eta, Dedekind eta, Dirichlet L-functions, and Dedekind zeta are connected by their documented product, Mellin, and Euler-product identities.

These bridges establish a common arithmetic–modular network. They do **not** establish an identity between the GP order parameter and the supergolden constant, nor a Q6/PSU derivation of the Weber invariant. Such further maps remain separate proof obligations.

## Cross-references

- [Digamma–supergolden–Q6 dossier](DIGAMMA_SUPERGOLDEN_Q6_PROGRAM_2026-11-10.md)
- [Unified Dedekind–Dirichlet eta / Weber–supergolden construction](UNITARY_DEDEKIND_DIRICHLET_ETA_BARYCENTRIC_RGS_MORANDOTTI_2026-11-10.md)
- [T111 GP zero-vortex refinement](../theorems/T111-gp-zero-vortex-refinement.md)
