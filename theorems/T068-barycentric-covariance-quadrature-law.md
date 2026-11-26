# T068 — Barycentric–covariance quadrature law on a planar triangle

**Status: PROVED (local Euclidean theorem).** The implementation-level tests are
maintained in the companion RGS–QLG bridge repository; their execution status
is reported separately from this proof.

## 1. Setting

Let F be a nondegenerate planar triangle in R^3 with vertices
v_0,v_1,v_2, area A_F and diameter h_F. Let

    c_F = (v_0+v_1+v_2)/3

be its areal barycentre, and define its normalized ambient covariance by

    Sigma_F = (1/A_F) integral_F (x-c_F)(x-c_F)^T dA.

For uniform barycentric coordinates lambda_0,lambda_1,lambda_2 on F,

    E[lambda_i^2]=1/6,    E[lambda_i lambda_j]=1/12 (i != j).

Writing x=sum_i lambda_i v_i and using sum_i(v_i-c_F)=0 gives the exact
formula

    Sigma_F = (1/12) sum_{i=0}^2 (v_i-c_F)(v_i-c_F)^T.

In particular Sigma_F is positive semidefinite and has rank at most two.

## 2. Theorem

Let U be an open Euclidean neighbourhood of F and g in C^3(U). Then

    integral_F g(x) dA
      = A_F g(c_F) + (A_F/2) D^2g(c_F):Sigma_F + R_F,

where the colon denotes Frobenius contraction and

    |R_F| <= (A_F h_F^3/6) sup_{x in F} ||D^3g(x)||.

The norm of D^3g is the operator norm of the trilinear form. Consequently,
for the barycentric one-point rule Q_F(g)=A_F g(c_F),

    Q_F(g)-integral_F g dA
      = -(A_F/2)D^2g(c_F):Sigma_F - R_F.

For every polynomial of degree at most two, R_F=0. In particular, if

    g(x)=a+b^T x+(1/2)x^T H x,

where H is symmetric, then

    integral_F g dA = A_F [g(c_F)+(1/2)H:Sigma_F].

## 3. Proof

Set y=x-c_F. Taylor expansion at c_F gives

    g(x)=g(c_F)+Dg(c_F)[y]+(1/2)D^2g(c_F)[y,y]+r_3(x),

with

    |r_3(x)| <= (1/6) sup_F ||D^3g|| |y|^3.

By the definition of the areal barycentre, integral_F y dA=0. Moreover,

    integral_F D^2g(c_F)[y,y] dA = A_F D^2g(c_F):Sigma_F.

Since |y|<=h_F throughout F, integration of the pointwise Taylor bound
gives the stated estimate for R_F. If g is quadratic, its third derivative
vanishes identically and the formula is exact. The covariance vertex formula
follows by integrating the barycentric monomials listed in Section 1.

## 4. Scope and exclusions

- The Hessian is the ambient Euclidean Hessian. The function must be defined
  on a neighbourhood of the planar cell.
- For a function defined only on a curved surface, an ambient extension or
  an intrinsic tangential expansion with curvature terms must be specified.
- The Q6 vertex covariance (1/4)I_6 is a distinct 6D vertex-measure result;
  it is not the covariance Sigma_F of a triangle.
- The Q6 edge-gradient FEM identity is a separate discrete result. It does
  not supply a bound on third derivatives or regularity of surface maps.
- This local theorem does not establish a closed embedded Q6 surface,
  orientability, absence of self-intersections, a refinement family, global
  weak convergence of surface measures, Mosco convergence, or Bernoulli
  coefficients in an asymptotic expansion.
- Bernoulli-number terms require a separate derivation from the chosen
  refinement or quadrature summation rule (for example, an applicable
  Euler–Maclaurin formula).

## 5. Companion implementation

The companion implementation and tests are maintained in
`fabianleonaressi95/rgs-qlg-quaternion-bridge`:

- `src/barycentric_triangle_quadrature.py`
- `tests/test_barycentric_triangle_quadrature.py`
- `docs/GATE_E1_BARYCENTRIC_COVARIANCE_QUADRATURE.md`

The test suite includes centroid and covariance checks, constant/affine and
quadratic exactness, an independent degree-three triangle rule, the cubic
remainder bound and h^5 scaling under similar-triangle refinement, and
degenerate-input rejection. Numerical tests support the implementation;
the proof above is independent of those tests.

## 6. Evidence classification

- **PROVED:** local covariance identity, Taylor formula, remainder bound,
  and exactness for polynomials of degree at most two.
- **NUMERICALLY VERIFIED:** only after the companion test suite is executed;
  no CI pass is asserted by this record.
- **OPEN:** geometric compatibility with the RGS/Q6 refinement family and
  any global quadrature or Bernoulli asymptotic theorem.