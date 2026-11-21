# Trasporti discreti sull'icosaedro troncato — costruzione esplicita

**Data:** 21 novembre 2026
**Script:** `build_truncated_icosahedron_transports.py`
**Dati:** `truncated_icosahedron_transports_2026-11-21.json` / `.npz`

## Costruzione

1. **Geometria**: 12 vertici di icosaedro (coordinate standard con φ) → 60 vertici troncati `p_ij = (2u_i + u_j)/3` per ogni spigolo orientato. Raggio comune 1,6520124394, lunghezza spigolo 2/3 — coincide col modello usato nell'audit Coulomb.
2. **Facce**: 12 pentagoni (uno per vertice icosaedrico, intorno ai vicini ordinati per angolo) + 20 esagoni (uno per faccia icosaedrica). Ogni faccia orientata verso l'esterno (Newell).
3. **Basi**: per ogni faccia, normale unitaria `n_f` e base `B_f = (e1, e2)` con `e1×e2 = n_f`, `e1` tangente al primo spigolo.
4. **Trasporto**: per facce adiacenti `f,g` con spigolo comune di direzione `t`:
   `m_f = n_f × t`, `m_g = n_g × t`, `T_fg = t tᵀ + m_g m_fᵀ`, `A_fg = B_gᵀ T_fg B_f ∈ SO(2)`.
   Indipendente dal segno di `t` (entrambi i `m` cambiano segno).
5. **Campo D_f**: `D_{f0} = I₂`, `D_g = A_fg D_f` lungo un albero ricoprente del grafo duale (32 nodi, 90 archi). Calcolato con alberi BFS e DFS per il test di gauge.

## Verifiche numeriche

| Test | Oggetto | Criterio | Residuo |
|---|---|---|---|
| Isometria | A_fg | AᵀA = I | 1,2·10⁻¹⁵ |
| Orientazione | A_fg | det A = 1 | ~10⁻¹⁵ |
| Inversa | A_gf | A_gf A_fg = I | 1,2·10⁻¹⁵ |
| Ricorrenza | D_f | D_g = A_fg D_f | 0 (esatto) |
| Olonomia vertice | 60 cicli duali | 12° per vertice | 11,99999999999996°–12,00000000000004° |
| Curvatura totale | somma | 4π | 720,0000000000° |
| Gauge | alberi BFS vs DFS | olonomie coincidenti | 2,3·10⁻¹⁵ |

**Risultato chiave**: l'olonomia attorno a *ognuno* dei 60 vertici è esattamente 12° (l'angolo di Frank del difetto), e la somma è 720° = 4π — la verifica discreta del teorema di Gauss–Bonnet. Il campo D_f dipende dall'albero ( gauge ), ma le olonomie dei cicli no: l'oggetto geometrico è l'olonomia, non le singole D_f.

## M_f (stato)

Con `G_f = B_f D_f ∈ ℝ^{3×2}` la dimensione è coerente: `M_f = ∇g|_f − B_f D_f`. Non abbiamo un campo di deformazione g nel modello, quindi il residuo M_f non è calcolabile senza dati aggiuntivi. Come controllo strutturale, con il riferimento piatto `∇g|_f = B_f` si ha `M_f = B_f(I₂ − D_f)` con norma media ≈ 1,59 (max 2,83): il campo D_f non è gauge-triviale, come deve essere su una superficie curva. La candidate resta `M_f = B_f(I₂ − D_f)` per la parte di trasporto; serve il ∇g reale del modello per il residuo fisico.

## Note

- I 32 D_f, le 90 A_fg (180 dirette) e i residui sono in `truncated_icosahedron_transports_2026-11-21.npz`.
- L'angolo di olonomia è intrinseco (dipende solo dagli angoli delle facce), coerente col fatto che A_fg ∈ SO(2) è costruito dalle normali e non dall'immersione.
