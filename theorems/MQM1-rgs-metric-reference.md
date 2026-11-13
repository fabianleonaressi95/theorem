# MQM-1 reference from the RGS-PSU edge coframe

**Classification:** the reconstructed A13 normalized coframe is hash-identical to the manifest's archived coframe; the 192 raw coframe norms and their metric-graph conductances are a finite-seed geometric construction. All 16 native RGS/Q6 gates preserve the resulting edgewise reference. **The inverse-length conductance is not yet derived by the current microscopic A13 SEA action.**

## 1. Exact A13 coframe provenance

The recovered A13 source defines, for every ordered Q6 edge e=(g,h),
C_e^raw=(X_h-X_g, ||X_h||-||X_g||) in R^4,
and archives the unit coframe
C_hat_e=C_e^raw/||C_e^raw||.

The reconstruction uses the hash-checked 64-site RGS seed and the canonical Q6 edge order. It reproduces:
- Q6 edge-order SHA-256: da7854ca655577b629dc508208918326fde1d50563485f953ea0fdc1b2fb78e8;
- A13 normalized-coframe SHA-256: 72980c38fdc652ece31895cf5c9f113a6206675fdf876c924bf6890d6e7fc263.

These match the exact hashes recorded in data/rgs_188d/ellis_curved_seed_manifest.json. Thus the reconstruction is not merely similar to the A13 coframe: in the canonical float64 byte order it is identical to the archived array. The normalized coframe has unit norm by construction; its norm must not be mistaken for a physical edge length.

The metric length used below is the norm of the **raw** coframe:
L_e=||C_e^raw||_2.
The raw lengths have 13 distinct classes at 12-decimal reporting precision.

## 2. Where inverse length comes from — and where it does not

For a scalar field linearly interpolated along a metric edge of length L_e, the one-dimensional continuum Dirichlet action is
S_e[f]=(1/2) integral_0^{L_e} |df/ds|^2 ds.
The linear interpolant has df/ds=(f_h-f_g)/L_e, so exactly
S_e[f]=(1/2)|f_h-f_g|^2/L_e.

With ell_rms=(192^{-1} sum_e L_e^2)^(1/2), define dimensionless conductance w_e=ell_rms/L_e. The corresponding discrete action is
S_metric[f]=(1/2) sum_e w_e |f_h-f_g|^2
           =(1/2) f^T B diag(w) B^T f,
where B is the 64x192 oriented incidence matrix. Hence
K_metric=B diag(ell_rms/L_e) B^T
and x*_e=log(w_e)=log(ell_rms/L_e).

This is an exact finite-element identity **conditional on choosing** the scalar metric-edge Dirichlet action and the raw PSU coframe norm as the edge metric. It is not obtained by taking the norm of the archived unit coframe.

### Comparison with the current A13 SEA action

The recovered SEA implementation uses the normalized unit coframe ehat_e in its fermion symbol,
(D_kin)_{gh}=kappa (gamma_A ehat_e^A) tensor U_gh,
and uses the unweighted graph Laplacian L_Q6 in its bosonic block,
K_B(q)=diag(L_Q6+m_B^2,L_Q6+m_B^2)+mu H_cross+lambda_B q diag(tau,tau).

Thus the currently archived A13 action contains directional PSU coframe data and an unweighted graph Laplacian, but no explicit scalar factor ell_rms/L_e. Its fermion/boson determinant identities do not, by themselves, prove that this extra inverse-length conductance is generated. The metric-edge term is a clearly specified candidate extension to the action.

To claim a microscopic derivation, the next necessary step is to introduce a scalar field (or identify an existing MQM-1 degree of freedom) in the RGS–PSU action, derive its continuum kinetic term in the PSU metric, and show that the A13/Q6 discretization converges to the displayed weighted form. Until then, classify w_e as a geometrically motivated constitutive closure, not a derived physical law.

## 3. Symmetry of the finite reference

Every native RGS/Q6 gate induces a permutation rho_g of the 192 canonical edges. The 16 adjacency-preserving actions preserve the reconstructed RGS seed's Cartesian distances and vertex radii, hence preserve L_e=||C_e^raw|| and w_e edge by edge. Therefore
G_MQM(x*)=G_RGS-Q6,   |G_MQM(x*)|=16.
PAIRSWAP survives. The other 32 elements of the 48-element point-cloud O_h action are not automorphisms of Q6 adjacency and are not promoted to graph symmetries.

The audit verifies the full edgewise reference, not merely direction-averaged RMS values.

## 4. Reproducibility

Run:
    python -m unittest discover -s tests -p test_mqm_rgs_metric_reference.py -v

The focused suite checks the exact A13 normalized-coframe hash, canonical edge order, raw-vs-unit coframe distinction, 13 raw-length classes, positive-semidefinite weighted Laplacian, all 16 gate invariances, and the current A13 action's explicit absence of the inverse-length factor.

## 5. Evidence ledger

**Exact identity:** linear-edge interpolation gives the factor 1/L_e in the one-dimensional Dirichlet action.

**Exact provenance match:** reconstructed normalized A13 coframe bytes match the SHA-256 recorded in the recovered manifest.

**Finite-seed numerical result:** all 16 native RGS/Q6 gates preserve the 192 raw PSU coframe norms and the associated reference.

**Candidate extension:** adding K_metric to the MQM-1 scalar sector.

**Open:** microscopic identification of the scalar field and its action; derivation from the full RGS–PSU variational principle; physical PSU length units and coupling calibration; FEEC/PSU higher-dimensional discretization; refinement/continuum convergence and experiment.
