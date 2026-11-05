# RGS Cellular Dynamics Benchmark — research roadmap

## Deliverable 01 status
Version 0.1 provides deterministic graph construction, synchronous binary updates, totalistic and ordered rule encodings, seeded initial conditions, trajectory metrics, JSON output, and basic tests.

## Work packages
1. **Reference reproduction:** reproduce the published evolving-CA setup with the exact active fitness function; separate rule effects from initial-condition effects using common random numbers.
2. **Q6 evolutionary engine:** evolve totalistic (14-bit) and ordered (128-bit) rules on Q6; record every seed, genotype, parent, mutation, and fitness.
3. **Multi-objective evaluation:** report stability, density regulation, symmetry, periodicity, and dynamical activity separately; use Pareto fronts rather than arbitrary scalar weights initially.
4. **Independent validation:** hold out initial-state seeds and rule seeds; report confidence intervals and effect sizes.
5. **PRISM transfer:** test rules trained on Q6 on C64 □ C6 □ C6 □ C6 □ C5; distinguish direct transfer, remapping, and retraining.
6. **Hodge/topological observables:** add cochain-valued states and discrete differential operators only after defining the cell complex, orientation, inner products, and boundary conventions.
7. **Continuum bridge:** formulate varying Hilbert spaces and identification maps; prove Mosco liminf, recovery sequence, and compactness before claiming resolvent or spectral convergence.

## Acceptance criteria
- Exact graph invariants and adjacency checks pass.
- Deterministic replay from recorded seeds and configuration.
- Training and validation seeds are disjoint.
- All objective components are reported independently.
- No claim of computational universality from visual patterns or activity alone.
- No physical claim from the cellular-automaton benchmark.

## Status labels
- **Implemented:** v0.1 graph/CA engine and smoke tests.
- **Numerically smoke-tested:** small runs on Moore, Q6, and PRISM.
- **Not yet established:** evolutionary performance, generalization, Hodge compatibility, continuum convergence, and physical interpretation.
