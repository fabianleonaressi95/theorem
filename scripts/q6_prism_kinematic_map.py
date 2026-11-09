#!/usr/bin/env python3
"""Exact Q6 -> periodic 2D material-cell kinematic quotient.

Q6 is represented as the 6-cube graph, grouped into three 2-bit Gray cycles:
Q6 ~= C4 x C4 x C4.  The third C4 is an internal fibre.  Collapsing it gives
the 4x4 periodic material cell C4 x C4.  Displacements are 0-cochains and
edge differences are their exact coboundary.

This is a finite kinematic model, not a continuum-limit theorem or a claim
that the 4x4 periodic cell is a physical specimen.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

N = 4
GRAY = (0, 1, 3, 2)  # binary pair -> position around C4


def bits_of_state(s: int) -> tuple[int, ...]:
    if not 0 <= s < 64:
        raise ValueError(s)
    return tuple((s >> (5-k)) & 1 for k in range(6))


def q6_coordinates() -> np.ndarray:
    """Rows are (x,y,z) in Z4^3, with each bit pair Gray-embedded."""
    out = np.zeros((64, 3), dtype=np.int64)
    for s in range(64):
        b = bits_of_state(s)
        for a in range(3):
            out[s, a] = GRAY[2*b[2*a] + b[2*a+1]]
    if len({tuple(x) for x in out.tolist()}) != 64:
        raise AssertionError("Gray coordinate map is not bijective")
    return out


def q6_edges():
    """Canonical undirected edges, oriented from smaller to larger state id."""
    edges = []
    for s in range(64):
        for k in range(6):
            t = s ^ (1 << (5-k))
            if s < t:
                edges.append((s, t, k))
    if len(edges) != 192:
        raise AssertionError(len(edges))
    return edges


def square_boundary(s: int, i: int, j: int, edge_index: dict) -> np.ndarray:
    """Oriented boundary s -> s_i -> s_ij -> s_j -> s."""
    si = s ^ (1 << (5-i))
    sj = s ^ (1 << (5-j))
    sij = si ^ (1 << (5-j))
    path = ((s, si), (si, sij), (sij, sj), (sj, s))
    row = np.zeros(192, dtype=np.int64)
    for a, b in path:
        idx = edge_index[(min(a,b), max(a,b))]
        row[idx] += 1 if a < b else -1
    return row


def base_complex():
    """C4 x C4 periodic cell: 16 vertices, 32 oriented edges, 16 faces."""
    d0 = np.zeros((32, 16), dtype=np.int64)
    d1 = np.zeros((16, 32), dtype=np.int64)
    edge_ids = {}
    def v(x,y): return (y % 4)*4 + (x % 4)
    def add_edge(idx, a, b):
        d0[idx,a] = -1; d0[idx,b] = 1
        edge_ids[(a,b)] = idx
    for y in range(4):
        for x in range(4):
            e = y*4+x
            add_edge(e, v(x,y), v(x+1,y))
            e = 16+y*4+x
            add_edge(e, v(x,y), v(x,y+1))
    for y in range(4):
        for x in range(4):
            f = y*4+x
            bottom = y*4+x
            right = 16+y*4+((x+1)%4)
            top = y*4+x
            left = 16+y*4+x
            d1[f,bottom] += 1
            d1[f,right] += 1
            d1[f,top] -= 1
            d1[f,left] -= 1
            # The top edge is the x-edge at y+1, and the bottom edge at y.
            d1[f,top] = -1
            d1[f,bottom] = 1
            # Correct the four oriented boundary entries explicitly.
            d1[f,:] = 0
            d1[f,y*4+x] = 1
            d1[f,16+y*4+((x+1)%4)] = 1
            d1[f,((y+1)%4)*4+x] = -1
            d1[f,16+y*4+x] = -1
    return d0, d1


def build_q6_complex():
    coords = q6_coordinates()
    edges = q6_edges()
    edge_index = {(a,b): k for k,(a,b,_) in enumerate(edges)}
    d0 = np.zeros((192,64), dtype=np.int64)
    for k,(a,b,_) in enumerate(edges):
        d0[k,a] = -1; d0[k,b] = 1

    full_faces = []
    product_faces = []
    for i in range(6):
        for j in range(i+1,6):
            for mask in range(64):
                if ((mask >> (5-i)) & 1) or ((mask >> (5-j)) & 1):
                    continue
                row = square_boundary(mask, i, j, edge_index)
                full_faces.append((i,j,mask,row))
                if i//2 != j//2:
                    product_faces.append((i,j,mask,row))
    if len(full_faces) != 240 or len(product_faces) != 192:
        raise AssertionError((len(full_faces),len(product_faces)))
    d1_full = np.stack([x[3] for x in full_faces])
    d1_product = np.stack([x[3] for x in product_faces])

    # Projection pi: Q6 vertices -> C4 x C4 vertices; z is the 4-state fibre.
    pi = np.array([coords[s,1]*4+coords[s,0] for s in range(64)], dtype=np.int64)
    d0_base, d1_base = base_complex()
    p0 = np.zeros((64,16), dtype=np.int64)
    p0[np.arange(64),pi] = 1

    # P1 maps each Q6 edge to its oriented quotient edge; fibre edges map to 0.
    p1 = np.zeros((192,32), dtype=np.int64)
    for k,(a,b,bit) in enumerate(edges):
        axis = bit//2
        if axis == 2:
            continue
        ca, cb = coords[a], coords[b]
        x,y = int(ca[0]), int(ca[1])
        if axis == 0:
            delta = (int(cb[0])-int(ca[0])) % 4
            edge_x = x if delta == 1 else (x-1) % 4
            target = y*4+edge_x
        else:
            delta = (int(cb[1])-int(ca[1])) % 4
            edge_y = y if delta == 1 else (y-1) % 4
            target = 16+edge_y*4+x
        if delta == 1:
            sign = 1
        elif delta == 3:
            sign = -1
        else:
            raise AssertionError(("non-neighbour Gray edge", a,b,axis,delta))
        p1[k,target] = sign

    # P2 maps the 192 product faces to the 16 quotient faces.
    # x-y faces survive; x-z and y-z faces collapse to zero.
    p2 = np.zeros((192,16), dtype=np.int64)
    for f,(i,j,mask,row) in enumerate(product_faces):
        ai, aj = i//2, j//2
        if {ai,aj} != {0,1}:
            continue
        mapped_boundary = row @ p1
        matches = []
        for target in range(16):
            if np.array_equal(mapped_boundary, d1_base[target]):
                matches.append((target, 1))
            elif np.array_equal(mapped_boundary, -d1_base[target]):
                matches.append((target, -1))
        if len(matches) != 1:
            raise AssertionError(("face projection is not a unique quotient 2-cell",i,j,mask,matches))
        target, sign = matches[0]
        p2[f,target] = sign
    return {
        "coords":coords, "edges":edges, "d0":d0, "d1_full":d1_full,
        "d1_product":d1_product, "product_faces":product_faces,
        "full_faces":full_faces, "pi":pi, "d0_base":d0_base,
        "d1_base":d1_base, "p0":p0, "p1":p1, "p2":p2
    }


def lift_displacement(u_base: np.ndarray, complex_data=None) -> np.ndarray:
    """Pull back a 16x2 periodic displacement to all 64 Q6 vertices."""
    c = complex_data or build_q6_complex()
    u = np.asarray(u_base, dtype=float)
    if u.shape != (16,2):
        raise ValueError(f"expected (16,2), got {u.shape}")
    return u[c["pi"]]


def cell_gradients(u_base: np.ndarray, complex_data=None) -> np.ndarray:
    """Centred cell gradient on the periodic 4x4 quotient (16 cells x 2 x 2)."""
    c = complex_data or build_q6_complex()
    u = np.asarray(u_base, dtype=float)
    if u.shape != (16,2):
        raise ValueError(f"expected (16,2), got {u.shape}")
    grad = np.zeros((16,2,2), dtype=float)
    for y in range(4):
        for x in range(4):
            f = y*4+x
            v00 = y*4+x
            v10 = y*4+((x+1)%4)
            v01 = ((y+1)%4)*4+x
            v11 = ((y+1)%4)*4+((x+1)%4)
            grad[f,:,0] = 0.5*((u[v10]-u[v00])+(u[v11]-u[v01]))
            grad[f,:,1] = 0.5*((u[v01]-u[v00])+(u[v11]-u[v10]))
    return grad


def cell_gradient_samples(u_base: np.ndarray, complex_data=None) -> np.ndarray:
    """Q1 bilinear gradients at the four 2x2 Gauss points of each unit cell."""
    c = complex_data or build_q6_complex()
    u = np.asarray(u_base, dtype=float)
    if u.shape != (16,2):
        raise ValueError(f"expected (16,2), got {u.shape}")
    a = 1.0/np.sqrt(3.0)
    samples = np.zeros((16,4,2,2), dtype=float)
    gauss = ((-a,-a), (a,-a), (-a,a), (a,a))
    for y in range(4):
        for x in range(4):
            f = y*4+x
            nodes = np.array((y*4+x, y*4+((x+1)%4),
                              ((y+1)%4)*4+x, ((y+1)%4)*4+((x+1)%4)))
            ue = u[nodes]
            for q,(xi,eta) in enumerate(gauss):
                dxi = 0.25*np.array((-(1-eta), (1-eta), -(1+eta), (1+eta)))
                deta = 0.25*np.array((-(1-xi), -(1+xi), (1-xi), (1+xi)))
                # Unit-square coordinates: d/dx = 2 d/dxi, d/dy = 2 d/deta.
                dN = 2.0*np.column_stack((dxi,deta))
                samples[f,q] = ue.T @ dN
    return samples


def elastic_energy(u_base: np.ndarray, lam: float=1.0, mu: float=1.0) -> float:
    """Periodic Q1 elastic energy integrated with full 2x2 Gauss quadrature."""
    if lam < 0 or mu <= 0:
        raise ValueError("require lam >= 0 and mu > 0")
    g = cell_gradient_samples(u_base)
    eps = 0.5*(g + np.swapaxes(g,2,3))
    tr = np.trace(eps, axis1=2, axis2=3)
    density = 0.5*lam*tr**2 + mu*np.sum(eps*eps, axis=(2,3))
    # Each reference Gauss weight is one and the unit-square Jacobian is 1/4.
    return float(0.25*np.sum(density))


def audit() -> dict:
    c = build_q6_complex()
    z = np.zeros((16,2), dtype=float)
    # Deterministic nontrivial test field; periodic by construction.
    for y in range(4):
        for x in range(4):
            z[y*4+x] = (np.sin(2*np.pi*x/4)+0.2*np.cos(2*np.pi*y/4),
                        np.cos(2*np.pi*y/4)-0.1*np.sin(2*np.pi*x/4))
    lifted = lift_displacement(z,c)
    edge_q6 = c["d0"] @ lifted
    edge_base = c["d0_base"] @ z
    chain0 = c["d0"] @ c["p0"] - c["p1"] @ c["d0_base"]
    chain1 = c["d1_product"] @ c["p1"] - c["p2"] @ c["d1_base"]
    pullback = edge_q6 - c["p1"] @ edge_base
    return {
        "status":"EXACT_FINITE_KINEMATIC_QUOTIENT",
        "q6":{"vertices":64,"edges":192,"full_hypercube_square_faces":240,
              "product_torus_square_faces":192,"same_pair_cap_faces":48,
              "graph_cycle_rank":129},
        "quotient":{"vertices":16,"edges":32,"faces":16,"fibre_cardinality":4,
                    "topology":"periodic C4 x C4 material cell"},
        "conventions":{"state_bits":"b0...b5, most-significant bit first",
                       "pair_codes":["2*b0+b1","2*b2+b3","2*b4+b5"],
                       "geometric_embedding":"Gray cycle 00->0, 01->1, 11->2, 10->3",
                       "spatial_pairs":"(b0,b1) and (b2,b3)",
                       "internal_fibre_pair":"(b4,b5)"},
        "exact_checks":{
            "D1_full_D0_max_abs":int(np.max(np.abs(c["d1_full"]@c["d0"]))),
            "D1_product_D0_max_abs":int(np.max(np.abs(c["d1_product"]@c["d0"]))),
            "quotient_D1_D0_max_abs":int(np.max(np.abs(c["d1_base"]@c["d0_base"]))),
            "vertex_chain_map_max_abs":int(np.max(np.abs(chain0))),
            "face_chain_map_max_abs":int(np.max(np.abs(chain1))),
            "displacement_pullback_max_abs":float(np.max(np.abs(pullback)))
        },
        "sample":{"lifted_displacement_shape":list(lifted.shape),
                  "edge_cochain_shape":list(edge_q6.shape),
                  "elastic_energy_lam1_mu1":elastic_energy(z),
                  "energy_quadrature":"periodic Q1 bilinear, full 2x2 Gauss",
                  "checkerboard_mode_energy":elastic_energy(np.array([[(-1.0)**x,0.0] for y in range(4) for x in range(4)]))}
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
