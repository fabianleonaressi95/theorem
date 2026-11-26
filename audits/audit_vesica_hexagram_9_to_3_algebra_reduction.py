#!/usr/bin/env python3
"""Audit the canonical pointwise-algebra reduction R^9 -> R^3."""
import json
from pathlib import Path
from collections import defaultdict
import numpy as np

D=np.diag([1.,1.,-1.])
S=np.array([[0.,0.,1.],[0.,1.,0.],[1.,0.,0.]])
Q=np.array([[0.,1/np.sqrt(2),1/np.sqrt(2)],
            [1.,0.,0.],
            [0.,1/np.sqrt(2),-1/np.sqrt(2)]])
assert np.max(np.abs(Q.T@S@Q-D)) < 1e-14

# Pointwise multiplication on labelled channels (-,0,+), transported to parity basis.
M=np.zeros((3,9))
for a in range(3):
    for b in range(3):
        for c in range(3):
            M[a,3*b+c]=sum(Q[l,a]*Q[l,b]*Q[l,c] for l in range(3))

C=np.array([
    np.ones(8)/np.sqrt(8),
    np.array([7,1,-3,-5,-5,-3,1,7])/np.sqrt(168),
    np.array([-7,-5,-3,-1,1,3,5,7])/np.sqrt(168)
])
P8=np.fliplr(np.eye(8))
K=np.kron(C,C)
T=M@K
D9=np.kron(D,D)
P64=np.kron(P8,P8)
err=lambda A: float(np.max(np.abs(A)))
checks={
 "channel_basis_orthogonality":err(Q.T@Q-np.eye(3)),
 "reflection_basis_is_D":err(Q.T@S@Q-D),
 "M_coisometry":err(M@M.T-np.eye(3)),
 "M_diagonal_reflection_equivariance":err(M@D9-D@M),
 "M_lower_factor_same_D_equivariance":err(M@np.kron(D,np.eye(3))-D@M),
 "M_upper_factor_same_D_equivariance":err(M@np.kron(np.eye(3),D)-D@M),
 "C_reflection_equivariance":err(C@P8-D@C),
 "T_diagonal_reflection_equivariance":err(T@P64-D@T)
}
assert checks["M_coisometry"]<1e-14
assert checks["M_diagonal_reflection_equivariance"]<1e-14
assert checks["T_diagonal_reflection_equivariance"]<1e-14
assert checks["M_lower_factor_same_D_equivariance"]>1
assert checks["M_upper_factor_same_D_equivariance"]>1

classes=defaultdict(list)
states=[]
for i in range(8):
    for j in range(8):
        v=T[:,i*8+j]
        key=tuple(round(float(x),14) for x in v)
        classes[key].append(i*8+j)
        states.append({"index":i*8+j,"lower_bits":format(i,"03b"),
          "upper_bits":format(j,"03b"),
          "three_channel_feature":[round(float(x),15) for x in v]})
multiplicities=defaultdict(int)
for group in classes.values():
    multiplicities[len(group)]+=1
result={
 "status":"exact algebraic reduction; numerical implementation audited",
 "construction":"pointwise multiplication in the three labelled channels, transported to the reflection-adapted basis",
 "basis_order":["f0=e0","f+=(e-+e+)/sqrt(2)","f-=(e--e+)/sqrt(2)"],
 "M_rows":M.tolist(),"M_rank":int(np.linalg.matrix_rank(M)),
 "M_kernel_dimension":6,"M_singular_values":np.linalg.svd(M,compute_uv=False).tolist(),
 "equivariance":{"physical_diagonal_reflection":"M(D tensor D)=D M",
   "independent_factor_flips_with_same_target_D":"fail; residuals in checks"},
 "64_to_3":{"rank":int(np.linalg.matrix_rank(T)),"kernel_dimension":61,
   "number_of_distinct_basis_state_features":len(classes),
   "multiplicity_distribution_number_of_classes_by_multiplicity":{str(k):v for k,v in sorted(multiplicities.items())},
   "states":states,"collision_classes":[v for v in classes.values() if len(v)>1]},
 "equivariant_linear_map_dimension_for_diagonal_Z2":14,
 "checks":checks,
 "RGS_comparison":{
  "shared_structure":"target reflection D matches the RGS half-scale channel involution; stored RGS BA blocks are +D/2 and -D/2",
  "not_established":"M does not derive the factor 1/2, does not act on the full 188D arrays, and does not intertwine K0, ZA, ZS",
  "interpretation":"The product algebra selects a natural 9-to-3 map, but it is a lossy quotient and is not selected uniquely by reflection symmetry or by the currently reconstructed RGS operators."
 }
}
out=Path("results/json/vesica_hexagram_9_to_3_algebra_reduction_2026-11-24.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"checks":checks,"rank_M":result["M_rank"],"rank_T":result["64_to_3"]["rank"],
 "distinct_64_state_images":len(classes),"multiplicities":result["64_to_3"]["multiplicity_distribution_number_of_classes_by_multiplicity"]},indent=2))
print("Wrote",out)
