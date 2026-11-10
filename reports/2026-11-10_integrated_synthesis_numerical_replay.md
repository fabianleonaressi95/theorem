# 10 November 2026 — independent numerical replay for the integrated synthesis

**Scope:** direct numerical recomputation of selected finite-seed, quadrature, tensor-variation and Q6 chain identities using the formulas and archived constants recorded in this repository.

**Important evidence boundary:** these are independent numerical calculations, not a run of the repository's full pytest suite or CI. They do not validate a real football scan, material calibration, a continuum limit or a Morandotti surface-homogenisation theorem.

## 1. Hash-checked RGS seed and fourth moment (S.4)

The 64-point, three-coordinate seed reconstructed from the six archived orbit constants has shape \(64\times3\) and coordinate-array SHA-256
\[
\texttt{6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf}.
\]
The raw second moment is \(M^{(2)}=80I_3\), up to floating-point residuals below \(10^{-15}\).

The independently recomputed fourth-moment values are:
\[
\begin{aligned}
c&=67.43619546321251,\\
M^{(4)}_{xxxx}&=195.9872446501132,\\
M^{(4)}_{xxyy}&=70.59686633297464,\\
R_{xxxx}&=-6.321341739524314,\\
R_{xxyy}&=+3.1606708697621286.
\end{aligned}
\]
The induced operator on the Frobenius-orthonormal \(\operatorname{Sym}_0(3)\) basis has eigenvalues
\[
(-9.48201261,-9.48201261,6.32134174,6.32134174,6.32134174),
\]
i.e. \(E_g\) multiplicity 2 and \(T_{2g}\) multiplicity 3. Across all 48 signed coordinate permutations, the maximum fourth-tensor invariance residual is \(2.7919899571868\times10^{-13}\). The residual pair-trace norm is \(1.014858018570358\times10^{-13}\); its Frobenius inner product with the isotropic projection is \(1.1368683772161603\times10^{-12}\).

These decimals are finite-seed numerical values, not exact rational identities.

## 2. Antipodal and Walsh replay (T.069)

For the recovered seed ordering:
- XOR 7 is the coordinate inversion: \(\max_v\|X_{v\oplus7}+X_v\|_\infty=0\).
- XOR 63 is the canonical Q6 graph antipode, not the seed coordinate inversion: the corresponding maximum residual is \(1.4234808254257256\).
- The normalized point-cloud covariance is \(1.25I_3\).
- Pairing by XOR 63 gives within-pair covariance \(0.9780321650557976I_3\) and between-pair covariance \(0.2719678349442023I_3\), summing to \(1.25I_3\).
- Canonical Q6 Walsh energy: even sector \(0.8159035048326073\), odd sector \(2.934096495167398\).

The exact pair-decomposition and Walsh-sign statements remain algebraic identities; these listed seed values are numerical.

## 3. Duffy–Gauss–Jacobi quadrature (T.070)

The Duffy map and Jacobi parameters are recorded in docs/DIRICHLET_DUFFY_JACOBI_QUADRATURE.md. Direct numerical checks give:

| Parameters | \(Z_{\rm quad}/(2A_F)\) | \(B_3(a)\) | max mean error | max covariance error |
|---|---:|---:|---:|---:|
| \((1,1,1)\), order 3 | 0.49999999999999994 | 0.5 | \(1.11\times10^{-16}\) | \(4.16\times10^{-17}\) |
| \((2,3,4)\), order 5 | 0.0002976190476190476 | 0.0002976190476190473 | \(1.67\times10^{-16}\) | \(1.11\times10^{-16}\) |
| \((1.5,2,3.5)\), order 5 | 0.004090615434361711 | 0.004090615434361709 | \(1.67\times10^{-16}\) | \(5.55\times10^{-17}\) |

For the physical triangle of area one, the uniform case gives \(Z_F=A_F=1\). A degree-two weighted polynomial integral at orders 5 and 8 differed by \(3.47\times10^{-18}\). The code separately returns the raw second moment \(M=\mathbb E[\lambda\lambda^T]\) and covariance \(C=M-mm^T\).

## 4. Fourth-moment connection current (S.6)

For the reconstructed residual and the declared test \(Q,\partial Q,\omega\):
- the shifted constitutive operator has minimum eigenvalue approximately \(10^{-8}\) for both \(\beta=+1\) and \(\beta=-1\);
- the current is antisymmetric to machine precision;
- the maximum central-finite-difference discrepancy over the three \(\mathfrak{so}(3)\) generators is \(5.42\times10^{-12}\).

The negative-\(\beta\) check is included because the shift must use \(\lambda_{\min}(\beta A)\), not \(\beta\lambda_{\min}(A)\) for either sign of \(\beta\). The central implementation has been corrected accordingly. No flat-connection constraint or complete TEGR field equation is claimed.

## 5. Maxwell obstruction and candidate response (S.7)

For the declared antisymmetric test field \(F\),
\[
R_{ijkl}F_{ij}F_{kl}=0
\]
numerically, consistent with the exact index-symmetry proof. For the declared STF test \(Q\), \(\operatorname{tr}(R:Q)\) is below \(6.0\times10^{-14}\), and the illustrative electric and magnetic response matrices have eigenvalues \((0.75,1,1.25)\). This checks one candidate input; it is not a physical Maxwell derivation or a fine-structure-constant prediction.

## 6. Algebraic coframe variation (S.8)

For the declared coframe, lapse, \(Q\), residual and coupling, the maximum absolute discrepancy between the analytic coframe derivative and central finite differences is \(2.23\times10^{-10}\). This supports the displayed determinant variation. The action is algebraic in the coframe and does not generate torsion.

## 7. Q6 cubical chain replay (T.071)

For the 64-vertex, 192-edge, 240-square 2-skeleton:
- \(B_1B_2=0\) exactly entrywise;
- \(\operatorname{rank}B_1=63\);
- \(\operatorname{rank}B_2=129\) (also checked by exact rational rank);
- the graph cycle rank is 129 and \(b_1=0\);
- the truncated 2-skeleton has \(b_2=240-129=111\);
- the complement-induced \(J_0,J_1,J_2\) satisfy both chain-map identities and square to the identity.

The full six-cube has 3-cells that kill these 2-dimensional classes; \(b_2=111\) refers only to the truncated 2-skeleton.

## 8. Not executed / still open

- The repository pytest suite and GitHub CI were not run as part of this replay.
- No real 180-facet football-shell coordinates or material scan were numerically audited here.
- No global quadrature convergence, Mosco convergence, curved-surface compactness/liminf/recovery result, or Morandotti surface homogenisation theorem is established.
- The explicit \(A_4\)-intertwiner matrix, connection-compatible bundle map, Wilson-derived order-parameter measure, flat teleparallel connection variation and full coframe equations remain open.
