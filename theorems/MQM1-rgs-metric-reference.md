# MQM-1 reference from the RGS-PSU edge coframe

**Classification:** canonical finite metric-graph construction from the hash-checked RGS seed and its documented four-component PSU edge coframe, with numerical verification of the 16 native RGS/Q6 gate invariances. The metric-graph Dirichlet constitutive choice is explicit; its physical identification with MQM-1 remains open.

## 1. Geometric input

Let X:V(Q6)->R^3 be the recovered 64-site RGS seed, with the canonical SHA-256 recorded in src/rgs_seed_64_reconstruction.py. For every canonical Q6 edge e=(u,v), reconstruct the PSU raw coframe documented in the recovered manifest:
C_e^PSU=(X_v-X_u, ||X_v||-||X_u||) in R^4.

Define the edge metric length by
L_e^PSU=||C_e^PSU||_2>0.
This uses the radial fourth component as well as the three Cartesian increments. It does not invent an independent coordinate or a cube-sphere weight.

## 2. Metric-graph Dirichlet reference

For a linearly interpolated scalar field on a one-dimensional metric edge of length L_e^PSU, the exact edge Dirichlet energy is proportional to |f_v-f_u|^2/L_e^PSU. Fix the common scale by the RMS PSU edge length
ell_rms=(192^{-1} sum_e (L_e^PSU)^2)^{1/2}.
The dimensionless conductance and MQM-1 log-reference are
w*_e=ell_rms/L_e^PSU,   x*_e=log(ell_rms/L_e^PSU).

This is an edgewise reference, not a six-number direction average. The metric-graph Dirichlet convention is mathematically standard once the PSU coframe norm is taken as edge length. Its adoption as the MQM-1 constitutive term is a declared model closure, not a uniquely forced consequence of the existing dissipative action.

## 3. Symmetry

Every native RGS/Q6 gate g induces a permutation of the 192 edges. The 16 adjacency-preserving RGS actions are restrictions of signed coordinate isometries of the recovered seed. These preserve Cartesian differences and vertex radii, hence preserve the four-component PSU coframe norm:
L^PSU_{rho_g(e)}=L^PSU_e.
Therefore x* is invariant under all 16 gates, including PAIRSWAP, and the metric-derived reference does not reduce the native RGS/Q6 gate group.

The remaining 32 elements of the 48-element point-cloud O_h action are not automorphisms of canonical Q6 adjacency and are not promoted to symmetries of the 192-edge MQM-1 graph.

## 4. Finite-seed numerical record

The audit reconstructs all 192 four-component coframes from the hash-checked seed. It reports 13 distinct PSU edge-length classes at 12-decimal precision and directional RMS lengths approximately
(2.23606798, 2.23606798, 2.23606798, 1.70244680, 1.70244680, 1.32773694).
All 16 induced edge permutations preserve the edgewise reference, with residual at most 1e-12.

Reproduce:
    python -m unittest discover -s tests -p test_mqm_rgs_metric_reference.py -v

## 5. Evidence boundary

**Established mathematically:** the one-dimensional metric-edge Dirichlet weight is proportional to inverse edge length; graph isometries preserving the metric preserve the associated weighted Laplacian and its reference conductances.

**Numerically verified for the finite RGS-PSU seed:** reconstruction of 192 four-component coframes; 13 length classes; invariance of the complete edgewise x* under all 16 native RGS/Q6 gates.

**Open:** independent comparison of the reconstructed coframes with the binary A13 archived coframe array; derivation of the metric-graph Dirichlet term from the full microscopic RGS-PSU action; physical PSU length units; stiffness/mobility calibration; whether higher-dimensional FEEC/PSU discretization changes the inverse-length exponent; continuum convergence and experiment. No physical anisotropy law is claimed.
