# C60 — geometric decomposition of the actual quadratic jump measure

Date: 2026-11-23  
Status: **OPEN — local estimates established; global fixed-stage estimate not proved.**

## 1. Purpose and scope

This note isolates the remaining geometric issue in the quadratic-jump recovery construction. It does not assert a fixed-stage recovery estimate and does not promote the diagonal recovery argument to a global recovery theorem.

For a fixed stage and a fixed staircase mesh \(h>0\), let \(u_h\in SBV(\Sigma;\mathbb R^q)\) be the field produced by the proposed cellwise construction. Its actual jump-energy measure is
\[
\mu_h(A):=\int_{J_{u_h}\cap A}|[u_h]|^2\,d\mathcal H^1,
\qquad A\subset\Sigma\ \text{Borel}.
\]
Every estimate below must concern this measure, hence the actual total trace difference of \(u_h\). Measures or costs assigned separately to the mechanisms that generate jumps may not be added on overlapping supports without accounting for their cross terms.

The target fixed-stage statement would be an estimate
\[
\mu_h(\Sigma)\le E_{\mathrm{inherited}}(v)
+\varepsilon_{\mathrm{stage}}(h),
\qquad
\varepsilon_{\mathrm{stage}}(h)\longrightarrow0
\quad(h\downarrow0),
\tag{1.1}
\]
where \(v\) is the intermediate splitting field and \(E_{\mathrm{inherited}}(v)\) is explicitly defined on its actual jump set. **Statement (1.1) is not established in this note.**

## 2. Local offset estimate — established

Fix a polygonal cell \(P\), an affine intermediate field
\[
v_P(x)=A_Px+c_P,
\]
and a target matrix \(G_P\). Put \(M_P=A_P-G_P\) and choose a singular-value decomposition
\[
M_P=\sum_{k=1}^{r_P}\sigma_{P,k}\,a_{P,k}\otimes\nu_{P,k}.
\]
For a mesh \(h>0\), define
\[
S_{P,h}(x)=\sum_{k=1}^{r_P}\sigma_{P,k}a_{P,k}
h\left\lfloor\frac{x\cdot\nu_{P,k}}h\right\rfloor,
\qquad
T_{P,h}(x)=S_{P,h}(x)-M_Px.
\]
Choose a reference point \(x_P\) in the cell and set
\[
b_{P,h}=c_P+M_Px_P-S_{P,h}(x_P),\qquad
u_{P,h}(x)=G_Px+b_{P,h}+S_{P,h}(x).
\]
Then \(r_{P,h}:=u_{P,h}-v_P\) satisfies
\[
r_{P,h}(x)=T_{P,h}(x)-T_{P,h}(x_P).
\]
Since
\[
\left|h\left\lfloor t/h\right\rfloor-t\right|\le h,
\]
the triangle inequality gives
\[
\|r_{P,h}\|_{L^\infty(P)}
\le 2h\sum_{k=1}^{r_P}\sigma_{P,k}.
\tag{2.1}
\]
This is a fixed-cell estimate. It requires the stated affine representation of \(v_P\) and the explicit offset choice above.

## 3. Common partition interfaces — established conditionally on trace assignment

Let \(\mathcal P\) be the frozen finite polygonal partition, and let \(e\) be a common interface assigned to the unique adjacent cell pair \(P,P'\). Assume \(v\) has the indicated one-sided traces on \(e\). From (2.1),
\[
[u_h]-[v]=r_{P,h}-r_{P',h}
\quad\mathcal H^1\text{-a.e. on }e,
\]
and therefore
\[
\|[u_h]-[v]\|_{L^\infty(e)}
\le hq_e,\qquad
q_e:=2\sum_k\sigma_{P,k}+2\sum_k\sigma_{P',k}.
\tag{3.1}
\]
Writing \(a_e=[v]\) and \(\eta_e=[u_h]-[v]\), one obtains
\[
\begin{aligned}
\int_e|[u_h]|^2\,d\mathcal H^1
&=\int_e|a_e+\eta_e|^2\,d\mathcal H^1\\
&\le \int_e|a_e|^2\,d\mathcal H^1
+2h\,\mathcal H^1(e)\|a_e\|_{L^\infty(e)}q_e
+h^2\mathcal H^1(e)q_e^2.
\end{aligned}
\tag{3.2}
\]
Summing (3.2) over the finite family of assigned common interfaces yields a residual \(R_{\rm seam}(h)=O(h)+O(h^2)\) for the frozen partition. This conclusion presupposes that each interface is assigned once and that the required traces are bounded.

Equation (3.2) controls the actual total jump on these interfaces. It does not by itself control the rest of \(J_{u_h}\).

## 4. Internal laminate length and cost — local \(O(h)\) estimate

For a fixed polygon \(P\) and one SVD direction \(\nu_{P,k}\), let
\[
\Lambda_{P,k,h}
=P\cap\bigcup_{n\in\mathbb Z}
\{x:x\cdot\nu_{P,k}=nh\}.
\]
For a fixed polygon, slicing in direction \(\nu_{P,k}\) gives a finite-geometry estimate of the form
\[
\mathcal H^1(\Lambda_{P,k,h})
\le \frac{|P|}{h}+C_{P,k},
\tag{4.1}
\]
where \(C_{P,k}<\infty\) depends on the polygon and direction, not on \(h\) for sufficiently small \(h\). On a laminate segment away from cell-boundary coincidences, the staircase jump has amplitude \(h\sigma_{P,k}a_{P,k}\). Its separately computed quadratic cost is consequently bounded by
\[
h^2\sigma_{P,k}^2\mathcal H^1(\Lambda_{P,k,h})
\le h|P|\sigma_{P,k}^2
+h^2C_{P,k}\sigma_{P,k}^2.
\tag{4.2}
\]
For finitely many cells and SVD directions, the right-hand side is \(O(h)\) at fixed stage.

This is a bound for the laminate contribution on the indicated sections. It is **not** yet a bound for the actual total jump energy on sections where an inherited jump, a cell seam, a chart seam, or a terminal boundary coincides with a laminate. On such a section the jump is the sum of all applicable trace contributions.

## 5. Required geometric decomposition of the actual jump set

A complete proof must construct, for each fixed \(h\), a measurable partition up to \(\mathcal H^1\)-null sets
\[
J_{u_h}
=E_{\rm inherited}\,\dot\cup\,
E_{\rm laminate}\,\dot\cup\,
E_{\rm overlap}\,\dot\cup\,
E_{\rm terminal}.
\tag{5.1}
\]
The sets must be specified as subsets of the actual jump set, not merely as labels for construction mechanisms. Every jump segment must be assigned exactly once. Intersections consisting only of points may be discarded as \(\mathcal H^1\)-null; coincident segments may not.

On each piece, the proof must identify the actual one-sided traces of \(u_h\) and estimate their difference:

1. **Inherited pieces.** Specify the portion of the intermediate jump set retained by the construction. If \([u_h]=a_e+\eta_e\), prove an integral bound for this total jump, including the cross term.
2. **Laminate-only pieces.** Specify the portions of the staircase sections on which no inherited or other jump mechanism contributes. Apply the geometric count (4.1) there.
3. **Overlap pieces.** Identify every positive-\(\mathcal H^1\) coincidence, including inherited jump/laminate coincidences and laminate/cell-seam or laminate/chart-seam coincidences. If
   \[
   [u_h]=a_e+\ell_e+\eta_e,
   \]
   estimate directly
   \[
   \int_e|a_e+\ell_e+\eta_e|^2\,d\mathcal H^1.
   \tag{5.2}
   \]
   For example, a valid estimate may use
   \[
   \|a_e+\ell_e+\eta_e\|_{L^2(e)}^2
   \le
   \bigl(\|a_e\|_{L^2(e)}
   +\|\ell_e\|_{L^2(e)}
   +\|\eta_e\|_{L^2(e)}\bigr)^2,
   \]
   but the resulting cross terms and their dependence on \(h\) must then be controlled. It is not valid to add the separate squared costs while omitting these terms.
4. **Terminal pieces.** Define the terminal support, its boundary geometry, and the actual traces on both sides. Prove a bound of the form
   \[
   \int_{E_{\rm terminal}}|[u_h]|^2\,d\mathcal H^1
   \le \tau_{\rm terminal}(h),
   \tag{5.3}
   \]
   with an explicit parameter dependence and a demonstrated limit or prescribed smallness. A symbol \(R_{\rm terminal}\) without this definition and estimate is not a proof.

The construction must also state how chart boundaries, face-edge crossings, vertex-disk boundaries, and cell boundaries are treated. If any of these carry a positive-\(\mathcal H^1\) jump, they must be assigned to one class in (5.1) and their actual total traces estimated.

## 6. Fixed-stage proof obligation

The remaining obligation is to combine the estimates on the disjoint sets in (5.1), using the actual jump on each set, to prove
\[
\begin{aligned}
\mu_h(\Sigma)
={}&\int_{E_{\rm inherited}}|[u_h]|^2\,d\mathcal H^1
+\int_{E_{\rm laminate}}|[u_h]|^2\,d\mathcal H^1\\
&+\int_{E_{\rm overlap}}|[u_h]|^2\,d\mathcal H^1
+\int_{E_{\rm terminal}}|[u_h]|^2\,d\mathcal H^1\\
\le{}& E_{\rm inherited}(v)+
R_{\rm seam}(h)+R_{\rm laminate}(h)
+R_{\rm overlap}(h)+R_{\rm terminal}(h),
\end{aligned}
\tag{6.1}
\]
where every residual is explicitly defined and the sum of residuals tends to zero as \(h\downarrow0\) at the frozen stage, or is bounded by a separately chosen terminal parameter tending to zero in the subsequent parameter selection.

No such complete decomposition and set of estimates is supplied here. In particular, (3.2) and (4.2) do not imply (6.1): they concern different construction mechanisms and do not resolve their positive-length overlaps.

## 7. Status and relation to the diagonal argument

- **ESTABLISHED:** the explicit offset bound (2.1).
- **ESTABLISHED under the stated trace and assignment hypotheses:** the common-interface estimate (3.2), hence \(R_{\rm seam}(h)\to0\) for a frozen finite partition.
- **LOCAL ESTIMATE:** the internal laminate cost bound (4.2) on laminate-only sections of a fixed polygonal cell.
- **OPEN:** the disjoint decomposition (5.1), the total-jump estimate on overlap pieces, and the terminal estimate (5.3).
- **NOT PROVED:** the global fixed-stage inequality (6.1).
- **CONDITIONAL:** the global quadratic-jump recovery sequence and any diagonal argument that uses (6.1).

A diagonal selection can absorb stage-dependent constants only after the fixed-stage estimate has been proved. It cannot supply the missing geometric decomposition, remove cross terms on coincident segments, or control an undefined terminal contribution. Accordingly, any diagonal recovery statement relying on a residual estimate that has not been verified for the actual common partition must remain conditional.

**No theorem-level recovery claim follows from this note.**