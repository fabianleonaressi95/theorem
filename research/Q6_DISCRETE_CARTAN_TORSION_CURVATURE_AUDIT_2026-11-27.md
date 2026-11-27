# Discrete Cartan geometry on the I Ching/Kirchhoff Q6 carrier

**Date:** 27 November 2026  
**Classification:** finite spatial construction; gauge covariance numerically audited; continuum and 4D lifts open.

## 1. Combinatorial carrier and provenance

The carrier is the 64 six-bit I Ching hexagrams
\[
\mathcal H=\{0,1\}^6.
\]
The chosen elementary adjacency is a single-line flip (Hamming distance one), giving \(Q_6\): 64 vertices, 192 positively oriented edges, degree six, and 240 coordinate-square plaquettes. The 64-site RGS seed and ordered edge list are reconstructed with the same SHA-256 checks used by the static coframe audit:
- \(X_{\rm Oh}\): \`6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf\`;
- Q6 edge list: \`da7854ca655577b629dc508208918326fde1d50563485f953ea0fdc1b2fb78e8\`.

The exact cubical incidence identities \(\partial_1\partial_2=0\) and \(\partial_2\partial_3=0\), with ranks and cell counts, are independently audited by \`audits/q6_face_cochain_green_kubo.py\` and the existing Q6 tests. The present construction uses the same oriented edge and square conventions.

## 2. Discrete coframe and connection

At each vertex \(g\), reconstruct the archived SPD spatial coframe \(E_g\) from the local Gaussian covariance prescription. For a positively oriented Q6 edge \(e=(g,h)\), define its coframe increment in the source orthonormal frame by
\[
\theta_e=E_g(X_h-X_g)\in\mathbb R^3.
\]
This is a finite edge cochain with a local-frame value. It is not a derivative inferred from an arbitrary smooth interpolation.

The edge connection is the existing shortest radial rotation
\[
U_{gh}=\operatorname{Rot}_{\min}
\left(\frac{X_g}{\|X_g\|},\frac{X_h}{\|X_h\|}\right)\in SO(3).
\]
For the reversed edge:
\[
U_{hg}=U_{gh}^{-1}=U_{gh}^{T},\qquad
\theta_{hg}=-U_{gh}\theta_{gh}.
\]
Thus every edge carries both a frame transport and a coframe displacement.

## 3. Face torsion as a developed closure defect

Take an oriented square \(p=(v_0,v_1,v_2,v_3)\), with \(v_4=v_0\). Let \(U_i=U_{v_i v_{i+1}}\) and let \(\theta_i=\theta_{v_i v_{i+1}}\), using the reversal rule above. Define the accumulated transport
\[
P_0=I,\qquad P_{i+1}=U_iP_i.
\]
Here \(P_i\) maps components at the base vertex \(v_0\) into the frame at \(v_i\). Develop each edge displacement back into the base frame and sum:
\[
\boxed{\mathcal T_p=\sum_{i=0}^{3}P_i^{-1}\theta_i
=\sum_{i=0}^{3}P_i^T\theta_i.}
\]
\(\mathcal T_p\) is the discrete Cartan torsion observable used in this audit: the failure of the transported coframe increments to close around the plaquette. It is a connection-twisted boundary sum, reducing to the ordinary oriented cochain boundary sum when all transports are identity. It is not asserted to be the exact integral of a continuum 2-form until a compatible reconstruction and convergence theorem are supplied.

## 4. Face curvature as holonomy

The same square has ordered holonomy
\[
\boxed{\mathcal H_p=U_3U_2U_1U_0\in SO(3).}
\]
Its rotation angle is
\[
\vartheta_p=\arccos\left(\frac{\operatorname{tr}\mathcal H_p-1}{2}\right).
\]
This measures curvature of the chosen discrete connection. Unlike a teleparallel connection, this connection is not constrained to have trivial plaquette holonomy.

## 5. Local gauge covariance

For arbitrary vertex frames \(G_g\in SO(3)\), the fields transform as
\[
\theta_{gh}'=G_g\theta_{gh},\qquad
U_{gh}'=G_hU_{gh}G_g^{-1}.
\]
Consequently
\[
\mathcal T_p'=G_{v_0}\mathcal T_p,\qquad
\mathcal H_p'=G_{v_0}\mathcal H_pG_{v_0}^{-1}.
\]
The executable audit generates a deterministic independent random \(SO(3)\) frame at each of the 64 vertices and checks both covariance laws on all 240 faces.

## 6. Numerical results

Reproduced by \`scripts/audit_q6_discrete_cartan.py\`:
- 64 hexagram states, 192 oriented-positive Q6 edges, 240 square faces;
- maximum edge-link orthogonality residual: \(2.09\times10^{-15}\);
- maximum edge-link determinant residual: \(1.44\times10^{-15}\);
- maximum face-torsion gauge covariance residual: \(5.76\times10^{-15}\);
- maximum face-holonomy conjugation residual: \(2.17\times10^{-15}\);
- mean face torsion norm: \(1.85258\), RMS \(2.36480\), maximum \(5.95771\);
- mean curvature rotation angle: \(0.66925\) rad, RMS \(1.00629\), maximum \(3.02091\);
- 236 of 240 faces have both torsion norm and curvature angle above \(10^{-10}\).

These are numerical checks of a finite, explicitly specified construction. The nonzero values are not fitted to force simultaneous curvature and torsion; they arise from the archived coframe increments and the previously used Q6 link rotations.

## 7. What this does and does not establish

**Established by this implementation and tests**
1. A reproducible finite edge coframe on the 64-state Q6 carrier.
2. An \(SO(3)\) connection on all 192 edges with inverse links on reversed edges.
3. A connection-developed torsion vector and an ordered curvature holonomy on all 240 faces.
4. Local \(SO(3)\) gauge covariance of both face observables to numerical precision.
5. Simultaneously nonzero discrete torsion and curvature on 236 faces for this chosen data.

**Not established**
- A Lorentzian \(SO(1,3)\) or \(\mathrm{Spin}(1,3)\) connection;
- a 4D Cartan field or a physical time leg selected from the internal 3-space;
- a teleparallel representative with exactly trivial plaquette holonomy;
- the non-Abelian cube Bianchi identity in this implementation;
- derivation of the edge connection from a common variational action;
- a discrete-to-continuum Cartan limit, Mosco convergence, or field equations.

The construction therefore resolves the immediate finite-dimensional issue—curvature and torsion can be represented together on the Q6 carrier—without claiming the still-open spacetime dynamics.

## 8. Reproduction

From the repository root:
\`\`\`bash
python -m unittest discover -s tests -p "test_q6_discrete_cartan.py" -v
python scripts/audit_q6_discrete_cartan.py
\`\`\`


## 9. CI reproduction

GitHub Actions workflow run #43 completed successfully, including the existing exact Q6 incidence/Hodge and Anti-Twin audits, the static coframe reference audit, the four discrete-Cartan unit tests, and the discrete-Cartan numerical report.

[Workflow run #43](https://github.com/fabianleonaressi95/theorem/actions/runs/46059768375)
