# RGS–PSU source transfer and provenance

This directory imports the recovered RGS–PSU provenance records from
[`fabianleonaressi95/rgs-qlg-quaternion-bridge`](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge).
The source project remains the provenance authority for its computational implementation.

## Transferred into this repository

- `data/rgs_188d/A14_jacobian_report.json`: reported A14 constraint-Jacobian audit.
- `data/rgs_188d/ellis_curved_seed_manifest.json`: coordinate/edge/coframe reconstruction manifest and SHA-256 fingerprints.
- `data/rgs_188d/RECOVERED_SOURCE_ARTIFACTS.md`: inventory, definitions, reported checks, and unresolved identification issues.

## Original binary archive identities

| Archive | SHA-256 | Role |
|---|---|---|
| `A14_RGS_PSU_QLG_JACOBIAN_BUNDLE.zip` | `80442238349cd6ddc720dabae93d083075dea88decba8acf0a78c3ec03e0abcc` | O_h coordinates, constraint Jacobian, tangent/normal bases |
| `A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip` | `7ca0cdfeadbe1d693d4f776a5e22d957630b206b842f4b822f3afb578c488922` | QLG fibre operators, Q basis, geometric tangent operators, SU(2)/SO(3) links |
| `Q6_exact_incidence_and_H241.npz` | Not recorded in the transferred manifest | Q6 edges/squares, B1/B2, adjacency/Laplacian, effective H241 |

**Binary-transfer status:** the ZIP/NPZ payloads themselves are not added by this change.
The source repository documents their recovery from Library and records their hashes,
but the binary archives are not present as committed files at the referenced source
paths. This PR therefore transfers provenance and numerical reports, not the original
binary bytes. No archive is regenerated or represented as byte-for-byte transferred.

## Mathematical scope and safeguards

- A14 validates the four constraint covectors, rank 4, and the 188-dimensional
  tangent kernel. Reported residuals are preserved verbatim in the JSON file.
- The A14 report explicitly does **not** validate the original 192x192 energy Hessian
  or the 29/3/156 Hessian spectrum.
- A13's `K0` and `K_geometry_tangent` must not be silently identified with
  (Q^T H Q) until their definitions and provenance are compared.
- The Q6 graph cycle rank (129) and the first Betti number after filling the 240
  square faces are different quantities.
- The curved Ellis refinement is a finite-domain geometric benchmark, not a
  full RGS–EMS field-equation solution; flat-torus Mosco convergence is not
  automatically transferred to this curved family.

## Source implementation

The Phase 6 audit implementation remains in the source project:
[`examples/rgs_q6_phase6_audit.py`](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/examples/rgs_q6_phase6_audit.py).
It imports `src.discrete_dirac` and its supporting Clifford/representation modules;
it is not copied here as a standalone runnable script because that dependency set
has not yet been ported into `theroem`.

## Next exact transfer required

To make this repository self-contained, add the actual A13/A14 ZIPs and Q6 NPZ
as binary assets (or publish immutable release assets), record their computed
SHA-256 hashes, then port the source audit package with tests. Until then, this
change is a provenance/documentation transfer, not a complete data migration.
