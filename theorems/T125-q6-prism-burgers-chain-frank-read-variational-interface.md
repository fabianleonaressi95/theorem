# T125 — Q6/PRISM Burgers-labelled chains and the variational Frank–Read interface

**Classification:** FINITE-DIMENSIONAL THEOREM under the stated fixed-graph and differentiability hypotheses; MODEL-DEPENDENT as a dislocation mechanics model; OPEN for mesh-independent convergence, Frank–Read topological emission/reconnection, and material calibration.

**Purpose:** turn the open interface identified in T124 into a precise variational specification. T125 proves the discrete first-variation and force-balance identities for a fixed combinatorial line network. It does not claim that Q6 or PRISM already generates a physical Frank–Read source.

## 1. Discrete support and Burgers data

Let \(G_h=(V_h,E_h)\) be a finite oriented graph embedded in a slip plane. For an oriented edge \(e=(v,w)\), let \(q_v,q_w\in\mathbb R^2\) be its endpoint positions and let
\[
\ell_e(q)=|q_w-q_v|>0,\qquad
t_e(q)=\frac{q_w-q_v}{\ell_e(q)}.
\]
The embedding is assumed non-degenerate on the configuration domain under consideration. Pinning vertices have prescribed positions; the remaining vertex positions form a finite-dimensional admissible set \(Q_h\).

Let \(\Lambda_B\subset\mathbb R^2\) be a declared Burgers lattice and assign a Burgers label \(b_e\in\Lambda_B\) to each oriented edge. Reversing an edge reverses its orientation and its Burgers label. The labelled discrete line current is
\[
c_h=\sum_{e\in E_h} b_e\,e
\in C_1(G_h;\Lambda_B).
\]
Its endpoint content is the cellular boundary
\[
\partial_1c_h\in C_0(G_h;\Lambda_B).
\]
The incidence identity \(\partial_0\partial_1=0\) is the ordinary chain-complex identity; it expresses endpoint balance and does not encode a cutting or reconnection event.

For a Frank–Read source, the pinned source segment is represented by a prescribed relative-boundary class (or, equivalently, prescribed endpoint content at the pinning set). A closed emitted loop is represented by a cycle \(\gamma_h\in C_1(G_h;\Lambda_B)\) with \(\partial_1\gamma_h=0\). Adding such a cycle preserves the endpoint content:
\[
\partial_1(c_h+\gamma_h)=\partial_1c_h.
\]
This algebraic fact does not specify when or how the graph topology changes to create \(\gamma_h\).

## 2. Discrete energy and external work

For each edge, let \(T_e=T(b_e,\chi_e,h)>0\) be a declared effective line-tension parameter; \(\chi_e\) records any chosen character/material label. Let \(E_{\rm core}(c_h,q)\) be a specified core contribution and let \(f_e^{PK}(s;q)\) be a resolved Peach–Koehler force per unit length along the edge. Define the potential
\[
\mathcal E_h(q;c_h)=
\sum_{e\in E_h}T_e\ell_e(q)
+E_{\rm core}(c_h,q)
-\sum_{e\in E_h}\int_{e(q)}
f_e^{PK}(s;q)\cdot x(s)\,ds
+E_{\rm pin}(q).
\tag{125.1}
\]
Here \(E_{\rm pin}\) is either the indicator of the admissible pinned configuration set or a declared pinning potential. The force/work term is meaningful only after the applied stress, slip system, sign convention and loading protocol have been specified. If the force is not conservative in the chosen state variables, it must instead be retained as a non-potential virtual-work functional; it cannot silently be included in \(\mathcal E_h\).

The discrete energy is a modelling definition, not a consequence of Q6 combinatorics. In particular, \(T_e\), \(E_{\rm core}\), and the force law require material calibration or an explicitly declared phenomenological choice.

## 3. First variation and nodal force balance

Assume \(q\mapsto E_{\rm core}(c_h,q)\), the loading potential and \(E_{\rm pin}\) are differentiable on the unconstrained degrees of freedom. For an edge \(e=(v,w)\),
\[
D\ell_e(q)[\delta q]
=t_e\cdot(\delta q_w-\delta q_v).
\tag{125.2}
\]
Consequently,
\[
D\!\left(\sum_eT_e\ell_e\right)[\delta q]
=\sum_{e=(v,w)}T_e\,t_e\cdot(\delta q_w-\delta q_v).
\tag{125.3}
\]
At an unpinned vertex \(v\), define the oriented incidence sign
\(\varepsilon_{ve}=+1\) if \(v\) is the head of \(e\), and \(-1\) if it is the tail. The line-tension contribution to the nodal gradient is
\[
\nabla_{q_v}E_{\rm line}
=\sum_{e\ni v}\varepsilon_{ve}T_e t_e.
\tag{125.4}
\]
Thus a stationary configuration \(q_h\in Q_h\) satisfies, at every free vertex,
\[
\boxed{
\sum_{e\ni v}\varepsilon_{ve}T_e t_e
+\nabla_{q_v}E_{\rm core}
-\mathcal F^{PK}_{h,v}
+\nabla_{q_v}E_{\rm pin}=0,
}
\tag{125.5}
\]
where \(\mathcal F^{PK}_{h,v}\) denotes the derivative of the declared external-work potential with the sign convention in (125.1). For hard pins, the equation is replaced at pinned vertices by the corresponding constraint reaction/KKT condition.

**Proof.** Equation (125.2) follows by differentiating the Euclidean norm away from zero-length edges. Summing over edges gives (125.3); collecting the coefficients of each independent variation \(\delta q_v\) gives (125.4). Adding the derivatives of the remaining terms in (125.1) and setting the first variation to zero on the tangent space of admissible configurations yields (125.5). Hard constraints give the standard finite-dimensional constrained-stationarity condition. \(\square\)

The identity is exact for the specified finite graph. It is a discrete force-balance law for a fixed network, not yet an evolution law.

## 4. Dissipative evolution is an additional modelling choice

A possible overdamped evolution is
\[
\mathsf M_h(q)\dot q=-\operatorname{grad}_{Q_h}\mathcal E_h(q;c_h),
\qquad \mathsf M_h(q)>0.
\tag{125.6}
\]
For time-independent loading and a fixed chain \(c_h\), this gives
\[
\frac{d}{dt}\mathcal E_h(q(t);c_h)
=-\langle \operatorname{grad}\mathcal E_h,
\mathsf M_h^{-1}\operatorname{grad}\mathcal E_h\rangle
\leq0.
\tag{125.7}
\]
Equation (125.7) is the finite-dimensional energy-dissipation identity. It does not apply unchanged to time-dependent loading, non-potential Peach–Koehler work, inertia, thermal noise, or quantum dynamics; those require separately specified terms and balances.

The choice of mobility \(\mathsf M_h\), admissible slip-plane motion, and pinning law is not fixed by the chain complex.

## 5. What is required for a Frank–Read event

The fixed-graph variational problem describes bowing of a line network while its combinatorial type is held fixed. A Frank–Read cycle requires an additional event map
\[
\mathscr R_h:(q_h,c_h,\text{event data})
\longmapsto(q_h^+,c_h^+)
\]
that specifies the admissible cutting/reconnection, orientation and Burgers-label bookkeeping, and source regeneration. A necessary conservation condition is
\[
\partial_1c_h^+=\partial_1c_h
\]
when the pinning endpoint content is unchanged; an emitted closed loop contributes a cycle. This condition is not sufficient to define the event map and does not select its occurrence time or geometry.

Accordingly:
- the boundary operator controls endpoint bookkeeping;
- the energy variation controls smooth motion on a fixed graph;
- a separate event rule controls topology change;
- a constitutive/microscopic model supplies line tension, core energy, mobility and Peierls/pinning data.

The circular-arc threshold \(\tau_c=2T/(bL)\) from T124 is recovered only in the corresponding constant-tension circular reduction. T125 does not derive a material-specific threshold from Q6/PRISM.

## 6. Relation to the existing RGS–PRISM and Morandotti records

- **Q6/PRISM support:** a chosen graph/cell complex supplies vertices, edges, incidence maps and refinement candidates. A physical embedding, slip-plane assignment and Burgers lattice are additional calibrated data; they are not canonical consequences of the 64 Q6 states.
- **T091 and Morandotti Actions:** the Frank/Burgers/mixed traction-jump decomposition provides an independently audited stress-reconstruction observable. It can be used to compare a calibrated stress field with the external loading in (125.1), but it does not itself provide the line-network energy or a Frank–Read event.
- **T096–T099:** the kinematic and identifiability records constrain how Burgers/Frank data may be extracted from reconstructed fields. In particular, symmetric Airy strain alone does not identify the Burgers closure.
- **T124:** supplies the reduced circular-arc activation threshold and the atomistic/core proof obligations.

The already successful Actions [43051485760](https://github.com/fabianleonaressi95/theorem/actions/runs/43051485760), [43052448456](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448456), and [43052448351](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448351) verify the stated Morandotti traction decomposition/refinement pipeline. They do **not** test (125.1)–(125.7), a Burgers-labelled line-network solver, a Frank–Read event map, or continuum convergence.

## 7. Proof obligations and status

1. **PROVED:** first-variation identity (125.2)–(125.5) for a fixed finite embedded graph with positive edge lengths and differentiable declared energy terms.
2. **PROVED:** energy-dissipation identity (125.7) for the explicitly chosen autonomous gradient flow with positive mobility and fixed chain.
3. **EXACT CHAIN ALGEBRA:** adding a closed Burgers-labelled cycle preserves endpoint content.
4. **MODEL-DEPENDENT:** the choice of Burgers lattice, physical embedding, line tension, core energy, Peach–Koehler work, mobility and pinning law.
5. **OPEN:** derive these data from RGS–PRISM/Q6 and atomistic calculations; establish mesh-refinement compactness and a \(\Gamma\)-limit; prove convergence of the constrained evolutions.
6. **OPEN:** construct and validate the cutting/reconnection/regeneration map, then show that the resulting dynamics emits a Frank–Read loop and recovers the T124 threshold in the appropriate limit.
7. **OPEN:** couple the line model to the T091 Morandotti stress reconstruction without identifying a manufactured-data audit with material validation; assess any thermal or quantum activation separately.

**Conclusion.** T125 closes the *formal variational specification* of the fixed-topology discrete line problem and identifies the exact missing structures for a Frank–Read source. It is not a proof of Frank–Read multiplication from Q6/PRISM.

## References

1. T124, [Frank–Read source: line-tension threshold, pinned-curve evolution and atomistic core input](T124-frank-read-source-line-tension-atomistic-core.md).
2. T091, [Frank–Burgers tensorial interaction and anisotropy composition law](T091-frank-burgers-tensorial-anisotropy-composition-law.md).
3. T. Hudson, F. Rindler and J. Rydell, “A quantitative model for the Frank–Read dislocation source based on pinned mean curvature flow,” *Proc. R. Soc. A* 481 (2025), 20240740, [DOI 10.1098/rspa.2024.0740](https://doi.org/10.1098/rspa.2024.0740).
4. P. Cesana, L. De Luca and M. Morandotti, “Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method,” *SIAM J. Math. Anal.* 56 (2024), 79–136, [DOI 10.1137/22M1523443](https://doi.org/10.1137/22M1523443).

**FLN**
