"""Bundle-valued tangent anisotropy induced by PRISM/G2 tripletti.

The G2 triplett supplies a positive-semidefinite 3x3 Gram form. A separately
specified rank-two map sends its three channels into a shell tangent fibre.
No identification between Q6's 188D tangent space and a football tangent
fibre is implicit: that transfer map is explicit input and remains a
mathematical/data obligation.
"""
from __future__ import annotations
import numpy as np

Q_G2 = np.array([[2.0, -3.0], [-3.0, 6.0]])


def triplett_gram(triplett, q_g2=Q_G2):
    """Return Gamma=R.T Q_G2 R for three column vectors in R^2."""
    R = np.asarray(triplett, dtype=float)
    Q = np.asarray(q_g2, dtype=float)
    if R.shape != (2, 3) or Q.shape != (2, 2):
        raise ValueError("triplett must be 2x3 and q_g2 must be 2x2")
    if not np.allclose(Q, Q.T, atol=1e-12):
        raise ValueError("q_g2 must be symmetric")
    G = R.T @ Q @ R
    return 0.5 * (G + G.T)


def tangent_triplet_anisotropy(triplett, channel_to_ambient, normal,
                               tangent_frame=None, q_g2=Q_G2, tol=1e-9):
    """Push a triplett Gram form into one shell tangent fibre.

    channel_to_ambient is a 3x3 map from the three triplett channels to
    ambient displacement vectors. Its image must lie in n-perp and have
    rank two. The output A is the ambient representative of an endomorphism
    of T_x S; in a local orthonormal tangent frame its matrix is F.T A F.
    """
    U = np.asarray(channel_to_ambient, dtype=float)
    n = np.asarray(normal, dtype=float)
    if U.shape != (3, 3) or n.shape != (3,):
        raise ValueError("channel map must be 3x3 and normal must be length 3")
    nn = np.linalg.norm(n)
    if nn <= tol:
        raise ValueError("normal must be nonzero")
    n = n / nn
    P = np.eye(3) - np.outer(n, n)
    if np.linalg.norm(P @ U - U) > tol * max(1.0, np.linalg.norm(U)):
        raise ValueError("channel map image is not contained in the tangent plane")
    if np.linalg.matrix_rank(U, tol=tol) != 2:
        raise ValueError("channel map must have rank two")
    G = triplett_gram(triplett, q_g2)
    A = U @ G @ U.T
    A = 0.5 * (A + A.T)
    if np.linalg.norm(P @ A @ P - A) > 10 * tol * max(1.0, np.linalg.norm(A)):
        raise ArithmeticError("pushed anisotropy failed tangent-fibre constraint")
    if tangent_frame is None:
        seed = np.array([1.0, 0.0, 0.0])
        if abs(seed @ n) > 0.9:
            seed = np.array([0.0, 1.0, 0.0])
        f1 = seed - (seed @ n) * n
        f1 /= np.linalg.norm(f1)
        f2 = np.cross(n, f1)
        F = np.column_stack((f1, f2))
    else:
        F = np.asarray(tangent_frame, dtype=float)
        if F.shape != (3, 2):
            raise ValueError("tangent_frame must be 3x2")
        if not np.allclose(F.T @ F, np.eye(2), atol=tol):
            raise ValueError("tangent_frame must be orthonormal")
        if np.linalg.norm(F.T @ n) > tol:
            raise ValueError("tangent_frame must span the tangent plane")
    A_local = F.T @ A @ F
    vals = np.linalg.eigvalsh(A_local)
    return {
        "gram": G,
        "ambient_tangent_tensor": A,
        "local_tangent_tensor": A_local,
        "tangent_frame": F,
        "eigenvalues": vals,
        "anisotropy_ratio": float(vals[-1] / vals[0]) if vals[0] > tol else float("inf"),
        "rank": int(np.linalg.matrix_rank(A_local, tol=tol)),
    }


def seam_fibre_stiffness(tangent_tensor, isotropic_tangent=0.0,
                         normal_stiffness=0.0, anisotropy_scale=1.0):
    """Build K_e on E|_Gamma = T S|_Gamma (+) N S|_Gamma.

    Returns diag(K_T, k_N) in a local orthonormal (tangent, normal) frame.
    Tangent anisotropy acts only on TS; the normal/peel channel is separate.
    """
    A = np.asarray(tangent_tensor, dtype=float)
    if A.shape != (2, 2) or not np.allclose(A, A.T, atol=1e-10):
        raise ValueError("tangent_tensor must be a symmetric 2x2 matrix")
    if min(isotropic_tangent, normal_stiffness, anisotropy_scale) < 0:
        raise ValueError("stiffness parameters must be non-negative")
    KT = isotropic_tangent * np.eye(2) + anisotropy_scale * A
    K = np.zeros((3, 3))
    K[:2, :2] = KT
    K[2, 2] = normal_stiffness
    if np.linalg.eigvalsh(K)[0] < -1e-10:
        raise ValueError("fibre stiffness must be positive semidefinite")
    return K


def induce_local_channel_map(t2u_basis, q6_to_shell_tangent, normal, tol=1e-9):
    """Compose the established Q6 T2u triplet with an explicit shell transfer.

    t2u_basis is V in R^(188x3); q6_to_shell_tangent is a pointwise
    3x188 map. Their composition U_x=P_x V must have rank two and image
    in the shell tangent plane. The transfer P_x is not inferred here.
    """
    V = np.asarray(t2u_basis, dtype=float)
    L = np.asarray(q6_to_shell_tangent, dtype=float)
    n = np.asarray(normal, dtype=float)
    if V.shape != (188, 3) or L.shape != (3, 188) or n.shape != (3,):
        raise ValueError("expected V(188x3), transfer(3x188), normal(3,)")
    if not np.allclose(V.T @ V, np.eye(3), atol=tol):
        raise ValueError("T2u triplet basis must be orthonormal")
    U = L @ V
    nn = np.linalg.norm(n)
    if nn <= tol:
        raise ValueError("normal must be nonzero")
    n = n / nn
    Ptan = np.eye(3) - np.outer(n, n)
    if np.linalg.norm(Ptan @ U - U) > tol * max(1.0, np.linalg.norm(U)):
        raise ValueError("Q6-to-shell transfer does not land in the tangent fibre")
    if np.linalg.matrix_rank(U, tol=tol) != 2:
        raise ValueError("transferred T2u triplet must have local rank two")
    return U


def build_rgs_shell_tangent_fibre_maps(source_points, shell_mesh, neighbors=16,
                                       rank_tolerance=1e-9):
    """Construct the pointwise maps L_x: R^188 -> T_x S from the audited bridge.

    Uses the existing 64->92 direction-grouped affine transfer W (lifted to
    Cartesian coordinates), the exact 188D source constraint tangent basis Q,
    and node-wise shell tangent projectors. Returns both ambient 3x188 maps
    and local 2x188 matrices in orthonormal tangent frames.

    This is a discrete nodal bundle map for this mesh, not yet a smooth
    continuum bundle morphism or a connection-preserving map.
    """
    from scipy.linalg import null_space
    from .football_quaternion_bridge import build_geometry_transfer

    X = np.asarray(source_points, dtype=float)
    nodes = np.asarray(shell_mesh["nodes"], dtype=float)
    triangles = np.asarray(shell_mesh["triangles"], dtype=int)
    if X.shape != (64, 3) or nodes.shape != (92, 3):
        raise ValueError("expected 64 RGS source points and 92 shell nodes")

    C = np.zeros((4, 192))
    C[0, 0::3] = 1.0
    C[1, 1::3] = 1.0
    C[2, 2::3] = 1.0
    C[3, :] = X.reshape(-1)
    Q = null_space(C)
    if Q.shape != (192, 188):
        raise ArithmeticError("source constraint tangent basis is not 192x188")

    W, transfer_diagnostics = build_geometry_transfer(
        X, nodes, neighbors=neighbors
    )
    # Node-wise oriented normals from the shell's triangular area vectors.
    normals = np.zeros_like(nodes)
    for tri in triangles:
        p = nodes[tri]
        area_normal = np.cross(p[1] - p[0], p[2] - p[0])
        for node in tri:
            normals[node] += area_normal
    lengths = np.linalg.norm(normals, axis=1)
    if np.any(lengths <= rank_tolerance):
        raise ArithmeticError("degenerate shell normal at one or more nodes")
    normals /= lengths[:, None]

    ambient_maps = np.empty((len(nodes), 3, 188))
    local_maps = np.empty((len(nodes), 2, 188))
    frames = np.empty((len(nodes), 3, 2))
    ranks = []
    tangency_residuals = []
    for i, normal in enumerate(normals):
        seed = np.array([1.0, 0.0, 0.0])
        if abs(seed @ normal) > 0.9:
            seed = np.array([0.0, 1.0, 0.0])
        e1 = seed - (seed @ normal) * normal
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(normal, e1)
        F = np.column_stack((e1, e2))
        P = F @ F.T
        Wi = W[3*i:3*i+3, :]
        Li = P @ Wi @ Q
        Llocal = F.T @ Li
        rank = int(np.linalg.matrix_rank(Llocal, tol=rank_tolerance))
        if rank != 2:
            raise ArithmeticError(f"tangent transfer rank {rank} at shell node {i}")
        ambient_maps[i] = Li
        local_maps[i] = Llocal
        frames[i] = F
        ranks.append(rank)
        tangency_residuals.append(float(np.linalg.norm((np.eye(3)-P) @ Li)))
    return {
        "ambient_maps": ambient_maps,
        "local_maps": local_maps,
        "tangent_frames": frames,
        "shell_normals": normals,
        "source_tangent_basis": Q,
        "cartesian_transfer": W,
        "transfer_diagnostics": transfer_diagnostics,
        "nodewise_ranks": ranks,
        "minimum_nodewise_rank": int(min(ranks)),
        "maximum_tangency_residual": float(max(tangency_residuals)),
        "source_constraint_residual": float(np.linalg.norm(C @ Q)),
        "source_basis_orthogonality": float(np.linalg.norm(Q.T @ Q - np.eye(188))),
        "interpretation": (
            "Explicit finite-mesh nodal bundle map assembled as "
            "L_i=P_i W_i Q. It is not yet a smooth connection-preserving "
            "continuum bundle morphism."
        ),
    }


def push_triplett_to_shell_nodes(triplett, fibre_maps, t2u_basis, q_g2=Q_G2):
    """Evaluate A_T(x_i)=(L_i V) Gamma_T (L_i V)* at all shell nodes.

    t2u_basis is the actual 188x3 orthonormal Q6 triplet basis. It is an
    explicit required input: the 188D-to-fibre map alone is not the 3-channel
    map and must not be multiplied directly by the 3x3 Gram matrix.
    """
    Gamma = triplett_gram(triplett, q_g2)
    L = np.asarray(fibre_maps["ambient_maps"], dtype=float)
    V = np.asarray(t2u_basis, dtype=float)
    if L.ndim != 3 or L.shape[1:] != (3, 188):
        raise ValueError("fibre maps must have shape (N,3,188)")
    if V.shape != (188, 3):
        raise ValueError("t2u_basis must have shape (188,3)")
    if not np.allclose(V.T @ V, np.eye(3), atol=1e-8):
        raise ValueError("t2u_basis must have orthonormal columns")
    channel_maps = np.einsum("nai,ik->nak", L, V)
    tensors = np.einsum("nak,kl,nbl->nab", channel_maps, Gamma, channel_maps)
    tensors = 0.5 * (tensors + np.swapaxes(tensors, 1, 2))
    return {"tangent_tensors": tensors, "channel_maps": channel_maps,
            "triplett_gram": Gamma}


def reconstruct_rgs_t2u_triplet(source_points, target_eigenvalue=-0.06994933008401777,
                                eigenvalue_tolerance=1e-8, rank_tolerance=1e-8):
    """Reconstruct the first Coulomb T2u triplet from the archived 64-site geometry.

    The 48 signed permutation matrices give O_h. The T2u character is obtained
    as odd inversion parity times the T2g character on (xy,yz,zx). The resulting
    character projector selects the 30-dimensional T2u isotypic component.
    The constrained Coulomb Hessian is then diagonalised only in that component.
    A deterministic coordinate-pivoted frame is extracted from the first
    three-dimensional spectral projector; the frame is reproducible for the
    fixed site ordering, while its physical alignment with PRISM channel labels
    remains a separate gauge-identification question.
    """
    from itertools import permutations, product
    from scipy.linalg import null_space, eigh

    X = np.asarray(source_points, dtype=float)
    if X.shape != (64, 3) or not np.all(np.isfinite(X)):
        raise ValueError("source_points must be a finite 64x3 array")

    # Exact four-constraint tangent space: translations plus fixed scale.
    C = np.zeros((4, 192))
    C[0, 0::3] = 1.0
    C[1, 1::3] = 1.0
    C[2, 2::3] = 1.0
    C[3] = X.reshape(-1)
    Q = null_space(C)
    if Q.shape != (192, 188):
        raise ArithmeticError("the source constraint nullspace is not 192x188")

    def t2g_character(R):
        # T2g is the action on the off-diagonal quadratic channels xy,yz,zx.
        value = 0.0
        for i, j in ((0, 1), (1, 2), (2, 0)):
            ii = int(np.argmax(np.abs(R[:, i])))
            jj = int(np.argmax(np.abs(R[:, j])))
            if {ii, jj} == {i, j}:
                value += R[ii, i] * R[jj, j]
        return float(value)

    projectors = []
    max_site_residual = 0.0
    max_tangent_residual = 0.0
    for perm_axes in permutations(range(3)):
        Paxis = np.zeros((3, 3))
        for i, j in enumerate(perm_axes):
            Paxis[j, i] = 1.0
        for signs in product((-1.0, 1.0), repeat=3):
            G = Paxis @ np.diag(signs)
            parity = int(round(np.linalg.det(G)))
            Rproper = parity * G
            character = parity * t2g_character(Rproper)

            transformed = X @ G.T
            distances = np.linalg.norm(transformed[:, None, :] - X[None, :, :], axis=2)
            site_map = np.argmin(distances, axis=1)
            residual = float(np.max(distances[np.arange(64), site_map]))
            if residual > 1e-8 or len(np.unique(site_map)) != 64:
                raise ArithmeticError("the recovered 64-site geometry is not O_h invariant")
            max_site_residual = max(max_site_residual, residual)

            D = np.zeros((192, 192))
            for source, target in enumerate(site_map):
                D[3*target:3*target+3, 3*source:3*source+3] = G
            Rtan = Q.T @ D @ Q
            max_tangent_residual = max(
                max_tangent_residual,
                float(np.linalg.norm(D @ Q - Q @ Rtan))
            )
            projectors.append((character, Rtan))

    if len(projectors) != 48:
        raise ArithmeticError("the O_h group construction did not produce 48 elements")
    P_T2u = (3.0 / 48.0) * sum(character * R for character, R in projectors)
    P_T2u = 0.5 * (P_T2u + P_T2u.T)
    projector_error = float(np.linalg.norm(P_T2u @ P_T2u - P_T2u))
    pvals, pvecs = eigh(P_T2u)
    selected = pvals > 0.5
    isotypic_rank = int(np.sum(selected))
    if projector_error > 1e-8 or isotypic_rank != 30:
        raise ArithmeticError(
            f"T2u character projector failed: rank={isotypic_rank}, "
            f"idempotence={projector_error:.3e}"
        )
    B_T2u = pvecs[:, selected]

    # Coulomb energy E=sum_{a<b}1/r_ab, its Hessian, and constrained Hessian.
    H = np.zeros((192, 192))
    force = np.zeros((64, 3))
    energy = 0.0
    I3 = np.eye(3)
    for a in range(64):
        for b in range(a + 1, 64):
            d = X[a] - X[b]
            r2 = float(d @ d)
            if r2 <= 0.0:
                raise ValueError(f"coincident source sites {a} and {b}")
            r = np.sqrt(r2)
            energy += 1.0 / r
            f = d / r**3
            force[a] += f
            force[b] -= f
            Hpair = 3.0 * np.outer(d, d) / r**5 - I3 / r**3
            ia, ib = slice(3*a, 3*a+3), slice(3*b, 3*b+3)
            H[ia, ia] += Hpair
            H[ib, ib] += Hpair
            H[ia, ib] -= Hpair
            H[ib, ia] -= Hpair
    H = 0.5 * (H + H.T)
    lambda_force = float(np.sum(force * X) / np.sum(X * X))
    K = Q.T @ (H + lambda_force * np.eye(192)) @ Q
    K = 0.5 * (K + K.T)

    K_projector_commutator = float(np.linalg.norm(K @ P_T2u - P_T2u @ K))
    K_T2u = B_T2u.T @ K @ B_T2u
    K_T2u = 0.5 * (K_T2u + K_T2u.T)
    eigenvalues, eigenvectors = eigh(K_T2u)
    matches = np.flatnonzero(np.abs(eigenvalues - target_eigenvalue) <= eigenvalue_tolerance)
    if len(matches) != 3 or not np.array_equal(matches, np.arange(3)):
        raise ArithmeticError(
            "the lowest T2u cluster is not the expected threefold eigenvalue "
            f"{target_eigenvalue}: first values={eigenvalues[:6].tolist()}"
        )

    Vraw = B_T2u @ eigenvectors[:, matches]
    P_triplet = Vraw @ Vraw.T

    # Deterministic frame from the invariant 3D spectral projector.
    columns = []
    pivots = []
    for j in range(188):
        v = P_triplet[:, j].copy()
        for qv in columns:
            v -= float(qv @ v) * qv
        nv = float(np.linalg.norm(v))
        if nv > rank_tolerance:
            v /= nv
            if v[j] < 0.0:
                v = -v
            columns.append(v)
            pivots.append(j)
        if len(columns) == 3:
            break
    if len(columns) != 3:
        raise ArithmeticError("could not extract a deterministic orthonormal T2u frame")
    V = np.column_stack(columns)
    reduced = V.T @ K @ V
    residual = float(np.linalg.norm(K @ V - V @ reduced))
    orthogonality = float(np.linalg.norm(V.T @ V - np.eye(3)))
    triplet_eigenvalues = np.linalg.eigvalsh(reduced)
    gap = float(eigenvalues[3] - eigenvalues[2])

    diagnostics = {
        "status": "RECONSTRUCTED_AND_NUMERICALLY_VERIFIED",
        "group_order": 48,
        "t2u_isotypic_rank": isotypic_rank,
        "triplet_rank": int(np.linalg.matrix_rank(P_triplet, tol=1e-8)),
        "triplet_pivot_columns": pivots,
        "coulomb_energy": float(energy),
        "lambda_force": lambda_force,
        "triplet_eigenvalues": triplet_eigenvalues.tolist(),
        "target_eigenvalue": float(target_eigenvalue),
        "triplet_eigenvalue_spread": float(np.ptp(triplet_eigenvalues)),
        "gap_to_next_t2u_eigenvalue": gap,
        "projector_idempotence_residual": projector_error,
        "K_T2u_commutator_residual": K_projector_commutator,
        "site_action_residual": max_site_residual,
        "tangent_action_residual": max_tangent_residual,
        "tangent_constraint_residual": float(np.linalg.norm(C @ Q)),
        "tangent_basis_orthogonality": float(np.linalg.norm(Q.T @ Q - np.eye(188))),
        "triplet_orthogonality_residual": orthogonality,
        "triplet_eigen_residual": residual,
        "basis_convention": (
            "deterministic coordinate-pivoted frame extracted from the first "
            "triplet spectral projector; PRISM-channel gauge alignment is not "
            "implied"
        ),
    }
    return {
        "basis": V,
        "triplet_projector": P_triplet,
        "t2u_isotypic_projector": P_T2u,
        "source_tangent_basis": Q,
        "constrained_coulomb_hessian": K,
        "t2u_eigenvalues": eigenvalues,
        "diagnostics": diagnostics,
    }
