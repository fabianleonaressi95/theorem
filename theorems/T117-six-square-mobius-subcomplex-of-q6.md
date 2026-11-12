# T117 — Six-square Möbius subcomplex of Q6

**Classification:** exact finite combinatorial/topological theorem for the declared six face patterns and cyclic orientation. The result is independent of any embedding into Euclidean RGS coordinates.

## 1. Definition

Use six-bit big-endian labels for Q6. A star denotes a free bit. Take the six patterns
\[
\begin{aligned}
(&**1100,\ *01*00,\ 00**00,\\
 &*11*00,\ *1*000,\ 0**000).
\end{aligned}
\]
For each pattern, read its two free bits in the cyclic order
\[
(0,0),\ (1,0),\ (1,1),\ (0,1).
\]
This gives the oriented square cycles
\[
\begin{aligned}
&(12,44,60,28), &&(8,40,44,12),\\
&(0,8,12,4), &&(24,56,60,28),\\
&(16,48,56,24), &&(0,16,24,8).
\end{aligned}
\]
Let K be the resulting finite 2-dimensional cell complex, with its 1-cells identified by unordered endpoint pairs and oriented from the smaller to the larger integer label. Let B_1 and B_2 be its integer incidence matrices.

## 2. Theorem

The complex K has:
\[
|K^{(0)}|=12,\quad |K^{(1)}|=18,\quad |K^{(2)}|=6,
\]
with 12 boundary edges and 6 interior edges. Its boundary has one connected component. Moreover:
\[
B_1B_2=0,\qquad \chi(K)=12-18+6=0.
\]
The cellular homology over \(\mathbb Z\) has Betti numbers
\[
\boxed{(b_0,b_1,b_2)=(1,1,0),}
\]
and K is non-orientable.

### Proof

The six displayed cycles contain 12 distinct vertices. Their edge union contains 18 distinct unoriented edges. Exactly six edges occur in two face boundaries and the remaining twelve occur once. The once-occurring edges form one connected boundary cycle.

Every face boundary is a closed oriented cycle. Applying the vertex-edge incidence map to such a cycle gives zero, hence \(B_1B_2=0\) over the integers.

The 1-skeleton is connected, so \(\operatorname{rank} B_1=12-1=11\). Each of the six faces has two boundary edges that occur in no other face; these private edges are distinct between faces. Thus the six columns of B_2 are linearly independent over \(\mathbb Z\), so \(\operatorname{rank}B_2=6\). It follows that
\[
b_0=12-11=1,\quad b_1=18-11-6=1,\quad b_2=6-6=0.
\]

For orientability, two faces sharing an interior edge must be assigned opposite induced directions along that edge. The face-adjacency graph is the six-cycle
\[
0-1-2-5-4-3-0.
\]
The relative orientation signs along these six adjacencies, in that order, are
\[
(+1,+1,+1,+1,+1,-1),
\]
whose product is \(-1\). Propagating a face orientation once around the cycle therefore returns the opposite orientation at the starting face. No globally consistent orientation exists. Hence K is non-orientable. \(\square\)

## 3. Relation to Q6

Every listed square is an elementary coordinate square of the canonical six-cube. The vertex set is
\[
\{0,4,8,12,16,24,28,40,44,48,56,60\}.
\]
Thus K is a specified cellular subcomplex of the Q6 2-skeleton, not a separately postulated geometric surface.

The theorem concerns this combinatorial subcomplex and its incidence maps. It does not identify a metric embedding, a physical membrane, or a torsion field.

## 4. Evidence and scope

- **Proved:** cell counts, boundary incidence counts, connected boundary, integer boundary-of-boundary identity, Euler characteristic, Betti numbers and non-orientability for the stated patterns.
- **Implementation audit:** \`src/mobius_complex.py\`; tests in \`tests/test_mobius_complex.py\`.
- **Not implied:** a Pin structure, spin structure, torsion, curvature of an RGS connection, or a continuum limit. Non-orientability alone establishes none of these.

Reproduce in \`rgs-qlg-quaternion-bridge\`:
\`\`\`bash
PYTHONPATH=. python -m pytest tests/test_mobius_complex.py -q
\`\`\`
