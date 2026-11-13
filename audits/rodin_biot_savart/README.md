# Rodin winding: Biot–Savart audit (provisional)

## Purpose

This audit implements a transparent filamentary Biot–Savart calculation for a
parametric toroidal winding with 5 toroidal and 12 poloidal turns. It is a
computational model, **not** a validated reconstruction of the manufactured
coil in Ramírez-Galindo et al. (2024).

## Geometry

For phase alpha, the centreline is

    x(t) = (R + a cos(12t + alpha)) cos(5t)
    y(t) = (R + a cos(12t + alpha)) sin(5t)
    z(t) = a sin(12t + alpha),   0 <= t < 2 pi.

The default radii (R = 35.25 mm, a = 14.5 mm) are provisional values inferred
from an assumed outer diameter of 99.5 mm and minor diameter of 29 mm. They
must be replaced if the primary source or coil drawings establish different
dimensions.

A second path can be added with a phase offset and opposite current. This
phase-offset family gives distinct parallel curves on the torus. It is not
asserted that a particular phase offset reproduces the actual neighbouring
wire in the Rodin winding.

**Parameterization check:** r(t + delta) for a single closed curve is the same
geometric path with a different parameter origin. It is not a second adjacent
conductor. The implementation therefore changes the poloidal phase 12t +
alpha, not the parameter t itself.

## Field

For each filament,

    B(p) = mu0 I/(4 pi) integral_0^(2 pi)
           [r'(t) x (p - r(t))] / |p - r(t)|^3 dt.

The integral is approximated by midpoint samples of the differential line
element. Multiple conductors are superposed with their signed currents.

## Run

    python -m scripts.audit_rodin_biot_savart

Add a second, phase-shifted path with opposite current:

    python -m scripts.audit_rodin_biot_savart --pair-phase-deg 15

Increase quadrature resolution with --segments 100000.

Dependencies: NumPy.

## Tests

    pytest -q tests/test_rodin_biot_savart.py

The tests check finite centreline construction, distinct phase-shifted paths,
linearity in current, current reversal, cancellation for coincident
opposite-current paths, and rejection of singular observation points. They
do not validate the physical winding or prove a vortex.

## Scientific status and limitations

- **Implemented:** numerical Biot–Savart field for explicitly specified
  ideal current filaments.
- **Unit tests added; CI execution pending:** algebraic and numerical
  invariants listed above.
- **Not established:** exact reconstruction of the 2024 coil, measured-field
  agreement, uniqueness relative to a conventional toroid, a special
  modulo-9 magnetic signature, magnetic helicity, or a physical vortex
  theorem.
- The default dimensions are assumptions, not a certified transcription of
  the article's manufacturing geometry.
- A filament model is singular on the wire and omits conductor cross-section,
  insulation, finite wire spacing, contact geometry, and measurement-probe
  averaging.
- The phase-offset second path is a controlled geometric experiment only.
  Actual winding connectivity and current directions must be recovered from
  primary drawings or direct inspection before interpreting it physically.

## Next evidence required

1. Obtain a dimensioned 3-D drawing or complete wire-centreline description.
2. Determine exact neighbouring-wire connectivity, phase offsets, and signed
   current directions.
3. Add a conventional toroidal control matched for current, conductor length,
   cross-section, and measurement volume.
4. Compare the complete vector field, not only its central magnitude, against
   published tri-axial measurements.
5. Only after field validation, evaluate circulation, curl, field-line
   topology, and gauge-invariant relative magnetic helicity under declared
   boundary conditions.

## References

- A. D. Ramírez-Galindo et al., “Vortex magnetic induction: Mathematical,
  geometric and experimental characterization,” Revista Mexicana de Física
  70 (2024), 030901. DOI: 10.31349/RevMexFis.70.030901.
- M. Rodin and G. Volk, “The Rodin Number Map and Rodin Coil,” Proceedings
  of the NPA 7 (2010), 437–443.
