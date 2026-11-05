"""Radial x icosphere graph prototype for the Ellis warped-product metric.

This is a positive-conductance finite-volume calibration, not a Mosco theorem.
Requires numpy and scipy.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass

import numpy as np
from scipy.spatial import ConvexHull, SphericalVoronoi


@dataclass
class EllisGraph:
    r0: float = 0.8292
    radial_cells: int = 24
    sphere_subdivisions: int = 1
    extent: float = 3.0

    def build(self) -> dict:
        if self.r0 <= 0 or self.radial_cells < 2 or self.sphere_subdivisions < 0:
            raise ValueError("Require r0>0, radial_cells>=2, subdivisions>=0")
        lo, hi = -self.extent * self.r0, self.extent * self.r0
        edges_u = np.linspace(lo, hi, self.radial_cells + 1)
        u = 0.5 * (edges_u[:-1] + edges_u[1:])
        du = np.diff(edges_u)
        dual_u = np.empty(self.radial_cells)
        dual_u[0] = (u[0] - lo) + 0.5 * (u[1] - u[0])
        dual_u[-1] = (hi - u[-1]) + 0.5 * (u[-1] - u[-2])
        if self.radial_cells > 2:
            dual_u[1:-1] = 0.5 * (u[2:] - u[:-2])

        vertices, faces = _icosphere(self.sphere_subdivisions)
        sv = SphericalVoronoi(vertices)
        sv.sort_vertices_of_regions()
        cell_area = sv.calculate_areas()
        face_centres = _spherical_face_centres(vertices, faces)
        edge_faces = {}
        for fi, face in enumerate(faces):
            for a, b in ((face[0], face[1]), (face[1], face[2]), (face[2], face[0])):
                key = (min(int(a), int(b)), max(int(a), int(b)))
                edge_faces.setdefault(key, []).append(fi)
        angular_edges = []
        for (a, b), adj in edge_faces.items():
            if len(adj) != 2:
                raise RuntimeError("Icosphere triangulation is not closed")
            primal = _angle(vertices[a], vertices[b])
            dual = _angle(face_centres[adj[0]], face_centres[adj[1]])
            w = dual / primal
            if not np.isfinite(w) or w <= 0:
                raise RuntimeError("Non-positive spherical finite-volume weight")
            angular_edges.append((a, b, w))

        nv = len(vertices)
        nr = len(u)
        masses = np.empty((nr, nv))
        for i in range(nr):
            masses[i] = dual_u[i] * (u[i] ** 2 + self.r0 ** 2) * cell_area

        # Edges are (flattened vertex a, flattened vertex b, conductance).
        # Flattening: node(i,j) = i*nv+j.
        graph_edges = []
        for i in range(nr - 1):
            um = 0.5 * (u[i] + u[i + 1])
            radial_area = (um * um + self.r0 ** 2) * cell_area
            for j in range(nv):
                graph_edges.append((i * nv + j, (i + 1) * nv + j,
                                    radial_area[j] / (u[i + 1] - u[i])))
        for i in range(nr):
            for a, b, w in angular_edges:
                graph_edges.append((i * nv + a, i * nv + b, dual_u[i] * w))

        return {
            "u": u, "radial_dual_width": dual_u, "sphere_vertices": vertices,
            "sphere_faces": faces, "sphere_cell_area": cell_area,
            "masses": masses.reshape(-1), "edges": np.asarray(graph_edges, dtype=float),
            "volume": float(masses.sum()), "continuum_volume": 96 * math.pi * self.r0**3,
            "nodes": nr * nv, "radial_edges": (nr - 1) * nv,
            "angular_edges_per_layer": len(angular_edges),
        }


def _angle(a: np.ndarray, b: np.ndarray) -> float:
    return float(math.acos(np.clip(np.dot(a, b), -1.0, 1.0)))


def _icosphere(level: int) -> tuple[np.ndarray, np.ndarray]:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    points = np.array([
        (-1, phi, 0), (1, phi, 0), (-1, -phi, 0), (1, -phi, 0),
        (0, -1, phi), (0, 1, phi), (0, -1, -phi), (0, 1, -phi),
        (phi, 0, -1), (phi, 0, 1), (-phi, 0, -1), (-phi, 0, 1)
    ], dtype=float)
    points /= np.linalg.norm(points, axis=1)[:, None]
    for _ in range(level):
        cache = {}
        out = points.tolist()
        def midpoint(i: int, j: int) -> int:
            key = (min(i, j), max(i, j))
            if key not in cache:
                p = points[i] + points[j]
                p /= np.linalg.norm(p)
                cache[key] = len(out)
                out.append(p.tolist())
            return cache[key]
        hull = ConvexHull(points)
        new_faces = []
        for tri in hull.simplices:
            a, b, c = map(int, tri)
            ab, bc, ca = midpoint(a, b), midpoint(b, c), midpoint(c, a)
            new_faces.extend(((a, ab, ca), (b, bc, ab), (c, ca, bc), (ab, bc, ca)))
        points = np.asarray(out, dtype=float)
        # ConvexHull is recomputed next iteration; final faces returned below.
    faces = ConvexHull(points).simplices
    # Orient faces outward.
    for k, tri in enumerate(faces):
        a, b, c = points[tri]
        if np.dot(np.cross(b - a, c - a), a + b + c) < 0:
            faces[k] = tri[[0, 2, 1]]
    return points, faces


def _spherical_face_centres(vertices: np.ndarray, faces: np.ndarray) -> np.ndarray:
    centres = []
    for tri in faces:
        a, b, c = vertices[tri]
        normal = np.cross(b - a, c - a)
        normal /= np.linalg.norm(normal)
        if np.dot(normal, a + b + c) < 0:
            normal = -normal
        centres.append(normal)
    return np.asarray(centres)


def audit(radial_cells: int, subdivisions: int, r0: float = 0.8292) -> dict:
    g = EllisGraph(r0=r0, radial_cells=radial_cells,
                   sphere_subdivisions=subdivisions).build()
    edge = g["edges"]
    return {
        "model": "ellis_radial_icosphere_positive_conductance_graph",
        "status": "geometric_discretization_prototype_not_Mosco_proof",
        "parameters": {"r0": r0, "radial_cells": radial_cells,
                       "sphere_subdivisions": subdivisions},
        "nodes": g["nodes"],
        "edges": len(edge),
        "minimum_mass": float(g["masses"].min()),
        "minimum_conductance": float(edge[:, 2].min()),
        "maximum_conductance": float(edge[:, 2].max()),
        "discrete_volume": g["volume"],
        "continuum_volume": g["continuum_volume"],
        "relative_volume_error": abs(g["volume"] - g["continuum_volume"]) / g["continuum_volume"],
        "radial_edges": g["radial_edges"],
        "angular_edges_per_layer": g["angular_edges_per_layer"],
        "boundary_condition": "natural graph Neumann (no exterior radial edges)",
        "limitations": [
            "angular dual cells use spherical Voronoi areas",
            "angular conductances use circumcentric dual/primal edge ratios",
            "radial-angular coupling is a product finite-volume approximation",
            "no uniform discrete Rellich estimate or Mosco liminf/recovery proof is supplied"
        ]
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--radial-cells", type=int, default=24)
    parser.add_argument("--sphere-subdivisions", type=int, default=1)
    parser.add_argument("--r0", type=float, default=0.8292)
    args = parser.parse_args()
    print(json.dumps(audit(args.radial_cells, args.sphere_subdivisions, args.r0), indent=2))


if __name__ == "__main__":
    main()
