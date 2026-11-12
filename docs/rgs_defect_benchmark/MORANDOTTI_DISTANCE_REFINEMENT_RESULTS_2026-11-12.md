# Morandotti two-core distance refinement: numerical results (2026-11-12)

## Status

**Classification: numerical verification on a finite mesh family. Not a convergence theorem.**

The GitHub Actions run on commit `c4e53db696fa3b10cdc0042be158edab5e68ad05` completed successfully. The DOLFINx 0.11.0 workflow ran the post-processing tests and all 12 finite-element configurations (three target mesh sizes and four core separations). The uploaded artifact contains the JSON report and twelve NPZ field exports.

Reference model: Cesana, Fabbrini, León Baldelli and Morandotti, *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, arXiv:2609.29614 (2026). This repository experiment is an independent, restricted two-core numerical audit; it is not a reproduction of the paper's general arbitrary-system theory.

## Protocol

- Annular domain: outer radius 1; two core radii 0.12.
- Target core separations: 0.48, 0.56, 0.64, 0.72.
- Target mesh sizes: 0.08, 0.06, 0.045.
- P3 C0-IPDG, penalty parameter 10, E=1, nu=0.
- At each nominal mesh size, one reference mesh connectivity is reused and geometrically deformed for the four separations. This is a fixed-connectivity deformation study, **not** an independent remeshing study.
- The 6x6 Laplacian interaction matrix is checked for symmetry; its symmetric-part minimum eigenvalue, sampled geometry Jacobian, boundary identity residual, and cross-core block diagnostics are recorded.

## FEM run diagnostics

| h | cells | dofs | minimum sampled det(J), across four separations | maximum boundary-identity relative residual |
|---:|---:|---:|---:|---:|
| 0.080 | 1,265 | 5,840 | 1.0881e-3 | 2.684e-7 |
| 0.060 | 2,145 | 9,848 | 7.3106e-4 | 4.196e-8 |
| 0.045 | 3,642 | 16,649 | 4.2546e-4 | 3.236e-8 |

All 12 sampled Jacobian minima are positive. All 12 interaction matrices are symmetric to the reported precision (relative symmetry residual 0). All 12 minimum eigenvalues of the interaction matrix are positive; across the run they range from 5.9418 to 8.2006. These are finite-sample diagnostics, not certificates of positivity at every point or a proof of coercivity in a continuum limit.

## Interaction diagnostics

The normalized cross-core coupling is
`C_d(h) = ||M_{01}(h,d)||_F / ||M_{00}(h,d)||_F`.
The signed directional indicator `A_d(h)` is the longitudinal-minus-transverse diagonal contrast of the cross block, divided by the sum of the absolute diagonal entries. It is a diagnostic in the chosen center-to-center frame, not a constitutive anisotropy law.

| d | h=0.080: C / A | h=0.060: C / A | h=0.045: C / A |
|---:|---:|---:|---:|
| 0.48 | 0.49363 / 0.43593 | 0.25834 / 0.61847 | 0.25083 / -0.11280 |
| 0.56 | 0.11108 / 0.54674 | 0.11376 / 0.54929 | 0.11658 / 0.55277 |
| 0.64 | 0.04871 / 0.52075 | 0.06235 / 0.57151 | 0.07155 / 0.56303 |
| 0.72 | 0.03639 / 0.59949 | 0.03490 / 0.47998 | 0.03738 / 0.62179 |

Relative Frobenius changes of the full 6x6 interaction matrix between successive mesh levels:

| d | 0.080 -> 0.060 | 0.060 -> 0.045 |
|---:|---:|---:|
| 0.48 | 295.86% | 79.00% |
| 0.56 | 3.10% | 1.55% |
| 0.64 | 8.75% | 4.25% |
| 0.72 | 4.11% | 4.38% |

## Interpretation

1. **d=0.56 is the cleanest result in this run.** The full interaction matrix changes by 3.10% and then 1.55%; the normalized coupling changes by about 2.4% at each refinement, while A changes by less than 0.004 in absolute value. This is evidence of numerical stabilization for this particular geometry and protocol, not proof of mesh convergence.
2. **d=0.64 remains mesh-sensitive.** The full-matrix changes decrease from 8.75% to 4.25%, but C increases by 28.0% and then 14.8%. The observable ratios therefore have not stabilized sufficiently.
3. **d=0.72 has modest full-matrix changes, but A is not stable.** Its signed indicator moves from 0.5995 to 0.4800 to 0.6218. The off-diagonal cross-block entries and a frame-invariant block analysis should be inspected before interpreting this as a robust directional anisotropy.
4. **d=0.48 is unresolved and should not be used for a physical conclusion.** The full-matrix changes are 295.9% and 79.0%; A even changes sign between the two finest levels. Positive sampled Jacobians alone do not cure this severe mesh sensitivity. The minimum sampled determinant also falls to 4.25e-4 at h=0.045, indicating a strongly compressed part of the mapped mesh.

## Conclusions permitted by this run

- The numerical implementation and its 12-case execution are operational.
- The computed matrices are symmetric and positive definite at the tested finite resolutions.
- At the reference separation d=0.56, the chosen matrix and directional diagnostics show encouraging stabilization.
- At d=0.48 and d=0.64, the interaction observables remain resolution-sensitive; at d=0.72 the signed directional indicator is not stable.

## Conclusions not permitted

This experiment does **not** establish a continuum limit, a universal distance-decay law, a Frank-Burgers constitutive relation, a material calibration, or a new theorem about defect interactions. It also does not prove that the observed directional contrast is caused solely by anisotropy.

## Next numerical gate

Before promoting any statement beyond finite-mesh verification:

1. perform an independent remeshing study (not only coordinate deformation on fixed connectivity);
2. add at least two finer levels near d=0.48 and inspect element-quality distributions, not only the minimum sampled Jacobian;
3. compare the full cross-block singular values and its symmetric/antisymmetric parts, in addition to the two diagonal entries used by A;
4. report uncertainty or observed rates only after enough levels show a consistent trend.

The correct classification remains **numerical verification / convergence study incomplete**.
