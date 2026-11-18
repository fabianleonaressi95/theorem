# Polloni, Thales and the Vesica Piscis: a geometric comparison

**Research note — 18 November 2026**  
**Status:** elementary Euclidean identities below are proved; the symbolic reading in Polloni is interpretive; the attribution of a specific Vesica construction to Tristan Needham remains **unverified** pending an exact primary-text citation. This note is not a new theorem about RGS, PRISM or Q6.

## 1. Scope and source record

This note compares Marco Polloni's article *Il Primo Angolo* (24 August 2020) with the circle geometry used in the Vesica Piscis discussion associated in the present research programme with Tristan Needham.

- Polloni, Marco, [“Il Primo Angolo”](https://argonauti.blog/il-primo-angolo-di-marco-polloni/), Argonauti, 24 August 2020. The supplied article text discusses the central/inscribed-angle theorem, Thales' theorem, Dante, and a symbolic interpretation of the right angle.
- Needham, Tristan, *Visual Complex Analysis*, Oxford University Press, 1997. This is a relevant geometric/visual-mathematical reference in the wider programme, but **no page or passage has yet been verified that attributes the Vesica Piscis construction or the identities below to Needham**. Do not cite Needham as the source of the Vesica theorem until that passage is located.
- Baldi, Mauro Maria, [*On a property of the Vesica Piscis*](https://zenodo.org/records/4273133), Zenodo record. Use as a related modern source; verify the deposited document's full bibliographic metadata before assigning journal, volume or DOI.
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

## 6. Relation to the golden ratio: what is and is not established

The pentagon/pentagram construction introduces
[
\varphi=\frac{1+\sqrt5}{2},\qquad \varphi^2=\varphi+1,
]
whereas the Vesica construction above gives \(\sqrt3\). These are different algebraic numbers, arising here from different exact configurations.

No identity \(\varphi=\sqrt3\), no derivation of \(\varphi\) from the Vesica alone, and no universal geometric equivalence between the regular pentagon and the Vesica follows from the constructions above. A bridge between the two requires an additional explicitly specified construction (for example, a common circle, a shared chord/diagonal constraint, or a polygonal incidence condition) and a separate proof.

Accordingly, the sequence “Vesica / hexagonal geometry → pentagon / golden ratio” is a **research direction**, not a theorem established by Polloni or by this note.

## 7. Classification and audit checklist

| Claim | Status | Reason |
|---|---|---|
| Central angle is twice the inscribed angle on the same arc | **Proved (classical)** | Standard circle theorem; arc/directed-angle convention stated |
| Triangle on a diameter is right-angled | **Proved (classical)** | Immediate corollary: Thales' theorem |
| Vesica common chord has length \(\sqrt3r\) when centre distance is \(r\) | **Proved here** | Pythagoras / cosine rule |
| Vesica chord subtends (120^\circ) centrally and (60^\circ) inscribed on the appropriate arc | **Proved here** | Cosine rule and central/inscribed-angle theorem |
| Polloni's Blake/Dante reading is a mathematical consequence | **Not established** | Interpretive claim, not a geometric deduction |
| Needham is the primary source of this Vesica construction | **Open / unverified** | Exact passage and page not yet identified |
| A necessary connection between \(\sqrt3\) and \(\varphi\) follows | **Not established** | No such implication in the constructions above |

## 8. Next source and mathematics tasks

1. Locate the exact Needham passage/page previously discussed and record its edition and context; until then retain the attribution caveat.
2. Verify the full metadata and mathematical statement in Baldi's deposited document.
3. Retrieve Polloni's companion articles on the pentagon/pentagram and the “poligono divino”; compare their constructions with the present Vesica geometry, not just their terminology.
4. If a pentagon–Vesica bridge is proposed, write down its incidence/metric constraints and derive the resulting polynomial before interpreting it in terms of \(\varphi\).
5. Keep the symbolic Blake/Dante layer in a separate historical/interpretive subsection.

## 9. Conclusion

Polloni's “Il Primo Angolo” and the Vesica Piscis can be connected rigorously through the central-angle/inscribed-angle theorem. Thales' theorem is its diametral case; the Vesica gives a different exact case with central angle (120^\circ), inscribed angle (60^\circ), and aspect ratio \(\sqrt3:1\). The appearance of \(\varphi\) belongs to the separate pentagonal construction until a further theorem is supplied.

**Repository classification:** research note; classical Euclidean results proved; source attribution to Needham and any pentagon–Vesica synthesis remain open. No new numbered theorem is claimed.
