# T161 record-level integration audit — 27 November 2026

**Purpose:** reconcile the primary theorem corpus with the generated register and extract explicit dependency declarations without confusing navigation with proof.

## 1. Live inventory

- Primary repository `main`: **284** Markdown records under `theorems/`.
- Working branch `rgs-q6-antitwin-spacetime-bridge`: **289** records.
- Branch-only records relative to main: 5 (`theorems/T146-q6-ivm-psu-spinorial-lift.md`, `theorems/T147-spinorial-rgs-q6-spin6-dirac-antitwin.md`, `theorems/T148-psu-antitwin-chiral-fluid-gauge.md`, `theorems/T149-q6-clifford-graph-dirac-spectrum.md`, `theorems/T161-q6-ivm-rhombic-triacontahedron-lorentzian-spin-lift.md`).
- Valid theorem rows in `docs/THEOREM_MASTER_REGISTER.csv`: **280**, covering 280 unique files.
- Main-tree files absent from the register: **4**:
  - `theorems/T157-vertex-fixed-metric-obstruction-jitterbug.md`
  - `theorems/T158-standard-snub-cube-twist-angle.md`
  - `theorems/T159-vertex-fixed-metric-obstruction-jitterbug.md`
  - `theorems/T160-standard-snub-cube-twist-angle.md`

The register therefore does not yet cover the full live theorem tree. Do not quote its status totals as corpus-wide totals until regenerated and checked.

## 2. Status counts — register rows only

| Status | Count |
|---|---:|
| CANDIDATE | 6 |
| CONDITIONAL | 83 |
| EXACT_CERTIFICATE | 14 |
| HYPOTHESIS | 2 |
| NUMERICALLY_VERIFIED | 86 |
| OPEN | 44 |
| PROVED | 45 |

These are machine-assisted register labels, not author-certified proof status. The authoritative evidence remains each theorem card and its proof/certificate.

## 3. Explicit dependency declarations

The 280 valid register rows contain 410 semicolon-separated dependency tokens across 142 rows.

| Resolution | Count | Treatment |
|---|---:|---|
| Unique register ID | 306 | Imported as `declared-dependency-unreviewed`; not yet a proof edge |
| Ambiguous ID | 101 | Kept unresolved with all candidate file paths |
| No matching ID | 3 | Kept unresolved; requires source/register correction |

There are **32 duplicated display-ID groups** in the register. Repeated IDs such as T021, T024, T129, T149, T157–T160, S009–S011 and others cannot safely be used as unique dependency keys. Full file paths are the canonical record keys.

## 4. Duplicate/parallel records requiring explicit disposition

The primary tree contains parallel records with repeated display IDs. In particular:
- `T157-vertex-fixed-metric-obstruction-jitterbug.md` and `T159-vertex-fixed-metric-obstruction-jitterbug.md` state the same vertex-fixed metric obstruction with different downstream T156/T159 labels.
- `T158-standard-snub-cube-twist-angle.md` and `T160-standard-snub-cube-twist-angle.md` state the same standard snub-cube twist comparison.

These files are preserved. They should be marked as duplicate/parallel records with provenance and a canonical successor chosen only after checking their complete histories; they are not counted as independent mathematical results merely because they have different T numbers.

## 5. Relation to the T161 geometric spine

The existing 27-chapter crosswalk remains canonical for narrative placement. T161 is a geometric spine, not a universal proof parent. Its directly reviewed interfaces remain:
- T129 golden cut-and-project frame → T161 zonotope window;
- T146 Q6–IVM–PSU carrier → T161 distinction between 64 projected points and 32 zonotope vertices;
- T147 Spin(6) → T161 Euclidean representation input, not a Lorentzian identification;
- T148 PSU–Anti-Twin → T161 conditional timelike/spacelike decomposition;
- T149 bare Q6 Clifford operator → T161 exact spectral obstruction;
- T150 D6/Fibonacci two-sheet orbit → comparison only.

The IVM/FCC (O_h) to golden (I_h) map, Lorentzian time-leg derivation, ISO((1,3)) Cartan transport, and refinement-consistent (mathrm{Spin}^+(1,3)) Dirac limit remain open.

## 6. Reproduction and next gates

Machine-readable evidence: [T161_REGISTER_DEPENDENCY_AUDIT_2026-11-27.json](T161_REGISTER_DEPENDENCY_AUDIT_2026-11-27.json).

1. Regenerate the theorem register from the current tree using `scripts/build_theorem_register.py`; inspect its diff rather than trusting heuristic totals.
2. Replace display-ID dependency references with full theorem paths or stable unique keys.
3. Review the 306 unique declarations against both endpoint cards before upgrading any edge to a proof dependency.
4. Resolve the 101 ambiguous and 3 missing references.
5. Record duplicate/parallel-card provenance without deleting or renumbering history.
6. Continue the 27-chapter crosswalk at chapter level; do not make T161 the parent of unrelated arithmetic, Rumin, FEEC, Morandotti or dynamics theorems.
