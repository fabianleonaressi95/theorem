# Ideal C60 Coulomb Hessian and T_h comparison with Q6-64

**Numerical construction and symmetry audit completed.** The same all-pairs Coulomb functional is compared on two different point configurations. No correspondence between the 60 C60 vertices and the 64 Q6 labels is imposed.

## Geometry

The 60 coordinates are generated from a regular icosahedron. For each of its 30 edges {u,v}, include the two directed truncation points
\[
x_{u\to v}=(2u+v)/3,\qquad x_{v\to u}=(2v+u)/3.
\]
This gives the ideal truncated icosahedron: 60 vertices, 90 shortest-distance bonds, degree 3 at every vertex, all bond lengths 2/3, and common radius 1.6520124394. This is an exact ideal polyhedral model, not an experimentally optimized or DFT-relaxed C60 geometry.

## Functional and tangent reduction

For both configurations use
\[
E_C(X)=\sum_{i<j}\frac{1}{\|X_i-X_j\|},\qquad H_C=\nabla^2 E_C.
\]
The 180D ambient displacement space of C60 is reduced by the same four normal directions used in Q6-64: three translations and one global dilation. The resulting tangent dimension is 176.

For comparison, both operators are raw projected Hessians:
\[
K_{60}^{raw}=Q_{60}^{T}H_CQ_{60},\qquad
K_{64}^{raw}=Q_{64}^{T}H_CQ_{64}.
\]
No radial Lagrange shift is applied to either comparison operator.

## Stationarity finding

For ideal C60:
- \(E_C=939.3989137315\);
- \(\|\nabla E_C\|_2=73.4774650022\);
- radial least-squares multiplier \(\lambda_{radial}=5.7368325938\);
- residual after radial correction \(\|\nabla E_C+\lambda X\|_2=3.1246689813\);
- tangent gradient norm \(\|Q_{60}^{T}\nabla E_C\|_2=3.1246689813\);
- radial alignment cosine \(0.99909538\).

The ideal truncated icosahedron is **not a stationary point** of the all-pairs Coulomb energy on the translation/scale-reduced tangent. The radial multiplier is diagnostic only, not a valid Lagrange multiplier for a stationary point. Thus \(K_{60}^{raw}\) is a projected Hessian diagnostic, not a constrained-equilibrium Hessian.

The raw projected C60 Hessian has 87 negative and 89 positive eigenvalues, with extremes \(-17.9194337444\) and \(23.4511700119\). There are no near-zero modes at tolerance \(10^{-8}\).

## Symmetry verification

The ideal C60 point set carries 60 proper icosahedral rotations and inversion, giving \(I_h\) of order 120. An order-24 \(T_h=A_4\times C_2\) subgroup was selected from the icosahedral rotation group.

Maximum relative commutator residuals:
- full \(I_h\) on C60: \(1.6405\times10^{-15}\);
- selected \(T_h\) on C60: \(1.5836\times10^{-15}\);
- selected \(T_h\) on Q6-64: \(1.8938\times10^{-15}\).

Both projected Hessians are numerically \(T_h\)-equivariant; the C60 operator is also \(I_h\)-equivariant.

## Sector comparison

Each raw Hessian spectrum is multiplied by \(R_{rms}^{3}\), equivalent to rescaling each configuration to RMS radius 1. Coulomb Hessians scale as length to the power -3.

Entries are multiplicity; normalized minimum; normalized maximum; normalized mean.

| \(T_h\) sector | Q6-64 | Ideal C60 |
|---|---:|---:|
| \(1_g\) | 7; -19.985; 85.964; 22.891 | 7; -75.420; 105.732; 13.309 |
| \(1'_g\) | 8; -24.647; 53.132; 14.969 | 8; -68.613; 90.693; 13.646 |
| \(1''_g\) | 8; -24.647; 53.132; 14.969 | 8; -68.613; 90.693; 13.646 |
| \(3_g\) | 24; -43.459; 45.757; -6.306 | 22; -80.791; 90.693; -5.503 |
| \(1_u\) | 8; -34.442; 38.482; -8.498 | 7; -80.296; 68.956; -8.019 |
| \(1'_u\) | 8; -47.307; 27.125; -18.914 | 7; -72.098; 47.764; -13.574 |
| \(1''_u\) | 8; -47.307; 27.125; -18.914 | 7; -72.098; 47.764; -13.574 |
| \(3_u\) | 23; -34.753; 58.133; 5.371 | 22; -80.296; 100.440; 3.730 |

The conjugate \(1'\) and \(1''\) sectors have identical spectra in each real symmetric problem. Their labels can be interchanged by the orientation convention for the two \(A_4\) three-cycle classes.

All eight sector labels occur in both systems. Multiplicities agree in \(1_g,1'_g,1''_g\), and differ in \(3_g,1_u,1'_u,1''_u,3_u\). The normalized sector means have the same sign in all eight sectors. The spectra are not equal, and no mode-by-mode pairing is asserted.

## Classification

- Exact ideal truncated-icosahedron construction: verified.
- \(I_h\) and \(T_h\) point actions: verified.
- Coulomb Hessian \(I_h/T_h\)-equivariance: verified numerically.
- \(T_h\) projectors and block spectra: verified numerically.
- C60 Coulomb stationarity: fails.
- C60 projected Hessian: diagnostic only, not a constrained-equilibrium Hessian.
- Equality with Q6-64 or archived \(K_0\): not claimed.
