# Rodin winding: geometry and Biot–Savart audit

## Current result: geometry must be reconciled before field fitting

The 2024 paper by Ramírez-Galindo et al. reports:
- external toroid diameter D = 9.95 cm;
- aperture diameter 2 Rc = 2.9 cm;
- 12 poles used in the simplified model, while the numerical-map discussion
  starts from 36 poles;
- winding angle theta_s = 150 degrees.

The paper gives the geometric relations

    Rc = Rp sin(theta),       l = 2 Rp cos(theta),
    Rp = D/2,                 theta = 90 degrees - theta_s/2.

Substitution of the reported D and theta_s gives Rp = 49.75 mm and theta =
15 degrees, hence Rc = 12.876 mm, whereas the reported aperture radius is
14.5 mm. The discrepancy is about 1.624 mm (11.2% of the reported radius).
Conversely, the reported aperture and outer radius imply a winding angle of
about 146.1 degrees under the same triangle convention.

This is an explicit source-geometry inconsistency to resolve, not a parameter
to tune away. The audit script records it reproducibly:

    python -m scripts.audit_rodin_paper_geometry

## Scope and evidence boundary

The 2024 article explicitly says its mathematical and FEM models simplify the
actual winding and represent the polygonal field source; the authors note
that the actual Rodin-map winding differs and that changing its trace changes
the geometry and field. The article's central-field comparison is:

| Current | Theoretical | FEM | Experimental |
|---:|---:|---:|---:|
| 1.60 A | 3.90 mT | 4.08 mT | 4.13 mT |
| 1.25 A | 3.01 mT | 3.00 mT | 3.05 mT |
| 0.60 A | 1.30 mT | 1.10 mT | 1.16 mT |

The article also describes a 16 x 16 x 8 cm 3-D scan using a triaxial
Melexis MLX90393 sensor with 0.5 cm steps. The raw vector scan data and a
dimensioned 3-D wire centreline are not supplied in the retrieved article
text. A centre-point magnitude table is not sufficient to validate a
pointwise vector-field model.

## Existing torus-knot code

`scripts/audit_rodin_biot_savart.py` is retained only as a parametric
mathematical test fixture. Its 5x12 torus-knot centreline is NOT the
reconstructed geometry in the 2024 paper and must not be fitted to the
reported 3.90 mT value or described as the experimental Rodin coil.

## Required next inputs

1. Resolve the 150-degree / 2.9-cm aperture discrepancy against Fig. 1 and
   the original geometric construction.
2. Obtain the actual wire path, connection topology, number of turns, and
   signed current directions from a dimensioned drawing or authors.
3. Obtain the measured XYZ scan data (or digitizable source data), sensor
   coordinates, and coil coordinate frame.
4. Implement the paper's 12-segment polygon model separately from the
   physical wire model, then compare both to the vector scan.
5. Add a conventional control coil with matched current and comparable
   dimensions before making claims about a special vortex signature.

## Scientific status

- **Verified by source transcription and exact arithmetic:** reported
  dimensions do not satisfy the paper's stated triangle equations to 1%.
- **Implemented:** Biot–Savart integration for an explicitly specified
  ideal filament; paper-parameter consistency audit.
- **Not established:** full physical winding reconstruction, pointwise
  measured-field agreement, superiority over a matched conventional coil,
  modulo-9-specific field structure, or a vortex theorem.

## Reference

A. D. Ramírez-Galindo et al., “Vortex magnetic induction: Mathematical,
geometric and experimental characterization,” *Revista Mexicana de Física*
70 (2024), 030901. DOI: 10.31349/RevMexFis.70.030901.
