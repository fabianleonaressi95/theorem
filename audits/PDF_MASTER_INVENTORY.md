# PDF master inventory — 18 November 2026

**Repository:** `fabianleonaressi95/theorem`  
**Branch:** `main`  
**Snapshot:** 30 PDF files in the repository before this reorganization.  
**Policy:** preserve every source blob; classify only what is supported by existing repository records; leave unidentified files quarantined. A filename is not bibliographic evidence.

## Result of the reorganization

- **10** identified bibliographic/source PDFs grouped by subject (including the structured-deformation preprint).
- **1** exact-computation report grouped with its corresponding 2I audit.
- **12** internal or author-associated research documents grouped separately from the external bibliography.
- **6** unidentified PDFs moved to `archive/unclassified/`; the already quarantined `zps (1).pdf` remains there.
- **No PDF was deleted or altered.** Moves preserve the original Git blob SHA.

## A. Bibliography and source literature

| New repository path | Identification / scope | Editorial status |
|---|---|---|
| `bibliography/special-functions-beta-zeta-bernoulli-veneziano/S0025-5718-97-00854-5.pdf` | Yui–Zagier (1997), *On the Singular Values of Weber Modular Functions* | Primary source; audited in the 10 November source audit |
| `bibliography/special-functions-beta-zeta-bernoulli-veneziano/JTNB_2002__14_1_325_0.pdf` | Reinhard Schertz (2002), *Weber's Class Invariants Revisited* | Primary source; metadata recorded in the bibliography |
| `bibliography/special-functions-beta-zeta-bernoulli-veneziano/DLMF_ NIST Digital Library of Mathematical Functions.pdf` | NIST Digital Library of Mathematical Functions, general reference | Reference work; cite exact sections |
| `bibliography/special-functions-beta-zeta-bernoulli-veneziano/DLMF_ §23.18 Modular Transformations ‣ Modular Functions ‣ Chapter 23 Weierstrass Elliptic and Modular Functions.pdf` | NIST DLMF §23.18 | Reference source for modular transformations |
| `bibliography/special-functions-beta-zeta-bernoulli-veneziano/DLMF_ §25.2 Definition and Expansions ‣ Riemann Zeta Function ‣ Chapter 25 Zeta and Related Functions.pdf` | NIST DLMF §25.2 | Reference source for zeta/eta identities |
| `bibliography/special-functions-beta-zeta-bernoulli-veneziano/minka-dirichlet.pdf` | Thomas P. Minka, *Estimating a Dirichlet Distribution* | Technical reference; see existing bibliography entry |
| `bibliography/special-functions-beta-zeta-bernoulli-veneziano/mit18_785f21_lec19.pdf` | A. V. Sutherland, MIT 18.785 Lecture 19, *The Analytic Class Number Formula* | University lecture notes; see existing source audit |
| `bibliography/special-functions-beta-zeta-bernoulli-veneziano/2203.12769v1.pdf` | Amar–Matias–Morandotti–Zappale, *Periodic Homogenization in the Context of Structured Deformations* | Published ZAMP 73 (2022), article 173; DOI 10.1007/s00033-022-01817-6 |
| `bibliography/gauge-wilson-qft/0205083v1.pdf` | Sameen Ahmed Khan, *Maxwell Optics: I. An Exact Matrix Representation of the Maxwell Equations in a Medium* | Physica Scripta 71 (2005), 440–442; arXiv:physics/0205083; background only, scope caveat in prior audit |
| `bibliography/spin-geometry-quaternionic/spherical-space-forms/18_57.pdf` | Akira Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Mathematical Journal* 18 (1995), 57–67 | Identified primary source for spherical spectra and finite-group quotients |
| `audits/2i_real_molien_exact/GAP_sessione_2A5_McKay_2I.pdf` | PDF companion to the archived GAP session report `GAP_sessione_2A5_McKay_2I.html` | Computational audit artifact, not an external publication |

## B. Internal research documents — not bibliography entries

| New repository path | File(s) | Treatment |
|---|---|---|
| `documents/research-materials/fdt/` | `FDT-Fmax-Modulus.pdf`; `FDT-What-Psi-Is.pdf`; `FDT-c-Geometric-Derivation.pdf`; `born-rule-fdt.pdf`; `fdt-analysis-jet-diffusion-wake-g49y-8cjl.pdf` | Working/research material. Keep separate from peer-reviewed sources; claims require theorem-level and physical validation before promotion. |
| `documents/research-materials/ratti/` | `Estrarre-Positroni-dal-Vuoto_Prof-Sergio-P-Ratti_2009.pdf`; `Fondamenti-teorici-e-analisi-qualitativi-e-quantitativi_Prof-Sergio-P-Ratti.pdf`; `Generatore-Energia-a-trasporto-positronico_Prof-Sergio-P-Ratti_2009.pdf`; `Generatore-Energia-per-separazione-coppie-virtuali_Prof-Sergio-P-Ratti_2009.pdf`; `Notes-on-positrons-extraction-from-the-quantum-vacuum_Prof-Sergio-P-Ratti_2010.pdf`; `Polveri-e-Cubi_Prof-Sergio-P-Ratti.pdf`; `Produzioni-ioni-metallici-senza-intervento-antimateria_Prof-Sergio-P-Ratti_2007.pdf` | Author-associated technical/research documents. Preserve as source material; do not treat filenames as proof of publication status or scientific validity. Full document-level audit remains a separate task. |

## C. Quarantined — identity or provenance not established

| New repository path | Original filename | Reason |
|---|---|---|
| `archive/unclassified/1836400843.pdf` | `1836400843.pdf` | Numeric filename; no reliable identification in current repository records |
| `archive/unclassified/1848547691.pdf` | `1848547691.pdf` | Numeric filename; no reliable identification in current repository records |
| `archive/unclassified/504794103.pdf` | `504794103.pdf` | Numeric filename; no reliable identification in current repository records |
| `archive/unclassified/Mukai.pdf` | `Mukai.pdf` | Surname-only filename; author, title, edition and content not established |
| `archive/unclassified/OMNIUM-VORTEX.pdf` | `OMNIUM-VORTEX.pdf` | Title-like filename; authorship, provenance and relevance not established |
| `archive/unclassified/master05-26-2025.pdf` | `master05-26-2025.pdf` | Filename/date insufficient to establish author, title, version or content |
| `archive/unclassified/zps (1).pdf` | `zps (1).pdf` | Previously quarantined; retain until document-level identification |

Quarantined sources are retained, not endorsed, and not cited as evidence. Do not delete or reclassify them without inspecting their title pages, provenance and contents.

## D. Reorganization rules

1. External publications and authoritative references belong in subject-specific `bibliography/` directories.
2. Internal research notes, technical dossiers and author-supplied documents belong in `documents/research-materials/`, not in the peer-reviewed bibliography.
3. Computational reports belong beside their audit or code.
4. Unidentified sources remain in `archive/unclassified/`.
5. Every future move must update this inventory and preserve source provenance.
6. The 10 November audit remains the detailed mathematical/source audit for the 13 PDFs then reviewed; it is not the current complete inventory. Its mathematical corrections and caveats remain in force.

## E. Related records

- [10 November focused PDF source audit](2026-11-10_pdf_repository_audit.md)
- [General bibliography](../bibliography/README.md)
- [Special-functions / structured-deformations bibliography](../bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md)
- [Quarantined-source policy](../archive/README.md)
- [Manuscript and research-note policy](../manuscripts/README.md)
