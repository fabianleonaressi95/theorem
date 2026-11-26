# Audit incrociato: trasporti C60 — costruzione Devin vs dati GH

Data: 2026-11-21
Script: `audit_gh_crosscheck.py`
Output: `audits/C60_TRANSPORTS_GH_CROSSAUDIT_2026-11-21.json`

## Sorgenti confrontate

| | Costruzione Devin | Dati GH |
|---|---|---|
| Script | `build_truncated_icosahedron_transports.py` | (pipeline GH, non in repo) |
| Artefatti | `truncated_icosahedron_transports_2026-11-21.npz/.json` | `~/Immagini/C60_facewise_Df_Gf_Mf.{npz,csv}`, `vertex_holonomies.json`, `report.json`, `D_f.npy`, `G_f.npy`, `M_f.npy`, `grad_g.npy`, `face_*.npy`, `X.npy`, `connection_laplacian.npy` |

## Che cosa è stato effettivamente verificato

- **Geometria:** corrispondenza esatta dei 60 vertici (distanza massima 0.0) e matching delle 32 facce.
- **Frame:** tutte le trasformazioni di confronto `R_f` hanno determinante +1 (fino a 4e-16): preservano l'orientazione.
- **Trasporti:** gli `A_fg` sugli archi dell'albero concordano entro **1.6e-15** dopo il gauge di frame.
- **Ricorrenza:** ricostruendo `D_f` sullo stesso albero di GH (`parent_by_face` da `report.json`), il campo GH si recupera a meno di una rotazione globale, con residuo **1.4e-15**.
- **Olonomie:** le 60 matrici di olonomia concordano — non solo gli angoli — con differenza massima ~1.4e-15; angoli tutti 12.000000000°, errore massimo 2.8e-14 gradi; tracce e determinanti a 2.4e-15; segni concordi 60/60.

Il confronto di matrici, tracce, determinanti e segni è più stringente del solo confronto angolare: esclude matrici diverse con la stessa traccia.

## Il gauge globale: spiegato

La rotazione `C = R(-108°)` **non è una legge geometrica**: è la gauge di frame alla faccia radice condivisa.

Derivazione: se `B'_f = B_f R_f` e `A'_fg = R_gᵀ A_fg R_f`, la propagazione sull'albero dà

```
D'_f = R_fᵀ D_f R_{f0}
```

Quindi `C = R_{f0}` per costruzione. Verifica numerica: la radice GH è la faccia 0 (un **pentagono**), e l'angolo di `R_0` vale esattamente **−108°** — coincide con il `C` fittato. Il fatto che 108° sia l'angolo interno del pentagono è una coincidenza di convenzione: le gauge dei pentagoni assumono solo valori multipli di 36° {−144, −108, −72, 0, 36, 180}, e GH ha selezionato quella radice/frame. Cambiando radice o ruotando il frame radice di α, `C` diventa `R_{f0}` ruotato di conseguenza — comportamento covariante atteso, non un invariante.

## Il risultato negativo su M_f è altrettanto importante

Valori medi di ‖M_f‖:

| Campo | ⟨‖M_f‖⟩ |
|---|---|
| GH | 1.2014 |
| Devin BFS | 1.5882 |
| Devin DFS | 1.8701 |

La norma cambia con la gauge (albero + frame + radice): **non è un invariante della connessione**. Di conseguenza non si può interpretare ‖M_f‖ come densità fisica di disarrangiamento. La coincidenza `max |M_mine − M_GH| = 1.4e-15` riflette il matching esatto delle convenzioni, non un significato fisico.

## Classificazione

| Risultato | Stato |
|---|---|
| Ricostruzione geometria C60 | verificato numericamente |
| Connessione discreta `A_fg` | **replica indipendente verificata** |
| Olonomie locali 12° (matrici, non solo angoli) | **replica indipendente verificata** |
| Curvatura totale 4π | verifica numerica Gauss–Bonnet discreto |
| Gauge globale −108° | spiegato: `C = R_{f0}`, artefatto di convenzione |
| Norma media di `M_f` | dipendente dalla costruzione, non invariante |
| `G_f`, `M_f` come campi | candidati algebrici dipendenti dalla gauge |
| Ammissibilità Del Piero–Owen | **problema aperto** |

**Decisione:** consolidare la connessione e le olonomie come risultato verificato, indipendentemente dalla soluzione del problema DPO. La costruzione di una `g` globale compatibile resta il passo successivo per `G_f`/`M_f`.
