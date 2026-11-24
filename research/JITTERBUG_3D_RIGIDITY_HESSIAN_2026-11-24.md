# 3D Jitterbug linkage: rigidity Hessian and mechanism spectrum

**Date:** 2026-11-24  
**Classification:** [P] exact 12-joint/24-rod/eight-panel incidence inherited from the canonical Jitterbug construction; [N] linearized rigidity rank and Hessian spectrum; [O] material phonons, physical phasons, damping, Green–Kubo transport and continuum calibration.

## 1. Why this is the next admissible 3D lift

The existing Q6/FCC audit proves an exact geometric identification of a distinguished 12-point subset with the 12 Jitterbug joints, but it also proves that the 24 Jitterbug rods are **not** edges of the stored 64-TG FCC graph. The full 64-TG dynamic extension remains open. We therefore do not identify the Jitterbug linkage with the full Q6 graph or invent trajectories for its other vertices.

The construction below uses only the independently established 12-joint Jitterbug linkage in its cuboctahedral reference pose. It is a genuine three-dimensional mechanical benchmark and a controlled starting point for a later coupled model.

## 2. Geometry and incidence

Let the 12 vertices be the permutations of
\[
2^{-1/2}(\pm1,\pm1,0).
\]
Join two vertices when their Euclidean distance is one. This gives 24 unit rods. The eight sign-triple triangular panels are the existing rigid_triangles faces. Their 24 panel edges cover the rod set exactly. The panel shared-vertex contact graph has 8 vertices and 12 contacts, with Hamming distance one between adjacent sign triples. A contact is one shared vertex, not a shared hinge edge.

These are linkage incidence data; they are not inherited Q6/FCC cell incidence.

## 3. Central-force energy and Hessian

For vertex displacements u_i in R^3, define the stress-free unit-spring energy
\[
H(u)=\frac12\sum_{(i,j)\in E_J}
\left(\lVert x_i+u_i-x_j-u_j\rVert-1\right)^2.
\]
At the cuboctahedral reference pose every rod has length one, so the first derivative vanishes. Let R in R^(24x36) be the rigidity matrix, with row for rod (i,j) equal to the unit rod direction in the i block, its negative in the j block, and zero elsewhere. The quadratic expansion is
\[
H(u)=\frac12u^T K u+O(\lVert u\rVert^3),
\qquad K=R^TR.
\]
This is derived from one declared energy; no independent spring weights or fitted Hessian entries are introduced.

## 4. Numerical rigidity result

The reproducible audit obtains:
- 36 Cartesian degrees of freedom;
- rigidity rank 24 and Hessian rank 24;
- nullity 12;
- six null modes are rigid-body translations/rotations;
- six additional null modes are internal infinitesimal mechanisms.

The positive Hessian spectrum, in the unit spring/length convention, is
\[
\begin{array}{c|rrrrrr}
\lambda & 2-\sqrt2 & 1 & 2 & 3 & 2+\sqrt2 & 4\\
\text{multiplicity} & 3&5&9&3&3&1
\end{array}
\]
The multiplicities sum to 24, matching the rigidity rank. The six non-rigid mechanisms mean that this 24-rod framework is not infinitesimally rigid and its Hessian is not positive definite on the quotient by rigid-body motions.

The rank, nullity and spectrum are numerical linear-algebra results with explicit tolerances, not a formal exact-arithmetic proof. The finite incidence counts and the energy-to-Hessian identity are exact under the stated construction.

## 5. Physical interpretation boundary

This is a finite central-force linkage model. Its 24 positive modes are finite-framework stiffness modes, not automatically material phonon branches. The six additional mechanisms are not called phasons: a physical phason sector requires an independently defined internal coordinate, a microscopic energy coupling, and a dynamical law. Nor does this static Hessian provide damping or a Green–Kubo coefficient.

In particular, the scalar-mobility OU result for the bare Q6 model cannot simply be transferred to this linkage. A valid next transport calculation must derive a strain-dependent energy for the same Jitterbug coordinates, differentiate that energy to obtain the stress observable, resolve the six mechanisms (or retain them as explicit zero modes), and justify any relaxation process. A physical viscosity still requires a calibrated material volume, stress, and long-time/size limits.

## 6. Reproduction

Run:

    python audits/jitterbug_mechanical_hessian.py
    python -m pytest -q tests/test_jitterbug_mechanical_hessian.py

Implementation: audits/jitterbug_mechanical_hessian.py.  
Tests: tests/test_jitterbug_mechanical_hessian.py.  
Dedicated CI: https://github.com/fabianleonaressi95/theorem/actions/runs/45403756229 (success; 2 tests passed and audit JSON emitted).

**Conclusion:** [N] the 3D Jitterbug central-force lift has six internal infinitesimal mechanisms in addition to six rigid-body modes. This is a useful structural constraint on any future phonon/phason or Green–Kubo extension, not yet such an extension.
