# X6 — Symbolic billiard coding and irrational rotations

**Status:** exact finite arithmetic for rational rotations; finite-precision comparison for the declared irrational target. No physical billiard or continuum PRISM identification is claimed.

## 1. Rotation and coding

Fix irrational alpha in (0,1) and T_alpha(x)=x+alpha mod 1. Use the half-open partition I0=[0,1-alpha), I1=[1-alpha,1), and code
s_n(x)=1 iff {x+n alpha} >= 1-alpha.
For phase x=0 this is floor((n+1)alpha)-floor(n alpha). The alternative interval [0,1-alpha) codes the complementary symbol (away from boundary conventions); the convention must not be silently mixed.

For rational alpha=p/q in lowest terms and rational phase, the orbit and code are periodic with period dividing q. Rational coding uses exact Fraction arithmetic. An irrational target stored as Decimal is only a finite-precision approximation.

## 2. Rational approximants

Continued-fraction convergents are computed exactly from p_k=a_k p_(k-1)+p_(k-2), q_k=a_k q_(k-1)+q_(k-2). The default target is sqrt(2)-1=[0;2,2,...]. The experiment records prefix mismatch counts, symbol frequency, finite-word subword complexity, return-time gaps, six-bit Q6 labels and Hamming transitions.

A finite-prefix mismatch count is not a convergence-rate theorem. Prefix length, phase, precision and partition are part of the experiment.

## 3. Q6 and PRISM comparison

Six consecutive symbols are packed as an integer in {0,...,63}, giving a label of a Q6 binary state. This is a coding map, not a dynamical conjugacy with the Q6 graph. A symbolic word can also be sampled periodically along a PRISM cycle factor C_m by reducing indices modulo m. Such a finite-cycle comparison does not identify an irrational orbit with a graph path or nearest-neighbour walk.

## 4. Implementation

- models/prism_billiard_coding.py: rotation coding, exact convergents, word complexity, return times, Q6 block packing and approximation report.
- scripts/run_prism_billiard_coding.py: deterministic JSON CLI.
- tests/test_prism_billiard_coding.py: rational periodicity, Decimal target, convergents and Q6 checks.

Example commands:

~~~bash
python -m pytest tests/test_prism_billiard_coding.py -q
python -m scripts.run_prism_billiard_coding --length 4096 --output prism_billiard_coding.json
~~~

Tests are added but must be executed before being described as passing.

## 5. Evidence boundary

**Exact:** rational convergents, rational orbit coding, integer block packing and finite-word combinatorics.

**Numerical:** comparison with a finite-decimal representation of sqrt(2)-1 at declared precision.

**Open:** discrepancy bounds; phase and partition dependence; symbolic coding for actual polygonal or curved billiards; a map into Q6/PRISM preserving a relevant dynamical structure; any continuum or physical interpretation.

The XCont billiard-fractal project motivates this comparison, but its visual patterns are not proof of an RGS–PSU claim.
