"""Hash-checked reconstruction of the 64-site RGS/O_h seed.

Provenance: A14_RGS_PSU_QLG_JACOBIAN_BUNDLE.zip, SHA-256
80442238349cd6ddc720dabae93d083075dea88decba8acf0a78c3ec03e0abcc.
The reconstructed coordinate array is checked against its canonical
float64 SHA-256 before being returned.
"""
from __future__ import annotations
import hashlib
from itertools import product
from dataclasses import dataclass
import numpy as np

_ORBIT_VALUES = {
    "cube_inner": 0.47863916086470326,
    "small_1": 0.48042984818593559,
    "small_2": 0.48230704367200045,
    "cube_outer": 0.95183963342906408,
    "large_1": 1.5073116806169751,
    "large_2": 1.9039106736116611,
}
EXPECTED_X_SHA256 = "6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf"

@dataclass(frozen=True)
class RGSSeedData:
    coordinates: np.ndarray

def load_rgs_seed_data() -> RGSSeedData:
    v = _ORBIT_VALUES
    reps = [
        (v["cube_inner"], v["cube_inner"], v["cube_inner"]),
        (v["large_1"], v["large_1"], v["small_1"]),
        (v["large_1"], v["small_1"], v["large_1"]),
        (v["small_1"], v["large_1"], v["large_1"]),
        (v["large_2"], v["small_2"], v["small_2"]),
        (v["small_2"], v["large_2"], v["small_2"]),
        (v["small_2"], v["small_2"], v["large_2"]),
        (v["cube_outer"], v["cube_outer"], v["cube_outer"]),
    ]
    signs = tuple(product((-1.0, 1.0), repeat=3))
    x = np.asarray([[s[0]*p[0], s[1]*p[1], s[2]*p[2]]
                    for p in reps for s in signs], dtype=float)
    if x.shape != (64,3):
        raise RuntimeError("recovered RGS seed has wrong shape")
    digest = hashlib.sha256(np.ascontiguousarray(x,dtype="<f8").tobytes()).hexdigest()
    if digest != EXPECTED_X_SHA256:
        raise RuntimeError(f"RGS seed hash mismatch: {digest}")
    return RGSSeedData(coordinates=x)
