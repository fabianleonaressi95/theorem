# Flat teleparallel branch on the I Ching/Kirchhoff Q6 carrier

**Date:** 27 November 2026  
**Classification:** finite spatial flat-connection representative; physical selection and 4D lift open.

## 1. Separate the two connections

The previously audited curved spatial connection has nontrivial face holonomy. It is not teleparallel and is retained unchanged.

On the same 64-vertex, 192-edge, 240-square carrier, choose a second connection in one global trivialization:
\[
U^{\mathrm W}_{gh}=I_3.
\]
Under local vertex-frame changes \(G_g\in SO(3)\), it transforms as
\[
(U^{\mathrm W}_{gh})'=G_hU^{\mathrm W}_{gh}G_g^{-1}.
\]
It is therefore a pure-gauge connection. Its holonomy telescopes to identity on every closed face.

## 2. Same coframe, different connection

Keep the reconstructed RGS site coframes \(E_g\) and edge increments
\[
\theta_{gh}=E_g(X_h-X_g),\qquad \theta_{hg}=-\theta_{gh}
\]
in the chosen global trivialization. For each oriented square \(p=(v_0,v_1,v_2,v_3)\), define
\[
\mathcal T^{\mathrm W}_p=\sum_{i=0}^3(P_i^{\mathrm W})^{-1}\theta_i,\qquad
P_0^{\mathrm W}=I,\quad P_{i+1}^{\mathrm W}=U_i^{\mathrm W}P_i^{\mathrm W}.
\]
In the Weitzenboeck gauge this is the oriented sum of the four edge increments. Meanwhile
\[
\mathcal H^{\mathrm W}_p=I_3
\]
on all 240 faces. A flat connection does not force the coframe closure defect to vanish.

## 3. Interpretation

The same coframe now has two connection choices:
- curved branch: nontrivial face holonomy and the previously audited developed torsion;
- flat branch: identity face holonomy and its own developed coframe closure defect.

This is the finite discrete separation needed before attempting a continuum contorsion identity. It does not yet prove the continuum formula \(\omega=\omega_{\rm LC}+K\), TEGR dynamical equivalence, or that the flat connection is selected by an RGS/PSU action.

## 4. Tests and limits

The executable audit applies independent deterministic \(SO(3)\) frame changes at all 64 vertices and checks covariance of face torsion and holonomy. Tests check all 240 face holonomies are identity to numerical precision and that the closure defect is nonzero on at least one face.

Reproduce:
\`\`\`bash
python -m unittest tests.test_q6_teleparallel_branch -v
python scripts/audit_q6_teleparallel_branch.py
\`\`\`

**Still open:** variational selection of the flat connection; a discrete contorsion law with a continuum limit; Lorentzian \(SO(1,3)\)/Spin(1,3) lift and 4D coframe; TEGR or Poincare-gauge action and field equations; discrete Bianchi identities and refinement/Mosco convergence.
