# Independent mathematical audit: curvilinear de Rham / FEEC / Mosco

**Scope.** This is a source-level mathematical audit of the merged benchmark and PR #87, not a reproduction of its numerical experiments. The inspected implementation is under `projects/de_rham_benchmark/`, especially `ddr/mesh.py`, `ddr/geometry.py`, `ddr/hodge.py`, `ddr/feec_mass.py`, and `docs/CONSISTENT_FEEC_MASS.md`.

## 1. Executive findings

| Item | Finding | Status |
|---|---|---|
| Cubical incidence complex | The matrices satisfy the chain identity, but their sign is opposite to the standard coordinate orientation used by the FEEC basis described in the documentation. | **Correction required for FEEC commuting diagram** |
| FEEC local spaces | The local basis described and assembled is the lowest-order tensor-product cubical de Rham space (Q^-_1\Lambda^k), provided the stated ordered-wedge orientation is used. | **Mathematically appropriate** |
| Consistent masses | The integrand assembled is the correct pullback Gram integrand for covariant (k)-forms. | **Correct, subject to quadrature and geometry hypotheses** |
| Global assembly | Local face DoFs are assembled using common global face IDs. | **Correct for this conforming structured mesh** |
| Discrete codifferential | (\delta_h^k=M_{h,k-1}^{-1}D_{k-1}^TM_{h,k}) is the correct adjoint formula for the declared coefficient inner products. | **Correct** |
| Projections | No commuting projection, boundedness proof, or approximation theorem is implemented in the audited files. | **Absent / open** |
| Mosco, compactness, norm-resolvent, harmonic kernels | The benchmark contains no reconstruction maps or estimates proving these properties. | **Not established** |

The principal correction is an orientation convention mismatch, not a defect in the positive-definite mass integral. The numerical Hodge spectra can remain unchanged under the global sign reversal of every differential matrix, so the existing spectral tests do not detect this mismatch.

---

## 2. Discrete spaces, pullbacks, and orientation

### 2.1 Reference tensor-product complex

On the reference cube \(\widehat K=[0,1]^d\), the lowest-order tensor-product cubical de Rham spaces are
\[
\widehat V^k(\widehat K)=
\bigoplus_{|I|=k}
\left(\bigotimes_{j\notin I} Q_1(\widehat x_j)\right)
\otimes
\left(\bigotimes_{i\in I} Q_0(\widehat x_i)\right)
\,d\widehat x^I.
\]
Here \(I=(i_1<\cdots<i_k)\), \(d\widehat x^I=d\widehat x_{i_1}\wedge\cdots\wedge d\widehat x_{i_k}\), and \(Q_0\) means constant dependence in the axes in \(I\). A basis function is
\[
\widehat\phi_{I,s}(\widehat x)
=\left(\prod_{j\notin I}\ell_{s_j}(\widehat x_j)\right)d\widehat x^I,
\qquad \ell_0(t)=1-t,\quad \ell_1(t)=t.
\]
Its degree of freedom is the integral over the corresponding oriented coordinate (k)-face. This is exactly the basis pattern assembled in `ddr/feec_mass.py`: the scalar factor is a product over fixed axes, and the component is indexed by the varying axes.

For a cell diffeomorphism \(F_K:\widehat K\to K\), the physical space is defined by the covariant pullback:
\[
F_K^* V^k(K)=\widehat V^k(\widehat K),\qquad
F_K^*(d\omega)=d(F_K^*\omega).
\]
This identity is exact for a sufficiently regular diffeomorphism. It is the reason the incidence matrices are geometry-independent. It does **not**, by itself, imply stability or approximation of a projection.

### 2.2 Concrete sign mismatch in `ddr/mesh.py`

The mesh code uses
\[
D_k[\tau,\sigma]=(-1)^{p+1}(2s-1),
\]
where (p) is the zero-based position of the removed axis in the sorted varying-axis tuple and (s=0,1) selects the lower/upper facet.

With the coordinate orientation (dx_{i_1}\wedge\cdots\wedge dx_{i_k}) stated for the FEEC basis, the standard cubical boundary coefficient is
\[
[\tau:\sigma]=(-1)^p(2s-1).
\]
Thus the stored matrices are the **negative** of the standard coboundary matrices in every degree.

The discrepancy is already visible on one interval. With the vertex basis \((1-x,x)\) and the positively oriented edge (dx),
\[
d(1-x)=-dx,\qquad d(x)=dx.
\]
Therefore the standard degree-zero incidence row is \((-1,+1)\), whereas the code constructs \((+1,-1)\).

This does not break (D_{k+1}D_k=0): replacing every (d_k) by (-d_k) preserves the zero composition. It also does not change the Hodge energy matrices, because each term contains two factors of (D). It **does** break the stated identification of the incidence differential with the exterior derivative of the stated oriented FEEC basis, and therefore invalidates a claimed commuting diagram unless the convention is repaired.

There are two consistent repairs:

1. **Standard coordinate orientation:** change the incidence coefficient to
   \[
   (-1)^p(2s-1),
   \]
   i.e. negate the current matrices.
2. **Keep current matrices:** explicitly orient every degree-(k) face by ((-1)^k) times the coordinate orientation and multiply the degree-(k) FEEC basis/DoF convention by the same sign. The documentation currently describes ordered coordinate wedges and unit positive face integrals, so this alternative must be stated and implemented consistently.

A regression test must compare the incidence action on every local basis function with the actual exterior derivative, not merely test (D_{k+1}D_k=0).

---

## 3. Consistent FEEC mass matrices

### 3.1 Pullback formula

Let (A=DF_K\) and let (G) be the ambient metric. The reference metric is
\[
g=A^T G A.
\]
For reference (k)-forms, the pointwise inner product is induced by the exterior power of (g^{-1}):
\[
\langle d\widehat x^I,d\widehat x^J\rangle_g
=\det\big((g^{-1})_{I,J}\big).
\]
Consequently the local Gram matrix is
\[
(M_K^k)_{ab}
=\int_{\widehat K}
\widehat\phi_a^T\,\Lambda^k(g^{-1})\,\widehat\phi_b
\sqrt{\det g}\,d\widehat x.
\]
This is the formula implemented by `_minor_matrix` and `assemble_consistent_masses`. The minor extraction uses rows (I) and columns (J), as required. For (k=0), the exterior-power metric is (1); for (k=d), it is ((\det g)^{-1}).

For an affine cell with constant (A), a unit-integral top-form basis gives
\[
M_K^d=\int_{\widehat K}(\det g)^{-1}\sqrt{\det g}
=1/|\det A|=1/\operatorname{vol}_g(K).
\]
Thus the top-degree FEEC scaling and the reciprocal-volume primal top-cochain weight are consistent under this DoF normalization. The historical (M_d=\operatorname{vol}_g(K)) is the opposite scaling for integral top-degree cochains and is not the standard primal top-degree Hodge weight.

### 3.2 Local basis and assembly

For each local (k)-face, the code selects the ordered component (I) and multiplies the endpoint linear factors in the complementary axes. This is the correct lowest-order cubical tensor-product basis. The global assembly uses the same face IDs as the incidence complex, so shared DoFs are identified.

For the structured mesh and a single globally defined smooth map, neighboring cells have matching face restrictions. This gives conformity for this particular mesh family. A general collection of independently defined curvilinear hexahedra would additionally require matching geometric face maps and compatible trace parameterizations.

### 3.3 Positivity and quadrature qualifications

If (g(\widehat x)) is uniformly symmetric positive definite and the local basis is linearly independent, the exact Gram matrix is symmetric positive definite. The implemented matrix is a quadrature approximation. Positive Gauss weights and a sufficiently unisolvent quadrature set give a positive discrete Gram matrix for these polynomial basis functions when the metric is positive definite at the quadrature nodes; however, this finite-node property is not a uniform quadrature-error theorem.

For non-polynomial (g), fixed-order Gauss quadrature is not exact. A convergence theorem needs uniform regularity of the metric coefficients and a quadrature error estimate uniform in (h), or exact integration. CI positivity checks on a finite set of meshes do not prove a uniform lower bound for all refinements.

**Assessment:** the FEEC mass formula and the local basis are mathematically sound under the stated pullback convention. The implementation still needs (i) the orientation correction above, (ii) explicit quadrature-error control for convergence claims, and (iii) uniform geometric ellipticity bounds.

### 3.4 Scope of the DEC comparison

The replacement (M_d(K)=1/\operatorname{vol}_g(K)) is correct for integral primal top-degree cochains. It does not prove that every lower-degree diagonal weight in `PullbackGeometry` is a canonical DEC Hodge star on arbitrary curved meshes. The lower-degree formula is a particular dual-volume approximation. The most precise label for the three-way experiment is therefore **historical diagonal / top-degree-corrected diagonal / consistent cubical FEEC**, unless the dual-cell construction for all lower degrees is separately defined and justified.

The flat row-sum identity is plausible and correct for the tensor-product basis on a uniform orthogonal cubical grid: summing endpoint basis functions in each fixed direction gives one, leaving the factor (2^{-(d-k)}h^{d-2k}) per incident cell. It is a property of this flat tensor-product setting, not a general identity between DEC and FEEC masses on curved or non-orthogonal meshes.

---

## 4. Discrete codifferential and Hodge operator

Let (D_{k-1}:C^{k-1}\to C^k) have matrix shape (n_k\times n_{k-1}), and let (M_{h,k}) be the Gram matrix of the degree-(k) inner product. By definition of the adjoint,
\[
(D_{k-1}u,v)_{M_{h,k}}
=(u,\delta_h^k v)_{M_{h,k-1}}.
\]
Writing this in coordinates gives
\[
u^T D_{k-1}^T M_{h,k}v
=u^T M_{h,k-1}\delta_h^k v
\]
for every (u,v). Since (M_{h,k-1}) is invertible,
\[
\boxed{\delta_h^k=M_{h,k-1}^{-1}D_{k-1}^TM_{h,k}.}
\]
This formula is correct for full consistent mass matrices as well as diagonal masses.

The nonnegative quadratic form is
\[
q_h^k(u)=\|D_{k}u\|_{M_{h,k+1}}^2
+\|\delta_h^k u\|_{M_{h,k-1}}^2.
\]
The symmetric energy matrix representing (M_{h,k}\Delta_{h,k}) is
\[
B_{h,k}
=M_{h,k}D_{k-1}M_{h,k-1}^{-1}D_{k-1}^TM_{h,k}
+D_k^TM_{h,k+1}D_k.
\]
This agrees with `consistent_hodge_matrices`. It is symmetric positive semidefinite if all masses are SPD. The generalized eigenproblem (B_{h,k}x=\lambda M_{h,k}x) is therefore the correct symmetric generalized problem.

The sign convention issue in §2 does not alter this quadratic form, because (D_k\mapsto-D_k) leaves every term unchanged. It does alter the identification of (D_k) with the continuous exterior derivative.

---

## 5. Commuting projections: what must actually be proved

A commuting family must consist of genuine projections
\[
\pi_h^k:V^k\to V_h^k,\qquad
\pi_h^k|_{V_h^k}=I,
\]
and satisfy
\[
d_h^k\pi_h^k=\pi_h^{k+1}d^k.
\]
Neither property implies uniform boundedness. For example, take the zero complex (V^0=V_h^0=\mathbb R^2), (d_h=d=0), and
\[
\pi_h(x,y)=(x,h^{-1}y).
\]
It commutes with (d) but (\|\pi_h\|=h^{-1}\to\infty). Also, (2I) commutes with the zero differential but is not a projection.

A usable FEEC projection theorem needs at least:

1. (V_h^\bullet\subset V^\bullet) is a conforming subcomplex.
2. ((\pi_h^k)^2=\pi_h^k) and range (\pi_h^k=V_h^k).
3. (d_h^k\pi_h^k=\pi_h^{k+1}d^k) on the stated graph domain.
4. Uniform graph-norm bounds, e.g.
   \[
   \sup_h\|\pi_h^k\|_{H\Lambda^k\to H\Lambda^k}<\infty.
   \]
5. Approximation on a dense class, followed by uniform boundedness to extend strong convergence to the whole space.
6. Uniformly shape-regular, conforming geometry maps and uniform equivalence of pulled-back norms.
7. Boundary trace spaces and domains of (d) are fixed consistently across (h).

The pullback identity (F_h^*d=dF_h^*) is not a construction of (pi_h). The audited repository does not currently define a commuting projection operator or prove any of the uniform bounds above.

---

## 6. Why commutation does not imply convergence of adjoints

Commutation concerns the primal differential. The adjoint depends on the inner products:
\[
\delta_h=M_{h,k-1}^{-1}D_{k-1}^TM_{h,k}.
\]
A one-dimensional counterexample suffices. Let (H^0=H^1=\mathbb R), (d=I), (D_h=I), and (pi_h^0=\pi_h^1=I). The projections commute exactly. Give degree zero its usual inner product (M_{h,0}=1), but degree one the inner product (M_{h,1}=4). Then
\[
\delta_h=M_{h,0}^{-1}D_h^TM_{h,1}=4I,
\]
whereas the continuous adjoint for the usual inner products is (\delta=I). Thus exact commutation coexists with a nonconvergent adjoint.

To identify adjoints in a limit, one additionally needs convergence and uniform coercivity of the degree-wise inner products, compatible identifications/reconstructions of the discrete spaces, and a graph argument for the adjoints themselves. In particular, one must prove both a lower-limit statement for weakly convergent ((u_h,\delta_hu_h)) and a recovery statement for the continuous adjoint domain. A commuting projection may help construct recovery sequences for (d); it does not automatically construct recovery sequences for (\delta).

---

## 7. Mosco convergence, discrete compactness, resolvents, and kernels

Let
\[
q_h^k(u_h)=\|d_h^ku_h\|_{h,k+1}^2
+\|\delta_h^ku_h\|_{h,k-1}^2,
\qquad
q^k(u)=\|d^ku\|^2+\|\delta^ku\|^2.
\]
The following are sufficient conditions for Mosco convergence on a common Hilbert space (or on varying spaces with explicitly controlled identification maps).

### M1 — lower bound

For every sequence (J_hu_h\rightharpoonup u), assume bounded (q_h(u_h)) implies, after subsequences,
\[
J_hd_hu_h\rightharpoonup a,\qquad
J_h\delta_hu_h\rightharpoonup b,
\]
and separate graph closure identifies (a=du), (b=\delta u). Assume also that the reconstructed inner products converge compatibly and are uniformly coercive. Weak lower semicontinuity then gives
\[
q(u)=\|du\|^2+\|\delta u\|^2
\le\liminf_h q_h(u_h).
\]

### M2 — recovery

For every (u\in D(d)\cap D(\delta)), require a single sequence (u_h\to u) such that
\[
J_hd_hu_h\to du,\qquad
J_h\delta_hu_h\to\delta u.
\]
Then (q_h(u_h)\to q(u)), proving the Mosco upper bound.

These two conditions prove Mosco convergence. They are not established in the repository: there are no common-space reconstruction maps, no separate graph-closure estimates, and no simultaneous recovery construction.

### Discrete compactness

Mosco convergence alone does not imply compactness. A sufficient compactness statement is:
\[
\sup_h(\|u_h\|_{h}+q_h(u_h))<\infty
\quad\Longrightarrow\quad
\{J_hu_h\}\text{ is relatively compact in }H.
\]
For de Rham complexes this is typically proved using a uniform discrete Gaffney inequality, uniform control of the discrete co-closed subspaces, shape regularity, and compactness of the continuous embedding
\[
H\Lambda^k\cap H^*\Lambda^k\hookrightarrow L^2\Lambda^k
\]
with the correct boundary conditions. No such estimate is present in the benchmark.

### Norm-resolvent convergence

Mosco convergence of closed nonnegative forms yields strong resolvent convergence under coherent identification of the Hilbert spaces. Norm-resolvent convergence requires stronger compactness, for example collective compactness of the identified resolvents and their adjoints (for self-adjoint resolvents, the adjoint condition is aligned), together with convergence on a dense set. Without this, strong convergence need not be norm convergence.

### Harmonic kernels and spectral stability

Mosco convergence does not stabilize kernels. For
\[
q(x,y)=x^2,\qquad q_n(x,y)=x^2+n^{-1}y^2
\]
on \(\mathbb R^2\), (q_n\) Mosco-converges to (q), but
\[
\ker q_n=\{0\},\qquad
\ker q=\operatorname{span}\{(0,1)\}.
\]
The small positive gap of (q_n) tends to zero.

Stable harmonic spaces require, in addition, correct discrete cohomology dimensions, convergence of harmonic representatives, compactness near zero, and a uniform positive gap on the orthogonal complement of the kernel. Norm-resolvent convergence plus an isolated spectral cluster is a standard route to convergence of spectral projectors and multiplicities.

---

## 8. A conditional principal theorem for this benchmark

**Theorem (conditional curvilinear cubical Hodge convergence).** Let \(\Omega\subset\mathbb R^d\) be a bounded Lipschitz polyhedron and let \(\mathcal T_h\) be conforming cubical meshes with maximum diameter (h\to0). Suppose:

1. **Uniform geometry.** Each cell map (F_{K,h}\) is an orientation-preserving diffeomorphism. After scaling to the reference cube, the maps and inverses have uniform (W^{r,\infty}) bounds for the regularity (r\) required by the approximation estimates. Cell face maps match across neighbors.
2. **Uniform metric ellipticity.** The ambient/pullback metrics satisfy (cI\le g_h\le CI), with constants independent of (h,K\), and have sufficient uniform coefficient regularity. The metrics converge in a topology strong enough to pass the mass pairings to the limit (uniform (L^\infty) convergence is a sufficient simple hypothesis).
3. **Conforming FEEC complex.** The mapped tensor-product spaces (V_h^\bullet\) form a subcomplex of the selected continuous de Rham complex, with the same boundary-condition convention.
4. **Correct incidence orientation.** The matrices (D_h^k\) are exactly the matrices of (d:V_h^k\to V_h^{k+1}\) in the oriented integral-DoF bases.
5. **Stable commuting projections.** There are genuine cochain projections \(\pi_h^k\) commuting with (d\), uniformly bounded in the graph norms and convergent on a dense subspace.
6. **Mass/quadrature consistency.** The discrete Gram matrices are uniformly coercive and bounded relative to the exact FEEC Gram matrices; quadrature errors tend to zero uniformly in the mesh.
7. **Adjoint graph convergence.** The identified discrete codifferentials satisfy separate weak graph closure and admit simultaneous strong recovery sequences on (D(d)\cap D(\delta)\).
8. **Compactness.** The identified bounded-energy sets are collectively relatively compact in the common (L^2\) space; equivalently, a suitable uniform discrete Gaffney/compactness estimate holds.
9. **Topology and gap.** The discrete cohomology dimensions equal the continuous Betti numbers, and a uniform positive Poincaré/Gaffney gap holds on the orthogonal complement of the harmonic subspaces.

Then:

(a) the quadratic forms (q_h^k\) Mosco-converge to (q^k\);

(b) the associated nonnegative self-adjoint Hodge Laplacians converge in strong resolvent sense;

(c) under the compactness hypothesis, the identified resolvents converge in norm, and isolated eigenvalue clusters and their spectral projectors converge;

(d) under the topology and gap hypotheses, the dimensions of the harmonic kernels are eventually the correct Betti numbers and the harmonic subspaces converge.

**Proof.** (a) Hypothesis 7 gives the separate graph identification needed for the M1 lower bound and the simultaneous recovery sequence needed for M2. Uniform coercivity and convergence of the mass pairings transfer weak lower semicontinuity and strong convergence of the two energy terms. Thus both Mosco conditions hold.

(b) The representation theorem for closed nonnegative forms identifies each form with its self-adjoint operator. Mosco convergence gives strong convergence of the corresponding resolvents after the stipulated identifications.

(c) Hypothesis 8 makes the identified resolvents collectively compact. Strong convergence on a dense set, together with collective compactness of the resolvents and adjoints, upgrades to operator-norm convergence. The spectral-projection conclusion follows from the resolvent functional calculus on contours separating an isolated cluster.

(d) Correct cohomology dimensions and the uniform gap prevent additional eigenvalues from entering or leaving zero. Norm convergence of the spectral projectors for the isolated zero cluster then gives convergence of the harmonic subspaces and equality of their dimensions for sufficiently small (h). \(\square\)

**Important:** this theorem is a roadmap theorem with explicit sufficient assumptions. The benchmark currently verifies neither hypotheses 5, 7, 8, nor 9. It must not be cited as a theorem already proved for the repository.

---

## 9. Intermediate lemmas required

1. **Orientation/derivative lemma.** The local incidence matrix equals the exterior derivative matrix of the oriented local tensor-product basis.
2. **Pullback lemma.** Covariant pullback maps the physical FEEC space onto the reference tensor-product space and commutes with (d).
3. **Trace conformity lemma.** Neighboring cell maps and local traces identify shared face DoFs consistently.
4. **Mass Gram lemma.** The assembled local Gram matrices represent the stated pullback inner product and are SPD.
5. **Uniform mass-equivalence lemma.** Geometry ellipticity and quadrature estimates yield (c\|v_h\|_{L^2}^2\le v_h^TM_{h,k}v_h\le C\|v_h\|_{L^2}^2) with (c,C) independent of (h).
6. **Commuting projection lemma.** Construct (pi_h^k), prove it is a projection, commutes with (d), and is uniformly bounded in the graph norm.
7. **Approximation lemma.** Prove the required (L^2) and (H\Lambda^k) approximation rates on the mapped cubical family.
8. **Adjoint consistency lemma.** Prove separate graph closure for (delta_h), not just primal commutation.
9. **Recovery lemma.** Construct one sequence recovering both (du) and (delta u).
10. **Mosco lemma.** Combine graph closure, pairing convergence, and recovery to prove M1/M2.
11. **Discrete Gaffney lemma.** Establish a mesh-uniform estimate controlling the graph norm by the Hodge energy and (L^2) norm.
12. **Discrete compactness lemma.** Deduce relative compactness of bounded-energy sequences.
13. **Cohomology lemma.** Show the discrete cohomology agrees with the continuous topology, with boundary conditions fixed.
14. **Uniform gap lemma.** Prove a Poincaré inequality uniformly on the orthogonal complement of discrete harmonic forms.
15. **Spectral convergence lemma.** Upgrade strong to norm-resolvent convergence and obtain convergence of isolated spectral clusters.

---

## 10. Corrections to the repository's mathematical wording

1. The statement that the incidence signs are the “standard cubical boundary sign” is incorrect for the ordered coordinate orientation described in the FEEC mass documentation. Either reverse the sign in `mesh.py` or explicitly change the orientation of every degree-(k) DoF by ((-1)^k).
2. The exactness test (D_{k+1}D_k=0) does not validate the orientation convention or the FEEC derivative matrix.
3. The FEEC mass construction is a valid consistent Gram construction, but finite quadrature positivity and finite refinement tests do not establish uniform mass equivalence or quadrature consistency as (h\to0).
4. The phrase “top-corrected primal DEC” should be restricted to the top-degree normalization unless the lower-degree dual-cell weights are independently justified for the curved geometry.
5. The report's revised interpretation of the historical spectral collapse is appropriately cautious: the finite experiments identify a top-degree normalization mechanism in the tested families; they do not prove general Mosco convergence or discrete compactness.
6. The repository does not currently establish commuting projections, adjoint graph convergence, discrete compactness, norm-resolvent convergence, or harmonic-kernel stability. These must remain **open**, not inferred from the mass comparison or CI.

## 11. Overall conclusion

The consistent mass formula in PR #87 is mathematically well-founded for the stated lowest-order cubical tensor-product FEEC basis and pullback metric. The adjoint formula and generalized symmetric Hodge energy are also correct. The main concrete defect is the sign/orientation mismatch between the incidence matrices and the documented FEEC basis orientation. The main structural gap is that the repository constructs Gram matrices but not the uniformly bounded commuting projections or the reconstruction/compactness machinery needed for convergence theorems.

Accordingly, the benchmark supports finite-dimensional algebraic and numerical conclusions. It does **not** yet support a theorem of curvilinear FEEC spectral convergence. The numbered hypotheses and lemmas above specify the route by which such a theorem could be established.
