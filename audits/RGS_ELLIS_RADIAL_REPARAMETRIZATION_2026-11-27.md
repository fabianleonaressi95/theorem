# RGS–Ellis radial reparametrization: analytic audit (2026-11-27)

**Status:** exact conditional geometric identity; not a new Einstein-equation solution and not yet a theorem about an independently specified RGS metric.

## 1. Input profile and its global minimum

Take the previously used profile, with the parameters stated in the working record,

\[
\phi(r)=r^2-2.963\log(r),\qquad r>0,
\]
\[
R(r)=r e^{\phi(r)}=r^{-1.963}e^{r^2}.
\]

The logarithm is dimensionless here because the inherited convention is \(\ell=1\). For a dimensionful radial coordinate, the reference scale must be restored: \(\log(r/\ell)\).

Set \(f(r)=\log R(r)\). Then
\[
f'(r)=2r-\frac{1.963}{r},\qquad
f''(r)=2+\frac{1.963}{r^2}>0.
\]
There is exactly one critical point on \((0,\infty)\), and it is the strict global minimum:
\[
r_*=\sqrt{0.9815}=0.990706818387761\ldots
\]
Since \(R(r)\to\infty\) as \(r\downarrow0\) and as \(r\to\infty\), the minimum is global. Numerically,
\[
R_0=R(r_*)=2.717813807421031\ldots
\]
and
\[
A_0=4\pi R_0^2=92.8216459798357\ldots.
\]
At the minimum, \(f'(r_*)=0\) and \(f''(r_*)=4\), hence
\[
R''(r_*)=4R_0,\qquad A''(r_*)=32\pi R_0^2.
\]

## 2. Exact radial reparametrization

Define
\[
l(r)=\operatorname{sgn}(r-r_*)\sqrt{R(r)^2-R_0^2}.
\]
This is real for every \(r>0\), because \(R(r)\ge R_0\). It maps the two sides of the minimum to the two signs of \(l\). The inverse relation is exactly
\[
\boxed{R(l)=\sqrt{R_0^2+l^2}}.
\]
The map is strictly increasing. Away from the throat,
\[
\frac{dl}{dr}=\frac{R(r)|R'(r)|}{\sqrt{R(r)^2-R_0^2}}>0,
\]
and the limit at the throat is
\[
\lim_{r\to r_*}\frac{dl}{dr}=2R_0>0.
\]
Thus it is a regular local coordinate through the throat; the asymptotics of \(R\) at both ends show that its range is all of \(\mathbb R\).

Differentiating the exact inverse relation gives
\[
\frac{dR}{dl}=\frac{l}{R},\qquad
\frac{d^2R}{dl^2}=\frac{R_0^2}{R^3}.
\]
At the throat,
\[
R'(0)=0,\qquad R''(0)=\frac1{R_0}
=0.3679427918\ldots.
\]

## 3. Spatial metric and shape function: the conditional step

If one **chooses** the radial spatial metric to be
\[
ds_{\rm sp}^2=dl^2+R(l)^2d\Omega^2,
\]
then in areal-radius coordinates it becomes
\[
ds_{\rm sp}^2=
\frac{dR^2}{1-b(R)/R}+R^2d\Omega^2,
\]
with
\[
\boxed{b(R)=\frac{R_0^2}{R}}.
\]
Consequently,
\[
b(R_0)=R_0,\qquad b'(R_0)=-1<1.
\]
This is the standard Ellis spatial wormhole geometry (the zero-redshift, ultrastatic choice gives the usual Ellis–Bronnikov spacetime form).

**Logical limitation:** the coordinate definition above does not derive this radial metric from an independently specified RGS line element. It constructs a coordinate in which the chosen spatial metric has the Ellis form. The profile \(R(r)\) fixes the areal-radius function and its minimum, but by itself does not fix \(g_{rr}\), lapse/redshift, field equations, or matter source. Therefore the exact identity is a conditional geometric representation, not evidence that the RGS model dynamically predicts an Ellis wormhole.

## 4. Mass and energy-condition statements

For the spatial metric just specified, the Misner–Sharp mass is
\[
M_{\rm MS}(R)=\frac{b(R)}2=\frac{R_0^2}{2R}
=\frac{R_0^2}{2\sqrt{R_0^2+l^2}}.
\]
It tends to zero as \(|l|\to\infty\). This is the mass function of this ultrastatic Ellis geometry; the ADM mass is zero at either asymptotic end.

If the spacetime is additionally taken to be ultrastatic (constant redshift) and Einstein's equations are imposed in four dimensions with \(G=c=1\), the required stress tensor has
\[
\rho=p_r=-\frac{R_0^2}{8\pi R^4},\qquad
p_t=+\frac{R_0^2}{8\pi R^4}.
\]
Thus \(\rho+p_r<0\): the radial null energy condition is violated. This is a property of the specified Ellis solution and its required source, not a matter model derived from RGS.

## 5. Inherited raccordo coordinates: do not conflate symbols

The working notes contain the coordinate values
\[
r_1=1.089778,\qquad r_2=1.981414.
\]
They are carried here as **inherited, not independently revalidated** interface coordinates. Evaluating the unmodified profile gives
\[
R(r_1)=2.770004974239646\ldots,\qquad
R(r_2)=13.245805999223967\ldots.
\]
If (and only if) the historical symbol \(R_1\) was defined as the areal radius at the first interface, then \(R_1=R(r_1)\). The present record does not establish that historical definition; it must not silently identify \(R_1\) with \(r_1\), nor infer a new independent parameter from notation alone.

The corresponding values of the above constructed proper coordinate are
\[
l(r_1)=-0.535178162394523\ldots,\qquad
l(r_2)=12.963983364586257\ldots.
\]
These evaluations do not prove that a proposed cutoff or matching function is \(C^2\), monotone, or compatible with the full metric.

## 6. Status and open gates

**Established analytically in this note**
- the unique global minimum of the stated scalar profile;
- the exact, monotone radial reparametrization defined above;
- the Ellis form of the spatial metric, conditional on choosing \(ds_{\rm sp}^2=dl^2+R(l)^2d\Omega^2\);
- the associated shape function and its flare-out condition.

**Not established**
1. That this spatial metric follows from the original RGS ansatz rather than being imposed by the reparametrization.
2. The original definition and provenance of \(R_1\), and the derivation/status of \(r_1,r_2\).
3. A valid global matching/cutoff preserving \(R\ge R_0\), with the required differentiability of the complete metric.
4. A lapse/redshift function and a solution of the full Einstein equations from an independently specified RGS matter/action sector.
5. Any RGS derivation of the exotic stress tensor or resolution of the null-energy-condition violation.

**Repository classification:** audit / conditional geometric identity. Do not assign a numbered theorem or promote it to a proved RGS wormhole theorem until gates 1–4 are closed. The earlier claim that a particular quintic multiplicative cutoff produces two additional extrema is not repeated as a verified result here; it requires a committed reproducible calculation and exact definition of the cutoff before it can be cited.


## 7. Metric-level equivalence test: the missing RGS coefficient

The RGS–EMS radial ansatz used in the earlier geometric work is
\[
ds^2=-N(r)^2c^2dt^2+A(r)^2dr^2+R(r)^2d\Omega^2.
\]
Here \(A(r)\) is the radial metric coefficient (not the areal radius), and the proper radial coordinate is defined by
\[
dl=A(r)\,dr
\]
on an oriented chart, with \(A>0\). The scalar profile \(R(r)\) alone does not determine \(A(r)\) or \(N(r)\).

For this metric to be exactly the ultrastatic Ellis metric with throat radius \(R_0\),
\[
ds^2=-c^2dt^2+dl^2+R(l)^2d\Omega^2,\qquad
R(l)^2=R_0^2+l^2,
\]
the necessary and sufficient coefficient conditions (away from the throat, extended by continuity at it) are
\[
\boxed{N(r)=1,\qquad
A(r)^2=\frac{R'(r)^2}{1-R_0^2/R(r)^2}
=\frac{R(r)^2R'(r)^2}{R(r)^2-R_0^2}.}
\]
Equivalently, on the two sides,
\[
A(r)=\left|\frac{R(r)R'(r)}{\sqrt{R(r)^2-R_0^2}}\right|.
\]
For the inherited profile, \(R'/R=2r-1.963/r\). At the throat the apparent \(0/0\) has the finite limit
\[
A(r_*)=2R_0=5.435627614842063\ldots.
\]
This is a **testable required form** for the original RGS radial coefficient, not a derivation of that coefficient. If the independently derived RGS \(A(r)\) fails this identity, the metric is not the ultrastatic Ellis metric in this coordinate. If it satisfies it and the lapse is unity, the equivalence follows by direct coordinate change.

For a nonconstant lapse, the spatial slices can still have the Ellis spatial geometry, but the full spacetime is not the ultrastatic Ellis solution. A lapse profile must be derived from the RGS field equations or action; it cannot be chosen after the fact and described as an RGS prediction.

### What the current archive establishes

The historical RGS ansatz record supplies the general coframe/metric notation \(N,A,R\), with proper distance \(d\ell=A\,du\), but the exact functions \(A(r)\) and \(N(r)\) for the numerical profile \(\phi(r)=r^2-2.963\log r\) have not been recovered in the available source material. No equation currently links \(A\) to \(\phi\). Consequently the metric-level identity above cannot yet be evaluated against the original RGS model.

### Required source recovery / next proof obligations

1. Locate the original RGS derivation that defines \(A\) and \(N\) as functions of the same coordinate used in \(R(r)=r e^{\phi(r)}\). Do not combine formulas written in different radial gauges without transforming them.
2. Substitute the original \(A(r)\) into the boxed identity and simplify symbolically. Check the throat limit separately.
3. Derive or retrieve \(N(r)\) from the same model and test whether it is identically one after asymptotic time normalization.
4. Only after 1–3, compute the Einstein tensor of the complete metric and compare it with the stress tensor derived from the RGS action. Do not import the Ellis phantom-scalar source as though it had been derived by RGS.
5. Treat \(r_1,r_2\) as matching coordinates only after the actual matching equations and boundary data are located. A pair of coordinate values cannot determine a \(C^2\) metric matching by itself.

**Updated classification:** the radial-profile lemma is proved; the Ellis coordinate representation is an exact conditional construction; equivalence of the original RGS–EMS spacetime to Ellis is **open / not established** pending recovery and verification of \(A(r)\), \(N(r)\), and the model field equations.


For reproducibility, evaluating the required coefficient from the inherited profile gives
\[
A_{\rm Ellis}(r_*)=5.435627614842062\ldots,
\]
\[
A_{\rm Ellis}(r_1)=5.423336691037318\ldots,\qquad
A_{\rm Ellis}(r_2)=40.22396279314685\ldots.
\]
These are **target values** for comparison with a separately derived RGS coefficient; they are not measured or recovered RGS metric data.
