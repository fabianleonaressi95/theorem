# C60 — finite jump-graph splitting: geometry and trace audit

Date: 2026-11-22. This note replaces the implicit endpoint/cap compatibility in the splitting framework with an explicit local construction. It proves the planar finite-complex statement; transfer to a polyhedral surface is by intrinsic flat charts away from cone vertices, which are excised.

## 1. Data and finite constants

Let K be a finite planar polygonal complex and let g be piecewise affine on a finite polygonal partition. Let Γ be the finite union of jump segments, subdivided so that each open edge e has two affine traces g_e^-,g_e^+ and h_e=g_e^+-g_e is affine on the plane. Choose a finite subdivision of Γ at every crossing, endpoint, and point where the incident-cell configuration changes. Let V be this finite vertex set.

For each e=[A,B], choose ρ>0 so that the vertex disks B_ρ(P), P∈V, are pairwise disjoint and meet only the incident edge pieces. Choose δ>0 with δ<ρ/4 and so that the width-δ tubular neighborhoods of nonincident truncated edges are disjoint. Since the complex and all affine traces are finite, all trace differences on the compact local patches are bounded. Denote by D_e the maximum of these bounds (including |h_e| and the differences between the proposed strip trace and the actual adjacent-cell trace); D_e<∞. This constant, not merely C_e=‖[g]‖∞, controls cap interfaces.

## 2. Truncated edge strip and layer values

Write e in intrinsic Euclidean coordinates (s,t), with s along e and t normal into the minus side. Work only on the truncated core e_ρ={ρ≤s≤|e|−ρ}. Remove endpoint disks. In the strip 0<t<δ, divide into m layers of thickness δ/m. On layer i, set

v_i=g^-_aff + (m−i+1)/m h_e, i=1,…,m,

where i=1 is adjacent to e. Outside the strip set v=g, except inside the vertex disks where no splitting is performed. The trace on e (core) is g^+; the original jump is cancelled. The outer strip boundary t=δ has residual jump h_e/m. Internal layer interfaces each have jump h_e/m. Thus there are m interfaces including the outer boundary; each has length at most |e| and amplitude at most (C_e+c_eδ)/m.

At the longitudinal ends s=ρ and s=|e|−ρ, the strip is cut off. These cap interfaces are counted in K, never in V; because they lie outside the open vertex disks and have total length at most 2δ, their jump is bounded by D_e. The portions inside B_ρ are assigned only to V. No cap trace compatibility is assumed: the actual neighboring trace is used and its difference is bounded by D_e. The construction is SBV/piecewise affine; changes between layers are jumps, not ramps, so no gradient of order δ^{-1} is introduced.

## 3. Disjoint accounting

Define:
- S: internal layer interfaces plus the outer t=δ interface, restricted to the edge core and outside vertex disks;
- K: lateral cap interfaces at s=ρ and s=|e|−ρ, and any lateral strip boundary where the strip meets the actual neighboring cells, after deleting portions in vertex disks;
- V: all jump portions in the union of vertex disks, where the original field is retained.

These are disjoint measurable subsets of the jump set by construction. Their union contains every modified jump and every jump in the vertex disks; unchanged jump portions outside the strips are counted once in the baseline energy. For a finite graph, summing over edges is legitimate. At a vertex, the disk contribution is bounded by the finite sum of incident affine jump bounds times the circumference-scale length, hence O(ρ).

## 4. Estimates

For quadratic jump density φ(t)=t², on S:
\[
E_S\le \sum_{e\in Γ}|e|\,\frac{(C_e+c_eδ)^2}{m}.
\]
On K, total cap length per edge is at most 2δ and jump amplitude at most D_e:
\[
E_K\le 2δ\sum_e D_e^2.
\]
On V:
\[
E_V\le C_Vρ,
\]
where C_V is finite and depends on the finite incident-edge trace bounds. Consequently, for fixed finite data, choose m→∞, then δ→0, ρ→0 with δ<ρ/4 and geometric separation; all three contributions vanish.

For continuous φ:[0,∞)→[0,∞), φ(0)=0, no monotonicity is needed:
\[
E_S\le \sum_e |e|m\,\sup_{0\le t\le(C_e+c_eδ)/m}φ(t)\quad
\text{(or use }φ(t)\le ε_m t\text{ if }φ(t)/t\to0),
\]
and
\[
E_K\le 2δ\sum_e\sup_{0\le t\le D_e}φ(t),\qquad
E_V\le C_Vρ\max_{e\text{ incident}}\sup_{0\le t\le D_e}φ(t).
\]
The cap and vertex terms vanish as δ,ρ→0. The S term vanishes as m→∞ under φ(t)/t→0. For the quadratic case the displayed estimates reduce to the explicit O(1/m), O(δ), O(ρ) bounds.

## 5. L1 and finite partition

The modification is supported in the union of edge strips and vertex disks. Since all affine traces are bounded on the finite compact complex, |v−g|≤D globally on the modified region. Its area is O(δ+ρ²) for fixed graph, hence v→g in L1 as δ,ρ→0. Intersecting strips/layers/caps with the original finite polygonal partition gives a finite polygonal refinement. Every piece carries an affine map, so the construction remains piecewise affine and SBV.

## 6. Intrinsic polyhedral-surface transfer

For a two-dimensional polyhedral surface, every point in the interior of a face has a Euclidean chart. Every interior point of an edge has a flat neighborhood obtained by unfolding the two incident faces; the total angle is 2π for a polyhedral surface without boundary. Therefore an edge strip crossing that edge is represented by the same planar construction in the unfolded chart. The only obstruction is a cone vertex, which is included in V and excised by B_ρ. A finite cover and a finite subdivision of the jump graph ensure that each modified edge piece lies in one such chart. On chart overlaps, the coordinate changes are rigid motions, preserving lengths, affine-layer estimates, and the S/K/V accounting.

Boundary points are treated as vertices of the relative jump complex; strips are intersected with the surface and cap estimates use the actual boundary trace. This does not assert a recovery construction for arbitrary non-polyhedral or non-flat embedded surfaces.

## 7. What this closes—and what it does not

Closed here: finite planar polygonal jump graph, explicit layer orientation, outer interface counted, cap traces bounded by actual neighboring affine traces, disjoint S/K/V accounting, finite partition refinement, and intrinsic transfer across flat polyhedral edges away from cone vertices.

Still required for the full quadratic theorem: insert this lemma into the CFI recovery partition with a fully specified common refinement; state the parameter diagonal with all geometric constraints; verify the staircase construction on each unfolded chart and trace on chart interfaces. This note does not independently claim the global theorem on Σ.
