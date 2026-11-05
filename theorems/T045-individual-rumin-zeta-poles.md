# T045-R1 — Corrected residue audit for the separate Rumin degree zeta functions

## 1. Correction notice

The original T045 classified the singular binomial terms incorrectly. In the displayed expansion
\[
H_\rho(s)=H_{\rm finite}(s)+16^s\sum_{k\ge0}\frac{(2s)_k}{k!}
\sum_{A,B}\left[
\frac{\alpha_r}{2}\{U_A(2s+k-1)U_B(2s+k)+U_A(2s+k)U_B(2s+k-1)\}
+(\beta_r-\alpha_r)U_A(2s+k)U_B(2s+k)
\right],
\]
where \(r=((A+B-2)/2)\bmod60\), the candidate pole at \(s=0\) is at **k=1**, not k=2 or k=3.

The k=1 term that can have a double Hurwitz pole is precisely
\[
(2s)_1(\beta_r-\alpha_r)U_A(1+2s)U_B(1+2s).
\]
The two alpha terms at k=1 contain at most one Hurwitz pole and are killed at the residue level by \((2s)_1=O(s)\). For k>=2, the alpha terms have at most one Hurwitz pole and the beta terms have none; the factor \((2s)_k=O(s)\) removes any candidate residue. At k=0 all Hurwitz arguments are regular at zero.

## 2. Residue of the only candidate term

For every odd residue class modulo 120,
\[
U_A(1+2s)=\frac{1}{240s}+O(1).
\]
Since \((2s)_1=2s\), the residue contributed by a fixed pair \((A,B)\) is
\[
\frac{\beta_r-\alpha_r}{28800}.
\]
For each fixed \(r\pmod {60}\), exactly 60 ordered pairs of odd classes \((A,B)\pmod {120}\) satisfy \(r=((A+B-2)/2)\pmod {60}\). Summing all pairs therefore gives
\[
\operatorname{Res}_{s=0}H_\rho(s)
=\frac{1}{480}\sum_{r=0}^{59}(\beta_r-\alpha_r).
\]
The exact Molien moment identities already encoded in T032/T045 give
\[
\sum_r\alpha_r=\sum_r\beta_r=\frac{\dim\rho}{2}.
\]
Hence
\[
\boxed{\operatorname{Res}_{s=0}H_\rho(s)=0.}
\]

The one-dimensional boundary sums \(B_\rho,C_\rho\) are regular at zero. Thus
\[
\boxed{\operatorname{Res}_{s=0}\zeta_{0,\rho}(s)
=\operatorname{Res}_{s=0}\zeta_{1,\rho}(s)=0.}
\]
Under the locally uniform Hurwitz/binomial continuation stated above, both separate degree zeta functions are regular at \(s=0\). This reverses the original T045 conclusion.

## 3. Sector-by-sector exact check

The source module computes the period-60 Molien tails using exact rational arithmetic. For each of the nine irreducible 2I sectors it checks both moment identities and then checks that their difference, and therefore the candidate residue, is exactly zero. No floating-point residue estimate is used.

## 4. Consequences for T046

The original reason for requiring individual Hadamard finite-part determinants was the alleged nonzero poles. That reason is removed. If the analytic continuation is holomorphic as established by the corrected expansion, the ordinary derivatives \(\zeta'_{0,\rho}(0)\) and \(\zeta'_{1,\rho}(0)\) are defined, and ordinary zeta determinants are the natural objects.

The individual values are still not computed by the alternating torsion: the latter fixes only the combination \(-2\zeta'_{0,\rho}(0)+\zeta'_{1,\rho}(0)\). T046's algebraic finite-part formula remains a possible scheme, but it is no longer necessary to regularize a pole at zero. The individual constants and derivatives remain open until independently evaluated.

## 5. Reproducibility and status

Run:
\`\`\`bash
python -m pytest tests/test_t045_individual_rumin_zeta_poles.py -q
python -m src.t045_individual_rumin_zeta_poles
\`\`\`

| Claim | Status |
|---|---|
| Period-60 affine Molien tails | Exact algebraic consequence |
| \(\sum\alpha=\sum\beta=\dim(\rho)/2\) | Exact identity |
| Correct candidate pole index | k=1 |
| Candidate residue | Exact expression \(\sum(\beta-\alpha)/480\) |
| Candidate residue in all nine sectors | Exactly zero |
| Separate zeta regularity at zero | Analytic conclusion under locally uniform continuation |
| Individual Laurent constants and derivatives | Not computed |
| Individual determinant values | Open |

The tests in this correction branch are added; they must still be run in CI before this correction is certified by repository automation.
