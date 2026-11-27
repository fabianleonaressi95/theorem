# SGC-003 source audit — the 1837 attribution and diagram

**Audit date:** 2026-11-27  
**Scope:** compare the equal-radius model in SGC-003 with the published descriptions and diagrams for the 1837 Aichi/Ohsu Kannon Sangaku material.

## Result

The algebra in SGC-003 is exact for its stated model. The available evidence does **not** establish that this model is the geometry of the survivingly documented 1837 Ohsu Kannon tablet. In fact, the 1837 Ohsu Kannon problem explicitly described and illustrated in Fukagawa–Rothman (2008), Problem 16, Figure 4.15, is a different configuration.

This distinction is important: the 1837 tablet problem in Figure 4.15 has four equal circles of radius r inside a larger circle R, with their centres forming a rectangle whose one side is 2r; a central circle p touches all four, and two circles q touch two of the r-circles externally and R internally. Its question is to find p in terms of q. The figure on printed page 101 was inspected directly in the PDF. The solution on printed page 126 derives p=q.

By contrast, SGC-003 uses a diameter AB of a containing circle, two equal circles in one semicircle tangent to AB and internally tangent to the containing circle, their mirror images in the other semicircle, a circle r3 externally tangent to all four, and a circle r4 tangent externally to the upper pair and internally to the containing circle. These are not the same incidence/tangency diagrams.

## Evidence chain

1. Alexander Bogomolny's Cut-the-Knot page, “A Sangaku with Many Circles and Some,” says its applet *purports to suggest* an 1837 Aichi Sangaku, citing *Temple Geometry* 1.5.7. It then gives exactly the geometric description and the equations used in SGC-003. This is a secondary web reconstruction, not the original tablet image. Its own wording is appropriately tentative.
2. Fukagawa Hidetoshi and Tony Rothman, *Sacred Mathematics: Japanese Temple Geometry* (Princeton University Press, 2008), Chapter 4, Problem 16, printed p. 101 and Figure 4.15, identifies a tablet presented in 1837 to Ohsu Kannon temple, Nagoya, Aichi, and describes the four-r-circles / p-and-q configuration above. The published figure was visually inspected from the accessible PDF.
3. The same book's selected solution, printed p. 126, Figure 4.52 and equations, derives (p-q)(2r+p)=0 and hence p=q for positive radii. This is an independent 1837 problem, not a confirmation of SGC-003's r3=r4 model.

## Mathematical status of SGC-003

For r>0 and 0<=x<=r, set
\[
r_1=\frac{r^2-x^2}{2r},\qquad
r_3=-r_1+\sqrt{r_1^2+x^2},\qquad
r_4=\frac{r^2+x^2}{2r}-r_1.
\]
The nonnegative square-root branch satisfies
\[
\sqrt{r_1^2+x^2}=\frac{r^2+x^2}{2r},
\]
so
\[
r_3=r_4=\frac{x^2}{r}.
\]
At x=r/3, r1=4r/9 and r3=r4=r/9. This proves the identity for the idealized diagram encoded by those equations. It does not prove that the equations are a transcription of the 1837 Ohsu Kannon tablet.

## Classification decision

- **SGC-003 algebra:** MODEL / EXACT-COMPUTATION.
- **Cut-the-Knot geometric transcription:** SECONDARY-SOURCE-TRANSCRIBED; not primary-artifact verified.
- **Identification of SGC-003 with the 1837 Ohsu Kannon Problem 16:** REJECTED — the published Figure 4.15 has a different incidence/tangency structure.
- **Identification with the separate item cited as *Temple Geometry* 1.5.7:** HISTORICAL-UNVERIFIED pending inspection of the exact 1989 source page and, ideally, the original tablet or archival photograph.
- **1837 Ohsu Kannon Problem 16:** independently documented as the four-r-circles / p,q configuration; do not merge it with SGC-003.

## Sources

- Bogomolny, Alexander, [“A Sangaku with Many Circles and Some”](https://www.cut-the-knot.org/Curriculum/Geometry/CirclesInCirclesSangaku.shtml), especially the attribution and equations.
- Fukagawa, Hidetoshi; Rothman, Tony, *Sacred Mathematics: Japanese Temple Geometry*, Princeton University Press, 2008, Chapter 4, Problem 16, Figure 4.15, printed p. 101; selected solution, printed p. 126. [Accessible PDF copy](https://nnty.fun/downloads/books/TAEL/HISTORY/SCIENCE/MATHEMATICS/Sacred%20Mathematics%20Japanese%20Temple%20Geometry%20-%20Hidetoshi%20Fukagawa%2C%20Tony%20Rothman%202008.pdf).

The accessible 2008 book is a published secondary source. It is not the original 1837 tablet or Nagata Toshimasa's unpublished manuscript. This audit therefore avoids claiming direct inspection of the historical artifact.

## Follow-up check: the exact 1989 reference 1.5.7

The bibliographic identity of the cited 1989 book is confirmed independently by Google Books and WorldCat: Hidetoshi Fukagawa and Daniel Pedoe, *Japanese Temple Geometry Problems*, Charles Babbage Research Centre, Winnipeg, 1989, 206 pp., ISBN 0919611214 / 9780919611214. Google Books identifies its digitized exemplar as originating from the University of Michigan.

Bogomolny's page explicitly cites the item as *Temple Geometry*, **1.5.7** and gives the SGC-003 incidence description and equations. However, the accessible Google Books record exposes bibliographic metadata and partial indexing, not a readable scan or searchable transcription of the exact 1.5.7 page. I therefore cannot independently verify from the 1989 volume that the problem statement, date 1837, Aichi attribution, diagram and labels are transcribed faithfully. The citation itself is verifiable; the content of that cited page remains uninspected.

Do not confuse the two editions/references:
- **1989, Fukagawa–Pedoe, item 1.5.7:** cited by Bogomolny for the SGC-003-style four-circle/semicircle arrangement; exact page content not yet independently inspected.
- **2008, Fukagawa–Rothman, Chapter 4, Problem 16, Figure 4.15, p. 101:** explicitly describes a different 1837 tablet presented to Ohsu Kannon, with four equal circles inside a larger circle and auxiliary p/q circles. Its published solution is on p. 126.

Thus the 2008 Problem 16 comparison disproves an identification of SGC-003 with **that particular Ohsu Kannon Problem 16**, but it does not disprove the separate 1989 item 1.5.7 cited by Bogomolny. These may be distinct Sangaku problems associated with Aichi in 1837. Resolving whether the 1989 item 1.5.7 is faithfully represented requires direct inspection of that page (physical copy, library scan, or a full-view digital copy) and ideally its cited source image.

Additional catalogue references:
- [Google Books record for the 1989 Fukagawa–Pedoe volume](https://books.google.com/books?id=JVjvAAAAMAAJ)
- [WorldCat record](https://search.worldcat.org/title/613367446)
- [Bogomolny's explicit 1.5.7 citation and transcription](https://www.cut-the-knot.org/Curriculum/Geometry/CirclesInCirclesSangaku.shtml)
- [2008 Problem 16, Figure 4.15, page 101 (accessible searchable transcription)](https://anyflip.com/iurx/mipd/basic/101-150)
