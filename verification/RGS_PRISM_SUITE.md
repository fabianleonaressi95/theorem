# RGS / PRISM finite verification suite

Run the repository-contained PRISM audit:

```bash
python -m pip install numpy
python scripts/verify_rgs_prism_laws.py --output rgs-prism-report.json
```

## PRISM product graph

The checked graph is exactly
`C64 □ C6 □ C6 □ C6 □ C5`, with the mixed-radix index

```
((((g*6 + l)*6 + c)*6 + t)*5 + b)
```

The script verifies the 69,120 vertices, degree 10, reciprocal adjacency,
345,600 undirected edges, and the product-graph Laplacian gap

```
lambda_1 = 4 sin^2(pi/64) = 0.009630546656...
```

This is the full Cartesian product graph. It must not be conflated with a
filtered/active PRISM subgraph or with a separate Hodge operator.

## Optional RGS 188D audit

The repository does not bundle the user's numerical arrays. To audit them,
prepare an NPZ archive with these exact keys:

- `Q`: shape (192,188)
- `K_tangent`: shape (188,188)
- `B_T2U_TAN`: shape (188,3)
- optional `X_Oh_reconstructed`: shape (64,3)

For example, with the original NPY files available locally:

```python
import numpy as np
np.savez(
    "rgs188d.npz",
    Q=np.load("Q.npy"),
    K_tangent=np.load("K_tangent.npy"),
    B_T2U_TAN=np.load("B_T2U_TAN.npy"),
    X_Oh_reconstructed=np.load("X_Oh_reconstructed.npy"),
)
```

Then run:

```bash
python scripts/verify_rgs_prism_laws.py --rgs-npz rgs188d.npz
```

It checks array dimensions, finiteness, orthonormality of the 188 columns of
Q, symmetry of K, and reports the numerical inertia of K using tolerance
1e-8. It does not hard-code a desired inertia or treat a near-zero threshold
as an exact nullity certificate.

## Optional Krist-All polynomial audit

If the finite Krist-All operator is available as a square NumPy matrix K:

```bash
python scripts/verify_rgs_prism_laws.py --kristall-matrix K.npy
```

The test reports the normalized Frobenius residual of
`K^3 - K^2 - I`. This verifies the polynomial identity for that supplied
matrix only; it does not reproduce or certify the reported 11,725-class
enumeration.

## Evidence boundary

The product-graph checks are deterministic finite combinatorics. The RGS and
Krist-All sections are conditional on user-supplied arrays. Floating-point
residuals are numerical checks, not exact certificates. This suite does not
establish Mosco-2 compactness, a second-order form limit, a
Laplace-Beltrami-Yang-Mills limit, or a physical interpretation.


## Auditing the recovered source archives

The original source archives were recovered from the research Library:

- `Q6_K_J_reconstruction.zip`
- `188D_FINAL_BUNDLE.zip`

Run the archive-aware verification:

```bash
python scripts/verify_archived_rgs_q6.py \
  --q6-zip Q6_K_J_reconstruction.zip \
  --188d-zip 188D_FINAL_BUNDLE.zip \
  --output archived-rgs-q6-report.json
```

The Q6 archive contains `states_Q6.npy`, `A_Q6.npy`, `K6_laplacian.npy`,
`J_antipodal.npy`, and `R_bit_rotation.npy`. The 188D archive contains
`K0.npy`, `Kinv.npy`, `P_G.npy`, `J.npy`, `J_A.npy`, and `J_B.npy`.
The script tests the actual stored arrays, including

```
K0 Kinv = Kinv K0 = I - P_G
```

The recovered Krist-All source package also runs
`src/audit/verify_core_identities.py`, which checks the 69,120-state mixed-radix
index bijection, the positive root of `psi^3 - psi^2 - 1 = 0`, and the
simultaneous shift order 960. The archive-aware PRISM audit repeats these
source-level identities.

**Evidence boundary:** the 188D archive does not contain `Q_tangent`,
`X_Oh_reconstructed`, or `B_T2U_TAN`; the full geometric 188D construction
therefore remains unverified by this bundle. The recovered Krist-All package
does not contain the 11,725-class operator matrix K, so `K^3 = K^2 + I`
remains untested against that operator. No continuum or physical conclusion
follows from these finite checks.
