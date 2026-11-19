# T143 follow-up — antipodal connection and holonomy

**Evidence tracks:** this page records the reconstructed-embedding audit.
The exact conditional theorem is stated separately in
[T143-A — Antipodal equivariance of the minimal SO(3)/SU(2) connection](../theorems/T143A-antipodal-equivariance-minimal-so3-su2-connection.md).
The direct replay of the original archived edge matrices is documented in
[T143 original-archive replay](T143-original-archived-connection-replay.md).

## 1. Geometric antipode

The source archive supplies \`X_Oh_reconstructed\` and \`Q6_adjacency\`.
Recompute
\[
p(g)=\arg\min_h\|X_h+X_g\|.
\]
It agrees exactly with \(p(g)=g\oplus7\); the antipodal residual is zero,
and XOR 7 is an exact Q6 adjacency automorphism.

## 2. Reconstructed link transport

Normalize \(n_g=X_g/\|X_g\|\). The minimal rotation from \(n_g\) to
\(n_h\) is
\[
R_{gh}=I+[v_{gh}]_\times+
\frac{[v_{gh}]_\times^2}{1+c_{gh}},
\qquad c_{gh}=n_g\cdot n_h,\quad v_{gh}=n_g\times n_h.
\]
The reconstructed directed transports satisfy
\(R_{p(g)p(h)}=R_{gh}\) on every directed Q6 edge, with maximum
Frobenius residual zero. The structural reason is that both \(c\) and
\(v\) are invariant under simultaneous antipodal reversal.

For the canonical spin lift use
\[
U_{gh}=\sqrt{\frac{1+c_{gh}}2}\,I_2
-\frac{i}{\sqrt{2(1+c_{gh})}}(v_{gh}\cdot\sigma),
\]
with convention
\(U_{gh}(x\cdot\sigma)U_{gh}^{\dagger}=(R_{gh}x)\cdot\sigma\).
With this fixed formula the SU(2) equality is direct. Arbitrary
independent signs on edge lifts would require an additional compatibility
condition. The exact statement is T143-A.

## 3. Reconstructed plaquette holonomy

For each of the 240 oriented square faces, form the ordered SO(3)
product and its canonical spin lift. The antipodal image loop has the
same ordered holonomy in the global Cartesian trivialization. The
reconstructed angle statistics are
\[
\bar\theta=0.6692474402132716,\quad
\theta_{\rm RMS}=1.0062929279515105,\quad
\theta_{\max}=3.020912654710446.
\]
These statistics belong to the reconstructed connection. They must not
be silently identified with measurements on the original stored
\`U_SU2\` array.

## 4. Consequence for a global complex phase

The reconstructed plaquette holonomies are non-Abelian: 22,248 of the
28,680 unordered pairs fail to commute modulo the centre of Spin(3).
Thus the full fundamental SU(2) holonomy family has no common invariant
complex line. A single global U(1) phase line cannot be selected as a
common eigenline of all these holonomies.

This obstructs interpreting the 29 numbers as phases of one globally
parallel line selected by this connection. It does not rule out a
different construction, such as a chosen reduction of structure group,
a gauge-covariant section with transition functions, or a path-dependent
phase. Each requires additional geometric data.

## 5. Anti-Twin quotient and scope

For Q6, \(p(g)=g\oplus7\) has 32 vertex orbits. Under the hypotheses of
T143-A, the canonical SO(3) and SU(2) link transports descend to the
quotient graph. This is a discrete graph quotient; no manifold,
flatness, or continuum assertion follows.

The theorem concerns the connection. Commutation of a separately
assembled operator \(K\) with the Anti-Twin permutation \(P\), and
therefore a \(P=\pm1\) spectral decomposition, requires a separate
operator-level proof.

## 6. Remaining archive/provenance checks

1. Compare original stored \(R_{\rm SO(3)}\) and \(U_{\rm SU(2)}\)
   directly with the normal-based formulae, not only with their
   antipodal images.
2. Preserve the direct replay JSON and its tolerances.
3. Verify the source format and ordering of the 240 oriented square
   cycles before claiming an original-archive plaquette replay.
4. Recover or document the generator specification establishing that
   the original stored matrices were constructed by the formulae in
   T143-A.
5. Specify the representation/associated bundle mapping the connection
   to the proposed complex coordinates; do not infer that the 29-angle
   family is fixed by the connection.

## 7. Reproduction

\`\`\`bash
python scripts/audit_t143_antipodal_connection.py --archive RGS_PSU_all_matrices.npz --out T143_antipodal_connection_audit.json
python -m unittest tests.test_t143_antipodal_connection

python scripts/audit_t143_original_archived_connection.py \\
  --fibre psu_fibre_connection_matrices.npz \\
  --embedding RGS_PSU_all_matrices.npz \\
  --out T143_original_connection_antipodal_replay.json
\`\`\`

The direct-replay script reports link-level residuals and can compare
plaquettes only when supplied with an independently verified ordered
\`squares\` array.
