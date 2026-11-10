"""Tests for the relative cubical FEEC complex."""
import numpy as np

from ddr.mesh import CubicalMesh
from ddr.geometry import PullbackGeometry
from ddr.feec_mass import assemble_consistent_masses
from ddr.boundary_complex import (build_relative_complex,
                                  relative_betti_numbers,
                                  relative_boundary_mask)


def test_relative_boundary_masks_and_dimensions_2d():
    mesh = CubicalMesh(2, 2)
    rel = build_relative_complex(mesh)
    assert rel.dimensions == [1, 4, 4]
    assert [int(m.sum()) for m in rel.boundary] == [8, 8, 0]


def test_relative_betti_square():
    mesh = CubicalMesh(3, 2)
    rel = build_relative_complex(mesh)
    beta, _ = relative_betti_numbers(rel)
    assert beta == [0, 0, 1]


def test_relative_betti_cube():
    mesh = CubicalMesh(2, 3)
    rel = build_relative_complex(mesh)
    beta, _ = relative_betti_numbers(rel)
    assert beta == [0, 0, 0, 1]


def test_relative_differential_is_a_complex():
    for dim, N in ((2, 3), (3, 2)):
        mesh = CubicalMesh(N, dim)
        rel = build_relative_complex(mesh)
        for k in range(dim - 1):
            dd = rel.dmat[k + 1] @ rel.dmat[k]
            assert dd.nnz == 0 or np.max(np.abs(dd.data)) == 0


def test_relative_subspace_has_no_boundary_leakage():
    mesh = CubicalMesh(3, 2)
    rel = build_relative_complex(mesh)
    for k, D in enumerate(mesh.dmat):
        omitted = np.flatnonzero(rel.boundary[k + 1])
        leak = D[omitted, :][:, rel.keep[k]]
        assert leak.nnz == 0 or np.max(np.abs(leak.data)) == 0


def test_relative_consistent_masses_are_spd():
    mesh = CubicalMesh(2, 2)
    geo = PullbackGeometry(mesh, {"type": "sinusoid",
                                 "amplitude": 0.15, "freq": 1},
                           {"type": "identity"}, nq=5, nqf=5)
    masses, _ = assemble_consistent_masses(mesh, geo)
    rel = build_relative_complex(mesh, masses)
    assert rel.masses is not None
    for M in rel.masses:
        Md = M.toarray()
        np.testing.assert_allclose(Md, Md.T, atol=1e-12)
        if Md.size:
            assert np.linalg.eigvalsh(Md)[0] > 0


def test_top_degree_has_no_boundary_trace_dofs():
    mesh = CubicalMesh(3, 3)
    mask = relative_boundary_mask(mesh, 3)
    assert not np.any(mask)
    assert np.all(build_relative_complex(mesh).dimensions[-1]
                  == mesh.nk[3])


if __name__ == "__main__":
    for name, fn in sorted(list(globals().items())):
        if name.startswith("test_"):
            fn()
            print(f"{name}: ok")
