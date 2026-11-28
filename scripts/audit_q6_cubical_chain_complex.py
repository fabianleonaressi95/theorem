"""Generate the oriented cubical chain complex of the six-bit hexagram cube Q6."""
from itertools import combinations
import json
import numpy as np

N=6

def cells(k):
    out=[]
    for axes in combinations(range(N),k):
        free=set(axes)
        fixed=[i for i in range(N) if i not in free]
        for bits in range(1 << len(fixed)):
            base=0
            for j,axis in enumerate(fixed):
                if (bits >> j) & 1:
                    base |= 1 << axis
            out.append((base,tuple(axes)))
    return out

def index_map(k):
    return {cell:i for i,cell in enumerate(cells(k))}

def boundary(k):
    """Matrix of partial_k: C_k -> C_(k-1), with oriented axes ascending."""
    ck=cells(k); lower=index_map(k-1)
    B=np.zeros((len(lower),len(ck)),dtype=np.int8)
    for col,(base,axes) in enumerate(ck):
        for j,axis in enumerate(axes):
            face_axes=tuple(a for a in axes if a != axis)
            low=(base,face_axes)
            high=(base | (1 << axis),face_axes)
            sign=1 if j%2==0 else -1
            B[lower[high],col] += sign
            B[lower[low],col] -= sign
    return B

def build_report():
    counts=[len(cells(k)) for k in range(N+1)]
    boundaries={k:boundary(k) for k in range(1,4)}
    residual12=int(np.max(np.abs(boundaries[1]@boundaries[2])))
    residual23=int(np.max(np.abs(boundaries[2]@boundaries[3])))
    euler=sum(((-1)**k)*counts[k] for k in range(N+1))
    ranks=[int(np.linalg.matrix_rank(boundaries[k])) for k in range(1,4)]
    return {"status":"EXACT_Q6_CUBICAL_CHAIN_COMPLEX",
      "cell_counts_by_dimension":counts,
      "expected_counts":[64,192,240,160,60,12,1],
      "boundary_matrix_shapes":{str(k):list(boundaries[k].shape) for k in boundaries},
      "boundary_squared_max_abs":{"d1_d2":residual12,"d2_d3":residual23},
      "boundary_ranks_k1_to_k3":ranks,
      "euler_characteristic":euler,
      "interpretation":"Q6 graph cycle rank 129 belongs to the 1-skeleton; the full cubical 6-cube is contractible with Euler characteristic 1."}

if __name__=="__main__":
    report=build_report()
    print(json.dumps(report,indent=2))
    if report["cell_counts_by_dimension"] != report["expected_counts"]:
        raise SystemExit("cubical cell count mismatch")
    if report["boundary_squared_max_abs"]["d1_d2"] or report["boundary_squared_max_abs"]["d2_d3"]:
        raise SystemExit("boundary composition is not zero")
    if report["euler_characteristic"] != 1:
        raise SystemExit("Euler characteristic mismatch")
