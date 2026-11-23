# Golden ratio, Riemann zeta, Fibonacci electromagnetism and fullerene geometry

**Status:** research programme / corrected specification.  
**Scope:** exact identities, derived model results, numerical results, physical derivations and open hypotheses are kept separate. No physical bridge between sections is assumed.

## 1. Research chain and claim classes

The programme investigates
\[
\text{regular pentagon / }\varphi
\to \text{cotangent and }\zeta(2n)
\to \text{Fibonacci transfer response}
\to \text{Maxwell spectral problem}
\to \text{fullerene / Stone--Wales / discrete geometry}.
\]
Only the first two stages are presently exact analytic identities. The Fibonacci response is a result within a specified one-dimensional model. Maxwell and fullerene links require independently defined operators and observables.

Every claim must be labelled: **exact identity**, **derived model result**, **computational result**, **physical derivation**, or **hypothesis/open obligation**. Passing a numerical test does not prove a theorem or physical law.

## 2. Regular polygon identities

Define
\[
\Delta_p=p\pi\cot\frac{\pi}{p}.
\]
Then
\[
\Delta_3=\pi\sqrt3.
\]
Since
\[
\cot\frac{\pi}{5}=\sqrt{\frac{5+2\sqrt5}{5}},
\]
we obtain
\[
\boxed{\Delta_5=5\pi\cot\frac{\pi}{5}
=\pi\sqrt{25+10\sqrt5}
=\pi\sqrt{15+20\varphi}},
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]
This is a trigonometric scalar defined by the regular-polygon formula. It is not, without an additional model, an energy, a fullerene curvature or an electromagnetic observable.

## 3. Cotangent expansion and Riemann zeta

For |x|<1,
\[
\pi\cot(\pi x)=\frac1x
-2\sum_{n=1}^{\infty}\zeta(2n)x^{2n-1}.
\]
Putting x=1/p and multiplying by p gives
\[
\boxed{\Delta_p=p^2-
2\sum_{n=1}^{\infty}\frac{\zeta(2n)}{p^{2n-2}}}.
\]
The exponent is 2n-2 because of the additional factor p.

Set
\[
\varepsilon=\frac{\sqrt5-2}{2}=\frac1{2\varphi^3},
\qquad a=\frac{\sqrt5}{2}=1+\varepsilon.
\]
Periodicity of cotangent gives
\[
\boxed{
\pi\cot\left(\pi\frac{\sqrt5}{2}\right)
=\frac1\varepsilon-
2\sum_{n=1}^{\infty}\zeta(2n)\varepsilon^{2n-1}
=2\varphi^3-
2\sum_{n=1}^{\infty}\zeta(2n)
\left(\frac1{2\varphi^3}\right)^{2n-1}.
}
\]
The exponent 2n-1 applies to the entire parenthesized quantity. The series converges because 0<epsilon<1.

Define
\[
C_\varphi=\pi\cot\left(\frac{\pi}{2\varphi^3}\right).
\]
Recompute every quoted decimal value at high precision and compare it with partial sums of the zeta expansion. Do not copy unverified decimals into theorem statements.

## 4. Fibonacci transfer model and boundary normalization

Fix the word convention
\[
W_1=A,\quad W_2=AB,\quad W_m=W_{m-1}W_{m-2},
\]
with Fibonacci indexing F_1=F_2=1. Then N_A=F_m and N_B=F_{m-1}. State explicitly whether w_1,...,w_N are ordered left-to-right; for that convention the total transfer matrix is M=P_{w_N}...P_{w_1}.

For the model parameters
\[
T=1,\quad \rho_A=1,\quad \rho_B=\varphi^2,
\quad q_A=\omega,\quad q_B=\varphi\omega,
\]
use the stated length normalization
\[
\ell_{A,m}=\frac1{F_m+\varphi^{-1}F_{m-1}},
\quad
\ell_{B,m}=\frac{\varphi^{-1}}{F_m+\varphi^{-1}F_{m-1}}.
\]
Thus ell_B/ell_A=phi^{-1}. Since F_m/F_{m-1}->phi, the limiting total-length ratio is
\[
\frac{N_A\ell_A}{N_B\ell_B}\to\varphi^2,
\]
and the spatial fractions are
\[
\theta_A=\frac{\varphi^2}{\varphi^2+1},
\quad \theta_B=\frac1{\varphi^2+1}.
\]
The mean density for these parameters is
\[
\bar\rho=\theta_A\rho_A+\theta_B\rho_B
=\frac{2\varphi^2}{\varphi^2+1}=1+\frac1{\sqrt5}.
\]
This is model-specific, not a universal property of Fibonacci media.

The segment matrix is
\[
P_j(\omega)=
\begin{pmatrix}
\cos(q_j\ell_j)&\sin(q_j\ell_j)/(Tq_j)\\
-Tq_j\sin(q_j\ell_j)&\cos(q_j\ell_j)
\end{pmatrix}.
\]
For fixed-end conditions, the spectral equation is M_12(omega)=0 under this state-vector convention. Every numerical spectrum must include the finite word, parameters, matrix order, root tolerances and residuals.

For the homogeneous equation
\[
u''+Q^2u=0,\quad u(0)=1,\quad u(L)=0,
\]
the solution is
\[
u(x)=\frac{\sin(Q(1-x/L))}{\sin Q},
\]
hence
\[
-u'(0)=\frac QL\cot Q.
\]
The dimensionless normalized response is therefore R(Q)=L[-u'(0)]=Q cot Q for this particular unit-coefficient equation and normalization. A different physical flux, impedance, state vector or normalization requires a fresh derivation and unit check.

For |Q|<pi,
\[
Q\cot Q=1-2\sum_{n=1}^{\infty}\zeta(2n)(Q/\pi)^{2n}.
\]
Setting Q=pi/(2 phi^3) gives the algebraic identity
\[
C_\varphi=2\varphi^3 Q\cot Q.
\]
This does not derive the special value of Q from the Fibonacci model. A selection rule for Q is an open obligation.

## 5. Maxwell on Ellis--Bronnikov: derive before using

Declare the metric and conventions, for example
\[
ds^2=-c^2dt^2+du^2+(u^2+a^2)d\Omega^2.
\]
Derive the radial equations from dF=0 and d star F=0 (or equivalent covariant Maxwell equations), using a specified vector-spherical-harmonic basis and gauge constraints. Do not assume a scalar-wave radial operator is automatically the Maxwell operator.

For every proposed radial operator specify: metric/sign convention; time dependence and k=omega/c; angular mode and polarization; radial dependent variable and any Liouville transformation; Hilbert-space measure and self-adjoint domain; behavior at both ends u->+-infinity; scattering normalization and spectral measure.

An expression such as
\[
\mathcal L_L=-\frac{d^2}{du^2}+\frac{L(L+1)}{u^2+a^2}
\]
is only a candidate reduced operator until derived. On the full line the spectrum is generally continuous. The ordinary trace Tr(L_L^{-s}) is not automatically finite or defined. A spectral zeta requires a specified relative operator, reference operator, resolvent/scattering definition, regularization and analytic continuation.

Keep Riemann zeta zeta(s) distinct from a Maxwell spectral zeta zeta_L(s). A relation between them is a theorem to prove, not a naming convention.

## 6. Fullerene topology and curvature descriptors

A classical fullerene is a simple 3-connected planar cubic graph whose faces all have size 5 or 6. Euler and degree counting imply exactly 12 pentagons. For C64: V=64, E=96, F=34, with 12 pentagons and 22 hexagons.

At a trivalent vertex v, let k(v) count incident pentagonal faces. Only for a realization with regular pentagonal and hexagonal faces, the angular deficit is
\[
K(v)=2\pi-\sum_{f\ni v}\theta_f(v)=\frac{\pi}{15}k(v),
\]
because the interior angles are 3pi/5 and 2pi/3. Since each pentagon has five corners,
\[
\sum_vk(v)=60,\quad \sum_vK(v)=4\pi.
\]
This is discrete Gauss--Bonnet for that angle assignment. It does not determine a unique embedding, metric, energy or electromagnetic operator.

A possible descriptor is
\[
\mathcal K_2=\sum_vK(v)^2
=\frac{\pi^2}{225}\sum_vk(v)^2.
\]
Call it an angle-deficit-square descriptor, not an energy or spectral correction. Also compute graph-theoretic alternatives (pentagon adjacency, explicitly defined face-distance distributions, vertex-distance distributions).

## 7. Stone--Wales: define the move and verify the face inventory

“90-degree rotation” is not a complete mathematical definition. Specify the local edge reconnection on the embedded cubic graph, involved vertices, cyclic order and induced face-boundary changes. Verify planarity, simplicity, connectivity, vertex degrees and face sizes after each move.

**Class distinction:** a standard Stone--Wales bond rotation can create a local 5--7--7--5 defect, so it need not map a classical all-pentagon/hexagon fullerene to another classical fullerene. If a restricted fullerene-isomer move is intended, define it separately and prove its face-vector preservation. Never assume the pentagon/hexagon counts are preserved without checking the actual reconnection.

For each move record before/after canonical graph identifiers; face-size vector (including heptagons); pentagon/heptagon adjacency; k(v) histogram and K2 when the regular-face angle convention applies; automorphism group and orbits; reversibility and whether the inverse returns the original canonical graph.

A claimed invariant must be a predeclared falsifiable proposition. Distinguish invariance of V,E, degree sequence, Euler characteristic, face-size multiset and any finer descriptor. Do not search unconstrained statistics and report a coincidental constant as a law.

## 8. Null test for a fullerene--spectrum bridge

1. Select a complete reproducible C64 isomer dataset: generator/version, command, filters, canonicalization and checksum. Do not call a partial list “all isomers”.
2. Validate every graph: V=64, E=96, cubic, planar, 3-connected, 34 faces, face sizes 5/6 with counts 12/22.
3. Compute predeclared descriptors: pentagon adjacency, defined face distances, k(v) histogram and K2.
4. Apply only explicitly defined Stone--Wales moves; distinguish moves preserving classical fullerene class from moves introducing heptagons.
5. Define a spectral observable independently of K2. Adjacency, graph Laplacian and discrete Hodge spectra are graph spectra, not automatically Maxwell spectra.
6. Compare against controls (vertex/edge counts, face vector, degree sequence, symmetry); use held-out isomers or a predeclared permutation/null model to avoid post-selection.
7. Report negative results and uncertainty. Correlation is not a physical derivation; a graph-Laplacian spectrum is not Maxwell scattering without a proved discretization/convergence map.

## 9. De Aquino: conditional algebra only

If the source's proposed relation is assumed,
\[
\frac{m_g}{m_{i0}}=3-2\sqrt{1+\xi^2},
\]
then setting m_g=0 gives xi_star=sqrt(5)/2 and algebraically phi=1/2+xi_star. Retrieve and cite the original source; define symbols, dimensions, units, regime and assumptions. This consequence is not independent experimental validation and must not be presented as accepted gravitational or electromagnetic physics.

## 10. Required claim ledger and deliverables

Maintain a ledger with columns: Claim; mathematical/physical definition; status; evidence/proof; falsification test/open obligation.

Separate records are required for polygon/cotangent identities; zeta series and convergence; Fibonacci finite transfer matrices and root computations; homogenized density and boundary normalization; Maxwell reduction and scattering/spectral construction; C64 enumeration and graph descriptors; Stone--Wales move class and face-vector behavior; proposed fullerene--spectral relation; De Aquino conditional algebra; and any Krist-All/Kathara chain-level map.

Suggested deliverables:
- docs/GOLDEN_ZETA_MAXWELL_FULLERENE_PROGRAM.md (this programme);
- results/golden_zeta_maxwell/claim_ledger.csv;
- executable algebraic/numerical regression checks for Sections 2--4 (floating-point regression tests are not formal symbolic proofs);
- tests for polygon identities, zeta-series convergence and transfer-matrix determinant;
- C64 dataset manifest and descriptor tables;
- separate Maxwell derivation note with references and domains;
- Stone--Wales transition catalogue;
- only after chain groups and boundary maps are defined, a Krist-All/Kathara compatibility test.

Do not merge a conjectural cross-domain identity into the theorem catalogue. Numerical verification can upgrade a claim only to computational result, never to theorem or physical law.


## 11. Repository verification entry points

- Claim ledger: [\u0060results/golden_zeta_maxwell/claim_ledger.csv\u0060](../results/golden_zeta_maxwell/claim_ledger.csv).
- Standard-library regression tests: [\u0060tests/test_golden_zeta_maxwell.py\u0060](../tests/test_golden_zeta_maxwell.py).
- Run: \u0060python -m unittest discover -s tests -p 'test_golden_zeta_maxwell.py' -v\u0060.

These tests cover polygon identities, the two cotangent/zeta expansions, Fibonacci word counts and homogenized density, unit determinant of segment/total transfer matrices, and the normalized homogeneous boundary derivative. They do not test the Maxwell reduction, C64 enumeration, Stone--Wales catalogue or any physical cross-domain relation.
