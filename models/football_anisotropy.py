"""Coarse panel-network model for pentagon/hexagon-induced football anisotropy.

This is an explicitly phenomenological, linear panel-normal model. It is not a
finite-element shell solver and does not claim material validation.
"""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations

import numpy as np


def _icosahedron():
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    raw = []
    for a in (-1.0, 1.0):
        for b in (-phi, phi):
            raw.append((0.0, a, b))
            raw.append((a, b, 0.0))
            raw.append((b, 0.0, a))
    vertices = np.unique(np.asarray(raw, dtype=float), axis=0)
    vertices /= np.linalg.norm(vertices, axis=1)[:, None]
    distances = np.linalg.norm(vertices[:, None, :] - vertices[None, :, :], axis=2)
    edge_length = np.min(distances[distances > 1e-10])
    edges = {
        (i, j)
        for i in range(len(vertices))
        for j in range(i + 1, len(vertices))
        if abs(distances[i, j] - edge_length) < 1e-8
    }
    faces = [
        tuple(triangle)
        for triangle in combinations(range(len(vertices)), 3)
        if all(tuple(sorted(edge)) in edges for edge in combinations(triangle, 2))
    ]
    return vertices, edges, faces


def _ordered_ring(points: np.ndarray, center: np.ndarray):
    normal = center / np.linalg.norm(center)
    trial = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(trial, normal)) > 0.9:
        trial = np.array([0.0, 1.0, 0.0])
    e1 = trial - np.dot(trial, normal) * normal
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(normal, e1)
    relative = points - center
    angles = np.arctan2(relative @ e2, relative @ e1)
    return np.argsort(angles)


def build_truncated_icosahedron(radius: float = 1.0):
    """Build the 60-vertex, 12-pentagon, 20-hexagon panel complex."""
    if radius <= 0:
        raise ValueError("radius must be positive")
    ico, ico_edges, ico_faces = _icosahedron()
    directed = {}
    for i, j in ico_edges:
        directed[(i, j)] = (2.0 * ico[i] + ico[j]) / 3.0
        directed[(j, i)] = (2.0 * ico[j] + ico[i]) / 3.0
    directed_keys = sorted(directed)
    key_to_id = {key: index for index, key in enumerate(directed_keys)}
    vertices = np.asarray([directed[key] for key in directed_keys])
    vertices *= radius / np.mean(np.linalg.norm(vertices, axis=1))

    panels = []
    panel_types = []
    for i in range(len(ico)):
        neighbors = sorted(j for a, j in directed_keys if a == i)
        ids = [key_to_id[(i, j)] for j in neighbors]
        points = vertices[ids]
        order = _ordered_ring(points, np.mean(points, axis=0))
        panels.append(tuple(ids[k] for k in order))
        panel_types.append("pentagon")

    for a, b, c in ico_faces:
        cycle = (a, b, c)
        directed_cycle = []
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            directed_cycle.extend((key_to_id[(u, v)], key_to_id[(v, u)]))
        points = vertices[directed_cycle]
        order = _ordered_ring(points, np.mean(points, axis=0))
        panels.append(tuple(directed_cycle[k] for k in order))
        panel_types.append("hexagon")

    for index, face in enumerate(panels):
        points = vertices[list(face)]
        normal = np.zeros(3)
        for x, y in zip(points, np.roll(points, -1, axis=0)):
            normal += np.cross(x, y)
        if np.dot(normal, np.mean(points, axis=0)) < 0:
            panels[index] = tuple(reversed(face))

    edge_to_panels = defaultdict(list)
    for panel_index, face in enumerate(panels):
        for u, v in zip(face, face[1:] + face[:1]):
            edge_to_panels[tuple(sorted((u, v)))].append(panel_index)
    if any(len(adjacent) != 2 for adjacent in edge_to_panels.values()):
        raise RuntimeError("non-manifold panel edge incidence")
    panel_edges = [
        (adjacent[0], adjacent[1], edge)
        for edge, adjacent in edge_to_panels.items()
    ]

    centers = np.asarray([np.mean(vertices[list(face)], axis=0) for face in panels])
    normals = []
    areas = []
    for face, center in zip(panels, centers):
        points = vertices[list(face)]
        normal = np.zeros(3)
        for x, y in zip(points, np.roll(points, -1, axis=0)):
            normal += np.cross(x, y)
        normal /= np.linalg.norm(normal)
        if np.dot(normal, center) < 0:
            normal = -normal
        normals.append(normal)
        area_vector = np.zeros(3)
        for i in range(1, len(points) - 1):
            area_vector += np.cross(points[i] - points[0], points[i + 1] - points[0])
        areas.append(0.5 * np.linalg.norm(area_vector))

    return {
        "vertices": vertices,
        "panels": panels,
        "panel_types": np.asarray(panel_types),
        "panel_centers": centers,
        "panel_normals": np.asarray(normals),
        "panel_areas": np.asarray(areas),
        "panel_edges": panel_edges,
        "mesh_edges": list(edge_to_panels),
    }


def solve_panel_model(mesh, pressure=0.01, C5=1.25, C6=1.0, coupling=0.15):
    r"""Solve the convex panel-normal energy.

    E(q) = 1/2 sum_i C_type(i) A_i q_i^2
         + 1/2 coupling sum_(i,j) l_ij (q_i-q_j)^2
         - pressure sum_i A_i q_i.

    q_i is the normal displacement of panel i's representative patch centre.
    """
    if min(pressure, C5, C6) <= 0 or coupling < 0:
        raise ValueError("pressure and moduli must be positive; coupling nonnegative")
    areas = mesh["panel_areas"]
    types = mesh["panel_types"]
    moduli = np.where(types == "pentagon", C5, C6)
    panel_count = len(types)
    stiffness = np.diag(moduli * areas)
    for i, j, edge in mesh["panel_edges"]:
        length = np.linalg.norm(
            mesh["vertices"][edge[0]] - mesh["vertices"][edge[1]]
        )
        weight = coupling * length
        stiffness[i, i] += weight
        stiffness[j, j] += weight
        stiffness[i, j] -= weight
        stiffness[j, i] -= weight

    force = pressure * areas
    displacement = np.linalg.solve(stiffness, force)
    residual = float(
        np.linalg.norm(stiffness @ displacement - force)
        / max(np.linalg.norm(force), 1e-30)
    )
    energy = float(
        0.5 * displacement @ stiffness @ displacement - force @ displacement
    )

    radii_before = np.linalg.norm(mesh["panel_centers"], axis=1)
    moved_centers = (
        mesh["panel_centers"]
        + displacement[:, None] * mesh["panel_normals"]
    )
    radii_after = np.linalg.norm(moved_centers, axis=1)
    radial_increment = radii_after - radii_before
    mean_increment = float(np.average(radial_increment, weights=areas))
    radial_rms = float(
        np.sqrt(
            np.average((radial_increment - mean_increment) ** 2, weights=areas)
        )
    )
    pentagon_q = displacement[types == "pentagon"]
    hexagon_q = displacement[types == "hexagon"]
    geometry = {
        "vertices": int(len(mesh["vertices"])),
        "panels": int(panel_count),
        "pentagons": int(np.sum(types == "pentagon")),
        "hexagons": int(np.sum(types == "hexagon")),
        "panel_adjacencies": int(len(mesh["panel_edges"])),
        "pentagon_hexagon_adjacencies": int(
            sum(types[i] != types[j] for i, j, _ in mesh["panel_edges"])
        ),
        "hexagon_hexagon_adjacencies": int(
            sum(
                types[i] == types[j] == "hexagon"
                for i, j, _ in mesh["panel_edges"]
            )
        ),
        "pentagon_pentagon_adjacencies": int(
            sum(
                types[i] == types[j] == "pentagon"
                for i, j, _ in mesh["panel_edges"]
            )
        ),
    }
    solution = {
        "linear_system_relative_residual": residual,
        "energy": energy,
        "mean_panel_displacement": float(np.average(displacement, weights=areas)),
        "pentagon_mean_displacement": float(np.mean(pentagon_q)),
        "hexagon_mean_displacement": float(np.mean(hexagon_q)),
        "pentagon_hexagon_displacement_contrast": float(
            np.mean(pentagon_q) - np.mean(hexagon_q)
        ),
        "panel_center_mean_radius_before": float(
            np.average(radii_before, weights=areas)
        ),
        "panel_center_mean_radius_after": float(
            np.average(radii_after, weights=areas)
        ),
        "mean_radial_increment": mean_increment,
        "panel_center_radial_increment_peak_to_peak": float(
            np.ptp(radial_increment)
        ),
        "panel_center_radial_rms_anisotropy": radial_rms,
        "stiffness_min_eigenvalue": float(np.linalg.eigvalsh(stiffness)[0]),
    }
    report = {
        "model": "linear_panel_normal_network_v1",
        "status": "numerically_verified_phenomenological_model",
        "not_claimed": [
            "nonlinear_shell_solution",
            "finite_element_validation",
            "experimental_material_validation",
        ],
        "parameters": {
            "pressure": float(pressure),
            "C5": float(C5),
            "C6": float(C6),
            "coupling": float(coupling),
        },
        "geometry": geometry,
        "solution": solution,
        "interpretation": (
            "The pentagon/hexagon contrast is a coarse-grained patch response. "
            "Radial RMS is the weighted variation of panel-centre radial "
            "increments, not a certified continuum sphericity measure."
        ),
    }
    return displacement, stiffness, report


def run_audit(pressure=0.01, C5=1.25, C6=1.0, coupling=0.15):
    mesh = build_truncated_icosahedron()
    displacement, stiffness, report = solve_panel_model(
        mesh, pressure, C5, C6, coupling
    )
    isotropic_q, _, isotropic = solve_panel_model(
        mesh, pressure, 1.0, 1.0, coupling
    )
    report["isotropic_control"] = {
        "C5": 1.0,
        "C6": 1.0,
        "displacement_contrast": isotropic["solution"][
            "pentagon_hexagon_displacement_contrast"
        ],
        "panel_center_radial_rms_anisotropy": isotropic["solution"][
            "panel_center_radial_rms_anisotropy"
        ],
        "expected_uniform_displacement": float(pressure),
        "max_abs_displacement_error": float(
            np.max(np.abs(isotropic_q - pressure))
        ),
    }
    report["comparison"] = {
        "anisotropic_minus_isotropic_radial_rms": (
            report["solution"]["panel_center_radial_rms_anisotropy"]
            - isotropic["solution"]["panel_center_radial_rms_anisotropy"]
        ),
        "anisotropy_ratio_C5_over_C6": float(C5 / C6),
    }
    return mesh, displacement, stiffness, report
