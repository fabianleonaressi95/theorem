# Morfodinamica Quantistica — quantum geometry modules

This directory records the mathematical bridge from discrete combinatorial structures to quantum-geometric spin networks. Each module distinguishes exact representation-theoretic results, numerical checks, model-dependent constructions, and open physical identifications.

## Current scope

- **MQ-002 — Four-valent spin-1/2 quantum tetrahedron:** exact dimension and explicit basis of the SU(2)-invariant intertwiner space.
- **MQ-003 — One-link gluing of two quantum tetrahedra:** invariant contraction, shared-spin/area matching, and the distinction between area matching and shape matching.
- **MQ-005 — RGS–QLG bridge:** intentionally not asserted here. It requires an identified RGS cellular complex, a dual graph, face labels, orientations, and an explicit map to SU(2) representation data.

## Records

- [MQ-002 mathematical note](foundations/MQ-002-quantum-tetrahedron.md)
- [MQ-003 mathematical note](foundations/MQ-003-quantum-tetrahedron-gluing.md)
- [MQ-T002 — dimension of the four-valent spin-1/2 intertwiner space](../theorems/MQ-T002-four-valent-spin-half-intertwiner-dimension.md)
- [MQ-T003 — invariant one-link gluing](../theorems/MQ-T003-invariant-one-link-gluing.md)
- [Reproducible audit](../scripts/audit_mq002_mq003.py)
- [Regression tests](../tests/test_mq002_mq003.py)
- [Machine-readable results](../results/mq002_mq003.json)

## Evidence policy

The dimension-two statement is an exact SU(2) representation-theoretic theorem. The explicit matrices and contraction checks are finite-dimensional computational audits. A spin-network contraction is not, by itself, a proof of a classical shape-matched Regge geometry, nor does the four-qubit NMR experiment establish a complete theory of quantum gravity.
