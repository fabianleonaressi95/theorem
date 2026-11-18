# Polloni, Thales and the Vesica Piscis: a geometric comparison

**Research note — 18 November 2026**  
**Status:** the Euclidean identities and the complex-number calculation below are proved. Needham's treatment of cube roots and their three branches is a verified conceptual/mathematical connection to the equilateral-triangle geometry underlying the Vesica, **not** a claim that Needham states the Vesica theorem. Bonilla's Vesica-to-pentagon construction is recorded as a claim requiring independent reconstruction. Polloni's symbolic reading remains interpretive. This note is not a new theorem about RGS, PRISM or Q6.

## 1. Scope and source record

This note compares Marco Polloni's article *Il Primo Angolo* (24 August 2020) with the circle geometry used in the Vesica Piscis discussion associated in the present research programme with Tristan Needham.

- Polloni, Marco, [“Il Primo Angolo”](https://argonauti.blog/il-primo-angolo-di-marco-polloni/), Argonauti, 24 August 2020. The supplied article text discusses the central/inscribed-angle theorem, Thales' theorem, Dante, and a symbolic interpretation of the right angle.
- Needham, Tristan, *Visual Complex Analysis*, Clarendon Press / Oxford University Press, 1997, Chapter 2, “Complex Functions as Transformations”, §VI “Multifunctions”, §1 “Example: Fractional Powers”, especially the discussion of the three cube-root determinations and branch permutation (pp. 91–95 in the 1997 pagination; check pagination against the copy/edition cited). Needham supplies the complex-analytic framework for the three cube roots of unity; the Vesica Piscis identification below is our explicit geometric deduction, **not a statement attributed to Needham**. Oxford's publisher record confirms the book, author, publication date and Chapter 2 scope ([book record](https://academic.oup.com/book/52945), [Chapter 2](https://academic.oup.com/book/52945/chapter-abstract/421959387)).
- Baldi, Mauro Maria, [*On a property of the Vesica Piscis*](https://zenodo.org/records/4273133), Zenodo record. Use as a related modern source; verify the deposited document's full bibliographic metadata before assigning journal, volume or DOI.
- Ibo Bonilla, [“Relación áurea entre pentágono y hexágono”](https://iboenweb.com/ibo/docs/relacion_aurea_pentagono_hexagono_phi.html): proposes constructions from Vesica Piscis to pentagons/pentagram and discusses hexagon, truncated icosahedron and φ. Its construction diagrams and claims must be independently reconstructed and checked; the page itself is not proof.
- [Dante, *Paradiso* XIII, 97–102](https://it.wikisource.org/wiki/Divina_Commedia/Paradiso/Canto_XIII): the passage quoted by Polloni invokes the impossibility of inscribing in a semicircle a triangle with the diameter as a side and without a right angle.

The Polloni page is a source for what Polloni argues, not an independent proof of the mathematical claims. The elementary proofs are supplied below.

## 2. Polloni's two Euclidean statements

### 2.1 Central angle and inscribed angle

Let (O) be the centre of a circle, (A,B) two distinct points on it, and (P) another point on the circumference. The central angle and the inscribed angle are related by
[
\angle AOB = 2\angle APB,
]
provided the angles are understood as subtending the same arc (AB) (or with a consistent directed-angle convention).

The qualification about the intercepted arc matters: without it, the statement “any other point” can conceal the supplementary-angle case. The theorem is standard and exact.

### 2.2 Thales' theorem

Let (AB) be a diameter and (C) a point on the same circle, distinct from (A,B). Since the central angle subtending the semicircle is (180^\circ), the inscribed-angle theorem gives
[
\angle ACB=\frac{1}{2}\,180^\circ=90^\circ.
]
Thus every triangle inscribed in a circle with one side equal to a diameter is right-angled at the opposite vertex.

This is exactly the mathematical content needed for the question quoted from *Paradiso* XIII. The impossibility is not a separate exceptional case: it is Thales' theorem.

### 2.3 Interpretive layer

Polloni reads Blake's *The Ancient of Days* and the right angle as an “angle coming from God”, and connects the geometry to Dante's distinction between divine and human wisdom. These are philosophical, iconographic and theological interpretations. They are not consequences of the central-angle theorem or of Thales' theorem and must remain labelled **interpretive**, not mathematical results.

## 3. Vesica Piscis: exact construction and metric identity

Let two circles have equal radius (r>0), with centres (O_1,O_2) satisfying
[
|O_1O_2|=r.
]
Let their two intersection points be (P,Q). Then
[
|O_1P|=|O_2P|=|O_1O_2|=r,
]
and likewise for (Q). Hence (O_1O_2P) and (O_1O_2Q) are equilateral triangles.

The common chord (PQ) is perpendicular to the line of centres and bisects it. In the right triangle formed by a centre, the midpoint of (PQ), and an intersection point, the hypotenuse is (r) and one leg is (r/2). Therefore
[
\frac{|PQ|}{2}
=\sqrt{r^2-\left(\frac r2\right)^2}
=\frac{\sqrt3}{2}r,
\qquad
\boxed{|PQ|=\sqrt3\,r}.
]
Thus the exact aspect ratio of the Vesica (full common-chord length divided by the radius) is
[
\boxed{|PQ|:r=\sqrt3:1}.
]

The angle subtended by chord (PQ) at either circle centre is (120^\circ): indeed, the two radii to the intersections and the chord form an isosceles triangle with sides (r,r,\sqrt3r), so the cosine rule gives
[
\cos\angle PO_1Q
=\frac{r^2+r^2-3r^2}{2r^2}=-\frac12.
]
At a point on the major arc of the corresponding circle, the inscribed angle subtending the minor arc (PQ) is (60^\circ), by the central/inscribed-angle theorem. This is a direct point of contact with Polloni's §2.1.

## 4. The precise bridge between Polloni and the Vesica

The connection is not that Thales' theorem *creates* the Vesica, nor that the two configurations are identical. The valid bridge is the shared circle-angle theorem:

1. The Vesica's equal-circle construction produces a common chord of length (\sqrt3r).
2. That chord subtends a central angle of (120^\circ) in either circle.
3. The same chord subtends an inscribed angle of (60^\circ) at a point on the major arc.
4. Thales' theorem is the limiting/diametral special case of the same central-angle/inscribed-angle relation: a diameter subtends (180^\circ) at the centre and (90^\circ) at the circumference.

The two configurations therefore belong to one coherent theory of chords and subtended angles, but they are distinct cases: (120^\circ/60^\circ) for the Vesica chord, (180^\circ/90^\circ) for a diameter.

## 5. The (30^\circ-60^\circ-90^\circ) triangle and the constant \(\sqrt3\)

Bisecting an equilateral triangle of side (r) gives a right triangle with side lengths
[
\frac r2,\quad \frac{\sqrt3}{2}r,\quad r,
]
hence the ratio
[
1:\sqrt3:2.
]
This is the standard exact source of \(\sqrt3\) in the Vesica construction. It is a Euclidean metric identity, not an approximation.


## 6. Needham's complex roots of unity: the exact connection to the Vesica

Needham's relevant contribution is not an exposition of the Vesica Piscis. In *Visual Complex Analysis*, Chapter 2, §VI.1, he explains fractional powers as multifunctions, including the three determinations of a cube root and their cyclic permutation as the argument winds around the origin. The algebraic object behind the three determinations is the set of cube roots of unity:
\[
1,\qquad \omega=e^{2\pi i/3},\qquad \omega^2=e^{4\pi i/3},
\qquad \omega^3=1.
\]
The two non-real roots are the vertices of an equilateral triangle on the unit circle, and
\[
\omega-\omega^2=i\sqrt3,
\qquad |\omega-\omega^2|=\sqrt3.
\]
This is the complex-plane source of the same \(\sqrt3\) chord length that appears in the unit-radius Vesica construction.

For the Vesica with unit radius and centres \(O_1=(-1/2,0)\), \(O_2=(1/2,0)\), the intersection points are
\[
P=(0,\sqrt3/2),\qquad Q=(0,-\sqrt3/2),
\qquad |PQ|=\sqrt3.
\]
Thus the pair of non-real cube roots of unity and the two Vesica intersection points determine congruent segments of length \(\sqrt3\); after a rigid motion, one pair is carried to the other. This is a precise metric/geometric bridge between Needham's roots-of-unity discussion and the Vesica chord. It does **not** mean that Needham proves or names the Vesica Piscis.

### 6.1 Eisenstein-integer formulation

The cube roots of unity belong to the Eisenstein integers
\[
\mathbb Z[\omega]=\{a+b\omega:a,b\in\mathbb Z\},
\qquad \omega^2+\omega+1=0.
\]
Their difference has norm
\[
N(\omega-\omega^2)
=(\omega-\omega^2)(\bar\omega-\bar\omega^2)=3,
\]
so its Euclidean length is \(\sqrt3\). This places the Vesica chord length in the triangular/Eisenstein lattice, rather than treating \(\sqrt3\) as an isolated trigonometric coincidence. The identity is elementary and proved here; it is not presented as a theorem stated verbatim by Needham.

## 7. Bonilla's proposed Vesica–pentagon–hexagon construction

Bonilla's online article explicitly claims that a Vesica Piscis, with specified “opening” or “span”, generates a unit pentagon/pentagram, nested golden pentagons and a relation with the hexagon and \(\varphi\). This is the missing bridge worth auditing in the present programme.

The claim is **not yet promoted to a theorem**. The article's diagrams and construction steps must be converted into a coordinate/ruler-and-compass construction, with all points, circles, intersections and lengths defined. In particular:
1. Distinguish the Vesica's **opening** (the common chord) from its **span** (the full transverse dimension); do not assume the article uses these terms consistently without checking its diagrams.
2. Reconstruct the proposed pentagon vertices from the stated initial unit and verify all five side lengths and angles.
3. Derive the diagonal/side ratio and check whether it is exactly \(\varphi\), rather than a numerical approximation.
4. Reconstruct the claimed hexagon from the same initial construction and verify its side length, circumradius and incidences.
5. Check whether the icosahedral/truncated-icosahedral discussion is a separate 3D construction or follows from the planar one.

The article's assertion that the Vesica construction yields an exact golden pentagon is a **candidate construction / open verification**, not an established consequence of the \(\sqrt3\) identity. This is where Needham's complex roots-of-unity geometry, the Vesica and Bonilla's golden-ratio construction can be compared without conflating their claims.

## 8. Relation to the golden ratio: what is and is not established

The pentagon/pentagram construction introduces
[
\varphi=\frac{1+\sqrt5}{2},\qquad \varphi^2=\varphi+1,
]
whereas the Vesica construction above gives \(\sqrt3\). These are different algebraic numbers, arising here from different exact configurations.

No identity \(\varphi=\sqrt3\), no derivation of \(\varphi\) from the Vesica alone, and no universal geometric equivalence between the regular pentagon and the Vesica follows from the constructions above. A bridge between the two requires an additional explicitly specified construction (for example, a common circle, a shared chord/diagonal constraint, or a polygonal incidence condition) and a separate proof.

Accordingly, the sequence “Vesica / hexagonal geometry → pentagon / golden ratio” is a **research direction**, not a theorem established by Polloni or by this note.

## 9. Classification and audit checklist

| Claim | Status | Reason |
|---|---|---|
| Central angle is twice the inscribed angle on the same arc | **Proved (classical)** | Standard circle theorem; arc/directed-angle convention stated |
| Triangle on a diameter is right-angled | **Proved (classical)** | Immediate corollary: Thales' theorem |
| Vesica common chord has length \(\sqrt3r\) when centre distance is \(r\) | **Proved here** | Pythagoras / cosine rule |
| Vesica chord subtends (120^\circ) centrally and (60^\circ) inscribed on the appropriate arc | **Proved here** | Cosine rule and central/inscribed-angle theorem |
| Polloni's Blake/Dante reading is a mathematical consequence | **Not established** | Interpretive claim, not a geometric deduction |
| Needham's cube roots of unity give an equilateral triangle whose non-real-root chord has length \\(\\sqrt3\\) | **Verified connection / proved calculation** | Needham's cube-root discussion; explicit distance calculation in §6 |\n| Needham states/proves the Vesica Piscis theorem | **Not claimed** | The Vesica identification is our deduction, not an attribution to Needham |\n| Bonilla's Vesica-to-pentagon/hexagon construction yields exact \\(\\varphi\\) | **Candidate / open verification** | Requires reconstruction from diagrams and exact metric checks |
| A necessary connection between \(\sqrt3\) and \(\varphi\) follows | **Not established** | No such implication in the constructions above |

## 10. Next source and mathematics tasks

1. Locate the exact Needham passage/page previously discussed and record its edition and context; until then retain the attribution caveat.
2. Verify the full metadata and mathematical statement in Baldi's deposited document.
3. Retrieve Polloni's companion articles on the pentagon/pentagram and the “poligono divino”; compare their constructions with the present Vesica geometry, not just their terminology.
4. If a pentagon–Vesica bridge is proposed, write down its incidence/metric constraints and derive the resulting polynomial before interpreting it in terms of \(\varphi\).
5. Keep the symbolic Blake/Dante layer in a separate historical/interpretive subsection.

## 11. Conclusion

Polloni's “Il Primo Angolo” and the Vesica Piscis can be connected rigorously through the central-angle/inscribed-angle theorem. Thales' theorem is its diametral case; the Vesica gives a different exact case with central angle (120^\circ), inscribed angle (60^\circ), and aspect ratio \(\sqrt3:1\). The appearance of \(\varphi\) belongs to the separate pentagonal construction until a further theorem is supplied.

**Repository classification:** research note. Classical Euclidean results and the roots-of-unity distance calculation are proved; Needham is cited for the complex-analytic cube-root framework, not as author of the Vesica theorem. Bonilla's Vesica–pentagon–hexagon construction remains a candidate requiring independent verification. No new numbered theorem is claimed.


## 12. Coordinate audit of Bonilla's shared-circle pentagon–hexagon construction

This addendum reconstructs the configuration shown in Bonilla's diagrams for the Vesica, the pentagon and the hexagon. It supersedes the earlier statement that the whole construction was still awaiting any quantitative check. The exact shared-circle comparison is now derived; the broader sequence of nested polygons and the second pentagon construction still require a point-by-point construction audit.

### 12.1 Coordinates of the Vesica and its outer circle

Set the common radius to (r>0), and choose
\[
O_1=(-r/2,0),\qquad O_2=(r/2,0).
\]
The two generating circles are
\[
(x+r/2)^2+y^2=r^2,\qquad (x-r/2)^2+y^2=r^2.
\]
Their intersections are
\[
P=(0,\sqrt3r/2),\qquad Q=(0,-\sqrt3r/2).
\]
Thus the span (distance between centres) and opening (common chord) are
\[
E=r,\qquad A=|PQ|=\sqrt3r.
\]

The smallest circle centred at the midpoint (O=(0,0)) that contains both generating circles has radius
\[
R=r+E/2=3r/2.
\]
This is the natural “circumscribed circle of the two generating circles” referred to in Bonilla's opening-based claim.

### 12.2 Inscribed regular pentagon and circumscribed regular hexagon

Use this same circle of radius (R=3r/2) as the circumcircle of a regular pentagon and as the incircle of a regular hexagon.

For the inscribed regular pentagon, the side is the chord subtending (72^\circ):
\[
p=2R\sin(\pi/5)=3r\sin36^\circ
=\frac{3r}{4}\sqrt{10-2\sqrt5}.
\]

For the regular hexagon circumscribed about that circle, (R) is its apothem. Half a side and the apothem form a right triangle with angle (30^\circ), so
\[
h=2R\tan(\pi/6)=\frac{2R}{\sqrt3}=\sqrt3r=A.
\]
This is the exact Vesica–hexagon identity:
\[
\boxed{h=A=\sqrt3r.}
\]

The pentagon side is close to, but not equal to, the same length:
\[
\boxed{\frac{p}{h}=\sqrt3\sin36^\circ
=\frac{\sqrt{30-6\sqrt5}}4
\approx1.018073921.}
\]
The relative excess is approximately (1.8073921\%\). Therefore the diagram's “about 1.5/100” description is qualitatively close but is not the exact value for this standard shared-circle interpretation. In particular, the claim that the Vesica opening equals the side of the pentagon inscribed in the circle circumscribing the two generating circles is **false as an exact equality** under this natural reading: the opening equals the side of the circumscribed hexagon, while the inscribed-pentagon side is about 1.8% longer.

Two normalisations make the result transparent:

- If (E=r=1), then (A=h=\sqrt3), (R=3/2), and (p=3\sin36^\circ\approx1.763355757).
- If (A=1), then (r=1/\sqrt3), (R=\sqrt3/2), (h=1), and (p=\sqrt3\sin36^\circ\approx1.018073921).

The ratio (p/h) is independent of scale.

### 12.3 Where the golden ratio actually enters

For every regular pentagon, independently of the Vesica construction, its diagonal (d) and side (p) satisfy
\[
\boxed{d/p=\varphi=(1+\sqrt5)/2.}
\]
Consequently, in the shared-circle configuration,
\[
\frac d h=\varphi\sqrt3\sin36^\circ
=\varphi\frac{\sqrt{30-6\sqrt5}}4,
\]
not exactly \(\varphi\). The Vesica supplies the exact \(\sqrt3\) scale and the shared circle; the pentagon supplies \(\varphi\) through its diagonal/side ratio. Their numerical near-equality of side lengths does not collapse these two independent facts into a new identity.

### 12.4 Classification after the audit

| Statement | Status |
|---|---|
| Vesica opening (A=\sqrt3r), span (E=r) | **Proved** |
| Smallest concentric circle containing both generating circles has radius (3r/2) | **Proved** |
| Circumscribed hexagon side (h=A) on that circle | **Proved** |
| Inscribed pentagon side (p=3r\sin36^\circ) | **Proved** |
| (p=A) for the inscribed pentagon in that same circle | **Disproved**; (p/A\approx1.018073921) |
| Pentagon diagonal/side (=\varphi) | **Proved (classical)** |
| A new exact identity directly equating the Vesica opening and the pentagon side | **Not established** |
| Bonilla's nested pentagons and the separately drawn second pentagon | **Still open** until every vertex and auxiliary circle in those diagrams is reconstructed |

**Source diagrams:** Bonilla, “Relación áurea entre pentágono y hexágono”, especially the construction plates [1](https://iboenweb.com/ibo/images/fotos_pag/relacion%20pentagono%20hexagono%20phi/construccion-pentagono-a-partir-de-hexagono-ibo-1.jpg) and [2](https://iboenweb.com/ibo/images/fotos_pag/relacion%20pentagono%20hexagono%20phi/construccion-pentagono-a-partir-de-hexagono-ibo-2.jpg); and “Vesica Piscis y Proporción Divina”, especially the opening/envergadura plates [3](https://www.iboenweb.com/ibo/images/fotos_pag/vesica_phi/vesica-pentagono-pentaculo-fibonacci-%20ibo.jpg) and [4](https://www.iboenweb.com/ibo/images/fotos_pag/vesica_phi/envergadura-vesica-pentagono-phi-%20IBO.jpg). The equations above are our independent coordinate derivation, not statements attributed to Bonilla.
