"""EQC gate realization of the induced RGS-compatible Q6 subgroup.

The canonical RGS seed ordering and Q6 labels are inherited from
audits.morphodynamics.q6_mqm_symmetry. No geometric relabelling is introduced.
"""
from itertools import product

from audits.morphodynamics.q6_mqm_symmetry import (
    edge_permutation,
    induced_rgs_permutations,
    preserves_q6_adjacency,
    q6_edges,
)

N = 6
IDENTITY = tuple(range(64))
COORDINATE_SWAP = (1, 0, 2, 4, 3, 5)

# The first three Q6 bits encode the three RGS sign choices in the seed order.
# The RGS signed-coordinate action maps x,y,z sign flips to Q6 bits 2,1,0.
RGS_Q6_GATE_SOURCE = {
    "flip_bit_0": "P q0 0 2 1",
    "flip_bit_1": "P q1 0 2 1",
    "flip_bit_2": "P q2 0 2 1",
    "swap_paired_coordinates": "SWAP q0 q1\nSWAP q3 q4",
}


def q6_coordinate_permutation(order):
    if len(order) != N or sorted(order) != list(range(N)):
        raise ValueError("order must permute six bit positions")
    return tuple(
        sum(((v >> order[i]) & 1) << i for i in range(N))
        for v in range(64)
    )


def q6_bit_flip(position):
    if not isinstance(position, int) or not 0 <= position < N:
        raise ValueError("bit position must be in [0,5]")
    return tuple(v ^ (1 << position) for v in range(64))


def compose_permutations(left, right):
    """Return left after right."""
    if len(left) != 64 or len(right) != 64:
        raise ValueError("Q6 permutations must have 64 entries")
    return tuple(left[right[v]] for v in range(64))


def generated_rgs_q6_group():
    """Closure of three independent flips and one paired coordinate swap."""
    generators = (
        q6_bit_flip(0),
        q6_bit_flip(1),
        q6_bit_flip(2),
        q6_coordinate_permutation(COORDINATE_SWAP),
    )
    seen = {IDENTITY}
    frontier = [IDENTITY]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = compose_permutations(generator, current)
            if candidate not in seen:
                seen.add(candidate)
                frontier.append(candidate)
    return frozenset(seen)


def induced_rgs_q6_group():
    """Extract the Q6-preserving actions from the 48 signed RGS permutations."""
    return frozenset(
        action for action in induced_rgs_permutations()
        if preserves_q6_adjacency(action)
    )


def rgs_q6_edge_stabilizer(reference_log_conductances):
    """Stabilizer inside the 16-element RGS-compatible subgroup."""
    if len(reference_log_conductances) != 192:
        raise ValueError("reference vector must have 192 edge values")
    stabilizer = []
    for vertex_map in generated_rgs_q6_group():
        edge_map = edge_permutation(vertex_map)
        if all(reference_log_conductances[e] ==
               reference_log_conductances[edge_map[e]]
               for e in range(192)):
            stabilizer.append(vertex_map)
    return frozenset(stabilizer)


def q6_vertex_to_qutrit_digits(vertex):
    """Q6 bit 0/1 becomes EQC stored digit 1/2; digit 0 is excluded."""
    if not isinstance(vertex, int) or not 0 <= vertex < 64:
        raise ValueError("Q6 vertex must be in [0,63]")
    return tuple(1 + ((vertex >> i) & 1) for i in range(N))


def qutrit_digits_to_q6_vertex(digits):
    """Inverse on the binary sector; reject any occurrence of digit 0."""
    if len(digits) != N or any(d not in (1, 2) for d in digits):
        raise ValueError("binary Q6 sector requires six digits in {1,2}")
    return sum((digits[i] - 1) << i for i in range(N))


def apply_q6_gate_generator(vertex, name):
    """Apply one named RGS-compatible generator to a Q6 vertex."""
    if name not in RGS_Q6_GATE_SOURCE:
        raise ValueError("unknown RGS-Q6 generator")
    if name == "flip_bit_0":
        return vertex ^ 1
    if name == "flip_bit_1":
        return vertex ^ 2
    if name == "flip_bit_2":
        return vertex ^ 4
    # Simultaneous qutrit-wire swaps q0<->q1 and q3<->q4.
    return q6_coordinate_permutation(COORDINATE_SWAP)[vertex]


def qutrit_gate_source():
    """Return the five existing EQC instructions implementing the generators."""
    return tuple(RGS_Q6_GATE_SOURCE[name] for name in (
        "flip_bit_0", "flip_bit_1", "flip_bit_2",
        "swap_paired_coordinates",
    ))
