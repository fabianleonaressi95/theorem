# T143 follow-up — antipodal connection and holonomy audit

**Type:** reproducible numerical audit of the reconstructed geometric connection.  
**Status:** SO(3) and canonical Spin(3) checks pass for the connection reconstructed from the archived embedding. Direct replay of the archived U_SU2 binary array remains pending.

## 1. Geometric antipode

The source archive supplies X_Oh_reconstructed and Q6_adjacency. Recompute
\[
p(g)=\arg\min_h\|X_h+X_g\|.
\]
It agrees exactly with p(g)=g xor 7; the antipodal residual is zero, and XOR 7 is an exact Q6 adjacency automorphism.

## 2. Link transport

Following build_connection.py, normalize n_g=X_g/||X_g|| and let R_(g->h) be the minimal rotation carrying n_g to n_h. The reconstructed directed transports satisfy
\[
R_{p(g)\to p(h)}=R_{g\to h}
\]
on every directed Q6 edge, with maximum Frobenius residual zero. This follows structurally because the minimal-rotation formula depends on n_g dot n_h and n_g cross n_h, both unchanged when both vectors change sign.

Canonical quaternion lifts in Spin(3) satisfy the same relation, projectively. These are lifts of the reconstructed SO(3) links, not the stored U_SU2 matrices.

## 3. Plaquette holonomy

For each of the 240 oriented square faces, form the ordered SO(3) product and its quaternion lift. The antipodal image loop has exactly the same ordered holonomy in the global Cartesian trivialization. The reconstructed angle statistics reproduce the archived connection report:
\[
\bar\theta=0.6692474402132716,\quad
\theta_{RMS}=1.0062929279515105,\quad
\theta_{max}=3.020912654710446.
\]
Antipodal SO(3), Spin(3) (projectively), and angle residuals are zero in this reconstruction.

## 4. Consequence for a global complex phase

The reconstructed plaquette holonomies are non-Abelian: 22,248 of the 28,680 unordered pairs fail to commute modulo the centre of Spin(3). Thus the full fundamental SU(2) holonomy family has no common invariant complex line. A single global U(1) phase line cannot be selected as a common eigenline of all these holonomies.

This obstructs interpreting the 29 numbers as phases of one globally parallel line selected by this connection. It does not rule out a different construction, such as a chosen reduction of structure group, a gauge-covariant section with transition functions, or a path-dependent phase. Each requires additional geometric data.

## 5. Open checks

1. Recover the original fibre archive and compare stored R_SO3 and U_SU2 edge-by-edge, including orientation and the SU(2) sign ambiguity.
2. Specify the representation/associated bundle mapping the connection to the proposed complex coordinates.
3. Determine whether the 29-angle family is gauge freedom, a section constrained by transport, or an ansatz incompatible with the non-Abelian holonomy.
4. Do not claim that the connection uniquely fixes the 29 angles.

## 6. Reproduction

\`\`\`bash
python scripts/audit_t143_antipodal_connection.py --archive RGS_PSU_all_matrices.npz --out T143_antipodal_connection_audit.json
python -m unittest tests.test_t143_antipodal_connection
\`\`\`
