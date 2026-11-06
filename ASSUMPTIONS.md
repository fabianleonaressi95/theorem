# Assumptions and conventions

This document states every modelling choice made in the benchmark. Anything
not listed here is either a direct numerical observation or flagged as a
conjecture in `REPORT.md`.

## 1. Discrete complex

* The mesh is the Cartesian product of 1D interval complexes on `[0,1]^d`
  (`d = 2, 3`). Cochains `C^k` are the free vector spaces on oriented
  k-faces (vertices, edges, square faces, cubes). `dim C^k = n_k` equals the
  number of k-faces; Euler characteristic is 1 (contractible domain).
* Coboundary matrices `d_k : C^k -> C^{k+1}` are the oriented incidence
  matrices with the standard cubical boundary sign
  `(-1)^{pos+1} (2s-1)` (`pos` = position of the removed direction inside the
  sorted `vary` tuple, `s` = lower/upper facet). `d_{k+1} d_k = 0` holds
  exactly; the residual `max |d_{k+1} d_k|` is reported per run.
* This is a *cochain* complex: no finite-element conformity is assumed or
  needed. In particular the discrete spaces are NOT the FEEC
  polynomial differential form spaces; they are the cubical cochain spaces
  with a diagonal Hodge inner product (see §3).

## 2. Cell maps and pullback metric

* A single global smooth map `Phi : [0,1]^d -> R^d` generates the mesh.
  Cell maps are restrictions `F_K(xi) = Phi(p_K + h * xi)`, which have the
  required form `x_K + A_K xi + r_K(xi)` with `A_K = h D Phi(center_K)`.
  Conformity (shared face parametrisations) is automatic because `Phi` is
  single-valued.
* Available maps: `identity`, `affine` (constant matrix), `sinusoid`
  `Phi(x) = x + a P(x) c` with `P(x) = prod_i sin(m pi x_i)`.
  `P` vanishes on `∂[0,1]^d`, so the domain boundary is held fixed while
  interior cells are curved. The amplitude `a` is independent of `h`
  unless the `amplitude_h = [a0, gamma]` schedule `a = a0 h^gamma` is
  selected explicitly.
* Pullback metric `g_K = DF_K^T G(F_K) DF_K`, where `G` is an ambient
  metric (`identity`, `aniso`, `oscillatory`, `nonuniform`; all diagonal
  SPD). The Riemannian volume element on the reference cube is
  `sqrt(det g_K) dxi` — this already equals the physical volume element,
  no extra `det DF` factor appears.
* Quadrature: tensor Gauss-Legendre, `nq` points per direction for cell
  quantities, `nqf` for face measures (defaults 5 and 4).

## 3. Discrete inner products (Hodge weights)

For `k < d`, with `|sigma|_{g,K}` the k-volume of face `sigma` measured in
the pullback metric of cell `K`:

```
M_k[sigma,sigma] = sum_{K supset sigma}  vol_g(K) / (2^{d-k} |sigma|^2_{g,K})
M_d[K,K]         = vol_g(K)
```

* For a flat affine mesh with `G = I` this reduces **exactly** to the
  standard DEC weights `|sigma*| / |sigma|` (verified: e.g. interior edge
  weight 1 in 2D, `h` in 3D; interior face weight `1/h` in 3D).
* Under anisotropic/non-uniform metrics the formula is a documented
  approximation of the true dual-volume ratio: `vol(sigma*_K)` is
  estimated as `vol_g(K) / (2^{d-k} |sigma|_{g,K})`. Off-diagonal (consistent)
  mass matrices are NOT implemented.
* `M_k` are diagonal hence trivially SPD when all face measures are
  positive; `cond(M_k)` is reported per run.

## 4. Operators

* Codifferential `delta_k = M_{k-1}^{-1} d_{k-1}^T M_k`.
* Hodge Laplacian `Delta_k = d_{k-1} delta_k + delta_{k+1} d_k`, self-adjoint
  w.r.t. `M_k`; eigenproblem solved as `B_k x = lambda M_k x` with
  `B_k = M_k Delta_k` (symmetric; symmetry residual reported).
* No boundary conditions are imposed — this is the algebraic Hodge
  Laplacian of the full complex ("absolute" type). On the contractible
  domain the analytic Betti numbers are `(1,0,...,0)`; `kernel_num` is the
  numerically observed dimension of `ker Delta_k` and is compared with
  `betti` computed from ranks of the incidence matrices.

## 5. What is and is not claimed

* **Verified numerically**: all residuals in `algebraic_residuals`
  (`d^2=0`, symmetry of `B_k`, adjointness, self-adjointness, partition of
  unity), Betti/kernel agreement, Jacobian determinants and singular
  values, condition numbers, eigenvalues on each fixed mesh.
* **Indicators only**: refinement behaviour of `lambda_min^+`,
  `lambda_max`, `cond(M_k)`, `cond_effective`. Convergence of these
  discrete eigenvalues as `h -> 0` is *consistent with* stability of the
  discrete scheme but is NOT a proof of Mosco/variational convergence of
  the underlying forms — that is left to the analytical work.
* **Conjectures** are labelled as such in `REPORT.md`.
