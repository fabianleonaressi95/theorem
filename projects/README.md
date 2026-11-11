# Mappa dei filoni di ricerca

Questa directory descrive i progetti e le loro dipendenze; non contiene duplicati dei codici nei repository originari.

1. **RGS–PSU / geometria e gravità** — strutture geometriche, tetradi, torsione, simmetria Lorentz, Anti-Twin.
   - Sottofilone cosmologico: [modello torsione–Lambda dust-like](../models/TORSION_LAMBDA_DUST_CLOSURE.md). È una chiusura FLRW fenomenologica; la derivazione da torsione Einstein–Cartan algebrica è aperta.
2. **PRISM–Krist-All** — grafi prodotto, struttura spettrale, complessi e limiti geometrici.
3. **Q6 / gauge / Wilson / D5** — complesso cubico, flussi interi, legge di Gauss, marginale Wilson, confronto con Bergman–Hua.
4. **Vetri di spin Q6** — modello Edwards–Anderson su Q6; indipendente dal gauge SU(2) finché non è provato un ponte.
5. **Spin geometry / quaternionic bridge** — rappresentazioni, commutanti, strutture spinoriali, connessioni e intertwiners.
6. **QAT / luce topologica** — modello geometrico della luce, OAM e rappresentazioni; ipotesi separate dai dati.
7. **Wyler–Hua** — ricostruzione geometrica e misura; nessun fitting del cutoff.
8. **Fonti non standard** — ricostruzione critica di Legge del Ritmo, etere verticale e *Against the Tide*.

Ogni progetto deve avere una scheda con: obiettivo, oggetti matematici, fonti, teoremi dipendenti, risultati numerici, problemi aperti e collegamenti al repository implementativo.

9. **Q6 ipercubo / Stora–Zumino / Green–Kubo / Green–Schwarz** — sintesi corretta della legge ipercubica e della risposta lineare, polinomio d'anomalia (I_8), discesa BRST in 6D, settore misto gauge-gravitazionale e fattorizzazione tensoriale; il ponte discreto-continuo e l'indice chirale restano esplicitamente aperti. Vedi [nota di sintesi e correzione](Q6-HYPERCUBE-STORA-ZUMINO-GREEN-KUBO.md).

10. **de Rham curvilineo / FEEC / Mosco con scale aurea e superaurea** — sintesi delle identità algebriche di φ e ψ, raffinamenti autosimili alternativi, lemma di scaling FEEC e teorema condizionale di convergenza. Le proiezioni commutanti, la convergenza degli aggiunti, la compattezza discreta e la stabilità armonica restano obblighi aperti. Vedi [sintesi FEEC aurea/superaurea](de_rham_benchmark/docs/GOLDEN_SUPERGOLDEN_FEEC_SYNTHESIS.md) e [audit matematico indipendente](de_rham_benchmark/docs/INDEPENDENT_MATHEMATICAL_AUDIT.md).

11. **Q6 topological synchronization and hysteresis industrial benchmark** — Q6 cubical 2-skeleton, exact chain identities, Anti-Twin lift, NL/NLT topological synchronization and separate Preisach/Prandtl-Ishlinskii/Bouc-Wen constitutive baselines. Industrial validation remains data-dependent. See [project specification](q6_hysteresis_benchmark/README.md) and [T068 audit record](../theorems/T068-q6-cubical-topological-synchronization-audit.md).

12. **Q6 multi-seed/multi-rate hysteresis study** — forward/backward continuation over multiple seeds and dwell times, effective sigma sweep rates, branch-gap/loop-area statistics and NL/NLT plots. See [protocol and reproduction](q6_hysteresis_benchmark/README.md).


13. **Gravitoelectromagnetism / MHD / quantum hydrodynamics / fluxons** — weak-field mass-current effects, magnetic induction and flux freezing, Madelung/Pauli spin-fluid equations, compact phase winding and Josephson fluxons; cross-linked to T047 and T049B–T049D. The Q6/PRISM discrete field equations and any common GEM–Einstein–Cartan action remain open. See [integrated bridge note](../research/GRAVITOMAGNETISM_MHD_QHD_FLUXON_BRIDGE.md).
