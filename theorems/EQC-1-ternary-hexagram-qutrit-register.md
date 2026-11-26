# EQC-1 — Ternary hexagram state space and qutrit register

**Status:** exact finite combinatorial and linear-algebraic specification; computationally tested.  
**Scope:** a proposed programming substrate for the Morfodinamica Quantistica programme. No claim of hardware advantage or physical realization is made.

## 1. Ternary alphabet and six-position words

Let \(\mathbb T=\{-1,0,+1\}\). A six-position word is
\[
\mathbf s=(s_1,\ldots,s_6)\in\mathbb T^6.
\]
There are exactly \(3^6=729\) words. The symbols are three distinct labels. Their numerical values do not, by themselves, imply probabilities, amplitudes, charges, or physical polarities.

Fix the bijection \(d(-1)=0,d(0)=1,d(+1)=2\). The lexicographic/base-three rank is
\[
I(\mathbf s)=\sum_{j=1}^6 d(s_j)3^{6-j}\in\{0,\ldots,728\}.
\]
This gives a reversible encoding and decoding convention.

## 2. Ternary Hamming graph

Connect two words iff they differ in exactly one coordinate. The graph is the Cartesian power \(K_3^{\square 6}\), with:
- 729 vertices;
- degree \(6(3-1)=12\);
- \(729\cdot12/2=4374\) undirected edges.

Its adjacency spectrum follows from the Cartesian-product spectrum of \(K_3\):
\[
\lambda_k=12-3k,\qquad
m_k=\binom 6k 2^k,\quad k=0,\ldots,6.
\]
The multiplicities sum to \((1+2)^6=729\). This is an exact graph-theoretic result, not a physical energy spectrum.

## 3. Relation to the existing Q6

The subset \(\{0,+1\}^6\subset\mathbb T^6\), with adjacency inherited from the ternary Hamming graph, is exactly the binary six-cube \(Q_6=K_2^{\square6}\):
\[
|V(Q_6)|=64,\quad \deg(Q_6)=6,\quad |E(Q_6)|=192.
\]
Thus the established Q6 is an induced subgraph, not discarded. The ternary extension adds states containing \(-1\); it does not identify \(-1\) with a negative quantum amplitude.

## 4. Quantum realization: six qutrits

The associated register Hilbert space is
\[
\mathcal H_{3}^{\otimes6}=(\mathbb C^3)^{\otimes6},
\qquad \dim\mathcal H=729.
\]
For one qutrit, with basis \(|j\rangle\), \(j\in\mathbb Z_3\), define
\[
X|j\rangle=|j+1\!\!\pmod3\rangle,\qquad
Z|j\rangle=\omega^j|j\rangle,\quad \omega=e^{2\pi i/3}.
\]
Then \(X^3=Z^3=I\), \(X,Z\) are unitary, and \(ZX=\omega XZ\). These are the standard qutrit shift/clock operators. They act on a three-dimensional complex Hilbert space; they are not the same thing as arithmetic on the labels \(-1,0,+1\).

The computational basis is indexed by the 729 words using \(d\). A general pure register state is a normalized complex vector \(\psi\in\mathbb C^{729}\). A valid gate is a unitary operator on this space (or a specified tensor factor), not an arbitrary map between labels.

## 5. Minimal language semantics (proposal)

The first EQC instruction set is deliberately small:
1. `ENCODE`: map a six-symbol word to its base-three index.
2. `DECODE`: inverse operation.
3. `FLIP_SIGN`: apply \(s_j\mapsto-s_j\) at a selected position (a classical reversible permutation).
4. `SHIFT3`: apply the qutrit cyclic shift \(X\) at a selected register position.
5. `PHASE3`: apply \(Z\) at a selected position.
6. `HOP(j,a\to b)`: classical graph rewrite changing one selected symbol; this is not a quantum gate unless embedded in a unitary permutation on the full basis.
7. `MEASURE`: specify a measurement basis and report probabilities; measurement is not reversible.

A compiler must distinguish classical word transformations, unitary gates, and measurements. In particular, a one-way overwrite or a non-bijective rewrite cannot be advertised as a reversible quantum instruction.

## 6. Exact finite statements and open questions

**Proved by construction:** cardinality, rank/unrank bijection, Hamming adjacency counts, Q6 induced-subgraph identity, and qutrit Weyl relations.

**Computationally checked:** finite enumeration and the identities above in the accompanying tests.

**Open:** useful gate synthesis for a target hardware platform; fault-tolerant qutrit error correction; comparison of circuit depth, noise and resource cost against qubit encodings; a physically derived choice of ternary transition Hamiltonian; and any continuum or MQM dynamical interpretation.

No quantum speedup, new physical degree of freedom, or superiority over binary computing is claimed. The proposal is a mathematically precise candidate language and benchmark substrate.
