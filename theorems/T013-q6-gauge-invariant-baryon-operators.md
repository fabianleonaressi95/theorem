# T013 — Gauge-invariant baryon interpolators on a graph (Q6–SU(3) framework)

**Status:** Gauge-invariance proof is exact for local SU(3)_C transformations. The mapping to Q6 is a proposed construction; spectroscopy and continuum QCD remain open.

## 1. Graph gauge fields and quark fields

Let G=(V,E) be an oriented finite graph (for the Q6 candidate, |V|=64, |E|=192). Assign:
- a color link U_{vw}∈SU(3)_C to each oriented edge v→w, with U_{wv}=U_{vw}^{−1}=U_{vw}†;
- a quark field q_f(v)∈C^3_color⊗C^4_spin for each flavor f∈{u,d,s};
- local gauge transformation g_v∈SU(3)_C.

Transformations:
\[
q_f(v)\mapsto q_f'(v)=g_vq_f(v),\qquad
\bar q_f(v)\mapsto\bar q_f'(v)=\bar q_f(v)g_v^{-1},
\]
\[
U_{vw}\mapsto U'_{vw}=g_vU_{vw}g_w^{-1}.
\]

These are color transformations; flavor labels are untouched by SU(3)_C.

## 2. Local baryon operator: gauge invariance

At one vertex, define a generic three-quark baryon interpolator
\[
B_{f_1f_2f_3}^{\alpha}(v)=
\epsilon_{abc}\,
\mathcal S^{\alpha}_{\rho\sigma\tau}
q_{f_1}^{a\rho}(v)q_{f_2}^{b\sigma}(v)q_{f_3}^{c\tau}(v),
\]
where ε_{abc} is the invariant SU(3) color tensor and \mathcal S is a spin/flavor projector.

Under q(v)→g_vq(v):
\[
\epsilon_{abc}(g_v)^a{}_i(g_v)^b{}_j(g_v)^c{}_k
=(\det g_v)\epsilon_{ijk}=\epsilon_{ijk},
\]
because det(g_v)=1. Therefore
\[
B'(v)=B(v).
\]
This proves local color gauge invariance, independent of the chosen flavor/spin projection. □

## 3. Representative spin/flavor structures

For Euclidean lattice conventions, C is the charge-conjugation matrix. Common nucleon interpolators include
\[
N_p^\alpha(v)=\epsilon_{abc}
\big(u^{aT}(v)C\gamma_5d^b(v)\big)u^{c\alpha}(v),
\]
\[
N_n^\alpha(v)=\epsilon_{abc}
\big(d^{aT}(v)C\gamma_5u^b(v)\big)d^{c\alpha}(v).
\]
These are schematic local interpolators: spin projection, symmetrization, and convention-dependent normalization should be specified in an implementation.

A spin-3/2 decuplet interpolator can be written schematically as
\[
\Delta_{\mu}^{++}(v)=\epsilon_{abc}
\big(u^{aT}(v)C\gamma_\mu u^b(v)\big)u^c(v),
\]
with a spin-3/2 projector applied to remove spin-1/2 contamination. Analogous flavor-symmetrized operators generate Σ*, Ξ*, and Ω. For the octet, mixed-symmetry flavor/spin projectors distinguish N, Λ, Σ, and Ξ.

## 4. Nonlocal baryons on Q6

If quarks are placed at distinct vertices v_1,v_2,v_3, gauge invariance requires parallel transport to a common reference vertex x along chosen paths P_i:
\[
Q_{f_i}(x;v_i)=U(P_i:x\leftarrow v_i)q_{f_i}(v_i).
\]
Then construct
\[
B(x;v_1,v_2,v_3)=\epsilon_{abc}
Q_{f_1}^{a}(x;v_1)Q_{f_2}^{b}(x;v_2)Q_{f_3}^{c}(x;v_3).
\]
Path choices affect the operator and its overlap with states; they are not physically interchangeable without specifying the gauge-field ensemble and operator basis.

## 5. Correlators and spectrum extraction

For baryon operators B_i, define
\[
C_{ij}(t)=\sum_{\mathbf x}
\langle B_i(\mathbf x,t)\bar B_j(\mathbf0,0)\rangle.
\]
On a finite graph, a temporal direction or transfer operator must be supplied. A generalized eigenvalue problem
\[
C(t)v_n(t,t_0)=\lambda_n(t,t_0)C(t_0)v_n(t,t_0)
\]
can then estimate energy levels, subject to a valid action, boundary conditions, statistical ensemble, and sufficient operator basis. Q6 alone does not provide these ingredients.

## 6. What is required before calling this a QCD baryon calculation

- Define a fermionic action (Wilson, staggered, overlap, or a clearly justified graph analogue) and its Dirac operator.
- Define SU(3)_C links and gauge action/measure, not merely a plaquette count.
- Specify spinor representation, graph directions/edge labels, temporal evolution and boundary conditions.
- Include fermion determinant or justify a quenched approximation.
- Construct and numerically validate octet/decuplet correlators; test gauge covariance and antisymmetry.
- Establish finite-size and continuum/scaling behavior before physical mass claims.

**Classification:** color-singlet operator construction and local gauge-invariance proof = exact algebraic result. Q6 realization = proposed discrete model. Baryon masses, confinement, and continuum limit = open.

## References
- M. Gell-Mann, “The Eightfold Way,” 1961 (flavor classification).
- Particle Data Group, *Review of Particle Physics*, Quark Model review: https://pdg.lbl.gov/
- C. Gattringer and C. B. Lang, *Quantum Chromodynamics on the Lattice*, Springer (2010), for lattice gauge links, fermion actions, and hadron correlators.
