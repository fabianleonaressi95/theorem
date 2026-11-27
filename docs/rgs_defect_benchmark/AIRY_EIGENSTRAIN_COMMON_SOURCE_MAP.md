# Airy–eigenstrain common-source map: transfer audit

**Status:** analytical identity implemented; periodic spectral regression tests added. This is a source-consistency bridge, not yet the perforated-domain Q1/P1 comparison.

## Convention and derivation

Use the Airy convention
\[
\sigma_{xx}=\partial_{yy}\phi,\qquad
\sigma_{yy}=\partial_{xx}\phi,\qquad
\sigma_{xy}=-\partial_{xy}\phi,
\]
and engineering incompatibility
\[
\operatorname{inc}\varepsilon
=\partial_{yy}\varepsilon_{xx}
+\partial_{xx}\varepsilon_{yy}
-\partial_{xy}\gamma_{xy}.
\]

For isotropic plane strain, the compliance map is
\[
\varepsilon_{xx}=\frac{1+\nu}{E}
 ((1-\nu)\sigma_{xx}-\nu\sigma_{yy}),\quad
\varepsilon_{yy}=\frac{1+\nu}{E}
 ((1-\nu)\sigma_{yy}-\nu\sigma_{xx}),\quad
\gamma_{xy}=\frac{2(1+\nu)}{E}\sigma_{xy}.
\]
Consequently,
\[
\operatorname{inc}(S\sigma_\phi)
=\frac{1-\nu^2}{E}\Delta^2\phi.
\]

Define the stress-equivalent eigenstrain
\[
\boxed{\varepsilon^*_\phi=-S\sigma_\phi.}
\]
Then
\[
\operatorname{inc}\varepsilon^*_\phi
=-\frac{1-\nu^2}{E}\Delta^2\phi.
\]
If the Airy source convention is
\[
\frac{1-\nu^2}{E}\Delta^2\phi=-\zeta,
\]
the map gives \(\operatorname{inc}\varepsilon^*_\phi=\zeta\), matching the displacement formulation's incompatibility source.

At constitutive level, with zero displacement,
\[
C:(\varepsilon(0)-\varepsilon^*_\phi)=\sigma_\phi.
\]
This identity fixes the sign and normalization of the transfer map.

## Implementation and tests

- `scripts/rgs_airy_eigenstrain_map.py`: periodic spectral Airy stress, plane-strain compliance, eigenstrain map, incompatibility and biharmonic operators.
- `tests/test_rgs_airy_eigenstrain_map.py`: constitutive identity and spectral incompatibility identity on smooth periodic trigonometric fields.
- Test command: `python -m pytest -q tests/test_rgs_airy_eigenstrain_map.py`.

## Interpretation boundary

- **Analytically established:** the plane-strain compliance/incompatibility identity under the stated Airy and engineering-shear conventions.
- **Numerically testable:** spectral implementation identities for smooth periodic fields.
- **Not established:** equivalence of the existing perforated-domain C0-IPDG and Q1/P1 computations; mesh transfer; traction-free boundary compatibility; singular-core behavior; energy convergence; Mosco or Gamma convergence.

Important: \(\varepsilon^*_\phi\) is derived from the Airy stress itself. This is intentionally a *manufactured transfer source*, not an independent Frank/Burgers eigenstrain. Therefore reproducing the Airy stress with it is a consistency/patch test, not independent physical validation.

## Next coupled-mesh step

Evaluate the P3 Airy Hessian on the same perforated Gmsh mesh, project \(\varepsilon^*_\phi\) into a common quadrature representation, and solve Q1/P1 displacement systems on that geometry with identical traction-free outer/core boundaries and rigid-mode gauge. Report stress, energy, core traction and incompatibility residuals separately. Only that run can quantify the cross-method discretization gap.
