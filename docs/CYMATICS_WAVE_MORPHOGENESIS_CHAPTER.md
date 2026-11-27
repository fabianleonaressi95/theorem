# Cimatica e morfogenesi ondulatoria: dalla geometria spettrale alla dinamica dei campi e dei plasmi

## 1. Scope and terminology

Cymatics studies experimentally observable patterns associated with driven vibrations, including nodal patterns on plates and membranes. Wave morphogenesis is the broader study of how spatial structures arise from the spectrum of an operator, its eigenfunctions, forcing, dissipation, material parameters, and boundary conditions.

The chapter treats Chladni figures as mechanical vibration phenomena. It does not identify them with electromagnetic helicon modes: the latter are vector fields in a magnetized plasma and require Maxwell–fluid or kinetic plasma equations.

## 2. Linear response and modal structure

Let (M) be positive definite, (K) self-adjoint and nonnegative, and (D) a nonnegative damping operator in a finite-dimensional discretization. The forced system is
[
M\ddot u+D\dot u+Ku=f(t).
]
For (f(t)=\Re(Fe^{-i\omega t})), the steady-state complex amplitude solves
[
(K-\omega^2M-i\omega D)U=F.
]
The generalized eigenproblem
[
K\phi_j=\lambda_jM\phi_j
]
provides undamped modal frequencies (omega_j=\sqrt{\lambda_j}), when (lambda_j\ge0). A mode shape is an eigenvector, not itself a complete prediction of the observed pattern: forcing, damping, mode superposition, nonlinearities, and measurement thresholds matter.

## 3. Classical plate benchmark

For a homogeneous Kirchhoff–Love plate with simply supported boundary conditions on ((0,L)^2),
[
D_b\Delta^2w+\rho h\,\partial_t^2w=0,
quad w=\Delta w=0\text{ on }\partial\Omega.
]
The modes and angular frequencies are
[
w_{mn}=\sin(m\pi x/L)\sin(n\pi y/L),qquad
\omega_{mn}=\sqrt{D_b/(\rho h)}\,\pi^2(m^2+n^2)/L^2.
]
This idealized model is a controlled baseline. Real Chladni experiments additionally involve finite support compliance, damping, granular transport, and potentially nonlinear response; these must be measured rather than silently absorbed into a fitted geometric operator.

## 4. Nodal geometry

For a real scalar mode (w), its nodal set is
[
\mathcal N(w)=\{x\in\Omega:w(x)=0\}.
]
For a complex field (U), “node” must be defined componentwise or through a specified observable (for example (|U|=0)); phase singularities and amplitude minima are different objects. A robust comparison should state the observable, threshold, spatial resolution, and uncertainty.

Courant's nodal-domain theorem gives an upper bound on the number of nodal domains of an eigenfunction of an elliptic self-adjoint problem, indexed consistently with eigenvalue multiplicity. It is a constraint, not a universal formula predicting the exact morphology.

## 5. Symmetry, degeneracy, and perturbation

If an operator commutes with a symmetry representation, its eigenspaces decompose into symmetry-invariant subspaces. Degenerate eigenvalues allow different bases within the same eigenspace; a symmetry-breaking perturbation can split eigenvalues and select preferred linear combinations. The observed orientation of a nodal pattern can therefore depend on small imperfections and forcing.

The C02/C03 benchmarks test this distinction on a square plate: the ideal square has the ((m,n)leftrightarrow(n,m)) degeneracy, while an asymmetric perturbation can split the corresponding eigenvalues. The numerical test is not a theorem about all geometries.

## 6. Discrete geometry and RGS–PRISM

A graph or cell complex can support discrete operators (graph Laplacians, incidence/Hodge operators, or finite-element matrices). Such an operator is relevant to a physical wave problem only after specifying:
- the discrete degrees of freedom and their physical meaning;
- the inner product/mass matrix;
- the stiffness or field operator and its derivation;
- boundary conditions and symmetry action;
- a convergence or consistency argument against a continuum model.

Q6 is included as an exact graph-spectral control. Its hypercube Laplacian spectrum is not, by itself, a plate spectrum or a plasma dispersion relation. RGS 188D and PRISM/Krist-All data must likewise be connected by an explicit, audited map before any physical interpretation.

## 7. Helicon plasma extension

A helicon wave is an electromagnetic wave in a magnetized plasma. Its description involves Maxwell's equations coupled to a plasma response (fluid or kinetic), including the equilibrium magnetic field, density profile, boundary/antenna coupling, and collisional or kinetic damping. A schematic phase factor such as
[
\exp(i m\varphi+i k_zz-i\omega t)
]
labels an azimuthal/axial harmonic; it is not a complete helicon dispersion model.

The current-drive problem requires a momentum-transfer calculation, not merely a match of spatial patterns. A future C05 model must derive the wave operator and antenna coupling. C06 must then connect absorbed RF power and the electron distribution to the parallel current (J_\parallel=\mathbf J\cdot\mathbf B/|\mathbf B|), with uncertainty-aware comparison to published measurements. No prediction of fusion-relevant steady-state operation is claimed here.

## 8. Falsifiable validation protocol

For every benchmark, report:
1. eigenvalue/frequency error against an analytic or independently converged reference;
2. mode-subspace angle for degenerate or nearly degenerate eigenvalues (not raw eigenvector correlation alone);
3. nodal-set distance and topology under a stated extraction rule;
4. sensitivity to mesh, boundary conditions, damping, and perturbations;
5. energy balance and numerical conditioning;
6. comparison with a classical baseline using the same data and degrees of freedom.

An RGS/PRISM claim is supported only if it yields a reproducible improvement or a new invariant prediction under this matched comparison. Numerical agreement on one fitted example is insufficient.

## 9. Status

This chapter is a research specification. The C01–C04 reference computations are implemented in the companion script. The RGS/PRISM predictive bridge and the helicon/plasma extensions remain open.
