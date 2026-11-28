# C60 DPO immersion and T-BIANCHI: certification and refinement work plan

**Date:** 2026-11-21  
**Branch:** `research/c60-dpo-intervals-bianchi-refinement`  
**Status:** implementation specification; no new numerical certificate is claimed by this commit.

This record separates three tasks that were previously mixed together:

1. rigorous interval certification on the 90 C60 edge strips;
2. rank/orientation control on the 60 vertex caps;
3. a mesh-hierarchy experiment for the continuum Cartan identity
   `D_omega T = R wedge e` and the rotational Bianchi identity
   `D_omega R = 0`.

The numerical values reported in the research notes (including the strip minimum
`|a x b| ~= 8.5e-4`, the cap contribution scaling, and the 23-test volumetric
suite) are treated as **reported results**, not independently reproduced here.
The source implementation and raw JSON artifacts were not present at the
corresponding paths on `main` when this work item was prepared.

## 1. Strip certification: exact target and proof obligation

For each of the 90 strips, let `(sigma,u) in [0,1]^2` and let
`a(sigma,u), b(sigma,u) in R^3` be the two columns of the explicitly derived
`3 x 2` strip differential. Define

```
v(sigma,u) = a(sigma,u) x b(sigma,u).
```

The local immersion condition is exactly `v != 0`, equivalently
`rank [a b] = 2`. A rigorous certificate must cover the **whole closed
parameter square**, or explicitly state which boundary pieces are excluded
and prove that they have zero two-dimensional measure for the a.e. claim.

### 1.1 Valid interval criterion

For an interval box `B = I_sigma x I_u`, compute outward-rounded interval
enclosures `V_k(B)` of each component of `v`. The box is certified if at
least one component interval excludes zero:

```
0 notin V_x(B)  OR  0 notin V_y(B)  OR  0 notin V_z(B).
```

This is a sufficient, rigorous criterion. An alternative is a rigorously
outward-rounded lower bound for `v dot v` that is strictly positive.

A box whose enclosure contains zero is **unresolved**, not degenerate. It must
be bisected or handled by a separate analytic argument. The sum of areas of
unresolved boxes is a useful diagnostic, but tending to zero does not prove
that the zero set is empty; nor does it by itself prove nonvanishing a.e.
unless a separate measure-theoretic argument is supplied.

### 1.2 Arithmetic requirements

The illustrative `mpmath.iv` sketch in the research note is not accepted as
a proof certificate without repair:

- converting interval endpoints to ordinary `mp.mpf` values and then doing
  arithmetic does not preserve outward-rounded interval guarantees;
- adding an arbitrary `1e-25` epsilon is not a substitute for a documented
  directed-rounding guarantee;
- converting lower bounds to binary `float` before the final positivity test
  can erase a small positive margin.

The implementation must keep interval values in the interval type through the
entire calculation, record precision/backend and rounding mode, and serialize
bounds losslessly (decimal strings or exact rationals). If coefficients are
derived from radicals or trigonometric data, their enclosures must themselves
be rigorous. Prefer exact algebraic coefficients where available.

### 1.3 Adaptive algorithm and output contract

For each strip:

1. initialize a partition of `[0,1]^2`;
2. evaluate interval enclosures for `a`, `b`, and `a x b`;
3. certify a box when one component excludes zero (or a rigorous norm-square
   lower bound is positive);
4. otherwise bisect the longer parameter direction, prioritizing the known
   critical neighbourhood `sigma in [0.25,0.31]`, `u in [0,0.02]` on strip 5;
5. stop only with every box certified, or report the remaining boxes as
   unresolved. Never relabel unresolved boxes as certified.

Required JSON fields per strip:

- parameterization/version and coefficient source hash;
- number of boxes visited, certified leaves, unresolved leaves, and maximum depth;
- certified lower bound for `|a x b|` (or per-component exclusion witness);
- union area of unresolved boxes;
- explicit list of unresolved boxes and their interval bounds;
- precision, interval backend/version, and rounding mode.

A global all-strip certificate requires zero unresolved boxes. A result with
unresolved boxes is a partial certificate and must say so.

## 2. Vertex caps: rank, orientation, and gluing

For each of the 60 vertices, the cap map is
`C_v = sum_{i=1}^3 w_i g_{f_i}`, with the three incident face maps and the
partition-of-unity weights. Its differential is

```
dC_v = sum_i w_i dg_{f_i} + sum_i (g_{f_i} - C_v) tensor dw_i.
```

The second term is essential: checking only the weighted face differentials
does not certify the cap rank.

### 2.1 Required checks

For each cap, in a fixed oriented chart:

- derive both columns of `dC_v` analytically from the actual weight formula;
- certify `partial_1 C_v x partial_2 C_v != 0` a.e. (or everywhere if that
  stronger statement is intended) using the same interval-box criterion as
  Section 1;
- record the sign of the oriented area vector relative to the chosen cap
  orientation and check agreement with all three strip interfaces;
- treat the centre separately if the weights are angular or otherwise
  non-smooth there; prove integrability and the a.e. rank statement rather
  than relying on a polar-grid sample;
- on the cap boundary, verify value matching and the required tangential
  derivative matching with each incident strip.

A positive sampled minimum singular value is numerical evidence only. A
certified lower bound on the cross-product norm, together with a consistent
orientation sign, is the desired proof-level output.

### 2.2 Scaling check

For cap radius `R`, compute `integral_{cap_v} |dC_v|` with a quadrature rule
whose error is controlled independently of the mesh used for the rank test.
Report all 60 caps and a regression against `R`. The expected `O(R)`
scaling is a claim to test; it must not be hard-coded into the output.

### 2.3 Missing inputs blocking executable certification

The repository task must include the exact definitions of `w_i`, cap chart,
cap radius convention, incident face ordering, and strip-to-cap gluing maps.
Without those definitions, a script can only be a generic checker and cannot
certify the actual C60 candidate.

## 3. T-BIANCHI: hierarchy and continuum-consistency experiment

The existing volumetric tests (as reported) exercise a tetrahedral complex and
a boundary-holonomy identity. Those tests are valuable algebraic regression
tests, but they do not yet establish convergence to a continuum Cartan
identity.

Keep the two identities distinct:

```
D_omega R = 0                 (rotational Bianchi identity)
D_omega T = R wedge e         (Cartan torsion identity)
```

The first concerns curvature and the connection. The second also requires a
coframe `e`, torsion `T = D_omega e`, a consistent covariant wedge product,
and compatible primal/dual discretizations. A product of based face
holonomies around a tetrahedron is not, by itself, a discretization of the
second identity.

### 3.1 Mesh family

Construct a nested family `K_l` of tetrahedral meshes of a fixed 3D domain,
with `h_l = h_0 2^{-l}`. Record for each level:

- vertex/edge/face/tetrahedron counts and boundary counts;
- orientation consistency and `partial^2 = 0` checks;
- shape-regularity metrics (minimum dihedral angle and diameter/inradius ratio);
- the exact refinement map and parent-child cell correspondence.

A cube split into six tetrahedra is a valid initial mesh, but the refinement
rule must be specified so adjacent cubes induce matching face triangulations.
The 12-vertex/20-face icosahedral surface with a centre and 20 tetrahedra is a
single volumetric filling, not by itself a refinement hierarchy.

### 3.2 Discrete fields and operators

For every level define, with units and orientations fixed:

- edge coframe data `e_l` as integrated coframe 1-cochains (not an
  undocumented normalized edge displacement);
- edge transports `G_vw in SE(3)`, with inverse-edge consistency;
- face curvature `R_l` from based rotational holonomy and a stated
  logarithm/branch convention where a Lie-algebra value is needed;
- torsion `T_l = D_{omega,l} e_l` using a declared covariant coboundary;
- the discrete covariant wedge `wedge_{omega,l}`, including the cell
  interpolation/projection and all basepoint transports.

The definitions of `D_{omega,l}` and `wedge_{omega,l}` must be independent
of the desired identity. Do not define one side of the residual by subtracting
the other side.

### 3.3 Manufactured solutions

Use at least two smooth continuum data sets:

**Flat case.** Choose a smooth coframe and a flat connection for which
`R = 0`; the continuum residual in both identities is known exactly.

**Curved case.** Choose a smooth connection/coframe with nonzero curvature and
compute the continuum `R`, `T`, and `D_omega T - R wedge e` analytically
or with a separately validated symbolic derivation. A curved case is needed
to test the nonzero source term and avoid a test that passes only because both
sides vanish.

For each level, compare the discrete residual against the cell projection of
the continuum residual:

```
E_l = norm( Res_l - P_l(Res_cont) )
p_l = log2(E_(l-1) / E_l)
```

Report norms, observed orders, and the projection/quadrature error separately.
Do not announce first- or second-order convergence until the sequence exhibits
it over a refinement range and the expected order is justified by the chosen
discretization.

### 3.4 Gauge and basepoint covariance

Repeat each level under vertexwise gauge changes and alternate admissible
basepoint trees. Compare gauge-related residuals after transporting them to
the same cell frames. Raw matrix entries in different frames are not expected
to agree. The norm used for the error must be invariant under the chosen
representation (or its frame dependence must be explicitly normalized).

### 3.5 Interpretation boundary

The tetrahedral boundary-holonomy identity is an exact discrete algebraic
consistency check for edge-derived transports, subject to the implementation's
orientation and basepoint conventions. It is not evidence by itself for
continuum convergence, the Cartan torsion identity, or a physical dislocation
law. The C60 surface remains a boundary fixture; it cannot replace a 3D
refinement study.

## 4. Acceptance gates and repository status

| Work item | Acceptance condition | Status in this record |
|---|---|---|
| 90-strip interval proof | every parameter box certified, rigorous outward rounding, reproducible JSON | Open; exact strip coefficients/source not yet in this branch |
| 60-cap immersion | analytic cap differential, rank/orientation certificate, gluing checks | Open; cap weights/charts not yet in this branch |
| Hierarchical T-BIANCHI | nested shape-regular meshes, independent `D_omega`/`wedge_omega`, manufactured solutions, observed convergence | Specification; implementation and runs open |
| Existing volumetric regression | original source and 23-test run independently replayed | Reported by project owner; not replayed in this commit |

## 5. Required next artifacts

- `scripts/certify_c60_dpo_intervals.py`: interval backend, actual strip
  coefficient evaluator, adaptive subdivision, machine-readable certificate.
- `scripts/certify_c60_dpo_caps.py`: exact cap differential, interval rank and
  orientation checks, gluing checks, cap-scaling audit.
- `output/dec_se3/src/dec_se3/refinement.py` and a separate convergence
  driver: mesh hierarchy, field sampling/integration, covariant operators,
  manufactured solutions, and gauge/basepoint regression.
  *(2026-11-27 note: the legacy `dec_se3` package was archived to
  `archive/dec_se3_legacy/` during the repository reorganisation; the planned
  `output/dec_se3` path no longer exists. This item remains an open
  requirement — see `docs/POST_REORG_CONSISTENCY_AUDIT.md` §4.)*
- Raw JSON outputs and tests tied to exact source hashes.

These scripts must be added only together with the actual mathematical input
data and tests. A generic interval routine or a one-mesh identity test must
not be presented as completion of the corresponding theorem.
