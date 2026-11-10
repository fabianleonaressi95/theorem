# S.2 — Unified square–triangle–pentagon–hexagon and supergolden geometry

**Status: exact component results proved; common reference-circle construction specified; labelled incidence and supergolden construction remain open.**

## 1. Common geometric frame

Take a square of side length \(2R\), centred at \(O\), with incircle of radius \(R\). This circle is the common reference circle for the square construction and for regular polygons inscribed in it.

The square, regular pentagon, and regular hexagon can therefore be studied at one scale. Their orientations are not automatically fixed relative to one another: any assertion about a particular vertex lying on a square diagonal, a side midpoint, or a tangency point requires an explicit rotation convention.

## 2. Square and right triangles: the silver ratio

Let \(C\) be a square corner. The centre distance is the hypotenuse of a right isosceles triangle with legs \(R\), so \(CO=R\sqrt2\). The near intersection \(P\) of diagonal \(CO\) with the incircle is at distance

$$
d=CP=R(\sqrt2-1)=\frac{R}{\delta_S},
\qquad \delta_S=1+\sqrt2.
$$

If a smaller circle of radius \(r\) is tangent to the two sides issuing from \(C\) and externally tangent to the incircle, its centre is \((r,r)\) in corner coordinates. The centre-distance equation is

$$
\sqrt2(R-r)=R+r,
$$

which gives

$$
r=R(\sqrt2-1)^2=\frac{R}{\delta_S^2}.
$$

Thus Lemma S.1 establishes the exact local scale relation

$$
R:d:r=1:\delta_S^{-1}:\delta_S^{-2},
\qquad r=\frac{d^2}{R}.
$$

The small circle is externally tangent to the incircle. This is a local corner configuration, not a general packing or a refinement law.

## 3. Inscribed regular pentagon: the golden ratio

Inscribe a regular pentagon in the same circle of radius \(R\). A side subtends \(72^\circ\) at the centre and a diagonal subtends \(144^\circ\). If \(s\) and \(D\) denote its side and diagonal, respectively, then

$$
s=2R\sin36^\circ,
\qquad D=2R\sin72^\circ.
$$

Consequently,

$$
\frac{D}{s}
=\frac{\sin72^\circ}{\sin36^\circ}
=2\cos36^\circ
=\frac{1+\sqrt5}{2}
=\varphi.
$$

This is an exact chord identity, independent of the pentagon's rotation. Its particular alignment with the square remains a separate incidence question.

## 4. Inscribed regular hexagon: the bronze ratio

Inscribe a regular hexagon in the same circle of radius \(R\). Its circumradius equals its side length, so write

$$
s_6=R.
$$

The distance between opposite vertices is the major diagonal \(2s_6\). The distance between opposite sides (the across-flats width) is twice the apothem:

$$
h_6=2s_6\cos30^\circ=\sqrt3\,s_6.
$$

The hexagon therefore supplies the dimensionless geometric factor \(\sqrt3\). In particular, the sum of one side length and the across-flats width, normalized by the side, is

$$
\frac{s_6+h_6}{s_6}=1+\sqrt3=\delta_B.
$$

Thus

$$
\boxed{\delta_B=1+\sqrt3}.
$$

This makes precise one way the regular hexagon encodes the bronze ratio. It is important not to identify \(\delta_B\) with either the major-diagonal/side ratio \(2\), or the across-flats/side ratio \(\sqrt3\): the bronze ratio is the **sum** \(1+\sqrt3\).

## 5. Supergolden rectangle

Define \(\Psi\) as the unique positive real root of

$$
\Psi^3=\Psi^2+1,
\qquad \Psi\approx1.465571231876768.
$$

A supergolden rectangle has longer-to-shorter side ratio \(\Psi\). Its defining equation is equivalently

$$
\Psi-1=\Psi^{-2}.
$$

This reciprocal-square identity is structurally reminiscent of the square-corner relation \(r/R=\delta_S^{-2}\), but it does not derive one construction from the other. In this record the supergolden rectangle is an additional exact algebraic ratio; a construction of it from the square, pentagon, or hexagon has not yet been established.

## 6. Unified comparison on the common reference scale

The four structures now sit in one geometric framework:

| Figure | Exact geometric datum | Ratio |
|---|---|---|
| Square and diagonal right triangle | diagonal leg ratio | \(\sqrt2\), giving \(\delta_S=1+\sqrt2\) |
| Square-corner circle tangency | corner-circle scale | \(r/R=\delta_S^{-2}\) |
| Regular pentagon | diagonal / side | \(\varphi=(1+\sqrt5)/2\) |
| Regular hexagon | across-flats / side | \(\sqrt3\), giving \(\delta_B=1+\sqrt3\) |
| Supergolden rectangle | long side / short side | \(\Psi\), with \(\Psi^3-\Psi^2-1=0\) |

The square, pentagon, and hexagon are co-located by the same circle: the square's incircle is simultaneously the circumcircle of the two regular polygons. The pentagon contributes the golden chord ratio; the hexagon contributes the \(\sqrt3\) metric and, by adding one side to its across-flats width, the bronze ratio. The square contributes the \(\sqrt2\) diagonal geometry and the silver corner-tangency scale.

This is a common geometric **framework**, not yet one single forced polygonal overlay. A specific simultaneous orientation of the pentagon and hexagon relative to the square must be supplied before claims about shared vertices, crossings, or special intersection points can be made.

## 7. What remains open

The exact component identities above do not by themselves prove:

1. a unique orientation or vertex correspondence for the pentagon and hexagon relative to the square;
2. that \(\delta_S\), \(\varphi\), \(\delta_B\), and \(\Psi\) arise as eigenvalues or scale factors of one common geometric operator;
3. that the supergolden rectangle is constructible from this polygonal overlay by a specified finite sequence of incidences, tangencies, or intersections;
4. that the construction is generated by Q6, PRISM, Krist-All, or an RGS–PSU refinement rule.

To close these bridges, the next mathematical input is a labelled coordinate diagram: fix the square, specify the angular phase of the pentagon and hexagon, and state which vertices, diagonals, sides, and tangencies are intended to coincide. The resulting incidence equations can then be solved exactly and tested for the appearance of \(\Psi\).

## 8. Algebraic identities for audit

$$
\delta_S=1+\sqrt2,\qquad \delta_S^{-1}=\sqrt2-1,
\qquad \delta_S^2=2\delta_S+1;
$$

$$
\varphi=\frac{1+\sqrt5}{2},\qquad
\varphi^2=\varphi+1,\qquad \varphi^{-1}=\varphi-1;
$$

$$
\delta_B=1+\sqrt3,\qquad \delta_B^{-1}=\frac{\sqrt3-1}{2};
$$

$$
\Psi^3=\Psi^2+1,\qquad \Psi-1=\Psi^{-2}.
$$

These are distinct algebraic signatures: silver and bronze are quadratic over \(\mathbb Q\), golden is quadratic over \(\mathbb Q\), and supergolden is cubic. Their coexistence in the common-circle construction is exact; any deeper algebraic or dynamical relation requires a separately proved incidence or operator identity.
