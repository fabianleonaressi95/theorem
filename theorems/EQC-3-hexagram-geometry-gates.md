# EQC-3 — Hexagram geometry gates and relational instruction algebra

**Status:** exact finite gate definitions with a reference state-vector implementation and numerical tests. The gates act on a six-qutrit register; this is a proposed language layer, not a claim of hardware advantage or physical dynamics.

## 1. Six positions are geometric, not merely six labels

Write a computational basis word as |d0 d1 ... d5>, with each digit in Z3. The corresponding symbol labels are -1, 0, +1 under the convention d=0,1,2, respectively. The six tensor factors are the six ordered line positions of an esagram.

EQC-2 supplied local qutrit gates and a relational SUM gate. EQC-3 adds operations that act on the arrangement of the six lines.

## 2. Geometric gates

**Line reversal**
REV |d0 d1 d2 d3 d4 d5> = |d5 d4 d3 d2 d1 d0>.
It is a permutation matrix, hence unitary, and REV^2=I.

**Cyclic line rotation**
ROT |d0 d1 d2 d3 d4 d5> = |d1 d2 d3 d4 d5 d0>.
It is unitary and ROT^6=I. Together REV and ROT generate a representation of the dihedral symmetry group D6 on the six line positions (with the convention that REV is a reflection).

**Register swap** SWAP(a,b) exchanges two selected line positions. It is unitary and involutive.

**Symbol polarity inversion**
INV_a|-1>=|+1>, INV_a|0>=|0>, INV_a|+1>=|-1>.
In the stored digit convention this is the permutation (0 2), not multiplication by -1 in Z3. It is unitary and INV_a^2=I. This distinction prevents a common encoding error.

## 3. Relational operations and algebra

The generalized SUM gate is
SUM(a,b)|d_a,d_b> = |d_a,d_b+d_a mod 3>.
It couples two line positions and is entangling when combined with a Fourier gate. REV, ROT and SWAP transport the line positions on which local and relational gates act. Consequently, the language can express the same local relation at different positions without rewriting the gate's mathematical meaning.

The generated gate set now contains:
- local phase/shift/Fourier gates X,Z,F,F†;
- local symbol permutations P, including the named polarity gate INV;
- relational entangling SUM;
- geometric line-position symmetries REV, ROT and SWAP.

Every listed gate is unitary. Compositions are therefore unitary. Measurement, reset and irreversible overwrite are intentionally not included in this reversible core.

## 4. Implementation and tests

The reference compiler accepts INV qN, SWAP qA qB, REV and ROT. The simulator applies the corresponding permutations to a 729-amplitude state vector. Focused tests check REV squared, ROT to the sixth power, INV squared, and SWAP squared against the identity, alongside the EQC-2 tests.

The identities are exact consequences of the definitions; the code checks their implementation numerically. No physical significance is assigned to the dihedral action without a separately derived model.

## 5. Research boundary and next mathematical question

The next substantive step is not adding arbitrary gates. It is deriving a preferred relational gate family from the actual hexagram/Q6 incidence structure and its automorphism group, then comparing it with the full qutrit Clifford group. In particular, one must determine which line symmetries preserve the chosen incidence/adjacency data; visual symmetries of a drawn hexagram are not automatically automorphisms of Q6 or of an MQM action.

No speedup, fault-tolerance advantage, or superiority over qubits is claimed.
