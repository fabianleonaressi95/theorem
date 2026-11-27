# Möbius coefficients, square-free subsequences and Brownian diagnostics

**Records:** RGS-MB-001 / RGS-MB-002 / RGS-MB-003  
**Status:** OPEN / HYPOTHESIS — computational baseline only  
**Date:** 2026-11-26

## Primary source

Giuseppe Mussardo and André Leclair, *Randomness of Möbius coefficients and Brownian motion: Growth of the Mertens function and the Riemann hypothesis*, J. Stat. Mech. (2021) 113106, DOI https://doi.org/10.1088/1742-5468/ac22fb, arXiv:2101.10336.

The article studies global block properties of the Mertens sum and local statistics of Möbius coefficients restricted to square-free integers. It reports a probabilistic argument and 18 statistical tests. The authors explicitly distinguish their probabilistic/experimental case from a rigorous proof of RH.

The companion code is an independently written finite arithmetic baseline. It does not reproduce the full 90-page analysis, paper data volume, complete test suite or probabilistic argument.

## Exact arithmetic definitions

\[
\mu(1)=1,\qquad
\mu(n)=0\text{ if a prime square divides }n,\qquad
\mu(n)=(-1)^{\omega(n)}\text{ otherwise},
\]
where ω(n) is the number of distinct prime factors.

\[
M(N)=\sum_{n\leq N}\mu(n).
\]

Let f₁<f₂<⋯ enumerate square-free positive integers. Since μ(fⱼ)∈{-1,+1}, define bⱼ=μ(fⱼ) and B(m)=Σ(j≤m)bⱼ=M(fₘ). The density of square-free integers is 6/π², so fₘ~(π²/6)m; this is asymptotic, not an exact finite identity.

## Questions to test

### MB-1 — Block-increment scaling (HYPOTHESIS)

For the square-free sign sequence bⱼ, form non-overlapping complete blocks of length ℓ:
\[
X_{r,\ell}=\sum_{j=r\ell+1}^{(r+1)\ell}b_j.
\]
Compute empirical variance V(ℓ) across blocks and test the descriptive relation
\[
V(\ell)\approx A\ell^{2H}.
\]

For independent unbiased signs the benchmark is V(ℓ)∝ℓ, hence H=1/2. An estimated slope near 1/2 on a finite range is not evidence of an asymptotic invariance principle. Report scales, complete-block counts, regression residuals and sensitivity to block alignment.

### MB-2 — Distribution and dependence diagnostics (HYPOTHESIS)

For each block size, center and standardize block sums when variance is nonzero; report skewness and excess kurtosis with conventions; compute lagged correlations; compare empirical distributions against a declared Gaussian benchmark; compare with independent Rademacher signs and random multiplicative models.

Gaussian-looking marginals do not establish independence. Vanishing sample correlations do not establish independence. NIST randomness batteries are diagnostics under specified null models, not mathematical proofs of randomness.

### MB-3 — Mertens growth and iterated-log benchmark (OPEN)

Track M(N) and compare its observed scale with reference functions such as
\[
\sqrt{N\log\log N}.
\]
The classical law of the iterated logarithm concerns almost-sure limsup behavior for specified stochastic processes. It must not be asserted as a pointwise theorem for the deterministic Möbius sequence.

RH is equivalent to the family of bounds M(x)=Oε(x^(1/2+ε)) for every ε>0. Finite data cannot verify this asymptotic statement.

### MB-4 — Dirichlet twists (OPEN)

For a Dirichlet character χ modulo q, define
\[
M_\chi(N)=\sum_{n\leq N}\mu(n)\chi(n),\qquad
\frac{1}{L(s,\chi)}=\sum_{n\geq1}\frac{\mu(n)\chi(n)}{n^s}
\quad(\Re(s)>1).
\]
A future audit may compare statistics across primitive characters, separating principal/non-principal and real/complex characters. Character conventions, conductors, parity and treatment of (n,q)>1 must be explicit. The implication RH ⇒ GRH discussed in the source is a separate analytic argument, not an inference from finite tests.

## Finite arithmetic implementation

The companion script scripts/audit_mobius_brownian.py:
- computes μ(1),…,μ(N) with a linear sieve;
- computes M(N);
- extracts the square-free sign sequence;
- computes non-overlapping block sums, empirical variance, standardized fourth moment and lag-one correlation;
- optionally estimates a descriptive log-log slope across block sizes.

The script uses only the Python standard library. Tests check exact small values and deterministic bookkeeping. It does not test RH/GRH or claim Brownian convergence.

Run:
~~~bash
python scripts/audit_mobius_brownian.py --n-max 100000 --block-sizes 8,16,32,64,128 --json
python -m pytest tests/test_mobius_brownian_audit.py -q
~~~

## Required next validation stages

1. Reproduce the paper's exact square-free indexing and block construction before comparing reported statistics.
2. Recover exact sample ranges, block sizes, filters and null distributions for each reported test.
3. Reproduce the 18-test battery with multiple-testing and p-value aggregation handled transparently.
4. Compare with independent Rademacher and random multiplicative baselines.
5. Check robustness under block shifts and disjoint subsamples.
6. Extend to Dirichlet characters only after the untwisted baseline is validated.
7. Keep analytic proof obligations separate from finite computational evidence.

## Evidence ledger

| Item | Status | Upgrade requirement |
|---|---|---|
| Linear-sieve values μ(n) | FINITE-EXACT | independent implementation / factorization cross-check |
| M(N) for finite N | FINITE-EXACT | exact arithmetic regression |
| Block moments on finite samples | NUMERICAL | larger independent samples and uncertainty analysis |
| H=1/2 asymptotic law for Möbius | OPEN | rigorous theorem under explicit arithmetic hypotheses |
| Functional Brownian limit | OPEN | functional convergence proof, not a finite test battery |
| RH / GRH | OPEN | analytic proof or counterexample |

## Bibliography

- Mussardo & Leclair, arXiv:2101.10336: https://arxiv.org/abs/2101.10336
- Mussardo & Leclair, J. Stat. Mech. (2021) 113106, DOI: https://doi.org/10.1088/1742-5468/ac22fb
- SapereScienza explanatory article (3 Dec 2021): https://www.saperescienza.it/rubriche/fisica-e-tecnologia/le-leggi-del-moto-browniano-e-la-congettura-di-riemann-generalizzata-3-12-2021/

**Evidence status:** finite exact arithmetic is reproducible; asymptotic Brownian, RH and GRH claims remain open.
