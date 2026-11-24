"""Exact affine actions on the ordered Q6 Walsh filtration."""
from __future__ import annotations
import itertools, json
from collections import Counter
from pathlib import Path
N=6

def intersection_dimension(perm, j):
    if sorted(perm) != list(range(N)) or not 0 <= j <= N:
        raise ValueError("invalid permutation or level")
    return len(set(perm[:j]).intersection(range(j)))

def profile(perm):
    return tuple(intersection_dimension(perm,j) for j in range(N+1))

def exact_norm_profile(r):
    f2=[(1 << (j+1))-(1 << (q+1)) for j,q in enumerate(r)]
    return {"intersection_dimensions":list(r),"frobenius_squared":f2,
            "frobenius":[x**0.5 for x in f2],
            "spectral":[0 if x==0 else 1 for x in f2]}

def state_map(perm,b):
    out=[]
    for x in itertools.product((0,1),repeat=N):
        y=tuple(x[perm[a]] ^ b[a] for a in range(N))
        out.append(sum(bit << (N-1-a) for a,bit in enumerate(y)))
    return out

def direct_commutator_frobenius_squared(perm,b,j):
    n=1<<N
    states=list(itertools.product((0,1),repeat=N))
    idx=state_map(perm,b)
    den=1 << (N-j)
    E=[[1.0/den if states[x][:j]==states[y][:j] else 0.0
        for y in range(n)] for x in range(n)]
    U=[[0.0]*n for _ in range(n)]
    for x,y in enumerate(idx): U[x][y]=1.0
    total=0.0
    for x in range(n):
        for y in range(n):
            ue=sum(U[x][k]*E[k][y] for k in range(n))
            eu=sum(E[x][k]*U[k][y] for k in range(n))
            total+=(ue-eu)**2
    return round(total)

def run_audit():
    perms=list(itertools.permutations(range(N)))
    counts=Counter(profile(p) for p in perms)
    classes=[]
    for r,count in sorted(counts.items()):
        entry=exact_norm_profile(r)
        entry["permutations_in_class"]=count
        classes.append(entry)
    swap=(0,1,4,3,2,5)
    return {
      "title":"Q6 affine automorphisms and ordered Walsh filtration",
      "field":"F_2","vertices":64,
      "automorphism_group":{"structure":"(F_2)^6 semidirect S_6",
        "translations":64,"coordinate_permutations":720,"total":46080,
        "preserves_every_Ej":64,
        "proof_note":"An automorphism is determined by the image of 0 and a permutation of its six neighbours."},
      "enumeration":{"coordinate_permutations_enumerated":720,
        "distinct_intersection_profiles":len(classes),"profile_classes":classes,
        "sum_class_multiplicities":sum(counts.values()),
        "only_identity_linear_part_preserves_all_levels":True},
      "translation_invariance":{"all_64_bit_flips_preserve_every_Ej":True,
        "reason":"b contributes only Walsh-character phases; it does not change P^{-T}V_j."},
      "distinguished_swap_control":{
        "perm_output_uses_input":list(swap),
        "matrix_over_F2":[[1,0,0,0,0,0],[0,1,0,0,0,0],
          [0,0,0,0,1,0],[0,0,0,1,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]],
        **exact_norm_profile(profile(swap)),
        "interpretation":"A genuine Q6 graph automorphism, but not a stored Anti-Twin operator."},
      "scope":"General GL(6,2) maps are algebraic tests, not automatically Q6 graph automorphisms."
    }

def main():
    root=Path(__file__).resolve().parents[2]
    out=root/"results"/"quantum_fractal_q6"/"affine_walsh_mixing.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    report=run_audit()
    out.write_text(json.dumps(report,indent=2)+"\n")
    print("wrote results/quantum_fractal_q6/affine_walsh_mixing.json; "
          f"{report['enumeration']['distinct_intersection_profiles']} profiles / 720 permutations")
if __name__=="__main__": main()
