# Exact discrete connection-difference identity on Q6

**Classification:** exact finite group identity plus numerical reconstruction audit; continuum contorsion theorem remains open.

## Relative link

The curved and flat spatial connections live on the same oriented Q6 edges. Links map vectors from the source frame \(g\) to target frame \(h\). Define
\[
V_{gh}=U^{\mathrm C}_{gh}(U^{\mathrm W}_{gh})^{-1}.
\]
It is based at the target frame and transforms as
\[
V'_{gh}=G_hV_{gh}G_h^{-1}.
\]
Thus its principal Lie-algebra logarithm
\[
A_{gh}=\operatorname{Log}(V_{gh})\in\mathfrak{so}(3)
\]
is a gauge-covariant edge connection-difference candidate. It obeys the exact link factorization
\[
U^{\mathrm C}_{gh}=\exp(A_{gh})U^{\mathrm W}_{gh}.
\]

## Exact plaquette identity

For a face with ordered links \(U_i\), set \(V_i=U_i^{\mathrm C}(U_i^{\mathrm W})^{-1}\). The curved face holonomy is exactly the ordered product
\[
H_{\mathrm C}=(V_3U^{\mathrm W}_3)(V_2U^{\mathrm W}_2)
(V_1U^{\mathrm W}_1)(V_0U^{\mathrm W}_0).
\]
Equivalently, moving the flat links to the right conjugates each intermediate \(V_i\) by the accumulated flat transport. This is the finite non-Abelian lattice counterpart of comparing curvatures of two connections. It is not yet the differential identity \(R(\omega^{\mathrm C})=R(\omega^{\mathrm W})+D^{\mathrm W}K+K\wedge K\); the latter requires a defined continuum/discrete covariant derivative and compatible interpolation.

## Audit

The script reconstructs the existing curved links and the flat pure-gauge branch on all 192 edges, computes \(V\) and its principal logarithm, and checks link reconstruction and all 240 face factorizations. The branch cut at rotation angle \(\pi\) is explicitly acknowledged.

Run:
\`\`\`bash
python scripts/audit_q6_connection_difference.py
python -m unittest discover -s tests -p "test_q6_connection_difference.py" -v
\`\`\`

**Open:** discrete covariant derivative and contorsion convergence; compatibility of edge coframe definitions under reverse orientation; Lorentzian lift; 4D action and equations; variational selection of the teleparallel branch.
