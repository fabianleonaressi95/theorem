# Classification protocol

Every case receives a stable identifier and the following record.

## A. Source provenance
- Full title, author(s), year, venue, DOI/URL.
- Exact page/figure/table for the diagram.
- Source access status and transcription reviewer.
- Distinguish original historical object, modern redraw, and mathematical idealization.

## B. Geometric data
- Coordinate frame and normalization (state which length is set to 1).
- Marked points, centres, radii, lines and circle equations.
- Incidence table and tangency table; distinguish internal/external tangency.
- Construction DAG: parent objects, operation, and branch/sign choice at every step.
- Degenerate cases and excluded parameter values.

## C. Symmetry
Report separately: full Euclidean isometry group of the unlabelled configuration; subgroup preserving all marks and labels; orientation-preserving subgroup; similarity symmetries if scale is quotiented out. Never infer the symmetry group solely from a visually symmetric diagram.

## D. Algebraic fields
Record separately: base field K0; coordinate field in the chosen frame; real coordinate field; squared-distance/radius-square field; distance/radius field; minimal polynomials and degrees where established; field automorphism/Galois group only when explicitly computed.

Do not equate the geometric symmetry group with the Galois group. Record the effect of changing the coordinate frame.

## E. Equivalence relations
A comparison must state which relation is used: labelled congruence; unlabelled congruence; labelled similarity; incidence-graph isomorphism; tangency-graph isomorphism; equality of normalized metric data; isomorphism of generated fields (strictly weaker than geometric equivalence).

## F. Evidence labels
Use exactly one primary status:
- PROVED: symbolic derivation with assumptions and proof;
- EXACT-COMPUTATION: exact symbolic/combinatorial calculation independently reproducible;
- NUMERICAL: floating-point evidence with tolerances and seed/method;
- MODEL: result conditional on an explicitly chosen idealized diagram/model;
- HISTORICAL-UNVERIFIED: attribution or transcription not checked against primary source;
- OPEN: unresolved question.

A case can have multiple subclaims with different statuses. Never upgrade a historical claim because its algebra is correct.
