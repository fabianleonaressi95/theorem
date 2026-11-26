# C60 — diagonal recovery lemma for quadratic jump cost

Date: 2026-11-23. This note gives the parameter order and the dependence of constants required to turn the finite jump-graph splitting into a recovery sequence. It is a planar finite-complex lemma; the polyhedral-surface transfer is stated with the chart-seam conditions that must be checked.

## 1. Fixed-stage data

Let Σ be a compact polygonal surface, and let g_j be a piecewise-affine SBV approximation on a finite polygonal partition, with G_j piecewise constant on a common finite refinement. Assume
\[
g_j\to g\quad L^1,\qquad \nabla g_j\to\nabla g\quad L^p,\qquad G_j\to G\quad L^p,
\]
where p=1 for W(F)=|F| and p=2 for W(F)=|F|². For each fixed j, the jump graph Γ_j is finite and all traces are affine on its subdivided edges.

All constants below are stage-dependent and finite. Let:
- N_j be the number of edge pieces and vertices;
- C_j bound the jump amplitudes on Γ_j;
- L_j bound the total jump-graph length;
- D_j bound every actual cap/chart-seam trace difference in the construction (not just the original jump);
- V_j bound the coefficient of the vertex-disk jump cost;
- Q_j bound the SVD mismatch norms and the finite-cell staircase trace constants;
- d_j>0 be the minimum separation between nonincident graph pieces and distinct vertices, after subdivision.

These are finite for fixed j because the graph, common partition, and affine traces are finite and compact. No uniform bound in j is assumed or needed.

## 2. Fixed-stage estimates

For m layers, vertex radius ρ, strip width δ, and staircase mesh h, the quadratic jump cost of the constructed field u_{j,m,ρ,δ,h} is bounded by
\[
E_J\le \underbrace{L_j(C_j+c_jδ)^2/m}_{S}
+\underbrace{2N_jδD_j^2}_{K}
+\underbrace{V_jρ}_{V}
+\underbrace{R_j(m,ρ,δ,h)}_{\text{finite partition/staircase residual}}.
\]
Here the constants c_j,N_j,D_j,V_j are fixed once j and the finite graph/chart refinement are fixed. The cap estimate uses the actual trace difference on the cap, bounded by D_j; it is not inferred from C_j alone. The S/K/V sets are chosen disjoint up to H¹-null boundaries; those boundaries carry no jump-energy mass unless they are themselves jump segments, in which case they are assigned to exactly one class.

The residual is controlled at fixed (j,m,ρ,δ) by the staircase:
\[
R_j(m,ρ,δ,h)\le A_{j,m,ρ,δ}h+B_{j,m,ρ,δ}h^2,
\]
with finite coefficients. This estimate includes the coarea cost of the SVD laminates and the perturbation of the finite splitting interfaces/cap traces. The construction must verify these coefficients for the chosen common partition; their finiteness, not uniformity, is what the diagonal uses.

The determinant error satisfies
\[
\|u_{j,m,ρ,δ,h}-v_{j,m,ρ,δ}\|_{L^1}
\le |Σ|\,hQ_{j,m,ρ,δ},
\]
where Q is finite at the fixed stage. The intermediate splitting field satisfies
\[
\|v_{j,m,ρ,δ}-g_j\|_{L^1}
\le M_j(δL_j+ρ^2N_j),
\]
for a finite bound M_j on the modified region.

For the gradient measure, the staircase is constructed cellwise with ∇u=G_j H²-a.e. Thus
\[
\nabla_Σu\,H²=G_jH²
\]
exactly; convergence to G H² follows from G_j→G in L¹. For the quadratic bulk, ∫|∇u|²=∫|G_j|² exactly, and the L² convergence of G_j gives the bulk limit.

## 3. Quantified diagonal choice

Let ε_j=2^{-j}. Choose parameters in the following order.

**(i) Layer number.** Choose m_j so large that
\[
L_j(C_j+1)^2/m_j<ε_j/8.
\]
If the local constants c_jδ are not yet bounded by 1, this is imposed after δ_j is selected; equivalently choose m_j using L_j(C_j+c_j)^2.

**(ii) Vertex radius.** Choose ρ_j>0 such that
\[
ρ_j<\min(ε_j/(8(V_j+1)),d_j/8,1/j)
\]
and the vertex contribution V_jρ_j<ε_j/8.

**(iii) Strip width.** Choose δ_j>0 such that
\[
δ_j<\min(ρ_j/4,d_j/8,1/j,ε_j/(16N_j(D_j^2+1))),
\]
and small enough that L_j(C_j+c_jδ_j)^2/m_j<ε_j/4 and the modified-region L¹ bound is <ε_j/8. This makes K<ε_j/8 and enforces geometric separation. If terminal truncation has an additional parameter r_j, choose it at this stage with its finite terminal constant times r_j<ε_j/8 and r_j<ρ_j/4.

**(iv) Staircase mesh.** Freeze j,m_j,ρ_j,δ_j and the finite common partition. Choose h_j>0 so small that
\[
A_{j,m_j,ρ_j,δ_j}h_j+B_{j,m_j,ρ_j,δ_j}h_j²<ε_j/8,
\[
h_jQ_{j,m_j,ρ_j,δ_j}<ε_j/(8(|Σ|+1)),
\]
and all finite interface-trace perturbations are <ε_j/8. No uniformity in j is invoked: each coefficient is finite, and h_j is chosen last.

With these choices, the quadratic jump cost tends to zero and the determinant error tends to zero. The total recovery energy obeys
\[
E(u_j)\le \int_ΣW(G_j)\,dH²+ε_j,
\]
while u_j→g in L¹ and ∇u_jH²⇀*GH². For W=|F|² the stronger convergence G_j→G in L² gives convergence of bulk energies; for W=|F|, L¹ convergence suffices.

## 4. What must be checked in the surface implementation

This lemma does not silently assume a global planar chart. To transfer it to a compact polyhedral surface:
1. subdivide each jump edge at face-edge crossings and at chart changes;
2. unfold each flat edge neighborhood into a plane;
3. include chart-seam traces in D_j and the finite residual coefficients A,B;
4. excise cone vertices with the disks counted in V;
5. choose strips so their interiors are disjoint; assign all H¹-relevant interfaces on their boundaries exactly once.

The finite number of pieces at fixed j makes all constants finite. The diagonal absorbs their growth with j. The global theorem is justified only once the specific staircase construction verifies the residual estimate in §2 on this common refinement.

## 5. Status

The parameter-selection principle and the dependence on stage constants are rigorous once the fixed-stage estimates in §2 are established. The key point is that D_j,N_j,V_j,A_j,B_j,Q_j may grow arbitrarily with j: the order j → (m_j,ρ_j,δ_j) → h_j avoids any uniform-in-j assertion.

This note is a diagonal lemma, not a claim that all fixed-stage cap/chart-seam estimates have already been verified for the current CFI partition. That verification is the remaining integration audit.
