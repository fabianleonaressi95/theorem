# Exact Q6 edge-order alignment for the RGS carrier

**Classification:** exact finite combinatorial/indexing result. This does not identify a continuum connection or certify the contents/action convention of unavailable A13 transport binaries.

## 1. Two edge orderings

The recovered RGS seed uses the vertex-major ordering
\[
E_{\rm RGS}=\bigl((v,v\mathbin{|}2^a,a):
0\leq v<64,\ 0\leq a<6,\ (v\mathbin{\&}2^a)=0\bigr),
\]
where \(a=0,\ldots,5\) labels least-significant-bit positions. Each edge is oriented from the smaller endpoint to the larger endpoint.

The canonical Q6 complex labels axes big-endian:
\[
m_b=2^{5-b},\qquad b=0,\ldots,5,
\]
and stores the lexicographically sorted endpoint pairs \((u,v)\), \(u<v\).

The vertex labels and coordinates agree: both seed reconstructions use the same eight orbit representatives, the same sign-product ordering, and the same verified coordinate SHA-256
\[
\texttt{6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf}.
\]

## 2. Exact permutation

The edge sets coincide because both constructions join precisely those pairs whose six-bit labels differ in one bit. The axis labels are related by
\[
b=5-a.
\]
The edge orderings differ only by a permutation. The executable audit constructs
\[
\pi_{\rm RGS\to Q6}(e)
=\operatorname{index}_{E_{\rm Q6}}(u_e,v_e)
\]
from endpoint pairs, and its inverse. It verifies:
- 192 distinct edges in each ordering;
- exact equality of endpoint pairs after permutation;
- the two permutations are mutual inverses;
- every vertex has degree six;
- the reconstructed RGS edge array has the archived SHA-256
  \texttt{da7854ca655577b629dc508208918326fde1d50563485f953ea0fdc1b2fb78e8}
  after canonical int64 serialization.

No nearest-neighbour inference or geometric rematching is used.

## 3. What this closes for the coframe work

This closes the **combinatorial edge-index map** between the RGS carrier ordering and the canonical Q6 ordering. It provides the exact permutation needed before comparing edge-indexed quantities across the two conventions.

It does **not** by itself compare the A13 arrays \(R_{SO(3)}\) or \(U_{SU(2)}\). The archived A13 payloads are not part of this source checkout, and the direction in which each stored transport acts must be read from its generating convention or checked against reverse-edge identities. The permutation must not be used to silently assume a transport action convention.

The carrier-derived three-component edge coframe in theorem PR #476 remains a separate finite construction on its selected tetrahedral fixture. The Q6 incidence alignment here does not assert that this four-vertex tetrahedron is a Q6 3-cell or that its face quantity is continuum Cartan torsion.

## 4. Reproduction

From the repository root:

~~~bash
python scripts/audit_rgs_q6_edge_order_alignment.py
python -m pytest tests/test_rgs_q6_edge_order_alignment.py -q
~~~

The script writes \`audits/RGS_Q6_EDGE_ORDER_ALIGNMENT_2026-11-26.json\`, including both 192-entry permutations and explicit NOT_TESTED fields for the transport payloads.
