# MQM-Q6 Symmetry — exact graph automorphisms and action stabilizer

**Classification:** exact finite combinatorial result plus an exact finite stabilizer algorithm. The fixed-reference symmetry group of MQM-1 is conditional on the 192 reference log-conductances; the repository does not prescribe their numerical values.

## 1. Three symmetry groups must be separated

### 1.1 Ternary hexagram Hamming graph

The full ternary graph has automorphism group
\[
\operatorname{Aut}(H(6,3))=S_3\wr S_6,
\qquad |\operatorname{Aut}|=33,592,320.
\]
This preserves the ternary Hamming adjacency. It is not automatically a symmetry of the binary Q6 incidence matrix or of the RGS embedding.

### 1.2 Canonical binary Q6

The Q6 graph has vertices \(\{0,1\}^6\), with an edge for each one-bit flip. Its automorphism group is
\[
\operatorname{Aut}(Q_6)=S_2\wr S_6
=(C_2)^6\rtimes S_6,
\qquad | \operatorname{Aut}(Q_6)|=2^6 6!=46,080.
\]
The six factors \((C_2)^6\) are bit translations; \(S_6\) permutes the six bit directions. This is the full combinatorial symmetry group of the unweighted Q6 graph and its cubical cell structure.

### 1.3 The actual induced RGS point-cloud subgroup

T113-D constructs the 48 signed-coordinate permutations \(O_h\) on the hash-checked 64-point RGS seed. Repeating that construction without changing its label order gives:
- 48 induced permutations of the 64 sites;
- 16 preserve the canonical Q6 adjacency;
- 32 fail to preserve it.

The 16 survivors are exactly the signed coordinate permutations preserving the first coordinate axis as a set. Their matrices have block form
\[
G=\begin{pmatrix}
\epsilon&0&0\\
0&&\\
0&&R
\end{pmatrix},
\quad \epsilon\in C_2,\quad R\in C_2\wr S_2.
\]
Thus the induced subgroup is
\[
\boxed{C_2\times (C_2\wr S_2)
\cong C_2\times \operatorname{Dih}(4)}
\]
of order \(2\cdot(2^2\cdot2!)=16\), where \(\operatorname{Dih}(4)\) denotes the order-eight symmetry group of a square. This is a subgroup of \(\operatorname{Aut}(Q_6)\), not the whole group. The statement is about the particular hash-checked RGS seed and its established label-to-Q6 identification.

## 2. Exact symmetry covariance of MQM-1

MQM-1 uses an oriented incidence matrix \(B\in\mathbb R^{64\times192}\), real log-conductances \(x\), positive edge weights \(w_e=e^{x_e}\), a normalized state \(\psi\in\mathbb C^{64}\), and
\[
H(x)=\gamma B\operatorname{diag}(e^x)B^T,
\qquad
E(x,\psi)=\frac{\kappa}{2}\|x-x_*\|^2+
\langle\psi,H(x)\psi\rangle.
\]
Let \(p\in\operatorname{Aut}(Q_6)\) be a vertex permutation and \(\rho_p\) its induced permutation of the 192 unoriented edges. Orientation may change under \(p\), but this only multiplies individual incidence columns by signs; those signs cancel in \(B\operatorname{diag}(e^x)B^T\).

Define
\[
(P_p\psi)_{p(v)}=\psi_v,
\qquad
(\rho_p x)_{\rho_p(e)}=x_e.
\]
Then
\[
H(\rho_p x)=P_p H(x)P_p^T.
\]
The quantum term is covariant:
\[
\langle P_p\psi,H(\rho_p x)P_p\psi\rangle
=\langle\psi,H(x)\psi\rangle.
\]
The geometry penalty is invariant exactly when
\[
\rho_p x_*=x_*.
\]
Consequently the fixed-parameter symmetry group of the MQM-1 energy and its coupled equations is
\[
\boxed{G_{\rm MQM}(x_*)=
\operatorname{Stab}_{\operatorname{Aut}(Q_6)}(x_*)}.
\]
Because MQM-1 uses scalar stiffness, scalar mobility and scalar coupling, these coefficients introduce no additional symmetry breaking. If the reference edge vector is generic, the stabilizer is trivial. If it is uniform, the full group of order 46,080 survives. This dependence cannot be collapsed to one numerical group until \(x_*\) is specified.

## 3. Useful exact cases

1. **Uniform reference:** \(x_{*,e}=c\) for all edges. Then \(G_{\rm MQM}=S_2\wr S_6\), order 46,080.
2. **Direction-only reference:** \(x_{*,e}=c_i\) for edges in bit direction \(i\). If all six \(c_i\) are distinct, the stabilizer is the translation subgroup \((C_2)^6\), order 64. If directions have equal coefficients in blocks of sizes \(m_1,\ldots,m_r\), the stabilizer is \((C_2)^6\rtimes(S_{m_1}\times\cdots\times S_{m_r})\).
3. **Generic edgewise reference:** if all 192 edge values are distinct, any stabilizing graph automorphism must fix every edge; since Q6 is connected, it fixes every vertex, so the stabilizer is the identity.

If one additionally requires the symmetry to preserve the actual RGS point-cloud embedding, intersect these groups with the order-16 subgroup from Section 1.3. In particular, for uniform \(x_*\), the combined Q6+RGS symmetry is order 16, not 46,080 and not 48.

## 4. What the result says about EQC gates

- The full ternary symbol-relabeling group is a symmetry of the abstract ternary Hamming graph.
- Only the binary-preserving subgroup acts on the chosen Q6 subgraph.
- The Q6 incidence Hamiltonian is covariant under \(S_2\wr S_6\), with edge conductances permuted along with the graph.
- A fixed MQM-1 reference configuration reduces this to its edge-colouring stabilizer.
- The actual RGS embedding further reduces the point-cloud symmetry to the 16-element subgroup above.

Therefore an EQC instruction is a native symmetry of the coupled MQM model only if it belongs to the appropriate stabilizer. A gate that merely preserves ternary Hamming adjacency is insufficient. A gate that permutes Q6 edges but does not preserve \(x_*\) maps one MQM-1 parameter choice to another rather than leaving the same model invariant.

## 5. Reproducibility

The companion audit uses only Python's standard library. It reconstructs the exact 64-site RGS seed from the same orbit constants and sign ordering as T113-D, enumerates all 48 signed-coordinate permutations, and checks the 16/32 adjacency split. It also enumerates Q6 graph automorphisms to compute the fixed-reference stabilizer for test colourings.

Run:
    python -m unittest tests.test_q6_mqm_symmetry -v

The tests check:
- 64 vertices and 192 edges;
- the exact order 46,080 of \(\operatorname{Aut}(Q_6)\);
- edge-permutation covariance for a nontrivial cube automorphism;
- full stabilizer 46,080 for uniform \(x_*\);
- stabilizer 64 for six distinct direction-dependent reference values;
- the T113-D split 16/32 and the order-16 block subgroup.

## 6. Evidence boundary

**Proved combinatorially:** the full automorphism group of the six-cube; covariance of the weighted incidence Hamiltonian under simultaneous vertex/edge permutation; the fixed-reference stabilizer characterization.

**Reproduced finite computation:** the 48-to-16 induced RGS/Q6 symmetry reduction using the repository's canonical seed.

**Not determined:** the actual symmetry group for a physical MQM-1 instance, because its reference vector \(x_*\) has no prescribed numerical calibration; the symmetry of a future non-scalar constitutive tensor or nonuniform mobility; a physical interpretation of any of these transformations. No quantum speedup is inferred.
