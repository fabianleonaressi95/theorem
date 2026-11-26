# T102 — Cubical supersymmetric quantum mechanics, heat supertrace, and the Sakharov boundary

**Status:** exact finite-dimensional cubical Hodge/supersymmetric construction; continuum gravity induction, four-dimensional field content, and any identification with \(N=4\) SYM remain open and are not claimed.

## 1. Scope and claim boundary

This record builds the strongest exact bridge available from Q6 without identifying it prematurely with a four-dimensional supersymmetric gauge theory.

The six-dimensional unit cube is treated as a finite cubical cell complex. Its cells are indexed by words
\[
c=(c_1,\ldots,c_6)\in\{0,1,*\}^6,
\]
where \(0,1\) denote fixed coordinates and \(*\) a free coordinate. A cell has degree equal to the number of stars. The number of \(k\)-cells is
\[
N_k=\binom6k2^{6-k},\qquad (N_0,\ldots,N_6)=(64,192,240,160,60,12,1).
\]
The zero-cells and one-cells are exactly the 64 vertices and 192 edges of the Q6 graph. The higher cells supply its canonical square faces and higher-dimensional cubical filling data.

This is finite-dimensional supersymmetric quantum mechanics (the de Rham/Hodge complex of a cube), **not** a construction of four-dimensional \(N=4\) super-Yang–Mills.

## 2. Cubical boundary and Hodge Laplacians

Orient each cell by increasing order of its free coordinate directions. Its boundary is
\[
\partial(c)=\sum_{r:c_{i_r}=*}(-1)^{r-1}
\big(c[i_r\mapsto1]-c[i_r\mapsto0]\big),
\]
where \(i_1<\cdots<i_k\) are the free coordinates. Let \(B_k:C_k\to C_{k-1}\) be the resulting integer boundary matrix. Then
\[
B_{k-1}B_k=0.
\]
With the standard Euclidean inner products, define
\[
\Delta_k=B_{k+1}B_{k+1}^{T}+B_k^{T}B_k,
\]
omitting nonexistent boundary matrices at the endpoints.

On the graded Hilbert space \(\mathcal H=\bigoplus_{k=0}^6 C_k\), let
\[
d=\bigoplus_k B_k^T,\qquad Q=d+d^\dagger,
\qquad H=Q^2=dd^\dagger+d^\dagger d.
\]
With fermion parity \((-1)^F|_{C_k}=(-1)^k\), this gives
\[
Q^2=H,\qquad [H,Q]=0,\qquad \{(-1)^F,Q\}=0.
\]
This is the standard supersymmetric quantum-mechanics algebra. The nonzero spectrum is paired between even and odd degree sectors.

## 3. Exact heat supertrace (McKean–Singer identity)

Define the ordinary degree-wise heat traces
\[
K_k(t)=\operatorname{Tr}_{C_k}(e^{-t\Delta_k})
\]
and the graded heat supertrace
\[
\mathcal I(t)=\operatorname{Str}(e^{-tH})
=\sum_{k=0}^6(-1)^kK_k(t).
\]
For every \(t>0\), positive eigenvalues cancel in even/odd pairs, leaving the Betti numbers:
\[
\mathcal I(t)=\sum_{k=0}^6(-1)^k\dim H_k
=\chi([0,1]^6)=1.
\]
The cube is contractible, so its Betti numbers are \((1,0,0,0,0,0,0)\). This is an exact finite-complex identity, not a numerical fit.

At degree zero, \(\Delta_0=B_1B_1^T\) is the combinatorial graph Laplacian of Q6. Its spectrum is \(2k\) with multiplicity \(\binom6k\), hence
\[
\boxed{K_0(t)=\operatorname{Tr}(e^{-t\Delta_0})=(1+e^{-2t})^6.}
\]
This ordinary heat trace is not the supertrace: \(K_0(t)\) is nonconstant, while the alternating sum over all cell degrees is exactly one.

## 4. Wrapping, periodicity, and topology

Three notions must remain separate.

1. **Geometric wrapping/identification:** quotienting or gluing boundary faces changes the cell complex and its topology. A periodic six-torus is not the same complex as the contractible six-cube; its Betti numbers and heat supertrace differ.
2. **Finite-size/wrapping corrections in QFT:** these are contributions from propagation around compact directions or nontrivial cycles. They require a specified field operator, compactification, boundary conditions, and interaction expansion. They are not implied merely by drawing a periodic graph.
3. **Phase winding:** the T101 cross-circle complement-mismatch phase can have integer winding on Q6 plaquettes. That winding is a candidate phase-vortex index; its interpretation as a Frank or Burgers defect still requires calibrated orientation or translational-density-wave data.

A useful next experiment is to compare the cubical complex with explicitly defined periodic quotients and compute how the ordinary heat traces and supertraces change. One must specify the face identifications before claiming a toroidal topology.

## 5. One-loop determinants and the Sakharov connection

For a positive operator \(D\), a regulated one-loop determinant can be represented schematically by
\[
\log\det{}'D=-\int_0^\infty\frac{ds}{s}
\operatorname{Tr}'(e^{-sD})+\text{counterterms/regularization}.
\]
For a bosonic Gaussian field the contribution is conventionally \(+\tfrac12\log\det{}'D_B\) to the Euclidean effective action; fermionic Gaussian integrals contribute a determinant with statistics-dependent sign and power. In a supersymmetric complex, matched bosonic/fermionic modes cancel in the graded combination, subject to zero modes, gauge fixing, ghosts, and the actual field content.

Sakharov's induced-gravity idea uses the short-proper-time expansion of continuum field heat kernels on a background metric:
\[
\operatorname{Tr}(e^{-sD_g})\sim
(4\pi s)^{-d/2}\int_M\sqrt g\,
\big(a_0+a_1s+a_2s^2+\cdots\big).
\]
In four dimensions the integrated coefficient multiplying \(s\) contains a term proportional to scalar curvature \(R\) for Laplace-type operators; after regularization this can contribute to an Einstein–Hilbert term. The precise coefficient depends on the operator, spin, couplings, statistics, regulator, and field multiplicities.

The finite Q6/cube calculation above supplies exact spectral data and a supersymmetric index. It does **not** yet supply:
- a four-dimensional manifold or metric \(g_{\mu\nu}\);
- a family of operators \(D_g\) coupled covariantly to that metric;
- a controlled continuum/large-graph limit with local heat-kernel coefficients;
- gauge fixing, ghosts, renormalization conditions, or physical field multiplicities;
- a derived Newton constant or cosmological constant.

Therefore no Einstein–Hilbert action or Sakharov coefficient is claimed from Q6 alone.

## 6. Why this is not yet \(N=4\) SYM

Four-dimensional \(N=4\) super-Yang–Mills has gauge field \(A_\mu\), six real adjoint scalars, and four Weyl fermions (equivalently the field content obtained by dimensional reduction of ten-dimensional \(N=1\) SYM). It has \(SU(4)_R\simeq SO(6)\) R-symmetry and a conformal quantum field theory structure.

The cubical Hodge complex has a degree grading and a nilpotent differential, but it has not constructed:
- a four-dimensional Lorentzian or Euclidean gauge connection with local \(SU(N)\) gauge symmetry;
- six adjoint scalar fields and four Weyl fermions;
- the interacting supersymmetry transformations and closure algebra;
- the \(SU(4)_R\) action and the required conformal dynamics.

The number six in Q6 is the number of cube directions; it is not, by itself, the six-scalar multiplet of \(N=4\) SYM. Likewise, the finite-complex supertrace is not evidence of exact conformal invariance, S-duality, AdS/CFT, or planar integrability.

## 7. Reproducible audit and theorem status

Run:
\`\`\`bash
python scripts/audit_t102_cubical_susy_heat.py
pytest -q tests/test_t102_cubical_susy_heat.py
\`\`\`

The script constructs all 729 cells, their boundary matrices, verifies \(B_{k-1}B_k=0\), computes the seven Hodge Laplacians, checks the Q6 graph spectrum, and numerically evaluates the ordinary heat traces and graded supertrace at selected positive times.

| Statement | Status |
|---|---|
| Cell counts \(\binom6k2^{6-k}\) | Exact combinatorics |
| \(\partial^2=0\) for the oriented cube | Exact algebraic identity; audited computationally |
| Q6 graph Laplacian spectrum and \(K_0(t)\) | Exact theorem |
| Cubical Hodge supersymmetric algebra \(Q^2=H\) | Exact finite-dimensional construction |
| \(\operatorname{Str}(e^{-tH})=1\) for the 6-cube | Exact McKean–Singer/Euler identity |
| Periodic quotient/wrapping corrections | Open until quotient and operator are specified |
| T101 winding as physical Frank/Burgers charge | Conditional calibration problem |
| Sakharov-induced Einstein–Hilbert term from a continuum limit | Open |
| Identification with four-dimensional \(N=4\) SYM | Not established; separate construction required |
