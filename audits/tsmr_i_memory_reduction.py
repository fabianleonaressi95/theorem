"""Finite Galerkin/Feshbach reduction of the golden Markov compression.

The five-mode matrix is ordered (phi_c, phi_s, 1, psi_c, psi_s).
The constant mode is exactly invariant and is excluded from the memory
subsystem. The retained active block is (phi_c, phi_s); the resolved
complement is the two-mode block (psi_c, psi_s).

This is a 2+2 reduction of the stored 5x5 compression, not an exact
elimination of the infinite-dimensional L2 complement.
"""
import json
from pathlib import Path


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b)))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matadd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def inverse2(a):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if abs(det) < 1e-14:
        raise ValueError("singular 2x2 matrix")
    return [[a[1][1] / det, -a[0][1] / det],
            [-a[1][0] / det, a[0][0] / det]]


def frobenius(a):
    return sum(x * x for row in a for x in row) ** 0.5


def eigenvalues2(a):
    tr = a[0][0] + a[1][1]
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    disc = tr * tr - 4.0 * det
    if disc >= 0.0:
        root = disc ** 0.5
        return [(tr + root) / 2.0, (tr - root) / 2.0]
    root = (-disc) ** 0.5 / 2.0
    return [{"real": tr / 2.0, "imag": root},
            {"real": tr / 2.0, "imag": -root}]


def extract_blocks(matrix):
    # Constant mode (index 2) is invariant and decoupled analytically.
    active = [0, 1]
    harmonic_complement = [3, 4]
    a = [[matrix[i][j] for j in active] for i in active]
    b = [[matrix[i][j] for j in harmonic_complement] for i in active]
    c = [[matrix[i][j] for j in active] for i in harmonic_complement]
    d = [[matrix[i][j] for j in harmonic_complement]
         for i in harmonic_complement]
    return a, b, c, d


def memory_kernel(b, d, c, n):
    dn = eye(2)
    for _ in range(n):
        dn = matmul(dn, d)
    return matmul(matmul(b, dn), c)


def self_energy(b, d, c, z):
    z_minus_d = [[(z if i == j else 0.0) - d[i][j]
                  for j in range(2)] for i in range(2)]
    return matmul(matmul(b, inverse2(z_minus_d)), c)


def audit(matrix=None):
    if matrix is None:
        path = Path(__file__).resolve().parents[1] / "results" / "tsmr_i_golden_markov_blocks.json"
        matrix = json.loads(path.read_text())["operator_matrix"]
    a, b, c, d = extract_blocks(matrix)
    sigma_1 = self_energy(b, d, c, 1.0)
    effective_1 = matadd(a, sigma_1)
    kernels = {str(n): memory_kernel(b, d, c, n) for n in range(6)}
    eig = eigenvalues2(d)
    spectral_radius = max(abs(v) if isinstance(v, (int, float))
                          else (v["real"] ** 2 + v["imag"] ** 2) ** 0.5
                          for v in eig)
    return {
        "retained_active_block_A11": a,
        "active_to_complement_B": b,
        "complement_to_active_C": c,
        "second_harmonic_complement_D": d,
        "D_eigenvalues": eig,
        "D_spectral_radius": spectral_radius,
        "memory_kernels_B_Dn_C": kernels,
        "memory_kernel_norms": {n: frobenius(k) for n, k in kernels.items()},
        "self_energy_at_z_1": sigma_1,
        "self_energy_frobenius_at_z_1": frobenius(sigma_1),
        "effective_active_operator_at_z_1": effective_1,
        "interpretation": (
            "2+2 finite Galerkin/Feshbach reduction; constant mode excluded; "
            "not the exact infinite-dimensional L2 memory kernel"
        ),
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
