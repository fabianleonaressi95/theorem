# T121 — Icosahedral A5 action on Q6 and its exterior Clifford module

**Classification:** exact functorial algebraic consequence of an orthogonal signed-permutation representation; finite group-action audits in the repository are numerical.

The proper rotational icosahedral group, of order 60, acts on six unoriented antipodal vertex axes by signed permutations \(S(g)\in O(6)\), with \(S(g_1g_2)=S(g_1)S(g_2)\). A positive signed entry copies a Q6 bit and a negative entry complements it. This permutes all 64 vertices and preserves Hamming-distance-one adjacency, hence acts by automorphisms of the Q6 graph and its cubical complex. The source checks \(S(g)^TC_6S(g)=C_6\). The axis-to-coordinate identification is a declared convention, not a metric embedding.

Let \(V=\mathbb R^6\), \(\mathcal S=\Lambda^*V_\mathbb C\), so \(\dim_\mathbb C\mathcal S=64\). Define \(c(v)=\varepsilon(v)+\iota(v)\), with exterior multiplication and contraction. Their standard identities imply
\[
c(v)c(w)+c(w)c(v)=2\langle v,w\rangle I,
\]
so \(\mathcal S\) is a complex Euclidean Clifford module.

For any \(S\in O(6)\), the induced map \(\Lambda S=\bigoplus_k\Lambda^kS\) obeys
\[
(\Lambda S)c(v)(\Lambda S)^{-1}=c(Sv).
\]
This follows from naturality of exterior multiplication and the isometry covariance of contraction. Therefore each signed-axis transformation induces a Clifford-module automorphism, and these maps form a representation.

**Central distinction:** the Q6 signed-axis action is an \(A_5\) representation. Viewed as a representation of \(2I\), it factors through \(2I/\{\pm1\}\), so the central element \(-1\) acts trivially on Q6 and on the induced exterior module. In contrast, the defining two-dimensional representation in T119 sends \(-1\) to \(-I_2\). These are different central characters; an intertwiner between these spaces cannot be presumed.

**Source:** `src/rgs_icosahedral_q6_intertwiner.py`, `src/rgs_q6_clifford_module.py`. **Tests:** `tests/test_rgs_icosahedral_q6_intertwiner.py`, `tests/test_rgs_q6_clifford_module.py`. They check the 60 signed actions, group law, C6 covariance, Q6 vertex/edge preservation, 729 cubical cells, Clifford anticommutators and chirality. The induced exterior action \(\Lambda S\) is the mathematical construction recorded here, not an already implemented/tested source feature.

**Boundary:** this does not construct a Pin lift of the Möbius transitions, a connection-compatible Dirac operator, torsion, a continuum limit or physical QLG dynamics.