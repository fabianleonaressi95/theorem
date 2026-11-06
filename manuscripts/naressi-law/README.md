# Critical scientific audit — *Computational Analysis of the Naressi Law*

## Editorial verdict

**Current status: not suitable for submission as a physics paper in its present form.** The document contains one elementary, exactly checkable coupling ansatz and a number of claims that are unsupported, internally inconsistent, or not derived from the stated model. The correct response is not to present the speculative sections as established physics. Preserve the ansatz as a candidate inhomogeneous spin-chain model; remove the claims of ultraviolet regularization, holistic renormalization, Yang–Mills mass-gap generation, universal quasicrystalline localization, and Marx-generator optimization unless independent derivations and evidence are supplied.

This audit concerns the 8-page Library copy dated 28 September 2026. It is not a peer-review decision and does not assert that every possible model based on the ansatz is false.

## 1. What is mathematically correct

The manuscript defines
\[
J_n=\alpha\,\varphi^{-n}\exp(-n/\varphi^2),\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]
For fixed \(\alpha\), this gives
\[
J_n=\alpha q^n,\qquad
q=\varphi^{-1}e^{-1/\varphi^2}
=0.4218194769076527\ldots .
\]
Therefore \(J_{n+1}/J_n=q\) exactly. This is an elementary consequence of the definition. It is a geometrically decaying, position-dependent bond profile. It is not, by itself, a renormalization-group law or a new physical law.

For \(\alpha=\varphi\), the central bond of the stated \(N=64\) open chain is indexed by \(n=31\), and
\[
J_{31}=\varphi q^{31}\simeq 3.87\times10^{-12}.
\]
Thus the interaction crossing the central bipartition is extremely small. The reported central-cut entropy \(S_{64}=0.623\) requires a reproducible calculation and a clear explanation of why it remains this large despite the exponentially weak bond across that cut. This is a concrete internal consistency test, not a proof that the table is necessarily false.

Also,
\[
\sum_{n=0}^{\infty}|J_n|=\frac{|\alpha|}{1-q}<\infty.
\]
The total bond strength is summable and concentrated near the low-index end of the chain. With a fixed uniform field and the stated one-sided profile, the thermodynamic sequence is not a translation-invariant bulk system. The energy density and entropy must be interpreted accordingly; ordinary homogeneous-chain finite-size-scaling language is not justified without further construction.

## 2. The stated spin Hamiltonian is not the transverse-field Ising model

The manuscript uses
\[
H=-\sum_{n=0}^{N-2}J_n
(\sigma_n^x\sigma_{n+1}^x+\sigma_n^z\sigma_{n+1}^z)
-g\sum_{n=0}^{N-1}\sigma_n^x.
\]
This contains two exchange channels, \(XX\) and \(ZZ\), and a field along \(X\). It is not the canonical transverse-field Ising Hamiltonian \(-J\sum ZZ-h\sum X\). It must not be called a modified TFIM without defining the precise transformation and explaining which properties survive that transformation.

Before any numerical claim is retained, specify:
- the value and sign of \(g\), the range and units of \(\alpha\), and whether Pauli matrices or spin operators \(S^a=\sigma^a/2\) are used;
- the exact Hamiltonian for every system size and the bond-index convention;
- the observable and bipartition used for each entropy value;
- the eigensolver, tolerances, residuals, degeneracy handling and raw output;
- for MPS/DMRG, bond dimension, truncation error, sweeps, convergence criteria and boundary conditions.

The paper says MPS/DMRG is used for \(N\ge100\), but its table stops at \(N=64\). No MPS result is actually documented in the reported table.

## 3. The numerical table is not reproducible and needs a decisive cross-check

The table reports only four values at \(\alpha=1.618\):
\[
(N,E_0/N,S_N)=(8,-1.243,0.452),\ (16,-1.412,0.581),\
(32,-1.489,0.612),\ (64,-1.502,0.623).
\]
It does not state \(g\), the precision, the raw data, or the error bars. Four sizes do not establish a thermodynamic limit or a stable critical point. The paper also refers to a peak/inflection near \(\alpha\simeq\varphi\) but does not provide a machine-readable sweep or uncertainty analysis.

The one-sided exponential profile makes the central-cut result especially important: for \(N=64\), the cut bond is approximately \(3.87\times10^{-12}\) at the stated \(\alpha\). Recompute the entropy from the exact stated Hamiltonian and verify the bond indexing. If the reported entropy instead comes from a different profile (for example, a profile centered on the cut or symmetrized about the chain midpoint), the model and the table must be corrected to match.

The energy-density limit also needs a careful interpretation. Since the bond couplings are absolutely summable, their total contribution is not extensive for fixed \(\alpha\), whereas the uniform field term is extensive. In the Pauli convention, the field-only ground-state energy density is \(-|g|\). The reported limiting value cannot be interpreted without the missing value of \(g\) and an explicit comparison with this field-dominated limit.

## 4. Claims that must be removed from a scientific-paper version

| Manuscript claim | Audit | Required editorial action |
|---|---|---|
| The profile is a natural UV cutoff | A site-index decay is not a momentum-space regulator. No map from \(n\) to momentum or wavelength is defined. | Remove. Retain only “spatially inhomogeneous bond profile”. |
| “Holistic renormalization” challenges RG scale separation | The introduction mischaracterizes renormalization-group methods and the decoupling theorem. No RG transformation, beta function, matching condition or cutoff-removal limit is derived. | Remove the paradigm-shift language. |
| The profile prevents UV divergences and singular collapse | No divergent field-theory integral is defined or regularized. Summability of lattice bonds does not prove UV finiteness of a continuum QFT. | Remove. |
| Entropy peak near \(\alpha=\varphi\) is intrinsic | No raw sweep, uncertainty, controls or finite-size extrapolation is supplied. | Report only after reproducible numerical audit. |
| Automatic eigenvalue localization on quasicrystals | No graph family, operator, boundary conditions, spectral measure, inverse participation ratio, Lyapunov exponent or transport calculation is specified. | Remove as a result; retain as a testable future question only. |
| Marx-generator optimization and reduced overstress | No circuit diagram, component model, parasitics, switching law, pulse data or experiment is supplied. | Remove from the physics paper; develop separately as an engineering study. |
| Yang–Mills mass-gap mechanism | No non-Abelian gauge field, gauge-invariant action, continuum limit, Hilbert space, positivity argument or spectral lower-bound proof is constructed. | Remove from the results and conclusions. At most mention as an unrelated long-term motivation, without claiming a mechanism. |
| Golden Action Principle and nonlinear morphodynamic flow | The field \(\mathcal M\), its configuration space, metric/gradient, functional derivative, \(\Gamma\), dimensions and variational principle are not defined consistently. | Remove until a well-posed functional and evolution equation are supplied. |
| Golden coupling tensor \(J_{\mu\nu}\) | The vectors, index \(k\), covariance, symmetry and relation to the lattice couplings are undefined. | Remove. |
| Eigenvalue ratios tend to \(\varphi\) | This is imposed as a boundary/stability condition, not derived from the Hamiltonian. | Remove or label explicitly as an independent conjecture to be tested. |
| Fibonacci normalization of transition probabilities | No transition kernel or probability law is derived. The constraint is an imposed postulate. | Remove. |

## 5. Dimensional and notation problems

The manuscript uses \(\varphi\) both for the golden ratio and for a field in the proposed Lagrangian. These must be given distinct symbols. The expression
\[
\mathcal L_\varphi=\tfrac12\operatorname{Tr}(\partial_\mu\varphi\,\partial^\mu\varphi)-\mathcal H_\varphi
\]
does not define what object is being traced, what its field space is, or how the Hamiltonian operator becomes a local Lagrangian density with matching dimensions. The displayed “morphodynamic flow equation” likewise has undefined gradient and norm operations. These are not cosmetic omissions: without them there is no well-defined variational problem to analyze.

## 6. Minimum viable scientific replacement

A defensible short paper could be titled **“A geometrically decaying inhomogeneous spin-chain coupling profile”** and contain only:

1. the exact definition of \(J_n\) and its elementary ratio/summability properties;
2. the fully specified finite-chain Hamiltonian, with no TFIM label unless justified;
3. exact-diagonalization results that can be regenerated from archived code and raw data;
4. a central-cut entanglement audit, including the tiny cut bond at \(N=64\);
5. comparisons against uniform, generic exponential, pure \(\varphi^{-n}\), mirrored and randomized control profiles;
6. finite-size statements restricted to the sizes actually computed, with numerical uncertainty and convergence diagnostics.

Quasicrystal transport and Marx-generator design should be separate papers with their own models and evidence. Yang–Mills, UV regularization, quantum gravity, mass generation, and universal golden-ratio claims must not appear as established conclusions.

## 7. Epistemic status

- **Proved from the ansatz:** the exact geometric ratio \(q\) and absolute summability of the couplings.
- **Specified but not independently reproduced here:** the finite-chain spin Hamiltonian.
- **Unverified numerical claims:** all tabulated energies, entropies and plots.
- **Open candidate question:** whether the inhomogeneous chain exhibits any robust, nontrivial finite-size phenomenon after controls and the central-cut consistency test.
- **Unsupported in this manuscript:** UV regularization, RG replacement, quasicrystal localization, Marx optimization, Yang–Mills mass gap and quantum morphodynamics.

The source PDF is retained as provenance. This audit does not silently rewrite or erase the original file.
