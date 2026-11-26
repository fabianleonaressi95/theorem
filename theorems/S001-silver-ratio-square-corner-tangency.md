# Lemma S.1 — Silver-ratio scaling in a square-corner tangency configuration

**Status: PROVED (exact Euclidean geometry).**

## 1. Configuration

Let a square have side length `2R`, with `R>0`, and let its incircle have
radius `R` and centre `O=(R,R)`. Choose one square corner as the origin
`C=(0,0)`. The diagonal from `C` through `O` meets the incircle at its
near intersection point `P`.

In the same corner, consider a circle of radius `r>0` tangent to both
adjacent sides of the square and externally tangent to the incircle. Its
centre is necessarily `Q=(r,r)`.

Define `d=|CP|`, the distance from the corner to the near intersection
of the incircle with the diagonal, and define the silver ratio

    delta_S = 1 + sqrt(2).

## 2. Lemma

In this configuration,

    d/R = 1/delta_S,
    r/R = 1/delta_S^2,

and hence

    R : d : r = 1 : delta_S^(-1) : delta_S^(-2),
    r = d^2/R.

## 3. Proof

Taking the diagonal as the line from `(0,0)` in direction `(1,1)`, the
distance from the corner to the incircle centre is

    |CO| = sqrt(R^2+R^2) = R sqrt(2).

The near intersection `P` lies one radius `R` back from `O` along this
diagonal. Therefore

    d = |CO|-R = R(sqrt(2)-1).

Since `(sqrt(2)-1)(sqrt(2)+1)=1`,

    d/R = sqrt(2)-1 = 1/(1+sqrt(2)) = delta_S^(-1).

For the small circle, tangency to the two perpendicular sides places its
centre at `Q=(r,r)`, while `O=(R,R)`. Thus

    |OQ| = sqrt(2)(R-r).

External tangency to the incircle is equivalent to `|OQ|=R+r`. Hence

    sqrt(2)(R-r)=R+r,

which gives

    r/R = (sqrt(2)-1)/(sqrt(2)+1)
         = (sqrt(2)-1)^2
         = delta_S^(-2).

Combining the two identities yields `r/R=(d/R)^2`, or `r=d^2/R`.
This proves the lemma.

## 4. Geometric interpretation and scope

Taking `R` as the reference length, the incircle-to-corner-intercept
distance and the corner-circle radius form the first three terms

    R, R/delta_S, R/delta_S^2

of a silver-ratio-scaled sequence. The lemma establishes these two exact
scale factors for this particular square-corner tangency construction.
It does **not** establish an infinite self-similar packing, a general law
for arbitrary square tilings, or a dynamical refinement rule.

The result is independent of the Q6 cell complex and of Gate E.1. A
connection to RGS–PSU refinement would require an explicit map showing
that the same geometric construction is reproduced by the relevant
cell maps or scale operators. No such identification is asserted here.

The term “pennacchio” may be used for the corner region in a chosen
geometric drawing, but the lemma depends only on the coordinates and
tangency conditions stated above.

## 5. Exact identities for audit

With `delta_S=1+sqrt(2)`, the following equivalent identities hold:

    delta_S^(-1) = sqrt(2)-1,
    delta_S^(-2) = 3-2sqrt(2),
    delta_S^2 = 2 delta_S + 1,
    r/R = (d/R)^2.

These are algebraic identities, not numerical fits.