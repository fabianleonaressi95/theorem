# Manuscripts and research notes

This directory contains cleaned mathematical notes, critical audits, and records of external manuscripts. It is **not** a list of peer-reviewed publications. A document is not promoted to a scientific result merely because it uses physical terminology, displays equations, or reports numerical output.

## Active, cleaned research notes

These are the parts that can be stated precisely without importing unsupported physical conclusions:

| Document | Scope | Status |
|---|---|---|
| [A geometrically decaying inhomogeneous spin chain](INHOMOGENEOUS_SPIN_CHAIN.md) | Exact coupling profile, finite-chain Hamiltonian, summability and elementary operator bound | Mathematical model definition; numerical claims not certified |
| [Scalar–torsion variational identity](SCALAR_TORSION_VARIATIONAL_IDENTITY.md) | Scalar variation of one explicitly displayed scalar–torsion action | Conditional derivation; not a complete tetrad/spin-connection solution |

These notes are deliberately narrower than the source documents. They preserve useful equations and remove conclusions that do not follow from them.

- [Technical audit of T047–T049D](T047_T049D_TECHNICAL_AUDIT.md) — EC spin scaling, varying-space calibration, microscopic correlators, and the corrected Lorentz boost convention.
- [Mosco convergence for curved cubical refinements](MOSCO_CURVED_CUBICAL_REFINEMENT_OPEN_PROBLEM.md) — standalone open-problem dossier, five-factor PRISM refinement baseline, non-affine cell-map hypotheses, Mosco proof obligations, compactness and review questions.
- [XCont emergent-dynamics integration](XCONT_EMERGENT_DYNAMICS_INTEGRATION.md) — research mapping of evolutionary cellular automata, initial-state co-evolution, symbolic billiards and graph convolution to PRISM/Q6, with attribution, exact model definitions and implementation work packages.
  - Implemented first interface: [PRISM cellular-automaton engine](../models/prism_cellular_automata.py) and [tests](../tests/test_prism_cellular_automata.py); the genetic algorithm and other modules remain pending.
  - Five-dimensional flat calibration: [generator](../scripts/rgs_prism_product_refinement.py) and [M0–M4 tests](../tests/test_t048_rgs_prism_product_refinement.py); this does not prove the curved Mosco limit.

## Theorem extraction from audited sources

The defensible identities have been promoted to standalone theorem records in the repository's [theorem register](../README.md#theorem-and-result-register):

- [T050 — Geometric spin-chain summability and operator bound](../theorems/T050-geometric-spin-chain-bounds.md)
- [T051 — Crank–Nicolson unitarity for a fixed Hermitian Hamiltonian](../theorems/T051-crank-nicolson-unitarity.md)
- [T052 — Scalar Euler–Lagrange equation for the displayed scalar–torsion action](../theorems/T052-scalar-torsion-variation.md)
- [T053 — Conditional exterior-square projector lemma](../theorems/T053-exterior-square-projector-lemma.md)
- [T054 — Static radial Klein–Gordon reduction](../theorems/T054-static-radial-klein-gordon.md)

Each record states its hypotheses, proof and non-conclusions. In particular, T053 is conditional on matrix identities not certified by the source PDF.

## Critical audits and source provenance

| Source | Editorial status | Use |
|---|---|---|
| [FORMULAZIONE — critical audit](FORMULAZIONE_CRITICAL_AUDIT.md) | Historical exploratory compilation; not a validated paper or solution report | Identifies variational, teleparallel, gauge, LQG and phenomenological claims that cannot be retained as results |
| [Naressi Law — critical audit](naressi-law/README.md) | Internal working manuscript; not peer-reviewed; physical extensions unsupported | Use together with the cleaned spin-chain note; do not cite its former UV/RG/Yang–Mills conclusions |
| [NVM external manuscript — editorial assessment](NVM_EXTERNAL_MANUSCRIPT_ASSESSMENT.md) | External candidate-model manuscript by Michael Blasco (October 2026); publication status unverified | Comparative reading only; not evidence for RGS–PSU |
| [Consolidated audit of four exploratory PDFs](FOUR_PDF_CONSOLIDATED_AUDIT.md) | Critical review of `dirac.pdf`, `siiiiii.pdf`, `soluzione.pdf` and `yess.pdf` | Records defensible residue, failed claims and next mathematical requirements; not a paper |

## Source files and archival policy

Original PDFs and imported documents are not automatically scientific papers. They belong in the source inventory or archive, not in the active research-note list. The repository's [source-file inventory](../library-inventory/README.md) records Library provenance; [quarantined files](../archive/README.md) records files whose identity or relevance is unresolved.

No source is deleted merely because its claims are rejected. A source may be removed from the active bibliography, quarantined, or deleted only when its identity, duplication or irrelevance has been established. The original Library upload is not modified by changes in this repository.

## Publication-status categories

- **Published / peer-reviewed:** publication venue and bibliographic record independently identifiable.
- **Preprint:** publicly deposited manuscript without a verified peer-review outcome.
- **Internal research note:** working document produced within the programme; not an independent source.
- **Technical report / computational audit:** reproducibility or implementation document, not automatically a mathematical proof.
- **Unverified external manuscript:** bibliographic status, provenance, or claims still require checking.
- **Non-standard / speculative source:** retained for critical analysis; not used as scientific evidence for the programme's theorems.

## Editorial acceptance checklist

Before a manuscript is promoted as a scientific result, it must provide:

1. A precise problem statement, definitions, conventions and units.
2. Explicit hypotheses and a derivation for every theorem or claimed physical relation.
3. Correct use of established mathematical and physical terminology.
4. Traceable primary references for standard results.
5. Reproducible computations, source code, raw data, tolerances and convergence checks.
6. Limiting cases, dimensional analysis, counterexamples and appropriate null models.
7. A clear separation between theorem, conditional result, numerical observation, candidate model, conjecture and speculation.
8. A statement of what the work does **not** establish.

Claims about quantum gravity, Yang–Mills mass gaps, particle spectra, cosmology, energy extraction, or new fundamental interactions require their own complete mathematical and/or empirical justification. They must not be inferred from numerical coincidences, geometric analogies, fitted constants, or terminology alone.

## Citation rule

An internal manuscript may document the origin of an idea, but it cannot serve as independent evidence for that same idea. A non-standard source may be quoted to reconstruct its proposal, but its statements must be checked against primary literature, established theory, and explicit mathematical or experimental tests.

The theorem records and verification matrix—not this catalogue—control the status of mathematical claims.
