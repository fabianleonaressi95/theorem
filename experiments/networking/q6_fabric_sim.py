#!/usr/bin/env python3
"""Q6 Modular Interconnection Fabric benchmark (standard library only).

This is a transparent graph/queueing abstraction, NOT a cycle-accurate switch
simulator. All flows are injected at time zero; each directed link serializes
one packet per cycle; store-and-forward; one cycle per hop. No finite buffers,
packet sizes, switch arbitration, credit flow control, adaptive escape VCs,
or physical link-rate differences are modelled.

Examples:
  python experiments/networking/q6_fabric_sim.py --flows 4096 --seed 20261116
  python experiments/networking/q6_fabric_sim.py --flows 4096 --csv results.csv
"""
import argparse
import csv
import random
import statistics
from collections import deque

MODULES = 64
LOCAL_N = 64
N = MODULES * LOCAL_N


def q6_path_edges(a, b, group):
    """Dimension-order path inside one Q6 module; returns directed link keys."""
    x = a
    edges = []
    for bit in range(6):
        if ((x ^ b) >> bit) & 1:
            y = x ^ (1 << bit)
            edges.append(("q6", group, x, y))
            x = y
    return edges


def global_adjacency(kind):
    adj = [set() for _ in range(MODULES)]
    if kind == "complete":
        for u in range(MODULES):
            for v in range(u + 1, MODULES):
                adj[u].add(v)
                adj[v].add(u)
    elif kind == "circulant8":
        # Eight distinct neighbours: +/-1, +/-2, +/-3, +/-4 mod 64.
        for u in range(MODULES):
            for d in (1, 2, 3, 4):
                v = (u + d) % MODULES
                adj[u].add(v)
                adj[v].add(u)
    else:
        raise ValueError(kind)
    return [sorted(row) for row in adj]


def bfs_global(adj, source, target):
    if source == target:
        return [source]
    parent = {source: None}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                if v == target:
                    queue.clear()
                    break
                queue.append(v)
    if target not in parent:
        raise RuntimeError("global topology is disconnected")
    path = []
    u = target
    while u is not None:
        path.append(u)
        u = parent[u]
    return list(reversed(path))


def q6_modular_path(src, dst, global_kind, valiant, rng):
    gs, ls = divmod(src, LOCAL_N)
    gd, ld = divmod(dst, LOCAL_N)
    adj = global_adjacency(global_kind)

    if gs == gd:
        return q6_path_edges(ls, ld, gs)

    if valiant:
        candidates = [g for g in range(MODULES) if g not in (gs, gd)]
        intermediate = rng.choice(candidates)
        group_sequence = [gs, intermediate, gd]
    else:
        group_sequence = [gs, gd]

    edges = []
    current_local = ls
    for leg in range(len(group_sequence) - 1):
        route = bfs_global(adj, group_sequence[leg], group_sequence[leg + 1])
        for u, v in zip(route, route[1:]):
            # Gateway slots are assigned deterministically by sorted-neighbour
            # index. This is a logical wiring convention, not an optimized
            # physical gateway placement.
            out_slot = adj[u].index(v)
            in_slot = adj[v].index(u)
            edges.extend(q6_path_edges(current_local, out_slot, u))
            edges.append(("global", u, v))
            current_local = in_slot
    edges.extend(q6_path_edges(current_local, ld, gd))
    return edges


def torus_path(src, dst):
    """Dimension-order path on a 16 x 16 x 16 3D torus."""
    a = [(src // 256) % 16, (src // 16) % 16, src % 16]
    b = [(dst // 256) % 16, (dst // 16) % 16, dst % 16]
    x = a[:]
    edges = []
    for dim in range(3):
        forward = (b[dim] - x[dim]) % 16
        backward = (x[dim] - b[dim]) % 16
        step = 1 if forward <= backward else -1
        hops = min(forward, backward)
        for _ in range(hops):
            old = x[:]
            x[dim] = (x[dim] + step) % 16
            u = old[0] * 256 + old[1] * 16 + old[2]
            v = x[0] * 256 + x[1] * 16 + x[2]
            edges.append(("torus", u, v))
    return edges


def fat_tree_path(src, dst, rng):
    """Abstract 64-pod, 1:1 folded-Clos path with 4096 endpoints.

    64 pods x 64 endpoints; each pod has 8 leaf and 8 aggregation switches,
    each leaf serves 8 endpoints; 8 spine switches. This is a declared
    reference model, not a vendor-specific Fat Tree implementation.
    """
    ps, es = divmod(src, 64)
    pd, ed = divmod(dst, 64)
    leaf_s, leaf_d = es // 8, ed // 8
    ls = ("leaf", ps, leaf_s)
    ld = ("leaf", pd, leaf_d)
    ag_s = ("agg", ps, rng.randrange(8))
    ag_d = ("agg", pd, rng.randrange(8))
    path = [("endpoint", src), ls, ag_s]
    if ps != pd:
        path.extend([("spine", rng.randrange(8)), ag_d])
    else:
        path[-1] = ag_d
    path.extend([ld, ("endpoint", dst)])
    return [("clos", path[i], path[i + 1]) for i in range(len(path) - 1)]


def route(topology, src, dst, rng):
    if topology == "Q6-K64-direct":
        return q6_modular_path(src, dst, "complete", False, rng)
    if topology == "Q6-C8-direct":
        return q6_modular_path(src, dst, "circulant8", False, rng)
    if topology == "Q6-C8-Valiant":
        return q6_modular_path(src, dst, "circulant8", True, rng)
    if topology == "Torus-16x16x16":
        return torus_path(src, dst)
    if topology == "FatTree-1to1":
        return fat_tree_path(src, dst, rng)
    raise ValueError(topology)


def make_flows(pattern, count, rng):
    count = min(count, N)
    flows = []
    if pattern == "uniform":
        for _ in range(count):
            s = rng.randrange(N)
            d = rng.randrange(N - 1)
            if d >= s:
                d += 1
            flows.append((s, d))
    elif pattern == "hotspot":
        hot = 0
        for i in range(count):
            s = rng.randrange(N)
            d = hot if i % 2 == 0 else rng.randrange(N)
            if d == s:
                d = (d + 1) % N
            flows.append((s, d))
    elif pattern == "all-to-all-permutation":
        destinations = list(range(N))
        rng.shuffle(destinations)
        # Rotate until the permutation has no self-destinations (a derangement).
        while any(i == destinations[i] for i in range(N)):
            destinations = destinations[1:] + destinations[:1]
        flows = [(i, destinations[i]) for i in range(count)]
    elif pattern == "nearest-neighbour":
        for s in range(count):
            x, y, z = (s // 256) % 16, (s // 16) % 16, s % 16
            d = x * 256 + y * 16 + ((z + 1) % 16)
            flows.append((s, d))
    elif pattern == "gather-broadcast-proxy":
        # Centralized gather/broadcast stress proxy, not MPI All-Reduce.
        half = count // 2
        flows.extend((i + 1, 0) for i in range(half))
        flows.extend((0, i + 1) for i in range(count - half))
    else:
        raise ValueError(pattern)
    return flows


def simulate(topology, pattern, count, seed):
    rng = random.Random(seed)
    flows = make_flows(pattern, count, rng)
    # Randomize injection arbitration order reproducibly; all packets arrive
    # at time zero. Directed links are full-duplex independent resources.
    rng.shuffle(flows)
    next_free = {}
    latencies = []
    hop_total = 0
    for src, dst in flows:
        edges = route(topology, src, dst, rng)
        time = 0
        for link in edges:
            time = max(time, next_free.get(link, 0)) + 1
            next_free[link] = time
        latencies.append(time)
        hop_total += len(edges)

    ordered = sorted(latencies)
    n = len(ordered)
    p95 = ordered[min(n - 1, int(0.95 * n))] if n else 0
    p99 = ordered[min(n - 1, int(0.99 * n))] if n else 0
    makespan = max(ordered, default=0)
    return {
        "topology": topology,
        "pattern": pattern,
        "flows": n,
        "mean_hops": round(hop_total / n, 4) if n else 0,
        "mean_latency_cycles": round(statistics.mean(ordered), 4) if n else 0,
        "p95_latency_cycles": p95,
        "p99_latency_cycles": p99,
        "max_latency_cycles": makespan,
        "throughput_flows_per_cycle": round(n / makespan, 6) if makespan else 0,
    }


def self_test():
    adj = global_adjacency("circulant8")
    assert all(len(row) == 8 for row in adj)
    assert all(len(q6_path_edges(0, x, 0)) == x.bit_count() for x in range(64))
    assert max(len(q6_path_edges(0, x, 0)) for x in range(64)) == 6
    assert len({(u, v) for u in range(64) for v in adj[u]}) == 512
    for target in range(64):
        assert len(bfs_global(adj, 0, target)) - 1 <= 8
    for src, dst in ((0, 4095), (63, 64), (1000, 1001), (4095, 0)):
        for kind in ("complete", "circulant8"):
            path = q6_modular_path(src, dst, kind, False, random.Random(1))
            assert len(path) <= 6 + 8 * 7 + 6
    return "PASS"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--flows", type=int, default=4096)
    parser.add_argument("--seed", type=int, default=20261116)
    parser.add_argument("--csv", default="q6_fabric_results.csv")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    print("self_test:", self_test())
    if args.self_test:
        return

    topologies = [
        "Q6-K64-direct", "Q6-C8-direct", "Q6-C8-Valiant",
        "Torus-16x16x16", "FatTree-1to1",
    ]
    patterns = [
        "uniform", "hotspot", "all-to-all-permutation",
        "nearest-neighbour", "gather-broadcast-proxy",
    ]
    rows = []
    for pi, pattern in enumerate(patterns):
        for ti, topology in enumerate(topologies):
            result = simulate(topology, pattern, args.flows,
                              args.seed + pi * 100 + ti)
            rows.append(result)
            print(result)

    with open(args.csv, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print("CSV:", args.csv)


if __name__ == "__main__":
    main()
