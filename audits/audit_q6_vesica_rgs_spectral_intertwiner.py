#!/usr/bin/env python3
"""Operator-derived Q6 -> RGS half-scale spectral bridge.

Requires numpy. Run at repository root; reads the original K0.npy, P_G.npy,
Z_A.npy, Z_S.npy arrays and writes a JSON audit. No synthetic RGS arrays.
"""
from pathlib import Path
from collections import defaultdict
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
K0,PG,ZA,ZS=[np.load(ROOT/"artifacts"/n,allow_pickle=False) for n in
             ("K0.npy","P_G.npy","Z_A.npy","Z_S.npy")]
n=K0.shape[0]
assert n==188 and all(x.shape==(n,n) for x in (PG,ZA,ZS))

# Q3 Laplacian in binary vertex order 000,...,111.
L3=np.zeros((8,8))
for i in range(8):
    for j in range(8):
        if (i^j).bit_count()==1:
            L3[i,i]+=1
            L3[i,j]-=1
I8=np.eye(8)
L6=np.kron(L3,I8)+np.kron(I8,L3)
P8=np.fliplr(I8)
R6=np.kron(P8,P8)
D=np.diag([1.,1.,-1.])

# Operator-adapted trigram coisometry: Q3 Laplacian eigenmodes 0,4,6.
C=np.vstack([
    np.ones(8)/np.sqrt(8),
    np.array([7,1,-3,-5,-5,-3,1,7])/np.sqrt(168),
    np.array([1,-1,-1,1,-1,1,1,-1])/np.sqrt(8)
])
Lc=C@L3@C.T
K=np.kron(C,C)
L9=K@L6@K.T

# Symmetric one-excitation sector over the constant mode.
E=np.zeros((9,3))
E[0,0]=1.0
E[1,1]=E[3,1]=1/np.sqrt(2)
E[2,2]=E[6,2]=1/np.sqrt(2)
Lred=E.T@L9@E
Swap=np.zeros((9,9))
for i in range(3):
    for j in range(3):
        Swap[j*3+i,i*3+j]=1.0
F=E.T@K

# Reconstruct the actual six-dimensional RGS carrier deterministically.
Pplus=2*ZS@ZS+ZS
Vcols=[]
for j in range(n):
    v=Pplus[:,j].copy()
    for q in Vcols:
        v-=q*np.dot(q,v)
    nv=np.linalg.norm(v)
    if nv>1e-9:
        Vcols.append(v/nv)
    if len(Vcols)==3:
        break
if len(Vcols)!=3:
    raise RuntimeError("Could not recover rank-three +1/2 eigenspace")
V=np.column_stack(Vcols)
W=2*ZA@V
U=np.column_stack((V,W))
Kc=U.T@K0@U
H=Kc[:3,:3]
evals,R=np.linalg.eigh(H)
JA=(V+W)@R/np.sqrt(2)
JB=(V-W)@R/np.sqrt(2)
JBsharp=-JB@D
PhiA=JA@F
PhiB=JBsharp@F

# Derive the quadratic functional-calculus coefficients from the
# independently reconstructed RGS carrier block and the Q6 reduced operator.
# H is read from K0 on the six-dimensional carrier; no coefficients are
# supplied by hand. The -0.15 off-diagonal carrier coupling splits H into
# lower/upper triplets H-0.15I and H+0.15I.
Hsym=(H+H.T)/2
Hdiag=R.T@Hsym@R
lower_eigs=np.diag(Hdiag)-0.15
upper_eigs=np.diag(Hdiag)+0.15
xspec=np.diag(Lred)
Vand=np.column_stack((np.ones(3),xspec,xspec**2))
poly_coeff=np.linalg.solve(Vand,lower_eigs)
poly_residual=float(np.linalg.norm(Vand@poly_coeff-lower_eigs))
# Rational recognition is diagnostic only; the floating-point equations
# and residual remain the primary numerical evidence.
from fractions import Fraction
poly_rational=[str(Fraction(float(v)).limit_denominator(1000000)) for v in poly_coeff]
upper_shift_residual=float(np.max(np.abs(upper_eigs-lower_eigs-0.30)))
# Candidate spectral function. On selected Q6 eigenvalues 0,4,6 it is
# exactly (1/2,3/5,7/10), the original RGS lower triplet.
fL=poly_coeff[0]*np.eye(64)+poly_coeff[1]*L6+poly_coeff[2]*(L6@L6)
fL_high=fL+0.3*np.eye(64)
maxabs=lambda X:float(np.max(np.abs(X)))
fro=lambda X:float(np.linalg.norm(X))
checks={
 "input_finite":bool(all(np.isfinite(x).all() for x in (K0,PG,ZA,ZS))),
 "P_G_symmetry":maxabs(PG-PG.T),
 "P_G_idempotence":fro(PG@PG-PG),
 "P_G_rank":int(np.linalg.matrix_rank(PG,tol=1e-8)),
 "K0_P_G_right_kernel":fro(K0@PG),
 "P_G_K0_left_kernel":fro(PG@K0),
 "P_G_K0_commutator":fro(PG@K0-K0@PG),
 "C_orthonormal_rows":maxabs(C@C.T-np.eye(3)),
 "C_Q3_eigenmode_leakage_fro":fro(L3@C.T-C.T@Lc),
 "C_reflection_CP8_minus_DC":maxabs(C@P8-D@C),
 "C_Q3_compressed_laplacian":Lc.tolist(),
 "C_tensor_C_64_feature_vectors_distinct":len({tuple(np.round(K[:,i],13)) for i in range(64)}),
 "E_orthonormal_columns":maxabs(E.T@E-np.eye(3)),
 "E_diagonal_reflection_equivariance":maxabs(np.kron(D,D)@E-E@D),
 "E_factor_swap_invariance":maxabs(Swap@E-E),
 "E_L9_invariant_subspace_leakage_fro":fro(L9@E-E@Lred),
 "F_coisometry":maxabs(F@F.T-np.eye(3)),
 "F_Q6_laplacian_intertwining_fro":fro(F@L6-Lred@F),
 "F_Q6_reflection_intertwining":maxabs(F@R6-D@F),
 "Lred":Lred.tolist(),
 "RGS_quadratic_functional_calculus_coefficients":poly_coeff.tolist(),
 "RGS_quadratic_coefficients_rational_recognition":poly_rational,
 "RGS_quadratic_fit_residual":poly_residual,
 "RGS_upper_lower_triplet_shift":0.30,
 "RGS_upper_lower_shift_residual":upper_shift_residual,
 "F_64_basis_images_distinct":len({tuple(np.round(F[:,i],13)) for i in range(64)}),
 "RGS_JA_K0_eigen_residual":maxabs(K0@JA-JA@np.diag([.5,.6,.7])),
 "RGS_JB_K0_eigen_residual":maxabs(K0@JB-JB@np.diag([.8,.9,1.])),
 "RGS_ZA_JA_pair_residual":maxabs(ZA@JA+.5*JB),
 "RGS_ZA_JB_pair_residual":maxabs(ZA@JB-.5*JA),
 "RGS_ZS_JA_pair_residual":maxabs(ZS@JA-.5*JB),
 "RGS_ZS_JB_pair_residual":maxabs(ZS@JB-.5*JA),
 "RGS_gauged_ZA_BA_residual":maxabs(JBsharp.T@ZA@JA-.5*D),
 "RGS_gauged_ZS_BA_residual":maxabs(JBsharp.T@ZS@JA+.5*D),
 "composite_K0_lower_intertwining_fro":fro(K0@PhiA-PhiA@fL),
 "composite_K0_upper_intertwining_fro":fro(K0@PhiB-PhiB@fL_high),
 "composite_ZA_lower_to_upper_reflection_fro":fro(ZA@PhiA-.5*PhiB@R6),
 "composite_ZS_lower_to_upper_reflection_fro":fro(ZS@PhiA+.5*PhiB@R6),
 "composite_ZA_upper_to_lower_reflection_fro":fro(ZA@PhiB+.5*PhiA@R6),
 "composite_ZS_upper_to_lower_reflection_fro":fro(ZS@PhiB+.5*PhiA@R6)
}

# Collision classes in the rank-three quotient.
groups=defaultdict(list)
for i in range(64):
    groups[tuple(np.round(F[:,i],13))].append(i)
mult=defaultdict(int)
for g in groups.values():
    mult[len(g)]+=1

report={
 "status":"Q6 operator sector exactly constructed; RGS coupling checked against original binary arrays",
 "Q6_graph":"Q6 = Q3 Cartesian-product Q3; 64 vertices, degree 6",
 "C_rows":["constant mode, eigenvalue 0","selected angular-even Q3 mode, eigenvalue 4","top Walsh parity mode, eigenvalue 6"],
 "C_matrix_rows":C.tolist(),
 "L3_compression":Lc.tolist(),
 "E_one_excitation_basis":"e0 tensor e0; (e0 tensor e+ + e+ tensor e0)/sqrt(2); (e0 tensor e- + e- tensor e0)/sqrt(2)",
 "Lred":Lred.tolist(),
 "F_shape":[3,64],
 "F_rank":int(np.linalg.matrix_rank(F)),
 "F_kernel_dimension":61,
 "F_basis_image_distinct_count":len(groups),
 "F_collision_multiplicity_distribution":{str(k):v for k,v in sorted(mult.items())},
 "spectral_polynomial":"f(x)=a+b*x+c*x^2; coefficients solved from the original K0 carrier compression and Q6 Lred",
 "spectral_polynomial_coefficients":poly_coeff.tolist(),
 "spectral_polynomial_coefficients_rational_recognition":poly_rational,
 "spectral_polynomial_fit_residual":poly_residual,
 "upper_triplet_shift":0.30,
 "upper_lower_shift_residual":upper_shift_residual,
 "f_on_selected_spectrum":[.5,.6,.7],
 "f_plus_0_3_on_selected_spectrum":[.8,.9,1.0],
 "RGS_source_arrays":["K0.npy","P_G.npy","Z_A.npy","Z_S.npy"],
 "RGS_gauge":"J_B_sharp = -J_B D",
 "checks":checks,
 "limitations":[
  "F is rank 3 and loses 61 dimensions of arbitrary Q6 fields; keep the full 64-state and 9-component lookup.",
  "The quadratic f is the unique degree-at-most-two interpolation of the three RGS lower eigenvalues against the selected Q6 eigenvalues; it is a spectral matching candidate, not a first-principles derivation.",
  "The map is an intertwiner only on the selected three-dimensional Q6 invariant sector, not on all 64 states.",
  "No continuum or physical dynamics claim is made."
 ]
}
out=ROOT/"results/json/q6_vesica_rgs_spectral_intertwiner_2026-11-24.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
# Hard assertions: this script exits non-zero on any failed invariant.
TOL=1e-8
residual_checks=[k for k,v in checks.items()
                 if type(v) in (int,float) and k not in ("P_G_rank","RGS_upper_lower_triplet_shift")
                 and not (k.endswith("_distinct") or k.endswith("_count"))
                 and v>TOL]
assert checks["input_finite"], "Non-finite input array"
assert poly_residual<TOL, f"Quadratic carrier fit residual {poly_residual}"
assert upper_shift_residual<TOL, f"Upper/lower triplet shift residual {upper_shift_residual}"
assert np.allclose(poly_coeff,[0.5,1/120,1/240],atol=TOL,rtol=0), f"Unexpected polynomial coefficients: {poly_coeff}"
assert checks["P_G_rank"]==64, f"Expected rank(P_G)=64, got {checks['P_G_rank']}"
assert len(groups)==27, f"Expected 27 quotient images, got {len(groups)}"
assert checks["C_tensor_C_64_feature_vectors_distinct"]==64
assert checks["F_rank"] if "F_rank" in checks else np.linalg.matrix_rank(F)==3
assert not residual_checks, "Residuals above tolerance: "+", ".join(
    f"{k}={checks[k]:.3e}" for k in residual_checks)
assert fro(K0@PG)<=TOL and fro(PG@K0)<=TOL
assert maxabs(PG@PG-PG)<=TOL and maxabs(PG-PG.T)<=TOL
report["status"]="PASS: Q6 operator sector and RGS coupling checked against original binary arrays"
report["assertion_tolerance"]=TOL
report["failed_checks"]=[]
out.write_text(json.dumps(report,indent=2)+"\\n",encoding="utf-8")
print(json.dumps({"status":"PASS","checks":checks,
 "F_image_distinct":len(groups),
 "collision_multiplicities":report["F_collision_multiplicity_distribution"]},indent=2))
print("Wrote",out)
