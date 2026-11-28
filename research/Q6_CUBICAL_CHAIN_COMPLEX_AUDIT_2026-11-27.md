# Exact cubical chain complex of the six-line Q6 carrier

The carrier is the six-dimensional binary cube of hexagrams, with Hamming-one edges. For a k-cell, choose k free bit positions and fix the other \(6-k\) bits. Its oriented axes are ordered increasingly. The cellular boundary is
\[
\partial_k[c]=\sum_{j=0}^{k-1}(-1)^j([c_{j,+}]-[c_{j,-}]).
\]
The script constructs all cells and integer boundary matrices \(\partial_1,\partial_2,\partial_3\) and checks the chain identities
\[
\partial_1\partial_2=0,\qquad \partial_2\partial_3=0.
\]
The exact cubical counts are
\[
(64,192,240,160,60,12,1),
\]
and the Euler characteristic of the full 6-cube is 1. This confirms why the graph-only cycle rank 129 must not be used as the first Betti number after attaching the square and higher cells.

Run:
\`\`\`bash
python scripts/audit_q6_cubical_chain_complex.py
python -m unittest discover -s tests -p "test_q6_cubical_chain_complex.py" -v
\`\`\`

This is an exact combinatorial chain-complex audit. It does not yet construct nonlinear \(SE(3)\) face holonomies or prove their covariant Bianchi identities.
