# EQC-4 — Hamming-graph automorphisms and the qutrit Clifford subgroup

**Status:** exact finite combinatorial theorem with a proof sketch and exhaustive checks of the selected generators. The result identifies a graph-symmetry subgroup of the qutrit Clifford group; it does not establish a computational speedup.

## 1. The graph determined by the ternary esagram alphabet

Let V = {-1,0,+1}^6. Join two words when they differ in exactly one position. This is the Hamming graph H(6,3), equivalently K3 Cartesian-power six times.

Its full graph automorphism group is the wreath product
Aut(H(6,3)) = S3 wr S6 = (S3)^6 semidirect S6.
Its order is (3!)^6 6! = 33,592,320.

The established binary Q6 is the induced subgraph on any selected two-symbol alphabet in each coordinate, in particular {0,+1}^6. Its automorphism group is S2 wr S6, of order (2!)^6 6! = 46,080. The ternary automorphism group is 729 times as large. This ratio is a group-order comparison, not a speedup.

## 2. Why the wreath product is the full group

For H(n,q), the maximal cliques of size q are exactly the coordinate lines: all vertices obtained by varying one coordinate while fixing the others. A graph automorphism maps maximal cliques to maximal cliques and preserves the relation of belonging to the same parallel coordinate class. It therefore induces:
1. a permutation of the n coordinate directions;
2. an independent permutation of the q symbols in each coordinate.

Conversely, every such combination preserves Hamming distance one. Hence Aut(H(n,q)) = S_q wr S_n for n>=2 and q>=2. Applying n=6, q=3 gives the formula above.

## 3. The EQC gate generators realize this group

At each line, the language has:
- X: the cyclic symbol permutation -1 -> 0 -> +1 -> -1;
- INV: the transposition -1 <-> +1 with 0 fixed.

A 3-cycle and a transposition generate S3. Thus X and INV on each of the six positions generate (S3)^6.

SWAP gates generate all coordinate permutations S6. Therefore local X/INV plus SWAP generate the complete Hamming-graph automorphism group S3 wr S6. REV and ROT are useful named generators inside this S6 action, but are not additional independent group factors.

## 4. Relation to qutrit Clifford operations

The computational digits j=0,1,2 form F3. Every permutation of three symbols is an affine map j -> a j + b over F3 with a in {1,2}, b in F3; AGL(1,3) has order 6 and is isomorphic to S3. Such local affine basis permutations are qutrit Clifford operations. Wire permutations are also Clifford operations. Consequently the graph-automorphism action is contained in the six-qutrit Clifford group (more precisely, in its basis-permutation/monomial subgroup, modulo global phase).

The inclusion is strict. The qutrit Fourier gate F maps a computational basis vector to a superposition, so it is not a permutation of H(6,3) vertices. SUM is a Clifford entangling gate, but is not generally an automorphism of the Hamming graph: changing one control trit can change both control and target output coordinates. Thus the Clifford group contains operations beyond the graph's classical automorphisms.

Important encoding subtlety: semantic symbol inversion INV is the transposition (0 2) on stored digits under d(-1)=0,d(0)=1,d(+1)=2. It is still an affine permutation of F3 (j -> 2j+2), but it is not the linear map j -> -j. This is why the language specifies the symbol map rather than calling it field negation.

## 5. What this establishes for EQC

This is the first non-arbitrary gate family derived from the ternary Hamming geometry:
- local symbol relabelings preserve Hamming adjacency;
- line permutations preserve Hamming adjacency;
- their generated group is exactly the full graph automorphism group;
- this group has a natural embedding into the qutrit Clifford group.

It does not yet establish that this is the correct physical symmetry group of the MQM model. If a weighted incidence operator, action, or Q6/RGS coupling is introduced, its stabilizer may be a strict subgroup. The relevant next audit is to compute the stabilizer of the actual MQM/Q6 data, not to assume all Hamming automorphisms remain physical symmetries.

## 6. Verification

The companion code exhaustively checks that the named local symbol and coordinate generators preserve adjacency on all 729 vertices and tests the group-order formulas. The full-group identification follows from the maximal-coordinate-clique argument above, not from numerical enumeration alone.
