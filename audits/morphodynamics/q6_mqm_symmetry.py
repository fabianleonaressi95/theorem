"""Finite Q6/MQM symmetry audit using exact combinatorial labels.

No numerical linear algebra is required. The RGS seed uses the exact
float64 constants already hash-checked by src/rgs_seed_64_reconstruction.py.
"""
from itertools import permutations, product
from math import factorial

ORBIT = {
    "cube_inner": 0.47863916086470326,
    "small_1": 0.48042984818593559,
    "small_2": 0.48230704367200045,
    "cube_outer": 0.95183963342906408,
    "large_1": 1.5073116806169751,
    "large_2": 1.9039106736116611,
}


def q6_edges():
    return tuple((v, v ^ (1 << bit), bit)
                 for v in range(64) for bit in range(6)
                 if not (v & (1 << bit)))


def q6_vertex_permutation(mask=0, coordinate_order=tuple(range(6))):
    """Output bit i = input bit coordinate_order[i] XOR bit_i(mask)."""
    if not 0 <= mask < 64 or sorted(coordinate_order) != list(range(6)):
        raise ValueError("invalid Q6 translation or coordinate permutation")
    out = []
    for v in range(64):
        w = 0
        for i, old_bit in enumerate(coordinate_order):
            bit = ((v >> old_bit) & 1) ^ ((mask >> i) & 1)
            w |= bit << i
        out.append(w)
    return tuple(out)


def edge_permutation(vertex_permutation):
    """Map each canonical edge index to its image edge index."""
    if len(vertex_permutation) != 64 or sorted(vertex_permutation) != list(range(64)):
        raise ValueError("vertex map must be a permutation of 0..63")
    edges = q6_edges()
    lookup = {(u, v): i for i, (u, v, _) in enumerate(edges)}
    lookup.update({(v, u): i for i, (u, v, _) in enumerate(edges)})
    return tuple(lookup[(vertex_permutation[u], vertex_permutation[v])]
                 for u, v, _ in edges)


def preserves_q6_adjacency(vertex_permutation):
    edges = q6_edges()
    edge_set = {tuple(sorted((u, v))) for u, v, _ in edges}
    return all(tuple(sorted((vertex_permutation[u], vertex_permutation[v])))
               in edge_set for u, v, _ in edges)


def q6_automorphism_order():
    return (2 ** 6) * factorial(6)


def count_reference_stabilizer(reference_log_conductances):
    """Order of the Q6 automorphism subgroup fixing x_* edgewise."""
    if len(reference_log_conductances) != 192:
        raise ValueError("x_reference must have 192 edge values")
    count = 0
    for mask in range(64):
        for order in permutations(range(6)):
            p = q6_vertex_permutation(mask, order)
            ep = edge_permutation(p)
            if all(reference_log_conductances[e] ==
                   reference_log_conductances[ep[e]] for e in range(192)):
                count += 1
    return count


def directional_reference_weights(values_by_direction):
    """Expand six direction-specific log-conductances to 192 Q6 edges."""
    if len(values_by_direction) != 6:
        raise ValueError("six direction values are required")
    return tuple(values_by_direction[bit] for _, _, bit in q6_edges())


def rgs_seed_coordinates():
    reps = [
        (ORBIT["cube_inner"],) * 3,
        (ORBIT["large_1"], ORBIT["large_1"], ORBIT["small_1"]),
        (ORBIT["large_1"], ORBIT["small_1"], ORBIT["large_1"]),
        (ORBIT["small_1"], ORBIT["large_1"], ORBIT["large_1"]),
        (ORBIT["large_2"], ORBIT["small_2"], ORBIT["small_2"]),
        (ORBIT["small_2"], ORBIT["large_2"], ORBIT["small_2"]),
        (ORBIT["small_2"], ORBIT["small_2"], ORBIT["large_2"]),
        (ORBIT["cube_outer"],) * 3,
    ]
    return tuple((sx*x, sy*y, sz*z)
                 for x, y, z in reps
                 for sx, sy, sz in product((-1.0, 1.0), repeat=3))


def signed_permutation_matrices():
    matrices = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row in range(3):
                entries = [0, 0, 0]
                entries[perm[row]] = signs[row]
                rows.append(tuple(entries))
            matrices.append(tuple(rows))
    return tuple(sorted(matrices))


def apply_matrix(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3))
                 for i in range(3))


def induced_rgs_permutations():
    coords = rgs_seed_coordinates()
    lookup = {point: i for i, point in enumerate(coords)}
    if len(lookup) != 64:
        raise AssertionError("RGS seed coordinates are not distinct")
    return tuple(
        tuple(lookup[apply_matrix(matrix, point)] for point in coords)
        for matrix in signed_permutation_matrices()
    )


def rgs_q6_stabilizer_report():
    matrices = signed_permutation_matrices()
    actions = induced_rgs_permutations()
    preserved = [
        (matrix, action)
        for matrix, action in zip(matrices, actions)
        if preserves_q6_adjacency(action)
    ]
    block_form = all(
        matrix[0][1] == matrix[0][2] == matrix[1][0] == matrix[2][0] == 0
        for matrix, _ in preserved
    )
    return {
        "induced_Oh_order": len(matrices),
        "Q6_adjacency_preserving_order": len(preserved),
        "not_Q6_adjacency_preserving": len(matrices) - len(preserved),
        "survivors_fix_first_coordinate_axis": block_form,
        "survivor_group_order_formula": 2 * (2**2 * factorial(2)),
    }
