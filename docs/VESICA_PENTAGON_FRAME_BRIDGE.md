# Vesica–pentagon construction and the mixed-frame map

**Status:** exact Euclidean construction; explicit convention-dependent linear correspondence; no derived nonzero torsion law.

## 1. Scope and provenance

This note records the Vesica Piscis–regular pentagon construction described by A. C. Sparavigna and M. M. Baldi, *A Study of the Regular Pentagon with a Classic Geometric Approach* (2016), especially §6, Figs. 3–5 and Eqs. (25)–(27).

It keeps separate:
- the exact geometric construction of the regular pentagon;
- a subsequently chosen linear map between two selected pairs of directions;
- the independent problem of deriving a non-holonomic transport law and nonzero torsion.

The Flower-of-Life-to-Vesica correspondence is not asserted here: it requires its own explicit circle/point incidence map.

## 2. Vesica and exact pentagonal construction

Let the two equal circles have radius \(r>0\) and centres
\[
O=(0,0),\qquad A=(0,-r).
\]
Their centre distance is \(r\), so each centre lies on the other circle. Their intersections are
\[
E,F=\left(\pm\frac{\sqrt3}{2}r,-\frac12r\right),
\]
and therefore
\[
EF=\sqrt3\,r.
\]

Choose
\[
C=(r,0),\qquad G=\left(0,-\frac r2\right).
\]
Then \(G\) is the midpoint of \(OA\), and
\[
GC^2=r^2+\frac{r^2}{4}=\frac54r^2,
\qquad GC=\frac{\sqrt5}{2}r.
\]
Transfer this length onto the ray from \(G\) opposite to \(A\), defining \(H\) by \(GH=GC\). Since \(GO=r/2\),
\[
OH=GH-GO=\frac{\sqrt5-1}{2}r=\frac r\varphi,
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]
Thus
\[
H=\left(0,\frac r\varphi\right),\qquad OC\perp OH.
\]
The segment \(CH\) satisfies
\[
CH^2=r^2+\frac{r^2}{\varphi^2}
=4r^2\sin^2 36^\circ,
\qquad CH=2r\sin36^\circ.
\]
Hence \(CH\) is the chord subtending \(72^\circ\) in the circle of radius \(r\) centred at \(O\). Five successive copies give a regular pentagon.

The exact angular phases are therefore
\[
\alpha_k=\alpha_0+\frac{2\pi k}{5},\qquad k=0,1,2,3,4,
\qquad 5\cdot72^\circ=360^\circ.
\]
These are the established pentagonal phases. They specify the fivefold construction; by themselves they do **not** specify a spatially varying phase field \(\alpha(x)\) or a transport law for a mixed frame.

## 3. A declared linear correspondence between selected directions

Fix the following ordered pairs:
\[
u_1=\frac{A-O}{r}=(0,-1),\qquad
u_2=\frac{E-O}{r}=\left(\frac{\sqrt3}{2},-\frac12\right),
\]
\[
v_1=\frac{C-O}{r}=(1,0),\qquad
v_2=\frac{H-C}{CH}
=\left(-\frac{1}{2\sin36^\circ},
\frac{1}{2\varphi\sin36^\circ}\right).
\]
The convention is explicitly
\[
Fu_1=v_1,\qquad Fu_2=v_2.
\]
Both ordered pairs are bases, so this determines one invertible linear map. Direct calculation gives
\[
\boxed{
F=
\begin{pmatrix}
-\dfrac{1+\sin36^\circ}{\sqrt3\sin36^\circ}&-1\\[2mm]
\dfrac{1}{\sqrt3\,\varphi\sin36^\circ}&0
\end{pmatrix}.}
\]
Its determinant is
\[
\det F=\frac{1}{\sqrt3\,\varphi\sin36^\circ}>0.
\]
The formula is independent of the scale \(r\).

**Correction note.** A previously circulated matrix with second column
\((-1/(2\sin36^\circ),0)^T\) does not satisfy \(Fu_1=v_1\). Since \(u_1=(0,-1)\), the second column must be exactly \((-1,0)^T\). The first column above then follows from \(Fu_2=v_2\).

This map is a declared correspondence between two ordered direction bases. It is not canonically selected by the pentagon construction alone, and it is not claimed to intertwine the full \(D_3\) and \(D_5\) actions.

## 4. Mixed-frame interpretation and torsion check

If, as an additional modelling convention, the two coordinate planes are identified by
\[
A_a{}^m=F^m{}_a
\]
with constant \(F\), and
\[
E^m=dy^m-A_a{}^m dx^a,
\]
then
\[
dE^m=-dA_a{}^m\wedge dx^a=0.
\]
Thus the nonzero mixed block does not produce torsion.

More generally, if one proposes a position-dependent pentagonal phase \(\alpha(x)\) and sets
\[
A(x)=R(\alpha(x))F,
\]
then
\[
dE^m=-dA_a{}^m\wedge dx^a
\]
can be nonzero. But the construction above supplies only the discrete phases \(\alpha_k=\alpha_0+2\pi k/5\); it does not derive a continuous field \(\alpha(x)\). Such a field must come from an independently specified transport/holonomy rule, incidence constraint, or non-holonomic distribution. Do not present it as a consequence of the Vesica–pentagon construction.

For a genuine frame/coframe model, retain the full previously fixed convention
\[
E_a=e_a{}^\mu\partial_\mu+A_a{}^m\partial_m,
\qquad
E_i=\phi_i{}^m\partial_m,
\]
\[
E^a=e^a{}_\mu dx^\mu,
\qquad
E^i=\phi^i{}_m(dy^m-A_a{}^m e^a).
\]
The torsion must be computed from the full coframe and the declared spin connection; it is not generally exhausted by the simplified expression \(-dA\wedge dx\).

## 5. Classification

| Statement | Status |
|---|---|
| Vesica intersection separation \(EF=\sqrt3r\) | Proved by coordinates |
| Exact construction of the regular pentagon from \(CH\) | Proved; cited construction |
| Five phases separated by \(72^\circ\) | Proved |
| Linear map \(F\) for the declared ordered direction pairs | Proved by matrix calculation |
| Identification \(A=F\) as a mixed-frame block | Modelling convention |
| Nonzero torsion from constant \(F\) | False in the stated simplified coframe |
| Continuous phase transport \(\alpha(x)\) derived from Vesica/pentagon | Open |
| Nonzero torsion and the desired \(T B_\perp\) coupling | Open; requires further geometric/dynamical derivation |

## References

- A. C. Sparavigna and M. M. Baldi, *A Study of the Regular Pentagon with a Classic Geometric Approach* (2016), §6, Figs. 3–5, Eqs. (25)–(27). Institutional repository PDF: https://iris.polito.it/retrieve/e384c431-930e-d4b2-e053-9f05fe0a1d67/properties-pentagon.pdf
- A. C. Sparavigna and M. M. Baldi, *A Mathematical Study of a Symbol: the Vesica Piscis of Sacred Geometry*.
