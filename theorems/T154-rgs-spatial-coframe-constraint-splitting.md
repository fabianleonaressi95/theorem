# T154 — RGS spatial coframe and labelled constraint splitting

**Date:** 26 November 2026  
**Classification:** exact finite algebra under explicit seed hypotheses; numerical verification on the archived 64-site seed; discrete covariant torsion remains a finite-graph candidate.  
**Related records:** A13 archived Q6 fibre connection and edge coframe; A14 labelled constraint Jacobian; Q6 cellular incidence; indexing audit PR #490.  
**Scope:** spatial \(SO(3)\) vector channel plus radial scalar channel. This is not a Lorentzian \(3+1\) tetrad.

## 1. Labelled constraint Jacobian

Let \(X=(X_1,\ldots,X_{64})\in(\mathbb R^3)^{64}\), \(X_i=(x_i,y_i,z_i)\), with
\[
\sum_{i=1}^{64}X_i=0,\qquad \sum_{i=1}^{64}\|X_i\|^2=240.
\]
Let \(X_{\rm flat}\in\mathbb R^{192}\) be the site-major flattening. Consider
\[
F_x=\sum_i x_i,\quad F_y=\sum_i y_i,\quad F_z=\sum_i z_i,\quad
F_r=\frac12\left(\sum_i\|X_i\|^2-240\right).
\]
The Jacobian \(J:\mathbb R^{192}\to\mathbb R^4\) has three uniform Cartesian translation rows and the radial row \(J_r=X_{\rm flat}^T\). The admissible variations satisfy \(J\,\delta X=0\).

## 2. Exact finite theorem

**Theorem 154.** Under the centred and fixed-scale hypotheses,
\[
JJ^T=\operatorname{diag}(64,64,64,240).
\]
Hence \(\operatorname{rank}J=4\), \(\dim\ker J=188\), and the labelled normal frame
\[
N_{\rm lab}=J^T\operatorname{diag}\left(\frac18,\frac18,\frac18,\frac1{\sqrt{240}}\right)
\]
is orthonormal. Its first three columns are the uniform Cartesian translation normals; its fourth is \(X_{\rm flat}/\sqrt{240}\), the fixed-radius normal. Therefore
\[
\mathbb R^{192}=\ker J\oplus N_{\rm tr}\oplus N_{\rm rad},
\quad \dim N_{\rm tr}=3,\quad\dim N_{\rm rad}=1.
\]

*Proof.* The first three rows have squared norm 64 and are mutually orthogonal. Their inner products with the radial row are the three coordinate sums, hence vanish. The radial row has squared norm 240. Thus the displayed Gram matrix follows. The rank, normalized normal frame and orthogonal decomposition follow immediately. \(\square\)

The \(3+1\) here is a decomposition of the **constraint-normal space**: three translations and one radial scale constraint. It does not identify a physical time direction.

## 3. The archived edge feature as an \(SO(3)\)-module

For an oriented Q6 edge \(g\to h\), put \(r_g=\|X_g\|\) and define the raw integrated feature
\[
\widetilde e_{gh}=(X_h-X_g,\ r_h-r_g)\in\mathbb R^3\oplus\mathbb R,
\qquad e_{gh}=\frac{\widetilde e_{gh}}{\|\widetilde e_{gh}\|}.
\]
The A13 archive stores the normalized \(192\times4\) feature; the raw increments are reconstructed from the same coordinates and edge list.

The natural spatial action is
\[
\rho(R)=\begin{pmatrix}R&0\\0&1\end{pmatrix},\qquad R\in SO(3),
\]
so
\[
\mathbb R^4\big|_{SO(3)}
\cong \mathbb R^3_{\rm standard}\oplus\mathbb R_{\rm trivial}.
\]
The first three components transform as a spatial vector; the fourth is a radial scalar singlet.

The archived links have shapes \(R_{gh}\in SO(3)\) and \(U_{gh}\in SU(2)\), 192 links each. The numerical A13/A14 audit reports a direct quaternion-to-\(SO(3)\) lift residual \(9.42\times10^{-16}\); the transpose convention fails. Thus the archived lift fixes the active-rotation convention on the spatial block. The radial singlet is transported trivially by \(\rho(R_{gh})\).

## 4. Numerical verification on the archived seed

The following values are reused from the existing A14 Jacobian report, A13/A14 cross-check, and discrete-torsion report. They are not recomputed by this theorem-record PR.

| Check | Reported value |
|---|---:|
| \(X\), \(J\), \(Q\) shapes | \(64\times3,\ 4\times192,\ 192\times188\) |
| \(\operatorname{rank}J\) | 4 |
| \(\|JQ\|_F\) | \(1.2385\times10^{-14}\) |
| \(\|Q^TQ-I\|_F\) | \(1.3145\times10^{-14}\) |
| labelled-normal orthonormality residual | \(2.4533\times10^{-18}\) |
| projector-complement residual | \(8.98\times10^{-15}\) |
| radial-row alignment | \(0.9999999999999998\) |
| A13/A14 tangent-projector difference | 0 |
| A13/SEA edge-list identity | true |
| \(SO(3)\) orthogonality residual | \(1.1716\times10^{-15}\) |
| \(SU(2)\) unitarity residual | \(3.2096\times10^{-16}\) |
| direct \(SU(2)\to SO(3)\) lift residual | \(9.4206\times10^{-16}\) |

The reported centroid residual is \(2.22\times10^{-16}\) and the squared radius is \(240.00000000000006\). The exact theorem is stated for the ideal centred, fixed-scale hypotheses; the table records the floating-point validation.

## 5. Discrete covariant torsion: correct cochain and limits

For a square face \(p=(v_0,v_1,v_2,v_3,v_0)\), use the raw integrated edge cochain, not its normalized version, and define
\[
T_p=\sum_{k=0}^{3}\mathcal P_{v_0\leftarrow v_k}\,
\widetilde e_{v_kv_{k+1}},\qquad
\mathcal P=\operatorname{diag}(P,1),
\]
where \(P\) is the archived spatial parallel transport along the chosen face path.

The raw feature is the ordinary vertex difference of \((X,r)\), so its plain exterior derivative around a closed face vanishes. The discrete-torsion report gives
\[
\|d\widetilde e\|_F=2.85\times10^{-15}.
\]
The nontrivial archived connection gives a nonzero transported face sum: RMS norm \(2.3537\), minimum \(0.0553\), maximum \(7.7403\). The flat-connection control is \(1.93\times10^{-15}\), and the reported gauge-covariance residual is \(2.95\times10^{-14}\).

The normalized feature is not an integrated 1-cochain: its reported boundary-closure norm is \(13.1469\). It must not be inserted into the cochain torsion formula. The radial fourth component is a singlet and its reported torsion RMS is zero. This is a finite spatial-connection diagnostic, not a continuum Cartan torsion theorem.

## 6. Non-identifications and open gates

1. **No spacetime tetrad:** neither edge feature supplies a coordinate-dependent field \(e^a{}_\mu(x)\). The separate static lift \(\operatorname{diag}(1,E_i)\) does not provide \(\partial_\mu e\).
2. **No Levi-Civita/TEGR certification:** a coordinate atlas, a differentiable or refinement-compatible coframe field, and a connection with a stated transformation law are still required.
3. **No physical uniqueness of the connection:** the existing audit reports \(K_{\rm geometry}=D_{\rm tangent}^TD_{\rm tangent}\), but
   \[
   \frac{\|K_{\rm geometry}-K_0\|_F}{\|K_0\|_F}=0.84497.
   \]
   The archived geometric connection is therefore not shown to reproduce or factorize \(K_0\).
4. **No continuum result:** one finite Q6 complex does not establish a refinement-compatible Bianchi identity, Mosco convergence, a continuum torsion tensor, or a gravitational field equation.

## 7. Provenance

Numerical evidence is reused from the A13 fibre-connection and SEA payloads, the A14 labelled Jacobian matrices/report, the RGS QAT generalization audit, and the discrete-torsion report. The A13/A14 binary bundles are not copied into this theorem repository by this record. Values above are provenance-preserving reuse, not a fresh binary recomputation.
