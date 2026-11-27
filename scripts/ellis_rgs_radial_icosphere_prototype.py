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
            dual = _signed_circumcentric_dual_length(
                vertices, a, b, face_centres, adj
            )
            w = dual / primal
            if not np.isfinite(w) or w <= 0:
                raise RuntimeError("Non-positive spherical finite-volume weight")
            angular_edges.append((a, b, w))

        nv = len(vertices)
        nr = len(u)
        masses = np.empty((nr, nv))
        for i in range(nr):
            left, right = edges_u[i], edges_u[i + 1]
            radial_mass = ((right ** 3 - left ** 3) / 3.0
                           + self.r0 ** 2 * (right - left))
            masses[i] = radial_mass * cell_area

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


def _signed_circumcentric_dual_length(
    vertices: np.ndarray,
    a: int,
    b: int,
    face_centres: np.ndarray,
    adjacent_faces: list[int],
    tol: float = 1e-10,
) -> float:
    """Return dual arc length only when it crosses the primal edge orthogonally.

    The normalized edge midpoint and the two spherical face circumcentres lie
    on the great circle orthogonal to the primal chord.  Signed angles from
    the midpoint must have opposite signs: otherwise the shortest centre arc
    does not cross the primal edge and is not its circumcentric dual.
    """
    if len(adjacent_faces) != 2:
        raise ValueError("A closed spherical edge must have two adjacent faces")
    midpoint = vertices[a] + vertices[b]
    midpoint_norm = float(np.linalg.norm(midpoint))
    if midpoint_norm <= tol:
        raise RuntimeError("Antipodal primal edge has no unique midpoint")
    midpoint /= midpoint_norm

    c0 = face_centres[adjacent_faces[0]]
    tangent = c0 - float(np.dot(c0, midpoint)) * midpoint
    tangent_norm = float(np.linalg.norm(tangent))
    if tangent_norm <= tol:
        raise RuntimeError("Degenerate first circumcentre at primal-edge midpoint")
    tangent /= tangent_norm

    def signed_angle(c: np.ndarray) -> float:
        return math.atan2(float(np.dot(c, tangent)),
                          float(np.dot(c, midpoint)))

    theta0 = signed_angle(c0)
    theta1 = signed_angle(face_centres[adjacent_faces[1]])
    if theta0 <= tol or theta1 >= -tol:
        raise RuntimeError(
            "Circumcentres are not on opposite sides of the primal edge; "
            "unsigned centre distance is not a valid circumcentric dual"
        )
    dual = theta0 - theta1
    if not np.isfinite(dual) or dual <= 0 or dual >= math.pi:
        raise RuntimeError("Invalid oriented circumcentric dual arc")
    return float(dual)


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
        for tri in hull.simplices:
            a, b, c = map(int, tri)
            midpoint(a, b)
            midpoint(b, c)
            midpoint(c, a)
        points = np.asarray(out, dtype=float)
        # Re-hulling all normalized vertices gives the subdivided spherical triangulation.
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


def spherical_l1_rayleigh(subdivisions: int) -> float:
    """Discrete Rayleigh quotient of a coordinate l=1 spherical harmonic."""
    vertices, faces = _icosphere(subdivisions)
    areas = SphericalVoronoi(vertices).calculate_areas()
    centres = _spherical_face_centres(vertices, faces)
    edge_faces = {}
    for fi, face in enumerate(faces):
        for a, b in ((face[0], face[1]), (face[1], face[2]), (face[2], face[0])):
            key = (min(int(a), int(b)), max(int(a), int(b)))
            edge_faces.setdefault(key, []).append(fi)
    energy = 0.0
    values = vertices[:, 2]
    for (a, b), adjacent in edge_faces.items():
        primal = _angle(vertices[a], vertices[b])
        dual = _signed_circumcentric_dual_length(
            vertices, a, b, centres, adjacent
        )
        energy += (dual / primal) * (values[a] - values[b]) ** 2
    norm2 = float(np.dot(areas, values ** 2))
    if norm2 <= 0:
        raise RuntimeError("Degenerate l=1 test mode")
    return float(energy / norm2)


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
        "spherical_l1_rayleigh": spherical_l1_rayleigh(subdivisions),
        "spherical_l1_continuum_eigenvalue": 2.0,
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
