# Recovered-source Q6/Kirchhoff audit — 2026-11-19

**Input:** Library archive `RGS_PSU_all_matrices(1).npz` (original source archive; read-only).
**SHA-256:** `29b758d56c20ba9eb488d1846d1439c0fc145973762421d03083239ee832bba1`

## Results reproduced from the recovered NPZ

| Check | Result | Evidence |
|---|---|---|
| Q6 states | PASS | Shape `(64,6)`; 64 unique states |
| Adjacency | PASS | `(64,64)`, symmetric, zero diagonal, every vertex degree 6 |
| Edge count | PASS | 192 edges, each changes exactly one bit |
| Six coordinate edge sectors | PASS | 32 edges for each bit 0…5 |
| Kirchhoff lower/upper split | PASS | Bits 0–2: 96; bits 3–5: 96 |
| Graph Laplacian | PASS | Archived `Q6_laplacian = diag(degree)-adjacency`; zero row sums |
| Vertex-edge incidence | PASS | Canonical incidence `B1` derived from archived states and adjacency |
| Square faces | PASS | 240 coordinate 2-cells derived from the 6-bit cube |
| Chain identity | PASS | Exact integer `B1 B2 = 0` |
| Incidence Laplacian | PASS | `B1 B1ᵀ = Q6_laplacian` |
| Source integrity | PASS | Container hash recorded above |

## Source array inventory

| Array | Shape | SHA-256 |
|---|---|---|
| `X_Oh_reconstructed` | `(64,3)` | `6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf` |
| `Q_tangent` | `(192,188)` | `829f9fa5be27fb93db91252f60381e1af6803e6629fa5a586b023b851088e6a2` |
| `A_geometry_orthonormal` | `(188,64)` | `6da9140a6632d8251fa2ae1ec86e0a5aaca6354f95296627b2ee28195155f873` |
| `A_raw` | `(188,64)` | `bdb04174dbd0c2e9b9f108163ba698e1d6786140dc3842013ac9900201874cc4` |
| `P_G` | `(188,188)` | `9ef8571fa82e2a6e670a32ea60c6c3762231646ee0c09016570e6266c0f151f0` |
| `K0` | `(188,188)` | `d7e70c87d1f068af9399be231f95f5f7b09e70ba1d444df52bc70c19011bb614` |
| `R_geo_tangent` | `(188,188)` | `aebe273e5500c248fe4a06b0d4c5e5c8540c17aa7575e8a776f9d2f51aedd14f` |
| `Pi_AT` | `(64,64)` | `4e109f68f58116cce04b60aa9b9f39c4277979997e369960c2d88fabba7c56cb` |
| `B_PG_A` | `(188,64)` | `76dab1a76bcb16b68230d16c92240564874e5208dbeb8f9256ca3c871339ad48` |
| `U_polar` | `(188,64)` | `7109c318a50ead096ef43c3532b3dc221fd0b2340ae9a8d2ccfff97f54cfe0cb` |
| `T_transport` | `(188,188)` | `3ba0e8ec76fd004604ae7b94d658668864b650707aad08be04f82f4a6df95f2f` |
| `Q6_states` | `(64,6)` | `d6872a1c84ee288c42517c3753bd6245470877380005b350e8cdaecd00759d70` |
| `Q6_adjacency` | `(64,64)` | `b6a659c81d9b8305b551f45f1271cb2f91965b988bf5bb78a9ea4fa35ddfa2b5` |
| `Q6_laplacian` | `(64,64)` | `c214acc1a40d2a37f981f1f82ab95fae94fb8cfcee2e6fd832842b5a46d5c913` |
| `Q6_antipodal` | `(64,64)` | `e46d8583203f97afa521c07ec89a0f1dab4824f23ca24643e205f7743c397c8c` |

## NOT TESTED

The archive contains no explicit SU(2) link array, two-sheet operator blocks, mirror permutation/spin map, polariton reservoir parameters, stress-response data, or independent RGS site measure/edge weights. Therefore gauge-link covariance, two-sheet conjugation and J=0, mirror intertwining, polariton dynamics, Keldysh response and physical viscosity remain **NOT TESTED**. They are not inferred from the Q6 Kirchhoff PASS results.

The edge and face incidence were derived only from the archived 6-bit Q6 states and adjacency matrix, which is an exact combinatorial audit—not a reconstruction of the RGS geometry.
