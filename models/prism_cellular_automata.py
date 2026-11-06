"""Binary cellular automata on finite five-factor PRISM product graphs.

This is an independent RGS–PRISM implementation inspired by the publicly
documented evolutionary-CA experiments of xcontcom. It does not copy their
source code. The external 2D Moore-neighbourhood rule has 512 entries;
the degree-10 PRISM neighbourhood used here has 11 binary inputs (centre
plus ten oriented neighbours), hence 2**11 = 2048 truth-table entries.

Neighbour order is fixed as (-e_1,+e_1,...,-e_5,+e_5). This convention is
part of the model and is not automatically invariant under graph symmetries.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import prod
from typing import Iterable, Sequence

BASE_FACTORS = (64, 6, 6, 6, 5)
DIMENSION = 5
LOCAL_INPUTS = 1 + 2 * DIMENSION
RULE_BITS = 1 << LOCAL_INPUTS
RULE_MASK = (1 << RULE_BITS) - 1


def _check_factors(factors: Sequence[int]) -> tuple[int, ...]:
    values = tuple(factors)
    if len(values) != DIMENSION:
        raise ValueError("PRISM graph must have exactly five cycle factors")
    if any(isinstance(n, bool) or not isinstance(n, int) or n < 3 for n in values):
        raise ValueError("every cycle factor must be an integer >= 3")
    return values


@dataclass(frozen=True)
class PrismProductGraph:
    """Lazy Cartesian product of five cycles; no adjacency matrix is stored."""

    factors: tuple[int, ...] = BASE_FACTORS

    def __post_init__(self) -> None:
        object.__setattr__(self, "factors", _check_factors(self.factors))

    @property
    def vertex_count(self) -> int:
        return prod(self.factors)

    @property
    def degree(self) -> int:
        return 2 * DIMENSION

    def encode(self, vertex: Sequence[int]) -> int:
        if len(vertex) != DIMENSION:
            raise ValueError("vertex must have five coordinates")
        index = 0
        for x, n in zip(vertex, self.factors):
            if isinstance(x, bool) or not isinstance(x, int) or not 0 <= x < n:
                raise ValueError("vertex coordinate out of range")
            index = index * n + x
        return index

    def decode(self, index: int) -> tuple[int, ...]:
        if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < self.vertex_count:
            raise ValueError("vertex index out of range")
        coords = [0] * DIMENSION
        value = index
        for j in range(DIMENSION - 1, -1, -1):
            coords[j] = value % self.factors[j]
            value //= self.factors[j]
        return tuple(coords)

    def neighbours(self, vertex: Sequence[int]) -> tuple[tuple[int, ...], ...]:
        if len(vertex) != DIMENSION:
            raise ValueError("vertex must have five coordinates")
        point = tuple(vertex)
        self.encode(point)
        result = []
        for axis, n in enumerate(self.factors):
            for step in (-1, 1):
                q = list(point)
                q[axis] = (q[axis] + step) % n
                result.append(tuple(q))
        return tuple(result)

    def positive_edges(self) -> Iterable[tuple[int, int]]:
        """Yield every undirected edge once, oriented in +coordinate direction."""
        for vertex in product(*(range(n) for n in self.factors)):
            tail = self.encode(vertex)
            for axis, n in enumerate(self.factors):
                q = list(vertex)
                q[axis] = (q[axis] + 1) % n
                yield tail, self.encode(q)


def validate_rule(rule: int) -> int:
    if isinstance(rule, bool) or not isinstance(rule, int) or not 0 <= rule <= RULE_MASK:
        raise ValueError(f"rule must be an integer encoding exactly {RULE_BITS} truth-table bits")
    return rule


def local_input_index(centre: int, neighbour_values: Sequence[int]) -> int:
    """Pack centre then ten ordered neighbour bits, most-significant first."""
    if centre not in (0, 1) or isinstance(centre, bool):
        raise ValueError("centre state must be binary")
    if len(neighbour_values) != 2 * DIMENSION:
        raise ValueError("exactly ten neighbour states are required")
    index = int(centre)
    for value in neighbour_values:
        if isinstance(value, bool) or value not in (0, 1):
            raise ValueError("neighbour states must be integer bits")
        index = (index << 1) | value
    return index


def step(graph: PrismProductGraph, state: Sequence[int], rule: int) -> bytearray:
    """Apply one synchronous deterministic CA step."""
    rule = validate_rule(rule)
    if len(state) != graph.vertex_count:
        raise ValueError("state length must equal graph vertex count")
    if any(isinstance(v, bool) or v not in (0, 1) for v in state):
        raise ValueError("state must contain only integer bits 0 and 1")

    output = bytearray(graph.vertex_count)
    for index in range(graph.vertex_count):
        vertex = graph.decode(index)
        neighbours = graph.neighbours(vertex)
        local = local_input_index(state[index], [state[graph.encode(q)] for q in neighbours])
        output[index] = (rule >> local) & 1
    return output


def trajectory(graph: PrismProductGraph, initial: Sequence[int], rule: int, steps: int) -> list[bytearray]:
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    current = bytearray(initial)
    if len(current) != graph.vertex_count or any(v not in (0, 1) for v in current):
        raise ValueError("initial state must be a binary vector of graph vertex count")
    result = [current]
    for _ in range(steps):
        current = step(graph, current, rule)
        result.append(current)
    return result


def observables(graph: PrismProductGraph, state: Sequence[int], next_state: Sequence[int] | None = None) -> dict:
    """Return density, optional temporal activity, and graph Dirichlet energy."""
    if len(state) != graph.vertex_count or any(v not in (0, 1) for v in state):
        raise ValueError("state must be a binary vector of graph vertex count")
    density = sum(state) / graph.vertex_count
    energy = sum(state[u] != state[v] for u, v in graph.positive_edges())
    result = {"density": density, "graph_dirichlet_energy": int(energy)}
    if next_state is not None:
        if len(next_state) != graph.vertex_count or any(v not in (0, 1) for v in next_state):
            raise ValueError("next_state must be a binary vector of graph vertex count")
        result["temporal_activity"] = sum(a != b for a, b in zip(state, next_state)) / graph.vertex_count
    return result


def elementary_rules() -> dict[str, int]:
    """Canonical controls under the declared local-input bit ordering."""
    zero = 0
    one = RULE_MASK
    identity = sum(1 << i for i in range(RULE_BITS) if (i >> LOCAL_INPUTS) & 1)
    # The central bit is the most significant of 11 local bits.
    identity = sum(1 << i for i in range(RULE_BITS) if ((i >> (LOCAL_INPUTS - 1)) & 1))
    negation = RULE_MASK ^ identity
    return {"zero": zero, "one": one, "identity": identity, "negation": negation}
