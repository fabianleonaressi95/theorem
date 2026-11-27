# SGC-003 source audit — the 1837 Ohsu Kannon Sangaku

**Audit date:** 2026-11-27  
**Scope:** identify the geometry cited as *Japanese Temple Geometry Problems* 1.5.7 and compare it with Fukagawa–Rothman (2008), Problem 16.

## Result

**Correction to the previous audit:** the earlier statement that the 2008 Problem 16 is a different configuration from the Sangaku reconstructed by Cut-the-Knot was wrong. The two descriptions encode the same circle-tangency arrangement, with different notation.

Cut-the-Knot explicitly cites Fukagawa–Pedoe (1989), *Japanese Temple Geometry Problems*, item **1.5.7**, for its “A Sangaku with Many Circles and Some” construction. The uploaded searchable transcription of Fukagawa–Rothman (2008), *Sacred Mathematics*, independently describes the 1837 Ohsu Kannon tablet as **Problem 16**, Figure 4.15, and gives the same geometry. The 2008 text says the tablet was presented in 1837 to Ohsu Kannon temple in Nagoya, Aichi; it attributes the problem to Mizuno Tsuneyuki and says it was recorded in Nagata Toshimasa's unpublished *Sangaku of Ohsu Kannon* (1837).

The correspondence of configurations is therefore established at the level of the two published descriptions. The exact printed page of the 1989 item 1.5.7 has not, however, been directly inspected; its link to the Cut-the-Knot reconstruction remains a citation-mediated identification.

## Geometry and notation correspondence

- Outer circle: radius \(R\).
- Four congruent inner circles: radius \(r\); their centres form a rectangle with one side \(2r\).
- Central circle tangent externally to all four: radius \(p\).
- Two side circles, each tangent externally to two of the four inner circles and internally to the outer circle: radius \(q\).

The notation in the Cut-the-Knot reconstruction is \(r_1,r_3,r_4\). The correspondence is:
\[
r_1=r,\qquad r_3=p,\qquad r_4=q.
\]
Thus the requested relation in Rothman–Fukagawa Problem 16, “Find \(p\) in terms of \(q\),” is precisely the identity \(r_3=r_4\) in the Cut-the-Knot formulation.

## Mathematical verification

### Rothman–Fukagawa 2008, Problem 16

The problem statement is in Chapter 4, Problem 16, Figure 4.15. The text directs the reader to the solution on printed page 125. In the solution's notation, let \(t\) denote the relevant horizontal/vertical centre offset in the right-triangle relations. The two Pythagorean relations are
\[
(r+p)^2=t^2+r^2,
\]
\[
(r+q)^2=t^2+(R-r-q)^2,
\]
together with the outer-circle relation
\[
R=2r+p.
\]
Consequently,
\[
t^2=p^2+2rp
\]
and, after substituting \(R=2r+p\) into the second relation,
\[
t^2=(r+q)^2-(r+p-q)^2=(2q-p)(2r+p).
\]
Equating the expressions for \(t^2\) gives
\[
p^2+2rp=(2q-p)(2r+p),
\]
hence
\[
(p-q)(p+2r)=0.
\]
Since \(p>0\) and \(r>0\), \(p+2r>0\), so
\[
\boxed{p=q}.
\]

### Cut-the-Knot parametrization

For the same diagram, Cut-the-Knot uses \(R\) for the outer radius and \(x\) for the horizontal displacement. Its relations are
\[
r_1=\frac{R^2-x^2}{2R},\qquad
r_3=-r_1+\sqrt{r_1^2+x^2},\qquad
r_4=\frac{R^2+x^2}{2R}-r_1.
\]
Since
\[
\sqrt{r_1^2+x^2}=\frac{R^2+x^2}{2R},
\]
it follows that
\[
r_3=r_4=\frac{x^2}{R}.
\]
For \(x=R/3\), this gives \(r_1=4R/9\) and \(r_3=r_4=R/9\). The identity agrees with the 2008 result \(p=q\) under \(r_3=p\), \(r_4=q\).

## Source and attribution status

1. **Cut-the-Knot:** Alexander Bogomolny, “A Sangaku with Many Circles and Some.” The page cites Fukagawa–Pedoe (1989), *Japanese Temple Geometry Problems*, **1.5.7**, and supplies the semicircle/mirror-pair description and parametrized equations. This is a secondary reconstruction, not direct evidence from the original tablet.
2. **Fukagawa–Rothman (2008):** *Sacred Mathematics: Japanese Temple Geometry*, Chapter 4, Problem 16, Figure 4.15. The uploaded TXT transcription states the 1837 Ohsu Kannon provenance, names Mizuno Tsuneyuki and Nagata Toshimasa, describes the four-\(r\)-circles/\(p,q\) arrangement, and points to the solution on printed p. 125.
3. **1989 volume:** Fukagawa Hidetoshi and Daniel Pedoe, *Japanese Temple Geometry Problems*, Charles Babbage Research Centre, 1989, 206 pp., ISBN 0919611214 / 9780919611214. Bibliographic metadata is confirmed, but the exact 1.5.7 page has not been directly inspected in a full-view scan.

The 2008 Problem 16 is therefore not a separate geometry to be contrasted with SGC-003. The 1989 item 1.5.7 and the 2008 Problem 16 are linked by the Cut-the-Knot citation and by matching published descriptions, but a page-level collation of the 1989 printing remains outstanding.

## Mathematical status of SGC-003

- **Circle identity \(r_3=r_4\):** EXACT for the idealized tangency model and parametrization stated above.
- **Rothman–Fukagawa Problem 16 identity \(p=q\):** follows from the displayed Pythagorean reduction for positive radii.
- **Historical attribution to the 1837 Ohsu Kannon tablet:** explicitly stated in the 2008 Problem 16 text; original tablet/manuscript not directly inspected here.
- **Exact equivalence of the 1989 printed item 1.5.7 wording and diagram:** strongly supported by the explicit Cut-the-Knot citation and matching geometry in the 2008 description, but not page-level verified from the 1989 volume itself.

## Sources

- Bogomolny, Alexander, [“A Sangaku with Many Circles and Some”](https://www.cut-the-knot.org/Curriculum/Geometry/CirclesInCirclesSangaku.shtml).
- Fukagawa, Hidetoshi; Rothman, Tony, *Sacred Mathematics: Japanese Temple Geometry*, Princeton University Press, 2008, Chapter 4, Problem 16, Figure 4.15; solution on printed p. 125. [Accessible PDF copy](https://nnty.fun/downloads/books/TAEL/HISTORY/SCIENCE/MATHEMATICS/Sacred%20Mathematics%20Japanese%20Temple%20Geometry%20-%20Hidetoshi%20Fukagawa%2C%20Tony%20Rothman%202008.pdf).
- Fukagawa, Hidetoshi; Pedoe, Daniel, *Japanese Temple Geometry Problems*, Charles Babbage Research Centre, 1989, item 1.5.7 as cited by Cut-the-Knot. [Google Books catalogue record](https://books.google.com/books?id=JVjvAAAAMAAJ); [WorldCat record](https://search.worldcat.org/title/613367446).

**Audit limitation:** this correction relies on the uploaded searchable transcription of the 2008 book and the cited secondary webpage. It does not claim direct inspection of the original 1837 tablet, Nagata's unpublished manuscript, or the exact 1989 page 1.5.7.
