# Krist-All recovery status

The recovered source archive was inspected file-by-file. It contains:
- a manuscript on the 64-state coding layer and 69,120-state product space;
- a schematic Merkle/Q-PROOF provenance pipeline;
- figure-generation scripts;
- supplementary PDFs and a recovered Python-notes artifact.

It does not expose the data model required to reproduce the previously cited count of 11,725 Krist-All classes. In particular, the archive lacks:
1. a formal equivalence relation on the objects being classified;
2. a canonical representative encoding;
3. the complete representative/class table or a deterministic enumeration program;
4. the exact definitions and matrices for K and W0;
5. an independent test of K^3=K^2+I and the claimed W0 residual.

Therefore no numerical claim about 11,725 classes, W0≈5.22e-16, or K^3=K^2+I is certified by this recovered package. These are retained as historical research claims pending the original generator and data. This is a provenance limitation, not a proof that the claims are false.


## Additional recovered supplementary notes

A supplementary source artifact, `Recovered_Kristall_related_python_notes.py`, was inspected. It contains code/text notes for a separate 14-site cube–octahedron model (56 real degrees of freedom), including a graph correction and an audit of constraint ranks and spectra. Those notes distinguish the corrected 48-edge graph (12 cube edges, 12 octahedron edges, 24 cross edges) from an earlier erroneous 51-edge graph with three antipodal non-edges. They report rank 52 and a four-dimensional constant-site kernel after the correction, while warning that the previous spectrum changed.

This is useful recovered Krist-All-related computational material, but it is **not** the missing PRISM/Krist-All 11,725-class enumerator. The 14-site model must be documented as a separate finite construction. It does not verify the 11,725 count, W0 residual, or K³=K²+I.
