# Q6 carrier-derived coframe from the archived PSU connection — 2026-11-27

## Purpose and status

This is the full-Q6 extension of the four-point carrier-derived construction. It uses the original 64-site embedding, the 192 archived oriented PSU links, and the 240 coordinate-square faces. Unlike the tetrahedral fixture, it uses the actual Q6 edge and square incidence.

**Classification:** finite construction and executable numerical audit. The script must be run against the two binary NPZ archives before any numerical result is claimed. The square path sum is a gauge-covariant discrete candidate; no continuum Cartan theorem or torsion Bianchi identity is asserted.

## 1. Indexing and archive alignment

The script reads `Q6_states`, `X_Oh_reconstructed`, `edges`, `normals`, and `R_SO3` from the existing archives. It verifies:

- the 64 state rows are exactly the binary labels (g=0,ldots,63);
- every stored edge ((g,h,d)) satisfies (h=g\oplus 2^d);
- the graph has 192 distinct undirected edges and degree six at every vertex;
- archived normals agree with (X_g/\|X_g\|);
- the archived (SO(3)) links agree with the normal-based minimal-rotation formula.

The script does **not** use (Q_{\mathrm{tangent}}) as an edge list: its 192 rows are 64 Cartesian displacement triples, not graph edges.

## 2. Local connection and coframe

For a deterministic oriented radial frame (F_g=(u_g,v_g,n_g)\in SO(3)), define
\[
R^{\mathrm{loc}}_{gh}=F_h^T R^{\mathrm{PSU}}_{gh}F_g.
\]
This is the archived connection expressed in the local radial frames. It fixes the radial basis vector (e_3), as checked numerically.

For the carrier chord (Delta X_{gh}=X_h-X_g), set
\[
\boxed{
E_{gh}=\frac12\left(F_g^T\Delta X_{gh}
+(R^{\mathrm{loc}}_{gh})^{-1}F_h^T\Delta X_{gh}\right).
}
\]
The direct reverse-orientation formula is checked on all 192 edges:
\[
E_{hg}=-R^{\mathrm{loc}}_{gh}E_{gh}.
\]
The construction also obeys (\|E_{gh}\|\leq\|X_h-X_g\|).

## 3. Square path-sum candidate

For each ordered coordinate square (v_0\to v_1\to v_2\to v_3\to v_0), define
\[
\boxed{
\mathcal T_{v_0v_1v_2v_3}
=E_{v_0v_1}
+(R_{01})^{-1}E_{v_1v_2}
+(R_{12}R_{01})^{-1}E_{v_2v_3}
+(R_{30}R_{23}R_{12}R_{01})^{-1}E_{v_3v_0}.
}
\]
Here (R_{ab}=R^{\mathrm{loc}}_{ab}), and every summand is transported to the fibre at (v_0). Under independent vertex-frame rotations (S_g\in SO(3)),
\[
R'_{gh}=S_hR_{gh}S_g^{-1},\qquad E'_{gh}=S_gE_{gh},
\]
so (\mathcal T'_{v_0v_1v_2v_3}=S_{v_0}\mathcal T_{v_0v_1v_2v_3}).

The 240 squares are generated from the six bit directions, fixing the other four bits. This is the coordinate-square 2-skeleton of Q6, not a guessed face ordering.

## 4. Numerical audit

Run from the repository root:

```bash
python scripts/audit_q6_archived_carrier_coframe.py
```

The script writes `audits/Q6_ARCHIVED_CARRIER_COFRAME_2026-11-27.json`. It checks all 192 edge coframes, all 240 square path sums, direct edge reversal, radial-axis preservation, local (SO(3)) integrity, normal/embedding and archived-link formula fits, 1,000 independent local-frame gauge changes, and 100 common ambient rotations with the frames transported along with the carrier.

No numerical values are pre-filled in this document. The report is created only by executing the script against the actual NPZ files.

## 5. Evidence boundary and next theorem gate

A nonzero square path sum is a finite geometric diagnostic, not automatically continuum Cartan torsion. To identify it with (D_\omega e), one must define a refinement family, a cochain integration map, and prove convergence with compatible transport and incidence conventions. A torsion Bianchi identity requires a separately defined compatible discrete differential and curvature action. deWit–Nye/Burgers interpretation additionally requires material/spatial conventions and a continuum limit.

**Not claimed:** a continuum Cartan limit, a torsion Bianchi identity, deWit–Nye dislocation density, a Burgers vector, or a spacetime tetrad.
