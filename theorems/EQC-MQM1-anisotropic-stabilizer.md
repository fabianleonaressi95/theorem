# EQC–MQM-1 anisotropic stabilizer

**Classification:** exact finite result for the 16-element RGS/Q6 gate subgroup acting on the 192 MQM-1 edge references. It is not a calibration of a physical anisotropy.

## 1. Exact invariance condition

MQM-1 uses the reference penalty
\[
E_{\mathrm{ref}}(x)=\frac{\kappa}{2}\|x-x_*\|^2,
\]
where the 192 entries of \(x_*\) are indexed by canonical Q6 edges. For a Q6 automorphism \(g\), let \(\rho_g\) be its induced edge permutation. The fixed-parameter model is invariant exactly when
\[
\rho_g x_*=x_*.
\]
Thus the surviving EQC–RGS gates form
\[
G_{\mathrm{surv}}(x_*)=
G_{\mathrm{RGS-Q6}}\cap\operatorname{Stab}(x_*),
\qquad |G_{\mathrm{RGS-Q6}}|=16.
\]

A gate failing this condition remains a unitary basis permutation; it maps the chosen MQM-1 reference to a different reference configuration.

## 2. Directional anisotropy

Write \(x_{*,e}=c_i\) for an edge in Q6 direction \(i\), in the canonical edge ordering used by the repository. The three local sign-flip gates \(B_3,B_4,B_5\) are Q6 vertex translations. They preserve every direction-coloured edge reference, so their generated subgroup
\[
\langle B_3,B_4,B_5\rangle\cong C_2^3
\]
of order 8 always survives.

The coupled coordinate exchange PAIRSWAP(q1,q2;q4,q5) permutes Q6 directions in pairs (0 1)(3 4), leaving directions 2 and 5 fixed. It survives exactly when
\[
c_0=c_1\quad\text{and}\quad c_3=c_4.
\]
Therefore six pairwise-distinct directional values leave exactly 8 gates; the two pair equalities restore all 16; a uniform reference also preserves all 16.

## 3. Fully edgewise anisotropy

For a general reference vector with 192 independent edge values, the stabilizer is computed from the actual induced edge permutations. If all 192 entries are pairwise distinct, every stabilizing automorphism fixes each edge; because Q6 is connected, its vertex action is the identity. The stabilizer inside the 16-element RGS/Q6 subgroup is therefore trivial.

Intermediate edge-colouring patterns can retain proper subgroups; their classification is an exact finite stabilizer problem, not determined by the word anisotropic alone.

## 4. Reproducibility

The audit constructs the group by closure of the four implemented EQC generators, induces each permutation on the 192 canonical edges, and tests exact equality of the reference vector under each action. No floating-point tolerance is used: equality is equality of the specified reference parameters.

Run:
    python -m unittest discover -s tests -p test_eqc_mqm_anisotropic_stabilizer.py -v

Tests cover six distinct directional coefficients, the pair-equality case, uniform coefficients, a generic edgewise reference, canonical direction expansion, and subgroup closure.

## 5. Evidence boundary

**Exact:** the finite stabilizer characterization and the 8-versus-16 result for the stated directional patterns.

**Not asserted:** that a real MQM-1 material has any one of these reference patterns; a physical anisotropy calibration; a symmetry of a future model with tensor-valued stiffness/mobility not included in the current scalar-parameter action.
