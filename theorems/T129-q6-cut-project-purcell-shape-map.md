# T129 — Q6 cut-and-project shape map and state-dependent Purcell transport

**Status:** [P] exact finite-dimensional construction conditional on calibration; [N] implementation tests; [O] physical calibration and refinement limit.  
**Scope:** Q6 graph, recovered golden 6D→3D⊕3D frame, two-angle shape map, and state-dependent SE(2) transport.  
**Depends on:** T128; source cut-and-project implementation rgs_psu_cut_project.py in rgs-qlg-quaternion-bridge.

## 1. Recovered golden frame

Let \(\phi=(1+\sqrt5)/2\) and \(\phi_*=(1-\sqrt5)/2=-1/\phi\). Define

\[
A(p)=\begin{pmatrix}
0&0&1&-1&p&p\\
1&-1&p&p&0&0\\
p&p&0&0&1&-1
\end{pmatrix},
\quad
P_\parallel=\frac{A(\phi)}{\sqrt{2(2+\phi)}},
\quad
P_\perp=\frac{A(\phi_*)}{\sqrt{2(2+\phi_*)}}.
\]

The recovered convention satisfies

\[
P_\parallel P_\parallel^T=I_3,\quad
P_\perp P_\perp^T=I_3,\quad
P_\parallel P_\perp^T=0.
\]

Thus the six-dimensional coordinate space splits orthogonally into the physical and internal three-spaces. The Q6 vertices are \(v\in\{0,1\}^6\), centered as \(\bar v=v-\tfrac12\mathbf1\). Their internal coordinates are \(y_\perp(v)=P_\perp\bar v\). This uses the existing golden cut-and-project convention rather than a newly invented coordinate assignment.

## 2. The two-angle map is necessarily calibrated

The internal space is three-dimensional, whereas the Purcell shape space is two-dimensional. The cut-and-project frame alone supplies no distinguished two-plane or rank-two quotient. Accordingly introduce an explicit full-row-rank calibration \(C\in\mathbb R^{2\times3}\), scale \(\sigma>0\), and offset \(s_0\in\mathbb R^2\):

\[
\Phi_{C,\sigma,s_0}(v)
=s_0+\sigma C P_\perp\left(v-\tfrac12\mathbf1\right).
\]

The shape angles are obtained modulo \(2\pi\) only when a periodic chart is explicitly selected; the unwrapped lift is used for local edge integration. For an edge \(e=(v,v')\) with \(v'-v=\pm e_j\),

\[
\Delta s_e=\sigma C P_\perp(v'-v)
=\pm\sigma C P_\perp e_j.
\]

All six cut-and-project directions remain in the construction. The 192 undirected Q6 edges comprise 32 edges of each coordinate-flip type. No two axes are privileged, and the projected directions need not have equal lengths or equal angular effects.

**Non-canonicity statement.** No \(C\) is selected by the 6D→3D⊕3D decomposition alone. A two-dimensional shape chart requires additional data (e.g. an independently specified calibration/observable coupling). Therefore \(C\) and \(\sigma\) are model inputs, not derived material constants.

## 3. State-dependent discrete connection

For the wall problem the continuous connection is

\[
A(s,y,\theta)=-R_{bb}^{-1}(s,y,\theta)R_{bs}(s,y,\theta)\in\mathbb R^{3\times2}.
\]

Because the no-slip wall breaks full Euclidean invariance, \(A\) depends on swimmer height and orientation. A fixed, state-independent edge matrix \(U_e\in SE(2)\) is therefore generally insufficient. For an oriented shape edge \(s(t)=s_0+t\Delta s_e\), define the edge update by

\[
\frac{d}{dt}\begin{pmatrix}x\\y\\\theta\end{pmatrix}
=A(s(t),y(t),\theta(t))\,\Delta s_e,
\qquad
G_e=g(1)g(0)^{-1}\in SE(2),
\]

where

\[
g(x,y,\theta)=
\begin{pmatrix}
\cos\theta&-\sin\theta&x\\
\sin\theta&\cos\theta&y\\
0&0&1
\end{pmatrix}.
\]

This is a state-dependent edge transport, computed by integrating the continuous connection along the edge. Reverse traversal uses the reversed path and yields the inverse transport when the ODE is solved consistently. The implementation accepts \(A\) as a callback, so the published resistance connection can be inserted without hard-coding a different hydrodynamic model.

## 4. Finite audit and tests

Implementation: audits/purcell_swimmer_wall/q6_cut_project_interface.py.  
Tests: tests/test_purcell_q6_interface.py.

The tests check the golden orthogonal split, 64 vertices, 192 edges, 32 edges in each of the six coordinate directions, rank-two calibrated shape coordinates, and forward/reverse edge transport for a constant test connection. They do not assert a physical calibration or a Q6 controllability theorem.

## 5. Evidence classification and open gates

- **Exact finite construction, conditional on \(C,\sigma,s_0\):** the affine shape map and all six edge increments.
- **Numerically tested:** matrix orthogonality, graph counts, map rank, and a reversible test transport.
- **Open:** derive/calibrate \(C,\sigma,s_0\) from independent swimmer/Q6 observables; insert the actual wall-dependent \(A\) and run the 192-edge holonomy audit; compare discrete loop holonomy with the continuous connection; establish refinement/convergence and a controllability-rank theorem.
- **Not claimed:** a canonical Q6 two-plane; a physical identification of Q6 vertices with swimmer shapes; isotropy of the six cut-and-project directions; or reproduction of the published local controllability theorem by Q6.

## References

1. Micalizio, Morandotti, Shum & Zoppello (2026), *Purcell swimmer near a wall*, DOI: 10.1007/s11012-026-02136-0.
2. fabianleonaressi95/rgs-qlg-quaternion-bridge/src/rgs_psu_cut_project.py: recovered golden icosahedral six-axis projection and orthogonal internal/physical frame.
