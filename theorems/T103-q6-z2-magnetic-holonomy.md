# T103 — Z2 magnetic connections, plaquette fluxes, and the Q6 magnetic heat trace

**Status:** exact finite-dimensional classification identities; representative spectral computations are implemented as reproducible audits. No physical charge assignment, continuum limit, supersymmetry in the curved case, or induced-gravity result is claimed.

## 1. Q6 and its cubical completion

Let \(Q_6\) be the six-dimensional hypercube graph. Its vertices are \(v\in\{0,1\}^6\), with an edge between vertices differing in one bit. Thus
\[
|V|=64,\qquad |E|=192,\qquad \deg(v)=6.
\]
We use the full cubical cell complex \(I^6\) when discussing square faces and 3-cells. It has 240 square faces and 160 three-cells. The graph alone does not contain these higher-dimensional cells; they are part of this explicit cubical completion.

A \(k\)-cell is specified by a set \(S\subseteq\{0,\ldots,5\}\) of \(k\) free coordinates and fixed values on the complementary coordinates. All chain groups in the \(\mathbb Z_2\) classification below have coefficients in \(\mathbb F_2\).

## 2. Link variables and gauge action

Assign one bit \(a_e\in\mathbb F_2\) to each unoriented edge and set
\[
U_{vw}=(-1)^{a_{vw}}\in\{+1,-1\},\qquad U_{wv}=U_{vw}.
\]
A vertex gauge field \(g:V\to\mathbb F_2\) acts by
\[
a_{vw}\longmapsto a_{vw}+g_v+g_w\pmod 2,
\]
equivalently \(U_{vw}\mapsto (-1)^{g_v}U_{vw}(-1)^{g_w}\).

Since the graph is connected, the vertex gauge group has a one-dimensional constant stabilizer. Its action has rank \(64-1=63\). Therefore
\[
\dim_{\mathbb F_2}(C^1/\delta C^0)=192-63=129,
\qquad
\#(C^1/\text{gauge})=2^{129}.
\]
This is the exact number of gauge classes; it is not a feasible exhaustive spectral-enumeration target.

## 3. Plaquette flux and the 3-cell constraints

For each oriented square \(p=(v_0v_1v_2v_3)\), define
\[
W_p=\prod_{(v,w)\in\partial p}U_{vw}
=(-1)^{\sum_{e\subset\partial p}a_e}.
\]
The value is independent of the orientation and invariant under vertex gauge transformations. In additive notation let \(b_p\in\mathbb F_2\) be defined by \(W_p=(-1)^{b_p}\).

The cubical boundary maps satisfy
\[
\partial_1\partial_2=0,\qquad \partial_2\partial_3=0.
\]
For the contractible six-cube, their exact ranks are
\[
\operatorname{rank}\partial_1=63,\quad
\operatorname{rank}\partial_2=129,\quad
\operatorname{rank}\partial_3=111.
\]
Consequently the 240 plaquette bits are not independent: they satisfy 111 independent 3-cell constraints,
\[
\partial_3^{\,T}b=0\quad\text{over }\mathbb F_2.
\]
The map from gauge classes of edge fields to admissible plaquette-flux assignments is an isomorphism. In particular, every admissible flux assignment is realized, and two edge fields with the same plaquette flux are gauge-equivalent. The count of admissible flux assignments is \(2^{240-111}=2^{129}\).

The all-trivial-flux sector \(b=0\) contains exactly one gauge class. Thus every flat \(\mathbb Z_2\) connection on this contractible complex is gauge-equivalent to \(U=1\). A single isolated negative plaquette is not an admissible flux assignment: the 3-cell constraints must hold.

## 4. Magnetic graph Laplacian

For \(f:V\to\mathbb C\), define
\[
(L_Uf)(v)=\sum_{w\sim v}\bigl(f(v)-U_{vw}f(w)\bigr).
\]
With the stated convention, \(L_U=6I-A_U\), where \((A_U)_{vw}=U_{vw}\) on edges and is zero otherwise. It is Hermitian and positive semidefinite, with
\[
\langle f,L_Uf\rangle
=\sum_{\{v,w\}\in E}|f(v)-U_{vw}f(w)|^2.
\]
Gauge-related operators are unitarily conjugate, so their spectra and heat traces agree.

Write the 64 eigenvalues, with multiplicity, as \(\lambda_j(U)\). The ordinary magnetic heat trace is
\[
K_U(t)=\operatorname{Tr}(e^{-tL_U})
=\sum_{j=1}^{64}e^{-t\lambda_j(U)},\qquad t\geq0.
\]
For \(U=1\), the hypercube spectrum gives
\[
K_1(t)=(1+e^{-2t})^6.
\]
This is an ordinary trace. No supertrace or supersymmetry is inferred from this graph operator.

## 5. Reproducible audit and finite representative set

The accompanying audit constructs all cubical cells and boundary maps, checks the chain identities and ranks over \(\mathbb F_2\), fixes gauge on a deterministic spanning tree, verifies the plaquette-flux constraints and injectivity on gauge classes, and diagonalizes the magnetic Laplacian for a small declared set of representatives:
- the trivial connection;
- one negative link (a representative of the one-link-flip orbit);
- a specified two-link configuration.

The script also checks gauge invariance of the spectrum and heat trace numerically. This is a representative computation, not enumeration of all \(2^{129}\) classes and not a classification of all spectral degeneracies.

Run:
\`\`\`bash
python scripts/audit_t103_q6_z2_magnetic_holonomy.py --output reports/t103_q6_z2_magnetic_holonomy.json
python -m pytest -q tests/test_t103_q6_z2_magnetic_holonomy.py
\`\`\`

## 6. Scope and open extensions

1. The \(\mathbb Z_2\) link model is a finite magnetic graph model. A physical interpretation of \(U\), charge, or an individual hexagram requires a separately specified measurement map and calibration.
2. Nontrivial plaquette flux is curvature. A covariant differential with such curvature does not in general square to zero, so the ordinary flat-connection cochain supersymmetry complex cannot simply be reused.
3. A periodic family \(T_n^6=(\mathbb Z/n\mathbb Z)^6\) is a different cubical complex from the single contractible cube. Its quotient cell structure, fundamental-cycle holonomies, and flux constraints must be specified independently.
4. A Seeley–DeWitt or Sakharov limit requires a demonstrated continuum family, geometric scaling, a Laplace-type continuum operator, field content, and regulator. None follows from the finite Q6 heat trace alone.

## 7. Literature

- F. Friedli, “The bundle Laplacian on discrete tori,” *Annales de l’Institut Henri Poincaré D* **6** (2019), no. 1, 97–121. DOI: [10.4171/AIHPD/66](https://doi.org/10.4171/AIHPD/66). Relevant to bundle Laplacians and spectral/determinant asymptotics on discrete tori; it does not by itself establish a limit for this Q6 model.
- J. S. Fabila-Carrasco, F. Lledó, and O. Post, “Spectral gaps and discrete magnetic Laplacians,” *Linear Algebra and its Applications* **547** (2018), 183–216. DOI: [10.1016/j.laa.2018.02.006](https://doi.org/10.1016/j.laa.2018.02.006).
- O. Knill, “The McKean–Singer Formula in Graph Theory,” arXiv:1301.1408 (2013). [arXiv](https://arxiv.org/abs/1301.1408). Its simplicial/clique-complex construction is not automatically the cubical completion used here.
- D. V. Vassilevich, “Heat Kernel Expansion: User’s Manual,” *Physics Reports* **388** (2003), 279–360. DOI: [10.1016/j.physrep.2003.09.002](https://doi.org/10.1016/j.physrep.2003.09.002), [arXiv:hep-th/0306138](https://arxiv.org/abs/hep-th/0306138).
- M. Visser, “Sakharov’s Induced Gravity: A Modern Perspective,” *Modern Physics Letters A* **17** (2002), 977–992. DOI: [10.1142/S0217732302006886](https://doi.org/10.1142/S0217732302006886), [arXiv:gr-qc/0204062](https://arxiv.org/abs/gr-qc/0204062).

The last two references provide continuum heat-kernel and induced-gravity context only; they are not evidence that the finite Q6 construction induces gravity.


## 8. CI execution record — 12 November 2026

The deterministic Q6 magnetic-holonomy audit and the T103/T104 regression suite completed successfully in [GitHub Actions run #43245722504](https://github.com/fabianleonaressi95/theorem/actions/runs/43245722504). The run reports 11 passing tests, cycle-space dimension 129, cocycle-space dimension 63, and H1 dimension 0 for the declared finite cubical complex. This is a reproducible finite-complex/software certificate; it does not extend the physical interpretation beyond the hypotheses above.
