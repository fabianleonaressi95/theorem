# THEOREM — RGS–PSU–PRISM–Q6 Mathematical Research Programme

**THEOREM** is the central research repository for a structured programme in discrete geometry, spectral analysis, gauge theory, spin geometry, quantum-light models, and mathematical physics.

It brings together source literature, manuscript records, reproducible computational audits, theorem statements, model implementations, and explicitly tracked open problems. The repository is intended to make each mathematical claim traceable to its assumptions, derivation, implementation, and verification status.

> **Scientific-status policy.** A symbolic proof, a numerical verification, a model-dependent conclusion, and a research hypothesis are different kinds of evidence. This repository labels them separately and does not treat computational agreement as a substitute for proof or physical validation.

## Research scope

The main research strands include:

- **RGS–PSU–PRISM:** discrete geometric structures, variable-space limits, Dirichlet forms, Hodge operators, and candidate continuum descriptions.
- **Q6 and QLG:** the 64-state six-bit configuration space, its graph and cell structures, discrete Dirac constructions, and the question of how quaternionic or two-component fibres can be related to Lorentzian spinors.
- **Binary icosahedral geometry:** the group (2I), its irreducible representations, the Poincaré quotient (S^3/2I), and Rumin-type spectral and analytic-torsion calculations.
- **Gauge theory and QFT:** Wilson operators, gauge-covariant discrete operators, QCD-related constructions, and continuum-resolvent questions.
- **Einstein–Cartan and teleparallel gravity:** algebraic torsion, spin currents, Weyssenhoff-fluid assumptions, and the distinction between phenomenological closures and field-equation-derived results.
- **Quantum-light and emergent-spacetime foundations:** a critical mathematical review of candidate geometric models, with conjectural physical interpretations kept separate from established results.

These strands are connected only where an explicit mathematical map, shared operator, or derivation is available. Similar terminology or numerical coincidences alone do not establish equivalence.

## Repository map

The tree below summarizes the principal areas. The live repository may contain additional scripts, data, tests, and theorem records.

```text
theorem/
├── .github/workflows/       # Continuous-integration workflows
├── archive/                 # Quarantined source files retained for provenance
├── audits/                  # Reproducible mathematical/computational audits
├── bibliography/             # Source literature and formula audits
├── data/                    # Machine-readable data and audit outputs
├── docs/                    # User and research documentation
├── models/                  # Explicit mathematical and phenomenological models
├── open-problems/           # Validation matrices and unresolved questions
├── projects/                # Research-strand index
├── scripts/                 # Executable research and verification scripts
├── tests/                    # Automated tests
└── theorems/                # Numbered theorem statements and proof records
```

### Main indexes

- **[Ricostruzione dalle fondamenta](monographs/00_FROM_FIRST_PRINCIPLES_LIGHT_CUBE_SPHERE_PHI_PSU_QAT.md)** — luce e unità di Planck, cubo-sfera, derivazione π→φ, icosaedro/quaternioni/2I, PSU–Anti-Twin, Q-ball, QAT e interfaccia Calabi–Yau. È il punto di partenza della ricostruzione; Q6 e PRISM vengono dopo.
- **[Rubino–QAT–quaternionic SU(2) bridge](docs/RUBINO_QAT_QUATERNIONIC_SU2_BRIDGE.md)** — source audit of Rubino's tensorial parallel-transport discussion, quaternionic QAT-current covariance, the coframe/spin-connection reduction, and the exact finite-graph result already proved in T118; the Q6 continuum limit and unified field equations remain open.

- [Morandotti benchmark I — discrete Saint-Venant KKT specification](manuscripts/MORANDOTTI_BENCHMARK_I_DISCRETE_SAINT_VENANT_KKT.md) — finite-dimensional constrained energy, implemented generic KKT solver and energy assembly, D1–D3 defect tests and Airy/CIP-DG comparison gates; CI execution, continuum convergence and physical validation remain open.
- **[Integrated 27-chapter monograph](monographs/RGS_PSU_PRISM_Q6_QLG_MONOGRAPH_27_CHAPTERS.md)** — consolidated reference for Q6, Q6-D5/Wilson, 2I/Rumin, RGS 188D, PRISM/Krist-All, FEEC/Mosco, QLG, Einstein–Cartan/teleparallelism, QAT, XCont and hysteresis. Includes explicit epistemic status and recovery caveats.
- [Canonical synthesis and closure programme](manuscripts/SINTESI_CANONICA_RGS_PSU_PRISM_Q6_QLG.md) — short strategic overview.

- **[Document A1 — Exact scalar spectrum of the Poincaré spherical space](documents/DOCUMENT_A1_EXACT_SPECTRAL_GEOMETRY_S3_2I.md)** — exact (2I)-invariant harmonic multiplicities on (S^3/2I), derived from the binary Molien series and independently checked by the nine-class Reynolds character average through degree 120.
- [A1 exact character/Molien audit](audits/a1_poincare_scalar_spectrum.py) and [regression tests](tests/test_a1_poincare_scalar_spectrum.py).
- [Bibliography and source catalogue](bibliography/README.md)
- [Special functions and Morandotti bibliography](bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md)
