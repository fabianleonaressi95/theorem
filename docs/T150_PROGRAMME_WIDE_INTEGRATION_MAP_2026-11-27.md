# Programme-wide integration map — T161 geometric spine

**Date:** 27 November 2026  
**Status:** architecture and repository crosswalk; theorem-by-theorem proof dependencies require record-level review.  
**Primary repository:** `fabianleonaressi95/theorem`  
**Companion repository:** `fabianleonaressi95/rgs-qlg-quaternion-bridge`  
**Geometric anchor:** T161 — Q6–IVM–rhombic triacontahedron–Lorentzian spin lift.

## 1. Governing principle

T161 is not a replacement for the existing theorem corpus and is not a claim that every result is a logical consequence of the rhombic triacontahedron. It is the **geometric spine** around which the programme's distinct mathematical sectors are organized.

The global architecture has three levels:

1. **Programme membership:** every theorem, law, model, audit, experiment and chapter belongs to the RGS–PSU–PRISM–Q6–QLG programme. This is an organizational edge, not a proof dependency.
2. **Geometric interfaces:** records connect to one or more explicit interfaces of the T161 spine: Q6 carrier; 6D golden/cut-and-project frame; 3D zonotope/icosahedral window; IVM/FCC sector; coframe and Lorentzian metric; Cartan connection; Clifford/spin lift; refinement/continuum.
3. **Mathematical dependencies:** only after inspecting both endpoint records may an edge be typed as proves, uses-definition, implements, representation-input, discretizes, candidate-successor, application-of, comparison-only or open-obligation.

No theorem is to be renumbered, deleted, silently rewritten or upgraded in status as part of this integration.

## 2. Geometric spine and interfaces

```text
Q6 = {0,1}^6 (64 labelled states; cubical incidence)
                  |
                  | centred cube, exact finite projection
                  v
       R^6 = E_parallel (3D) + E_perp (3D)
                  |
          golden cut-and-project
                  |
                  v
  W = sum_i [-g_i,g_i] (3D zonotope)
  rhombic triacontahedral window (32 vertices,
  60 edges, 30 rhombic faces under general position)
                  |
          [OPEN: explicit map]
                  v
        IVM / FCC vector equilibrium
        (cubic O_h sector; not I_h)
                  |
     spatial triad + PSU/Anti-Twin time leg
                  |
                  v
       Lorentzian coframe (1,3), metric eta
                  |
        independent Cartan connection
             (omega, e; R and T)
                  |
                  v
       Cl(1,3) / Spin+(1,3) = SL(2,C)
                  |
          refinement and limit
                  v
        continuum Dirac / field equations
```

The golden 6D projection, IVM/FCC, and Lorentzian spacetime are distinct sectors. The IVM-to-icosahedral bridge, physical interpretation of the PSU/Anti-Twin fluid modes as unit four-velocities, derivation of the time leg, ISO(1,3) lattice transport, and continuum spinor limit remain explicit open obligations. The T149 identity-link Q6 Clifford operator remains exactly gapped and cannot be treated as the continuum fermion.

## 3. Typed programme hubs

Each existing theorem record must be assigned one or more topical hubs for navigation. These hub edges are not proofs.

| Hub | Mathematical content | T161 interface |
|---|---|---|
| H-Q6 | 64-state Boolean cube, Walsh/Fourier, graph and cubical chains, antipodes, Hodge | Q6 carrier |
| H-GOLDEN | φ, 6D orthogonal split, cut-and-project, zonotopes, rhombic triacontahedron | 6D to 3D projection |
| H-IVM | FCC/vector equilibrium, tetrahedral/octahedral cells, Fullerene and solid geometry | unresolved IVM/icosahedral map |
| H-CELL | Kathara, Vesica, Sangaku, Jitterbug, rhombic solids, chain maps, FEEC | geometric incidence and discretization |
| H-REP | SU(2), SO(3), 2I, A5, Spin(6), Clifford modules, Rumin and spectral geometry | representation and spin lifts |
| H-SPACETIME | RGS coframes, PSU, Anti-Twin, Minkowski, Einstein–Cartan and teleparallel branches | Lorentzian coframe/Cartan |
| H-ANALYSIS | Dirichlet forms, FEM/FEEC, Mosco, resolvents, spectral and continuum limits | refinement/continuum gate |
| H-DYNAMICS | PRISM/Krist-All, Fibonacci, Green–Kubo, MHD, hysteresis, Q-ball and field models | dynamics on the carrier/coframe |
| H-ARITH | D5, Bergman–Liouville, η functions, zeta, φ/ψ scales | spectral/scale interfaces |
| H-MORPH | C60/C64, Stone–Wales, morphodynamics, multifractal and symbolic dynamics | geometric/material applications |

A theorem may belong to multiple hubs. Its canonical ID, filename, proof status and provenance remain unchanged. The existing 27-chapter monograph remains the canonical narrative; this table is its navigation layer.

## 4. Crosswalk to the 27-chapter monograph

The 27 chapters are not flattened into one linear proof. They are connected as follows:

- **Chapters 1–5 (discrete foundations):** H-Q6, H-CELL, H-GOLDEN. Establish the carrier, incidence, chain maps, Hodge structures and the 6D projection. T161's 64 projected states must not be confused with 64 IVM tetrahedra or with the 32 extreme zonotope vertices.
- **Chapters 6–9 (gauge and discrete Dirac):** H-REP, H-SPACETIME, H-ANALYSIS. Connect link covariance, Wilson operators, Clifford modules and Nielsen–Ninomiya constraints. T149's exact gap is a required negative dependency.
- **Chapters 10–12 (2I, Rumin, quaternionic representations):** H-REP. These are representation/spectral inputs; they do not automatically identify the icosahedral action on the cut-and-project window with the cubic IVM action.
- **Chapters 13–19 (RGS, PSU, PRISM, FEEC, golden/supergolden scales and Mosco):** H-GOLDEN, H-IVM, H-SPACETIME, H-ANALYSIS, H-ARITH, H-DYNAMICS. Connect recovered coordinates, coframes, two-sheet variables, product graphs and refinement, while preserving the distinction between finite identities and continuum theorems.
- **Chapters 20–27 (Einstein–Cartan/teleparallel gravity, fluids, electromagnetism/MHD, QAT and phenomenology):** H-SPACETIME, H-DYNAMICS, H-MORPH. Each physical sector must attach an action, field variables, equations, observables and a derivation of its coupling to the geometric spine. Similarity of a field equation or numerical scale is not a derivation.

The detailed chapter titles and source-by-source crosswalk remain in `research/UNIFIED_PROGRAM_27_CHAPTER_CROSSWALK_2026-11-24.md` and the canonical monograph `monographs/RGS_PSU_PRISM_Q6_QLG_MONOGRAPH_27_CHAPTERS.md`.

## 5. Companion repository: 51-step formal suite

The 51 records S01–S51 in `rgs-qlg-quaternion-bridge/docs/INTEGRATED_MATHEMATICAL_SUITE_FORMALIZATION_2026-11-25.md` are preserved as a second, implementation-oriented layer. Their links to the geometric spine are grouped without changing their formal status:

- **S01–S04:** quaternion algebra, SU(2)→SO(3), 2I and intertwiners → H-REP.
- **S05–S18:** Q6 graph/cells, antipode, RGS seed, metrics, FEM and Mosco → H-Q6/H-CELL/H-ANALYSIS.
- **S19–S40:** qutrit/Kathara/PRISM/A5/D5 and arithmetic thresholds → H-DYNAMICS/H-ARITH/H-CELL.
- **S41–S46:** shear, metric response, two-sheet matter, Gibbs and Green–Kubo → H-DYNAMICS/H-SPACETIME.
- **S47–S51:** S3/2I, self-adjoint two-sheet operators, D6 intertwiners and RGS–PSU–PRISM bridge → H-REP/H-SPACETIME.

This is a topical crosswalk, not a claim that all 51 statements follow from T161. Preserve the 51-step evidence matrix and all implementation/test/result paths.

## 6. Additional theorem families and their interfaces

The following families must not be dropped merely because they are not direct lemmas about the triacontahedron:

- Vesica piscis, two-circle geometry, Sangaku, barycentres and gradients → H-CELL; potential coordinate/face maps to Q6 require their own incidence and metric proofs.
- Jitterbug, cuboctahedron, rhombicuboctahedron, snub cube and rhombic solids → H-IVM/H-CELL; preserve each polyhedral incidence model and its own transition parameters.
- C60/C64, Stone–Wales and fullerene tangent spaces → H-MORPH/H-REP; retain the V4 locality obstruction and do not infer a 64-state equivalence from matching dimensions.
- 2I, Poincaré quotient S3/2I, Rumin complex, analytic torsion and Dedekind/zeta calculations → H-REP/H-ARITH; distinguish scalar, spinorial and contact-complex spectra.
- Q6–D5, Wilson fibres, Bergman–Liouville and Hua measures → H-ARITH; keep the atomic-marginal no-go and all measure-pullback hypotheses.
- PRISM, Krist-All, Fibonacci, supergolden ψ, eta/zeta and multifractal records → H-DYNAMICS/H-ARITH/H-MORPH; retain generator and provenance requirements.
- FEEC, Mosco, Morandotti, IPDG, Sangaku and geometric variational records → H-ANALYSIS/H-CELL; finite compatibility is not a continuum limit.
- Einstein–Cartan, teleparallelism, torsion, rotating magnetic fields, MHD, Jiles–Atherton, Green–Kubo and Q-ball records → H-SPACETIME/H-DYNAMICS; preserve independent connection, action-derived couplings and physical-time calibration.

## 7. Repository inventory and graph migration

The 24 November cross-repository graph snapshot covered 239 theorem Markdown records and 51 formal companion steps/catalogue entries. The live `main` tree inspected on 27 November contains 284 Markdown files under `theorem/theorems/`; the primary README and older graph snapshots report different earlier counts. Therefore:

1. Rebuild the primary theorem register from the live tree; do not rely on README counts.
2. Reconcile the existing graph's 239 theorem nodes against all current theorem paths using full filename-stem keys, not display IDs alone (legacy IDs are reused).
3. Add missing theorem files as nodes with `programme-membership` and reviewed topical-hub edges. Do not invent proof dependencies from filenames.
4. Add T161 and its explicit T129/T146/T147/T148/T149 interfaces, with each edge caveated by the source record.
5. Preserve the companion S01–S51 records and their exact statuses; attach each to topical hubs and to source/test/result artifacts.
6. Maintain reciprocal graph copies and a single schema/version for both repositories.
7. For every direct mathematical edge, record source path, target path, relation type, exact shared object/map/operator, evidence status and open caveat.

The 284 count is the live primary `main` tree snapshot observed on 27 November 2026; it is not a count of distinct theorem numbers. The branch containing T161 is a separate working snapshot.

## 8. Required edge schema

Each edge should have:
- `source`, `target`;
- `relation`: `programme-membership`, `topic-classification`, `uses-definition`, `proves`, `implements`, `representation-input`, `discretizes`, `candidate-successor`, `application-of`, `comparison-only`, or `open-obligation`;
- `shared_object` (explicit map, matrix, group action, complex, metric, action or operator);
- `status` and `evidence`;
- `caveat` and `source_revision`.

An organizational edge must never be rendered as a proof arrow. A test edge must never be rendered as a theorem proof. If a record is independent, connect it to programme membership and state `independent-root` rather than forcing a false derivation.

## 9. Immediate integration work queue

1. Reconcile all current theorem paths against the old 239-node graph; generate a unique filename-stem node for every record.
2. Review T129, T146–T149 and T161 together as the geometric/spinorial spine.
3. Add the companion 51-step suite as a typed cross-repository layer.
4. Map all 27 monograph chapters and the additional families above to the same hubs.
5. Audit each direct edge from the endpoint theorem bodies; split proved, numerical, conditional, candidate and open edges.
6. Generate a human-readable graph and machine-readable registry from the same source of truth.
7. Only then revise theorem cards individually where a precise dependency or interface is missing.

## 10. Scientific conclusion

The programme is connected at the architectural level. The rigorous objective is to turn that architecture into a typed, reproducible graph of explicit maps and operators. T161 supplies a useful geometric spine from the 64-state Q6 carrier through the golden 6D-to-3D projection and rhombic-triacontahedral window toward the IVM/FCC and Lorentzian spin sectors. It does **not** make every theorem a consequence of that geometry. The full integration is complete only when every canonical record is inventoried and each mathematical edge is justified from its source documents.
