# T141 — Antipodally equivariant incidence lift of the supergolden icosahedron into Q6

**Status:** exact finite construction on the T139 vertex ordering; executable regression tests committed but not yet run in CI. This is a path-valued lift on the 1-skeleton, not a graph embedding and not a PSU–Anti-Twin mixing operator.

## 1. Antipodal pairing and Q6 codes

For the coordinate ordering used in T139,
`(0,1,2,3,4,5,6,7,8,9,10,11)`, the antipodal involution is
[
(0 3)(1 2)(4 7)(5 6)(8 11)(9 10).
]
Choose one representative from each pair and assign the following even-weight Q6 words:
[
egin{array}{c|c|c}
	ext{icosahedron representative}&	ext{Q6 word}&	ext{support}\hline
0&000011&{1,2}\
1&000101&{1,3}\
4&001001&{1,4}\
5&010001&{1,5}\
8&100001&{1,6}\
9&000110&{2,3}
end{array}
]
Map each antipodal partner to the bitwise complement. In T139 index order this is
[
egin{array}{c|rrrrrrrrrrrr}
v&0&1&2&3&4&5&6&7&8&9&10&11\
iota(v)&3&5&58&60&9&17&46&54&33&6&57&30
end{array}
]
where integers are six-bit words (leading zeroes are retained when displayed).

The map is injective, all images have even parity, and by construction
[
oxed{iota(ar v)=iota(v)oplus 63.}
]

## 2. Why every icosahedral edge lifts

The six chosen representatives have weight two and are pairwise distinct. Any two distinct weight-two words in six coordinates have Hamming distance either 2 or 4. Replacing either endpoint by its complement changes the distance from (d) to (6-d). Hence for any two distinct antipodal classes, and in particular for every icosahedral edge,
[
d_H(iota(u),iota(v))in{2,4}.
]
No icosahedral edge joins a vertex to its antipode. Thus every edge has a Q6 path lift of length 2 or 4.

This deliberately relaxes T140's two-step-only requirement. Some edges necessarily use four steps under this explicit assignment.

## 3. Equivariant path lift

For a directed edge ([u,v]), list the bit positions where (iota(u)) and (iota(v)) differ in increasing order and flip them one at a time. Denote the resulting path by (iota_1([u,v])). Then
[
partial_1^{Q_6}iota_1([u,v])
=[iota(v)]-[iota(u)].
]
Because complementing both endpoints leaves the set and order of differing bit positions unchanged, the same construction gives
[
iota_1([ar u,ar v])=J_#,iota_1([u,v]),
qquad J(x)=xoplus63,
]
as an equality of directed paths and therefore of 1-chains. The lift is antipodally equivariant.

## 4. Scope and limitations

- The vertex map is injective; the path lift need not be edge-disjoint or an embedding of the subdivided icosahedral graph.
- The chain map is defined on the 1-skeleton. No 2-chain/facial compatibility is claimed.
- This construction supplies antipodal equivariance, not a canonical geometric coupling to the archived Q6 tangent variables or transport matrices.
- It does not by itself define a Hermitian operator (T_{m geom}), prove ({T_{m geom},J}=0), or establish PSU–Anti-Twin mixing. Those require an additional rule turning the lifted oriented paths into an operator, followed by an independent audit.

## 5. Reproduction

```bash
python scripts/audit_t141_antipodal_icosahedron_q6_lift.py
python -m unittest tests.test_t141_antipodal_icosahedron_q6_lift
```
