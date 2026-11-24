"""Operator-level bridge audit: Q6 pair-overlap transfer vs physical stress.

This module deliberately does NOT identify the overlap transfer with a
Green--Kubo relaxation generator.  It constructs the exact substochastic
pair transfer induced by the existing finite-type automaton and reports
the structural tests a reversible identification would have to pass.

The optional state_stress array is an externally derived Q6 state observable.
It is not inferred from the golden scalar coding.  Even with such an array,
the weighted pair statistic is a two-replica overlap statistic, not the
single-system time autocorrelation used by Green--Kubo.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Callable, Mapping

from audits.tsmr_c_iching_overlap_automaton import build_overlap_automaton

State = tuple[int, int, int, int]


@dataclass(frozen=True)
class TransferAudit:
    states: int
    directed_edges: int
    min_row_sum: int
    max_row_sum: int
    rows_with_killing: int
    total_missing_transitions: int
    reciprocal_directed_edges: int
    reciprocal_fraction: float
    uniform_reversible: bool


def build_pair_transfer():
    """Return canonical states, exact integer adjacency and T=A/36.

    Each independent Q6 walk chooses one of six neighbours, hence 36
    equiprobable paired choices.  Transitions excluded by the finite
    real/conjugate enclosure are killing/escape, not renormalized away.
    """
    states, outgoing, diameter = build_overlap_automaton()
    ordered = tuple(sorted(states))
    index = {state: i for i, state in enumerate(ordered)}
    rows: list[dict[int, int]] = []
    edge_set: set[tuple[int, int]] = set()
    for state in ordered:
        counts: dict[int, int] = defaultdict(int)
        for target in outgoing[state]:
            j = index[target]
            counts[j] += 1
            edge_set.add((index[state], j))
        rows.append(dict(counts))

    row_sums = [sum(row.values()) for row in rows]
    reciprocal = sum((j, i) in edge_set for i, j in edge_set)
    edge_count = len(edge_set)
    audit = TransferAudit(
        states=len(ordered),
        directed_edges=edge_count,
        min_row_sum=min(row_sums),
        max_row_sum=max(row_sums),
        rows_with_killing=sum(s < 36 for s in row_sums),
        total_missing_transitions=sum(36 - s for s in row_sums),
        reciprocal_directed_edges=reciprocal,
        reciprocal_fraction=(reciprocal / edge_count if edge_count else 1.0),
        uniform_reversible=(reciprocal == edge_count),
    )
    if audit.max_row_sum > 36:
        raise AssertionError("pair transfer is not substochastic")
    return ordered, rows, diameter, audit


def apply_transfer(rows, vector: Mapping[int, float]) -> dict[int, float]:
    """Apply T=A/36 to a sparse column vector."""
    result: dict[int, float] = defaultdict(float)
    for i, mass in vector.items():
        if mass == 0:
            continue
        for j, multiplicity in rows[i].items():
            result[j] += mass * multiplicity / 36.0
    return dict(result)


def pair_partition_sum(
    ordered_states,
    rows,
    depth: int,
    terminal_weight: Callable[[State], float],
) -> float:
    """Compute rho_0 T^depth terminal_weight for uniform initial (p,q,0).

    The initial distribution is uniform over 64*64 ordered pairs.  Because
    T is substochastic, the result is a killed-path contribution.  It is an
    exact-probability interpretation only to the extent that the existing
    enclosure-coverage lemma captures every path relevant to the terminal
    event.
    """
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    index = {state: i for i, state in enumerate(ordered_states)}
    vector = {
        index[(p, q, 0, 0)]: 1.0 / 4096.0
        for p in range(64)
        for q in range(64)
    }
    for _ in range(depth):
        vector = apply_transfer(rows, vector)
    return sum(
        mass * terminal_weight(ordered_states[i])
        for i, mass in vector.items()
    )


def stress_weighted_close_pair_statistic(
    ordered_states,
    rows,
    depth: int,
    close_pair: Callable[[State], bool],
    state_stress,
) -> float:
    """Two-replica stress-weighted overlap statistic.

    state_stress[p] must be derived independently from a specified physical
    energy/embedding.  The output is NOT a Green--Kubo autocorrelation:
    p and q are independent replicas, not the same trajectory at two times.
    """
    if len(state_stress) != 64:
        raise ValueError("state_stress must contain 64 state-resolved values")

    def terminal(state: State) -> float:
        p, q, _a, _b = state
        return state_stress[p] * state_stress[q] if close_pair(state) else 0.0

    return pair_partition_sum(ordered_states, rows, depth, terminal)


def main() -> None:
    ordered, rows, diameter, audit = build_pair_transfer()
    print("Q6 pair-overlap transfer audit")
    print(f"states={audit.states}")
    print(f"directed_edges={audit.directed_edges}")
    print(f"diameter_Zsqrt5={diameter}")
    print(f"row_sum_range=[{audit.min_row_sum},{audit.max_row_sum}]")
    print(f"rows_with_killing={audit.rows_with_killing}")
    print(f"total_missing_transitions={audit.total_missing_transitions}")
    print(f"reciprocal_directed_edges={audit.reciprocal_directed_edges}")
    print(f"reciprocal_fraction={audit.reciprocal_fraction:.12g}")
    print(f"uniform_reversible={audit.uniform_reversible}")
    print("operator=T=A/36; it is substochastic, not automatically a Markov")
    print("semigroup on a closed state space or a physical relaxation generator.")
    print("No stress spectral measure is produced by this audit.")


if __name__ == "__main__":
    main()
