# End-to-end RGS rotational triplet / football spectral comparison

This executable closes the first complete spectral bridge using only committed
source geometry and the current shell model. It does **not** relabel the result
as T2u. The RGS 188D Hessian eigenvectors are not present in the repository's
recovered source artifacts, so the triplet tested here is the exactly defined
infinitesimal-rotation subspace.

Let X_i be the 64 recovered sites. The four exact linearised constraints are
three translations and fixed radius. Their Jacobian C is 4x192 and
Q=null_space(C) is 192x188. For Cartesian generators e_a define
G_a(i)=e_a cross X_i. These are tangent to all four constraints. The
orthonormal RGS triplet is the polar factor of Q Q^T G.

The 64-to-92 interpolation W is the local affine directional transfer in
RGS_FOOTBALL_GEOMETRIC_TRANSFER.md. Apply the football node tangent projector,
then compare its three-dimensional range with the three lowest eigenvectors
of Ktan=T^T K T from the unpinned shell stiffness. Report principal angles,
the low-three/next-eigenvalue gap and a normalized stiffness residual.

Quaternionic frames are retained node-by-node by the established SU(2)->SO(3)
lift. This is a geometric rotational-triplet experiment, not proof that the
triplet is symmetry protected. A separate original T2u comparison requires the
original 188D T2u basis/eigenvectors and provenance-aligned Hessian.
