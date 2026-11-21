# 64-point Coulomb Hessian: O_h / T_h audit

**Status: numerical verification completed for items 1–4.** The operator is (K_C), not the archived (K_0).

## Construction

Using the canonical `RGS_PSU_all_matrices.npz`, the 64 coordinates (X_{O_h}), the 192×188 tangent frame (Q_{m tangent}), and the stored Q6 adjacency, we formed the pairwise Coulomb energy
[
E_C(X)=sum_{i<j}rac{1}{|X_i-X_j|}.
]
The constrained Hessian is
[
K_C=Q_{m tangent}^{T}igl(H_C+lambda I_{192}igr)Q_{m tangent},
qquad lambda=3.7375336948226257.
]
The multiplier is fixed by the global spherical constraint stationarity condition
[

abla E_C(X)+lambda X=0.
]
The gradient norm is (57.9016230), but it is entirely radial (alignment cosine 1); the residual after the radial multiplier is (4.39\times10^{-8}). Thus the configuration is stationary for the global norm constraint, not an unconstrained critical point.

## 1. Action on the 64 labels and Q6 adjacency

All 48 signed coordinate permutations in (O_h) induce point permutations of the 64-point configuration. However, only **16 of 48** preserve the stored Q6 adjacency:
[
A[p,p]=A.
]
Therefore the point set carries the full (O_h) action, but the labelled Q6 graph does not: its automorphism subgroup here is the previously identified (D_8\times C_2). Do not describe all 48 elements as Q6 graph automorphisms.

The 188D tangent subspace is invariant under the induced ambient action to (1.46\times10^{-15}); the induced matrices are orthogonal to (4.14\times10^{-14}).

## 2. Coulomb gradient and multiplier

- (E_C=897.0080867574)
- (|\nabla E_C\|_2=57.9016230237)
- radial multiplier (lambda=3.7375336948)
- (|\nabla E_C+\lambda X\|_2=4.39\times10^{-8})

The 188D frame annihilates the three translations and the global scale vector (X), explaining (188=192-4) as three translation normals plus one dilation normal. The three near-zero eigenvectors of (K_C) match the three rigid rotational modes.

## 3. Equivariance

For every one of the 48 point-set actions,
[
\frac{\|K_C\rho(g)-\rho(g)K_C\|_F}{\|K_C\|_F}
\le 1.65\times10^{-15}.
]
The same holds on the 16-element Q6 adjacency-preserving subgroup. This is a numerical verification of the expected Coulomb (O_h)-equivariance, given the reconstructed point action and invariant tangent frame.

## 4. Isotypic decomposition

Multiplicities of the 188D representation:

| (O_h) irrep | Multiplicity | (O_h) irrep | Multiplicity |
|---|---:|---|---:|
| (A_{1g}) | 5 | (A_{1u}) | 2 |
| (A_{2g}) | 2 | (A_{2u}) | 6 |
| (E_g) | 8 | (E_u) | 8 |
| (T_{1g}) | 10 | (T_{1u}) | 13 |
| (T_{2g}) | 14 | (T_{2u}) | 10 |

Dimension check: 95 even + 93 odd = 188.

For the selected order-24 (T_h) subgroup (tetrahedron (xyz>0), together with inversion):

| (T_h) irrep | Multiplicity | (T_h) irrep | Multiplicity |
|---|---:|---|---:|
| (1_g) | 7 | (1_u) | 8 |
| (1'_g) | 8 | (1'_u) | 8 |
| (1''_g) | 8 | (1''_u) | 8 |
| (3_g) | 24 | (3_u) | 23 |

The conjugate one-dimensional irreps (1') and (1'') occur equally, as required for this real representation. Dimension check: 95 even + 93 odd = 188.

## Coulomb spectrum and interpretation

(K_C) has 29 negative, 3 near-zero, and 156 positive eigenvalues, with minimum (-2.7768623) and maximum (15.5753024). The three near-zero modes are the rigid rotations. The negative modes mean the constrained configuration is not a local minimum of the Coulomb energy on this 188D tangent space.

Crucially, (K_C\ne K_0): the previously measured Frobenius distance is approximately 79.57. (K_C) is a symmetry-controlled comparison operator, not a reconstruction of (K_0).

## Scope

Completed: requested points 1–4, including the (O_h) and (T_h) representation multiplicities.

Not done here: the 60-vertex C60 Hessian and sector-by-sector C60 comparison (points 5–6). No 64↔60 vertex identification is assumed.
