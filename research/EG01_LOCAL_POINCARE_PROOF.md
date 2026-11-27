# EG-01: local path congestion and a uniform discrete Poincare estimate

**Status:** first proof note for the strengthened, boundary-complete version of (G1)-(G5). It proves local path congestion, nonlocal-energy domination, Poincare, and L2 compactness. The companion `EG01_H1_INTERPOLATION_AND_INTEGRAL_REPRESENTATION.md` now derives the H1 interpolation, upper growth, and fundamental estimate.

## 1. Main conclusion

The previous bottleneck diagnostic does not test the full path-tube hypothesis. In fact, (G2) and (G5) together imply a useful quantitative fact that was not extracted in the first framework draft:

> For every fixed (R<\infty), all pairs of vertices at distance at most (R\varepsilon) can be connected by paths of uniformly bounded length, and the family of such paths has uniformly bounded edge congestion.

Consequently, if the vertex set is also uniformly dense up to the boundary, the graph energy controls a standard nonlocal (L^2) difference quotient. This yields a uniform discrete Poincare inequality (modulo constants) and strong (L^2) precompactness.

The boundary-complete density assumption is important: the earlier interior-only version of (G3) does not by itself control the boundary Voronoi cells.

## 2. Hypotheses

Let (\Omega\subset\mathbb R^d) be bounded, connected, and Lipschitz. For (\varepsilon\downarrow0), let (V_\varepsilon\subset\overline\Omega) be finite and let (G_\varepsilon=(V_\varepsilon,E_\varepsilon)).

Assume:

- **(S) separation:** ( |x-y|\ge c_s\varepsilon) for distinct vertices;
- **(D(_b)) boundary-complete fill:** (\sup_{z\in\overline\Omega}\operatorname{dist}(z,V_\varepsilon)\le C_f\varepsilon);
- **(E) edge scale:** every edge has length at most (C_e\varepsilon);
- **(P) path tube:** for every pair (x,y\in V_\varepsilon), there is an edge path joining them whose vertices lie within (C_p\varepsilon) of ([x,y]);
- **(W) conductances:** (a_e^\varepsilon\ge a_->0).

Use the energy
\[
\mathcal E_\varepsilon(v)=\frac12\sum_{e=\{p,q\}\in E_\varepsilon}
\varepsilon^{d-2}a_e^\varepsilon(v(p)-v(q))^2.
\]

The lower edge-length bound is automatic from (S), since distinct endpoints are separated.

## 3. Packing gives bounded local path length

Fix (R>0). Consider (x,y\in V_\varepsilon) with ( |x-y|\le R\varepsilon). Choose a path supplied by (P), and erase loops so that it is simple.

Every vertex of this path lies in
\[
B\bigl(x,(R+C_p)\varepsilon\bigr).
\]
By (S), the balls of radius (c_s\varepsilon/3) around distinct vertices are disjoint. A volume-packing estimate therefore gives
\[
\#\bigl(V_\varepsilon\cap B(x,(R+C_p)\varepsilon)\bigr)
\le N_R,
\]
where (N_R) depends only on (d,c_s,R,C_p), not on \(\varepsilon,x,y\).

The chosen simple path consequently has at most (N_R-1) edges. In particular,
\[
|v(x)-v(y)|^2
\le N_R\sum_{e\in P_\varepsilon(x,y)}
|D_ev|^2. \tag{3.1}
\]

This is the missing local path-length estimate: it follows from separation and the tube condition, rather than needing to be postulated separately.

## 4. Bounded congestion for local pairs

For each unordered pair (\{x,y\}) with ( |x-y|\le R\varepsilon), fix one of the simple paths above.

Suppose a fixed edge (e=\{p,q\}) belongs to the selected path for the pair (\{x,y\}). Since a path vertex (p) lies within (C_p\varepsilon) of the segment ([x,y]), and ( |x-y|\le R\varepsilon), both endpoints (x,y) lie in a ball of radius ((R+C_p)\varepsilon) about (p). The same packing estimate bounds the number of possible choices of (x), and independently of (y), by (N_R).

Thus each edge is used by at most (N_R^2) selected local-pair paths. Summing (3.1) over all local pairs gives
\[
\sum_{\substack{\{x,y\}\subset V_\varepsilon\\
0<|x-y|\le R\varepsilon}}
|v(x)-v(y)|^2
\le N_R^3\sum_{e\in E_\varepsilon}|D_ev|^2. \tag{4.1}
\]
The precise exponent on (N_R) is inessential; only uniformity matters.

This is a genuine bounded-congestion statement, but only for pairs at a fixed multiple of the mesh scale. No global all-pairs congestion estimate is asserted.

## 5. Voronoi cells and comparison with a nonlocal energy

Let (V_\varepsilon(x)) be the clipped Euclidean Voronoi cell of (x\in V_\varepsilon), and let (P_\varepsilon v) be the associated piecewise-constant function.

Under (S), (D(_b)), and the uniform Lipschitz cone property of \(\Omega\), there are constants (0<c_V\le C_V<\infty) such that
\[
c_V\varepsilon^d\le |V_\varepsilon(x)|
\le C_V\varepsilon^d
\quad\text{for all }x\in V_\varepsilon. \tag{5.1}
\]
The upper bound follows because every point of a Voronoi cell is within (C_f\varepsilon) of its nucleus. For the lower bound, separation implies that \(\Omega\cap B(x,c_s\varepsilon/2)\) belongs to that cell up to null sets; the Lipschitz cone property gives a uniform lower volume bound for this intersection, including at the boundary.

For (0<r\le1), define
\[
\mathcal N_\varepsilon(u)
=\varepsilon^{-d-2}
\int_\Omega\int_{\Omega\cap B(z,r\varepsilon)}
|u(z)-u(z')|^2\,dz'\,dz.
\]
If (z\in V_\varepsilon(x)), (z'\in V_\varepsilon(y)), and ( |z-z'|\le r\varepsilon), then
\[
|x-y|\le (r+2C_f)\varepsilon.
\]
Choose (R=r+2C_f) in (4.1). Using the upper cell-volume bound in (5.1), we obtain
\[
\begin{aligned}
\mathcal N_\varepsilon(P_\varepsilon v)
&\le C\varepsilon^{d-2}
\sum_{\substack{\{x,y\}\subset V_\varepsilon\\
0<|x-y|\le R\varepsilon}}
|v(x)-v(y)|^2\\
&\le C'\varepsilon^{d-2}\sum_{e\in E_\varepsilon}|D_ev|^2\\
&\le C''\mathcal E_\varepsilon(v).
\end{aligned} \tag{5.2}
\]
All constants are independent of \(\varepsilon\) and \(v\).

Equation (5.2) is the central estimate: the graph energy dominates a continuum nonlocal difference quotient at scale \(\varepsilon\).

## 6. Consequences: Poincare and compactness

We use the standard nonlocal compactness fact for bounded Lipschitz domains: if \(\varepsilon_n\to0\), and \(u_n\) is bounded in \(L^2(\Omega)\) with \(\sup_n\mathcal N_{\varepsilon_n}(u_n)<\infty\), then \((u_n)\) is relatively compact in \(L^2(\Omega)\). This follows, for example, by uniform mollification estimates at scale \(\varepsilon_n\), followed by Rellich compactness; the Lipschitz boundary is handled by a uniform extension construction.

Applying this fact to (5.2) gives:

**Theorem EG-01A (uniform-energy compactness).** If \(\varepsilon_n\downarrow0\) and
\[
\sup_n\left(\|P_{\varepsilon_n}v_n\|_{L^2(\Omega)}^2+
\mathcal E_{\varepsilon_n}(v_n)\right)<\infty,
\]
then \((P_{\varepsilon_n}v_n)\) has a strongly convergent subsequence in \(L^2(\Omega)\).

A uniform Poincare inequality follows by contradiction. If it failed for arbitrarily small \(\varepsilon\), there would be a sequence with zero mean, unit \(L^2\)-norm, and energy tending to zero. Compactness gives a strong limit (u) with zero mean and unit norm. Equation (5.2), or the corresponding vanishing nonlocal seminorm, forces (u) to be constant on the connected domain, a contradiction.

Hence there are \(\varepsilon_0,C_P>0\), depending only on the stated geometric and domain constants, such that
\[
\|P_\varepsilon v-(P_\varepsilon v)_\Omega\|_{L^2(\Omega)}^2
\le C_P\mathcal E_\varepsilon(v),
\qquad 0<\varepsilon<\varepsilon_0. \tag{6.1}
\]
Here ((P_\varepsilon v)_\Omega) denotes the Lebesgue mean of the Voronoi embedding, not the unweighted arithmetic mean of vertex values.

## 7. Exact scope and limitations

1. **EG-01 is resolved for the strengthened boundary-complete class.** The proof uses separation, boundary-complete fill, the path-tube property, and a positive lower conductance bound.
2. **The interior-only G3 in the initial framework is insufficient for the Voronoi-cell estimate (5.1).** A boundary coverage/extension hypothesis must be added, or the boundary layer must be treated separately.
3. **This proves compactness and Poincare, not the full \(H^1\) extension estimate (4.1).** It does not by itself establish the graph fundamental estimate, integral representation, quadratic Γ-limit, or full-sequence convergence.
4. **No upper conductance bound is needed for this lower coercivity estimate.** It remains relevant for upper-growth and recovery-sequence arguments.
5. The single-bridge benchmark violates (P), so it is consistent with this result.

## 8. Required framework correction

Replace the earlier statement that (G1)-(G6) do not provide a uniform path-length bound: for local pairs, that bound follows immediately by packing as shown in Section 3. Also replace the blanket statement that the path-tube condition gives no uniform local congestion: Section 4 proves bounded congestion for fixed-radius local pairs.

The correct remaining open questions are the explicit localized measure-property verification, the subsequential cell-density identification, and uniqueness of the effective tensor needed for full-sequence convergence. Boundary-complete fill remains a standing strengthened hypothesis.

## 9. Classification

- Local path-length bound: **proved** under (S) and (P).
- Fixed-radius local path congestion: **proved** under (S) and (P).
- Graph-to-nonlocal-energy domination: **proved** under (S), (D_b), (P), (W), and the stated Voronoi boundary geometry.
- Uniform Poincare / strong \(L^2\) compactness: **proved conditionally** under the same assumptions and the standard nonlocal compactness lemma.
- H1 interpolation, upper growth, and fundamental estimate: **proved conditionally** in the companion note.
- Subsequential integral representation: **conditional** on the localized measure-property verification.
- Full-sequence Gamma-convergence: **open without a uniqueness/homogenization hypothesis**.


## 10. Reference for the nonlocal compactness step

A standard reference for nonlocal difference-quotient characterizations and their relation to Sobolev compactness and Gamma-convergence is:

- A. C. Ponce, “A new approach to Sobolev spaces and connections to Γ-convergence,” *Calculus of Variations and Partial Differential Equations* 19 (2004), 229–255, DOI: [10.1007/s00526-003-0195-z](https://doi.org/10.1007/s00526-003-0195-z).

The graph-specific contribution here is the estimate (5.2), which reduces the discrete graph energy to that established nonlocal framework.
