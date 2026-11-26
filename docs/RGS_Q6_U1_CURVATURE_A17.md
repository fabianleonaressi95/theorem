# A17 — Induced U(1) curvature on the RGS/Q6 transverse bundle

**Classification:** numerical verification on the archived finite Q6 graph.  
**Input:** `data/psu_fibre_connection_matrices.npz` (A13 fibre archive).  
**Scope:** discrete Euclidean bundle only; no continuum curvature 2-form or spacetime claim.

## 1. Local reduction

For each vertex, set (n_g=X_g/\|X_g\|) and choose an oriented orthonormal frame
(E_g=(u_g,v_g,n_g)\in SO(3)). The choice of (u_g,v_g) is a local gauge choice,
not additional geometry. For each oriented edge define

\[
A_{gh}=\left.E_h^T R_{gh}E_g\right|_{n_g^\perp}\in SO(2).
\]

A change of local transverse frame (E_g\mapsto E_g\,\mathrm{diag}(G_g,1)),
(G_g\in SO(2)), gives

\[
A_{gh}\mapsto G_h^T A_{gh}G_g.
\]

Since (SO(2)) is abelian, the oriented plaquette holonomy has a gauge-invariant
angle (Theta_p\in(-\pi,\pi]):

\[
\Theta_p=\operatorname{Arg}\!\left(\prod_{(g,h)\in\partial p} A_{gh}\right).
\]

This is the induced discrete (SO(2)\cong U(1)) connection/curvature on the
transverse rank-2 bundle.

## 2. Spin lift

The (SU(2)) plaquette holonomy commutes with (sigma(n_g)). Its two eigenphases
are the spinorial half-angle lift of the corresponding (SO(3)) rotation, with
the expected central-sign ambiguity (U\sim -U). The comparison is made after
folding the (SU(2)\) phase through the double cover; it is not a second
independent curvature.

## 3. Numerical result

Run:

```bash
python scripts/audit_rgs_q6_u1_curvature.py \
  data/psu_fibre_connection_matrices.npz \
  --output reports/RGS_A17_U1_CURVATURE_2026-11-26.json
```

The archived run checks all 240 elementary square plaquettes and returns **PASS**.

| Check | Maximum residual |
|---|---:|
| Edge (SO(2)\) orthogonality | (1.0553\times10^{-15}) |
| Edge off-block leakage | (9.1399\times10^{-16}) |
| Radial normal transport | (4.0887\times10^{-16}) |
| Plaquette holonomy fixes (n_g) | (1.4542\times10^{-15}) |
| (SU(2)\) plaquette commutator with (sigma(n_g)) | (1.8734\times10^{-15}) |
| Edge product vs. plaquette holonomy angle | (6.6613\times10^{-16}) |
| Local (SO(2)\) gauge covariance | (4.2999\times10^{-16}) |
| (SO(3)\)/(SU(2)\) double-cover angle | (3.6501\times10^{-8}) rad |

The 240 principal curvature angles have minimum (-3.0209126547), maximum
(+3.0209126547), mean (0), and RMS (1.00629292795) rad. Their sum is zero.
Thus the curvature is **not** zero plaquette by plaquette; the vanishing sum is
a global cancellation in this finite set.

## 4. Convention correction to A16 audit

The plaquette transport convention is column-vector transport:
(R_{gh}n_g=n_h). Along (g\to h\to k\to l\to g), the composed holonomy is
(H=R_{lg}R_{kl}R_{hk}R_{gh}), i.e. each next edge acts on the left.
The A16 audit script is corrected in this PR to use this order for both (SO(3)\)
and (SU(2)\) products. The new A17 script independently checks the reduced
(SO(2)\) edge product against the full plaquette holonomy.

## 5. Interpretation and limits

**Established numerically:** the archived finite Q6 link data carry a radial
parallel line and a transverse rank-2 bundle with an induced abelian plaquette
curvature; the spin lift is consistent with the (SU(2)\to SO(3)\) double cover.

**Not established:** a continuum principal bundle, a smooth curvature 2-form,
a continuum limit, identification with the A14 (S^{188}(\sqrt{240})\)
Levi-Civita connection, a 3+1 tetrad, or Lorentzian spacetime.
