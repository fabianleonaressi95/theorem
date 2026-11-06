# RGS 188D: reconstruction of the cubic action and T2u intertwiner

This audit closes the missing-data step identified in the Herasymov/RGS thread:
the 48 tangent representation matrices are reconstructed from the original
vertex coordinates and tangent basis, rather than guessed or synthesized.

## Input

An NPZ with:
- `X`: (64, 3) vertex coordinates (accepted aliases: `X_Oh`,
  `X_reconstructed`);
- `Q`: (192, 188) orthonormal tangent basis (accepted aliases:
  `Q_archived`, `Q_tangent_svd`, `Q_tangent`).

The A14 Jacobian bundle contains the original coordinate and tangent-basis
artifacts; inspect its NPZ key names and select the compatible archive.

## Construction

For each signed permutation matrix (g\in O_h), match the transformed
vertices (gX_i) to the original vertex set. The induced ambient action on
vertex displacements is
[
(U_{amb}(g)v)_{\pi_g(i)}=g v_i.
]
The tangent action is
[
U_{tan}(g)=Q^T U_{amb}(g)Q.
]
The script checks tangent invariance before accepting the restriction.

The carrier (T_{2u}) is realized by the cubic harmonic vector
[
h(x,y,z)=\big(x(y^2-z^2),\ y(z^2-x^2),\ z(x^2-y^2)\big).
]
Its 3D matrices (D_{T2u}(g)) are obtained by exact finite-dimensional
least-squares realization of (h(gx)=D(g)h(x)) on generic sample points.
The full isotypic projector is
[
P_{T2u}=\frac{3}{48}\sum_{g\in O_h}
\chi_{T2u}(g)U_{tan}(g).
]
For ten carrier copies, the source representation is
(I_{10}\otimes D_{T2u}(g)), dimension 30. A deterministic Reynolds
projection produces one intertwiner candidate:
[
J=\frac1{48}\sum_g U_{tan}(g)J_0
(I_{10}\otimes D_{T2u}(g))^T.
]

## Run

```bash
python audit_rgs_t2u_from_XQ.py path/to/original_matrices.npz \
  --output results/rgs_t2u_reconstruction
```

Writes JSON diagnostics and a compressed NPZ with `U_tan`, `D_t2u`,
`group`, `P_T2u`, `J`, and singular values.

## Evidential status

The code is committed as a reproducible reconstruction procedure. A numerical
RGS result is established only after running it on the recovered original
NPZ and inspecting the generated residuals. The synthetic intertwiner
self-test elsewhere in this directory is not a substitute for that run.
