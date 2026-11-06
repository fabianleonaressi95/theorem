"""Smoke tests for the FEEC projection / adjoint benchmark (Phases A-C)."""
import numpy as np

from ddr.mesh import CubicalMesh
from ddr.geometry import PullbackGeometry, DomainMap
from ddr.feec_mass import assemble_consistent_masses
from ddr.feec_study import (analyze_feec, adjoint_consistency, boundary_mask,
                            commutation_residual, core_mask, face_dofs,
                            l2_norm, map_quality, projection_l2_error,
                            vertex_ref_coords)
from ddr.test_forms import ScalarField, Form


def _setup(N=4, dim=2, map_spec=None, metric_spec=None, nqf=6):
    mesh = CubicalMesh(N, dim)
    geo = PullbackGeometry(mesh, map_spec or {"type": "identity"},
                           metric_spec or {"type": "identity"},
                           nq=4, nqf=nqf)
    M, _ = assemble_consistent_masses(mesh, geo)
    return mesh, geo, M


def _poly_form(dim):
    terms = [{"kind": "monomial", "powers": tuple([2] + [0] * (dim - 1)),
              "coeff": 1.0},
             {"kind": "monomial",
              "powers": tuple([0] * (dim - 1) + [1]), "coeff": 1.0}]
    return Form(dim, 0, [(ScalarField(dim, terms), ())])


def test_vertex_coordinates_match_key_order():
    for dim, N in ((2, 3), (3, 2)):
        mesh = CubicalMesh(N, dim)
        vc = vertex_ref_coords(mesh)
        for vid in range(mesh.nv):
            for a in range(dim):
                c = (vid // mesh.vstride[a]) % (mesh.Ns[a] + 1)
                assert abs(vc[vid, a] - c / mesh.Ns[a]) < 1e-12


def test_commutator_exact_polynomial():
    mesh, geo, M = _setup()
    f0 = _poly_form(2)
    r0 = commutation_residual(mesh, geo, f0, 0, nqf=6, Mnext=M[1])
    assert r0["rel_inf_residual"] < 1e-12
    u1 = f0.d()
    r1 = commutation_residual(mesh, geo, u1, 1, nqf=6, Mnext=M[2])
    assert r1["rel_inf_residual"] < 1e-10


def test_commutator_curved_map():
    mesh, geo, M = _setup(map_spec={"type": "sinusoid",
                                    "amplitude": 0.15, "freq": 1})
    f0 = _poly_form(2)
    r0 = commutation_residual(mesh, geo, f0, 0, nqf=6, Mnext=M[1])
    assert r0["rel_inf_residual"] < 1e-10


def test_projection_error_decreases():
    errs = []
    for N in (4, 8):
        mesh, geo, M = _setup(N=N)
        form = Form.exact_gradient(2, ScalarField.mixed(2, seed=1))
        cu = face_dofs(mesh, geo, form.eval, 1, 6)
        ref = l2_norm(mesh, geo, form.eval, 1, nq=5)
        perr = projection_l2_error(mesh, geo, form.eval, 1, cu, nq=5)
        errs.append(perr["l2_error"] / ref)
    assert errs[1] < 0.7 * errs[0]


def test_adjoint_compact_form_converges():
    rels = []
    for N in (4, 8):
        mesh, geo, M = _setup(N=N, nqf=8)
        fb = ScalarField.bump(2)
        u = Form.single(2, 1, fb, (0,))
        r = adjoint_consistency(mesh, geo, geo.metric, M, u, 1, nqf=8)
        rels.append(r["rel_m_residual"])
        assert r["rel_m_residual_core"] < r["rel_m_residual"] + 1e-12
    assert rels[1] < 0.7 * rels[0]


def test_adjoint_boundary_layer_documented():
    # u = dx has zero strong codifferential but nonzero boundary flux;
    # the unconstrained algebraic adjoint must show a boundary residual.
    mesh, geo, M = _setup(N=6)
    f = ScalarField(2, [{"kind": "monomial", "powers": (0, 0),
                         "coeff": 1.0}])
    u = Form(2, 1, [(f, (0,))])
    r = adjoint_consistency(mesh, geo, geo.metric, M, u, 1, nqf=6)
    assert r["m_norm_residual_boundary"] > 0
    assert r["inf_residual"] > r["inf_residual_core"]


def test_map_quality_identity_and_sinusoid():
    for spec in ({"type": "identity"},
                 {"type": "sinusoid", "amplitude": 0.2, "freq": 1}):
        mesh, geo, _ = _setup(map_spec=spec)
        q = map_quality(mesh, geo)
        assert q["min_det_jac"] > 0
        assert q["face_conformity_ok"]
        assert q["injectivity_proxy"]
    q = map_quality(*_setup(map_spec={"type": "axis_bump",
                                      "amplitude": 0.15})[:2])
    assert q["min_det_jac"] > 0 and q["face_conformity_ok"]


def test_axis_bump_jacobian_fd():
    dm = DomainMap({"type": "axis_bump", "amplitude": 0.2}, 2)
    rng = np.random.default_rng(0)
    X = rng.random((20, 2))
    J = dm.jac(X)
    eps = 1e-7
    for a in range(2):
        Xp = X.copy(); Xp[:, a] += eps
        Xm = X.copy(); Xm[:, a] -= eps
        fd = (dm.phi(Xp) - dm.phi(Xm)) / (2 * eps)
        assert np.abs(fd - J[:, :, a]).max() < 1e-6


def test_masks():
    mesh = CubicalMesh(6, 2)
    bm = boundary_mask(mesh, 0)
    cm = core_mask(mesh, 0)
    assert bm.sum() == mesh.nv - (mesh.Ns[0] - 1) * (mesh.Ns[1] - 1)
    assert cm.sum() > 0 and not np.any(bm & cm)


def test_analyze_feec_small():
    mesh, geo, M = _setup(N=4)
    from ddr.hodge import betti_numbers
    beta, _ = betti_numbers(mesh)
    out = analyze_feec(mesh, geo, geo.metric, M, beta, nqf=6, nq=4,
                       spectral=False)
    assert out["geometry_checks"]["face_conformity_ok"]
    assert "spectra" not in out
    for k in range(3):
        for entry in out["forms"][str(k)]:
            assert np.isfinite(entry["l2_projection_rel"])
            if "commutator" in entry:
                assert entry["commutator"]["rel_inf_residual"] < 1e-8


if __name__ == "__main__":
    for name, fn in sorted(list(globals().items())):
        if name.startswith("test_"):
            fn()
            print(f"{name}: ok")
