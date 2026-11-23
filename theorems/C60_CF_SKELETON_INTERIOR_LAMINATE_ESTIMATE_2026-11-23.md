# C60 — skeleton/interior decomposition for the staircase jump measure

Date: 2026-11-23  
Status: **CONDITIONAL LEMMA — resolves staircase overlap accounting under an exact common polygonal refinement; does not by itself certify the preceding splitting geometry.**

## 1. Geometric setup

Fix a stage of the C60 construction. Let \(\mathcal P=\{P\}\) be a finite polygonal partition of the flat polyhedral surface (or a finite collection of planar charts with all chart/face seams included in the partition skeleton). Assume:

1. the intermediate splitting field \(v\) is affine on each \(P\);
2. every jump of \(v\), every boundary of a cap/terminal/vertex region, every boundary of a splitting strip, and every chart or face seam carrying a trace discontinuity is contained in the one-dimensional skeleton
   \[
   \mathscr S:=\bigcup_{P\in\mathcal P}\partial P;
   \]
3. on each cell \(P\), the staircase field is defined by
   \[
   u_h|_P(x)=G_Px+b_{P,h}
   +\sum_{k=1}^{r_P}\sigma_{P,k}a_{P,k}
   h\left\lfloor\frac{x\cdot\nu_{P,k}}h\right\rfloor,
   \]
   with the offset chosen as in the explicit offset construction, so that
   \[
   r_{P,h}:=u_h-v,\qquad
   \|r_{P,h}\|_{L^\infty(P)}
   \le 2h\sum_{k=1}^{r_P}\sigma_{P,k}.
   \tag{1.1}
   \]
4. all one-sided traces of \(v\) on the finite skeleton are bounded.

The refinement in item 2 is essential: if a terminal boundary or chart seam is not already a cell boundary, refine \(\mathcal P\) along it before applying the staircase. The lemma does not assume that such a refinement has already been carried out automatically.

## 2. Skeleton estimate: all inherited and terminal jumps are counted once

Let \(e\subset\mathscr S\) be an open interface segment assigned to its unique adjacent cell pair \(P^+,P^-\). Write
\[
a_e=[v],\qquad
\eta_e=[u_h]-[v]=r_{P^+,h}-r_{P^-,h}.
\]
By (1.1),
\[
\|\eta_e\|_{L^\infty(e)}
\le hq_e,\qquad
q_e:=2\sum_k\sigma_{P^+,k}
+2\sum_k\sigma_{P^-,k}.
\tag{2.1}
\]
Consequently,
\[
\begin{aligned}
\int_e|[u_h]|^2\,d\mathcal H^1
&=\int_e|a_e+\eta_e|^2\,d\mathcal H^1\\
&\le \int_e|[v]|^2\,d\mathcal H^1
+2h\,\mathcal H^1(e)\|[v]\|_{L^\infty(e)}q_e
+h^2\mathcal H^1(e)q_e^2.
\end{aligned}
\tag{2.2}
\]
Since the skeleton has finitely many segments at the frozen stage,
\[
\int_{\mathscr S\cap J_{u_h}}|[u_h]|^2\,d\mathcal H^1
\le
\int_{\mathscr S}|[v]|^2\,d\mathcal H^1
+C_{\mathcal P,v}h+D_{\mathcal P}h^2.
\tag{2.3}
\]
Here the constants are the explicit finite sums of the coefficients in (2.2).

This estimate uses the **total** trace difference of \(u_h\) on every skeleton segment. It therefore includes, without a separate addition, any staircase laminate that coincides for positive length with a cell boundary, inherited jump, cap boundary, terminal boundary, vertex-disk boundary, or chart seam. Such a coincident segment is assigned to the skeleton, not to the interior-laminate family.

In particular, terminal contributions are not an extra undefined \(R_{\rm terminal}\): they are part of the skeleton baseline \(\int_{\mathscr S}|[v]|^2\), which must itself be estimated by the splitting construction (including its cap and vertex terms).

## 3. Interior laminate estimate, with coincident directions grouped

For a cell \(P\), consider only staircase jump sections lying in the relative interior \(P^\circ\). For each SVD direction \(\nu_{P,k}\), the jump sections are
\[
P^\circ\cap\{x:x\cdot\nu_{P,k}=nh\},\qquad n\in\mathbb Z.
\]
If two SVD directions generate the same geometric family of lines (in particular \(\nu\) and \(-\nu\)), their contributions must be grouped before squaring. For each distinct unoriented direction class \(\alpha\), let \(I_\alpha\) be its index set and put
\[
A_\alpha:=\sum_{k\in I_\alpha}\sigma_{P,k}a_{P,k}.
\]
On each line in that class, the total jump contribution is \(hA_\alpha\), not a list of independent jumps. Hence
\[
\int_{\Lambda_{\alpha,P,h}}|[u_h]|^2\,d\mathcal H^1
=h^2|A_\alpha|^2\,
\mathcal H^1\!\left(
P^\circ\cap\bigcup_{n\in\mathbb Z}
\{x:x\cdot\nu_\alpha=nh\}\right).
\tag{3.1}
\]
For a fixed polygon and direction, slicing gives
\[
\mathcal H^1\!\left(
P\cap\bigcup_{n\in\mathbb Z}
\{x:x\cdot\nu_\alpha=nh\}\right)
\le \frac{|P|}{h}+C_{P,\alpha},
\tag{3.2}
\]
with a finite geometry-dependent constant. Thus
\[
\int_{\Lambda_{\alpha,P,h}}|[u_h]|^2\,d\mathcal H^1
\le h|P||A_\alpha|^2
+h^2C_{P,\alpha}|A_\alpha|^2.
\tag{3.3}
\]
There are finitely many cells and direction classes, so the sum of (3.3) is \(O(h)+O(h^2)\) at the frozen stage.

Intersections of nonparallel laminate lines have \(\mathcal H^1\)-measure zero. Coincident parallel families are grouped as above. Any laminate section coinciding with \(\partial P\) is excluded from \(P^\circ\) and already counted in (2.3).

## 4. Actual jump-set partition and fixed-stage inequality

Under the assumptions of §1, and provided the cellwise staircase has no other discontinuity mechanisms, the actual jump set is contained, up to \(\mathcal H^1\)-null sets, in
\[
J_{u_h}\subset
\mathscr S\ \cup\
\bigcup_{P\in\mathcal P}\bigcup_{\alpha}
\Lambda_{\alpha,P,h}.
\tag{4.1}
\]
Use the disjoint assignment
\[
E_{\rm skel}:=J_{u_h}\cap\mathscr S,\qquad
E_{\rm int}:=J_{u_h}\setminus\mathscr S.
\]
Within \(E_{\rm int}\), group coincident laminate lines by their unoriented direction class. Distinct nonparallel lines intersect only in points, hence the groups are disjoint up to \(\mathcal H^1\)-null sets. It follows from (2.3) and (3.3) that
\[
\boxed{
\mu_h(\Sigma)
\le
\int_{\mathscr S}|[v]|^2\,d\mathcal H^1
+C_{\mathcal P,v}h
+D_{\mathcal P}h^2
+\sum_{P,\alpha}
\left(h|P|+h^2C_{P,\alpha}\right)|A_\alpha|^2.
}
\tag{4.2}
\]
In particular, for the frozen partition,
\[
\mu_h(\Sigma)
\le
\int_{\mathscr S}|[v]|^2\,d\mathcal H^1
+O_{\mathcal P,v}(h).
\tag{4.3}
\]

Equation (4.2) is a fixed-stage bound for the staircase **conditional on the exact common-refinement and jump-set hypotheses in §1**. It resolves the specific seam/laminate overlap issue: the skeleton estimate controls the total jump on every coincident segment, while the laminate estimate is applied only in cell interiors. It also accounts for terminal and cap boundaries provided they were included in the skeleton and their inherited energy is included in \(\int_{\mathscr S}|[v]|^2\).

## 5. What remains to prove for the global recovery argument

The lemma does not prove that the intermediate splitting field \(v\) has small skeleton energy. One still needs the preceding splitting construction to establish, with a genuinely disjoint geometric accounting,
\[
\int_{\mathscr S}|[v]|^2\,d\mathcal H^1
\le
E_{\rm outside}(g_j)
+E_S(m,\delta,\rho)
+E_K(\delta,\rho)
+E_V(\rho),
\tag{5.1}
\]
with the exact supports and traces of the strip interfaces, outer strip edges, lateral caps, terminal pieces, and vertex disks specified. In particular:

- the layer indexing must be consistent: \(S_1\) is adjacent to the original jump, so its coefficient is \(1\);
- the terminal/cap regions must be cells of the common refinement, or be added to it;
- all physical face/chart seams must be included or proved to carry no jump;
- the actual trace on each skeleton segment must be the one used in (2.2).

The current splitting framework contains duplicate, incompatible layer formulas; this has to be corrected before (5.1) can be treated as a verified estimate. This note does not promote the complete fixed-stage estimate or the global recovery sequence to a theorem.

## 6. Status

- **PROVED under §1:** skeleton cross-term estimate (2.3).
- **PROVED for fixed polygonal cells:** interior laminate estimate (3.3), including coincident SVD directions after grouping.
- **CONDITIONAL:** fixed-stage staircase estimate (4.2).
- **OPEN:** verification of the exact common refinement for the full C60 splitting construction and the disjoint estimate (5.1) for its intermediate field.
- **NOT PROVED:** unconditional global fixed-stage recovery estimate and global recovery sequence.

The point of this reduction is that the staircase overlap problem need not be handled by separately estimating inherited, laminate, overlap, and terminal mechanisms. It is enough to assign the entire partition skeleton once, estimate its actual total traces by (2.2), and estimate only the laminate sections strictly inside each cell.
