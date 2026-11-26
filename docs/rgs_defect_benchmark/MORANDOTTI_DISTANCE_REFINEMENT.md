# Morandotti two-core distance refinement: numerical gate

**Purpose.** Close the gap between the earlier one-mesh separation sweep and a
mesh-refined interaction study for the two-core P3 C0-IPDG reconstruction.

## Fixed protocol

The audit uses the published six-cell-field architecture for two circular
cores: three cell fields per core, followed by the \(6\times6\) interaction
matrix. For each target mesh size \(h\in\{0.08,0.06,0.045\}\), one reference
mesh is generated with core centres \((-0.28,0)\), \((0.28,0)\), core radius
\(a=0.12\), and outer radius \(R=1\). The same mesh object and geometry-DOF
map are reused for separations \(d\in\{0.48,0.56,0.64,0.72\}\), restoring
the reference coordinates before each deformation.

Material and numerical parameters are fixed at \(E=1\), \(\nu=0\), and
C0-IPDG penalty \(\alpha=10\). Defect data remain fixed in laboratory axes.
The four separations satisfy the disjoint-core and support constraints used
by the two-core map.

## Reported observables

For the off-diagonal Burgers block \(M_{01}=M[1:3,4:6]\), the report records
\[
C_d=\frac{\|M_{01}\|_F}{\|M_{00}^{BB}\|_F},
\qquad
A_d=\frac{M_{\parallel\parallel}-M_{\perp\perp}}
{|M_{\parallel\parallel}|+|M_{\perp\perp}|},
\]
where \(M_{00}^{BB}\) is the longitudinal/transverse Burgers block of the
first core. It also records the two diagonal directional couplings, matrix
symmetry, minimum symmetric-part eigenvalue, mesh Jacobian diagnostics,
boundary identity residual and reconstructed interior-facet traction-jump
norms.

For each fixed \(d\), adjacent mesh levels are compared by
\[
\delta_h(d)=
\frac{\|M_{h_{\rm fine}}(d)-M_{h_{\rm coarse}}(d)\|_F}
{\|M_{h_{\rm fine}}(d)\|_F}.
\]
This is a finite-resolution comparison, not an asserted convergence rate.

## Acceptance and interpretation

The workflow fails if a sampled mesh Jacobian is non-positive, the
interaction matrix loses symmetry beyond tolerance, or the data grid is
incomplete. The pure post-processing tests check the matrix extraction,
normalization, and validation logic independently of DOLFINx.

The experiment can establish whether the earlier separation trend is stable
across the three tested mesh sizes. It cannot by itself prove a continuum
interaction law, a universal decay exponent, a singular-core limit, physical
force balance, or experimental material validity. A decay fit is deliberately
not performed in this gate.

Reference: Cesana, Fabbrini, León Baldelli and Morandotti, *Semidiscrete
Modeling of Dislocation-Disclination Systems: Finite Element Formulation*,
arXiv:2609.29614 (2026), especially the six-cell-field and interaction-matrix
reconstruction.
