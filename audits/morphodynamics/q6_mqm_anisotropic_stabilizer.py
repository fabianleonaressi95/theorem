"""Exact stabilizer of the EQC-RGS gate subgroup for MQM-1 references."""
from audits.morphodynamics.q6_mqm_symmetry import edge_permutation, directional_reference_weights
from models.eqc_rgs_gates import apply_gate, q6_subspace_indices, rgs_generators


def rgs_gate_vertex_permutations():
    states = q6_subspace_indices()
    lookup = {state: v for v, state in enumerate(states)}
    generators = [tuple(lookup[apply_gate(state, gate)] for state in states)
                  for gate in rgs_generators()]
    identity = tuple(range(64))
    group, frontier = {identity}, [identity]
    while frontier:
        current = frontier.pop()
        for gen in generators:
            composed = tuple(gen[current[v]] for v in range(64))
            if composed not in group:
                group.add(composed)
                frontier.append(composed)
    return tuple(sorted(group))


def mqm_reference_stabilizer(reference):
    if len(reference) != 192:
        raise ValueError("MQM-1 reference must contain 192 edge values")
    survivors = []
    for vertex_map in rgs_gate_vertex_permutations():
        edge_map = edge_permutation(vertex_map)
        if all(reference[e] == reference[edge_map[e]] for e in range(192)):
            survivors.append(vertex_map)
    return tuple(survivors)


def directional_anisotropy(values_by_direction):
    return directional_reference_weights(values_by_direction)


def anisotropic_gate_report(values_by_direction):
    reference = directional_anisotropy(values_by_direction)
    survivors = set(mqm_reference_stabilizer(reference))
    states = q6_subspace_indices()
    lookup = {state: v for v, state in enumerate(states)}
    gate_results = {}
    for gate in rgs_generators():
        action = tuple(lookup[apply_gate(state, gate)] for state in states)
        gate_results[str(gate)] = action in survivors
    return {
        "stabilizer_order": len(survivors),
        "surviving_generators": gate_results,
        "survives_pair_swap": gate_results[str(rgs_generators()[-1])],
    }


def arbitrary_reference_stabilizer_order(reference):
    return len(mqm_reference_stabilizer(reference))
