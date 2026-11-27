# Cartan refinement consistency: local theorem and open convergence gates

**Status:** CONDITIONAL local consistency proposition for smooth sampled fields; the Taylor/Magnus proof is outlined below, while fully expanded coordinate remainder estimates remain to be written before promotion to PROVED. Convergence of arbitrary discrete fields or discrete solutions is open. A Q6-derived 4D Lorentzian refinement family is not yet constructed.

This record formalizes the next step after the exact finite affine-Poincare tetrahedral boundary identity. It must not be read as a continuum theorem derived from Q6 alone.

## 1. Smooth Cartan data and refinement family

Let (M) be an oriented four-dimensional manifold, (einOmega^1(M,mathbb R^{1,3})) a smooth nondegenerate coframe, and (omegainOmega^1(M,mathfrak{so}(1,3))) an independent smooth Lorentz connection. Set
[
T=de+omegawedge e,qquad R=domega+omegawedgeomega.
]
No condition (T=0) or (R=0) is imposed.

Let (mathcal K_h) be an oriented, shape-regular simplicial refinement family on a relatively compact region, with maximal diameter (h	o0), uniformly bounded aspect ratios, and embedded simplices in local charts. All estimates are local and uniform on compact subsets.

For each oriented edge (i	o j), let (L_{ij}in SO^+(1,3)) be the connection parallel transport with convention
[
L'_{ij}=g_iL_{ij}g_j^{-1}.
]
Let (E_{ij}) be the integral of the coframe along the edge, parallel-transported to the initial vertex frame, with
[
L_{ji}=L_{ij}^{-1},qquad E_{ji}=-L_{ij}^{-1}E_{ij},qquad E'_{ij}=g_iE_{ij}.
]
Package (G_{ij}=(L_{ij},E_{ij})in SO^+(1,3)ltimesmathbb R^{1,3}), where
[
(H,a)(K,b)=(HK,a+Hb).
]

## 2. Face observables

For (f=[i,j,k]), define
[
F_f=G_{ij}G_{jk}G_{ki}=(H_f,	au_f).
]
Then (H_f'=g_iH_fg_i^{-1}) and (	au_f'=g_i	au_f).

For a small oriented triangle with tangent edge vectors (hu,hv), its parameter-domain area is (1/2). Use the normalization
[
mathscr R_f=2h^{-2}log H_f,qquad mathscr T_f=2h^{-2}	au_f,
]
with the principal logarithm near the identity.

## 3. Local consistency proposition (conditional; proof outline)

**Proposition.** If the edge data are exact samples of the same smooth pair ((e,omega)), then
[
log H_f=	frac12h^2R(u,v)+O(h^3),qquad
	au_f=	frac12h^2T(u,v)+O(h^3).
]
Thus
[
mathscr R_f=R(u,v)+O(h),qquad
mathscr T_f=T(u,v)+O(h).
]
The remainder is uniform on compact subsets under uniform shape regularity and bounded derivatives of the smooth fields.

**Proof.** Work in a local gauge centered at the face base point. The path-ordered edge transports expanded to second order give the antisymmetric second-order term (domega+omegawedgeomega); taking the logarithm isolates the leading integrated curvature. Expanding the three transported coframe edge integrals, the first-order boundary terms cancel and the leading area term is (de+omegawedge e). The oriented parameter triangle has area (1/2), giving the factors displayed. Taylor remainders are (O(h^3)); shape regularity gives uniform constants. This proves local consistency for smooth sampled data, not convergence for arbitrary discrete data.

## 4. Exact finite identity and its smooth limit

For a tetrahedron ([0,1,2,3]), let
[
A=F_{012},quad B=F_{023},quad C=F_{031},quad
D=G_{01}F_{123}G_{01}^{-1}.
]
Exact edge cancellation gives
[
ABC D^{-1}=mathbf1.
]
If (A=(H_A,t_A)), etc., its translation component is
[
t_A+H_At_B+H_AH_Bt_C-t_D=0.
]
This is a finite identity with curvature transports retained; an untransported sum of face translation vectors is not equivalent.

For a refinement family sampled from a smooth Cartan pair, insert the face expansions and expand the transported factors to the first non-vanishing order on each tetrahedron. The corresponding continuum Cartan identities are
[
D_omega R=0,qquad D_omega T=Rwedge e.
]
This is a consistency comparison for smooth sampled fields. It is not a derivation of the continuum theory from Q6 and does not prove convergence of discrete solutions.

## 5. Established and open

**Established exactly or conditionally:** local Lorentz covariance; the exact finite tetrahedral affine boundary identity; the stated curvature/torsion leading terms under smooth sampling, subject to completing the detailed uniform remainder estimates; compatibility with the smooth Cartan Bianchi identities under sampling/refinement. The local consistency statement is not promoted to PROVED until the coordinate-level remainder bounds and convention checks are fully written out.

**Open:** a Q6-incidence-derived 4D Lorentzian mesh; coframe nondegeneracy and signature control; compactness/stability for arbitrary discrete fields; a gauge-invariant discrete action with independent coframe and connection variations; convergence of discrete critical points; compatible (mathrm{Spin}^+(1,3)) lift and Dirac-operator limit; selection of time from the 6D Euclidean golden split.

Riemann-Cartan, teleparallel ((R=0)) and torsion-free ((T=0)) branches remain distinct. PSU–Anti-Twin sheet exchange is not Cartan torsion.

## 6. Requirements for a genuine solution-convergence theorem

A full theorem must supply:
1. a specified 4D simplicial/cellular refinement family with uniform shape regularity and controlled Lorentzian signature;
2. gauge-invariant field bounds sufficient for compactness;
3. a gauge-invariant discrete action (S_h[L,E,mathrm{matter}]), varied independently in (L) and (E), including boundary terms;
4. consistency of the discrete Euler-Lagrange operators on smooth test fields;
5. stability/coercivity after gauge fixing and a separate treatment of Lorentzian hyperbolicity;
6. subsequential compactness and identification of every limit as a weak solution of the target Cartan equations.

Until these are supplied, the status is **local smooth-sampling consistency proved; global continuum convergence open**.

## 7. Ten-family interface

Q6 is the finite carrier, not automatically a 4D triangulation. GOLDEN supplies a Euclidean (3+3) split, not a time direction. IVM/CELL must provide explicit incidence data. SPACETIME must provide the Lorentzian coframe and independent connection. REP must provide a (mathrm{Spin}^+(1,3)) lift, not identify it with (mathrm{Spin}(6)). ANALYSIS supplies consistency/stability/compactness methods; DYNAMICS supplies the action and variations. PSU–Anti-Twin remains a two-sheet sector distinct from torsion. Family-interface graph edges are architectural links, not proof dependencies.
