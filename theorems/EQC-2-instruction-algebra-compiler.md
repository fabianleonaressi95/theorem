# EQC-2 — Instruction algebra and six-qutrit reference compiler

**Status:** proposed language semantics with exact finite gate definitions and a reference state-vector interpreter. The implementation is a classical simulator of a quantum circuit; it is not a quantum computer or a hardware-performance claim.

## 1. Three semantic layers

EQC separates:
1. **Symbols:** \(-1,0,+1\), encoded as qutrit basis digits \(0,1,2\).
2. **Classical reversible transformations:** permutations of the three labels or of complete register words.
3. **Quantum gates:** unitary maps on \((\mathbb C^3)^{\otimes6}\).

A destructive overwrite, a one-way rewrite, or a measurement is not a reversible gate. The language must not conflate these categories.

## 2. Gate algebra

For one qutrit, let \(\omega=e^{2\pi i/3}\). Define
\[
X|j\rangle=|j+1\pmod3\rangle,\quad
Z|j\rangle=\omega^j|j\rangle,
\]
\[
F|j\rangle=\frac1{\sqrt3}\sum_{k=0}^2\omega^{jk}|k\rangle.
\]
Then \(X^3=Z^3=I\), \(F^\dagger F=I\), and \(ZX=\omega XZ\).

For distinct registers \(a,b\), define the SUM gate
\[
\operatorname{SUM}_{a,b}|j,k\rangle=|j,k+j\pmod3\rangle.
\]
It is a permutation of the computational basis and \(\operatorname{SUM}^3=I\). Together with local qutrit gates it supplies an entangling primitive.

A classical local permutation \(P_\pi|j\rangle=|\pi(j)\rangle\), for \(\pi\in S_3\), is also unitary when extended linearly. The sign inversion \(-1\leftrightarrow+1\), with \(0\) fixed, is one such permutation.

## 3. Minimal source language

The reference compiler accepts one instruction per line:
\
`X q0`, `Z q1`, `F q2`, `FDG q2`, `SUM q0 q1`, `P q0 1 0 2`.

The permutation instruction lists the output digit for each input digit. For example, `P q0 1 0 2` swaps basis labels 0 and 1 and leaves 2 fixed. Registers are indexed q0 through q5. Comments begin with `#`.

The compiler rejects malformed operands, out-of-range registers, non-permutations, and a SUM gate whose control and target coincide. It emits an immutable instruction sequence. The interpreter applies it to a normalized 729-component state vector, initialized by default to \(|000000\rangle\).

## 4. Exact semantics and numerical checks

The gate definitions are exact. The reference implementation uses floating-point complex arithmetic for simulation. Tests check:
- normalization preservation under the implemented gates;
- \(X^3=I\) and \(\operatorname{SUM}^3=I\);
- \(F^\dagger F=I\) numerically;
- a Fourier-plus-SUM circuit creates a three-term entangled state;
- classical sign inversion is a reversible local permutation;
- invalid programs are rejected.

The simulator is deliberately dependency-free and small. It is a semantic prototype, not an optimized simulator. A dense state vector has 729 complex entries for six qutrits; larger registers grow exponentially.

## 5. What remains open

This does not establish a computational advantage over qubits. The next fair comparison must fix a task and compare qutrit and qubit encodings under the same logical operation, error model, hardware constraints, and resource accounting. Fault tolerance, compilation cost, connectivity, gate fidelity, and measurement overhead must be included. No physical interpretation of ternary symbols is assumed.
