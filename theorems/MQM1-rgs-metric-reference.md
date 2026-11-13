# MQM-1 reference from the RGS seed metric

**Classification:** canonical finite metric-graph construction from the hash-checked RGS embedding, with numerical verification of the 16 native RGS/Q6 gate invariances. The metric-graph Dirichlet constitutive choice is explicit; its physical identification with MQM-1 remains open.

## 1. Geometric input

Let the canonical RGS seed be X:V(Q6)->R^3, with 64 vertices, loaded from src/rgs_seed_64_reconstruction.py. Its coordinate bytes are checked against SHA-256:
6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf.

For each of the 192 canonical Q6 edges e=(u,v), define its RGS chord length L_e=||X_u-X_v||_2>0. No new coordinates, vertex weights, or cube-sphere interpolation factors are introduced.

## 2. Metric-graph Dirichlet reference

On a one-dimensional metric graph, the edgewise Dirichlet energy of a linearly interpolated scalar field is
D(f)=1/2 sum_{e=(u,v)} (ell_0/L_e)|f_v-f_u|^2,
where ell_0 is a common reference length making conductances dimensionless. Fix the scale without an external parameter by
ell_0=L_rms=(192^{-1} sum_e L_e^2)^{1/2}.
This yields
w*e=L_rms/L_e,   x*e=log(L_rms/L_e).

This is an edgewise reference, not a six-number direction average. It is the standard metric-graph Dirichlet weighting after a declared scale normalization. The graph-energy convention is a modelling choice; it is not claimed to be uniquely forced by the current MQM-1 action.

## 3. Exact symmetry criterion

Every native RGS/Q6 gate g acts on vertices and induces an edge permutation rho_g. The recovered RGS embedding is invariant under the corresponding induced signed-coordinate isometry for all 16 adjacency-preserving actions. Consequently
L_{rho_g(e)}=L_e, hence x*_{rho_g(e)}=x*_e.
Therefore the full 16-element RGS/Q6 gate group survives the metric-derived reference, including the coupled PAIRSWAP.

This is checked edge by edge on all 192 conductances. The full 48-element point-cloud group O_h is not claimed to act on the bare Q6 graph: the 32 transformations that fail Q6 adjacency remain excluded.

## 4. Finite-seed numerical record

The audit reports:
- 192 positive RGS edge lengths;
- 13 distinct edge-length classes at 12-decimal reporting precision;
- direction-wise RMS chord lengths approximately (2.23606798, 2.23606798, 2.23606798, 1.55036970, 1.55036970, 1.14963135);
- all 16 induced RGS/Q6 edge permutations preserve the full edgewise x*, with maximum numerical residual at most 1e-12.

The repeated directional RMS values are consistent with the paired coordinate actions, but the symmetry conclusion is based on the full edge permutation, not on those averages.

Reproduce:
    python -m unittest discover -s tests -p test_mqm_rgs_metric_reference.py -v

## 5. Evidence boundary

**Established mathematically:** given a metric graph with edge lengths L_e, the linear-edge Dirichlet form has conductance proportional to L_e^{-1}; any graph isometry preserving edge lengths preserves these conductances and the corresponding weighted Laplacian.

**Numerically verified for this finite seed:** the 16 RGS/Q6 actions preserve all 192 reconstructed edge lengths and hence the constructed reference vector.

**Open:** derivation of the metric-graph Dirichlet term from a microscopic RGS-PSU action; physical units and PSU length scale; calibration of overall stiffness and coupling; whether a higher-dimensional FEEC/PSU discretization changes the exponent of L_e; continuum convergence and experimental validation. This does not prove a physical anisotropy law.
