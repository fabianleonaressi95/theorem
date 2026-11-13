# EQC-3 — Native RGS symmetry gates

**Classification:** exact finite group construction and permutation-unitary lift; finite tests compare the subgroup with the RGS seed. Not a universal physical symmetry claim.

## Label convention

T113-D uses big-endian six-bit labels. The first three bits select the eight RGS orbit representatives; the last three encode coordinate signs. In EQC, digits 0,1,2 encode symbols -1,0,+1. The Q6 alphabet {0,+1} is represented by qutrit digits {1,2}.

## Generators

Let B_q exchange qutrit basis states |1> and |2>, fixing |0>. The three sign reversals are B_3, B_4, B_5. The geometric y-z exchange is **not** a simple SWAP of q4 and q5: it simultaneously exchanges the representative bits q1,q2 and the sign bits q4,q5. Its gate is PAIRSWAP(q1,q2;q4,q5).

The four generators are therefore B_3, B_4, B_5 and PAIRSWAP(1,2;4,5). They generate C2^3 semidirect C2, with the final involution exchanging B_4 and B_5. The order is 16, and the group is isomorphic to C2 x D4.

## Exact gate semantics

Each B_q is a local qutrit permutation matrix. PAIRSWAP is the simultaneous permutation of two disjoint register pairs. All four are permutation matrices on the full 729-dimensional six-qutrit basis, hence exactly unitary. They preserve the 64-dimensional Q6 subspace.

The tests compare the complete lifted 16-element permutation set with the subgroup induced by the 48 signed-coordinate transformations on the canonical RGS seed, retaining only those preserving Q6 adjacency. This comparison caught and corrected an initially insufficient single-pair SWAP.

## Scope

These gates generate the RGS/Q6 subgroup, not all of Aut(Q6) or the ternary Hamming automorphism group. For a fixed MQM-1 reference vector x*, the native symmetry group is further intersected with Stab(x*). No quantum speedup or physical calibration is claimed.

Run: python -m unittest discover -s tests -p test_eqc_rgs_gates.py -v
