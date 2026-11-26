# Relazione per il colloquio — Geometria del pallone, anisotropia RGS–PRISM e convergenza

**Destinatario:** prof. Morandotti
**Oggetto:** raccordo tra la geometria dell'icosaedro troncato e i dati discreti RGS–PRISM; deformazioni strutturate e convergenza variazionale
**Premessa metodologica:** in tutto il documento si distingue rigorosamente tra *risultato numerico* (verificato su matrici specifiche, con controlli di tolleranza), *costruzione candidata* (definizione da studiare) e *obiettivo aperto* (da dimostrare). Nessun obiettivo è presentato come teorema.

---

## 1. Il pallone come complesso geometrico

Il punto di partenza è l'**icosaedro troncato di Archimede**, il modello geometrico esatto associato alla struttura classica del pallone. La sua combinatoria è esatta:

- **60 vertici, 90 spigoli, 32 facce** (12 pentagoni, 20 esagoni);
- valenza 3 in ogni vertice;
- caratteristica di Eulero: 60 − 90 + 32 = 2;
- simmetria icosaedrica, il gruppo di 60 rotazioni.

**Precisazione importante.** Nel modello di Archimede le facce sono regolari: il pentagono regolare è caratterizzato dal rapporto aureo φ = (1+√5)/2, l'esagono regolare dalla struttura triangolare del piano e dagli angoli di 60° (fattore √3). Nel **C₆₀ fisico**, però, i due tipi di legame hanno lunghezze diverse (circa 1,40 e 1,45 Å): le facce **non** sono regolari. In tutto il documento «icosaedro troncato» indica sempre il modello geometrico esatto, non la molecola rilassata.

**Curvatura: come dirla correttamente.** La curvatura non è «concentrata sui pentagoni»: nel modello geometrico è distribuita in modo uniforme sui **60 vertici** (12° per vertice). Un anello attorno a un esagono racchiude 6 vertici e misura **72°**, non zero. Ciò che distingue il pentagono è l'**angolo di Frank** — il confronto con il reticolo esagonale piano (60°) — non una curvatura locale. Dodici difetti pentagonali, distribuiti con la simmetria dell'icosaedro, sommano la curvatura necessaria a chiudere la superficie: è il teorema di Gauss–Bonnet in forma discreta. Vanno tenuti distinti due piani: la **curvatura intrinseca** della superficie e la **geometria della molecola fisica**.

**Non-identificazione.** Il pallone ha 60 vertici; la struttura RGS–PRISM ha 64 stati, 192 connessioni, 240 facce e uno spazio tangente di dimensione 188. Non vanno identificate: il raccordo proposto è strutturale e geometrico, non un'identificazione di grafi.

## 2. I dati RGS–PRISM

Sul modello discreto esistente è stata ricostruita una decomposizione numerica:

- spazio tangente di dimensione **188 = 94 × 2**;
- verifica numerica di 94 coppie di piani ortogonali: QᵀQ ≃ I₁₈₈ e QᵀDQ ≃ ⊕ⱼ ωⱼ² I₂;
- settore **T₂u**: autovalore λ ≃ −0,069949330084 con degenerazione ~10⁻¹⁵;
- matrice locale Uᵢ = (QV)ᵢ ∈ ℝ³ˣ³ con **rank(Uᵢ) = 2 in tutti i 64 siti**;
- correlazione numerica corr(Tr(Sⱼ)/ωⱼ², ωⱼ) ≃ **−0,670439**.

Tutti questi sono **risultati numerici** sulla matrice analizzata: non dimostrano ancora che la struttura sia la discretizzazione di una geometria continua, e la loro stabilità rispetto alle scelte di base è da verificare.

## 3. Il ponte matematico: due cerchi, due triangoli

La costruzione «T-1916/T-1918» fornisce la struttura generatrice. Due cerchi di raggio r con centri a distanza r generano due triangoli equilateri di orientazione opposta, con:

- intersezioni P± = M ± (√3 r / 2) u⊥;
- baricentri B± = M ± (r / 2√3) u⊥, con B₊ − B₋ = (r/√3) u⊥ e punto medio coincidente con M.

La dualità associata è:

- **triangolo positivo → gradiente**: ⟨∇g⟩_T = (1/A_T) ∮_∂T g⊗n ds (identità esatta della divergenza);
- **triangolo negativo → baricentro e covarianza**: ∫_T q ≈ A_T q(c_T) + (A_T/2) D²q(c_T):Σ_T + R_T.

**Convenzione sul segno dell'errore di quadratura.** Per q = e^{iθ} con fase lineare θ(x) = θ(c_T) + k·(x−c_T) si ha D²q = −e^{iθ} k⊗k. Pertanto:

- **esatto − quadratura** = −(A_T/2) e^{iθ(c_T)} kᵀΣ_T k;
- la formula con segno **+** vale per **quadratura − esatto**, oppure si legge come **modulo**.

La convenzione va dichiarata: invertire l'ordine di sottrazione cambia il segno dell'intera correzione. In ogni caso, geometria, baricentro, covarianza, gradiente di fase e anisotropia restano in un'unica formula.

La composizione in SE(2), (R₂,b₂)(R₁,b₁) = (R₂R₁, b₂ + R₂b₁), e la legge di Burgers b_γ = ∮ D t ds = ∫ Curl D chiudono il quadro: rotazione e traslazione sono derivate dalle stesse leggi, non postulate.

## 4. Trasporti e olonomie

Si esplora l'introduzione di mappe discrete T_fg : E_f → E_g tra gli spazi associati a facce adiacenti, e l'olonomia ℋ = T_{f_{k−1}f_k} ⋯ T_{f₀f₁} attorno a cicli chiusi. **Costruzione eseguita sull'icosaedro troncato** (audit del 21/11): 60 vertici da p_ij = (2u_i+u_j)/3, 32 facce, 90 spigoli; per ogni coppia di facce adiacenti A_fg = B_gᵀ T_fg B_f ∈ SO(2) con T_fg = t tᵀ + m_g m_fᵀ; il campo D_f ∈ SO(2) è propagato lungo un albero del grafo duale. Verifiche: A_fg isometrica e det = 1 a ~10⁻¹⁵, ricorrenza esatta, e **olonomia di 12° attorno a ognuno dei 60 vertici** — somma 720° = 4π, la verifica discreta di Gauss–Bonnet. Il D_f dipende dall'albero (gauge), le olonomie no. **Audit incrociato GH (21/11).** Una costruzione indipendente di terze parti (dati in `~/Immagini/`) è stata confrontata con la nostra: vertici coincidenti esattamente, 32/32 facce, frame di gauge propri. Ricostruendo D_f sullo stesso albero di GH, le matrici coincidono a **1,4·10⁻¹⁵**; le A_fg sugli archi dell'albero a 1,6·10⁻¹⁵; le 60 olonomie a **1,4·10⁻¹⁵** con angolo massimo 12,000000000° ed errore massimo 2,8·10⁻¹⁴ gradi, segni concordi 60/60 — il confronto è sulle matrici, non solo sugli angoli. **La connessione discreta è una replica indipendente verificata.** La rotazione di gauge C = −108° è spiegata: coincide esattamente con la gauge di frame R_{f0} alla radice condivisa (un pentagono), è un artefatto di convenzione e non una legge geometrica. Attenzione però: ‖M_f‖ media vale 1,20 (GH), 1,59 (nostra BFS), 1,87 (nostra DFS) — cambia con la gauge, quindi **non è un invariante** e M_f resta un residuo algebrico, non ancora un disarrangiamento Del Piero–Owen. **Candidata g globale (21/11).** Presa D_f dall'albero, Q_f = B_f D_f B_fᵀ + n_f n_fᵀ ∈ SO(3) è la rotazione di θ_f = arg D_f attorno alla normale (verificato Q_f B_f = B_f D_f); la mappa pezzo per pezzo g_f(x) = Q_f x + t_f ha gradiente per faccia ∇g|_f = B_f D_f = G_f esatto. Le traslazioni t_f sono fissate per minimizzazione LS dei salti sul grafo duale. **Non esiste una g continua**: l'olonomia di 12° per vertice è l'ostruzione, e la g ha salti sugli spigoli — il candidato disarrangiamento DPO (g solo limitata, discontinua su insieme trascurabile). Salti: media 0,745 / max 1,50 (lunghezza spigolo 2/3); spread ai vertici media 0,56; M_f = ∇g − G_f = 0 identità per costruzione — il disarrangiamento è nei JUMP, non nel residuo. I jump dipendono dalla gauge (BFS 0,745 vs DFS 0,755): serve una formulazione gauge-invariante o la gauge che minimizza il salto totale. **Problema variazionale risolto (21/11).** Lasciando libero l'angolo φ_f del gradiente per faccia (∇g|_f = B_f rot φ_f) e minimizzando F = J(salti) + μ·Σ‖M_f‖², il fronte di Pareto è netto: μ→0 dà l'identità (J=0, Σ‖M‖²=53,2), μ→∞ la g che segue la connessione (J→114,5, M→0), transizione netta intorno a μ≈1–3. **Il salto minimo a M=0 è ≈114,5** — la forma quantitativa dell'ostruzione di olonomia; il campo D_f da albero è quasi ottimale (entro 0,06%). Il prezzo della fedeltà alla connessione è ~114 unità di energia di salto (rms ~0,8 per endpoint); permettendo ⟨‖M‖²⟩~50 si compra continuità perfetta. La famiglia g(φ*(μ)) è una deformazione esplicita a un parametro. **Test DPO eseguito (21/11).** Per la g che segue la connessione (M=0 a.e., campo D_BFS): G_fᵀG_f = I₂ a 2,9·10⁻¹⁵ (immersione isometrica, il det classico non si applica alle 3×2), orientazione preservata, ∇g = G dA + S dH¹ con S = misura dei salti sugli spigoli (massa totale 38,9; esagono-esagono 0,478 > penta-esa 0,410). La determining sequence a strip di larghezza h converge in misura: ∫|∇g_h| ≈ 84–86 stabile mentre h→0, limite previsto 84,57 (bulk 45,6 + salti 38,9), errore <1,4%. **Verdetto: candidata ammissibile DPO numericamente** — mancano la prova formale per il caso immersione 2→3, i vertici (stimati O(h)) e la scelta di approssimanti iniettivi. Resta da formalizzare la versione per RGS–PRISM: lì non esiste ancora una definizione canonica dei trasporti.

**Prova formale parziale + vertici + immersi (21/11).** Tre punti aperti del test DPO sono stati affrontati in `prove_dpo_vertex_immersed.py` e documentati in `audits/C60_DPO_FORMAL_PROOF_2026-11-21.md`. **Provato**: g ∈ BV(Σ) con ∇g = G dA + S dH¹ come misura (S = salto sugli spigoli), GᵀG = I₂ a.e., e esistenza della determining sequence: strip di larghezza h attorno agli spigoli + cap di raggio O(h) ai vertici con partition of unity sulle 3 wedge. **Contributo vertici provato O(h)**: |∇C| ≤ C′/R + √2 su area O(R²), verificato numericamente (∫|∇C| = 19,2 / 9,5 / 4,7 per R = 0,15/0,075/0,0375, rapporto ~2 → O(R)). **Immersione locale**: σ_min(∇S) > 0 su tutte le strip (min 8,9·10⁻⁴, margine piccolo — la stima uniforme resta aperta). **Embeddedness globale**: sonda vertice→triangolo sulle immagini delle 32 facce dà distanza minima 1,0·10⁻³ tra facce non adiacenti — supportata, non esaustiva (intersezioni spigolo-spigolo non campionate). **Resta aperto**: la formulazione DPO completa per immersioni 2→3 — il det classico non si applica a matrici 3×2; candidato: ammissibilità formulata su GᵀG e salto, non su det.

**Esempio calcolabile.** Nel modello a facce, il ciclo anulare H₀→H₁→…→H₄→H₀ racchiude 5 vertici. La curvatura concentrata è 12° per vertice (π/15), quindi l'olonomia è **5·π/15 = π/3**. Poiché SO(2) è abeliano, l'angolo non dipende dal punto base; il verso di percorrenza va fissato rispetto alla normale esterna, perché determina il segno.

**Osservazione sull'intrinseco.** La mappa T_fg dipende dall'immersione in ℝ³, ma l'**angolo di olonomia è intrinseco**: dipende solo dagli angoli delle facce, non dalla realizzazione nello spazio.

**Precisazione sul raccordo.** Collegare E_f = n_f^⊥ (dimensione 2 in ℝ³) al rango locale 2 delle U_i è suggestivo — entrambi dicono che la struttura locale è bidimensionale — ma resta un'**analogia**, non un legame: la presentazione esclude l'identificazione con RGS–PRISM (32 facce e 60 vertici contro 64 stati). Va presentata come motivazione.

## 5. Deformazioni strutturate e complessi cellulari

Nel quadro di Del Piero–Owen una configurazione è la coppia (g, G): deformazione macroscopica e gradiente non classico, con M = ∇g − G come misura di incompatibilità. L'ipotesi di lavoro è che le cuciture del pallone — gli spigoli dove pentagoni ed esagoni si incontrano — possano essere luoghi di vincoli, discontinuità o difetti della deformazione, **da verificare e non presupporre**. L'energia ℰ(g,G) = ∫_Ω W(x,∇g,G) dx + ℛ(g,G) è una forma di lavoro: W e ℛ vanno derivate dal modello, non postulare.

Il linguaggio dei **complessi cellulari** (C₂ → C₁ → C₀, ∂₁∂₂ = 0) fornisce la condizione di coerenza topologica necessaria per definire trasporti ed energie in modo non ambiguo. Primo lavoro concreto proposto: costruire il complesso cellulare dell'icosaedro troncato e confrontarlo con RGS–PRISM senza identificazione.

## 6. Convergenza di Mosco

Obiettivo teorico: per una successione di discretizzazioni T_h, h→0, la convergenza di Mosco richiede (i) la condizione di liminf — il limite non perde energia — e (ii) la condizione di recupero — ogni configurazione limite è approssimabile. Insieme danno esistenza, unicità e convergenza dei minimi. Per i raffinamenti curvi servono in più mappe quasi-isometriche con costanti uniformi e stime a priori dimostrate: è un obiettivo, non un risultato.

## 7. Aggiornamento — audit Coulomb Q6 / C60 (21 novembre 2026)

Materiale di riserva, non in scaletta. Verifiche numeriche complete, riproducibili dagli script nel repository `theorem`.

### Modello a 64 stati

- **Simmetrie**: O_h (48 operazioni) induce permutazioni dei 64 punti, ma solo 16 preservano l'adiacenza Q6 (sottogruppo D8×C2). Lo spazio tangente 188D è invariante sotto tutte le 48 (residuo ~1,5·10⁻¹⁵): geometria con simmetria O_h, struttura combinatoria solo con il sottogruppo.
- **Equilibrio Coulomb**: per E_C = Σ_{i<j} 1/‖X_i−X_j‖ si ha ∇E_C + λX ≈ 0 con λ = 3,7375336948 e residuo 4,4·10⁻⁸ — il gradiente è interamente radiale. Q_tangent elimina 3 traslazioni + 1 scala (192−188); i tre modi quasi nulli sono le rotazioni rigide.
- **Equivarianza**: K_C = Q_tangentᵀ(H_C + λI)Q_tangent commuta con O_h, T_h e il sottogruppo Q6 a residui ~1,6·10⁻¹⁵.
- **Spettro di K_C**: 29 modi negativi, 3 quasi nulli, 156 positivi (λ_min = −2,777, λ_max = 15,575): **punto di sella**, non minimo.
- **K_C ≠ K_0**: distanza di Frobenius ~79,6; la provenienza di K_0 resta aperta.

### C60 geometrico (icosaedro troncato)

- Costruzione esatta: 60 vertici da x_{u→v} = (2u+v)/3, 90 legami di lunghezza 2/3, raggio comune 1,6520124394, spazio tangente 176D.
- **Non è un equilibrio Coulombiano**: gradiente tangenziale residuo ≈ 3,12; nessun moltiplicatore di Lagrange viene attribuito.
- Simmetria I_h (120 operazioni) verificata; restrizione a T_h verificata.
- **Confronto settori T_h**: molteplicità coincidenti in 1_g, 1'_g, 1''_g (7, 8, 8); differenze negli altri cinque settori (totale 188 vs 176). Gli spettri normalizzati non coincidono: **decomposizione comune, non identificazione dei modi**.

### Riferimenti

- `scripts/audit_q6_coulomb_oh_th_equivariance.py` → `docs/Q6_COULOMB_OH_TH_EQUIVARIANCE_2026-11-21.md` → `audits/Q6_coulomb_Oh_Th_equivariance_2026-11-21.json`
- `scripts/audit_c60_coulomb_th_comparison.py` → `docs/C60_COULOMB_TH_COMPARISON_2026-11-21.md` → `audits/C60_coulomb_Th_comparison_2026-11-21.json`
- Repository: `github.com/fabianleonaressi95/theorem`

## 8. Le domande per il professore

1. Qual è il modo più rigoroso per descrivere la compatibilità tra facce pentagonali ed esagonali sotto deformazioni non rigide — in particolare, esiste una formulazione intrinseca della curvatura concentrata / dei difetti di disclination?
2. È opportuno introdurre mappe tra carte locali e studiare l'olonomia lungo circuiti chiusi, oppure esiste una formulazione più naturale nelle deformazioni strutturate (distrain, Saint-Venant generalizzato)?
3. Come incorporare un'anisotropia locale in un funzionale variazionale senza introdurre tensori arbitrari?
4. Quale classe di funzionali sulle deformazioni strutturate è adatta a deformazioni, discontinuità e difetti su un complesso poliedrale?
5. Quali ipotesi geometriche e funzionali per la convergenza di Mosco su complessi curvi — quali condizioni di compattezza sono indispensabili?
6. Quale risultato circoscritto sarebbe il primo obiettivo realistico? Preferenza dichiarata: un risultato piccolo ma rigoroso — per esempio il complesso cellulare del pallone con i suoi operatori di bordo, o una stima di compattezza per una classe semplice — piuttosto che un quadro generale senza dimostrazioni.

---

*Documento di accompagnamento alla presentazione `Colloquio_Morandotti_45min.pptx` / `nuova.odp`; le note per lo speaker sono in `notes.py`.*
