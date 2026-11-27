# Q6 golden zonotope, IVM and Lorentzian spin synthesis

**Date:** 27 November 2026  
**Status:** exact projection/set identities plus finite numerical audit; IVM/FCC bridge and Lorentzian/spinorial refinement remain open.

## Recovered construction

T129 supplies the golden frame
\[
P_\parallel=A(\phi)/\sqrt{2(2+\phi)},\qquad
P_\perp=A(\phi_*)/\sqrt{2(2+\phi_*)}.
\]
T146 identifies the same 64-state Q6 carrier with the six golden axes and explicitly separates the point cloud from the proposed 64 tetrahedron cells. T147 provides the Euclidean \(\operatorname{Spin}(6)\) lift. T148 supplies the PSU–Anti-Twin right/left sheet lock. T149 supplies an exact negative result for the bare Q6 Clifford graph operator. T150 is a distinct D6/Fibonacci six-state two-sheet orbit and is used only for comparison.

The internal acceptance window is the projection of the centred 6-cube:
\[
W=P_\perp([-\tfrac12,\tfrac12]^6)
=\bigoplus_{i=1}^6[-p_i/2,p_i/2],
\]
where \(p_i\) are the six columns of \(P_\perp\). For the specified golden frame all 20 triples of generators are numerically independent. The resulting 3D zonotope has 32 vertices, 60 edges and 30 rhombic facets: the rhombic triacontahedron.

The 64 centred Q6 states \(c(q)=q-\mathbf1/2\) project to 64 distinct internal points in this window. Complementation \(q\mapsto\mathbf1-q\) gives
\[
X_\perp(\mathbf1-q)=-X_\perp(q).
\]
The 64 points are not all vertices: the window has 32 extreme vertices. Q6's 192 graph edges are not the 60 edges of the triacontahedron.

## Why this does not yet identify the IVM

The IVM/FCC vector equilibrium has its own 12-vector/6-antipodal-axis cubic \(O_h\) symmetry convention, including the previously audited tight-frame normalization \(NN^T=2I_3\). The golden projected-cube window is icosahedral \(I_h\). A metric or equivariant map between the two cannot be inferred from shared six-direction language, 64-state cardinality, or antipodality. It needs explicit coordinates, incidence data, and a declared preservation condition. No such map is claimed in T161.

## Conditional Lorentzian bridge

If the two PSU–Anti-Twin fluid fields can be interpreted as future-directed unit timelike four-velocities \(u_+,u_-\), then with
\[
u_+\cdot u_-=\cosh\chi,\quad
v_0=(u_++u_-)/2,\quad
s_{\rm AT}=(u_+-u_-)/2
\]
one obtains
\[
v_0\cdot s_{\rm AT}=0,\quad
v_0^2=\cosh^2(\chi/2),\quad
s_{\rm AT}^2=-\sinh^2(\chi/2).
\]
For \(\chi>0\), this supplies a conditional unit timelike leg and a unit spacelike relative leg. The fluid variables have not yet been shown to satisfy these relativistic normalization hypotheses.

A spatial triad must be supplied by an independently verified IVM/icosahedral spatial construction and orthonormalized in the complement of the timelike leg. The resulting Lorentzian coframe then supports an independent metric-compatible Cartan connection, with both curvature and torsion allowed. The teleparallel flat-connection branch remains distinct.

The spin lift uses \(\operatorname{Spin}^+(1,3)\simeq SL(2,\mathbb C)\), \(\mathrm{Cl}(1,3)\), and a four-component local Dirac spinor. The six-dimensional Euclidean cut-and-project frame does not by itself produce Lorentzian signature or identify \(\operatorname{Spin}(6)\) with \(\operatorname{Spin}(1,3)\).

## Continuum gate

T149's identity-link Q6 Clifford operator is exactly gapped:
\[
D_{Q6}^2=-\frac32I.
\]
A new refinement-consistent operator is required. The future programme must test locality, low-energy spectrum, Hermiticity/unitary time evolution, spectral flow, species multiplicity and anomaly cancellation. The finite zonotope audit does not establish any of these continuum properties.

## Reproduction

\`\`\`bash
python scripts/audit_q6_golden_zonotope_t161.py
python -m unittest discover -s tests -p "test_q6_golden_zonotope_t161.py" -v
\`\`\`
