# C60 face geometry and tangent-fibre construction

**Classification:** geometric construction; no Q6 intertwiner is claimed.

Start with the standard regular icosahedron
\[
(0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1),
\qquad \varphi=(1+\sqrt5)/2.
\]
For each undirected edge {a,b}, include both directed truncation points
\[
x_{a\to b}=(2a+b)/3,\qquad x_{b\to a}=(a+2b)/3.
\]
The resulting convex hull is the truncated icosahedron with 60 vertices. Coplanar triangular hull facets are merged by supporting plane to recover polygonal faces.

For each recovered face, let n_f be its outward unit normal and set
\[
E_f=n_f^\perp\subset\mathbb R^3,\qquad
\mathcal E_{C60}=\bigoplus_{f=1}^{32}E_f.
\]
The required inventory is 12 pentagons and 20 hexagons. Hence dim(E_f)=2 and dim(E_C60)=64. Opposite supporting planes yield 16 antipodal face pairs.

This replaces the earlier proxy based on antipodal Q6 coordinate points. It constructs C60 face-normal data independently.

**Open:** comparison with Q6 requires an explicit group action on the 64 Q6 states, a common subgroup, and a face-to-state map. Equal dimensions alone do not imply equivalent representations. No spectral comparison is justified until the character and intertwiner tests pass.

Reproduce with:
python scripts/build_c60_face_tangent_fibres.py --out audits/C60_face_tangent_fibres.json
