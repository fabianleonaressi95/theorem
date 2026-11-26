# T126 — Exact Burgers conservation under a local equal-vector reconnection

**Classification:** PROVED combinatorial theorem for the stated local graph rewrite; NUMERICAL/COMPUTATIONAL IMPLEMENTATION PENDING CI for the source implementation; MODEL-DEPENDENT as a physical dislocation event; OPEN for unequal-vector reactions, event energetics, trigger criteria and Frank–Read source regeneration.

## 1. Oriented Burgers chains

Let \(G=(V,E)\) be a finite oriented graph and let \(\Lambda_B\subset\mathbb R^m\) be an additive Burgers lattice. For an oriented edge \(e=(u,v)\), use
\[
\partial_1 e=v-u.
\]
An edge carrying Burgers vector \(B\in\Lambda_B\) contributes \(B e\) to the vector-valued 1-chain. For a finite labelled edge family \(\mathcal C\), its vertex boundary is
\[
\partial_1\mathcal C
=\sum_{e=(u,v)\in\mathcal C} B_e(v-u)
\in C_0(V;\Lambda_B).
\]
At a vertex, this is the signed Burgers flux: incoming labels contribute positively and outgoing labels negatively under this convention. A conservative junction has zero net boundary coefficient.

## 2. Local head-exchange rule

Take four pairwise distinct vertices \(a,b,c,d\) and two disjoint oriented strands
\[
e_1=(a,b;B_1),\qquad e_2=(c,d;B_2).
\]
The proposed local head exchange is
\[
\mathscr R(e_1,e_2)
=\big((a,d;B_1),(c,b;B_2)\big).
\tag{126.1}
\]
This is a valid boundary-preserving reconnection precisely when \(B_1=B_2\).

**Theorem 126.** If \(B_1=B_2=B\), the local head exchange (126.1) preserves the complete vertex-valued Burgers boundary:
\[
\boxed{
\partial_1\big(B(a\!\to\! b)+B(c\!\to\! d)\big)
=
\partial_1\big(B(a\!\to\! d)+B(c\!\to\! b)\big).
}
\tag{126.2}
\]
Equivalently, the difference between the post-event and pre-event 1-chains is a 1-cycle. If \(B_1\ne B_2\), the same head exchange changes the boundary by
\[
(B_1-B_2)(d-b),
\tag{126.3}
\]
which is nonzero for distinct \(b,d\) and unequal vectors. Therefore this particular two-strand head exchange is rejected unless the Burgers vectors agree.

**Proof.** With \(\partial_1(u\to v)=v-u\), the pre-event boundary is
\[
B_1(b-a)+B_2(d-c),
\]
and the post-event boundary is
\[
B_1(d-a)+B_2(b-c).
\]
Their difference is
\[
(B_1-B_2)(d-b).
\]
For \(B_1=B_2\) it vanishes identically, proving (126.2). For \(b\ne d\) and \(B_1\ne B_2\), the vector-valued 0-chain difference is nonzero. \(\square\)

The equality is stronger than conservation of the total Burgers vector: it preserves the coefficient at every vertex, including the boundary ports of the local patch.

## 3. Junction conservation for general reactions

For a declared junction with incoming Burgers vectors \(B_i^{\rm in}\) and outgoing vectors \(B_j^{\rm out}\), the local conservation condition is
\[
\boxed{\sum_i B_i^{\rm in}=\sum_j B_j^{\rm out}.}
\tag{126.4}
\]
This is the vector equation, not equality of magnitudes. It is necessary for a Burgers-conservative junction reaction. It does not by itself determine the reaction products, their geometry, admissible slip systems, or energetic favourability.

The equal-vector head exchange in Theorem 126 is one explicit topology update satisfying the full boundary condition. It is not a universal rule for arbitrary Burgers-vector pairs. Unequal-vector reactions require a different local patch and an explicitly balanced multi-arm junction; they are not silently accepted by (126.1).

## 4. Exact finite algorithm and audit

The source implementation is [\`src/burgers_reconnection.py\`](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/feat/burgers-equal-burgers-reconnection-2026-11-12/src/burgers_reconnection.py). It:
- computes the full \(C_0(V;\Lambda_B)\)-valued boundary;
- exchanges heads only for two disjoint strands with equal Burgers vectors;
- rejects unequal-vector head exchange and degenerate endpoint data;
- checks the boundary before and after the rewrite exactly;
- provides a separate vector-sum test for a declared junction.

The accompanying tests are in [\`tests/test_burgers_reconnection.py\`](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/feat/burgers-equal-burgers-reconnection-2026-11-12/tests/test_burgers_reconnection.py), proposed in source [PR #199](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/199). **The tests have been authored but are not claimed to have passed CI** at this record's creation.

## 5. Relation to T125 and the Frank–Read programme

- **T125** supplies the fixed-topology energy, first variation and dissipative flow. T126 supplies one explicit, exactly Burgers-conserving local topology update.
- **T124** supplies the reduced circular-arc Frank–Read threshold under its constant-line-tension assumptions.
- **T091 and Morandotti Actions #161/#162** supply upstream traction-jump reconstruction/decomposition evidence. Those Actions do not test this reconnection routine or a Frank–Read event.
- **Q6/PRISM** may supply a finite incidence substrate after a physical embedding and Burgers assignment are declared. Neither the 64-state Q6 graph nor its incidence matrices determine the physical Burgers lattice or the reconnection trigger.

A complete Frank–Read simulation still needs an event criterion, local core/Peierls energetics, admissible glide geometry, a rule for source regeneration, and coupling to the evolving stress field. Boundary conservation is necessary bookkeeping, not a sufficient physical event law.

## 6. Status ledger

1. **PROVED:** exact boundary invariance (126.2) for equal-vector head exchange.
2. **PROVED:** formula (126.3) identifies why unequal-vector head exchange is not admissible under this rule.
3. **PROVED:** junction vector balance (126.4) is the correct algebraic conservation condition for a declared oriented junction.
4. **IMPLEMENTATION WRITTEN; CI PENDING:** exact boundary calculation, guarded rewrite, and unit tests in source PR #199.
5. **OPEN:** physically selected reconnection criterion, energy drop/barrier, core resolution, mobility and event timing.
6. **OPEN:** unequal-Burgers reactions on multi-arm patches, with complete local boundary matching.
7. **OPEN:** coupling the event map to T125 evolution and proving a Frank–Read emission/regeneration result under calibrated material data.

**Conclusion.** T126 gives a constructive, exact local reconnection operation for equal-Burgers strands and proves preservation of the full discrete Burgers boundary. It closes the algebraic conservation requirement for this restricted move, not the physical Frank–Read event problem.

## References

1. [T124 — Frank–Read source, line-tension threshold and atomistic core input](T124-frank-read-source-line-tension-atomistic-core.md).
2. [T125 — Q6/PRISM Burgers-labelled chains and variational Frank–Read interface](T125-q6-prism-burgers-chain-frank-read-variational-interface.md).
3. [T091 — Frank–Burgers tensorial interaction and anisotropy composition law](T091-frank-burgers-tensorial-anisotropy-composition-law.md).
4. [Source implementation PR #199](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/199).

**FLN**
