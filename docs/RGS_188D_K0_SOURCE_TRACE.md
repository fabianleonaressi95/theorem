# RGS 188D — K0 source trace (forensic update)

**Status:** upstream data path identified; exact producer of the archived `K0` remains unresolved.

## 1. Proven data path

The recovered script `A13_RGS_PSU_QLG_TWINE_ANTITWIN.py` loads

```python
F = np.load(fibre_path, allow_pickle=True)
Q = np.asarray(F['Q'], float)
K0 = np.asarray(F['K0'], float)
```

from `RGS_PSU_fiber_connection_audit/psu_fibre_connection_matrices.npz`.

The builder `build_psu_fiber_connection.py` does **not** generate `K0`. It loads the already-existing `RGS_PSU_all_matrices.npz`, extracts `K0`, and writes that same array into `psu_fibre_connection_matrices.npz` alongside the independently constructed fibre-connection data. Its own header and report explicitly say that the connection is built independently of `K0`, and that physical identification with `K0` has not passed.

Therefore the fibre-connection archive is a carrier/copy of `K0`, not its source.

## 2. Notebook evidence: synthetic paths exist, but are not linked to this array

The recovered notebook dump contains at least two distinct synthetic examples:

1. A random Gram-matrix example:
   `K0 = R.T @ R + 0.1 * I`.
2. A function `generate_mock_kernel_188d()`, with a 185D internal block and 3 collective dimensions. The loader `load_or_create_data()` first tries to read `K0_kernel_188.npy`; only if that file is absent does it invoke the mock generator. The same code then constructs `P_G` by selecting eigenvectors of the loaded/generated `K0` with a spectral mask.

These establish that synthetic fallback/test paths were present in the notebook. They do **not** establish that either path produced the archived `/kaggle/working/188D_CHECKPOINT/AUTO_DUMP/K0.npy` or the `K0` stored in `RGS_PSU_all_matrices.npz`.

The notebook dump also contains a separate constrained Coulomb-Hessian calculation,
`K = Q.T @ (H_E + lambda * I) @ Q`, with its own tangent basis. It must not be silently identified with the archived `K0`: the names and arrays are not shown to be identical, and the reported spectral signatures differ.

## 3. Checkpoint provenance

The notebook PDF lists an AUTO_DUMP manifest with a timestamp of 2026-10-02 21:13:54 and an entry for `K0.npy` of shape 188x188, float64. This establishes that a matrix under that variable name was checkpointed. The manifest does not record the producing cell, input hashes, assignment history, or a basis identifier.

## 4. Conclusions

- **Verified:** A13 reads `K0` from the fibre archive.
- **Verified:** the fibre builder copies `K0` from `RGS_PSU_all_matrices.npz`; it does not derive it.
- **Verified:** the notebook includes synthetic random-Gram and mock-kernel paths, including a fallback loader and a spectral-mask projector.
- **Not verified:** either synthetic path generated the exact archived `K0`.
- **Not verified:** the exact generating cell/script, input arrays, and 188D basis metadata for the archived `K0`.
- **Not justified:** identifying the separately computed Coulomb constrained Hessian with this `K0` solely because both are 188D matrices.

Until the producer and basis metadata are recovered, classify `K0` as an **archived PSD matrix of unresolved provenance**, and `P_G` as its **spectral kernel projector**, not as an independently derived geometric projector.
