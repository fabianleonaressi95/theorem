# Volterra dipole-to-edge: matched Morandotti C0-IPDG benchmark

**Status:** implementation added; numerical status is determined only by the dedicated CI artifact.  
**Driver:** `scripts/rgs_volterra_morandotti_c0_ipdg.py`  
**Data contract:** `models/volterra_morandotti_benchmark.py`

## 1. Common perforated geometry

At fixed separation (d), core radius (a), mesh size (h), and outer radius (R), both defect configurations use the same perforated disk:

[
Omega_{a,d}=B_R(0)\setminus
\left(\overline B_a(0,d/2)\cup
\overline B_a(0,-d/2)\cup
\overline B_a(0,0)\right).
]

The three cores are ordered upper, lower, centre. The disjointness condition is (d>4a), since the centre-to-outer-core distance is (d/2).

The driver computes the same nine P3 C0-IPDG cell fields and the same (9\times9) interaction matrix for both configurations. This is the key control: only the Frank/Burgers data change.

## 2. Source convention and moment matching

The cell-reconstruction convention already used in the repository is

[
\Phi_i=(s_i,\ s_i x_i+b_{i,y},\ s_i y_i-b_{i,x}).
]

The dipole configuration is

[
(s_+,s_-,s_0)=(+\Omega,-\Omega,0),\qquad b_i=0,
]
at (x_+=(0,d/2)), (x_-=(0,-d/2)), (x_0=(0,0)).

The matched edge configuration is

[
s_i=0,\qquad b_0=(-\Omega d,0),\qquad b_+=b_-=0.
]

Thus both have the same global first-moment vector:

[
\sum_i s_i=0,\qquad
\sum_i(s_i x_i+b_{i,y})=0,\qquad
\sum_i(s_i y_i-b_{i,x})=\Omega d.
]

The sign (b_x=-\Omega d) is fixed by the repository's \,(Phi_i) convention. The test suite checks this identity and separately checks that the local (3N)-vectors are **not** equal at finite (d). This avoids mistaking equality of global moments for exact equality of finite-separation defect configurations.

## 3. What the numerical driver computes

For each requested pair ((d,h)), with (a) fixed, the script:

1. generates the same Gmsh perforated geometry for both source configurations;
2. solves the three P3 cell problems on each of the three cores using the C0-IPDG bilinear form and (alpha=10) by default;
3. assembles the Laplacian-product interaction matrix used by the published reconstruction;
4. reconstructs the Airy potential separately for the disclination dipole and the matched edge dislocation;
5. recovers stress, plane-strain elastic strain, bulk elastic energy, and traction norms on the outer and all three core boundaries;
6. reports direct (L^2) differences of the stress and strain fields, the relative bulk-energy difference, the global moment residual, matrix conditioning, and boundary residuals.

The bulk elastic energy reported here excludes singular-core renormalization and any additional core self-energy terms. It must not be identified with the full asymptotic energy expansion in Cesana–De Luca–Morandotti (2024).

## 4. Run

In the DOLFINx 0.11 / Gmsh / PETSc-MUMPS environment:

```bash
python scripts/rgs_volterra_morandotti_c0_ipdg.py \
  --separations 0.48 \
  --core-radii 0.06 0.04 0.03 \
  --mesh-size-factors 1.0 0.75 \
  --alpha 10 \
  --young-modulus 1.0 --poisson-ratio 0.0 \
  --out artifacts/volterra_morandotti_c0_ipdg/report.json
```

The CI workflow runs the algebraic moment tests and uploads the complete JSON report. It now varies the core radius at fixed separation and refines the mesh relative to the core radius. This separates the fixed-core source comparison from the core-shrinking asymptotic question.

## 5. Relation to the existing periodic Fourier experiment

The periodic Fourier solver in `scripts/rgs_volterra_elastic_limit.py` solves a smooth-core source problem on a periodic square. This new C0-IPDG driver solves the finite-core, perforated-disk boundary-value problem with the cell reconstruction used in the Morandotti framework. The source moment convention is matched, but the boundary geometries and boundary conditions are not the same. Therefore their raw stress and energy values are **not** a direct head-to-head error comparison.

The new driver supplies the missing independent C0-IPDG calculation for a dipole and its matched edge source on a common perforated geometry. A strict Fourier-versus-C0-IPDG comparison still requires a common domain and boundary formulation (for example, a periodic C0-IPDG variant or a bounded-domain Fourier replacement). The report explicitly preserves this limitation.

## 6. Interpretation gates

- **Proved algebraically:** the dipole and edge source data have identical global Frank/Burgers first moments under the declared convention.
- **Numerically testable:** whether the C0-IPDG reconstructed stress, strain, bulk energy, and traction fields approach one another under mesh refinement and controlled (d/a) variation.
- **Not claimed:** exact equality at finite separation; singular-core renormalized-energy equivalence; Mosco or (Gamma)-convergence; superiority over the published method; direct equivalence to the periodic Fourier boundary-value problem.

## References

- Cesana, De Luca, Morandotti (2024), *Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method*, SIAM J. Math. Anal. 56(1), 79–136, DOI 10.1137/22M1523443.
- Cesana, Fabbrini, León Baldelli, Morandotti (2026), *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, arXiv:2609.29614.


## 7. First fixed-core pilot result (CI run 46020780577)

The first run completed successfully and produced artifact `volterra-morandotti-three-core-c0-ipdg-46020780577-1` (artifact ID `15206804672`). It used (a=0.06), (d\in\{0.48,0.56\}), and (h\in\{0.06,0.045\}).

| d | h | cells | relative stress difference | relative bulk-energy difference | interaction-matrix condition |
|---:|---:|---:|---:|---:|---:|
| 0.48 | 0.060 | 2,332 | 0.9913 | 0.6667 | 604 |
| 0.48 | 0.045 | 3,947 | 0.9890 | 0.6723 | 656 |
| 0.56 | 0.060 | 2,344 | 1.0235 | 0.7213 | 343 |
| 0.56 | 0.045 | 3,955 | 1.0456 | 0.7042 | 346 |

Additional diagnostics:

- Global first-moment residual: exactly zero in all four rows (up to floating-point representation).
- Interaction matrix: symmetric to the assembled precision; minimum eigenvalue between 3.90 and 4.31.
- Outer-boundary traction L2 residuals: approximately (6.7\times10^{-6}) to (1.15\times10^{-5}).
- Core-boundary traction residuals are larger, reaching approximately (10^{-3}); they remain a validation blocker and must be studied under further refinement.
- The Hessian-product versus Laplacian-product interaction-matrix discrepancy ranges from about 0.59% to 4.83%.

**Interpretation:** equality of global Frank/Burgers first moments does not make the finite-separation stress fields or bulk energies close in this finite-core pilot. The stress differences are about 99–105%, and the bulk-energy differences about 67–72%. This is not a failure of the moment identity; it shows that matching the global first moment is not enough to replace the full local (3N) defect data at finite separation. The core traction and matrix-form discrepancies also mean this first run is a pilot, not a validated convergence result.

## 8. Core-radius refinement gate

The updated workflow now fixes (d=0.48), varies (a\in\{0.06,0.04,0.03\}), and uses (h/a\in\{1,0.75\}). The next artifact will test whether the stress and bulk-energy discrepancies change as the cores shrink while the defect separation remains fixed. It does not by itself establish the full singular-core energy equivalence: the correct core-energy subtraction/renormalization from the 2024 variational theorem must be implemented before that claim can be tested.
