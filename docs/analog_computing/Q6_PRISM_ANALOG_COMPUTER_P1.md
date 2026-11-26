# Q6–PRISM Analog Computer: P1 H(2,3) RC prototype

**Status:** mathematical specification and proposed bench prototype. The hardware has not been built or measured. This document does not claim an experimental validation or a quantum implementation.

## 1. Purpose and scope

P1 is the smallest physical test of the ternary Hamming-graph diffusion model. Its graph is
\[
H(2,3)=K_3\square K_3,
\]
with vertex set \(V=\{-1,0,+1\}^2\). Two vertices are adjacent exactly when they differ in one coordinate. The circuit is a passive RC network whose node voltages obey the graph-Laplacian evolution.

The ternary symbols label graph vertices; they are not voltage levels. Each vertex has one continuous electrical state variable, its node voltage.

P1 tests the graph-to-circuit correspondence and the predicted relaxation modes. It does **not** implement unitary quantum evolution, prove a physical information principle, or establish computational advantage over digital hardware.

## 2. Exact graph specification

There are 9 vertices and 18 undirected edges. Every vertex has degree 4.

Use the labels:

| Label | Vertex |
|---|---|
| A | (-1,-1) |
| B | (0,-1) |
| C | (+1,-1) |
| D | (-1,0) |
| E | (0,0) |
| F | (+1,0) |
| G | (-1,+1) |
| H | (0,+1) |
| I | (+1,+1) |

Install one resistor on each of these edges:

- Rows: A–B, A–C, B–C; D–E, D–F, E–F; G–H, G–I, H–I.
- Columns: A–D, A–G, D–G; B–E, B–H, E–H; C–F, C–I, F–I.

Equivalently, each row and each column of the 3-by-3 array is a complete graph \(K_3\). There are no other resistor connections in the ideal model.

## 3. Circuit model

For every vertex \(i\), connect a capacitor \(C_i=C\) from node \(i\) to the common reference ground. For every graph edge \(\{i,j\}\), connect a resistor \(R_{ij}=R\) between nodes \(i\) and \(j\). Do not add intentional shunt resistors from nodes to ground.

Kirchhoff's current law gives
\[
C\dot v_i=-\frac1R\sum_{j\sim i}(v_i-v_j)+I_i(t),
\]
or
\[
\boxed{C\dot{\mathbf v}=-\frac1R L\mathbf v+\mathbf I(t),}
\]
where \(L=D-A\) is the combinatorial graph Laplacian.

For the proposed nominal values \(R=10\,\mathrm{k\Omega}\), \(C=10\,\mu\mathrm F\), one has \(RC=0.1\,\mathrm s\). These are starting values, not measured or optimized component values.

## 4. Analytic spectral prediction

Since \(H(2,3)=K_3\square K_3\), its Laplacian spectrum is the sum spectrum of two copies of \(K_3\), whose Laplacian eigenvalues are 0 (multiplicity 1) and 3 (multiplicity 2). Thus
\[
\operatorname{spec}(L)=
\begin{cases}
0 & \text{multiplicity }1,\\
3 & \text{multiplicity }4,\\
6 & \text{multiplicity }4.
\end{cases}
\]

The unforced voltage evolution has modal decay rates
\[
0,\qquad \frac{3}{RC},\qquad \frac{6}{RC}.
\]
At the nominal values these are 0, 30 and 60 s\(^{-1}\), corresponding to time constants \(\infty\), 33.3 ms and 16.7 ms.

For an ideal isolated network, the zero mode is the uniform voltage vector. Therefore the arithmetic mean of the nine node voltages is conserved, while all voltage differences decay. Real source leakage, instrument loading, capacitor leakage and parasitic paths can violate this ideal conservation law.

## 5. Bench bill of materials

| Item | Quantity | Nominal specification |
|---|---:|---|
| Edge resistors | 18 | 10 kΩ, 1% |
| Node capacitors | 9 | 10 µF; observe polarity if electrolytic |
| Input current/voltage pulse path | 1 | low-voltage source with series current limiting |
| Breadboard and jumpers | as needed | isolated low-voltage assembly |
| Measurement | 1 set | high-impedance probes; preferably simultaneous channels |

Use only a low-voltage, current-limited source. Never connect this passive prototype to mains voltage. The source must be disconnected after initialization when measuring free relaxation.

## 6. Measurement protocol

1. Check every resistor value and verify the 18-edge connectivity against the list in §2.
2. Check that each capacitor is connected from its assigned node to the common reference. Avoid adding resistive paths to ground.
3. Apply a small, current-limited pulse to one selected node. Record the actual source waveform; a finite-width pulse is not an exact mathematical delta impulse.
4. Disconnect the source and record all nine node voltages against the same reference. Use high-impedance inputs to minimize loading.
5. Repeat with excitation at the central node E. If nine-channel acquisition is unavailable, repeat the experiment under reproducible initial conditions and measure sequentially.
6. Estimate modal decay rates by fitting the measured voltage vector to the predicted eigenspaces, or compare the full voltage trace against a numerical solution using the measured component values and recorded input waveform.

The 100 Ω series resistor sometimes used for input current limiting is part of the source path only; it is not one of the 18 graph edges and must not remain as a shunt in the free-relaxation network.

## 7. Acceptance checks

The accompanying standard-library script `scripts/verify_hamming_ternary_p1.py` constructs the graph and checks:

- 9 vertices, 18 edges and degree 4 at every vertex;
- Laplacian symmetry and zero row sums;
- the exact polynomial identity \(L(L-3I)(L-6I)=0\);
- rank 8, \(\operatorname{tr}L=36\), and \(\operatorname{tr}(L^2)=180\), which together certify multiplicities 1, 4 and 4 for eigenvalues 0, 3 and 6.

Run:
```bash
python scripts/verify_hamming_ternary_p1.py
```

These are exact combinatorial checks of the specified graph, not measurements of a physical circuit. Experimental acceptance additionally requires:

- observed topology matching the edge list;
- mean-voltage drift quantified and consistent with known leakage/loading;
- decay rates compatible with 0, 30 and 60 s\(^{-1}\), within uncertainty from measured R, C and instrumentation;
- repeatability under controlled initial conditions.

No experimental data are included in this PR.

## 8. Relation to the binary Q6 corner subgraph

The four corner vertices \(\{(-1,-1),(-1,+1),(+1,-1),(+1,+1)\}\) induce a 4-cycle, the binary Hamming graph \(H(2,2)\). They are not an invariant subsystem of the full ternary network: each corner also has two edges to vertices with a zero coordinate. To isolate the binary 4-cycle physically, those eight corner-to-interior edges must be opened with switches. That switched circuit is a different network and has a different Laplacian from the full P1 circuit.

## 9. Scaling outlook and limitations

The same construction generalizes to \(H(6,3)\), with 729 vertices, degree 12 and 4,374 edges. This count is a graph-theoretic specification, not a claim that a 729-node circuit has been assembled or is practical on a single breadboard. A staged scale-up should validate layout parasitics, component spread, measurement loading, power dissipation and reproducibility at each size.

Memristive elements, nonlinear devices and reservoir-computing claims are outside P1. They require separate constitutive models and experiments; they must not be inferred from the passive linear RC result.
