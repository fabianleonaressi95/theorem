# T064 — Gauge covariance of finite SU(2) lattice transport and Wilson traces

**Status:** proved finite-graph theorem.  
**Scope:** a finite graph with one SU(2) matrix on each oriented edge, reverse links defined by Hermitian conjugation, and vertex gauge transformations. This formalizes the conventions implemented by `SU2Lattice`; no continuum limit or Yang–Mills dynamics is asserted.

## 1. Setup and conventions

Let \(G=(V,E)\) be a finite graph. For each oriented edge \(g\to h\), let
\[
U_{gh}\in SU(2),\qquad U_{hg}=U_{gh}^{\dagger}.
\]
A gauge field is a choice \(G_v\in SU(2)\) for each vertex. Define the transformed link by
\[
U_{gh}^{G}=G_h U_{gh}G_g^{\dagger}.
\]
For an ordered path \(p=(v_0,v_1,\ldots,v_n)\), with column vectors transported by left multiplication, define
\[
P(p)=U_{v_{n-1}v_n}\cdots U_{v_1v_2}U_{v_0v_1}.
\]

## 2. Theorem

For every path,
\[
\boxed{P^G(p)=G_{v_n}P(p)G_{v_0}^{\dagger}.}
\]
If \(p\) is closed at \(v_0\), its holonomy transforms by conjugation:
\[
H^G(p)=G_{v_0}H(p)G_{v_0}^{\dagger}.
\]
Consequently the Wilson trace is gauge invariant:
\[
\boxed{\operatorname{Tr}H^G(p)=\operatorname{Tr}H(p).}
\]
Moreover, \(P(p)\) and \(H(p)\) lie in \(SU(2)\); for a closed path the trace is real and the normalized Wilson observable
\[
W(p)=\tfrac12\operatorname{Tr}H(p)
\]
lies in \([-1,1]\).

## 3. Proof

By definition,
\[
P^G(p)=
(G_{v_n}U_{v_{n-1}v_n}G_{v_{n-1}}^{\dagger})
\cdots
(G_{v_1}U_{v_0v_1}G_{v_0}^{\dagger}).
\]
Adjacent factors \(G_{v_j}^{\dagger}G_{v_j}\) cancel to the identity, leaving
\[
P^G(p)=G_{v_n}
(U_{v_{n-1}v_n}\cdots U_{v_0v_1})
G_{v_0}^{\dagger}.
\]
This proves path covariance. If \(v_n=v_0\), the transformation is conjugation. Cyclicity of trace then gives
\[
\operatorname{Tr}(G_{v_0}HG_{v_0}^{\dagger})
=\operatorname{Tr}(HG_{v_0}^{\dagger}G_{v_0})
=\operatorname{Tr}H.
\]
Products of SU(2) matrices remain in SU(2). Every SU(2) matrix is unitarily diagonalizable with eigenvalues \(e^{i\theta},e^{-i\theta}\); hence its trace is \(2\cos\theta\in\mathbb R\), and the half-trace lies in \([-1,1]\). Finally,
\[
(U_{gh}^{G})^{\dagger}
=G_g U_{gh}^{\dagger}G_h^{\dagger}
=G_g U_{hg}G_h^{\dagger}
=U_{hg}^{G},
\]
so the reverse-link convention is preserved by the gauge transformation. \(\square\)

## 4. Implementation and test correspondence

Implementation:
- `src/holonomies.py`: `SU2Link`, `SU2Lattice`, path transport, closed holonomy, Wilson trace and vertex gauge transform.
- `tests/test_holonomies.py`: reverse-link adjoint, column-vector product order, reverse-path inverse, SU(2) closure, gauge covariance, conjugation of closed holonomy, trace invariance, and invalid-input guards.

The tests are finite numerical checks of the stated formulas. They do not establish a continuum Yang–Mills limit, a lattice-action continuum approximation, or any RGS–PSU physical interpretation.
