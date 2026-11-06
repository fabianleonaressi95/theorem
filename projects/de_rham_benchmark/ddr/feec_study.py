"""FEEC projection and discrete-adjoint benchmark on curvilinear cubical meshes.

Builds on the consistent tensor-product cubical FEEC masses of
``feec_mass.assemble_consistent_masses`` and measures, under mesh
refinement and under the curvature/metric stress tests:

* map-quality checks (uniform Jacobian bounds, inverse regularity,
  face conformity, injectivity proxy)               [Phase A]
* de Rham (face-integral) projections pi_h, the commutator
  d_h pi_h = pi_h d, L2 / H-Lambda approximation errors, and operator
  norms of pi_h                                          [Phase B]
* discrete codifferentials delta_h = M_{k-1}^{-1} D_{k-1}^T M_k and their
  consistency residuals against the continuous codifferential on test
  forms, plus mass stability (conditioning, spectral bounds) [Phase C]
* convergence indicators: lambda_min^+, spectral gap, kernel dimension,
  harmonic subspace dimension for the FEEC masses          [Phase D]

Everything is a *numerical observation* on fixed meshes; no compactness
or Mosco-convergence claim is made (see docs/FEEC_PROJECTIONS.md).
"""
from __future__ import annotations

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import scipy.linalg as sla

from .mesh import CubicalMesh
from .geometry import _tensor_gauss
from .kforms import (combos, combo_index, pullback_components,
                     pointwise_norm2_g, subdet)
from .feec_mass import assemble_consistent_masses


# ====================================================================== #
# Phase A: geometry checks
# ====================================================================== #
def vertex_ref_coords(mesh):
    """Reference coordinates of every vertex, shape (nv, d)."""
    d = mesh.dim
    out = np.zeros((mesh.nv, d))
    for vid in range(mesh.nv):
        for a in range(d):
            c = (vid // mesh.vstride[a]) % (mesh.Ns[a] + 1)
            out[vid, a] = c / mesh.Ns[a]    # ref coord in [0,1]
    return out


def map_quality(mesh, geometry, nq_check=6):
    """Uniform bounds on the cell maps, evaluated on a check grid.

    All quantities are mesh-independent (D Phi, not DF):
      det_min/max, sigma_min/max of D Phi, ||D Phi||_2, ||(D Phi)^{-1}||_2,
      an estimate of ||D^2 Phi||_inf by central differences,
      min sqrt(det g_K), max cond(g_K), and the minimum k-face measure.
    Face conformity is checked by comparing the physical images of the
    vertices of every interior facet computed from each incident cell
    (identical by construction of the global map; the check catches
    implementation errors).  Injectivity is *not* proven; the proxy
    reported is min det(D Phi) > 0 together with boundary preservation
    (|Phi(x)-x| = 0 on dOmega for the bump family), which for a map
    homotopic to the identity implies global injectivity.
    """
    d = mesh.dim
    xiq, _ = _tensor_gauss(nq_check, d)
    dets, smins, smaxs, invs, d2 = [], [], [], [], []
    eps = 1e-5
    for cid in range(mesh.nk[d]):
        DF, g, Y, J = geometry._cell_frame(cid, xiq)
        detJ = np.linalg.det(J)
        sv = np.linalg.svd(J, compute_uv=False)
        dets.append(detJ)
        smins.append(sv[..., -1])
        smaxs.append(sv[..., 0])
        try:
            invs.append(np.linalg.norm(np.linalg.inv(J), axis=(-2, -1)))
        except np.linalg.LinAlgError:
            invs.append(np.full(J.shape[:-2], np.inf))
        # ||D^2 Phi|| estimate: central difference of J along each axis
        p = geometry.cell_p[cid]
        for a in range(d):
            xp = (p + xiq * geometry.hs).copy()
            xm = xp.copy()
            xp[..., a] += eps
            xm[..., a] -= eps
            Jp = geometry.dmap.jac(xp)
            Jm = geometry.dmap.jac(xm)
            d2.append(np.abs(Jp - Jm).max(axis=(-2, -1)) / (2 * eps))
    dets = np.concatenate([np.atleast_1d(x) for x in dets])
    smins = np.concatenate([np.atleast_1d(x) for x in smins])
    smaxs = np.concatenate([np.atleast_1d(x) for x in smaxs])
    invs = np.concatenate([np.atleast_1d(x) for x in invs])
    d2 = np.concatenate([np.atleast_1d(x) for x in d2]) if d2 else np.array([0.0])

    # boundary preservation of Phi on dOmega: the *normal* component must
    # stay fixed on each face (tangential sliding is allowed)
    bnd = []
    grids = np.meshgrid(*[np.linspace(0, 1, 5)] * d, indexing="ij")
    X = np.stack([g_.ravel() for g_ in grids], axis=-1)
    for a in range(d):
        for side in (0.0, 1.0):
            Xb = X.copy()
            Xb[..., a] = side
            bnd.append(np.abs(geometry.dmap.phi(Xb)[..., a] - side).max())
    boundary_dev = float(max(bnd)) if bnd else 0.0

    # Face conformity.  Because a single global map Phi defines every cell
    # map F_K(xi) = Phi(p_K + h xi), shared faces are conforming by
    # construction; the numerical check verifies (i) every interior
    # k-face has exactly 2^{d-k} incident cells and every boundary face
    # fewer, and (ii) the physical images of face vertices computed via
    # each incident cell agree to roundoff.
    vcoords = vertex_ref_coords(mesh)
    max_dev = 0.0
    incidence_ok = True
    for k in range(d):
        for fid, cells in enumerate(mesh.cells_of_face[k]):
            f = mesh.faces[k][fid]
            # expected incident count: interior 2^{d-k}, boundary less
            if len(cells) > 2 ** (d - k):
                incidence_ok = False
            imgs = []
            for cid in cells:
                ci = np.asarray(mesh.cell_lo[cid], dtype=float)
                # vertex ref coords of this face -> cell-local xi -> F_K
                loc = (vcoords[list(f.verts)] - ci * geometry.hs) \
                    / geometry.hs
                imgs.append(geometry.dmap.phi(ci * geometry.hs
                                               + loc * geometry.hs))
            if len(imgs) > 1:
                for other in imgs[1:]:
                    max_dev = max(max_dev,
                                  float(np.abs(imgs[0] - other).max()))
    conformity_ok = bool(incidence_ok and max_dev < 1e-10)

    return {
        "min_det_jac": float(dets.min()),
        "max_det_jac": float(dets.max()),
        "min_sigma_jac": float(smins.min()),
        "max_sigma_jac": float(smaxs.max()),
        "max_inv_jac_norm": float(np.max(invs)),
        "max_second_derivative_est": float(d2.max()),
        "min_sqrt_det_g": float(geometry.geo["min_sqrt_det_g"]),
        "max_cond_g": float(geometry.geo["max_cond_g"]),
        "boundary_deviation": boundary_dev,
        "face_conformity_max_dev": max_dev,
        "face_conformity_ok": conformity_ok,
        "injectivity_proxy": bool(dets.min() > 0 and boundary_dev < 1e-12),
    }


# ====================================================================== #
# Phase B: de Rham (face-integral) projections
# ====================================================================== #
def _face_quad_points(mesh, geometry, cid, f, nqf):
    """Local xi points and weights on the k-face f of cell cid."""
    k = f.k
    ci = np.asarray(mesh.cell_lo[cid], dtype=float)
    fixed = dict(f.fixed)
    xiqf, wqf = _tensor_gauss(nqf, k)
    npts = xiqf.shape[0]
    xi = np.empty((npts, mesh.dim))
    vary = list(f.vary)
    for j, ax in enumerate(vary):
        xi[:, ax] = xiqf[:, j]
    for ax, line in fixed.items():
        xi[:, ax] = float(line) - float(ci[ax])
    return xi, wqf


def face_dofs(mesh, geometry, comps_func, k, nqf=5):
    """De Rham degrees of freedom: integral of the k-form over each
    oriented k-face (point value for k = 0).

    comps_func(x) -> (..., ncomp_k) evaluates the *physical* k-form.
    """
    d = mesh.dim
    ncomp = len(combos(d, k))
    out = np.zeros(mesh.nk[k])
    if k == 0:
        vcoords = vertex_ref_coords(mesh)
        # vertex physical positions
        Y = geometry.dmap.phi(vcoords)
        vals = comps_func(Y)[..., 0]
        out[:] = np.asarray(vals).reshape(-1)[: mesh.nv]
        return out

    if k == d:
        # top-degree DOFs: integral of the d-form over each cell
        xiq, wq = _tensor_gauss(nqf, d)
        Ifull = tuple(range(d))
        jfull = combo_index(d, d)[Ifull]
        for cid in range(mesh.nk[d]):
            DF, g, Y, J = geometry._cell_frame(cid, xiq)
            u = comps_func(Y)[..., jfull]
            out[cid] = float(np.sum(wq * u * np.linalg.det(DF)))
        return out

    # integrate each face exactly once, using its first incident cell
    for fid in range(mesh.nk[k]):
        f = mesh.faces[k][fid]
        cid = mesh.cells_of_face[k][fid][0]
        xi, wqf = _face_quad_points(mesh, geometry, cid, f, nqf)
        DF, g, Y, J = geometry._cell_frame(cid, xi)
        u = comps_func(Y)                     # (..., ncomp_k)
        S = tuple(f.vary)
        # contraction u(t_1,...,t_k), t_j = DF[:, s_j]:
        # = sum_J u_J det(DF[J, S])
        acc = np.zeros(xi.shape[0])
        for b, Jdx in enumerate(combos(d, k)):
            minor = subdet(DF, Jdx, S)        # (...,)
            acc = acc + u[..., b] * minor
        out[fid] = float(np.sum(wqf * acc))
    return out


def commutation_residual(mesh, geometry, form, k, nqf=5, Mnext=None):
    """||d_h pi_h u - pi_h du|| residual for a k-form u (k < d)."""
    cu = face_dofs(mesh, geometry, form.eval, k, nqf)
    lhs = mesh.dmat[k] @ cu
    du = form.d()
    rhs = face_dofs(mesh, geometry, du.eval, k + 1, nqf)
    r = lhs - rhs
    num = float(np.max(np.abs(r)))
    # normalise by the largest relevant DOF magnitude so that exactly
    # closed forms (du == 0, rhs ~ 0) still give a meaningful residual
    scale = max(float(np.max(np.abs(cu))),
                float(np.max(np.abs(rhs))), 1e-300)
    out = {"level": k, "inf_residual": num,
           "rel_inf_residual": num / scale,
           "rhs_inf": float(np.max(np.abs(rhs)))}
    if Mnext is not None:
        out["m_norm_residual"] = float(np.sqrt(max(discrete_norm2(r, Mnext), 0.0)))
        out["m_norm_rhs"] = float(np.sqrt(max(discrete_norm2(rhs, Mnext), 0.0)))
    return out


# ====================================================================== #
# L2 norms and projection errors (pullback to reference element)
# ====================================================================== #
def l2_norm(mesh, geometry, comps_func, k, nq=None):
    """Continuous L2 norm of a physical k-form over the domain."""
    nq = nq or geometry.nq
    if nq == geometry.nq:
        xiq, wq = geometry.xiq, geometry.wq
    else:
        xiq, wq = _tensor_gauss(nq, mesh.dim)
    total = 0.0
    d = mesh.dim
    for cid in range(mesh.nk[d]):
        DF, g, Y, J = geometry._cell_frame(cid, xiq)
        u = comps_func(Y)
        uh = pullback_components(u, DF, d, k)
        n2 = pointwise_norm2_g(uh, g, d, k)
        rho = np.sqrt(np.linalg.det(g))
        total += float(np.sum(wq * n2 * rho))
    return float(np.sqrt(max(total, 0.0)))


def _reconstruct_cell(mesh, geometry, cid, coeffs, k, xiq):
    """Values of the FEEC reconstruction u_h = sum_sigma c_sigma w_sigma
    at cell quadrature points, as components in the dxi^I basis."""
    d = mesh.dim
    npts = xiq.shape[0]
    ncomp = len(combos(d, k))
    comps = np.zeros((npts, ncomp))
    ci = np.asarray(mesh.cell_lo[cid], dtype=float)
    if k == d:
        I = tuple(range(d))
        comps[:, combo_index(d, k)[I]] = coeffs[cid]
        return comps
    idx = combo_index(d, k)
    for fid in mesh.cell_to_faces[cid][k]:
        f = mesh.faces[k][fid]
        phi = np.ones(npts)
        for ax, line in dict(f.fixed).items():
            side = int(line - ci[ax])
            if side == 0:
                phi = phi * (1.0 - xiq[:, ax])
            elif side == 1:
                phi = phi * xiq[:, ax]
            else:
                raise ValueError("face not a facet of cell")
        comps[:, idx[tuple(f.vary)]] += coeffs[fid] * phi
    return comps


def projection_l2_error(mesh, geometry, comps_func, k, coeffs, nq=None):
    """||u - pi_h u||_{L2} and ||pi_h u||_{L2} for a physical k-form."""
    nq = nq or geometry.nq
    if nq == geometry.nq:
        xiq, wq = geometry.xiq, geometry.wq
    else:
        xiq, wq = _tensor_gauss(nq, mesh.dim)
    d = mesh.dim
    err2 = 0.0
    uh2 = 0.0
    for cid in range(mesh.nk[d]):
        DF, g, Y, J = geometry._cell_frame(cid, xiq)
        u = comps_func(Y)
        uh_target = pullback_components(u, DF, d, k)
        uh_disc = _reconstruct_cell(mesh, geometry, cid, coeffs, k, xiq)
        diff = uh_target - uh_disc
        rho = np.sqrt(np.linalg.det(g))
        err2 += float(np.sum(wq * pointwise_norm2_g(diff, g, d, k) * rho))
        uh2 += float(np.sum(wq * pointwise_norm2_g(uh_disc, g, d, k) * rho))
    return {"l2_error": float(np.sqrt(max(err2, 0.0))),
            "l2_reconstruction": float(np.sqrt(max(uh2, 0.0)))}


def discrete_norm2(coeffs, M):
    """c^T M c for sparse or diagonal M."""
    if sp.issparse(M):
        return float(coeffs @ (M @ coeffs))
    return float(np.sum(M * coeffs ** 2))


def hodge_energy_parts(mesh, M, coeffs, k):
    """Discrete H-Lambda energy split: grad (d_{k-1} delta part) and curl."""
    grad = 0.0
    curl = 0.0
    if k > 0:
        t = mesh.dmat[k - 1].T @ (M[k] @ coeffs if sp.issparse(M[k])
                                 else M[k] * coeffs)
        Minv = 1.0 / M[k - 1] if not sp.issparse(M[k - 1]) else None
        if Minv is not None:
            grad = float(np.sum(t ** 2 / M[k - 1]))
        else:
            # sparse mass: solve M_{k-1} y = t
            y = spla.spsolve(M[k - 1].tocsc(), t)
            grad = float(t @ y)
    if k < mesh.dim:
        dx = mesh.dmat[k] @ coeffs
        Mk1 = M[k + 1]
        curl = float(dx @ (Mk1 @ dx) if sp.issparse(Mk1)
                     else np.sum(Mk1 * dx ** 2))
    return grad, curl


# ====================================================================== #
# Phase C: discrete adjoints
# ====================================================================== #
class DiscreteAdjoints:
    """delta_h^k = M_{k-1}^{-1} D_{k-1}^T M_k with sparse FEEC masses."""

    def __init__(self, mesh, Mfeec):
        self.mesh = mesh
        self.M = Mfeec
        self._lu = {}
        for k in range(1, mesh.dim + 1):
            self._lu[k - 1] = spla.splu(Mfeec[k - 1].tocsc())

    def delta(self, k, coeffs):
        """Apply delta_h^k : C^k -> C^{k-1}."""
        Mk_c = self.M[k] @ coeffs
        t = self.mesh.dmat[k - 1].T @ Mk_c
        return self._lu[k - 1].solve(t)


def boundary_mask(mesh, j):
    """Boolean mask over j-face DOFs lying on the domain boundary."""
    mask = np.zeros(mesh.nk[j], dtype=bool)
    if j == mesh.dim:
        return mask                       # cells are never "on" dOmega
    for fid, f in enumerate(mesh.faces[j]):
        for ax, line in f.fixed:
            if line == 0 or line == mesh.Ns[ax]:
                mask[fid] = True
                break
    return mask


def core_mask(mesh, j, margin=0.2):
    """j-face DOFs whose closure lies inside [margin, 1-margin]^d.

    Fixed physical interior region: isolates the bulk consistency of the
    discrete adjoint from the boundary layer that the unconstrained
    algebraic adjoint develops near dOmega.
    """
    mask = np.zeros(mesh.nk[j], dtype=bool)
    if j == mesh.dim:
        return mask
    for fid, f in enumerate(mesh.faces[j]):
        ok = True
        fixed_map = dict(f.fixed)
        for a in range(mesh.dim):
            if a in f.vary:
                i = f.vary.index(a)
                lo, hi = f.lo[i], f.lo[i] + 1
                if lo / mesh.Ns[a] < margin or hi / mesh.Ns[a] > 1 - margin:
                    ok = False
                    break
            else:
                line = fixed_map[a]
                if line / mesh.Ns[a] < margin or line / mesh.Ns[a] > 1 - margin:
                    ok = False
                    break
        mask[fid] = ok
    return mask


def adjoint_consistency(mesh, geometry, metric, Mfeec, form, k, nqf=5):
    """Compare delta_h pi_h u with pi_h(delta u) for a k-form u (k >= 1).

    Returns residual norms in the M_{k-1} inner product, split into
    interior and boundary degrees of freedom.  Without essential boundary
    conditions the algebraic adjoint delta_h = M^{-1} D^T M contains a
    boundary flux contribution, so the *global* residual need not vanish
    under refinement; the interior residual isolates the bulk consistency.
    """
    adj = DiscreteAdjoints(mesh, Mfeec)
    cu = face_dofs(mesh, geometry, form.eval, k, nqf)
    dh = adj.delta(k, cu)
    dform = form.delta
    rhs = face_dofs(mesh, geometry,
                    lambda x: dform(x, metric), k - 1, nqf)
    r = dh - rhs
    bmask = boundary_mask(mesh, k - 1)
    cmask = core_mask(mesh, k - 1)
    imask = ~bmask
    Mkm1 = Mfeec[k - 1]

    def mnorm2(v, sel):
        if not np.any(sel):
            return 0.0
        vs = v[sel]
        if sp.issparse(Mkm1):
            sub = Mkm1[sel][:, sel]
            return float(vs @ (sub @ vs))
        return float(np.sum(Mkm1[sel][:, sel] * np.outer(vs, vs)))

    num = mnorm2(r, np.ones(len(r), dtype=bool))
    num_i = mnorm2(r, imask)
    num_b = mnorm2(r, bmask)
    num_d = mnorm2(r, cmask)
    den = max(mnorm2(rhs, np.ones(len(rhs), dtype=bool)), 1e-300)
    return {
        "level": k,
        "m_norm_residual": float(np.sqrt(max(num, 0.0))),
        "m_norm_residual_interior": float(np.sqrt(max(num_i, 0.0))),
        "m_norm_residual_core": float(np.sqrt(max(num_d, 0.0))),
        "m_norm_residual_boundary": float(np.sqrt(max(num_b, 0.0))),
        "m_norm_rhs": float(np.sqrt(den)),
        "rel_m_residual": float(np.sqrt(max(num, 0.0) / den)),
        "rel_m_residual_interior": float(np.sqrt(max(num_i, 0.0) / den)),
        "rel_m_residual_core": float(np.sqrt(max(num_d, 0.0) / den)),
        "inf_residual": float(np.max(np.abs(r))),
        "inf_residual_interior": (float(np.max(np.abs(r[imask])))
                                  if np.any(imask) else 0.0),
        "inf_residual_core": (float(np.max(np.abs(r[cmask])))
                              if np.any(cmask) else 0.0),
        "inf_rhs": float(np.max(np.abs(rhs))),
        "n_boundary_dofs": int(np.sum(bmask)),
        "n_core_dofs": int(np.sum(cmask)),
    }


def mass_stability(Mfeec):
    """Condition numbers / spectral bounds of the FEEC mass matrices."""
    out = []
    for k, M in enumerate(Mfeec):
        Md = M.toarray()
        w = sla.eigvalsh(0.5 * (Md + Md.T))
        out.append({"k": k, "n": M.shape[0],
                    "min_eig": float(w[0]), "max_eig": float(w[-1]),
                    "cond": float(w[-1] / w[0]) if w[0] > 0 else np.inf})
    return out


# ====================================================================== #
# Phase D: spectral indicators for FEEC masses
# ====================================================================== #
def feec_spectrum(mesh, Mfeec, beta, k_eig=10, k_max=3):
    """Smallest positive eigenvalue, gap and kernel dimension per level.

    Uses dense generalized eigh (audit-size meshes only).
    """
    from .feec_mass import consistent_hodge_matrices
    B = consistent_hodge_matrices(mesh, Mfeec)
    out = {}
    for k in range(mesh.dim + 1):
        Bd = B[k]
        Md = Mfeec[k].toarray()
        w, V = sla.eigh(0.5 * (Bd + Bd.T), 0.5 * (Md + Md.T))
        order = np.argsort(w)
        w = w[order]
        n = len(w)
        # kernel dim = beta_k expected; measure gap after beta_k zeros
        bk = beta[k]
        pos = w[bk:] if bk < n else np.array([])
        lam_min = float(pos[0]) if len(pos) else np.nan
        # numerical kernel count with absolute tolerance scaled to lambda_max
        tol = 1e-8 * max(float(w[-1]), 1.0)
        kernel_num = int(np.sum(w < tol))
        # first positive eigenpair residual
        resid = np.nan
        if len(pos):
            x = V[:, order[bk]]
            r = Bd @ x - w[bk] * (Md @ x)
            resid = float(np.linalg.norm(r) /
                          max(1e-300, np.linalg.norm(Bd) * np.linalg.norm(x)
                              + abs(w[bk]) * np.linalg.norm(Md @ x)))
        out[k] = {
            "lambda_min_pos": lam_min,
            "lambda_max": float(w[-1]),
            "spectral_gap": (float(pos[1] - pos[0])
                             if len(pos) > 1 else np.nan),
            "kernel_num": kernel_num,
            "betti": int(bk),
            "kernel_matches_betti": bool(kernel_num == bk),
            "eigs_small": [float(v) for v in w[:min(k_eig, n)]],
            "max_eig_resid_first_pos": resid,
        }
    return out


# ====================================================================== #
# Test-form suite
# ====================================================================== #
def default_test_forms(dim, seed=0):
    """Deterministic suite of smooth forms, one per degree plus extras."""
    from .test_forms import ScalarField, Form
    forms = {}
    f0 = ScalarField.mixed(dim, seed=seed)
    fb = ScalarField.bump(dim)
    forms[0] = [("scalar_mixed", Form(dim, 0, [(f0, ())])),
                ("scalar_bump", Form(dim, 0, [(fb, ())]))]
    # generic (non-exact) 1-form: independent coefficients per direction
    f1 = [ScalarField.mixed(dim, seed=seed + 10 + i) for i in range(dim)]
    forms[1] = [
        ("generic_1form", Form(dim, 1, [(f1[i], (i,)) for i in range(dim)])),
        ("exact_gradient", Form.exact_gradient(dim, f0)),
        ("compact_1form", Form.single(dim, 1, fb, (0,))),
    ]
    if dim == 2:
        forms[2] = [("top_form", Form.from_scalar_top(dim, f0)),
                    ("compact_top", Form.from_scalar_top(dim, fb))]
    else:
        # generic 2-form + top form
        g01 = ScalarField.mixed(dim, seed=seed + 30)
        g12 = ScalarField.mixed(dim, seed=seed + 31)
        forms[2] = [
            ("generic_2form",
             Form(dim, 2, [(g01, (0, 1)), (g12, (1, 2))])),
            ("compact_2form", Form.single(dim, 2, fb, (0, 1))),
        ]
        forms[3] = [("top_form", Form.from_scalar_top(dim, f0)),
                    ("compact_top", Form.from_scalar_top(dim, fb))]
    return forms


# ====================================================================== #
# One-shot analysis for a (mesh, geometry) pair
# ====================================================================== #
def analyze_feec(mesh, geometry, metric, Mfeec, beta, nqf=5, nq=None,
                 seed=0, spectral=True):
    """Run the full FEEC projection/adjoint study on one mesh."""
    d = mesh.dim
    out = {"geometry_checks": map_quality(mesh, geometry),
           "mass_stability": mass_stability(Mfeec),
           "forms": {}}
    adj = DiscreteAdjoints(mesh, Mfeec)
    forms = default_test_forms(d, seed)
    for k in range(d + 1):
        out["forms"][str(k)] = []
        for name, form in forms.get(k, []):
            entry = {"name": name}
            cu = face_dofs(mesh, geometry, form.eval, k, nqf)
            entry["dofs_norm_M"] = float(np.sqrt(max(
                discrete_norm2(cu, Mfeec[k]), 0.0)))
            entry["l2_norm"] = l2_norm(mesh, geometry, form.eval, k, nq)
            # operator norm of pi_h on this test form
            entry["pi_h_over_L2"] = (entry["dofs_norm_M"] / entry["l2_norm"]
                                     if entry["l2_norm"] > 0 else np.nan)
            # projection L2 error
            perr = projection_l2_error(mesh, geometry, form.eval, k, cu, nq)
            entry["l2_projection_error"] = perr["l2_error"]
            entry["l2_projection_rel"] = (perr["l2_error"] / entry["l2_norm"]
                                          if entry["l2_norm"] > 0 else np.nan)
            # commutator d_h pi_h = pi_h d (k < d)
            if k < d:
                entry["commutator"] = commutation_residual(
                    mesh, geometry, form, k, nqf, Mnext=Mfeec[k + 1])
            # adjoint consistency (k >= 1)
            if k >= 1:
                entry["adjoint"] = adjoint_consistency(
                    mesh, geometry, metric, Mfeec, form, k, nqf)
            # energy consistency: discrete energy vs continuous
            # ||du||^2 + ||delta u||^2 (L2 norms of the respective forms)
            grad, curl = hodge_energy_parts(mesh, Mfeec, cu, k)
            e_disc = grad + curl
            e_cont = 0.0
            if k < d:
                du = form.d()
                e_cont += l2_norm(mesh, geometry, du.eval, k + 1, nq) ** 2
            if k >= 1:
                dform = form.delta
                e_cont += l2_norm(mesh, geometry,
                                  lambda x: dform(x, metric), k - 1,
                                  nq) ** 2
            entry["energy_discrete"] = float(e_disc)
            entry["energy_continuous"] = float(e_cont)
            entry["energy_ratio"] = (float(e_disc / e_cont)
                                     if e_cont > 0 else np.nan)
            out["forms"][str(k)].append(entry)
    if spectral:
        out["spectra"] = {str(k): v for k, v in
                          feec_spectrum(mesh, Mfeec, beta).items()}
    return out
