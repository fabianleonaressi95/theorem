"""Exact qutrit lift of the 16-element RGS/Q6 symmetry subgroup."""
from itertools import product
DIM = 3 ** 6

def rgs_generators():
    """Three sign flips and the exchange of spatial coordinates y,z."""
    flip = (0, 2, 1)  # |1> <-> |2>, |0> fixed
    return (("P", 3, flip), ("P", 4, flip), ("P", 5, flip), ("SWAP", 4, 5))

def _digits(i):
    return tuple((i // (3 ** (5-q))) % 3 for q in range(6))

def _index(ds):
    n = 0
    for d in ds: n = 3*n + d
    return n

def apply_gate(i, gate):
    if not 0 <= i < DIM: raise ValueError("basis index outside six-qutrit register")
    ds = list(_digits(i))
    if gate[0] == "P":
        _, q, p = gate
        if not 0 <= q < 6 or sorted(p) != [0,1,2]: raise ValueError("invalid local permutation")
        ds[q] = p[ds[q]]
    elif gate[0] == "SWAP":
        _, a, b = gate
        if not (0 <= a < 6 and 0 <= b < 6 and a != b): raise ValueError("invalid SWAP")
        ds[a], ds[b] = ds[b], ds[a]
    else: raise ValueError("unknown gate")
    return _index(ds)

def q6_subspace_indices():
    return tuple(_index(ds) for ds in product((1,2), repeat=6))

def lifted_group_on_q6():
    sub = q6_subspace_indices()
    lookup = {state:i for i,state in enumerate(sub)}
    result = set()
    for mask in range(8):
        for swap in (False, True):
            program = [("P", q, (0,2,1)) for axis,q in enumerate((3,4,5))
                       if mask & (1 << (2-axis))]
            if swap: program.append(("SWAP",4,5))
            image = []
            for state in sub:
                j = state
                for gate in program: j = apply_gate(j,gate)
                image.append(lookup[j])
            result.add(tuple(image))
    return result

def rgs_q6_group_on_labels():
    def swap_yz(v):
        return v ^ (3 if ((v >> 1) & 1) != (v & 1) else 0)
    return {tuple(((swap_yz(v) if swap else v) ^ mask) for v in range(64))
            for mask in range(8) for swap in (False,True)}
