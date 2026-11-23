# C60 — geometry A: terminal trace bound and separation of incident strips

Date: 2026-11-23  
Status: **PROVED for a finite planar polygonal jump complex with fixed affine data, under the explicit preprocessing hypotheses below.** This closes the local geometric estimates for geometry A; it does not by itself establish the full C60 splitting-to-staircase recovery theorem on the polyhedral surface.

## 1. Setting and preprocessing

Let \(K\subset\mathbb R^2\) be a compact polygonal region and let \(\mathcal T\) be a finite polygonal partition. Let \(g\) be affine on every cell of \(\mathcal T\). Assume the jump set is a finite union of straight segments. Subdivide and merge this representation so that:

1. every endpoint, crossing, T-junction, and change of the pair of one-sided affine traces is a vertex of a finite embedded polygonal graph \(\Gamma\);
2. the relative interiors of distinct graph edges are disjoint;
3. collinear overlapping copies of the same geometric edge have been merged, and an edge is not counted twice;
4. each edge \(e\) has a fixed pair of affine extensions \(g_e^-,g_e^+\) from its two incident cells, with \(h_e=g_e^+-g_e^-\).

All statements below are local to a fixed finite complex and its fixed affine data. The constants may depend on that data, but not on \(m,\delta,\rho\).

For every graph vertex \(P\), list the distinct outgoing unit rays \(t_{P,1},\ldots,t_{P,N_P}\). If \(N_P\ge2\), set
\[
\alpha_P:=\min_{i\ne j}\arccos(t_{P,i}\cdot t_{P,j})>0.
\]
The strict positivity follows because the list is finite and duplicate rays were merged. Vertices with one incident ray impose no angular separation condition.

Choose a polygon \(Q_1\) containing the origin in its interior, with
\[
B_{c_0}(0)\subset Q_1\subset B_{C_0}(0),
\qquad \mathcal H^1(\partial Q_1)=L_0<\infty,
\]
and put \(Q_\rho(P)=P+\rho Q_1\). Since the graph is finite, choose \(\rho_0>0\) so that the terminal polygons \(Q_\rho(P)\) are pairwise disjoint for \(0<\rho<\rho_0\), and remain inside the chosen local planar charts.

## 2. Geometry A and the exact trace on the terminal boundary

For an oriented edge \(e=[P,P']\), let \(S_\delta(e)\) be its one-sided strip of width \(\delta\), and define the active splitting region
\[
D_{e,\delta,\rho}:=S_\delta(e)\setminus
\bigl(Q_\rho(P)\cup Q_\rho(P')\bigr).
\]
Assume \(\delta<c_0\rho\). Then each short lateral end of the full strip at an endpoint is contained in the corresponding terminal polygon: every point on that end is within distance \(\delta<c_0\rho\) of the endpoint. Thus there is **no lateral cap segment outside the terminal polygons** and no separate \(K\)-term in geometry A.

On the active part of the strip, split into \(m\) layers, numbered from the original jump toward the outer edge, and set
\[
v=g_e^-+\theta_i h_e,\qquad
\theta_i=\frac{m-i+1}{m}\in[0,1].
\]
Outside the union of active splitting regions and inside terminal polygons set \(v=g\). The trace on the original edge is matched because \(\theta_1=1\). The outer strip edge and the internal layer interfaces carry the expected jumps \(h_e/m\) (with the outer edge compared to the unmodified \(g_e^-\) trace).

The only new boundary created by switching the splitting off at a terminal polygon is the portion of \(\partial Q_\rho(P)\) adjacent to an active strip. On its two sides the actual traces are:
- the unmodified trace of \(g\) on the terminal-polygon side;
- the active layer trace \(g_e^-+\theta_i h_e=(1-\theta_i)g_e^-+\theta_i g_e^+\) on the strip side.

This identifies the actual trace difference; it is not replaced by \(h_e\) unless the two traces happen to be the original edge pair.

## 3. Uniform affine-trace bound

Fix a compact neighborhood \(K_P\) containing \(Q_\rho(P)\) and all strip portions meeting it for every \(0<\rho\le\rho_0\) and \(0<\delta<c_0\rho\). Such a compact neighborhood can be fixed once, for example by taking a sufficiently large closed ball about \(P\) and reducing \(\rho_0\) if necessary.

Let \(\mathcal A_P\) be the finite collection of affine extensions of the cellwise values of \(g\) whose cells meet this neighborhood or are incident to an edge ending at \(P\). Define
\[
M_P:=\max_{F,G\in\mathcal A_P}
\sup_{x\in K_P}|F(x)-G(x)|<\infty.
\tag{3.1}
\]
This is a maximum over a finite family of continuous functions on a fixed compact set.

On a terminal boundary piece adjacent to edge \(e\), the strip-side trace is the convex combination
\((1-\theta_i)g_e^-+\theta_i g_e^+\), while the other trace is one member \(G\) of \(\mathcal A_P\). Hence, pointwise,
\[
\begin{aligned}
|(1-\theta_i)g_e^-+\theta_i g_e^+-G|
&\le (1-\theta_i)|g_e^--G|+\theta_i|g_e^+-G|\\
&\le M_P.
\end{aligned}
\tag{3.2}
\]
Crucially, (3.2) is uniform in the layer index \(i\), hence in \(m\), and uniform in \(\delta,\rho\) in the stated range. It does not assume that the exterior trace equals \(g_e^-\).

Since \(\mathcal H^1(\partial Q_\rho(P))=L_0\rho\), the actual quadratic cost on the artificial terminal boundary is bounded by
\[
E_{\partial V(P)}
:=\int_{\partial Q_\rho(P)\cap J_v}|[v]|^2\,d\mathcal H^1
\le L_0\rho M_P^2.
\tag{3.3}
\]
The number of intersections of the boundary with layer interfaces may depend on \(m\), but this does not affect (3.3): the pieces partition a subset of the same boundary, their total length is at most \(L_0\rho\), and the pointwise bound is uniform.

The original jump retained inside the terminal polygon is also controlled. If \(N_P\) is the number of graph edges incident to \(P\), each such edge contributes length at most \(2C_0\rho\) inside \(Q_\rho(P)\), and its jump is bounded by \(M_P\). Therefore
\[
E_{J_g\cap Q_\rho(P)}
\le 2C_0N_P\rho M_P^2.
\tag{3.4}
\]
Combining (3.3) and (3.4), the terminal contribution at \(P\) is at most
\[
E_{V(P)}\le (L_0+2C_0N_P)\rho M_P^2.
\tag{3.5}
\]
Summing over the finite vertex set gives \(E_V\le C_\Gamma\rho\), where
\[
C_\Gamma:=\sum_{P\in V(\Gamma)}
(L_0+2C_0N_P)M_P^2
\]
is finite and independent of \(m,\delta,\rho\).

## 4. Disjointness of active strips outside terminal polygons

Let \(e,e'\) be distinct edges incident to the same vertex \(P\), with outgoing angle \(\alpha\in(0,\pi]\). Every point in either one-sided strip is within distance \(\delta\) of its supporting ray. If such a point lies outside \(Q_\rho(P)\), its projection parameter on the ray is at least \(c_0\rho-\delta\), because \(Q_\rho(P)\) contains \(B_{c_0\rho}(P)\). The distance between the two truncated supporting rays, with radial parameters at least \(r>0\), is bounded below by \(2r\sin(\alpha/2)\). Consequently the distance between the two strip portions outside the terminal polygon is bounded below by
\[
2(c_0\rho-\delta)\sin(\alpha/2)-2\delta.
\tag{4.1}
\]
In particular it is positive if
\[
\delta<
\frac{c_0\rho\sin(\alpha/2)}
{1+\sin(\alpha/2)}.
\tag{4.2}
\]
A simpler uniform sufficient condition for all incident pairs is
\[
\delta<\frac{c_0}{4}\rho
\min_{P:N_P\ge2}\sin(\alpha_P/2).
\tag{4.3}
\]
If there are no vertices of valence at least two, the angular factor is omitted.

For nonincident edges, after the preprocessing in §1 their compact supporting segments are disjoint. There are finitely many such pairs, so their minimum separation \(d_*>0\) is positive. Their width-\(\delta\) strips are disjoint whenever \(2\delta<d_*\). Thus the combined choice
\[
0<\delta<
\min\left\{
c_0\rho/2,\frac{c_0\rho}{4}
\min_{P:N_P\ge2}\sin(\alpha_P/2),d_*/3
\right\}
\tag{4.4}
\]
(with absent minima omitted) ensures disjoint active strips outside the terminal polygons. The same argument applies at a boundary endpoint after using the corresponding one-sided local chart.

## 5. Consequence for the splitting jump budget

Under the exact geometry A construction above, every positive-length jump segment belongs to exactly one of:
- an internal layer interface or the outer strip edge (the \(S\)-family);
- the original jump set outside active strips and terminal polygons;
- a terminal polygon boundary or the original jump inside a terminal polygon (the \(V\)-family).

There is no lateral-cap family \(K\) outside the terminal polygons. Intersections at isolated points are \(\mathcal H^1\)-null. The disjointness estimate in §4 prevents positive-length overlap between distinct active strips. Within one strip the layer interfaces are parallel and distinct. Hence the splitting-stage jump energy can be summed without double counting:
\[
E_{J_v}
\le E_{\rm outside}(g)
+\sum_{e\in E(\Gamma)}
\frac{|e|(C_e+c_e\delta)^2}{m}
+C_\Gamma\rho,
\tag{5.1}
\]
where \(C_e=\|[g]\|_{L^\infty(e)}\), \(c_e\) depends on the fixed affine gradient of \(h_e\), and \(C_\Gamma\) is defined after (3.5). The outer-edge term is included in the layer count, as in the established estimate (S).

For fixed graph and affine data, first choose \(\rho\downarrow0\), then choose \(\delta\) satisfying (4.4) and \(\delta/\rho\to0\), and choose \(m\to\infty\) so that the finite sum in (5.1) tends to zero. The local construction also gives \(v\to g\) in \(L^1\), since the modified area is \(O(\delta)+O(\rho^2)\) and the affine data are bounded on the fixed compact set.

## 6. Scope and remaining transfer obligations

The proof above establishes the terminal trace and strip-disjointness estimates for a finite planar polygonal jump complex with fixed affine data. To use it in the full C60 argument on \(\Sigma\), one must still verify for the actual \(g_j\) and its mesh that:
1. the jump complex can be subdivided exactly as in §1, including face-edge crossings, chart transitions, and conical vertices;
2. each local neighborhood is represented in a flat chart or by an explicit intrinsic unfolding, with all chart/face seams placed in the common skeleton;
3. the finite affine trace collection used to define \(M_P\) includes every cell whose trace can meet a terminal boundary;
4. the chosen terminal polygons remain within the relevant charts and are pairwise disjoint.

These are finite-data checks for each fixed CFI stage, but they must be recorded for the actual stage; they are not consequences of the planar lemma alone.

**Status:** terminal bound (3.5) and angular disjointness (4.4) are proved under §§1–2. The transfer checks in §6 remain open until verified against the actual C60 mesh. The global quadratic-jump recovery theorem is therefore not asserted here.
