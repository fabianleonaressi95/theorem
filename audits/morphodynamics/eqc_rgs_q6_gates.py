"""Minimal native EQC gates for the RGS-induced Q6 subgroup.

Q6 bit i is stored in EQC register qi, matching the established repository
mapping in the original RGS-Q6 gate audit.
"""
from audits.morphodynamics.q6_mqm_symmetry import (
    edge_permutation, induced_rgs_permutations, preserves_q6_adjacency,
    q6_edges,
)

N = 6
IDENTITY = tuple(range(64))
COORDINATE_SWAP = (1, 0, 2, 4, 3, 5)

# Three generators: independent x-axis flip, y-axis flip, and y<->z exchange.
RGS_Q6_GATE_SOURCE = {
    "flip_bit_2": "P q2 0 2 1",
    "flip_bit_1": "P q1 0 2 1",
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
    """Closure of the three minimal generators; order is exactly 16."""
    generators = (
        q6_bit_flip(2),
        q6_bit_flip(1),
        q6_coordinate_permutation(COORDINATE_SWAP),
    )
    seen, frontier = {IDENTITY}, [IDENTITY]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = compose_permutations(generator, current)
            if candidate not in seen:
                seen.add(candidate)
                frontier.append(candidate)
    return frozenset(seen)


def induced_rgs_q6_group():
    """Extract Q6-preserving actions from the 48 signed RGS permutations."""
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
    """Q6 bit i becomes stored qutrit digit 1/2 in register qi."""
    if not isinstance(vertex, int) or not 0 <= vertex < 64:
        raise ValueError("Q6 vertex must be in [0,63]")
    return tuple(1 + ((vertex >> i) & 1) for i in range(N))


def qutrit_digits_to_q6_vertex(digits):
    """Inverse on the binary sector; reject excluded digit 0."""
    if len(digits) != N or any(d not in (1, 2) for d in digits):
        raise ValueError("binary Q6 sector requires six digits in {1,2}")
    return sum((digits[i] - 1) << i for i in range(N))


def apply_q6_gate_generator(vertex, name):
    """Apply one of the three named generators to a Q6 vertex."""
    if not isinstance(vertex, int) or not 0 <= vertex < 64:
        raise ValueError("Q6 vertex must be in [0,63]")
    if name == "flip_bit_2":
        return vertex ^ 4
    if name == "flip_bit_1":
        return vertex ^ 2
    if name == "swap_paired_coordinates":
        return q6_coordinate_permutation(COORDINATE_SWAP)[vertex]
    raise ValueError("unknown RGS-Q6 generator")


def qutrit_gate_source():
    """Return the four EQC instructions implementing three generators."""
    return tuple(RGS_Q6_GATE_SOURCE.values())


def direction_reference_weights(values):
    """Expand six direction-specific reference values over all Q6 edges."""
    if len(values) != 6:
        raise ValueError("six direction values are required")
    return tuple(values[direction] for _, _, direction in q6_edges())


def direction_reference_stabilizer_order(values):
    return len(rgs_q6_edge_stabilizer(direction_reference_weights(values)))
