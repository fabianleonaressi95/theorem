#!/usr/bin/env python3
"""Audit reflection-equivariant 8-to-3 trigram moments and the 64-state tensor map."""
import json, math
from pathlib import Path

C = [
    [1/math.sqrt(8)]*8,
    [x/math.sqrt(462) for x in (7,1,-3,-5,-5,-3,1,7)],
    [x/math.sqrt(168) for x in (-7,-5,-3,-1,1,3,5,7)],
]
D = [[1,0,0],[0,1,0],[0,0,-1]]
P = [[1 if j == 7-i else 0 for j in range(8)] for i in range(8)]
I8 = [[int(i == j) for j in range(8)] for i in range(8)]
I3 = [[int(i == j) for j in range(3)] for i in range(3)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):
    return [list(x) for x in zip(*A)]
def err(A,B):
    return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

assert err(mm(C,tr(C)),I3) < 1e-14
assert err(mm(C,P),mm(D,C)) < 1e-14
K = [[C[a][i]*C[b][j] for i in range(8) for j in range(8)] for a in range(3) for b in range(3)]
assert err(mm(K,tr(K)),[[int(i==j) for j in range(9)] for i in range(9)]) < 1e-14

# Permutations on the 64 basis states and target 9 modes.
PL = [[P[i//8][j//8] if i%8 == j%8 else 0 for j in range(64)] for i in range(64)]
PU = [[P[i%8][j%8] if i//8 == j//8 else 0 for j in range(64)] for i in range(64)]
DL = [[D[i//3][j//3] if i%3 == j%3 else 0 for j in range(9)] for i in range(9)]
DU = [[D[i%3][j%3] if i//3 == j//3 else 0 for j in range(9)] for i in range(9)]
assert err(mm(K,PL),mm(DL,K)) < 1e-14
assert err(mm(K,PU),mm(DU,K)) < 1e-14

states=[]
cols=[]
for i in range(8):
    for j in range(8):
        v=[K[r][i*8+j] for r in range(9)]
        cols.append(tuple(round(x,14) for x in v))
        states.append({"index":i*8+j,"lower_bits":format(i,"03b"),"upper_bits":format(j,"03b"),
                       "nine_channel_feature":[round(x,15) for x in v]})
assert len(set(cols)) == 64
result={
 "status":"exact finite-dimensional construction; canonical relative to the declared polynomial-moment prescription",
 "sample_reflection":"k -> 7-k",
 "C_rows_order":["even_constant","even_quadratic_moment","odd_linear_moment"],
 "C_exact":{
  "row_1":[1,1,1,1,1,1,1,1],"row_1_denominator":"sqrt(8)",
  "row_2":[7,1,-3,-5,-5,-3,1,7],"row_2_denominator":"sqrt(462)",
  "row_3":[-7,-5,-3,-1,1,3,5,7],"row_3_denominator":"sqrt(168)"},
 "D":[[1,0,0],[0,1,0],[0,0,-1]],
 "dimensions":{"C":[3,8],"rank_C":3,"C_tensor_C":[9,64],"rank_tensor":9,"kernel_dimension":55},
 "checks":{"C_orthonormal_rows":err(mm(C,tr(C)),I3),
           "CP_equals_DC":err(mm(C,P),mm(D,C)),
           "tensor_orthonormal_rows":err(mm(K,tr(K)),[[int(i==j) for j in range(9)] for i in range(9)]),
           "lower_reflection_equivariance":err(mm(K,PL),mm(DL,K)),
           "upper_reflection_equivariance":err(mm(K,PU),mm(DU,K)),
           "distinct_64_feature_vectors_at_1e-14":len(set(cols))},
 "hexagrams":states,
 "caveat":"All 64 labels have distinct nine-component feature vectors, but the linear map R^64 -> R^9 has rank 9 and is not injective on arbitrary fields."
}
out=Path("results/json/vesica_hexagram_moment_compression_2026-11-24.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result["checks"],indent=2))
print("Wrote",out)
