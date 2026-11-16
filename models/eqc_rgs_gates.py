"""Exact qutrit lift of the 16-element RGS/Q6 symmetry subgroup."""
from itertools import product
DIM = 3 ** 6

def rgs_generators():
    """Three coordinate sign flips and the coupled representative/sign y-z swap."""
    flip = (0, 2, 1)  # |1> <-> |2>, |0> fixed
    return (("P", 3, flip), ("P", 4, flip), ("P", 5, flip),
            ("PAIRSWAP", 1, 2, 4, 5))

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
    elif gate[0] == "PAIRSWAP":
        _, a, b, c, d = gate
        if len({a,b,c,d}) != 4 or any(not 0 <= q < 6 for q in (a,b,c,d)):
            raise ValueError("PAIRSWAP requires four distinct valid registers")
        ds[a], ds[b] = ds[b], ds[a]
        ds[c], ds[d] = ds[d], ds[c]
    else: raise ValueError("unknown RGS gate")
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
            if swap: program.append(("PAIRSWAP",1,2,4,5))
            image = []
            for state in sub:
                j = state
                for gate in program: j = apply_gate(j,gate)
                image.append(lookup[j])
            result.add(tuple(image))
    return result

def rgs_q6_group_on_labels():
    def swap_yz(v):
        # Big-endian labels: exchange representative bits b1,b2 and sign bits b4,b5.
        v ^= 24 if ((v >> 3) & 1) != ((v >> 4) & 1) else 0
        v ^= 3 if ((v >> 0) & 1) != ((v >> 1) & 1) else 0
        return v
    return {tuple(((swap_yz(v) if swap else v) ^ mask) for v in range(64))
            for mask in range(8) for swap in (False,True)}
