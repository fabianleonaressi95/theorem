# T046-R1 — Determinant consequences after the corrected T045 audit

## 1. Corrected analytic premise

The original T046 adopted a Hadamard finite-part prescription because T045 claimed nonzero simple poles for the two separate degree zeta functions. T045-R1 corrects the binomial-index classification: the only candidate residue is proportional to \(\sum_r(\beta_r-\alpha_r)\), which vanishes exactly in every irreducible 2I sector.

Thus
\[
R_{0,\rho}=R_{1,\rho}=0.
\]
Under the locally uniform Hurwitz continuation established in T045-R1, both separate zeta functions are regular at zero. Their ordinary derivatives are therefore the natural determinant inputs. The finite-part convention remains an optional scale-dependent reparameterization, not a required pole subtraction.

## 2. Optional scale convention

For a regular expansion
\[
\zeta_{k,\rho}(s)=C_{k,\rho}+D_{k,\rho}s+O(s^2),
\]
one may still define
\[
\log\det_\mu\Delta_{k,\rho}
=-\left[D_{k,\rho}+2C_{k,\rho}\log\mu\right].
\]
At \(\mu=1\), this is the ordinary zeta determinant \(-\zeta'_{k,\rho}(0)\). The scale law follows by differentiating \(\mu^{2s}\zeta(s)\); there is no \(\log^2\mu\) term because the residue is zero.

## 3. What the alternating torsion determines

With \(\kappa_\rho(s)=-2\zeta_{0,\rho}(s)+\zeta_{1,\rho}(s)\), T043/T044 give
\[
\kappa_\rho(0)=0,\qquad \kappa'_\rho(0)=2\log T_\rho.
\]
Consequently
\[
C_{1,\rho}-2C_{0,\rho}=0,\qquad
D_{1,\rho}-2D_{0,\rho}=2\log T_\rho.
\]
The same derivative relation holds at every scale because the constant combination also vanishes:
\[
D_{1,\rho}(\mu)-2D_{0,\rho}(\mu)=2\log T_\rho.
\]
This determines only the alternating combination, not the two individual values.

## 4. Status

| Claim | Status |
|---|---|
| Individual residues at zero | Exactly zero by corrected T045 |
| Separate zeta regularity at zero | Analytic conclusion under the locally uniform continuation |
| Ordinary individual zeta determinants | Well-defined if the stated continuation is accepted |
| Individual Laurent constants \(C_0,C_1\) | Not computed |
| Individual derivatives \(D_0,D_1\) | Not computed |
| Alternating derivative relation | Exact from T043/T044 |
| Optional scaled finite-part convention | Defined; no pole subtraction required |

## 5. Reproducibility

\`\`\`bash
python -m pytest tests/test_t045_individual_rumin_zeta_poles.py tests/test_t046_hadamard_finite_part_determinants.py -q
python -m src.t046_hadamard_finite_part_determinants --log-mu 0 --dps 60
\`\`\`

The updated tests are added in this correction branch and still require execution by CI. No individual determinant values are claimed.
