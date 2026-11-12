# T129 — Icosahedral equivariance obstruction and calibrated Q6–Purcell map

**Status:** [P] exact representation-theoretic no-go under stated hypotheses; [N] finite implementation checks; [C] calibrated map family; [O] physical calibration and transport convergence.  
**Depends on:** T128; the recovered golden RGS–PSU 3+3 cut-and-project convention.  
**Scope:** maps from the Q6 internal projection to the two-dimensional Purcell shape torus.

## 1. Recovered cut-and-project data

Use the already recovered golden icosahedral six-axis convention, not a newly selected pair of cube axes. Let

\[
A(p)=
\begin{pmatrix}
0&0&1&-1&p&p\\
1&-1&p&p&0&0\\
p&p&0&0&1&-1
\end{pmatrix},\qquad
\phi^*=-\phi^{-1}.
\]

The orthonormal internal projection is

\[
P_\perp=\frac{A(\phi^*)}{\sqrt{2(2+\phi^*)}},
\qquad
Y_v=P_\perp(v-\tfrac12\mathbf 1),\quad v\in\{0,1\}^6.
\]

This is the already recovered RGS–PSU projection, with the canonical projected-cube acceptance window. The six Q6 edge directions are the six columns of \(P_\perp\); all 192 graph edges are retained.

## 2. Exact obstruction to an intrinsic linear two-control map

Assume the standard rotational icosahedral group \(A_5\) acts on \(E_\perp\simeq\mathbb R^3\) through its irreducible real three-dimensional icosahedral representation. Suppose the two-dimensional linear control space \(\mathbb R^2\) carries a continuous orthogonal representation of the same \(A_5\) action.

Every homomorphism \(A_5\to O(2)\) is trivial: its kernel is normal, and simplicity of \(A_5\) makes a nontrivial homomorphism injective; but no finite subgroup of \(O(2)\) is isomorphic to the nonabelian simple group \(A_5\) (finite subgroups of \(O(2)\) are cyclic or dihedral). Thus every real two-dimensional orthogonal representation of \(A_5\) is trivial.

An equivariant linear map \(L:E_\perp\to\mathbb R^2\) would therefore have two invariant linear coordinate functionals on the irreducible, nontrivial \(E_\perp\) representation. There are no such functionals. Hence

\[
\operatorname{Hom}_{A_5}(E_\perp,\mathbb R^2)=\{0\}.
\]

**Conclusion.** Under these representation hypotheses, no nonzero *linear, globally \(A_5\)-equivariant* map from the internal icosahedral three-space to the two Purcell controls exists. Therefore the golden cut-and-project data alone do not select a canonical pair of hinge controls. A nonzero map must introduce additional calibration data, reduce the symmetry, or use a more general non-linear/fibred construction.

This is a conditional representation-theoretic theorem, not a claim that no nonlinear map or no physically calibrated coupling can exist.

## 3. Explicit calibrated family

Let \(B\in\mathbb R^{2\times3}\) have orthonormal rows and let \(\kappa>0\) be an angular calibration scale. Define

\[
\Phi_{B,\kappa}(v)
=\kappa B Y_v\pmod{2\pi}
\in\mathbb T^2.
\]

For an oriented Q6 edge \(e=(v,w)\), define its lifted shape increment

\[
\Delta_e\alpha
=\kappa B P_\perp(w-v).
\]

All six coordinate-flip directions contribute; no two axes are privileged. Reversing an edge reverses its lifted increment. Since the increments are differences of a vertex potential, their sum around every closed graph cycle is exactly zero in the lift (and hence zero in \(\mathbb T^2\)). This is a kinematic consistency property, not a dynamical locomotion result.

The pair \((B,\kappa)\) is deliberately exposed as calibration input. The icosahedral cut-and-project construction fixes \(P_\perp\), but does not fix an oriented two-frame in its three-dimensional internal space or an angle scale. The calibration must eventually be derived from independently stated swimmer/wall boundary data or measured controls.

## 4. Local discrete body transport

T128 gives the continuous connection

\[
A(\alpha,y,\theta)=-R_{bb}^{-1}R_{bs}.
\]

For a Q6 edge, the audit code evaluates \(A\) at the midpoint of the lifted shape segment and forms the integrated body twist

\[
\zeta_e=A(\alpha_{mid},y,\theta)\Delta_e\alpha,
\qquad
U_e=\exp_{SE(2)}(\widehat{\zeta_e}).
\]

This is a one-step midpoint approximation to the path-ordered continuous transport. The body base state \((x,y,\theta)\), the calibration \((B,\kappa)\), and all hydrodynamic parameters are explicit inputs. The implementation verifies that each returned matrix lies in \(SE(2)\).

It does **not** yet prove a global discrete connection, exact path-ordering, convergence under graph refinement, or a Q6 controllability theorem. Wall-dependent body propagation and refinement of the Q6 shape map remain open.

## 5. Reproducible audit

Code:
- audits/purcell_swimmer_wall/q6_shape_interface.py
- tests/test_purcell_q6_shape_interface.py

The tests check:
1. the recovered internal projection and all 64 vertices;
2. the 192 edges, with 32 edges in each of the six coordinate directions;
3. rank-two calibrated shape increments and exact vertex-potential differences;
4. rejection of non-orthonormal calibration frames and nonpositive scales;
5. proper rigid-motion structure of the local \(SE(2)\) exponential and edge transport.

## 6. Evidence ledger

- **[P] Proved under explicit hypotheses:** no nonzero linear \(A_5\)-equivariant map from the irreducible internal three-space to a real two-dimensional orthogonal control representation.
- **[N] Finite checks:** 64 Q6 states, 192 edges, all six cut-and-project directions retained; calibrated increments are vertex-potential differences; local edge transports satisfy the \(SE(2)\) matrix constraints.
- **[C] Candidate family:** \(\Phi_{B,\kappa}\), with calibration frame and scale exposed rather than hidden.
- **[O] Open:** derive \(B,\kappa\) from swimmer/wall geometry; propagate the body state consistently along paths; compare loop holonomy with the continuous connection; establish refinement convergence and a discrete controllability criterion.
- **Not claimed:** an intrinsic canonical Q6-to-two-joint map, a physical identification of internal coordinates with hinge angles, or a completed Q6 microswimmer.

## References

- Micalizio, E., Morandotti, M., Shum, H. & Zoppello, M. (2026), *Purcell swimmer near a wall*, DOI: 10.1007/s11012-026-02136-0.
- RGS–PSU source repository: src/rgs_psu_cut_project.py and docs/RGS_PSU_GOLDEN_CUT_AND_PROJECT.md in fabianleonaressi95/rgs-qlg-quaternion-bridge.
