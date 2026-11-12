#!/usr/bin/env python3
"""Exact symmetry-orbit audit for scalar laws on six ordered binary lines."""
from __future__ import annotations
import argparse, json
from pathlib import Path
N, MASK = 64, 63

def reverse_lines(h: int) -> int:
    if not 0 <= h < N: raise ValueError("label must lie in {0,...,63}")
    return sum(((h >> i) & 1) << (5-i) for i in range(6))

def complement_yin_yang(h: int) -> int:
    if not 0 <= h < N: raise ValueError("label must lie in {0,...,63}")
    return h ^ MASK

def orbit_partition(transformations):
    unseen, orbits = set(range(N)), []
    while unseen:
        seed = min(unseen)
        orbit, frontier = {seed}, [seed]
        while frontier:
            h = frontier.pop()
            for transform in transformations:
                hp = transform(h)
                if hp not in orbit:
                    orbit.add(hp); frontier.append(hp)
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    return tuple(orbits)

def line_reversal_orbits():
    return orbit_partition((reverse_lines,))

def reversal_and_complement_orbits():
    return orbit_partition((reverse_lines, complement_yin_yang))

def permutation_orbits():
    return tuple(tuple(h for h in range(N) if h.bit_count() == k)
                 for k in range(7))

def project_to_orbit_invariant(values, orbits):
    if len(values) != N: raise ValueError("exactly 64 values are required")
    out = [0.0] * N
    for orbit in orbits:
        mean = sum(float(values[h]) for h in orbit) / len(orbit)
        for h in orbit: out[h] = mean
    return out

def symmetry_audit():
    counts = {
        "no_extra_symmetry": 64,
        "line_reversal_only": len(line_reversal_orbits()),
        "arbitrary_line_permutations_S6": len(permutation_orbits()),
        "line_reversal_and_global_yin_yang_exchange": len(reversal_and_complement_orbits()),
        "full_Q6_automorphism_invariance": 1,
    }
    assert counts == {"no_extra_symmetry":64, "line_reversal_only":36,
        "arbitrary_line_permutations_S6":7,
        "line_reversal_and_global_yin_yang_exchange":20,
        "full_Q6_automorphism_invariance":1}
    return {"bit_convention":"bit 0 bottom; bit 5 top",
            "independent_scalar_values":counts,
            "interpretation":"alternative symmetry hypotheses; none selected as physical law",
            "status":"PASS"}

def analyze_measured_vector(values):
    """Compare orbit-invariance hypotheses without selecting one as truth."""
    if len(values) != N:
        raise ValueError("exactly 64 measured/derived values are required")
    hypotheses = {
        "unrestricted": (tuple((h,) for h in range(N))),
        "line_reversal": line_reversal_orbits(),
        "line_permutations_S6": permutation_orbits(),
        "reversal_and_global_complement": reversal_and_complement_orbits(),
        "full_cube_automorphisms": (tuple(range(N)),),
    }
    out = {}
    for name, orbits in hypotheses.items():
        fit = project_to_orbit_invariant(values, orbits)
        residual = [float(values[h]) - fit[h] for h in range(N)]
        out[name] = {
            "independent_values": len(orbits),
            "residual_l2": sum(x*x for x in residual) ** 0.5,
            "residual_max_abs": max(abs(x) for x in residual),
            "orbit_means": [sum(float(values[h]) for h in o) / len(o) for o in orbits],
        }
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--charges", type=Path,
                        help="JSON array of 64 measured or independently derived values")
    args = parser.parse_args()
    result = symmetry_audit()
    if args.charges:
        values = json.loads(args.charges.read_text(encoding="utf-8"))
        result["measured_vector_comparison"] = analyze_measured_vector(values)
        result["data_source"] = str(args.charges)
    print(json.dumps(result, indent=2))
