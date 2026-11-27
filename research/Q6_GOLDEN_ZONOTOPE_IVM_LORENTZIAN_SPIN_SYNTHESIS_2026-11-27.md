# Q6 golden zonotope, IVM and Lorentzian spin synthesis

**Date:** 27 November 2026  
**Status:** finite golden projection audit plus conditional mathematical synthesis; IVM/FCC bridge and Lorentzian/spinorial refinement remain open.

## Recovered construction

The repository's earlier 4D–6D–3D synthesis already records the explicit golden frame
[
P_\parallel=A(\phi)/\sqrt{2(2+\phi)},\qquad
P_\perp=A(\phi_*)/\sqrt{2(2+\phi_*)}.
]
The internal acceptance window is the projection of the centred 6-cube, not the older provisional sphere. Writing the columns of (P_\perp) as (p_i), the window is
[
W=P_\perp([-	frac12,	frac12]^6)
=\bigoplus_{i=1}^6[-p_i/2,p_i/2].
]
For this explicit frame, all 20 triples of generators are numerically independent. The corresponding 3D zonotope has 32 vertices, 60 edges and 30 rhombic facets. This is the rhombic triacontahedral acceptance window.

The 64 centred Q6 states (c(q)=q-mathbf1/2) project to 64 distinct internal points in this window. Complementation (qmapstomathbf1-q) gives (X_\perp(mathbf1-q)=-X_\perp(q)). The 64 points are not all vertices: the window has 32 extreme vertices. Q6's 192 graph edges are not the 60 edges of the triacontahedron.

## Why this does not yet identify the IVM

The IVM/FCC vector equilibrium has its own 12-vector/6-antipodal-axis cubic symmetry convention, including the previously audited tight-frame normalization (NN^T=2I_3). The golden projected-cube window is icosahedral. A metric or equivariant map between the two cannot be inferred from shared six-direction language, 64-state cardinality, or antipodality. It needs explicit coordinates, incidence data, and a declared preservation condition. No such map is claimed in T161.

## Conditional Lorentzian bridge

If the two PSU–Anti-Twin fluid fields can be interpreted as future unit timelike four-velocities (u_+,u_-), then their common and relative modes
[
v_0=(u_++u_-)/2,qquad s_{AT}=(u_+-u_-)/2
]
obey (v_0\cdot s_{AT}=0), (v_0^2=\cosh^2(\chi/2)) and (s_{AT}^2=-\sinh^2(\chi/2)), where (u_+\cdot u_-=\cosh\chi). This provides a conditional unit timelike leg and a unit spacelike relative leg for (chi>0). The fluid variables have not yet been shown to satisfy these relativistic normalization hypotheses.

A spatial triad must be supplied by an independently verified IVM/icosahedral spatial construction and orthonormalized in the complement of the timelike leg. The resulting Lorentzian coframe then supports an independent metric-compatible Cartan connection, with both curvature and torsion allowed. The teleparallel flat-connection branch remains distinct.

The spin lift uses (operatorname{Spin}^+(1,3)\simeq SL(2,\mathbb C)), (mathrm{Cl}(1,3)), and a four-component local Dirac spinor. The six-dimensional Euclidean cut-and-project frame does not by itself produce Lorentzian signature or identify (operatorname{Spin}(6)) with (operatorname{Spin}(1,3)).

## Continuum gate

T149's identity-link Q6 Clifford operator is exactly gapped, (D_{Q6}^2=-3I/2). A new refinement-consistent operator is required. The future programme must test locality, low-energy spectrum, Hermiticity/unitary time evolution, spectral flow, species multiplicity and anomaly cancellation. The finite zonotope audit does not establish any of these continuum properties.

## Reproduction

```bash
python scripts/audit_q6_golden_zonotope_t161.py
python -m unittest discover -s tests -p "test_q6_golden_zonotope_t161.py" -v
```
