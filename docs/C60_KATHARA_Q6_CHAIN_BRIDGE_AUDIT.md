# C60–Kathara–Q6 bridge: cellular obstruction and exact test contract

**Status:** exact C60 homology audit implemented; cross-complex chain map remains open because the canonical Kathara and Q6 boundary matrices and the recorded R-matrices have not yet been imported into this audit.

## 1. C60 is a sphere, not merely a graph

The fullerene cellulation has
\[
(C_0,C_1,C_2)=(60,90,32),\qquad \chi=60-90+32=2.
\]
Its exact rational boundary ranks are
\[
\operatorname{rank}_{\mathbb Q} B_1=59,\qquad
\operatorname{rank}_{\mathbb Q} B_2=31,
\]
hence
\[
(\beta_0,\beta_1,\beta_2)=(1,0,1).
\]
The graph 1-skeleton by itself has cycle rank \(90-60+1=31\). Attaching the 32 spherical face cells kills those 31 independent graph cycles, leaving \(H_1(S^2)=0\). Confusing the graph cycle rank with the first homology of the closed fullerene surface would therefore be a category error.

The new script scripts/audit_c60_q6_bridge.py computes these ranks over \(\mathbb Q\) using exact fraction arithmetic and checks \(B_1B_2=0\).

## 2. Dimension comparison is not a map

The currently recorded dimensions are:

| Complex | \(C_0\) | \(C_1\) | \(C_2\) | Euler characteristic |
|---|---:|---:|---:|---:|
| C60 fullerene sphere | 60 | 90 | 32 | 2 |
| Kathara (recorded) | 12 | 21 | 10 | 1 |
| Q6 (recorded) | 64 | 192 | 240 | 112 |

The Kathara/Q6 values are the dimensions recorded in the existing project notes (including \(R_0:64\times12\), \(R_1:192\times21\), \(R_2:240\times10\)); this audit does not independently certify the source arrays or orientations.

There can be no cellular isomorphism between these three complexes because their chain-group dimensions and Euler characteristics differ. A non-invertible chain map may still exist. Euler characteristic alone does not obstruct a general chain map, nor does it establish one.

The Q6 1-skeleton cycle rank \(192-64+1=129\) is a graph invariant. It must **not** be reported as \(\beta_1\) of the Q6 2-complex until the 240 plaquette boundary columns are supplied and the rank of \(B_2^{Q6}\) is calculated.

## 3. Required commuting diagram

Let \(K\) be the canonical Kathara complex. The recorded maps have types
\[
R_0:C_0(K)\to C_0(Q6),\quad
R_1:C_1(K)\to C_1(Q6),\quad
R_2:C_2(K)\to C_2(Q6).
\]
Their claimed chain-map conditions are
\[
B_1^{Q6}R_1=R_0B_1^K,\qquad
B_2^{Q6}R_2=R_1B_2^K.
\]
These must be rechecked against the actual integer arrays.

A fullerene-to-Kathara map would require new integer matrices
\[
P_0\in\mathbb Z^{12\times60},\quad
P_1\in\mathbb Z^{21\times90},\quad
P_2\in\mathbb Z^{10\times32}
\]
satisfying
\[
B_1^K P_1=P_0B_1^{C60},\qquad
B_2^K P_2=P_1B_2^{C60}.
\]
Only after these equations pass can the composed maps \(R_iP_i:C_i(C60)\to C_i(Q6)\) be asserted to be chain maps.

For the SW move, let \(S_i:C_i(C60)\to C_i(C60')\) be the already constructed local chain correspondence. An intertwining claim requires a separately defined post-SW target map \(P_i'\) and an explicit Q6/Kathara action \(A_i\), with a commuting condition
\[
P_i'S_i=A_iP_i.
\]
No \(A_i\) is currently defined. The equation is a research target, not a result.

## 4. Immediate blockers and exact next data

To complete the numerical bridge without inventing correspondences, the repository must expose:

1. \(B_1^K,B_2^K\) with canonical cell order and orientation;
2. \(B_1^{Q6},B_2^{Q6}\), especially the exact 240 plaquette boundaries;
3. the actual integer arrays \(R_0,R_1,R_2\), not only their dimensions/ranks;
4. the canonical incidence/assignment defining what each Kathara cell represents relative to C60.

The audit should then check every chain identity with integer arithmetic, report ranks and homology on both sides, and solve for candidate \(P_i\) only under explicit combinatorial constraints. A least-squares fit or visual alignment is not an acceptable substitute.

## 5. Evidence classification

| Statement | Status |
|---|---|
| C60 cellulation has (60,90,32), chi=2 | Exact |
| C60 cellular homology is (1,0,1) | Exact rational computation |
| C60 graph 1-skeleton cycle rank is 31 | Exact |
| Q6 graph 1-skeleton cycle rank is 129 (using recorded 64,192) | Exact conditional on recorded graph counts |
| Q6 2-complex homology | Open until B2_Q6 is supplied |
| Kathara/Q6 chain-map identities | Recorded claim; re-audit requires canonical arrays |
| C60/Kathara chain map P_i | Open |
| SW/Q6 intertwiner | Open; no Q6/Kathara action A_i defined |

## Reproduction

\`\`\`bash
python scripts/audit_c60_q6_bridge.py --out c60_q6_bridge_audit.json
pytest -q tests/test_c60_q6_bridge.py
\`\`\`
